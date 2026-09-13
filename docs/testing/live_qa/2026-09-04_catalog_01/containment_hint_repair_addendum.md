# Event 016 containment static political-power hint repair

Disposition: implemented, with engine validation pending.
Acceptance basis: the parent explicitly authorized repair of the eight launch_08 malformed `ai_hint_pp_cost` fields using same-value file-local aliases, preserving costs, debits, AI weights, earlier parameter fixes, and active concurrent work.
This addendum extends `containment_parameter_repair_plan.md` without changing that repair's helper contract.

## Confirmed field and evidence

The eight errors in `logs/launch_08/logs/error.log:28–35` identify `constant:brilliant_scientist_containment_cost.*_political_power` at original decision source lines 37, 109, 181, 253, 326, 398, 472, and 545.
Each source field is `ai_hint_pp_cost`.
This field supplies a static numeric political-power amount for AI saving behavior; it is not an `ai_will_do` score or a payment effect.
The offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:319` says that its amount must be constant rather than a runtime variable.

Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md` was read; it documents decision trigger evaluation but does not provide a field-specific `ai_hint_pp_cost` declaration.
The installed vanilla precedent `common/decisions/CZE.txt:1863` uses `ai_hint_pp_cost = 25`, followed by custom PP/command-power affordability and matching debits.
Installed `documentation/script_concept_documentation.md:216–222` distinguishes the file-local `@` macro from globally referenced script constants and limits global constant access to supported fields.
The offline Data structures Constants section documents numeric `@` aliases in decision fields, including `cost = @CONSTANT_1`.
The observed malformed-token errors establish that this consumer rejects the current `constant:` form; no integer-versus-fixed-point engine subtype is inferred beyond its documented static numeric requirement.

## Exact implementation and value linkage

Changed gameplay file: `common/decisions/016_brilliant_scientist_containment_decisions.txt` only.
Eight declarations were added beside the existing file-local modifier aliases, and the eight hint fields now reference those declarations.
The accompanying source comment names the authoritative `brilliant_scientist_containment_cost` category in `common/script_constants/016_brilliant_scientist_containment_constants.txt` and requires alias alignment when its values change.

Every alias begins with `@CR_SC_BRILLIANT_SCIENTIST_CONTAINMENT_COST_` and ends with the uppercase source key shown below.

| Decision action | Authoritative source key | Alias value | Updated hint line |
| --- | --- | --- | --- |
| release | `release_political_power` | 25 | 47 |
| exile | `exile_political_power` | 40 | 119 |
| arrest | `arrest_political_power` | 55 | 191 |
| shutdown | `shutdown_political_power` | 65 | 263 |
| charter | `charter_political_power` | 75 | 336 |
| military seizure | `military_seizure_political_power` | 85 | 408 |
| foreign containment | `foreign_containment_political_power` | 65 | 482 |
| concession | `concession_political_power` | 50 | 555 |

For example, release uses `ai_hint_pp_cost = @CR_SC_BRILLIANT_SCIENTIST_CONTAINMENT_COST_RELEASE_POLITICAL_POWER`, whose declaration is 25.
The shared tuning file was not edited.
The aliases are the authorized compatibility representation for this static field; all live affordability and debit values still reference the original shared constants.

## Preservation and validation

Immediate original bytes were archived at `pre_patch_containment_hints/common/decisions/016_brilliant_scientist_containment_decisions.txt` beneath this exact QA directory, `docs/testing/live_qa/2026-09-04_catalog_01`.
Before writing, the patch checked that both decision bytes and the source cost table still matched the snapshots used to construct the aliases.
An initial preparation assertion expected a CRLF header delimiter and stopped before writing or archiving; the subsequent patch preserved the file's existing mixed line endings rather than normalizing unrelated bytes.

`containment_hint_repair_validation.json` records every source key, integer value, full alias name, and before/after SHA256 values.
Before SHA256: `31f92e6c538791f201e0204c088c91e3fe2943d29a2d34d10d4894097b5c71dd`.
After SHA256: `1aa246e942e85e89fdad60ad79c7db64dff1947e08215524f367af15aea8f7d1`.
The task-specific preservation check reverses precisely the eight hint substitutions and removes only the new declaration/comment block, then compares the result byte-for-byte with the archived original.
It passed, proving that earlier parameter repairs, decision IDs, AI weights, costs, extra resource debits, triggers, effects, timers, modifiers, and tooltips are untouched by this patch.

The refreshed narrow MCP trace for `chaosx.nr16.1` returned `EVENT_INSPECTED_PARTIAL`, focused analysis, revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f176f702092d4f5be95424222ad462825a5853770de4fb8781a4351ba7716fb/e18fcb885dc35ae3632057fe7092947100c2539271b0e5445df46e3671c5ba99/event-trace-1102e50fad94.json`.
As documented in the earlier handoff, focused event analysis excludes decision/helper validation and defers lifecycle passes; this artifact is not engine acceptance evidence for the static hint syntax.
No weighted probability surface was changed or balance result claimed.
No game, desktop, process, staging, or commit operation was performed.

## Limits and remaining work

The launch_08 malformed hint forms are repaired in source, but no post-patch game execution was performed.
The documented static alias form still requires engine acceptance evidence from the parent's broader QA work.
No gameplay simplification or unapproved fallback was used.
Skills used: chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-subagents; no skill was changed.
