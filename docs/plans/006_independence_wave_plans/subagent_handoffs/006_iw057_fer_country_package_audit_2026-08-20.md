# IW-057 Far Eastern Republic package audit handoff — 2026-08-20

## Disposition

IW-057 remains HOLD / package-local PARTIAL. The package has a narrow source-backed planner tranche, but it is not admitted to the central Event 006 runtime because the required central adapter and runtime content-attestation receipt are intentionally absent. No central attestation, preflight, SCN-008, scenario, Join, or shared focus-list surface was widened.

The package-local planner gate was corrected in `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt`. Before the change, `can_plan_independence_wave_package_iw_057` delegated to the retired generic `is_independence_wave_candidate_tag_available` gate, which requires `independence_wave_package_content_ready`; repository scan found no setter for that flag. After the change, the planner calls the existing exact `is_independence_wave_exact_package_iw_057_tag_available` wrapper, which checks the dormant FER shell, origin availability, and an available 408/409 anchor. The central attestation hard stop remains unchanged.

## Immediate answer: why manual `chaosx.nr6.1` can select zero countries

`events/006_independence_wave.txt` does not choose FER directly. `chaosx.nr6.1` calls `independence_wave_prepare_and_execute_standalone_incident`, which runs the automatic plan, regional allocator, and frozen-package execution in `common/scripted_effects/006_independence_wave_execution_effects.txt` and `common/scripted_effects/006_independence_wave_package_allocator_effects.txt`.

The old Region 05 planner path used `FER = { is_independence_wave_candidate_tag_available = yes }`. That generic trigger requires both an available original country and `has_country_flag = independence_wave_package_content_ready` in `common/scripted_triggers/006_independence_wave_package_triggers.txt`. No repository setter was found for that flag, so IW-057 could not contribute a candidate through that path even though its package-local exact wrapper and 408/409 reservation contract existed.

