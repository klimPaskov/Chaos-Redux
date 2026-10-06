# Event003 Release QA Follow-up - 2026-10-06

## Status

This follow-up closes the accepted source defects in the Bodhisattva escort mission, three unreachable Bodhisattva actions, the Bhumi advancement ceiling, the Unshaken Seat capital prerequisite, and the terminal Final Silence text path. Parent integration still owns the shared Final Silence achievement condition. No focus coordinates, AI weight values, shared settings files, shared event-log registry files, GFX, interface, or workbook files were edited.

## Files changed

- `common/decisions/003_holy_realm_decisions.txt`
- `common/scripted_effects/003_holy_realm_effects.txt`
- `common/scripted_effects/003_holy_realm_effects.md`
- `common/scripted_triggers/003_holy_realm_triggers.txt`
- `common/national_focus/003_holy_realm.txt`
- `events/003_the_holy_realm.txt`
- `localisation/english/003_the_holy_realm_l_english.yml`
- `localisation/english/003_holy_realm_requirement_flags_l_english.yml`
- `docs/events/003_holy_realm/overview.md`
- `docs/events/003_holy_realm/systems/buddhahood_progression.md`
- `docs/plans/003_holy_realm_plans/agent_decisions_2026-10-05.md`

Final current-source SHA-256 values for the principal touched files:

- `common/national_focus/003_holy_realm.txt`: `29C3BD371CFC53912C1F3C72BDD00CEFB2262BD6303EE7195DE5750E244278D9`
- `common/decisions/003_holy_realm_decisions.txt`: `88DAE2B720A330214A3858623AC41010B2FBDAB10D0402CDE833AAB6D5B54C04`
- `common/scripted_effects/003_holy_realm_effects.txt`: `EC66BD83349BCE11B3DEA1DFD4C15008777A6BFBDB228C4DB08CDFD9C73CD710`
- `common/scripted_triggers/003_holy_realm_triggers.txt`: `E0E7F8151B468911022F761FBA6F63FA76C674694D86C793FEBCA4906EF32964`
- `events/003_the_holy_realm.txt`: `149D693B96F008FA7977DF3A1CFC179D47A772C727BF57C76C968C50A65E0E16`
- `localisation/english/003_the_holy_realm_l_english.yml`: `AE570FF0CC5FF26669B66C320899F1B45E2F5858929D4BD8DB8DF37B29C45D80`
- `localisation/english/003_holy_realm_requirement_flags_l_english.yml`: `C98CEE1B72ECD16AD7C0E5F9A343A830C85B051DE2A2D386624E74C51B5F70B7`

## Mission and decision fixes

`THR_bodhisattva_guard_pilgrimage_route` now cancels while its timer is active if the selected state leaves Realm control or falls below two divisions. The existing presence check uses the same `FROM` state and nested `ROOT` country scopes as the already-required availability check. `cancel_effect` and the timeout failure branch share the idempotent country effect `holy_realm_cancel_pilgrimage_route_escort`.

At selection, the decision saves the exact current Political Power quote used by the native `cost` and records a Black Friday purchase receipt with the shared receipt-aware helper. Cancellation refunds that saved quote, the 20 Command Power, and 120 Support Equipment, withdraws the sale receipt only if its sale sequence is still current, frees the teaching seat, clears active/escrow state, and keeps the original Defilements increase and Sangha Cohesion loss. Timeout failure uses the same refund and cleanup path. Successful completion clears the saved receipt without refund and retains the existing infrastructure, experience, Bodhi, Compassion, Sangha, and Reach rewards. A country can run only one escort at a time, protecting the per-country escrow from overlapping state-target missions.

The mission description now states the two-division obligation for all 60 days, loss-of-control or troop-loss cancellation, resource returns, and failure penalties. The available-block tooltip describes the selected-state division requirement, busy state, and exact resource costs.

The three source-defined Bodhisattva actions previously had `visible = { always = no }` and no caller. Their route visibility and availability now follow existing route gates: `THR_bodhisattva_mission_refuge_circuit` follows the Bodhisattva teaching unlock, `THR_bodhisattva_mission_white_scarf_envoys` follows the Buddha path, and `THR_bodhisattva_mission_wounded_border` follows the guardian unlock plus war or serious chaos pressure. Their existing completion-memory flags now make each one-time. No new category, focus, or route family was added.

`THR_bodhisattva_hold_teachings_for_refugees`, `THR_bodhisattva_teach_foreign_officers`, and the three newly surfaced actions now share `holy_realm_bhumi_advancement_available`, which uses `constant:holy_realm_buddhahood.bhumi_max`. Existing non-Bhumi completion rewards cannot be repeated after the Bodhisattva reaches the tenth Bhumi. The AI weight values remain unchanged.

`THR_hold_dharma_teaching` intentionally remains a general teaching action after the Bhumi cap. The shared effect continues to record teaching success but stops increasing Bhumi at its cap, and the threshold PP/CP/stability milestones are guarded one-time awards. Its `.110.b` and `.111.b` outcomes each grant five PP; the lowest discounted quote for its 25 PP native cost remains seven PP, so those outcomes remain net costs even during a sale. This follow-up did not alter its availability or AI weights.

## Focus prerequisite and source-to-spec correction

