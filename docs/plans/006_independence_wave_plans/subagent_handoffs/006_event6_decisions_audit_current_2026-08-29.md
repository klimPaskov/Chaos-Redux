# Event 006 decision and mission audit — current 2026-08-29

Date: 2026-08-29

Status: HOLD / PARTIAL for the decision and mission surfaces.

Mode: Read-only audit. The only repository write made for this task is this dated handoff. No gameplay, AI, event, decision, mission, scripted-GUI, localisation, asset, plan, or spreadsheet source was patched, and no commit was created.

## Scope and authority

The audit covers Event 006 Independence Wave decisions, decision categories, automatic and selectable missions, timed objectives, scripted-GUI-owned status surfaces, costs, requirements, tooltips, AI targets and weights, route locks, cleanup, exploit risk, and pre-event visibility.

The controlling pre-event requirement is explicit in docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md:9-15 and docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md:41. Before the public Event 006 report fires, there must be no pressure category, mission, cost, queue, history row, or other Event 006 indication. The coding prompt repeats the same absolute gate at docs/specs/006_independence_wave_specs/prompts/independence_wave_coding_prompt.md:48-50.

The accepted SCN-008 triggerable scenario is separately specified at docs/specs/006_independence_wave_specs/prompts/independence_wave_coding_prompt.md:181-196. That selector and confirmation flow are an explicit launcher; the finding below concerns its Event 006-branded failure result and ledger before the public report, not the existence of the accepted launcher itself.

I read AGENTS.md, .agents/skills/chaos-redux-decisions-missions/SKILL.md, .agents/skills/chaos-redux-events/SKILL.md, and .agents/skills/chaos-redux-subagents/SKILL.md. I also consulted the required offline Paradox wiki pages in paradox_wiki/ and the relevant vanilla documentation under C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\, including decision, trigger, effect, scripted-GUI, localisation, and script-constant references.

## Required MCP evidence and exact blocker

The required production decision/GUIs and weighted logic could not be inspected in this runtime. No callable HOI4 MCP entries for hoi4.gui_inspect, hoi4.gui_render, hoi4.probability_inspect, or chaosx_ai_probability_auditor are exposed in the current functions.exec tool catalog. The repository still declares the hoi4_agent_tools server in .codex/config.toml, so this is a tool exposure/transport blocker rather than a source absence.

Consequently, there is no current MCP GUI artifact, production render, click-region report, state/resolution matrix, probability scenario, probability evaluation, or probability compare result. Source review and the local semantic GUI validator below are not substitutes for that required engine evidence. HOI4 was not launched.

## Executive disposition

The normal post-event category and package surfaces are substantially active-origin gated, and the retired pre-event crisis helpers are inert. The strict pre-event contract nevertheless has a source-proven SCN-008 exception: a failed scenario with one or more blocked packages can display an Event 006 report and open an Event 006 scenario ledger without firing the public Event 006 report or creating an active origin.

The largest implementation-wide clarity issue is the administration cost contract. Thirty Event 006 decision blocks require the civilian-factory availability gate and display the factory in the generic administration cost string, but do not reserve or consume a factory in the decision block. DM-35 additionally hides the always-paid diplomatic cost on its Later line. This needs an owner decision per action family before any blanket localisation or modifier edit.

The package foundation missions also activate automatically but are absent from the corresponding package-local active-project lock. This allows the passive founding crisis to run alongside package paid projects. Existing historical package policy intentionally permits cross-package/shared operation parallelism; the narrow unresolved question is whether each package's own paid project lock should also serialize its founding mission.

Decision-category density and status-GUI cognitive load remain unproven because the mandatory production render is unavailable. Static source counts exceed the six-action design ceiling in several categories, although individual activation and route locks may hide most children at runtime.

## Severity-sorted findings

### High / P1 — SCN-008 failure result exposes an Event 006 surface before the public report

The delayed SCN-008 barrier has an early invalid-queue failure branch at events/006_independence_wave.txt:553-577. Separately, after scenario allocation or execution has built blocked-package rows, independence_wave_trigger_scenario enters its failure path at common/scripted_effects/006_independence_wave_scenario_effects.txt:1379-1421, freezes that summary, and schedules chaosx.triggerable_scenarios.80 after one day without firing chaosx.nr6.2.

The public Event 006 report is chaosx.nr6.2 at events/006_independence_wave.txt:71-91. It is only triggerable when the presentation count is greater than no_candidates. The failed SCN-008 branch does not fire chaosx.nr6.2.

