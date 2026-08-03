# IW-019 Sicily current attestation reconciliation

Date: 2026-08-03

Scope: current-source country-package audit of Event 006 IW-019 Sicily (`ASX`) after the shared runtime content-attestation change.

Disposition: **SAFE_PACKAGE_PROMOTION = ALREADY PRESENT / NO PATCH**.

The exact `iw_019` attestation clause is already present in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:86` (adapter at `:23`, package preflight at `:95-99`, and scenario dispatch at `:259-260`). The clause was added by commit `7f368753b6` (`iw_017`/`iw_019` promotion). Adding another clause would duplicate the package ID and is not safe. No gameplay, map, registry, asset, localisation, focus, decision, or spreadsheet file was changed by this audit.

## Current attestation and package coverage

The current exact compile-time attestation set is fourteen packages: IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-017, IW-018, IW-019, IW-173, and IW-184. IW-019 maps to `ASX`, reservation group `RG-115`, and anchor state `115` in `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` and `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_registry_package_counts_reaudit_v79_2026_08_01.md`.

The runtime gate is fail-closed: `is_independence_wave_runtime_package_preflight_ready` requires both the exact adapter and the exact content-attestation trigger, rejects Soviet-collapse and active-origin reuse, and then selects only the matching package/tag branch. IW-019 therefore executes through the same attested path as the other thirteen packages; no admission bypass or fallback is present.

## Country package coverage checklist

| Surface | Evidence and disposition |
| --- | --- |
| Tag and identity | `common/country_tags/006_independence_wave_countries.txt:21` maps `ASX` to `countries/006_independence_wave_ASX.txt`; the country file owns the IW-019 graphical cultures and map colour, and localisation defines Sicily/Sicilian names in `localisation/english/006_independence_wave_countries_l_english.yml:106-120`. |
| History and setup shell | `history/countries/ASX - Sicily.txt` is absent at game start, grants only `civilian_economy`, `export_focus`, and `volunteer_only`, and recruits the six package characters; runtime setup assigns territory, capital, politics, forces, ideas, focus framework, and AI. |
| Runtime package identity | `is_independence_wave_asx_package` and `can_initialize_independence_wave_iw_019_package` in `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt:21-72,185-200` require `original_tag = ASX`, package `iw_019`, Mediterranean/Iberia regional depth, port/island archetype, anchor `115`, and the complete roster. |
| Setup and cleanup | `independence_wave_setup_iw_019_sicily` and its dispatch/final-validation hooks are in `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt:832-898`; package cleanup is at `:1015-1082` and is gated by exact ASX/package identity. |
| Map and host survival | Installed state `115-Sicily.txt` is currently Italian-owned and has city-category, Palermo/other victory points, infrastructure/buildings, and 3,836,571 manpower; the binding row records `115=ITA`, `ITA=2`, and host survival through the compact anchor set. Runtime checks require state `115` to be owned and controlled by ASX after release while former host Italy retains its protected capital state `2`. |
| Politics and parties | `independence_wave_setup_iw_019_sicily` initializes the ASX party and route state; current localisation defines the civic, labor, neutrality, fascist, constitutional, traditional, emergency, and patron party names in `006_independence_wave_mediterranean_l_english.yml:62-79`. |
| Leaders and command roles | `common/characters/006_independence_wave_mediterranean_characters.txt:162-220` has Sturzo and Lanza as civilian-large country leaders, Rizzo as civilian-large despotism leader only, Di Benedetto as army-large corps commander only, and Lo Giudice/Messina as portraitless political advisors. All six character records are recruited by the history shell and have male metadata; no opposite-gender pool or female metadata is used. |
| Portraits and provenance | `interface/006_independence_wave_mediterranean_portraits.gfx:33-46` registers exactly four full ASX sprites and all four runtime DDS files exist. The current source-placeholder manifest and acceptance review are `docs/assets/006_independence_wave/source_placeholder_2026_08_03/manifest.md` and `docs/plans/006_independence_wave_plans/subagent_handoffs/006_grounded_portrait_acceptance_review_2026_08_03.md`; the four source-to-crop-to-156x210-PNG-to-DDS chains are present. Rizzo, Lanza, and Di Benedetto retain the documented role/provenance disclosures; Sturzo is clean. No advisor, dossier, `_small`, or female ASX portrait is registered. |
| Flags and assets | The standard ASX flag family is complete (`ASX`, democratic, communism, fascism, neutrality in root/medium/small variants); `python -B .tools/audit_event6_flags.py --strict` passes 102/102 registered Event 006 flag families. ASX focus, decision, and idea icon tokens resolve in `interface/006_independence_wave_mediterranean_assets.gfx` with corresponding DDS textures. |
| Focus tree | `common/national_focus/006_independence_wave_focus.txt:3198-3315` provides the eight ASX route focuses from Palermo port books through the mutually exclusive Two Sicilies dossier or Mediterranean Republic routes, with prerequisites, ASX availability, icons, rewards, and AI weights. |
| Decisions and mission | `common/decisions/006_independence_wave_mediterranean_decisions.txt:301-465` defines the founding port-authority mission and ten ASX projects/government/FORM-05 decisions with visibility, payment, cancellation, completion, and AI gates; the current Mediterranean decision audit found no missing ASX localisation keys. |
| Ideas and lifecycle | ASX baseline and route ideas are in `common/ideas/006_independence_wave_mediterranean_ideas.txt`; setup and route effects install/retire them through the package lifecycle, and the shared icon definitions resolve. |
| Forces and technology | `006_force_package_mapping.csv:20` binds IW-019 to `regular_defectors`, force table `p19`, military tradition `65`, five reinforcement pathways, and navy/air inheritance. The runtime mapping constants resolve `p19` to profile `3`, tradition `65`, reinforcement mask `527`, inheritance mask `3`, and research-sensitive `0`; the generic loader validates the mapping revision before applying the dynamic starting force. No custom technology tree is claimed; the package uses the shared runtime technology/force contract. |
| Industry, supply, and production | ASX AI prioritises infantry/support/artillery/train/convoy production, infrastructure, dockyards, and emergency coastal/bunker defence in `common/ai_strategy/006_independence_wave_mediterranean.txt:175-260`; port authority, grain-route, straits-garrison, and Italian-property projects gate the opening supply/industry loop. |
| AI and playability | The ASX AI profiles are origin-locked, setup-complete gated, and split between island survival, founding restraint, host threat, civic maritime, emergency straits command, and Two Sicilies dossier behavior. No automatic war-start or free-force shortcut is present. |
| FORM-05 and diplomacy | `common/scripted_triggers/006_independence_wave_form05_triggers.txt:70-98,100-160` and the corresponding effects explicitly admit ASX as an exact carrier at anchor `115`, require the ASX delegation/congress flags, and use the shared connected-core/member and host-threat checks. |
| Event 005 collision and reservation safety | The allocator and package triggers reject Event 005 opening cores/hosts/anchors, duplicate reservation groups, and invalid host survival; IW-019's conservative capacity witness is state `115`/`RG-115` with former host Italy retained. |

## Missing or stale surfaces

No active country-package gameplay blocker was found. The stale historical blocker is the final admission audit `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw019_sicily_final_admission_reaudit_2026_07_24.md`, whose only remaining runtime hold was the then-missing `iw_019` attestation clause. Commit `7f368753b6` resolved that hold; the older `006_iw019_sicily_country_package_reaudit_2026_07_24.md` is likewise superseded for its pre-Rizzo-role and pre-attestation wording.

Those July audits also describe the former painted/repainted portrait metadata. The current authority is the 2026-08-03 source-placeholder manifest and acceptance review; old painted PNGs, prompts, hashes, and `independently_approved_and_wired` metadata are historical evidence and must not be used to describe current runtime bytes. This is a documentation/status boundary, not a live ASX admission defect.

The package cleanup does not visibly restore the generic focus-tree assignment or retire every recruited character in the same way as some other carrier cleanups. No harmful ASX execution case was found, but this remains a low-risk parity observation outside this narrow reconciliation and is not silently treated as a new requirement.

## Validation and limitations

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008-ranked packages, 14 attested packages, 13 compatible reservation groups, the 6/8/10/14/20 ladder, and Event 005-before-Event 006 ordering.
- `python -B .tools/audit_event6_flags.py --strict` passed with 102 registered and 102 complete Event 006 flag families.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan --workshop-root C:\__event6_no_workshop__ --local-mod-root C:\__event6_no_local__` passed with 136 protected Event 006/Soviet tags and zero external definition or identity-surface collisions.
- Direct source checks confirmed the exact fourteen attestation IDs, the IW-019 adapter/preflight/scenario branches, ASX roster/anchor/setup/final-validation/cleanup helpers, focus/decision/localisation/icon references, force mapping, AI strategy, FORM-05 hooks, flag family, and four runtime DDS paths.

Live HOI4 launch, campaign execution, save/load, runtime force materialisation, live AI/balance observation, map writes, and Technology Tree Viewer validation were not performed. The installed package exposes no Technology Tree Viewer, and agent-side live game testing is outside the repository validation boundary.

## Final handoff

Changed files: this handoff only. No gameplay files, tags, state histories, map data, focus IDs, decision IDs, ideas, portraits, flags, GFX, localisation, or spreadsheet rows were changed.

No fallback or simplification was used. IW-019 is already safely promoted in the central attestation; the whole Event 006 remains **HOLD / PARTIAL** because the current admitted set is fourteen packages across thirteen reservation groups and does not provide a static 14/20-package runtime witness. The hold is event-wide capacity/runtime evidence, not a Sicily package defect.
