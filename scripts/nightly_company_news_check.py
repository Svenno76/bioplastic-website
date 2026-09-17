#!/usr/bin/env python3
"""
Nightly Company News Checker - HIGH QUALITY VERSION
Iterates all Supabase companies with news_page_url or rss_feed_url,
scrapes their news pages via Firecrawl/Jina, finds new bioplastics articles,
and creates Supabase drafts with change_status='new' for next-day approval.

QUALITY GATES:
1. Non-news filtering (removes nav pages, category pages, legal pages, etc.)
2. 404 checking for all article URLs
3. Deduplication by URL
4. 4-week recency filter
5. Only delivers verified, high-quality news stories
"""

import os
import re
import json
import time
import logging
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List, Dict, Set
from urllib.parse import urlparse
from dotenv import load_dotenv

# Load environment
env_path = Path('/home/jarvis/.hermes/.env')
load_dotenv(env_path)

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_ANON_KEY = os.environ.get('SUPABASE_ANON_KEY')
FIRECRAWL_URL = 'http://localhost:3002'  # Local Firecrawl on VPS

# Setup logging
log_dir = Path('/home/jarvis/.hermes/logs/bioplastics_company_news')
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / f"company_news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Supabase headers
# CRITICAL: Array columns (company, tags) require Prefer: resolution=headers
# Using return=representation causes HTTP 400 with error 22P02
SB_HEADERS = {
    "apikey": SUPABASE_ANON_KEY,
    "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
    "Content-Type": "application/json",
    "Prefer": "resolution=headers"
}

# Hugo content path for slug dedup
HUGO_NEWS_DIR = Path("/tmp/bioplastics-website/content/news")

# ============================================================
# QUALITY FILTERING CONFIGURATION
# ============================================================

# Non-news URL patterns (navigation, category, legal, etc.)
NON_NEWS_URL_PATTERNS = [
    # Navigation/category/tag pages
    r'^https?://[^/]+/news/?$',
    r'^https?://[^/]+/category/',
    r'^https?://[^/]+/tag/',
    r'^https?://[^/]+/page/\d+',
    # Legal/policy pages
    r'privacy\.?policy',
    r'terms\.?(of\.?)?(service|use|conditions)',
    r'cookie\.?policy',
    r'legal',
    r'disclaimer',
    r'accessibility',
    # Contact/about pages
    r'^https?://[^/]+/contact',
    r'^https?://[^/]+/about',
    r'^https?://[^/]+/imprint',
    r'^https?://[^/]+/media\.?contacts?',
    r'^https?://[^/]+/media\.?kit',
    r'^https?://[^/]+/press\.?contacts?',
    # Search/filter pages
    r'search', r'filter', r'sort',
    # Product/category listing pages
    r'/products/search', r'/products/category', r'/industries', r'/solutions',
    # PDF/downloads that aren't press releases
    r'\.pdf$', r'\.docx$',
    # Job/career pages
    r'career', r'job', r'intern',
    # University course pages
    r'study\.html', r'undergrad', r'bschons', r'honours', r'fellows', r'affiliated',
    # Cookie/consent management
    r'cookie', r'consent', r'vendor', r'manage\.?services', r'manage\.?options',
    # Fragment-only URLs
    r'#(editCookieSettings|main-content|cmplz|sidr)',
    # Non-descriptive titles
    r'^(home|news|contact|about|categories|publications|administration|achievements|memoriam|commencement|campus\.?life|in\.?memoriam)$',
    r'^read\.?more', r'^view\.?(media|all|download)', r'^download\.?(press\.?)?release',
    r'^press\.?release$', r'^media\.?(contacts|gallery|kit)$',
    r'^skip\.?(to\.?)?(main|navigation|content)', r'^close\.?menu',
    r'^go\.?to\.?(navigation|content)', r'^back\.?to\.?(investors|home)',
    r'^listen\.?now', r'^more\.?information', r'^graphic\.?q\d',
    r'^spokespersons', r'^sign\.?up', r'^our\.?(global\.?)?organization',
    r'^our\.?(mission|technology|partnerships)', r'^cotiza\.?aqu[ií]',
    r'^cultivating\.?ag\.driven', r'^key\.?takeaways', r'^the\.?story\.?behind',
    r'^data\.?privacy\.?policy', r'^footer\.?navigation',
    r'^profil\.?universit', r'^vizitka\.?rektora', r'^co\.?se\.?deje',
    r'^zero\.?odpad', r'^zarzadzanie', r'^polityka\.?ochrony',
    r'^aktualnosci', r'^powrot\.?do', r'^админ', r'^в мемориам',
    r'^компании', r'^категории', r'^публикации', r'^достижения',
    r'^начало\.?страницы', r'^назад',
]

