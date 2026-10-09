# Formables and decision-category presentation

Read the relevant complete sections when adding or changing category presentation, formable decisions, state-puzzle formation UI, or a dedicated mechanic window. Ordinary costs, timing, lifecycle, AI, and balance remain in the main skill.

## Decision category presentation hierarchy

A complex scripted GUI is not the default presentation for a decision category. Choose the least complex surface that communicates the category's current state, purpose, and available actions clearly.

Use static or animated category pictures only for simple categories containing a description, an ordinary decision list, and at most basic formatted value tables.
Do not add a picture when the category already has complex UI, meters, additional custom buttons or controls, rich interactive panels, or other animations.
Ordinary decision-list buttons and basic formatted value tables remain allowed, and an animated picture itself is supported as a simple-category alternative, but it must not accompany existing animated GUI.
Identity, atmosphere, propaganda, and territorial context alone do not override this gate.

Use this order:

1. ordinary category icon with concise category text
2. static category picture when eligible
3. animated category picture with a static fallback when eligible
4. compact attached display or category header
5. full scripted GUI or separate mechanic window

Do not move to a more complex layer only because the category is important. Within the eligibility gate, a static or animated category picture is often stronger for a category that needs identity and atmosphere but does not require the player to manage several live values or targets.

Within this gate, category pictures are especially suitable for:

- propaganda and public campaigns
- civil-war preparation, insurgency, and national preparedness
- ideology, elections, monarchism, party control, and trade-union politics
- faction management, diplomatic blocs, treaties, and intervention campaigns
- formables where a territorial overview is useful but individual state pieces do not need interaction
- one-theme crisis categories whose decisions already explain the actionable details

A category picture must remain presentation. Do not draw fake buttons, meters, values, or controls into it. Do not use a full custom window when the normal decision category plus one strong picture communicates the mechanic more clearly.

Use a full scripted GUI only when the player must manage a living system that cannot be read cleanly from ordinary decisions, category text, tooltips, and a category picture. Valid reasons include several interacting values, target selection, repeated map interaction, competing factions, a state-by-state formable display, or a persistent board whose state changes often.

### Player-facing category text and attached displays

Decision category descriptions, status summaries, scripted localisation, and compact attached displays must read as intentional game UI. Do not use repeated pipes or vertical bars, divider-character runs, ASCII or Unicode table rows, or other text separators to simulate columns, meters, ledger rows, buttons, or panel layout. Do not emit debug-style telemetry dumps such as `Label value | Label value | ...`, generic developer-state labels, raw variable names, or country-agnostic fallback prose that can leak another country's wording.

Use short natural-language lines, properly wired icons or texticons, real meters or panels, and concise tooltips. Basic formatted value tables remain allowed and do not by themselves require scripted GUI or exclude category pictures. This does not permit the fake text layouts prohibited above. Introduce a real scripted GUI only when a justified, functional layout gives the player interaction or state clarity that ordinary category text, decisions, tooltips, and pictures cannot provide. Category pictures and compact attached displays must not paint or textually simulate fake buttons, meters, ledger columns, or controls. Resolve country- or route-specific wording through explicit localisation branches with a neutral default fallback that cannot inherit another country's text, and verify the fallback in every supported context.

This restriction applies to runtime player-facing text and art. Internal Markdown audit tables may still use normal table syntax and must never be copied into localisation.

### Decision category picture reference workflow

