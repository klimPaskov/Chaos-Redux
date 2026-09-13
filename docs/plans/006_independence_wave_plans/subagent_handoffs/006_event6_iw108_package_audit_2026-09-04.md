# Event 006 IW-108 Buganda package audit

Date: 2026-09-04

Scope: bounded country-package audit for IW-108 Buganda (`UGA`) in the shared Chaos Redux repository.

## Decision

**FAIL-CLOSED / NO GAMEPLAY OR ASSET PATCH.** The accepted IW-108 row is not source-complete for Event 006 admission, and UGA is already an Event 012 Buganda carrier. No central admission gate, origin, tag, state, history, event, focus, decision, idea, AI, localisation, flag, portrait, map, asset, adapter, attestation, Join, or cleanup source was changed by this audit.

The existing Event 012 implementation is ownership evidence, not Event 006 admission evidence. Reusing it as a fallback would create competing origin, leader, focus, idea, decision, force, and cleanup owners, which is expressly outside the accepted contract.

## Authority and source review

The audit followed `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, `.agents/skills/chaos-redux-comfyui/SKILL.md`, `.agents/skills/chaos-redux-focus-trees/SKILL.md`, and `.agents/skills/chaos-redux-decisions-missions/SKILL.md`.

The required offline Paradox wiki pages consulted were `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, `AI modding - Hearts of Iron 4 Wiki.md`, `Country creation - Hearts of Iron 4 Wiki.md`, `Character modding - Hearts of Iron 4 Wiki.md`, `Map modding - Hearts of Iron 4 Wiki.md`, `National focus modding - Hearts of Iron 4 Wiki.md`, `Division modding - Hearts of Iron 4 Wiki.md`, and `AI focuses - Hearts of Iron 4 Wiki.md`.