# Non-news title patterns
NON_NEWS_TITLE_PATTERNS = [
    r'^(home|news|contact|about|categories|publications|administration|achievements|memoriam|commencement|campus.?life|in.?memoriam)$',
    r'^read\.?more', r'^view\.?(media|all|download)', r'^download\.?(press\.?)?release',
    r'^press\.?release$', r'^media\.?(contacts|gallery|kit)$',
    r'^skip\.?(to\.?)?(main|navigation|content)', r'^close\.?menu',
    r'^go\.?to\.?(navigation|content)', r'^back\.?to\.?(investors|home)',
    r'^listen\.?now', r'^more\.?information', r'^graphic\.?q\d',
    r'^spokespersons', r'^sign\.?up', r'^our\.?(global\.?)?organization',
    r'^our\.?(mission|technology|partnerships)', r'^cotiza\.?aqu[ií]',
    r'^cultivating\.?ag\.driven', r'^key\.?takeaways', r'^the\.?story\.?behind',
    r'^data\.?privacy\.?policy', r'^footer\.?navigation',
    r'^profil\.?universit', r'^vizitka\.?rektora', r'^co\.?se\.?deje',
    r'^zero\.?odpad', r'^zarzadzanie', r'^polityka\.?ochrony',
    r'^aktualnosci', r'^powrot\.?do', r'^админ', r'^в мемориам',
    r'^компании', r'^категории', r'^публикации', r'^достижения',
    r'^начало\.?страницы', r'^назад',
    # Language selectors
    r'^(en|de|fr|es|it|pt|nl|pl|cz|ja|zh|ko|ru|ar)$',
    # Very short titles
    r'^[\d\s\-\*\\]+$',
]

# Bioplastics keywords for relevance filtering
BIOPLASTICS_KEYWORDS = {
    'bioplastic', 'bioplastics', 'pla', 'pha', 'pbat', 'pbs', 'pcl', 'bio-pe', 'bio-pet', 'bio-pp',
    'biodegradable', 'compostable', 'bio-based', 'biobased', 'renewable', 'circular economy',
    'chemical recycling', 'mechanical recycling', 'feedstock', 'biopolymer', 'biopolymers',
    'natureworks', 'totalenergies corbion', 'corbion', 'avantium', 'futerro', 'cj biomaterials',
    'danimer scientific', 'novamont', 'basf', 'borealis', 'braskem', 'arkema', 'covestro',
    'lactide', 'lactic acid', 'fdca', 'pef', 'yxy', 'releaf', 'bio-pa', 'bio-pc', 'bio-pu',
    'starch blend', 'cellulose', 'lignin', 'bio-succinic', 'bio-butanediol', 'bio-ethylene',
    'packaging', 'mulch film', 'agricultural film', 'food packaging', 'single-use plastic',
    'ppwr', 'eu taxonomy', 'usda biopreferred', 'ok compost', 'en 13432', 'astm d6400',
    'investment', 'funding', 'series a', 'series b', 'grant', 'partnership', 'collaboration',
    'joint venture', 'acquisition', 'merger', 'plant', 'facility', 'capacity', 'tonnes',
    'scale-up', 'commercial', 'demo plant', 'pilot plant', 'groundbreaking', 'commissioning'
}

