# Event 016 delayed-news host-context continuation

Date: 2026-08-02

## Scope

This bounded continuation preserves the host-archetype context in the seven delayed minor news headlines. Unlike country events, a `news_event` is presented from a global news scope, so the ordinary `GetBrilliantScientistHostFlavorClause` helper would evaluate the wrong scope.

## Changed surfaces

- `common/scripted_localisation/016_brilliant_scientist_host_flavor_scripted_localisation.txt`
  - Adds `GetBrilliantScientistNewsHostFlavorClause`.
  - The helper checks the global `brilliant_scientist_current_host` event target and selects the existing refugee, colonial, university, industrial, militarized, threatened, or default clause.
  - The final branch is safe after terminal cleanup clears the global target.
- `localisation/english/016_brilliant_scientist_l_english.yml` and `localisation/english/016_brilliant_scientist_aftermath_l_english.yml`
  - Append the helper to the seven delayed milestone descriptions `.302` and `.304` through `.309`.
- `docs/events/016_brilliant_scientist/systems/news_events.md`
  - Documents the delayed global-host lookup and neutral cleanup branch.
- `docs/events/016_brilliant_scientist/overview.md`
  - Records the news-context continuation as presentation-only content.
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md`
  - Adds the handoff to the bounded continuation ledger.
- `docs/specs/016_brilliant_scientist_specs/handoffs/016_completion_status.md`
  - Records the news-context continuation and preserves the incomplete broader-content boundary.
- `docs/specs/016_brilliant_scientist_specs/package_checksums.sha256`
  - Recomputed for the selected 55-entry documentation ledger.

## Preserved contracts

No global receipt, news trigger, super-event, terminal transition, event-log row, Event Details row, asset, project stage, evolution, unit, model, or cleanup effect changed. The helper reads only the existing global host target and reuses existing clause localisation.

## Validation

- Confirmed the Event 016 localisation files remain UTF-8 with BOM.
- Confirmed all seven news descriptions contain the helper once and remain unique.
- Focused `hoi4.event_inspect` lint for the related news path returned `EVENT_INSPECTED_PARTIAL`, status `ok`, with no blocking diagnostics; the tool deferred its workspace-wide helper/lifecycle pass as documented for this large workspace.
- Recomputed the 55-entry documentation checksum ledger and checked for zero mismatches.

## Deferred work

Broader country-specific chains, quantitative news or route-balance evidence, live in-game presentation acceptance, and the seven Event 016-specific 3D packages remain outside this continuation. No model or fallback asset was created.
