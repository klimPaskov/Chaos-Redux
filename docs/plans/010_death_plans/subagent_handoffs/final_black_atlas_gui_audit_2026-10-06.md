# Event 010 Black Atlas GUI handoff, 6 October 2026

Disposition: the accepted four-tab native implementation is present. Required production GUI visual acceptance remains unresolved because the post-change GUI MCP inspect and render calls returned Transport closed without artifacts.

The user authorized the Event 010 release audit and G5/G6 fixes through the parent. The parent accepted preserving all current Atlas values in four native tabs, limiting each visible pane to four mechanic values, adding a native Close button, and keeping Book conditional. The parent updated the accepted design in docs/specs/010_death_specs/specs/010_death_decisions_ui_ai.md, lines 234-255.

The larger six-panel Map, Census, Coasts, Line, Compact, and Forbidden Methods proposal remains unresolved. Its presence in the earlier spec did not authorize that broader redesign, and this implementation does not claim it.

## Ownership and entry path

The Black Atlas belongs to Event 010 Death. The accepted spec names it as a custom Death interface, common/decisions/categories/010_death_categories.txt attaches death_black_atlas_scripted_gui to death_country_containment_category, and the view uses Death scoped identifiers and visibility rules.

The entry decision is death_open_black_atlas in common/decisions/010_death_decisions.txt. The parent-owned current decision hides it while death_black_atlas_open is set, has no re-enable lock, remains human-only, has no declared cost, and has AI weight zero. Closing clears the open flag, so the player can reopen the view immediately.

The category registration remains at common/decisions/categories/010_death_categories.txt, line 19. The scripted GUI is death_black_atlas_scripted_gui in common/scripted_guis/010_death_black_atlas_scripted_gui.txt. It uses decision_category context and death_black_atlas_container.

The window is visible only to a non-AI player while death_black_atlas_open is set, after public reveal, and before Death is defeated. The window has no gameplay costs or gameplay-changing buttons.

## Implemented layout and interaction

The main container remains 520x236 and retains GFX_death_black_atlas_background and GFX_death_black_atlas_header_animated. The background, animation, sprite registration, and all DDS files were left unchanged.

The title remains at x=22, y=13. Its maxWidth is now 450, leaving an 8-pixel gap before the native Close control at x=480, y=8. The Close sprite is the installed GFX_closebutton at 32x33. Its click effect clears death_black_atlas_open and all three tab state flags.

The tab strip uses the installed GFX_tab_small_116 texture. Its 232x36 sheet contains two 116x36 frames. Frame 0 is used for a normal tab and frame 1 for the selected tab. The buttons sit at x=22, 142, 262, and 382, y=46.

Seas is the default when all three tab flags are clear. Fronts, Compact, and Book each set one country tab flag after clearing all three. The normal and selected button elements are paired by visibility triggers, so at most one control for each logical tab is visible.

Book is visible only while the existing forbidden-office condition is true. If Book loses that condition while selected, its button and pane hide and Seas becomes the selected fallback. Closing clears the open flag and all three tab flags. The opener also clears the three tab flags before setting the existing timed open flag.

The four logical tab actions plus Close are the five simultaneous in-window actions. Paired normal and selected button elements reuse each tab action and do not add simultaneous choices. All actions are navigation or close controls. The surface has zero spendable cost types and no cost texticons.

| Pane | Retained values | Visible mechanic value count |
| --- | --- | --- |
| Seas | Stage, consumed states, consumed population band, and coast risk | 4 |
| Fronts | Watch network current, Watch network maximum, jump surcharge, and front readiness | 4 |
| Compact | Quarantine line status, compact status and cohesion, and world footholds | 3 |
| Book | Existing forbidden-office status | 1 |

Watch current and maximum count separately. Every row is built from native label and value text boxes. The labels start at global x=22 with maxWidth 160. Values start at global x=194 with maxWidth 304, leaving a 12-pixel gutter after the label field.

The pane area is x=22, y=82, size 476x112. The Seas row positions are local y=0, 22, 44, and 66. Fronts has three rows, Compact has three, and Book has one. The final Coast and Book label/value boxes allow 26 pixels of height. The footer remains at x=22, y=206 with maxWidth 478 and maxHeight 22. Its text is Coasts, watches, and fronts against Death., 42 characters.

The four tab labels are Seas, Fronts, Compact, and Book. Each has a short pane-specific tooltip. Values continue to use the existing GetDeathAtlasStage, GetDeathConsumedPopulation, GetDeathAtlasCoastRisk, GetDeathAtlasLineStatus, GetDeathAtlasCompactStatus, and GetDeathAtlasForbiddenStatus scripted localisation, plus the existing global display variables.

