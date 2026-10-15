# Camp administration monthly dispatch

## Management-window presentation

Camp Administration shares the native brass/olive management-window family with Migration and Famine.
Its Administration, Locations, Records and policy pickers preserve existing actions and accounting, with status colors, complete scroll rows and concise text.
There is no manual refresh control.
Native GUI state reevaluates each tick; a separate [presentation-only observer](../../common/scripted_effects/national_policy_panel_effects.md) updates cached display fields automatically while a human window is open.
That observer never calls this monthly processing path, changes population or advances funded work.
It uses the existing annexation/terminal closure/release boundaries to retire stale UI reservations, with an earliest-hour guard for delayed callbacks.
The shared [implementation report](../plans/famine_and_migration_system_plans/national_policy_panels_implementation.md#shared-camps-styling-and-automatic-updates-15-october-2026) records the source, visual, localisation and lifecycle checks.

## Monthly gameplay dispatch

The camp package registers eligible countries with an active camp, custody, institutional, aftermath or focus-hook responsibility.
Registration stores the country in `global.camp_repression_active_countries` and starts one hidden `camp_administration_country.2` timer guarded by `camp_admin_dispatch_timer_active`.
The focus-hook watch initializer uses the same timer-start helper when it is the first registry entry path.
The package-owned integer constant `camp_admin_dispatch.period_days` schedules each next timer call after 28 days, including when the Chaos Meter setting disables its existing monthly dispatcher.
The installed vanilla `common/scripted_effects/SIA_scripted_effects.txt` uses `country_event = { ... days = constant:propaganda.SIA.default_propaganda_campaign_old_days }` at lines 768, 793 and 818, a direct precedent for this `country_event` delay field (SHA-256 `ac1e86a0ffe5e46f7083318c584993667eaafb3cd1585e15db71fbd51fa276af`).
Installed `documentation/effects_documentation.md` lines 2943–2967 documents `country_event` and its `days` delay (SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`).
The [direct installed MCP 3.6.0 event review](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/dispatch_event_3_6_0_2026-09-27/review.md) recognizes the delayed self-call but still leaves its shared constant and helper path unresolved.
The vanilla precedent supports syntax without proving the timer fires or keeps one chain in a running game.
At each call, the event verifies eligibility and registry membership, runs `camp_admin_integration_monthly_country_recipient`, and schedules its successor.
If eligibility or membership has ended, it clears the timer flag and stops; a country that became a special Chaos actor also runs the package's existing exclusion cleanup.
After an eligible month's processing, the timer uses the same package-owned registry-work trigger as the existing global cleanup; if no active network, reform, open ledger, focus watch or continuing administration work remains, it removes that country from the registry and stops.
The timer flag stays set during registry removal until that outstanding delayed event arrives, so a rapid return cannot start a second chain.
Each scheduled call goes through `camp_rework_schedule_country_timer`, which also stores `camp_admin_dispatch_timer_earliest`: the current date plus `camp_admin_dispatch.period_days` minus `camp_admin_dispatch.due_tolerance_days` (1), converted with `chaosx_convert_days_to_date_offset`.
Annexation and special-country exclusion both run `camp_admin_integration_close_country`, which clears the timer flag and that date, because the pending event may never arrive for a country that no longer exists.
A re-released country therefore starts a fresh chain on registration.
If the old event is still delivered later, `camp_admin_dispatch_timer_is_due` finds it earlier than the stored date, and it stops without running the month or rescheduling, so only one timer stays outstanding; the calendar month guard still blocks any double monthly run.
A save whose timer predates the stored date treats that timer as current.

The recipient calculates a calendar month key and records it before maintenance, economy, institution, territorial and country processing.
The existing Chaos Meter dispatcher and this timer may both reach the recipient in an enabled month; the key allows only the first to pay or apply losses.
After ordinary monthly work processing, the same recipient checks paid Belgian quota and corridor receipts left in flight by a country entering camp administration.
Each receipt retains its original state ID and waits until the current site ledger establishes the same responsible country, eligible state type, current authority, and a free works slot.
Quota receipts are considered before corridor receipts, so two simultaneous paid orders start one at a time and the second remains pending while the first project occupies the slot.
The accepted order uses the existing Administration works project and its ordinary monthly funding; the original action is not charged again upfront.
The receipt clears only after the country project slot records the matching state ID and `works` type, and current authority loss, site closure, or C6 conversion retires it without a legacy scalar grant or refund.

A corridor receipt becomes a separate started receipt only after its own order passes the free-slot state/type postcondition. The central economy project completion path applies the original `guard_relief` pressure reduction only while that started receipt matches the exact active works slot, then consumes it before the shared cancellation helper clears the slot. Cancellation, replacement, invalid-site cleanup, country closure, and C6 cleanup clear an unfinished started receipt; quota and unrelated works never earn corridor relief.
Every administration payment, reward and physical population debit remains in the existing package helpers.
The Civil Administration pressure refresh also resynchronizes the existing USA, France/Vichy, Italy, and Belgium national idea sets from those updated values and policy flags; these ideas contain social, political, or reform modifiers, while factory, resource, and forced-labor output remains in the current state/country economy modifiers.
Continuing institutional harm belongs to the guarded monthly state owner, while automatic Mengele reports `.10`–`.13` retain evidence-only compatibility calls and submit no additional casualty transaction or request-derived hidden atrocity under the parent's accepted single monthly processor contract.
The [current institutional report handoff](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/mengele_exact_custody_adapter_2026-10-03.md) records 32 parsed-source cases and blocked MCP domain inspection without claiming engine scheduling or native receipt proof.
Lasting closed-site metadata is separate from active monthly recipients, as recorded in the [closed-site archive handoff](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_closed_site_archive_integration_2026-10-03.md).
Its one-time existing-startup bootstrap retains original actors for Records, filtered Locations and reform PAUSE, and records-only opening does not register a monthly recipient or recreate active work.
No core registry or recurring world hook is added by that metadata contract, and native iteration/ceased-country setter behavior remains unproved.
No shared Chaos Meter hook or registry definition is changed by this timer.

## Restored colonial decisions and Civil Administration

When a French or Belgian country has `camp_admin_initialized`, its restored inspection and reform decisions hand settlement into `camp_administration_civil_action_two` only after `camp_admin_country_sites_ready_for_reform` and `camp_administration_civil_action_two_available` both pass.
This is the existing Civil Administration review entry point, so the country continues through the existing monthly payment and completion contract rather than receiving a second legacy closure settlement.
The monthly review charges 15 support equipment and 8 political power for each accepted month, and its three-month target pauses when the shared payment helper cannot pay.
France's initialized `fr_inspect_camp_legacy` reads the current site and evidence registries without replacing their responsibility or evidence fields.
Its 180-day Gurs mission retains the limited historical pressure and reform-credit outcome, then starts the current paid review only when that review remains eligible.
The initialized `fr_close_camp_legacy_sites` path consumes its existing support-equipment order and starts the same review. Its delayed removal callback cannot perform a second site settlement.
The decision leaves the list when the Civil Administration review completes or when its existing 270-day timer ends, while the legacy pre-initialization closure path retains its existing per-site behavior.
Belgium's `bel_concession_reform_mandate` keeps its 365-day historical mandate period, but the initialized path does not start legacy per-site closure timers.
At mandate completion, a current full-record preflight and an available Civil Administration review start one paid review. An already active or completed review is treated as the existing outcome and is never started again.
The legacy pre-initialization Belgian mandate retains its previous dismantlement outcome.
When a country becomes nonhuman before the legacy mission completes, its mission, active French timed closure decision, and pending route flags are retired without running success or delayed removal callbacks.
This cleanup preserves an already active or completed Civil Administration review and its paid progress.

The timer is triggered-only and hidden, so it creates no notification or choice.
Its registration flag is an internal true/false state, while the period is a shared script constant.
The package UI uses existing `gfx/interface/camp_repression/` sprites and `interface/camp_repression_rework.gfx`; this dispatch feature needs no new icon or sprite name.

The parsed-source and calendar model in `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/dispatch_source_tests.py` covers both registry entry paths, a full normal year, leap year, both Chaos Meter settings, exclusion, ordinary inactivity, and annexation followed by re-release before and after the stale event would arrive.
That model cannot verify Clausewitz event scheduling or month-key persistence in a running game; the scoped HOI4 MCP result and any unresolved engine evidence belong in the package completion report.
The [current resume packet](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/resume_packet.md) indexes dispositions and remaining acceptance work.
The event inspector's partial result and the installed vanilla delay precedent do not establish that this timer fires in game.

## Future work

If a future package adds an eligible country or a new terminal country transition, call `camp_rework_register_country_for_monthly_pulse` on acquisition and remove the country from the bounded registry on termination.
Keep new recipients behind the same calendar guard so they cannot debit reserves, population or records twice.
