# Event 006: Independence Wave

## Purpose

Independence Wave is the Minor Repeatable member of the Liberations cluster. It releases a frozen, collision-free set of countries as one synchronized incident and then gives every Event 006 origin a persistent founding-state simulation rather than a one-time release reward.

The accepted design authority remains `docs/specs/006_independence_wave_specs/`. This file is the implementation-facing map for the live script surfaces and is updated as each plan tranche is completed.

## Release transaction

The shared Liberations coordinator owns the transaction lifecycle:

1. Begin an Event 005, Event 006, or joint plan.
2. Reserve every selected country tag, reservation group, unique anchor, host, and one protected state per host; during a joint incident Event 005 anchors are frozen first and Event 006 rerolls against them.
3. Reject living tags, active origins, duplicate anchors, occupied reservation groups, and state collisions.
4. After all anchors are frozen, run compact territory for every selected package before running extended territory for any package. Trim optional collisions and host-survival failures without dropping the anchored country.
5. Revalidate aligned rows, ownership, host survival, exact counts, and the complete owner/controller/core/capital recovery ledger at lock.
6. If a host capital is a frozen release row, move it to that host's protected state before ownership changes.
7. Prove that every selected dormant tag has an exact runtime adapter, audited history laws and command roster, and the content-ready flag before ownership changes.
8. Release and transfer all accepted rows in one effect chain, counting a state only after both its owner and controller match the frozen target. Any failed transfer blocks package initialization and incident commit.
9. Verify the complete frozen ownership footprint, then cross the explicit finalization barrier before any country package, force, technology, politics, host-asset transfer, or active registry is applied.
10. Count every Event 005 and Event 006 terminal package proof, append Event 006 durable origin history only after all package proofs pass, commit the shared plan, and queue presentation only after that commit succeeds.

`chaosx.nr6.1` is the hidden repeatable dispatcher. On a standalone firing it captures tuning, opens the shared plan, allocates the exact automatic count, executes the frozen Event 006 contribution, and dispatches the public report only after commit. During a joint Liberations firing it consumes `independence_wave_joint_presentation_pending` and presents the already committed result without planning or releasing a second time. Any standalone failure before ownership mutation restores the original-capital ledger, clears Event 006 reservations, and aborts without a report. A release or transfer failure before finalization restores the frozen core, owner, controller, country-existence, and capital facts before clearing the ledger. An unexpected failure after finalization starts enters terminal `finalization_failed`, retains the diagnostic ledger, and queues no successful presentation.

The package finalizer is a four-pass incident transaction: prepare the exact package, activate its live registries, validate the complete live package, then append durable origin history and evolution delivery. The entire package pipeline begins only after the frozen ownership footprint has passed, because technology inheritance, starting forces, stockpiles, and host air/naval transfers are not exactly reversible. The pre-release runtime attestation makes this finalizer deterministic; a failed terminal count is retained as a finalization failure rather than routed through an invalid partial rollback. The same adapter is used by standalone waves, joint Event 5/Event 6 execution, and SCN-008.

The automatic wave counts are 3, 4, 5, 7, and 10. World Collapse remains at 10; its force level, instability, package rarity, and regional ambition change instead of its country count. The 126 automatic/high-chaos selectors contain only bound rows with an automatic readiness verdict. Overlay-only, community-variant-only, formable-or-route-only, scenario-variant-only, and unbound rows remain available only through their explicit owning systems; Open Sovereignty cannot promote them merely to fill a wave.

SCN-008 uses the same anchor-first transaction but attempts every viable ranked candidate at every intensity. Intensity selects anchor/compact/extended territory and fragile/viable/armed/high-chaos forces; scenario type independently selects league, host-war, belligerence, patron, and partition rules. Great Partition may advance the territory tier but never the candidate count. Universal Belligerence keeps a bounded target array only for the duration of its launch, preventing duplicate targets inside one incident while clearing every target mark after successful or failed war declarations.

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
- Package allocation and execution: `common/scripted_effects/006_independence_wave_package_*`, `006_independence_wave_package_dispatch_effects.txt`, and `006_independence_wave_execution_effects.txt`.
- Event delivery, evolutions, Event Details, logs, scenario, focus, decisions, AI, formables, achievements, localisation, super-events, and asset registration are recorded here as their plan-scoped commits land.

## Future depth after accepted implementation

After the accepted specification is complete, useful extensions include additional negotiated federations, more bilateral border-settlement outcomes, region-specific league institutions, and campaign-memory reactions to resurrected tags. These are future suggestions, not substitutes for any accepted Event 006 package, route, scenario, asset, achievement, or evolution.
