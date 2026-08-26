# Event 016 D’Rhondan contact and landing decision audit — 2026-08-26

Status: audited and locally patched for player-facing requirement clarity; no gameplay tuning, AI weight, random weight, event, or dedicated GUI implementation was changed. The parent agent must review this handoff and the concurrent localisation edits before claiming the larger Event 016 work complete. No commit was created.

## Scope and source boundary

The reviewed decision-owned surfaces are `common/decisions/016_alien_infantry_landing_decisions.txt`, `common/decisions/016_dhrondan_contact_decisions.txt`, `common/decisions/categories/016_alien_infantry_landing_category.txt`, `common/decisions/categories/016_dhrondan_contact_category.txt`, `common/scripted_effects/016_dhrondan_contact_effects.txt`, `common/scripted_triggers/016_dhrondan_contact_triggers.txt`, `common/script_constants/016_dhrondan_contact_constants.txt`, `localisation/english/016_alien_infantry_api_l_english.yml`, and `localisation/english/016_dhrondan_contact_l_english.yml`.

The accepted contract was checked against `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md`, `docs/plans/016_brilliant_scientist_plans/016_alien_dhrondan_acceptance_scenarios.md`, and `docs/events/016_brilliant_scientist/systems/dhrondan_contact.md`.

Required repository guidance was read before source inspection, including `AGENTS.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.

The required offline Paradox wiki pages and relevant vanilla documentation were consulted for decision targeting, mission activation and timeout behavior, custom costs, triggers, effects, localisation, script constants, scopes, and text icons.

## Issue list sorted by severity

### P0/P1 — confirmed parser or runtime defects

None found in the reviewed source. The state-target syntax, mission `activation`/`available` contract, variable timeout syntax, script-constant references, custom costs, and effect scopes match the inspected wiki, documentation, and vanilla precedents.

### P2 — confirmed gameplay or balance defects

None found in the reviewed source. The accepted 2,000-equipment/7-day/one-pending landing contract, 30-day recovery default, 180-day/50 Political Power/500 fuel expedition contract, 75 Political Power/−10 strain/180-day Accord contract, exactly-once contact/pact guards, and six-arrival/30-strain/600-Chaos rebellion gate are present.

### P2 — unresolved engine evidence

The mandatory current `hoi4.gui_inspect` and `hoi4.gui_render` calls for `countrydecisionview` using workspace `mod_chaos_redux_ea3b2d67c2c0` and Event 016 scenarios both timed out after 180 seconds with `timed out awaiting tools/call after 180s`. No current GUI artifact or parser diagnostic exists for this surface.

The mandatory current `hoi4.probability_inspect` calls for the Event 016 decision source and mission adapter also timed out after 180 seconds after the initial invalid `relativePath` input was rejected with `Unrecognized key: "relativePath" at source`. The named custom `chaosx_ai_probability_auditor` route is not callable in this runtime, so no current same-scenario compare was run and AI conclusions remain source-backed or previously partial rather than certified.

### P3 — fixed in this pass

The four decision availability blocks exposed bare scripted helpers without a dedicated reason key. A blocked button could therefore fall back to raw scripted-trigger text or an unresolved key. Each helper is now wrapped in `custom_trigger_tooltip` with a concise localisation key while retaining the exact helper as the hidden trigger, so this patch does not change eligibility or costs.

### P3 — remaining review notes

The concurrent edit in `localisation/english/016_dhrondan_contact_l_english.yml:27` describes the medium rebellion tier without explicitly repeating that the 40% high tier takes precedence. The resolver already checks high before medium, but the player-facing line should retain wording such as “unless the high tier applies” for unambiguous comprehension. I did not rewrite that line because another agent currently owns the dynamic-constant localisation edit.

The D’Rhondan expedition and Accord descriptions still spell their current 180/50/500/75/10 values directly while the gameplay source uses script constants. All spendable values have the correct text icons and currently match the constants, but a later localisation pass could convert these values to dynamic constant references to prevent future drift. No behavior depends on this wording-only recommendation.

## Applied patch

| File | Identifiers | Before | After |
| --- | --- | --- | --- |
| `common/decisions/016_alien_infantry_landing_decisions.txt:23-30` | `alien_infantry_call_landing` | `available` directly called `alien_infantry_can_call_landing` | `available` uses `alien_infantry_landing_requirements_tt` with the same helper under `hidden_trigger`. |
| `common/decisions/016_dhrondan_contact_decisions.txt:24-33` | `dhrondan_send_kruger_to_dhronda` | Route eligibility was a bare helper. | Route eligibility now uses `dhrondan_kruger_expedition_requirements_tt` with the same helper under `hidden_trigger`; the fuel tooltip and cost are unchanged. |
| `common/decisions/016_dhrondan_contact_decisions.txt:57-66` | `dhrondan_send_mengele_to_dhronda` | Route eligibility was a bare helper. | Route eligibility now uses `dhrondan_mengele_expedition_requirements_tt` with the same helper under `hidden_trigger`; the fuel tooltip and cost are unchanged. |
| `common/decisions/016_dhrondan_contact_decisions.txt:86-94` | `dhrondan_honor_accord` | Pact maintenance eligibility was a bare helper. | Eligibility now uses `dhrondan_honor_accord_requirements_tt` with the same helper under `hidden_trigger`; the 75 Political Power cost and effect are unchanged. |
| `localisation/english/016_alien_infantry_api_l_english.yml:6` | `alien_infantry_landing_requirements_tt` | No dedicated landing availability reason existed. | Added a concise contact, pending/cooldown, icon-first equipment, and target-state requirement line using the landing constants. |
| `localisation/english/016_dhrondan_contact_l_english.yml:13,16,28` | `dhrondan_kruger_expedition_requirements_tt`, `dhrondan_mengele_expedition_requirements_tt`, `dhrondan_honor_accord_requirements_tt` | No dedicated route or Accord availability reason existed. | Added concise route, character, pact, cooldown, rebellion, and resource-context lines. |

## Decision category lifecycle notes

`dhrondan_contact_category` appears after the envoy craft is completed, while a pact or expedition keeps it visible for lifecycle reporting. Its status header is an unavailable informational row that appears only after the pact and displays the two meaningful player-facing counters.

Before the pact, Kruger and Mengele authorization decisions are mutually exclusive in practice because both availability helpers reject an existing expedition or pact. During an expedition, the opposite route may remain visible but is greyed by its helper; this is at most two route rows plus one active mission and does not create a duplicate expedition.

After the pact, the Accord is the only repeatable action and the status row remains available as a compact header. The category has no dedicated scripted GUI, consistent with the accepted ordinary decision-category design.

`alien_infantry_landing_category` is contact-gated and intentionally uses `visible_when_empty = yes` so the map-targeted entry remains discoverable even when no state is currently valid. The call decision targets states with `state_target = yes` and `on_map_mode = map_and_decisions_view`, while the active mission is country-scoped and holds one saved state target.

No `on_daily`, `on_weekly`, or `on_monthly` world-iterating action appears in the reviewed files. Rebellion refresh is called by bounded country effects after pact, landing, or Accord changes.

## Cognitive-load notes

The contact category exposes a compact status header, at most two pre-pact route actions, one post-pact Accord action, and at most one expedition or rebellion mission because a shared expedition flag and one active-mission guard prevent parallel copies. The landing category exposes one state action and one active reservation mission.

Alien Presence and Pact Strain are labelled in the status row and explained in the category description. The rebellion mission description states the cadence, gate, and tier values; the concurrent medium-tier wording should still make high-tier precedence explicit as noted above.

Decision descriptions explain the expedition routes, duration, resource costs, Kruger role suspension, Mengele independence, landing reserve, and recovery ladder. The applied tooltips now explain blocked route and target requirements without exposing raw helper names.

The landing reserve, expedition resources, Accord cost, arrival gate, strain gate, Chaos gate, rebellion tiers, cooldowns, and durations all have clear mechanical significance. The only remaining clarity issue is the medium-tier precedence wording and the optional dynamic-constant hardening of D’Rhondan cost prose.

## Mission quality notes

| Mission | Owner/category | Requirement and region | Duration | Success/timeout | Failure/cancel and duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `alien_infantry_landing_mission` | Contact country / `alien_infantry_landing_category` | Pending reserve, contact, valid saved state still owned and controlled; state target is saved in `dhrondan_landing_state_id`. | `var:alien_infantry_landing_reservation_days`, seven days from the API constant. | `timeout_effect` calls `alien_infantry_spawn_landing_cohort`, which creates one locked ten-battalion cohort, records the state and counters, and applies cooldown. | Lost contact, state, or world-end invalidates the mission and `cancel_effect` calls the API refund path. One pending flag and API idempotence prevent duplicate reserves or cohorts. |
| `dhrondan_kruger_expedition_mission` | Host country / `dhrondan_contact_category` | Current host, completed craft, canonical active/uninjured/unconfined Kruger, no obligation/pact/expedition/transaction lock; country route, not a map target. | `var:dhrondan_expedition_days`, set to 180. | Timeout rechecks the route and opens one planetary-audience event; the audience option authorizes the pact once. | Route loss invokes `dhrondan_fail_expedition`, restores the obligation state, clears flags and variable, and raises one failure report. The shared expedition flag prevents a second mission. |
| `dhrondan_mengele_expedition_mission` | Mengele Directorate country / `dhrondan_contact_category` | Mengele route, completed craft, no pact or expedition, and no world end; independent of Kruger. | `var:dhrondan_expedition_days`, set to 180. | Timeout rechecks the route and opens the same bounded audience event with route-specific text. | Route loss uses the same failure cleanup without mutating Kruger measures. The shared expedition flag prevents duplicates. |
| `dhrondan_rebellion_pulse_mission` | Pact host country / `dhrondan_contact_category` | Established pact, no triggered rebellion, at least six arrivals, Pact Strain at least 30, global Chaos at least 600, and no world end; no map target. | `constant:dhrondan_contact.rebellion_pulse_days`, 90 days. | Timeout resolves high 40%, medium 20%, or low 10% in precedence order and derives no-revolt as 100 minus revolt. No revolt refreshes the same bounded mission. | Gate loss removes the mission without effects. `has_active_mission` and country scope prevent duplicate pulses, while the warning event is one-time presentation. |

## Cost and requirement clarity

The landing call has one spendable cost type: exactly 2,000 `alien_laser_weapon_equipment_1`, shown with `£GFX_alien_laser_weapon_equipment_medium` and sourced from `constant:alien_infantry_landing.reserve_equipment`.

Each expedition has two spendable cost types: native `constant:dhrondan_contact.expedition_political_power_cost` at 50 Political Power and custom fuel at `constant:dhrondan_contact.expedition_fuel_cost` at 500 fuel. The descriptions and fuel tooltip use `£pol_power` and `£fuel_texticon`; the native PP cost remains engine-visible and the AI helper debits the same values exactly once.

The Accord has one spendable cost type: native `constant:dhrondan_contact.pact_honor_political_power_cost` at 75 Political Power, shown with `£pol_power` in its description.

No gameplay-changing decision or scripted GUI action in this scope exceeds four spendable cost types. The newly added landing requirement tooltip also uses the correct laser-equipment text icon rather than a literal resource-only cost.

## AI validity and route-lock notes

Kruger and Mengele decisions use dominant source scores from `constant:dhrondan_contact_ai.dominant`; the Accord uses the low source score and a strained-state factor. The landing decision uses the standard source score and four focus-derived factors. No AI weights were changed in this pass.

The AI expedition event helper checks AI scope, both PP and fuel affordability, and at least one valid route before debiting PP, then prefers Kruger when that route is valid and otherwise tries Mengele. The visible decisions retain the same valid-route checks and native/custom costs.

The current direct-random MCP evidence from the earlier audit remains the strongest available weighted artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e6b12c1c58d429149c8cfd862db1eb27fa2828abe9b019d28f7742f5b3bc5d5/4f8da02c2da90ddb1005a32456c01c0b3f80491073478574d0c2381ef2d085338/probability-ce533f32be4dd0efbce3f9f8.json` proves the declared conditional 10/90, 20/80, and 40/60 rebellion branch arithmetic but not mission cadence or campaign timing.

