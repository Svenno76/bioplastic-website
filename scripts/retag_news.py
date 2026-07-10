#!/usr/bin/env python3
"""Retag all news articles using glossary-only controlled vocabulary."""

import re
from pathlib import Path
import yaml

NEWS_DIR = Path("/tmp/bioplastics-website/content/news")

# Controlled vocabulary from glossary (all valid glossary terms)
VALID_TAGS = {
    # Materials
    "pla", "pha", "pbat", "pbs", "pcl", "phb", "bio-pe", "bio-pet", "bio-pp",
    "starch-based-bioplastic", "cellulose-based", "fdca", "bioplastics",
    "bio-based", "drop-in-bioplastic", "drop-in-replacement",
    # Technologies
    "chemical-recycling", "pyrolysis", "hydrothermal-liquefaction", "depolymerization",
    "enzymatic-recycling", "fermentation", "biorefinery", "thermochemical-liquefaction",
    "mass-balance-approach", "continuous-fermentation", "synthetic-biology",
    "life-cycle-assessment",
    # Properties
    "biodegradable", "compostable", "composting-infrastructure", "en-13432",
    # Circular economy
    "circular-economy", "recycled-content", "ppwr-packaging-waste-regulation",
    "iscc-plus", "extended-producer-responsibility", "carbon-footprint", "biobased-content",
    # Applications
    "packaging", "automotive", "textiles", "agriculture-films", "food-contact",
    "medical-healthcare", "construction", "consumer-goods",
    # Feedstocks
    "feedstock", "sugarcane", "corn", "lignocellulosic-biomass", "used-cooking-oil", "co2-feedstock",
}

# Material tags (at least one required)
MATERIAL_TAGS = {"pla", "pha", "pbat", "pbs", "pcl", "phb", "bio-pe", "bio-pet", "bio-pp",
                 "starch-based-bioplastic", "cellulose-based", "fdca", "bioplastics"}

# Tag mapping from old free-form tags to controlled vocabulary
TAG_MAPPING = {
    # Company names -> remove (use company field)
    # Categories -> remove (use category field)
    "innovation": None,
    "product launch": None,
    "product-launch": None,
    "investment": None,
    "partnership": None,
    "partnerships": None,
    "m&a": None,
    "m&a;": None,
    "regulatory": None,
    "policy": None,
    "certification": None,
    "market analysis": None,
    "technology": None,
    
    # Geographic -> remove
    "china": None, "europe": None, "brazil": None, "usa": None, "us": None,
    "india": None, "japan": None, "germany": None, "france": None, "italy": None,
    "netherlands": None, "uk": None, "canada": None, "south korea": None,
    "thailand": None, "australia": None,
    
    # Generic -> map to specific
    "bioplastics": "bioplastics",
    "biopolymers": "bioplastics",
    "bio-based plastics": "bio-based",
    "biobased": "bio-based",
    "biodegradable plastics": "biodegradable",
    "compostable plastics": "compostable",
    "recycling": "chemical-recycling",  # default, may need context
    "advanced recycling": "chemical-recycling",
    "chemical recycling": "chemical-recycling",
    "mechanical recycling": "mechanical-recycling",
    "circular economy": "circular-economy",
    "circular": "circular-economy",
    "sustainability": "circular-economy",
    "sustainable packaging": "packaging",
    "packaging": "packaging",
    "food packaging": "food-contact",
    "medical": "medical-healthcare",
    "automotive": "automotive",
    "textiles": "textiles",
    "agriculture": "agriculture-films",
    "agricultural films": "agriculture-films",
    "mulch films": "agriculture-films",
    "construction": "construction",
    "consumer goods": "consumer-goods",
    "consumer": "consumer-goods",
    "carbon footprint": "carbon-footprint",
    "lca": "life-cycle-assessment",
    "life cycle assessment": "life-cycle-assessment",
    "ppwr": "ppwr-packaging-waste-regulation",
    "single-use plastics directive": "ppwr-packaging-waste-regulation",
    "supd": "ppwr-packaging-waste-regulation",
    "iscc": "iscc-plus",
    "iscc plus": "iscc-plus",
    "epr": "extended-producer-responsibility",
    "extended producer responsibility": "extended-producer-responsibility",
    "feedstock": "feedstock",
    "sugarcane": "sugarcane",
    "corn": "corn",
    "corn stover": "lignocellulosic-biomass",
    "stover": "lignocellulosic-biomass",
    "bagasse": "sugarcane",
    "used cooking oil": "used-cooking-oil",
    "uco": "used-cooking-oil",
    "co2": "co2-feedstock",
    "carbon capture": "co2-feedstock",
    "ccu": "co2-feedstock",
    "carbon capture and utilization": "co2-feedstock",
    "fermentation": "fermentation",
    "biorefinery": "biorefinery",
    "depolymerization": "depolymerization",
    "enzymatic recycling": "enzymatic-recycling",
    "enzymatic": "enzymatic-recycling",
    "pyrolysis": "pyrolysis",
    "hydrothermal liquefaction": "hydrothermal-liquefaction",
    "htl": "hydrothermal-liquefaction",
    "thermochemical liquefaction": "thermochemical-liquefaction",
    "chemical recycling": "chemical-recycling",
    "mass balance": "mass-balance-approach",
    "mass balance approach": "mass-balance-approach",
    "rpet": "recycled-content",
    "recycled": "recycled-content",
    "recycled content": "recycled-content",
    "bio-pet": "bio-pet",
    "bio-pe": "bio-pe",
    "bio-pp": "bio-pp",
    "biobased": "bio-based",
    "bio-based": "bio-based",
    "drop-in": "drop-in-bioplastic",
    "dropin": "drop-in-bioplastic",
    "biodegradable": "biodegradable",
    "compostable": "compostable",
    "marine biodegradable": "biodegradable",
    "soil biodegradable": "biodegradable",
    "en 13432": "en-13432",
    "astm d6400": "en-13432",
    "ok compost": "compostable",
    "home compostable": "compostable",
    "industrial compostable": "compostable",
    "3d printing": "pla",
    "3d-printing": "pla",
    "filament": "pla",
    "fibers": "textiles",
    "fibre": "textiles",
    "yarn": "textiles",
    "nonwovens": "textiles",
    "wipes": "textiles",
    "hygiene": "textiles",
    "medical devices": "medical-healthcare",
    "implants": "medical-healthcare",
    "sutures": "medical-healthcare",
    "drug delivery": "medical-healthcare",
    "tissue engineering": "medical-healthcare",
    "electronics": "consumer-goods",
    "toys": "consumer-goods",
    "cosmetics": "consumer-goods",
    "personal care": "consumer-goods",
    "household": "consumer-goods",
    "footwear": "consumer-goods",
    "sporting goods": "consumer-goods",
    "luggage": "consumer-goods",
    "pipe": "construction",
    "piping": "construction",
    "insulation": "construction",
    "composite": "construction",
    "3d printed construction": "construction",
    "coatings": "construction",
    "adhesives": "construction",
}

