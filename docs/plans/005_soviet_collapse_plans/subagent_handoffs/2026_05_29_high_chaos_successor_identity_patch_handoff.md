# Soviet Collapse High-Chaos Successor Identity Patch Handoff

Date: 2026-05-29

Scope: narrow focus/decision/localisation patch for concept-led high-chaos/custom successors: PRA, DSC, CFR, MFR, NRF, and ARD.

## Changed files

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

`common/ideas/005_soviet_collapse_ideas.txt` was inspected but not edited in this patch. Existing dirty worktree changes in that file are not mine.

## Route coverage table

| Required route | Implemented route or focus/decision surface | Status | Notes |
| --- | --- | --- | --- |
| PRA railway/logistics identity | `PRA_armored_train_directorate`, `pra_mobilize_station_guard` | Patched | Added trains, motorized equipment, a controlled-state supply hub, and rail construction so the guard path deploys logistics rather than only modifiers. |
| DSC manpower/recruitment pressure | `DSC_dead_regiment_columns`, `dsc_raise_dead_regiment_columns` | Patched | Added infantry/support/artillery stores, mobilization variable gain, and a fortified roll-call post to make dead-regiment recruitment mechanically visible. |
| CFR civilian construction identity | `cfr_survey_unfinished_sites`, `cfr_issue_reconstruction_contracts` | Patched | Survey can reopen a rail link under crane/rail planning; reconstruction contracts can add an extra civilian build site on state-builder/contract/final-foundation routes. |
| MFR military factory/units identity | `mfr_audit_arsenal_orders`, `mfr_convert_depots_to_arms_lines` | Patched | Audit adds support stores; depot conversion can mobilize factory guard manpower and additional infantry/support equipment on war-cabinet/rifle-order/eternal-arsenal routes. |
| Northern naval successor | `NRF_northern_revenant_fleet`, `nrf_raise_icebound_marines` | Patched | Added convoy/support stores, naval XP, coastal fortification, dockyard/coastal-bunker payoff on the revenant fleet end state. |
| Arctic naval directorate | `ARD_arctic_port_endurance`, `ard_mobilize_signature_forces`, `ard_push_extreme_route` | Patched | Added convoy stores, naval XP, coastal defenses, and dockyard construction to the Arctic port survival/extreme route. |

## Missing or simplified content

- CFR and MFR focus trees live outside the permitted focus file, so this patch improved their existing decisions rather than editing `common/national_focus/005_soviet_collapse_factory_successors.txt`.
- No new unit templates were added. The patch uses existing manpower/equipment/controlled-state building patterns to stay inside the narrow scope and avoid new scripted helper work.
- No new ideas were added. Existing ideas already cover these concepts, and the task asked to avoid visible idea spam.
- No new formable, release, evolution, scripted effect, scripted trigger, or constant logic was touched; the parent is handling release/evolution/flag mechanics separately.

## Icon coverage table

| Surface | Icon id | Status |
| --- | --- | --- |
| `PRA_armored_train_directorate` | `GFX_focus_PRA_armored_train_directorate` | Existing icon found |
| `DSC_dead_regiment_columns` | `GFX_focus_DSC_dead_regiment_columns` | Existing icon found |
| `NRF_northern_revenant_fleet` | `GFX_focus_NRF_northern_revenant_fleet` | Existing icon found |
| `ARD_arctic_port_endurance` | `GFX_focus_ARD_arctic_port_endurance` | Existing icon found |
| `pra_mobilize_station_guard` | `GFX_decision_pra_mobilize_station_guard` | Existing icon found |
| `dsc_raise_dead_regiment_columns` | `GFX_decision_dsc_raise_dead_regiment_columns` | Existing icon found |
| `nrf_raise_icebound_marines` | `GFX_decision_nrf_raise_icebound_marines` | Existing icon found |
| `ard_mobilize_signature_forces` | `GFX_decision_ard_mobilize_signature_forces` | Existing icon found |
| `ard_push_extreme_route` | `GFX_decision_ard_push_extreme_route` | Existing icon found |
| `cfr_survey_unfinished_sites` | `GFX_decision_cfr_survey_unfinished_sites` | Existing icon found |
| `cfr_issue_reconstruction_contracts` | `GFX_decision_cfr_issue_reconstruction_contracts` | Existing icon found |
| `mfr_audit_arsenal_orders` | `GFX_decision_mfr_audit_arsenal_orders` | Existing icon found |
| `mfr_convert_depots_to_arms_lines` | `GFX_decision_mfr_convert_depots_to_arms_lines` | Existing icon found |

