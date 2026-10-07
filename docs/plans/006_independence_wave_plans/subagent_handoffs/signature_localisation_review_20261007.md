# Signature localisation review, 7 October 2026

Disposition: implemented text corrections, unresolved visual and nested framework requirement coverage.
Parent assignment authorizes routine localisation corrections, with all gameplay source owned by the parent.
Only the assigned YML and this handoff were changed by this worker.
No commit, index operation, launch, logs, assets, GUI changes, price changes or workbook/export edits were made.

## Scope and source review

Read AGENTS.md and the events, decisions-missions, focus-trees and subagents skills.
Consulted the improvement-loop guidance for the already pending Mon river-office closure gap without inventing a capstone or opening another plan.
Reviewed every title, description and effect tooltip for the 31 shared focuses: 10 Oyo, 10 Aceh and 11 Mon.
Reviewed all seven paid decisions, their price variants, ideas, player gate flags, signature triggers/effects/constants and referenced shared payment and transport selectors.
The files reviewed are common\national_focus\006_independence_wave_signature_modules_focus.txt, common\decisions\006_independence_wave_signature_modules_decisions.txt, common\scripted_effects\006_independence_wave_signature_modules_effects.txt, common\scripted_triggers\006_independence_wave_signature_modules_triggers.txt, common\ideas\006_independence_wave_signature_modules_ideas.txt and common\script_constants\006_independence_wave_signature_modules_constants.txt.
Shared dependencies were reviewed read-only in 006_independence_wave_decision_effects.txt, 006_independence_wave_decision_triggers.txt, 006_independence_wave_constants_registry.txt, 006_independence_wave_scripted_localisation_registry.txt, 006_independence_wave_decisions_l_english.yml and the focus helpers.

## Payment and timer evidence

| Decision suffix | Startup payment | Temporary factories | Timer |
| --- | --- | --- | --- |
| dsx_signature_fund_market_roads | 10 percentage points stability, 20 command power, 10 convoys or 10 trains | 2 | 180 days |
| atj_signature_organize_pusa | 20 command power, 5,000 manpower | 2 | 120 days |
| atj_signature_secure_port_credit | 20 command power, 10 convoys or 10 trains | none | 120 days |
| atj_signature_retire_port_credit | 10 percentage points stability, 20 command power, 10 convoys or 10 trains | 2 | 180 days |
| iax_signature_build_salween_transport | 10 percentage points stability, 20 command power, 10 convoys or 10 trains | 2 | 180 days |
| iax_signature_prepare_tenasserim_watch | 10 command power, 250 infantry equipment, 50 support equipment | none | 120 days |
| iax_signature_school_delegates | 20 command power, 10 convoys or 10 trains | none | 120 days |

All figures above describe the inspected constant revision and are not hardcoded into the new text.
The eight positive price constants match the negative payment constants exactly.
The diplomatic payment and both standard transport selectors use the same NOT convoy < convoy_standard predicate, choosing convoys at 10 and trains when the convoy reserve is below 10 and trains qualify.
The blocked variant uses the matching blocked selector, while the fallback offers the two alternatives.
This is source proof of matching predicates and amounts, not observed native stockpile behavior.
Strategic factories appear in the hover explanation, and administration factories appear in the compact row and lifecycle explanation.
The four factory commitments are modifiers during the timer, not resources consumed by the payment effect.
Cancellation has no refund effect, while timer removal releases the modifier.
The hover text now explicitly identifies the count and duration and distinguishes released factories from resources already spent.
The persistent package/current-generation gates and single active project slot introduced by the decision auditor were preserved.

## Prose and behavior before and after

