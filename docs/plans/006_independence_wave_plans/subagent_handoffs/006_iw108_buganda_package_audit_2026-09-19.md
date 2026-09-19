# IW-108 Buganda country-package audit

Date: 2026-09-19.

Scope: bounded Event 006 country-package audit for IW-108 Buganda, registered carrier `UGA`, accepted compact anchor state `548`, and reservation group `RG-GREAT-LAKES-COARSE`.

Disposition: **HOLD / FAIL-CLOSED**.

No gameplay, country, history, map, character, portrait, flag, idea, focus, decision, mission, AI, central admission, formable, localisation, or cleanup source was changed. No source-safe narrow repair was proven. This handoff is documentation only, as requested; nothing was staged or committed.

## Authority and review boundary

The reviewed design authority was:

- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`
- `docs/plans/006_independence_wave_plans/006_event6_first_footprint_admission_improvement_addendum_2026-08-26.md`
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`
- `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/events/006_independence_wave/systems/country_registry.md`

The required repository guidance and skills were read before review: `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-focus-trees/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, and `.agents/skills/chaos-redux-comfyui/SKILL.md`.

The offline Paradox wiki snapshot was consulted for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, State modding, National focus modding, Character modding, Cosmetic tag modding, Graphical asset modding, Map modding, Portrait modding, and Technology modding. Installed vanilla documentation was consulted under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, `modifiers_documentation.md`, `loc_formatter_documentation.md`, `loc_objects_documentation.md`, `script_collection_input.md`, and `script_collection_operator.md`.

## Package coverage checklist

| Surface | Current status | Evidence and exact path |
| --- | --- | --- |
| Identity and carrier | **Map/planner metadata present; Event 006 package content absent.** | `IW-108,Buganda,...,UGA,reuse_registered_tag,...,548,...,RG-GREAT-LAKES-COARSE` in `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:109` and `.../matrices/006_candidate_country_registry.csv:109`. |
| UGA carrier preservation | **Existing Event 012 carrier must remain authoritative.** | Event 012 origin/package predicates in `common/scripted_triggers/012_africa_priority_member_triggers.txt:33-35,288-295`; Event 012 origin is written by `common/scripted_effects/012_africa_priority_member_effects.txt:584-610`. No safe Event 006 overlay can be added without a separate accepted origin/package gate. |
| Anchor and reservation | **Present and coherent.** | Current binding fixes state `548` and host `ENG`, with Kampala VP `12989`, in `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:109`; reservation capacity-one group is `RG-GREAT-LAKES-COARSE` in `.../006_current_map_reservation_groups.csv:81`. |
| Former host | **Planner captures it; package lifecycle consumer absent.** | `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:2150-2153` saves state `548` owner as `liberation_candidate_primary_host`; no IW-108 setup/final/cleanup adapter consumes a former-host receipt. |
| Origin separation | **Event 012 owns the active UGA identity path; Event 006 origin path absent.** | Event 012 writes `africa_priority_origin_buganda` and `africa_priority_player_origin_buganda` in `common/scripted_effects/012_africa_priority_member_effects.txt:584-610`; dispatch preflight rejects active foreign origins in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:207-214`, but has no IW-108 admission branch. |
| Setup/effects | **Absent for IW-108.** | The package registry only loads planner metadata and publishes reservation state in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:2138-2154,2360-2367`. Central setup dispatch at `common/scripted_effects/006_independence_wave_effects.txt:3692-3720` has no IW-108 package setup call. |
| Forces and production | **Absent for Event 006; vanilla/012 carrier setup is not an Event 006 force profile.** | No `iw108`/`iw_108` package force effect, template, equipment, manpower, production, supply, or reinforcement consumer exists. The existing Buganda reinforcement action is Event 012 `africa_priority_buganda_reinforce_force` in `common/decisions/012_africa_priority_member_decisions.txt:481-496`, with shared Event 012 effects. |
| Visible ledgers and ideas | **Absent for Event 006; Event 012 has separate visible state.** | Event 012 starts `africa_priority_buganda_starting_problem` and later `africa_priority_buganda_mature_compact` in `common/scripted_effects/012_africa_priority_member_effects.txt:323-354`; its Buganda variables/flags are package-local to Event 012. No IW-108 ledgers, ideas, icons, or lifecycle exist. |
| Focus callbacks/tree | **Carrier focus exists only through Event 012.** | Event 012 loader/guard is `africa_priority_member_ensure_focus_tree_loaded` in `common/scripted_effects/012_africa_priority_member_effects.txt:586` and tree `africa_priority_member_focus_tree` in `common/national_focus/012_africa_priority_member_focus.txt`. No IW-108 callback IDs or additive Event 006 overlay are present. Shared Event 006 tree is generic only: `independence_wave_focus_tree` in `common/national_focus/006_independence_wave_focus.txt`. |
| Decisions/missions | **No Event 006 Buganda category, decision, mission, or timed objective.** | The only Buganda decisions found are Event 012 `africa_priority_buganda_advance_mechanic`, `africa_priority_buganda_reinforce_force`, and `africa_priority_buganda_post_settlement_action` in `common/decisions/012_africa_priority_member_decisions.txt:218-232,481-496,747-761`. |
| AI strategy | **No IW-108 package strategy or AI route.** | No `iw108`/`iw_108` match exists in package AI sources. Planner weight preparation only exists in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:2268-2277`; seeded zero weight is initialized at `common/scripted_effects/006_independence_wave_effects.txt:3529`. |
| Roster/leader/portrait | **Event 012 sovereign exists; Event 006 roster and portrait admission absent.** | `africa_priority_buganda_sovereign` is male and wired in `common/characters/012_africa_priority_member_characters.txt:71-78`, recruited by `history/general/012_africa_priority_member_character_recruitment.txt:24-27`, and rendered through `interface/012_africa_priority_member_characters.gfx:27-29`. This is not Event 006 ownership evidence and must not be copied into a new origin. |
| Flags | **No Event 006 Buganda flag family or provenance gate.** | Vanilla UGA ideology/base flag family remains the carrier baseline; no package-local UGA/Event 006 flag files or accepted provenance manifest were found. The research row requires reuse only when released identity/origin match and otherwise source review. |
| FORM-27 | **No Buganda member/consent/anchor adapter.** | `rg` found no IW-108 or Buganda FORM-27 member, consent, integration, cosmetic, or flag hook in the current Event 006 formable registries. The accepted research direction is only the Great Lakes Federation family; no Event 006 FORM-27 admission is proven. |
| Cleanup | **No IW-108 cleanup path.** | Central cleanup dispatch has no IW-108 adapter in `common/scripted_effects/006_independence_wave_effects.txt:3771-3797`; no package-local flags, ideas, ledgers, decisions, focus callbacks, role retirement, reunion, annexation, formable, or host-death cleanup exists. |
| Central attestation/preflight | **Absent; package cannot pass admission.** | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63` has no `independence_wave_package_id.iw_108`; content attestation at `:159-201` also has no IW-108. Preflight at `:207-214` requires both gates. |
| Central Join | **Absent.** | `common/scripted_effects/006_independence_wave_join_effects.txt:128-185,236-...` contains the dynamic package probe and Join route, but no IW-108 package ID branch or adapter. |
| SCN-008/capacity | **Ranked/visible in scenario bookkeeping only, not admitted.** | `common/scripted_effects/006_independence_wave_scenario_effects.txt:254` ranks `independence_wave_package_id.iw_108`, but the package remains absent from central adapter and attestation gates; rank-list membership is not admission. |
| Exact localisation | **Event 012 Buganda localisation exists; Event 006 package localisation absent.** | Event 012 keys such as `africa_priority_buganda_starting_problem`, `..._mature_compact`, `..._advance_mechanic`, `..._reinforce_force`, and `..._post_settlement_action` are present in `localisation/english/012_africa_priority_member_focus_l_english.yml:200-254` and `localisation/english/012_africa_priority_member_l_english.yml:54-56,102-104,150-...`. No `independence_wave_iw108_*` or `independence_wave_...buganda...` package keys exist. |

## File-surface checklist

The following Event 006 package-local surfaces are missing, not stale-but-fixable:

- country package definitions/history/roster: no IW-108-specific Event 006 files; registered tag `UGA` and vanilla/Event 012 history remain the carrier.
- package triggers/effects/constants: only planner metadata (`iw_108` constant, readiness trigger, loader, weight preparation, reservation publisher) exists in `common/script_constants/006_independence_wave_constants_registry.txt:7607`, `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:807-814`, and `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:2138-2153,2268-2277,2360-2367`.
- package values/visible ledgers/ideas: absent for Event 006.
- forces/templates/equipment/manpower/industry/supply: absent for Event 006.
- Event 006 Buganda leader, command roster, portrait manifest, portrait worker handoff, and final runtime asset: absent. The Event 012 portrait is source-locked and belongs to the Event 012 carrier path.
- Event 006 flag family, source/provenance manifest, and flag wiring: absent.
- package-local focus callback file, decisions/missions, AI strategy factors, formable adapter, exact localisation, and cleanup effects: absent.
- central adapter, attestation, preflight branch, setup/final-validation/cleanup dispatch, deterministic Join branch, and capacity registration: absent.

## Map and state setup

The installed-map binding is coherent for a dormant registered carrier. State `548` is the accepted compact Buganda/Uganda anchor, Kampala VP `12989` is present, and the planner records the current owner as former host `ENG` (`ENG` protected remnant evidence is `126` in the binding row). `RG-GREAT-LAKES-COARSE` is capacity one and also contains IW-109/IW-110/IW-111/IW-112; no second automatic package can reserve the same coarse anchor in one wave.

The read-only map inspection returned workspace `mod_chaos_redux_ea3b2d67c2c0`, code `MAP_INSPECTED`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c899569e58c75d97df412b8480ab95a1ce2a48ba14c8cbe300f7b199647e33b9/1a39ad681781e213911388a39ca1d664102fb3735886780180bf0d0aa023b6da/map-inspect.a3a978700b84ac21.json`, and map revision `a3a978700b84ac211db7ede802e4b3060012b85a02c130c0ff36f1555c06c8dd`. It inspected one requested state and passed state/region membership and adjacency/network checks; the workspace-wide map report also exposed unrelated existing `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics in `map/buildings.txt` and did not establish an IW-108 defect. The read-only map render returned `MAP_RENDERED` with state-layer artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/272d46998a7713e4167493ad7a4b4e6e450a67715c25c98a11a95fa3c5d475e0/fade5441a744757d6d764aa40dfa47a2a8486ad8ddae336174ff030dcb2251a4/map-state.png` and matching JSON/HTML artifacts.