The result event chaosx.triggerable_scenarios.80 nevertheless permits option .a when either the scenario is committed or the blocked-package array is non-empty at events/006_independence_wave.txt:584-607. In the execution-failure path, the frozen blocked-package rows satisfy the second condition, so option .a can be shown even though .2 was never fired. The result event is visibly Event 006 branded: its title and description are chaosx.triggerable_scenarios.80.t and .80.d, and it uses GFX_report_event_006_asset_001_wave_summary at events/006_independence_wave.txt:584-589. Its localisation says Every Banner Rises and describes an incident record at localisation/english/006_independence_wave_scenario_l_english.yml:33-38.

Option .a sets independence_wave_scenario_ledger_visible at events/006_independence_wave.txt:603-607. The category then requires only that flag and a non-empty blocked array at common/decisions/categories/006_independence_wave_categories.txt:607-618. The three zero-cost navigation decisions are visible while that flag is set at common/decisions/006_independence_wave_decisions.txt:936-1008; previous and next additionally require more than one blocked row. Their labels are Unavailable Movements, Previous unavailable movement, Next unavailable movement, and Close the record at localisation/english/006_independence_wave_scenario_l_english.yml:48-55.

The successful scenario path at common/scripted_effects/006_independence_wave_scenario_effects.txt:1362-1378 sets independence_wave_scenario_committed, applies the releases, and fires chaosx.nr6.2 before the delayed .80 summary. The execution-failure path at :1379-1421 freezes the blocked rows and fires only .80. This makes the failure-ledger leak deterministic when blocked candidates exist; it is not a speculative stale-flag report.

Recommended owner fix: make the Event 006 result and ledger publication require a current successful public-report receipt, not merely blocked-package data. The narrowest strict-gate choice is to suppress the Event 006-branded .80 result and ledger option on the failure path, or to route any needed blocked-candidate explanation through a non-Event-006 scenario result that the owner explicitly accepts under the superseding requirement. Adding an active-origin predicate only to the category is insufficient because the .80 event and its report text already expose the indication. Do not set the persistent runtime-unlocked flag on a failed scenario. If the existing independence_wave_scenario_committed flag is used as the success receipt, it must be used only for the committed path at :1362-1378 and must not be allowed to become stale across reset.

### High / P1 — Administration factory requirements are disclosed but not reserved or consumed in 30 decision blocks

The shared affordability helpers require available civilian factories plus command power and manpower at common/scripted_triggers/006_independence_wave_decision_triggers.txt:229-239. The shared payment helpers pay only command power and manpower for administration light and standard at common/scripted_effects/006_independence_wave_decision_effects.txt:125-133. A civilian factory is reserved only when an individual decision declares a civilian_factory_use modifier.

The generic administration strings show all three values, including the factory icon, at localisation/english/006_independence_wave_decisions_l_english.yml:38-41 and blocked variants at :62-67. This is correct for decisions that actually declare the modifier, such as DM-02 at common/decisions/006_independence_wave_decisions.txt:96-105 and DM-04 at :213-222. It is not correct for the following blocks, which use can_pay_independence_wave_administration_light_cost or can_pay_independence_wave_administration_standard_cost but have no civilian_factory_use modifier in the same decision:

