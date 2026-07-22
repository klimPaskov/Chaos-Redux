# IW-007 Frisia (AGX) post-wire country-package re-audit — 2026-07-22

## Scope and verdict

This is a fresh country-package audit after portrait retry-02 was wired. The audit covers the AGX tag, state anchor and host safety, politics and characters, portraits and flags, ideas and values, focus loading, decisions and mission, formable integration, dynamic force and technology setup, AI, localisation, cleanup, and dormant/Event 005 collision behavior.

**Country-package verdict: PASS.** No AGX-specific gameplay, identity, asset, localisation, focus, decision, map, or cleanup defect was found.

**Runtime admission verdict: BLOCKED by a parent-owned gate only.** `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:42-44` currently makes `has_independence_wave_runtime_package_content_attestation_for_execution_id` true only for `constant:independence_wave_package_id.iw_004`. The IW-007 wrappers are present (`:14-16`, `:66-76`, `:151-160`), but this checkout must not be treated as runtime-promotable until the parent adds IW-007 to that compile-time attestation and performs the parent admission review. This is not an AGX country-package defect, and I did not edit the attestation.

Promotion recommendation to `/root`: after the parent-owned attestation change, promote IW-007/AGX. Do not promote the current checkout before that gate is updated.

## Authority and evidence reviewed

- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` row 8 (`IW-007`, `Frisia`, `AGX`, state 36, `RG-36`).
- `docs/specs/006_independence_wave_specs/matrices/006_state_anchor_and_reservation_groups.csv` row 30 (`RG-36`, Friesland/state 36).
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` row 8 (`ready_unique_state_confirmed`, `36=HOL`, host remnant required).
- `docs/events/006_independence_wave/northern_western_europe_packages.md` Frisia contract (Kalma, Reenalda, three government routes, waterline project, North Sea conference, Low Countries formable, cleanup and AI requirements).
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/frisia_retry_02/manifest.md` (approved wired runtime portrait targets and SHA-256 hashes).
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_frisia_retry_02_independent_visual_audit_2026_07_22.md` (commit `c9712459c`, independent visual PASS for both selected portraits; candidate-01 blocked).
- Required offline Paradox wiki pages and vanilla HOI4 documentation were consulted before inspection: data structures, triggers, effects, modifiers, localisation, scopes, on actions, event/decision/idea/AI modding, country creation, national focuses, technology, states, portraits, graphical assets, and the corresponding vanilla documentation files.

## Country-package coverage checklist