Map evidence proves feasibility only. It does not prove identity, origin, host survival at runtime, forces, package readiness, or admission.

## Politics, leader, portrait, flag, advisor, and party issues

UGA is a reused registered carrier and must preserve vanilla identity/history until a valid Event 006 origin transaction owns it. Event 012 already installs the Buganda sovereign path, party names, route leaders, starting problem, mature compact, and Buganda-specific descriptions. The Event 006 package cannot copy or overwrite those consumers merely because both rows use `UGA`.

The Event 006 research row requires a sourced real male period leader when valid for the release date, otherwise archival material for the actual provisional institution; it explicitly blocks an undefended leader assignment. It also requires source review for historical flag variants and disallows treating generic vanilla ideology flags as Event 006 provenance. No IW-108 portrait-worker manifest, grounded source archive, runtime final DDS, role-specific wiring, flag provenance, or rights acceptance was found.

No Event 006 advisor, high-command, commander, or institutional roster exists. If the future package uses a Lukiiko, council, or other symbolic body, it must use an institutional name rather than a personal random-name pool. Any future portrait must route through `chaosx_portrait_creator`; no generated grounded leader or unreviewed Event 012 portrait reuse is accepted.

## Focus, decision, idea, and asset issues

The Event 006 shared tree is structurally available, but that is not a Buganda package. The read-only `hoi4.focus_inspect` for `common/national_focus/006_independence_wave_focus.txt` returned `FOCUS_INSPECTED`, tree `independence_wave_focus_tree`, 184 focuses, no blocking diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f821ffd6967de9928b2ef48821863dee4ece4a9fdd00dfc620d1cfa8d4b59fe1/eabdece7f4478bd3e234e4c0c29431afff459c3384221209dd9bd1defcad34f0/focus-inspect.2d040167557f5849.json`. Its render returned HTML/SVG/JSON/source-map/plan artifacts, including `independence_wave_focus_tree.focus.svg` SHA-256 `5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109`.

The Event 012 tree inspection for `common/national_focus/012_africa_priority_member_focus.txt` returned `FOCUS_INSPECTED`, tree `africa_priority_member_focus_tree`, eight focuses, no blocking diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2112a813080625ad8ca64a9333ce23c951a0f076b6870d63d81625b09a71ce78/f985141be535e6fff5f729dc78b8ae911cb76bd5bbb87ec7e36d1249d292065b/focus-inspect.2d040167557f5849.json`. Its render returned HTML/SVG/JSON/source-map/plan artifacts, including `africa_priority_member_focus_tree.focus.svg` SHA-256 `d7ff305dc7e966848d142e5205d6ca2e31f65741a62e46685d98d77c2aeeab52`. These are separate existing surfaces; neither supplies IW-108 Event 006 callbacks.

