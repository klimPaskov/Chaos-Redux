# Event 005 Soviet Collapse Focus Layout Audit Patch Handoff

## Scope

Audited only:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

No `gfx/flags` paths or flag asset files were touched.

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Republic political route locks | Ukraine and Belarus route-lock rows, plus broader republic/breakaway/internal republic route families in `005_soviet_collapse_republics.txt` | Implemented, visual risk remains | Ukraine row 5 and Belarus row 5 still use complete mutual-exclusion route-lock clusters. Logic is reciprocal, but the route-lock arrows remain dense. |
| Republic industry/logistics routes | Ukraine grain/depot/Black Sea/arsenal routes; Belarus rail/timetable/depot routes; Kazakhstan and regional republic logistics branches | Implemented | Parser found no missing rewards, icons, filters, AI, or duplicate IDs. Several rewards are helper-backed. |
| Republic expansion/diplomacy routes | Ukraine League, Black Sea, western question, foreign liaison; Belarus League, Baltic, corridor; regional branches | Implemented, needs parent review | Route content is present, but some branch rows still feel dense and should be visually reblocked in a larger pass. |
| Custom splinter political/industry/war/diplomacy branches | 19 custom splinter trees in `005_soviet_collapse_custom_splinters.txt`, mostly 47 focuses each | Implemented, repeated scaffold risk | Branches exist, but many trees share near-identical early branch shapes and several direct rewards still read like scaffolding. |
| Factory successors | CFR, MFR, OGB, PRA/RMC/DSC/NRF/ICD/TSC successor packages in `005_soviet_collapse_factory_successors.txt` | Implemented, mixed depth | CFR/MFR have stronger helper-backed routes. OGB and smaller factory/restoration packages are shorter and should be reviewed for payoff depth. |
| Ancient restorations | KZR, SOG, KHW, ALN in `005_soviet_collapse_ancient_restorations.txt` | Implemented compact routes | Four 16-focus trees have political, economic, guard, claim, and endgame arcs. Reused icons are intentional family icons but reduce visual uniqueness. |

## Patch

Changed file:

- `common/national_focus/005_soviet_collapse_republics.txt`

Changed focus IDs:

- `ukr_soviet_collapse_coalition_of_three_ministries`
- `ukr_soviet_collapse_rural_deputy_bloc`
- `ukr_soviet_collapse_british_caution`
- `ukr_soviet_collapse_black_soil_oath`
- `blr_soviet_collapse_foreign_aid_through_brest`
- `blr_soviet_collapse_railway_neutrality`
- `blr_soviet_collapse_guide_companies`
- `blr_soviet_collapse_swamp_roads_closed`
- `blr_soviet_collapse_minsk_supplies_the_front`
- `blr_soviet_collapse_the_league_depot_at_minsk`

Before:

- Belarus had five prerequisite layout violations where child focuses sat on the same row as, or above, visible prerequisite parents:
  - `blr_soviet_collapse_railway_neutrality` against `blr_soviet_collapse_quiet_recognition_letters`
  - `blr_soviet_collapse_guide_companies` against `blr_soviet_collapse_council_bargains_with_forests`
  - `blr_soviet_collapse_swamp_roads_closed` against `blr_soviet_collapse_village_warning_bells`
  - `blr_soviet_collapse_minsk_supplies_the_front` against `blr_soviet_collapse_baltic_wire_rooms`
  - `blr_soviet_collapse_minsk_supplies_the_front` against `blr_soviet_collapse_prepare_league_freight_tables`
- Ukraine and Belarus had several adjacent same-row focuses one x-unit apart.

After:

- All parsed prerequisite parents now sit above their dependent focuses.
- All same-position and one-x-unit adjacent focus placements in the four audited files are cleared.
- No focus reward, route lock, mutual exclusion, icon, localisation key, or AI behavior was changed.

## Icon Coverage Table

| File | Parsed focuses | Missing icons | Repeated icon risk |
| --- | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 501 | 0 | Several intentional/shared route-family icons remain, e.g. `GFX_ukr_soviet_collapse_democratic` across democratic Ukraine focuses. |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 0 | Repeated regional pattern icons remain, e.g. BSC/TNC/ALA-style branch families and repeated FEV/SZA diplomatic-plan icons. |
| `005_soviet_collapse_factory_successors.txt` | 128 | 0 | No missing icons found; repeated icons should be reviewed where shorter successor packages share identity beats. |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 0 | Intentional repeated ancient-family icons appear four times each, e.g. `GFX_focus_soviet_collapse_ancient_workshop_compact`, `GFX_focus_soviet_collapse_ancient_league_bargain`, and endgame icons. |

