# Historical Gas-Mask Stockpiles and Gameplay Conversion

## Research anchors

Gas-mask production reached mass scale during the First World War. The French M2 was produced in roughly 29.3 million units, with millions issued to British forces. The Russian Zelinsky-Kummant family also reached multi-million production. These figures support large residual military expertise and industrial tooling among former belligerents.

British civil defence before the Second World War moved far beyond military issue. Contemporary and museum summaries commonly describe tens of millions of civilian respirators, often around fifty million, prepared for the population. The exact date and count vary by source, so the game should use a broad high-coverage profile rather than claim a single precise historical stock figure.

The 1925 Geneva Protocol prohibited the use of chemical and biological weapons in war. It did not create the later Chemical Weapons Convention model of universal production and stockpile prohibition. Period diplomacy should therefore distinguish treaty status, reservations, retaliation doctrine, first use, confirmed civilian attack, and repeated escalation.

## Why literal masks do not work as equipment units

One literal mask per equipment unit would produce stockpiles in the tens of millions. This is technically possible but creates unreadable production and decision costs. One unit should instead represent a standardized protective-equipment crate.

### Recommended abstraction

One `gas_mask_equipment` unit represents a crate of approximately one thousand civilian respirators or roughly one hundred complete military protective sets with spare filters, fitting equipment, anti-fog supplies, training consumables, and replacement parts.

The difference is intentional. Military issue consumes more supporting material per protected person.

### Military issue conversion

A normal division uses about 80 to 120 crates for full protective issue, depending on manpower, motorisation, and support-company composition. A small elite formation uses fewer crates. A large militia formation uses more because fitting and wastage are worse.

### Civilian issue conversion

A state distribution action uses one crate per one thousand protected civilians before efficiency modifiers. Urban density, low infrastructure, occupation, panic, and damaged railways increase the cost. Civil-defence institutions and prior registration lower it.

## Starting coverage formula

Use population and program profiles rather than fixed universal stocks.

`starting crates = military issue reserve + civilian reserve + training reserve`

- Military issue reserve scales with fielded manpower and intended mobilisation.
- Civilian reserve scales with core population and coverage target.
- Training reserve scales with doctrine, industry, and First World War experience.

The matrices provide explicit 1936 target bands. The implementation agent should calculate exact values from the current map and population data, then clamp them to those bands.

## Historical profile tiers

### Tier A: Mass civil-defence program

Britain is the main 1936 example. Civilian coverage can begin around 65 to 85 percent with high military reserve and established distribution capacity.

### Tier B: Large military and urban reserve

France, Germany, the Soviet Union, Poland, Czechoslovakia, Belgium, and the Netherlands can begin with meaningful military issue and 20 to 50 percent civilian reserve depending on country profile.

### Tier C: Military reserve with limited civilian issue

Italy, Japan, the United States, Commonwealth dominions, Romania, Yugoslavia, Turkey, and other industrial or First World War participants can begin with military stocks and 5 to 25 percent civilian coverage.

### Tier D: Small reserve or emergency procurement

Most small states begin with 0 to 8 percent civilian coverage and enough military stock for a few divisions. They can expand through imports, licensed production, or emergency decisions.

## Filter life and attrition

Stockpile is not permanent coverage. Active chemical alerts, contaminated states, training, tropical climate, and poor storage consume filters and damage masks. Coverage falls when replacements are unavailable. Improved and advanced equipment increases shelf life and reduces recurring consumption.

## Confidence statement

The game bands are historically informed abstractions. They are not claims that every country possessed the exact suggested number of masks in 1936. Country-specific values should be documented as gameplay tuning with a confidence label.