The Event 006 focus render carries two unrelated workspace warnings: one long connector in `006_independence_wave_focus.txt` and one vanilla generic-focus localisation warning. They are not assigned to IW-108.

No Event 006 Buganda decisions, missions, idea icons, focus icons, decision icons, or asset manifest exist. The existing Event 012 Buganda localisation and icons are not transferable across origins without an accepted overlay design.

## Starting military, technology, industry, supply, and production issues

The vanilla UGA history remains a basic carrier setup centred on state `548`, with basic infantry technology and no Event 006-specific OOB, template, manpower budget, equipment profile, production line, convoy reserve, train/fuel plan, supply adjustment, or reinforcement lifecycle. Event 012's Buganda reinforcement action is not an Event 006 military package. There is no safe narrow fix because the missing content requires accepted package design and package-owned force constants/effects.

The exposed technology routes were checked read-only. `hoi4.tech_inspect` scan returned `TECH_INSPECTED` in workspace `mod_chaos_redux_ea3b2d67c2c0`, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/17bb9ecdc497af718386bd6bf9d0c0bdd9da6e71ce8fdbe5081f342984fb7f51/cd54de505af5b12cc07ab130b445a86d64b5eeb51d23e73359fdc5ce99494783/technology-scan-13a4e28a716d.json`. It reported a workspace-wide 1,396 blocking technology diagnostics and did not identify an IW-108 technology defect. No standalone Technology Tree Viewer application was separately exposed or verified; the callable `hoi4.tech_inspect`/`hoi4.tech_render` routes are not evidence of a standalone viewer. Record standalone viewer availability as a package-validation gap.

## AI and playability issues

Planner readiness and weight preparation are present, but admission/readiness is not. `can_plan_independence_wave_package_iw_108` requires the release plan to be open, a free plan slot, no existing package/reservation-group collision, available dormant `UGA`, and an available anchor `548` at `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:807-814`. That trigger proves only planner eligibility.

The required probability pass was routed through the exposed read-only HOI4 probability route. Source discovery for `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` returned `PROBABILITY_SOURCE_DISCOVERED`, suggested adapter `random_list`, source revision `7ba35851afbc228ca63fc3f9dd510545c97912faf72dff69e1b820d694f8c86f`, source hash `17e35c209602f859bd3e5b71bd6b394aa613d7d8686e0d07f1d8ee3b803585e6`, and 126 available source candidates; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/799eeaa55d143ae1dbdd239b8df06fdad6414f27849b9055c37a982b906e21ad/0f8b51ad3a6ca0545cc0189bd9054ed2688394608bbfbe8dddb41b890bd32cf9/probability-inspect-17e35c209602.json`.

