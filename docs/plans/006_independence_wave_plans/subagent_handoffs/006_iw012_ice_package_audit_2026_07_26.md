# Event 006 IW-012 Iceland country-package audit

## Scope and verdict

This audit covers the installed-map Iceland package (`IW-012`, resolved tag `ICE`, reservation group `RG-100`, anchor state `100`) and the smallest safe Event 006 integration that preserves vanilla Iceland content.

Verdict: **HOLD; not content-ready and not admitted to the runtime pool.** `RG-100` is a valid unique reservation group on the current map, so a fully attested IW-012 package could provide the missing tenth compatible group for the ten-country capacity band. The current repository has only a candidate/reservation shell and a scenario ranking entry; it does not have an executable ICE adapter, final validation/cleanup path, or content attestation.

The safe design is an additive non-focus overlay. ICE must retain the vanilla `iceland_tree`, `ICE_personal_union`, DLC-aware history, existing characters, and dedicated AI plans. Do not call `load_focus_tree = independence_wave_focus_tree` for ICE. A visible Event 006 focus branch would require a separate, version-sensitive static design for `common/national_focus/iceland.txt`.

## Country package coverage checklist

| Surface | Status | Evidence and finding |
|---|---|---|
| Tag and identity | PASS for vanilla identity; FAIL for Event 006 admission | Vanilla `ICE` is registered in `common/countries/Iceland.txt` and `history/countries/ICE - Iceland.txt`. `ICE` appears in the Event 006 candidate registry, but no exact IW-012 runtime identity wrapper or adapter exists. |
| Reservation group | PASS on paper; HOLD at runtime | `RG-100` reserves state `100` for IW-012 in `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv:3`. The row requires a non-living tag and a successful host-remnant test. |
| Candidate trigger | BLOCKED/stale | `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt:89-96` calls `ICE = { is_independence_wave_candidate_tag_available = yes }`. That shared trigger also requires `independence_wave_package_content_ready`, but no ICE history or adapter sets that flag; the repository explicitly says accepted packages do not set it (`common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:11`). |
| Runtime readiness | MISSING | `can_plan_independence_wave_package_iw_012` references undefined `is_independence_wave_runtime_automatic_package_iw_012_ready`. Definitions exist for IW-001/002/004/006/007/008/009/010/017/018/019/184 in `common/scripted_triggers/006_independence_wave_triggers.txt:405-513`, but not IW-012. |
| Host and anchor safety | Partial | State `100` is Iceland's capital, sole owner/core, and protected host footprint. `history/states/100-Iceland.txt:1-28` confirms owner/core `ICE`, capital anchor, port, dockyard, and industry. The current IW-012 trigger only checks generic anchor availability and does not provide the package-specific host-survival witness required by the map binding. |
| Politics and laws | Vanilla only | Vanilla history starts democratic with 96/2/2 popularity, stability 0.65, and DLC-conditional `disarmed_nation`/`isolation` or `civilian_economy` setup. No Event 006 ICE politics, law, route, or cleanup adapter was found. |
| Leaders and characters | Vanilla roster available; Event 006 consumer missing | AAT recruits a broad real-character roster in `history/countries/ICE - Iceland.txt:97-126` from `common/characters/ICE.txt`; non-AAT dated history creates a smaller leader set. No IW-012 setup effect selects a date-valid leader, institutional body, commander, or advisor without duplicate recruitment. |
| Portraits and names | Vanilla coverage only | Vanilla ICE flags and leader portraits exist. No Event 006 ICE portrait/leader asset package, manifest, or localisation was found. Any alternate route must use a sourced real male period leader or authentic institutional material, with no opposite-gender pool pairing. |
| Focus tree | Preserve | `common/national_focus/iceland.txt:9-24` defines `iceland_tree`, about 89 ICE focuses, and `shared_focus = NORDIC_form_joint_alliance`. Event 006's shared focus blocks are detached from this tree. |
| Decisions and missions | Generic framework only | `common/decisions/006_independence_wave_decisions.txt` contains shared Event 006 decisions gated by `is_independence_wave_active_country`, but no ICE-specific visibility, route actions, or package cleanup exists. |
| Ideas and lifecycle | Vanilla only | Vanilla ideas and the AAT `ICE_the_icelandic_economy_modifier` are present in history. No IW-012 idea lifecycle, starting spirit, icon, or removal contract exists. |
| Formables and ambitions | Collision policy required | Event 006 FORM-02 North Atlantic Compact already recognizes `ICE`/state `100` in `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt:26-49,146-179,248-273` and transfers the ICE anchor in `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt:255`. Vanilla `form_nordic_league` also allows `original_tag = ICE` and cores state `100` (`common/decisions/formable_nation_decisions.txt:137-249,420-423`). An ICE adapter needs an explicit collision/precedence policy. |
| Military setup | Generic force profile exists; country adapter missing | `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:13` defines IW-012 as `coastal_maritime`, tradition `45`, patrol craft/coastal guards/foreign volunteers, and no air inheritance. Vanilla `history/units/ICE_1936.txt:1-37` defines the Ríkislögreglan template and production only; no fielded division exists, so runtime materialization is mandatory. |
| Technology, industry, and supply | Vanilla baseline available | Vanilla has two research slots, 30 convoys, infantry/support/recon and DLC-conditioned air/naval technology, one dockyard/naval base, and one industrial complex. The adapter must inherit/validate this baseline without duplicating dated history or inventing stockpiles. |
| AI | Preserve and extend narrowly | `common/ai_strategy/ICE.txt` and `common/ai_strategy_plans/ICE_historical_strategy_plan.txt` plus `ICE_alternate_strategy_plan.txt` are dedicated to `original_tag = ICE`. No Event 006 origin-aware AI weights or decision strategy exists. |
| Localisation and assets | Generic Event 006 only | Vanilla country, party, focus, decision, idea, and flag localisation exists. No `independence_wave_ice_*` localisation, icon, decision sprite, report art, portrait manifest, or flag variant was found. |
| Runtime dispatch | MISSING | `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-52` dispatches nine package families and has no ICE/region-01 setup, final-validation, or cleanup call. |
| Runtime admission | MISSING | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-159` omits IW-012 from adapter, content-attestation, and exact tag preflight lists. Scenario preflight at `:168-247` also omits it. |
| Automatic capacity | MISSING | `common/scripted_triggers/006_independence_wave_triggers.txt:593-952` has capacity tries through IW-010 and then IW-017/018/019/184; no IW-012 try or selected `RG-100` row exists. |
| Scenario registry | Stale listing | `common/scripted_effects/006_independence_wave_scenario_effects.txt:184` ranks IW-012, but the scenario dispatch gate cannot execute it because the attestation and exact package preflight entries are absent. |

## File surface checklist

### Existing source and authoritative records

- `common/countries/Iceland.txt` defines the vanilla ICE graphical identity and colour.
- `history/countries/ICE - Iceland.txt` owns the capital, OOB, slots, convoys, ideas, technology, DLC branches, economy variables, and character recruitment.
- `history/states/100-Iceland.txt` is the sole state owner/core and capital anchor.
- `history/units/ICE_1936.txt` supplies the Ríkislögreglan template and production but no fielded division.
- `common/characters/ICE.txt` provides AAT leaders, advisors, service chiefs, and commander roles.
- `common/national_focus/iceland.txt` provides `iceland_tree` and the Nordic shared focus.
- `common/ai_strategy/ICE.txt`, `common/ai_strategy_plans/ICE_historical_strategy_plan.txt`, and `common/ai_strategy_plans/ICE_alternate_strategy_plan.txt` provide dedicated AI behavior.
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:13` and `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:13` resolve IW-012 to `ICE`, state `100`, `RG-100`, `automatic_pool_ready_if_not_living`, North Atlantic Compact, and a sourced-leader requirement.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:13` records `100=ICE`, `ICE=100`, fixed compact anchoring, and explicit host-erasure rejection.
- `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:13` defines the existing generic force mapping for IW-012.

### Missing or stale package surfaces

- Add a bounded region-01/ICE setup effect and trigger file or equivalent named blocks, rather than changing vanilla country/history files.
- Define `is_independence_wave_runtime_automatic_package_iw_012_ready` and an exact `IW-012`/`ICE` identity wrapper that uses the shared runtime preflight contract.
- Replace the stale `is_independence_wave_candidate_tag_available` gate in the IW-012 planner row with the same runtime readiness contract used by admitted packages, after content attestation is complete.
- Add IW-012 to the adapter, content-attestation, exact tag preflight, scenario preflight, automatic capacity, and dispatch setup/final-validation/cleanup registries only after the package surfaces below are complete.
- Add ICE-specific runtime setup for identity/provenance, political route, ideas, command roster, force materialization, route/formable hooks, and cleanup.
- Add ICE-specific decisions/missions, ideas, icons, localisations, AI weights, and asset manifests, or document an explicit decision to use shared surfaces only.
- Add current-map/host-survival receipts and a post-wire reservation/transaction proof before promotion.

## Map and state setup issues

The current map binding is safe as a compact anchor only when state `100` is not protected by another release and the living ICE host is not erased. State `100` contains the Icelandic capital, seven provinces, a naval base, dockyard, industrial complex, and ICE core. It is also the host's only state in the 1936 baseline. The binding therefore correctly says to skip/reject when the protected-capital rule applies and to reject any release that would consume the host's sole state.

The region-01 planner currently checks only `100 = { is_independence_wave_candidate_anchor_available = yes }`, which proves owner/control and generic reservation/protection status but not the full former-host remnant policy. The future runtime witness must prove that the host survives with a valid capital or explicitly fail closed before the state transfer. No map rewrite is authorized or needed for the current IDs; the installed state-history audit found no Chaos Redux override for state `100`.

## Politics, leader, portrait, flag, advisor, and party issues

Vanilla ICE already has a coherent democratic identity, AAT/non-AAT conditional politics, party names, flags, cosmetic tag, and period-character roster. Reusing that identity is the lowest-risk path. Do not add a second ICE country definition, duplicate party set, or dormant history package.

The AAT roster contains Hermann Jónasson, Gísli Sigurbjörnsson, Brynjólfur Bjarnason, Sveinn Björnsson, Ólafur Thors, advisors, three service-chief roles for Agnar Eldberg Kofoed-Hansen, and corps commander Björn Sveinsson Björnsson. Non-AAT history creates Sveinn Björnsson, Johannes Valurson, Haraldur Gudmunsson, and Einar Olgeirsson on dated branches. An Event 006 setup must select only a valid, not-already-active consumer for the release date and DLC state, or use an authenticated institutional provisional authority. It must not recruit a duplicate named leader or infer a leader from a generic/random opposite-gender pool.

Vanilla flags are complete at `gfx/flags/ICE.tga`, `ICE_communism.tga`, `ICE_fascism.tga`, and `ICE_neutrality.tga` with corresponding medium/small variants. No Event 006 ICE flag or portrait package is present. Any alternate constitutional, emergency, or high-chaos identity requires source review and a new manifest before wiring.

## Focus, decision, idea, and asset issues

ICE's dedicated `iceland_tree` is meaningful and includes Nordic shared content. The shared Event 006 focus framework explicitly treats additive modes as no-`load_focus_tree` paths (`common/scripted_effects/006_independence_wave_focus_effects.txt:25-57`). The existing ICE tree does not contain `independence_wave_overlay_take_stock_of_independence`; therefore the package must expose Event 006 mechanics through decisions and scripted ledgers while retaining vanilla focus progress. A visible overlay branch needs a separate static proposal and review.

The generic Event 006 decision category can be reused once the country receives `independence_wave_active_origin` and complete package setup flags. At present no ICE package-specific trigger, decision, mission, effect, cleanup, or localisation file exists. The package must decide which shared government, host, league, North Atlantic, patron, and military actions are visible to a one-state island and give every visible choice trigger/effect text.

Vanilla ICE ideas should remain intact at release, including DLC-conditional `ICE_the_icelandic_economy_modifier`. Any Event 006 starting weakness or lifecycle idea must have an ICE-specific icon, localisation, install/remove timing, and cleanup proof. No such package-specific idea or asset is currently present.

FORM-02 already names ICE as a North Atlantic member and transfers state `100` during full integration. Vanilla `form_nordic_league` also accepts ICE and cores state `100`; the adapter must prevent duplicate authority, duplicate coring, or stale invitation flags when the Event 006 origin is active. The existing ICE condition in `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt:255` is a dependency to preserve, not a replacement for the package adapter.

## Starting military, technology, industry, supply, and production issues

The generic force profile is already specified as `coastal_maritime` with tradition `45`, patrol craft/coastal guards/foreign volunteers, navy inheritance enabled, air inheritance disabled, and reinforcement paths for militias, volunteers, foreign arms, league cadres, and capital/border defence. Generic force constants contain a `p12` row, so the missing work is not inventing a new force profile; it is proving and applying the profile in an ICE setup adapter.

Vanilla ICE starts with two research slots, 30 convoys, infantry/support/recon technology, DLC-conditioned early air/naval technology, and the `ICE_1936` OOB. The OOB has no fielded division, only the Ríkislögreglan template and two production lines. Event 006 must materialize a playable opening force and equipment/manpower/reinforcement path through the existing generic runtime effects. Do not add a static Event 006 OOB or duplicate vanilla production in history.

State `100` has one dockyard/naval base and one industrial complex, so coastal supply and fuel/convoy dependency must be part of the package balance and AI proof. The foreign-volunteer corridor and any navy inheritance must remain conditional on diplomacy and actual equipment access rather than free stockpiles.

## AI and playability issues

Preserve `ICE_avoid_joining_baddies`, its reverse check, `ICE_historical_plan`, and the three alternate plans. Add only origin-aware Event 006 strategy weights and decision preferences after the package flags exist. The AI needs a one-state survival plan that values capital control, convoy/port security, volunteer corridor access, and host pressure without blindly selecting vanilla Nordic or Event 006 formable content.

Required playability proof must cover a returned ICE retaining `iceland_tree`, dedicated AI, valid DLC/non-DLC roster, cosmetic identity, and vanilla Nordic content while gaining the additive Event 006 decisions and force system. It must remain ineligible while the standard-start ICE is alive, and no release may erase the former host's sole protected state. The AI must also avoid duplicating or corrupting Scottish/Welsh communist-uprising decisions in states `121` and `122`, as called out by the implementation map.

## Safe additive-overlay admission plan

1. Add an exact IW-012 runtime readiness trigger that sets package ID `12`, proves `original_tag = ICE`, calls `is_independence_wave_runtime_package_preflight_ready`, checks anchor `100`, and proves the host-remnant/protected-capital condition.
2. Add a named ICE/region-01 setup adapter that initializes the shared Event 006 origin, politics, ideas, force mapping, command consumer, route/formable policy, and origin-aware AI without replacing `iceland_tree` or vanilla history.
3. Add final validation and cleanup for every ICE-specific variable, flag, idea, decision, mission, character assignment, and formable invitation. Keep the generic force mapping and shared ledgers as the source of truth.
4. Complete DLC/date/portrait/source checks, localisation, icons, manifests, and package-level static audit before adding IW-012 to the adapter/content-attestation/exact-tag lists.
5. Add IW-012 to automatic capacity and scenario dispatch only after a dry-run/review/apply/post-validation cycle proves state `100` reservation, host survival, disjoint `RG-100` allocation, and synchronized transaction rollback/commit behavior.
6. Reconcile FORM-02 North Atlantic Compact with vanilla `form_nordic_league` and the ICE Nordic shared focus before any route is marked complete.
7. Keep the whole Event 006 ten-country claim fail-closed until this package is admitted and the resulting ten compatible reservation groups are proven live. `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:244-247` still records the current nine-group blocker because IW-008 and IW-010 share `RG-RHINE-SAAR`.

## Validation performed

- Read the required Chaos Redux subagent, event, focus-tree, and decision/mission skills before auditing.
- Consulted the required offline Paradox wiki pages and the relevant vanilla HOI4 documentation for country creation, triggers/effects, focus trees, decisions, ideas, AI, state ownership, and `load_focus_tree`/release behavior.
- Inspected the installed vanilla ICE country, history, state, OOB, focus, character, AI, flag, party, and formable sources.
- Ran targeted repository searches for IW-012/ICE runtime adapters, readiness triggers, force maps, dispatch hooks, focus loading, decisions, ideas, localisation, portraits, flags, and manifests.
- Confirmed no Chaos Redux gameplay file was changed by this audit. No in-game execution, live reservation, save/load, or map-write validation was performed; those checks remain parent-owned and are required before admission.

## Changed files

- Added `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw012_ice_package_audit_2026_07_26.md`.
- No country, state, focus, decision, event, AI, localisation, asset, or runtime script was patched.

## Simplifications, omissions, and blockers

- No fallback country tag, copied focus tree, invented leader, generated portrait, replacement flag, or static Event 006 OOB was added.
- IW-012 remains incomplete and must not be described as automatically selectable or runtime-ready.
- The undefined readiness trigger and the stale candidate-content flag gate are concrete wiring defects, not a balance choice.
- The host-survival receipt, ICE-specific setup/final-validation/cleanup, package content attestation, DLC/date leader proof, Nordic/formable collision policy, localisation/assets, AI weights, and live reservation/transaction evidence remain outstanding.
- A visible Event 006 focus branch for ICE is intentionally not included; it requires explicit static integration design authority.
