# Event 012 Africa Charter scripted GUI handoff

Status: the bounded event-owned Charter window layout repair is implemented in the shared worktree and is ready for parent review.

This tranche changes only `interface/012_africa_charter.gui` and adds this handoff; `common/scripted_guis/012_africa_charter_scripted_gui.txt`, `interface/012_africa_charter.gfx`, the event-owned scripted-localisation file, and `localisation/english/012_africa_charter_gui_l_english.yml` were inspected but not changed in this tranche.

## Ownership and entry point

The surface is Event 012, slug `012_africa`, Africa Charter League, and the GUI is exclusively attached to the Event 012 decision category `africa_charter_council_category` by `scripted_gui = africa_charter_window` in `common/decisions/categories/012_africa_categories.txt:13`.

The accepted design in `docs/specs/012_africa_specs/specs/012_africa_spec_part_2_charter_league_integration.md` calls for a scripted GUI attached to the main Charter decision category that presents the continental picture, members, regions, and action costs, while `spec_part_3_focus_tree_architecture.md` names the Charter Authority, Reach, Burden, Pressure, and member-confidence presentation.

The scripted GUI is host-only through `context_type = decision_category`, `window_name = "africa_charter_window"`, `is_ai = no`, and `africa_is_current_host = yes`; it presents existing cursor and quote state and does not execute action outcomes.

## Exact surface and identifier map

The GUI file is `interface/012_africa_charter.gui` and defines the 1000 by 680 `africa_charter_window` container.

The scripted GUI file is `common/scripted_guis/012_africa_charter_scripted_gui.txt` and defines `africa_charter_window` with overlay selectors `africa_charter_overlay_1` through `africa_charter_overlay_9`, member selectors `africa_charter_member_1` through `africa_charter_member_5`, state selectors `africa_charter_state_1` through `africa_charter_state_5`, family selectors `africa_charter_family_protection`, `africa_charter_family_accession`, `africa_charter_family_congress`, `africa_charter_family_integration`, `africa_charter_family_economy`, `africa_charter_family_diaspora`, `africa_charter_family_rival`, and `africa_charter_family_chaos`, plus four diaspora-origin and four diaspora-skill selectors.

The scripted-GUI click effects are presentation and cursor calls such as `africa_charter_overlay_1_click`, `africa_charter_member_1_click`, `africa_charter_state_1_click`, `africa_charter_family_protection_click`, `africa_charter_diaspora_origin_1_click`, and `africa_charter_diaspora_skill_1_click`; all numbered variants remain wired to their pre-existing effects and triggers.

The event entry point is the `africa_charter_council_category` decision category, not a new decision, event option, action effect, AI rule, or shared GUI registry.

The GFX file is `interface/012_africa_charter.gfx` and the event-owned sprite identifiers are `GFX_012_africa_charter_window_background`, `GFX_012_africa_charter_header_plate`, `GFX_012_africa_member_card_frame`, `GFX_012_africa_regional_card_frame`, `GFX_012_africa_relationship_badges`, `GFX_012_africa_primary_value_icons`, `GFX_012_africa_secondary_value_icons`, `GFX_012_africa_clause_tabs`, `GFX_012_africa_regional_overlay_buttons`, `GFX_012_africa_project_progress_frame`, `GFX_012_africa_rival_bloc_panel`, `GFX_012_africa_diaspora_summary_panel`, `GFX_012_africa_charter_seal_activation_animated`, `GFX_012_africa_charter_seal_activation_static`, `GFX_012_africa_charter_authority_ring_animated`, and `GFX_012_africa_charter_authority_ring_static`.

The GUI localisation file is `localisation/english/012_africa_charter_gui_l_english.yml`, with the main display keys `africa_charter_gui_title`, `africa_charter_gui_route_identity`, `africa_charter_gui_primary_values`, `africa_charter_gui_secondary_values`, `africa_charter_gui_member_*`, `africa_charter_gui_selected_member_*`, `africa_charter_gui_regional_*`, `africa_charter_gui_state_*`, `africa_charter_gui_rival_*`, `africa_charter_gui_diaspora_*`, `africa_charter_gui_project_summary`, `africa_charter_gui_action_summary`, and `africa_charter_gui_family_*`, plus the `africa_charter_overlay_*`, `africa_charter_action_family_*`, `africa_charter_diaspora_origin_*`, and `africa_charter_diaspora_skill_*` value labels.

The event-owned scripted-localisation source is `common/scripted_localisation/012_africa_charter_gui_scripted_localisation.txt`; it was not changed here.

## Precedents and required references inspected

