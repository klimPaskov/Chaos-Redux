# IW-044 Tatarstan founding gate and shared-focus documentation handoff, 2026-09-27

## Scope, acceptance, and disposition

The user authorized the IW-044 shared-focus group and founding-route gate repair in the [accepted design](../../../specs/006_independence_wave_specs/specs/006_iw044_tatarstan_foundation_and_focus_group.md).

The five-focus group and the founding-route decision gate are **implemented at source** within the existing Event 006 Tatarstan package; the current files and line spans below are implementation evidence, not a separate acceptance basis or live-game proof.

The [package summary](../../../events/006_independence_wave/tatarstan_package.md) remains a description of the admitted IW-044 carrier and its bounded runtime flow.

Event 006 remains **HOLD / PARTIAL**.

## Inspected and changed files

| File | Role and disposition | Changed here |
| --- | --- | --- |
| `docs/specs/006_independence_wave_specs/specs/006_iw044_tatarstan_foundation_and_focus_group.md` | Accepted design with the explicit user authorization above; no promotion or redesign needed. | No |
| `docs/events/006_independence_wave/tatarstan_package.md` | Current package summary; source and evidence limits remain distinct. | No |
| `common/decisions/006_independence_wave_siberian_decisions.txt` | Source evidence for the founding mission and four route decisions. | No |
| `common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt` | Source evidence for the separate founding-choice, serialization, ordinary-project, and focus-group gates. | No |
| `common/national_focus/006_independence_wave_focus.txt` | Source evidence for five root-level imports and definitions inside the existing full tree. | No |
| `localisation/english/006_independence_wave_tatarstan_l_english.yml` | Source evidence for five focus names/descriptions and gate/tooltips. | No |
| `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` | Current source-of-truth ledger; inserted this exact tranche's implemented-source disposition and limits, and removed the stale “TAT group” work-queue wording. | Yes |
| `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` | Current resume ledger; inserted the exact source crosswalk and evidence limits, and changed the work queue to the remaining TAT layout and AI comparison. | Yes |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw044_tat_founding_focus_implementation_2026-09-27.md` | This documentation-only handoff. | Created |

No gameplay, localisation, package reference, specification, spreadsheet, prompt, or foreign-reaction plan file was changed.

No document was merged, deleted, rejected, or marked superseded.

## Exact five-focus source crosswalk

The existing `independence_wave_focus_tree` imports all five Tatarstan `shared_focus` IDs at [focus lines 96–101](../../../../common/national_focus/006_independence_wave_focus.txt#L96-L101).

| Player-facing focus | ID and source definition | Gate and existing hook |
| --- | --- | --- |
| Convene the Provisional Assembly | [`independence_wave_tat_convene_the_provisional_assembly`, lines 5216–5239](../../../../common/national_focus/006_independence_wave_focus.txt#L5216-L5239) | Follows `independence_wave_prepare_capital_administration`; the depot flag bypasses its existing assembly/depot hook. |
| Guarantee River Communities | [`independence_wave_tat_secure_river_communities`, lines 5241–5263](../../../../common/national_focus/006_independence_wave_focus.txt#L5241-L5263) | First sibling after the assembly; the communities flag bypasses its existing hook. |
| Unify the Border Guards | [`independence_wave_tat_unify_border_guards`, lines 5265–5287](../../../../common/national_focus/006_independence_wave_focus.txt#L5265-L5287) | Second sibling after the assembly; the guards flag bypasses its existing hook. |
| Reconcile the Former-Host Ledgers | [`independence_wave_tat_reconcile_former_host_ledgers`, lines 5289–5328](../../../../common/national_focus/006_independence_wave_focus.txt#L5289-L5328) | Requires both siblings and checks completed generic founding settlement before use; the host-ledger flag bypasses its hook, and the tooltip distinguishes peace, war, or no surviving former host. |
| Connect the Volga Network | [`independence_wave_tat_connect_volga_network`, lines 5330–5366](../../../../common/national_focus/006_independence_wave_focus.txt#L5330-L5366) | Follows the host-ledger focus and generic network-recognition focus; availability requires completed founding settlement, resolved compact crisis, stable ledgers, network membership, and the League route, while the corridor flag bypasses its hook. |

The [focus-group trigger at lines 240–249](../../../../common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt#L240-L249) requires active IW-044 origin, complete package setup, the full generic focus contract, state 249 as owned and controlled capital, and no failed or ended origin.

The focus names, descriptions, and focus-specific tooltips are in [Tatarstan localisation lines 133–150](../../../../localisation/english/006_independence_wave_tatarstan_l_english.yml#L133-L150).

The group uses the registered focus sprites and existing Tatarstan hook effects under the accepted design; this documentation pass created no asset or second focus tree.

## Founding-route gate source crosswalk

The [Civic Compact founding mission at decision lines 2837–2887](../../../../common/decisions/006_independence_wave_siberian_decisions.txt#L2837-L2887) requires stable compact ledgers, an installed route government, state 249 ownership and control, and capital control for successful resolution.

The [ordinary project trigger at lines 16–23](../../../../common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt#L16-L23) remains closed until the founding mission has resolved.

The separate [government-choice trigger at lines 25–32](../../../../common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt#L25-L32) requires the active founding mission, complete package setup, no failed or resolved crisis, and no installed route government; the [serialization trigger at lines 34–45](../../../../common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt#L34-L45) excludes another active government project.

The four [government route decisions at lines 3105–3284](../../../../common/decisions/006_independence_wave_siberian_decisions.txt#L3105-L3284) use those triggers in `visible` and `available`, retain matching route flags, require capital control and their existing costs, and retain their existing durations and government-install effects.

Their source-declared `ai_will_do` blocks occur at decision lines 3147, 3191, 3236, and 3280–3283; a same-scenario route-decision AI comparison remains pending and is not a passed balance result.

## MCP evidence and exact limitations

The parent-supplied focus MCP receipt records source revision `50daae4758395e86728a1e07dbc67e4a21eefe854cfc63b092c8ecf7a4b07938`, direct `focusCount` 184, unchanged `layoutHash` `ea3ad753bd8a8841e959710671564f9fa392b172c9cc8b8d2e7e0f6ea21ccafb`, and no blocking diagnostics.

That count describes direct inspected focus nodes and does not establish that the five imported root-level `shared_focus` nodes appear in the assembled tree layout.

The user accepted the shared architecture while imported nodes are absent from MCP inspect/render layout evidence; Tatarstan focus attachment, connector geometry, icon placement, and assembled-tree visual acceptance remain blocked as MCP evidence.

This curator called the exposed read-only `hoi4.focus_inspect` and `hoi4.focus_render` routes against the existing tree, and both returned `status=error`, `code=JOB_WORKER_EXIT`, blocker “The worker stopped without publishing a terminal job outcome,” and no artifacts.

The exposed read-only `hoi4.probability_inspect` route for the four government decision scores also returned `status=error`, `code=JOB_WORKER_EXIT` with the same blocker and no artifacts after a source-path request; the owner `chaosx_ai_probability_auditor` comparison under named matching scenarios remains pending.

Exposed tool names and the parent-supplied prior focus receipt are separate from current service health; no fresh successful focus render or quantitative route-choice result is claimed here.

No live-game, save/reload, or player-visible layout result is claimed.

## Documentation checks

Targeted source checks found each of the five Tatarstan focus IDs exactly once in the full-tree import list, exactly once as a definition, and exactly once as a localisation key.

All relative Markdown links in the changed map, resume packet, and this handoff resolve to existing files; both current ledgers retain **HOLD / PARTIAL**, the supplied focus revision, and the pending AI comparison.

The old “TAT group” continuation wording is absent from the current top sections of both ledgers, and the scoped tracked diff contains only the two authorized ledger files.

No accidental mid-sentence hard-wrap issue was found in the newly edited paragraphs of the map or resume packet or in this handoff; there are no affected paths in that scoped check, and headings, tables, and paragraph boundaries remain intact.

No gameplay, workbook, or live-game validation was performed because this was a documentation-only reconciliation with those surfaces read only; the failed MCP calls and pending owner comparison are recorded above.

## Current disposition and parent follow-up

| Surface | Disposition | Basis or remaining requirement |
| --- | --- | --- |
| Five IW-044 shared focuses and founding-route gate | Implemented at source | Explicit user-approved design and the exact focus, decision, trigger, and localisation lines above. |
| Imported shared-focus layout and attachment evidence | Blocked | Accepted MCP omission of imported nodes, compounded by this run's `JOB_WORKER_EXIT` on focus inspect/render. |
| Four government route decision AI comparison | Unresolved | The required scenario-specific `chaosx_ai_probability_auditor` comparison has not been returned; this run's probability inspect also failed. |
| Whole Event 006 | **HOLD / PARTIAL** | Existing recurring incidents, package readiness/admission, imported-focus proof, weighted logic, and other mapped gaps remain outside this tranche. |

The source map and resume packet no longer route the already implemented Tatarstan source group as an unstarted task; they route its imported-focus proof and route-decision AI comparison as remaining work.

No acceptance conflict was found within the named Tatarstan design and source files, so no new design decision is requested from the parent.

No duplicate or stale prompt was named for this scope.

The parent should review the bounded source crosswalk, obtain focus evidence that includes imported shared nodes when the route supports it, and route the decision weights through `chaosx_ai_probability_auditor` under matching named scenarios before any stronger focus or AI claim.

## Parent follow-up (2026-10-03)

The [current parent review](006_iw044_tat_parent_review_2026-10-03.md) supersedes this historical balance snapshot for the 720-day founding deadline, deficit-only Kazan civilian-works reserve, and origin-activation layout refresh.
The government-choice gate, shared-focus architecture, existing route project costs/durations, and numeric AI weights are retained.
The source map and resume packet carry the corresponding current disposition and audit-route limits.
