# Event 012 world-order decision and mission audit

Status: patched and handed back to the Event 012 parent.

Scope: Actions 85 through 92 and the Action 102 disposition in the existing shared decision, mission, world-order, union, war, and terminal systems.

## Issue list, sorted by severity

1. Resolved critical: the world-package initializer now sets `africa_the_world_super_event_package_ready`, while the two terminal-review decisions, both review openers, and the proof finalizer previously required that readiness flag to be absent.
2. Resolved major: Action 89 was a 540-day epic mission despite the accepted matrix requiring an instant commitment after the long mediation preparation, and changing it to generic instant behavior would have silently removed its partial and failure paths.
3. Resolved documentation disposition: Action rows 85 through 92 still said `blocked_with_gate` after the shared package certification and presentation package became runtime writers, leaving the acceptance ledger contrary to the live lifecycle.
4. Retained accepted disposition: Action 102 remains list-only within the regional-restorations category because it reuses the existing target survey, shared quote, region selector, execute, result, and cleanup lifecycle without creating a second priority-member store or Charter control.

## Changed files and identifiers

| File | Identifiers | Before | After |
| --- | --- | --- | --- |
| `common/decisions/012_africa_decisions.txt` | `africa_world_open_unanimous_union_review`, `africa_world_open_last_standing_review` | The terminal review decisions were hidden whenever presentation readiness existed. | They are visible to the living host and available until political proof completes, subject to existing protocol cleanup. |
| `common/scripted_triggers/012_africa_world_union_war_triggers.txt` | `africa_world_terminal_protocol_can_finalize` | The political-proof finalizer treated a loaded super-event package as a veto. | The finalizer treats presentation readiness as orthogonal and still requires one complete political proof branch. |
| `common/scripted_effects/012_africa_world_union_war_effects.txt` | `africa_world_terminal_protocol_begin_unanimous_union`, `africa_world_terminal_protocol_begin_last_standing` | Both openers rejected an available presentation package and could reopen after the world end. | Both openers work with presentation readiness, but reject a world end and completed political proof. |
| `common/scripted_effects/012_africa_action_effects.txt` | Action 89 profile and `africa_begin_quoted_action_against_target` | Action 89 used an epic mission, and all instant actions were forced full. | Action 89 is instant after Action 86 and rolls its normal high-risk full, partial, or failure result before resolving; all other instant actions retain their prior deterministic behavior. |
| `common/script_constants/012_africa_action_constants.txt` | `africa_action_contract.form_dynamic_two_continent_union_*_days` | Action 89 was 360 to 900 days with a 540-day default. | Action 89 has a one-day instant contract after its preparation. |
| `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` | Rows 85 through 92 | All were stale `blocked_with_gate` rows with unaccepted list-only wording. | All are `implemented` with current lifecycle, cost, target, AI, result, and cleanup evidence. |

## Decision category lifecycle notes

`africa_world_order_actions_category` remains the accepted staged page for Actions 85 through 92, guarded by the existing world-order family selection and world-order, Scramble aftermath, or The World state.

Action 85 selects only an atomically certified external candidate, and its installer remains the sole initial package-install owner.

Actions 86 through 89 target installed package actors through the existing world actor array and share target revalidation with the AI dispatcher.

Action 87 prepares a target-specific war plan and leaves the actual legal declaration to `africa_world_launch_prepared_continental_war`, so planning cannot repeatedly declare war.

Action 90 is a global host action that resolves full only when `africa_terminal_world_identity_can_commit` proves every final gate.

Actions 91 and 92 appear only after The World exists and retain explicit regional administration and high-chaos containment targets.

Action 102 keeps its accepted list-only selector disposition because its target survey must establish the promotion dossier before the shared quote can revalidate and start the action.

## Mission quality notes

