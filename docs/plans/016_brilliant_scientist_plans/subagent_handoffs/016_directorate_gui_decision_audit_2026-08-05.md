# Event 016 Directorate GUI and decision-category audit

## Parent resolution

The P0 width defect is resolved by rebuilding the full and compact surfaces at `500x620` and `500x58`, within the vanilla decision grid's approximately 502-pixel content width. Every authored click target ends at or before x=488, every tab ends at or before x=482, and the footer and tab panels end at or before x=486.

The GUI no longer exposes a Refresh control, and opening the panel only changes collapsed view state. Persistent government-control, project-count, facility-count, idea-lifecycle, and portrait-stage reconciliation remains owned by gameplay transitions rather than a repeatable display click.

The header presents Government Control as the primary status and Mandate, Dependence, and Exposure as its three supporting values. Capacity moved into the Projects tab. Public-value tooltips state their `0-100` range and whether higher values are safer or more dangerous. The category description and fixed tab copy were shortened for the bounded layout.

Generated replacement backgrounds reserve low-detail functional bays for the dossier, telemetry, tabs, content, and footer. Illustrated cards are used as separate visual panes rather than text backdrops. Selected tabs use a persistent disabled presentation, and the footer uses host-versus-sovereign scripted localisation.

`hoi4.gui_inspect` and `hoi4.gui_render` successfully parsed and rendered the rebuilt `kruger_directorate_container` at `1920x1080` and `1366x768`, including normal, hover, selected, disabled, and long-text states. The rendered source revision was `7a5bebe8672c0775937f34cf812473674b433f48d40aa3a0f7a9bdb03f0c2205`. The tool's aggregate failure is not accepted as a scoped Directorate defect: it includes 1,888 repository-wide GUI source-graph diagnostics and counts mutually exclusive hidden tab panels and deliberate background, portrait, and card layers as visible overlaps. The bounded layout, click-region coordinates, source registrations, and direct localisation contracts were reviewed separately.

Two audit observations remain deferred: GUI preference flags are inert after host loss but are not explicitly cleared, and the dashboard remains visible before a primary campus exists so that the facility-starting category retains a usable entry surface. These are documented lifecycle and specification discrepancies, not unwired references or repeatable reward paths.

Status: audit complete; parent resolution applied in the same tranche.

Scope: `interface/016_brilliant_scientist_directorate.gui`, `interface/016_brilliant_scientist_directorate.gfx`, `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`, the Directorate category and decision files, their selectors and localisation, the Event 016 UI asset handoff, and the relevant source specification.

The original audited dashboard was correctly intended as a read-only complement to ordinary decisions, but it could not work in its actual decision-category host. The parent resolution above records the accepted layout, art, interaction, and localisation rework.

## Evidence and validation boundary

The GUI is registered on `brilliant_scientist_directorate_category` through `scripted_gui = brilliant_scientist_directorate_scripted_gui` in `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt`.

Vanilla `interface/countrydecisionview.gui` defines the decision grid at 502 pixels wide under a clipping decision container, while `kruger_directorate_container` and both of its panels are fixed at 700 pixels wide.

This is a host-container constraint rather than a display-resolution edge case.

The parent attempted the requested `hoi4.gui_inspect` and `hoi4.gui_render` evidence, but both were blocked by `SCAN_BYTE_LIMIT`.

No MCP render artifact is claimed by this audit.

Manual source evidence was used instead: source coordinates, vanilla container dimensions, direct DDS inspection, the 64-texture asset handoff, and a parent-supplied decoded background coverage check.

Static consistency checks found all 9 GUI buttons have matching scripted-GUI effects and enabled triggers, all 21 direct GUI localisation keys exist, all 12 dynamic sprite selectors resolve, and all 64 Directorate GFX texture paths exist.

The one direct portrait sprite outside the Directorate GFX file, `GFX_portrait_KRG_doctor_warren_kruger_stage_0`, is registered in `interface/016_brilliant_scientist.gfx`.

The two inspected English localisation files retain UTF-8 with BOM.

## Issues, sorted by severity

### P0 — fixed 700px dashboard is clipped inside the 502px decision grid

`kruger_directorate_container`, `kruger_directorate_full_panel`, and `kruger_directorate_compact_panel` use 700-pixel fixed widths with clipping enabled.

