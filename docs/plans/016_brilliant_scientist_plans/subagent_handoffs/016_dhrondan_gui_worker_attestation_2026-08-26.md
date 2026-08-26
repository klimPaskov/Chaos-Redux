# Event 016 Kruger Directorate GUI worker attestation, 2026-08-26

## Scope, ownership, and result

This attestation covers Event 016, `brilliant_scientist`, and only its event-owned Directorate decision-category attachment.
The decision category `brilliant_scientist_directorate_category` declares `scripted_gui = brilliant_scientist_directorate_scripted_gui` in `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt`.
That scripted GUI uses `context_type = decision_category` and resolves `window_name = "kruger_directorate_container"` in `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`.
The accepted Event 016 design in `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_2_host_directorate_and_decisions.md` assigns Mandate, Dependence, Exposure, Project Capacity, Kruger's profile, and a broad government-control summary to this event-owned surface while ordinary decisions remain the gameplay action surface.
Independent Capacity and Grievance remain hidden as required.

No GUI, scripted-GUI, GFX, sprite, localisation, gameplay, decision, or asset source was changed.
The active compact implementation has no source-supported overlap, clipping, symmetry, density, or click-region defect that justifies a speculative rewrite.
This is an evidence-only handoff and does not claim whole Event 016 completion or in-game completion.

No shared Event Log, Event Details, settings, options, super-event, registry, generic debug, or unrelated interface was inspected or modified.

## Exact identifiers and source surfaces

- Event entry root: `chaosx.nr16.1`.
- Decision entry: `brilliant_scientist_directorate_category`.
- Scripted GUI: `brilliant_scientist_directorate_scripted_gui`.
- Root layout window: `kruger_directorate_container`.
- Presentation containers: `kruger_directorate_compact_panel` and `kruger_directorate_full_panel`.
- Presentation controls: `kruger_directorate_open_button` and `kruger_directorate_close_button`.
- Dynamic profile sprites: `GetBrilliantScientistDirectorateProfileFrameSprite` and `GetBrilliantScientistDirectoratePortraitSprite`.
- Dynamic meter sprites: `GetBrilliantScientistDirectorateMandateSprite`, `GetBrilliantScientistDirectorateDependenceSprite`, `GetBrilliantScientistDirectorateExposureSprite`, and `GetBrilliantScientistDirectorateCapacitySprite`.
- Layout: `interface/016_brilliant_scientist_directorate.gui`.
- Presentation wiring: `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`.
- Sprite registration inspected: `interface/016_brilliant_scientist_directorate.gfx`.
- GUI localisation: `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml`.
- Decision entry inspected: `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt`.
- Existing event-owned background sprites: `GFX_kruger_directorate_background` and `GFX_kruger_directorate_compact_header`.
- Existing event-owned controls: `GFX_kruger_directorate_open_control` and `GFX_kruger_directorate_close_control`, each registered as a four-frame `buttonstate.lua` sheet.
- Existing event-owned meter families: `GFX_kruger_directorate_mandate_*`, `GFX_kruger_directorate_dependence_*`, `GFX_kruger_directorate_exposure_*`, and `GFX_kruger_directorate_capacity_*`.

The dormant `brilliant_scientist_directorate_gui_tab_*`, project, facility, foreign, and sovereignty localisation entries are not attached to any element in the current `kruger_directorate_container`.
They are remnants of the superseded dashboard and do not create painted states or click regions.
Removing them would be unrelated cleanup outside this attestation.

## Required references reviewed

The required offline wiki snapshot pages were consulted before source review: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, and Scripted GUI modding.
Installed vanilla documentation was consulted in parallel, including `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, and `script_concept_documentation.md`.

The exact vanilla precedent was the Soviet paranoia decision-category attachment:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/sov_paranoia_system_scripted_gui.gui`.

That precedent uses `context_type = decision_category`, one named window, and state-driven presentation properties while ordinary decisions remain outside the visual status surface.

## Pre-change MCP inspection evidence

The required exact-window route was run with `windowName = kruger_directorate_container` and workspace `mod_chaos_redux_ea3b2d67c2c0`.
The primary scenario was `event016_dhrondan_attestation_prechange`.
Related scenarios were `event016_dhrondan_collapsed`, `event016_dhrondan_expanded`, `event016_dhrondan_project_pressure`, `event016_dhrondan_facility_pressure`, `event016_dhrondan_foreign_pressure`, and `event016_dhrondan_authority_pressure`.
The inspection returned `GUI_INSPECTED` with status `ok`.

