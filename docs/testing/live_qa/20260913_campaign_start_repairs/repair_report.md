# Campaign-start error and Scientists popup repair

Status: source repairs implemented and reviewed; campaign runtime not executed.
The user requested fixes for the pasted campaign-start errors and the unrequested Scientists window, with the persistent prohibition on Astra subagents and computer control.
This report covers the new runtime batch separately from the earlier main-menu startup verification.

## Reported faults and changes

The attachment contains 7,166 error lines in eight distinct diagnostic groups from January 1–3, 1936.
`user_error_batch.json` retains the exact attachment hash, timestamps, messages, and repeat counts.

| Surface | Fault and correction | Evidence |
| --- | --- | --- |
| Camp startup | One `camp_occ_historical_setup` call ran from the None-scoped startup hook. It now runs inside the existing country selection after migration and CXT registration. | `camp_scope_handoff.md`; original byte backup; unchanged historical actors, state scans, and idempotence guards. |
| Missile state gates | 3,915 evaluations used Country-only `exists` on a State. Eight State helpers now use documented `scope_exists`; Country helpers retain `exists`. | `missile_scope_handoff.md`, `missile_scope_receipt.json`; reversing the eight substitutions restores the original source. |
| Murder-mystery decisions | Five availability predicates accessed the global assassin-country target before its creation, producing 1,625 invalid-target lines and 1,625 undefined-target lines. Six ordinary availability guards cover those five sites and the same direct-target risk in the high-value operation. | `assassin_target_handoff.md`, `assassin_target_parent_review.json`; unwrapping all six guards restores every original byte. |
| Scientists popup | The copied reference-capture roster was registered in player context with an unconditional true visibility gate. Its capture binding now has an unconditional false gate. | Original user image, baseline binding, before/after MCP inspection and preview artifacts, `scientist_preview_comparison.json`. |

## Source and behavior contracts

The Scientists panel is `capture_scientist_scientist_roster_window`, linked by `capture_scientist_roster` in `common/scripted_guis/reference_capture_fixtures.txt`.
The exact title, instruction text, list geometry, search control, and recruitment button identify it as the panel shown in the user image.
The interface definition remains byte-identical.
Installed vanilla scripted-GUI bindings and the offline Interface and Scripted GUI modding pages are the syntax precedents.
The gameplay scientist roster remains owned by its existing native controls.

The camp correction retains one existing country selection, the migration/registration order, 21 fixed historical origin calls, GER/JAP controlled-state scans, and existing one-shot guards.
The origin helpers use their fixed country scopes and locally nested PREV relationships; the selected outer country does not replace an origin or controller.
The existing camp helper documentation records its concrete invocation requirement.

The parent accepted the decision worker's five guards and applied the same required-target guard to `murder_mystery_order_high_value_operation` after its residual risk was identified in the handoff.
The high-value decision retains its leading selected-cell maturity requirement and its exact target-present predicates.
All other decision-source bytes, including AI blocks, cost fields, effects, and mission/cancellation gates, are unchanged after unwrapping the six guards.
The assassin target is created only after the existing transaction commits and is cleared by the existing final cleanup; no substitute target or additional lifecycle flag was added.

Installed `documentation/triggers_documentation.md` documents `exists` as Country-only, `scope_exists` as any-scope, `has_event_target`, and `if` as a conditional trigger.
The offline trigger table explicitly permits nested `else` and documents that a conditional trigger without a matching branch returns true, making the false branch necessary for required-target availability.
Vanilla `common/decisions/INS.txt` guards an optional event target through an `if` limit before using it.

## GUI evidence and limits

