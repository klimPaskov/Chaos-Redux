# Event 011 decision and mission audit patch handoff

Scope: Event 011 Secret Alliance decisions, missions, decision costs, AI hints, mission timers, and local tooltip clarity.

## Files changed

- `common/decisions/011_secret_alliance_decisions.txt`
- `common/script_constants/011_secret_alliance_constants.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
- `common/scripted_guis/011_secret_alliance_dossier_board_scripted_gui.txt`
- `localisation/english/011_anti_player_pact_l_english.yml`

## Changed surfaces and ids

- Timed missions:
  - `guard_capital_network_mission`
  - `secure_industrial_belt_mission`
  - `keep_foreign_route_watched_mission`
  - `expose_patron_hand_mission`
  - `hold_border_public_crisis_mission`
- Decisions with AI PP saving hints:
  - `turn_courier`
  - `audit_foreign_missions`
  - `build_public_dossier`
  - `secure_capital_ministries`
  - `quiet_talks_member`
  - `face_saving_exit`
  - `pressure_neutrals`
  - `rally_friendly_governments`
  - `prepare_public_war_case`
- Decisions with dynamic random seed:
  - `trace_diplomatic_pouches`
  - `turn_courier`
  - `break_radio_net`
  - `audit_foreign_missions`
  - `quiet_talks_member`
  - `face_saving_exit`
  - `controlled_leak`
  - `sweep_frontier_safehouses`
  - `limited_border_reprisal`
- Trigger:
  - `can_pay_secret_alliance_courier_pass_cost`
- Scripted GUI visibility triggers:
  - `secret_alliance_thread_glow_visible`
  - `secret_alliance_radio_pulse_visible`
  - `secret_alliance_seal_crack_visible`
  - `secret_alliance_border_warning_visible`
- Localisation keys:
  - `secret_alliance_*_cost_text`
  - `secret_alliance_*_cost_text_blocked`

## Before and after behavior

Before:

- The five missions used 45, 60, 55, 75, and 50 day timers, below the normal medium mission band and too short for action-based defense objectives.
- The missions used failure-style `available` triggers but had `is_good = no`, so the mission UI could present failure conditions like normal completion conditions.
- PP-spending custom-cost decisions had no `ai_hint_pp_cost`, so target AI was not told to save PP for those decisions.
- Repeatable decisions with random outcomes used the default fixed decision random seed, making repeated outcomes more predictable.
- `seal_courier_pass` could appear and be paid without a neighboring hidden member.
- Dossier Board icon visibility triggers did not match the actual GUI element names, so radio pulse, thread glow, seal crack, and border warning visibility was not being controlled by the scripted GUI.
- Cost text was generic and did not show concrete values or blocked-cost variants.

After:

- Mission timers are now 90, 120, 105, 150, and 120 days, mirrored between file-scoped decision constants and `secret_alliance_mission` tuning constants.
- Failure-style missions use `is_good = yes` for clearer failure tooltip labeling while preserving the existing effect semantics.
- PP-spending custom-cost decisions have matching `ai_hint_pp_cost` values.
- Random-outcome decisions use `fixed_random_seed = no`.
- `seal_courier_pass` requires a neighboring hidden member in visibility and cost validation.
- Dossier Board icon visibility triggers now match the actual GUI element names and include a high-evidence gate for the seal crack.
- Cost text is icon-first, numeric, and has `_blocked` variants for all Event 011 custom costs.

## Why this is safe and bounded

The patch does not redesign Event 011, add new decisions, add new event chains, or change member selection. It only adjusts existing Event 011 decision and mission tuning, UI clarity, a missing local target gate, and mismatched scripted-GUI trigger ids.

## Validation run

- `rg -n "<=|>="` across Event 011 decision, trigger, effect, constant, scripted GUI, GUI, and localisation files: no matches.
- Mission timer and `is_good` scan confirmed the five mission timers and tooltip-direction changes are present.
- Custom-cost localisation scan confirmed every `custom_cost_text` key in `common/decisions/011_secret_alliance_decisions.txt` has a base and `_blocked` key in `localisation/english/011_anti_player_pact_l_english.yml`.
- Brace-balance check across touched script and GUI files reported balanced braces:
  - decisions: 273 pairs
  - triggers: 107 pairs
  - effects: 641 pairs
  - constants: 10 pairs
  - scripted GUI: 11 pairs
  - GUI: 22 pairs
- Scripted-GUI trigger scan confirmed visibility trigger ids now match `secret_alliance_radio_pulse`, `secret_alliance_thread_glow`, `secret_alliance_seal_crack`, and `secret_alliance_border_warning`.

## Skipped validation

- No in-game launch or HOI4 error-log validation was run from this subagent pass. The repo contains many pre-existing untracked Event 011 files and unrelated dirty tracked files, so this pass kept validation to scoped text and structural checks.
- No visual GUI screenshot validation was run because the patch only renamed scripted-GUI trigger ids and did not alter GUI layout or sprites.

## Remaining issues

- The missions still use broad country-level checks such as `num_divisions` and equipment/fuel totals instead of named state, route, port, rail, or supplied-division objectives. That is a design-quality gap, not fixed here because a proper state-group implementation would be broader than a local audit patch.
- The Dossier Board is a readout surface, not an interactive board with member cards or GUI buttons. Existing decisions provide the gameplay surface, but the scripted GUI is thinner than the spec direction.
- There is no robust central cleanup helper for invalid targets, invalid members, stale arrays, stale mission flags, obsolete ideas, or public-pact collapse. Existing success/failure effects clear their own mission flags, but lifecycle cleanup remains incomplete.
- Public reveal and war logic still use whole-country loops over member flags. They are not on-action world scans, but stale member flags can make those loops unsafe without cleanup.