The relevant installed vanilla documentation consulted was `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, `modifiers_documentation.md`, `loc_formatter_documentation.md`, `loc_objects_documentation.md`, `script_collection_input.md`, and `script_collection_operator.md`.

Binding Event 006 sources were `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`, `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`, `docs/specs/006_independence_wave_specs/diagrams/006_origin_separation_model.md`, `docs/specs/006_independence_wave_specs/diagrams/006_release_planner_flow.md`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`, `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`, `docs/specs/006_independence_wave_specs/research/006_sensitive_package_resolution.md`, `docs/specs/006_independence_wave_specs/research/006_sensitive_identity_research_rules.md`, `docs/specs/006_independence_wave_specs/quality/research_acceptance_checklist.md`, `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, and `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`.

## Accepted IW-108 contract

| Surface | Current receipt | Finding |
| --- | --- | --- |
| Package identity | Candidate registry row 109 and research-resolution row 109 bind `IW-108`, Buganda, `UGA`, `reuse_registered_tag`, `automatic_pool_ready_if_not_living`, package constant `iw_108`, and anchor `548`. | The research row requires a sourced period leader or institution and a reviewed identity/flag/portrait packet before admission. **Blocked.** |
| Current map binding | Installed binding row 109 records `fixed_anchor_compact`, state `548`, `548=ENG`, `ENG=126`, `RG-GREAT-LAKES-COARSE`, and Kampala victory point `12989`. The accepted anchor text is “Uganda, with Buganda as the required capital location.” | State `548` is authoritative for the current installed map. State `518` is not the accepted IW-108 binding. **No map rewrite was authorized or attempted.** |
| Reservation group | `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:81` binds `RG-GREAT-LAKES-COARSE` to 548 and mutually excludes IW-108, IW-109, IW-110, IW-111, and IW-112 on the same coarse state. | A compact state reservation alone does not prove a release package. **Blocked pending package admission.** |
| Host survival | The current binding records `ENG=126` and requires the host to retain a safe remnant. | The planner can inspect the host and anchor, but no IW-108 Event 006 transaction, host-remnant callback, or failure rollback exists. **Blocked.** |
| Event 012 origin ownership | `common/scripted_triggers/012_africa_priority_member_triggers.txt:33-35,288-295` defines the Buganda package and `africa_priority_member_origin_is_buganda`; `common/scripted_effects/012_africa_priority_member_effects.txt:66-69` records `africa_priority_origin_buganda` for UGA. | UGA/Buganda already has an origin owner. Event 006 must not substitute or silently coexist with this owner. **Blocked.** |

## Country-package coverage checklist

| Gate | Evidence and exact identifiers | Verdict |
| --- | --- | --- |
| Tag and identity | `common/script_constants/006_independence_wave_constants_registry.txt:7607` defines `iw_108 = 108`; `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:2138-2153` loads UGA and state 548; `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:807-814` exposes planner readiness only. | **BLOCKED.** No accepted non-duplicating Event 006 identity contract exists beside Event 012 UGA ownership. |
| State, capital, cores, claims, and host | Vanilla state `548-Uganda.txt` has owner `ENG`, core `UGA`, victory point `12989`, infrastructure 2, rubber 3, and manpower 3,515,625. Vanilla UGA history uses capital 548. | **PARTIAL / BLOCKED.** The current map anchor is known, but Event 006 has no release control, capital, core, claim, extension, supply, or host-survival adapter for IW-108. |
| Origin and lifecycle | Event 012 registration is `africa_priority_member_register_from_origin` and `africa_priority_member_register_requested_package` in `common/scripted_effects/012_africa_priority_member_effects.txt:434-483,626-628`; setup invokes its focus, idea, force, and recruitment helpers around `:579-610`; cleanup is `africa_priority_member_cleanup_runtime` around `:2331-2378`. | **BLOCKED.** Event 006 cannot call Event 012 lifecycle as an unapproved fallback. |
| Historical leader and roster | `common/characters/012_africa_priority_member_characters.txt:71-78` defines `africa_priority_buganda_sovereign`, male, with `GFX_portrait_012_africa_priority_buganda_sovereign`; `history/general/012_africa_priority_member_character_recruitment.txt:25-26` recruits it for UGA; Event 012 event `africa_priority_member.1240` checks it at `events/012_africa_priority_member_events.txt:18-42`. | **BLOCKED for Event 006.** The existing Daudi Cwa II source packet is an Event 012 consumer, and no independent Event 006 roster checkpoint or ownership transfer exists. |
| Portrait rights and wiring | `interface/012_africa_priority_member_characters.gfx:27-29` points to `gfx/leaders/012_africa/priority_members/portrait_012_africa_priority_buganda_sovereign_source_locked.dds`; both source-locked and non-source-locked DDS files exist under that directory. The prior ownership packet records the Jules Leclercq 1913 Public Domain Mark source, runtime-concept hash prefix `c73ca793`, and source-locked placeholder SHA-256 `b7dfc91bf2a62e9d55df61eb96589b113826422e8d6aa41a620fccbcf5257951`. | **BLOCKED.** The source-locked repaint, independent likeness/style crosswalk, and current review remain `needs_user_review`. No generated fallback, new portrait, or Event 006 wiring was made. |
| Flag provenance | Vanilla has only `gfx/flags/UGA_communism.tga`, `UGA_democratic.tga`, `UGA_fascism.tga`, and `UGA_neutrality.tga` plus medium/small variants. No mod-owned `gfx/flags/UGA*` family was found. | **BLOCKED.** The Buganda flag and released-identity review remain unresolved. No flag was copied, recoloured, synthesized, or promoted. |
| Parties and politics | Event 012 localisation supplies `africa_priority_buganda_council_party`, `africa_priority_buganda_civic_party`, and `africa_priority_buganda_producer_party` at `localisation/english/012_africa_priority_member_characters_l_english.yml:62-69`; Event 012 political event options are `africa_priority_member.1200` in `events/012_africa_priority_member_events.txt:48-158`. | **BLOCKED for Event 006.** These names and routes belong to Event 012 and cannot be promoted without an ownership and setup contract. |
| Advisors and command roster | Vanilla `common/characters/UGA.txt` contains generic UGA advisors with generic African portrait tokens; vanilla history recruits them. Event 012 adds only its sovereign character through its own recruitment file. | **BLOCKED.** No Event 006 Buganda advisor, commander, high-command, party, or institutional roster contract is accepted. No character file was changed. |
| Starting ideas | Event 012 defines `africa_priority_buganda_starting_problem` and `africa_priority_buganda_mature_compact` at `common/ideas/012_africa_priority_member_ideas.txt:64-70,180-186`, with setup and lifecycle calls in `common/scripted_effects/012_africa_priority_member_effects.txt:319-354`. | **BLOCKED for Event 006.** Existing ideas cannot be duplicated or re-owned by IW-108 without a lifecycle reconciliation. |
| Decisions and missions | Event 012 Buganda decisions are `africa_priority_buganda_advance_mechanic` at `common/decisions/012_africa_priority_member_decisions.txt:218-232`, `africa_priority_buganda_reinforce_force` at `:481-496`, and `africa_priority_buganda_post_settlement_action` at `:747-761`; shared Event 012 settlement missions use `africa_priority_member.*` events. | **BLOCKED for Event 006.** No Event 006 package decision, mission, cost, visibility, AI, or cleanup contract exists. |
| Focus tree and callbacks | Event 012 owns `africa_priority_member_focus_tree` at `common/national_focus/012_africa_priority_member_focus.txt:21-44`, with Buganda-specific conditions around `:108,174`; its loader is `africa_priority_member_ensure_focus_tree_loaded` at `common/scripted_effects/012_africa_priority_member_effects.txt:245-275`. Event 006 shared focus has zero current IW-108/UGA/Buganda matches. | **BLOCKED.** No Event 006 callback or additive Buganda tree is safe before origin/tree precedence is settled. |
| Starting forces and production | Vanilla `history/countries/UGA - Uganda.txt` has capital 548, `infantry_weapons = 1`, zero convoys, and no Event 006 force profile. Event 012's Buganda force route is `africa_priority_buganda_reinforce_force`. | **BLOCKED.** No Event 006 template, manpower, equipment, officer, production-line, train, fuel, navy, air, or supply receipt exists. |
| Technology and industry | Vanilla UGA starts with `infantry_weapons = 1`; `common/countries/Uganda.txt` contains graphical culture and colour only; vanilla UGA ideas are empty. | **BLOCKED / INCOMPLETE.** No Event 006 technology, research-slot, industry, production, or logistics setup is defined. The installed package exposes no Technology Tree Viewer. |
| AI strategy and playability | Event 012 has decision/focus AI factors, but no Event 006 IW-108 strategy profile or package-specific survival scenarios exist. | **BLOCKED.** No quantitative probability or survival claim is made. |
| Adapter and package publisher | `independence_wave_load_package_iw_108` at `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:2138-2153` is planning/reservation metadata; `independence_wave_prepare_weight_iw_108` and `independence_wave_reserve_package_iw_108` occur at `:2268-2274,2360-2365`. | **BLOCKED.** `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` has zero current IW-108/UGA/Buganda matches, so there is no runtime adapter. |
| Attestation, preflight, SCN-008, and Join | The central Event 006 attestation OR-list and adapter OR-list in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-62,159-210` contain no IW-108 entry. Preflight still requires both adapter and content attestation. Event 006 Join has zero IW-108 matches. | **BLOCKED.** This audit intentionally did not widen central admission, attestation, SCN-008 publication, or Join. |
| Cleanup and no-pre-event visibility | Event 012 cleanup owns its package variables and flags; Event 006 has no IW-108 setup/failure/cleanup branch. Current source map states that nothing is visible before Event 006 fires. | **BLOCKED.** No Event 006 generation-safe cleanup, host-remnant rollback, subject/puppet/cosmetic cleanup, leader retirement, or no-pre-event package receipt exists. |
| GUI and technology viewers | No Buganda-owned scripted GUI was found. The Event 006 Statehood Ledger GUI is shared and unrelated to IW-108. | **N/A for a local patch.** No dedicated Buganda GUI was invented. No Technology Tree Viewer is installed. |

