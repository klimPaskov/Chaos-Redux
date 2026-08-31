# Event 006 IW-060 KUR force-contract repair handoff

Date: 2026-08-31

Status: COMPLETE for a package-local source repair; KUR remains FAIL-CLOSED for central Event 006 admission.

## Scope

The repair corrects the generation-bound military-tradition receipt in the KUR package trigger and aligns the current KUR documentation. No central adapter, attestation, reservation, planner weight, scenario preflight, deterministic Join, identity receipt, rights decision, portrait, flag, map binding, formable, or pre-event surface was changed.

## Evidence and correction

The accepted IW-060 row in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` specifies the `mountain_frontier` force profile with military tradition score `72`.

The shared force tables are keyed by the numeric package id: `independence_wave_force_package_profile.p60` resolves to `mountain_frontier` (profile value `4`) and `independence_wave_force_package_military_tradition.p60` resolves to `72`. The adjacent p72 row belongs to another package row and resolves to `regular_defectors` with tradition `73`, so the former KUR p72 receipt could never match its own `mountain_frontier` profile and tradition-72 contract after the generic IW-060 loader applied p60.

The KUR prepared-setup trigger now checks p60, matching its package id, profile, and accepted tradition. The package loader already publishes the required `mountain_or_frontier` candidate archetype, so no loader change was needed for KUR.

## Files changed

- `common/scripted_triggers/006_independence_wave_kurdistan_package_triggers.txt`: KUR prepared-setup tradition receipt corrected from p72 to p60.
- `docs/events/006_independence_wave/kurdistan_package.md`: current KUR runtime contract records p60 `mountain_frontier` and tradition 72.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`: current KUR authority records p60 and tradition 72.
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`: current KUR authority records p60 and tradition 72.
- `docs/specs/006_independence_wave_specs/quality/package_manifest.md`: KUR package manifest records p60 and tradition 72.
- `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md`: KUR package boundary records p60 and tradition 72.

## Validation

The focused allocator, country API, and flag validators remain green after the source correction: 149 publishers, 126 automatic/high-chaos selectable candidates, 138 SCN-008-ranked candidates, 40 runtime adapters, 32 attested packages, 29 compatible groups, 102 complete flags, and zero missing or duplicate country API rows. The exact automatic ladder remains 3/4/5/7/10 with World Collapse at 10.

No live or save-load claim is made. The available Event 006 MCP route remains partial and the typed probability compare route remains unavailable, so KUR is not promoted into central admission.

## Remaining KUR gates

KUR still requires a parent-owned choice between the public state-421/Form-18 anchor and the installed state-1001 binding, identity and leadership rights, a rights-cleared Seyid Riza portrait, an accepted institution-specific symbol, Event 005 collision and host-remnant proof, typed probability evidence, central content attestation, deterministic Join, and live engine release evidence.