- common/decisions/006_independence_wave_balkan_decisions.txt:131 independence_wave_axx_ratify_municipal_charter
- common/decisions/006_independence_wave_balkan_decisions.txt:146 independence_wave_axx_convene_mountain_workers
- common/decisions/006_independence_wave_balkan_decisions.txt:372 independence_wave_bos_ratify_sarajevo_charter
- common/decisions/006_independence_wave_balkan_decisions.txt:387 independence_wave_bos_convene_drina_workers
- common/decisions/006_independence_wave_balkan_decisions.txt:606 independence_wave_bbx_ratify_municipal_charter
- common/decisions/006_independence_wave_balkan_decisions.txt:621 independence_wave_bbx_convene_mountain_workers
- common/decisions/006_independence_wave_balkan_decisions.txt:836 independence_wave_mac_ratify_municipal_charter
- common/decisions/006_independence_wave_balkan_decisions.txt:851 independence_wave_mac_convene_workers_and_rail_council
- common/decisions/006_independence_wave_balkan_decisions.txt:1066 independence_wave_bax_ratify_federal_charter
- common/decisions/006_independence_wave_balkan_decisions.txt:1081 independence_wave_bax_convene_workers_and_rail_council
- common/decisions/006_independence_wave_balkan_decisions.txt:1550 independence_wave_tra_ratify_federal_charter
- common/decisions/006_independence_wave_balkan_decisions.txt:1565 independence_wave_tra_convene_workers_and_rail_council
- common/decisions/006_independence_wave_decisions.txt:379 independence_wave_retain_former_host_officials
- common/decisions/006_independence_wave_decisions.txt:1945 independence_wave_balance_patrons
- common/decisions/006_independence_wave_form03_decisions.txt:282 independence_wave_form03_publish_member_language_codes
- common/decisions/006_independence_wave_iw043_iw058_decisions.txt:164 independence_wave_iw043_ratify_mari_udmurt_language_rights
- common/decisions/006_independence_wave_karelia_crimea_decisions.txt:247 independence_wave_kar_ratify_constitutional_mandate
- common/decisions/006_independence_wave_karelia_crimea_decisions.txt:333 independence_wave_cri_ratify_constitutional_mandate
- common/decisions/006_independence_wave_mediterranean_decisions.txt:88 independence_wave_cor_constitutional_communes
- common/decisions/006_independence_wave_mediterranean_decisions.txt:102 independence_wave_cor_mountain_communes
- common/decisions/006_independence_wave_mediterranean_decisions.txt:227 independence_wave_arx_form_island_constitution
- common/decisions/006_independence_wave_mediterranean_decisions.txt:241 independence_wave_arx_ratify_labor_compact
- common/decisions/006_independence_wave_mediterranean_decisions.txt:382 independence_wave_asx_form_palermo_constitution
- common/decisions/006_independence_wave_mediterranean_decisions.txt:396 independence_wave_asx_ratify_labor_compact
- common/decisions/006_independence_wave_pacific_decisions.txt:477 independence_wave_fij_register_communal_veto
- common/decisions/006_independence_wave_western_decisions.txt:211 independence_wave_bri_ratify_federalist_compact
- common/decisions/006_independence_wave_western_decisions.txt:226 independence_wave_bri_charter_dock_rail_fisheries_councils
- common/decisions/006_independence_wave_western_decisions.txt:241 independence_wave_bri_entrust_regionalist_union
- common/decisions/006_independence_wave_western_decisions.txt:477 independence_wave_cat_ratify_constitutional_charter
- common/decisions/006_independence_wave_western_decisions.txt:493 independence_wave_cat_convene_workers_board

AXX is a representative mismatch at common/decisions/006_independence_wave_balkan_decisions.txt:131-141: the available and custom-cost trigger uses the administration-light helper and the generic factory-bearing cost string, while complete_effect calls only independence_wave_decision_pay_administration_light and no modifier is present. FORM-03 has the same shape at common/decisions/006_independence_wave_form03_decisions.txt:282-300. DM-08 has the same shape at common/decisions/006_independence_wave_decisions.txt:379-397. FIJ has the same shape at common/decisions/006_independence_wave_pacific_decisions.txt:477-490.

This is a requirement/payment and tooltip mismatch, not proof of a free-resource loop. It can also leave factory capacity available for other projects while the player is told that a factory is part of this action. The constants are centralised at common/script_constants/006_independence_wave_constants_registry.txt:1052-1149, with light, standard, and major factory requirements of 1, 2, and 3.

Recommended owner fix: classify each affected decision as either a factory-consuming project or a non-consuming administration action. For the former, add the appropriate local civilian_factory_use modifier and preserve the factory-bearing dynamic localisation. For the latter, use an explicit non-consumed capacity requirement and a cost key that displays only spendable values. Do not add modifiers mechanically across all 30 blocks without checking their accepted package design and durations.

### High / P1 — DM-35 hides an always-paid base cost on its Later branch

independence_wave_balance_patrons at common/decisions/006_independence_wave_decisions.txt:1944-2003 always requires and pays diplomatic-standard command power plus either convoy or train at :1954-1969 and :1973-1978. When independence_wave_patron_balance_count is greater than the minimum, it also pays administration-light command power and manpower. The custom localisation at localisation/english/006_independence_wave_decisions_l_english.yml:46 and its blocked variant at :87 display First as diplomatic standard and Later as administration light, but the Later line does not repeat the always-paid diplomatic standard transport cost or the civilian-factory availability requirement inherited from can_pay_independence_wave_administration_light_cost.

This violates cost clarity even though the core palette stays within four distinct spendable resource types across both branches: command power, one transport type, manpower, and the non-consumed or reserved factory capacity question. The repeat cooldown is major at :1971-1972, and balance_count increments on completion and timeout at :1979 and :1989, so no infinite aid loop is proven from source.

Recommended owner fix: replace the First/Later shorthand with dynamic branch text that explicitly shows the full cost on every applicable path and separates spendable costs from capacity requirements. Keep the branch conditional on the current balance count and preserve the cooldown and patron influence consequences.