## File-surface checklist

| Surface | Current path(s) | State |
| --- | --- | --- |
| Accepted registry and research | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:109`; `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:109` | Present as design metadata only. |
| Map package binding | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:109`; `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:81` | Present and bound to state 548. |
| Planner/loader | `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:807-814`; `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:2138-2153,2268-2274,2360-2365` | Present, but not executable admission. |
| Runtime dispatch | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-62,159-210`; `common/scripted_effects/006_independence_wave_effects.txt:3451`; `common/scripted_effects/006_independence_wave_join_effects.txt` | The shared weight initializer only assigns `independence_wave_weight_iw_108 = zero` at `:3451`; IW-108 is absent from runtime adapter and Join surfaces. |
| Event 012 ownership | `common/scripted_triggers/012_africa_priority_member_triggers.txt:33-35,288-295`; `common/scripted_effects/012_africa_priority_member_effects.txt:66-69,245-275,319-354,434-483,579-610,626-628,2331-2378`; `events/012_africa_priority_member_events.txt:1-42,48-158` | Existing UGA/Buganda owner and lifecycle. |
| Country and history | Vanilla `common/country_tags/00_countries.txt:147`; `common/countries/Uganda.txt`; `history/countries/UGA - Uganda.txt`; `history/states/548-Uganda.txt`; `common/characters/UGA.txt`; `history/general/012_africa_priority_member_character_recruitment.txt:25-26` | Vanilla UGA carrier plus Event 012 sovereign recruitment. |
| Event 012 focus, decisions, ideas | `common/national_focus/012_africa_priority_member_focus.txt:21-44,108,174`; `common/decisions/012_africa_priority_member_decisions.txt:218-232,481-496,747-761`; `common/ideas/012_africa_priority_member_ideas.txt:64-70,180-186` | Existing content is Event 012-owned and not an Event 006 substitute. |
| Localisation | `localisation/english/012_africa_priority_member_characters_l_english.yml:62-69`; `localisation/english/012_africa_priority_member_focus_l_english.yml:37,56,74,92,110,128,146,164,182,200,238,285-287`; `localisation/english/012_africa_priority_member_l_english.yml:54-56,102-104,150-152,246,269,294,319` | Event 012 Buganda strings exist; Event 006-specific strings do not. |
| Portrait and icon assets | `interface/012_africa_priority_member_characters.gfx:27-29`; `interface/012_africa_priority_member_assets.gfx:46-47,96-98`; `gfx/leaders/012_africa/priority_members/portrait_012_africa_priority_buganda_sovereign_source_locked.dds`; `gfx/leaders/012_africa/priority_members/portrait_012_africa_priority_buganda_sovereign.dds` | Existing Event 012 assets only; rights review remains open. |

## Map and state setup issues

The accepted current-map binding is state 548, not state 518. Vanilla state 548 is an ENG-owned rural Uganda state with UGA core, Kampala victory point 12989, infrastructure 2, rubber 3, and manpower 3,515,625. The Event 006 reservation group is coarse and mutually exclusive with other Uganda/Great Lakes rows. The current binding records `548=ENG` and `ENG=126`, but there is no IW-108 release transaction, control callback, compact-extension ledger, host-remnant check, or rollback.

No `hoi4.map_rewrite` call was made. Map mutation is outside this bounded package audit and would require the parent-owned dry-run/review/apply/post-validation and recovery workflow. A previous read-only state artifact remains useful but does not prove Event 006 release safety: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/deb61c2bcbf748c79b881cc3a365b4e77af5fa7be64984be00572d33e1dfbe93/3e7d7dee8a4c85a36a4822f84a4bdb22982339a8b7ce4f04d24b39ea19cce21a/map-inspect.b7b2aed87ddd4e30.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd8b53eb2549add50b207cbe2fd618aafa44f6729a7363de31f02dba24b7b466/353e1fb67d7db1e6c58a1d7707e2ae0e6b815f316bc244b9a33ea73089c55885/map-state.png`.