The focused `random_list` inspection of the region-10 selection entries `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:2424.entry.1` through `.entry.7` returned `PROBABILITY_SOURCE_INSPECTED`, pool complete with seven candidates and zero unresolved inputs, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bfe2d604db7562b77b8722590f6c17337f3e860a711a84c1e246287260e0b07a/9a80f9d016b20f437c9a9f4a28748cf745bd07624ea3e83e174336afc5b96169/probability-inspect-17e35c209602.json`. The adapter still exposed zero available candidates because the weights are dynamic planner variables; no normalized IW-108 selection probability, rank, threshold, or balance claim is made. A mistaken custom-pool probe with package weight names was also rejected as an incomplete six-input pool; it is not used as evidence of gameplay balance.

No owner-applied AI patch exists, so no `hoi4.probability_compare` is applicable. Named scenario evaluation, sweeps, and simulation remain unresolved until the package has an accepted strategy source, complete external-state manifest, and parent-owned balance scenarios. Do not tune IW-108 weight from the zero-initializer or planner metadata.

## Central admission, FORM-27, cleanup, and exact blockers

The central Event 006 boundary is intentionally fail-closed for IW-108:

1. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63` has no `independence_wave_package_id.iw_108` runtime adapter.
2. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-201` has no IW-108 content attestation.
3. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:207-214` requires both exact adapter and exact attestation, so IW-108 cannot pass preflight.
4. `common/scripted_effects/006_independence_wave_effects.txt:3692-3720` omits IW-108 setup dispatch; `:3724-3751` omits IW-108 final validation; `:3771-3797` omits IW-108 cleanup.
5. `common/scripted_effects/006_independence_wave_join_effects.txt` contains no IW-108 branch. Join must not bypass the admission boundary.
6. `common/scripted_effects/006_independence_wave_scenario_effects.txt:254` includes IW-108 only in a ranked registry, which is bookkeeping and not admission.
7. No IW-108 central capacity receipt, package-local capacity ledger, origin marker, or SCN-008 released-package attestation exists.
8. No accepted FORM-27 Great Lakes Federation member/consent/integration adapter exists for Buganda. The research direction is not an implementation authorization.
9. No cleanup path exists for annexation, voluntary reunion, host death, formable absorption, or generation retirement.

