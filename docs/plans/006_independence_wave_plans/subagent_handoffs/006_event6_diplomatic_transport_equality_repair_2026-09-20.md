# Event 006 diplomatic transport equality repair

Date: 2026-09-20.

Status: implemented as a bounded shared transaction repair; Event 006 remains HOLD / PARTIAL.

## Finding

The shared `can_pay_independence_wave_diplomatic_light_cost` and `can_pay_independence_wave_diplomatic_standard_cost` triggers accepted a stockpile exactly equal to the displayed convoy debit through `NOT = { has_equipment = { convoy < cost } }`. Their payment effects selected convoys only with strict `convoy > cost`, so an exact convoy balance could pass availability and then fall through to the train payment branch.

## Change

`independence_wave_decision_pay_diplomatic_light` and `independence_wave_decision_pay_diplomatic_standard` now select convoys with the same inclusive `NOT = { has_equipment = { convoy < cost } }` contract used by their affordability triggers. Actors below the convoy debit still use the existing train fallback. No cost amount, command-power charge, localisation, caller, AI weight, or decision lifecycle changed.

The FORM-08 administration-strategic payment remains unchanged because its package-local affordability trigger intentionally uses strict convoy/train capacity checks. The IW-093/IW-098 paid transaction paths also remain unchanged because they own separate package-local resource selection and ledger semantics.

## Validation

The focused source assertion confirms inclusive light and standard predicates, inclusive light and standard payment branches, the unchanged FORM-08 strict branch, and zero remaining strict convoy branch inside the two shared diplomatic payment helpers.

`python -B .tools/audit_event6_allocator.py --strict` passes with 32 content-attested packages, 29 compatible reservation groups, 40 runtime adapters, and the exact 3/4/5/7/10 automatic ladder. `python -B .tools/audit_event6_scenario_matrix.py` passes all 32 declared cells and eight edge cases with success-only `chaosx.nr6.2 -> chaosx.triggerable_scenarios.80` publication.

The focused read-only `hoi4.event_inspect` lint for `common/scripted_effects/006_independence_wave_decision_effects.txt` returned `EVENT_INSPECTED_PARTIAL` with source revision `7bc390e9516d5b5dfe63dbd72b96eddd673953d1ad2177f259c603cef9509573`, zero blocking diagnostics, and zero skipped sources. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a036419150aaacc4feca6f649fc4cd1381f1d4662e1a1b1130bd93fe15ec6c5c/9df00d4b70f7026ae523d44137a75be41d5b9b0015eb1883cc5b2884ad539e41/event-lint-7bc390e9516d.json`.

The matching read-only options render returned `EVENT_RENDERED_PARTIAL` at the same graph revision with zero blocking diagnostics. Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d0b7ebcbb8c9ecc380783b953e6337966d36e1d6b09bc06a68d18e5d05aab81/3e6ad24a601c9d8b378c74d0403d02d099e540b6c23d5fbdb06c354d3e6dd692/event-options-7bc390e9516d-manifest.json`.

The Event MCP graph revision remained the same as the preceding focused decision surface because helper/lifecycle projections are deferred; no semantic before/after comparison is claimed from that structural receipt.

## Scope limits

This repair changes only resource selection at exact convoy equality. It does not establish campaign probability, native decision-row rendering, live execution, save/load behavior, package admission, Join, identity, portrait, flag, GUI, asset, or audio completion. No fallback or central admission widening was used.
