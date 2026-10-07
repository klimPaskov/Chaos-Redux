# HQ payment and service integrity

Disposition: source repair implemented and independently reviewed; native transactions, scheduling and personal raid-service attribution remain unproved.
Acceptance follows the approved overhaul's real payments, bounded maintenance and genuine completed commander-service requirements.
This repair preserves the existing five protective HQ orders and introduces no gameplay simplification or additional player action.

## Repair

`common/scripted_effects/cbrn_hq_effects.txt` establishes caller-owned storage before consuming returning helper outputs.
Each of the five public starters owns its nine package debit values, preparation base/minimum/maximum, active duration, native/total Command Power and calculated preparation days.
Each of the five upkeep wrappers owns the nine package debit values.
The common debit consumer owns completed mask, decontamination, instrument and motorized outputs before recording actual consumption in the country's counters.
Literal declarations remain in their consuming frames; moving them into a returning initializer helper would recreate the lifetime problem.

The [architecture audit](subagent_handoffs/2026-10-07_hq_helper_lifetime_audit.md) maps the exact calls, variables and scopes.
Removing only the 129 new zero declarations restores every original HQ statement and its order.
All seven other captured ability, event, trigger, progression and constant files remain byte-identical.
The original prices, force bands, oldest-first equipment order, readiness multipliers, command discount, duration bounds, finite upkeep, planned-end lock and completion guard are retained.
Temporary variables are unscoped; saved commander and owner-country state remain distinct.

## Evidence

The parent reran `node docs/testing/2026-10-07_cbrn_hq_lifetime_source_tests.js`: 292 source cases pass and 275 baseline missing-output failures are reproduced under conservative helper-frame cleanup.
The [regression handoff](subagent_handoffs/2026-10-07_hq_lifetime_source_checks.md) records all fixtures and native/stub boundaries.
Cases exercise five activation and upkeep families, three force bands, readiness boundaries, commander discounts, decontamination designer branches, mixed stock models, final paid/failed upkeep, duplicate receipts and planned cleanup.
A mixed-stock case retains distinct completed totals of three masks, five decontamination kits, nine instruments and four trucks after their helpers return.
These are actual-source models; equipment effects update fixture stocks and native timers are captured as arguments, not executed by the game.

The offline Data structures reference at lines 435-443, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, documents the helper-return caveat and caller-preinitialization guarantee.
Installed `effects_documentation.md:7820-7827`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, permits `set_temp_variable` in any scope.
The same installed document at lines 8424-8448 documents character-scoped `unit_leader_event`; vanilla `events/BBA_ItaloEthiopianWar.txt:9-23` is an unchanged precedent.
The existing named commander event target and native event definitions are retained.

Whole-file MCP validation checked 642 commands with no findings, but returned `valid=null`, 37 unknown-scope roots and 446 unchecked argument blocks.
The exact `cbrn_hq.2` before trace was partial and its artifact could not be read because its provenance manifest was unavailable.
The after scope render's complete JSON was read: it includes the HQ event file's hash but selects zero nodes for the exact event ID, so it proves no HQ chain behavior.
The matching event comparison returned `EVENT_REVISION_NOT_CACHED`.
The [MCP receipt](../../testing/2026-10-07_cbrn_hq_lifetime/mcp_receipt.json) retains the requests, revisions, artifacts and limitations.

## Remaining requirements

The installed raid outcome contract still exposes actor/victim countries, target state/province and a participating division callback, without a documented division-to-army-commander bridge.
No country-wide raid result is assigned to an arbitrary officer.
No Wind Is Friendly still lacks genuine forecast-failure and affected-army recovery proof; Unbroken Supply Corridor still lacks exact assigned-army supply and offensive-objective proof.
Those accepted requirements remain incomplete, and this HQ repair does not substitute for them.
The complete native payment, event timing, cancellation, target persistence and trait-award paths remain acceptance gates.

No localisation key, public event wording, asset, CXT registration, workbook or CSV changes are required by this internal storage repair.
Skills used: events, native raids, subagents and shared Git commits; the existing event skill already contains the reusable helper-output lifetime rule.