## Reference images and acceptance

The accepted source-based reference is in docs/plans/010_death_plans/subagent_handoffs/final_black_atlas_gui_audit_2026-10-06_evidence/reference/acceptance.md. The default Seas and conditional Book references use the actual Atlas background and header previews and the installed vanilla tab and Close textures.

The parent reviewed the 1040x472 Seas and Book references. The initial Seas preview placed the population value too close to its long label. The value column was moved to x=194 for all rows, the Seas reference was rerendered, and the parent reviewed the corrected gutter before the GUI source edit. The corrected final Seas preview is black_atlas_tabs_seas_reference_final_preview_1040x472.png. The Book preview is black_atlas_tabs_book_reference_preview_1040x472.png.

The source-based reference mapping uses a native label box at x=22 with width 160 and a value box at x=194 with width 304. The reference text uses a synthetic 350K population and the source getter result watch network holding for watch strength 5. Reference typography is schematic. The reference images do not establish production font metrics or production render acceptance.

The installed vanilla button precedent is C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/countrydiplomacyview.gui, lines 192-216 for tab buttonType definitions and lines 910-919 for its native Close button. The tab sprite is registered in interface/general_stuff.gfx, lines 347-352 as GFX_tab_small_116 with two frames and uses gfx/interface/tab_small_116.dds. The Close sprite is registered in interface/general_stuff.gfx, lines 201-205 and uses gfx/interface/closebutton.dds.

The offline Interface modding section buttonType was read locally at lines 227-249. It documents buttonText, buttonFont, frame, quadTextureSprite, clicksound, and pdx_tooltip. The offline Scripted GUI modding Effects and Triggers sections were read locally at lines 179-204. The installed common/scripted_guis/_documentation.md section was read at lines 18-92. The installed effects_documentation.md flag sections were read at lines 2792-2797 and 6730-6735.

The Black Atlas textures exist at gfx/interface/death/black_atlas/death_black_atlas_background.dds, death_black_atlas_header.dds, and death_black_atlas_header_animated.dds. No Black Atlas specific asset manifest or gfx_handoff.md was found under docs/assets/010_death. No GFX file or runtime texture was changed.

## Files changed and source identities

| File | SHA-256 at handoff | Change |
| --- | --- | --- |
| interface/010_death_black_atlas.gui | 884a6c83f0593035d9a24a0ac01344fecc590b84a4f160dcfc5f84e4d00ff399 | Four tab pairs, four value panes, native Close button, aligned value fields, and title width adjustment |
| common/scripted_guis/010_death_black_atlas_scripted_gui.txt | a2721ceb482d74210cbf1a2cabeab99bfe636026fe810acbbe9ba02f2fbbe0f0 | Tab and Close effects plus visibility triggers |
| common/scripted_effects/010_death_effects.txt | 7bbcc7dcde966c73ede0886193cf9965387520f96689c02da2577e29fcead790 | Three GUI tab state resets in death_decision_open_black_atlas_effect |
| localisation/english/010_death_l_english.yml | 6bcdd877df8006b7a5068280ae272767e0d450bb309333d12415a0a0b35aae38 | Four pane labels and values, four tab labels and tooltips, existing header and footer |
| common/decisions/010_death_decisions.txt | d734796e6aca2ad158ddfcd3c560ed52ba123b3de62e28d0f60cce1fef97800e | Parent-owned opener visibility and cooldown update, not edited by this worker |
| common/decisions/categories/010_death_categories.txt | 5c02b9a6e6f453b15d78ac910e712d46703da599e11eb95edd45f65baca5b80d | Existing Event 010 category attachment, not changed |
| interface/010_death.gfx | 6b413b300a36ca2a2bb9a04e698b3c460284ba5ad4ebf7ce94aa3a71e48d38d0 | Parent-owned registrations, not changed |
| common/scripted_localisation/010_death_scripted_localisation.txt | ba77c54a48601ce4d17d67f2fdd8b7a46402655b95a8e5e69c6142731528af46 | Existing Atlas getters, not changed |
| gfx/interface/death/black_atlas/death_black_atlas_background.dds | 3897dcee2a07fa11ea385e0bc2b8df430453c0460696ee85b09326866236acfb | Existing background, not changed |
| gfx/interface/death/black_atlas/death_black_atlas_header.dds | f24c09c2f6fa638d718524744abfb327e1da6e3b2fa1972d8c2abdcae2337bb3 | Existing static header frame, not changed |
| gfx/interface/death/black_atlas/death_black_atlas_header_animated.dds | 37037837cc0b01606771aa1a8c992154c005f3337f659703a3be79681eaf6026 | Existing eight-frame header sheet, not changed |

