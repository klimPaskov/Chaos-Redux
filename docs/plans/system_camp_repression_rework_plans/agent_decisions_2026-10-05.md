# Camps continuation decisions

Date of this pass: 6 October 2026.
Acceptance basis: the director's request to finish the camps workstream and implement the latest remaining-work audit, together with G6 authority to correct weak design.
The earlier accepted decisions remain in [the 4 October log](agent_decisions_2026-10-04.md).

## German and Japanese authority

Disposition: implemented.
One state-controller rule accepts Germany and its eligible puppet administrations while leaving Hungary, Romania, Bulgaria, Slovakia, Croatia, Vichy, Italy, Finland and special Chaos countries outside that authority.
Vichy's cosmetic identity is tested with `has_cosmetic_tag`, and ordinary FRA subjects remain eligible administrations.
Germany remains responsible after a handover to GEN or an RK country, including Kraków setup, killing-role conversion, Mengele, Łódź and paid transports.
The separate AI Kraków gate uses the same predicate.
The legacy `germany_controls_auschwitz_area` helper also uses that predicate, so Mengele's chain, active-program and restricted-program consumers do not reintroduce a direct-control requirement.
Custody-import preflight relies on the operational site's authority validation and exact responsible-country match, removing a redundant direct-controller check that would reject a GEN-held Auschwitz.
Parent review preserves enrollment tracking before the campaign's date or mandate gate opens.
Otherwise states taken before June 1941 would never enter the later campaign without another control change.
Tracking is harmless before that gate, while actual registration and deaths still require the live campaign.
Japan's eligible Chinese campaign includes its clients and excludes MAN/MEN core territory.
The explicit ITA exclusion also excludes vanilla's cosmetic `ITA_rsi`, rather than inventing a separate RSI tag.
Source consumers and tests are documented in `occupation/controller_authority_handoff.md` under the administration plan.

## Achievement paths

Disposition: implemented.
ENG's civil review sets the retained Raj-review receipt.
USA's wartime court review sets the before-victory receipt, while property claims retain 1 July 1948.
Italy's achievement reads completed civil review and closed camps instead of retired road and transport-guard actions, retaining the developed Libyan state and stationed division.
The complete 60 to 69 flag trace and executed review scenarios are in `subagent_handoffs/achievement_repair_2026-10-06.md`.

## Partner handovers

Disposition: implemented with the modeling limits below.
This decision supersedes round 2's rejection of the four wider partner routes within the current director-authorized completion scope.
It keeps the existing finite movement contract and avoids a separate country-run campaign or another world hook.
The [implementation contract](../../../common/scripted_effects/camp_occ_partner_effects.md) records historical sources, windows, enrollment shares and regional limits.
Each country receives one demand, the two Croatian operations share that demand, and Germany receives at most one halt notification per partner.
Hungary's existing first-wave behavior and 1944 numbers remain intact.
The wider partners answer before their first wave, and comply or delay dispatches the current month's transport immediately.
Waiting for another month would make the Bulgarian March order and some Croatian first-window schedules impossible.
A successful per-country month marker prevents repeated waves from replayed callbacks.
Delay halves the source offer as well as transport capacity, so it affects small countries too.
The Croatian first operation retains a 30-percent living remainder for May because the historical source establishes two operations without a reliable split.
That 70/30 split is a scheduling parameter, not a sourced historical count.
Vichy's start is 11 August 1942, so an immediate answer cannot send a convoy before the documented Les Milles departure.
The established monthly cadence can miss that first partial month, and the source scenarios retain that timing limit.

The wider route uses state 92 as an aggregate reception district, as suggested by audit r3's generic movement acceptance.
Deaths occur only after a real transfer, at that host, with the existing arrival fraction and GER responsibility.
This district-level representation does not claim exact killing-center geography, and it is a recorded parent choice under G6.
State 803 likewise approximates the Pirot area and contains territory beyond it.
Bulgarian control of state 731 also qualifies as an altered-control Macedonian case, while historical German control of Salonika remains on Germany's own route.
This conditional inclusion can increase the Bulgarian order's exposed population in that altered map, and no fixed historical total limits it.
Enrollment shares operate on living apportioned origins, without forcing transport or casualty quotas.
No research, productive allocation or material reward follows these deaths.

The halt decisions disappear when no living people remain to deport and refund rejected stale paid completions without granting sale credit.
Halt consequences retain the existing political pressure, stability, war support and subject-autonomy contract.
The new action uses the already registered halt price instead of another price-table entry or shared-file rewrite.
The report option and paid halt tooltip state their stability, war support, German opinion and subject-autonomy consequences.
An explicit regular event target carries the halted partner's name into Germany's notification.

## Campaign start dates

Disposition: implemented, with source execution and sensitivity evidence in `subagent_handoffs/campaign_dates_2026-10-06.md`.
Salonika's origin state 731 keeps 15 March 1943.
Other Greek origins start on 24 March 1944 and Italian origins on 16 October 1943.
The shared monthly and manual-source predicates use those dates, while the dated partner handover remains its own historical route.

## Evidence and remaining approval gates

The MCP tools are absent from the root session's callable wrapper list, but the unchanged direct installed client reports 3.8.1 and serves narrow reference, event and probability routes.
Revision-bound source sections and saved requests are retained under `administration_redesign_2026-09-06/mcp/takeover_2026-10-06/`.
The root's Records inspect and render each timed out after 60 seconds, with no PNG or visual approval.
The new halt label uses the existing row and shorter wording than the retained Hungarian label, but source review cannot substitute for the missing current render.
Live engine, AI and visual gates remain in the final takeover status.
