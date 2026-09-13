# Event 021 parent completion audit — 2026-09-02

Status: Needs Testing for the rework catalog state, with acceptance certification incomplete. The release gate remains closed and this document is not a live-game completion certificate.

## Audit scope

This parent audit reconciles the current Event 021 source, acceptance evidence, improvement-loop disposition, Event 006 adapter crosswalk, owned-asset ledger, reused-asset ledger, and workbook export after the final bounded repair pass.

The requested read-only `chaosx_event_completion_auditor` workers were spawned with `fork_context=false`, but both remained in bounded scans and were shut down without producing a durable handoff. This parent audit records the resulting evidence boundary and does not present the absent worker output as a pass.

## Implemented source surface

- `events/021_random_civil_war.txt` owns `chaosx.nr21.1`, the callback events, settlement/reconstruction callbacks, and the two non-major news events.
- The normal decision category is registered in `common/decisions/categories/021_random_civil_war_categories.txt` with one static picture, one category icon, dynamic descriptions, a visible State Authority value, phase-gated actions, and three missions.
- The reusable framework is split across the Event 021 effect, trigger, lifecycle, treaty, successor, evidence, decision, and achievement helpers, with centralized `common/script_constants/021_random_civil_war_constants.txt` tuning.
- Hidden Fracture Pressure and visible State Authority have explicit bands, `N/A` localization fallbacks, recalculation, caps, and cleanup paths.
- Target preparation covers normal-human eligibility, pressure and administration inputs, connected-state planning, viable capitals, protected remnants, reservations, severity, route selection, and no-target skip logging.
- Normal target, scenario target, sponsor, and neighboring-exposure routes apply the shared individual-crisis load cap, and the normal cross-event opening predicate requires the closed-until-ready release flag.
- The six baseline routes are represented: ideological, rival legal, regional, complete Event 006 independence, command schism, and same-tag takeover.
- Opening force and stockpile planning uses bounded connected territory and live equipment, manpower, experience, supply, infrastructure, factory, air, naval, external-war, and severity inputs; no half-army or half-territory split is used as a blind default.
- Actor adapters, front and theater registries, route-specific roles, active and prefire evolution paths, front objectives, neighboring exposure, separate relief and armed-support decisions, sponsor and mediator profiles, strange-incident gating, settlement obligations, recurrence memory, successor grace, cleanup, and bounded global queue handling are source-wired.
- Evolution III uses Stable, Exposed, Fractured, and Critical bands with due-country reviews and a bounded Critical queue. The only all-eligible-country transaction is the explicitly requested Maximum manual scenario.
- Event 004, Event 007, and Event 021 are aligned in the Wars cluster with reservation, collision, skip-reason, and pacing state.
- The Fracture Cascade is registered as scenario ID 18 with four types and four intensities. Maximum has an explicit capacity bypass and fixed eligible pool; no unmeasured seven-day fallback was added.
- Event 021-origin Event 006 setup is separated from Event 006 firing, evolution, network, league, and fired-count state. The Event 006 adapter owns the 32-entry package allowlist and the parent records the separate Event 021 origin.
- Country-local Event 006 focus, category, and aggregate-decision surfaces now use the origin-neutral complete-package predicate where appropriate. Network, league, evolution, adapter-only, and other explicitly global gates remain strict.
- Event Details, Event Logs, evolution records, settlement/reconstruction records, six achievements, AI roles, localization, asset manifests, system documentation, workbook data, and CSV exports are present.

## Asset disposition

The Event 021-owned visual inventory contains 40 unique runtime texture registrations in `interface/021_random_civil_war.gfx`: one report picture, two news pictures, one category picture, one category icon, 11 decision sprites, three mission sprites, three idea sprites, and 18 achievement state sprites.

The owned asset audit decoded the 40 runtime DDS files and compared their decoded pixels with their processed PNGs. All owned paths resolve, all 18 achievement states exist under the engine-facing `gfx/achievements/` root, and the achievement triplet audits are recorded. Two achievement alpha-edge repairs were promoted in v2: `fractals_of_sovereignty_grey` and `the_terms_hold_not_eligible`.

Fifteen older achievement DDS files remain under `gfx/interface/achievements/021_random_civil_war/` as isolated legacy provenance. They are not referenced by the current GFX and are documented as orphaned historical files rather than active assets.

The inherited Event 006 surface is not certified. The current bounded crosswalk identifies 32 admitted packages, 46 current portrait registration rows, 14 shared focus rows, eight shared idea rows, 12 shared decision rows, specialized focus and decision families, shared status/animation assets, formable emblems, and package identity/flag consumers. Ten admitted packages have no current mod portrait row, current portrait source/final-rights status is not accepted, flag and cosmetic-tag paths are not fully re-extracted, several specialized families remain incomplete, and the package-wide consumer render matrix has not been completed.

No grounded portrait was invented, no Event 021 portrait replacement was silently substituted, no custom GUI, animation, super-event, 3D model, or audio package was added, and no runtime reference points into `docs/assets/`.

## Validation evidence