### Medium / P2 — Package foundation missions activate automatically but are absent from package-local active-project locks

The five package foundation missions are automatic missions because each has an activation block and available = always no. Vanilla decision guidance confirms that activation is checked automatically, while available does not gate automatic activation. The exact mission blocks are:

| Package and owner | Mission/category and region | Requirement and duration | Success and failure | Duplicate or phase risk |
| --- | --- | --- | --- | --- |
| AXX / Banat | independence_wave_axx_hold_banat_council_together in independence_wave_axx_banat_council_category; Banat/Danube | AXX identity, setup flag, unresolved and not failed; 420 days from common/decisions/006_independence_wave_balkan_decisions.txt:19-63 and common/script_constants/006_independence_wave_constants_registry.txt:172-179 | Stable ledgers plus capital control set the resolved flag; timeout or invalid cancellation sets failed and applies project failure at :40-60 | has_independence_wave_axx_active_package_project at common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt:84-98 checks a dead foundation flag branch but not has_active_mission |
| BOS / Bosnia | independence_wave_bos_hold_drina_council_together in independence_wave_bos_drina_council_category; Drina/Balkans | BOS identity, setup flag, unresolved and not failed; 420 days at common/decisions/006_independence_wave_balkan_decisions.txt:239-283 and common/script_constants/006_independence_wave_constants_registry.txt:323-330 | Stable ledgers plus capital control resolve; timeout or invalid cancellation fails at :252-279 | has_independence_wave_bos_active_package_project at common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt:280-295 has the same dead foundation flag branch and no active-mission test |
| BBX / Epirus | independence_wave_bbx_hold_epirus_council_together in independence_wave_bbx_epirus_council_category; Epirus/Ionian | BBX identity, setup flag, unresolved and not failed; 330 days at common/decisions/006_independence_wave_balkan_decisions.txt:490-538 and common/script_constants/006_independence_wave_constants_registry.txt:1352-1359 | Stable ledgers, government route, and capital control resolve; timeout or invalid cancellation fails at :503-534 | has_independence_wave_bbx_active_package_project at common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt:476-490 omits the foundation branch entirely |
| MAC / Macedonia | independence_wave_mac_hold_vardar_council_together in independence_wave_mac_vardar_council_category; Vardar/Danube | MAC identity, setup flag, unresolved and not failed; 420 days at common/decisions/006_independence_wave_balkan_decisions.txt:724-768 and common/script_constants/006_independence_wave_constants_registry.txt:6515-6522 | Stable ledgers plus capital control resolve; timeout or invalid cancellation fails at :737-764 | has_independence_wave_mac_active_package_project at common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt:669-684 contains an unused foundation flag branch and no active-mission test |
| BAX / Thrace | independence_wave_bax_hold_thrace_council_together in independence_wave_bax_thrace_council_category; Thrace/Aegean | BAX identity, setup flag, unresolved and not failed; 360 days at common/decisions/006_independence_wave_balkan_decisions.txt:954-997 and common/script_constants/006_independence_wave_constants_registry.txt:8934-8941 | Stable ledgers plus capital control resolve; timeout or invalid cancellation fails at :967-994 | has_independence_wave_bax_active_package_project at common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt:1075-1090 contains an unused foundation flag branch and no active-mission test |

The five foundation active flags have no setter in the current source. An rg scan finds them only in the four helper branches for AXX, BOS, MAC, and BAX; BBX has no branch. The automatic missions therefore are not represented by those flags. The package paid decisions use NOT = { has_independence_wave_*_active_package_project = yes }, so they can coexist with the active automatic mission. This is a local duplicate/phase risk, not a demand to join the intentional shared diplomatic/security operation caps.

Recommended owner fix: either include has_active_mission = <foundation mission id> in each package-local active-project helper, or deliberately add/set/clear a real foundation-active flag and document the accepted parallelism. Preserve the existing choice that package-local projects need not join the shared cross-package diplomatic/security locks.

### Medium / P2 — Static category density and status-ledger cognitive load need production evidence

An ephemeral structural parser over all Event 006 decision files found 88 category roots, with 57 having more than six direct child decisions and 37 having more than ten. This is not a simultaneous-visible count because many children are hidden or activated only by route, phase, package, target, or project locks, but it is a source-level risk against the specification ceiling at docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md:851-865.