The vanilla category grid only exposes approximately x=0 through x=501, so controls and text beyond that boundary cannot be read or reliably clicked on any resolution.

| Surface | Current coordinates | Result in the decision category |
| --- | --- | --- |
| Compact open control | x=646 to 682 | Completely off-screen, so a persisted collapsed dashboard cannot be reopened from its own control. |
| Full close control | x=646 to 682 | Completely off-screen. |
| Capacity meter and label | x=559 to 682 | Completely off-screen. |
| Foreign tab | x=493 to 585 | Only its leftmost 9 pixels remain in the grid. |
| Authority tab | x=590 to 682 | Completely off-screen. |
| Shared tab content panels | x=202 to 682 | Their rightmost 180 pixels are clipped. |
| Control warning | x=448 to 672 | Only its leftmost portion can remain visible. |
| Footer | x=474 to 684 | Nearly all text is clipped. |

This makes the five-tab navigation and the compact fallback non-functional in their real host.

Recommended fix: rebuild the presentation around the vanilla decision-grid width, using a responsive `100%`-width root or a fixed width no greater than the actual grid, and regenerate or recompose the 700px shell and compact header to match.

All controls and their full click regions must remain within the accepted decision-grid width, with no right-side affordance that depends on hidden overflow.

This is not safe to correct with a local coordinate nudge because the background, header, five-tab pitch, panel cards, and text contracts are all authored for the 700px composition.

### P1 — the declared read-only dashboard mutates persistent Directorate state

The source comment says that the GUI owns only view state, yet both `kruger_directorate_open_button_click` and `kruger_directorate_refresh_button_click` call four persistent-state helpers.

`brilliant_scientist_refresh_government_control` recalculates a stored score, clears and reassigns control flags, and invokes `brilliant_scientist_refresh_directorate_idea_lifecycle`, which removes and reapplies lifecycle ideas.

`brilliant_scientist_refresh_project_counts` rewrites stored portfolio counts and also invokes the idea-lifecycle helper.

`brilliant_scientist_refresh_containment_facility_count` performs an `every_owned_state` scan and writes the facility count.

`brilliant_scientist_refresh_kruger_portrait_stage` writes the stored portrait stage and invokes the current-stage portrait application effect.

The helpers appear idempotent and this audit found no direct resource grant, cooldown reset, or random outcome on repeat clicks.

They nevertheless make opening or refreshing a view capable of repairing or changing gameplay-visible persistent state, which breaches the design and leaves UI clicks as a second lifecycle entry path.

Recommended fix: move these reconciliations to existing authoritative appointment, project, facility, transfer, evolution, and cleanup effects, then reduce the GUI controls to collapse, tab, and presentation preference state only.

Do not remove the current refresh calls as a small patch without first proving every authoritative transition refreshes the caches, because removing the repair path alone could leave stale presentation or lifecycle ideas.

### P1 — source-art coverage does not reserve clear functional regions for text and controls

The decoded 700x500 background contains prominent central geometric drafting imagery and a lower-right laboratory ornament.

The existing profile, meters, Control surface, tabs, content panels, and footer cover x=18 to 684 and y=76 to 486, including most of those focal regions.

The content card overlays produce the same problem at the local level: the Projects, Facilities, Foreign, and especially Sovereignty text blocks sit directly over illustrated cards rather than independently reserved opaque text surfaces.

The Sovereignty text block spans x=222 to 522 and y=220 to 414 over the sovereignty artwork, while its singularity indicator is farther right and currently also lost to the category-width clipping.

`016_directorate_ui_asset_handoff.md` records dimensions and static asset acceptance but does not provide a functional background coverage map that reserves text, metrics, controls, and decoration.

Recommended fix: create a coverage map before regenerating the width-safe composition.

The replacement background should reserve opaque or low-detail regions for the profile, one primary control status, metrics, tab controls, content text, and the footer, while focal art stays outside those zones or is placed in a dedicated non-text visual pane.

The source-art overlap is established by coordinate and decoded-asset evidence, but live composite legibility remains unresolved because the requested MCP render could not run.

### P2 — information hierarchy and category description exceed the view budget