- The final scoped static pass checked 151 relevant source/GFX files for balanced delimiters and unsupported comparator operators, found zero failures, found nine Event 021 entry references, resolved all 40 Event 021 GFX textures, found all 18 owned achievement DDS states, and confirmed the 13-column reused-asset table.
- The Event 006 country API audit passed with 242 broad tags, 191 resolved carriers, zero missing mappings, and zero duplicates.
- The Event 006 scenario matrix passed 32 declared cells and eight edge cases.
- The Event 006 allocator passed with 149 publishers, 138 scenario-selectable packages, 40 runtime adapters, eight adapter-only IDs, 32 content-attested packages, and 29 compatible reservation groups.
- FORM-16 passed its exact member-state, consent, mutation, rollback, and readiness checks.
- The Event 006 flag audit passed 102 registered tags, 102 complete flag families, and zero incomplete families.
- The current narrow `hoi4.event_inspect` lint for `chaosx.nr21.1` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics at revision `d9bc467fb6be1fcf671b83710d9940db0a537ee6023f85a3c12c0a3641c39c05` and graph hash `55ad0cfc2056ed488503d6456c2045e83f5a359d86d65b413c920aa3f7c38bf3`; its current artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/382e0f595eabaf944a65bfe4c12eccdd455af6f230178c10739349c41a33146e/34204580ff469bb55ee1d4b968a44a20ef1423ca75b8a6a79835025b42628f5d/event-lint-d9bc467fb6be.json`. Validation remained false because large-workspace helper and lifecycle projection was deferred. The no-target callback `chaosx.nr21.17` has a matching zero-blocker lint at the same revision, recorded in the acceptance ledger.
- A matching bounded current-revision overview render returned `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics and layout hash `3cf23da1fa05f76b7c4361d9fc375759010e2528fb44bd24566df7de8387ecf8`; its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1047ed552a704b1a8f8ac5856280860554f9e156f9c75248e951bb21088b9a15/3da9b94a83276be8de36f047445d5b3227037cee87c1027276d5b76e0359314d/event-overview-d9bc467fb6be.json`. Partial validation reflects deferred workspace-wide helper/lifecycle analysis, not a selected Event 021 blocker.
- The current shared-cap/release-gate target projection was inspected, evaluated, and compared through `hoi4.probability_*` under the same ten named scenarios. The manifest-backed compare completed with zero unresolved inputs and four expected eligibility changes; the inspect, evaluation, and compare artifacts are recorded in `docs/events/021_random_civil_war/acceptance_evidence.md`. This is target-pool projection evidence only and does not certify the full runtime country registry or the remaining named probability families.
- The matching current Event 021 entry render timed out at the full 180-second MCP limit and produced no artifact. It is not treated as render evidence.
- Focus, map, shared Event Details, targeted decision/mission probability, and selected historical asset evidence are retained in the acceptance document, but none substitutes for the missing current full Event 021 runtime matrix.

## Unresolved completion gates

- Event 021 remains intentionally unavailable because the one-time fail-closed gate initialization clears `random_civil_war_rework_ready` and the reworked-event default allowlist does not enable it.
- The remaining named current-revision probability matrix and same-scenario comparisons for archetype, severity, evolution, strength, recurrence, global queue, cluster, scenario, and the live target-country registry are not fully certified. The new target-pool compare is manifest-backed projection evidence; existing targeted results outside that projection remain partial parent diagnostics.
- The shared candidate-ticket targeting contract is source-wired, but the separate fixed-target companion `apply_individual_crisis_fixed_target_event_pressure` remains undeclared and unconsumed for the fixed-target package owners listed in the shared targeting documentation. No fixed-target load-adjusted probability behavior is claimed.
- Helper-expanded event lifecycle projection, current event-entry rendering, actual war continuity, settlement/recurrence sequences, annexation and successor sequences, save/reload survival, and performance measurements remain unproven without engine-backed evidence.
- The Event 006 32-package Event 021 launch matrix remains pending. Static source audits do not prove every package's runtime identity, leaders, flags, focus access, decisions, formables, AI, force package, cleanup, and postwar playability.
- The inherited visual/provenance audit remains incomplete. In particular, all 46 current portrait rows, ten missing-package portrait surfaces, package flags/cosmetic identities, unresolved formable emblem families, specialized decision/idea families, and package-specific consumer renders remain open.
- The authoritative workbook was reopened and exported after the current source pass. The fresh exports contain 166 Event rows, 20 Cluster rows, and 16 Scenario rows; Event 021 is now `Needs Testing`, the Wars row includes Event 021 at Medium severity, and SCN-018 remains `Needs Testing`. The export hashes are recorded in `docs/events/021_random_civil_war/acceptance_evidence.md` and `docs/plans/021_random_civil_war_plans/subagent_handoffs/spreadsheet_alignment_2026-09-02.md`.
- The final completion-auditor subagent handoff was unavailable because both bounded worker attempts were shut down without writing one. This parent document is an explicit audit record, not an independent worker certificate.
- A final read-only decision and mission auditor was likewise spawned with `fork_context=false`, remained running through the bounded wait, and was shut down without returning a handoff. The parent source review covers the phase-bounded category, mission, cost, AI, and tooltip contract, but no independent specialist certificate is claimed.

## Simplifications, fallbacks, and blockers

- The current implementation uses immediate Maximum scenario setup because no measured one-frame failure exists to authorize a delayed seven-day batch fallback.
- The fixed-target shared targeting adapter is an explicit unimplemented dependency, not a silent no-op or substitute; its package owners remain outside the release certification until it is declared, consumed, and compared.
- The inherited/owned achievement processing history includes a documented local Pillow border-connected alpha fallback for inputs that failed native transparency generation. The fallback is disclosed in the asset manifest and remains subject to user visual review; it is not a silent replacement.
- Inherited Event 006 portraits remain source-placeholder or rights-pending where the available evidence does not authorize promotion. No fabricated grounded replacement was made.
- Fifteen legacy orphan achievement files were preserved for provenance and excluded from current wiring rather than destructively deleted.
- No other silent asset substitute or unreported route omission was introduced. The remaining omissions above are release blockers, not accepted completion simplifications.

## Release recommendation

Do not promote the rework-ready flag, do not expose automatic Event 021 selection, and do not mark The Fracture Cascade as tested until the inherited Event 006 asset/provenance matrix, fixed-target targeting adapter, full probability comparison matrix, helper-expanded/engine evidence, and user-owned consumer checks are resolved.