| Action | Owner, category, and target | Requirement and duration | Full, partial, and failure result | Duplicate risk and cleanup |
| --- | --- | --- | --- | --- |
| 85 | Africa host, world-order category, certified package candidate | Sponsorship gate, valid candidate, 360 to 900 days, default 630 | Sponsored package, independent package, rival package | The installer removes the candidate and writes one installed actor receipt. |
| 86 | Africa host, world-order category, compatible sovereign package actor | Consent, legitimacy, non-rival status, 540 to 1080 days, default 810 | Union plan, alliance without union, intensified rivalry | Action 89 remains the only union-formation commit. |
| 87 | Africa host, world-order category, reachable rival package actor | Terminal route, target eligibility, 360 to 900 days, default 630 | Prepared war plan, proxy conflict, conditional rival first strike | The launcher clears the plan target before declaring and records one news/super-event receipt. |
| 88 | Africa host, world-order category, defeated package actor | Defeat proof and postwar eligibility, 720 to 1440 days, default 1080 | Submission settlement, armistice, resistance and renewed opponent state | Terminal resolution is counted once only after its proof is valid. |
| 89 | Africa host, world-order category, prepared compatible package actor | Action 86 plan, consent, no terminal war, instant one-day contract | Dynamic union, loose federation, revolt and constitutional review | The union helper selects one cosmetic identity and records one terminal resolution. |
| 90 | Africa host, world-order category, host | Full terminal gate and registered presentation package, instant one-day contract | The World only, no partial substitute, invalid state remains unavailable | Identity formation clears incompatible volatile protocol and world-order state. |
| 91 | The World, world-order category, resolved package region | World end and an unresolved regional administration, 365 to 730 days, default 540 | Administration, protected autonomy, regional revolt | The selected state cursor and live action record clear through the shared resolver. |
| 92 | The World, world-order category, registered hostile high-chaos actor | Live hostile or breach receipt, 360 to 1080 days, default 720 | Contained, truce, continuing disaster | The target persists as an explicit outcome and is never silently deleted. |

## Cost, requirement, AI, and route-lock notes

Each row uses the existing target-aware quote rather than a passive political-power exchange.

Action 85 pays dynamic political, equipment, convoy, civilian, intelligence, target, risk, and duration inputs.

Action 86 uses political, command, civilian, target, risk, and duration inputs, while Action 87 adds manpower, infantry equipment, trains, convoys, fuel, and stability.

Action 88 applies political, command, manpower, infantry, motorized, civilian, war-support, target, risk, and duration inputs.

Action 89 applies political, command, fuel, war-support, target, risk, and instant-duration inputs.

Action 90 applies political and civilian commitment only after its terminal conditions are proven, and it has no fallback terminal result.

Actions 91 and 92 use the existing governance and containment components and retain explicit target and outcome checks.

The AI late-action scorer and dispatcher already contain target paths for every Action 85 through 92, and each path reuses the same candidate, installed actor, valid war target, regional target, or terminal high-chaos target predicate as the player path.

## Localisation and tooltip notes

No new player-facing identifier was introduced, so no localisation key was added.

The existing shared dynamic-cost and duration tooltip reads the per-action quote and contract, so Action 89 now presents the one-day instant commitment instead of the former epic duration.

Action 102 already has an accepted list-only wording and does not need a duplicate selector description or tooltip.

## Cleanup and exploit-risk notes

The review changes preserve the existing terminal political-proof and handoff records, and they prevent a late re-open after either world end or proof completion.

Action 89 remains one action record and resolves immediately, so it cannot hold an epic mission open while retaining a second union attempt.

Action 87 retains a distinct preparation receipt and a launch helper that clears the plan target before declaration, preventing repeated war declarations from the plan.

The current world package, union, successor, exile, breakup, and terminal helpers remain the owners of their respective arrays, flags, targets, and cosmetic identity changes.

## Meaningful validation

Static validation confirmed that the acceptance ledger has exactly nine target rows and reports `implemented` for Actions 85 through 92 and Action 102.

Static lifecycle validation confirmed no remaining `NOT = { has_global_flag = africa_the_world_super_event_package_ready }` veto in the terminal decisions, terminal opener effects, or terminal finalizer trigger.

Static Action 89 validation confirmed its instant profile, one-day contract constants, and the scoped high-risk outcome roll before the shared resolver.

Read-only `hoi4.event_inspect` scan returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostic and produced `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72d78fc2ea626ba8d3c6581083b6d8d6d06d03acc5ca923320b12e072c9232d7/c6a67ff9149609c5381121eaf873a689345947ce9711dbdb05163c29e6930637/event-scan-abcb2d5afb2d.json`.

The MCP report is partial because it deliberately defers workspace-wide helper and lifecycle projections, so it is structural evidence only and not a live gameplay claim.

Live Hearts of Iron IV validation was skipped as directed by the user and repository policy.

## Remaining issues and ownership

No unresolved Action 85 through 92 or Action 102 gameplay gate remains in this audit scope.

The shared world-order source now writes the six-package certification and terminal presentation readiness during initialization, but its older W5 comments still describe those receipts as externally human-owned and not gameplay-written.

That comment contradiction is parent-owned shared world-order documentation cleanup and does not change the now-reachable lifecycle.

The user-directed model deferral still applies only to Actions 74 through 76 and is not a blocker for this world-order tranche.

No fallback package, duplicate target store, new tag, or new decision system was introduced.

No commit was created because this shared worktree contains concurrent Event 012 edits in `common/scripted_effects/012_africa_world_union_war_effects.txt`, including an upstream cleanup addition that is outside this audit's ownership.
