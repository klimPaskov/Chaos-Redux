# Event 006 IW-101/IW-102/IW-105 COG Cosmetic Overlay Adapter Handoff

Status: PARTIAL bounded source adapter. This handoff is not package admission, selectable-release admission, or live-runtime proof.

## Accepted vanilla identity contract

- Carrier remains the vanilla `COG` tag and its existing history, cores, leaders, flags, and focus tree remain authoritative.
- Vanilla `common/national_focus/congo.txt` keeps the three route branches under `COG_assemble_a_regency_council`. Their `allow_branch` gates require the Gotterdammerung DLC and the exact flags `COG_kingdom_of_kongo_flag`, `COG_kingdom_of_kuba_flag`, or `COG_kingdom_of_loango_flag`.
- The matching completion rewards set the exact cosmetic identities `COG_kingdom_of_kongo`, `COG_kingdom_of_kuba`, and `COG_kingdom_of_loango`. Vanilla `events/WUW_Congo.txt` sets the three country flags before the branches become available.
- State 538 is the current-map COG anchor contract used by the bounded adapters (`history/states/538-Cameroun.txt` is the vanilla state record and is not overwritten). No state transfer, new tag, history file, flag, portrait, advisor asset, or focus replacement is introduced.
- The three identities are mutually exclusive in the vanilla route. Each adapter therefore requires `original_tag = COG`, its exact cosmetic tag, and its exact country flag before initialization.

## Implemented source surfaces

- `common/script_constants/006_independence_wave_iw101_iw102_iw105_cog_overlays_constants.txt` centralizes route values, costs, guard timing, and AI weights.
- `common/scripted_triggers/006_independence_wave_iw101_iw102_iw105_cog_overlays_triggers.txt` defines exact identity gates, state-538 control/objective checks, payment checks, and charter thresholds.
- `common/scripted_effects/006_independence_wave_iw101_iw102_iw105_cog_overlays_effects.txt` supplies initialization, suspension/resume, value updates, lifecycle ideas, five costed actions per route, and timed mission success/failure. Force integration starts the timed guard mission so the fifth action is reachable; the mission pays concrete command, manpower, equipment, and experience costs.
- `common/on_actions/006_independence_wave_iw101_iw102_iw105_cog_overlays_on_actions.txt` owns one shared `on_daily_COG` carrier hook and calls all three identity-gated refresh effects, avoiding duplicate carrier definitions.
- `common/ideas/006_independence_wave_iw101_iw102_iw105_cog_overlays_ideas.txt` provides four lifecycle ideas for each identity: contested, integrated force, civic/council compact, and final charter.
- `common/decisions/categories/006_independence_wave_iw101_iw102_iw105_cog_overlays_categories.txt` and `common/decisions/006_independence_wave_iw101_iw102_iw105_cog_overlays_decisions.txt` expose route-specific government, depot, force, timed guard, and charter actions with concrete costs and static AI weights.
- `localisation/english/006_independence_wave_iw101_iw102_iw105_cog_overlays_l_english.yml` localizes every category, decision, mission, tooltip, cost, idea, and lifecycle description in UTF-8 with BOM.

## Route-specific values and action meaning

| Route | Visible values | Anchor and force identity | Action sequence |
| --- | --- | --- | --- |
| IW-101 Kongo | River Logistics, Regency Legitimacy, Veteran Integration | State 538; river/jungle profile | Convene Kongo Regency, secure river depots, integrate Kongo veterans, hold river corridor, establish Kongo Assembly |
| IW-102 Kuba | Forest Mobility, Royal Council Legitimacy, Territorial Stewardship | State 538; river/jungle profile | Convene Kuba Council, secure forest depots, integrate forest guard, hold forest anchor, charter Kuba Council |
| IW-105 Loango | Coastal Logistics, Regency Legitimacy, Port Security | State 538; coastal/maritime profile | Convene Loango Regency, secure port depots, integrate port authority, hold port guard, charter Loango Coastal Council |

Values change on every completion and guard outcome. Ideas are refreshed from the current lifecycle flags and thresholded values. Failed or interrupted guards reset their hold ledger and apply the shared stability/legitimacy penalty; suspended routes remove their Event 006 ideas without destroying vanilla identity.

## Validation evidence

- `hoi4.probability_inspect` with `decision_ai_will_do` on the decisions source: `PROBABILITY_SOURCE_INSPECTED`, 12 weighted candidates, zero unresolved inputs, `poolComplete=false` because world-state eligibility is intentionally runtime-dependent.
- `hoi4.probability_inspect` with `mission_ai_will_do` on the same source: `PROBABILITY_SOURCE_INSPECTED`, three mission candidates, zero unresolved inputs, `poolComplete=false` for the same reason.
- Static brace/quote and unsupported-operator checks pass for all new Clausewitz files; the localisation file begins with the UTF-8 BOM.

## Remaining boundary

The adapters do not claim a complete Event 006 country package, meaningful-tree insertion, network/league/patron integration, formable surface, historical-symbol package, portrait clearance, save/load proof, host-survival proof, or live AI/balance/scenario evidence. The next exact route-overlay work remains IW-156, IW-196, IW-197, and IW-204.
