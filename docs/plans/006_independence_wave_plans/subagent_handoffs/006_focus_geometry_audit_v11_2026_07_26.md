# Event 006 focus geometry and AGX overlay audit v11

Date: 2026-07-26

Scope: Fresh read-only audit of the restored shared Event 006 national-focus tree and the accepted IW-007/AGX Frisia additive overlay. The audit covers route coverage, prerequisites, mutual exclusions, completion rewards, localisation, icons, AI declarations, AGX decision hooks, and authoritative MCP layout evidence. No gameplay, localisation, focus coordinates, or asset files were edited.

## Verdict

The restored baseline is structurally complete for the bounded scope and the accepted AGX overlay is present and wired. All 184 focus blocks have resolved IDs and prerequisite references where present, icons, titles, descriptions, completion rewards, custom reward tooltips, and `ai_will_do` declarations. The AGX overlay contains all eight accepted focus IDs and its North Sea conference authorization is correctly handed to the decision layer.

The tree is not layout-clean. Authoritative MCP inspect/render still reports 14 blocking layout diagnostics, 49 connector crossings, 18 node intersections, and 27 long connectors. These are the same restored-baseline geometry failures recorded by the reversion handoff; no coordinate repair is guessed or applied here.

## Authoritative MCP evidence

- `hoi4.focus_inspect` returned `FOCUS_INSPECTED` for `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, workspace `mod_chaos_redux_ea3b2d67c2c0`, revision `746605c33341e077f6ef1705ccb1ae7eb772fff3dafc8e2c7636184385803620`.
- Inspect artifact: [focus-inspect JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7687a6ef8ccaa58e3db06843e8eedce7748ed4e8bfac066ae627d266ee05a747/a449ad20edc2494a0296bb63132353b98e598c03ba7be829d9191918441fc6af/focus-inspect.3d724616b947591c.json).
- Layout hash: `a7bd7fe6afd3db003f656ef344cedcc280edb3c30cb5e0c5f12cab316890acb1`.
- Inspect metrics: 184 focuses, 223 connectors, 49 crossings, 18 node intersections, 27 long connectors, bounds `x=1..101`, `y=0..19`, 6 same-row pairs below the required spacing, and validation failed only because of `14 blocking focus diagnostics`.
- `hoi4.focus_render` returned `FOCUS_RENDERED` with the same layout hash and failed validation for the same 14 blocking diagnostics. The render is 17,904 by 2,440 pixels: [HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e6e02d372fbc89f1610dd6fc67bb41df5350630f09ab3fc33f5996685b2f9a2/28cbfaebefd8dad451233c80b4c81db53014c2f6ed57692e0b826e3f2dc6f7c9/independence_wave_focus_tree.focus.html), [SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11c1c32334716d360aed8105602ef180f5f6e359d9b94dbadef434508ac4f5b7/21220cef7ce65b69efeb5b55ca1a6859a5bc4b45f437641f2ef2d728206a5ab4/independence_wave_focus_tree.focus.svg), [JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0a5364ddc48692af3b46891697ec1b21075c2443170d1ed7a8583b008165cb3/5b2f957e4009adca3a92dba535d3f284640e03070bbf465b96568a3cba0cd878/independence_wave_focus_tree.focus.json), [source map](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ead208b59f0fff34c6c50ee23310980e953b16b42b45dc718e1da1c81b139542/409016204ef63502eea8a6c677f7155253e98163310b9ff72cb688017fe6740b/independence_wave_focus_tree.focus.source-map.json).

Blocking diagnostics are concentrated in authored source ranges `006_independence_wave_focus.txt:280-297`, `:319-336`, `:442-461`, and `:502-525`:

- One avoidable crossing between `bind_the_first_oath -> integrate_provinces_and_councils` and `inventory_the_state -> establish_emergency_revenue`.
- One additional unsatisfied crossing for that same pair.
- Three unsatisfied crossings from `complete_founding_settlement` to `ajx_appoint_neutral_commission_focus`, `define_former_host_policy`, and `recognize_fellow_new_states` against `secure_food_and_fuel -> build_regional_transport_authority`.
- Three unsatisfied crossings from the same three founding/expansion connectors against `secure_national_depots -> recall_and_vet_officers`.
- Six unsatisfied crossings around `adopt_military_archetype_program` and `found_professional_defense_institution`, covering the civilian/autonomy, border-defense/reclamation, independent-command/professional-core, and league-standardization pairs.

Non-blocking layout warnings also include long connectors `complete_founding_settlement -> map_internal_power_centers` (17 columns), `inventory_the_state -> establish_emergency_revenue` (12 columns), and `bind_the_first_oath -> integrate_militia_commands` (14 columns), plus two through-node warnings where the regional-ambition connector passes through `activate_package_economic_program` and `adopt_military_archetype_program`. MCP reports all relevant endpoints as fixed or relative, so this needs an authored coupled reflow rather than a coordinate guess.

## Route coverage

| Required lane | Source coverage and route anchors | Audit result |
|---|---|---|
| Survival/state construction | `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement` at `common/national_focus/006_independence_wave_focus.txt:63-216`; capstone writes `independence_wave_survival_capstone_complete` and `independence_wave_founding_settlement_complete` | Present and internally connected. |
| Government/internal power | Constitutional, popular-council, traditional-restoration, emergency-military, patron-client, radical-sovereignty, and AJX municipal-neutral anchors at `:818-1270`; route locks and exclusions are authored in the same blocks | All seven route families are represented; route locking is explicit. |
| Economy/infrastructure/administration | `establish_emergency_revenue` through `create_independent_treasury` at `:281-389`; the treasury focus adds `independence_wave_independent_treasury` and `independence_wave_economy_capstone_complete` | Present. The repeatable `independence_wave_treasury_backed_public_works` decision is visible from `common/decisions/006_independence_wave_decisions.txt:498-547`, so the earlier marker-only concern is resolved in the current baseline. |
| Army/security/military identity | `integrate_militia_commands` through the five paired identity choices and `found_professional_defense_institution` at `:401-662`; professional-army decision consumer at `common/decisions/006_independence_wave_decisions.txt:1165` | Present. The five one-line prerequisite blocks intentionally implement OR semantics across mutually exclusive pairs. |
| Diplomacy/recognition/patrons | `establish_foreign_office` through `become_treaty_backed_state` at `:672-809`; foreign-service decision consumer at `common/decisions/006_independence_wave_decisions.txt:802` | Present. Neutrality and patron parents remain a deliberate OR block. |
| Former-host/borders/expansion | `define_former_host_policy` and living-host/collapse branches through `settle_empty_claim` at `:1275-1442` | Living-host settlement, former-host collapse, coexistence, reclamation, and claims are all represented. |
| Network/league/formables/high-chaos | Regional ambition at `:1458-1520`, network/league at `:1532-1705`, generic formable preparation and FORM-03 branch at `:1716-1873`, hidden high-chaos lane at `:1914-2018` | Present with distinct capstone/decision flags; full multi-country/formable scenario reachability was not run. |
| Accepted AGX additive overlay | Eight focuses at `:2458-2672`: waterline authority, dikes/pumps/harbors, coastal guard, water-board government, host succession, North Sea network office, coastal conference mandate, and Low Countries dossier | Present and correctly additive. The first focus is package-gated; government, host, network, recognition, candidate, and client-lock gates are preserved through `006_independence_wave_wallonia_frisia_package_triggers.txt:96-126`. |

## Prerequisite and route-lock audit

- Static parsing found 184 unique focus IDs, 223 prerequisite references, and zero unresolved prerequisite targets.
- There are no duplicate IDs, duplicate coordinates, or `relative_position_id` entries in this source; all parent nodes are above their direct children.
- All 184 focus blocks have non-empty `search_filters`; no focus-filter omission was found.
- Twenty-seven focuses use multiple prerequisite blocks, correctly expressing AND semantics. The AGX government focus at `:2534-2535` requires both dike/pump binding and coastal-guard integration.
- Eight single prerequisite blocks contain two focus tokens and therefore intentionally express OR semantics: five professional-defense choice pairs, the neutral-or-patron treaty capstone, the RHI transit/neutral pair, and the BAY court/guardian pair.
- Forty-one mutual-exclusion blocks contain 96 resolved target references. The asymmetric AJX municipal-neutral exclusions against the six shared government anchors are intentional overlay protection; AGX uses package decisions for government/client locking and therefore has no additional AGX mutual-exclusion block.

## AGX reward and decision wiring

Every AGX focus has a completion reward, custom tooltip, and defined scripted helper in `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:538-699`:

- `chart_waterline_authority_focus` sets waterline/coastal gains and founding-state progress.
- `bind_dikes_pumps_harbors_focus` adds the anchor-state infrastructure level and administrative progress.
- `integrate_coastal_guard_focus` adds army experience and command power with security progress.
- `codify_water_board_government_focus` branches by constitutional, popular-council, or patron route.
- `settle_water_board_succession_focus` handles the living former-host record requirement versus a collapsed host.
- `open_north_sea_network_office_focus` requires network membership and updates network/league ledgers.
- `mandate_north_sea_coastal_conference_focus` sets `independence_wave_agx_north_sea_conference_authorized`; the paid decision at `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:575-629` requires that flag and retains the strategic cost/duration.
- `prepare_low_countries_dossier_focus` requires `independence_wave_agx_north_sea_conference_complete` and sets the formable-discovery/delegation flags.

## Icon coverage

Static coverage found 184 icon references across 50 unique focus icon IDs. Every used regular sprite and matching `_shine` sprite is registered; no missing focus icon was found. The AGX overlay deliberately reuses registered generic Event 006 focus sprites rather than introducing an unregistered asset.

| AGX focus ID | Icon ID | Registration |
|---|---|---|
| `independence_wave_agx_chart_waterline_authority_focus` | `GFX_goal_independence_wave_infrastructure_authority` | `interface/006_independence_wave.gfx`, regular and `_shine` |
| `independence_wave_agx_bind_dikes_pumps_harbors_focus` | `GFX_goal_independence_wave_founding_administration` | `interface/006_independence_wave.gfx`, regular and `_shine` |
| `independence_wave_agx_integrate_coastal_guard_focus` | `GFX_goal_independence_wave_army_integration` | `interface/006_independence_wave.gfx`, regular and `_shine` |
| `independence_wave_agx_codify_water_board_government_focus` | `GFX_goal_independence_wave_constitutional_state` | `interface/006_independence_wave.gfx`, regular and `_shine` |
| `independence_wave_agx_settle_water_board_succession_focus` | `GFX_goal_independence_wave_former_host_settlement` | `interface/006_independence_wave.gfx`, regular and `_shine` |
| `independence_wave_agx_open_north_sea_network_office_focus` | `GFX_goal_independence_wave_league_congress` | `interface/006_independence_wave.gfx`, regular and `_shine` |
| `independence_wave_agx_mandate_north_sea_coastal_conference_focus` | `GFX_goal_independence_wave_recognition_diplomacy` | `interface/006_independence_wave.gfx`, regular and `_shine` |
| `independence_wave_agx_prepare_low_countries_dossier_focus` | `GFX_goal_independence_wave_regional_formable` | `interface/006_independence_wave.gfx`, regular and `_shine` |

Generic icon reuse remains a readability consideration rather than a wiring failure: `former_host_settlement` is used 18 times, while `army_integration` and `infrastructure_authority` are each used 17 times across the 184-focus source.

## Localisation and reward mismatch audit

- All 184 focus IDs have title and `_desc` keys, with no duplicate relevant keys.
- All 51 custom focus tooltip keys resolve, including all eight AGX tooltip keys in `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:159-180`.
- Both `localisation/english/006_independence_wave_focus_l_english.yml` and `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml` are UTF-8 with BOM.
- All 184 focus blocks contain a completion reward and a custom effect tooltip. The 130 hidden-effect helper references found by static parsing resolve to scripted definitions; no missing reward helper was found.
- No AGX tooltip/reward mismatch was found. The numeric text aligns with `independence_wave_nwe_package_pressure` (`minor_gain = 10`, `standard_gain = 15`) and `independence_wave_value` (`minor_gain = 5`, `minor_loss = -5`). The treasury focus now also has the promised idea and repeatable decision consumer.

## AI behavior gaps

- Declaration coverage is complete: all 184 focus blocks have `ai_will_do` with a base weight and no missing base.
- Nineteen focus blocks have inline modifiers, including all eight AGX focuses; the remaining 165 use base-only weights. AGX modifiers react to waterline stability, host threat, government route, network membership, and formable/high-chaos compatibility at `:2474-2678`.
- Package AI strategy files provide founding posture, host-threat, civic-policy, and production behavior for AGX and other admitted packages, for example `common/ai_strategy/006_independence_wave_wallonia_frisia.txt:65-166`.
- The remaining gap is evidence, not a parser failure: no weighted focus-selection sweep was run across all route states, living/collapsed hosts, patron availability, league membership, or formable families. Base-only shared weights therefore do not prove the full Part 4/Part 7 route-invalidation contract under every scenario.

## Missing or simplified content

- No missing required shared lane or accepted AGX focus ID was found in this bounded audit.
- No gameplay or localisation simplification was introduced by this audit.
- Broader package-registry coverage, dynamic naming breadth outside AGX, and cross-country/formable reachability remain outside this geometry-focused pass and are not claimed complete here.

## High-priority fixes and follow-up

1. Perform a coupled authored reflow of the four MCP crossing clusters in `common/national_focus/006_independence_wave_focus.txt`, preserving the 223 prerequisite edges, the eight OR blocks, and all mutual exclusions. Do not move only one endpoint based on the warning text.
2. After any reflow, rerun `hoi4.focus_inspect` and `hoi4.focus_render` and require the same tree to report zero blocking diagnostics before claiming layout completion.
3. Run a read-only weighted-AI/reachability sweep for shared government, host, patron, league, regional-formable, and AGX conference states. This is needed to turn the current AI declaration evidence into route-selection evidence.

## Validation and limits

Meaningful checks completed: authoritative MCP inspect/render; source parser for IDs, coordinates, prerequisites, mutual exclusions, completion rewards, hidden helper definitions, focus filters, and AI declarations; icon registry check across `interface/*.gfx`; localisation key/duplicate/BOM check; AGX helper/decision flag cross-reference; treasury capstone consumer check. The required AGENTS.md, repository focus/events/decisions/assets/improvement/subagent skills, offline national-focus/core wiki pages, and relevant vanilla documentation were consulted before auditing.

Skipped: no `hoi4.focus_rewrite` was run because the task is read-only and coordinates are intentionally unchanged; no game launch or live-save validation was performed; no broad probability sweep was run; no focus raster was needed after the structural SVG/HTML render.

Remaining risk: MCP layout validation remains failed until the authored reflow is completed. Runtime package admission, live focus availability, and AI route choice still require parent-owned scenario validation.

Changed files: none besides this read-only audit handoff.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_focus_geometry_audit_v11_2026_07_26.md`.
