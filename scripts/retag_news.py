#!/usr/bin/env python3
"""
Retroactive retagging script for Bioplastics Portal news articles.
Maps legacy tags to canonical taxonomy and updates front matter.
"""

import os
import yaml
import re
from pathlib import Path

# Canonical taxonomy from bpp-tagging-taxonomy skill
TAXONOMY_TAGS = {
    # Materials
    "PLA", "PHA", "PBAT", "PBS", "PCL", "Bio-PE", "Bio-PET", "Bio-PP",
    "Starch-Based", "Cellulose-Based", "Lignin-Based", "Protein-Based", "PEF",
    # Feedstock & Production
    "Bio-Based", "Mass Balance", "Drop-In", "Fermentation",
    "Chemical Recycling", "Mechanical Recycling",
    # End-of-Life
    "Compostable", "Biodegradable", "Circular Economy", "Recycling Infrastructure",
    # Technology
    "Synthetic Biology", "Thermochemical Liquefaction", "Life Cycle Assessment",
    # Policy & Market
    "PPWR", "Single-Use Plastics Directive", "Carbon Border Adjustment", "Green Deal",
    "Investment", "Partnership",
    # Applications
    "Packaging", "Textiles", "Automotive", "Agriculture", "Medical",
}

MATERIAL_TAGS = {"PLA", "PHA", "PBAT", "PBS", "PCL", "Bio-PE", "Bio-PET", "Bio-PP",
                 "Starch-Based", "Cellulose-Based", "Lignin-Based", "Protein-Based", "PEF"}

# Alias mapping: legacy tag -> canonical tag (or None to remove)
ALIASES = {
    # Too broad - remove
    "Bioplastics": None,
    "Biopolymers": None,
    "Bio-Based Plastics": "Bio-Based",
    "Sustainable Packaging": None,  # -> Packaging + material tag
    "CircularEconomy": "Circular Economy",
    "circulareconomy": "Circular Economy",
    "Circular Economy": "Circular Economy",
    "ChemicalRecycling": "Chemical Recycling",
    "Chemical Recycling": "Chemical Recycling",
    "chemical-recycling": "Chemical Recycling",
    "Recycling": None,  # -> Chemical OR Mechanical Recycling (context needed)
    "MechanicalRecycling": "Mechanical Recycling",
    "Mechanical Recycling": "Mechanical Recycling",
    "MassBalance": "Mass Balance",
    "Mass Balance": "Mass Balance",
    "Fermentation": "Fermentation",
    "Synthetic Biology": "Synthetic Biology",
    "Investment": "Investment",
    "Partnership": "Partnership",
    "M&A": None,  # category, not tag
    "rPET": "Mechanical Recycling",  # + Bio-PET if bio-based
    "Recycled Plastics": "Mechanical Recycling",
    "Compostable Films": "Compostable",  # + Packaging if relevant
    "Bio-Based Aniline": None,  # Chemical Recycling + Fermentation (new glossary needed)
    "PEF": "PEF",
    "FDCA": "FDCA",
    "Bio-PET": "Bio-PET",
    "Bio-PP": "Bio-PP",
    "Cellulose": "Cellulose-Based",
    "PHB": "PHA",  # PHB is a type of PHA
    "Biopolymer": None,  # remove
    "Bioplastic": None,  # remove
    "Bio-Based Polymers": "Bio-Based",
    "Bio-Based Chemicals": "Bio-Based",
    "Biomass": "Bio-Based",
    "Biodegradable Polymers": "Biodegradable",
    "Advanced Recycling": "Chemical Recycling",
    "Pyrolysis": "Chemical Recycling",
    "Bio-PE": "Bio-PE",
    "Polyurethane": None,  # not in taxonomy - use specific if bio-based
    "Polyurethanes": None,
    "Polyamide": None,
    "Polyesters": None,
    "Biocomposites": None,
    "Biomanufacturing": "Fermentation",
    "Carbon Capture": "Carbon Border Adjustment",
    "Green Deal": "Green Deal",
    "European Commission": "Green Deal",
    "Regulatory Policy": "Green Deal",
    "Sustainability": "Circular Economy",
    "Innovation": None,  # implied
    "Product": None,  # vague
    "Product Launch": None,  # category
    "Plant Announcement": None,  # category
    "Funding": "Investment",
    "Collaboration": "Partnership",
    "M&A": None,
    "Company": None,
    "Technology": "Life Cycle Assessment",  # or specific tech
    "Packaging": "Packaging",
    "Cellulose-Based": "Cellulose-Based",
    "Bio-Based": "Bio-Based",
    "MassBalance": "Mass Balance",
    "chemical-recycling": "Chemical Recycling",
    "circular-economy": "Circular Economy",
    "releaf": "PEF",  # Avantium brand
    "polyethylene furanoate": "PEF",
    "bio-based packaging": "Packaging",
    "functional beverages": "Packaging",
    "Portugal": None,  # location, not tag
    "Netherlands": None,
    "China": None,
    "Korea": None,
    "Italy": None,
    "Spain": None,
    "Germany": None,
    "France": None,
    "UK": None,
    "USA": None,
    "North America": None,
    "Europe": None,
    "EU": None,
    "Investment": "Investment",
    "Partnership": "Partnership",
    "Circular Economy": "Circular Economy",
    "Chemical Recycling": "Chemical Recycling",
    "Mechanical Recycling": "Mechanical Recycling",
    "Life Cycle Assessment": "Life Cycle Assessment",
    "Synthetic Biology": "Synthetic Biology",
    "Fermentation": "Fermentation",
    "Mass Balance": "Mass Balance",
    "Drop-In": "Drop-In",
    "Bio-Based": "Bio-Based",
    "Compostable": "Compostable",
    "Biodegradable": "Biodegradable",
    "Recycling Infrastructure": "Recycling Infrastructure",
    "PPWR": "PPWR",
    "Single-Use Plastics Directive": "Single-Use Plastics Directive",
    "Carbon Border Adjustment": "Carbon Border Adjustment",
    "Green Deal": "Green Deal",
    "Textiles": "Textiles",
    "Automotive": "Automotive",
    "Agriculture": "Agriculture",
    "Medical": "Medical",
    "Packaging": "Packaging",
    "Starch-Based": "Starch-Based",
    "Lignin-Based": "Lignin-Based",
    "Protein-Based": "Protein-Based",
    "PCL": "PCL",
    "PBS": "PBS",
    "PBAT": "PBAT",
    "PLA": "PLA",
    "PHA": "PHA",
    "PEF": "PEF",
    "Bio-PE": "Bio-PE",
    "Bio-PET": "Bio-PET",
    "Bio-PP": "Bio-PP",
}

