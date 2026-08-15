# IW-036 Courland (BJX) country-package scaffold audit — 2026-08-12

## Disposition

IW-036 remains fail-closed and is not viable for admission. This was a read-only country-package crosswalk; no gameplay, asset, localisation, registry, attestation, readiness, history, or central-dispatch files were changed. The existing dormant shell and Region-04 planner wrapper are the only safe current scaffolding.

The bounded implementation plan remains queued at `docs/plans/006_independence_wave_plans/006_iw036_courland_plans/006_iw036_courland_bounded_implementation_plan.md`. Do not promote BJX from registry, reservation, or random-pool membership alone.

## Country-package coverage checklist

| Surface | Current result | Exact evidence / blocker |
| --- | --- | --- |
| Tag registration and collision | Partial / static pass | `common/country_tags/006_independence_wave_countries.txt:30` registers `BJX = "countries/006_independence_wave_BJX.txt"`; `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:43` lists `original_tag = BJX`. `python -B .tools/audit_chaosx_country_tags.py` reports 136 protected tags, 0 external country-definition collisions, 0 external identity-surface collisions, and 1 intentionally skipped Random Events root. This does not clear package readiness or excluded surfaces. |
| Country shell/history | Dormant partial | `common/countries/006_independence_wave_BJX.txt:1-9` owns only graphical cultures and map colour. `history/countries/BJX - Courland.txt:1-15` sets neutral/no-election loading only; it has no capital, OOB, technology, production, characters, or runtime lifecycle. |
| Localisation | Base-only partial | `localisation/english/006_independence_wave_countries_l_english.yml:241-256` supplies BJX/Courland/Curonian names for all four ideology keys. No IW-036 route, party, institution/leader, advisor, idea, decision, focus-hook, or dynamic host/territory keys exist. |
| Current map anchor | Static candidate pass; runtime evidence unavailable | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:37` binds IW-036 to state `190` Kurzeme, `190=LAT`, host capital `LAT=808`; vanilla `history/states/190-Kurzeme.txt` contains six provinces `3194 3296 3319 6322 9262 11246`, owner/core LAT, VP 9262/3296, naval base and dockyard. The required current `hoi4.map_inspect` and `hoi4.map_render` calls returned `ARTIFACT_MANIFEST_INVALID` before scanning, so the earlier 2026-08-10 artifacts are historical evidence only. |
| Host survival / Event-005 conflict | Blocked for admission | State 808 Riga is Latvia's capital in vanilla `history/states/808-Riga.txt`; state 190 is separate, but `common/scripted_triggers/006_independence_wave_package_triggers.txt:9-18` proves only owner/controller/Soviet/reservation/protected-state conditions. A BJX package still needs a final LAT-remnant proof and the exact Event-005 footprint/conflict guard. |
| Reservation group | Planner-only partial | `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:67` places IW-034/IW-035/IW-036 in `RG-BALTIC-LIVONIA`; the group allows at most one automatic package and protects host states. `common/scripted_triggers/006_independence_wave_packages_region_04_triggers.txt:28-35` and `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt:41-50,122,145,154` provide only candidate planning, weighting, and state-190 reservation. |
| Identity / institutions | Unresolved | `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:37` requires a period royal/customary/historical institution bridged to a provisional assembly/cabinet/municipal administration with veterans, schools, labour, and mixed-population rights/autonomy routes. No institution, community roster, or route baseline has been selected in gameplay source. |
| Leaders, advisors, commanders, portraits | Blocked | No BJX-specific `common/characters`, `common/country_leader`, `gfx/leaders`, or portrait-wiring files exist. The research gate requires a sourced male officeholder or authentic institutional material; generated personal portraits are forbidden for this grounded regional identity. Portrait work belongs to `chaosx_portrait_creator` only after identity selection. |
| Flags and symbols | Present but provenance-blocked | BJX base/ideology TGA ladders exist under `gfx/flags/BJX*.tga`, `gfx/flags/medium/BJX*.tga`, and `gfx/flags/small/BJX*.tga`, but `docs/plans/006_independence_wave_plans/asset_research/006_generated_flag_blockers.md:23` and `006_package_asset_coverage.md:110` keep IW-036 blocked pending exact symbol owner/date/function/route/licence review. Existing TGAs must not be promoted as attested assets. |
| Politics / parties / laws | Blocked | Dormant neutrality is only a parser-safe loader. No BJX party names, popularity, elections/laws, route leader, stability/war-support, diplomacy, or cleanup semantics exist. |
| Focus | Blocked; shared tree only | `common/national_focus/006_independence_wave_focus.txt:34-42` defines shared `independence_wave_focus_tree` with an active-country gate. No BJX package assignment or route hooks exist. Required current `hoi4.focus_inspect`/`hoi4.focus_render` calls failed with `ARTIFACT_MANIFEST_INVALID`; no BJX node can be validated. |
| Decisions / missions / ideas | Blocked | No IW-036 decision category, paid project, mission, idea lifecycle, icon, or cleanup file exists. The only three BJX hits at `common/decisions/006_independence_wave_iw043_iw058_decisions.txt:770,1450,1819` are generic country target lists, not Courland content. |
| Forces / industry / supply | Blocked | `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:37` specifies coastal guards and territorial infantry, `coastal_maritime`, military identity 49, with engineers/recon/coastal signals and port-depot assumptions. No IW-036 setup effect maps it to templates, stockpiles, manpower, production, port, supply, or reinforcement/cleanup. |
| Technology | Unresolved limitation | No custom BJX technology exists. The installed package exposes no Technology Tree Viewer; if custom technology is later proposed, a separate technology audit route is required. |
| AI / playability | Blocked and quantitatively unresolved | No IW-036 `common/ai_strategy` file exists. Region-04 contains IW-036 in the `random_list`, but no survival strategy or package score is implemented. The required current `hoi4.probability_inspect` random-list call also returned `ARTIFACT_MANIFEST_INVALID`; no numeric probability or balance claim is made. |
| Formable / Baltic route | Blocked | The generic Baltic Federation metadata and state-puzzle references are not a BJX adapter. `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:116-166,551-629` has no Baltic founding-carrier/readiness/commit branch. State 190 alone cannot prove formation. |
| Event / network / cleanup | Blocked | Root Event 006 exists, but no IW-036 opening/setup receipt, actor/event-log mapping, host settlement, route decision, network registration, final validation, or generation-safe cleanup exists. Central dispatch remains unchanged: `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-38,42-83,85-110` has no IW-036 setup/final-validation/cleanup wrapper; `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-58,142-181,187-360,370-526` has no IW-036 adapter, attestation, normal preflight, or scenario-preflight branch. |

## File-surface crosswalk

Existing, safe-to-preserve surfaces:

- `common/country_tags/006_independence_wave_countries.txt:30` — BJX tag registration.
- `common/countries/006_independence_wave_BJX.txt` — graphical culture and colour shell only.
- `history/countries/BJX - Courland.txt` — dormant neutral loader only.
- `localisation/english/006_independence_wave_countries_l_english.yml:241-256` — base country names/adjective.
- `common/script_constants/006_independence_wave_package_constants.txt:87` — package id `iw_036 = 36`.
- `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:43` — registry membership.
- `common/scripted_triggers/006_independence_wave_packages_region_04_triggers.txt:28-35` — planner availability predicate.
- `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt:41-50,122,145,154` — planner load/weight/reservation/random-list entry.
- `common/scripted_effects/006_independence_wave_scenario_effects.txt:265` — scenario ranking membership.
- `gfx/flags/BJX*.tga`, `gfx/flags/medium/BJX*.tga`, `gfx/flags/small/BJX*.tga` — existing but provenance-blocked flag family; no promotion is authorized.
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:37`, `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:37`, `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:37` — research and force design inputs.

