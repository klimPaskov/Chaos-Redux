# Gas Masks, Civil Defence, and Population Protection

## Gameplay promise

Gas masks become a strategic stockpile shared by the military and civil defence. The player must decide how much protection to reserve for frontline formations, headquarters, industry, cities, occupied territory, and emergency replacement.

A country that expects chemical war can prepare and survive. A country that ignores protection can suffer mass organisation collapse, deaths, medical saturation, and political panic after the first raid.

## Equipment abstraction

One `gas_mask_equipment` unit is a protective-equipment crate.

For civilian distribution, one crate protects about one thousand people before efficiency modifiers.

For military issue, one crate supports about one hundred fully fitted soldiers once filters, training supplies, spare parts, carrying equipment, and replacement material are included.

This abstraction keeps stockpiles readable and lets one equipment family serve civilian and military systems.

## Protection components

### Respirator coverage

Primary defence against choking agents and aerosol exposure.

### Protective clothing

Needed for blister and persistent agents. Improved and advanced equipment provides more clothing and sealing support.

### Filter reserve

Determines how long a protected posture can remain active.

### Training and warning

Determines how quickly troops and civilians use protection after warning.

### Antidote and medical support

Needed for strong nerve-agent protection and casualty reduction.

The UI can show one headline coverage value with component details in the tooltip.

## Military protection

### Division coverage

Coverage is calculated from:

- gas-mask equipment assigned to the division
- Gas Mask and Decontamination Detachment
- headquarters Protective Logistics Section
- equipment model
- division manpower
- supply status
- active protective posture
- recent filter consumption

### Coverage bands

| Coverage | Effect |
| ---: | --- |
| 0 to 24 | Unprotected. Full surprise and exposure. |
| 25 to 49 | Partial issue. Reduced choking effect, high unit variance. |
| 50 to 74 | Standard issue. Strong choking protection, modest blister and nerve protection. |
| 75 to 89 | Improved issue. Strong organisation and death reduction. |
| 90 to 100 | Full protected posture. Maximum protection with movement and supply penalties. |

### Protective posture penalty

Protection should not be a pure bonus. When masks and suits are worn continuously:

- movement falls slightly
- attack and breakthrough fall slightly
- supply consumption rises
- heat and desert penalties increase
- fatigue or recovery worsens during long alerts

Improved technology and headquarters logistics reduce these penalties.

## Civilian protection

### State coverage

Each controlled core or occupied state can track civilian protective coverage after chemical threat becomes relevant.

Coverage is created by decisions and can decay through:

- filter use
- storage loss
- bombing
- occupation
- disrupted railways
- panic and poor fitting
- repeated alerts

### Distribution cost formula

Base crates:

`state population / 1,000`

Modifiers:

- urban or capital state: 1.10 to 1.30
- low infrastructure: 1.10 to 1.40
- active bombing or combat: 1.20 to 1.50
- occupied non-core state: 1.25 to 1.75
- established civil defence: 0.75 to 0.90
- prior registration and fitting: 0.80 to 0.90
- emergency improvised issue: 0.60 cost, lower effective coverage and faster decay

A single action can distribute partial coverage when full cost is unaffordable.

## Civil-defence decision family

### Establish National Respirator Reserve

Purpose: create a permanent reserve target and production priority.

Costs:

- civilian factory burden
- rubber or strategic material pressure where appropriate
- support equipment
- time

Outcome:

- raises reserve efficiency
- unlocks state distribution
- creates periodic training and replacement cost

### Register and Fit the Population

Purpose: improve distribution efficiency and warning response.

Costs:

- political administration
- local manpower
- small equipment loss through fitting
- time

Outcome:

- lowers future distribution cost
- reduces first-use civilian deaths
- increases public awareness, which can create war-support or panic effects depending on threat

### Issue Masks to Priority Cities

Targeted decision for capitals, major victory points, ports, airbases, and industrial states.

Consumes crates based on population and target efficiency. Creates 25 to 60 coverage depending on selected intensity.

### Full State Distribution

Expensive action that attempts 80 to 100 coverage. Requires stockpile, infrastructure, and administrative readiness.

### Emergency Distribution During Raid Alert

Fast, inefficient, high-wastage action available after a chemical air threat or confirmed enemy use.

- immediate partial coverage
- consumes 20 to 40 percent more crates
- creates congestion and temporary local output loss

### Replace Filters and Damaged Masks

Restores coverage after exposure. Cost scales with contamination severity and population already protected.

### Collect and Recondition Old Masks

Cheap recovery decision with lower reliability. Useful for minors and desperate countries. Can create defective-mask events.

### Supply Occupied Populations

Reduces deaths and resistance but consumes large stocks. Withholding masks can save equipment while increasing deaths, evidence, resistance, and atrocity pressure when the occupier created the hazard.

### Export Protective Equipment

Lend-lease or decision-based aid to allies and victims. It can improve relations, lower sanction pressure for a compliant country, and create shortages at home.

## Chemical raid response

When a chemical raid begins or a probable attack is detected, the target can choose a response based on warning time.

### Sound the chemical alarm

Consumes no masks but creates temporary production and movement disruption. Improves response time.

### Distribute reserve masks

Consumes crates and raises target-state coverage before raid resolution if warning is sufficient.

### Move civilians into shelters

Reduces exposed share. Costs local output, trains, and administration. Limited by infrastructure and warning time.

### Protect hospitals and utilities

Consumes support equipment and masks. Reduces medical saturation and continuing deaths.

### Keep industry operating

Maintains output but increases exposed share and deaths. This is a deliberate high-risk option, not a free default.

## Starting stockpile methodology

