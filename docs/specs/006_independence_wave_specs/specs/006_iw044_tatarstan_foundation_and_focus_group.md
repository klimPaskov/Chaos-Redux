# IW-044 Tatarstan Founding and Shared-Focus Design

## Acceptance

Status: accepted design; implemented at source with the evidence limits below.

Acceptance basis: the user authorized all pending design choices in this Event 006 task and accepted the shared-focus architecture. The five-node group reuses the already admitted Tatarstan package hooks and the existing generic Event 006 tree.

The current parent instruction for this documentation-only IW-044 reconciliation explicitly identifies this as the accepted TAT spec and requires preserving the five-focus AND gates, founding route-cycle repair, and implemented-at-source disposition with limits.
That instruction reaffirms the bounded acceptance basis independently of the document's location or older status label; it does not approve whole Event 006 completion or close the separate auditors' comparisons.

The user-approved baseline keeps Tatarstan in the shared Event 006 focus tree, keeps the existing paid package decisions, and requires its founding mission to receive a government route before it can resolve.

## Founding government

The four government decisions must be visible and available while the Tatarstan Civic Compact founding mission is active, before a government has been installed, and while the package is not failed.

Each decision remains tied to its matching constitutional, traditional, popular-council, or emergency route. State 249 and the capital must remain under Tatarstan control, the original cost and duration remain in force, and only one government project may be active at a time.

The ordinary Tatarstan project layer opens only after the founding mission resolves, with the founding depot project as a specific exception.
The depot project may run during the mission when its existing industry/resource costs are affordable, so it can genuinely substitute for the assembly focus.
The government-choice opening is also separate from the ordinary layer so the mission does not exclude the very action it requires.
All paid TAT projects share one active-project slot; the founding mission itself does not occupy that slot.
The mission, project entry/cancellation, and focus group share the exact owned-and-controlled Kazan capital contract.

The founding window is 720 days.
Acceptance basis for this balance refinement: on 2026-10-03 the user directed continuation without waiting for input and instructed the parent to take the recommended option whenever a choice arises.
The parent accepted preserving every route project's existing costs and durations, extending the deadline from the nominal agrarian route's exact 600-day boundary, and providing civilian capacity through the existing assembly focus.
The provisional-assembly reward brings Kazan's civilian factories up to a centrally tuned target of four when fewer are present, adds only the deficit and matching building slots, preserves existing industry, and uses the existing depot-reward flag to prevent repeat grants.
This addresses the installed vanilla anchor's zero civilian factories without removing the government projects' factory, manpower, equipment, transport, or command costs.

## Shared-focus group

The IW-044 group is a five-focus package overlay inside `independence_wave_focus_tree` and does not define a second country focus tree.
Origin activation refreshes TAT's focus layout after its complete setup and network receipts are published, so the group's `allow_branch` checks are reevaluated after tree assignment.
The refresh retains the existing tree and completed focus history.

`Convene the Provisional Assembly` follows `independence_wave_prepare_capital_administration` and calls the existing provisional-assembly and depot hook.
That hook also establishes the bounded Kazan civilian-works reserve used by the founding administration.

`Guarantee River Communities` and `Unify the Border Guards` are sibling focuses after the assembly and call the existing community and guard hooks.

`Reconcile the Former-Host Ledgers` requires both sibling focuses through two separate `prerequisite` blocks, which express AND; multiple focus entries inside one block express OR.
The generic Event 006 founding-settlement focus is also required through `available = { has_completed_focus = independence_wave_complete_founding_settlement }`, rather than a third drawn prerequisite connector.
It uses the existing host-ledger hook and distinguishes a peaceful host, a host at war, and a former host that no longer exists in its completion tooltip.

`Connect the Volga Network` requires the host-ledger focus AND `independence_wave_recognize_fellow_new_states` through separate `prerequisite` blocks.
It additionally requires the generic founding settlement, a resolved Tatarstan crisis, stable Civic Concord and River Security, Independence Network membership, and an available League route.

The package decisions remain paid alternate routes. Their existing idempotence flags bypass the matching focus, preserving a single reward for each hook.
Each matching focus/project pair prevents the paid decision from starting while that focus has progress and prevents the focus from starting while the paid project is active.
This preserves the player's chosen cost/time path without a later free focus consuming the already-paid project reward.

The five existing hook effects remain the source of ledger changes, stability effects, host settlement, and network rewards. The generic full-tree focuses keep their shared rewards but no longer invoke Tatarstan's five package hooks.

## Assets and localization

All focus icons reuse registered sprites in `interface/006_independence_wave.gfx`.

| Focus | Reused sprite |
| --- | --- |
| Provisional assembly | `GFX_goal_independence_wave_founding_administration` |
| River communities | `GFX_goal_independence_wave_popular_councils` |
| Border guards | `GFX_goal_independence_wave_army_integration` |
| Former-host ledgers | `GFX_goal_independence_wave_former_host_settlement` |
| Volga network | `GFX_goal_independence_wave_league_congress` |

Focus names, descriptions, trigger tooltips, and package-effect tooltips live in `localisation/english/006_independence_wave_tatarstan_l_english.yml`.

