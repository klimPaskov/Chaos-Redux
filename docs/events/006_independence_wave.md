# Event 006: Independence Wave

## Purpose

Independence Wave is the Minor Repeatable member of the Liberations cluster. It releases a frozen, collision-free set of countries as one synchronized incident and then gives every Event 006 origin a persistent founding-state simulation rather than a one-time release reward.

The accepted design authority remains `docs/specs/006_independence_wave_specs/`. This file is the implementation-facing map for the live script surfaces and is updated as each plan tranche is completed.

## Release transaction

The shared Liberations coordinator owns the transaction lifecycle:

1. Begin an Event 005, Event 006, or joint plan.
2. Reserve country tags, reservation groups, exact states, hosts, and one protected state per host.
3. Reject living tags, active origins, duplicate anchors, occupied reservation groups, and state collisions.
4. Trim optional territory before rejecting a package.
5. Revalidate aligned rows, ownership, host survival, and exact counts at lock.
6. If a host capital is a frozen release row, move it to that host's protected state before ownership changes.
7. Execute all accepted rows in one effect chain and commit only after every Event 006 country initializes.

`chaosx.nr6.1` is the hidden repeatable dispatcher. On a standalone firing it captures tuning, opens the shared plan, allocates the exact automatic count, executes the frozen Event 006 contribution, and dispatches the public report only after commit. During a joint Liberations firing it consumes `independence_wave_joint_presentation_pending` and presents the already committed result without planning or releasing a second time. Any standalone failure before ownership mutation restores the original-capital ledger, clears Event 006 reservations, and aborts without a report. A failure after execution begins is recorded as non-rollbackable and is never presented as success.

The automatic wave counts are 3, 4, 5, 7, and 10. World Collapse remains at 10; its force level, instability, package rarity, and regional ambition change instead of its country count.

## Origin separation

`liberation_origin` is the active-origin enum. Event 006 countries use `independence_wave_active_origin` and the Independence Wave enum value. Event 005-created republics and high-chaos successors use `soviet_collapse_active_origin` and the Soviet Collapse enum value. Historical creation flags remain available after annexation, while the active contract is cleared by the owning event's end path.

A later resurrection receives the origin of the event that recreates it. Historical Event 005 flags therefore do not permanently exclude an absent tag from Event 006; a living or still-active Event 005 origin does.

## Country state

Every active Event 006 generation stores:

- package, region, archetype, territory level, force level, anchor, former host, origin date, and generation ID;
- Legitimacy, Recognition, State Capacity, Security, and Founding Instability on visible 0–100 scales;
- Emergency Founding, Provisional State, Recognized State, and Regional Power progression;
- government route, bilateral host outcome, network standing, patron ledger, and idea lifecycle stages.

The generation ID is part of active-country, host, patron, network, league-founder, league-member, and history row identity. Registry reconciliation removes dead, duplicate, ended, or stale-generation rows and derives public counts from the surviving arrays.

## Former-host relationship

The released country owns eight bilateral values, mirrored to an aligned former-host ledger:

- claim intensity;
- hostility;
- obligations;
- property dispute;
- population dispute;
- border settlement progress;
- host domestic pressure;
- reconquest fear.

Host death records Host Collapse and removes only the bilateral mirror. It does not end Event 006 origin. Annexation, voluntary reunion, formable absorption, and dissolution use the separate active-origin termination API.

## Patron, network, and league state

Patron rows store the patron country, owner generation, total influence, aid value, and nine channel values. Dead, stale, and empty rows are reverse-pruned before strongest-patron and dependency checks.

The informal network and league registries use country plus generation as their authoritative key. League transitions have exact source phases, idempotent dates, and mutually exclusive phase flags. Network exit cascades founder and member removal; league exit preserves the informal network and active origin.

## Idea lifecycles

The mechanics foundation currently defines visible starting, mitigation, mature, and failure spirits for:

- government administration;
- diplomatic recognition;
- military command;
- borders and the former host;
- patron pressure;
- founding instability;
- league membership.

Fourteen regional identity ideas provide the base overlay. Package-specific identity progression and route institutions are implemented by the focus/package tranches and must not be replaced with a generic political identity.

## Asset wiring

Runtime sprites are registered in `interface/006_independence_wave.gfx`. The idea pictures used by the mechanics foundation are:

- `independence_wave_improvised_government`;
- `independence_wave_unrecognized_state`;
- `independence_wave_fragmented_command`;
- `independence_wave_unsettled_borders`;
- `independence_wave_patron_pressure`;
- `independence_wave_post_release_instability`;
- `independence_wave_league_membership`;
- `independence_wave_founding_identity`.

Generated report, news, and super-event scenes are registered in `interface/006_independence_wave_event_pictures.gfx`. The committed wave report uses `GFX_report_event_006_asset_001_wave_summary`; its displayed wave, country, region, host, armed-state, and earlier-network facts are copied into a presentation ledger before the plan can be reset.

Final source, processed PNG, DDS, provenance, contact-sheet, and animation records live under `docs/assets/006_independence_wave/`. Animated league, route, and high-chaos pieces require genuine frame sequences plus static fallbacks and are wired through the same interface file and the relevant scripted GUI surface.

## Implementation surfaces

- Shared transaction: `common/scripted_effects/chaosx_liberation_release_effects.txt` and matching triggers/constants.
- Country mechanics: `common/scripted_effects/006_independence_wave_effects.txt`, matching triggers/constants, and `common/ideas/006_independence_wave_ideas.txt`.
- Package allocation and execution: `common/scripted_effects/006_independence_wave_package_*` and `006_independence_wave_execution_effects.txt`.
- Event delivery, evolutions, Event Details, logs, scenario, focus, decisions, AI, formables, achievements, localisation, super-events, and asset registration are recorded here as their plan-scoped commits land.

## Future depth after accepted implementation

After the accepted specification is complete, useful extensions include additional negotiated federations, more bilateral border-settlement outcomes, region-specific league institutions, and campaign-memory reactions to resurrected tags. These are future suggestions, not substitutes for any accepted Event 006 package, route, scenario, asset, achievement, or evolution.