# Company names that appear in tags (move to company field)
COMPANY_TAGS = {
    "Avantium", "Braskem", "BASF", "CJ Biomaterials", "NatureWorks", "TotalEnergies",
    "Covestro", "SABIC", "Kingfa", "LyondellBasell", "Novamont", "Danimer",
    "Kaneka", "Mitsubishi", "Showa Denko", "Perstorp", "Daicel", "RWDC",
    "Blue Ocean Closures", "Blue Circle Olefins", "AIMPLAS", "NaturePlast",
    "L'Oréal", "Fibenol", "CovationBio", "Futerro", "Borealis", "Radici Group",
    "Teknor Apex", "Gepack", "Frubaça", "Evonik", "Lenzing", "TreeToTextile",
    "H&M Group", "Inter IKEA Group", "MycoWorks", "DFX Corp", "Pulpex",
    "National Wealth Fund", "SWFT Labs", "Stony Brook University", "Cellulose Nanomaterials",
    "Nitro-Oxidation Process", "BePLAYER", "WOOD4PLASTIC", "Hardwood", "Zeus Packaging",
    "Koex Packaging Solutions", "Selenis", "Modern Meadow", "HELLER-LEDER",
    "Innovera Europe", "Dr Bio", "Futerro", "Biorefinery", "Recupero Etico Sostenibile",
    "BIOVOX", "Frankfurt", "Research", "Sugar", "Genetic Engineering", "ANIPH Project",
    "FDCA", "Delfzijl", "Commissioning", "YXY Technology", "Releaf", "Cost Parity",
    "Northeast Forestry University", "Shenyang University of Chemical Technology",
    "Bamboo Bioplastic", "NEXTCHEM", "MAIRE Group", "Maleic Anhydride", "NX Conser",
    "Renaissance BioScience and Biome Bioplastics", "Eastman", "Kolmar Korea",
    "Personal Care Packaging", "Låkril Technologies", "Bio-Acrylic Acid", "Catalysts",
    "Mycelium", "Fine Mycelium", "Reishi", "National Wealth Fund", "SWFT Labs",
    "Stony Brook University", "Cellulose Nanomaterials", "Nitro-Oxidation Process",
    "BePLAYER", "WOOD4PLASTIC", "Hardwood", "Zeus Packaging", "Koex Packaging Solutions",
    "Co-extrusion", "European Bioplastics (EUBP)", "Market Data", "Production Capacity",
    "Ingevity", "Earth Sense Pro", "Flexible Packaging Association", "Bio-Based Films",
    "Westlake", "ACI Compounding Solutions", "Nature Chemistry", "d2w", "Symphony Environmental",
    "IG4 Sol", "Green Polyethylene", "Spain", "LNP LUBRICOMP", "Medical Tubing",
    "Fluoropolymers", "Seaweed Packaging", "Sachets", "B Corp", "Market Launch",
    "UK", "Trevira", "Flame Retardants", "Bionside", "Bio-Based Nylon", "Fakuma 2024",
    "Engineering Plastics", "Automotive", "ETB Global", "Bio-butadiene", "Bio-ethanol",
    "Lactide", "RIKEN Center for Emergent Matter Science", "Fraunhofer UMSICHT",
    "Smart Pyrolysis", "Bloom", "EPFL", "Aldehyde-Assisted Fractionation",
    "The Pew Charitable Trusts", "Prasus", "Italy", "Financial Results", "Bioplastics Profitability",
    "Sojitz", "Bio-Based Feedstocks", "Indiana", "Joint Venture", "North America",
    "Green Polyethylene", "Mono-materials", "Pongamia", "Sway", "Atlantic Packaging",
    "Technip-Energies", "Alterra", "Neste", "Nerea", "Modular-Solution",
    "Selenis", "Recycled Polyester", "Copolyesters", "Modern Meadow", "HELLER-LEDER",
    "Innovera Europe", "Bio-VERA", "Dr Bio", "Cornstarch", "Thermoplastic Starch",
    "TotalEnergies Corbion", "Yuhan-Kimberly", "Washable Wipes", "FKuR", "Gepack",
    "Frubaça", "Releaf", "Polyethylene Furanoate", "Bio-Based Packaging",
    "Functional Beverages", "Portugal", "Röchling Industrial", "Terbrack Kunststoff",
    "Röchling BioConnect", "Engineering Plastics", "Renewable Aromatics", "BTX",
    "Circular Chemistry", "Plastic Waste", "€80M", "National Institute of Forest Science",
    "Low-Energy Catalysis", "Extrusion Coatings", "CEO Appointment", "Korea",
    "CovationsBio", "Precision Plants", "Flinders University", "Casein", "Food Packaging",
    "Futerro", "Biorefinery", "Recupero Etico Sostenibile S.p.A", "Personal Care",
    "Biogenic Carbon", "COP30", "Carbon Neutrality", "Green Materials",
    "Northeast Forestry University and Shenyang University of Chemical Technology",
    "Packamama", "Zhongke Kelan", "CHINAPLAS", "Home Compostable", "Paper Coating",
    "Production Expansion", "Bioplastics Capacity", "Nebraska", "PET Biorecycling",
    "Haining", "Twogee Biotech", "RIKEN Center", "CMCSP", "Nova-Institute",
    "Carbon Capture and Utilisation", "CCU Polymers", "Catalysis", "LyondellBasell",
    "Asset Divestiture", "CirculenRenew", "Ather Energy", "Amplitex", "Flax Fiber",
    "Orinko Advanced Plastics", "Omikron", "Celanese Corporation", "Engineered Materials",
    "Thermoplastics", "Bio-Succinic Acid", "BIOSUCCINIUM", "EcoCortec", "VCI Packaging",
    "Green Biomanufacturing", "Lenzing AG", "TreeToTextile AB", "Textile Fibers",
    "H&M Group", "Inter IKEA Group", "Venture Capital", "Vichem", "Ecopha Biotech and Terra Sol Studio",
}