# Known companies (multi-word first, longest first)
KNOWN_COMPANIES = [
    'TotalEnergies Corbion', 'CJ Biomaterials', 'Hyosung TNC', 'Lindex and BASF',
    'Technip Energies', 'nova-Institute', 'WinCup',
    'The North Face', 'Goldwin', 'Idemitsu Kosan', 'Toray Industries',
    'UPM', 'Michelman', 'BOBST', 'Lenzing', 'Covestro',
    'Eco-Products', 'Avantium', 'BASF', 'Arkema', 'Cargill', 'Roquette',
    'Kaneka', 'Futerro', 'Stora Enso', 'SABIC',
    'PureCycle', 'Evonik', 'Alterra', 'Neste', 'IMG Group',
    'ECONIC Technologies', 'AMP Polymix', 'Lignin Industries', 'Adsorbi',
    'Yuhan-Kimberly', 'BitByBit', 'Helian Polymers', 'AXENS', 'IFPEN', 'JEPLAN',
    'Corbion', 'Kelpi', 'NatureWorks', 'Novamont',
    'Danimer Scientific', 'Praj Industries', 'Biome Bioplastics', 'Biome',
    'Green Dot Bioplastics', 'NaturePlast', 'FKuR', 'GreenMantra',
    'Genomatica', 'CJ CheilJedang', 'CJ Bio',
    'PureCycle', 'Econic Technologies', 'Evonik', 'Lanxess', 'Borealis', 'Borouge',
    'Sabic', 'Oxo', 'RenewCO2', 'Carbios', 'Loop Industries', 'Ioniqa', 'Glycol',
    'Mura Technology', 'Recycling Technologies', 'Plastic Energy', 'Quantafuel',
    'Brightmark', 'Agilyx', 'Mitsui Chemicals', 'Mitsubishi Chemical', 'Toray',
    'Teijin', 'Asahi Kasei', 'Daicel', 'Kuraray', 'Sumitomo Chemical',
    'Braskem', 'Dow', 'DuPont', 'Eastman', 'ExxonMobil', 'Solvay', 'LyondellBasell',
    # Single-word companies (check last, with word boundaries) - REMOVED "Loop"
    'Carbios', 'Ioniqa', 'Glycol', 'Mura', 'Quantafuel', 'Brightmark', 'Agilyx',
    'Econic', 'Peel', 'Sphere', 'Traceless', 'Sulapac', 'Paptic', 'Woodly',
    'Sulzer', 'Sulzer Chemtech', 'Sulzer Mixpac', 'Sulzer Metco',
]

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')

def extract_slug_from_url(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    return slugify(path.split('/')[-1]) if path else ''

def is_non_news_url(url: str) -> bool:
    """Check if URL matches non-news patterns"""
    url_lower = url.lower()
    for pattern in NON_NEWS_URL_PATTERNS:
        if re.search(pattern, url_lower, re.IGNORECASE):
            return True
    return False

def is_non_news_title(title: str) -> bool:
    """Check if title matches non-news patterns"""
    title_lower = title.lower().strip()
    for pattern in NON_NEWS_TITLE_PATTERNS:
        if re.search(pattern, title_lower, re.IGNORECASE):
            return True
    return False

def check_url_accessible(url: str, timeout: int = 15) -> bool:
    """Check if URL returns 2xx/3xx status (not 404/500)"""
    try:
        req = requests.head(url, timeout=timeout, headers={'User-Agent': 'Mozilla/5.0 (compatible; BPP News Bot)'})
        return req.status_code < 400
    except requests.exceptions.HTTPError as e:
        return e.response.status_code < 400
    except Exception:
        return False  # Treat timeout/connection error as potentially inaccessible

def firecrawl_scrape(url: str) -> Optional[str]:
    try:
        payload = {"url": url, "formats": ["markdown"], "onlyMainContent": True}
        resp = requests.post(f"{FIRECRAWL_URL}/v1/scrape", json=payload, timeout=60)
        if resp.status_code == 200:
            data = resp.json()
            return data.get('data', {}).get('markdown', '')
    except Exception as e:
        logger.warning(f"Firecrawl failed for {url}: {e}")
    return None

def jina_extract(url: str) -> Optional[str]:
    try:
        resp = requests.get(f"https://r.jina.ai/{url}", timeout=30)
        if resp.status_code == 200:
            return resp.text
    except Exception as e:
        logger.warning(f"Jina AI failed for {url}: {e}")
    return None

def fetch_rss_feed(rss_url: str) -> Optional[str]:
    return jina_extract(rss_url)

def extract_links_from_markdown(markdown: str, base_domain: str) -> List[Dict]:
    articles = []
    link_pattern = r'\[([^\]]+)\]\((https?://[^)]+)\)'
    for match in re.finditer(link_pattern, markdown):
        title, url = match.groups()
        parsed = urlparse(url)
        if base_domain in parsed.netloc or any(d in parsed.netloc for d in ['press', 'news', 'blog', 'media']):
            articles.append({'title': title.strip(), 'url': url.strip()})
    return articles

def extract_links_from_rss(rss_content: str) -> List[Dict]:
    articles = []
    item_pattern = r'<item>.*?<title><!\[CDATA\[(.*?)\]\]></title>.*?<link>(.*?)</link>'
    for match in re.finditer(item_pattern, rss_content, re.DOTALL):
        title, url = match.groups()
        articles.append({'title': title.strip(), 'url': url.strip()})
    if not articles:
        title_pattern = r'<title>(.*?)</title>'
        link_pattern = r'<link>(.*?)</link>'
        titles = re.findall(title_pattern, rss_content)
        links = re.findall(link_pattern, rss_content)
        for t, u in zip(titles[1:], links[1:]):
            if 'http' in u:
                articles.append({'title': t.strip(), 'url': u.strip()})
    return articles

def is_relevant_article(title: str, content: str) -> bool:
    text = (title + ' ' + content[:5000]).lower()
    return any(kw in text for kw in BIOPLASTICS_KEYWORDS)

def extract_date_from_text(text: str) -> Optional[datetime]:
    # Pattern 1: YYYY-MM-DD
    match = re.search(r'(\d{4}-\d{2}-\d{2})', text)
    if match:
        try:
            return datetime.strptime(match.group(1), '%Y-%m-%d')
        except ValueError:
            pass
    # Pattern 2: DD.MM.YYYY or DD/MM/YYYY
    match = re.search(r'(\d{2}[./]\d{2}[./]\d{4})', text)
    if match:
        try:
            return datetime.strptime(match.group(1).replace('/', '.'), '%d.%m.%Y')
        except ValueError:
            pass
    # Pattern 3: Month DD, YYYY
    match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}', text)
    if match:
        try:
            return datetime.strptime(match.group(0), '%B %d, %Y')
        except ValueError:
            try:
                return datetime.strptime(match.group(0), '%B %d %Y')
            except ValueError:
                pass
    return None

