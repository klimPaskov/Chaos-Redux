# Achievement Implementation and Asset Prompt: Event 15 Utopia Manifesto

Use the achievement matrix as the source design. Inspect the live Chaos Redux achievement registry, localisation pattern, icon GFX file, and tracking conventions before implementation.

All working labels require final localisation writing.

## Required achievements

Implement every proposed ID unless repository review finds an identifier conflict. Preserve the design conditions if an ID must change.

### `utopia_manifesto_no_place_but_home`

Route:

- voluntary commonwealth

Conditions:

- Event 15 accepted by human player
- voluntary final identity formed
- island or capital-ring project completed
- no offensive war initiated by the Event 15 actor after acceptance
- no coercive ultimatum
- no Assigned Colony

Tracking:

- offensive-war disqualifier flag
- coercive ultimatum flag
- assigned-colony flag

Icon:

- open island and linked homes

### `utopia_manifesto_need_not_greed`

Conditions:

- resolve three distinct Need cases through purchase, lease, joint administration, associate charter, or domestic substitution
- renounce at least one obsolete case
- never annex unrelated land through a case

Tracking:

- distinct case-resolution counters
- obsolete-case renunciation flag
- unrelated annexation disqualifier

Icon:

- balanced land and full store

### `utopia_manifesto_every_calling_chosen`

Routes:

- Consent or hidden humanist

Conditions:

- no severe calling shortage
- high Choice
- high Concord
- stable Plenty
- maintain conditions for a sustained period

Disqualifier:

- non-emergency assignment quota beyond allowed limit

Icon:

- six tools around an open hand

### `utopia_manifesto_two_year_table`

Conditions:

- complete two-year reserve objective
- maintain it through a major war, blockade, or equivalent severe supply test

Tracking:

- reserve objective complete
- challenge period
- no manual exploit reset

Icon:

- full store and long calendar ring

### `utopia_manifesto_archipelago_of_small_places`

Conditions:

- lead league with at least five independent or meaningfully autonomous members
- complete shared reserve goal
- complete shared defense goal
- remain independent from a major

Disqualifier:

- annex a league member

Icon:

- five small islands or civic nodes linked together

### `utopia_manifesto_inland_island`

Eligibility:

- recipient was landlocked when Event 15 was accepted

Conditions:

- select Inland Island variant
- complete project
- form final identity
- maintain capital supply through a major war

Disqualifier:

- acquire coastline before variant selection

Icon:

- fortified garden ring around rail hub

### `utopia_manifesto_gold_for_common_use`

Conditions:

- complete common-use or anti-luxury policy
- use the proceeds for emergency imports or public provision
- later reach surplus Plenty
- no severe household shortage at unlock

Icon:

- broken gold ornament beside grain and tools

### `utopia_manifesto_the_joke_understood`

Eligibility:

- hidden humanist route

Conditions:

- reveal hidden route
- preserve open debate
- form practical commonwealth
- complete one peaceful Need case
- complete district network

Disqualifiers:

- penal labor
- Assigned Colony
- censorship of debate

Icon:

- open book reflected in a mirror

### `utopia_manifesto_consent_of_the_governed`

Routes:

- Consent or hidden humanist

Conditions:

- integrate or federate three external areas through local charter and status vote
- no repeated vote on the same territory

Disqualifier:

- Assigned Colony

Icon:

- three charter seals around a house

### `utopia_manifesto_the_perfect_measure`

Route:

- Guardians of Measure

Conditions:

- complete five functioning district roles
- reach high Plenty
- maintain stable Concord
- form planned Utopia
- no active data scandal or district revolt at unlock

Icon:

- compass over a living city grid

### `utopia_manifesto_closed_circle`

Route:

- Closed Island

Conditions:

- World Collapse chaos tier
- complete Perfect Island
- survive a major war
- maintain highest reserve band
- maintain high Assignment

Disqualifier:

- regime or island project reopened before unlock

Icon:

- sealed fortress ring and stocked gate

### `utopia_manifesto_no_foreign_hands`

Conditions:

- defeat a stronger attacking major or faction while Event 15 is active
- hire no auxiliaries

Tracking:

- relative strength or major-attacker check
- auxiliary disqualifier
- defensive war victory

Icon:

- citizen watch holding a gate

### `utopia_manifesto_the_stores_remain`

Conditions:

- enter constitutional crisis
- recover to stable Plenty and Concord
- complete final identity
- preserve public provision institutions

Disqualifier:

- resolve crisis through total repeal

Icon:

- damaged store rebuilt under an open roof

### `utopia_manifesto_no_one_in_chains`

Routes:

- Consent, Common Table, or hidden humanist

Conditions:

- form final identity
- at least one autonomous associate

Disqualifiers:

- penal labor
- Assigned Colony
- forced relocation

Icon:

- open chain beside a common table

## Implementation rules

- Register achievements in the single Chaos Redux achievement registry.
- Use stable flags and variables only when final-state triggers cannot prove the condition.
- Record disqualifiers at the moment they occur.
- Do not let route switching erase disqualifiers.
- Prevent subject, tag-switch, release, and cosmetic-tag exploits.
- Make hidden achievements genuinely hidden where specified.
- Do not unlock an achievement merely because Event 15 fired.
- Add localisation and documentation.
- Add full icon triplets under `gfx/achievements/` with filenames matching exact IDs.
- Update GFX references and manifests.
- Run exploit review and completion audit.

## Asset production

Use the icon artist and achievement reference folder.

For each achievement:

1. Generate a completed 64 by 64 icon designed for the exact condition.
2. Create the grey variant.
3. Create the not-eligible variant by applying the repository overlay to the grey icon.
4. Keep source PNG, processed PNG, contact sheet, final DDS triplet, prompt, manifest, and GFX handoff.
5. Do not reuse one completed icon with only small recolors across different achievements.