## Politics, leader, portrait, flag, advisor, and party issues

Event 012 owns the Buganda package identity, the male `africa_priority_buganda_sovereign` character, its source-locked portrait consumer, the Crown Compact/Federal Balance/Land Reform Compact party strings, and the associated recruitment and political settlement events. The sourced historical leader packet identifies Daudi Cwa II in a 1913 Jules Leclercq source with a Public Domain Mark, but the independent likeness/style review and current UGA portrait/flag review remain `needs_user_review`. The package is grounded and therefore cannot use a generated fictional leader or institutional fallback.

Vanilla UGA's neutral name is already “Kingdom of Buganda,” but this does not resolve Event 006 origin or rights ownership. Vanilla UGA advisors use generic African portrait tokens and are not an Event 006 Buganda roster. No politics, party, leader, advisor, portrait, or flag file was touched.

## Focus, decision, idea, and asset issues

Event 012's eight-focus `africa_priority_member_focus_tree`, Buganda-specific focus conditions, three Buganda decisions, starting/mature ideas, and their localisation/icons are coherent as an Event 012 package but are not an Event 006 package. Event 006's shared `independence_wave_focus_tree`, `common/decisions/006_independence_wave_decisions.txt`, and `common/scripted_effects/006_independence_wave_join_effects.txt` have no IW-108 package route or callback. No generic content, copied decision, duplicate idea, fallback tree, or new asset was added.