- Vagueness: route tooltips that said a route follows a settlement now state the required institutional choice or explain how an already settled balance limits the fork.
The port-board gate now requires the extended school network rather than describing an earlier institutional step.
Aceh federation text now names retiring the port credit, and Mon federation text names publishing autonomy.
- Bloat: factory hover explanations were shortened to one lifecycle sentence with a dynamic count and timer.
- Obvious explanation: maritime-congress effect text now states the unlocked invitation/consent process rather than repeating the description's sovereignty promise.
- Repetition: Mon school descriptions distinguish preparation from funding and the resulting bilateral relations.
Clear institutional prose elsewhere was retained rather than rewritten to impose a different voice.
- Overcomplication: abstract phrases such as an institution entering the settlement now name the actual granted idea.
Burma/Siam requirements specify peace with Mon instead of suggesting peace in every war.
- Style repair: three semicolon-bearing cancellation lines were rewritten as complete sentences.
The delegate cancellation line covers lost school eligibility, missing neighbors and war with a neighbor without promising a retry under insufficient conditions.
- Source mismatch: Aceh route-selection focuses remove the Council of Notables and set a route receipt, while the follow-up focuses grant the replacement idea.
The text now places the grant at the confirmation, seating or ratification step.
- Source mismatch: infrastructure and naval-base/fort rewards are building levels rather than newly created whole buildings.
The two extra shared-building-slot counts now use the existing building_slot constant.
- Source mismatch: capital requirements now state ownership as well as control.
PUSA is available from 5 May 1939, not only on that date.
- Concealed consequence: the Oyo compact tooltip now includes the internal instability increase from reward_ambition, and the Mon autonomy tooltip states the instability reduction from reward_public_settlement.

## Missing keys, duplicate keys, scripted localisation and encoding

Six directly exposed Aceh route/completion flag keys and nineteen additional paid-decision/helper requirement keys were missing and added below.
All 31 focus title, description and effect-tooltip sets exist.
All explicit decision/focus names, descriptions, custom requirements and effect tooltip references resolve.
All four used cost families have enabled, blocked and hover keys.
The English-wide duplicate scan found no duplicate for any owned key.
No unresolved dollar-key reference or missing This selector definition was found in the assigned YML.
The shared standard transport selector output keys and predicates were checked read-only and left unchanged.
UTF-8 BOM was preserved and no key:0 syntax introduced.
No colour-bearing report descriptions were changed.
Literal colour codes remain confined to the inherited dark decision price and hover surfaces in this file.
No quotation-bearing text was found in this assigned set, so no sourced quotation was changed.
Existing dynamic tokens and formatting codes were retained, with extra building-slot/count tokens added for existing values.

## MCP and visual limits

The connected reference tools responded successfully for localisation context, localisation-variable search/read and custom_cost_text search/read.
Workspace identity: mod_chaos_redux_ea3b2d67c2c0.
Initial focus_inspect on common/national_focus/006_independence_wave_signature_modules_focus.txt returned FOCUS_TREE_NOT_FOUND: The selected source contains no national focus tree.
That file defines shared_focus blocks, consumed by independence_wave_focus_tree in common/national_focus/006_independence_wave_focus.txt.
The subsequent parent-tree inspect and source_lookup request did not deliver results before their orchestration was terminated after several minutes.
No result from those requests was available to review, so they establish no coverage.
The parent-tree focus_render request using the three module entry focus IDs did not return within a 45-second bounded attempt and produced no artifact URI.
Initial decision inspect requests without scenarios were rejected with MCP -32602, Decision inspection requires declared scenarios at scenarios.
Corrected requests for each of the seven decision IDs declared signature-price-exact-convoy and signature-price-exact-train scenarios, actor DSX/ATJ/IAX, date 1939.5.5, command power 20, stability 0.10, manpower 5000, available factories 2, infantry equipment 250 and support equipment 50.
The convoy scenario used 10 convoys and zero trains, while the train scenario used 9 convoys and 10 trains.
Each corrected request remained unresolved at the 30-second bounded attempt and returned no inspected artifact.
These partial price scenarios do not declare full package, generation, school, state-control or route state, and would not prove availability even if they returned.
No decision-render route is exposed in the connected tool list.
Focus overflow, layout, wrapping and before/after render proof remain blocked.
Source checks are not substituted for production visuals.
No GUI, map, event popup or technology surface was assigned or edited.
Standalone Technology Tree Viewer availability was checked separately through the connected tool inventory and repository tool/agent filenames.
No standalone viewer capability or package entry was found there, while tech_inspect, tech_render and tech_compare are exposed.
Record this as a package gap in the checked inventories, with uncertainty about installations outside those inventories, not proof that those technology services are healthy.
No useful focus/decision artifact URI was obtained.