The offline wiki pages `Interface Modding - Hearts of Iron 4 Wiki.md` and `Scripted GUI Modding - Hearts of Iron 4 Wiki.md` were read alongside the required data-structure, trigger, effect, modifier, localisation, scope, on-action, event, decision, idea, and AI pages.

The installed vanilla documentation and GUI precedents inspected were `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/interface_documentation.md`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/scripted_gui_documentation.md`, `interface/usa_congress_scripted_gui.gui` with `common/scripted_guis/USA_congress_scripted_gui.txt`, and `interface/raj_local_leaders_investments_decision_ui.gui` with `common/scripted_guis/RAJ_local_leaders_investments_scripted_gui.txt`.

The local layout and event references inspected were `docs/specs/012_africa_specs/specs/012_africa_spec_part_2_charter_league_integration.md`, `docs/specs/012_africa_specs/specs/012_africa_spec_part_3_focus_tree_architecture.md`, `common/decisions/categories/012_africa_categories.txt`, `common/scripted_guis/012_africa_charter_scripted_gui.txt`, `interface/012_africa_charter.gfx`, and `localisation/english/012_africa_charter_gui_l_english.yml`.

## Layout hierarchy and budgets

The first layer is the full 1000 by 680 `GFX_012_africa_charter_window_background` at the window origin, followed by a 976 by 84 header plate at `(12,8)` and the title, route identity, and primary-value header text.

The left column is the member roster and selected-member dossier at approximately `x=16..316`, `y=104..650`, with five bounded member slots, one selected-member flag/name/detail area, and the existing relationship, confidence, protection, clause, obligation, project, departure, and rival-pressure readout.

The centre column is the regional card at `x=322..638`, `y=104..650`, with regional heading/detail, a 3 by 3 overlay selector grid, regional metrics, and five prepared-state candidate rows.

The right column begins with the rival warning panel at `x=654`, `y=104`, continues with the diaspora summary panel at `x=654`, `y=210`, and places the project/action ledger at `x=654`, `y=424` followed by the eight family-page selectors at `y=594` and `y=622`.

The primary visible value is Charter Authority, with Continental Reach, Integration Burden, and Colonial Pressure as the three supporting values; readiness, trust, relationship, confidence, clause, overlap, corridor, settlement, project, action, administration, intelligence, diaspora, and rival-ledger fields are contextual support rather than additional primary meters.

The action budget is eight family-page buttons in the action phase, five roster selectors, five prepared-state selectors, nine regional presentation selectors, four diaspora-origin selectors, and four diaspora-skill selectors; family buttons open the existing action-family page and do not execute an outcome, while the other selectors update existing bounded cursor or quote state.

The visible-state budget keeps the central regional phase to nine overlay choices plus up to five prepared states and the action phase to eight family choices, with supporting values kept adjacent to the panel that explains them.

The background coverage map is intentional: the header plate owns title and values, the left frame owns member cards and dossier, the regional frame owns the overlay grid and state list, the rival frame owns the warning ledger, the diaspora frame owns origin and skill selectors, the project frame owns progress and capacity, and the action-family tabs own the eight family controls.

## Layout change

Before the repair, `scale = 0.82` overlay buttons and `scale = 0.72` diaspora buttons were given their already-scaled source positions and sizes, so the MCP layout resolver placed them left/up of their painted regions and displaced the diaspora selectors into the centre of the window.

The repair preserves the intended text scale and sprite IDs while compensating the source geometry: overlay buttons now use positions `(412,307)`, `(532,307)`, `(651,307)`, `(412,349)`, `(532,349)`, `(651,349)`, `(412,390)`, `(532,390)`, `(651,390)` with size `112 by 34` and `scale = 0.82`.

The four origin buttons now use positions `(931,461)`, `(1033,461)`, `(1136,461)`, `(1239,461)` with size `97 by 33` and `scale = 0.72`, and the four skill buttons use the same x positions at `y=539` with the same size and scale.

The post-layout MCP rectangles resolve to overlay row one at approximately `(337.84,251.74)` with `91.84 by 27.88`, rows two and three at `y=286.18` and `y=319.80`, and diaspora origin selectors at approximately `(670.32,331.92)`, `(743.76,331.92)`, `(817.92,331.92)`, and `(892.08,331.92)` with `69.84 by 23.76`; the skill row resolves to the same x positions at `y=388.08`.

All repaired selectors remain `clickable = true` and `visible = true` in the post-change layout artifact, so painted controls and click regions now coincide in the offline layout model.

## State and resolution matrix

The post-change render covered the state IDs `default-normal`, `default-hover`, `default-selected`, `default-locked`, `default-disabled`, `default-warning`, `default-active`, `default-completed`, `default-empty-list`, `default-full-list`, `default-minimum-value`, `default-maximum-value`, `default-long-text`, and `default-missing-localisation`.

The post-change render covered the base 1920 by 1080 route and explicit resolution-scale routes for 1366 by 768 and 2560 by 1440 at `uiScale = 1`; the returned 1366 route ID was `default-1366x768-1` and the returned 2560 route ID was `default-2560x1440-1`.

Member and state selector visibility remains data-driven by the existing prepared arrays, so empty, partial, full, selected, disabled, warning, and completed states are represented by the state matrix but live values still depend on the parent-owned decision context.

## Pre-change MCP evidence

The pre-change `hoi4.gui_inspect` call used `windowName = "africa_charter_window"` and `scenario.id = "default"` and returned `GUI_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7a01ec5a0e4805c3097830405a3a5a920f43e1659e87b9661303c6f642c540a/0f3b36f0399ea78d46725bced87e3836d52162f83fb8999deed4196e243e4d8a/gui-inspect.4f664932032b5432.json`.

The pre-inspect reported 87 inspected elements, 59081 nodes, 129472 edges, 24820 elements, 25839 sprites, 208 fonts, and 83 scripted GUIs, with fidelity counts of 837 modelled, 7 approximated, 133 ignored, 6 missing, 54 unsupported, and 13 unresolved.

The pre-change 1920 render root was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/425864770f020dc23e83dfc8c7f9e5a8420696d51769c3013dfb496e272aefe8/`; the full SVG and PNG were `.../6181a1825f119c37fe6e54ea09be048e0bcf66244f8180b334ca85a6d2623cd8/africa_charter_window-full.svg` and `.../8e5f941a6699f173b0911927c15d0a2ce70b59cc35f370a9d0eb0c6ef4231cd1/africa_charter_window-full.png`.