The core category counts are founding 5, government 6, recognition 6, security 7, host relations 7, patron 8, network 7, league 6, borders 5, formables 4, high chaos 3, and scenario ledger 3. The security children are visible in source at common/decisions/006_independence_wave_decisions.txt:1014, :1055, :1103, :1131, :1171, :1228, and :1281. The patron category is similarly eight children, and the IW-095 first-footprint category has ten.

The specification requires only the current founding phase to be expanded and no more than six visible primary actions at a time at :851-865. The source has phase and route activation predicates, but no production decision-list render was available to prove the visible result. Do not collapse or delete categories solely from these structural counts.

The status GUI is attached to the active founding category at common/decisions/categories/006_independence_wave_categories.txt:51-56. Its scripted-GUI contract is active-origin gated at common/scripted_guis/006_independence_wave_scripted_gui.txt:9-15, provides five mutually exclusive tabs at :27-61 and :73-97, and has four static/animated cue pairs at :89-104. The 700x500 layout places five numeric values, former-host, patron, network, phase, active-mission text, and five tab buttons in interface/006_independence_wave.gui:8-68.

The numeric values are banded in localisation/english/006_independence_wave_gui_l_english.yml:8-13, which gives a useful high-level state. Host claim, hostility, obligations, patron influence, and network standing are raw values or names at :14-20 without concise threshold/consequence text. The active-mission summary is generic at :37-38 and resolves to “Founding work is in progress,” “Security work is in progress,” or similar at :98-102; it does not identify the exact mission, remaining duration, failure consequence, or available response.

Recommended owner fix: obtain the required hoi4.gui_inspect and hoi4.gui_render evidence for every tab and resolution, then reduce simultaneous visible action rows or add phase grouping only where the render proves a breach. Add concise dynamic tooltips for host, patron, network, and mission values that state the current threshold, consequence, and player response. Do not route this shared state ledger to chaosx_event_ui_worker as a new event-owned GUI; it is an existing shared Event 006 category surface.

### Medium / P2 — Weighted AI and route behavior remain unclosed without the required probability pass

The source has explicit AI weights on the core decision and mission families. DM-01 uses urgent AI at common/decisions/006_independence_wave_decisions.txt:23-81, DM-02 uses high AI at :84-129, DM-03 uses standard AI with a war modifier at :131-197, DM-04 and DM-05 use route-aware standard AI at :199-311, and DM-35 uses high AI with a patron-client modifier at :1944-2003. Shared active-operation helper caps are centralised at common/script_constants/006_independence_wave_constants_registry.txt:1290-1297 and enumerated in common/scripted_triggers/006_independence_wave_decision_triggers.txt:41-98.

Target guards include exists, self/member exclusion, war-state checks, and declaration legality in common/scripted_triggers/006_independence_wave_decision_triggers.txt:101-110. Package predicates inspected for AXX, BOS, MAC, BAX, IW-043/IW-058, IW-093/IW-098, and the overlay families resolve to active-origin or the shared runtime-unlocked gate. For example, IW-043 and IW-058 require is_independence_wave_active_country at common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:19-55, and IW-093/IW-098 require an active origin and package id at common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:136-188. No dead-country target or impossible border target was proven by the source scan.

The current worktree also contains uncommitted package-trigger changes affecting war-support gates in the Komi, Kosovo, Kuban, Ruthenia, and Udmurt package trigger files. They are probability-bearing and remain provisional until the owner runs the same named scenario baseline and compare.

Required action: route all complex decision, mission, scenario-ranking, and package-weight surfaces through chaosx_ai_probability_auditor with hoi4.probability_inspect, scenario evaluation, and probability_compare. No quantitative AI or balance conclusion is made in this handoff because that route is unavailable.

### Low / P3 — Preparation comment and origin-registry call disagree and need owner reconciliation

The preparation effect says it writes only reversible country-local generation state and does not publish active, network, host, history, evolution, or released-package rows at common/scripted_effects/006_independence_wave_effects.txt:687-695. The same effect calls independence_wave_registry_record_event6_origin at :696-710, and that helper sets independence_wave_active_origin and liberation_origin at :54-60. The call order is protected by the committed-plan executor, so this is not alone proof of a pre-event leak, but the comment and implementation use “publish” differently. Reconcile the documentation and the intended publication boundary before using the comment as a gate proof.

## Decision-category lifecycle notes

The canonical active-origin gate is is_independence_wave_active_country at common/scripted_triggers/006_independence_wave_triggers.txt:9-14. It requires an existing country, independence_wave_active_origin, the Event 006 liberation_origin value, and no origin-ended flag.