## Parent dependencies and unresolved work

- The available blocks of the paid decisions and three Aceh institutional follow-ups still expand shared can_start/package/current-generation helpers directly.
The new keys repair player-meaningful signature receipts, but do not conceal raw nested framework flags, package variables, generation comparisons or native construction diagnostics.
Parent should wrap implementation-only framework checks in hidden_trigger and state the real requirement with custom_trigger_tooltip in the owned gameplay files.
Do not create localisation for internal generation counters merely to disguise missing custom requirements.
- The seven-project slot is hidden in availability and excludes another project through visibility.
No price or lifecycle change is needed for the existing slot contract.
- The Mon river-office branch closure remains pending with the planner/parent.
No fictional post-1947 groups, Thai annexation or new capstone mechanics were added.
Parent-added capstone keys after this snapshot need their own review and are outside this worker's changed-key list.
- Shared cost/localisation helpers outside the assigned YML were not patched.
- Event catalog workbook comparison was not assigned and was not run.
No workbook mismatch is established by this review.
If the spreadsheet owner mirrors these passages, the exact final key-value list below is the wording handoff.
- Exact historic claim research beyond the user-supplied historical gates was not expanded.
PUSA's dated gate and the Mon period/sovereignty constraints were preserved.
- Meaningful skipped validation: native rendering/overflow and live timer/factory/stockpile behavior, because no required artifact returned and live gameplay belongs to the user.
No gameplay simplification was introduced by the localisation patch.
The audit is not a claim of full engine or visual completion.

## Reference evidence

All relative paths below are rooted at C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.

- paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md, lines 184-215, Formatting variables, MCP read revision 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064.
- paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md, lines 305-336, custom-cost enabled/blocked/hover semantics, MCP read revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162.
Local direct reading also covered lines 337-355 for timer modifiers and cancellation.
- C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\loc_formatter_documentation.md, MCP header lines 1-2 and direct local lines 1-70, SHA-256 1fbd9a031fd09100d79bac08dec3c16e19468f23516c5e67c67578156282af08.
The header-only MCP section did not establish detailed formatter coverage.
- C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md, direct lines 216-246, Script Constants.
- C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md, direct lines 1-55, scoped constants and schema.
- Vanilla localisation\english\decisions_l_english.yml, lines 135-147, factory cost hover precedents describing use while active.

## Exact changed keys and final wording

Changed existing keys: 47.
Added keys: 25.

### Changed existing values

