#!/usr/bin/env python3
"""
Create missing glossary terms for the controlled vocabulary tagging system.
Based on GLOSSARY_TAGGING_PROPOSAL.md
"""

import os
from pathlib import Path

GLOSSARY_DIR = Path("/tmp/bioplastics-website/content/glossary")

# Missing glossary terms from the proposal
MISSING_TERMS = {
    "chemical-recycling": {
        "title": "Chemical Recycling",
        "description": "Advanced recycling technologies that break down polymers into monomers or feedstocks through chemical processes (pyrolysis, depolymerization, solvolysis, gasification), enabling infinite recycling loops unlike mechanical recycling.",
        "related_terms": ["mechanical-recycling", "pyrolysis", "depolymerization", "circular-economy", "mass-balance-approach"],
    },
    "pyrolysis": {
        "title": "Pyrolysis",
        "description": "Thermal decomposition of plastics in the absence of oxygen (400-800°C) to produce pyrolysis oil, gas, and char. The oil can be used as feedstock for new plastics production, enabling chemical recycling of mixed or contaminated plastic waste.",
        "related_terms": ["chemical-recycling", "thermochemical-liquefaction", "mass-balance-approach", "circular-economy"],
    },
    "hydrothermal-liquefaction": {
        "title": "Hydrothermal Liquefaction",
        "description": "Thermochemical process converting wet biomass or plastic waste into biocrude oil using water at elevated temperatures (250-400°C) and pressures. Suitable for high-moisture feedstocks without energy-intensive drying.",
        "related_terms": ["thermochemical-liquefaction", "chemical-recycling", "feedstock", "lignocellulosic-biomass"],
    },
    "depolymerization": {
        "title": "Depolymerization",
        "description": "Chemical recycling process that breaks polymers back into their original monomers through solvolysis (glycolysis, methanolysis, hydrolysis) or enzymatic action. Enables true circularity for condensation polymers like PET, PA, and PU.",
        "related_terms": ["chemical-recycling", "enzymatic-recycling", "circular-economy", "bio-pet"],
    },
    "enzymatic-recycling": {
        "title": "Enzymatic Recycling",
        "description": "Biological depolymerization using engineered enzymes (e.g., PETase, MHETase) to break down plastics into monomers under mild conditions. Emerging technology with potential for low-energy, selective recycling of specific polymers.",
        "related_terms": ["depolymerization", "chemical-recycling", "fermentation", "synthetic-biology"],
    },
    "fermentation": {
        "title": "Fermentation",
        "description": "Microbial conversion of sugars or other feedstocks into chemical building blocks (lactic acid for PLA, 1,3-propanediol, succinic acid, PHA). Core bioprocess for producing bio-based monomers and biopolymers at industrial scale.",
        "related_terms": ["pla", "pha", "bio-based-aniline", "continuous-fermentation", "synthetic-biology", "feedstock"],
    },
    "biorefinery": {
        "title": "Biorefinery",
        "description": "Integrated facility converting biomass into multiple products (fuels, chemicals, materials, power) through combined biochemical and thermochemical processes. Maximizes value extraction from feedstocks — analogous to petroleum refineries but using renewable carbon.",
        "related_terms": ["feedstock", "lignocellulosic-biomass", "circular-economy", "bio-based", "fermentation"],
    },
    "recycled-content": {
        "title": "Recycled Content",
        "description": "Proportion of post-consumer or post-industrial recycled material in a product. Key metric for circular economy compliance, mandated by EU PPWR (30% recycled content in plastic packaging by 2030). Verified through chain-of-custody certification (ISCC PLUS, RSB).",
        "related_terms": ["ppwr-packaging-waste-regulation", "iscc-plus", "circular-economy", "mass-balance-approach", "mechanical-recycling"],
    },
    "iscc-plus": {
        "title": "ISCC PLUS",
        "description": "International Sustainability & Carbon Certification PLUS — voluntary certification system for bio-based and circular (recycled) materials using mass balance approach. Enables credible claims for recycled/bio-based content allocation across complex supply chains.",
        "related_terms": ["mass-balance-approach", "recycled-content", "circular-economy", "biobased-content", "carbon-footprint"],
    },
    "extended-producer-responsibility": {
        "title": "Extended Producer Responsibility (EPR)",
        "description": "Policy principle making producers financially/physically responsible for end-of-life management of their products. Drives design for recycling, collection infrastructure, and recycled content incorporation. EU Packaging Directive and national EPR schemes are key implementations.",
        "related_terms": ["ppwr-packaging-waste-regulation", "circular-economy", "recycling-infrastructure", "composting-infrastructure"],
    },
    "carbon-footprint": {
        "title": "Carbon Footprint",
        "description": "Total greenhouse gas emissions caused directly/indirectly by a product, organization, or activity, expressed as CO₂ equivalent. For bioplastics, includes biogenic carbon uptake, land use change, processing emissions, and end-of-life. LCA methodology (ISO 14040/44) required for credible claims.",
        "related_terms": ["life-cycle-assessment", "bio-based", "co2-feedstock", "circular-economy", "mass-balance-approach"],
    },
    "biobased-content": {
        "title": "Bio-based Content",
        "description": "Fraction of carbon in a material derived from biomass vs. fossil sources, measured via ¹⁴C analysis (ASTM D6866 / ISO 16620). Distinct from biodegradability — drop-in bioplastics (Bio-PE, Bio-PET) have high bio-based content but are not biodegradable.",
        "related_terms": ["bio-based", "drop-in-bioplastic", "bio-pe", "bio-pet", "mass-balance-approach", "iscc-plus"],
    },
    "packaging": {
        "title": "Packaging Applications",
        "description": "Largest market segment for bioplastics (~48% of market). Includes rigid packaging (bottles, trays, clamshells), flexible films, food service items, and barrier coatings. Driven by EU PPWR recycled content mandates, SUPD bans, and brand sustainability commitments.",
        "related_terms": ["pla", "pha", "bio-pe", "bio-pet", "pbat", "compostable", "food-contact", "ppwr-packaging-waste-regulation", "single-use-plastics-directive"],
    },
    "automotive": {
        "title": "Automotive Applications",
        "description": "Growing bioplastics segment for interior parts (seat foams, dashboards, door panels), under-hood components, and structural elements. Driven by OEM sustainability targets, recycled content mandates, and weight reduction for EV range. Key materials: Bio-PA, Bio-PP, PLA blends, PHA.",
        "related_terms": ["bio-pp", "bio-pet", "pla", "drop-in-bioplastic", "mass-balance-approach", "carbon-footprint"],
    },
    "textiles": {
        "title": "Textile Applications",
        "description": "Bioplastics in fibers for apparel, nonwovens, technical textiles. PLA fibers (moisture-wicking, UV resistance), PHA (marine-degradable fishing gear), Bio-PET (recyclable polyester). Addresses microplastic pollution and textile waste. Blends with natural fibers common.",
        "related_terms": ["pla", "pha", "bio-pet", "biodegradable", "marine-biodegradable", "microplastics", "circular-economy"],
    },
    "agriculture-films": {
        "title": "Agricultural Films",
        "description": "Mulch films, silage wrap, greenhouse covers, controlled-release fertilizer coatings. Soil-biodegradable films (PBAT/PLA blends, PHA) eliminate retrieval/disposal costs. Certified to EN 17033 (soil biodegradability) or EN 13432 (industrial compostable).",
        "related_terms": ["pbat", "pla", "pha", "biodegradable", "compostable", "soil-biodegradable", "starch-based-bioplastic"],
    },
    "food-contact": {
        "title": "Food Contact Materials",
        "description": "Bioplastics approved for direct food contact (EU 10/2011, FDA 21 CFR). PLA, Bio-PET, Bio-PE, PHBH widely used for packaging, bottles, cutlery. Migration testing required for additives, monomers, oligomers. Barrier properties critical for shelf life.",
        "related_terms": ["pla", "bio-pet", "bio-pe", "pha", "packaging", "compostable", "single-use-plastics-directive"],
    },
    "medical-healthcare": {
        "title": "Medical & Healthcare Applications",
        "description": "Resorbable sutures, implants, drug delivery systems, tissue scaffolds, 3D-printed devices. PLA, PGA, PLGA, PHA, PCL dominate. Biocompatibility and tunable degradation rates are key. FDA/EMA regulatory pathways for absorbable biomaterials well established.",
        "related_terms": ["pla", "pha", "pcl", "biodegradable", "pga", "plga", "synthetic-biology"],
    },
    "construction": {
        "title": "Construction Applications",
        "description": "Insulation foams (PLA-based), piping (Bio-PE), geotextiles (PLA/PHA), concrete additives, 3D-printed building components. Durability requirements differ from packaging — longer service life, weathering resistance. Bio-based content credits in green building certifications (LEED, BREEAM).",
        "related_terms": ["pla", "bio-pe", "bio-pet", "drop-in-bioplastic", "carbon-footprint", "life-cycle-assessment"],
    },
    "consumer-goods": {
        "title": "Consumer Goods",
        "description": "Electronics housings, toys, cosmetics packaging, personal care products, appliances. Brands use bioplastics for sustainability positioning and carbon footprint reduction. Materials must meet performance (durability, aesthetics, processing) and cost targets. Bio-PC, Bio-PA, PLA blends common.",
        "related_terms": ["bio-pc", "bio-pa", "pla", "mass-balance-approach", "carbon-footprint", "drop-in-bioplastic"],
    },
    "sugarcane": {
        "title": "Sugarcane Feedstock",
        "description": "Primary feedstock for Bio-PE (Braskem I'm Green), Bio-PET (via bio-MEG), and PLA (via lactic acid fermentation). High sucrose yield per hectare, established agricultural infrastructure in Brazil/Thailand/India. Bagasse co-product used for process energy. Sustainability concerns: land use, water, labor.",
        "related_terms": ["bio-pe", "bio-pet", "pla", "feedstock", "fermentation", "biobased-content", "mass-balance-approach"],
    },
    "corn": {
        "title": "Corn Feedstock",
        "description": "Primary feedstock for PLA (NatureWorks, Total Corbion) via corn starch → glucose → lactic acid fermentation. High starch yield, established US/China supply chains. Concerns: food vs. fuel competition, fertilizer/pesticide use, land use change. Second-gen feedstocks (corn stover) in development.",
        "related_terms": ["pla", "fermentation", "feedstock", "lignocellulosic-biomass", "biobased-content", "life-cycle-assessment"],
    },
    "lignocellulosic-biomass": {
        "title": "Lignocellulosic Biomass",
        "description": "Non-food biomass (agricultural residues, forestry waste, dedicated energy crops) composed of cellulose, hemicellulose, lignin. Second-generation feedstock for bio-based chemicals/materials. Requires pretreatment (steam explosion, acid/enzymatic hydrolysis) to release fermentable sugars. Key for sustainable scaling beyond food crops.",
        "related_terms": ["feedstock", "biorefinery", "fermentation", "corn", "sugarcane", "used-cooking-oil", "circular-economy"],
    },
    "used-cooking-oil": {
        "title": "Used Cooking Oil (UCO)",
        "description": "Waste lipid feedstock for bio-based chemicals (azelaic acid, sebacic acid → Bio-PA, Bio-PP) and HVO/SAF. Circular feedstock avoiding food competition. ISCC-certified supply chains. Limited volume (~3-4 Mt/yr EU) creates competition with transport fuel mandate.",
        "related_terms": ["feedstock", "bio-pa", "bio-pp", "mass-balance-approach", "iscc-plus", "circular-economy", "hydrothermal-liquefaction"],
    },
    "co2-feedstock": {
        "title": "CO₂ Feedstock",
        "description": "Carbon capture and utilization (CCU) using CO₂ as carbon source for chemicals/materials. Pathways: electrochemical reduction (CO, formate, ethylene), catalytic hydrogenation (methanol, methane), mineralization. Avantium's Volta technology, Covestro's cardyon® (CO₂-based polyols). Enables negative-emission materials when paired with DAC.",
        "related_terms": ["carbon-footprint", "life-cycle-assessment", "mass-balance-approach", "circular-economy", "bio-based-aniline", "synthetic-biology"],
    },
}


def create_glossary_entry(slug, data):
    """Create a glossary markdown file."""
    content = f"""---
title: "{data['title']}"
description: "{data['description'][:150]}..."
---

{data['description']}

## Related Terms

{', '.join(f'[{term.replace("-", " ").title()}](/glossary/{term}/)' for term in data['related_terms'])}

## See Also

- [Glossary Index](/glossary/)
"""
    filepath = GLOSSARY_DIR / f"{slug}.md"
    filepath.write_text(content)
    print(f"Created: {filepath}")


def main():
    print(f"Creating {len(MISSING_TERMS)} missing glossary terms...")
    for slug, data in MISSING_TERMS.items():
        create_glossary_entry(slug, data)
    print("Done!")


if __name__ == "__main__":
    main()