The main categories are active or phase gated at common/decisions/categories/006_independence_wave_categories.txt:51-122. Founding, government, and security require an active origin; recognition and patron require provisional-or-later; network and league require recognized-or-later; borders and high chaos require regional-power plus their unlock flags. The founding category deliberately has visible_when_empty = yes and owns the Statehood Ledger scripted GUI.

Overlay categories use is_independence_wave_overlay_runtime_unlocked at common/decisions/categories/006_independence_wave_categories.txt:271-330. That trigger is only the global Event 006 runtime flag at common/scripted_triggers/006_independence_wave_minor_overlay_triggers_registry.txt:20-22, and each inspected overlay route adds its own active identity check. The overlay route trigger begins with the runtime gate and exists check at :35-40.

Root Event 006 sets independence_wave_event6_runtime_unlocked only after a committed joint plan or committed standalone incident at events/006_independence_wave.txt:18-45 and :47-65. The flag is intentionally persistent in the current design; overlay predicates still require their active route identities. The failed SCN-008 result path does not set this runtime flag, which is why using only the persistent flag as a new ledger gate would not distinguish a current successful public report from an old event. A current scenario-success receipt or a category-specific committed flag is safer.

The old pre-event crisis helpers are correctly inert. Their triggers are always no at common/scripted_triggers/006_independence_wave_compatibility_triggers.txt:379-400, and their effects are empty stubs at common/scripted_effects/006_independence_wave_compatibility_effects.txt:211-236. The retired hidden callback only clears old flags and variables at events/006_independence_wave.txt:107-128. The allocator validator also reports “pre-event crisis surface: retired; no category, mission, cost, or queue.”

## Cognitive-load notes

- Visible action count: structural direct-child counts exceed six in security, host relations, patron, and network categories, with additional high counts in package and formable categories. Individual activation and route locks may reduce the simultaneous list, but production decision-list evidence is missing.
- Active missions: shared helper caps are one founding, one diplomatic, one security, one league crisis, one border operation, and one formable operation at common/script_constants/006_independence_wave_constants_registry.txt:1290-1297. The five package foundation missions are outside those generic helpers and outside package-local locks, so the package-level active-mission count is not proven.
- Player-facing values: the five core values have numeric values and bands. Host, patron, and network values expose raw numbers or names without a short consequence/response explanation.
- Text density: the status GUI fits 5 values plus 5 relationship/phase/mission cards and 5 tabs into 700x500. The panel source has no render evidence for clipping, overlap, or text overflow. The scenario ledger description is intentionally long and includes a dynamic movement row plus failure reason; it is an explicit secondary inspection surface.
- Significance: the GUI mission status is generic, and the network and host rows do not state what threshold unlocks or blocks. The decision descriptions and custom tooltips need runtime review for blocked reasons and actual success/failure consequence.
- Phase presentation: source categories are phase gated, but the required “only current phase expanded” behavior is not demonstrated by a production decision render.

## Mission quality notes

DM-01 Secure the Provisional Capital is owned by every active released country and lives in the founding category. Its start gate requires active origin, package setup, capital control, garrison, equipment, transport, no prior result, and no active mission at common/scripted_triggers/006_independence_wave_decision_triggers.txt:369-384. The automatic mission is activated only after the material reservation at common/scripted_effects/006_independence_wave_decision_effects.txt:966-991. Its 75-day base is shortened to 30 or 45 days for fragile or viable force levels, matching the 30-to-75-day spec band; cancellation on capital, garrison, or origin loss applies relocation and bounded losses, while timeout sets secured and administration-ready flags at common/decisions/006_independence_wave_decisions.txt:23-80. No duplicate start path was found.

DM-02 Establish the Revenue Service is an active-origin founding mission after DM-01, with capital control, no severe instability, a 150-day founding duration, a civilian factory-use modifier, success effects, salary-crisis timeout, and origin-loss cancellation at common/decisions/006_independence_wave_decisions.txt:84-129. Its activation excludes any active shared founding mission, so the shared duplicate gate is explicit.

DM-03 Register the Population is a hidden automatic mission after DM-02. It requires administration affordability during activation, excludes active shared founding missions, has a 150-day founding duration, and pays administration at timeout only if resources remain. Capital loss or severe instability cancels it with registration failure at common/decisions/006_independence_wave_decisions.txt:131-197. The timeout partial-success branch is explicit and no duplicate shared start was found.

DM-04 Hold the First Assembly and DM-05 Confirm Traditional Authority are mutually exclusive route missions after the provisional phase. Both require the relevant unlock, no government-route lock, capital control, administration affordability, and no active shared founding mission at common/decisions/006_independence_wave_decisions.txt:199-311. Each runs for 180 days in the current constants, succeeds into its route, fails on timeout, and cancels when the origin or government route becomes invalid.