def get_existing_slugs() -> Set[str]:
    slugs = set()
    for f in HUGO_NEWS_DIR.glob('*.md'):
        if f.name == '_index.md':
            continue
        match = re.match(r'\d{4}-\d{2}-\d{2}-(.+)\.md$', f.name)
        if match:
            slugs.add(match.group(1))
    return slugs

def get_existing_supabase_urls() -> Set[str]:
    urls = set()
    try:
        offset = 0
        while True:
            url = f"{SUPABASE_URL}/rest/v1/news?select=url&limit=1000&offset={offset}"
            req = requests.get(url, headers=SB_HEADERS, timeout=30)
            if req.status_code != 200:
                break
            data = req.json()
            if not data:
                break
            for item in data:
                if item.get('url'):
                    urls.add(item['url'])
            if len(data) < 1000:
                break
            offset += 1000
    except Exception as e:
        logger.warning(f"Failed to fetch existing Supabase URLs: {e}")
    return urls

def identify_companies(text: str) -> List[str]:
    found = []
    text_lower = text.lower()
    for c in KNOWN_COMPANIES:
        c_lower = c.lower()
        if len(c_lower.split()) == 1:
            if re.search(r'\b' + re.escape(c_lower) + r'\b', text_lower):
                found.append(c)
        else:
            if c_lower in text_lower:
                found.append(c)
    seen = set()
    return [x for x in found if not (x in seen or seen.add(x))]

def sb_insert(table: str, data: dict) -> dict:
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    resp = requests.post(url, headers=SB_HEADERS, json=data, timeout=30)
    resp.raise_for_status()
    return resp.json()[0] if resp.json() else {}

# Bioplastics-relevant industries (case-insensitive match)
BIOPLASTICS_INDUSTRIES = {
    'additive producer', 'bioplastic producer', 'bioplastics', 'compounder',
    'research institute', 'technology company', 'university'
}

# Domain allowlist for known bioplastics companies
BIOPLASTICS_DOMAIN_ALLOWLIST = {
    'natureworks.com', 'totalenergiescorbion.com', 'avantium.com', 'futerro.com',
    'corbion.com', 'danimer.com', 'novamont.com', 'basf.com', 'arkema.com',
    'covestro.com', 'borealisgroup.com', 'braskem.com', 'sabic.com',
    'purecycle.com', 'econic.com', 'evonik.com', 'alterra.com', 'neste.com',
    'lanzatech.com', 'gevo.com', 'originmaterials.com', 'cardiacbioplastics.com',
    'biomebioplastics.com', 'natureplast.com', 'fkur.com', 'greenmantra.com',
    'genomatica.com', 'cjbio.net', 'cjcheiljedang.com', 'roquette.com',
    'kaneke.com', 'toyota-tsusho.com', 'mitsubishi-chemical.com', 'toray.com',
    'teijin.com', 'asahi-kasei.com', 'daicel.com', 'kuraray.com',
    'sumitomo-chem.co.jp', 'mitsui-chem.com', 'toyobo.co.jp', 'unitika.co.jp',
    'ecovia.bio', 'rwdc-industries.com', 'lummus.com', 'bioweg.com',
    'ecopha.bio', 'bluepha.com', 'biopolymer.com', 'sulzer.com',
    'packaginginsights.com', 'bioplasticsmagazine.com', 'bioplasticsnews.com',
    'bioplasticsportal.com', 'bioplastics.org', 'european-bioplastics.org',
    'bioplasticseurope.org', 'uspda.gov', 'eu.biopreferred.gov'
}

