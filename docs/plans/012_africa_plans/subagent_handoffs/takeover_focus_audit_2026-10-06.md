# Event 012 Gods of Africa Focus Takeover Audit

Disposition: read-only audit and after-change evidence update for the 25-focus Gods of Africa overlay inside the Event 012 tree. This subagent made no gameplay, localisation, GFX, decision, or asset edits; the parent applied the three coordinate changes described below. This handoff is the only file created by this subagent.

## Basis and coverage

The route source is docs/specs/012_africa_is_one_gods_of_africa_specs/specs/012_gods_of_africa_focus_integration.md. Its architecture, reveal rules, branch payoffs, Evolution II/III expansion, settlement capstone, and route table are at L29-L81, L83-L224, L229-L445, and L475-L680.

The requested accepted decisions are in docs/plans/012_africa_plans/agent_decisions_2026-10-04.md: L22 at file L272 accepts the Evolution II/III gates and visible focus-reward tooltips; L27 at L359 accepts the real focus payoffs and the No Sanctuary for Occupiers node; L30 at L405 accepts the 35/70/126-day durations and filter choices; L35 at L488 accepts the native-tree host offer and replacement route. Their dispositions are implemented, with live-game behavior retained as user validation. The all-three settlement convergence is accepted within the current takeover scope and follows the architecture map at focus-integration L64-L78.

| Required route | Implemented focus path | Result |
| --- | --- | --- |
| Institutional preparation | Prepare Proclamation -> Office of the Voices -> Continental Proclamation (tree L7326-L7422). Prepare also requires africa_identify_host_problem complete. | Present. The overlay requires the current host, Evolution I, active Gods, and committed activation. |
| Reciprocal doctrine | gods_of_africa_focus_reciprocal_covenant at L7423. | Present; 35 days; mutually exclusive with Exaction. |
| Extractive doctrine | gods_of_africa_focus_sovereign_exaction at L7462. | Present; 35 days; mutually exclusive with Reciprocal. |
| Provision | Measure the Needs -> Continental Arsenals -> Rails, Ports, and Fuel; Continental Reserve branches from Arsenals (L7504-L7640). The last two require Evolution II. | Present. Measure has one prerequisite group containing both doctrines, which is the correct OR form. |
| Oaths | Recognize the Continental Voice -> Return of African Soil -> End Foreign Sponsorship -> Continental Security Oaths (L7640-L7772). Security Oaths requires Evolution III. | Present. |
| Protection | Shelter the Faithful -> Relief Beyond the Continent -> African Expedition -> A Place at the Final Council (L7772-L7900). | Present. |
| Judgment | Record Every Refusal -> Reach Beyond the Coast -> Let the World Answer -> Hand of Judgment (L7900-L8029), then Sanctuary for Reliable Partners and No Sanctuary for Occupiers (L8029-L8108), then The Last Sentence (L8109-L8151). Hand of Judgment requires Evolution II; later nodes require Evolution III. | Present. The Last Sentence additionally requires the Strength and Chaos gates. |
| Continental settlement | Africa Speaks for Itself at L8152 requires Evolution III and africa_continental_settlement_complete, and calls gods_of_africa_commit_final_settlement. Three separate prerequisite blocks require Final Council, Security Oaths, and Hand of Judgment together. | Present and accepted as an all-three convergence by the architecture map at focus-integration L64-L78. The three 126-day branch capstones and the 126-day settlement capstone define the implemented late-game pacing. |

Prerequisite semantics are verified. The offline wiki National focus modding section “Interaction with other focuses” says multiple focus entries inside one prerequisite group mean OR, while separate prerequisite blocks mean AND: paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md L275-L296, revision bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203. Its “Cost” section at L299-L302, same revision, says one cost unit is seven days by default. A vanilla convergence precedent is game:common/national_focus/afghanistan.txt, AFG_forge_a_national_identity L8929-L8958: its L8932 group accepts AFG_expand_the_kings_powerbase or AFG_biding_our_time, which mutually exclude each other at L8862 and L8904. source_lookup confirmed the vanilla and mod locations at source revision 06b082b3849047eb2326c2aa4c27518ae9178c214f1dae5d062d78f30b663747.