The absence of these surfaces is a package-content blocker, not a small tag-reference or focus-loading defect. Adding a central branch now would invent identity, roster, assets, mechanics, and admission evidence and would violate the requested boundary.

## Validation record

Completed meaningful read-only checks:

- Current-source search for `iw_108`, `iw108`, `UGA`, Buganda, FORM-27, Great Lakes, package setup/final/cleanup, Join, central attestation/preflight, visible ledgers, origin, and former-host references.
- Installed-map `hoi4.map_inspect` for state `548` and read-only `hoi4.map_render` with state/building/port/VP/resource/railway overlays.
- Read-only `hoi4.focus_inspect` and `hoi4.focus_render` for both `independence_wave_focus_tree` and `africa_priority_member_focus_tree`.
- Read-only `hoi4.event_inspect` and `hoi4.event_render` for Event 006 root `chaosx.nr6.2`; both returned partial global-workspace analysis with no blocking diagnostics, artifacts `event-scan-a8fde3e58546.json` and `event-overview-a8fde3e58546.*`. The partial result is structural evidence only; no IW-108 event-owned branch was found in source.
- Read-only `hoi4.tech_inspect` availability check and standalone-viewer availability check.
- Mandatory probability inspection through the exposed route, including source discovery and complete focused region-10 random-list pool inspection.
- Vanilla UGA country/state/history/character/flag references and relevant installed documentation review.

Skipped meaningful validation:

- No live game launch or user-owned live validation, per repository policy.
- No map rewrite: no map defect was proven and the parent scope forbids speculative map mutation.
- No technology render/compare for IW-108: no Event 006 technology surface exists to render; the standalone viewer was not separately available.
- No probability evaluate/sweep/simulate/compare: no accepted named IW-108 AI scenarios or owner-applied weight patch exist, and dynamic planner weights were unresolved by the adapter.
- No portrait/flag asset validation beyond source/runtime search: no Event 006 Buganda asset package or accepted provenance manifest exists to inspect.

## Changed files and identifiers

Changed files: none.

Changed tags, states, leaders, parties, focus IDs, localisation keys, formable IDs: none.

No plan handoff beyond this file was written. No commit was created.

## Next gates for parent review

IW-108 should remain outside Event 006 selectable/attested sets until the parent-owned design and admission tranche supplies all of the following:

- accepted UGA carrier/origin ownership decision that preserves Event 012 and prevents cross-event overwrites;
- package-local identity, sourced male leader/institution roster, portrait-worker evidence, and historical/alternate-history flag provenance;
- package setup, values, visible ledgers, ideas, forces, equipment/manpower/production/supply/reinforcement, AI strategy, exact localisation, and generation-safe cleanup;
- reviewed shared-tree/additive overlay callbacks and package decisions/missions with real route effects;
- host remnant, former-host settlement, capacity/attestation, preflight, final-validation, Join, SCN-008, FORM-27, and cleanup wiring;
- baseline probability inspection plus named scenario evaluation, and a same-scenario `hoi4.probability_compare` only after any owner-applied weight change;
- fresh package-local country audit and parent acceptance before adding `iw_108` to central adapter/attestation lists.

Until those gates are accepted, the safe behavior is the current one: planner metadata may identify the dormant `UGA` carrier and reserve `548` under `RG-GREAT-LAKES-COARSE`, but Event 006 must not create, mutate, admit, or expose Buganda gameplay.