# Company name keywords for bioplastics relevance (exact word matching)
BIOPLASTICS_COMPANY_KEYWORDS = {
    'bioplastic', 'biopolymer', 'pla', 'pha', 'pbat', 'biodegradable',
    'compostable', 'biobased', 'renewable', 'biotech', 'biotechnology',
    'fermentation', 'enzyme', 'circular', 'recycling',
    'natureworks', 'corbion', 'avantium', 'futerro', 'danimer', 'novamont',
    'purecycle', 'econic', 'gevo', 'origin', 'biome', 'bioplastics',
    'ecovia', 'rwdc', 'bioweg', 'ecopha', 'bluepha', 'sulzer',
    'packaging', 'sustainability', 'circular economy', 'bioeconomy'
}

# Domain denylist for known non-bioplastic companies (false positives)
BIOPLASTICS_DOMAIN_DENYLIST = {
    'agrorenew.org', 'westlake.com', 'wacker.com', 'agilyx.com',
    'plastipak.com', 'lubrizol.com', 'amcor.com', 'berryglobal.com',
    'dupont.com', 'kemvera.com', 'pew.org', 'mercurynews.com',
    'enviplast.com'
}

def is_bioplastic_company(name: str, industry: str, url: str) -> bool:
    """Check if company is likely bioplastics-relevant"""
    name_lower = name.lower()
    url_lower = url.lower()
    
    # Check domain against denylist FIRST
    parsed = urlparse(url)
    domain = parsed.netloc.lower().replace('www.', '')
    if any(d in domain for d in BIOPLASTICS_DOMAIN_DENYLIST):
        return False
    
    # Check domain against allowlist
    if any(d in domain for d in BIOPLASTICS_DOMAIN_ALLOWLIST):
        return True
    
    # Check industry
    if isinstance(industry, list):
        industry_lower = [i.lower() for i in industry]
    elif isinstance(industry, str):
        industry_lower = [industry.lower()]
    else:
        industry_lower = []
    if any(t in BIOPLASTICS_INDUSTRIES for t in industry_lower):
        return True
    
    # Check company name keywords with word boundaries
    import re
    for kw in BIOPLASTICS_COMPANY_KEYWORDS:
        # Use word boundary for multi-word keywords
        if ' ' in kw:
            if re.search(r'\b' + re.escape(kw) + r'\b', name_lower):
                return True
        else:
            # Single word - check as whole word
            if re.search(r'\b' + re.escape(kw) + r'\b', name_lower):
                return True
    
    return False

def fetch_companies_with_news_sources() -> List[Dict]:
    companies = []
    offset = 0
    while True:
        url = f"{SUPABASE_URL}/rest/v1/companies?select=id,name,news_page_url,rss_feed_url,url,industry&news_page_url=not.is.null&limit=1000&offset={offset}"
        req = requests.get(url, headers=SB_HEADERS, timeout=30)
        if req.status_code != 200:
            break
        data = req.json()
        if not data:
            break
        # Filter by bioplastics relevance
        for item in data:
            if is_bioplastic_company(item.get('name', ''), item.get('industry', ''), item.get('url', '')):
                companies.append(item)
        if len(data) < 1000:
            break
        offset += 1000
    # Also fetch companies with rss_feed_url but no news_page_url
    offset = 0
    while True:
        url = f"{SUPABASE_URL}/rest/v1/companies?select=id,name,news_page_url,rss_feed_url,url,industry&rss_feed_url=not.is.null&news_page_url=is.null&limit=1000&offset={offset}"
        req = requests.get(url, headers=SB_HEADERS, timeout=30)
        if req.status_code != 200:
            break
        data = req.json()
        if not data:
            break
        for item in data:
            if is_bioplastic_company(item.get('name', ''), item.get('industry', ''), item.get('url', '')):
                companies.append(item)
        if len(data) < 1000:
            break
        offset += 1000
    return companies

