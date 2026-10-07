# Chemical raid caller-storage patch

Disposition: narrow source patch implemented and frozen for parent review, independent transaction tests, MCP evidence, and isolated commit.
The parent explicitly authorized only the caller-storage insertions from the committed action-lifetime audit and map at `0afbdf4d`.
No staging or commit was performed by this agent.

## Changes owned by this patch

| Source file | Exact inserted storage |
| --- | --- |
| `common/scripted_effects/cbrn_chemical_land_raid_effects.txt` | 60 public action-packet scalars before the resolver's reset in the existing actor-valid branch |
| `common/scripted_effects/cbrn_chemical_raid_effects.txt` | 63 action/forwarded air-result scalars before reservation resolution, three private attempt-consequence outputs inside the existing accepted no-release branch, and one attribution output before its returning evidence helper |
| `common/scripted_effects/cbrn_chemical_doomsday_effects.txt` | 60 public packet scalars for each existing exact-state resolver, nine release-owned target/arsenal/condemnation outputs, and one release-owned temporary target-array initializer |
| `common/scripted_effects/cbrn_protection_effects.txt` | Six private protection-weight outputs inside the valid-input branch before the weight profile helper |
| `common/scripted_effects/cbrn_consequence_effects.txt` | Three private context/evidence-floor/civilian-death outputs inside the existing accepted and undispatched branch |
| `events/cbrn_doomsday_raid_bridge.txt` | The returned release-status scalar immediately before the existing release helper |

There are 206 new scalar declarations and one temporary-array initializer in nine insertion blocks.
Every new script statement is either `set_temp_variable` or `clear_temp_array`.
Defaults and field names come from the accepted insertion map and original reset contract.
No runtime initializer helper, new wrapper, persistent state, payment, refund, timing value, tuple field, target scope, profile formula, outcome draw, weight, authorization gate, or callback order was changed.

`cbrn_action_dispatch_proof` is initialized only in the fresh action owners' packet.
No declaration for it was added to the dispatcher.
The dispatcher still has exactly its original supplied-proof assignment under its original `NOT supplied` guard.
The failed-attempt proof is likewise preserved as an action-owner field rather than reset by the attempt dispatcher.

## Existing ownership reused

The fresh source already owned eighteen route/class/exact-agent profile outputs in `cbrn_calculate_chemical_action_outputs`.
It already owned six generic protection outputs before both target-protection calculation passes.
It already owned the two metadata outputs required by `cbrn_payload_validate_request_authorization` before its reset and model/default helpers.
Those 26 declarations were reused without changing their values or duplicating their statements.

Consequently `common/scripted_effects/cbrn_exposure_effects.txt` and `common/scripted_effects/cbrn_payload_reservation_effects.txt` are byte-identical to their captured working baselines.
The exposure file's pre-existing dirty work and the entirely untracked payload-reservation source remain other actors' work and are not claimed by this patch.
The existing generic protection ownership in the dirty protection file is also preserved.
Only the six mapped weight-output declarations were added to that file by this agent.

The parent retains the shared missile and camp integrations.
This agent made no edit to `032_missiles_operations_effects.txt`, `camp_repression_rework_effects.txt`, biological incubation timing, or any test or shared system document.

## Exact before, after, and insertion evidence

Evidence root: `docs/testing/2026-10-07_chemical_raid_lifetime/`.
The captured baseline HEAD is `9c3418607b164096d4c3ddaf3e7f380c576bb669`.
The baseline uses the actual working bytes rather than assuming dirty files equal HEAD or index.

- `source_manifest.json` records all eight authorized files' working SHA-256 values, raw sizes, CRLF/bare-LF counts, HEAD hashes, index hashes and stage entries, scoped Git status, and baseline HEAD.
- `before/` contains those exact working files before any source mutation.
- `after/` contains all eight frozen post-patch files, including the two byte-unchanged reused sources.
- `.gitattributes` sets `before/** -text` and `after/** -text` to protect raw mixed line endings during parent staging.
- `insertion_manifest.json` records each owner, preceding producer/helper, zero-based before/after byte spans, original line, exact inserted bytes, indentation, line ending, every scalar field/default, array initializer, reused declaration/default, before/after hashes, and conflict status.

Five authorized files had mixed CRLF and bare LF in the captured baseline.
Insertions use the existing producer call's line ending and indentation, and all original bytes were retained.
Source replacements used an exact-byte race check followed by atomic replacement in the same source directory.
No baseline/write conflict was observed and no temporary source file remained.

The first in-memory insertion-plan attempt rejected the two expected protection-calculation producer calls as ambiguous before writing any source.
The plan was corrected to select the documented first call in that resolver, whose existing storage covers both passes.
No source edit, fallback, or original-statement rewrite resulted from that planning error.

## Meaningful verification performed

The frozen live source matched every `after/` snapshot at final verification.
Removing only the recorded insertion spans reproduced every captured original byte for all eight files.
The existing Clausewitz parser also reproduced the original parsed source, so existing command values, branches, scope transitions, callback order, and weighted bodies were retained exactly.

Every inserted block was checked in its actual owner and directly precedes the mapped producing helper in the same containing sequence.
The parsed inserted statements contain only the 206 mapped scalar assignments and one array initializer.
The dispatcher contains exactly its original proof assignment to supplied and no new missing-proof initialization.
Scoped Git index entries still match the captured baseline, confirming that this agent did not stage these sources.

This verification establishes insertion placement and preservation, not native transaction behavior.
The parent's independent tests own accepted/rejected actor and target cases, paid payload receipts, repeated dispatch, exact deaths/history, no-release attempt accounting, doomsday allocation, and scope-aware conservative lifetime execution.
No generic VM, test generator, or gameplay substitute was created.

## References and remaining limits

`AGENTS.md`, the event skill's caller-owned output rule, the native-raids skill's scope/payment contract, and subagent ownership guidance were reviewed before the patch.
Live reference reading reconfirmed offline `Data structures:435-443`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, and installed `effects_documentation.md:7820-7827`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The prior audit's installed raid creation-payment and raid-instance scope references and vanilla actor-country bridge precedent remain the authoritative basis.
The complete variable/call map and native assumptions are retained in `2026-10-07_chemical_action_lifetime_audit.md` and its JSON sidecar.

No duplicate domain MCP call was made because the parent owns before/after evidence and the preceding event artifacts were unreadable.
Native helper-return behavior, callback transaction execution, and final domain evidence remain parent validation work.
The packet preserves the original missing/zero condition defaults and does not invent weather, forecast, density, payload, protection, or release receipts.
No simplification, fallback, rebalance, or policy change was implemented.

The source patch is frozen.
Parent review, independent tests, MCP disposition, updated owning API documentation, and isolated mixed-file commit remain outstanding.