def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    
    fm_str = parts[1]
    body = parts[2]
    
    try:
        fm = yaml.safe_load(fm_str)
        return fm or {}, body
    except yaml.YAMLError as e:
        print(f"YAML error: {e}")
        return {}, content

def serialize_frontmatter(fm):
    """Serialize frontmatter to YAML string."""
    return '---\n' + yaml.dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False) + '---\n'

def map_tags(old_tags):
    """Map old free-form tags to controlled vocabulary."""
    if not old_tags:
        return ["bioplastics"]
    
    if isinstance(old_tags, str):
        old_tags = [old_tags]
    
    new_tags = set()
    
    for tag in old_tags:
        tag_lower = tag.lower().strip()
        
        # Skip empty
        if not tag_lower:
            continue
        
        # Direct mapping
        if tag_lower in TAG_MAPPING:
            mapped = TAG_MAPPING[tag_lower]
            if mapped and mapped in VALID_TAGS:
                new_tags.add(mapped)
            continue
        
        # Check if already a valid tag
        if tag_lower in VALID_TAGS:
            new_tags.add(tag_lower)
            continue
        
        # Try partial matching for compound tags
        for pattern, mapped in TAG_MAPPING.items():
            if pattern in tag_lower and mapped and mapped in VALID_TAGS:
                new_tags.add(mapped)
                break
    
    # Ensure at least one material tag
    has_material = any(t in MATERIAL_TAGS for t in new_tags)
    if not has_material and new_tags:
        # Try to infer from remaining tags
        if "packaging" in new_tags or "food-contact" in new_tags:
            new_tags.add("pbat")  # common for packaging films
        elif "automotive" in new_tags:
            new_tags.add("bio-pp")
        elif "textiles" in new_tags:
            new_tags.add("pla")
        elif "agriculture-films" in new_tags:
            new_tags.add("pbat")
        elif "medical-healthcare" in new_tags:
            new_tags.add("pla")
        elif "construction" in new_tags:
            new_tags.add("pla")
        elif "consumer-goods" in new_tags:
            new_tags.add("pla")
        else:
            new_tags.add("bioplastics")
    
    # Limit to 6 tags max
    return sorted(list(new_tags))[:6]

def process_news_files():
    """Process all news files."""
    news_files = list(NEWS_DIR.glob("*.md"))
    print(f"Found {len(news_files)} news files")
    
    updated = 0
    skipped = 0
    errors = 0
    
    for news_file in news_files:
        try:
            content = news_file.read_text(encoding='utf-8')
            fm, body = parse_frontmatter(content)
            
            if not fm:
                print(f"  WARNING: No frontmatter in {news_file.name}")
                continue
            
            old_tags = fm.get('tags', [])
            new_tags = map_tags(old_tags)
            
            if set(new_tags) != set(old_tags):
                fm['tags'] = new_tags
                new_content = serialize_frontmatter(fm) + body
                news_file.write_text(new_content, encoding='utf-8')
                updated += 1
                if updated % 50 == 0:
                    print(f"  Updated {updated} files...")
            else:
                skipped += 1
                
        except Exception as e:
            print(f"Error processing {news_file.name}: {e}")
            errors += 1
    
    print(f"\nDone! Updated: {updated}, Skipped: {skipped}, Errors: {errors}")

if __name__ == "__main__":
    process_news_files()