## Missing Or Simplified Content

- `common/national_focus/005_soviet_collapse_republics.txt:236`, `:275`, `:320`, `:546`, `:1716`: Ukraine's five-way political route lock is mechanically reciprocal but still visually dense because every row-5 route focus mutually excludes several non-adjacent route focuses.
- `common/national_focus/005_soviet_collapse_republics.txt:8881`, `:8912`, `:8945`, `:8977`: Belarus has the same complete-graph route-lock row issue, with `blr_soviet_collapse_timetable_state` visually sitting among route-lock arrows.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:4297` through `:4623`: the BSC starter package shows the repeated custom-splinter scaffold pattern (`birth`, `first_guard`, `stores`, `legitimacy`, `rival`, `doctrine`, `economy`, `league`, `foreign`, `diplomatic_plan`, etc.). This is present across many custom splinters and needs a broader parent pass if the goal is less random, more identity-specific branch feel.
- Direct shallow reward examples still present and not patched because helper edits are out of scope: `DHC_steppe_watch_posts` at `005_soviet_collapse_custom_splinters.txt:14088`, `DHC_rostov_workshop_contracts` at `:14364`, `KHC_steppe_watch_posts` at `:15282`, `FEV_harbor_fortress_line` at `:16605`, `SZA_station_fortress_line` at `:17768`, `OGB_fortify_the_volga_crossings` at `005_soviet_collapse_factory_successors.txt:1459`, and `KHW_symbolic_oasis_authority` at `005_soviet_collapse_ancient_restorations.txt:939`.

## Localisation And Reward Mismatch List

- External localisation files were not inspected or edited because the requested file scope was limited to the four focus files. No focus IDs or localisation keys were renamed.
- Reward mismatch risk remains where a focus name implies a concrete map/mechanic payoff but the reward is mostly `set_country_flag` plus a small flat value. Examples are listed under simplified content.
- No icon IDs were changed.

## AI Behavior Gaps

- Parser found `ai_will_do` present on all 1,698 parsed focuses.
- Route-aware AI exists in many focus blocks through flags, war state, stability, and Soviet pressure checks.
- Gap: custom splinter trees still frequently use similar base weights and similar early-route logic across country identities. Making Chaos countries "very strong and aggressive" likely needs parent-owned AI strategy/helper work outside these four focus files.

## High-Priority Fixes First

1. Parent should reblock Ukraine and Belarus route-lock rows into cleaner route hubs or staggered branch heads so complete mutual-exclusion arrows do not cross through unrelated route choices.
2. Parent should replace remaining direct shallow rewards with existing or new helper calls where appropriate, especially in custom splinter and shorter factory/ancient packages.
3. Parent should deepen repeated custom splinter scaffolds into stronger country-specific political, industrial, military, and expansion payoffs.
4. Parent should review repeated icon families and request new focus icon art only after route identities are stable.

## Validation Run

Ran a focused parser over the four requested files:

- Total parsed focuses: 1,698
- By file:
  - `005_soviet_collapse_republics.txt`: 501
  - `005_soviet_collapse_custom_splinters.txt`: 1,005
  - `005_soviet_collapse_factory_successors.txt`: 128
  - `005_soviet_collapse_ancient_restorations.txt`: 64
- Missing icons: 0
- Missing search filters: 0
- Missing `ai_will_do`: 0
- Missing `completion_reward`: 0
- Duplicate focus IDs: 0
- Non-reciprocal mutual exclusions: 0
- Missing or upward/same-row prerequisite placements after patch: 0
- Same-position or adjacent one-x-unit focus placements after patch: 0

Also ran:

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Result: no whitespace errors reported.

## Skipped Validation

- No in-game load test run.
- No broad HOI4 validator was found or run inside this bounded audit.
- No localisation validation was run because localisation files were outside the requested edit/inspection scope.

## Remaining Route Risks

- Ukraine and Belarus route locks are mechanically safer after this patch but still visually noisy because complete mutual-exclusion clusters remain on the same row.
- Custom splinter trees still risk feeling formulaic due repeated branch skeletons and similar early rewards.
- Some direct rewards remain shallow and should be converted by the parent only if broader helper/mechanic edits are allowed.
- Chaos-country aggression likely needs parent-owned AI strategy or helper work beyond local focus coordinates.
