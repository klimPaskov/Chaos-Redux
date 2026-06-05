# Event 006 Decision/GUI Audit Handoff

Date: 2026-06-05
Role: `chaosx_decision_mission_auditor`
Scope: bounded decision-category and scripted-GUI sidecar audit for Event 006 Independence Wave.

## Changed files

- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_event006_decision_gui_audit_handoff.md`

No gameplay, localisation, scripted GUI, scripted effect, scripted trigger, interface, or asset files were patched. The gap is broad enough that a small gameplay patch would leave the non-negotiable materially unresolved.

## Required references read

- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, Scripted GUI modding.
- Vanilla docs: `documentation/script_concept_documentation.md`, `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/modifiers_documentation.md`, `common/scripted_guis/_documentation.md`.
- Vanilla precedents checked: category-embedded scripted GUIs in `common/scripted_guis/*_scripted_gui.txt`, decision category `scripted_gui = ...` call sites, vanilla decision cost/AI/tooltip patterns.

## Identifiers audited

- Decision categories:
  - `independence_wave_host_aftermath_category`
  - `independence_wave_committee_survival_category`
  - `independence_wave_new_states_congress_category`
  - `independence_wave_patron_ledger_category`
  - `independence_wave_patronage_recognition_category`
  - `independence_wave_formation_ledger_category`
  - `independence_wave_border_commission_category`
  - `independence_wave_sealed_dossier_category`
- Scripted GUI definitions:
  - `independence_wave_dossier_board_scripted_gui`
  - `independence_wave_congress_board_scripted_gui`
  - `independence_wave_patron_ledger_scripted_gui`
  - `independence_wave_formation_ledger_scripted_gui`
  - `independence_wave_border_commission_scripted_gui`
- Scripted GUI containers:
  - `independence_wave_dossier_board_container`
  - `independence_wave_congress_board_container`
  - `independence_wave_patron_ledger_container`
  - `independence_wave_formation_ledger_container`
  - `independence_wave_border_commission_container`
- Decision/mission entries parsed: 186.

## Audit result

The scripted GUI files currently contain no clickable GUI buttons:

- `interface/006_independence_wave_scripted_gui.gui` has zero `buttonType` blocks.
- `common/scripted_guis/006_independence_wave_scripted_guis.txt` has no `effects = { ... }`, click handlers, `triggers = { ... }`, or `ai_weights = { ... }`.
- Every GUI is `context_type = decision_category`, display-only, and `ai_enabled = { always = no }`. This is acceptable only because AI behavior is represented by the underlying decisions, not GUI clicks.

Decision-surface strengths:

- All 186 parsed decision/mission entries have localisation name and desc keys.
- All non-mission decisions have a `cost = ...`.
- All AI-usable non-mission decisions have `ai_will_do`.
- No non-mission decision is missing both cost and AI.
- No direct `<=` or `>=` operators were found in the audited script/localisation/interface files.
- Braces balance in the audited script and GUI files.
- `localisation/english/006_independence_wave_l_english.yml` is UTF-8 with BOM and has no `:0` keys.
- Event 005 references in the audited implementation are origin-safety blockers only, notably `has_independence_wave_soviet_collapse_runtime_state`, not focus/formable wiring.

Blocking gap:

- 89 decision/mission entries expose requirements through plain `available`, `target_trigger`, `target_root_trigger`, or `custom_cost_trigger` without a `custom_trigger_tooltip`.
- 5 early clickable decisions use inline effects without a dedicated scripted helper or effect-feedback tooltip:
  - `independence_wave_recognize_the_loss`
  - `independence_wave_invite_observers`
  - `independence_wave_request_recognition`
  - `independence_wave_seize_depot_inventory`
  - `independence_wave_send_delegates_to_congress`
- Many targeted decisions have real costs and AI behavior but lack missing-requirement localisation. Examples include:
  - Host target decisions: `independence_wave_offer_local_autonomy`, `independence_wave_arrest_committee_couriers`, `independence_wave_arm_loyalist_councils`
  - Patronage target decisions: `independence_wave_major_supply_rifles`, `independence_wave_major_offer_military_mission`, `independence_wave_major_demand_cabinet_seats`, `independence_wave_major_sabotage_rival_patron`
  - Congress target decisions: `independence_wave_sign_mutual_guarantee`, `independence_wave_recognize_impossible_delegate`, `independence_wave_bind_strange_cooperation`, `independence_wave_send_congress_volunteer_cadre`
  - Border target decisions: `independence_wave_petition_border_parish`, `independence_wave_request_league_arbitration`, `independence_wave_offer_protected_transfer`, `independence_wave_issue_dossier_ultimatum`, `independence_wave_freeze_claim_under_observers`

Conclusion: the implementation is structurally present, but it does not yet satisfy the non-negotiable that every decision/GUI button has real costs, tooltips, AI equivalent/behavior where AI-usable, cleanup, and scripted helper logic.

## Validation run

- `rg --files paradox_wiki | rg 'Data structures|Triggers|Effects|Modifiers|Localisation|Scopes|On actions|Event modding|Decision modding|Idea modding|AI modding|Interface Modding|Scripted GUI'`
- Opened/read offline wiki pages listed above.
- Opened/read vanilla documentation listed above.
- `rg -n "scripted_gui\\s*=|context_type = decision_category|ai_enabled|ai_will_do|cost =" "$HOME/projects/Hearts of Iron IV/common/decisions" "$HOME/projects/Hearts of Iron IV/common/decisions/categories" "$HOME/projects/Hearts of Iron IV/common/scripted_guis"`
- Parsed `common/decisions/006_independence_wave_decisions.txt`: 186 decision/mission entries.
- Checked GUI buttons: zero `buttonType` blocks.
- Checked Event 005 references in scoped files.
- Checked unsupported operators: no `<=` or `>=` found.
- Checked brace deltas: all audited script/GUI files returned `brace_delta=0`.
- Checked localisation encoding: `006_independence_wave_l_english.yml` has UTF-8 BOM.
- Checked localisation key style: no `:0` keys found.

Skipped:

- No live game validation. Per project instructions, the parent/user owns live-session verification.
- No gameplay patch validation, because no gameplay patch was applied.

## Remaining risks

- Tooltip gap is broad and player-facing: raw target/availability triggers may leak or obscure requirements.
- Early aftermath/congress decisions still use inline `complete_effect` logic, making future cleanup and audit harder.
- Scripted GUI panels are display-only. If the parent later adds actual GUI buttons to these containers, each click needs cost, requirement tooltip, effect helper, AI equivalent if AI-usable, and cleanup before completion can be claimed.
- Event 005 separation looks correct in this surface, but parent should keep origin checks in all future Event 006 focus/formable/package edits.

## Exact next parent actions

1. Create a narrow patch tranche for the 5 inline-effect decisions:
   - Add scripted helpers in `common/scripted_effects/006_independence_wave_effects.txt`.
   - Replace inline `complete_effect` blocks in `common/decisions/006_independence_wave_decisions.txt` with helper calls.
   - Add effect-feedback localisation keys in `localisation/english/006_independence_wave_l_english.yml`.
2. Create a tooltip tranche for targeted decisions:
   - Wrap target requirements in `custom_trigger_tooltip` where supported.
   - Add concise requirement localisation for host, patronage, congress, compact, and border target decisions.
   - Keep raw checks inside existing scripted triggers; do not duplicate full trigger logic in decisions.
3. Create a formation-ledger tooltip tranche:
   - Add missing requirement tooltips for opener/map/register decisions that currently use only direct `available = { can_* = yes }`.
   - Reuse existing `*_requirements_tt` keys where present before adding new keys.
4. Re-run the same parser/audit checks and require:
   - zero non-mission decisions without cost
   - zero AI-usable non-mission decisions without `ai_will_do`
   - zero available/targeted decision entries without a custom requirement tooltip or intentionally hidden, documented reason
   - zero clickable decisions without a scripted helper or explicit effect feedback
5. Do not wire Event 005 focus trees, formables, route flags, republic missions, or event-log state into Event 006 releases. Keep Event 005 references limited to origin-safety blockers.

## Skills used

- `hoi4-decisions-missions`
- `chaos-redux-subagents`
