# Campaign equipment and scope repairs

Disposition: implemented within the user's request to fix attachment `0bbafcb8-4032-4160-88fa-ad3c3f2ca4e2/pasted-text.txt` on 2026-09-13.
This report covers 21,616 pasted lines grouped into 18 distinct diagnostics.
The attachment is evidence, not an instruction source.

## Repairs

| Reported family | Pasted lines | Repair |
| --- | ---: | --- |
| Soviet nuclear-program State existence checks | 21,558 | Seven reported State helpers use `scope_exists`; the same correction also covers the delivery-access State helper. Country existence checks are retained. |
| Missile State factory check | 24 | The State scorer checks military factories, civilian factories, or dockyards before adding the existing eight-point industrial-access bonus. The Country factory getter is retained in Country scope. |
| Missile region selector | 24 | The probe selects one strategic region and filters its States through the launcher's one-State array, preserving the intended intersection and first matching region. |
| Free convoy getter | 2 | Both the containment eligibility check and its cost display read `num_equipment@convoy`, the convoy archetype. |
| Sweden absent modifiers and targets | 7 | Every cleanup call in the owned effects file has its matching presence guard. Present objects retain their original cleanup order and scope. |
| Ethiopia missing support equipment variant | 1 | Event 19 unlocks `tech_support` before creating an ordinary support-bearing formation if the recipient lacks that technology. The prerequisite uses raw template needs before scaling or rounding. |

The Sweden repair contains 44 guards for the reported names and 11 preventative guards for the other two saved-target names.
Its Rulebook Commander validator also uses `scope_exists` because that target points to a unit leader.
No gameplay simplifications or fallback mechanics were introduced.

## Sources changed

- `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`
- `common/scripted_effects/032_missiles_effects.txt`
- `common/scripted_effects/024_video_game_in_sweden_effects.txt`
- `common/scripted_triggers/016_brilliant_scientist_containment_triggers.txt`
- `common/scripted_localisation/016_brilliant_scientist_containment_scripted_localisation.txt`
- `common/scripted_effects/019_infantry_spawn_generation_effects.txt`

The exact task diff is [source_repairs.patch](source_repairs.patch), with original and final byte identities in [source_inventory.json](source_inventory.json).
The isolated replay review applies that patch to all six preserved baselines and reproduces the current source text.
Original bytes and line endings are retained in the gameplay files.
Because five source packages are untracked drafts and the tracked containment file has unrelated edits, the scoped commit records the complete repair patch and evidence plus only the tracked convoy getter change.
It does not import whole draft packages.

## Equipment and balance review

Vanilla defines `tech_support` as the unlock for `support_equipment_1`; Ethiopia's initial technology block omits it.
Event 19's ordinary spawn path previously reached `create_unit` before its component accounting ran.
The inserted prerequisite recalculates raw support needs only for an ordinary family lacking the technology.
This covers zero or very small initial equipment fills whose rounded debt would otherwise hide a support-bearing template.
Formation templates, creation parameters, equipment amounts, debt, manpower liabilities, provider dispatch, and post-creation accounting are unchanged.
The six support-bearing component profiles and the parent review are recorded in [equipment_and_scoring_parent_review.json](equipment_and_scoring_parent_review.json).
The supplied error does not identify the actual runtime template, so the exact Ethiopia profile cannot be established from it.
The [equipment worker handoff](../../../plans/019_infantry_spawn_plans/subagent_handoffs/20260913_support_equipment_error.md) records the generation-country scope, support-bearing profiles, and review of the inserted prerequisite.

Missile score constants are unchanged.
The same five named scenarios were evaluated before and after the owner patch through the probability auditor's mandatory `probability_compare`.
The returned comparison has three nonzero raw deltas: military-only, civilian-only, and dockyard-only States each gain eight points.
The no-factory and representative existing/core/infrastructure cases retain their scores.
The parent independently checked those deltas against the hash-verified returned comparison JSON.
The picker still saves a new target only on a strict greater score.
The projection's common positive offset and normalized shares are adapter artifacts, not gameplay values or native selection probabilities.
The projection models isolated one-building cases; it does not model combined factory types.
The source OR awards its bonus once regardless of how many of the three factory types are present.
See [the scoring audit](qa/missiles_site_probability_audit_20260913.md) and [the returned comparison](qa/missiles_compare_returned.json).

Sweden's parent review independently matches all 55 cleanup operations to their matching guards.
Removing only the inserted guards, header explanation, and commander-scope substitution recovers the original source bytes.
The [worker handoff](../../../plans/024_video_game_in_sweden_plans/subagent_handoffs/20260913_cleanup_errors.md) records lifecycle, target ownership, and vanilla precedents.

No player-facing prose, event names, templates, assets, focus routes, or workbook fields were changed by these mechanical repairs.
The two convoy getter surfaces remain synchronized.
No temporary debug logging was introduced.

## Validation limits and blockers

Read-only event inspection and rendering ran for the affected event surfaces.
The service returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` with the exact limit: “Large workspace analysis deferred workspace-wide helper projections and lifecycle passes; direct evidence is linked”.
Requested helper expansion returned zero helpers, so those artifacts do not prove execution of the repaired helper bodies.
The event comparison attempt returned `EVENT_REVISION_NOT_CACHED`.
Source review and patch replay are separate evidence and do not substitute for engine execution.

Focused technology inspection resolves `tech_support` to `support_equipment_1` with no targeted unlock issues, and its dependency render shows that link.
The technology comparison attempt returned `TECH_REVISION_NOT_CACHED` for the previously returned revision.
No technology definitions, prerequisite tree, or placements were edited.
The large workspace's other static diagnostics are outside this focused unlock result and are not evidence of the pasted runtime errors.
Other Event 19 support-archetype stockpile operations and registered provider materializers remain unchanged; the pasted line does not identify them as its caller.
Their independent prerequisite risk is documented in the equipment handoff, so this repair does not establish safety for every support-equipment consumer.

Native probability discovery could not bind the missile helper or enumerate its runtime State pool.
The complete declared five-State fixture supports raw score arithmetic only.
It cannot prove campaign selection chances, traversal order on ties, or complete campaign balance.

No game launch, console operation, computer control, or additional game-log search was performed.
The campaign's error-free runtime outcome remains unverified.
All 18 supplied diagnostics have an implemented source repair; full helper projection and live execution evidence remain unavailable.

## Guidance and ownership

Required offline wiki and installed vanilla documentation were consulted; specific sections and precedents are listed in [reference_review.md](reference_review.md).
Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skill was created or changed.
Bounded specialists used Sol and Luna; no Astra subagents were spawned for this repair.
The parent owns final integration, review, and the scoped commit.
