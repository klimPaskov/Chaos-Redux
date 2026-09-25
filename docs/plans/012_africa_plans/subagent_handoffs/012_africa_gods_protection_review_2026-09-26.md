# Event 012 Gods protection review, 2026-09-26

Disposition: The accepted protection costs, services, report art mapping, and separate Event 013 relief choice are implemented in source. This review made no gameplay changes because the current source already matches the accepted decisions. Full Gods of Africa completion remains unresolved because route scope, probability evidence, aggregate MCP validation, and live scenario acceptance remain open.

## Acceptance basis

The user selected Arms Against Tyranny market access plus enemy intelligence, directed that Event 013 relief remain a separate choice, and clarified that only Event 012 protection is subject to the four cost type cap. Event 013 relief retains its full existing price and penalties.

For cost counting, the user delegated the common defence reserve decrement to parent judgment. It is bookkeeping for the same infantry shipment, not a second material payment. The optional transport shipment remains available as the fourth type.

The user selected the existing response art for reports `.611` through `.613` and the dedicated protection art for `.614`. This confirms the sprite mapping only and does not approve image content or game scale appearance.

The older Event 012 Part 8 focus route promises remain outside the accepted 24 node overlay until the separate route scope question is resolved.

## Source review

`common/scripted_triggers/012_africa_gods_triggers.txt` checks the Event 012 host for infantry equipment, fuel, political power, a valid host generation, and enough common defence reserve for the same infantry shipment. The participant affordability trigger combines that host gate with the recipient eligibility checks.

`common/decisions/012_africa_gods_decisions.txt` exposes `gods_of_africa_protect_partner` only through the maintained participant target array and requires the complete transaction to pass before selection.

`common/scripted_effects/012_africa_gods_effects.txt` debits infantry equipment, fuel, and political power once, mirrors the infantry amount in `africa_common_defence_stockpile`, credits the equipment and fuel to the participant, and starts the protection cooldown. With the logistics focus, it may transfer one shortage checked 20 unit convoy or train shipment while retaining the configured host floor.

The same effects gate AAT market access on the DLC, peace, and Sanctuary capability. Enemy intelligence requires La Résistance, agencies for both countries, an active African war, and an eligible enemy the recipient is not fighting. Created access and guarantees have owner receipts for later withdrawal.

The protection reports use `GFX_report_event_012_africa_gods_response` for `.611`, `.612`, and `.613`, and `GFX_report_event_012_africa_gods_protection` for `.614`. Both sprites and their DDS files are registered in `interface/012_africa_event_pictures.gfx` and `gfx/event_pictures/012_africa/`.

The Foreign Disaster Relief choice remains in the Event 013 decision system. Its neighbor relief transaction keeps manpower, support equipment, trucks, convoys, fuel, stability loss, war support loss, and the temporary construction burden. Event 012 protection does not invoke that price bundle.

The source review found no mismatch with the accepted choices. It does not establish live effect execution, DLC runtime behavior, or disaster mission outcomes.

## HOI4 MCP evidence

Fresh `hoi4.event_inspect` state flow requests for `chaosx.nr12.610` and `chaosx.nr12.614` returned `status=ok`, `code=EVENT_INSPECTED`, and `analysisMode=full`. Both artifacts report `complete=true` at graph revision `bf6c8d603c391a1acf54a845101b5ffc912fdc368d799386fe5caa33055ce593` and graph hash `bc212f1910f54f9a306ede9341406ccfb68ae98d4a7248b8da08a82872f18d60`.

The full workspace summary contains 9,835 events, 15,184 options, 23,545 entries, 19,652 helpers, 29,396 unresolved nodes, 328,203 edges, 358,104 state accesses, and 3,911 blocking diagnostics. It reports zero skipped sources. The source hash inventory covers 4,053 paths, retains 256 hashes, and marks the inventory truncated. `validation.passed=false`; the blocking diagnostics are not separated by selected event in the compact result, so their relevance to the protection path remains unresolved.

The `.610` artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a8fddba5171417978aed9b326664c215af69f677b532668fff40054c1dcb70f7/a8e30fd06c3ccabfe94e38d7083ed528cb3c0b7b1302b05fb2dd67751c702d81/event-state_flow-bf6c8d603c39.json`.

The `.614` artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4fad65632a9c025993620b93e7eb8a938ba343abe5b0ce8f8e61c0e63851bcc4/baab56f01c8bf64b08e80bbdc23899e3c80fca91cf9d637898001561d77792e9/event-state_flow-bf6c8d603c39.json`.

The earlier focused `.610` and `.614` traces and options renders remain partial. Each options render selected three nodes, omitted 42,852 nodes, rendered zero helper or branch paths, and reported zero blocking diagnostics. Those renders do not establish helper lifecycle coverage.

The current `hoi4.event_inspect` schema exposes `scan`, `roots`, `trace`, `explain_path`, `state_flow`, `lint`, and `impact`. It has no `helper_expansion` mode. The connected tool inventory and MCP resources expose no separate server version, health, or client task negotiation endpoint, so the prescribed helper expansion gate cannot be satisfied and that route was not used.

A comparison from the earlier Event 012 revision `811e61df0f66e2986e5ba3d637f8f755945d0c067de0b312c964852355901694` to the focused revision `a69de429c01f9f10d4f64e0476382dc3e229687be56c86e99a4c43cd79701f69` returned `EVENT_REVISION_NOT_CACHED`. No event graph comparison is claimed.

## Remaining limits

The dedicated probability auditor found no supported weighted candidate pool for the Gods strategy file and could not run a valid same scenario comparison. The retained AI strategy values are unchanged, and no balance conclusion is claimed.

The accepted 24 node overlay has not been compared against the older Part 8 promises because the user has not answered the separate route scope question. No focus expansion is inferred from the protection choices.

The user owns live game validation. No game was launched, and no test suite was run or added during this source review.

No costs were hidden, waived, or repriced. No Event 013 price was changed. No new art or visual fallback was introduced.
