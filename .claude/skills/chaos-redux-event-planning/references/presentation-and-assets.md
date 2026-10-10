# Event presentation and asset planning

Read the relevant complete sections before specifying a custom UI, super-event, visual asset family, asset prompts, or a research handoff. These are planning requirements; the owning production skills govern implementation.

## Custom UI and presentation

If the event benefits from custom UI, design one.

Describe what the player sees, how it changes, and what visual assets are needed.

Map the UI states if the UI represents pressure, route choice, threat, stage, faction cohesion, recognition, contamination, loyalty, or any other living value.

### Interactive mechanic UI and animated presentation in event specs

When an event has an important decision category, choose its presentation layer before designing a custom window. Start with an ordinary category, then apply the picture eligibility gate before testing whether a static or animated category picture is enough. Basic formatted value tables alone do not require a richer GUI. Use a richer scripted GUI or a separate mechanic window only when the system needs active visual management that normal decisions, tooltips, and one category picture cannot provide.

For a new or redesigned scripted GUI, use `chaos-redux-scripted-gui` to create reference image(s) before native implementation and carry the image-to-element mapping, supported HOI4 adaptations, acceptance basis, assets, states, and matched MCP scenarios into the implementation handoff. A plan or image file does not establish approval; record explicit user direction or parent acceptance within the authorized scope. If the named event specifically introduces a dedicated scripted GUI, include a bounded `chaosx_event_ui_worker` handoff in the implementation prompt. Name the event-owned GUI identifiers, files, entry point, layout regions, states, resolutions, decisions, assets, allowed files, and handoff path. Require the reference-image, native-layout, and layout review rules from `chaos-redux-scripted-gui`, preferring targeted MCP views with code review and local checks after the shared retry limit, which permits direct application of reviewed edits and makes `gui_rewrite` optional rather than requiring its automatic post-write/index validation to pass. Explicitly exclude the shared event log, event-details framework, settings, super-event framework, shared registries, and unrelated existing UIs.

For major events, important decision categories, custom mechanic windows, formable routes, high-chaos route reveals, active crisis meters, special leader transformations, faction boards, patron influence networks, or occult and supernatural systems, run a presentation-choice pass. The pass must choose between ordinary category presentation, an eligible static or animated picture, a compact attached display, and a full scripted GUI. Existing complex UI, meters, additional custom controls, rich interactive panels, or other animations exclude category pictures from this choice. Animation should be planned only when it clarifies a changing state or materially strengthens the category. Static presentation needs no defensive justification when it is the clearer option.

A mechanic UI spec should include:

- chosen presentation layer and why a simpler layer would be insufficient
- category picture eligibility and direction when a static or animated picture is used
- formable state-puzzle layout and exact state-piece rules when map qualification is the mechanic
- where the UI appears, such as decision category header, attached scripted GUI, custom window, event-details panel, or country mechanic panel
- what button opens or closes the window
- what values, targets, meters, cards, lists, tabs, or map states the player sees
- what buttons the player can click and what each costs
- how unavailable buttons explain missing requirements
- what scripted effects and scripted triggers own the button logic
- how AI performs equivalent actions without relying on human-only clicks
- how the UI cleans itself up after route change, tag change, annexation, civil war, peace, or event completion
- what localisation and scripted localisation the UI needs
- what static assets, animated sprites, hover states, selected states, locked states, warning states, and progress variants it needs
- what animated state communicates, such as available action, rising pressure, critical danger, selected target, active ritual, foreign influence spread, reform momentum, hidden route reveal, route corruption, or completion
- which animation surfaces are state-driven and which are decorative
- which static fallback appears when animation is disabled, unsupported, not yet produced, or hidden by route state
- exact `chaosx_event_ui_worker` scope and MCP evidence when the named event introduces and owns the UI, plus explicit exclusions for every shared interface it merely opens or references

The spec should not make an interactive window for every small modifier. Use custom UI when it improves readability, choice, atmosphere, or management of a living system.

Animation is useful when the player needs to notice a changed state without reading a long tooltip. Use it for pressure rising, corruption spreading, a council activating, an occult meter pulsing, a patron influence network changing, a formable seal becoming available, a faction board entering crisis mode, a route emblem changing after a focus, or a warning frame appearing near failure. It should not hide information or add noise.