The localisation hash immediately before the tab redesign was 9ff624c5e1209f6f2b86a6d32d36a786c91cc7587f92f5dc2301c1b8703e11ab. That source already contained the accepted 42-character footer copy.

Exact pre-layout source snapshots are in docs/plans/010_death_plans/subagent_handoffs/final_black_atlas_gui_audit_2026-10-06_evidence/source_before. Their SHA-256 values are:
- interface/010_death_black_atlas.gui: db33c8f417752b965531f88f10e330601d7bee4015dbfb533fc9f3cdca4740e3
- common/scripted_guis/010_death_black_atlas_scripted_gui.txt: 2097ce3409da89a96d3fcaef4ce144540501c076c2555d0aef9494062cdfc95e
- localisation/english/010_death_l_english.yml: 9ff624c5e1209f6f2b86a6d32d36a786c91cc7587f92f5dc2301c1b8703e11ab
- common/scripted_effects/010_death_effects.txt after the approved opener reset: 7bbcc7dcde966c73ede0886193cf9965387520f96689c02da2577e29fcead790

The parent-owned decision and GFX hashes include shared workspace changes. This worker did not edit, stage, or commit those files.

## MCP calls and visual evidence limits

The parent supplied the earlier inspection artifact URI:
hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0409f19d138b85c4eb5080ff1033a85647d4b177f3340b59c0928c23ce106ff7/dcf11512a2c7b63b2f9a2f3d320e6aefd1fe842f3729aec28f985fcf40832fc9/gui-inspect.0ba93b175482e098.json

A read_mcp_resource call on server hoi4_agent_tools returned Artifact provenance manifest is unavailable. The JSON and its rendered detail were not recoverable.

The parent reported four prior fidelity gaps and seven visible overlaps. The specific details of three fidelity gaps and the seven overlapping element pairs could not be recovered. The parent also reported an animated header static fallback warning. Although interface/010_death.gfx contains GFX_death_black_atlas_header pointing at the existing static DDS, the inherited warning remains unresolved until its artifact can be reviewed. No new alias or GFX registration was added.

The pre-layout gui_inspect attempt on death_black_atlas_container used the explicit low and Book-closed fixture, disabled generated scenarios, and exceeded the 60-second client bound at cell 13 without returning a tool result. The pre-layout gui_render used that fixture at 1920x1080 and 1366x768, UI scale 1, and normal state. It exceeded the 60-second client bound at cell 14 without returning an artifact.

Two earlier text-only stage attempts were also bounded at 60 seconds. The baseline gui_render at cell 14 and the post-footer gui_render at cell 28 returned no result before client observation ended. The post-footer gui_inspect at cell 33 also returned no result. These calls predate the four-pane redesign and do not serve as post-design visual evidence.

The post-design gui_inspect selected death_black_atlas_container with the explicit Seas, Fronts, Compact, Book-open, and Book-hidden-fallback fixtures, generatedScenarios disabled, and no country record. It returned Transport closed immediately with no diagnostics, revision, or artifact.

The post-design gui_render used the same five fixtures, normal state, and 1920x1080 and 1366x768 at UI scale 1. It supplied sourceBaseline for interface/010_death_black_atlas.gui using the saved pre-layout source. The call returned Transport closed immediately with no rendered image, source revision, manifest, or comparison artifact.

One script_validate call checked the country-scoped tab flag effects against installed game documentation. It returned Transport closed and no validation result. No retry was made.

The earlier buttonType reference_search and source_lookup batch ended at its 61-second client bound in cell 47 without a result. The relevant offline wiki and vanilla files were read directly instead. The connected service version was reported by the parent as 3.8.1 and was not independently queried by this worker. No standalone GUI compare tool was exposed. No refresh field was exposed or sent.

The production GUI render remains the required one-to-one visual acceptance surface. No post-change production render was returned, so alignment, state transitions, clipping, z-order, click-region quality, and the seven inherited overlap diagnostics remain unverified. The two source-based reference composites are not substitutes for that evidence.

## Scenario and state matrix

The explicit fixture date was 1936.1.1. Each fixture used an id, date, flags map, and variables map. No country record or scenario.values override was sent. The sample numbers are declared text-fit assumptions, not campaign observations.

