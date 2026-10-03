# Event 021 sponsor receipt live QA repair

Disposition: implemented source repair, live confirmation pending.
Acceptance basis: the user-provided 2026-10-03 13:20 live QA report requests a committed definition for `event021_sponsor_repayment_receipt_valid` called by the settlement selector in committed HEAD `d51bba41f`.

## Repair

The trigger existed only in the unfinished working-tree parent trigger changes.
Its definition belongs in `common/scripted_triggers/021_random_civil_war_sponsor_receipt_triggers.txt`, with the duplicate uncommitted definition removed from the parent file.
The settlement effect remains intact.
The receiving sponsor commitment records `random_civil_war_sponsor_scope = ROOT` alongside the existing reciprocal IDs in `common/scripted_effects/021_random_civil_war_decision_effects.txt`.
Only that pointer assignment is part of this repair, not the other unfinished changes in that file.

The validator requires the received commitment, active sponsor evidence, a stored sponsor pointer, recipient-side sponsor ID, an existing sponsor with an active commitment, and the sponsor-side recipient ID.
Both IDs must match the actual countries.
Inside the sponsor pointer scope, `PREV` identifies the current settlement recipient.
Using `ROOT` there would check the original callback or event sender when a different participant is being settled.
The definition has no custom helper or tuning dependency and changes no weights, timing, resources, or settlement preference order.

## Source review and reference evidence

- Installed `documentation/triggers_documentation.md`, lines 2110-2134, 2708-2715, and 5006-5013, SHA-256 `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`, documents variable comparison, country-only existence, and variable presence.
- Offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, lines 2359-2400, SHA-256 `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06`, documents scripted trigger definition, invocation, and duplicate override behavior.
- Offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, lines 260-270, SHA-256 `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49`, documents `ROOT`, `THIS`, `PREV`, and variable-pointer scopes.
- Vanilla `common/scripted_triggers/NOR_scripted_triggers.txt`, lines 47-73, SHA-256 `D756467264C6B1C467BD6346DCB6CAF8C0AC2A37B6711A081BFD2BCA32AF5D8B`, provides guarded variable country pointers with country existence checks.

Read-only contract cases are valid reciprocal receipt, missing recipient pointer, missing recipient ID, missing sponsor recipient ID, dead sponsor, inactive commitment, mismatched sponsor ID, mismatched recipient ID, and valid receipt while ROOT is a third country.
Only the valid reciprocal cases should pass.
These source contract cases are not executed game evidence.

The live MCP schemas expose reference context, reference search, reference read, source lookup, and event inspection.
A bounded reference context call is pending under load, with a separate narrower installed-documentation search for `has_variable` also requested before any route gap is declared.
Relevant local sections were read directly while the service calls were pending.
No `script_validate` tool is exposed in this connected tool list.

## Limits

The user has not yet supplied a fresh live result for this commit.
This repair addresses the named unknown-trigger error and the receipt pointer required by its committed caller.
It does not establish a clean full error.log or completion of the Event 021 goal.
The existing unfinished implementation, active Evolution I work, broader actor and asset acceptance, probability tooling gaps, and runtime checks retain their recorded status.
Skills used for this repair are `chaos-redux-events` and `chaos-redux-shared-git-commit`.
