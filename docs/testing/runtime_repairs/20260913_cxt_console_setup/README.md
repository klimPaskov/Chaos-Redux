# CXT console setup crash repair

Disposition: implemented within the user's request to repair errors and the crash caused by `e chaosx_test`; live-engine outcome remains unverified.

The supplied attachment contains 269 diagnostics: 176 invalid CXT capital accesses, 87 invalid State scopes at the static unit spawn sites, two invalid camp responsibility targets, and four Country effects or triggers invoked in None scope.
The command entered dormant CXT before providing land and a capital, and its inline setup retained the originating console country's ROOT.
The repair supplies a valid CXT capital before constructing its country scope and moves setup to a hidden CXT country event so its country and State traversals have the intended ROOT.

## Implementation

- `common/scripted_effects/chaosx_test_country_effects.txt`: records the source country and capital, transfers ownership and control of that capital State to activate CXT, resolves CXT through a runtime meta effect, sets its capital, changes the player tag, and fires `chaosx_test_country.1`; the dedicated capital camp fixture explicitly assigns its responsible-country pointer to the CXT parent before registration.
- `events/chaosx_test_country.txt`: hidden, triggered-only receiver with country ROOT CXT; annexes remaining origin States without importing troops, skips empty and self-annexes, restores the recorded owned capital, and requires an owned controlled capital before calling the unchanged initialization or refresh helpers.
- `common/scripted_effects/camp_repression_rework_effects.txt`: adds pointer presence and country-existence guards to `camp_rework_register_active_site`, including its ROOT default, equality check, and pool classification.
- `docs/testing/chaosx_test_country.md`: describes the activation and receiver contract and lists the new event file.

The existing technology, project, doctrine, stockpile, resource, static-unit, and package-extension implementations remain unchanged.
The capital's camp fixture retains its buildings and registrations; its explicit CXT responsibility assignment prevents a transferred State from retaining an unusable origin-country pointer after annexation.
The receiver supplies their correct country ROOT rather than replacing their behavior.
No UI, assets, Chaos event catalog entries, recurring hooks, AI weights, or balance values are needed or changed by this debug infrastructure repair.

## Review and source evidence

`public_command_receipt.json` records the exact old and new public effect and their hashes.
Reversing the public fragment and the single recorded capital-fixture responsibility assignment recovers the exact saved source bytes, proving all other private setup code is preserved.
`source_contract_checks.json` records byte-identical preservation of the unit helper, all 87 static templates and spawn sites, three divisions per template, and the capital-State PREV owner contract.
The 261 static divisions and registered-content processing remain available.
The same artifact distinguishes documented source behavior for multi-State origins, one-State origins, initialized CXT re-entry, and unusable camp responsibility pointers from live-engine results.
`camp_registration_handoff.md` records the specialist's caller review, unchanged 16 registration writes, references, and MCP coverage limits.
`country_transition_audit.md` records the independent country-package review.

`repair.patch` contains only the three changes relative to the saved task baselines; the receiver event is a separate source file committed in full.
The patch applies to the current HEAD index without including unrelated working-tree drafts.
Baseline copies are ignored locally; their identities are recorded in `baseline_inventory.json`.
The pasted error groups are recorded in `error_batch.json`.

## MCP and runtime limits

The required event inspection and rendering were requested with bounded selectors.
The focused analysis recognizes the receiver as a hidden triggered-only Country event and links its setup and refresh calls, but reports `helpers = 0` and failed analysis validation: `Large workspace analysis deferred workspace-wide helper projections and lifecycle passes; direct evidence is linked`.
Its scope view therefore selects no nodes and cannot demonstrate helper scope evaluation or pointer lifecycle.
Exact results and artifact references are recorded in the MCP evidence files; comparison status is recorded separately.
The neighborhood render selects the receiver and four unresolved nodes: the two setup/refresh helpers and the documented nested parameter tokens `remember_old_capital` and `transfer_troops`.
The installed vanilla documentation defines those parameters under `set_capital` and `annex_country`; their unresolved-node classification does not establish an engine syntax error.
The partial graph does not constitute helper validation.
The comparison request between the preserved before and after revisions returned `EVENT_REVISION_NOT_CACHED` with the exact blocker `Requested event graph revision is not cached`.
MCP source inspection does not establish that the live crash or every runtime error is resolved.
No game launch, console execution, computer control, or additional game-log search was performed.

## Simplifications, omissions, and blockers

No gameplay simplifications or replacement content were introduced.
Full engine evaluation and helper lifecycle proof remain unavailable in this source-only task.
The guards intentionally reject an unusable capital or responsibility pointer rather than invent a replacement State or country.
The camp pointer messages are repaired independently; the attachment does not establish that those two messages alone caused the crash.

Skills used: `chaos-redux-events`, `chaos-redux-subagents`, and `skill-creator`.
The event skill received a narrow reusable country activation, ROOT, event-target lifetime, and inherited sandbox-pointer note; `skill_update.patch` records only that guidance.
The bounded specialists used Sol and Luna; no Astra agents were used for this task.
