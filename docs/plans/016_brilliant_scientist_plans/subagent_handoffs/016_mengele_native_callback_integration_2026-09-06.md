# Event 016 four-family native callback integration

## Disposition and authority

Disposition: implemented in current source; engine callback and full portfolio acceptance remain unresolved.
The parent accepted the minimal strict-owner dispatch described in `016_mengele_native_callback_audit_2026-09-06.md` after the read-only audit identified missing private receipts in four reused native families.
The parent confirmed that the no-DLC reviewer's shared-file scope excludes the completion hook and applied the exact reviewed patch after notifying that reviewer.
Existing-file `apply_patch` calls from this subagent failed twice without changing gameplay source; parent-side application succeeded.
The exact review payload remains `016_mengele_native_callback_2026-09-06.patch` in this directory.
No files were staged or committed and no native project definitions were edited.

## Files and helper contract

- `common/scripted_effects/016_mengele_project_stage_effects.txt:1336`: added `brilliant_scientist_mengele_reconcile_reused_native_project_prototypes`.
- `common/on_actions/016_brilliant_scientist_project_on_actions.txt:20`: added the separate strict-Mengele `else_if` branch, calling the new helper at line 22.
- `common/scripted_effects/016_mengele_project_stage_effects.md`: documented scope, authentication, cleanup, and native completion entry point.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_mengele_native_callback_audit_2026-09-06.md`: exact prepatch source inventory, native result/helper paths, accepted narrow design, and source references.
- This integration handoff and the review payload record application and validation evidence.

The new helper runs in country scope, has no parameters, and does nothing unless `brilliant_scientist_mengele_project_stage_provider_is_valid` succeeds.
Its inputs are private Theory/Prototype flags and country-scope completed native project identities.
It selects Electronics, Rocketry, High Energy, and Biological Weapons one at a time using existing shared family constants, then invokes `brilliant_scientist_mengele_record_native_project_prototype` for each.
That API independently authenticates matching Theory and native completion before the existing output predecessor rejects any repeated Prototype grant.
Its outputs are the eligible private Prototype flags and the already-existing directorate presentation flags/modifiers.
Every recording call clears private family/stage/index selectors and output authorization.
No shared family selector, Kruger Capacity, Kruger history, payment receipt, or resource balance is changed by this reconciliation.
No constants, tuning, event targets, periodic hook, world scan, native output replay, or special-project completion effect was added.
No migration is required: this is an additional call site for the existing authentic private receipt API, not a changed receipt schema.

The current-host branch still calls only `brilliant_scientist_sync_native_project_prototypes` and `brilliant_scientist_capture_biological_agent_history`.
It is not broadened to private owners.
The ten ordinary native Event016 definitions that already call the owner-aware shared wrapper remain intact.
The separate Singularity registry and the shared no-DLC board remain under their existing owner.

## Current parsed-disk scenario evidence

An in-memory JavaScript Clausewitz subset interpreter parsed the actual files after the parent applied the patch, including the completion hook, private effects, private triggers, and numeric shared constants.
The tests execute the actual strict provider trigger body; country existence, directorate identity, active-program aliases, idea membership, global flags, and completed-project membership are explicit fixture inputs.
Native completion status is represented by a set of abstract `sp:<id>` tokens, not by simulated native project outputs.
Modifiers are represented by their identifiers, and the two original Kruger helper calls are recorded as dispatch boundaries instead of simulating their internal ledger.
This is source-model evidence, not HOI4 execution or MCP engine evidence.

| Scenario | Observed result |
| --- | --- |
| Strict active owner, matching private Theory, each of the ten accepted native IDs separately | Exactly the matching family's private Prototype was recorded in every case |
| Repeated notification for each of those ten fixtures | Persistent flags, receipt arrays, modifier identifiers, resources, and shared selectors/history sentinels remained unchanged |
| Each of the four families with Theory but only an unrelated completed project | No Prototype output |
| Each family with its accepted native completion but without Theory | No Prototype and no fabricated Theory |
| Inactive, closed, defeated, rejected, expired, recently expired, incident-locked, missing-registry, world-terminal, or conflicting-host owner | No private output and no Kruger dispatch |
| Current Kruger host with native completions | Exactly the original two host helpers were dispatched, and no private Prototype was recorded |
| All ten accepted native projects complete in one notification with all four Theory receipts | All four private family Prototypes recorded once, with no skipped family |
| Repeat of that multi-family notification | Persistent no-op |
| Every pre-existing private scripted-effect body compared with prepatch source AST | Identical; only the added reconciliation helper differs |

For every eligible private fixture the shared selector, Capacity, and history sentinels remained at their distinct seeded values, direct resources were unchanged, and private family/stage/authorization selectors were cleared.
The exact native IDs and output paths are in the audit inventory; the vanilla Jet definition is `common/special_projects/projects/air_projects.txt:793`, with `project_output` at 837.
Biological IDs were tested only as abstract identity tokens, without modeling their native gameplay result branches.

## Source SHA-256 at validation

| Source | SHA-256 |
| --- | --- |
| `common/scripted_effects/016_mengele_project_stage_effects.txt` | `E303B6AF9AD26502DCE339AB240F252CF1EF9CADCE4EE2FECA9CC329E42EC4AA` |
| `common/scripted_triggers/016_mengele_project_stage_triggers.txt` | `9990812298092939C45070ACBE111F8C0D4248596B9648412019D04201B312AF` |
| `common/on_actions/016_brilliant_scientist_project_on_actions.txt` | `5EABC430BB938288035172A362AC5F0F96AD25187C04ED6B1FA45C34BC8E7DFA` |

The unchanged trigger hash also identifies the exact native-authentication and strict-owner predicates tested here.
These hashes identify this bounded validation revision; concurrent later edits require their own review.

## Engine evidence, omissions, and remaining work

No additional identical MCP retry was made, per the parent's instruction after two 180-second failures.
The earlier `chaosx.nr16.901` state_flow attempt used depth 2, 20 nodes, 30 edges, and helper expansion; the following trace used depth 1, 10 nodes, 15 edges, and no helper expansion.
Neither produced a current artifact or revision, and source modeling does not replace the missing engine lifecycle/render/compare evidence.
The scope precedent remains the offline On actions page and installed vanilla `12_wuw_on_actions.txt:1782`: ROOT country, FROM project.
Native completion status visibility during the hook and hook firing/order for scripted `complete_special_project` remain unverified engine behavior.
The patch preserves the existing completion-status authenticity semantics and does not equate that status with a successful operational result from every native alternative result branch.
It does not add a scheduler to backfill native completions that predate private Theory; the private receipt still requires an eligible completion reconciliation.
No fallback or simplification was introduced into the accepted receipt contract.
Full portfolio presentation, non-Computation paid adapters, public/native output consumers, Biological Weapons and Singularity late-stage outputs, and broader engine evidence remain incomplete and outside this bounded callback patch.
No icons, localisation, GUI, assets, models, weights, focus routes, or technology-tree layouts changed.
The events and subagents skills governed the source/owner boundary and evidence separation; no skill was created or updated.
