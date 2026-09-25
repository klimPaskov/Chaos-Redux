# Event 012 Gods mission visibility cleanup

Disposition: `implemented` for the two timer definitions; the wider Gods of Africa completion goal remains `unresolved`.

## Decision basis

This is a narrow source-correctness cleanup within the user-authorized Event 012 Gods work. The accepted design keeps participant demand and reconciliation as owner-started timers that players resolve through separate response decisions. The user's accepted protection choices remain unchanged: AAT market access plus enemy intelligence, the four-cost-type cap on Event 012 protection only, the preserved Event 013 relief price in a separate choice, the reserve-counter decrement as bookkeeping for the infantry shipment, and the `.611`–`.613` response art with dedicated `.614` protection art.

The offline `Decision modding` page says `visible` does nothing on missions and should not be used there. The wiki's `Effects` page and installed vanilla `effects_documentation.md` say `activate_mission` starts a mission while bypassing its ordinary trigger conditions. Vanilla `common/decisions/AUS.txt` uses a non-clickable timer with `available = { hidden_trigger = { always = no } }` and a timeout effect for this same mission pattern.

## Change

Removed the no-op `visible` blocks from `gods_of_africa_demand_mission` and `gods_of_africa_reconciliation_mission` in `common/decisions/012_africa_gods_decisions.txt`.

Owner effects still explicitly activate both timers. Their disabled `activation` prevents automatic starts, disabled `available` keeps completion in the separate response decisions, and their cancellation, completion, timeout, durations, and AI score blocks are unchanged. No localisation, event, cost, or other gameplay behavior changed.

Updated `docs/events/012_africa/gods_of_africa.md` to describe the timer ownership and resolution contract.

## Source and MCP evidence

Source review confirmed the demand dispatcher sets the active contract state before `activate_mission = gods_of_africa_demand_mission`, and the reconciliation owner sets its pending flag before `activate_mission = gods_of_africa_reconciliation_mission`. Response effects remove the demand timer when the contract resolves; reconciliation completion and failure effects remove the review timer. Existing cancellation and host-loss cleanup call sites remain intact.

Fresh `hoi4.event_inspect` traces for `chaosx.nr12.610` and `.614` returned `EVENT_INSPECTED_PARTIAL` at revision `13bfefb0efc8ce0c8d3c24ceec0269c9b5372bd9efb2c49bf2c0afa7d556d340`. They indexed the current workspace but deferred helper and lifecycle projections, reported zero expanded helpers, and set `validation.passed = false`. Trace artifacts: `.610` `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/292566e373dc12f6e3770bda878f3e9434d0a7afe57748cde4659bab5fb3a3fc/ea52de02e15c66458c36795b1201e65acd92be0ce1f9f667d2752eaeb0de50d8/event-trace-13bfefb0efc8.json`; `.614` `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b10b74a9158e41977d53e4f505f0326c754ac40b10eda33640a0c1d956a8a36/a9da5a5e1c2acc1e8c10af4dfaffa6cf547a0a65998cf10a7cc235a3a017e929/event-trace-13bfefb0efc8.json`.

Matching neighborhood renders for both reports returned `EVENT_RENDERED_PARTIAL`; each selected three nodes, omitted 42,855 nodes, rendered zero branches, and deferred helper/lifecycle projections. `.610` render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6abb19e37e6629afc32a6f9585641460dc8744b2450d55165f636054b58ab958/6950e6057c9318ea25bcb570f0082917999ed21a1e3cb90b275c8dd2fd2dc963/event-neighborhood-13bfefb0efc8-manifest.json`; `.614` render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/37433c8952700c00a3f70409c28cfa4b6ae6587f0808bf7ee8ae12b61ced68b7/6d88843abb0fecc8c0e9b5bc8f430135551f0ed5b255789c1bb4acbad8a12e08/event-neighborhood-13bfefb0efc8-manifest.json`.

An event graph comparison from earlier revision `bf6c8d603c391a1acf54a845101b5ffc912fdc368d799386fe5caa33055ce593` to the initial post-edit inspect revision returned `EVENT_REVISION_NOT_CACHED`; no graph comparison is claimed. The cleanup did not change any AI score, so the existing probability audit remains applicable as source inventory only: the mission adapter found two base-1 candidates, but eligibility and same-scenario balance remain unresolved. No campaign execution or live-game validation is claimed.

## Remaining goal limits

This cleanup does not resolve the user's pending direction on whether older Part 8 focus-route promises should return to scope. Event 012 probability scenarios, branch-level focus visual review, report-art content approval, and end-to-end owner-system runtime evidence also remain open as recorded in `docs/events/012_africa/gods_of_africa.md`.
