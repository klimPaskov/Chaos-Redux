---
name: chaos-redux-events
description: Use when implementing or updating Chaos Redux events.
---


# Chaos Redux Events

Use this skill for any Chaos Redux event work, including:

- adding or updating `chaosx.nr<ID>.*` event chains
- wiring event log, event details, evolutions, and world-end branches
- maintaining `docs/events/` event documentation
- updating the gameplay-facing event spreadsheet

Repository-wide reading and style rules live in `AGENTS.md`. This skill only adds the Chaos Redux event-specific implementation contract.

When an event implementation creates broad visible text, spawn `chaosx_localisation_auditor` before completion. When an event needs repeated dynamic logic across events, decisions, focuses, evolutions, logs, or GUI, use `chaosx_scripted_system_architect` before duplicating logic.

## Reference map

Read a reference file only when the work touches its topic. Each root section that points to a reference keeps its mandatory gate and links to the full requirements.

- [references/scripted-systems-and-country-integration.md](references/scripted-systems-and-country-integration.md): owner-side unit-family coverage, supporting gameplay systems, duration fields, world threat, formables, 3D model and entity integration, and loop break isolation.
- [references/event-text-formatting-and-details.md](references/event-text-formatting-and-details.md): parchment colour rules, tooltip display audits, Event Details text, integer and `defined_text` formatting, and safe localisation writes.
- [references/event-log-evolutions-and-clusters.md](references/event-log-evolutions-and-clusters.md): evolution implementation, event-log UI surfaces, event log integration, and event cluster integration.
- [references/world-end-triggerable-scenarios-and-aftermath.md](references/world-end-triggerable-scenarios-and-aftermath.md): world-end scenario implementation, triggerable scenarios, and major-event defeat aftermath.

## Working model

Treat every event as a contract across some or all of these implementation surfaces:

- event definition and subevents
- random-event classification and registration
- auto-fire or runtime hooks
- shared scripted effects, scripted triggers, and script constants
- event logs, actor mapping, event-details content, and evolution views
- super-event image, localisation, and audio wiring
- decisions, ideas, AI, characters, unit templates, and more
- visible 3D unit, building, creature, vehicle, aircraft, naval, or map-entity model packages
- `docs/events/` documentation and spreadsheet

If a task seems to need custom one-off plumbing, first check whether the same behavior should become generic for future events.

### Owner-side unit-family coverage

