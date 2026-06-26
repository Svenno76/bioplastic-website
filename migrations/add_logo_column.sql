-- SQL Migration for Bioplastics Portal Logo Support
-- Run this in the Supabase SQL Editor to add logo support

-- 1. Add logo column if not exists
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'companies' AND column_name = 'logo'
    ) THEN
        ALTER TABLE companies ADD COLUMN logo TEXT;
    END IF;
END $$;

-- 2. Create index for faster lookups
CREATE INDEX IF NOT EXISTS idx_companies_logo ON companies(logo) WHERE logo IS NOT NULL;

-- 3. Bulk update logos (newly discovered + existing from frontmatter)
UPDATE companies SET logo = '/images/logos/chugai-pharmaceutical.png' WHERE slug = 'chugai-pharmaceutical' OR name ILIKE '%Chugai%';
UPDATE companies SET logo = '/images/logos/entec-polymers.png' WHERE slug = 'entec-polymers' OR name ILIKE '%Entec%';
UPDATE companies SET logo = '/images/logos/handm-group.png' WHERE slug = 'handm-group' OR name ILIKE '%H&M%';
UPDATE companies SET logo = '/images/logos/hugo-boss.png' WHERE slug = 'hugo-boss' OR name ILIKE '%Hugo Boss%';
UPDATE companies SET logo = '/images/logos/inter-ikea-group.png' WHERE slug = 'inter-ikea-group' OR name ILIKE '%Inter IKEA%';
UPDATE companies SET logo = '/images/logos/lego-group.png' WHERE slug = 'lego-group' OR name ILIKE '%Lego%';
UPDATE companies SET logo = '/images/logos/mondi.png' WHERE slug = 'mondi' OR name ILIKE '%Mondi%';
UPDATE companies SET logo = '/images/logos/novonor.png' WHERE slug = 'novonor' OR name ILIKE '%Novonor%';
UPDATE companies SET logo = '/images/logos/precision-plants.png' WHERE slug = 'precision-plants' OR name ILIKE '%Precision Plants%';
UPDATE companies SET logo = '/images/logos/psaltry-international.png' WHERE slug = 'psaltry-international' OR name ILIKE '%Psaltry%';
UPDATE companies SET logo = '/images/logos/releaf.png' WHERE slug = 'releaf' OR name ILIKE '%ReLeaf%';
UPDATE companies SET logo = '/images/logos/sealed-air.png' WHERE slug = 'sealed-air' OR name ILIKE '%Sealed Air%';
UPDATE companies SET logo = '/images/logos/siemens.png' WHERE slug = 'siemen%';
UPDATE companies SET logo = '/images/logos/sojitz.png' WHERE slug = 'sojitz' OR name ILIKE '%Sojitz%';
UPDATE companies SET logo = '/images/logos/technip-energies.png' WHERE slug = 'technip-energies' OR name ILIKE '%Technip%';

-- 4. Verify
SELECT name, logo FROM companies WHERE logo IS NOT NULL ORDER BY name;