Before designing or auditing a category picture, inspect:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\gfx_references\icons\decision_categories\pictures`

This folder is the canonical picture reference family. It is separate from `icons/decision_categories/`, which contains small category icons.

The reference family must contain its own `contact_sheet.png`. If the sheet is missing, create it from the reference images, label every example with its filename and native dimensions, and update `assets/gfx_references/README.md` and `assets/gfx_references/CATALOG.md` with provenance and surface ownership. Reference images and the contact sheet are review material only and must never be wired into runtime GFX.

When reviewing existing Chaos Redux decision categories, produce a category presentation audit with these columns:

| Category id | Owner system | Current presentation | Picture eligibility, including existing UI and animations | Recommended layer | Picture or GUI reason | Missing asset or implementation |
| --- | --- | --- | --- | --- | --- | --- |

Apply the eligibility gate above before identifying existing categories that would benefit from a static or animated category picture and currently lack one. Categories that the gate excludes because of complex UI, meters, additional custom controls, rich interactive panels, or other animations are ineligible, not missing picture assets. Do not add a picture to every category. Keep ordinary categories ordinary when a picture would add no useful identity, territorial context, or state feedback.

## Formable nation decisions

Use decisions for formable nations when the player should prove control over land, complete a political route, or spend resources before changing the country identity. A formable decision should feel like a proclamation, settlement, congress, coronation, constitutional act, annexation settlement, liberation charter, or administrative project. It should not be only a hidden tag switch.

A formable decision must define:

- visible name and hidden debug name
- decision category and visibility timing
- required owned and controlled states
- required subjects, allies, faction members, puppets, occupied territories, cores, claims, or compliance thresholds
- required focus, event flag, route flag, ideology, leader, legitimacy, chaos tier, or hidden reveal state
- whether the decision is visible before requirements are met, hidden until unlocked, or fully secret until an event reveals it
- political, military, economic, legitimacy, stability, war support, command power, XP, equipment, fuel, convoy, train, manpower, or factory costs
- what happens to the tag, cosmetic tag, country name, adjective, flag, leader, portrait, ruling party, advisors, national spirits, cores, claims, puppets, factions, wars, and guarantees
- whether claims become cores instantly, gradually through decisions, or only after compliance and local support work
- follow-up missions, border integration projects, legitimacy projects, resistance suppression, diplomatic reactions, and achievement hooks
- AI willingness, AI blockers, AI timing, and AI target safety
- cleanup for obsolete formation decisions after the formable is created

State requirements must be readable. Use named state groups and custom trigger tooltips. Do not expose raw state id lists to the player unless the existing UI pattern already does that cleanly. If several alternate maps can qualify, create clear requirement groups.

### Formable state-puzzle presentation standard

When exact territorial control is the central proof for a formable, use the reusable formable state-puzzle presentation. The interface should show the required territory assembled from the exact in-game shapes of its states, arranged in their real geographic positions like pieces of one map.

Each required state must be represented separately:

- a state that does not currently satisfy the formation requirement is grey
- a state that currently satisfies the formation requirement is green
- borders, texture, labels, or another non-colour cue must distinguish the two states for players who cannot rely on colour alone
- hovering a piece should name the state and explain whether it qualifies
- the panel should show the current qualifying count, required count, and final eligibility state without exposing raw internal variables

The pieces must use the exact state geometry from the installed map data. Do not approximate state outlines by hand, generate them with ImageGen, replace them with generic tiles, or use province blobs that do not match the actual formable requirement. Every piece must share one map projection, scale, origin, and border treatment so the territory assembles correctly.

The display must update from current game state. Reopening or refreshing the category must show current ownership and control, subject or ally counting rules, alternate state-set rules, route locks, and formation eligibility. Do not cache a green piece after the state stops qualifying. Do not run a whole-world daily scan for this display unless the user explicitly authorizes that performance pattern. Prefer scoped scripted triggers, event-driven refresh, or the verified scripted GUI evaluation pattern.

Use the same eligibility helpers for the visible pieces, the eligibility summary, and the formation decision. The GUI must never show the territory as complete while the decision rejects formation, or show it as incomplete while the decision can be taken.

The state-puzzle display is a justified scripted GUI surface because it communicates dynamic exact map requirements. It should stay compact. Do not add extra meters, fake buttons, lore paragraphs, or unrelated mechanic values around the map.

Create and maintain a reusable template package under:

`.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/`

The template package should include:

- `README.md` with the selection rules, ownership boundaries, and setup workflow
- a state-manifest example that records formable id, state ids, state names, alternate groups, counting rules, projection bounds, and sprite names
- `.gui`, `.gfx`, and scripted-GUI templates
- scripted trigger and scripted effect helper templates
- scripted localisation and tooltip templates
- a static category-picture option for eligible simple formable categories that do not need per-state interaction, without an interactive state-puzzle GUI alongside it
- a validation checklist covering exact geometry, projection, current control state, eligibility agreement, click and hover regions, resolution behavior, AI equivalence, cleanup, and runtime asset paths

Templates are reference scaffolding. Future agents must copy and adapt them into event or system-owned files. Do not wire the skill-local template files directly into the game.

AI must use the same formation conditions and decision logic without depending on the human-facing GUI. The puzzle is a player presentation layer, not the AI action path.

Hidden formables need extra care. A hidden formable can be locked behind an event, secret focus, rare ideology, high chaos, special leader, historical artifact, super-event, achievement route, or scripted GUI investigation. Hidden does not mean undocumented. The implementation handoff must still define all triggers, effects, assets, and cleanup.

### Formation missions and integration projects

Large formables should usually need post-formation work. Use missions or decision chains for integration when instant cores would be too strong.

Good formation follow-ups include:

- hold named capitals for 180 days
- secure rail links between old and new capitals
- integrate border districts through local support work
- spend infantry equipment and support equipment to build local administrations
- negotiate autonomy with subject members
- reduce resistance before coring a newly claimed area
- hold a plebiscite under observer conditions
- build a capital road, port, or rail hub before moving the capital
- keep stability and legitimacy above a threshold during the formation crisis
- prevent rivals from reaching an influence threshold before the final proclamation

Formation systems should support partial success and failure. A country can form the title but gain only claims, delay core grants, create dissatisfied regions, trigger rival reactions, or open emergency missions.

## Scripted GUI decision categories and mechanic windows

Choose the presentation layer from the hierarchy above before creating a custom window. Use an attached scripted GUI or a separate mechanic window only when active values, targets, meters, factions, or exact state pieces need a visual management surface that ordinary decisions, tooltips, and a category picture cannot provide clearly. Basic formatted value tables alone do not require this richer presentation. A custom interface must have a gameplay reason and cannot compensate for weak actions.

Use the scripted GUI skill's [reference-image workflow](../../chaos-redux-scripted-gui/SKILL.md#reference-image-before-implementation), [bounded MCP preview and comparison workflow](../../chaos-redux-scripted-gui/SKILL.md#mcp-visual-review-and-optional-rewrite), and [visual and usability review](../../chaos-redux-scripted-gui/SKILL.md#scripted-gui-visual-and-usability-review). Apply that skill to GUI layout, backgrounds, text, content budgets, interaction presentation, and bounded visual checks; unavailable MCP evidence is a limitation under AGENTS.md. Route layout work on a dedicated UI introduced and owned by one named event to `chaosx_event_ui_worker` under `chaos-redux-subagents`. Shared event log, event details, settings, super-event frameworks, and unrelated interfaces remain parent-owned and require their own authorization. The decision owner retains the gameplay rules below.

### GUI action integrity

Every gameplay-changing GUI action follows the same cost, affordability, requirement, payment, effect, AI, and cleanup contract as a normal decision. Use the same scripted effect families, validation triggers, logging, and lifecycle helpers so a GUI cannot bypass decision balance. Each action may have at most four distinct spendable cost types, with the correct texticon for every displayed cost; never hide an extra cost in a tooltip or confirmation window. Keep non-consumed requirements separate from payment and explain missing requirements precisely.

For each gameplay-changing control, document:

- its action and target
- visible costs and requirement summary, with a precise action/blocked-reason tooltip
- shared availability and affordability checks
- the single payment path and scripted effect or decision action
- AI equivalent where AI countries can use the mechanic
- cleanup when the target, route, action, or mechanic becomes invalid

Do not add actions to fill layout space or manufacture depth. Merge duplicate actions and remove controls whose result does not change play. Information and navigation controls follow [click regions and state behavior](../../chaos-redux-scripted-gui/SKILL.md#click-regions-overlap-and-state-behavior); they do not require an invented gameplay effect.

### Animated decision category presentation

Animation is optional. First apply the same category-picture eligibility gate to static and animated pictures, then decide whether a static picture is sufficient. Use an animated category picture or animated GUI sprite only when motion makes a changing state easier to notice or strengthens a category whose identity depends on active propaganda, mobilization, escalating crisis, or transformation. An animated picture remains a simple-category alternative and must not accompany existing animated GUI. Every animated category picture needs a static fallback.

The examples below include GUI animations for their appropriate controls, meters, panels, and windows. They do not make those categories eligible for an additional static or animated category picture.

Suitable uses include:

- soft glow around an available formation seal
- warning pulse when pressure is near a threshold
- slow float on an occult, diplomatic, or propaganda emblem
- particle drift behind a high-chaos category header
- meter shimmer when a value changes
- selected-card glow for the active sponsor, faction, or route
- animated border for crisis mode
- animated leader or council portrait inside a special mechanic window

Use static fallback sprites for every animated element. Keep animations subtle unless the route is deliberately supernatural or high-chaos. Do not animate every icon in a category. Too much movement makes the UI harder to read.

The decision implementation handoff should list animated sprite names, static fallback names, target sizes, frame counts if known, loop behavior, file paths, source mode, and whether the animation is purely decorative or tied to a mechanic state.
