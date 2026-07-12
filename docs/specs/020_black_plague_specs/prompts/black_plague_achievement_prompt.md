# Black Plague Achievement Implementation Prompt

Implement the Event 20 achievement set from `matrices/achievement_matrix.md`. Read the accepted Event 20 specs, `AGENTS.md`, `chaos-redux-events`, `hoi4-focus-trees`, `hoi4-decisions-missions`, and `chaos-redux-event-assets` before editing.

## Achievement set

Implement all fourteen planned achievements unless the parent explicitly records a rejection or merge.

1. The First Cordon
2. Forty Days
3. Open Roads, Closed Graves
4. Physician Against the Night
5. The Common Remedy
6. The Cabinet of Black Glass
7. The Physician's Folly
8. Burn the Warrens
9. No Census Required
10. One Crown, Many Tails
11. The Rat That Read
12. Crown of One Continent
13. The Pale Sovereign
14. Doctor Wu's Last House Call

These are working labels. Write final titles and descriptions from the directions in the achievement matrix. Do not reveal hidden event mechanics in ordinary event, decision, or focus text.

## Implementation rules

- use the single Chaos Redux root achievement registry
- conflict check every final achievement ID
- implement explicit eligibility, success, and disqualifier tracking
- preserve intended tracking through Rat Nation to Rat King tag transfer where required
- set and check a permanent Black Plague triggerable-scenario launch flag that disqualifies every ordinary Event 20 achievement unless one is explicitly approved for scenario play
- prevent accidental unlock from manual debug firing, other scenario shortcuts, puppet control, or unrelated tags according to the existing achievement pattern
- do not make any achievement unlock merely because Event 20 fired
- use flags for boolean history and variables only when real counters are needed
- centralize repeated tracking helpers
- document tracking lifecycle and cleanup

## Cross-system tracking

The set needs reliable tracking for:

- origin state and population at Event 20 firing
- maximum infected-state count
- event-attributed deaths
- border corridor timer and route attribution
- use of prohibited or required containment actions
- countermeasure progress and timing relative to evolutions
- unique countries aided
- publication and deployment history
- weapon project branch, stockpile duration, accidents, and domestic return provenance
- Rat Nation destruction contribution
- global burrow clearance
- pulse-created rat divisions
- Rat-Controlled state count
- absorbed Rat Nation count
- Rat King candidate and transfer identity
- government route, Sentience, continent control, and world-end scenario
- Event 163 Doctor Wu bridge and continent cure set

Tracking must not double-count repeated aid to one country, transferred rat units, or disease deaths already recorded by the shared Deaths system.

## Asset requirements

Create one completed 64 by 64 icon for every achievement through the Event 20 asset prompt. Produce grey and not-eligible variants using the project achievement workflow. Put final DDS files directly under `gfx/achievements/` using exact registered IDs.

Do not reuse one icon with recolors across the set. Use the visual directions in the achievement matrix.

## Localisation requirements

For every achievement provide:

- final title
- final player-facing description
- hidden or visible behavior
- clear eligible actor direction
- no internal variable, threshold implementation, or planning-language leakage

## Documentation and audit

Update the canonical Event 20 doc and achievement asset manifest. Before completion, audit every achievement against the exact matrix conditions and test at least one positive and one disqualifying path for each tracking family.