Do not animate a category only to make it look important. Within the picture eligibility gate, strong static pictures are often better for propaganda, ideology, civil-war preparation, national preparedness, elections, treaties, and formable territory overviews. Animated category pictures follow the same gate and are appropriate when the picture itself represents active mobilization, escalating crisis, a changing map state, or route transformation. The meter, board, control, and window animations above are GUI animation examples, not reasons to add a category picture alongside them.

For each planned animated asset, the spec should define the in-game use, target surface, state logic, frame count expectation, loop behavior, static fallback, source mode, asset handoff owner, and proposed sprite names when they are known. The final animation must follow `chaos-redux-frame-animation`, meaning real source frames, a frame sheet, a static fallback, a preview GIF for review only, and a `.gfx` handoff. Do not describe a GIF, filter pulse, recolour loop, shifted still image, or transform-only mockup as the final game animation.

Leader portraits can have animated variants for major route reveals, high-chaos leaders, supernatural leaders, symbolic councils, final formables, or dramatic country transformations. The spec should say when the animated portrait appears, what static fallback exists, whether the portrait is sourced or generated, what state or route controls it, what removes or replaces it, and how the animation remains period-appropriate and readable at leader-portrait size.

## Super-event planning

If the event needs a super-event, design the super-event as part of the event's emotional and gameplay pacing.

A super-event should not be used only because something large happens. It should mark a moment that changes how the player understands the campaign, the event chain, the world state, or the stakes of the current crisis.

When planning a super-event, define:

- why this moment deserves super-event treatment
- what exact event state triggers it
- whether it is a reveal, escalation, transformation, defeat, aftermath, or world-end moment
- what the player should feel when it appears
- what the world believes has happened
- what information is still uncertain
- what image direction would fit
- what quote direction would fit
- what cultural remark direction would fit
- what audio mood would fit
- whether it needs follow-up events, decisions, or focus routes

Keep the super-event tone specific to the event. Do not make every super-event feel like the same apocalypse with a different image.

Do not fully research quotes, cultural remarks, or music inside this skill. Use `chaos-redux-super-events` for that work.

The event spec should provide enough direction for `chaos-redux-super-events` to find real quotes, meaningful cultural remarks, and suitable audio.

### Super-event text boundary and research gate

This skill is direction-only for super-event title text, `.a` button text, `.q` quote text, and any cultural reference. Do not write a final title, option, button line, quote, lyric fragment, slogan, proverb, scripture excerpt, literary allusion, or film, song, book, or game reference inside the event spec unless the exact wording has already been researched, sourced, and documented through the super-event skill or a provided source file.

If research has not been done, use neutral research gates instead of lines that could be pasted into localisation:

- `Reveal super-event title: research required`
- `Button remark: research required`
- `Main quote: research required`
- `Cultural reference: research required`

Do not include unresearched `possible line`, `sample title`, `placeholder quote`, or `temporary button text`. Implementation agents may treat those as final localisation.

Describe the desired shape instead. For example, write `short title direction about public recognition of the threat, avoiding generic apocalypse wording`, not a finished title.

Functional labels are allowed for spec structure, asset filenames, and prompt routing, but they must be neutral and explicitly non-final. Use labels such as `mainland reveal super-event`, `world-end super-event`, or `se_death_mainland_reveal`. Do not name assets, localisation keys, or prompt files after unresearched title concepts.

### Major-event defeat aftermath

