# Event 012 protection report localisation handoff

## Basis and scope

The parent assignment identifies Arms Against Tyranny mutual market access and gated enemy intelligence as accepted design for this protection tranche. Event 012 protection spends at most four resource types. Event 013 relief remains a separate choice at its existing full price. This handoff records a bounded localisation patch only. The parent owns the `.610` event logic, costs, service behavior, and final integration.

## Changed files

- `localisation/english/012_africa_gods_l_english.yml`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_protection_report_feedback_locale_audit_2026-09-25.md`

## Changed keys and display

Added these ten keys to match the conditional branches currently visible in `events/012_africa_gods_of_africa.txt` at `chaosx.nr12.610`:

- `gods_of_africa_protection_service_market_missing_dlc_tt`: "Mutual market access requires Arms Against Tyranny."
- `gods_of_africa_protection_service_market_capability_locked_tt`: "Africa must complete Sanctuary for Reliable Partners to offer mutual market access."
- `gods_of_africa_protection_service_market_unconfirmed_tt`: "Mutual market access with [gods_of_africa_protected_participant.GetName] was not secured under this pledge."
- `gods_of_africa_protection_service_intelligence_missing_dlc_tt`: "Sharing enemy intelligence requires La Résistance."
- `gods_of_africa_protection_service_intelligence_capability_locked_tt`: "Africa must complete Swear Continental Security Oaths to share enemy intelligence."
- `gods_of_africa_protection_service_intelligence_host_agency_missing_tt`: "Africa has no intelligence agency to share intelligence on its enemies."
- `gods_of_africa_protection_service_intelligence_participant_agency_missing_tt`: "[gods_of_africa_protected_participant.GetName] has no intelligence agency to receive Africa's enemy intelligence."
- `gods_of_africa_protection_service_intelligence_no_war_tt`: "Africa is not at war, so it has no enemy intelligence to share."
- `gods_of_africa_protection_service_intelligence_no_eligible_enemy_tt`: "Africa has no active enemy that [gods_of_africa_protected_participant.GetName] is not also fighting."
- `gods_of_africa_protection_service_intelligence_unconfirmed_tt`: "No enemy intelligence was shared with [gods_of_africa_protected_participant.GetName] under this pledge."

Revised `gods_of_africa_protection_service_conditions_tt` to: "Guarantees and access depend on focus and diplomatic conditions. Transport and reconstruction depend on shortages, stockpiles, and territorial control. Reception depends on Migration capacity."

Before this patch, the ten conditional branches had no matching localisation entries. The shared line repeated market and intelligence requirements and used semicolon-separated clauses. After this patch, each named blocker has a direct line, and the shared line covers only the other conditional services.

## Audit findings and limits

- Missing keys in this assigned set after patch: none. Duplicate keys in this assigned set: none. Wrong namespace in this assigned set: none.
- Scripted localisation issues in these changed lines: none found. The participant name token is retained in every new line that names the participant. No new cost or timer values were introduced. Existing dynamic cost, timer, actor, and service tokens outside these lines were untouched.
- Dynamic text opportunity: the participant actor is used in the market and intelligence lines where its identity helps distinguish the result. The DLC and Africa agency blockers do not need an actor token.
- Cross-surface mismatch: the `.610` description still summarizes withheld conditional services, which is consistent with the more specific tooltip lines. No event catalog text was edited. If the catalog mirrors this tooltip, `chaosx_spreadsheet_doc_worker` should copy the final key wording above from the workbook source.
- Prose quality: the old shared line was bloated, repetitive, and mechanically crowded. The replacement removes the repeated market and intelligence clauses and the semicolon chain. The new lines identify the missing DLC, focus, agency, war, eligible enemy, or unconfirmed result directly. No unrelated prose was revised.
- Sourced quotations: none in the inspected `.610` tooltip set. No quotation wording was changed.
- Encoding: the localisation file still begins with the UTF-8 BOM. The eleven assigned keys occur exactly once, use one physical line per value, and contain no em dash or semicolon. Git reports a possible future LF-to-CRLF conversion under working-tree settings; the patch did not change unrelated lines.

## Evidence and parent follow-up

The read-only `hoi4.event_inspect` trace for `chaosx.nr12.610` returned `EVENT_INSPECTED_PARTIAL` at source revision `f737d8d5eb3e07985d0b73c706f872a0ccada3c8856c1f2fc0b0984806ade4e9`; its linked report is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b79d61a72799ca9f899ce643e0408d6d43f47265a220e15a82ebf9e51e0b5429/835282870ba50444ac8fe9db13affaab899ab8943d9ff4393566b855eb0504e7/event-trace-f737d8d5eb3e.json`. The read-only options render returned `EVENT_RENDERED_PARTIAL` at the same revision, with `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc9fd99a2bb85a79a825efe3085aac215b7824f7b86b0eb21a491baa09ee0fa8/973bc75948be063634e204dfb6ded7dbed372f9b97355f7fba6e18ecade0c009/event-options-f737d8d5eb3e-manifest.json`. These linked artifacts provide source and option coverage but do not prove in-game tooltip layout or condition outcomes.

The exposed technology inspect, render, and compare routes are separate from a standalone Technology Tree Viewer. No standalone viewer tool was available in this session's tool inventory, which is a package gap. No technology surface was changed or inspected for this patch.

Parent integration: the parent reviewed the final `.610` branch order against the service owner effects, confirmed that each new key has one event reference and one localisation definition, and reran Event MCP lint and options rendering at revision `f737d8d5eb3e07985d0b73c706f872a0ccada3c8856c1f2fc0b0984806ade4e9`. Those results remain partial and are detailed in `012_africa_gods_protection_report_feedback_2026-09-25.md`. In-game tooltip layout and condition outcomes were not tested; live-game confirmation remains with the user. The parent added only conditional report tooltips, without changing service eligibility, costs, AI, cooldowns, focus rewards, or Event 013 behavior.