Exact artifact probe:

- Scenario: `event016_dhrondan_attestation_artifact_probe`.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7773e9a94e5f46dcfcc13649534f130b179fac8695618fa59744986158b4374a/7291dbc76ab889d8485f4de2b4b8aec4cf4f3bd86f9ca15ab64a2f8f04d962a4/gui-inspect.017d249c791c0735.json`.
- Artifact SHA-256: `7773e9a94e5f46dcfcc13649534f130b179fac8695618fa59744986158b4374a`.
- Inspected Event 016 element count: 22.
- Fidelity counts: 194 modelled, 5 approximated, 7 ignored, 2 missing, 2 unsupported, and 7 unresolved.

The inspection response also reported workspace-wide source-graph and validation diagnostic truncation.
The retained inline examples were dominated by unrelated Event 003 and Event 005 sprite collisions.
This global diagnostic ceiling is not evidence of an Event 016 layout defect, and this worker did not inspect or modify those unrelated surfaces.

## Pre-change MCP render evidence

The required render route was run for 1280x720 and 1920x1080 at UI scale 1.
The requested generic states were normal, hover, selected, active, disabled, warning, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation.
The related collapsed, expanded, project-pressure, facility-pressure, foreign-pressure, and authority-pressure scenarios used the identifiers listed above.
The route returned `GUI_RENDERED` with status `ok` and one packaged artifact.

A bounded normal-state artifact probe was also run:

- Scenario: `event016_dhrondan_attestation_normal_artifact`.
- Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efb93e06f3584a666ca7a109061b9b9a929f3bf3b75e7965d96252280e504cce/7c5cff6fb82157781f4fc6385ccda0a6fc8fb7b91dd2e8143bcb91f09f511279/kruger_directorate_container-full.svg`.
- Artifact SHA-256: `efb93e06f3584a666ca7a109061b9b9a929f3bf3b75e7965d96252280e504cce`.
- Artifact size: 727,134 bytes.

The packaged SVG metadata records hierarchy, nested offsets, inherited clipping, sprite-frame resolution, font metrics, tooltips omitted from offline painting, and decision-category context.
It also records deterministic font substitution, missing offline glyph data for the title strings, and primary-frame-only approximation for the four-frame open and close controls.
The renderer returned `MCP_RESPONSE_TRUNCATED`, so separate crop, annotated, hierarchy, click-region, per-state, and per-resolution files were not exposed as individual artifacts in the response envelope.
The exact packaged artifact is retained above rather than treating source inspection as equivalent visual evidence.

## Layout hierarchy and background coverage map

| Background region | Intended content | GUI elements | Interaction or state | Status |
| --- | --- | --- | --- | --- |
| 500x58 compact painted header | Collapsed Directorate identity | `kruger_directorate_compact_background`, compact title, open control | Visible only with `brilliant_scientist_directorate_gui_collapsed` | Covered by the matching registered 500x58 asset |
| 500x360 full painted panel | Expanded Directorate status | full background, title, profile, four meters, control summary, footer, close control | Visible when the collapsed flag is absent | Covered by the matching registered 500x360 asset |
| Left profile inset | Kruger identity and current profile state | profile frame, portrait, profile name | Dynamic frame and portrait sprite routing | Content stays within the left column |
| Right four-row status field | Mandate, Dependence, Exposure, Project Capacity | four meter icons and four value labels | Dynamic meter sprite routing and value tooltips | Rows share one 44-pixel rhythm |
| Lower summary strip | Current institutional role and government-control state | `kruger_directorate_role_control` | Dynamic text and control tooltip | Centered inside a 428x30 bound |
| Bottom instruction strip | Points the player to the ordinary decisions | `kruger_directorate_footer` | Host or sovereign dynamic footer | Centered inside a 428x20 bound |

The root is clipped at 500x360.
The full title spans x=40 through x=400 and the close control begins at x=422.
The four meter rows begin at y=82, 126, 170, and 214, while their value baselines begin seven pixels lower at y=89, 133, 177, and 221.
The portrait/profile column ends before the meter column begins.
The role/control box at y=272 and footer at y=326 do not intersect.

## Visible-value, action, cost, and density budgets