| Surface | Evidence | Result |
| --- | --- | --- |
| Tag registration and identity | `common/country_tags/006_independence_wave_countries.txt:17` registers `AGX` as IW-007; `common/countries/006_independence_wave_AGX.txt` defines the western-European map identity and `rgb { 48 116 170 }`. | PASS |
| History and starting setup | `history/countries/AGX - Frisia.txt` starts `civilian_economy`, `export_focus`, `volunteer_only`, recruits `AGX_friesland_coastal_council` and `AGX_friesland_coastal_commander`; no static OOB/production conflicts with the documented dynamic-force layer. | PASS |
| Anchor, owner, controller, core, capital | Vanilla `history/states/36-Friesland.txt` starts `owner = HOL`, `add_core_of = HOL`; IW-007 preparation and proof require AGX to own/control state 36 and capital state 36. | PASS |
| Host remnant and release safety | IW-007 preparation requires the former host to exist and not be ROOT; package release transfers only the frozen anchor through the execution path. HOL retains its other states. | PASS |
| Politics and parties | `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:216-363` initializes the four base party names, promotes Kalma, and provides constitutional, popular-council, and patron-harbor route effects. No AGX emergency/traditional/radical route is falsely enabled. | PASS |
| Leaders, commander, portraits | `common/characters/006_independence_wave_wallonia_frisia_characters.txt:81-126` defines the two male characters and commander traits; history recruits both. No opposite-gender pool, female metadata, or institutional-name mismatch. | PASS |
| Flags and country art | `gfx/flags/AGX.tga` and medium/small derivatives exist; the flag is a valid RGBA TGA. AGX country identity uses the existing registered palette. | PASS |
| Ideas and values | `common/ideas/006_independence_wave_wallonia_frisia_ideas.txt:111-167` defines `agx_exposed_waterline`, `agx_dike_and_coast_authority`, `agx_constitutional_water_board`, `agx_coastal_labor_councils`, and `agx_patron_harbor_mandate`; all are AGX-gated and have registered generic sprites. Waterline and coastal-security values use shared constants. | PASS |
| Focus assignment and routes | `common/scripted_effects/006_independence_wave_focus_effects.txt:35-43` loads `independence_wave_focus_tree` for full mode; `common/scripted_triggers/006_independence_wave_focus_triggers.txt:32-42` gates full versus additive mode; `common/national_focus/006_independence_wave_focus.txt:25` supplies the tree and AGX route gates. The full tree contains 190 focus IDs and AGX prepared proof requires the full-framework flag and assignment. | PASS |
| Decisions and mission | `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:309-607` provides `independence_wave_agx_hold_the_waterline` (540-day mission) plus pump, harbor watch, rail, dike guards, records, three route-government, and North Sea conference decisions. Visible/available/cancel/timeout effects, costs, tooltips, and AI weights are present. | PASS |
| Formable integration | `common/scripted_triggers/006_independence_wave_form03_triggers.txt:32-53,202-228` requires the exact AGX state-36 anchor, capital, readiness adapters, reserved X tag, flag/identity/integration/member-policy attestations, aligned arrays, and consent. `common/scripted_effects/006_independence_wave_form03_effects.txt:85-177` transfers/cores only the consenting AGX anchor; BEL/HOL/LUX remain sovereign associated members. | PASS |
| Force, technology, industry, supply | IW-007 prepared proof (`common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:223-278`) requires current mapping, `coastal_maritime`, p7 tradition, force generation/applied flags, roster, anchor, and supply/industry inputs. p7 constants are profile `5` (`common/script_constants/006_independence_wave_force_package_constants.txt:72-85`), tradition `45` (`:286-298`), reinforcement mask `1047` (`:500-512`, five bits), inheritance mask `0` (`:714-726`), research-sensitive `0` (`:928-940`). Dynamic force effects inherit host technology/slots and create the opening template/stockpiles without a static military bundle. | PASS |
| AI and playability | `common/ai_strategy/006_independence_wave_wallonia_frisia.txt:78-133` gates AGX coastal survival, founding restraint, host-threat response, and civic coastal policy to setup/AI flags; weights cover infantry, support, artillery, trains, convoys, infrastructure, coastal defenses, factories, and war restraint. | PASS |
| Diplomacy and formable/host cleanup | AGX has former-host negotiation/guarded-frontier/association paths, no reclamation route, and a North Sea network hook; cleanup removes package decisions/mission/ideas/variables/route and formable flags, AI profile, network link, and IW-007 lifecycle flags (`common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:788-826`). | PASS |
| Localisation | `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml` supplies leader, party, value, idea, category, mission, decision, tooltip, and project text; `006_independence_wave_countries_l_english.yml` supplies AGX country/adjective/ideology forms. Both files begin with UTF-8 BOM. | PASS |
| Assets and runtime consumers | The approved retry-02 manifest and independent visual audit authorize exactly two runtime DDS files and no alternate/female/advisor/dossier/`_small` consumer. `.gfx` registers exactly the same two stable names. | PASS |
| Dormant and collision safety | AGX tag has no vanilla registration; no candidate-01 runtime reference exists; no AGX `_small`, advisor, or dossier reference exists. Event 005 capacity checks AGX country clear, state-36 anchor clear, host clear, and duplicate package/group guards before selecting IW-007. | PASS |

## File-surface checklist and concrete identifiers

- Tag/country/history: `common/country_tags/006_independence_wave_countries.txt:17`; `common/countries/006_independence_wave_AGX.txt`; `history/countries/AGX - Frisia.txt`.
- Characters/portraits: `common/characters/006_independence_wave_wallonia_frisia_characters.txt:81-126`; `interface/006_independence_wave_region_01_portraits.gfx:19-24`; `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds`; `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds`.
- Flags: `gfx/flags/AGX.tga`, `gfx/flags/medium/AGX.tga`, and `gfx/flags/small/AGX.tga` are present; no separate ideology-specific AGX flag consumer is wired or required by this package.
- Ideas/constants: `common/ideas/006_independence_wave_wallonia_frisia_ideas.txt:111-167`; `common/script_constants/006_independence_wave_wallonia_frisia_constants.txt:9-101`.
- Package setup/proof/cleanup: `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:631-724,788-826`; `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:14-72,223-306`.
- Focus: `common/scripted_effects/006_independence_wave_focus_effects.txt:35-43`; `common/scripted_triggers/006_independence_wave_focus_triggers.txt:32-42`; `common/national_focus/006_independence_wave_focus.txt:25`.
- Decisions/category: `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:309-607`; `common/decisions/categories/006_independence_wave_wallonia_frisia_categories.txt:12-13`.
- Formable FORM-03: `common/scripted_triggers/006_independence_wave_form03_triggers.txt:32-71,202-265`; `common/scripted_effects/006_independence_wave_form03_effects.txt:14-25,85-177,287-310`.
- Region publisher/reservation: `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt:84-97,281-287`; `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt:48-54`.
- Event 005 capacity/collision: `common/scripted_triggers/006_independence_wave_triggers.txt:442-450,508-552,696-720`.
- Force mapping/AI: `common/script_constants/006_independence_wave_force_package_constants.txt:72-85,286-298,500-512,714-726,928-940`; `common/scripted_effects/006_independence_wave_force_effects.txt:790-803,869-889`; `common/ai_strategy/006_independence_wave_wallonia_frisia.txt:78-133`.