Missing package-owned surfaces that must remain absent until gates close:

- `common/scripted_effects/006_independence_wave_*iw036*` setup/final-validation/cleanup/force helpers.
- `common/scripted_triggers/006_independence_wave_*iw036*` active/final host, identity, roster, and Event-005 conflict checks.
- `common/characters/*iw036*`, `common/ai_strategy/*iw036*`, `common/ideas/*iw036*`, `common/decisions/*iw036*`, decision categories, focus-hook effects/localisation, and package-specific events.
- Central adapter/attestation/preflight branches in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` and wrappers in `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`.
- Baltic Federation family adapter, member/readiness/commit proof, route cosmetics, and cleanup.

## Research, wiki, and vanilla references consulted

- Offline wiki: `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, `AI modding - Hearts of Iron 4 Wiki.md`, `Country creation - Hearts of Iron 4 Wiki.md`, `National focus modding - Hearts of Iron 4 Wiki.md`, `Character modding - Hearts of Iron 4 Wiki.md`, `State modding - Hearts of Iron 4 Wiki.md`, and `Portrait modding - Hearts of Iron 4 Wiki.md`.
- Vanilla documentation: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, and `loc_objects_documentation.md`.
- Vanilla precedents: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/Latvia.txt`, `history/states/190-Kurzeme.txt`, `history/states/808-Riga.txt`, `common/national_focus/latvia.txt`, and `common/on_actions/07_nsb_on_actions.txt` (Baltic capital restoration and focus-tree loading patterns).

## Required MCP evidence and exact current blocker

Fresh required read-only calls in workspace `mod_chaos_redux_ea3b2d67c2c0` were attempted for:

- `hoi4.map_inspect` on states 190/808/195/12/191 and Kurzeme provinces, plus `hoi4.map_render`;
- `hoi4.focus_inspect` and `hoi4.focus_render` for `independence_wave_focus_tree`;
- `hoi4.event_inspect` and `hoi4.event_render` for `chaosx.nr6.1`;
- `hoi4.probability_inspect(adapter=random_list, source={path: common/scripted_effects/006_independence_wave_packages_region_04_effects.txt})`;
- `hoi4.tech_inspect(mode=folders)`.

Every call failed before source scanning with the exact response `ARTIFACT_MANIFEST_INVALID — Artifact provenance manifest is invalid`; no current artifact URI, source revision, map record, focus graph, event graph, or probability result was produced. This is a tooling/provenance blocker, not evidence of package readiness. Historical artifacts in `006_iw036_courland_preflight_2026_08_10.md` remain useful context but are not current post-change MCP proof.

The installed package still exposes no Technology Tree Viewer. No custom technology was added.

## Static validation performed

- `python -B .tools/audit_chaosx_country_tags.py` — 136 protected Event 006/Soviet tags; 0 external definition collisions; 0 external identity-surface collisions; 1 intentionally skipped Random Events root.
- `python -B .tools/audit_event6_allocator.py` — allocator audit passed; 149 publishers; 29 attested packages; 26 compatible reservation groups; no change to IW-036 disposition.
- Direct source crosswalk confirmed no BJX/Courland/IW-036 character/portrait, AI, or package-specific idea/decision files; the three decision hits are generic country target lists only.

## Safe next steps / blockers

1. Resolve the identity and symbol dossier, select the provisional institution and any sourced male/institutional portrait package through `chaosx_portrait_creator`, and clear flag provenance before adding package-visible assets or names.
2. Obtain the exact Event-005 footprint and add final host-remnant/conflict proof before any owner-transfer setup.
3. Implement the package lifecycle, force mapping, shared-tree assignment, decisions/ideas, AI, host settlement, and Baltic family adapter as one bounded package tranche; do not grant `independence_wave_package_content_ready` as a shortcut.
4. Repair/regenerate the HOI4 MCP artifact provenance manifest, then rerun map/focus/event/technology/probability inspections and retain current artifact URIs. Route all weighted surfaces through `chaosx_ai_probability_auditor` with named scenarios and later `hoi4.probability_compare`.
5. Only after those gates pass may the parent add central adapter, attestation, normal/scenario preflight, and final-validation/cleanup branches.

No simplification or fallback was used. No gameplay or runtime behavior changed.