The local fix removes that unreachable generic gate, but it does not make FER centrally selectable by itself. `independence_wave_calculate_package_candidate_weight` in `common/scripted_effects/006_independence_wave_package_planner_effects.txt` and `independence_wave_begin_package_reservation` still require `has_independence_wave_runtime_package_content_attestation_for_execution_id`. IW-057 is absent from the central attestation list in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`. Therefore a zero-country result remains expected fail-closed behavior whenever no centrally attested package can be reserved; it is not evidence that the 408/409 transaction is unordered.

The post-patch custom weighted-pool MCP inspection reports `poolComplete=false`, `candidates=0`, and `available=0` for the planner source. This is structural evidence of the central fail-closed state, not a quantitative balance claim. The mandatory `chaosx_ai_probability_auditor` worker was not present in the callable tool inventory, so no worker-backed probability signoff or compare was claimed.

## Ordered anchor transaction and safety review

The source order is coherent and remains package-local at the FER edge.

- `common/scripted_effects/006_independence_wave_packages_region_05_effects.txt` assigns IW-057, reservation group `rg_408_409`, region/depth/archetype/disposition, and selects state 408 first or state 409 second only when the candidate-anchor trigger passes. It saves the selected anchor and former host.
- The shared planner reserves the country and anchor before execution.
- `common/scripted_effects/006_independence_wave_execution_effects.txt` loads the frozen country, anchor, and former-host arrays before execution.
- `independence_wave_prepare_frozen_country_packages` sets the execution country's capital to the frozen 408/409 anchor with `remember_old_capital = no` before dispatching package setup.
- The FER setup effect then performs the package-local roster checkpoint, force profile, route/ledger/idea initialization, and founding mission setup.
- `is_independence_wave_exact_package_iw_057_runtime_ready` requires setup completion, current force generation, origin continuity, anchor ownership, a capital anchor in 408/409, and a surviving former host with protected state.

The collision and origin guards are present in `has_independence_wave_candidate_anchor_available`, the FER exact tag wrapper, `can_initialize_independence_wave_iw_057_package`, and the shared dispatch preflight. They reject Soviet origin/controller conflicts, protected-state conflicts, reserved anchors, wrong original tags, wrong package/region/depth/archetype, and missing 408/409 ownership/control. Dormant vanilla FER state 563 is a source baseline only; current execution deliberately reanchors to 408/409.

The package documentation is stale at `docs/events/006_independence_wave/far_eastern_republic_package.md` where it says the pre-release gate tolerates dormant capital 563. Current source accepts only an available 408/409 candidate anchor. Git history shows the old 563 alternative was removed in commit `b39845ffd` after being introduced by `a9f5f8771`; this handoff does not widen the 563 gate.

## Package coverage checklist

| Surface | Current state | Admission consequence |
|---|---|---|
| Tag and loader | `FER` is mapped by vanilla; IW-057 is present in Region 05 package planning and has exact package triggers/effects. | Package-local loader exists; central attestation is still absent. |
| Anchor and map | Ordered 408/409 anchor selection, ownership/control checks, capital reanchor, and former-host protection are present. | MCP map evidence found no FER-specific geometry or membership defect. |
| Host, collision, origin | Exact wrapper and shared preflight reject invalid origins, collisions, reserved anchors, and protected-state conflicts. | No source-backed reason to widen central guards. |
| Force profile | `regular_defectors`, `p57`, current generation, five reinforcement paths, navy/air inheritance, and roster checkpoint are wired. | Setup is fail-closed on missing parent receipts. |
| Politics and parties | FER package setup applies the accepted package-local political setup and localized party/country strings. | Identity-rights receipt remains required. |
| Leader, portrait, flag, advisor | No accepted Event 006 FER character, portrait, flag, cosmetic-tag, or rights manifest exists. Vanilla fallback `gfx/leaders/005_soviet_collapse/FER_leader.dds` is not Event 006 identity evidence. | Blocking identity/rights gap; do not invent or reuse evidence. |
| Focus | FER uses the shared `independence_wave_focus_tree` callbacks; no dedicated FER tree or assignment is claimed. | Focus is not a package admission blocker, but global MCP diagnostics remain. |
| Mission and decisions | One 420-day founding mission and ten project decisions exist with package localization. | Project-ready helper omits an anchor-owned check; see defects below. |
| Ideas | Seven package ideas, lifecycle cleanup, and shared icon references exist. | No missing package-local idea key was found. |
| Starting setup | Vanilla FER history supplies capital 563, three research slots, democratic politics, and baseline technology; Event 006 force setup is dynamic after execution. | No package-local OOB/industry expansion was justified. |
| Technology | FER inherits vanilla technology and shared force effects. | Technology Tree Viewer is not installed, so tree-level viewer evidence is unavailable. |
| AI | Four IW-057 strategy blocks exist. | Probability worker unavailable; settled strategy also lacks setup/current-generation guards and needs a separate reviewed balance pass. |
| Cleanup | Local cleanup removes the mission, ten decisions, seven ideas, ledgers, politics, and package flags. | Central cleanup remains outside package scope and is not widened here. |
| Localization and assets | FER package localization is present and BOM-encoded; package icons reuse accepted shared assets. | No identity asset/rights receipt exists for admission. |

## Concrete package-local defects and risks

1. Fixed in this tranche: Region 05 IW-057 planning no longer calls the unreachable generic content-ready trigger. This is the smallest source-backed change that lets the exact FER/408/409 wrapper participate in local planning without changing central admission.

2. Fixed in this tranche: `is_independence_wave_fer_project_ready` now calls the existing `has_independence_wave_fer_anchor_owned` trigger. The ten project decisions therefore fail closed immediately when neither ordered runtime anchor (408 or 409) remains owned and controlled. No project IDs, costs, durations, or central admission surfaces changed.

3. Package project constants are 45/75/105 days in `common/script_constants/006_independence_wave_far_eastern_constants.txt`, while the shared duration ladder includes 75/120/180/300 days. This is a design/balance discrepancy, not a safe syntax fix; no value was changed without the required baseline probability review.

4. The settled FER AI strategy in `common/ai_strategy/006_independence_wave_far_eastern.txt` lacks setup-complete/current-generation conditions used by the other package strategies. This is a weighted AI surface and requires the unavailable probability-auditor baseline/compare before any patch.

5. `has_independence_wave_fer_command_roster` trusts only `independence_wave_iw_057_identity_rights_cleared` and `independence_wave_iw_057_command_roster_ready`. The accepted identity/roster handoffs explicitly leave rights, portrait, flag, and manifest evidence unresolved. This intentional fail-closed behavior is the current release blocker.

## MCP evidence and limits

The mandatory read-only event route was run after the planner and project-readiness patches with selector `events/006_independence_wave.txt` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

- Event lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48e17a867a0e3f62ebdd0283352f92c6127c2ee1cdc9f0a5e87af833cda29af4/da274b785dec8a01b46494951ca4c4d9929fca086a64de8235ee5c2b77d1e2c7/event-lint-eb1d6f6a42dc.json`. The result is `EVENT_INSPECTED_PARTIAL` with `blockingDiagnostics=0`; deferred large-workspace helper/lifecycle projection remains.
- Event state render artifacts: manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/be217c303c47a7622b889085002c20b99b8aed0569fca4573331d5167cdf3aa2/791ddae05a6fad781233eaabacbbbd876eb91fb5511f727c8ee35466892c574d/event-state-eb1d6f6a42dc-manifest.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8562543fe522a0ee19d488ffcefb89dc8b43a0dc7505d62cc0ba9b304384782b/844898a228b5848784d1d1c6b50f916b55231d4c38e5e00f1f7c870879718011/event-state-eb1d6f6a42dc.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d3e2955fcbb9a50df318b2236360da7b3de9b9c876b5cd101613f356bfb1ea02/2a6e8a39418c37826c6eaf1f19c2dfd0dbc948b21238040755353283ffe689b0/event-state-eb1d6f6a42dc.png`. The event route reported `blockingDiagnostics=0`; the JSON/HTML siblings remain in the MCP manifest.
- FER planner probability artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/071f1fecc2b0f6f4eb547068856662dafd35f55fb91c5be143a71612edc7894f/9962b61c5570f833adddbcdc132f7d0ac5137a156058838b0307877a7f261d8d/probability-inspect-998f95c632e0.json`; it reports `poolComplete=false`, `candidates=0`, and `available=0`.
- FER decision probability artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/471ee4ca84e20cbac558d3d6b80cc88d6a49cdeec1535b2415c66c7df73acdbc/ca672e7effc37ad1f532cd6ffffa5e80ffd70d88c66e07154058a8e235e8678e/probability-inspect-d5c1417fc7a7.json`; it reports 11 structural candidates and 0 available candidates.
- FER AI probability artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc7b1e7bbb5d69865d0758594f2e726a4bf401592e7ee331d9ee13235f7eb35a/569928df82cbbb1a62ee6c3122d3ed622377b7453213054cdfcc85ee834adf09/probability-inspect-4b1b9d0035ee.json`; discovery found no weighted surfaces. This does not replace the mandatory worker route.
- Focus inspect/render used the shared `independence_wave_focus_tree`; no FER-specific source error was found, but global diagnostics include 14 unrelated missing continuous-focus icons/layout warnings. The focus artifacts are recorded in the earlier FER handoff and are not repeated as an admission claim here.
- Map inspect/render covered states 408, 409, and 563 plus coastlines, ports, victory points, resources, buildings, supply nodes, railways, and adjacencies. State/region membership and geometry were available; global position/locator diagnostics were unrelated to FER. The validated map render artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd8b53eb2549add50b207cbe2fd618aafa44f6729a7363de31f02dba24b7b466/bf6ee43bc71a5b51d3008995544cb6ff24fe0f2b4563cc48bab2e3ed1534891d/map-state.png`.
- Technology scan returned `technology-scan-b2e5b76ec3dc.json` with global unresolved issues; the installed package exposes no Technology Tree Viewer. FER uses vanilla/shared technology only, so no viewer-backed FER technology claim is made.

The post-tranche refresh of the Event 006 source returned the same source revision `98ac244e0b194a88389dbe53658d4876e5d76d2c5eb52b52ff572abea77b4fe3`: `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL`, both with zero selected blocking diagnostics and the documented large-workspace helper/lifecycle deferral. The refreshed state render produced the linked JSON/SVG/PNG/HTML bundle under `event-state-98ac244e0b19-*`; this is structural evidence only and does not waive central attestation or asset gates.

## Validation and changed files

`python -B .tools/audit_event6_allocator.py` completed with the repository allocator audit, including Event 006 order/anchor checks, package publisher counts, attestation counts, reservation groups, and standalone witness checks. The audit remains at the current 149 publishers / 40 adapters / 32 attestations / 29 groups / 161 unattested boundary.

The source files changed by this tranche are `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt` (exact FER planner wrapper) and `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt` (anchor-owned project readiness). No tags, states, leaders, parties, focus IDs, localization keys, formables, flags, portraits, or rights receipts were added or altered.

No map write was performed, so no map apply/rollback evidence is applicable. No live HOI4 launch or playtest was performed. No central adapter, attestation, preflight, scenario, Join, or shared focus-list surface was changed.

## Parent review / next tranche

The parent should review the planner and anchor-owned readiness changes and keep IW-057 centrally HOLD until the accepted identity/rights, command-roster, portrait, flag/symbol, and runtime attestation evidence exists. No probability-bearing surface was changed, so the existing structural probability receipts remain score-only and no quantitative balance claim is made.

This handoff deliberately does not claim full package admission, does not invent FER identity evidence, and does not stage or commit changes.