The previous mission and landing adapter artifacts are partial because route helpers, character scopes, equipment, and state-target inputs were unresolved. They must not be treated as exact AI-selection probabilities. The custom auditor route and current same-scenario compare remain blocked as described above.

## Localisation and tooltip gaps

All automatic decision and mission names/descriptions and all new custom tooltip keys resolve in the repository-wide localisation scan. Both edited localisation files retain the required UTF-8 BOM bytes `239 187 191`.

The four new requirement keys are `alien_infantry_landing_requirements_tt`, `dhrondan_kruger_expedition_requirements_tt`, `dhrondan_mengele_expedition_requirements_tt`, and `dhrondan_honor_accord_requirements_tt`. Existing cost and effect keys remain unchanged except for concurrent dynamic-constant edits in the two localisation files.

The medium rebellion line and static D’Rhondan cost values are the only remaining player-facing wording recommendations identified in this bounded audit.

## Cleanup and exploit-risk notes

The landing API clears the pending flag before refunding, removes the mission, clears the saved state and duration, and refunds exactly one reserve on cancellation or lost control. Successful materialization clears the same lifecycle state before applying one cohort, history receipt, counters, and cooldown.

Expedition success and failure both restore Kruger through the obligation-safe helper, clear the shared and route-specific flags, clear the audience flag, and clear the duration variable. Character and country receipt guards make authorization and return Directorate changes repeat-safe, and pact/contact setup is guarded against duplicate outcomes.