The AXX, BOS, BBX, MAC, and BAX package foundation missions are passive package-owned council objectives, not generic shared founding missions. Their exact owner, region, setup requirement, duration, success, timeout, and local lock status are recorded in the table under the P2 finding above. Their primary quality gap is the missing package-local has_active_mission lock, not missing timeout or failure effects.

DM-35 Balance the Patrons is owned by a recognized-or-later country with at least the minimum active patron count, lives in the patron category, and has a 240-day extended mission plus a major cooldown at common/decisions/006_independence_wave_decisions.txt:1944-2003. Completion reduces all patron influence and improves bounded country values; timeout increases balance count and applies losses; cancellation requires the origin to remain active. Its count and cooldown controls prevent a proven infinite repeat, but its branch cost text is incomplete.

SCN-008’s scenario ledger is not a timed mission. It is a zero-cost previous/next/close decision group at common/decisions/006_independence_wave_decisions.txt:936-1008, with cleanup through the close decision and independence_wave_scenario_reset_summary at common/scripted_effects/006_independence_wave_scenario_effects.txt:1104-1124. The lifecycle is otherwise clear; the failure publication gate is the P1 issue.

## Cost and requirement clarity

The shared spendable palettes are centralised and icon-first. Administration, diplomatic, security, border, coordinated-operation, and integration checks are at common/scripted_triggers/006_independence_wave_decision_triggers.txt:229-320, and payments are at common/scripted_effects/006_independence_wave_decision_effects.txt:125-292.

The largest normal palette uses no more than four distinct spendable types. Administration uses command power and manpower, with factory capacity as a reservation or requirement; diplomatic uses command power and either convoy or train; security uses manpower, army experience, infantry equipment, and support equipment; border and coordinated operations use dedicated four-group palettes. Every shared cost string inspected uses texticons such as £command_power, £manpower_texticon, £civ_factory, £convoy_texticon, £GFX_train_texticon, £infantry_equipment_text_icon, £support_equipment_text_icon, £army_experience, £stability_texticon, and £fuel_texticon at localisation/english/006_independence_wave_decisions_l_english.yml:33-61. No literal resource name was found in the shared cost strings.

The cost-count result does not excuse hidden branches. DM-35’s Later path omits its base diplomatic cost, and the 30 administration-gated blocks disclose a factory without reserving it. Split cost localisation from non-consumed requirement localisation rather than padding a single line with prose.

FORM-03’s technical mission cost is currently iconized, including the League Reserve icon, at localisation/english/006_independence_wave_form03_l_english.yml:206-208, with the sprite registered at interface/006_independence_wave_small_assets.gfx:315-316. No missing texticon was re-raised for that surface.

## AI validity and route-lock notes

Source route guards are generally conservative. The canonical active-origin helper prevents pre-event package categories. Package-specific identity predicates for AXX, BOS, MAC, BAX, IW-043, IW-058, IW-093, and IW-098 require active origin, package id, setup or identity flags, and in several cases former-host or anchor validity. The charter-war target guard additionally checks existence, non-self, non-member status, no existing war, and declaration legality at common/scripted_triggers/006_independence_wave_decision_triggers.txt:101-110.

The shared operation helpers enumerate active decisions and missions for the intended one-per-family caps at common/scripted_triggers/006_independence_wave_decision_triggers.txt:41-98. The package foundation mission omission is the local exception documented above.

No dead-country or impossible-border target was established by source-only inspection. This is not a balance or probability pass. The unavailable MCP probability route means no claim is made about score calibration, selection frequency, scenario ranking, or AI response to the current uncommitted war-support gate changes.

## Localisation and tooltip gaps

A static simple-key crosswalk over the Event 006 decision files found no missing English keys for parsed name, desc, custom effect, custom trigger, or custom cost references. This does not validate nested pdx_tooltip chains, dynamic localisation scopes, font fit, or blocked-state rendering.

Shared cost localisation is icon-first, but the factory-bearing administration strings are semantically wrong for the 30 non-reserving blocks. DM-35’s First/Later string is concise but omits costs on the Later branch. These are the primary cost-tooltip fixes.

The state-ledger GUI has understandable band names, but the host, patron, network, and mission strings do not communicate exact thresholds, consequence, remaining time, or next response. The generic active-mission keys are at localisation/english/006_independence_wave_gui_l_english.yml:98-102.