All 25 focus blocks have allow_branch, available, search_filters, and ai_will_do. Shared visibility requires current-host scope, africa_evolution_i_logged, gods_of_africa_active, and gods_of_africa_activation_committed. Evolution II/III nodes add their matching global evolution gate. The first focus has an additional completed-focus requirement.

## Layout findings

Before the coordinate change, the actual raster showed No Sanctuary and Africa Speaks for Itself could be visible together: both allow_branch blocks require the same Evolution III/current-host/Gods state. Africa Speaks becomes available only when Event 012 settlement is complete, but its box is already visible. The before-change FOCUS_LAYOUT_CONNECTOR_THROUGH_NODE diagnostic for Hand of Judgment -> Africa Speaks intersecting No Sanctuary was therefore a real overlay conflict.

The before-change full SVG exposed the route as M 15288 3172 C 15288 3308, 13528 3308, 13528 3444. The No Sanctuary node then occupied transform translate(15216 3212), so the path crossed its focus box. The before-change raster crop and this edge geometry support the defect.

The parent reports that its focus_rewrite call returned Transport closed with the source SHA unchanged, then applied the coordinate-only adjustment. Local source review and git diff confirm these exact focus coordinates:

| Focus | Before | After |
| --- | --- | --- |
| gods_of_africa_focus_no_sanctuary | (88,27) | (92,27) |
| gods_of_africa_focus_last_sentence | (88,28) | (92,28) |
| gods_of_africa_focus_no_sanctuary_for_occupiers | (90,27) | (90,28) |

The local SHA-256 changed from the previously inspected source hash 3793ca1b124090b3d11e7915bd4bbde5639fa00bc9c5f9fd943e2a4708b480c6 to BBBC87F353CD1221B2EAE0C2FC988A7743CB3F6E42FC46D9DCD98A642C01F0D6. In the focus source diff, only those three x/y values changed. IDs, prerequisites, rewards, costs, filters, branch gates, and weights stayed unchanged, and no non-Gods focus moved.

Anticipated layout result, not MCP-verified: the Hand -> Africa Speaks path now ends at x=78 and stays left of No Sanctuary at x=92, so FOCUS_LAYOUT_CONNECTOR_THROUGH_NODE should clear. The new Hand -> Sanctuary link spans 4 columns and 1 row, Hand -> Occupiers spans 2 columns and 2 rows, and Sanctuary -> Last Sentence is vertical. Occupiers and Last Sentence are two columns apart on row 28, meeting the inspector's minimum same-row spacing. The existing Hand -> Africa Speaks long-link warning (10 columns, 3 rows) and Security Oaths -> Africa Speaks warning (8 columns, 3 rows) are expected to remain. A fresh raster is still required to confirm there are no new route intersections.

The before-change full JSON contained six Gods-specific diagnostics:

- Hand of Judgment -> Africa Speaks for Itself passes through No Sanctuary.
- Sovereign Exaction -> Measure the Needs spans 12 columns and 2 rows. These are mutually exclusive choices; this is an alternative convergence, not a state where both can be completed.
- Measure the Needs -> Shelter the Faithful spans 16 columns and 1 row.
- Measure the Needs -> Record Every Refusal spans 26 columns and 1 row.
- Hand of Judgment -> Africa Speaks for Itself spans 10 columns and 3 rows.
- Security Oaths -> Africa Speaks for Itself spans 8 columns and 3 rows.