def is_valid_news_article(title: str, url: str) -> bool:
    """Quality filter: check if article is likely real news vs navigation/legal/category page"""
    if not title or not url:
        return False
    if len(title.strip()) < 15:
        return False
    if is_non_news_url(url):
        return False
    if is_non_news_title(title):
        return False
    return True

def process_company(company: Dict, existing_slugs: Set[str], existing_urls: Set[str], cutoff_date: datetime, four_weeks_ago: datetime) -> List[Dict]:
    new_records = []
    company_id = company['id']
    company_name = company['name']
    news_url = company.get('news_page_url')
    rss_url = company.get('rss_feed_url')
    base_domain = urlparse(company['url']).netloc if company.get('url') else ''

    sources_to_check = []
    if news_url:
        sources_to_check.append(('news_page', news_url))
    if rss_url:
        sources_to_check.append(('rss_feed', rss_url))

    for source_type, source_url in sources_to_check:
        logger.info(f"  Checking {source_type}: {source_url}")
        content = None

        if source_type == 'news_page':
            content = firecrawl_scrape(source_url) or jina_extract(source_url)
        else:
            content = fetch_rss_feed(source_url) or jina_extract(source_url)

        if not content:
            logger.warning(f"    Could not fetch content from {source_url}")
            continue

        if source_type == 'rss_feed':
            articles = extract_links_from_rss(content)
        else:
            articles = extract_links_from_markdown(content, base_domain)

        logger.info(f"    Found {len(articles)} article links")

        for article in articles[:30]:  # Limit per source
            article_url = article['url']
            article_title = article['title']

            # Quality filter 1: Basic validation
            if not is_valid_news_article(article_title, article_url):
                logger.debug(f"    Filtered (non-news): {article_title[:60]}")
                continue

            if article_url in existing_urls:
                continue

            slug = extract_slug_from_url(article_url)
            if slug and slug in existing_slugs:
                continue

            # Quality filter 2: Check URL accessibility (404 check)
            logger.info(f"    Checking URL accessibility: {article_url[:60]}...")
            if not check_url_accessible(article_url):
                logger.info(f"    Filtered (404/inaccessible): {article_title[:60]}")
                continue

            article_content = firecrawl_scrape(article_url) or jina_extract(article_url)
            if not article_content:
                continue

            if not is_relevant_article(article_title, article_content):
                logger.debug(f"    Filtered (irrelevant): {article_title[:60]}")
                continue

            pub_date = extract_date_from_text(article_content) or extract_date_from_text(article_title)
            if pub_date and pub_date < cutoff_date:
                logger.debug(f"    Filtered (too old): {article_title[:60]} - {pub_date}")
                continue
            # Also filter if older than 4 weeks
            if pub_date and pub_date < four_weeks_ago:
                logger.debug(f"    Filtered (older than 4 weeks): {article_title[:60]} - {pub_date}")
                continue
            if not pub_date:
                pub_date = datetime.now()

            found_companies = identify_companies(article_title + ' ' + article_content[:3000])
            if not found_companies:
                found_companies = [company_name]

            record = {
                'url': article_url,
                'title': article_title,
                'published_at': pub_date.isoformat() + '+02:00',
                'change_status': 'new',
                'source_name': company_name,
                'source_url': article_url,
                'company': found_companies[:5],
                'category': 'Technology',
                'tags': [],
                'summary': article_title[:200],
                'full_content': article_content[:10000]
            }

            new_records.append(record)
            existing_urls.add(article_url)
            logger.info(f"    ✓ NEW VALID: {article_title[:80]}")

            time.sleep(1)

    return new_records

