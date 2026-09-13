# CXT reserved technology-object repair

Date: 2026-09-13.
Disposition: implemented source repair; executed runtime validation unavailable.
This repair supersedes the unresolved zero-based delivery attempt in `../20260913_cxt_activation_errors/` for the two reported technology errors.
The separate first-day freeze investigation remains open and is not claimed as resolved by this technology change.

## Cause and implementation

The installed `global.technology` registration copies every technology database object ID in vector order, starting at vector index zero.
The database constructor inserts its shared default object at that index and explicitly sets the object's validity byte to false.
Native technology lookup searches real objects from index one and returns the default object when lookup fails.
Both native `has_tech` and `set_technology` reject an object with that false validity byte, at the engine source lines 3153 and 996 reported by the user.
The read-only machine-code captures, executable SHA256, and function hashes are in `binary_contract.json`.
No game was launched or executed for this inspection.

`common/scripted_effects/chaosx_test_country_technology_effects.txt` starts at the confirmed first real database index and keeps its exclusive runtime-count bound.
This excludes a reserved array position rather than guessing that a token or raw numeric technology value is invalid.
The native variable consumers, `popup = no`, already-owned guard, private break variable, and conditional layout refresh remain intact.
The three temporary technology diagnostics have been removed after identifying the reserved object.

## Review and verification

The scripted-system architect reviewed the array registration, default initialization, lookup, native consumer checks, and source traversal, and approved the exclusion as lossless for real database entries.
`technology_source_validation.json` checks empty, default-only, single-real-entry, complete inventory, and future-extension traversal models.
The complete-inventory model has 680 slots including its reserved default and visits all 679 real slots; adding one real slot visits 680 real slots without a source inventory edit.
These are source traversal scenarios, not a captured runtime database count or executed game test.
The executable grant body is unchanged apart from the starting index and removal of temporary diagnostics.

Required technology inspect, render, and compare calls returned `Transport closed`; exact receipts are in `mcp_receipt.json`.
Source and binary inspection do not substitute for executed runtime or MCP graph evidence.

## Scope and omissions

No simplifications were made to technology coverage.
History pre-unlocks, all special-project outputs, the zombie profile, equipment stockpiles, unit templates and formations, facilities, and the extension bus are preserved by this technology-only source change.
The CXT testing guide describes the indexed real-entry traversal and the engine evidence boundary.
The events skill records the reusable rule to prove a reserved default object's registration and validity before excluding its slot.
Skills used: `chaos-redux-events`, `chaos-redux-subagents`, and the official `skill-creator` workflow for the small guidance update.
No Astra subagents were used.
