# 15 · Event integration

## Identity and shared selection

Keep Event 076 as Minor Repeatable, Chaos level 1, Military Preparation / Low. The catalog status remains To Be Reworked until the implementation workflow authorizes its change. The Low member classification is a source requirement and does not limit the physical severity of a nuclear evolution.

Use zero-padded `076_` filenames and documentation folders. Preserve runtime namespace `chaosx.nr76` and the established entry `chaosx.nr76.1`. Inspect the full current namespace before assigning additional numeric event IDs. Reusing the entry requires replacing its old immediate victim-options behavior with the wave authorization flow, while preserving any documented external callers through an explicit migration.

The shared picker decides when the repeatable event fires. Event 076 supplies valid eligibility and capacity checks. It does not add another random scheduler, alter shared major weighting or bypass cluster selection. An exhausted target pool, absent USA, no free job capacity or no valid provider makes the event unavailable. The shared UI should use its established unavailable presentation, not pretend that a zero-weight entry is currently selectable.

Count one accepted shared dispatch as one wave and one Event 076 firing. Individual tests, victim responses, delayed impacts, reports and evolution activations are not additional random-event firings. Apply the existing repeat-weight and recovery rules once through their owner. Follow-up experiments cannot raise major-event pressure repeatedly by impersonating new minor firings.

The actor supplied to the pre-fire event-history context is USA, before the logger runs. For evolution logging, refresh the actual `events_log_evolution_actor` context and its associated readiness state immediately before the evolution record. Do not reuse a stale actor from another event.

## Integration touchpoints

The following is a proposed organization. Confirm actual project naming, existing owners and current paths before adding files. Extend a shared owner in its own location where its interface belongs.

| Surface | Intended location or treatment |
| --- | --- |
| Country and news event flow | Existing `events/076_usa_tests_weapons.txt`, with additional event-scoped files only if their separation has a clear role |
| Event decisions and missions | Event-scoped definitions beneath `common/decisions/`, following the current project convention |
| Job and selection helpers | Event-scoped files beneath `common/scripted_effects/` and `common/scripted_triggers/` |
| Tunable constants and derived values | Existing project scripted-variable or value convention, without duplicating shared constants |
| Dynamic owner adapters | Extend the actual Deaths, nuclear, missile, chemical, biological, condemnation and research owners |
| Institutional and backlash ideas | Event-scoped definitions under `common/ideas/`, with at most three Event 076 national spirits simultaneously in a country |
| English localisation | Existing `localisation/english/076_usa_tests_weapons_l_english.yml` and necessary event-scoped additions |
| Sprite registration | Event-scoped interface registrations following existing GFX ownership |
| Runtime art and audio | Category paths defined in [16](../presentation/16_presentation_and_assets.md) and [17](../presentation/17_nuclear_super_event.md) |
| Achievements | Only `common/achievements/chaos_redux_achievements.txt`, preserving existing unique IDs |
| Persistent source design | `docs/specs/076_usa_tests_weapons_specs/` |
| Working plan and actual audit handoffs | `docs/plans/076_usa_tests_weapons_plans/` |
| Runtime event documentation | Follow the repository's event documentation convention after implementation |

Do not place generated helper definitions in documentation folders and claim that the game loads them. Do not create a separate achievement registry file for Event 076. Localisation uses the project-required encoding and complete variable declarations. Dynamic actor, country, state, dates and casualty values must refer to the current experiment, not global scratch state.

## Scheduling and multiplayer

Use an event-owned bounded scheduler or delayed chain supported by the current architecture. No new all-country daily or weekly on_action is authorized by this package. Multiple jobs can be due on the same day, but their authoritative identities and actual transactions remain independent.

Random target and family choices are made once by authoritative game logic, then stored. A UI refresh, reopened decision category, client-side render, reload or report must not reroll them. Multiplayer must share the same accepted choices, impact records and rewards. Separate human victims receive only their own demands and consequences.

The program remains subject to the mod's established enabled-country and event settings. Inspect which setting applies to the actor, recipient and shared picker before wiring it. Do not invent an immunity toggle or remove the strong priority for valid human minors. Disabling new selection cannot undo a physical test or erase an owner-controlled outbreak already in progress.

## Catalog and documentation updates

The supplied Event 076 catalog row is not yet assigned to the required cluster. Resolve that planned change through the canonical workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. Add Military Preparation / Low using the real workbook schema and preserve the rest of the row. The CSV attachments are exported references, not editable source-of-truth substitutes.

Run the established exporter `.tools/export_event_catalog_csv.py` after the workbook change and inspect the resulting diff. The workbook and exporter were not available or executed in this planning task. Do not claim that the cluster is already integrated because it appears in this Markdown package.

The supplied Event 036 row and current convention-spec paths conflict. Verify the real Convention owner before updating cross-references. Do not rename the unrelated existing row on the assumption that one of these documents must be stale.

## Old behavior being replaced

The fully inspected legacy Event 076 immediately penalizes country manpower and selected buildings on acceptance, grants USA 50 Army Experience immediately, and makes the refusing victim declare war on USA. It has no independent multi-country testing schedule or typed analysis phase in the inspected file.

The replacement must make USA the attacker after a valid refusal, remove actual civilian population through the shared transaction, and award the correct family only after analysis. Remove the old option-side instant reward and country-manpower substitute from the active new path. Preserve no hidden parallel path that can still fire them after the wave implementation is installed.

Do not treat a documentation update as a behavioral migration. Inspect all callers of `chaosx.nr76.1`, the old flag, relevant localisation and any existing event registry entries. A compatibility entry must forward to the new authoritative flow exactly once.

## Delivery responsibility

The implementation agent must inspect the current working tree before editing and preserve unrelated user work. Split bounded work through the actual available supplied agents with explicit scope, clean context and expected handoffs. Use `fork_turns="none"` where the current subagent tool supports the supplied contract.

Required specialist checks include architecture, probability, decisions and missions, localisation, assets, event completion and the independent near-completion improvement loop. A real report belongs in the working-plan folder. A prompt addressed to an agent is not evidence that the agent ran.

All final player-facing prose is written during implementation from the direction in this package. The planning documents must not be copied verbatim into localisation as if their working headings, explanatory notes or acceptance conditions were player text.