```yaml
independence_wave_dsx_signature_fund_market_roads_effect_tt: "Adds [?constant:independence_wave_signature_project.infrastructure_level|.0] infrastructure level and [?constant:independence_wave_signature_project.building_slot|0] shared building slot in Oyo's capital state."
independence_wave_dsx_focus_authorize_the_yoruba_congress_effect_tt: "Unlocks Oyo's regional ambition and leadership decisions."
independence_wave_atj_signature_organize_pusa_desc: "From 5 May 1939, the ulama can organize Persatuan Ulama Seluruh Aceh (PUSA) to set shared standards for Aceh's reform schools."
independence_wave_atj_signature_secure_port_credit_effect_tt: "Adds [?constant:independence_wave_signature_project.naval_base_level|.0] naval base level in Banda Aceh and replaces the pepper-port trade terms with Penang Merchant Credit."
independence_wave_atj_focus_protect_uleebalang_districts_effect_tt: "Favors district authority and replaces the Council of Notables with district guarantees once they are confirmed."
independence_wave_atj_focus_give_ulama_a_school_board_effect_tt: "Favors the ulama and replaces the Council of Notables with a school board once it is seated."
independence_wave_atj_focus_keep_a_shared_council_effect_tt: "Balances district and school authority and replaces the Council of Notables with a shared council once it is ratified."
independence_wave_atj_focus_confirm_district_guarantees_effect_tt: "Grants Uleebalang District Guarantees."
independence_wave_atj_focus_seat_the_school_board_effect_tt: "Grants the Ulama School Board."
independence_wave_atj_focus_ratify_the_shared_council_effect_tt: "Grants the District and School Council."
independence_wave_atj_focus_convene_the_maritime_congress_effect_tt: "Opens the maritime federation invitation and consent process."
independence_wave_iax_signature_form37_available_tt: "Publish Mon Federal Autonomy after completing the local charter, Salween transport works and Tenasserim border watch. The mainland federal compact must remain available."
independence_wave_iax_signature_build_salween_transport_effect_tt: "Adds [?constant:independence_wave_signature_project.infrastructure_level|.0] infrastructure level and [?constant:independence_wave_signature_project.building_slot|0] shared building slot in Mon State's capital state."
independence_wave_iax_signature_prepare_tenasserim_watch_effect_tt: "Adds [?constant:independence_wave_signature_project.bunker_level|.0] land fort level on Tenasserim's Western Siam frontier."
independence_wave_iax_focus_trust_local_mon_councils_effect_tt: "Entrusts local administration to Mon councils and monasteries."
independence_wave_iax_focus_direct_the_river_office_effect_tt: "Entrusts river administration to the central Moulmein office."
independence_wave_iax_focus_exchange_school_delegates_desc: "Prepare school visits to Burma and Siam to share teaching methods and strengthen ties with both neighbors."
independence_wave_iax_focus_exchange_school_delegates_effect_tt: "Unlocks the paid school delegation to Burma and Siam while both exist and neither is at war with Mon."
independence_wave_dsx_signature_route_choice_tt: "Choose an institutional route before Oyo's power struggle is settled, or follow the crown, council or compromise settlement already reached."
independence_wave_dsx_signature_alaafin_route_tt: "Adopt the Alaafin's Charter to commission the horse guard."
independence_wave_dsx_signature_mesi_route_tt: "Adopt the Oyo Mesi mandate to register the town guard."
independence_wave_dsx_signature_town_route_tt: "Choose the Yoruba town federation and reconcile Ibadan's terms."
independence_wave_atj_signature_route_choice_tt: "Choose an institutional route before Aceh's power struggle is settled, or follow the district, ulama or compromise settlement already reached."
independence_wave_atj_signature_district_route_tt: "Choose Uleebalang district authority to confirm its guarantees."
independence_wave_atj_signature_school_route_tt: "Choose the ulama school board to seat it."
independence_wave_atj_signature_shared_route_tt: "Choose the shared district and school council to ratify it."
independence_wave_atj_signature_school_network_ready_tt: "Extend the Reform-School Network before chartering the port board."
independence_wave_iax_signature_route_choice_tt: "Choose a governing route before Mon's power struggle is settled. A central settlement requires the river office, while a local or compromise settlement allows the local councils."
independence_wave_iax_signature_local_route_required_tt: "Choose the local councils to guarantee their charter."
independence_wave_iax_signature_river_route_required_tt: "Choose the central Moulmein office to place river works under its authority."
independence_wave_iax_signature_delegates_ready_tt: "Mon must have the Mon Language School Trust. Burma and Siam must both exist, and neither may be at war with Mon."
independence_wave_iax_signature_school_delegates_desc: "Fund school visits to Burma and Siam while both countries exist and neither is at war with Mon."
independence_wave_iax_signature_school_delegates_effect_tt: "Improves relations in both directions between Mon and each of Burma and Siam for a limited time."
independence_wave_iax_signature_school_delegates_cancelled_tt: "The delegation stops if Mon loses its capital or governing settlement, its school trust closes, either neighbor disappears, or Mon goes to war with either. Resources already spent are not refunded."
independence_wave_dsx_signature_project_cancelled_tt: "The road project stops if Oyo loses its capital or governing settlement, or the state can no longer receive the infrastructure. Resources already spent are not refunded."
independence_wave_iax_signature_project_cancelled_tt: "The project stops if Mon loses its capital or governing settlement, or the works can no longer be built. Resources already spent are not refunded."
independence_wave_atj_signature_project_cancelled_tt: "The project stops if Aceh loses its capital or governing settlement, or its school or port requirements cease to hold. Resources already spent are not refunded."
independence_wave_signature_cost_strategic_tooltip: "$independence_wave_signature_cost_strategic$\nCommits §Y[?constant:independence_wave_decision_cost.civilian_factory_standard|0]§! £civ_factory for [?constant:independence_wave_decision_duration.long|0] days, released on completion or cancellation."
independence_wave_signature_cost_administration_standard_tooltip: "$independence_wave_cost_administration_standard$\nCommits §Y[?constant:independence_wave_decision_cost.civilian_factory_standard|0]§! £civ_factory for [?constant:independence_wave_decision_duration.standard|0] days, released on completion or cancellation."
independence_wave_dsx_signature_anchor_control_tt: "Oyo must own and control its capital state."
independence_wave_dsx_focus_publish_the_oyo_compact_effect_tt: "Raises legitimacy, recognition, administrative capacity and security. Regional ambition also raises internal instability."
independence_wave_atj_signature_l2_projects_complete_tt: "Complete the notables' council, madrasah and pepper-port projects to open Aceh's institutional choices."
independence_wave_atj_signature_anchor_control_tt: "Aceh must own and control its capital state."
independence_wave_atj_signature_form36_available_tt: "Extend Aceh's reform-school network and retire the Penang port credit. The maritime federation must remain available."
independence_wave_atj_signature_retire_port_credit_desc: "Commit resources to clear the port advance and bring the harbor under an Aceh Port Trust."
independence_wave_iax_signature_anchor_control_tt: "Mon State must own and control its capital state."
independence_wave_iax_focus_publish_mon_federal_autonomy_effect_tt: "Raises legitimacy, recognition and administrative capacity, and reduces internal instability."
```