## Portrait and asset authority

The retry-02 selected masters are the public-domain, identity-preserving F.O. Strüpert/Tresoar source portraits documented in `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/frisia_retry_02/manifest.md`. The runtime DDS files are byte-for-byte copies at the authoritative `.gfx` targets and both are 156x210 RGBA:

- `portrait_AGX_friesland_coastal_council.dds`: SHA-256 `2A98ECB576B331915E2B626C9CCC6DC03AF4012A411717B73D2F5253358E15A2` (Douwe Kalma, male civic leader).
- `portrait_AGX_friesland_coastal_commander.dds`: SHA-256 `07689A7045C145401E5AA7A2CFC1AE0949D59C62D4B64F144714E20197558BBA` (Pieter Reenalda, male commander).

The independent visual audit commit `c9712459c` passes both selected portraits and explicitly blocks candidate-01. Static runtime search found no candidate-01, generated-substitute, female, advisor, dossier, or `_small` AGX consumer. Protected unrelated RHI and BAY portrait hashes remain unchanged (`AA61CC3A12FB6670B690C7685FEB9383383CE58599C9E6D6E7C14F20FAB3BCE2` and `7F0AF64FDF4FECD49DF454D1198935BB3CE6A8F74AFC1AC82F8223704EAAAD2B`).

Known documentation inconsistency: retry-02 `gfx_handoff.md` still uses the old “no DDS / parent deferred conversion” wording, while the manifest, actual DDS files, and `.gfx` are wired. This is documentation debt only; it does not create a runtime consumer or asset gap. Older generated/`_small` references in historical handoffs are not live runtime references and should not be promoted as evidence.

## Map, state, and host safety

Vanilla state 36 (`history/states/36-Friesland.txt`) starts with HOL owner/core, four victory points, infrastructure 2, two civilian factories, naval base 3, manpower 2,364,000, and city category. IW-007 uses state 36 as the unique anchor and requires the former host to retain a living remnant. The region publisher reserves only state 36 for `RG-36`; the Event 005 capacity path checks country, anchor, host, duplicate package, and duplicate group conditions before selecting AGX. FORM-03 accepts AGX transfer only when AGX owns and controls 36 and keeps state 36 as capital; BEL/HOL/LUX remain autonomous members and do not silently transfer their states or cosmetic identity.

## Runtime gate and known limits

- Current checkout is not runtime-promotable because the compile-time attestation helper is IW-004-only (`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:42-44`). Parent owns that edit and final admission.
- The installed package exposes no Technology Tree Viewer. Force/technology coverage was therefore checked against the constants, scripted effects/triggers, vanilla documentation, and package proof; a viewer-based technology-tree inspection remains an unresolved tooling limitation.
- No gameplay or `.gfx` patch was made by this audit. No map write was attempted.
- The full `.tools/audit_hoi4_country_tags.py` run was attempted read-only with explicit repo/game/local-mod roots but timed out after 124 seconds while scanning installed local-mod content. Narrow direct checks still passed: mod AGX registration is exactly one line, vanilla has no `AGX` registration, and live runtime search has no candidate-01 or `_small`/advisor/dossier AGX references.
- No live HOI4 process or save-load test was run in this subagent scope.

## Simplifications, omissions, and remaining risks

No AGX country-package simplification or fallback was introduced. The only remaining risks are (1) the parent-owned IW-007 compile-time attestation gate and (2) stale wording in the retry-02 `gfx_handoff.md`. Historical superseded portrait references remain documentation-only. Parent should reconcile those docs after admission if desired.

## Handoff action

Parent may promote IW-007/AGX once the attestation helper admits `constant:independence_wave_package_id.iw_007` and the parent’s final admission checks are complete. No AGX-specific patch is requested by this audit.