def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown file."""
    if not content.startswith('---'):
        return {}, content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    try:
        fm = yaml.safe_load(parts[1])
        return fm or {}, parts[2]
    except:
        return {}, content

def dump_frontmatter(fm, body):
    """Serialize frontmatter + body to markdown."""
    yaml_str = yaml.dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False)
    return f"---\n{yaml_str}---\n{body}"

def canonicalize_tag(tag):
    """Map a tag to its canonical form, or None to drop."""
    # Direct match
    if tag in ALIASES:
        return ALIASES[tag]
    # Case-insensitive match
    for k, v in ALIASES.items():
        if k.lower() == tag.lower():
            return v
    # Already canonical
    if tag in TAXONOMY_TAGS:
        return tag
    return None

def process_article(filepath, dry_run=True):
    """Process a single article file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fm, body = parse_frontmatter(content)
    if not fm:
        return None, "No frontmatter"
    
    original_tags = fm.get('tags', [])
    if isinstance(original_tags, str):
        original_tags = [original_tags]
    
    companies = fm.get('company', [])
    if isinstance(companies, str):
        companies = [companies]
    
    # Track changes
    changes = []
    new_tags = []
    new_companies = set(companies)
    
    for tag in original_tags:
        canonical = canonicalize_tag(tag)
        
        if canonical is None:
            # Check if it's a company name
            if tag in COMPANY_TAGS or any(c.lower() in tag.lower() for c in COMPANY_TAGS):
                new_companies.add(tag)
                changes.append(f"  {tag} -> company field")
            else:
                changes.append(f"  {tag} -> DROP (not in taxonomy)")
        elif canonical != tag:
            new_tags.append(canonical)
            changes.append(f"  {tag} -> {canonical}")
        else:
            new_tags.append(canonical)
            changes.append(f"  {tag} -> OK")
    
    # Deduplicate
    new_tags = list(dict.fromkeys(new_tags))
    
    # Ensure at least one material tag
    has_material = any(t in MATERIAL_TAGS for t in new_tags)
    if not has_material and new_tags:
        # Try to infer from content
        body_lower = body.lower()
        if 'pla' in body_lower or 'polylactic' in body_lower:
            new_tags.append('PLA')
            changes.append("  + PLA (inferred from content)")
        elif 'pha' in body_lower or 'polyhydroxyalkanoate' in body_lower:
            new_tags.append('PHA')
            changes.append("  + PHA (inferred from content)")
        elif 'pbat' in body_lower:
            new_tags.append('PBAT')
            changes.append("  + PBAT (inferred from content)")
        elif 'pef' in body_lower or 'polyethylene furanoate' in body_lower or 'releaf' in body_lower:
            new_tags.append('PEF')
            changes.append("  + PEF (inferred from content)")
        elif 'bio-pe' in body_lower or 'bio-pe' in body_lower or 'braskem' in body_lower:
            new_tags.append('Bio-PE')
            changes.append("  + Bio-PE (inferred from content)")
        elif 'bio-pet' in body_lower or 'avantium' in body_lower:
            new_tags.append('Bio-PET')
            changes.append("  + Bio-PET (inferred from content)")
    
    # Limit to 6 tags max
    if len(new_tags) > 6:
        changes.append(f"  WARNING: {len(new_tags)} tags > 6 limit, truncating")
        new_tags = new_tags[:6]
    
    # Update frontmatter
    fm['tags'] = new_tags
    if new_companies != set(companies):
        fm['company'] = sorted(list(new_companies))
    
    new_content = dump_frontmatter(fm, body)
    
    if dry_run:
        return {
            'file': filepath,
            'changes': changes,
            'original_tags': original_tags,
            'new_tags': new_tags,
            'original_companies': companies,
            'new_companies': sorted(list(new_companies)),
            'has_material': has_material,
        }, None
    else:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return {'file': filepath, 'changes': changes}, None

