# Event 006 localisation gap scan, 2026-08-26

## Scope and authority

This bounded pass compared the current Event 006 event, decision, mission, focus, formable, league, scripted-localisation, and scripted-GUI sources with `docs/specs/006_independence_wave_specs/` and the current source-of-truth and retirement handoffs. The accepted authority is that no Independence Wave category, mission, cost, queue, pressure meter, history row, or crisis wording is visible before the committed public report. Post-release former-host pressure, founding crises, and revisionist pressure remain accepted mechanics and were not treated as forbidden pre-event content.

The working tree already contained unrelated changes, including edits to `006_independence_wave_form05_l_english.yml`, `006_independence_wave_rival_bloc_l_english.yml`, and `006_independence_wave_wallonia_frisia_l_english.yml`. This pass did not edit those files or any gameplay source.

## Patch applied

Changed file:

- `localisation/english/006_independence_wave_minor_overlay_l_english.yml`

Changed keys at current lines 313-322 and 410-419:

- `independence_wave_iw_cog_cabinet_cost`
- `independence_wave_iw_cog_cabinet_cost_blocked`
- `independence_wave_iw_cog_cabinet_cost_tooltip`
- `independence_wave_iw_cog_depot_cost`
- `independence_wave_iw_cog_depot_cost_blocked`
- `independence_wave_iw_cog_depot_cost_tooltip`
- `independence_wave_iw_cog_force_cost`
- `independence_wave_iw_cog_force_cost_blocked`
- `independence_wave_iw_cog_force_cost_tooltip`
- `independence_wave_iw_region_cabinet_cost`
- `independence_wave_iw_region_cabinet_cost_blocked`
- `independence_wave_iw_region_cabinet_cost_tooltip`
- `independence_wave_iw_region_depot_cost`
- `independence_wave_iw_region_depot_cost_blocked`
- `independence_wave_iw_region_depot_cost_tooltip`
- `independence_wave_iw_region_force_cost`
- `independence_wave_iw_region_force_cost_blocked`
- `independence_wave_iw_region_force_cost_tooltip`

Before, each string contained a bare trailing `£` after the command-power value, either `]£  £manpower_texticon` or `§!£  £manpower_texticon`. That marker could be parsed as the start of an invalid icon token. After, the stray marker is absent and the next valid icon begins normally. All dynamic constants, values, formatting colours, labels, and resource requirements are unchanged. No dynamic localisation was added or removed.

## Audit results

### Missing keys

The explicit and implicit gameplay-key scan covered 36 Event 006 event, decision, focus, scripted-GUI, and interface sources and 3,190 references. It found no missing ordinary event, option, decision, mission, focus, GUI, or tooltip key. `independence_wave_focus_tree_desc` appeared only as a mechanical false positive generated from the focus-tree container id; it is not a player-facing focus key.

The custom-cost-family scan found 190 unique `custom_cost_text` bases. Seven implicit suffix keys are absent:

- `independence_wave_fer_cost_administration_standard_blocked`
- `independence_wave_fer_cost_administration_standard_tooltip`
- `independence_wave_fer_cost_strategic_blocked`
- `independence_wave_fer_cost_strategic_tooltip`
- `independence_wave_form08_congress_cost_tooltip`
- `independence_wave_form08_arbitration_cost_tooltip`
- `independence_wave_form08_transport_cost_tooltip`

The consumers are `common/decisions/006_independence_wave_far_eastern_decisions.txt:173,507` and `common/decisions/006_independence_wave_formable_decisions.txt:34,58,82`. The existing bases are in `localisation/english/006_independence_wave_far_eastern_l_english.yml:81-82` and `localisation/english/006_independence_wave_formable_registry_l_english.yml:112-117`. These were not synthesized because the Far Eastern blocked text needs an accepted colour and wording contract, while the FORM-08 tooltip text should be checked against its scripted transport alternative rather than copied mechanically.

### Duplicate keys and namespaces

No duplicate key was found across the 37 `006_independence_wave*_l_english.yml` files. No legacy `:0` key syntax was found. The event-option `name` scan found no undefined option localisation.

### Scripted localisation

