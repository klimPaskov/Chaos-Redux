# IW-033 / IW-041 decision post-patch audit

Date: 2026-08-05

Owner: `chaosx_decision_mission_auditor`

## Scope

This audit inspected only the Event 006 Karelia IW-033 and Crimean Tatar State IW-041 decision package after the owner reserve-floor patch.

The reviewed gameplay surfaces are `common/decisions/006_independence_wave_karelia_crimea_decisions.txt`, the matching package triggers and constants, the package effects that initialize and resolve the foundations, and the package category.

## Issue list

### Critical, fixed: the foundation AI gate made the foundation impossible for AI countries

`independence_wave_kc_ai_foundation_ready` previously required `independence_wave_kc_foundation_settled`.

Every regular ledger project and every government action applies `factor = 0` when that helper is false, but the passive foundation mission requires both ledgers at 65 and a route government before it can set the settled flag.

Karelia starts at 36 forest supply and 42 civic mandate, and Crimea starts at 34 return capacity and 40 land settlement.

The actions whose AI scores were therefore forced to zero are the only package-local way to raise those ledgers and select the needed government.

The completed narrow fix changes only the AI-only helper `independence_wave_kc_ai_foundation_ready`.

It now accepts the exact active package's completed setup flag or the settled receipt, while still requiring package identity and rejecting `independence_wave_kc_foundation_failed`.

Player visibility, availability, costs, effects, active-project limits, and the reserve-floor predicates were not changed.

No other local decision, mission, cleanup, or localisation defect was found in the requested scope.

## Decision category lifecycle

`independence_wave_karelia_crimea_category` appears only for the active KAR or CRI package and owns two passive founding missions plus 20 regular decisions.

The foundation missions activate from their exact package setup receipt, run for 210 days, resolve only after stable package ledgers and a route government, and set the settled receipt on success.

One paid project or government action may run at a time through `has_independence_wave_karelia_crimea_active_project`.

A foundation failure remains an action lock, so the fix does not create a recovery or equipment-spending loop after failure.

KAR and CRI cleanup remove their own mission and decisions, including the shared former-host and network actions.

## Founding mission quality

| Mission | Owner | Category / region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `independence_wave_kar_hold_statehood_foundation` | KAR | Shared category, state 146 | Stable Karelian ledgers, valid route government, active package receipts, controlled capital | 210 days | `independence_wave_kc_resolve_foundation` | Shared failure bundle | None found |
| `independence_wave_cri_hold_statehood_foundation` | CRI | Shared category, state 137 | Stable Crimean ledgers, valid route government, active package receipts, controlled capital | 210 days | `independence_wave_kc_resolve_foundation` | Shared failure bundle | None found |

Both remain passive by design: each retains `available = { always = no }` and lacks `selectable_mission = yes`.

## Cost and requirement clarity

The eight local projects retain their package-specific concrete costs: command power with trains, infantry equipment and support equipment, manpower, convoys, or fuel.

The current local cost localisation provides normal, blocked, and hover variants.

The AI-only reserve checks do not alter player payment eligibility.

## AI validity and route locks

The static census found all 20 regular decisions retain all three owner-patch controls:

- `independence_wave_kc_ai_foundation_ready`
- a KAR, CRI, or combined lower-ledger preference helper
- a package-specific command/manpower, land-material, maritime, diplomatic, or major-security floor helper

The corrected foundation helper admits only the setup flag that matches the active carrier.

Former-host actions still require a living, peaceful saved former host, and the network action still requires a live league phase.

## Localisation, GUI, cleanup, and exploit risk

`docs/events/006_independence_wave/karelia_crimea_packages.md` now states the corrected AI lifecycle.

No player-facing localisation key changed.

The category has no `scripted_gui` binding, so there is no decision-owned GUI surface for `hoi4.gui_inspect` or `hoi4.gui_render` in this scope.

The fix leaves one-time action flags, the one-active-project guard, failure lock, and package cleanup unchanged.

## Changed files and identifiers

- `common/scripted_triggers/006_independence_wave_karelia_crimea_package_triggers.txt`: changed `independence_wave_kc_ai_foundation_ready`.
- `docs/events/006_independence_wave/karelia_crimea_packages.md`: corrected the AI-behavior description.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw033_iw041_decision_post_patch_audit_2026_08_05.md`: this handoff.

Before the change, all 20 regular decisions received an AI zero-weight modifier until foundation settlement, which cannot occur without those decisions.

After the change, those decisions may receive nonzero willingness after the matching package setup, subject to their existing costs, capital, route, active-project, former-host, league, lower-ledger, and reserve-floor gates.

## Meaningful validation

The static decision census verified 20 regular decisions with all three AI modifiers and two passive founding missions.

Fresh MCP probability inspection used `mission_ai_will_do` against the final decision source revision `ba3b740f7132ca6668d869ff4fd79a6a0ed7e5fdf7772492e9770498263ba36f`.

It reports 19 discovered candidates, 14 required inputs, an incomplete runtime pool, and two unresolved inputs: [probability inspection artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0279abaa354293edefd66c1dcf388a31fdabc9f2f120641dfd32eab9a560873c/34717b4c80182fd7cecd564f8994d438b3228e778552b8196e22cef1f123c6ad/probability-inspect-e5af5906af88.json).

The matching typed-state evaluation covered `PACKAGE_KAR_FOUNDING`, `PACKAGE_CRI_FOUNDING`, `PACKAGE_KAR_WAR`, and `PACKAGE_CRI_SETTLED`.

Its only diagnostics were the intentional `NEVER_ELIGIBLE` findings for the two passive founding missions: [typed-state evaluation artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/df4c3967503207d39bc464d65e2e83ff047faea28270c66d01026744eaec949a/3fe05b06a5d82d269e0e92dd7de538ce4296e3d871ec3ebfe3ba6b0ab266ddb5/probability-873a83b5767ac818381d7b06.json), scenario hash `f5ea20a48811380030e56b5865d0cba9057f6ef9ae9eb99b2e6f2c994745f922`.

The final source-level result is score-only, not a click probability: matching package setup or settlement can now make the foundation helper true, while foundation failure makes it false.

## Skipped meaningful validation and remaining risks

No dedicated decision or mission inspection/render transport exists in the installed MCP, and no package-owned scripted GUI exists.

The mandatory `hoi4.probability_compare` could not create a valid before/after receipt because the cached baseline is an analysis artifact rather than an accepted `before` source, and no old source path exists.

The adapter rejects cached `analysisId`, `id`, `uri`, `artifact`, and `sourceHash` as `before` inputs.

The same-path comparison completed with zero changes but is not treated as a patch comparison: [same-path capability artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc9dbecaf5a3967108998eaef6dda013ca4d5c7329edfc20906b7b8b7c04b6ff/c3b86f9738e71f157e159b21554febfe72e5678324cc0d384ea7246230fe8375/probability-1f9d31215f9ea367038586da.json).

Runtime pool completeness, full typed reserve/capital/route state, normalized decision selection, rank ordering, and live game behavior remain unresolved.

No game launch was performed under repository rules.

No separate improvement plan was written because the repaired defect is a local AI trigger gate, not a new decision system.
