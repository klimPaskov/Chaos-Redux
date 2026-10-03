# IW-044 Tatarstan bounded country-package audit (2026-10-03)

Status: source-level audit delivered; engine and quantitative coverage remains blocked. Scope is Event 006 IW-044, TAT, and state 249 Kazan only. State 245 Millerovo/IW-039 is excluded. No gameplay, localization, assets, Git index, or other agent files were changed. This report does not claim whole Event 006 completion.

## Coverage checklist

- **Package identity and capital:** the package identifies TAT by original tag and IW-044 package id. Preparation/runtime checks require state 249 to be TAT-owned and controlled and Kazan to be the capital. Vanilla state history gives Kazan to SOV, adds a TAT core, and starts it with one military factory, zero civilian factories, 25 steel, and a 10-VP province.
- **Government and politics:** package setup establishes TAT’s democratic provisional authority, party support values, four route parties, and baseline laws. All four custom party name/long-name pairs are localized. The TAT roster trigger checks character id `TAT_alexandr_alemasov`; portrait provenance, advisor wiring, flag art, and full leader metadata were outside this bounded source review.
- **Focus tree:** the five IW-044 nodes are imported into the existing `independence_wave_focus_tree`; they do not create a second tree. Their package, active-origin, setup, Kazan-control/capital, and failure guards remain in place. Each focus title and description is present in the TAT localization file.
- **Decisions and mission:** the founding mission, four government choices, ordinary project gate, failure effects, cancellation handling, and ten TAT timed/project decisions were source-reviewed. Costs and durations remain those in the current source.
- **Pressure and playability:** source arithmetic confirms all four routes can cross the two-ledger stability threshold within the accepted 720-day design when the required shared focuses are completed. The detailed source witness and its assumptions are below.
- **Industry and assets:** the Kazan grant is deficit-only, state-scoped, and reuses the existing `independence_wave_tat_depots_secured` idempotence flag. All five focus sprites resolve through the registered .gfx file to present 94x86 DDS textures.
- **AI:** all TAT decision willingness inputs and four TAT strategy plans were inventoried. Weighted logic was routed through `chaosx_ai_probability_auditor`, which completed source inspection but returned no analyzer-backed result because the HOI4 MCP probability requests timed out.
- **Map, supply, army, equipment, technology, advisors, and live country history:** the bounded map tool calls failed before returning a state render or inspection artifact. Only the vanilla state-history facts above were verified. Starting army, templates, stockpiles, supply, rail, technology, and portrait/advisor packages remain unaudited.
- **GUI/technology surfaces:** no TAT GUI or technology dependency was identified in the supplied IW-044 surface, so neither GUI nor technology-tree routes were in scope.

## Accepted-design fidelity and route evidence

The four government decisions use `is_independence_wave_tat_government_choice_open`, which requires the package setup and active founding mission, and excludes resolved, failed, or already-governed TAT. Each also checks its matching route, capital control, affordability, and the separate `is_independence_wave_tat_government_project_clear` gate. That gate uses `has_decision` for all four choices; installed trigger documentation defines this as an active selected decision, so the four projects serialize while the mission remains open.

Ordinary projects use `is_independence_wave_tat_project_ready`, which requires the founding mission to be resolved and the package not failed. This preserves the intended separation between government selection during the mission and ordinary projects after resolution. The founding mission resolves only when both compact values are stable, a government is installed, state 249 remains owned and controlled, and the current capital is controlled; timeout or invalidation marks the crisis failed and applies the guarded failure effect. `independence_wave_tat_project_failure_applied` prevents duplicate pressure penalties while an active project and the mission cancel together. Package cleanup removes the TAT mission/projects and resets the package lifecycle.

The source also has a conditional capital-integrity mismatch. The TAT focus-group gate requires `249 = { is_owned_and_controlled_by = ROOT is_capital = yes }`, but the founding mission’s cancellation/success checks require state 249 to remain owned and controlled and the current capital to remain controlled; they do not require Kazan to remain the capital. If an outside effect moves TAT’s capital while Kazan remains controlled and the ledgers are not yet stable, the focus group becomes unavailable while the founding mission can remain active. No in-scope TAT effect moves the capital, so this is a conditional route-stranding risk rather than a demonstrated normal-play failure.