def main():
    news_dir = Path("/tmp/bioplastics-website/content/news")
    files = sorted(news_dir.glob("*.md"))
    
    print(f"Found {len(files)} news articles")
    print(f"Dry run: {True}")
    print()
    
    results = []
    for f in files:
        result, err = process_article(f, dry_run=True)
        if result:
            results.append(result)
        if err:
            print(f"Error in {f.name}: {err}")
    
    # Summary
    total_changes = sum(len(r['changes']) for r in results)
    total_tags_before = sum(len(r['original_tags']) for r in results)
    total_tags_after = sum(len(r['new_tags']) for r in results)
    companies_moved = sum(len(r['new_companies']) - len(r['original_companies']) for r in results)
    missing_material = sum(1 for r in results if not r['has_material'])
    
    print(f"Articles processed: {len(results)}")
    print(f"Total tags before: {total_tags_before}")
    print(f"Total tags after: {total_tags_after}")
    print(f"Tags removed: {total_tags_before - total_tags_after}")
    print(f"Companies moved to company field: {companies_moved}")
    print(f"Articles missing material tag: {missing_material}")
    print()
    
    # Show per-article changes (first 10)
    for r in results[:10]:
        if any('DROP' in c or '->' in c for c in r['changes']):
            print(f"{r['file'].name}:")
            for c in r['changes']:
                print(c)
            print()
    
    # Save detailed report
    import json
    # Convert Path objects to strings
    for r in results:
        r['file'] = str(r['file'])
    with open('/tmp/retag_report.json', 'w') as f:
        json.dump(results, f, indent=2)
    print("Full report saved to /tmp/retag_report.json")

if __name__ == "__main__":
    main()