When planning defeat of a major event, apply the complete [Major-event defeat aftermath](../../chaos-redux-events/references/world-end-triggerable-scenarios-and-aftermath.md#major-event-defeat-aftermath) contract: assess the crisis’s reach, duration and cost, and specify its applicable lasting consequences.

## Asset planning

The event specification should identify all important visual assets. For major events, assume every visible system needs asset planning unless the spec explicitly explains why it does not.

Consider whether the event needs:

- idea icons
- national spirit icons
- focus icons for every focus or focus-family in each mapped tree
- decision category icons
- static and animated decision category pictures for eligible simple categories that need visual identity or territorial context
- exact formable state-puzzle pieces and composed territory previews when dynamic state qualification is central
- decision icons
- achievement icons
- news event pictures
- report event pictures
- super-event images
- leader portraits
- council, committee, regency, cult, junta, or symbolic leadership portraits
- faction emblems
- flags for every new country, modified country identity, ideology variant, focus-route variant, puppet identity, and major cosmetic transformation
- UI
- animated decision category seals for eligible simple categories, mechanic-window elements, warning pulses, route emblems, hover loops, selected states, glow loops, float loops, particle loops, and animated leader portraits when motion clarifies the mechanic
- progression-state variants
- static fallbacks for every animated UI piece, route emblem, icon, or portrait
- country-selection, event-log, or custom-window graphics when relevant

Asset generation, sourcing, cropping, resizing, DDS conversion, file placement, sprite handoff notes, and manifests belong to `chaos-redux-event-assets`. Animated frame planning and frame-sheet handoff requirements belong to `chaos-redux-frame-animation`. Final `.gfx` wiring belongs to the main implementation agent unless a parent prompt explicitly grants that scope.

This skill should define what assets are needed, what they should represent, what source mode they require, and which visible states, if any, benefit from animation. Static presentation is valid whenever it communicates the mechanic more clearly. Do not require animation only because a mechanic is important.

Historical or real-world assets need special care. Historical flags and symbols require reliable cited design references, and every final flag still uses image generation as a reference-constrained flat reconstruction. `chaosx_portrait_creator` owns sourced photographs, explicit head-and-shoulders crops, placeholders, and user-supplied HOI4-style finals for real leaders. Grounded polities must use sourced real subjects or authentic institutional material even when their route is alternate history. The portrait worker generates one-person portraits only for wholly fictional leaders of wholly fictional high-chaos polities. Generated non-portrait art remains appropriate for people-free symbolic councils, invented high-chaos identities, idea icons, focus icons, decision icons, achievements, faction emblems, UI art, and fictional or alternate-history report, news, and super-event images unless the user says otherwise.

### Reference examples for asset planning

When a spec or asset prompt asks for generated or sourced assets, tell the asset agent to inspect the matching reference examples before creating anything.

Use this single canonical reference root:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.claude\skills\chaos-redux-event-assets\assets\gfx_references`

The catalog and every category below are relative to that exact folder:

```text
CATALOG.md
icons
event_art
flags
portraits
units
event_art/super_event
icons/achievements
```

Reference mapping:

- idea and national spirit icons: `icons/ideas/`
- news event images: `event_art/news/`
- report event images: `event_art/report/`
- super-event images: supplemental `event_art/super_event/` plus the live Chaos Redux super-event UI
- technology icons: `icons/technologies/`
- special-project icons: `icons/special_projects/`
- achievement states: `icons/achievements/`. The reusable not-eligible overlay is `icons/achievements/template/overlay.png`
- decisions and missions: their separate folders under `icons/`
- decision category icons: `icons/decision_categories/`
- decision category pictures: `icons/decision_categories/pictures/`
- flags: the complete normal, medium, and small ladder under `flags/`
- focus icons: `icons/national_focus/`
- officer corps spirits and balance-of-power icons: their separate folders under `icons/`
- leader portraits: `portraits/leaders/`
- 2D equipment, two-frame unit counters, and 3D material references: their separate pipelines under `units/`
- other matching categories when needed

The decision category picture family is a separate reference surface. Its exact path is:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.claude\skills\chaos-redux-event-assets\assets\gfx_references\icons\decision_categories\pictures`

The implementation or asset prompt must require `contact_sheet.png` in that folder. If it is missing, the asset agent should build it from the references, label filenames and native dimensions, and update `assets/gfx_references/README.md` and `assets/gfx_references/CATALOG.md` before producing new category pictures.

The event spec does not need to analyze those images itself. It should make the handoff explicit so the asset agent knows which example set to inspect before generation, sourcing, cropping, or wiring.

## Asset prompt handoff

After the full event specification is complete, create a separate asset prompt file for `chaos-redux-event-assets`.

The asset prompt should include:

- required assets
- visual style
- symbols and motifs
- target sizes
- intended in-game use
- country package asset coverage, including base flags, ideology flags, focus-route flags, cosmetic flags, leaders, portraits, and faction emblems
- suggested filenames
- suggested sprite names
- suggested static fallback sprite names and animated sprite names when animation is planned
- whether each asset is for an event, report event, news event, super-event, decision, idea, focus, achievement, flag, leader portrait, faction emblem, or UI element
- animation brief needs for every animated asset, including state logic, frame count target, target frame size, expected sheet size, frames per second, loop behavior, `play_on_show` expectation, static fallback, source mode, and target `.gfx` or `.gui` surface when known
- achievement icon list with completed icon directions for every achievement
- manifest requirements
- source mode, including historically sourced design references for flags followed by image-generation reconstruction, and whether a symbol or portrait must be sourced historically instead of generated
- reference example folder that must be inspected before asset work
- decision category picture list, eligibility, source mode, presentation role, static or animated state, and exact reference folder when category pictures are planned
- formable state-puzzle manifest needs, exact state geometry source, grey and green qualification states, projection, sprite ownership, and static category-picture alternative when formables are planned
- instruction to create the decision category picture reference contact sheet and catalog entries when the canonical sheet is missing

The asset prompt must state the correct source mode where relevant.

It must also state the relevant reference folder from the list above when a matching folder exists.

Use `chaos-redux-event-assets` rules for source selection. Symbolic icons usually use image generation (see the Image-generation route section of chaos-redux-event-assets). News event images, report event images, and super-event images may be sourced or generated. Prefer generated assets for fictional, alternate-history, symbolic, high-chaos, or unique scenes, and sourced assets for photographed events and archival artifacts. Every flag uses image generation. Historical flags first require a cited design reference and must remain flat, faithful reconstructions. Route all portrait prompts to `chaosx_portrait_creator`. Name the leader and advisor reference folders, require an explicit head-and-shoulders crop and identity preservation for grounded subjects, and request separate `156x210` leader and `65x67` advisor outputs when both uses exist.

Do not make the asset prompt vague. If a country has multiple cosmetic identities, ideology names, focus-route transformations, or leader changes, the asset prompt must list the required assets for each visible identity state. Use animation only when the state change benefits from motion. A completed formable or living mechanic may use an eligible static or animated category picture, a compact state-puzzle display, or a full window according to the presentation-choice pass. Do not request category pictures alongside an interactive state-puzzle GUI or other excluded presentation.

## HOI4 asset size reference

Use these sizes when planning assets:

- report event images: 210x176
- news event images: 397x153, black and white
- leader portraits: 156x210
- flags small: 10x7
- flags medium: 41x26
- flags normal: 82x52
- tech icons small: 64x64
- tech icons medium: 132x52
- achievements: 64x64
- super-event images: 457x328
- decision icons: 32x32
- idea and national spirit icons: 64x64
- focus icons: 94x86

Use other sizes when the event UI or asset type requires it.

## Asset style reference

When planning visuals, use these style expectations.

Report and news event images should look like documentary photographs, whether sourced or generated. News event images should be black and white.

Super-event images should have a strong central composition, clear dramatic theme, readable subject, and enough contrast for HOI4 UI.

Focus icons should look like HOI4 focus icons, with a central symbol, readable silhouette, aged texture, painterly detail, and strong contrast.

Idea and national spirit icons should look like compact HOI4 icon art. They need strong symbolic shapes and clear readability at 64x64. They are similar to focus icons, but they are missing the main frame.

Achievement icons should be readable at 64x64 and have a clear completion theme. The completed version is generated first. Grey and not-eligible variants can be produced later.

Flags should use clean symbols that remain readable at HOI4 flag sizes.

Progression-state variants may include selected, dim, active, locked, completed, rejected, damaged, corrupted, urgent, meter-fill, and bar-fill states.

## Super-event research handoff

If the event has one or more super-events, create a separate super-event prompt file for `chaos-redux-super-events`.

The prompt should ask that skill to research or create the full super-event presentation package.

For each super-event, include:

- super-event purpose
- trigger moment
- tone
- title direction, not a final title unless researched and sourced
- description direction
- quote direction, not quote text unless researched and sourced
- cultural remark direction, not final button text unless researched and sourced
- audio mood, not a final track unless researched and licensed
- image direction
- whether it is a normal escalation, defeat moment, aftermath moment, or world-end moment
- any special constraints from the event spec

The `chaos-redux-super-events` prompt should ask the agent to:

- find a real quote using the repository web research workflow from `AGENTS.md`
- verify quote wording and attribution
- find a meaningful cultural remark, reference, allusion, or short line where appropriate
- follow copyright limits for songs, films, books, and other protected works
- find suitable public domain or clearly licensed audio
- document all sources, license notes, and uncertainties
- coordinate super-event image needs with `chaos-redux-event-assets`

Do not claim a quote, cultural reference, or audio track is usable without checking.

If a license or attribution is unclear, mark it as uncertain.

The super-event prompt must explicitly state that unresearched titles, button text, quotes, cultural remarks, slogans, lyric fragments, allusions, and audio choices are blockers. The implementation agent must not convert research directions, working labels, achievement names, asset names, or draft-like wording into final super-event localisation.
