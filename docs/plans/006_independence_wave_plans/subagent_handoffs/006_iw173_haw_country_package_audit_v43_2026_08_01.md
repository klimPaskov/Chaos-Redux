# Event 006 IW-173 HAW country-package audit v43

**Date:** 2026-08-01

**Owner:** Chaos Redux country-package audit subagent

**Scope:** Independent static audit of the Event 006 IW-173 Hawai'i package (`HAW`), including identity and vanilla roster boundaries, map and state setup, politics, leaders, portraits, ideas, focus and decision surfaces, forces, technology, industry, supply, production, AI, host relations, regional ambitions, FORM-48 links, localisation, flags, asset coverage, and package-dispatch admission wiring.

**Changes made:** This audit changed no gameplay, map, localisation, interface, portrait, flag, or asset file. The only new file is this handoff.

## Verdict

**BLOCKED for runtime admission.** The HAW package has a coherent gameplay implementation and the expected dispatch adapters, but it is deliberately fail-closed at the central runtime content-attestation gate. IW-173 is not listed in `has_independence_wave_runtime_package_content_attestation_for_execution_id` (`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:62-78`).

The visual admission gate is also incomplete. The Samuel Wilder King source package is explicitly `SOURCE-READY CANDIDATE / NOT RUNTIME-PROMOTED`, with no final DDS, `.gfx` definition, or character/leader consumer (`docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw173_haw_samuel_wilder_king_source_clearance_2026_07_26.md`; `docs/assets/006_independence_wave/hawaii_samuel_wilder_king_source_clearance_2026_07_26/manifest.md`). The independent likeness/style/provenance gate has not been recorded as passed.

Portrait approval alone would not authorize a leader change. Any King adoption requires an explicit consumer and name/roster decision that preserves or explicitly transfers the existing David Kalakaua Kawananakoa contract. A silent replacement is unsafe and not authorized by the current package.

## Country-package coverage checklist