- Visible mechanic values: four, exactly the accepted hard ceiling.
- Primary pressure hierarchy: Mandate is the lead legal-authority value, with Dependence, Exposure, and Capacity as separately colored and framed supporting values required by the accepted Event 016 specification.
- Hidden values: Independent Capacity and Grievance remain absent from the interface.
- Gameplay-changing GUI controls: zero.
- Presentation controls: one mutually exclusive open or close button in each collapsed or expanded state.
- Primary actions: zero because ordinary Directorate decisions remain below the attachment.
- Active missions or target controls: zero.
- Spendable cost types: zero.
- Texticon coverage: not applicable because this window displays no spendable costs.
- Literal resource-name fallbacks: none.
- Main explanatory paragraphs: none.
- Meter tooltips: two concise lines each, covering meaning, causes, and consequence.
- Open and close tooltips: one concise presentation-only sentence each.
- Government-control tooltip: identifies the summary and points to the ordinary decision response surface.

## State and resolution matrix

| State or scenario | Expected surface | Click region | Evidence and disposition |
| --- | --- | --- | --- |
| Expanded normal | Full 500x360 panel, profile, four meter rows, summary, footer, close control | One 36x36 close control at x=422, y=11 | MCP inspect/render route succeeded and source bounds are consistent |
| Collapsed | 500x58 header, title, open control | One 36x36 open control at x=422, y=11 | Related scenario requested and direct child visibility gates exist |
| Hover, pressed, disabled | Corresponding frame in the existing four-frame control sheet | Same 36x36 region | Sprite registration is correct, but the offline renderer exposed only primary-frame approximation |
| Minimum and maximum values | Existing low through extreme meter sprite families | No meter click regions | Requested through value extremes; dynamic tokens preserved |
| Warning and authority pressure | High Mandate or Dependence plus the government-control summary | Close control only | Requested as `event016_dhrondan_authority_pressure` |
| Project pressure | Existing active profile/meter/control summary only | Close control only | Requested as `event016_dhrondan_project_pressure`; no active Projects tab exists |
| Facility pressure | Capacity meter and government-control summary only | Close control only | Requested as `event016_dhrondan_facility_pressure`; no active Facilities tab exists |
| Foreign pressure | Exposure meter and government-control summary only | Close control only | Requested as `event016_dhrondan_foreign_pressure`; no active Foreign tab exists |
| Completed | Same compact status surface with dynamic values/profile resolved by current game state | Close control only | Generic state requested; no completed card or mission belongs to this display |
| Empty-list and full-list | No list surface exists | None beyond the presentation control | Generic states requested and correctly treated as semantically inapplicable |
| Long text and missing localisation | Existing fixed-size text bounds and renderer diagnostic overlays | Presentation control unchanged | Requested, but the package did not expose separate review images |
| 1280x720 and 1920x1080 | Same fixed 500x360 category attachment at UI scale 1 | Same local control bounds | Both resolutions requested; the response exposed one packaged SVG rather than one artifact per resolution |

The requested overview, project, facility, foreign, and authority review must not be interpreted as five active tab containers.
The accepted compact redesign removed those tabs.
Project, facility, foreign, and authority conditions are represented by existing dynamic values, profile sprites, and the control summary, while their gameplay actions remain in ordinary decisions.

## Rewrite and before/after disposition

No source defect was established, so `hoi4.gui_rewrite` was not invoked.
The required rewrite route is mandatory before an in-scope layout source change, but it is not a license to create a speculative diff when the active geometry and bindings are already consistent.
There is no separate post-change source or comparison artifact because no Event 016 source was changed.
The pre-change inspect/render artifacts are also the unchanged-source after-state reference.

## Missing assets, remaining risks, and parent-owned validation

- No missing asset was replaced, generated, or invented.
- Existing registered Event 016 art was preserved exactly.
- Separate annotated, hierarchy, click-region, crop, per-state, and per-resolution files remain unavailable from the current packaged render response.
- Offline glyph substitution prevents this pass from claiming exact title-glyph rendering.
- The offline renderer approximated the multi-frame open and close button sheets with their primary frame, so hover, pressed, and disabled appearance remains unresolved in MCP visual evidence even though registration and click geometry are source-consistent.
- Workspace-wide graph truncation prevents a clean global validation pass, but the retained inline examples point to unrelated interfaces and are not attributed to Event 016.
- Runtime consumer, decision-category placement, dynamic scripted-localisation values, and live in-game appearance remain parent/user-owned validation.
- No gameplay outcome, decision cost, AI behavior, probability weight, balance target, event effect, or ownership boundary was changed or audited.
- No simplification, fallback UI, placeholder art, fake control, guessed click region, or unapproved asset substitution was introduced in this pass.