The SCN-008 failure result is itself a localisation and visibility problem under the strict gate because its title, description, report picture, Open the ledger option, and Unavailable Movements category are visible before the public report. If the owner preserves a blocked summary for an explicitly launched scenario, it must be reconciled with the superseding no-indication requirement.

## Cleanup and exploit-risk notes

Active-origin cleanup is broad and explicit at common/scripted_effects/006_independence_wave_effects.txt:2948-3000. It dispatches package cleanup, clears decision, focus, league, network, host, patron, route, origin, and idea state, and unregisters the active origin. Generation reset also clears package decisions, registries, active-origin markers, and route flags at common/scripted_effects/006_independence_wave_effects.txt:462-488.

Decision-layer cleanup is separately owned at common/scripted_effects/006_independence_wave_decision_effects.txt:1140-1178. The scenario reset clears ledger visibility, indices, arrays, and counts before rebuilding at common/scripted_effects/006_independence_wave_scenario_effects.txt:1104-1124. Vanilla remove-decision/remove-mission semantics skip already completed or timed-out entries, so the explicit flag and variable cleanup is important and present.

No free unit, equipment, core, or war-goal loop was proven from the current source. DM-01 reserves material once before activating the mission and its start gate rejects an already-reserved or active mission. DM-35 increments its balance count and has a major cooldown. FORM-03 League Reserve is iconized and no repeatable free-reserve path was found.

The concrete lifecycle risks are the pre-public-report SCN-008 failure ledger, the factory requirement/payment mismatch, and package foundation missions running outside package-local project locks. These should be fixed or explicitly dispositioned before a completion claim.

## Validation run

The following task-specific local validators completed successfully on the current worktree:

- python .tools/audit_event6_allocator.py: Event 006 allocator audit passed; 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 runtime adapters, 32 attested packages, 29 compatible reservation groups, and the retired pre-event crisis surface reported with no category, mission, cost, or queue.
- python .tools/audit_event6_gui_matrix.py: semantic source matrix passed with five mutually exclusive tabs, five recognition frames, three dependency frames, four league frames, four formable frames, and four static/animated cue pairs. The validator explicitly did not claim runtime rendering or save/load evidence.
- python .tools/audit_event6_scenario_matrix.py: all 32 SCN-008 cells and eight edge cases passed.
- python .tools/audit_event6_country_api.py: 242 unique tags, 191 resolved carriers, no missing carriers, and no duplicates.
- python .tools/audit_event6_form16.py: ARM/GEO/AZR state, consent/refusal, rollback, cleanup, and readiness matrix passed.
- python .tools/audit_event6_flags.py: 102 registered flags, 102 complete, zero incomplete.
- An ephemeral static parser found the 88 category roots, 57 over-six category roots, 37 over-ten category roots, and the 30 administration-gated decision blocks without a civilian_factory_use modifier listed above.
- An ephemeral simple localisation crosswalk found no missing parsed decision name, desc, custom effect, custom trigger, or custom cost keys.

## Recommended owner work, ordered

1. Close the strict pre-event gate by suppressing the Event 006-branded SCN-008 failure report and ledger until a current successful public Event 006 report receipt exists. Re-run a source scan for every setter and consumer of independence_wave_scenario_ledger_visible after the owner patch.
2. Reconcile all 30 administration-gated blocks individually, deciding whether the factory is consumed/reserved or is a non-consumed capacity requirement. Update the decision modifier and custom cost key together.
3. Rewrite DM-35 branch cost localisation so every branch displays the full applicable diplomatic and administration costs and separates spendable values from capacity requirements.
4. Decide whether the five package-local foundation missions serialize with their own paid projects. If yes, add their active-mission IDs to the five local helpers. If no, document the accepted parallelism and remove the unused foundation-active flag branches or implement their full set/clear lifecycle.
5. Obtain the mandatory GUI inspect/render pass and probability inspect/evaluate/compare pass before claiming completion. Review the production decision list for the six-action and three-active-mission ceilings and verify every tooltip at representative blocked, active, success, timeout, and cleanup states.

## Changes, omissions, and blockers

Changed files: only this dated handoff.

Changed decision, mission, GUI, AI, or localisation identifiers: none.

Before/after behavior: no gameplay behavior changed.

Skipped meaningful validation: HOI4 MCP GUI inspection/render and probability audit/compare were unavailable in the current runtime; HOI4 was not launched per instruction. The local GUI matrix therefore remains semantic source evidence only.

No simplification was made to the audited source. The audit is incomplete for production visual and probability evidence until the MCP routes are restored, and the source findings above remain open for the owner.

No plan handoff was written because the findings are narrow owner fixes and this task was restricted to a dated audit handoff.