No broken scripted-localisation reference was found among the current explicit gameplay references. The retired crisis history selectors remain in `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt:19-64` and in the shared event-log selector at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:6148-6168,9616-9678`. Their compatibility localisation remains at `localisation/english/006_independence_wave_l_english.yml:123-135`.

The scan found no current writer that assigns an Event 006 history payload to `constant:independence_wave_crisis_history.*` or `constant:independence_wave_crisis_resolution_history.*`. These branches are therefore compatibility-only and not evidence of a visible pre-event crisis surface. Their stale names remain a maintenance risk: if a future writer reuses those payload constants, the retired record text could become visible again.

### Pre-event visibility and cross-surface consistency

`events/006_independence_wave.txt` keeps `chaosx.nr6.1` hidden and trigger-only, presents the first public wording through committed `chaosx.nr6.2`, and uses hidden `chaosx.nr6.3` for cleanup. The current allocator audit passed and explicitly reports `pre-event crisis surface: retired; no category, mission, cost, or queue`. No player-facing pre-event pressure meter, category, mission, cost, queue, request, or history row was found.

Two older design documents still carry superseded crisis language and should not be used as current implementation instructions: `docs/specs/006_independence_wave_specs/prompts/independence_wave_goal_prompt.md:3` still asks for a pre-event crisis, and `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md:186` says an existing country may receive crisis decisions. Parts 2 and 3, the quality checklist, the source-of-truth map, the resume packet, and the retired-crisis handoff supersede those sentences.

No direct contradiction was found between the current post-release event, focus, decision, formable, and league wording. The seven missing custom-cost suffixes are the concrete cross-surface gap.

### Dynamic text opportunities

- `independence_wave_afx_codify_basin_government_tt` and `independence_wave_agx_codify_water_board_government_tt` in `006_independence_wave_wallonia_frisia_l_english.yml:142,171` embed route values as static `5`, `10`, `15`, and `20`. They should use the existing script constants before the file is finalized. The file was already modified by another agent, so this pass did not touch it.
- `independence_wave_nav_route_effect_tt`, `independence_wave_glc_route_effect_tt`, and `independence_wave_kc_route_effect_tt` describe route-dependent changes without displaying the actual route values. Their owning decision effects should expose existing constants or route-specific scripted localisation if the values fit the tooltip consumer.
- The Iceland category and several host/network tooltips already use dynamic values, but the surfaces would be easier to read if secondary ledger values were moved into a detailed tooltip or the Statehood Ledger instead of being repeated in the category description.

### File encoding

All 37 Event 006 English localisation files retain UTF-8 BOM after the patch. No encoding concern was found.

### Prose quality

Vagueness:

- The three route tooltips above say values change “according to” the route without stating the amounts.
- Several package network tooltips only say that five league measures “rise,” which hides the magnitude despite nearby packages displaying dynamic values.

Bloat:

- Event 006 contains 609 cost-related keys. Twenty-seven display more than four icon tokens, exceeding the compact cost-string budget. The largest are `independence_wave_formable_commit_cost_revolutionary` and `independence_wave_formable_commit_cost_military` in `006_independence_wave_formable_registry_l_english.yml:29-30`, each displaying nine icons across a dense ledger.
- `independence_wave_ice_north_atlantic_category_desc` in `006_independence_wave_western_l_english.yml:234` exposes a large multi-line ledger in the category description.
- `independence_wave_rut_network_effect_tt` in `006_independence_wave_ruthenia_l_english.yml:121` repeats domestic, network, and corridor ledgers in one tooltip.

Obvious explanation:

- Several `_cost_tooltip` strings prefix an already visible resource list with labels such as “Cabinet commitment” or “Force commitment.” These labels add little context when the decision title already names the project.

Repetition:

- “Network Standing, League Cohesion, Common Cause, Shared Reserve, and Member Confidence rise” recurs across many package tooltips. Where the values are identical, a shared dynamic localisation fragment would reduce repetition and prevent package-to-package wording drift.

Overcomplication:

- `independence_wave_form16_integration_category_desc` in `006_independence_wave_transcaucasus_l_english.yml:5` combines tier logic, three thresholds, formation requirements, and three capital-control requirements in one paragraph.
- The Ruthenia and Kosovo host-ledger tooltips combine two overlapping settlement passes and long noun lists, making the actual consequence difficult to scan.

Style-rule repair:

- No em dash or sentence semicolon was found in the 37 Event 006 localisation files.
- The only style patch in this pass repaired malformed icon markers. No broad prose rewrite was made because the ledger density is tied to accepted mechanics and needs owner-led layout/cost-family decisions rather than deletion of consequences.

### Sourced quotations

The two attributed super-event quotations at `localisation/english/006_independence_wave_l_english.yml:115,119` were inspected and preserved verbatim, including their punctuation and attribution. No quote-bearing key was edited.

## MCP evidence

- Focus inspect resolved all 184 Event 006 focus titles and reported zero Event 006 diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/97b585dd45a20dcd85f9045f9b61e1a65ef479fb6bc8c625271cc93925550a69/70b013b9ea83aef8ed327d6eede218a8f9ed6ac959e60656efd5d7e332b74c67/focus-inspect.56ae3826618bdd95.json`.
- Focus render passed; the only localisation diagnostic was unrelated vanilla `continuous_restrict_freedom_desc`. HTML artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78e0cbb9e4fd013de3eccea8f414784f17864720bfe74a2639826ed9fca1efde/2b0f4614102879f6931ce60ef5e658a04b56f5c98689a0ebda9a3be5a36b99d1/independence_wave_focus_tree.focus.html`.
- Event lint returned `EVENT_INSPECTED_PARTIAL` with zero blocking event diagnostics; workspace-wide helper and lifecycle projection was deferred. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bbf2faf1589c44b4a93c30e46df6954bb20daa72da6bef4b21cc7852252b0893/589572885fb1736ee1b50732d49d086b7011a3a7c57220b215c7c5d09aa1d891/event-lint-f1288dea1225.json`.
- Event overview render returned `EVENT_RENDERED_PARTIAL` under the same large-workspace limitation. SVG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42c6e09416bb2ae53904932c6e71658e63426fd38950fdc7fbff1f8b3ca6ca5c/c24073c2b85000c43062a6cbe9fbbfaaa16eb55198cc5b5c6fd2336f507a8d16/event-overview-f1288dea1225.svg`.
- Statehood Ledger inspect selected 48 elements, but the global GUI graph retained 2,000 blocking diagnostics and 64 visible-overlap diagnostics; this is not a clean window-level localisation or overflow receipt. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b2321ca554605d41abd73aa5c994a2a24d809a6ba3a25841fdcdff01e1ffce08/b635db7dcd1a6088ecc121befd190ecf882c4104ed2fb0e64c59bfa6308f7f34/gui-inspect.ae68633c8c57de38.json`. Long-text and missing-localisation render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5cf000756ada11a3f72b77c58099ed8eb2f376d67cd52aa69bf75f77a8e2a31f/04a09497e40b2d15da36ee95496fc307c7c8942b612fc52a271044e03ef6dfde/independence_wave_status_window-full.svg`.
- Formable state-puzzle inspect selected 93 elements, but the global GUI graph retained 2,000 blocking diagnostics and 521 visible-overlap diagnostics; this is likewise not a clean bounded overflow receipt. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00c6e2b59a5b9133ee317c40786549dbaa05ed78f62de360cab4bb61c1703777/fb8282328778c75ea2dfa97a9747bdfebad0efb1a205371187ddbaaf06fe2385/gui-inspect.7cbf8a2157b6470f.json`. Long-text and missing-localisation render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f86acb57a7f08f83b7b8ebe592088caf6ffda99ea5648ac21ec9b878eadf1d7/d8e0970b4db959ae96ef0741f8ebb933464fbb0892cfc9711eb7f007de090817/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

The Technology Tree Viewer is absent from the installed package and no Event 006 technology surface was found in this localisation scope.

## Validation and unresolved decisions

- `python -B .tools/audit_event6_allocator.py` passed and confirmed the retired pre-event surface.
- `python -B .tools/audit_event6_gui_matrix.py` passed the Statehood Ledger semantic source matrix; it does not claim runtime layout or save/load evidence.
- A before/after key comparison proved that all 18 edited values differ from `HEAD` only by removal of the malformed bare marker. No other character, dynamic token, constant path, colour code, or prose changed.
- The post-patch marker scan found zero remaining `]£  £...` or `§!£  £...` sequences in the changed file.
- No in-game validation was performed. GUI MCP output is globally truncated and cannot close the remaining overflow question.

Unresolved wording and display decisions are the seven custom-cost suffix keys, the 27 cost strings with more than four icon tokens, the dense category/ledger descriptions, the generic route-effect wording, and whether compatibility-only crisis history selectors should be renamed or removed by their gameplay owner. No gameplay change, fallback, sourced-quotation change, or unapproved simplification was made.