## Starting military, technology, industry, supply, and production issues

Vanilla UGA provides only `infantry_weapons = 1`, zero convoys, capital 548, and a generic advisor roster. There is no accepted IW-108 template, equipment budget, manpower/officer allocation, research-slot or technology profile, production-line setup, train/fuel/supply setup, navy/air package, or generation receipt. Event 012's Buganda force decision cannot substitute for Event 006's starting force contract.

## AI and playability issues

No Event 006 IW-108 AI strategy profile, focus preference, decision score, mission score, host diplomacy factor, supply-aware force choice, or survival scenario exists. The required named `chaosx_ai_probability_auditor` route is not callable in this session, and the direct `hoi4.probability_inspect` route ended with `Transport closed`. Accordingly, no AI balance or probability claim is made and no weight was changed.

## Read-only HOI4 MCP evidence and blockers

All attempted calls used workspace `mod_chaos_redux_ea3b2d67c2c0`. No MCP write was issued.

| Required route | Result | Limitation recorded |
| --- | --- | --- |
| `hoi4.map_inspect` for state 548 | Timed out after 180 seconds with `tool call failed for hoi4_agent_tools/hoi4.map_inspect Caused by: timed out awaiting tools/call after 180s`. | Current map claims rely on accepted binding plus prior read-only artifacts; no fresh engine receipt is claimed. |
| `hoi4.map_render` | Not completed after the map transport failure. | No fresh render claim. |
| `hoi4.focus_inspect` and `hoi4.focus_render` for `africa_priority_member_focus_tree` and `independence_wave_focus_tree` | Each current route returned `tool call failed for hoi4_agent_tools/hoi4.focus_* Caused by: Transport closed`. | Prior read-only Event 012/Event 006 focus artifacts remain references only. Event 012 inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a29e0b6a0e05f8737d2eacb15b1c34ed3f1b3e796cb058a94071a129fc75d8d/d4c27a3caa9d275fc5fc177210725abb21a5f93b3f3359d97132539683372915/focus-inspect.725998323b332151.json`; Event 006 inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bbc157951d8fd106c8122563bc0f98ddeb6854410d7bdf276411bf6baf11a011/225bf73504c9cb0bb6e6babc31610b538fd24eca423214013b521f27968121b6/focus-inspect.725998323b332151.json`. |
| `hoi4.event_inspect` and `hoi4.event_render` for Event 012 and Event 006 | Current routes returned `tool call failed for hoi4_agent_tools/hoi4.event_* Caused by: Transport closed`. | Prior partial traces are not treated as current completion evidence. |
| `hoi4.tech_inspect` and `hoi4.tech_render` | Current routes returned `tool call failed for hoi4_agent_tools/hoi4.tech_* Caused by: Transport closed`. | No Technology Tree Viewer is installed; technology validation remains unresolved. |
| `hoi4.probability_inspect` | Current route returned `tool call failed for hoi4_agent_tools/hoi4.probability_inspect Caused by: Transport closed`. | The mandatory `chaosx_ai_probability_auditor` custom route is unavailable; no weighted claim is made. |