The top row presents Government Control plus Mandate, Dependence, Exposure, and Capacity, which is one primary metric and four supports rather than the recommended maximum of three supports.

Capacity belongs naturally to the Projects tab and should be moved there or the top line should otherwise be reduced to a primary state plus no more than three direct supports.

The four meter labels show raw integers but do not state a range, whether higher is safer or worse, or a non-colour threshold cue in the value itself.

Their tooltips explain provenance, but should also state the direction and threshold consequence in the re-layout.

The five tabs are within the intended navigation budget, and the ordinary decision list remains the action surface, so this is not a duplicate action-system finding.

The category description repeats the four public values, named causes, records, and explanatory prose beneath the embedded dashboard.

That duplicate description creates avoidable vertical pressure and is not a compact essential-values fallback at lower viewport heights.

Recommended fix: reduce the category description to a concise fallback summary and keep detailed causes in dashboard tooltips or one bounded overview panel.

### P2 — several fixed text boxes are likely to clip or collide even before host clipping

The Overview panel holds multiple headed dynamic records in 222px and 226px columns with fixed height.

The Project ledger has seven and eight dynamic rows in 126px and 128px columns respectively, including family names that can exceed the available width.

The Facilities and Foreign panels embed explanatory sentences in 188px-wide illustrated cards, while the Sovereignty panel embeds a long response explanation across a focal illustration.

All of these boxes use `fixedsize = yes` with no scroll or compact fallback.

Recommended fix: re-author each tab for one primary status, three to five short labeled rows, and tooltips or a selector for the full explanation.

Run a full-resolution GUI render and a long-string localisation pass after the re-layout to verify wrapping, clipping, tooltip reachability, and hover states.

### P3 — active-tab and sovereign-context clarity are weak

The tab sheets only provide normal, hover, pressed, and disabled states, but all ordinary tabs remain click-enabled regardless of the selected tab.

There is no persistent selected-tab visual state beyond the content panel itself.

Recommended fix: give the selected tab a distinct disabled or selected presentation with a matching tooltip, after the width-safe re-layout establishes viable controls.

The category is visible to a sovereign KRG country, while the footer says that all Directorate actions remain in the decision list below.

KRG action categories are separate, so this footer can be misleading when the same dashboard is displaying sovereign context.

Recommended fix: use a scripted-localisation footer that says where host actions or KRG actions actually appear.

### P3 — GUI preference flags have no explicit lifecycle cleanup

`brilliant_scientist_directorate_gui_collapsed`, five `brilliant_scientist_directorate_gui_tab_*` flags, and `brilliant_scientist_directorate_gui_animations_disabled` are referenced only by the GUI and portrait selector.

They do not create a gameplay exploit and remaining flags on a former host are inert because the category becomes invisible there.

Recommended fix: clear obsolete host-local view flags in the existing host-transfer and terminal-cleanup helper, while preserving only an explicitly intended KRG presentation preference if desired.

### P3 — the GUI enters earlier than the source-spec interface condition

The binding Directorate specification says the interface becomes available after appointment and primary laboratory selection, while the scripted GUI is currently visible to any human current host or sovereign KRG without a primary-campus condition.

The ordinary category should remain visible for the facility decision that creates the first campus, but the dashboard visibility should be gated separately once the re-layout is complete if the source specification remains authoritative.

The current unbuilt-facility selectors make this a source-contract discrepancy rather than a confirmed functional blocker.

## Decision category lifecycle notes

`brilliant_scientist_directorate_category` becomes visible to the current host or sovereign KRG and remains visible when empty, which gives the dashboard a valid entry point.

For a human country, the scripted GUI is visible and AI is disabled; this is correct for a display-only dashboard because ordinary decisions carry the AI paths.

The current GUI visibility does not require the primary campus, which differs from the source-spec entry condition noted above.

The full panel is the default state, while the compact panel is selected by a persistent collapsed flag.

Because the compact open control is off the real grid, a saved collapsed state is not recoverable through this GUI until the P0 layout defect is fixed.

The Authority tab correctly has its own visible and enabled trigger, `brilliant_scientist_directorate_sovereignty_surface_is_available`.

No obsolete panel can be selected through that tab when the sovereignty surface is unavailable, because the overview selector falls back correctly.

## Mission quality notes