The accepted Buddhahood Stage 3 spec at `docs/specs/003_holy_realm_specs/003_holy_realm_buddhahood_specs/specs/holy_realm_buddhahood_spec_part_1.md:79-87` requires protecting the capital sanctuary before the Unshaken Seat. `THR_buddha_mandate` previously checked only the Arhat path for availability. It now requires control of the current capital and no active `holy_realm_capital_sanctuary_recently_fallen` flag, the existing 180-day marker set after capital loss. The reason is visible through `THR_buddha_mandate_sanctuary_required_tt`.

The four existing `THR_buddha_mandate` support-root prerequisites remain because the accepted focus completion plan at `docs/plans/003_holy_realm_plans/003_holy_realm_buddhahood_plans/holy_realm_focus_tree_completion_plan.md:20` explicitly records them as the current route. The spec says the Bodhisattva enters the Seat at high progress but does not set a numeric threshold there; no threshold was guessed. No focus coordinates were changed. The focus auditor was notified to preserve the gameplay gate during its separate position-only work.

## Final Silence and Fallout alignment

The current terminal branch calls Fallout from `holy_realm_complete_terminal_final_silence`, records `world_end_final_silence_completed` and `fallout_cause_final_silence_memory`, and requests `fallout_request_intensity.maximum`. It does not set the retired global `world_end_final_silence` flag and it must not start a duplicate Event003 terminal sequence.

The current `chaosx.nr3.80` terminal branch schedules neither `chaosx.nr3.73` for every other country nor `chaosx.nr3.90` for the Realm; Fallout owns the terminal presentation. The `.73` witness flag has no consumers. Event definitions `.73` and `.90`, and legacy strike-wave events `.82-.84`, remain for already queued legacy event chains. The `.90` event no longer calls `world_end_scenario_triggered`; its only local scripted-effect definition is an empty block at `common/scripted_effects/chaos_meter_effects.txt:5681-5684`. The `chaosx_super_event.9` localization was rewritten to describe Fallout, but no current Event003 effect calls the Holy Realm terminal super-event slot. The `world_end_scenario_super_event.final_silence = 9` constant remains in the shared constants file, but parent integration removed the active shared registry row, so Event003 does not dispatch slot 9. The non-terminal Empty Seat still uses Event003 slot 8 through `holy_realm_show_super_event`.

The Event Details text now describes both outcomes and identifies Fallout as the terminal branch. `holy_realm_can_form_silent_mandala` no longer tests retired `world_end_final_silence`; it excludes the owner's `holy_realm_final_silence_terminal_completed` flag, which is written before Fallout's asynchronous terminal transition. Legacy strike-wave callbacks `.nr3.82-.84` remain for their existing legacy state paths and are not called by the current terminal completion effect.

The shared achievement `chaosx_achievement_003_holy_realm_final_silence_world_end` is outside this ownership boundary. Parent integration owns changing it from the retired global flag to the completed cause memory plus actual `world_end_fallout`, while preserving the current owner completion, readiness, and capital-safety checks. The completion effect marks `world_end_final_silence_completed` synchronously immediately before requesting Fallout; that cause flag alone does not prove that Fallout reached its terminal result.

## Reference and validation evidence

- `python .tools/report_colour_audit.py --event 003` returned `total keys with colour: 0` after the final localization pass. Both edited Event003 English localization files retain UTF-8 BOM and the current key scan found no duplicates or encoding replacement characters.
- Offline Decision modding wiki revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, lines 337-356, states that `cancel_trigger` ends a timer without running `remove_effect`, and that `cancel_effect` runs on cancellation. The same revision at lines 465-479 states that mission definitions can use `cancel_trigger` and `cancel_effect`.
- Installed decision documentation revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, lines 1-46, records the country/target scopes for availability and targeted decisions.
- Installed trigger documentation revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, lines 2648-2662, documents `divisions_in_state` in country scope with the requested `state` and `size` arguments. Offline Triggers wiki revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`, line 268, documents `capital_scope` as a country-scope trigger that enters the current capital state.
- `hoi4.script_validate` accepted command kinds and scopes for the cancellation trigger. It marked the `divisions_in_state` native argument block unchecked against prose docs, so that block is supported by the cited installed syntax and the existing identical owner availability pattern, not by a full MCP argument validation.
- `hoi4.script_validate` returned partial coverage for `capital_scope` because the installed-doc index omitted that trigger; the exact offline wiki row documents it. This partial validator result is not represented as a clean/full validation pass.
- Earlier Event003 decision scenario inspections for `THR_open_refuge_roads` timed out at 600 seconds. They were not repeated in this follow-up. This pass did not run a new decision scenario, live game, or weighted probability comparison. No AI weight changed.
- Focus inspect/render evidence remains with the parallel focus auditor. I supplied the final `common/national_focus/003_holy_realm.txt` source hash after my gate patch so that its result can bind to the same gameplay source before any position-only edit.

## Remaining limits

- The actual in-game timer cadence for `cancel_trigger`, auto-removal order on the final day, and refund behavior were not runtime-tested. The source uses the documented cancellation and cleanup blocks.
- Political Power uses the saved native quoted cost. Command Power refund remains subject to the engine's normal cap if the country fills its Command Power while the escort is active. Equipment is refunded in its consumed support-equipment type.
- The receipt-aware Black Friday helper can withdraw only when the original sale sequence is still the active retained sequence; its documentation says closed-sale history is not rewritten.
- Weighted AI probabilities and decision scenarios remain unresolved from the prior MCP timeouts. No probability-bearing value or AI weight was changed.
- Shared terminal achievement integration and final Event003 focus layout evidence remain parent-owned follow-ups.

No commit was made.
