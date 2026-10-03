# Assassin Network registration repair

Disposition: implemented in source; live launch, payload transactions, and mandatory MCP evidence remain unresolved.
Acceptance basis: the user's 2026-10-03 live-QA finding explicitly requests the next verified free scenario ID, normal shared registration paths, authoritative workbook correction, exports, and a shared-tree commit.
This is a bounded missing-registration repair, not completion of Event 039 or its Part 18 matrix.

## Identity and source coverage

The workbook reserved `SCN-019` at `Scenarios!A14` before code used ID 19.
The earlier provisional SCN-014 proposal in Part 11 and historical spreadsheet handoff is superseded for allocation by this explicit user decision.
Fallout retains raw ID 14, ID 17 remains reserved, and The Fracture Cascade retains ID 18.
Event 039's package-local runtime and catalog identity fields also use 19.

The repair touches the shared constants, registry and four view builders, launch dispatcher, shared eligibility bridge, and seven scripted-localisation getter families.
The row label is `#019` and all four intensity warnings describe the existing payload's Low Murder Cult, Medium international network, High country split/war, and Maximum Evolution IV setup.
Those warnings do not promise that incomplete transaction validation has passed.
The shared GUI layout is unchanged and the existing entry, four-stop intensity, confirmation, cancel, and launch controls are reused.
Its single scenario type requires no new type variable.
The completion audit found that the new status linkage described a resolved network as active; a separate resolved-status key precedes the active branch and corrects that registration defect.
No new icons, textures, models, audio, country packages, or recurring scans belong to this repair.

The existing scenario wrapper rechecks eligibility, freezes intensity at confirmation, selects a normal host, and queues `chaosx.nr39.1` on it.
The root applies intensity setup only after the opening transaction commits, then clears its launch flag and cached intensity.
The Low setup's unconditional fallback is `else`, not a conditionless `else_if`.
No AI weight, probability, cell-count tuning, or terminal gate is changed in this tranche.

## Evidence

`check_registration.py` passes with 17 unique registered rows, four paired 17-row views, preserved prior order and identities, seven getter families, all four warning keys, and gate/dispatch/root linkage.
This is a read-only source-contract check and does not execute Clausewitz effects.
Immutable pre-edit sources are the `*.before.*` files in this directory.
The workbook reservation and intensity alignment have separate specialist handoffs under `../../subagent_handoffs/`.

| Read reference | Lines | SHA-256 revision |
| --- | --- | --- |
| Offline `Data structures - Hearts of Iron 4 Wiki.md` | 1069-1104, persistent arrays and paired values | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `Effects - Hearts of Iron 4 Wiki.md` | 4477-4503, conditional fallback | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline `Scripted GUI modding - Hearts of Iron 4 Wiki.md` | 144-205, context and clicks | `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30` |
| Installed `documentation/script_concept_documentation.md` | 216-248, global script constants | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common/script_constants/documentation.md` | 1-80, schemas and variable access | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Installed `common/scripted_guis/_documentation.md` | 1-98, click gates and dynamic-list consumers | `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838` |
| Installed `common/scripted_guis/GER_monroe_doctrine_scripted_gui.txt` | 1-9, native context/window binding precedent | `4c65f8e0bae06ad57a6ed32fc2d012b7de9586b104089d0f5c5811155ee28d55` |
| Installed `documentation/effects_documentation.md` | 2278-2294 and 2773-2783, array append and variable cleanup | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation/triggers_documentation.md` | 2110-2139, selected-ID comparisons | `7d27ed77dadaf3a213a4b3e2c624bf9c02daE495317abe8eee833b27c2d1de29` |

## Validation limits and remaining work

The first shared-window `hoi4.gui_inspect` failed with `timed out awaiting tools/call after 600s`.
A subsequent shared-window render continuation became stale after a desktop host-generation change, so its outcome is unknown and supplies no evidence.
The connected HOI4 routes briefly disappeared from the live tool inventory, then returned; narrower requests are being retried.
The narrower `hoi4.source_lookup` for `murder_mystery_triggerable_scenario_launch` completed with one definition, no overrides, and complete source coverage at lines 59-81, revision `bcb661e2c2c5f10ef154908d7b9310e2b6b590cde713430cac3aa4a4c514e430`.
The targeted `hoi4.reference_search` found installed `add_to_array` section ID `b11098707fca8123566864381393f908217da93ca48203f5731a100d0143c95d` at lines 2278-2292, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The matching `hoi4.reference_read` completed and the full 15-line section was read, with no continuation.
The narrower GUI retry targets only `triggerable_scenario_entry_generic` and also failed with `timed out awaiting tools/call after 600s`.
The narrow event lint completed as `EVENT_INSPECTED_PARTIAL`, graph revision `8cff6caa71c9f1de7f7a76b61c662306289fbaa4573c5f106a8e4d0d6058bdd1`, with helper and lifecycle projections deferred.
Its linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c97e1b33d3e360feaea77e0f573c763562c49498176ccd866e81d54921571fee/2af09190d15d8c6c2f926255342b788faa2fc5fdd384a84a5f9d3caba8728ac6/event-lint-8cff6caa71c9.json`.
The complete 2,039,845-byte artifact was read through verified 24,000-byte resource chunks after a larger resource response truncated its base64 body.
The focused report has no issues, but `complete = false` and retains only 2,000 of 8,958 unresolved records.
Nine retained Event 039 unresolved records concern helper definitions excluded from that catalog, including CXT, cells, inheritance, country creation, and shared audio.
Their exact definitions exist in the current source, and the artifact's Event 039 source SHA-256 `5b582c80df580c85dba01077cccd734154f6cf2329deaec2c454501d79edc367` matches the current file.
This does not certify their scope semantics or runtime execution and is not a full helper-coverage pass.
No render, event comparison, or helper expansion is inferred from exposed schemas or local package files.
The installed live `hoi4.source_lookup` schema has neither `view` nor `keyPath`; `hoi4.script_validate` is not exposed.
The fallback reads above retain source revisions but are not substitutes for mandatory MCP engine-facing evidence.

The supplied cycle-1 log has no lines matching `murder_mystery`, `nr39`, or `039_` in the narrow source-owner filter.
This does not establish a clean full log and predates this registration repair.
The orchestrator owns the running game and will supply launch evidence; no agent launches HOI4.

Full Part 11 still requires host/intensity character and territory preflight, verified country capacity, cell-stage setup, viable split and derivative transactions, cleanup after all failures, and the terminal gate's actual execution.
The completion auditor's handoff at `../../subagent_handoffs/scenario_registration_audit_2026_10_03.md` accepts the bounded ID, registry, getter, and dispatcher wiring in source and records manual-gate, delayed-event recovery, intensity-preflight, and whole-transaction defects as open payload work.
The final type/intensity workbook specialist changed only D14 and E14 against its preserved before-copy and regenerated all three exports; the parent independently checked these values and the ID against the scenario CSV and localisation.
Full Event 039 additionally retains investigation, inheritance, character safety, country viability, assets, AI/probability, persistence, terminal outcomes, and cleanup acceptance work recorded in the accepted specs.
No substitute design or simplification is accepted by this repair.
