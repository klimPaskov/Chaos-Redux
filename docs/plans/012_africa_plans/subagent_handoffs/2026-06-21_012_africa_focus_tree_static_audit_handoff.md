# Event 012 Africa Focus Tree Static Audit Handoff

Date: 2026-06-21
Mode: focus-tree subagent audit, report-only
Scope: Event 012 Africa focus trees and focus-tree loading only

## Result

No gameplay, localisation, or GFX patch was made. The current Event 012 focus implementation is not a vertical reward ladder: it has one large Africa unifier tree plus two loaded created-country trees, with route locks, focus filters, hidden high-chaos refresh, varied rewards, and decision/scripted-helper integration.

Changed files:

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-21_012_africa_focus_tree_static_audit_handoff.md`

Unchanged audited implementation files:

- `common/national_focus/012_africa_focus.txt`
- `common/national_focus/012_africa_authority_focus.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/ai_strategy/012_africa.txt`
- `interface/012_africa.gfx`
- `localisation/english/012_african_union_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`

Changed focus ids: none.

Route behavior before/after: unchanged.

Localisation keys and icon ids changed: none.

## Route Coverage Table

| Required route surface | Evidence | Static audit result |
|---|---|---|
| Opening trunk / mandate | `africa_is_one_focus_tree` starts at `AFR_the_charter_mandate`, `AFR_continental_congress`, `AFR_liberation_war_office`, `AFR_authority_atlas` in `common/national_focus/012_africa_focus.txt:22`, `:34`, `:51`, `:68`, `:85`. | Covered. The tree fans out immediately into war office, Authority Atlas, industry, RSA, regional authority, and later political routes. |
| RSA emergency / failure-state branch | `AFR_rsa_congress_underground` through `AFR_rsa_victory_settlement` starts at `common/national_focus/012_africa_focus.txt:104`; supporting RSA emergency decisions are in `common/decisions/012_africa_decisions.txt` after `africa_rsa_civil_war_emergency_category`. | Covered as a focus subtree plus decision category. |
| Industry / logistics | `AFR_industrial_convergence`, rail/lake/foundry followups begin at `common/national_focus/012_africa_focus.txt:229`. | Covered. Rewards include construction, equipment, and core value changes rather than repeated PP only. |
| Regional authority / League / diplomacy | `AFR_regional_authority_charters` at `common/national_focus/012_africa_focus.txt:253`; created authority tree `africa_regional_authority_focus_tree` and `AFR_AUTH_charter_seat` at `common/national_focus/012_africa_authority_focus.txt:14`, `:26`; loading helper at `common/scripted_effects/012_africa_effects.txt:4164`. | Covered. Regional created-country focus tree exists and is loaded only by the setup helper. |
| Authority Atlas / Archive | `AFR_authority_atlas`, `AFR_dossier_selection_office`, and dossier lane start points at `common/national_focus/012_africa_focus.txt:85`, `:333`; decision/helper hooks reference `africa_dossier_selection_office_open` in `common/decisions/012_africa_decisions.txt:2243` and `common/scripted_effects/012_africa_effects.txt:8851`. | Covered. Dossier depth is mostly decisions/helpers, not only focus nodes. |
| Diaspora | `AFR_return_offices` branch starts at `common/national_focus/012_africa_focus.txt:798`; AI posture exists at `common/ai_strategy/012_africa.txt:452`. | Covered. |
| Military / Scramble response | `AFR_charter_general_staff`, `AFR_liberation_columns`, `AFR_scramble_reverse_claims` around `common/national_focus/012_africa_focus.txt:955`; route AI exists at `common/ai_strategy/012_africa.txt:284`, `:315`. | Covered. |
| Political route split | Federal, sovereign seats, peoples, general staff, crown, and high-chaos door route ids at `common/national_focus/012_africa_focus.txt:1083`, `:1254`, `:1345`, `:1438`, `:1542`; route AI at `common/ai_strategy/012_africa.txt:346`, `:372`, `:398`, `:424`. | Covered. The implementation has an additional sovereign-seats route beside the spec's core political families. |
| High-chaos / Bestiary | `AFR_high_chaos_door` at `common/national_focus/012_africa_focus.txt:1542` sets `africa_high_chaos_branch_revealed` and calls `mark_focus_tree_layout_dirty` at `:1572`-`:1573`; hidden children use `allow_branch` at `:1870` and later; created bestiary tree starts at `common/national_focus/012_africa_authority_focus.txt:735`, `:747`; load helper at `common/scripted_effects/012_africa_effects.txt:4192`. | Covered. Hidden route reveal uses the required layout refresh pattern. |
| Post-unification / sponsor / world order | `AFR_africa_is_one` at `common/national_focus/012_africa_focus.txt:2086`; world-order branch from `AFR_continental_export_office` through `AFR_the_world_is_one` at `:2123`-`:2300`; sponsor decisions and proof chain in `common/decisions/012_africa_decisions.txt:4970` onward; gate trigger at `common/scripted_triggers/012_africa_triggers.txt:2436` and `:2483`. | Covered. Static gates are strict; live validation remains needed. |
| World Is One terminal | `AFR_the_world_is_one` available gate uses `can_africa_start_world_is_one_gate` at `common/national_focus/012_africa_focus.txt:2306`; terminal effect is `africa_mark_world_is_one_gate_ready` in `common/scripted_effects/012_africa_effects.txt:9503`. | Covered by focus + decision proof gate, not a bare focus completion. |

## Missing Or Simplified Content

High priority first:

1. No blocking route-family omission found in the focus files. The implemented focus count is 157 total: 108 in `common/national_focus/012_africa_focus.txt` and 49 in `common/national_focus/012_africa_authority_focus.txt`.
2. `AFR_continent_sponsor_office` is a pre-`AFR_africa_is_one` preparatory focus at `common/national_focus/012_africa_focus.txt:2064`; the actual sponsor readiness mission and export branch are gated after `africa_is_one_complete` in `common/decisions/012_africa_decisions.txt:4970` and `common/national_focus/012_africa_focus.txt:2123`. This is coherent, but if the parent design requires the sponsor office itself to be invisible until after `AFR_africa_is_one`, that is a design-level route layout change and was not patched here.
3. Expansion is mostly represented by Scramble/claim/integration decisions and helper systems rather than focus-only direct war goals or cores. This matches the current architecture, but live scenario validation should verify the focus route consistently exposes those decision surfaces.
4. Idea lifecycle is not primarily focus-local. Focus/setup effects add package ideas, while cleanup/lifecycle work is in scripted effects and decisions. No focus-local orphan promise was found, but this audit did not revalidate the whole idea lifecycle outside the focus-loading surface.

## Icon Coverage Table

| Icon surface | Evidence | Result |
|---|---|---|
| Custom focus filters | `FOCUS_FILTER_AFR_CHARTER` through `FOCUS_FILTER_AFR_WORLD_ORDER` in `common/national_focus/012_africa_focus.txt:14`-`:18`; sprites in `interface/012_africa.gfx:19`-`:23`; localisation in `localisation/english/chaosx_gui_l_english.yml:1002`-`:1006`. | Covered. |
| Custom goal icons | 13 distinct `GFX_goal_africa_*` icons used by focuses; all have sprite definitions and `_shine` definitions in `interface/012_africa.gfx:71`-`:96`. | Covered. |
| Texture presence | Static texture reference check over `interface/012_africa.gfx` found 89 texture refs and no missing files. | Covered. |
| Repeated icon use | Repeated by theme, especially high-chaos and world-order capstones. | Acceptable; no missing or obviously wrong icon reference found. |

## Localisation And Reward Mismatch List

- No missing focus name/description keys were found for focus ids in `common/national_focus/012_africa_focus.txt` or `common/national_focus/012_africa_authority_focus.txt` against `localisation/english/012_african_union_l_english.yml`.
- No missing custom focus filter localisation was found; keys are in `localisation/english/chaosx_gui_l_english.yml:1002`-`:1006`.
- No obvious focus name/reward mismatch was found in sampled route anchors: political routes set route flags, Authority Atlas focuses open dossier surfaces, high-chaos focuses reveal/use bestiary package state, and world-order focuses open sponsor/proof gates.
- Reward variety is present. Static counts across the two focus files include 287 `add_to_variable`, 31 `add_building_construction`, 37 `add_equipment_to_stockpile`, 13 `add_manpower`, 11 `add_stability`, 164 `set_country_flag`, 8 `set_cosmetic_tag`, and 1 `mark_focus_tree_layout_dirty`.

## AI Behavior Gaps

- No static AI-routing gap was found for the focus-tree routes. `common/ai_strategy/012_africa.txt` has route-aware strategies for charter consolidation, peoples liberation, continental general staff, federal charter, sovereign seats, crown congress, high-chaos covenant, diaspora, world-order sponsor, Authority Atlas, regional authorities, and high-chaos actors at lines `71`, `284`, `315`, `346`, `372`, `398`, `424`, `452`, `478`, `526`, `1074`, and `1214`.
- Focus-level `ai_will_do` weights are present throughout the route anchors and use route/state flags in several convergence focuses.
- Remaining risk is balance/runtime, not static wiring: AI must still be observed in a live scenario to confirm it does not over-prioritise early sponsor setup, stall on decision-gated World Is One prerequisites, or choose invalid cross-continent proof decisions.

## Focus Loading

- Main unifier tree load: `load_focus_tree = { tree = africa_is_one_focus_tree keep_completed = no }` in `common/scripted_effects/012_africa_effects.txt:4891`.
- Regional authority created-country tree load: `load_focus_tree = { tree = africa_regional_authority_focus_tree keep_completed = no }` in `common/scripted_effects/012_africa_effects.txt:4164`.
- High-chaos created-actor tree load: `load_focus_tree = { tree = africa_high_chaos_actor_focus_tree keep_completed = no }` in `common/scripted_effects/012_africa_effects.txt:4192`.
- No other Event 012 focus-tree load calls were found in the audited scope.

## Meaningful Validation

- Read required repo instructions, focus-tree/events/decisions/assets/improvement/subagent skills, relevant offline Paradox wiki pages, vanilla focus examples/docs, and Event 012 specs including `docs/specs/012_africa_specs/prompts/012_africa_coding_prompt.md`.
- Checked focus tree shape and route anchors against the Event 012 coding prompt, focus tree plan, focus architecture graph, AI strategy matrix, high-chaos specs, and acceptance matrix.
- Checked brace balance for `common/national_focus/012_africa_focus.txt`, `common/national_focus/012_africa_authority_focus.txt`, and `common/scripted_effects/012_africa_effects.txt`; all reported balance `0`.
- Checked focus localisation key presence for all Event 012 focus ids; no missing focus names/descriptions found.
- Checked custom goal icon definitions and `_shine` definitions for all used `GFX_goal_africa_*` icons; none missing.
- Checked texturefile paths referenced by `interface/012_africa.gfx`; none missing.
- Checked focus loading calls and hidden high-chaos branch reveal/layout refresh.

Skipped meaningful validation:

- No live HOI4 scenario validation was run. This audit is static and cannot prove AI route sequencing, decision visibility after focus completion, or World Is One terminal behavior in an active run.

## Remaining Route Risks

- Live validation should specifically test: unifier startup focus replacement, regional authority load, bestiary actor load, high-chaos branch reveal after `AFR_high_chaos_door`, `AFR_africa_is_one` availability after dossier/regional/living-core gates, sponsor readiness after Africa Is One, and `AFR_the_world_is_one` after all proof decisions.
- If parent design wants the sponsor office itself to be strictly post-unification, move or additionally gate `AFR_continent_sponsor_office`; this is a route-design decision, not a small prerequisite typo.
- Broader country-package consequence depth, GUI/animation render proof, and full event completion validation remain outside this focus-tree-only audit.