The preserved baseline MCP source revision is `50071e1af9c12aea8c5b71f1170f839a7ced7b1e48e93aa6109e2cf49f0e1e0c`; the after revision is `98c83bd7dc32358b0bb248a4675b32019c1691e4c7426f11817ed9c907441088`.
Both selected binding expressions were inspected directly: `{ always = yes }` before and `{ always = no }` after.
At 1920×1080 and UI scale 1, the baseline contains 14 visible elements and four visible clickable controls; the after scene contains zero of either.
Full, cropped, annotated, hierarchy, click-region, state, resolution, validation, fidelity, and scenario evidence is retained with verified artifact hashes under `gui/before/` and `gui/after/`.
The parent reviewed the baseline crop against the user image and the blank after full-window preview.
The selected fixture binding and interface files remain unchanged after this GUI capture; later changes to the separate murder-mystery decision source do not alter this window or its unconditional visibility gate.

The offline renderer requires explicit scenario visibility inputs rather than executing the scripted-GUI visibility expression.
The after input is derived from the inspected unconditional false source gate.
The render comparison scenario represents the old true gate using the unchanged window definition; it is not an automatic older-source snapshot.
No hidden fixture is accepted as a visible production interface.
The source graph retains nine diagnostics in the dormant capture definitions, so global GUI validation is not claimed to pass.
The actual hidden after scene has no visible layout defect or click interception region.

## AI audit evidence and limits

The read-only Luna probability auditor inspected the preserved baseline and final six-guard decision source, then compared the same six candidate scores in three declared scenarios: `MM_START_ASSASSIN_TARGET_ABSENT`, `MM_ASSASSIN_TARGET_READY`, and `MM_ASSASSIN_TARGET_LOW_PP`.
The parent reviewed the authoritative comparison JSON: adapter and assumptions unchanged, no scenario score changes or regressions, and no diagnostics or unresolved inputs within that fixture.
The missile helper inspection reported `no_weighted_surfaces`; the ten consuming missile decision AI bases, modifiers, and zero-score gates remain source-identical.
The decision byte-reversal receipt independently establishes that all original AI arithmetic, costs, and effects remain unchanged.
`probability_audit_handoff.md` records source revisions, exact artifacts, and the audit contract; the comparison JSON, inspection JSON, and rendered evidence are retained under `probability/` with content and provenance records.

The successful comparison uses explicit eligibility and candidate overrides to isolate unchanged AI arithmetic in a complete six-candidate score fixture.
It does not establish actual normalized selection probability or the full decision pool: the final source adapter discovers 29 candidates, reports an incomplete pool, and requires 13 external inputs.
The first baseline-path comparison returned `PROBABILITY_SURFACE_EMPTY`; the auditor supplied the preserved baseline source inline for the successful comparison.
Target eligibility is source-derived and declared in those scenarios rather than evaluated by a running campaign.

## Simplifications, omissions, and blockers

No gameplay simplification or substitute mechanic is introduced by these repairs.
The source fixes and deterministic previews do not establish that a fresh campaign emits zero errors.
HOI4 was not launched or controlled for this campaign report.
Camp MCP helper projections were deferred, selected scope renders contained zero nodes, and comparison rejected the event graph artifact schema; those routes do not validate the repaired runtime scope.
The GUI visibility mock and probability candidate overrides are bounded audit projections, not substitutes for campaign runtime evidence.

## Skills and Git disposition

Used the subagent and scripted-GUI skills; the decision owner applied the decisions/missions skill, and the camp owner applied the relevant event/script guidance.
Used the official skill-creator guidance for one reusable addition to `chaos-redux-scripted-gui`: capture bindings must default inactive during gameplay.
No event-specific content was added to a skill.
The selected workers use Sol and Luna; no Astra worker was spawned or resumed.
Original source bytes and the task-only logical patch are retained separately from the repository's overlapping user drafts.
The four gameplay files, existing camp helper documentation, and one skill file are the six modified source paths recorded in `source_repair_inventory.json`.
The existing untracked or overlapping source drafts remain in the shared working tree; their exact task-only changes are preserved by the committed logical patch and byte/hash inventory rather than staging whole user drafts.
The tracked skill addition contains only the capture-fixture safety rule introduced by this task.
The task-owned repair evidence and skill addition are committed separately after review.
