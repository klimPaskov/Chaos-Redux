# Event 010 Death - Country Package Spec

## Fixed Identity

Death should use a fixed country tag, not a dynamic country, unless implementation discovers a hard engine blocker. The reserved tag is `DTH`.

Rationale:

- fixed flags, colors, leader, focus tree, AI, OOB, and localisation are simpler to wire
- Zol should have a stable character record and portrait
- event-log actor mapping is cleaner with a persistent tag
- defeat and cleanup checks are easier when the actor is known

Implementation must rerun a full collision search before adding `DTH`.

## Files To Add Or Update

| Surface | Expected file |
| --- | --- |
| country tag | `common/country_tags/chaosx_countries.txt` |
| country color | `common/countries/DTH - Death.txt` |
| history | `history/countries/DTH - Death.txt` |
| character | `common/characters/DTH.txt` |
| country names | `localisation/english/010_death_l_english.yml` or country localisation file |
| flag assets | `gfx/flags/DTH.tga`, `gfx/flags/medium/DTH.tga`, `gfx/flags/small/DTH.tga` |
| AI strategy | `common/ai_strategy/DTH.txt` |
| focus tree | `common/national_focus/010_death_focus_tree.txt` |
| OOB | `history/units/DTH_*.txt` if needed |

## Country Setup

Death should not begin on the map in 1936. Its history file can define politics, leader, technology shell, and non-playable setup, but the event creates the actual country presence by transferring the origin island.

History requirements:

- no starting owned states
- no normal factories or deployed units
- no normal generic advisor cabinet
- no ideology drift setup beyond what the UI needs
- no starting wars
- no starting faction
- load an empty OOB only if the engine or local pattern requires an OOB for spawned countries

Country file:

- map color: near-black, with enough contrast from borders and water
- graphical culture: use an existing compatible culture unless a dedicated one is needed
- cosmetic name should remain Death across ideologies

Localisation:

- `DTH: "Death"`
- `DTH_DEF: "Death"`
- `DTH_ADJ: "Death"`
- party name: `The Stillness`
- leader name: `Zol`
- player-facing text must not explain Zol too much

## Shared Classification

Death must be included in shared classifiers when implemented:

- `is_special_chaos_country`
- `is_actual_nonhuman_country`
- any civilian-deaths, diplomacy, event-selection, or chaos-country exclusion triggers that should ignore nonhuman actors

Death should be excluded from:

- ordinary random-country beneficial events
- normal faction invitations
- normal ideological diplomacy
- ordinary civilian-population reward systems
- generic AI economy and production expectations where possible

## Starting Ideas

| Idea | Role | Lifecycle |
| --- | --- | --- |
| `death_not_yet_a_country` | Suppresses normal aggression, diplomacy, and public threat. | Removed at reveal. |
| `death_empty_administration` | Prevents normal economy interpretation; factories do not matter to Death. | Upgraded by focus/economy lane. |
| `death_black_shore` | Early island concealment and target discipline. | Replaced by route spirits after reveal or world-end. |
| `death_the_counting` | Converts consumed population/industry into pressure. | Upgraded through focus lanes. |
| `death_named_by_the_living` | Public stage spirit after reveal. | Replaced or enhanced by world-end. |
| `death_no_more_shores` | World-end aggression and foothold behavior. | World-end only. |

All modifiers should be tuned through script constants. Death should not get normal industry bonuses.

## Leader And Character

Zol is fictional and symbolic.

Character requirements:

- stable `DTH_zol` character
- leader role assigned by event setup or history
- no real-person portrait
- portrait should be generated/symbolic and period-compatible
- traits should be fixed-purpose and not normal ideology buffs

Possible leader traits:

- `death_zol_the_last_clerk`
- `death_zol_no_envoy`
- `death_zol_the_counting`

Trait effects should reinforce spread, concealment, withering, or ghost capacity, not normal factory output.

## Defeat Rules

Death should have an effective zero-surrender fantasy, but the actual defeat rule is scripted:

- Death revealed or active
- all Death-controlled consumed states are occupied by enemies or no longer controlled by Death
- no active world-end foothold remains
- no pending consumption event target remains valid
- origin state is occupied and the clearance mission succeeds if the origin still exists
- Death has no active ghost divisions or scripted cleanup can safely remove them

Defeat effects:

- set `death_defeated`
- clear `world_threat_source_death`
- call `refresh_world_threat_state`
- cancel Death spread events and missions
- remove or retire Zol from normal country leadership
- clear global event targets used by Death
- convert consumed states to `death_recovered_wasteland`, not instant normal recovery
- fire aftermath super-event only if Death reached public/severe thresholds

If world-end fired first, defeat should be an aftermath branch with scars and reconstruction locks rather than clean restoration.

## Units And Templates

Death should not train a normal army. Ghost units are spawned by scripted effects and capped by consumed population/state counts.

Templates:

| Template | Stage | Behavior |
| --- | --- | --- |
| `death_pale_company_template` | early ghost stage | weak border-holding unit |
| `death_mute_regiment_template` | mature ghost stage | stronger local counterattack unit |
| `death_final_muster_template` | world-end | infantry-comparable emergency unit |

If custom battalions are required, define unit icons and localisation. If a new equipment archetype is introduced, update `common/script_enums.txt` in the same implementation change.

Ghost divisions must not be farmable for normal equipment, XP, or manpower. Prefer locked scripted templates and controlled spawn effects.

## AI Strategy

Death AI strategy should:

- avoid normal war justifications
- avoid normal faction behavior
- prioritize scripted target arrays and spread pulses
- defend origin/consumed states early
- use local attacks after `Mute Regiments`
- become aggressive only after world-end
- never spend on normal economic construction if it has no use

AI strategy values should be phase-gated and route-gated.

## Country Package Audit Checklist

Before implementation is considered complete, run a country package audit for:

- tag registration and no collision
- flag sizes and paths
- leader/portrait/character references
- focus tree loading
- AI strategy
- no normal diplomacy leaks
- no missing localisation
- no generic cabinet clutter
- defeat cleanup
