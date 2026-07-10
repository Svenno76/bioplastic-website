#!/usr/bin/env python3
"""Create missing glossary terms for controlled vocabulary."""

import os
from pathlib import Path

GLOSSARY_DIR = Path("/tmp/bioplastics-website/content/glossary")

MISSING_TERMS = {
    "chemical-recycling": {
        "title": "Chemical Recycling",
        "description": "Advanced recycling technologies that break down polymers into monomers or feedstocks through chemical processes (pyrolysis, depolymerization, solvolysis, gasification), enabling infinite recycling loops unlike mechanical recycling.",
        "aka": ["Advanced Recycling", "Feedstock Recycling", "Molecular Recycling"],
        "term_type": "technology",
        "related": ["mechanical-recycling", "pyrolysis", "depolymerization", "circular-economy", "mass-balance-approach"],
        "summary": "Chemical recycling breaks plastics down to molecular building blocks for virgin-quality recycled materials.",
        "companies": ["Alterra Energy", "Neste", "TotalEnergies", "BASF", "SABIC", "LyondellBasell", "Covestro", "Technip Energies"],
        "applications": ["Mixed plastic waste", "Contaminated plastics", "Multi-layer packaging", "Food-grade recycled content"],
        "standards": ["ISCC PLUS", "RSB", "ISO 15270"],
    },
    "pyrolysis": {
        "title": "Pyrolysis",
        "description": "Thermal decomposition of plastics in the absence of oxygen (400-800°C) to produce pyrolysis oil, gas, and char. The oil can be used as feedstock for new plastics production, enabling chemical recycling of mixed or contaminated plastic waste.",
        "aka": ["Thermal Cracking", "Plastic-to-Oil"],
        "term_type": "technology",
        "related": ["chemical-recycling", "thermochemical-liquefaction", "mass-balance-approach", "circular-economy"],
        "summary": "Pyrolysis converts plastic waste into pyrolysis oil for new plastic production via chemical recycling.",
        "companies": ["Alterra Energy", "Brightmark", "Plastic Energy", "Agilyx", "Nexus Circular", "OMV", "Shell"],
        "applications": ["Polyolefins (PE, PP, PS)", "Mixed plastic waste", "Food-contact recycled content via mass balance"],
        "standards": ["ISCC PLUS", "RSB"],
    },
    "hydrothermal-liquefaction": {
        "title": "Hydrothermal Liquefaction",
        "description": "Thermochemical process converting wet biomass or plastic waste into biocrude oil using water at elevated temperatures (250-400°C) and pressures. Suitable for high-moisture feedstocks without energy-intensive drying.",
        "aka": ["HTL", "Hydrothermal Processing"],
        "term_type": "technology",
        "related": ["thermochemical-liquefaction", "chemical-recycling", "feedstock", "lignocellulosic-biomass"],
        "summary": "HTL uses supercritical water to convert wet waste into biocrude without drying — efficient for algae, sewage sludge, wet biomass.",
        "companies": ["Licella", "Genifuel", "Steeper Energy", "Aarhus University", "PNNL"],
        "applications": ["Wet biomass", "Algae", "Sewage sludge", "Food waste", "Lignocellulosic biomass"],
        "standards": [],
    },
    "depolymerization": {
        "title": "Depolymerization",
        "description": "Chemical recycling process that breaks polymers back into their original monomers through solvolysis (glycolysis, methanolysis, hydrolysis) or enzymatic action. Enables true circularity for condensation polymers like PET, PA, and PU.",
        "aka": ["Molecular Recycling", "Solvolysis", "Chemolysis"],
        "term_type": "technology",
        "related": ["chemical-recycling", "enzymatic-recycling", "circular-economy", "bio-pet"],
        "summary": "Depolymerization reverses polymerization to recover pure monomers for virgin-quality recycled polymers.",
        "companies": ["Carbios", "Loop Industries", "Gramex", "Ioniqa", "Eastman", "Indorama", "JEPLAN", "Jeplan"],
        "applications": ["PET bottles", "Polyester textiles", "Polyamides", "Polyurethanes"],
        "standards": ["ISCC PLUS", "RSB", "FDA Food Contact"],
    },
    "enzymatic-recycling": {
        "title": "Enzymatic Recycling",
        "description": "Biological depolymerization using engineered enzymes (e.g., PETase, MHETase) to break down plastics into monomers under mild conditions. Emerging technology with potential for low-energy, selective recycling of specific polymers.",
        "aka": ["Biological Recycling", "Enzyme-Based Recycling"],
        "term_type": "technology",
        "related": ["depolymerization", "chemical-recycling", "fermentation", "synthetic-biology"],
        "summary": "Engineered enzymes selectively depolymerize target plastics at low temperature and pressure — a bio-based recycling route.",
        "companies": ["Carbios", "Samsara Eco", "Protein Evolution", "AIMPLAS", "University of Portsmouth", "CNRS"],
        "applications": ["PET", "PLA", "Polyurethanes", "Polyamides"],
        "standards": [],
    },
    "fermentation": {
        "title": "Fermentation",
        "description": "Microbial conversion of sugars or other feedstocks into chemical building blocks (lactic acid for PLA, 1,3-propanediol, succinic acid, PHA). Core bioprocess for producing bio-based monomers and biopolymers at industrial scale.",
        "aka": ["Bioprocessing", "Microbial Fermentation", "Biomanufacturing"],
        "term_type": "technology",
        "related": ["pla", "pha", "bio-based-aniline", "continuous-fermentation", "synthetic-biology", "feedstock"],
        "summary": "Industrial fermentation uses microorganisms to convert renewable feedstocks into bio-based monomers and polymers.",
        "companies": ["NatureWorks", "Total Corbion", "Corbion", "Danimer Scientific", "RWDC", "Newlight Technologies", "CJ Biomaterials", "Kaneka"],
        "applications": ["PLA production", "PHA production", "Bio-based chemicals", "Organic acids", "1,3-Propanediol", "Succinic acid"],
        "standards": ["ISO 14855", "ASTM D6400", "EN 13432"],
    },
    "biorefinery": {
        "title": "Biorefinery",
        "description": "Integrated facility converting biomass into multiple products (fuels, chemicals, materials, power) through combined biochemical and thermochemical processes. Maximizes value extraction from feedstocks — analogous to petroleum refineries but using renewable carbon.",
        "aka": ["Integrated Biorefinery", "Bioprocessing Facility"],
        "term_type": "technology",
        "related": ["feedstock", "lignocellulosic-biomass", "circular-economy", "bio-based", "fermentation"],
        "summary": "Biorefineries fractionate biomass into multiple product streams — maximizing value and minimizing waste, like oil refineries but renewable.",
        "companies": ["UPM", "Stora Enso", "Borregaard", "Sekab", "Clariant", "Novozymes", "DSM", "Roquette", "Tereos"],
        "applications": ["Cellulosic ethanol", "Lignin valorization", "Hemicellulose derivatives", "Bio-based chemicals", "Bio-materials", "Biofuels"],
        "standards": ["ISO 13065", "RSB"],
    },
    "recycled-content": {
        "title": "Recycled Content",
        "description": "Proportion of post-consumer or post-industrial recycled material in a product. Key metric for circular economy compliance, mandated by EU PPWR (30% recycled content in plastic packaging by 2030). Verified through chain-of-custody certification (ISCC PLUS, RSB).",
        "aka": ["Post-Consumer Recycled (PCR)", "Recycled Material Content"],
        "term_type": "standard",
        "related": ["ppwr-packaging-waste-regulation", "iscc-plus", "circular-economy", "mass-balance-approach", "mechanical-recycling"],
        "summary": "Recycled content mandates drive demand for recycled plastics — verified by certification to prevent greenwashing.",
        "companies": ["Veolia", "Suez", "Biffa", "Viridor", "ALPLA", "Greiner", "Berry Global", "Amcor", "Sealed Air"],
        "applications": ["Packaging", "Automotive parts", "Construction products", "Textiles", "Electronics"],
        "standards": ["PPWR", "ISCC PLUS", "RSB", "GRS", "RCS", "EN 15343"],
    },
    "iscc-plus": {
        "title": "ISCC PLUS",
        "description": "International Sustainability & Carbon Certification PLUS — voluntary certification system for bio-based and circular (recycled) materials using mass balance approach. Enables credible claims for recycled/bio-based content allocation across complex supply chains.",
        "aka": ["ISCC PLUS Certification", "International Sustainability & Carbon Certification"],
        "term_type": "standard",
        "related": ["mass-balance-approach", "recycled-content", "circular-economy", "biobased-content", "carbon-footprint"],
        "summary": "ISCC PLUS certifies bio-based and circular materials via mass balance — enabling traceable sustainability claims.",
        "companies": ["ISCC System GmbH", "SGS", "Control Union", "DNV", "Bureau Veritas", "TÜV"],
        "applications": ["Chemical recycling mass balance", "Bio-based feedstock tracking", "Sustainable aviation fuel", "Biomass supply chains"],
        "standards": ["ISCC 203", "ISCC PLUS", "RED II compliance"],
    },
    "extended-producer-responsibility": {
        "title": "Extended Producer Responsibility (EPR)",
        "description": "Policy principle making producers financially/physically responsible for end-of-life management of their products. Drives design for recycling, collection infrastructure, and recycled content incorporation. EU Packaging Directive and national EPR schemes are key implementations.",
        "aka": ["EPR", "Producer Responsibility", "Product Stewardship"],
        "term_type": "policy",
        "related": ["ppwr-packaging-waste-regulation", "circular-economy", "recycling-infrastructure", "composting-infrastructure"],
        "summary": "EPR shifts end-of-life costs to producers — incentivizing recyclable design and funding collection/recycling infrastructure.",
        "companies": ["Citeo (FR)", "DSD (DE)", "CONAI (IT)", "Ecoembes (ES)", "Valpak (UK)", "EXPRA", "PRO Europe"],
        "applications": ["Packaging", "WEEE", "Batteries", "Vehicles", "Textiles"],
        "standards": ["EU Packaging Directive 94/62/EC", "WEEE Directive", "Battery Directive", "PPWR"],
    },
    "carbon-footprint": {
        "title": "Carbon Footprint",
        "description": "Total greenhouse gas emissions caused directly/indirectly by a product, organization, or activity, expressed as CO₂ equivalent. For bioplastics, includes biogenic carbon uptake, land use change, processing emissions, and end-of-life. LCA methodology (ISO 14040/44) required for credible claims.",
        "aka": ["Carbon Footprint", "Product Carbon Footprint (PCF)", "GHG Emissions"],
        "term_type": "metric",
        "related": ["life-cycle-assessment", "bio-based", "co2-feedstock", "circular-economy", "mass-balance-approach"],
        "summary": "Carbon footprint quantifies climate impact across full lifecycle — bioplastics can offer 20-70% reduction vs fossil plastics.",
        "companies": ["Quantis", "Sphera", "EcoAct", "South Pole", "Carbon Trust", "SGS", "DNV", "TÜV"],
        "applications": ["Product carbon footprinting", "Scope 3 emissions", "Carbon labeling", "Green claims substantiation", "CBAM compliance"],
        "standards": ["ISO 14040/44 (LCA)", "ISO 14067 (PCF)", "GHG Protocol", "PEF", "ENVISAT"],
    },
    "biobased-content": {
        "title": "Bio-based Content",
        "description": "Fraction of carbon in a material derived from biomass vs. fossil sources, measured via ¹⁴C analysis (ASTM D6866 / ISO 16620). Distinct from biodegradability — drop-in bioplastics (Bio-PE, Bio-PET) have high bio-based content but are not biodegradable.",
        "aka": ["Bio-based Carbon Content", "Biogenic Carbon Content", "Renewable Carbon Content"],
        "term_type": "metric",
        "related": ["bio-based", "drop-in-bioplastic", "bio-pe", "bio-pet", "mass-balance-approach", "iscc-plus"],
        "summary": "Bio-based content measures renewable carbon fraction via radiocarbon dating — not the same as biodegradability.",
        "companies": ["Beta Analytic", "TÜV Austria", "DIN CERTCO", "Vinçotte", "SGS", "Intertek"],
        "applications": ["Bio-based product labeling", "USDA BioPreferred", "Green procurement", "Carbon footprint reduction claims"],
        "standards": ["ASTM D6866", "ISO 16620", "EN 16640", "USDA BioPreferred"],
    },
    "packaging": {
        "title": "Packaging Applications",
        "description": "Largest market segment for bioplastics (~48% of market). Includes rigid packaging (bottles, trays, clamshells), flexible films, food service items, and barrier coatings. Driven by EU PPWR recycled content mandates, SUPD bans, and brand sustainability commitments.",
        "aka": ["Sustainable Packaging", "Bio-based Packaging", "Compostable Packaging"],
        "term_type": "application",
        "related": ["pla", "pha", "bio-pe", "bio-pet", "pbat", "compostable", "food-contact", "ppwr-packaging-waste-regulation", "single-use-plastics-directive"],
        "summary": "Packaging drives bioplastics demand — regulation (PPWR, SUPD) and brand commitments are key growth drivers.",
        "companies": ["Amcor", "Berry Global", "Sealed Air", "DS Smith", "Smurfit Kappa", "Mondi", "Huhtamaki", "Tetra Pak", "SIG", "Novamont", "NatureWorks", "Total Corbion", "Danimer Scientific"],
        "applications": ["Food packaging", "Beverage bottles", "Flexible films", "Food service ware", "Cosmetic containers", "E-commerce packaging", "Agricultural films"],
        "standards": ["PPWR", "SUPD", "EN 13432", "ASTM D6400", "ISO 18602", "ISO 18606"],
    },
    "automotive": {
        "title": "Automotive Applications",
        "description": "Growing bioplastics segment for interior parts (seat foams, dashboards, door panels), under-hood components, and structural elements. Driven by OEM sustainability targets, recycled content mandates, and weight reduction for EV range. Key materials: Bio-PA, Bio-PP, PLA blends, PHA.",
        "aka": ["Automotive Bioplastics", "Bio-based Automotive Parts", "Green Automotive Materials"],
        "term_type": "application",
        "related": ["bio-pp", "bio-pet", "pla", "drop-in-bioplastic", "mass-balance-approach", "carbon-footprint"],
        "summary": "Automotive adopts bioplastics for sustainability targets, weight reduction, and recycled content mandates — interior and under-hood applications growing.",
        "companies": ["BASF", "Covestro", "DSM", "Lanxess", "SABIC", "Toyota", "Ford", "BMW", "Mercedes-Benz", "Volvo", "Stellantis", "Hyundai", "Mitsubishi Chemical"],
        "applications": ["Seat foams", "Dashboard components", "Door panels", "Under-hood parts", "Structural components", "Carpet fibers", "Airbag housings"],
        "standards": ["ISO 14021", "ISO 14040", "ELV Directive", "PPWR (future)"],
    },
    "textiles": {
        "title": "Textile Applications",
        "description": "Bioplastics in fibers for apparel, nonwovens, technical textiles. PLA fibers (moisture-wicking, UV resistance), PHA (marine-degradable fishing gear), Bio-PET (recyclable polyester). Addresses microplastic pollution and textile waste. Blends with natural fibers common.",
        "aka": ["Bio-based Textiles", "Sustainable Fibers", "Biopolymer Textiles"],
        "term_type": "application",
        "related": ["pla", "pha", "bio-pet", "synthetic-biology", "fermentation", "microplastic"],
        "summary": "Textiles adopt bio-based fibers to reduce microplastic pollution and enable recyclable/compostable apparel — PLA and PHA leading.",
        "companies": ["NatureWorks", "Total Corbion", "Far Eastern New Century", "Teijin", "Toray", "Mitsubishi Chemical", "RWDC", "Danimer", "Spinnova", "Renewcell"],
        "applications": ["Apparel fibers", "Nonwovens (wipes, hygiene)", "Technical textiles", "Fishing gear", "Geotextiles", "Carpet backing"],
        "standards": ["GRS", "RCS", "OEKO-TEX", "Bluesign", "EU Textiles Strategy"],
    },
    "agriculture-films": {
        "title": "Agricultural Films",
        "description": "Biodegradable mulch films, silage films, and controlled-release fertilizer coatings that can be tilled into soil after use. Eliminates plastic retrieval and disposal. Key materials: PBAT blends, PLA, starch-based, PHA. Certified to EN 17033 / ISO 23517 for soil biodegradability.",
        "aka": ["Mulch Films", "Biodegradable Mulch", "Ag Films", "Soil-Biodegradable Films"],
        "term_type": "application",
        "related": ["pbat", "pla", "starch-based-bioplastic", "biodegradable", "compostable", "soil-biodegradable"],
        "summary": "Soil-biodegradable mulch films eliminate plastic waste in agriculture — tilled in after harvest, no retrieval needed.",
        "companies": ["Novamont", "BASF", "Kingfa", "BioBag", "RKW", "AB Rani Plast", "Polifilm", "Groupe Barbier", "Agriplast"],
        "applications": ["Mulch films", "Silage films", "Greenhouse films", "Controlled-release fertilizers", "Seed coatings", "Plant pots"],
        "standards": ["EN 17033", "ISO 23517", "DIN EN 17033", "OK Biodegradable SOIL"],
    },
    "food-contact": {
        "title": "Food Contact Materials",
        "description": "Materials approved for direct contact with food. Bioplastics widely used: PLA (FDA 21 CFR, EU 10/2011), Bio-PE, Bio-PET, PBS. Must meet migration limits, compositional requirements, and GMP. Certification varies by region (FDA GRAS, EU positive lists, China GB).",
        "aka": ["Food-Grade Bioplastics", "Food Contact Approved", "FCM"],
        "term_type": "application",
        "related": ["pla", "bio-pe", "bio-pet", "pbs", "compostable", "packaging", "packaging-waste-regulation"],
        "summary": "Bioplastics widely approved for food contact — PLA, Bio-PE, Bio-PET, PBS meet FDA/EU migration limits for food packaging.",
        "companies": ["NatureWorks", "Total Corbion", "Novamont", "Danimer", "FKuR", "BASF", "Amcor", "Sealed Air", "Tetra Pak", "Huhtamaki"],
        "applications": ["Food packaging", "Beverage bottles", "Food service ware", "Disposable tableware", "Produce bags", "Coffee capsules"],
        "standards": ["EU 10/2011", "FDA 21 CFR 177", "China GB 4806", "ISO 18602", "EN 13432"],
    },
    "medical-healthcare": {
        "title": "Medical & Healthcare Applications",
        "description": "Biodegradable polymers for sutures, implants, drug delivery, tissue engineering. PLA, PGA, PLGA, PCL, PHA offer biocompatibility and tunable degradation. FDA Class VI, USP Class VI, ISO 10993 biocompatibility required. High-value, low-volume segment.",
        "aka": ["Medical Bioplastics", "Bioresorbable Polymers", "Biomedical Polymers"],
        "term_type": "application",
        "related": ["pla", "pga", "plga", "pcl", "pha", "biodegradable", "synthetic-biology"],
        "summary": "Medical bioplastics enable resorbable implants and controlled drug delivery — high value, strict biocompatibility requirements.",
        "companies": ["Corbion", "Evonik", "DSM", "KLS Martin", "Zimmer Biomet", "DePuy Synthes", "Bioretec", "Poly-Med", "Bezwada Biomedical"],
        "applications": ["Sutures", "Bone fixation", "Drug delivery", "Tissue scaffolds", "Stents", "Membranes", "Wound care"],
        "standards": ["ISO 10993", "USP Class VI", "FDA Class VI", "ISO 13485", "MDR 2017/745"],
    },
    "construction": {
        "title": "Construction Applications",
        "description": "Bioplastics in building materials: insulation foams (PHA, PLA), piping (Bio-PE), composites (natural fiber reinforced), coatings, adhesives. Driven by green building certifications (LEED, BREEAM, DGNB) and embodied carbon reduction. Still early stage vs packaging/automotive.",
        "aka": ["Green Building Materials", "Bio-based Construction", "Sustainable Construction"],
        "term_type": "application",
        "related": ["pha", "pla", "bio-pe", "drop-in-bioplastic", "carbon-footprint", "mass-balance-approach", "natural-fiber-composite"],
        "summary": "Construction adopts bioplastics for green building credits and embodied carbon reduction — insulation, piping, composites emerging.",
        "companies": ["BASF", "Covestro", "NatureWorks", "Total Corbion", "Kingfa", "Technoform", "Isocell", "Gutex", "Pavatex", "HempFlax"],
        "applications": ["Insulation foams", "Piping systems", "Natural fiber composites", "Coatings", "Adhesives", "Vapor barriers", "3D printed construction"],
        "standards": ["LEED", "BREEAM", "DGNB", "EPD", "EN 15804", "ISO 21930"],
    },
    "consumer-goods": {
        "title": "Consumer Goods Applications",
        "description": "Bioplastics in everyday products: electronics casings, toys, cosmetics packaging, household goods, footwear, personal care. Brands adopt for sustainability marketing and regulation compliance. Materials: PLA, Bio-PE, Bio-PET, PHA, PBAT blends. Often combined with recycled content.",
        "aka": ["Sustainable Consumer Products", "Green Consumer Goods", "Eco-friendly Products"],
        "term_type": "application",
        "related": ["pla", "pha", "bio-pe", "bio-pet", "pbat", "packaging", "recycled-content", "mass-balance-approach"],
        "summary": "Consumer brands adopt bioplastics for sustainability positioning — electronics, toys, cosmetics, household, footwear growing segments.",
        "companies": ["LEGO", "Mattel", "Hasbro", "Samsung", "LG", "Sony", "L'Oréal", "Unilever", "P&G", "Henkel", "Adidas", "Allbirds", "On Running", "Coca-Cola", "PepsiCo", "Nestlé", "Danone"],
        "applications": ["Electronics housings", "Toys", "Cosmetics packaging", "Household goods", "Footwear", "Personal care", "Sporting goods", "Luggage"],
        "standards": ["ISO 14021", "FSC", "PEFC", "Cradle to Cradle", "B Corp"],
    },
    "sugarcane": {
        "title": "Sugarcane Feedstock",
        "description": "Primary feedstock for bio-ethanol (→ Bio-PE, Bio-PET) and lactic acid (→ PLA). Brazil is dominant producer. Bagasse (fibrous residue) used for energy and 2G feedstocks. Sustainability concerns: land use, water, labor, biodiversity. Bonsucro certification addresses social/environmental criteria.",
        "aka": ["Sugar Cane", "Saccharum officinarum", "Cane Sugar"],
        "term_type": "feedstock",
        "related": ["bio-pe", "bio-pet", "pla", "fermentation", "bio-based", "lignocellulosic-biomass", "bagasse"],
        "summary": "Sugarcane is the main feedstock for Bio-PE and PLA — Brazil leads; bagasse enables 2G biorefineries.",
        "companies": ["Raízen", "Cosan", "São Martinho", "Tereos", "Braskem", "Dow", "NatureWorks", "Total Corbion", "Corbion", "GranBio"],
        "applications": ["Bio-ethanol (→ Bio-PE)", "Sugar (→ Lactic acid → PLA)", "Bagasse (→ Energy, 2G feedstock)", "Bioplastics feedstock"],
        "standards": ["Bonsucro", "RSB", "ISCC", "ProTerra"],
    },
    "corn": {
        "title": "Corn Feedstock",
        "description": "Primary feedstock for PLA production via corn starch → glucose → lactic acid fermentation. US is dominant producer. Concerns: food vs fuel, land use, fertilizer runoff, GMO. Alternative: wheat, cassava, potato starch. 2G pathways use corn stover (residue) to avoid food competition.",
        "aka": ["Maize", "Corn Starch", "Zea mays"],
        "term_type": "feedstock",
        "related": ["pla", "starch-based-bioplastic", "fermentation", "bio-based", "lignocellulosic-biomass", "food-vs-fuel"],
        "summary": "Corn starch is the main PLA feedstock — US dominates; corn stover enables 2G routes avoiding food competition.",
        "companies": ["NatureWorks", "Total Corbion", "Corbion", "ADM", "Cargill", "Ingredion", "Tate & Lyle", "Roquette", "COFCO", "Futerro"],
        "applications": ["Corn starch → Glucose → Lactic acid → PLA", "Corn stover → 2G ethanol/chemicals", "HFCS", "Starch derivatives"],
        "standards": ["RSB", "ISCC", "ProTerra", "Non-GMO Project"],
    },
    "lignocellulosic-biomass": {
        "title": "Lignocellulosic Biomass",
        "description": "Non-food plant biomass (agricultural residues, forestry residues, energy crops) composed of cellulose, hemicellulose, and lignin. Key 2G feedstock for bio-based chemicals, fuels, and materials. Avoids food vs fuel conflict. Pretreatment is key technical challenge. Includes corn stover, wheat straw, sugarcane bagasse, wood chips, miscanthus, switchgrass.",
        "aka": ["Lignocellulose", "2G Feedstock", "Non-Food Biomass", "Cellulosic Biomass"],
        "term_type": "feedstock",
        "related": ["biorefinery", "fermentation", "sugarcane", "corn", "hydrothermal-liquefaction", "thermochemical-liquefaction", "pretreatment"],
        "summary": "Lignocellulosic biomass (ag/forestry residues) is the sustainable 2G feedstock — avoids food competition, abundant, requires pretreatment.",
        "companies": ["Clariant", "DuPont (now Dow)", "POET", "GranBio", "Beta Renewables", "Abengoa", "Borregaard", "Stora Enso", "UPM", "Sekab", "Lanzatech"],
        "applications": ["2G bioethanol", "Furfural", "Levulinic acid", "Cellulose nanocrystals", "Lignin valorization", "Hemicellulose derivatives", "Biochemicals"],
        "standards": ["RSB", "ISCC", "FSC", "PEFC", "SBP"],
    },
    "used-cooking-oil": {
        "title": "Used Cooking Oil (UCO)",
        "description": "Waste lipid feedstock for HVO/HEFA renewable diesel, SAF, and bio-based chemicals (azelaic acid, sebacic acid, polymer precursors). Major circular feedstock — diverts waste from sewage, avoids land use. EU counts double toward renewable targets. Supply limited, fraud risk (virgin palm oil mislabeled as UCO).",
        "aka": ["UCO", "Waste Cooking Oil", "Yellow Grease", "Brown Grease"],
        "term_type": "feedstock",
        "related": ["circular-economy", "hydrothermal-liquefaction", "bio-based", "mass-balance-approach", "iscc-plus", "saf"],
        "summary": "Used cooking oil is a premium circular feedstock for renewable fuels and bio-chemicals — waste-to-value, double counting in EU.",
        "companies": ["Neste", "Diamond Green Diesel", "ENI", "TotalEnergies", "Preem", "Renewable Energy Group", "Greenergy", "Olleco", "Valley Proteins"],
        "applications": ["HVO/HEFA renewable diesel", "Sustainable Aviation Fuel (SAF)", "Azelaic/sebacic acid (→ Polyamides)", "Bio-lubricants", "Surfactants"],
        "standards": ["ISCC EU", "RSB", "RED II Annex IX", "RFS2"],
    },
    "co2-feedstock": {
        "title": "CO₂ Feedstock",
        "description": "Carbon dioxide captured from industrial emissions or direct air capture (DAC) used as carbon source for chemicals, fuels, and materials via electrochemical, catalytic, or biological pathways. Enables carbon-negative materials if paired with renewable energy. Key pathways: CO₂ → methanol → olefins; CO₂ → formic acid; CO₂ → polycarbonates; microbial electrosynthesis.",
        "aka": ["Carbon Capture and Utilization (CCU)", "CO₂ Utilization", "Carbon-to-Value", "Direct Air Capture (DAC)"],
        "term_type": "feedstock",
        "related": ["circular-economy", "carbon-footprint", "mass-balance-approach", "synthetic-biology", "electrochemical-reduction", "avantium"],
        "summary": "CO₂ as feedstock turns waste carbon into valuable products — carbon-negative if renewable energy powers the conversion.",
        "companies": ["Avantium", "LanzaTech", "Carbon Clean", "Climeworks", "Carbon Engineering", "Global Thermostat", "Covestro", "BASF", "Asahi Kasei", "Mitsubishi Chemical", "OPX Biotechnologies"],
        "applications": ["Polycarbonates (CO₂-based)", "Polyurethanes (CO₂-based polyols)", "Methanol → Olefins", "Formic acid", "SAF (Power-to-Liquid)", "Concrete curing"],
        "standards": ["ISO 14067", "RSB", "ISCC", "Corsia", "RED II RFNBO"],
    },
}