A new land sub-unit or equipment-backed family needs its owner-side consumer contract, registration, CXT setup, and complete integration coverage.
Read the complete requirements in [Owner-side unit-family coverage](references/scripted-systems-and-country-integration.md#owner-side-unit-family-coverage) before this work.

### Parent and subagent implementation ownership

Patch-capable subagents are active by default inside the current task scope. Use them when a large event touches focus trees, decisions, country packages, localisation, GUI, scripted helpers, or assets at the same time.

Small subagent patches are allowed when they improve a specific surface without changing the event design. A decision subagent can vary costs, clarify tooltips, add cleanup, improve AI weights, and patch related localisation. A focus subagent can fix a route lock, prerequisite, bypass, focus AI, icon reference, small reward, or formable unlock hook. A country package subagent can patch tag setup, party names, focus loading, leader references, country localisation, simple starting setup, or existing formable requirements. A localisation subagent can patch dynamic text directly. A scripted-system architect can add narrow helpers and direct call sites when the repeated logic is already present.

The parent still owns final integration, docs, spreadsheets, event chain direction, completion claims, and any broad mechanic expansion. If a subagent sees a needed route family, new country package, new formable suite, new scripted GUI system, new event chain, or major balance redesign, it writes a plan under `docs/plans/<event_id>_<event_slug>_plans/` and stops.

Every subagent edit must produce a handoff under `docs/plans/<event_id>_<event_slug>_plans/subagent_handoffs/` when the event id and slug are known. The handoff lists changed files, identifiers, behavior before and after, meaningful validation, remaining gaps, and follow-up work for the parent.

### Custom subagent use during event implementation

For large or multi-surface event work, use project subagents to keep the main implementation pass focused.

- Use `chaosx_repo_explorer` before editing only when file locations, existing patterns, vanilla references, likely touchpoints, missing-file recovery, or implementation order are unclear.
- Spawn `chaosx_asset_source_researcher`, `chaosx_generated_event_art`, and `chaosx_icon_artist` for actual visual asset packages according to `chaos-redux-event-assets`.
- Spawn `chaosx_3d_model_pipeline` for bounded Meshy 7 model geometry, textures, rigs, skeletal actions, Internet-sourced unit sound design, bespoke vanilla-green custom-unit counter handoffs, `.mesh`/`.anim` exports, reimport proof, and runtime handoff when the event owns a 3D unit or building surface.
- Spawn `chaosx_event_ui_worker` only when the named event specifically introduces and owns a dedicated scripted GUI or mechanic window. Never route shared event logs, event details, settings, super-event frameworks, or unrelated existing UIs to it.
- Spawn `chaosx_super_event_text_researcher` and `chaosx_super_event_audio_researcher` for actual super-event research packages according to `chaos-redux-super-events`.
- Spawn `chaosx_improvement_loop_planner` after a substantial implementation stage when several new mechanics, country packages, formables, focus routes, decisions, scripted GUI surfaces, super-event candidates, or lore systems have been added and the event needs deeper connection. Do not spawn it again for the same event until the previous addendum is implemented, folded into specs, queued with a reason, or rejected.
- Spawn `chaosx_focus_tree_auditor` after creating or heavily changing focus trees.
- Spawn `chaosx_ai_probability_auditor` for every in-scope AI weight, MTTH, random-selection, or weighted-pool surface before completion.
- Spawn `chaosx_event_completion_auditor` before claiming a large event, event rework, or spec-driven implementation is complete.
- Spawn `chaosx_spreadsheet_doc_worker` after implementation when the event catalog workbook rows need to match the final repo state. Docs, manifests, and route coverage tables stay with the parent or `chaosx_documentation_curator`.

Subagents do not remove the main agent's responsibility to wire, review, validate, and report honestly.

## Spec and plan locations

Source event specs live under `docs/specs/<event_id>_<event_slug>_specs/`. Read them as the main design source when they exist, and record the explicit user decision or parent acceptance within the user-authorized scope that supports each accepted claim. A spec location, date, status label, or old handoff does not prove approval, and implementation evidence proves what exists rather than what was accepted. Keep missing or conflicting acceptance evidence unresolved under the AGENTS.md Specs and Plans dispositions.

Subagent plans, expansion addenda, audit follow-up notes, and implementation handoffs live under `docs/plans/<event_id>_<event_slug>_plans/`. Plans are working documents. If a plan becomes accepted source design, merge it into the relevant spec.

## Spec fidelity and implementation quality

When implementing from `docs/specs/`, treat mapped content with recorded acceptance as acceptance criteria. Do not silently replace mapped mechanics, routes, countries, decisions, achievements, assets, or super-events with smaller fallback versions. If something must be merged, skipped, or simplified, report it in the completion notes with the reason and affected files.

Use dynamic factors for pressure, cooldowns, progress, chance, support, duration, costs, AI willingness, spawn strength, aid amounts, stage movement, recognition, etc when the spec calls for a living system. Flat values are allowed only as constants, caps, floors, or deliberate tuning anchors. Centralize shared values in script constants or documented tuning.

Do not implement major decisions, missions, focus rewards, GUI buttons, or event responses as political power or command power purchases by default. Use concrete costs and requirements from the spec when relevant: XP, equipment, manpower, fuel, trains, convoys, supply, stability, war support, local support, held states, unit presence, foreign access, intelligence exposure, or time pressure. Tooltips must explain blocked nonstandard requirements.

When the spec maps focus paths, implement a real tree, not a thin vertical chain. Preserve route locks, side branches, convergence points, hidden branches, crisis branches, AI weights, focus filters, varied icons, and branch payoffs. Rewards should vary across buildings, units, decisions, missions, advisors, identities, claims, cores, diplomacy, technologies, and mechanic changes. Do not fill trees with repeated new ideas, tiny modifiers, political power, stability, or war support.

When implementing starting or route ideas, wire their lifecycle. Negative, mixed, staged, or route-specific ideas should be removed, upgraded, replaced, worsened, or consumed by the mapped decisions, focuses, missions, wars, failures, or reforms. Avoid dead idea stacks that never change.

Mechanic variables must be visible somewhere meaningful, such as decision category text, scripted localisation, national spirit tooltip, scripted GUI, progress meter, or focus tooltip. Keep cause and effect readable. Values should be changed by the mapped decisions, focuses, missions, events, wars, state control, AI actions, and foreign influence. Use consistent localisation colours for important mechanic values and breakdowns.

Large decision systems must hide obsolete or irrelevant actions. Use phases, active caps, target pools, route locks, thresholds, emergency visibility, regional grouping, cooldowns, or cleanup flags. The category should show current playable actions, not every possible debug action.

If the spec defines achievements, implement the full achievement surface: tracking flags or variables, unlock triggers, disqualifiers, localisation, icons, docs, and any route or formable hooks. Do not convert hard achievements into automatic unlocks.

Before completion, check every visible asset named or implied by the spec: flags, ideology flags, cosmetic flags, leaders, portraits, focus icons, decision icons, ideas, achievements, faction emblems, report or news images, super-event images, UI sprites, animated sprites, static fallbacks, and 3D model/entity consumers. Do not claim completion while required visible assets are placeholders unless the completion report says so clearly.

Route every character portrait to `chaosx_portrait_creator`. Do not generate a real historical leader or an invented substitute for a grounded polity. For grounded packages, the portrait worker sources attributed real subjects or authentic institutional material, records provenance and rights status, creates the explicit crop and placeholder, and later installs the user-supplied HOI4-style final. It invokes image generation (see the Image-generation route section of chaos-redux-event-assets) only when both the polity and leader are wholly fictional and deliberately high-chaos, then processes and wires the result. Every new flag uses image generation. Historical flags and well-attested real symbols first require cited design research, then a strict flat reconstruction with no fabric scene, painterly flag artwork, fake lettering, or invented heraldry.

Any new, released, restored, transformed, or event-managed country that is expected to fight needs starting forces and a reinforcement pathway. Implement dynamic starting units, templates, equipment and manpower assumptions, commander or officer handling when relevant, and later unit growth through decisions, focuses, depots, objectives, volunteers, foreign support, mobilisation, or special mechanics. Do not leave a serious fighting country as an empty tag unless the spec says so and explains why.

Major events and country-creation events need route-specific AI. Implement focus choices, decision choices, unit-raising choices, faction behavior, foreign influence behavior, rare variant handling, high-chaos exceptions, invalid-route blocking, etc.

When an event needs a reusable country carrier, consult `common/collections/chaosx_country_collections.txt` and `docs/events/006_independence_wave/systems/country_registry.md` before reserving a new tag. Use the `chaosx_country_*` collection that matches the region or origin, then record the consuming event's own provenance and package identity before loading content. Do not create a duplicate tag for an Event 006 or Soviet Collapse carrier, and do not treat event-text mentions as tag collisions. After changing a protected carrier or its references, perform a fresh repository-wide collision scan against vanilla, installed Workshop mods, and sibling local mods. The legacy country-tag auditors under `.tools/archive/` are provenance only and are not current acceptance tools.

Do not reduce major spec effects to tiny decorative modifiers. Important effects must change incentives, unlock content, move visible mechanic values, alter army or economy behavior, create a real tradeoff, or connect to later outcomes.

### Historical restoration compatibility

When restoring an older direct or simple flow, apply this checklist within the existing integration and balance review:

- Separate explicitly requested historical values and actions from later useful lifecycle, state, records, receipts, cleanup, context, and AI systems. Honor the explicit restore and keep its direct flow without adding mandatory gameplay steps. Avoid blanket restoration of whole recent files.
- Compare the historical target, pre-restoration behavior, and edited behavior through actual runtime consumer call sites and their helper chains. A retained file or helper definition alone does not prove its dynamic logic still matters.
- Preserve useful later additions with compatibility adaptations so their inputs, outputs, scaling, guards, and state transitions remain meaningful. Check whether a restored helper and retained lifecycle calculation both grant the same effect or charge the same cost, and assign each contribution to one owner.
- Use named scenarios for the restored action alone, its interaction with retained lifecycle or context, repeated execution, and inverse cleanup where relevant. Calculate combined effects and costs from the actual calls, verify ownership and receipt handling during cleanup, and report behavior changes or unavailable historical evidence in the existing handoff. Follow existing weighted-AI review and verification limits.

## Event writing and player-facing text

Event implementation owns final player-facing wording for event popups, news events, report events, Event Details, decision text, focus text, tooltips, GUI labels, scripted localisation, documentation summaries, and spreadsheet-facing fields that mirror in-game text. Convert direction into finished wording, but do not paste working labels, prompt fragments, route notes, placeholder text, or process notes into localisation.

These writing style rules apply to every Chaos Redux prose surface, including event text, news text, super-event text, decision text, focus descriptions, tooltips, docs, specs, plans, prompts, spreadsheets, and all player-facing text.

1. Never use the em dash or semicolons in sentences.
2. Absolutely avoid dialectical hedging. Do not frame sentences as thesis, antithesis, synthesis.
   - Dialectical hedging examples:
     - `This is not just a strike. This is a warning.`
     - `The cult is not fighting for land, but for meaning.`
     - `The disaster is both a local tragedy and a global sign.`
     - `The army did not collapse. It transformed.`
     - `This is less a rebellion than a confession.`
     - `The question is not whether order can return, but what kind of order will survive.`
   - Thesis, antithesis, synthesis examples:
     - `The army claims the province is secure. Refugees say it is already lost. The truth lies between them.`
     - `Some call the new state liberation. Others call it occupation. In reality, it is both.`
     - `The priests call it a miracle. The generals call it a weapon. History will call it both.`
3. Avoid AI-style explanatory templates. Do not write lines that sound prebuilt or reusable across any event.
4. Absolutely avoid staccato sentences. Do not split one simple thought into a chain of tiny lines for artificial weight or dramatic effect. Use complete, readable sentences with enough context to be clear.
   - Staccato examples:
     - `No orders. No mercy. No dawn.`
     - `The guns stopped. The screaming did not.`
     - `First hunger. Then anger. Then flags.`
     - `The gate opened. The crowd moved. The guards ran.`
5. Absolutely avoid empty dramatic filler. Do not lean on vague intensity words when concrete detail would do the work.
6. Do not paste instruction text, task labels, prompt fragments, or process notes into in-game text, specs, docs, localisation, spreadsheet fields, or reports.
   - For example, when the user says `Do not reveal the hidden mechanics here.`, do not write `This path purposely doesn't reveal the hidden mechanics`.

Write in-world text. Describe what the country, army, population, strange force, disaster, cult, machine, disease, movement, or leader is doing. Do not make the emotional center a changed map, a staff-table scene, administrative paperwork, formal diplomatic phrasing, sealed reports or generic crisis communications. They should not become the default way to create mystery.

Player-facing escalation text must not label itself as a warning, a non-warning, a threat, a danger signal, or a world-ending risk. Let the player infer trouble through fear, missing people, strange behaviour, rumours, unexplained anomalies, local panic, and consequences that repeat over time. Do not build tension with staged contrast formulas. Forbid patterns such as `claim X while officials Y`, `reports say X while authorities Y`, `X before Y`, `people do X before governments Y`, and any similar construction that pairs one observation against a denial, admission, delay, or official reaction. Write the observed fear and uncertainty directly instead of using those contrast frames.

Only write sections for event surfaces that actually exist. Omit absent systems entirely. This applies to world-end branches, manual scenarios, super-events, achievement sets, focus trees, country packages, and custom UI.

Do not expose hidden routes, secret variables, future surprises, achievement paths, implementation history, tuning history, or rework history in player-facing text. Event Details and spreadsheet detail fields describe the situation and premise, not the mechanical effects. Options, decisions, focuses, and tooltips must still clearly describe visible consequences and requirements, but they should not read like reward lists or spoil content.

For super-events, do not invent quotes, cultural remarks, song fragments, title references, or final audio choices. Use `chaos-redux-super-events` and the relevant research subagents when the event needs sourced wording or audio.

### Detail text, immediate effects, and value formatting

Report and event descriptions on light parchment use plain text without colour formatting, and Event Details text never lists mechanical effects because real immediate effects belong in a `hidden_effect`. Visible integers use `|0` formatting, numeric `defined_text` output uses a real `.yml` key, and the section also fixes the safe route for localisation writes.
Read the complete requirements in [Detail text, immediate effects, and value formatting](references/event-text-formatting-and-details.md#detail-text-immediate-effects-and-value-formatting) before this work.

## Event anatomy

- entry event: the canonical `chaosx.nr<ID>.1` start
- player-facing popup events: the things the player actually reads and clicks
- follow-up/news events: broadcast or consequence popups
- evolutions: mutation tracks inside the same event identity, distinct from baseline stage progression
- world-end scenarios and super-events
- triggerable scenario launch variants when the event has a manual sandbox or challenge setup
- connection with other events (meaning that events are not standalone and actually interact with each other)

For confirmations before irreversible gameplay, put an always-available, consequence-free Cancel option first because native timeout selects the first option (13 days by default), and never treat silence as affirmation.
Native option triggers are evaluated when the event fires, not dynamically while its popup remains open.
Keep the option-availability guard separate from a click-time effect guard that rechecks permission, the current request and context against the immutable pending receipt before applying consequences.
Duplicate requests must not overwrite that receipt.
Treat controller changes or loss of authority as no consent.
Existing affirmative-first event patterns are not general precedents for safe confirmations.

### Proposal popup lifecycle

Keep a visible human popup's carrier pointer, family, proposal sequence, and carrier/recipient generation snapshots immutable through proposal withdrawal.
Invalidate the live proposal separately, retain the shown-popup lock, and serialize replacement delivery until the old event's `after` has closed its snapshot.
Every reply effect must revalidate the snapshot against the current proposal before mutation, even if its option was visible when the event fired.
A stale close option must remain usable and describe closing the old prompt without promising to accept, refuse, or change another proposal.
Treat `timeout_days` as execution of the guarded first option, followed by normal `after` closure, rather than a special timeout branch (offline Event modding, lines 184-186).

### Generation receipts and cleanup

Give every immutable birth/provenance tuple its own publication-generation receipt and publish the complete tuple together.
Mutable array/cache row presence or absence is not first-publication authority; first publication requires a validated unpublished identity with all tuple receipts absent.
Same-generation missing or stale row repair must preserve the old tuple rather than restamp it from mutable current fields.
Partial receipt loss fails closed rather than reconstructing from mutable fields; renewal may publish a new tuple only for a genuine validated newer generation proven against the publication receipt.

Match each entity's current generation to its own birth or installation snapshot, and validate the counterpart's generation separately against that counterpart's snapshot.
Never compare member generation to carrier generation as proof of shared identity, or infer a missing member receipt from the carrier snapshot.

Before destructive response, idea, flag, or relation clearing during bounded frozen-member cleanup, verify the actual member country, its matching frozen generation row, and the exact current binding.
Undo only the exact owned relation directions before clearing their ownership and binding receipts, and leave unowned relations intact.
Rejected frozen rows must not clear another incarnation's state; a direct stale-local-receipt retirement policy must be explicit and grant no world-relation mutation authority.

## Chaos source handling

Implement event-owned Chaos changes only on concrete outcomes defined by the spec, using the shared Chaos Meter and history path. Common hooks include meaningful movement success, special Chaos-country growth, spread, failed containment, actual use of dangerous capabilities, and durable containment or defeat.

Use one-shot milestones or thresholds where needed so routine growth cannot farm Chaos. Do not duplicate generic sources such as wars, annexations, deaths, contamination, or nuclear use unless the event adds a separate consequence that the generic source does not represent.

Evolution state itself always gives zero Chaos. Eligibility, activation, stage advancement, logging, or unlocking content changes nothing until evolved behavior actually causes a concrete consequence.

Before completion, check that mapped event-owned changes fire at the intended outcome, do not repeat incorrectly, and appear through the shared Chaos History path.

### Evolution implementation

Baseline stages and evolutions stay distinct. An evolution fires through MTTH-based pacing, is gated by `is_current_evolution_enabled`, sets the shared evolution context, records through `record_events_log_evolution_entry`, and never changes Chaos by itself.
Read the complete requirements in [Evolution implementation](references/event-log-evolutions-and-clusters.md#evolution-implementation) before this work.

### Event-log UI surfaces

Evolution log display changes target the exact surface (main Evolutions tab, History details related evolutions, or Event details evolution catalog) and patch the real GUI, localisation, or scripted data path. Unreworked events stay out of the default enable allowlist until they are ready.
Read the complete requirements in [Event-log UI surfaces](references/event-log-evolutions-and-clusters.md#event-log-ui-surfaces) before this work.

## World-end scenarios

A world-end scenario is a terminal branch that changes the campaign into a resolved or end-state condition, not just a large disaster or strong major event. It is chosen based on the world state and can only be triggered when the chaos value is over 1000.

### World-end scenario implementation

A world-end branch is guarded by `NOT = { has_global_flag = world_end }`, sets `world_end`, a scenario-specific global flag, and the matching `super_event_visible`, and gates incompatible future systems. Every public terminal branch also needs its own Event Details registry row with an independent persistent toggle, and hidden branches stay out of public surfaces.
Read the complete requirements in [World-end scenario implementation](references/world-end-triggerable-scenarios-and-aftermath.md#world-end-scenario-implementation) before this work.

## Triggerable scenarios

Triggerable scenarios are manual sandbox or challenge setups launched from the settings UI. They are always directly fireable unless the launch is impossible, are never blocked by normal event prerequisites, and need registry, constants, effects, triggers, GUI, localisation, documentation, and tightly scoped bypass cleanup.
Read the complete requirements in [Triggerable scenarios](references/world-end-triggerable-scenarios-and-aftermath.md#triggerable-scenarios) before this work.

## Major-event defeat aftermath

Only a global or near-global, long, costly crisis earns a structured aftermath such as a defeat super-event, postwar treaties, remembrance events, or lasting ideas. Do not add one after a contained or short-lived disaster.
Read the complete requirements in [Major-event defeat aftermath](references/world-end-triggerable-scenarios-and-aftermath.md#major-event-defeat-aftermath) before this work.

## Event implementation workflow

### MCP event-chain pass

For event-chain changes, use narrow inspect, render, and compare checks on the affected chain, preserve source review, and distinguish static evidence from game execution. Follow AGENTS.md when a check is unavailable or inconclusive.
Read the complete requirements in [MCP event-chain pass](../../../docs/systems/hoi4_agent_tools_mcp_integration.md#mcp-event-chain-pass) before this work.

### 1. Classify the event first

- Entry events keep the format `chaosx.nr<ID>.1`.
- Keep related subevents in the same namespace.
- Decide whether the event belongs in:
  - `global.major_events`
  - `global.repeatable_events`
  - `global.fire_once_events`
- Decide which pieces are:
  - hidden bootstrap/runtime events
  - player-facing popup events
  - news follow-ups
  - baseline progression events
  - evolution tracks
  - escalation events
  - world-end or super-event branches
  - aftermath content

Keep IDs stable when updating existing chains.

### 2. Map touched systems before editing

Always start from the event and walk outward through the systems it touches.

Core files to check:

- `events/<ID>_my_event.txt`
- `common/on_actions/chaosx_on_actions_system.txt`
- `common/on_actions/<event_id>_<event_slug>_on_actions.txt` for event-owned runtime hooks
- `common/ideas/<event_id>_<event_slug>_ideas.txt` for event-owned national spirits, hidden ideas, and other idea categories
- `common/scripted_guis/<event_id>_<event_slug>_scripted_guis.txt` for event-owned scripted GUI bindings
- `common/opinion_modifiers/<event_id>_<event_slug>_opinion_modifiers.txt` for event-owned opinion modifiers
- `common/dynamic_modifiers/<event_id>_<event_slug>_dynamic_modifiers.txt` for event-owned dynamic modifiers
- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_effects/chaosx_events_log_effects.txt`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/_chaosx_events_l_english.yml`
- `common/scripted_localisation/chaosx_scripted_localisation_debug.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`

Frequently-needed companion files:

- `common/on_actions/chaosx_on_actions.txt` only for shared hooks that do not belong to one event
- `common/scripted_effects/chaosx_settings_effects.txt`
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
- `common/scripted_guis/chaosx_scripted_gui_settings.txt`
- `common/scripted_guis/chaosx_scripted_gui_super_events.txt`
- `interface/chaosx_events_log_popup.gui`
- `interface/chaosx_super_events.gfx`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `localisation/english/chaosx_gui_l_english.yml`
- `common/script_constants/*.txt`
- `common/scripted_triggers/*.txt`
- `common/scripted_effects/*.txt`
- the shared Chaos Meter path when the event owns Chaos-changing outcomes
- `common/decisions/<event_id>_<event_slug>_decisions.txt` for event-owned decisions. Keep all decision categories owned by the same event in that event file unless a verified engine constraint requires root-only or separate placement
- `common/decisions/categories/<event_id>_<event_slug>_categories.txt` for event-owned decision category definitions
- shared or cross-event decision systems under `common/decisions/` and `common/decisions/categories/` with clear subsystem filenames, without fake event ids or unnecessary `chaosx_` prefixes. `common/decisions/chaosx_decisions.txt` and `common/decisions/categories/chaosx_decisions_categories.txt` are reserved for shared or legacy root-only hooks
- `common/ideas/*.txt`, with `common/ideas/chaosx_ideas.txt` reserved for shared or legacy root-only ideas that cannot safely belong to one event
- `common/achievements/chaos_redux_achievements.txt` for the single root-only Chaos Redux achievement registry. Keep event achievements grouped by event section inside this file instead of creating per-event achievement files with new `unique_id`s
- `common/ai_strategy/*.txt`
- `common/ai_templates/*.txt`
- and possibly more. Some events can truly touch all systems.

### 3. Register the event in the random-event system

Update the event system registration in the same change.

Required checks:

1. Add or keep the event ID in the correct array inside `initialize_event_categories`.
2. Keep the event classification aligned with the actual gameplay behavior.
3. Make sure `get_event_type` can resolve the ID through the registered arrays.
4. Keep debug/event-log name mappings aligned with the registered ID.

Do not add an event script and leave the event system unaware of it.

### 4. Handle supporting gameplay systems

Update every supporting system the event changes in the same implementation. Shared helpers and countries require the detailed scope, output-lifetime, identity, and cleanup contracts.
Read the complete requirements in [Handle supporting gameplay systems](references/scripted-systems-and-country-integration.md#handle-supporting-gameplay-systems) before this work.

### 5. Event log integration

Every event appears in the event log, and the full contract (script ownership, event-name and debug-name plumbing, actor mapping, detail-view selectors, public world-end rows, and `N/A` weights for events that cannot fire) is wired in the same change.
Read the complete requirements in [5. Event log integration](references/event-log-evolutions-and-clusters.md#5-event-log-integration) before this work.

### 6. Event cluster integration

Event clusters are a catalogue layer above random events: the Clusters tab shows every registered cluster and History shows only those that fired. A new cluster needs aligned registry entries, member arrays, scripted localisation, runtime context, and cooldown or one-time handling.
Read the complete requirements in [6. Event cluster integration](references/event-log-evolutions-and-clusters.md#6-event-cluster-integration) before this work.

### 7. Duration fields and constants

Use supported dynamic duration handling and centrally tuned constants; preserve native timer semantics.
Read the complete requirements in [Duration fields and constants](references/scripted-systems-and-country-integration.md#duration-fields-and-constants) before this work.

### 8. Super-event integration

If the event shows or drives a super event, wire the whole package:

- choose the slot intentionally
- set `super_event_visible`
- set `global.current_super_event_audio_id`. Every super-event has a unique audio id and unique final track.
- register the final cue as a game-ready OGG under `music/`, preserving the original recording and existing WAV sources
- add music song definitions and every settings-volume variant, including silent `0`, with matching music-list and station registrations under the `chaos-redux-super-events` contract
- play the cue with `play_current_super_event_audio = yes`, the settings-aware music helper, so each new cue replaces the prior super-event cue even when muted
- update scripted localisation in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- update image wiring in `interface/chaosx_super_events.gfx`
- update player-facing localisation in the correct `.yml` files
- update `music/chaosx_music_track_list.html`, the canonical audio catalogue, with the final track, super-event id, source, and rights details. If you can't get all the info from the file metadata and the user didn't provide the author or the name of the piece, then ask the user to do so.

Use `chaos-redux-super-events` whenever an event includes a super-event. That skill handles super-event title direction, description tone, quote research, cultural remark selection, audio research, source documentation, and super-event presentation rules. This skill handles implementation wiring: slot, flags, localisation, image, audio ID, scripted localisation, `.gfx`, docs, and spreadsheet updates.

### 9. World-end integration

If the event can produce a terminal scenario:

- keep the world-end flagging explicit and centralized
- make sure the terminal branch is distinguishable from ordinary major-event escalation
- gate later random events, branches, or systems that should no longer operate after the terminal state
- make the docs and spreadsheet agree on what the terminal branch actually is

If the branch is dramatic but not actually terminal, treat it as a major escalation evolution or super-event instead of world-end.

### World threat framework

Integrate event-owned threat through the shared world-threat framework.
Read the complete requirements in [World threat framework](references/scripted-systems-and-country-integration.md#world-threat-framework) before this work.

### Formable nations as event surfaces

Treat formables as complete event surfaces, including decisions, identity, assets, AI, and cleanup.
Read the complete requirements in [Formable nations as event surfaces](references/scripted-systems-and-country-integration.md#formable-nations-as-event-surfaces) before this work.

### Scripted GUI and animated event presentation

Major event mechanics can use scripted GUI windows, decision-category interfaces, animated leader portraits, or custom buttons when they make the system easier to play. Treat that UI as part of the event contract, not as decoration added later. Static or animated category pictures are eligible only for simple categories with a description, an ordinary decision list, and at most basic value tables. Do not add category pictures alongside an existing complex category GUI, meters, extra custom buttons or controls, rich interactive panels, or other animations. Normal decision-list action buttons are allowed, and the category picture itself may be animated when this simple-category gate passes.

Use `chaos-redux-scripted-gui` for every authorized scripted GUI layout change, including parent-owned shared surfaces. Create/select the reference before implementation and record its acceptance basis and native-element mapping under that skill. When the event specifically adds a dedicated scripted GUI or mechanic window, route its bounded layout implementation and visual-quality pass to `chaosx_event_ui_worker`. The worker follows the reference-image, native-layout, and layout review rules in `chaos-redux-scripted-gui`, preferring targeted MCP views, correcting confirmed defects, and using code review and local checks after the retry limit with material visual limitations reported. Never send the shared event log, event-details framework, settings, super-event framework, shared registries, or unrelated existing UIs to this worker. Eligibility requires accepted spec or source evidence that the named event introduces and owns the UI. Apply authorized reviewed source edits directly or optionally through `gui_rewrite`; its automatic post-write/index validation is not a mandatory gate under `chaos-redux-scripted-gui`.

When an event uses a custom interface, align these surfaces:

- decision category or entry button
- scripted GUI definition
- scripted triggers and effects
- costs and tooltips
- animated and static sprites
- localisation and scripted localisation
- AI fallback behavior
- cleanup and invalidation rules
- documentation and asset manifest

For a formable state puzzle, add the manifest-to-category attachment crosswalk to this contract. Verify every in-scope category metadata block against the generated scripted-GUI identifier and window, then prefer targeted `hoi4.gui_inspect` and `hoi4.gui_render` for the linked category window within the retry limit or inspect that exact category/window mapping directly. Do not claim category coverage from a state-piece render alone.

Every player-clickable GUI button that changes gameplay must validate the same requirements as a normal decision. It must show costs and missing requirements clearly. It must call scripted effects that can also be used by AI, decisions, focuses, and cleanup systems.

Event targets are valid scope pointers inside scripted GUI triggers, effects, and scripted localisation. Preserve `event_target:` usage when a GUI action intentionally carries a country, state, or character pointer across clicks, localisation, or event chains. Audits must verify that the target is referenced in a valid scope and that its lifecycle is safe, including cleanup for global targets and stale-target handling. Do not require migration to variables or remove an event-target GUI pattern merely because a variable could represent the same pointer.

Animated leader portraits, animated route emblems, glow effects, particles, and float effects should be used for major reveals, high-chaos escalation, hidden formables, supernatural leaders, or final transformations. Each animated asset needs a static fallback and manifest entry.

### 3D model and entity integration

Integrate model packages through the 3D owner and review their exact consumers, actions, assets, and runtime handoff.
Read the complete requirements in [3D model and entity integration](references/scripted-systems-and-country-integration.md#3d-model-and-entity-integration) before this work.

### Generated asset handling

Use the `chaos-redux-event-assets` skill whenever an event task requires generated or processed visual assets.

For every generated asset:

1. Create the base artwork by following the image generation workflow (see the Image-generation route section of chaos-redux-event-assets).
2. Save the original generated image as a source PNG in the active event-scoped temporary `docs/assets/<event_id>_<event_slug>/` workspace.
3. Create a processed PNG preview at the correct HOI4 target size in that temporary workspace.
4. Convert the processed PNG to DDS 32 bit unsigned BGRA 8.8.8.8.
5. Move the DDS into the correct mod asset folder.
6. Add or update the matching sprite definition in the correct `.gfx` file.
7. Update localisation, docs, and event spreadsheet entries that reference the asset.
8. Record the asset in the active workspace manifest and requirement-to-runtime crosswalk.

The asset manifest must include:

- asset name
- asset type
- source PNG path
- processed PNG path
- final DDS path
- target size
- sprite name
- intended in-game use
- related event id
- notes

Do not leave a runtime asset only in a temporary folder. While the event is active, retain the source, processed preview, manifest, crosswalk, and handoff in `docs/assets/<event_id>_<event_slug>/` for evidence and review. Before declaring the event goal fully complete, promote durable provenance, licensing, attribution, coverage, review, and wiring facts into permanent `docs/events/`, `docs/plans/`, `docs/specs/`, `docs/super_events/`, or another appropriate documentation surface, verify that no runtime reference points into `docs/assets/`, and delete the complete event-scoped workspace. If the event is blocked or incomplete, keep the workspace and report the blocker. The absence of the deleted workspace is expected for a fully complete event and is not an asset blocker.

## Documentation rules

Event-specific documentation belongs in `docs/events/`.

Preferred naming pattern:

- `docs/events/<zero_padded_id>_<slug>.md`, matching the event script file naming

Keep one canonical doc per event chain instead of splitting mechanics across multiple top-level docs unless the user explicitly asks for that.

Event doc structure:

1. What the event is.
2. Event map and subevents.
3. Trigger and runtime flow.
4. Main gameplay effects.
5. Supporting systems touched.
6. Event-owned Chaos changes when relevant.
7. AI behavior if relevant.
8. Baseline progression, evolution tracks, and escalation flow if relevant.
9. World-end and super-event integration if relevant.
10. Connections with other events if relevant.
11. Asset wiring and sprite expectations if relevant.
12. Limitations if any.
13. Open tuning notes and future expansion ideas.

### Docs and gameplay must stay aligned

When mechanics change, update the matching event doc in the same change.

Do not leave the doc describing:

- old triggers
- old cooldowns
- old stage counts
- removed branches
- removed assets
- outdated spreadsheet or deck expectations

### Event catalog spreadsheet

Maintain the gameplay-facing event table in:

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Rules:

- use the `chaos-redux-xlsx` skill
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is the only editable catalog source
- after every successful workbook save, run `python .tools/export_event_catalog_csv.py` from the mod root
- the exporter overwrites `chaos_redux_events_catalog.csv`, `chaos_redux_clusters_catalog.csv`, and `chaos_redux_scenarios_catalog.csv`
- treat those CSVs as export-only read-only snapshots and never edit them directly
- write for players, not script readers
- don't put effects into descriptions
- focus on what happens in play
- keep the `Details` field aligned with the event-details window description
- keep evolution and world-end columns aligned with the real chain structure
- do not put baseline progression stages into evolution columns unless they are actual mutation tracks

#### Event catalog status contract

- Use exactly these status labels: `Playable`, `Partially Available`, `To Be Reworked`, `Unavailable`, and `Needs Testing`.
- `Playable` requires explicit approval and must never be inferred or assigned by default.
- `Partially Available` means the catalog row has a usable implemented surface but still has material unavailable, blocked, or incomplete content. It is not equivalent to `Playable`.
- Events 1–20 awaiting validation use `Needs Testing` unless the user explicitly approves another status.
- A post-20 catalog ID with an actual root definition in the mod (`id = chaosx.nr<ID>.1`) is `To Be Reworked`, including hidden, bridge, or placeholder roots. Do not infer availability from category-array membership alone.
- A post-20 catalog ID without an actual `chaosx.nr<ID>.1` root definition is `Unavailable`.
- Treat the workbook `Legend` sheet as the source for status, Type, Member Severity, evolution-column, and World-End colors. Keep dropdown ranges, conditional-formatting rules, static fills, and exported values synchronized with the Legend.
- These status rules classify catalog entries only and must not silently change runtime registration or enablement.
- `Needs Testing` and the absence of approval for `Playable` do not keep an otherwise completed implementation task open; retain the honest catalog label without waiting for user testing or requesting a status upgrade.

## Final event checklist

After editing report or news text, run `python .tools/audits/report_colour_audit.py` and resolve every colour-bearing parchment key, including scripted localisation output.
Before review, run `python -B .tools/check.py quick` on the changed files and fix every error it lists; it covers the colour audit, localisation and GFX wiring, the script syntax rules and MCP script validation, and proves only those properties (CLAUDE.md section 4a).

Before closing an event task, verify:

1. Event script is updated.
2. Event classification/registration arrays are updated.
3. Auto-firing or runtime hooks are updated if needed.
4. Shared effects, triggers, and constants are updated if needed.
5. Event-name and debug-name mappings are updated.
6. Event log actor mapping is updated if needed.
7. Evolution logging and preview wiring are updated if relevant.
8. Triggerable scenario registry, launch gates, type controls, intensity controls, localisation, documentation, and bypass cleanup are updated if relevant.
9. Every public terminal branch has its own stable Event Details registry row, owner event ID, independent default-enabled persistent toggle, clickable details, useful status handling where relevant, and automatic selection gate. Multiple public branches for one event remain independently controllable.
10. Hidden or easter-egg terminal branches are absent from public Event Details controls, public docs, and spreadsheet-facing public fields. Every terminal branch still preserves its scenario-specific flag, matching super-event linkage, 1000+ Chaos gate, world-state selection rules, and `world_end` guard.
11. If the event has a super-event, `chaos-redux-super-events` has been used for quote, remark, audio, and presentation planning.
12. Supporting decisions, ideas, AI, country setup, or exclusions are updated if relevant.
13. For every manifest-driven formable, the category attachment audit lists all in-scope category IDs and proves each one points to the generated state-puzzle scripted GUI. A formable family that declares strict all-category coverage has no static or text-only substitute where exact state control is central.
14. `docs/events/` is updated.
15. `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is updated, then `.tools/export_event_catalog_csv.py` is run so all three export-only CSV snapshots are refreshed.
16. If assets are required, `chaos-redux-event-assets` has been used.
17. During active work, generated assets are resized, converted to DDS 32 bit unsigned BGRA 8.8.8.8, moved into the correct folders, wired in `.gfx`, and recorded in the temporary asset manifest and crosswalk. Before completion, durable facts are promoted and the event-scoped `docs/assets/<event_id>_<event_slug>/` workspace is deleted, with no runtime reference left to it.
18. Spec-mapped mechanics, routes, countries, decisions, achievements, assets, and super-events are implemented or clearly reported as blocked, merged, renamed, skipped, or simplified.
19. Dynamic values, concrete costs, mechanic visibility, decision category filtering, and effect strength are checked where the spec calls for them.
20. Focus trees preserve route structure, focus filters, varied rewards, idea lifecycles, route-specific AI, and visible branch payoffs where relevant.
21. New fighting countries have dynamic starting forces, template assumptions, equipment and manpower handling, and reinforcement pathways.
22. Every new land sub-unit or equipment-backed special family has an explicit provider, support-attachment, or parent-owned disposition, owner-side registration and callback coverage, CXT coverage, and full unit-inventory audit.
23. Mapped event-owned Chaos changes are tied to concrete outcomes, guarded against repeat farming, and do not double count shared sources.

For helpers that iterate records or scopes, read [Loop break isolation](references/scripted-systems-and-country-integration.md#isolate-foreach-break-state).