### Added gate values

```yaml
independence_wave_atj_signature_district_guarantees: "Aceh has chosen Uleebalang district guarantees"
independence_wave_atj_signature_district_terms_complete: "Aceh has confirmed its district guarantees"
independence_wave_atj_signature_ulama_school_board: "Aceh has chosen the ulama school board"
independence_wave_atj_signature_school_board_complete: "Aceh has seated the ulama school board"
independence_wave_atj_signature_shared_council: "Aceh has chosen the shared district and school council"
independence_wave_atj_signature_shared_council_complete: "Aceh has ratified the shared district and school council"
independence_wave_signature_module_open: "The country's institutional development is open"
independence_wave_dsx_signature_active: "Oyo's institutional development is active"
independence_wave_atj_signature_active: "Aceh's institutional development is active"
independence_wave_iax_signature_active: "Mon's institutional development is active"
independence_wave_dsx_signature_roads_authorized: "Oyo has authorized the market roads"
independence_wave_dsx_signature_roads_complete: "Oyo has completed the market roads"
independence_wave_atj_signature_school_network_extended: "Aceh has extended its reform-school network"
independence_wave_atj_signature_pusa_organized: "Aceh has organized PUSA"
independence_wave_atj_signature_port_board_chartered: "Aceh has chartered its port board"
independence_wave_atj_signature_port_credit_active: "Aceh has an outstanding Penang port advance"
independence_wave_atj_signature_port_credit_retired: "Aceh has repaid the Penang port advance"
independence_wave_iax_signature_local_charter_complete: "Mon has guaranteed the local councils' charter"
independence_wave_iax_signature_river_charter_complete: "Mon has placed river works under the Moulmein office"
independence_wave_iax_signature_transport_authorized: "Mon has authorized the Salween transport works"
independence_wave_iax_signature_transport_complete: "Mon has completed the Salween transport works"
independence_wave_iax_signature_border_watch_authorized: "Mon has authorized the Tenasserim border watch"
independence_wave_iax_signature_border_watch_complete: "Mon has completed the Tenasserim border watch"
independence_wave_iax_signature_delegate_program_authorized: "Mon has authorized its school delegation"
independence_wave_iax_signature_delegates_exchanged: "Mon has completed its school delegation"
```

### Source snapshot hashes

- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\localisation\english\006_independence_wave_signature_modules_l_english.yml`: `9e39ee37534fc5f544f74340bbc2a8cf9b4ffa7cba88f5f607b4f73b240f8662`.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\national_focus\006_independence_wave_signature_modules_focus.txt`: `9da9d4cfa63b79dc6d9ece9c44d8d9b1bc660cea5a75aa1719143e67f82ee3ba`.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\006_independence_wave_signature_modules_decisions.txt`: `084c77b9d5e5c00e26ba2bf3bc89cfedb5043908765ad55f32f3ef0fa419c73d`.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_effects\006_independence_wave_signature_modules_effects.txt`: `7a9e8f7f84d6142816715aa998be525a3306ae42077fd5ce8c46c4a46ec6ff76`.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_triggers\006_independence_wave_signature_modules_triggers.txt`: `31777494886998ebb77fc5e8a2be410803053155fcfdca88483b25643ee34ac9`.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\ideas\006_independence_wave_signature_modules_ideas.txt`: `d9c19bcc6de460596deedb1cc34a08b9b2e701c7a914f3d3841d7d6eed5e8cba`.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\script_constants\006_independence_wave_signature_modules_constants.txt`: `fdb6e13c7bd89560beeba84b0cc706676b4cd1cea43477f84c62afa6853a6a3e`.

## Parent wrapper follow-up, 7 October 2026

The earlier nested framework requirement blocker is superseded for the seven signature decision availability package predicates and the three Aceh institutional follow-up availability blocks.
Each now uses a custom_trigger_tooltip around its complete package predicate or full follow-up condition set, so the nested package/current-generation tests are concealed on these ten surfaces.
Affordability helpers remain separate, and anchor-control tooltips and the hidden single-project-slot check are preserved.
Reviewed only the ten parent-added strings, wrappers and their referenced signature conditions in this follow-up.
Reworded all ten strings to state concrete requirements, including unfinished/unchosen completion receipts, PUSA organization date, Aceh pepper-port trade and completed institutional settlement, outstanding credit, and Mon completed charter and bilateral peace.
The three Aceh follow-ups require completed opening projects, not retention of the Council of Notables idea removed by the route choice.
Meaningful source validation: all ten tooltip keys resolve uniquely and each has exactly one corresponding wrapper reference.
No missing or duplicate key, new scripted localisation call, dynamic-token change, quote change, price/timer change or gameplay edit was introduced.
No further MCP request was made per parent instruction, and the existing visual gap remains unchanged.
The planned Mon/PUSA payoff remains deferred to the planner and parent.

Exact follow-up changed keys and final wording:

```yaml
independence_wave_dsx_signature_roads_project_ready_tt: "Oyo must retain its capital and governing institutions. The market roads must be authorized, unfinished and able to add infrastructure in the capital state."
independence_wave_atj_signature_pusa_project_ready_tt: "Aceh must retain its capital and governing institutions, extend its reform-school network and reach 5 May 1939. PUSA must not already be organized."
independence_wave_atj_signature_port_project_ready_tt: "Aceh must retain its capital and pepper-port trade, complete an institutional settlement and charter the port board. It must control Banda Aceh, whose harbor can receive another naval-base level, and have neither an outstanding nor a repaid Penang advance."
independence_wave_atj_signature_retirement_project_ready_tt: "Aceh must retain its capital and governing institutions, with Penang Merchant Credit still active and the advance unpaid."
independence_wave_iax_signature_transport_project_ready_tt: "Mon must retain its capital and governing institutions. The Salween works must be authorized, unfinished and able to add infrastructure in the capital state."
independence_wave_iax_signature_border_project_ready_tt: "Mon must retain its capital and governing institutions, authorize the unfinished border watch and control its Tenasserim frontier province, where another land fort level can be built."
independence_wave_iax_signature_delegate_project_ready_tt: "Mon must retain its capital and school trust, complete either institutional charter and authorize its unfinished delegation. Burma and Siam must both exist and neither may be at war with Mon."
independence_wave_atj_signature_district_terms_ready_tt: "Aceh must own and control its capital and have completed the notables' council, madrasah and pepper-port projects. Uleebalang district guarantees must be chosen and still await confirmation."
independence_wave_atj_signature_school_board_ready_tt: "Aceh must own and control its capital and have completed the notables' council, madrasah and pepper-port projects. The ulama school board must be chosen and still await seating."
independence_wave_atj_signature_shared_council_ready_tt: "Aceh must own and control its capital and have completed the notables' council, madrasah and pepper-port projects. The shared district and school council must be chosen and still await ratification."
```