| Scenario ID | Selected pane and flags | Display input assumptions | Intended visible values |
| --- | --- | --- | --- |
| 010_death_atlas_seas_default | Atlas open, public reveal true, defeated false, no tab flags, and all forbidden flags false | States 2, population 350K, Watch 5/10, surcharge 20%, readiness 10, footholds 0 | Stage, states, population, coasts |
| 010_death_atlas_fronts_high | Atlas open, public reveal true, defeated false, Fronts flag true | States 999, population 999M, Watch 10/10, surcharge 150%, readiness 100, footholds 99 | Watch current and maximum, surcharge, readiness |
| 010_death_atlas_compact_coherent | Atlas open, public reveal true, defeated false, Compact flag true, compact formed | Cohesion 10, readiness 100, footholds 99 | Line status, compact status, footholds |
| 010_death_atlas_book_open | Atlas open, public reveal true, defeated false, Book flag true, death_black_book_opened true, and death_black_book_discredited false | Existing forbidden getter branch | Forbidden office status |
| 010_death_atlas_book_hidden_fallback | Atlas open, public reveal true, defeated false, stale Book flag true, and all six forbidden visibility flags false | Low Seas values | Seas fallback remains visible and Book control is hidden |

The numeric inputs use global.death_consumed_states, global.death_consumed_population, global.death_watch_network, global.death_watch_network_max_display, global.death_watch_network_jump_cost_percent_display, global.death_front_readiness, and global.death_world_end_footholds. The Compact fixture uses global.death_compact_cohesion and the global death_living_compact_formed flag.

The post-design MCP requests could not observe any state. Hover output was not separately requested because the live render route returned Transport closed. Disabled and warning pane states do not exist in this information-only window. The hidden Book and invalid Book fallback remain unverified by production render.

## Value, action, text, and cost budgets

All 11 original mechanic values remain present across four mutually exclusive panes. The maximum simultaneous visible value count is four. Fronts counts Watch current and maximum separately.

The maximum visible action count is five: four tab choices plus Close. Each tab's normal and selected frame variants share one logical action, and only one variant is visible at a time.

The window displays no gameplay costs and contains no spendable resources. Cost count is zero and no cost texticons are required. The tabs and Close only change or clear Atlas UI state.

Each pane uses short native label/value rows. Labels use 160 pixels at x=22, values use 304 pixels at x=194, and the 12-pixel field gap separates the longest label from its value. The Book pane has one row. The footer remains a single 42-character line.

## Evidence file inventory

The handoff is docs/plans/010_death_plans/subagent_handoffs/final_black_atlas_gui_audit_2026-10-06.md. All reference and source snapshot files are below docs/plans/010_death_plans/subagent_handoffs/final_black_atlas_gui_audit_2026-10-06_evidence.

The reference directory contains acceptance.md, black_atlas_footer_reference.svg, black_atlas_tabs_seas_reference.svg, black_atlas_tabs_seas_reference_embedded.svg, black_atlas_tabs_book_reference.svg, and black_atlas_tabs_book_reference_embedded.svg.

The final parent-reviewed composites are reference/black_atlas_tabs_seas_reference_final_520x236.png, reference/black_atlas_tabs_seas_reference_final_preview_1040x472.png, reference/black_atlas_tabs_book_reference_reference_520x236.png, and reference/black_atlas_tabs_book_reference_preview_1040x472.png.

Earlier reference iterations are retained as superseded evidence: reference/black_atlas_tabs_seas_reference_reference_520x236.png, reference/black_atlas_tabs_seas_reference_preview_1040x472.png, reference/black_atlas_tabs_seas_reference_spaced_520x236.png, and reference/black_atlas_tabs_seas_reference_spaced_preview_1040x472.png.

The inspected visual inputs are reference/atlas_background_source_preview.png, reference/atlas_header_static_source_preview.png, reference/vanilla_close_button_review.png, reference/vanilla_tab_2frames_preview.png, and reference/vanilla_tab_small_116_review.png.

The pre-layout source snapshots are source_before/interface/010_death_black_atlas.gui, source_before/common/scripted_guis/010_death_black_atlas_scripted_gui.txt, source_before/common/scripted_effects/010_death_effects.txt, and source_before/localisation/english/010_death_l_english.yml.

## Remaining gates and ownership

The parent owns the opener decision change that hides Open the Black Atlas while the view is open and removes its former re-enable lock. The parent also owns final source integration, release qualification, and commit.

Pending user live-consumer evidence includes opening the Atlas to Seas, selecting each available tab, confirming Book visibility follows its existing forbidden flags, clearing Book eligibility while selected to verify Seas fallback, then closing and immediately reopening to confirm the default returns to Seas. The user owns that live validation.

No game was launched and no desktop application window was used for testing. No GFX, texture, cost, AI, or shared UI framework source was changed by this worker. No skill was created or updated. Skills used were chaos-redux-scripted-gui, chaos-redux-decisions-missions, chaos-redux-events, chaos-redux-event-assets, chaos-redux-frame-animation, and chaos-redux-subagents. The ImageGen skill was read, but no generated art was used because the exact source textures and native button frames provided the accepted reference.
