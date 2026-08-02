# Event 016 project-army news family handoff

Date: 2026-08-02

## Scope

This bounded continuation deepens the existing delayed `chaosx.nr16.308` project-army news headline. The report now names the first materialized project-force family recorded by the active host instead of describing every formation as an undifferentiated experimental unit.

The selector is presentation-only. It reads the existing formation counters on the retained `brilliant_scientist_current_host` event target and adds no project stage, unit, provider, entity, receipt, trigger, world-state effect, or model dependency.

## Changed files

- `common/scripted_localisation/016_brilliant_scientist_host_flavor_scripted_localisation.txt`
  - Added `GetBrilliantScientistNewsProjectArmyClause`.
  - Uses guarded host-target counter checks with stable precedence: temporal, alien-interface, xenobiological, paleogenetic, machine, clone, portal, then neutral.
- `localisation/english/016_brilliant_scientist_l_english.yml`
  - Appended the new selector to `chaosx.nr16.308.d`.
  - Added eight player-facing clause keys for the seven known formation families and target-cleanup fallback.
- `events/016_brilliant_scientist_news_events.txt`
  - Corrected the file overview comment from six to seven delayed headlines.
- `docs/events/016_brilliant_scientist/systems/news_events.md`
  - Documents the formation-counter selector and its cleanup behavior.
- `docs/events/016_brilliant_scientist/overview.md`
  - Records the family-specific project-army headline content.
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md`
  - Adds the bounded project-army news continuation and handoff pointer.
- `docs/specs/016_brilliant_scientist_specs/handoffs/016_completion_status.md`
  - Adds the new handoff to the current continuation list.

## Preserved contracts

- The project-army news event remains a one-time minor `news_event` with the existing receipt and delay.
- Existing formation effects, Event 019 provider callbacks, native portal and temporal consumers, route weights, and unit templates are unchanged.
- The selector safely falls back when terminal cleanup has cleared the global current-host target.
- No Event Details row, Event Log row, achievement, evolution, asset, or 3D model is introduced.

## Validation record

- Confirm that all eight selector localisation keys exist exactly once and the selector definition exists exactly once.
- Confirm that each new family branch resolves an existing host formation counter and that `.308.d` calls the selector exactly once.
- Confirm UTF-8 BOM on the touched localisation file.
- Recompute `docs/specs/016_brilliant_scientist_specs/package_checksums.sha256` and require zero mismatches.
- Run focused `hoi4.event_inspect` lint for `chaosx.nr16.308`; accept only a report with no blocking diagnostics. The large-workspace deferred helper/lifecycle note remains a tool limitation.

## Deferred work

The seven Event 016-specific unit entity packages remain intentionally deferred. The ordinary sprites currently used by the route consumers are not reclassified as final model completion. Quantitative balance evidence, live game acceptance, and broader country-specific flavour remain outside this continuation.