def send_summary_email(new_records: List[Dict]):
    """Send high-quality formatted email with HTML + plain text versions"""
    try:
        import smtplib
        import ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        env = {}
        with open('/home/jarvis/.hermes/.env') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    env[k.strip()] = v.strip()

        EMAIL_FROM = env.get('EMAIL_ADDRESS', 'sven.cammerer@gmail.com')
        SMTP_SERVER = env.get('EMAIL_SMTP_HOST', 'smtp.gmail.com')
        SMTP_PORT = int(env.get('EMAIL_SMTP_PORT', '587'))
        EMAIL_PASSWORD = env.get('EMAIL_PASSWORD', '')
        EMAIL_TO = 'sven1976@pm.me'

        today = datetime.now().strftime('%Y-%m-%d')
        subject = f"[BPP Company News] {len(new_records)} VERIFIED news articles — {today}"

        # ============================================================
        # HTML EMAIL (rich formatting)
        # ============================================================
        html_lines = [
            "<html><body style='font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, sans-serif; line-height: 1.6; color: #1a1a2e; max-width: 800px; margin: 0 auto; padding: 20px;'>",
            f"<h1 style='color: #1e4d45; border-bottom: 3px solid #52a98c; padding-bottom: 10px;'>📰 BPP Company News — Verified Articles</h1>",
            f"<p style='font-size: 14px; color: #666;'><strong>Date:</strong> {today} | <strong>Articles:</strong> {len(new_records)} verified, deduplicated news items from company sources (last 4 weeks)</p>",
            
            "<div style='background: #f0f9f6; border-left: 4px solid #52a98c; padding: 16px; margin: 20px 0; border-radius: 4px;'>",
            "<h3 style='margin-top: 0; color: #1e4d45;'>✅ Quality Filters Applied</h3>",
            "<ul style='margin: 8px 0; padding-left: 20px;'>",
            "<li><strong>Non-news filtering</strong> — Removed navigation, category, legal, policy, cookie, job, university, language selector pages (60+ regex patterns)</li>",
            "<li><strong>404/accessibility checking</strong> — HEAD request validation for every article URL</li>",
            "<li><strong>Deduplication</strong> — By URL across all sources</li>",
            "<li><strong>4-week recency filter</strong> — Only articles published within last 28 days</li>",
            "<li><strong>Bioplastics relevance</strong> — Keyword filtering on title + content</li>",
            "<li><strong>Title/URL validation</strong> — Minimum 15 chars, non-descriptive title rejection</li>",
            "</ul>",
            "<p style='margin: 8px 0 0 0; font-size: 13px; color: #444;'><em>Original raw scrapes often contain 300+ items — mostly navigation/404s. This email delivers only verified articles.</em></p>",
            "</div>",
            
            "<h2 style='color: #1e4d45;'>📋 Verified News Articles</h2>",
        ]

        for i, item in enumerate(new_records, 1):
            pub = item.get('published_at', '')[:10]
            companies = ', '.join(item.get('company', [])) if item.get('company') else 'N/A'
            title = item.get('title', '').replace('&', '&').replace('<', '<').replace('>', '>')
            url = item.get('url', '')
            src = item.get('source_name', '')
            
            html_lines.append(f"""
            <div style='border: 1px solid #e0e7eb; border-radius: 8px; padding: 16px; margin: 12px 0; background: #fafbfa;'>
                <div style='display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;'>
                    <span style='background: #52a98c; color: white; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: 600; white-space: nowrap;'>
                        #{i}
                    </span>
                    <span style='color: #888; font-size: 13px;'>{pub}</span>
                </div>
                <h3 style='margin: 0 0 8px 0; font-size: 16px; color: #1a1a2e;'>{title}</h3>
                <div style='display: flex; gap: 12px; flex-wrap: wrap; font-size: 13px; color: #555; margin-bottom: 10px;'>
                    <span><strong>Source:</strong> {src}</span>
                    <span><strong>Companies:</strong> {companies}</span>
                </div>
                <a href='{url}' target='_blank' style='display: inline-block; background: #1e4d45; color: white; padding: 8px 16px; border-radius: 6px; text-decoration: none; font-size: 13px; font-weight: 500;'>
                    🔗 Read full article →
                </a>
            </div>
            """)

        html_lines.extend([
            "<hr style='border: none; border-top: 1px solid #e0e7eb; margin: 30px 0;'>",
            "<p style='font-size: 12px; color: #888; text-align: center;'>",
            "Generated by BPP Nightly Company News Checker | ",
            f"<a href='https://bioplasticsportal.com' style='color: #52a98c;'>bioplasticsportal.com</a> | ",
            f"<a href='mailto:sven1976@pm.me' style='color: #52a98c;'>sven1976@pm.me</a>",
            "</p>",
            "</body></html>"
        ])

        html_body = "\n".join(html_lines)

        # ============================================================
        # PLAIN TEXT EMAIL (fallback)
        # ============================================================
        text_lines = [
            f"BPP Company News — Verified Articles — {today}",
            "=" * 60,
            f"Articles: {len(new_records)} verified, deduplicated news items from company sources (last 4 weeks)",
            "",
            "QUALITY FILTERS APPLIED:",
            "  ✓ Non-news filtering — Removed navigation, category, legal, policy, cookie, job, university, language selector pages (60+ regex patterns)",
            "  ✓ 404/accessibility checking — HEAD request validation for every article URL",
            "  ✓ Deduplication — By URL across all sources",
            "  ✓ 4-week recency filter — Only articles published within last 28 days",
            "  ✓ Bioplastics relevance — Keyword filtering on title + content",
            "  ✓ Title/URL validation — Minimum 15 chars, non-descriptive title rejection",
            "",
            "=" * 60,
            "VERIFIED NEWS ARTICLES",
            "=" * 60,
        ]

        for i, item in enumerate(new_records, 1):
            pub = item.get('published_at', '')[:10]
            companies = ', '.join(item.get('company', [])) if item.get('company') else 'N/A'
            title = item.get('title', '')
            url = item.get('url', '')
            src = item.get('source_name', '')
            
            text_lines.extend([
                f"",
                f"{i:3d}. [{pub}] {companies}",
                f"      Source: {src}",
                f"      Title:  {title}",
                f"      URL:    {url}",
            ])

        text_lines.extend([
            "",
            "=" * 60,
            f"bioplasticsportal.com | sven1976@pm.me",
        ])
        text_body = "\n".join(text_lines)

        # ============================================================
        # SEND MULTIPART EMAIL
        # ============================================================
        msg = MIMEMultipart('alternative')
        msg['From'] = env.get('EMAIL_ADDRESS', 'sven.cammerer@gmail.com')
        msg['To'] = 'sven1976@pm.me'
        msg['Subject'] = subject
        msg.attach(MIMEText(text_body, 'plain'))
        msg.attach(MIMEText(html_body, 'html'))

        context = ssl.create_default_context()
        with smtplib.SMTP(env.get('EMAIL_SMTP_HOST', 'smtp.gmail.com'), int(env.get('EMAIL_SMTP_PORT', '587'))) as server:
            server.starttls(context=context)
            server.login(env.get('EMAIL_ADDRESS', 'sven.cammerer@gmail.com'), env.get('EMAIL_PASSWORD', ''))
            server.send_message(msg)
        logger.info(f"High-quality formatted email sent to sven1976@pm.me with {len(new_records)} articles")
    except Exception as e:
        logger.error(f"Failed to send summary email: {e}")