The rebellion warning is one-time, the pulse is country-scoped, and the revolt bridge has a one-call guard. No reviewed file adds a world-iterating daily/weekly/monthly action, free landing loop, duplicate active expedition, or cooldown bypass.

## Validation and skipped validation

Task-specific static checks after the patch found balanced braces in every touched script file, no unsupported `<=`/`>=` operators, no global cadence hook, no undeclared D’Rhondan constant reference, all four new localisation keys present, all automatic decision/mission keys present, and intact localisation BOMs.

The mandatory GUI inspection/render evidence was attempted for the ordinary `countrydecisionview` surface before and after the bounded source review, but both calls timed out after 180 seconds and yielded no artifact. No `hoi4.gui_rewrite` was used because this patch does not create or alter a GUI layout.

The mandatory probability inspection route was attempted and timed out for the current decision source after the documented input-schema rejection. No AI or probability-bearing source was patched, so no before/after probability compare exists. The custom `chaosx_ai_probability_auditor` route is unavailable in this runtime.

No live Hearts of Iron IV process was launched. Gameplay, save-state, and user-owned in-game acceptance remain outstanding and cannot be certified by this handoff.

## Remaining issues and parent actions

1. Preserve and review the concurrent dynamic-constant localisation edits before merging, especially the medium rebellion line’s explicit high-tier precedence wording.
2. Re-run `hoi4.gui_inspect` and `hoi4.gui_render` for `countrydecisionview` when the MCP service responds, using the current requirement-tooltip source and named landing, expedition, Accord, and rebellion states.
3. Re-run the custom probability auditor and same-scenario compare when the route becomes callable, preserving the unresolved status of route and landing target fixtures until the adapter accepts the required nested inputs.
4. Optionally convert the remaining D’Rhondan cost and duration prose to dynamic constants in a localisation-only pass if the parent wants drift-proof text; this is not a gameplay blocker.

Plan handoff path: this file. No broader implementation plan was written because no unresolved mechanic requires a new system or cross-file design beyond the parent-owned work.
