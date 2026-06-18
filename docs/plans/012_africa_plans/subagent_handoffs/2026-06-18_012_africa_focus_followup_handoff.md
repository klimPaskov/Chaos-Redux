# Event 012 Africa Focus Follow-up Handoff

## Scope

Audited Event 012 Africa focus-tree implementation against:

- `docs/specs/012_africa_specs/specs/012_africa_focus_tree_plan.md`
- `docs/specs/012_africa_specs/focus_graphs/`
- `docs/specs/012_africa_specs/matrices/012_africa_acceptance_criteria.md`
- `docs/specs/012_africa_specs/matrices/012_africa_ai_strategy_matrix.md`
- `docs/specs/012_africa_specs/prompts/012_africa_goal_prompt.md`
- `docs/specs/012_africa_specs/prompts/012_africa_coding_prompt.md`
- `common/national_focus/012_africa_focus.txt`
- `common/national_focus/012_africa_authority_focus.txt`
- directly related Event 012 ideas, effects, triggers, decisions, localisation, GFX, and AI strategy files.

Ignored unrelated dirty Event 010 files as requested.

## Changed files

- `common/ai_strategy/012_africa.txt`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_focus_followup_handoff.md`

No focus files, decision files, country history, or state files were edited.

## Patch summary

Added route-aware AI strategy plans for existing route flags that had focus-level weights but no strategy-plan layer:

- `africa_unifier_federal_charter`
- `africa_unifier_sovereign_seats`
- `africa_unifier_high_chaos_covenant`

### Behavior before

- Federal Charter, Sovereign Seats, and unifier high-chaos Covenant routes relied on generic unifier posture plus focus `ai_will_do`.
- Existing explicit unifier route plans covered People’s Front, General Staff, Crown Congress, diaspora return, world-order sponsor, and RSA emergency, but not these three route identities.

### Behavior after

- Federal Charter AI now emphasizes war restraint, civilian industry, and support equipment after `africa_route_federal_charter` or `africa_federal_congress_capitals_ready`.
- Sovereign Seats AI now emphasizes war restraint, infrastructure, and support equipment after `africa_route_sovereign_seats` or `africa_autonomous_regions_open`.
- High-chaos Covenant AI now emphasizes restraint, support equipment, and habitat/infrastructure posture after `africa_high_chaos_route_open`, `africa_route_forest_parliament`, `africa_route_archive_bestiary`, or `africa_world_root_mandate_open`.

## Changed focus ids

None.

## Changed localisation keys and icon ids

None.

## Route coverage table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Opening survival/statebuilding | `AFR_the_charter_mandate`, `AFR_continental_congress`, `AFR_regional_authority_charters`, `AFR_charter_courts` | Present, simplified | Trunk exists and moves legitimacy/authority/cohesion values, but the spec’s `Emergency Congress`, `Paper Cores, Real Burdens`, and `First Charter Diplomacy` are merged into fewer focuses. |
| RSA civil-war subtree | `AFR_rsa_congress_underground` through `AFR_rsa_victory_settlement` | Present | Bounded civil-war lane exists with politics, strikes, defectors, Allied pressure, Pretoria gate, and victory settlement. |
| Federal Congress | `AFR_federal_charter_path` through `AFR_congress_of_capitals` | Present | Has route lock, federal idea, courts, autonomy, citizenship, and integration mission hook. Added AI strategy-plan layer in this audit. |
| People’s Liberation Front | `AFR_peoples_liberation_front`, `AFR_port_unions_and_mine_cells`, `AFR_exile_radios`, `AFR_people_continental_army` | Present | Distinct rewards and existing AI strategy. Shorter than the spec’s full five focus groups. |
| Continental General Staff | `AFR_general_staff_above_parliament` through `AFR_continental_war_plan` | Present | Distinct rewards and existing AI strategy. War-plan hook opens Scramble counter-dockets. |
| Crown Congress and Old Thrones | `AFR_crown_congress` through `AFR_crowns_beneath_the_charter` | Present | Distinct route with regalia verification, no single crown, royal roads, and Charter settlement. |
| Green Covenant / high-chaos myth | `AFR_high_chaos_door`, `AFR_forest_parliament`, `AFR_archive_bestiary_clause`, `AFR_no_seats_for_caricature` through `AFR_world_root_mandate` | Present, visible-locked rather than hidden | High-chaos route is gated by archive mandate and later historical dossier/package flags, but is not hidden with `allow_branch`. This avoids stale visibility because Event 012 does not currently call `mark_focus_tree_layout_dirty`, but it is less hidden than the spec requested. Added AI strategy-plan layer in this audit. |
| Industry / continental economy | `AFR_industrial_convergence`, `AFR_lake_and_rail_agreements`, `AFR_mandate_foundries`, plus regional authority industry focuses | Present, simplified | Has factories, infrastructure, dockyards, and rail/port framing. It is not a full region-by-region economy branch with all named resource lanes. |
| Military / liberation armies | `AFR_liberation_war_office`, `AFR_charter_general_staff`, `AFR_liberation_columns`, military route focuses, authority and Bestiary military focuses | Present, simplified | Uses units/equipment/manpower and decision hooks. Elephant/special high-chaos unit handling is represented through Bestiary/high-chaos systems rather than a dedicated elephant branch in the focus tree. |
| Diplomacy and Charter League | `AFR_regional_authority_charters`, `AFR_charter_courts`, `AFR_charter_assembly_votes`, decision categories in `012_africa_decisions.txt` | Present | Focuses set flags consumed by Charter diplomacy and integration decisions. |
| Expansion and integration | `AFR_scramble_reverse_claims`, `AFR_integrated_regions`, `AFR_autonomous_regions`, `AFR_foreign_holder_case_files`, `AFR_scramble_counter_dockets`, `AFR_africa_is_one` | Present | Uses claims/objective flags and staged `Africa Is One` requirements instead of instant annexation. |
| Diaspora return | `AFR_return_offices` through `AFR_pan_atlantic_congress` | Present | Branch exists, integrates with diaspora decisions and South Atlantic sponsor gate. |
| Regional authorities companion tree | `africa_regional_authority_focus_tree`, `AFR_AUTH_*` focuses | Present, simplified | Shared tree with regional specialization capstones, not bespoke full trees per authority. |
| Archive of Old Seats / Authority Atlas | `AFR_authority_atlas`, `AFR_archive_of_old_seats`, register/dossier lanes, settlement fork, Continental Register | Present | Includes at least five regional dossier lanes and a three-way settlement fork. |
| High-chaos Bestiary companion tree | `africa_high_chaos_actor_focus_tree`, `AFR_BEST_*` focuses | Present | Shared Bestiary tree plus tag-specific capstones for high-chaos actors. |
| Post-unification / Africa Is One | `AFR_continent_sponsor_office`, `AFR_africa_is_one`, `AFR_continental_export_office` | Present | `AFR_continent_sponsor_office` can prepare before `AFR_africa_is_one`; actual export office requires Africa Is One. |
| Sponsor other continent unifiers | `AFR_middle_east_charter_staff`, `AFR_asia_charter_liaison_columns`, `AFR_europe_charter_observers`, `AFR_south_atlantic_return_mandate`, decisions in sponsor category | Present | Focuses prepare each sponsor lane; decisions set sponsorship flags. |
| Dynamic union / world-end path | `AFR_congress_of_continents` through `AFR_the_world_is_one` | Present | Heavily gated by Africa Is One, external proofs, certification, Bestiary, and world-end triggers. |

## Missing or simplified content

- Focus count is 150 total (`108` main + `42` authority/Bestiary companion), inside the spec’s likely `120-180` range, but several spec focus groups are merged into compact branches.
- Focus filters do not implement the exact ten-name taxonomy from the focus plan. Implementation uses five Event 012 custom filters (`FOCUS_FILTER_AFR_CHARTER`, `FOCUS_FILTER_AFR_AUTHORITY_ATLAS`, `FOCUS_FILTER_AFR_SCRAMBLE`, `FOCUS_FILTER_AFR_BESTIARY`, `FOCUS_FILTER_AFR_WORLD_ORDER`) plus vanilla filters. The authority companion tree uses only vanilla filters.
- High-chaos unifier route is visible but unavailable until gated, not fully hidden. Adding `allow_branch` would need a layout refresh hook because `allow_branch` is checked on tree load.
- Regional authority and Bestiary countries have shared companion trees with tag-specific capstones, not fully bespoke country trees. This is a simplification versus the full country-package standard.
- Reward variety is strong overall, but many mid-branch focuses still mainly set flags and move mechanic variables; their gameplay depth depends on the decision layer consuming those flags.
- Archive/Authority Atlas focus lane is present, but the full depth of the 24 historical dossiers lives primarily in scripted effects/decisions rather than one focus per dossier.

## Icon coverage table

| Surface | Status | Notes |
| --- | --- | --- |
| Main Africa focus custom icons | Covered | Event 012 `GFX_goal_africa_*` focus icons and shine variants are defined in `interface/012_africa.gfx`. |
| Main Africa focus vanilla/generic icons | Covered by vanilla | Generic `GFX_goal_generic_*` and `GFX_focus_research*` icons are vanilla references; no missing custom sprite issue found in Event 012. |
| Regional authority companion focus icons | Covered, mixed | Uses Event 012 icons plus vanilla generic icons. No broken Event 012 icon id found. |
| Bestiary companion focus icons | Covered, mixed | Uses Event 012 Bestiary/world/authority icons plus vanilla generic icons. |
| Focus filter icons | Partially covered | Five Event 012 custom focus filter sprites are defined; the spec’s ten conceptual filters are collapsed into these five plus vanilla filters. |

## Localisation and reward mismatch list

- No missing name or `_desc` localisation found for the 150 audited focus IDs in `localisation/english/012_african_union_l_english.yml`.
- No focus reward/name mismatch requiring a local patch was found. Some compact focuses do more mechanical work through flags/decisions than their descriptions can fully expose; this is acceptable if the decision layer remains aligned.
- `AFR_high_chaos_door` description says the Archive identifies impossible packages; reward also sets the `AFR_ARCHIVE_MANDATE` cosmetic tag and Bestiary spirit. This matches the route purpose, but the focus is more of a route transformation than a mere door.

## AI behavior gaps

- Patched: added strategy-plan layer for Federal Charter, Sovereign Seats, and unifier high-chaos Covenant.
- Remaining: authority and Bestiary companion trees have per-tag AI strategy blocks, but the focus files themselves still use mostly broad `constant:africa_ai.strong/normal/preferred` weights.
- Remaining: high-chaos unifier route still uses low focus weights and gating, but there is no rare-personality selector beyond flags/values visible in the focus files.
- Remaining: exact AI use of all focus-unlocked decision families depends on `common/decisions/012_africa_decisions.txt`, which was inspected for hook presence but not edited under this focus-only scope.

## High-priority fixes first

1. If the parent wants the high-chaos route truly hidden, add a safe reveal flow that sets the eligibility flag and calls `mark_focus_tree_layout_dirty`; do not add `allow_branch` alone.
2. Expand or remap focus filters if the exact ten-filter taxonomy is required in-game. This needs filter icon sprites/localisation and focus-file updates.
3. Consider a second pass that makes the authority companion tree use Event 012 custom filters, especially `FOCUS_FILTER_AFR_AUTHORITY_ATLAS`, `FOCUS_FILTER_AFR_CHARTER`, and `FOCUS_FILTER_AFR_BESTIARY`.
4. Broaden route-specific AI beyond strategy plans by adding safer focus `ai_will_do` modifiers for Federal/Sovereign/High-Chaos route invalid states and country archetypes.
5. If full bespoke country-package depth is required, write an improvement-loop plan rather than expanding it inside a focus audit patch.

## Checks performed

- Read required repo rules, skills, offline wiki focus/prerequisite/AI/localisation/decision/idea references, and vanilla focus/AI examples before implementation inspection.
- Counted focus IDs: `108` in `012_africa_focus.txt`, `42` in `012_africa_authority_focus.txt`.
- Checked duplicate focus IDs: none found in scoped Event 012 focus files.
- Checked duplicate focus coordinates: none found in scoped Event 012 focus files.
- Checked focus localisation coverage: no missing focus name or `_desc` keys found for scoped Event 012 focus IDs.
- Checked prerequisite blocks with multiple `focus =` entries and recorded OR-style convergence/branch shortcuts.
- Checked changed AI strategy flags against existing focus/scripted-effect flag writers.
- Checked brace balance for `common/ai_strategy/012_africa.txt`, `common/national_focus/012_africa_focus.txt`, and `common/national_focus/012_africa_authority_focus.txt` after the patch.

## Skipped meaningful validation

- Did not edit or validate decision runtime behavior beyond hook inspection because the prompt forbids decision edits.
- Did not inspect country history/state setup because the prompt forbids editing those surfaces and requested focus-tree scope.
- Did not run the game or in-game focus-tree validation.
- Did not stage or commit.

## Remaining route risks

- The implementation is robustly non-linear, but some branches are compact compared with the full spec and rely on decisions/effects for depth.
- The high-chaos branch is locked by requirements but not hidden.
- The exact spec filter taxonomy is simplified.
- Shared companion trees remain a practical simplification for many created authorities and nonhuman actors.

## Plan handoff

No separate improvement plan was written. Broader work should be queued as a parent-owned improvement-loop pass if the parent wants exact ten-filter taxonomy, true hidden high-chaos reveal, or fully bespoke authority country trees.
