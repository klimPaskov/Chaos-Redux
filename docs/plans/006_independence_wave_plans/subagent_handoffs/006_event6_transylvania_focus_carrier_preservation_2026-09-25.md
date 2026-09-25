# Event 006 Transylvania focus-carrier preservation

Disposition: **implemented for IW-023 carrier selection; REG-03 focus coverage remains partial**.
The user explicitly approved the accepted Event 006 design and implementation scope on 2026-09-25.
This handoff records a narrow correction to the accepted carrier-preservation contract and does not claim completion of the regional focus overlay.

## Change

`independence_wave_setup_iw_023_transylvania` now selects `independence_wave_focus_assignment.additive_overlay` when TRA currently has `austro_hungarian_releasable_focus`.
The existing `independence_wave_assign_focus_framework` helper then requires `can_attach_independence_wave_additive_focus_carrier`, which checks the IW-023 lifecycle receipt and the same carrier before publishing the overlay flags.
When that tree is absent, setup retains the pre-existing full Event 006 framework path.
The TRA lifecycle flag is set before assignment, so the existing accepted additive-carrier predicate can pass for this package.

The previous unconditional full-framework assignment called `load_focus_tree = { tree = independence_wave_focus_tree keep_completed = no }` and replaced a meaningful carrier.
The installed vanilla `austro_hungarian_releasable_shared.txt` defines `austro_hungarian_releasable_focus`, admits TRA when the required DLC is active, and retains `HABSBURG_part_of_something_bigger`.
The current repository carrier file `common/national_focus/austro_hungarian_releasable_shared.txt` already preserves that tree and imports all eight reviewed Event 006 overlay nodes for TRA.
The vanilla `effects_documentation.md` documents that `load_focus_tree` sets the country's tree, while `triggers_documentation.md` documents `has_focus_tree` as checking the current tree.
The accepted Event 006 focus architecture says existing meaningful trees retain their carriers and receive additive content.
The existing Bosnia setup uses the same conditional carrier-preservation pattern.

The prepared IW-023 package trigger previously hard-required the full framework, which contradicted the accepted carrier-preservation branch even when the additive carrier was correctly registered.
It now delegates to `has_independence_wave_generic_focus_contract`, whose full-framework and additive-carrier branches validate the selected assignment consistently.
The TRA setup order sets `independence_wave_iw_023_lifecycle_initialized` and `independence_wave_focus_carrier_registered` before assignment, then checks the prepared-package predicate before activation; the additive branch also requires the Austro-Hungarian tree through `can_attach_independence_wave_additive_focus_carrier`.

## Files and identifiers

- Gameplay: `common/scripted_effects/006_independence_wave_balkan_package_effects.txt`.
- Package validator: `common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt`.
- Setup effect: `independence_wave_setup_iw_023_transylvania`.
- Assignment variable: `independence_wave_focus_assignment_input`.
- Carrier: `austro_hungarian_releasable_focus`.
- Existing gate: `can_attach_independence_wave_additive_focus_carrier`.
- Fallback: existing `independence_wave_focus_assignment.full_framework` when the Austro-Hungarian carrier is not present.

## MCP and source review

Before the edits, `hoi4.focus_inspect` returned `FOCUS_INSPECTED` at revision `aa3ab963aef54dc3d25104b1178be069274bb3962a317dde81796371f5cfcfcd`, and `hoi4.focus_render` returned `FOCUS_RENDERED` with layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`.
After the carrier-selection and prepared-trigger edits, inspect returned `FOCUS_INSPECTED` at revision `5d5ee538def8f92ad98523f6f8c750cdda97ddc9343ed32211192e1cd80d8b40`, and render returned `FOCUS_RENDERED` with the same layout hash.
Both views report 184 focuses, 196 connectors, zero crossings, zero node intersections, and one existing ten-column connector warning.
The only other focus warning is the existing vanilla `continuous_restrict_freedom_desc` localisation reference; neither warning points to the TRA carrier edit.
The MCP has no focus-tree semantic compare route in the exposed live schemas, so identical before/after layout hashes are the available graph evidence.

A final inspect of the existing `austro_hungarian_releasable_focus` carrier returned `FOCUS_INSPECTED` at revision `bb6d5881f7e4da9d9ed7e8077dce3b56edf646ce67f76712fa5a027340c227f5`; render returned `FOCUS_RENDERED` with layout hash `8e1c44e617e03adc234cb622e850552e6b313e775be0cd3452761fa1f52f98bf`.
It reports 56 focuses and 62 connectors, with one pre-existing connector crossing and node intersection among the vanilla-tree diagnostics.
The package change does not edit that tree's nodes or layout.

The source review confirms the TRA carrier registration and lifecycle setter precede assignment, and the prepared-package trigger now accepts the generic full-framework or reviewed additive-carrier contract.
No focus node, prerequisite, reward, localisation key, icon, AI weight, decision, event, admission gate, or route identity changed.

## Coverage and validation limits

The fresh regional overlay audit remains the authority for matrix coverage: REG-03 is partial, with no country-specific Transylvania focus family; REG-06's literal “Volga overlap packages” mapping remains unresolved; other regional rows remain partial or absent.
This carrier correction restores the accepted existing-tree behavior but does not satisfy the package-specific focus-group requirement for IW-023 or add focus coverage to any other package.
The read-only `chaosx_ai_probability_auditor` completed `national_focus_ai_will_do` source discovery for the shared Event 006 focus file at source hash `1728c71832a1edec203cc0bbbcd96efb44f5517351bc1d4835705669335ffe6f`.
It found 184 candidates and an incomplete pool with 17 required inputs, no scenario-available candidates, and no candidate examples; the artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/be9d21881c553f1c41e2c55d63e978c1762a754356878f166fb532fb47e09441/18f73b553aa5ef7888a224ca3d26128005c32a6b402d7f14478c7fb0d5adfc26/probability-inspect-1728c71832a1.json`.
The existing 22-scenario set `event006_current_focus_route_matrix_2026_09_25` has hash `b252a5f84559be59e6d64c52e6c3c0a4826b71b45159d03f73b027e082436fd4`, but its nearest carrier scenario is Iceland and its flat inputs do not bind TRA package identity, carrier, completed-focus state, or external factors.
The handoff names `IW023_TRA_GOT_carrier_loaded` and `IW023_TRA_no_reviewed_carrier` without serializing their scenario definitions or hashes, so no scenario evaluation or same-scenario compare is supported and no TRA focus-selection probability is claimed.
The adapter's scenario limitations are unresolved; no AI weight was changed by this carrier correction.
No automated tests or live game were run, and the user's live session remains the runtime validation boundary.

No gameplay simplification or new fallback was introduced.
Whole Event 006 remains **HOLD / PARTIAL**.
