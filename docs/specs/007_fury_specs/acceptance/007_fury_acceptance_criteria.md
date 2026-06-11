# 007 Fury acceptance criteria

## Event identity

Implementation passes only if:

- Event ID `7` is still `Fury`.
- Fury replaces obsolete expansionism behavior.
- Fury is classified as minor repeatable.
- Fury belongs to the Wars cluster.
- event log, event details, debug name, and catalog text align.

## Selection and target safety

Implementation passes only if:

- player countries cannot become Fury through ordinary random event.
- player countries cannot become Fury through triggerable scenario setup.
- ordinary target selection can choose AI or player-controlled countries when they meet normal target gates.
- pure island minors with no practical land neighbor are excluded.
- candidate selection prefers one-state AI minors and broadens only when needed.
- special chaos or non-standard countries are excluded unless explicitly allowed.

## Fury gameplay loop

Implementation passes only if:

- selected Fury country receives the Fury package.
- weekly reinforcement uses a finite hidden reserve pool, consumes one reserve unit per weekly tick, and cleans up.
- each Fury actor's scripted reinforcement reserve is capped at 100 total divisions granted.
- weekly free spawning stops completely when the reserve pool reaches zero.
- focus and decision unit rewards are one-time direct spawns, not sources for the weekly reserve loop.
- first target is selected dynamically.
- Fury declares on a weaker eligible neighbor without warning.
- first conquest news fires when the first neighbor is defeated.
- conquest settlement adds compliance and overextension.
- coring requires decisions, compliance, control, and concrete costs.
- Fury repeats target selection after victory.
- Fury stops or enters no-neighbor branch when no valid target exists.
- Fury cleanup runs when the country capitulates.

## Evolutions

Implementation passes only if:

- Evolution I upgrades unit quality, reserve size, idea, and focus content within capped limits.
- Evolution II allows two Fury actors and cooperation or rivalry mechanics.
- Evolution III allows three Fury actors and all-neighbor declarations.
- active-event evolution affects existing Fury actors immediately.
- pre-fire evolved opening changes future Fury setup.
- disabled evolutions do not unlock their content or set recorded flags.

## Focus tree

Implementation passes only if:

- shared Fury focus tree exists.
- tree has opening trunk, army, expansion, occupation, cooperation, rivalry, evolution, and world-end branches.
- branches are non-linear enough to be meaningful.
- rewards are varied and not mostly political power or tiny modifiers.
- focus AI respects pact, hostile, evolution, target, and overextension state.
- focus icons are assigned or registered as placeholders with asset handoff.

## Decisions and missions

Implementation passes only if:

- Fury War Office decision category exists.
- decisions use concrete costs beyond political power where appropriate.
- target, settlement, reinforcement, coring, cooperation, rivalry, and no-neighbor families exist.
- anti-Fury response appears after major-Fury or world-end threshold.
- missions require real map action where used.
- stale target and state decisions clean up.

## Triggerable scenario

Implementation passes only if:

- scenario name is `The World in Fury`.
- scenario has Low, Medium, High, and Maximum intensity.
- scenario has Fury Pact and Hostile Fury type options.
- Low creates two Fury actors when safe.
- Medium creates five Fury actors when safe.
- High creates nine Fury actors when safe.
- Maximum creates up to sixteen Fury actors when enough safe candidates exist.
- scenario excludes player.
- scenario launch reads selected type and intensity at confirmation.
- scenario intensity changes initial army size and reserve pool size, not infinite weekly spawning.
- triggerable scenario actors still use the same per-actor 100 reserve cap and one-unit weekly draw cadence.
- scenario setup bypass flags are cleared after setup.

## Super-events and news

Implementation passes only if:

- first-conquest news event exists.
- Fury-major super-event exists.
- World in Fury world-end super-event exists if terminal branch is implemented.
- super-event image, text, quote, audio id, audio file, and docs align.
- quote and audio sources are verified in super-event docs.
- no placeholder or undocumented super-event audio is claimed final.

## World-end

Implementation passes only if:

- Fury world-end branch is separate from the triggerable scenario.
- branch requires terminal eligibility.
- branch sets world-end state and Fury-specific flag.
- branch creates or strengthens main Fury faction.
- branch seeds Fury actors in other continents.
- branch marks Fury as world threat source.
- terminal targeting rules warn before player can be threatened.

## Assets

Implementation passes only if:

- idea, decision, focus, achievement, news, report, super-event, faction emblem, and optional leader portrait asset needs are tracked.
- generated or sourced assets follow source-mode rules.
- final assets are processed, converted to DDS, moved, documented, and wired.
- placeholder sprites are reported as placeholders if used.

## Achievements

Implementation passes only if:

- achievement conditions are implemented or explicitly queued.
- achievements disqualify player-as-Fury exploit.
- scenario achievements read scenario intensity and type.
- achievement icons are planned and wired.

## Documentation and spreadsheet

Implementation passes only if:

- event documentation is updated.
- triggerable scenario docs are updated.
- event catalog spreadsheet row for Event 007 is updated.
- event details and spreadsheet wording match.
- simplifications, blockers, or queued items are reported clearly.

## Simplification rule

The implementation is incomplete if any requested surface is omitted without reporting it. This includes missing evolutions, missing scenario type, missing maximum-spread setup, missing finite reinforcement reserve caps, missing focus branches, missing coring decisions, missing super-event direction, missing AI, missing documentation, or missing asset handoff.