Only the first is targeted by the coordinate move. The other long connectors remain visible convergence paths. The tree-wide before report had 301 focuses and 297 diagnostics; only six diagnostics pointed to Gods IDs. Whole-tree metrics were 102 columns, 45 rows, 62 crossings, 32 long connectors, and 53 node intersections. Those totals are context, not Gods-only findings. The before MCP JSON returned no repeated-generic-reward diagnostic for the 25 Gods nodes.
## Icons, localisation, and payoffs

All eight distinct Gods sprite IDs are registered in interface/012_africa.gfx L76-L83. The raster resolver scanned all eight referenced DDS files under gfx/interface/goals/012_africa/gods_of_africa/. No missing or dangling in-scope icon was found; repeated icons are grouped by route family.

| Sprite family | Focuses |
| --- | --- |
| Proclamation institution | Prepare Proclamation; Office of the Voices; Continental Proclamation |
| Reciprocal doctrine | Reciprocal Covenant |
| Extractive doctrine | Sovereign Exaction |
| Provision logistics | Measure the Needs; Continental Arsenals; Rails/Ports/Fuel; Continental Reserve |
| Oaths diplomacy | Recognize the Continental Voice; Return of African Soil; End Foreign Sponsorship; Continental Security Oaths |
| Protection | Shelter the Faithful; Relief Beyond the Continent; African Expedition; Sanctuary for Reliable Partners |
| Judgment | Record Every Refusal; Reach Beyond the Coast; Let the World Answer; Hand of Judgment; No Sanctuary for Occupiers; The Last Sentence |
| Continental settlement | A Place at the Final Council; Africa Speaks for Itself |

All 25 title and description keys resolve in localisation/english/012_africa_gods_l_english.yml; the overlay navigation label is also present. Every focus has a search-filter block. All ten decision-tooltip targets resolve, all six granted idea IDs resolve, and every focus-set unlock flag has a downstream decision, event, or trigger consumer. No focus name/description mismatch was identified.

The rewards are backed by live effects and costs:

- Continental Arsenals calls gods_of_africa_build_continental_arsenal once. It uses the capital if eligible, otherwise the first eligible owned African state, and builds one arms factory plus one infrastructure level or an air base level when infrastructure is complete.
- The Expedition costs 25 political power, sends 1,000 infantry equipment, 200 support equipment, and 10,000 manpower, preserves configured reserves, and has a 180-day target cooldown. Its target must be a reliable partner fighting outside Africa.
- No Sanctuary for Occupiers costs 50 political power and has a 365-day target cooldown. It adds claims and a take-claimed-state war goal for eligible African core states; it sends 1,000 infantry equipment to a valid African claimant only when Africa retains the configured reserve.
- Africa Speaks for Itself calls the guarded settlement helper, which requires a secured continent and commits participant classifications, obligations, delivery, and finalization once.
- Focus costs are 5/10/18 cost units, or 35/70/126 days, consistent with the focus spec and wiki cost rule. The separate later national-tree adoption decision costs 25 political power.

Evidence: common/scripted_effects/012_africa_gods_focus_payoff_effects.txt L24-L52 and L103-L151; common/scripted_effects/012_africa_gods_focus_payoff_triggers.txt L9-L42 and L66-L89; common/scripted_effects/012_africa_gods_effects.txt L4584-L4628.

## AI and remaining review

Each of the 25 focus blocks has ai_will_do. The Reciprocal and Exaction choices include conditional modifiers; the occupier focus weighs African-core occupation; The Last Sentence checks its Strength gate. This proves weight presence and some route-state awareness only. Numerical selection and normalized probabilities remain with chaosx_ai_probability_auditor; no probability conclusions are made here.

## Host adoption and live-check recipe

Source-only live checklist for the parent/user:

1. Use an Event 012 run where a non-South-African host with a native focus tree is selected; Ethiopia is a suitable case if it is the current host.
2. After host initialization, the loader must leave the native tree loaded and queue chaosx.nr12.1211 after the one-day delay. The offer predicate requires the current host, original_tag other than SAF, and no existing continental or generic tree.
3. Choose Keep the national course. Expected: no tree replacement and africa_adopt_continental_programme remains available in the Charter Council category.
4. Complete that decision. Expected: 25 political power is spent, africa_continental_programme_adopted is set, africa_continental_focus_tree loads, existing completed focuses are kept, and the layout is marked dirty.
5. Repeat in a fresh eligible host and choose Adopt. Expected: the same replacement without the later decision cost.
6. Check generic-tree and South African hosts separately. Generic hosts load directly without the offer; SAF keeps its native tree and rupture path.
7. On host transfer, a successor inherits the continental tree only if the previous host had it; completed focus copying occurs while the predecessor event target exists. A generic successor loads directly. A native-tree successor whose predecessor did not adopt keeps its tree and receives the later offer through the successor event path.

Evidence: common/scripted_effects/012_africa_effects.txt L1647-L1724; common/scripted_effects/012_africa_host_transfer_effects.txt L1340-L1385; events/012_african_union.txt L279-L300 and L323-L349; common/scripted_triggers/012_africa_focus_route_triggers.txt L13-L22; common/decisions/012_africa_decisions.txt L30-L42; common/script_constants/012_africa_focus_route_constants.txt L286-L293. No game was launched, so these are expected source outcomes, not live observations.

## Simplifications, blockers, and evidence limits

- The optional Sacred State / Veiled Instrument fork is absent. Focus integration L445-L473 says it should only be added if the existing routes support it without clutter, so this is not a required-route omission.
- The settlement capstone's all-three prerequisite is implemented and accepted as the architecture convergence. Its long pacing is an implementation fact: all three branch capstones and the settlement focus cost 126 days each.
- The parent applied the coordinate proposal. Its after-layout effect remains unverified because the after-change MCP inspect/raster/render sequence was blocked by the transport closure documented below.
- Before the coordinate change, two focus-inspect scenarios passed for E-I reciprocal and E-I exaction completion. The live scenario schema accepts completedFocusIds and requires treeId, but cannot set Evolution or country/global flags. No scenario rendered the actual Evolution II/III reveal states.
- The connected tools expose focus_inspect, focus_render, and focus_raster, but no standalone focus_lint. Before-change inspect diagnostics served as lint evidence. The after-change focus_inspect returned tool call error: tool call failed for hoi4_agent_tools/hoi4.focus_inspect; Caused by: Transport closed. Per the parent instruction, I stopped all remaining HOI4 MCP calls after that single failure. No after-change raster, render, or focus scenario was run.
- The before-change rasterization took over a minute. No refresh=true, focus_rewrite, broad helper expansion, standalone viewer, or game launch was used.
- Focus reference context initially omitted National focus modding, AI focuses, triggers, and localisation. Targeted wiki search/read supplied prerequisite and cost rules. The installed-doc search found no national-focus syntax document; the only directly found focus documentation file was the unrelated focus-inlay document. Vanilla source and source_lookup cover the prerequisite precedent.
- The requested hoi4.script_validate calls did not run because the focus_inspect transport closed and all remaining MCP calls were stopped: common/national_focus/012_africa_continental_focus_tree.txt, common/scripted_effects/012_africa_gods_effects.txt, and common/scripted_effects/012_africa_world_order_effects.txt. The parent added gods_of_africa_emit_global_credibility_super_event calls at common/scripted_effects/012_africa_gods_effects.txt L800 and L4747; the world-order file change is a comment update at L12-L13. Static source diff is recorded, but these files have no script_validate result.
- AI probability and live-game validation are not complete in this subtask. Do not claim normalized AI behavior or live completion.

## MCP artifacts