The pre-change 1366 render root was the same artifact root with resolution route `default-1366x768-1`; its full SVG and PNG were `.../9b4899bc96dfe99974b6eefa43f48e3bb6d16b0f27706472fd8f20f57e03499a/africa_charter_window-full.svg` and `.../ce74905c375c5ecaf8d3d8ae76e921a61c332d2c48eef915de86946a8095648d/africa_charter_window-full.png`.

All 14 requested pre-change states rendered successfully at the base and 1366 routes, and the pre-change layout JSON showed overlay one at approximately `(277.16,206.64)` with `75.44 by 22.96` and diaspora origin one at approximately `(482.40,239.04)` with `50.40 by 17.28`, confirming the scale-induced displacement.

The pre-change event-local layout diagnostics contained 32 warnings, mainly the offline `GFX_flag_small2` masking limitation and the vanilla `GFX_tiled_window_transparent` resolver issue; the global source graph reported 1902 unrelated blockers and 178 overlaps.

## Post-change MCP evidence

The post-change `hoi4.gui_inspect` call used the same exact window and scenario and returned `GUI_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1d4ea30f50e5e7bfa2278c154ba44741936b8c2c36e96a8deb54fb1a8142a632/453af0f76d22114ec2778882aaee745f2a659748475d498a787e730c046c0d66/gui-inspect.eab478ecc98355b2.json`.

The post-inspect retained 87 inspected elements and the same fidelity counts, while the global graph reduced unrelated blocker reports to 1900 and overlap reports to 170; these global diagnostics are not evidence of an event-local gameplay or click-region failure.