def main():
    logger.info("=" * 60)
    logger.info("Starting Nightly Company News Check - HIGH QUALITY MODE")
    logger.info("=" * 60)

    # Quality config
    RECENCY_DAYS = 7      # Supabase insertion cutoff
    FOUR_WEEKS_DAYS = 28  # Email reporting cutoff
    cutoff_date = datetime.now() - timedelta(days=RECENCY_DAYS)
    four_weeks_ago = datetime.now() - timedelta(days=FOUR_WEEKS_DAYS)
    logger.info(f"Recency cutoff (DB insert): {cutoff_date.strftime('%Y-%m-%d')} (last {RECENCY_DAYS} days)")
    logger.info(f"Recency cutoff (email report): {four_weeks_ago.strftime('%Y-%m-%d')} (last {FOUR_WEEKS_DAYS} days)")

    existing_slugs = get_existing_slugs()
    existing_urls = get_existing_supabase_urls()
    logger.info(f"Existing Hugo slugs: {len(existing_slugs)}")
    logger.info(f"Existing Supabase URLs: {len(existing_urls)}")

    companies = fetch_companies_with_news_sources()
    logger.info(f"Companies with news sources: {len(companies)}")

    all_new_records = []

    for i, company in enumerate(companies):
        logger.info(f"Processing {i+1}/{len(companies)}: {company['name']}")
        try:
            new_records = process_company(company, existing_slugs, existing_urls, cutoff_date, four_weeks_ago)
            all_new_records.extend(new_records)
        except Exception as e:
            logger.error(f"  Error processing {company['name']}: {e}")
        time.sleep(2)

    if all_new_records:
        logger.info(f"Inserting {len(all_new_records)} new records into Supabase...")
        for record in all_new_records:
            try:
                sb_insert('news', record)
                logger.info(f"  Inserted: {record['title'][:60]}")
            except requests.HTTPError as e:
                if e.response.status_code == 409:
                    logger.info(f"  Duplicate URL (409): {record['title'][:60]}")
                else:
                    logger.error(f"  Failed to insert {record['title'][:60]}: {e}")
            except Exception as e:
                logger.error(f"  Failed to insert {record['title'][:60]}: {e}")
    else:
        logger.info("No new articles found after quality filtering")

    send_summary_email(all_new_records)

    logger.info("=" * 60)
    logger.info(f"Company news check complete. New articles: {len(all_new_records)}")
    logger.info("=" * 60)
    return 0


if __name__ == '__main__':
    exit(main())