## Localisation and reward mismatch list

- Updated `cfr_survey_unfinished_sites_tt` to mention rail-link reopening.
- Updated `cfr_issue_reconstruction_contracts_tt` to mention route-gated extra civilian build site.
- Updated `mfr_audit_arsenal_orders_tt` to mention support equipment.
- Updated `mfr_convert_depots_to_arms_lines_tt` to mention factory guard manpower.
- Updated `pra_mobilize_station_guard_tt` and `PRA_armored_train_directorate_desc` to mention rail supply yards and motor pools.
- Updated `dsc_raise_dead_regiment_columns_tt` and `DSC_dead_regiment_columns_desc` to mention rifle/artillery stores and fortified roll-call posts.
- Updated `nrf_raise_icebound_marines_tt` and `NRF_northern_revenant_fleet_desc` to mention convoy stores, coastal fortification, and dockyards.
- Updated `ard_mobilize_signature_forces_tt` and `ard_push_extreme_route_tt` to match the new naval/coastal rewards.

## AI behavior gaps

- Existing `ai_will_do` blocks already prefer war, high chaos, low stability, Soviet pressure, depot vulnerability, or route flags for the touched decisions/focuses.
- This patch did not add new AI strategy plans or route-wide AI strategy files. Remaining gap: broader route-aware AI could better distinguish moderate port survival from extreme naval expansion, but that is outside this safe patch.

## High-priority fixes first

1. Made the repeated custom decisions for PRA/DSC/NRF/ARD pay out concept-specific map/equipment effects instead of only variable or generic mobilization effects.
2. Made CFR/MFR existing decisions branch-sensitive so their construction/arsenal identities are more visible after their existing route flags.
3. Updated localisation for every changed visible effect.

## Changed focus ids

- `PRA_armored_train_directorate`
- `DSC_dead_regiment_columns`
- `NRF_northern_revenant_fleet`
- `ARD_arctic_port_endurance`

## Changed decision ids

- `cfr_survey_unfinished_sites`
- `cfr_issue_reconstruction_contracts`
- `mfr_audit_arsenal_orders`
- `mfr_convert_depots_to_arms_lines`
- `pra_mobilize_station_guard`
- `dsc_raise_dead_regiment_columns`
- `nrf_raise_icebound_marines`
- `ard_mobilize_signature_forces`
- `ard_push_extreme_route`

## Route behavior before and after

- Before: several concept countries already had thematic names and variables, but high-impact actions often collapsed into generic equipment, manpower, or abstract helper rewards.
- After: railway, dead-regiment, civilian construction, arsenal, and northern naval identities now place visible buildings, stores, manpower, or dockyard/port defenses in controlled states through existing focus and decision surfaces.

## Validation run

- Consulted required offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding.
- Consulted vanilla documentation: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, and `script_concept_documentation.md`.
- Inspected vanilla focus/decision precedents for `add_building_construction`, `add_extra_state_shared_building_slots`, `add_equipment_to_stockpile`, `add_manpower`, `build_railway`, and AI weights.
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt common/decisions/005_soviet_collapse_decisions.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml` passed.
- Brace-balance scan passed for the two edited Clausewitz files.
- Unsupported operator scan passed for the two edited Clausewitz files: no `<=` or `>=`.
- Indentation scan found zero space-indented script lines in the two edited Clausewitz files.
- Localisation BOM check passed for `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`.
- Localisation key count check found one copy of each changed tooltip key.
- Icon reference check found every touched focus/decision icon id.

## Skipped validation and why

- No full HOI4 runtime validation was run from this subagent environment.
- No broader scripted helper validation was run because scripted effects/triggers/constants were deliberately left untouched per parent scope.

## Remaining route risks

- `common/ideas/005_soviet_collapse_ideas.txt` appears dirty from prior work and was not changed here; any pre-existing idea syntax issues remain outside this patch.
- The worktree contains broad pre-existing Soviet Collapse changes, including changes in the same files. Review should compare the listed ids rather than treating the entire file diff as this patch.
- CFR/MFR would benefit from a later focused pass in `005_soviet_collapse_factory_successors.txt` if the parent expands scope.
- A route-wide AI strategy pass could make high-chaos naval and railway successors more deliberate, but current local `ai_will_do` behavior remains consistent with existing patterns.

## Plan handoff

No improvement plan was written. The observed gaps are suitable for a later bounded parent task rather than a new route-family redesign.