The post-change 1920 render root was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9d460bf7ed1aa7c06175b6136e09c9e746a7db24fb52c09b53c824985f373603/`.

The post-change full SVG and PNG were `.../3ea2a4b28a1a2ddd3a7269a9f1504068ed88f4dfba636c6f43f7f07266ad3b89/africa_charter_window-full.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b3f870c7f06d563005dea4fa4b76afd0dd3d6463f57a6f0e4be85018db61ce3/5c6b60ba58da917a258d68a3210d90009d844fa0103ce2c79e7189069c9d1b57/africa_charter_window-full.png`.

The post-change cropped, annotated, click-region, source-map, hierarchy, layout, fidelity, validation, state-matrix, resolution-scale, and comparison artifacts were all returned under that render root, including layout JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7e49167302dc608be4edad422d7912b7a3c47f801c7f35aa894496e3ff22dfc/8b3d0b68a9103d687cb4cd0438d8d53a7d84bfe84da7767a8862f5049b8d9919/africa_charter_window-layout.json`, click-region PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f88611c268255e409e7f65907ada2cd79ca4b243a013893d694cf201e9016066/cbe62faf64589e306a1f4741894a4675a2b1570b791b144118db3bfb45064c60/africa_charter_window-click-regions.png`, hierarchy SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5da8c6da1af5477466f7153c257ea23d8a0a726ec663aff91e4aec9a39f5b901/72e9bfa5b4dac19d54389152446a36be8f2a015f2e010b12262cfd5843527748/africa_charter_window-hierarchy.svg`, and state matrix JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ccca56300c6a7cc4f48b5ac4c902937efbb5e49871556999abc13d984a520bfa/976a19e95bbb9480bed2073fe4d966d6e80aa5bbc1e692c1b2b935e9b17b71e7/africa_charter_window-state-matrix.json`.

The post-change 1366 resolution-scale artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a2ffd179342c1233dccb39ee622c43e84b9a88b49d6291d8fd91115c2bd18942/abdd81f447c119e5d89e044cb0a66e3aff2e256f1fdea85f0dd817ca4b881dea/africa_charter_window-resolution-scale.json`, and the 2560 resolution-scale artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2b37f38b18995838413ff0d397d5dbf01fa94c960cc42c9dc9a241f7dd895dc5/8b07221f0abef0e41c9214a51e638e39d6bfef7dba91ca86fc17a71d3d7989bf/africa_charter_window-resolution-scale.json`.

The post-change state matrix reported all 14 requested state scenarios, and the resolution-scale artifacts reported `default-1366x768-1` and `default-2560x1440-1` at the requested dimensions.

The same-scenario MCP comparison artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9adc158e6281fc052f521427df898f2b3c8e9cd0fd90224c46f9d285479354c/685ce7182c4793d820fdbec4d32e669f90fc4cac9b3bf531c291e364858acf45/africa_charter_window-comparison.json` and reported `changedPixels = 0` and `changedRatio = 0`; this is the tool's same-scenario comparison, not a pre/post source-image comparison, so the before-to-after conclusion is based on the pre/post inspect graphs and measured click rectangles above.

The post-change event-local diagnostics remained the expected 32 offline warnings, with no scale-induced displacement and no event-local click-region mismatch reported for the repaired controls.

## Rewrite route and direct patch record

The required `hoi4.gui_rewrite` route was attempted after inspection and rendering, but the adapter rejected safe source and patch forms before producing an applicable rewrite.

The source-mode attempt returned `source is required in source mode` together with `patch fields accepted only in patches mode`, the stale hash attempt returned `GUI_SOURCE_STALE`, the correct source hash `743D07F59A082325A2D1FD851CEAC6D45CB7997A84040B07F6F5401AAA1F5540` with composite ranges returned `GUI_UNSAFE_PATCH_RANGE`, and scalar or 68-patch forms returned `REWRITE_STRUCTURE_LIMIT`.

The layout was therefore patched directly in the parent-granted `interface/012_africa_charter.gui` file using the bounded coordinate changes above; no gameplay, scripted-GUI effect, GFX registration, or localisation change was made to work around the adapter limitation.

The resulting GUI source SHA-256 is `A1AB9DB83542EA41DDF7005601A7E57E0A847DA66F03C1F5F6FABDA978B7CB1E`.

## Assets and unresolved renderer limitations

The existing twelve static event-owned textures and the two animated frame sheets with static fallbacks remain registered under the GFX identifiers above, and no asset handoff was routed from this layout-only tranche.

The offline renderer still reports `GFX_flag_small2` as partially unsupported because flag masking is not modelled, and it reports `GFX_tiled_window_transparent` as missing because its resolver does not normalize the vanilla path even though the installed vanilla texture exists at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/tiled_window_transparent.dds`.

Dynamic localisation variables and live state-dependent visibility are not executed by the offline renderer, so placeholder values in the static render are expected and are not a reason to alter the event-owned localisation or gameplay state.

No missing event-owned binary asset was introduced by this tranche, no fake or dead button was added, and no generic background or placeholder art was substituted.

## Parent-owned follow-up and limits

The parent retains ownership of action costs, effects, decision execution, immutable diaspora payload copying for Actions 52 and 54, AI selection, balance, runtime save-state behavior, and live in-game validation.

The parent should review the direct-patch result, decide whether to retain it despite the unresolved `hoi4.gui_rewrite` adapter route, and integrate this handoff with the final Event 012 acceptance record.

No shared event log, event-details framework, settings UI, super-event framework, generic registry, unrelated scripted GUI, event outcome, AI weight, probability, cost, or action scope was changed.

Simplifications and blockers: the GUI MCP rewrite remains unresolved because of the adapter errors above, the offline renderer retains the documented vanilla texture and dynamic-state limitations, and no claim of live in-game completion is made.