Workspace: mod_chaos_redux_ea3b2d67c2c0. The artifacts below are pre-coordinate-change evidence only; the after-change focus_inspect transport error prevented new artifacts. The current focus source SHA-256 was checked locally as BBBC87F353CD1221B2EAE0C2FC988A7743CB3F6E42FC46D9DCD98A642C01F0D6. Focus-inspect revision: d62959e07bd60f842bcbbda544603e2f9be1f898404f380e4e19e3761a2a2461. Focus-source hash: 3793ca1b124090b3d11e7915bd4bbde5639fa00bc9c5f9fd943e2a4708b480c6. Layout hash: b4447bf0f89889aa639aa7fa5320b95192a89b8e2ce7d3b6fa9cb3721f1e2847.

Inspection JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d49266890045e1f472440b93e3fc5aa3457acc39d34f4663676740daa9f459f7/fd20ce887b6273490c17f062f22073d3e72a4d8332bb743890dc7a3bc736c19c/focus-inspect.d62959e07bd60f84.json

Full raster PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/759693ee4bb1e6277c19334cf509a804eb05956b2863ce0b5b072e7b533bc998/014147ecc7d8fa01b721f8c81d38e14c85b1197633c4135e5e1091e2ffeb22f4/africa_continental_focus_tree.focus.png

Full graph JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d1895b6e38f7263232db6b46a7600287f960bc2e53a83f0a32bfabed19f22ba/9e3f1a2637c52a5855ed81dcac49555d74abdccadcc87b904c17078c2cb3275d/africa_continental_focus_tree.focus.json

Africa Speaks crop PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bcff58bf31a908e901ae37869edb25a884ac363da8b34b70875661bfa65a2a47/54ff1542c658eb7d8e420ea61f754d266c6059911463bcc210c72e68acc581e6/africa_continental_focus_tree.focus-problem-gods_of_africa_focus_africa_speaks_for_itself-4c5da2ae.png

No Sanctuary crop PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e31bf7fafbc6767cedb2b05f6277667a7e3bfcb411e665a6e2572e254f2d98ac/fb70f141431019a01fe0f57cfe7f8518ea99626e2889a7913ecdbbaa10a3a6ba/africa_continental_focus_tree.focus-problem-gods_of_africa_focus_no_sanctuary_for_occupiers-2a4778cf.png

The inspected physical artifacts were read from C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0\artifacts\, including the full PNG/JSON and focus-specific crops.

Skills read/applied: chaos-redux-focus-trees, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-event-assets, chaos-redux-subagents. The improvement-loop skill was not used because this is a populated, bounded overlay and no route design was requested. No skill was changed.



## Parent recovery supersession and visual review

The earlier transport-closed and after-raster gaps were resolved through one separately initialized read-only local MCP3.9.0 client.
The client/server version, exposed schemas and plain-call capability contract are recorded in `docs/plans/012_africa_plans/mcp_recovery_2026-10-06/connection_and_schemas.json`.
`focus_after.json` inspects the exact current source hash `bbbc87f353cd1221b2eae0c2fc988a7743cb3f6e42fc46d9dcd98a642c01f0d6`.
The final count is 296 diagnostics and 52 node intersections, down from 297/53, with crossing count 62 unchanged.
The Gods-specific through-node diagnostic is absent, and the five remaining warnings are the existing direct long convergences between retained branch lanes.
The first requested full-tree raster at scale 1 was blocked by its dimensions and is preserved as a failed request.
`focus_after_raster_half.json` successfully rasterizes the same layout at scale 0.5, with full PNG/SVG/JSON and five crops.
The parent read the full JSON and the Hand of Judgment/Last Sentence crops and confirmed the repaired terminal branches are outside the settlement connector.
No reward, prerequisite, duration, gate, AI weight or other 298 nodes changed.
`validate_focus.json` reports valid = true and no findings for its performed command/scope/text checks, with 567 argument blocks still unchecked.
`validate_gods.json` and `validate_world.json` report no findings but partial scope/parameter coverage, as recorded in those outputs.
Evolution-specific native reveal states and live execution remain separate checks.
