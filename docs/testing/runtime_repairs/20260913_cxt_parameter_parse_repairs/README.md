# CXT helper parameter repair

Disposition: the facility and project parameter repair is implemented; the full error-fixing request is incomplete because a technology database entry remains unidentified.
Acceptance basis: the user asked to fix the supplied errors without Astra agents or game control.

## Implemented repair

The supplied attachment reports literal `$FACILITY$`, `$COASTAL_REQUIRED$`, and `$PROJECT$` parsing failures, named helper argument failures, and a 264-error loader summary.
These failures came from the previous change set at `3a67634d47`.
Facility and project helpers accept documented temporary variable inputs through ordinary `= yes` calls.
Facility types are explicit building tokens expanded only inside supported `meta_effect` and `meta_trigger` templates.
Project IDs are explicit `sp:` scope objects passed to native `var:` project fields.

Changed source surfaces are `common/scripted_effects/chaosx_test_country_effects.txt`, `common/scripted_triggers/chaosx_test_country_triggers.txt`, and `common/scripted_effects/chaosx_test_country_special_project_effects.txt`.
The owner contracts are documented in `docs/testing/chaosx_test_country.md` and indexed in `common/scripted_effects/chaosx_dynamic_effects.md`.
The events skill records the reusable helper-input rule, maintained with the official skill-creator skill; the subagents skill guided the SOL implementation specialist and LUNA audits.

## Meaningful source checks

`verify_repairs.py` and `source_verification.json` compare the actual helper bodies and input wrappers against exact pre-repair bytes.
All 83 project IDs, their order and DLC gates, silent completion lifecycle, and zombie initialization remain intact.
All six facility types preserve intended construction legality, naval coast, owner/control predicates, search exhaustion, rejected-transfer restoration, missing-facility flags, and rejection-array cleanup.
Every other orchestration helper is identical, and the stockpile, roster, CXT history, and receiver event match HEAD.
No equipment, division, project, or facility inventory was removed; no content simplification or fallback was introduced.

The probability handoff under `facility_probability/` compares the same 31 declared scenarios under identical intended eligibility and weight expressions.
It models supplied native construction-legality results; it does not execute the foreign acquisition loop or prove that the pre-repair source loaded.
Event MCP inspection returned `EVENT_INSPECTED_PARTIAL`, with helper projections deferred and zero projected helpers.
The bounded event render and comparison calls did not return before termination, as recorded in `event_mcp_receipts.json`.
No live game run or error-free runtime result is claimed.
The country-helper specialist returned no verdict within the bounded review window and was interrupted; the scoped parent source checks above remain available, but are not a completed specialist country audit.

## Remaining blocker

The earlier and current supplied attachments contain one rejected `has_tech`/`set_technology` consumer pair per grant pass without an element identity.
The malformed technology meta interpolation has been replaced in a separate, uncommitted investigation patch by native `var:` consumers and temporary `CXT_TECH_DIAGNOSTIC` output for array size, index, numeric value, and token text.
All 679 named technology source definitions have valid IDs and wrappers and match the MCP source count; neither source review nor the installed technology adapter can identify the runtime element or execute dynamic consumers.
No unproven sentinel filter or static inventory substitute was applied.
`technology_handoff.md`, `technology_definition_audit.json`, and `technology_mcp_evidence.json` document this unresolved path.
The temporary diagnostics must be removed once the underlying rejection is resolved.
The technology investigation is excluded from the completed parameter-repair commit; its current source and wording remain local reviewable changes.