def create_glossary_file(slug, data):
    """Create a glossary markdown file from template."""
    
    # Build related terms list
    related_list = ",\n".join([f'    "{r}"' for r in data.get("related", [])])
    
    # Build companies list
    companies_list = ",\n".join([f'    "{c}"' for c in data.get("companies", [])])
    
    # Build applications list
    apps_list = ",\n".join([f'    "{a}"' for a in data.get("applications", [])])
    
    # Build standards list
    standards_list = ",\n".join([f'    "{s}"' for s in data.get("standards", [])])
    
    # Build aka list
    aka_list = ",\n".join([f'    "{a}"' for a in data.get("aka", [])])
    
    content = f'''---
title: "{data["title"]}"
description: "{data["description"]}"
aka:
{aka_list}
term_type: "{data["term_type"]}"
related:
{related_list}
summary: "{data["summary"]}"
sitemap:
  priority: 0.6
major_producers:
{companies_list}
applications:
{apps_list}
standards:
{standards_list}
---

## Overview

{data["description"]}

## Key Concepts

{data.get("summary", "")}

## Industry Landscape

### Major Companies & Projects

{", ".join(data.get("companies", ["Various industry players"]))} are actively developing {data["title"].lower()} technologies and applications.

## Applications

{", ".join(data.get("applications", ["Various applications across industries"]))}

## Standards & Certifications

{", ".join(data.get("standards", ["Industry standards under development"]))}

## Related Terms

{", ".join(data.get("related", []))}

## Further Reading

- Industry reports from Nova-Institute, European Bioplastics, ISCC
- Peer-reviewed literature in Green Chemistry, ACS Sustainable Chemistry & Engineering
- Regulatory updates from EU Commission, USDA BioPreferred, FDA
'''

    filepath = GLOSSARY_DIR / f"{slug}.md"
    filepath.write_text(content)
    print(f"Created: {filepath}")

if __name__ == "__main__":
    for slug, data in MISSING_TERMS.items():
        create_glossary_file(slug, data)
    
    print(f"\nCreated {len(MISSING_TERMS)} glossary terms!")