| Owner and category | Mission family | Requirement and region | Duration | Success and failure handling | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| Current host, Directorate | `brilliant_scientist_loyalty_review_mission` | Requires the ordinary security decision and internal security section; no map region. | Centralized loyalty-review timing constant. | Timeout snapshots the current investigative state and requests the result; host loss cancels the in-progress flag. | Low; the starter has a re-enable timer and a requested-state gate. |
| Current host, Directorate | Fifteen project incident missions | A family-specific active incident; no separate map region in the mission shell. | Family-class timing constants for technical, industrial, biological, or exotic incidents. | A normal response decision can resolve the incident; timeout calls the family failure helper; cancellation clears the active modifier and marks the incident resolved. | Low; family active/resolved flags and the shared project-incident lock prevent duplicate active cases. |
| Current host, Directorate | `brilliant_scientist_sovereignty_deadline_mission` | Active sovereignty deadline; no map region. | Dynamic country variable, deliberately used because the mission timeout field is not constant-safe. | Resolution, host loss, disabled evolution, or world end cancels through the dedicated cleanup helper; timeout marks the deadline expired. | Low; activation is tied to one active deadline flag. |

The dashboard merely reports these missions and does not create a parallel mission action surface.

## Cost, requirement, AI, and route-lock notes

The nine GUI controls are view-state or presentation controls except for the problematic refresh path described above, and none asks the player to pay a gameplay cost from the GUI.

The ordinary Directorate decision files use varied political power, support equipment, trucks, trains, convoys, fuel, manpower, experience, factory, state, project-stage, and foreign-target requirements rather than a flat political-power exchange.

The sampled Directorate action files use centralized timing and cost constants, custom trigger tooltips for complex gates, cancellation for host, facility, target, and route invalidation, and matching `ai_will_do` blocks.

The static audit counted 21 AI blocks in Institutions, 6 in Facilities, 6 in Foreign, 103 in the Project Board, 3 in Synthesis, and 8 in Containment decisions.

The displayed category itself correctly has no AI behaviour because it is not an action surface.

## Localisation, tooltip, and animation notes

All direct GUI labels and button tooltips resolve, and the visible numerical values are consistently formatted as integers.

The four public value tooltips identify named current causes, but need direction and threshold meaning during the P2 information-hierarchy revision.

The three animated modules have explicit static companion textures and a user-controlled still-presentation state, so the animation fallback contract is present.

No raw script trigger is exposed to the player through the dashboard.

## Cleanup and exploit-risk notes

No GUI button grants equipment, factories, units, political power, project stages, cores, or war goals, and no direct repeat-click resource-farming loop was found.

The refresh controls are a lifecycle-integrity risk rather than an observed farming loop because they may reapply current-state ideas and portrait records through a player click.

Ordinary timed decisions and missions sampled in scope clear their action locks or incident state on cancellation or resolution.

## Concrete recommended fix order

1. Replace the fixed 700px embedded composition with a decision-grid-safe layout and regenerated shell/header/card art guided by a formal background coverage map.
2. Validate the re-layout with `hoi4.gui_inspect` and `hoi4.gui_render` at the target decision context once the scanner can process the source, and retain the artifact references and unresolved visual findings.
3. Move display-cache reconciliation to authoritative lifecycle effects, then remove the GUI refresh side effects and revise its player-facing tooltip or remove the control.
4. Reduce the top metric row and category description, then shorten each tab to an at-a-glance status with tooltip detail.
5. Add selected-tab and sovereign-footer clarity, and clean stale host-local GUI preference flags at transfer or terminal cleanup.

## Changed files and identifiers

Changed file: this audit handoff only.

No decision, mission, scripted-GUI, localisation, or GFX runtime identifier was changed.

No code patch was applied because the P0 defect is inseparable from the current generated 700px asset and layout contract, and removing refresh mutations without a lifecycle-caller proof would risk stale state.

## Remaining risks and skipped validation

Live GUI composite rendering, click-region verification, long-string wrapping, and resolution acceptance remain unverified because the requested MCP GUI inspection and render were blocked by `SCAN_BYTE_LIMIT`.

The parent should not treat the static asset handoff as live GUI acceptance until the reworked category composition is rendered successfully.

No simplification or fallback was introduced by this audit.