The accepted spec says the paid project decisions remain alternate routes. The current gate makes `independence_wave_tat_secure_river_depots` unreachable as an alternate during normal founding. A scoped search across `common/` and `events/` found no external TAT-ledger writers: package setup initializes 38/44, government-route and focus hooks add positive deltas, and failure handling only subtracts. Starting pressure is 38/44 and stability requires 60/60. Government choice alone after the assembly gives 68/54 (constitutional), 68/59 (agrarian), 58/64 (socialist), or 48/69 (emergency), so every valid founding route needs the assembly plus at least one sibling focus before the mission can resolve; emergency specifically needs River Communities. The assembly focus is a prerequisite for both siblings and its completion hook sets `independence_wave_tat_depots_secured`. The depot decision itself requires mission resolution and is hidden once that flag is set. Thus its matching paid decision cannot substitute for the focus that supplies the factories and assembly pressure; this conflicts with the spec’s alternate-route claim at [the accepted IW-044 spec](../../../specs/006_independence_wave_specs/specs/006_iw044_tatarstan_foundation_and_focus_group.md#L46).

The source pressure witness after the three common focuses is Civic Concord 73 and River Security 74. Adding each government’s route delta gives:

| Government route | Final Civic Concord / River Security | Deadline duration |
| --- | ---: | ---: |
| Constitutional | 88 / 79 | 75 days |
| Agrarian | 88 / 84 | 180 days |
| Socialist | 78 / 89 | 75 days |
| Emergency | 68 / 94 | 120 days |

All four values exceed the stable threshold of 60 and remain below the 100 cap. The current parent timing handoff records nominal earliest joint completion at 525, 600, 490, and 505 days respectively, against the accepted 720-day mission deadline. It also records a constitutional reservation-delay witness that completes by day 626, leaving 94 days. These are source/timing calculations under its stated focus-speed, resource, control, and reservation assumptions; they are not campaign or AI test results.

## Factory affordability and one-time grant

The assembly hook subtracts Kazan’s current civilian-complex level from the configured target of four and, only for a positive deficit, adds matching shared slots and instant-built civilian industry inside state 249. The entire hook is guarded by `NOT = { has_country_flag = independence_wave_tat_depots_secured }`; it sets that flag after the grant and other assembly rewards. The shared-focus root also bypasses on that flag, preserving one reward through the focus/decision pair. Header and values are in [the TAT package effects](../../../../common/scripted_effects/006_independence_wave_tatarstan_package_effects.txt#L266) and [the TAT constants](../../../../common/script_constants/006_independence_wave_constants_registry.txt#L8830).

The vanilla starting anchor has no civilian factories. The installed civilian-economy law uses 0.35 expected consumer goods. The administration-light affordability trigger requires more than zero civilian factories available for projects, at least 10 command power, and at least 2,500 manpower; the project reserves one civilian factory. The four-factory target creates a source-level affordability path while preserving any existing industry, but actual available factories remain dependent on live consumer-goods rounding, country modifiers, and other reservations. Current balance assumptions are recorded in [the parent source/timing handoff](../../../plans/006_independence_wave_plans/subagent_handoffs/006_iw044_tat_parent_review_2026-10-03.md#L22).

## Focus loading, localization, and assets

The full shared focus tree is assigned before TAT setup completion. Origin activation then registers the active-country and network entries, checks their alignment, sets `independence_wave_origin_activation_ready`, and invokes `mark_focus_tree_layout_dirty` only for IW-039 or IW-044 after the package-specific setup flag is present. The new TAT condition is additive beside the DON/IW-039 condition. It does not reload the tree or reset completed focus history. The offline focus reference says `allow_branch` is evaluated when the tree loads and can be refreshed by this effect; installed effects documentation confirms country scope. See [the activation effect](../../../../common/scripted_effects/006_independence_wave_effects.txt#L877), [the five imported nodes](../../../../common/national_focus/006_independence_wave_focus.txt#L5216), and [the package focus gate](../../../../common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt#L239).

The five focus sprite ids are `GFX_goal_independence_wave_founding_administration`, `GFX_goal_independence_wave_popular_councils`, `GFX_goal_independence_wave_army_integration`, `GFX_goal_independence_wave_former_host_settlement`, and `GFX_goal_independence_wave_league_congress`. Their registrations in `interface/006_independence_wave.gfx` point to five existing files under `gfx/interface/goals/006_independence_wave/`; format-aware header reads confirm each is a 94x86 DDS. All four route party name pairs and the founding mission/focus descriptions are present in `localisation/english/006_independence_wave_tatarstan_l_english.yml`. No art was created or substituted.

The accepted spec records an earlier renderer limitation: imported root-level `shared_focus` nodes were omitted from the rendered layout. The fresh focus inspect and cropped render in this audit also timed out, so current in-tool layout/visibility evidence remains absent.

## AI and weighted-logic findings

The current TAT `ai_will_do` values are decision/mission willingness scores, not click probabilities:

| TAT candidate | Source score | Declared modifier or gate |
| --- | ---: | --- |
| Founding mission | urgent 100 | Active after setup until resolved or failed; 720-day timeout |
| Secure River Depots | high 25 | Ordinary-project gate; not normally available after the required assembly flag |
| Integrate Border Guards | high 25 | Doubled while at war |
| Register Community Compacts | high 25 | Ordinary-project gate |
| Settle Former-Host Ledgers | standard 10 | Doubled when severe host threat is absent |
| Constitutional government | high 25 | Constitutional route; 75 days |
| Agrarian government | standard 10 | Traditional route; 180 days |
| Socialist government | high 25 | Popular-council route; 75 days |
| Emergency government | urgent 100 | Doubled while at war; 120 days |
| Codify Durable Sovereignty | high 25 | Resolved founding, installed government, stable compact, strategic-cost gate |
| Open Volga Corridor | standard 10 | Resolved founding, stable compact, network membership, League route |

The live AI strategy plans use file-local `@CR_SC_IW_TAT_*` values in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`: River Survival has army 82, infantry production 44, artillery 26, support 58, infrastructure 62, and bunker 76; Host Restraint has avoid-starting-wars -250; Settled Compact has army 82, avoid-starting-wars -420, and infrastructure 62; Emergency Guard has army 112 and bunker 76. The mirrored `independence_wave_tatarstan_ai` table in the script-constants registry has no consumer anywhere under `common/`, so it is not the effective source of those factors.

The strategy plans overlap: River Survival can coexist with Host Restraint and Settled Compact; Emergency Guard can overlap River Survival and Settled Compact. Settled Compact is enabled by ledger stabilization alone, even before founding resolution or government installation. The plan `enable` blocks do not directly gate failure or Kazan control. Whether the package predicate/lifecycle removes these factors after failure or anchor loss remains unresolved. The at-war fallback for `independence_wave_tat_settle_former_host_ledgers` is also present in both availability and cancellation; MCP did not establish cancellation timing, cost outcome, or AI selection effect.

The probability audit was routed to `chaosx_ai_probability_auditor`. It supplied named source scenarios including `tat_guard_integration_war_toggle`, `iw044_tat_strategy_activation_matrix`, `iw044_tat_strategy_gate_sensitivity`, and `iw044_tat_focus_activation_timing`, but none returned an analyzer result or scenario hash. Probability inspect/evaluate/sweep calls timed out after 600 seconds. Probability compare rejected the call because no before/after source or manifests were supplied; there is no pre-change byte snapshot to verify a preservation delta. No rankings, modifiers, click probabilities, scenario hashes, or rendered probability artifacts are claimed. The five TAT focus nodes have no explicit `ai_will_do`; the recorded default score is one, but the full TAT candidate pool and external focus factors remain unaudited.

## HOI4 MCP evidence and blockers

All tool schemas were exposed under workspace `mod_chaos_redux_ea3b2d67c2c0`. Focus and map `reference_context` calls returned source bundles, but event, decision, and AI contexts timed out after 600 seconds. The targeted `reference_search`, two `reference_read` calls, and `source_lookup` also timed out after 600 seconds; exact local wiki and installed documentation sections were read directly and hashed.

Valid scoped domain calls produced no artifacts:

| Surface | Call | Result |
| --- | --- | --- |
| Event 006 root `chaosx.nr6.1` | `event_inspect` downstream trace; `event_render` neighborhood | Both timed out after 600 seconds |
| Shared focus tree | `focus_inspect` for `independence_wave_focus_tree`; cropped `focus_render` for the six-node TAT opening chain | Both timed out after 600 seconds |
| State 249 | `map_inspect` lookup for state 249; `map_render` cropped to state 249 with owner/building/supply/rail/port/resource/VP/adjacency overlays | Both timed out after 600 seconds |
| Founding mission | `decision_inspect` with a declared TAT opening-pressure scenario | Timed out after 600 seconds |
| Weighted surfaces | Probability inspect/evaluate/sweep through the auditor | Timed out after 600 seconds; no analysis id |

A prior rejected decision-inspect call lacked the required scenario; the corrected call included one and still timed out. No focus, event, decision, map, or probability visual/analysis artifact is available. Source review is not being presented as equivalent MCP evidence. There is no GUI or technology dependency in this bounded package; the standalone Technology Tree Viewer was not checked because no technology surface was in scope.

## Documentation and exact-source evidence

Accepted-design basis and prior source timing are recorded in `docs/specs/006_independence_wave_specs/specs/006_iw044_tatarstan_foundation_and_focus_group.md` and `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw044_tat_parent_review_2026-10-03.md`. Current references read locally:

- Offline National Focus modding, lines 297–301 and 419–420, SHA-256 `BD989A13237C464F140A0AA671CC42C30A48E84A27DAE791B8914654FB9C6203`.
- Offline Decision modding, lines 270–276, 339–343, 353–355, and 465–475, SHA-256 `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`.
- Offline Effects, lines 3613–3615 and 1803, SHA-256 `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C`.
- Installed effects documentation, lines 839–847, 1267–1275, and 4811–4820, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- Installed triggers documentation, lines 3022–3028 and 3693–3700, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
- Installed decision documentation, lines 1–46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeeea4a030deb1884f9726de019`.
- Offline AI modding, lines 28–31, 76–80, and 106–112, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`, documents score-race selection, positive/negative strategy values, and continuously checked enable triggers.
- Offline National focus modding, lines 604–626, revision `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203`, documents the default focus score of one and focus-pool score race.
- Installed `common/ai_strategy/_documentation.md` lists the available strategy tokens; SHA-256 `70f5d755ae7ed4060e49cc64a393d1a0dc5611b3acc8abc6dfb4538781c915a1`.
- Vanilla `history/states/249-Kazan.txt`, lines 2–23, SHA-256 `5016B4558416ED4F5D7CD54925DBBFB672B8E0BA1C4044D1C07BA537574F852F`.
- Vanilla `common/decisions/YUG.txt`, lines 760–805, SHA-256 `856D7E22C378A11D6FEC8B584F84543B45169F9BFC7E3C32A176CF622E7C7451`, for activated timed-mission structure.
- Vanilla `common/national_focus/baltic_shared.txt`, lines 379–385, SHA-256 `A95FC995B2CC6B84CB7BDEFA2E7934F745917ECF5AAE5753824DCDEBCC0AB5A0`, for state-scoped slots and instant civilian construction.
- Vanilla `common/ideas/_economic.txt`, lines 101–116, for the civilian-economy 0.35 consumer-goods value.

Current audited source fingerprints are SHA-256 values, not MCP revisions:

| File | SHA-256 |
| --- | --- |
| `common/scripted_effects/006_independence_wave_tatarstan_package_effects.txt` | `AA1DFD22308AEBEDF80DBA4058B8DAF29618D3EA161EC583BCD9A63F1C032861` |
| `common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt` | `A6EBB9A04F1FA7595F838DC50E20186D9DA3BDF751896B6C6DADE0EAD908583C` |
| `common/script_constants/006_independence_wave_constants_registry.txt` | `215FE277FA18E912C90A2BD59706568410227E5CFD6EA0A7DA65A03591F328F4` |
| `common/decisions/006_independence_wave_siberian_decisions.txt` | `BD3E36C9023158478A3654F11E106E484EE8A270188A4CF0D39F95B716D82326` |
| `common/national_focus/006_independence_wave_focus.txt` | `53C085B9F18D919FCCE4D9B26AFEEACE7410321A385F74F853257AB35BA1D031` |
| `common/scripted_effects/006_independence_wave_effects.txt` | `96B29CC156902F17DB7850B29E70A85CC45F5F36D2F0E86A0A02F26F21388192` |
| `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` | `60FCBCCAD8DF110F1E050DC35D33D8EB2C397721567CF6AC4580DF345F444E0F` |
| `localisation/english/006_independence_wave_tatarstan_l_english.yml` | `BC3F77466DF91679D4FB35AE56297C4B7927D9B5BBEC1E014D451B61C39032F3` |
| `interface/006_independence_wave.gfx` | `C5B730FFEC384FB706ED5F7E47E746B91E4C07A2230BC586D34F36966AEF99D8` |
| `docs/specs/006_independence_wave_specs/specs/006_iw044_tatarstan_foundation_and_focus_group.md` | `032178C6F03B0121D9D56A5FD5975ACA0A150FC3643FFD3A54A256A80B1ADFFC` |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw044_tat_parent_review_2026-10-03.md` | `62BB97371D92F3FF65061D01C4DD2E2C054782F1BBEA932ECE135ABB369F49B9` |

## Completion limits and handoff

No source, localization, asset, or Git-index changes were made. No in-game validation, save inspection, or log review was attempted. No test suite was run for this read-only task.

The actionable audit is complete at source level, but this is **not an engine-validated country-package completion**. Required event/focus/map renders and probability analysis have no artifacts because the HOI4 MCP service timed out; no source-only substitutions are treated as satisfying those gates. Remaining design review items are the unreachable paid depot alternate, the conditional Kazan/capital drift gate, AI strategy overlap/lifecycle, the host-war fallback cancellation outcome, and the exact pre-change weighted-source baseline if the parent needs a comparison.

Only this new audit handoff is to be created by this subagent. No plan for an identity redesign, new focus route, or map write was needed.

Skills used: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`; the probability subagent also applied `chaos-redux-mtth`.
