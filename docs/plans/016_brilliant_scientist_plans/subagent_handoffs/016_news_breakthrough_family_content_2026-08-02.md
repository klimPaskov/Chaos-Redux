# Event 016 public-breakthrough family news handoff

## Scope

This bounded continuation makes the existing first public-breakthrough headline identify the project family already recorded by the Directorate. It does not create a second project reward, a new event path, a new event-log row, a new receipt, or a unit or model dependency.

## Changed files

- `common/scripted_localisation/016_brilliant_scientist_host_flavor_scripted_localisation.txt` adds `GetBrilliantScientistNewsBreakthroughClause`.
- `localisation/english/016_brilliant_scientist_l_english.yml` appends that helper to `chaosx.nr16.306.d` and localizes all fifteen project-family clauses plus the neutral branch.
- `docs/events/016_brilliant_scientist/systems/news_events.md` records the existing public-family ledger and stable selector order.
- `docs/events/016_brilliant_scientist/overview.md` records the headline wording continuation.
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md` records the accepted bounded continuation and this handoff.
- `docs/specs/016_brilliant_scientist_specs/handoffs/016_completion_status.md` indexes this handoff in the current continuation ledger.

## Runtime contract

The helper reads `brilliant_scientist_current_host` only when that global event target exists. Inside that host it checks the existing `brilliant_scientist_breakthrough_public_families` array against the fifteen `constant:brilliant_scientist_project_family` values. The order is deterministic and is presentation-only when more than one public family exists before the delayed headline is shown. A missing target or an unrecognized ledger returns the neutral impossible-research clause.

The `.306` news event remains minor, triggered-only, and guarded by `brilliant_scientist_news_public_breakthrough_fired`. No effect, option, title, picture, timing, receipt, event-log actor, Event Details row, project stage, AI weight, or world-state threshold changed.

## Validation

- Focused `hoi4_event_inspect` lint for `chaosx.nr16.306` returned `status: ok`, `blockers: []`, and no blocking diagnostics. The inspector still reports the known workspace-wide helper/lifecycle analysis deferral for this large mixed workspace.
- The localisation file retains its UTF-8 BOM.
- The fifteen new localisation keys and the neutral key each occur exactly once, and the helper and `.306` call each occur exactly once.
- No Event 016 unit, provider, entity, sprite, or 3D model file was created or referenced.

## Deferred boundary

Broader country-specific chains, quantitative balance evidence, user-owned live acceptance, and the seven reusable Event 016 model packages remain deferred. This continuation does not change that boundary.