Starting stocks are calculated from:

- fielded and mobilisable military manpower
- core population
- First World War belligerent experience
- industrial capacity
- civil-defence program profile
- national chemical policy

### Recommended population-coverage targets

| Country profile | Civilian reserve target | Military reserve target |
| --- | ---: | --- |
| Mass civil defence | 65 to 85 percent | 125 to 175 percent of fielded need |
| Large prepared power | 30 to 50 percent | 100 to 150 percent |
| Military-first program | 10 to 30 percent | 100 to 140 percent |
| Limited program | 3 to 12 percent | 50 to 100 percent |
| Minimal program | 0 to 5 percent | 0 to 50 percent |

A military reserve target above 100 percent represents replacement filters, mobilisation stocks, and training losses.

### Major-power 1936 bands

The exact crate totals depend on current map population. The implementation should calculate from population and clamp to these broad ranges.

| Country | Civilian profile | Starting crate band | Notes |
| --- | --- | ---: | --- |
| Britain | Mass civil defence | 35,000 to 50,000 | Highest civilian distribution and registration. |
| France | Large prepared power | 18,000 to 30,000 | Strong military and major-city reserve. |
| Germany | Large prepared power | 20,000 to 32,000 | Strong military and urban reserve, uneven public issue. |
| Soviet Union | Military-first large program | 18,000 to 30,000 | Huge population limits percentage coverage. |
| United States | Industrial reserve | 10,000 to 18,000 | Low starting public issue, strong expansion capacity. |
| Italy | Limited to military-first | 7,000 to 13,000 | Military and priority-city emphasis. |
| Japan | Military-first | 8,000 to 15,000 | Limited civilian coverage, operational reserve. |
| Poland | Prepared frontier state | 6,000 to 10,000 | Significant military and urban reserve. |
| Czechoslovakia | Prepared industrial state | 4,000 to 7,000 | Strong per-capita readiness. |
| Belgium | First World War legacy | 2,500 to 4,500 | Priority urban and military stocks. |
| Netherlands | Civil-defence reserve | 2,500 to 5,000 | Urban and infrastructure focus. |

Commonwealth dominions and other First World War countries receive smaller population-scaled reserves. Most minors receive 0 to 2,000 crates unless a focus or history profile justifies more.

### Starting technology does not guarantee full stock

A country can know basic gas-mask technology and still have an inadequate reserve. Research, production, stockpile, distribution, and training remain separate.

## Production and procurement

### Production line

Gas-mask crates use a low individual IC cost but require large volume. Improved models raise cost and reduce replacement demand.

### Emergency procurement

Decision options:

- convert civilian rubber and textile plants
- import masks from allies
- license a foreign design
- recondition First World War stocks
- simplify filters for mass issue

Each option has quality, cost, and reliability tradeoffs.

### Designer effects

Protective designers can improve:

- production cost
- reliability
- filter life
- civilian distribution efficiency
- military posture penalty
- blister or nerve protection

No designer should provide all advantages without a tradeoff.

## Filter exhaustion

### Standing storage loss

A small annual or event-driven loss applies to old basic masks. It should not require a world daily loop.

### Alert consumption

Protective posture consumes filters according to divisions and duration.

### Exposure consumption

Actual exposure consumes additional crates. Persistent states continue to consume replacements until cleanup.

### Civilian consumption

A state under chemical attack loses part of its distributed stock. Replacement decisions restore effective coverage.

## UI

The CBRN interface should show:

- total mask crates
- military crates reserved
- civilian crates distributed
- replacement demand
- current production rate
- country military coverage
- selected state civilian coverage
- selected army order coverage
- current filter consumption

A shortage warning appears when projected reserve is below thirty days of active protective posture.

## AI behavior

AI protection priorities:

1. armies facing an enemy with chemical capability
2. capital and major industrial states
3. supply hubs, ports, airbases, and high-population states
4. occupation areas exposed to contamination
5. general reserve

AI starts production when:

- enemy has chemical technology or use history
- world Condemnation records confirmed chemical use
- it adopts Chaos Warfare
- it has low coverage relative to fielded manpower
- it receives an alert or alliance request

AI should not spend all masks on civilians while frontline divisions remain unprotected during active chemical war. Democratic or civil-defence profiles can reserve a higher civilian share.

## Death reduction

Civilian death multiplier by coverage:

| Coverage | Choking | Blister | Nerve |
| ---: | ---: | ---: | ---: |
| 0 to 24 | 1.00 | 1.00 | 1.00 |
| 25 to 49 | 0.75 | 0.92 | 0.88 |
| 50 to 74 | 0.45 | 0.80 | 0.70 |
| 75 to 89 | 0.25 | 0.60 | 0.48 |
| 90 to 100 | 0.12 | 0.42 | 0.32 |

Advanced civil defence, shelters, decontamination, and medical support can reduce the remaining effect. Masks alone do not eliminate blister or nerve deaths.

## Balance and exploit controls

- distributed masks cannot be instantly reclaimed at full value
- occupied-state distribution cannot be used to create free equipment
- repeated emergency distribution has wastage and cooldown
- protective posture consumes stock
- production cost is low per crate but required volume is high
- countries cannot gain full protection merely by researching the technology
- civilian distribution targets actual controlled population and cleans up after ownership changes

## Acceptance criteria

- every major chemical attack checks military and civilian coverage
- the player can produce and allocate masks
- WWI powers begin with differentiated stockpiles
- Britain has the strongest mass civil-defence profile
- distribution decisions reduce deaths visibly
- masks need replacement after use
- gas-mask support has real equipment requirements
- AI builds and distributes protection intelligently