Prior useful read-only Event 006/Event 012 artifacts are retained in the 2026-08-30 and 2026-09-02 Buganda handoffs, including focus, event, map, and technology artifact references. They do not prove current runtime admission, save/load, or live gameplay.

## Validators run

The refreshed task-specific validators passed without changing IW-108 admission:

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked selectable packages, 40 runtime adapters, 32 attested packages, 29 compatible reservation groups, and the unchanged 3/4/5/7/10 automatic ladder.
- `python -B .tools/audit_event6_country_api.py` passed with 242 broad rows, 191 unique carriers, 34 Soviet carriers, 45 Africa carriers, zero missing, zero duplicate, and IW-031 crosswalk pass.
- `python -B .tools/audit_event6_flags.py --strict` passed with 102 registered Event 006 tags, 102 complete flag families, and zero incomplete families; this does not prove UGA/Buganda admission because IW-108 is not attested.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge receipts with the single publication/result/log dispatch contract.
- `python -B .tools/audit_event6_form16.py` passed the existing FORM-16 ARM/GEO/AZR contract; it is unrelated to IW-108 but confirms the shared admission boundary was not altered.
- `python -B .tools/audit_event6_gui_matrix.py` passed the shared Statehood Ledger semantic source matrix; it does not provide Buganda GUI evidence.

## Changed files and before/after behavior

Only this handoff was added: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw108_package_audit_2026-09-04.md`.

No tag, state ID, leader, party, focus-tree ID, localisation key, decision ID, idea ID, formable ID, adapter, attestation entry, Join entry, map surface, or asset was changed. Before and after this audit, IW-108 remains planner/loader metadata only, UGA/Buganda remains Event 012-owned, central Event 006 admission remains unchanged, and no IW-108 content is visible before Event 006 fires.

## Remaining blockers and next owner

- Resolve the non-duplicating Event 012/Event 006 UGA origin and consumer ownership contract before any gameplay wiring.
- Complete and review the period-valid Buganda leader/institution source packet, portrait rights and likeness/style crosswalk, and flag provenance packet through the portrait and asset ownership routes.
- Define the Event 006 package-local force, politics, ideas, decisions/missions, focus callback or additive tree, AI, localisation, adapter, setup, rollback, cleanup, attestation, preflight, SCN-008, and Join receipts without calling Event 012 as a fallback.
- Rebind and engine-inspect state 548 and host survival through the parent-owned map workflow after the MCP transport is restored.
- Run the mandatory probability audit and comparison once `chaosx_ai_probability_auditor` and the HOI4 probability route are callable.
- Resolve the installed Technology Tree Viewer limitation before claiming technology-tree evidence.

No broad identity redesign plan was written because the accepted package is blocked at ownership and source admission, and the parent owns any future design decision. No staging, commit, live-game, or save-load claim was made.
