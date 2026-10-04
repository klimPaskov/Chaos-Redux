# Camp administration monthly dispatch

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

The recipient calculates a calendar month key and records it before maintenance, economy, institution, territorial and country processing.
The existing Chaos Meter dispatcher and this timer may both reach the recipient in an enabled month; the key allows only the first to pay or apply losses.
Every administration payment, reward and physical population debit remains in the existing package helpers.
Continuing institutional harm belongs to the guarded monthly state owner, while automatic Mengele reports `.10`–`.13` retain evidence-only compatibility calls and submit no additional casualty transaction or request-derived hidden atrocity under the parent's accepted single monthly processor contract.
The [current institutional report handoff](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/mengele_exact_custody_adapter_2026-10-03.md) records 32 parsed-source cases and blocked MCP domain inspection without claiming engine scheduling or native receipt proof.
Lasting closed-site metadata is separate from active monthly recipients, as recorded in the [closed-site archive handoff](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_closed_site_archive_integration_2026-10-03.md).
Its one-time existing-startup bootstrap retains original actors for Records, filtered Locations and reform PAUSE, and records-only opening does not register a monthly recipient or recreate active work.
No core registry or recurring world hook is added by that metadata contract, and native iteration/ceased-country setter behavior remains unproved.
No shared Chaos Meter hook or registry definition is changed by this timer.

The timer is triggered-only and hidden, so it creates no notification or choice.
Its registration flag is an internal true/false state, while the period is a shared script constant.
The package UI uses existing `gfx/interface/camp_repression/` sprites and `interface/camp_repression_rework.gfx`; this dispatch feature needs no new icon or sprite name.

The parsed-source and calendar model in `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/dispatch_source_tests.py` covers both registry entry paths, a full normal year, leap year, both Chaos Meter settings, exclusion and ordinary inactivity.
That model cannot verify Clausewitz event scheduling or month-key persistence in a running game; the scoped HOI4 MCP result and any unresolved engine evidence belong in the package completion report.
The [current resume packet](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/resume_packet.md) indexes dispositions and remaining acceptance work.
The event inspector's partial result and the installed vanilla delay precedent do not establish that this timer fires in game.

## Future work

If a future package adds an eligible country or a new terminal country transition, call `camp_rework_register_country_for_monthly_pulse` on acquisition and remove the country from the bounded registry on termination.
Keep new recipients behind the same calendar guard so they cannot debit reserves, population or records twice.