| Surface | Status | Evidence |
| --- | --- | --- |
| Tag and package identity | PASS | `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:19-23` binds `original_tag = HAW` to `independence_wave_package_id.iw_173`; dispatch preflight binds the same ID to `HAW` at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:146-149`. |
| Country history and vanilla roster | PASS, preserved | Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/HAW - Hawaii.txt:1-87` sets capital 629, neutrality, the 1936 popularity baseline, and David Kalakaua Kawananakoa, Joseph Poindexter, and Charles Fujimoto. No mod history override was found. |
| State, capital, and map reservation | PASS with intentional extension note | Anchor 629 and reservation group RG-629 are bound in `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:174` and `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv:49`; optional HAW-core states 630, 631, 642, and 727 remain host-held extensions. |
| Politics and laws | PASS | `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:685-732` initializes HAW baseline laws, shipping security, route flags, host routes, ambition, and lifecycle state; `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:304-360` proves the prepared state. |
| Leaders and portrait ownership | BLOCKED for new visual consumer; vanilla preservation PASS | `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:45-52,323` requires the ruling-only David name and states that Event 006 never recruits, promotes, retires, or replaces the vanilla HAW roster. No runtime King consumer exists. |
| Ideas and visible pressure | PASS | `common/ideas/006_independence_wave_pacific_ideas.txt:31-46` defines HAW-only `haw_exposed_island_supply` and `haw_island_shipping_compact`; start and stable pressure values are applied in `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:690-691` and `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:190-225`. |
| Full framework and HAW focus branch | PASS | `common/national_focus/006_independence_wave_focus.txt:24-60` owns the full Event 006 tree and imports the HAW branch; the seven bespoke focuses are in `common/national_focus/006_independence_wave_pacific_focus.txt:145-282`. |
| Decisions and mission | PASS | HAW category and mission/decisions are in `common/decisions/006_independence_wave_pacific_decisions.txt:170-280`; the category is registered in `common/decisions/categories/006_independence_wave_pacific_categories.txt:13-16`. |
| Forces, technology, industry, supply, and production | PASS with host-transaction risk | IW-173 maps to `coastal_maritime`, tradition 62, both navy and air inheritance, and five reinforcement paths in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:174`; p173 constants are in `common/script_constants/006_independence_wave_force_package_constants.txt`, and bounded force application is in `common/scripted_effects/006_independence_wave_force_effects.txt:790-888`. HAW has only vanilla starting infantry technology, so host technology inheritance is a required runtime transaction. |
| AI and playability | PASS | HAW survival, founding-restraint, and host-threat profiles are in `common/ai_strategy/006_independence_wave_pacific.txt:40-66`; tuning is centralized in `common/script_constants/006_independence_wave_pacific_constants.txt`. |
| Host relations and regional ambitions | PASS | HAW setup publishes host negotiation/frontier/association/reclamation routes, Pacific federation family, and HAW FORM-48 candidacy in `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:706-715`; living-host settlement and host-collapse delegation gates are covered by the HAW decisions/focus. |
| FORM-48 and sovereignty boundary | PASS | HAW exact member identity and anchor 629 are checked in `common/scripted_triggers/006_independence_wave_form48_triggers.txt:29-35,165-180,304-337`; the FORM-48 effects explicitly do not annex HAW (`common/scripted_effects/006_independence_wave_form48_effects.txt:5-10`). |
| Localisation and focus icons | PASS | HAW category, ideas, decisions, mission, seven focus names/descriptions/tooltips, and project text are present in `localisation/english/006_independence_wave_pacific_l_english.yml:34-161`; seven icon sprites are defined in `interface/006_independence_wave_pacific_focus_icons.gfx:66-126` and all seven referenced DDS files exist. |
| Flags and portrait assets | PASS for intentional vanilla reuse; BLOCKED for new leader asset | No HAW route-specific flag or portrait override is present. The package documentation explicitly keeps the vanilla HAW flag and leaves HAW leader visuals withdrawn until a sourced replacement passes the independent gate (`docs/events/006_independence_wave/pacific_country_packages.md:5-10,138-190`). |
| Package dispatch and cleanup | PASS as wiring, BLOCKED as admission | Setup/final-validation/cleanup dispatch includes IW-173 at `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:837-860,1032-1048`; the central attestation still excludes IW-173. |

## File-surface findings

### Identity, setup, history, and map

- `HAW` is an existing vanilla country. The exact package trigger is narrow and checks the original tag, active-country state, and IW-173 ID (`common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:19-23`).
- Setup is intentionally limited to dormant HAW with `generic_focus`; meaningful non-generic HAW trees fail closed (`common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:201-215`). The setup effect loads the full Event 006 framework only after this check (`common/scripted_effects/006_independence_wave_pacific_package_effects.txt:685-732`).
- Vanilla capital 629 is the fixed anchor. Vanilla state 629 is USA-owned with HAW core, infrastructure 2, air base 5, naval base 10, naval supply hub 1, and victory points 15 and 3 (`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/629-Hawaii.txt:8-29`).
- The installed binding records 630, 631, 642, and 727 as optional outlying HAW-core extensions while USA retains a protected remnant (`docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:174`). This is an intentional compact-anchor design, not a missing map transfer, but runtime extension behavior remains a parent-owned map validation point.
- No Chaos Redux state-history or province edit was required for this package audit.

### Politics, leaders, portraits, parties, and flags

- Vanilla HAW begins with neutrality, no elections, popularities democratic 38, fascism 6, communism 6, neutrality 50, and 20 convoys (`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/HAW - Hawaii.txt:41-52`).
- The existing vanilla leader roster is David Kalakaua Kawananakoa (ruling despotism), Joseph Poindexter (liberalism), and Charles Fujimoto (marxism) (`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/HAW - Hawaii.txt:59-87`). The package preservation trigger requires David as the ruling-only name and never mutates the roster (`common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:45-52`).
- There is no `common/characters` King definition, no HAW `.gfx` portrait consumer, and no HAW DDS runtime portrait. `interface/006_independence_wave_pacific_portraits.gfx` contains only HBX/FSM portrait definitions. This absence is correct while HAW is withdrawn, but it blocks visual admission.
- The Samuel Wilder King dossier is source-ready evidence only. Its manifest explicitly prohibits automatic David replacement, advisor/dossier use, `_small`, commander, operative, or outside-HAW use and says no final DDS or `.gfx` is claimed (`docs/assets/006_independence_wave/hawaii_samuel_wilder_king_source_clearance_2026_07_26/manifest.md`).
- If King is later adopted, the parent must choose one supported full-size HAW consumer and explicitly decide whether David remains ruler, is retired, or is transferred under a guarded, documented effect. Do not create a second ambiguous country-leader roster or silently rename the ruler.
- No HAW-specific flag asset is needed by the current design. Vanilla HAW flags remain the accepted identity surface; a route-specific flag would be a separate identity decision.

### Focus, decisions, ideas, and localisation

- The shared Event 006 tree is `independence_wave_focus_tree` (`common/national_focus/006_independence_wave_focus.txt:24-60`), and the HAW branch is a seven-focus fork-and-rejoin group: shipping registers, coastwatch, government compact, shipping/supply/coastwatch binding, base/property accounts, autonomous Pacific mandate, and Pacific delegation (`common/national_focus/006_independence_wave_pacific_focus.txt:145-282`).
- Every HAW focus has an icon, prerequisite chain, availability, completion tooltip, and AI weight. The capstone requires stable shipping and recognition and is host-collapse gated for AI (`common/national_focus/006_independence_wave_pacific_focus.txt:255-282`).
- The HAW mission and four decisions serialize visible work, project costs, cancellation, timeout, and focus mutual exclusion (`common/decisions/006_independence_wave_pacific_decisions.txt:170-280`). The government compact is correctly represented by a focus rather than an unregistered duplicate decision.
- The HAW-only ideas and lifecycle swaps are complete (`common/ideas/006_independence_wave_pacific_ideas.txt:31-46`; `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:190-225`). No orphan HAW idea key was found.
- Localisation coverage is complete for the HAW category, ideas, mission, decisions, projects, and all seven focuses (`localisation/english/006_independence_wave_pacific_l_english.yml:34-161`). A broader locale style review has noted punctuation style issues in this file, but no missing HAW key was found and this is not an admission blocker.

### Forces, technology, industry, supply, and production

- The force mapping is explicitly Hawaiian: coastal guards, sailors, and local infantry; coastal-maritime profile; military tradition 62; engineers/coastal signals/reconnaissance/maintenance first; artillery/logistics after port and base integration; both navy and air inheritance; and militia, regional guard, depot, volunteer-corridor, and professional-officer reinforcement paths (`docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:174`).
- `common/script_constants/006_independence_wave_force_package_constants.txt` sets p173 profile 5, tradition 62, reinforcement mask 535, inheritance mask 3, and research-sensitive false. The dynamic force effect creates bounded starting forces and transfers only approved air/navy fractions (`common/scripted_effects/006_independence_wave_force_effects.txt:790-888`).
- Vanilla HAW has only `infantry_weapons = 1` in the starting history. The dynamic package's host technology and research-slot inheritance is therefore required and must remain tied to the former-host transaction (`common/scripted_effects/006_independence_wave_force_effects.txt:790-803`).
- No HAW industrial factory, production-line, supply-node, or equipment-stockpile override was found in mod history. The package correctly avoids impossible civilian-factory reservations on the non-industrial anchor and uses shipping, manpower, equipment, stability, war support, and bounded host transfers instead (`docs/events/006_independence_wave/pacific_country_packages.md:259-263`).

### AI, diplomacy, host relations, and regional ambition

- `independence_wave_haw_island_shipping_survival` is enabled only after exact package setup and the HAW AI profile; founding restraint aborts under severe host threat or regional-power conditions; host-threat AI raises army and coastal-defence priorities (`common/ai_strategy/006_independence_wave_pacific.txt:40-66`).
- HAW setup registers host negotiation, guarded frontier, association, reclamation, Pacific regional federation, and FORM-48 member-candidate state (`common/scripted_effects/006_independence_wave_pacific_package_effects.txt:706-715`). The HAW settlement decision is visible only while the former host remains living, and the delegation route requires stable shipping and recognition.
- FORM-48 uses exact HAW tag, package ID, anchor state, ownership, control, capital, carrier generation, and Pacific-family checks. HAW remains autonomous and is never inferred from geography or annexed by the formable (`common/scripted_triggers/006_independence_wave_form48_triggers.txt:29-35,165-180,304-337`; `common/scripted_effects/006_independence_wave_form48_effects.txt:5-10`).

## Missing, stale, or blocked surfaces

1. **Central runtime admission is blocked.** IW-173 appears in the adapter list and exact tag preflight, but it is absent from the content-attestation OR block (`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:26,62-78,146-149`). Do not add it to attestation until the portrait/identity gate and the post-wire package audit are complete.
2. **The King portrait gate is not complete.** The source dossier contains a normalized 156x210 candidate, but it remains evidence-only and records the next required independent likeness/style/provenance audit; no final DDS, `.gfx`, character definition, or runtime owner exists (`docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw173_haw_samuel_wilder_king_source_clearance_2026_07_26.md`; `docs/assets/006_independence_wave/hawaii_samuel_wilder_king_source_clearance_2026_07_26/manifest.md`).
3. **Leader adoption is a design gate, not a missing-file fix.** Existing setup explicitly checks David Kalakaua Kawananakoa as ruling leader and the package docs prohibit silent replacement (`common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:45-52,323`; `docs/events/006_independence_wave/pacific_country_packages.md:172-190`). A parent decision must name the supported King consumer and the exact David roster transition before any runtime character/portrait wiring.
4. **Map extension behavior is intentional but should be exercised by the parent.** The compact anchor is 629; 630, 631, 642, and 727 are optional host-held extensions (`docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:174`). No static contradiction was found.
5. **No Technology Tree Viewer is installed.** Static review confirms the host-tech inheritance effect and vanilla HAW starting technology, but an MCP technology-tree render/compare could not be performed under the installed tool limitation.

## Validation run

- Cross-referenced the exact HAW ID/tag in package triggers, setup effects, final validation, cleanup, scenario preflight, and Pacific dispatch.
- Cross-referenced all seven HAW focus IDs against their localisation keys, icon definitions, and seven existing DDS files.
- Cross-referenced HAW ideas, mission, decisions, AI strategy, force mapping, p173 constants, host/formable triggers, and cleanup effects.
- Inspected vanilla HAW country history and state 629, plus the installed package-binding and reservation-group rows.
- Searched gameplay/interface roots for Samuel Wilder King runtime consumers; only the source dossier, manifest, and evidence files contain the candidate, with no character, leader, DDS, or `.gfx` runtime owner.
- No Hearts of Iron IV executable, save, scenario, or live game was launched. No map write was attempted. The Technology Tree Viewer limitation is recorded above.

## Admission recommendation

Keep IW-173 outside central runtime content attestation. After an independent King portrait audit passes, the parent must still make and document the explicit consumer/name decision, implement the bounded HAW character/portrait ownership if selected, verify David's guarded roster transition, rerun the country-package and post-wire asset audits, and then decide whether to add IW-173 to the attestation set. If the parent retains David as ruler and does not implement a supported King consumer, the package remains gameplay-valid but visually withdrawn and must stay out of runtime admission.

**Simplifications or omissions:** No gameplay simplification was introduced by this audit. The only unresolved items are the intentional visual withdrawal, the missing central attestation, and the explicit leader-consumer decision described above.