The strategic cost row displays Stability and Command Power.
Its tooltip describes the applicable convoy/train transport price, temporary civilian-factory reservation, and the non-consumed War Support requirement; administration light/standard rows retain their existing factory reservation display.
The transport selectors use `NOT = { has_equipment = { convoy < constant:independence_wave_decision_cost.convoy_standard } }` and the corresponding `train_equipment < constant:independence_wave_decision_cost.train_standard` form.
This replaces the former strict `>` comparisons so stock exactly at the cost threshold qualifies, with convoy first, train second, and an either-resource fallback when neither is affordable.
Community effect text describes improved Civic Concord and falling Instability, while host text describes reduced bilateral disputes only for a living host at peace and leaves war or missing-host outcomes distinct.
These wording and selector repairs describe current source; payment helpers, asset registration, and live consumer behavior are outside this documentation pass's verification.

No new image, portrait, flag, or `.gfx` registration is required.

## Interactions and validation limits

The dedicated focus branch supplies Tatarstan's package-specific progression without replacing the generic focus framework, route-selection decisions, Event 006 league network, or shared country-package lifecycle.

The HOI4 focus MCP inspects direct `focus = {}` nodes but omits imported root-level `shared_focus` nodes from its rendered layout. The user accepted retaining the shared architecture and recording that package-group layout coverage as blocked.

## Future work

The group can receive additional Tatar-language institutional detail after grounded source research identifies specific councils, river authorities, and former-host claims.

Additional package focuses should reuse the current shared tree and package gate, preserve decision-to-focus reward bypasses, and add a separate proposal before introducing new government routes, assets, or country identities.

## Engine references

The offline National focus modding snapshot covers focus prerequisites and AND/OR grouping at lines 275–296, branch visibility and bypass at lines 405–429, shared-focus declaration and imports at lines 818–838, and default AI score behavior at lines 604–626. Snapshot SHA-256: `BD989A13237C464F140A0AA671CC42C30A48E84A27DAE791B8914654FB9C6203`.

The current parent reference receipt identifies the offline Triggers sections at lines 329–408 and 1509–1583, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`; `hidden_trigger` and `custom_override_tooltip` are specifically listed at lines 344–346.

The installed decisions documentation covers decision visibility and availability at lines 1–46. SHA-256: `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019`.

The current parent reference receipt identifies installed `has_active_mission` documentation at lines 3022–3030 and `has_decision` at lines 3693–3701, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
The older 2431–2488 citation is superseded by these current spans.

The offline Decision modding snapshot covers AI decision scores at lines 357–374, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`; the offline AI modding snapshot covers score-based selection at lines 26–37, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`. The four source-declared Tatarstan route scores were audited before editing and were left unchanged.

Vanilla `common/national_focus/baltic_shared.txt` provides shared-focus, prerequisite, position, and bypass examples. SHA-256: `A95FC995B2CC6B84CB7BDEFA2E7934F745917ECF5AAE5753824DCDEBCC0AB5A0`.

No dedicated installed national-focus documentation file was found under the vanilla `documentation` folder, so the shared-focus contract was checked against the offline wiki and the vanilla Baltic shared-focus implementation.

The live `hoi4.reference_context`, `hoi4.reference_search`, and `hoi4.reference_read` routes returned the cited offline wiki and installed-game sections. The focus context at limit 12 had no omitted sources; the decision context omitted trigger/localisation sections, which were then found and read with targeted searches. The installed game search found no focus-tree syntax documentation; the relevant installed documentation route gap is recorded, and the vanilla Baltic shared-focus source was read directly.

The current parent-supplied focus inspect/render revision `e33599f200fe25183c0b547a38071a48fc5b24ee1aa39fc93f02d737d9f60d17` reports 184 direct focuses, unchanged layout hash `ea3ad753bd8a8841e959710671564f9fa392b172c9cc8b8d2e7e0f6ea21ccafb`, no blockers, and an unrelated vanilla continuous-restrict-freedom localization warning; the render is 10712×1220.
The imported IW-044 `shared_focus` nodes do not appear in its focus count or rendered layout, so package-group attachment and geometry remain blocked from MCP proof.

All four current route decision inspections are `DECISION_ANALYZED_PARTIAL`, source revision `2c94644950a0f035dfe561a1880f38d7ac357a013f9b6d1fac5dc0db311fbc4e`, with one declared scenario each and 218 unresolved definitions.
The parent's linked constitutional-artifact read confirms `has_active_mission` is `TRIGGER_UNRESOLVED`, and setup variables and capital scopes are undeclared.
The separate probability auditor reports source hash `18379e2e28d5e1a0d7196fc07446eaf3052d2fb2d54620d5c89b7f669e705989`, 184 direct focus candidates, and zero matches for the five imported IDs.
Preserve that auditor's scenario-specific route and focus comparison handoffs as pending/blocked; no quantitative AI, live behavior, or whole Event 006 completion is established.

Reference routes are present and worked in the current parent pass.
The parent's equipment `hoi4.reference_read` at offline Triggers lines 1509–1583 returned `UNKNOWN scandir` in request-capacity, after which a direct local read succeeded; the curator also read that local section.
This specific retrieval failure does not mean that reference tools or source files are unavailable.

`hoi4.source_lookup` found the route-opening scripted trigger and its eight decision references at source revision `7c3604a5fca8b93845d0594e5094c810a3643ea03bed7ff560bf5eef6a4530be`. The same indexed route returned zero definitions for both the mod and vanilla shared-focus symbols and 17,544 unresolved references, so the shared-focus source definition and vanilla Baltic example were verified by direct file reads instead.
