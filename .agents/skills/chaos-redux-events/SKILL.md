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

When an event or its owning system adds a land sub-unit or equipment-backed special family, declare its consumer disposition before wiring it: standalone provider family, support attachment under an existing provider, or intentionally parent-owned and not independently consumable.

A standalone family must register idempotently from the owner's existing startup path and expose the complete owner-side provider callback contract required by the shared consumer, including eligibility, template or spawn construction, sustainment, equipment-token resolution and publication, presentation, management, derivative setup, public-package removal, and cleanup where those surfaces apply. A support attachment must identify its provider and remain in the same provider-owned transaction or template. A parent-owned disposition must state the engine or consumer constraint and retain its unlock, equipment, sustainment, and cleanup behavior in the parent package.

Wire CXT coverage for every new land sub-unit or concrete equipment type through `docs/testing/chaosx_test_country.md`. Add a modifier-free hidden-idea carrier whose ID names the matching idempotent `_apply` setup effect, bounded startup registration, guarded tag-scoped daily repair, and weekly maintenance only when recurring work is not already covered by the shared CXT hooks.

Before completion, run a full inventory over all installed land sub-unit definitions under `common/units/` and concrete equipment definitions under `common/units/equipment/`, including support definitions, then cross-check provider or parent-owned dispositions, owner registrations, concrete equipment tokens, presentation and localisation tokens, CXT registrations and synchronizers, and duplicate or missing IDs. Every entry must be covered or explicitly blocked with the engine reason.

Do not extend a central consumer-maintained family list, equipment switch, or localisation selector when an owner-side provider contract can supply the data. A missing provider or malformed registry row is a blocking integration failure, not permission to substitute a generic family.

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
- Spawn `chaosx_improvement_loop_planner` after a meaningful implementation tranche when several new mechanics, country packages, formables, focus routes, decisions, scripted GUI surfaces, super-event candidates, or lore systems have been added and the event needs deeper connection. Do not spawn it again for the same event until the previous addendum is implemented, folded into specs, queued with a reason, or rejected.
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

Route every character portrait to `chaosx_portrait_creator`. Do not generate a real historical leader or an invented substitute for a grounded polity. For grounded packages, the portrait worker sources attributed real subjects or authentic institutional material, records provenance and rights status, creates the explicit crop and placeholder, and later installs the user-supplied HOI4-style final. It invokes native ImageGen only when both the polity and leader are wholly fictional and deliberately high-chaos, then processes and wires the result. Every new flag uses imagegen. Historical flags and well-attested real symbols first require cited design research, then a strict flat reconstruction with no fabric scene, painterly flag artwork, fake lettering, or invented heraldry.

Any new, released, restored, transformed, or event-managed country that is expected to fight needs starting forces and a reinforcement pathway. Implement dynamic starting units, templates, equipment and manpower assumptions, commander or officer handling when relevant, and later unit growth through decisions, focuses, depots, objectives, volunteers, foreign support, mobilisation, or special mechanics. Do not leave a serious fighting country as an empty tag unless the spec says so and explains why.

Major events and country-creation events need route-specific AI. Implement focus choices, decision choices, unit-raising choices, faction behavior, foreign influence behavior, rare variant handling, high-chaos exceptions, invalid-route blocking, etc.

When an event needs a reusable country carrier, consult `common/collections/chaosx_country_collections.txt` and `docs/events/006_independence_wave/systems/country_registry.md` before reserving a new tag. Use the `chaosx_country_*` collection that matches the region or origin, then record the consuming event's own provenance and package identity before loading content. Do not create a duplicate tag for an Event 006 or Soviet Collapse carrier, and do not treat event-text mentions as tag collisions. After changing a protected carrier or its references, perform a fresh repository-wide collision scan against vanilla, installed Workshop mods, and sibling local mods. The legacy country-tag auditors under `.tools/archive/` are provenance only and are not current acceptance tools.

Do not reduce major spec effects to tiny decorative modifiers. Important effects must change incentives, unlock content, move visible mechanic values, alter army or economy behavior, create a real tradeoff, or connect to later outcomes.

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

Report and event descriptions drawn on light parchment must use plain text for names and values, without `§` colour formatting, including strings returned by scripted localisation.
Keep colours only in supported dark option, tooltip, decision, or GUI consumers; use separate plain and coloured localisation variants when a shared helper feeds both.
Audit the whole owned description family and its dynamic substitutions for contrast in the actual consumer, including at 1080p.

Native PowerShell stdin can replace non-ASCII program text before Python receives it, even when Python writes a UTF-8 BOM correctly.
For localisation writes through that route, use ASCII program text with Unicode escapes or `chr()` for the `U+00A3` texticon and `U+00A7` formatting glyphs, or read the intended text from an explicitly UTF-8 file.
Re-read the affected values as UTF-8 and verify their actual glyphs after writing.
If an existing OneDrive-backed source file repeatedly rejects write-open with `OSError: [Errno 22] Invalid argument`, write the reviewed bytes to a uniquely named sibling file and replace the exact owned target atomically.
Preserve BOM and line endings, verify both resolved paths stay in the intended directory, and re-read the target immediately before replacement to confirm its bytes still match the edit baseline.
If another writer changed it, rebuild the narrow edit from that fresh content instead of replacing their work; retain or remove only the task-owned temporary file on failure.
When normalizing physical line endings, preserve authored `\n` escapes inside localisation values rather than rewriting them as literal `\r\n` escapes.

Event Details text must never display mechanical effects. The Event Details window, spreadsheet `Details` field, and player-facing detail summaries should describe the situation and premise, not list rewards, penalties, modifiers, variable changes, or script effects. If an event is meant to apply gameplay effects immediately regardless of which option the player chooses, place the real effects in the event `immediate` block inside a `hidden_effect`. The option should not reapply those effects. The option may show the immediate result only through a custom tooltip for cosmetic clarity, so the player sees the consequence without turning Event Details into an effects list.

Player-facing event, decision, focus, and Event Details text must describe in-world consequences rather than meta reward routes. Do not advertise that a choice opens, grants, counts toward, or completes an achievement path. Keep achievement conditions in achievement UI and docs, and use ordinary in-world consequence text elsewhere. For ambiguous report-stage incidents, describe what people see, fear, suffer, or fail to explain. Do not directly label the incident as a warning, a non-warning, a danger signal, or the absence of one.

Visible dynamic values often display decimal places unless their localisation formatter says otherwise. If a value is conceptually an integer, show it as an integer with `|0` formatting or an equivalent scripted-localisation helper. Only show decimal places when the value genuinely needs fractional precision, such as ratios, percentages, fractional costs, or progress values where the fraction changes player decisions.

For numeric `defined_text` output, put the formatted variable in a real `.yml` localisation value, such as `numeric_value_display: "[?temp_value|0]"`, and use the key's literal name in the corresponding `text` block: `localization_key = numeric_value_display`.
An inline formatted variable string such as `localization_key = "[?temp_value|0]"` is tokenized as a dynamic key and may fail with dynamic-token errors.
Temporary variables assigned in the same `text.trigger` remain visible to the selected localisation key, so calculate the display value there.
Retain constant-backed temporary getters where the installed documentation supports the assignment, and do not introduce persistent globals solely for formatting.

### Helper output lifetime

Temporary variables first created inside a scripted effect or trigger may disappear after return, while caller-preinitialized storage retains the helper's modifications (`paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, Variable types, line 440).

- Before each helper call, ensure every temporary scalar and temporary-array output consumed afterwards has caller-owned storage, including calls inside `if.limit` and scripted-localisation `text.trigger`. Initialize new output storage without resetting existing input or cursor values.
- Apply this at every nested call boundary: each caller initializes the outputs it consumes, and outer callers also initialize forwarded outputs needed after return.
- Public helper API docs must list caller-owned output storage and its required initial values.
- Actual-source tests must model conservative call-frame cleanup by discarding temporary scalars and arrays first created in the returning helper, retaining modifications to caller-preinitialized storage, and keeping scoped regular saved state separate from temporary storage instead of using one flat global temporary dictionary.

When a source audit or fixture cannot model this call-frame lifetime, report it as unmodelled and separately check caller preinitialization before consuming helper outputs.
For shared dispatchers, locate the matching authorization gate and recursively inspect its body and invoked helpers for actual dispatch and accounting, including package-specific nested branches.
A flat block-shape assertion or literal marker match does not establish that execution coverage.

Native effect loops stop after 1,000 iterations, so pending-queue recovery must preserve the unvisited suffix and every unacknowledged receipt rather than clear the whole queue and rebuild only visited rows.
Process a bounded batch by popping each selected row before recovery and appending unresolved rows behind the unvisited suffix, without adding a world scan.
Clear a receipt only after its matching recovery is acknowledged.
Actual-source fixtures must enforce the native loop ceiling and verify more than 1,000 queued rows across repeated invocations, unresolved-row rotation, and receipt preservation.

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

## Chaos source handling

Implement event-owned Chaos changes only on concrete outcomes defined by the spec, using the shared Chaos Meter and history path. Common hooks include meaningful movement success, special Chaos-country growth, spread, failed containment, actual use of dangerous capabilities, and durable containment or defeat.

Use one-shot milestones or thresholds where needed so routine growth cannot farm Chaos. Do not duplicate generic sources such as wars, annexations, deaths, contamination, or nuclear use unless the event adds a separate consequence that the generic source does not represent.

Evolution state itself always gives zero Chaos. Eligibility, activation, stage advancement, logging, or unlocking content changes nothing until evolved behavior actually causes a concrete consequence.

Before completion, check that mapped event-owned changes fire at the intended outcome, do not repeat incorrectly, and appear through the shared Chaos History path.

### Evolution implementation

The implementation must preserve the design split between baseline stages and evolutions.

Baseline progression can use whatever state, flags, variables, decisions, or events the mechanic needs. Do not record every normal stage as an evolution unless the spec deliberately treats it as an evolution track.

For actual evolutions, the usual pattern is:

1. the evolution condition becomes available from the current campaign state
2. the evolved incident, track, or milestone fires through MTTH-based dynamic pacing rather than instantly, and it can take a good amount of time: the base should be around 90 days, but it can be more or less depending on the evolution. Some happen instantly, for example for events that haven't fired yet, which makes the initial firing more intense
3. set the shared evolution context variables
4. record the evolution log entry through the shared pipeline
5. unlock or adjust the new behavior, tag, decision set, focus branch, or rare variant
6. do not change Chaos for the evolution state itself. Any Chaos change must come from a separate concrete consequence

Event evolutions that gate content must respect the enable and disable UI. If an evolution is disabled, the gated path must have a clean alternate route or must be safely skipped. Do not leave required baseline progression locked behind a disabled evolution.

The shared context is:

- `events_log_evolution_event_id`
- `events_log_evolution_type`
- `events_log_evolution_stage`
- `events_log_evolution_tier`
- `events_log_evolution_actor` when the milestone belongs to a specific country

Then:

- gate the milestone with `is_current_evolution_enabled = yes`
- call `record_events_log_evolution_entry = yes`
- If a helper sets a `*_recorded` flag or unlocks follow-up content, set the shared evolution context before its `limit` and include `is_current_evolution_enabled = yes` in that same limit. Disabled evolutions must not set recorded flags that later stages, decisions, reports, or focus branches read.
- When a logged evolution has an actor, save the country as `events_log_evolution_actor` and set `events_log_evolution_has_actor = 1` immediately before `record_events_log_evolution_entry = yes`. Regular event targets cannot be manually cleared and can leak through an effect chain, so no-actor records must rely on the shared logger's default `events_log_evolution_has_actor = 0` behavior instead of raw `has_event_target`.

Implementation design rules:

- `event_id` ties the evolution to the parent event.
- `type` separates parallel mutation tracks inside the same event.
- `stage` is the milestone inside one mutation track, not the ordinary event stage.
- `tier` is display-oriented. Do not use it as a substitute for real logic state.
- When a track uses stage-specific incidents, wire the stage-specific display text across every event-log view that can show it: list/current view, history/detail view, event-detail view, selected-detail title, selected-detail body, and any stage-number or roman-numeral helpers needed by the highest stage.
- Use dynamic factor models for evolution chance, pacing, intensity, and aftermath.
- If an evolution creates a persistent country, make the country playable or meaningful enough for its expected lifetime.

### Event-log UI surfaces

Before changing evolution log display, identify the exact surface and keep the change scoped to that surface. Patch the actual GUI/localisation/scripted data path. Do not record a process note as a substitute for fixing the visible row.

- **Main Evolutions tab** uses `global.events_log_evolution_view_*`, `events_log_evolution_index`, and `events_log_evolution_entry_*` templates. This is a global logged-evolution history surface. Rows should visibly show the log index, date, source event, evolution name, tier, and stage.
- **History details related evolutions** uses `global.events_log_history_detail_evolution_*`, `events_log_history_detail_evolution_index`, and `events_log_history_detail_evolution_entry`. This is the selected-event filtered logged-evolution history surface. Rows should use the same visible metadata as the main Evolutions tab.
- **Event details evolution catalog** uses `global.events_log_event_detail_evolution_*`, `events_log_event_detail_evolution_index`, and `events_log_event_detail_evolution_entry`. This is a catalog/preview surface, not a history log. Do not add fake log indexes, fake dates, or history-only metadata here.

When adding evolution row metadata, reuse the arrays for that row surface: main rows read the `global.events_log_evolution_view_*` arrays rebuilt by `rebuild_events_log_evolution_view`, while selected-history rows read the `global.events_log_history_detail_evolution_*` arrays rebuilt by `events_log_rebuild_history_details_view`. The required row metadata is sequence, date, source event, type/name, tier, stage, actor, and enabled state. If the user reports row alignment, patch `interface/chaosx_events_log_popup.gui` row sizes, button bounds, and text widths for the affected surface in the same change.

Event-log defaults must keep unreworked events disabled by default. An event that is still waiting for a rework should stay out of the reworked-event default enable allowlist so startup seeds it into `global.disabled_events` and it appears unchecked. When an event is reworked and ready for normal selection and log use, add its ID back to that allowlist in the same change as the event registration and log wiring.

## World-end scenarios

A world-end scenario is a terminal branch that changes the campaign into a resolved or end-state condition, not just a large disaster or strong major event. It is chosen based on the world state and can only be triggered when the chaos value is over 1000.

### World-end scenario implementation

The normal contract is:

1. guard the branch with `NOT = { has_global_flag = world_end }`
2. set `world_end`
3. set a scenario-specific global flag
4. set the matching `super_event_visible`
5. update the matching super-event text, image, and audio wiring
6. stop or gate incompatible future systems and branches
7. document the end-state in the event doc, and spreadsheet

Classify every terminal branch as public or hidden/easter-egg before wiring Event Details.

For every public terminal branch, complete the Event Details contract in the same implementation pass:

1. Give the branch a stable scenario registry entry and the owning event ID.
2. Create one row per branch. If one event has several public terminal branches, do not collapse them into one event-level row.
3. Give each row its own default-enabled persistent toggle state. Rebuilding or reopening Event Details must not reset it, and toggling one branch must not change sibling branches or the parent event.
4. Add player-facing title and details text that explains the premise and terminal state without listing raw effects, hidden variables, secret conditions, or implementation state.
5. Wire the row, selection, toggle, and detail-panel clicks through the shared Event Details behavior. Add availability or status text when it helps the player understand why a public branch cannot currently be selected, without exposing hidden logic.
6. Make automatic world-end selection read the branch toggle. A disabled branch is skipped as a candidate without disabling its owning event, suppressing enabled sibling branches, bypassing the 1000+ Chaos gate, or changing the normal world-state selection rules.
7. Keep the scenario-specific global flag and matching super-event visibility, text, image, and audio linkage distinct for that branch.
8. Align the public event doc and spreadsheet-facing world-end fields with the same title, premise, terminal state, and branch count.

Hidden or easter-egg world-end scenarios may retain a stable internal registry identity with hidden visibility, but they must stay out of the projected public Event Details rows, title/detail selectors, toggles, status controls, public docs, and spreadsheet-facing public fields. Their terminal flagging, chaos gate, selection logic, and super-event wiring still follow the normal world-end contract.

## Triggerable scenarios

Triggerable scenarios are manual sandbox or challenge setups launched from the Chaos Redux settings UI. They are separate from the normal random-event timer, chaos-tier eligibility, evolution pacing, and automatic source-event prerequisites.

Core rule: a triggerable scenario is always directly fireable from the scenario UI unless the launch would be impossible or conflict with an active terminal state. It creates instant chaos from setup controls, not from live Chaos Meter progression. After launch, ordinary event behavior resumes.

Use this contract when adding a scenario for an event:

1. Register a stable scenario ID and sort value in `triggerable_scenarios_initialize_registry`.
2. Add tuning constants in `common/script_constants/chaosx_triggerable_scenarios_constants.txt` for scenario IDs, sort values, intensity stops, scenario type IDs, and scale values.
3. Add or update launch, registry, sorting, intensity, and type effects in `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`.
4. Add launch eligibility in `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`.
5. Add scripted GUI click handling, dynamic list support, slider stops, and visibility checks in `common/scripted_guis/chaosx_scripted_gui_settings.txt`.
6. Add scenario name, sort text, detail text, type labels, and intensity impact text in `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`.
7. Add or update player-facing labels, tooltips, confirmation text, and scenario event text in `localisation/english/chaosx_gui_l_english.yml`.
8. Update `interface/chaosx.gui` only when the existing scenario window cannot present the new controls cleanly.
9. Document the scenario in the relevant event doc or scenario doc, for example in `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/systems/event_system/triggerable_scenarios.md`.

The scenario window is data-driven. It should use `global.triggerable_scenario_view_ids` for the sortable list, log-style entries for scenario rows, and a detail panel that updates from the selected entry. Do not hardcode one button per scenario when the registry and dynamic list can handle it.

The scenario button should open a confirmation window. Confirming must read the selected scenario, type, and intensity at launch time. Do not bake these values into the first click.

Intensity uses the existing four-stop scenario slider:

- Low
- Medium
- High
- Maximum

The selected intensity should be stored in `triggerable_scenarios_intensity`. The knob position, impact text, and launch effects must all read the same stored value. If a scenario deliberately ignores intensity, state that in its detail text and keep the slider harmless.

Scenario type controls are scenario-specific. If a scenario has types, define type constants, cycle buttons, labels, detail text, and launch branches.

Launch gates are not normal event prerequisites. They should only block impossible or conflicting launches, such as a required source country not existing, a required target scope being impossible to build. Do not block a triggerable scenario because chaos value, chaos tier, prior event state, evolution unlocks, date gates, route prerequisites, or super-event history flags are missing.

When a triggerable scenario needs to force a path that is normally gated, use an explicit scenario launch flag or variable. Scope the bypass tightly to the launch effect and clear it when the scenario setup is finished so automatic event behavior remains governed by normal event state.

Triggerable scenarios may call source-event helpers, unit-spawn helpers, release helpers, super-event helpers, or world-end helpers, but the scenario wrapper owns manual setup choices, intensity scaling, scenario type routing, confirmation flow, and bypass cleanup. Shared helpers must stay idempotent when the scenario and normal event chain can both call them.

The scenario UI normally reuses existing Chaos Redux and vanilla UI assets. Do not request dedicated scenario art, report images, icons, or animated UI unless the user asks for them or the existing scenario window cannot communicate the mechanic. If the UI requires a sprite entry for technical reasons, register a stable placeholder path and report that it is a placeholder.

Completion for a scenario-backed event requires:

- scenario ID and sort registration
- launch effect and confirmation flow
- launch eligibility using the same gate for click enablement and button state
- intensity and type controls wired
- scripted localisation and GUI localisation
- bypass flags scoped and cleaned up
- no normal chaos, evolution, date, route, or super-event-history prerequisite blocking manual launch
- documentation updated without listing stale or implementation-only debug details

## Major-event defeat aftermath

Some major events should also have a structured aftermath when the threat is beaten.

Use a defeat aftermath package when all of these are true:

- the defeated threat was global or near-global in reach
- the campaign lasted long enough to feel like a world crisis
- the cost in casualties, destruction, or political disruption was high enough that the world should not simply snap back to normal

Typical aftermath content:

- a defeat super-event or defeat-stage super-event effect
- postwar treaties, compacts, or new world orders
- recurring remembrance, reconstruction, or vigilance events
- lasting ideas, tech-sharing groups, or diplomatic rules that exist because the world learned from the crisis

Do not add a treaty/new world order after every contained or short-lived disaster. Those only make sense when the event genuinely reshaped the campaign.

## Event implementation workflow

### MCP event-chain pass

For long or cross-file chains, use the read-only `hoi4.event_inspect`, `hoi4.event_render`, and `hoi4.event_compare` tools to map entry points, branches, state and scope flow, impact, and structural changes. Event-owned GUI surfaces may also use `hoi4.gui_inspect` and `hoi4.gui_render`. Edit event source through the normal workflow, then compare and lint again. MCP evidence augments the event contract below and does not replace source review or the completion audit.

Check the live selector schema before narrowing an event call: an event selector is `selector: { kind: "event", eventId: "namespace.id" }`, not a bare `eventId` or `id` object.

#### MCP evidence gate

Before treating an inspection or render as lifecycle evidence, read its `analysisMode`, `complete`, indexed `counts.helpers`, `filesScanned` or source-hash inventory, unresolved entries, and diagnostics. `trace` and `explain_path` use focused analysis, and `scan`, `roots`, `lint`, or `event_render` use focused analysis when a selector is supplied. Focused analysis reads only `events/**/*.txt` and `common/on_actions/**/*.txt`, disables workspace-wide helper projections and lifecycle passes, and keeps the focused-boundary blocker even when `expandHelpers = true`. `state_flow` and `impact` request full analysis even when narrowed, while selector-free `scan` requests full analysis. Use a full route when helper or lifecycle coverage is required, and do not treat a focused trace or a zero helper count as proof that the chain has no helpers. If the required event route is unavailable, record the exact blocker and do not substitute source-only evidence.

When the connected server and live schema confirm `mode = helper_expansion` under the checks in `chaos-redux-subagents`, use bounded `hoi4.event_inspect` pages for large helper closures with distinct source-linked call paths. Continue with the returned opaque URI until `finished`, and report `complete`, source revision, depth stops, cycles, dynamic or missing references, and source coverage separately. If that route is unavailable, use the installed event routes and record the helper-coverage limit. Helper pages are coverage tools; they do not replace ordinary event inspect, render, compare, or scenario evidence, clear the focused-analysis lifecycle boundary, or prove runtime outcomes. Follow the verified job/task handling in `chaos-redux-subagents`.

`event_compare` accepts cached revisions, validated event-graph artifacts, or proposed source overlays. Report-only trace artifacts and render or manifest artifacts can fail `artifactUri` graph validation because their report or render schema does not contain an event-graph payload. Use a graph-bearing artifact or another supported compare input when available. If none is available, preserve the exact blocker and do not invent a conversion or comparison result.

For event-option `ai_chance`, event MTTH, direct random chance, and `random_list` logic, route the audit through `chaosx_ai_probability_auditor`. It must use `hoi4.probability_inspect` before choosing scenarios, then use `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_simulate`, or `hoi4.probability_compare` only for the surface being reviewed. Use `hoi4.probability_sequence` only when a complete custom-pool manifest explicitly declares cadence, recovery, caps, cooldowns, removals, resets, timer changes, and terminal states. Use `hoi4.probability_render` for timing, matrix, sensitivity, sequence, comparison, or unresolved views when they make the result easier to audit. Provide complete option or list pools when normalization applies, and provide scheduled state changes for timing questions. Treat exact, bounded, sampled, score-only, and unresolved results as different evidence. The analyzer does not choose balance targets or edit event source. If the probability route is unavailable, record the exact blocker and do not substitute source-only analysis. For `hoi4.probability_compare`, pass both `before` and `after` as `probabilitySourceSchema` objects with a source `identifier`/`path`, `inlineClausewitz`, or `virtualPatch`, or pass both `beforeManifest` and `afterManifest` under an identical `scenarioSet`. Do not put a cached `analysisId` in `identifier`, because `analysisId` belongs only to `hoi4.probability_render` and is not a compare source.

When the live schema exposes `snapshotPath`, bind a frozen copy with `{ path: original_engine_relative_path, snapshotPath: archived_workspace_relative_path, expectedSourceHash: copied_bytes_sha256 }`.
Some domain adapters use the logical engine path to recognize weighted blocks, so selecting only a documentation path or an inline fixture can return `PROBABILITY_SURFACE_EMPTY` even when the copied script parses.
Verify the before and after source identities and matched blocks before interpreting that result as a missing capability or input-size limit.

After renames, action consolidation, or edits that shift line-based candidate ids, inspect both sides before choosing `candidatePool`.
A filter containing only current ids can empty the frozen baseline, while removed ids can empty the current side; use the union of verified ids or each side's exact local source selector where supported.
Keep decision and mission adapters separate, and report unresolved target-scope and eligibility inputs rather than treating a definition-level comparison as target-level probabilities.

For deterministic max-score selectors, track explicit first-valid-candidate presence and accept that first candidate regardless of its score.
A numeric best-score sentinel must not reject an otherwise valid negative score.
After the first candidate, retain the exact score comparison and existing ID tie-break without changing weights or eligibility.

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

An event always needs more than its own script file.

Touch the relevant systems in the same change:

- decisions and categories if the event creates player tools, responses, or for example containment mechanics
- ideas or dynamic modifiers if the event creates persistent gameplay state
- AI strategies or templates if the event changes how AI should respond
- special-country exclusions if the event touches broad civilian, political, migration, or ideology systems
- Chaos Meter hooks when the event owns Chaos-changing outcomes
- shared country classification when the event creates or manages chaos countries, as required under [Event-created country setup and audit](#event-created-country-setup-and-audit)
- and much more

Keep the complete bodies of `is_special_chaos_country`, `is_actual_nonhuman_country`, and `uses_normal_civilian_systems` inside `hidden_trigger`. Player-facing callers that need to explain eligibility must provide a concise custom tooltip instead of exposing the classifiers' tags, flags, or provider triggers.

If you add a new reusable dynamic scripted effect (an effect that could be generalized for all events), document it in `common/scripted_effects/chaosx_dynamic_effects.md` in the same change.

#### Native special-project output overrides

Do not assume duplicate native project IDs safely replace or partially merge definitions across filenames.
For approved vanilla project output changes, use a complete replacement at the same relative vanilla file path unless the relevant engine merge behavior is proven.
Repeating full definitions in a distinct mod filename can duplicate enable-equipment or module list entries.

- Check installed native documentation, current vanilla source, and every existing mod owner of the file and project IDs before editing.
- Retain original tuning, availability, rewards, and file-scoped constants, including other projects in the replaced file, while adding only approved owned output hooks.
- Record vanilla source paths and SHA-256 hashes, then remove only the owned hooks from a comparison copy and verify exact remaining content against those sources.
- Check effective source-ID uniqueness after same-path masking, including other mod files that still declare the IDs.

Source equality establishes preservation only, and must not be described as engine validation.

#### Event-created country setup and audit

If the event creates or manages non-standard countries, account for that in shared classification triggers. Any event-created or event-managed chaos country must be registered in `is_special_chaos_country` in `common/scripted_triggers/chaosx_dynamic_triggers.txt` and documented in `common/scripted_triggers/chaosx_dynamic_triggers.md`. If that chaos country is actually nonhuman rather than merely unusual, supernatural, extremist, or scenario-specific, also register it in `is_actual_nonhuman_country` and update the same documentation. Do not create event-specific duplicate classifiers such as `is_<event>_chaos_enemy`, `is_<event>_special_country`, or per-event nonhuman triggers when the shared triggers can express the category. Events interact with each other, so systems that usually affect normal countries, such as black plague, mass panic, civilian migration, or ideology spread, should exclude zombie, alien, and other nonhuman countries through the shared triggers instead of one-off checks.

When an event can create a normal tag that may also already exist from vanilla, another mod, or prior campaign state, track whether the event actually created it before loading a runtime focus tree. A good pattern is to set a country flag immediately after `release = TAG` and have the focus-tree loader check that flag before `load_focus_tree`. Existing tags with their own meaningful trees should get crisis ideas, decisions, events, or additive branch integration, not a blind replacement tree.

Before registering any new country, cosmetic, formable, or route tag, audit it against vanilla, Chaos Redux, every installed Workshop mod, and other local mods. Do not add a duplicate new country for a national identity that already exists in vanilla: reuse the vanilla tag, preserve the living country and its meaningful content, and add only safely gated Event content. If a proposed new tag conflicts anywhere in the installed set, remap it and update every script, history, localisation, asset, manifest, scenario, documentation, and catalog reference together. Apply any event-specific suffix convention only after the collision-free tag is locked.

When auditing event-created country packages, verify the whole playable-country surface, not only the release effect. Check country files, custom-tag history files, additive startup grants for existing countries, generated startup scientists when needed, tag registration, base localisation, ideology-specific cosmetic localisation (`TAG_democratic`, `TAG_communism`, `TAG_fascism`, `TAG_neutrality` plus `_DEF` and `_ADJ`), flags, decision/focus/idea icons, focus loading, AI strategy, docs, and manifests together. For existing-country variants, verify the event-created flag is set only on the release path and every `load_focus_tree` path is gated by that flag. Do not copy vanilla country, state, or unit history only to add Chaos Redux technologies, equipment, facilities, traits, or other additive setup. Put that setup in `common/scripted_effects/chaosx_startup_history_effects.txt` and call it from `on_startup`. Static named characters requiring persistent script tokens must be recruited in history. Do not use runtime `recruit_character` or attempt a character-scope transfer of an unrecruited identity. For dated identities, a bounded `history/general` recruitment pool on a dedicated dormant holder is valid; the holder must have no owned states or gameplay route and must not reuse an event-owned playable holder or test harness. Check date eligibility and original ownership before transferring from the original owner's country scope with `set_nationality = { target_country = <destination> character = <static_token> }`. Preserve availability dates, roles, identity flags, and retirement gates. Use `generate_scientist_character` only when a generated unnamed identity without a persistent character token is intended; never silently replace approved static identities with generated substitutes. Validate native execution separately from source proof.

Every registered country tag, including stateless dormant or internal history holders, needs valid default and ideology flag lookup coverage in `gfx/flags/` (`82x52`), `gfx/flags/medium/` (`41x26`), and `gfx/flags/small/` (`10x7`) because native flag consumers remain active without territory or a playable route.
Use the existing `chaos-redux-event-assets` workflow for this minimum native consumer package, with asset authorization limited to that package and intentionally shared institutional designs across aliases documented in the manifest.
Validate actual 32-bit uncompressed bottom-left TGA headers and decoded orientation against installed and repository examples, correcting flag files directly without UI or dynamic-routing workarounds.

#### Country activation and ROOT

Stored state pointers refer to persistent map objects, so do not use COUNTRY-only `exists = yes` inside a STATE scope.
Validate the intended state with an appropriate documented native STATE predicate or registered state marker such as `has_state_flag`, together with its expected state ID using the documented identity semantics.
`scope_exists` is always true for variable scopes and does not validate the stored pointer.
Retain `exists = yes` checks in actual COUNTRY scopes, including a state's owner, controller, or stored country pointer.

Entering another country scope does not rebind ROOT.
Capture and annex callbacks retain their native ROOT: `on_annex` has the winner as ROOT and the annexed country as FROM, while `on_state_control_changed` has the new controller as ROOT, the old controller as FROM, and the changed state as FROM.FROM.
Trace each callback-to-helper scope chain before changing a receipt read.
When a country helper enters its exact source-state pointer, PREV there is the calling project owner, so read that owner's receipt through PREV rather than the callback's ROOT.
Within a state's stored-owner or holder country scope, return explicitly to the state through PREV for state flags.
PREV depends on the actual nesting, and ROOT remains valid wherever the contract explicitly requires it.

In a participant-country iterator reached from a country event, `ROOT` remains that event's original recipient across participant-country and state scope changes.
For targeted decisions, verify the actual callback's `ROOT`/`FROM` contract against installed documentation and a native precedent rather than assuming the owner's country-event contract: in the standard targeted-decision context, `ROOT` is the country taking the decision and `FROM` is its target country or state.
Capture the intended current participant with regular `save_event_target_as = participant` in that participant's country scope before entering state scope, then use `event_target:participant` for helper payer, victim, and target-country inputs and participant receipt or idempotence flags.
Using an unrelated `ROOT` can misattribute deaths and receipts even when the correct state was selected; retain `ROOT` wherever the documented callback or helper contract requires it.

For synchronous country transactions that can launch nested helper work, `ROOT` remains the original sender, temporary loop indexes are unscoped, and regular event-target names are shared throughout the effect chain.
Nested transaction setup can overwrite both indexes and named targets, so a regular event target alone is not a frozen transaction input.
Before any helper that can launch nested work, capture the proven source and origin pointers, actor/episode/receipt identity, and outer row indexes into recipient-owned normal private input fields.
At durable context commit, read those frozen fields and validate real object existence plus exact actor, episode, and receipt identity, rather than trusting overwritten aliases or `scope_exists` on a variable scope.
Restore outer row indexes only from that frozen frame, and clear the private fields on every success or rejection return while preserving the public immediate outputs.

Require matching actor/state nonce mirrors and exact source-state identity before closing a receipt or applying its accounting.
Use actor-owned persistent state pointers for asynchronous local projects and revalidate site identity and current holder at resolution.
Cleanup for a nonexistent or dead actor must not clear another living actor's global selection.
Partition recorded-owner and physical-holder accounting by the state disposition so each amount is debited and credited once even when both pointers identify the same country.
Review matching and stale nonces, distinct and identical owner/holder identities, repeated closure, and dead-actor cleanup along the exact source call chains.

When setup helpers require the recipient country as ROOT, invoke them from a hidden triggered-only country event received by that country; regular event targets carry through events fired by the originating effect chain.
Apply this ROOT contract to country scopes entered by `for_each_scope_loop` or debug dispatch as well.
Country-owned helpers need an explicit actor input contract or a generation-bound `country_event` relay rooted in the actual recipient.
Revalidate the saved recipient and generation before dispatching the helper, and cover direct actor entry and foreign-root debug/iterator entry separately.
Give a dormant tag owned land and a valid capital before entering capital-based setup or spawning units; use runtime meta construction when its TAG scope must be deferred until activation.
For a player-transfer bootstrap, queue the delayed recipient event before `change_tag_from` and make player transfer the final effect in that country block, so receiver scheduling does not reuse an invalidated country scope.
Inject file-scoped duration constants as meta arguments when generating a new script buffer, rather than leaving an unresolved `@` token inside generated text.
State transfers preserve stored variables, so a dedicated sandbox fixture must assign its intended responsible-country pointer before registration when it replaces an inherited site; ordinary historical responsibility should remain intact.

History grants can run before the recipient has a capital or other countries are initialized.
Keep their local grants and records, but queue capital-dependent scoring and diplomatic refreshes until country activation rather than dropping gameplay outputs.
Guard capital entry with an owned-state capital check; entering `capital_scope` to test whether it exists can itself raise an invalid-target error.

An exposed database array may include its reserved default object alongside real content.
Before excluding an entry, verify the array's registration order, the database's default-object initialization, and the consuming effect or trigger's validity check against installed documentation or other direct engine evidence.
Exclude only the confirmed reserved slot; do not guess that a numeric value or token is invalid, and preserve dynamic coverage of every real entry.
Keep read-only engine inspection distinct from executed runtime validation.

When additive tag-specific hooks can each request a full registry synchronization, coalesce their requests behind one pending recipient event instead of repeating the full consumer pass inside each hook.
Track scheduled delivery separately from pending work when an immediate refresh can consume that work before the queued event fires; this avoids scheduling duplicate receivers for a later request.
Set the scheduling flag before enqueueing, clear scheduling and pending-work flags before dispatch, and retain an immediate apply path for explicit setup or refresh.
Verify registration convergence, repeated requests, and refresh while a request is pending; preserve every registry consumer and package repair hook.

When bounded controller-country callbacks service a STATE-owned mechanic, keep each independent review or growth date persistently on that state and gate advancement on elapsed time.
Controller changes must preserve those dates so cycling controllers or receiving duplicate callbacks cannot accelerate the same mechanic's cadence.
Callback count is not elapsed time.

When a terminal record stops maintenance but an achievement or outcome still needs elapsed-time verification, schedule a one-time callback in the record owner's scope guarded by a persistent due date and a pending receipt consumed before verification.
Preserve the original due date across narrow controller changes, rescheduling only the remaining delay when delivery needs repair.
Revalidate the exact record and eligible actor tag under the existing identity contract, preserving any actor-specific invalidation.
Check early, duplicate, transferred, and stale-actor deliveries without adding a periodic world scan.

### 5. Event log integration

Events must appear in Chaos Redux’s event log, so wire the full log contract in the same change.

Script ownership:

- Put history/evolution recording, actor sanitizing, default actor mapping, Event Details catalog rows, event-detail evolution previews, and History/Evolutions/Events tab rebuild logic in `common/scripted_effects/chaosx_events_log_effects.txt`.
- Keep random selection, fired-event handlers, timers, and event type accounting in `common/scripted_effects/chaosx_logic_effects.txt`. Those effects should call the shared Event Logs recorders rather than defining log arrays themselves.
- Keep settings controls and generic event firing helpers in `common/scripted_effects/chaosx_settings_effects.txt`. Do not add new event-log history/evolution display logic there unless the settings window itself is changing.
- Keep button click routing in `common/scripted_guis/chaosx_scripted_gui_events_log.txt`, and layout changes in `interface/chaosx_events_log_popup.gui`.

Required name plumbing:

- add or update visible event-name loc in `localisation/english/chaosx_event_names_l_english.yml`
- update event-name selectors in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- update debug-name selectors in `common/scripted_localisation/chaosx_scripted_localisation_debug.txt`

Required actor plumbing when a flag should appear:

- update `events_log_set_default_actor_for_current_event` in `common/scripted_effects/chaosx_events_log_effects.txt`
- use a default actor only when the event should show a meaningful actor before or without a fired history row
- if fired history should override the default actor, keep the history-context flow intact
- for random-event history rows, remember that the generic fired-event handler records the row before the target event's `immediate` block runs. If the actor is created or refreshed inside that event, move that preparation into a shared pre-fire helper and call it before `record_events_log_history_entry`
- for evolution rows with actors and no-actor entries, follow the `events_log_evolution_actor` and `events_log_evolution_has_actor` rule under [Evolution implementation](#evolution-implementation)

Required detail-view plumbing:

- update the event-details text selectors in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- update the actual user-facing text in `localisation/english/chaosx_gui_l_english.yml`
- if new generic event-log behavior is needed, wire it through:
  - `common/scripted_effects/chaosx_events_log_effects.txt`
  - `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
  - `interface/chaosx_events_log_popup.gui`

Do not hardcode one-off GUI behavior if it should be reusable by later events.

Public world-end rows are part of the shared Event Details data path. In `common/scripted_effects/chaosx_events_log_effects.txt`, register them through `initialize_world_end_scenario_registry`, rebuild them with `events_log_rebuild_event_detail_world_end_scenarios`, persist disabled scenario IDs in `global.disabled_world_end_scenarios`, and toggle the selected row through `events_log_toggle_selected_world_end_scenario_disabled`. Keep automatic branch gates in `common/scripted_triggers/chaosx_world_end_scenario_triggers.txt`. Route row, selection, and detail clicks through `common/scripted_guis/chaosx_scripted_gui_events_log.txt`. Keep titles, details, and status selectors in the existing Event Details scripted-localisation and GUI-localisation files. Change `interface/chaosx_events_log_popup.gui` only when the shared row or detail layout itself needs a reusable control.

When it's impossible for an event to fire due to conditions (the actor country doesn't exist, prerequisite not fulfilled, etc), always show `N/A` in the event list in place of a `0` for the weight.

### 6. Event cluster integration

Event clusters are a catalogue layer above normal random events. The Clusters tab must show every registered cluster, while History shows only clusters that actually fired.

Core files:

- `common/script_constants/event_cluster_constants.txt`
- `common/scripted_effects/chaosx_event_cluster_effects.txt`
- `common/scripted_effects/chaosx_events_log_effects.txt` when event-log view state changes
- `common/scripted_effects/chaosx_settings_effects.txt` when settings controls or generic event firing helpers change
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt` when cluster log UI behavior changes
- `interface/chaosx_events_log_popup.gui` when cluster list/details layout changes
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `localisation/english/chaosx_gui_l_english.yml`

To add a new cluster:

1. Add an ID in `event_cluster_id`.
2. Add any cluster-specific tuning group, for example `event_cluster_<slug> = { unlock_tier cooldown_days }`.
3. Register the cluster in `initialize_event_cluster_definitions` by pushing aligned entries into `global.event_clusters`, `global.event_cluster_type_entries`, and `global.event_cluster_unlock_tier_entries`.
4. Map member events in `event_belongs_to_cluster`, from normal event ID to cluster ID.
5. Add ordered member rows in `load_event_cluster_members`.
6. Add or update cluster name/type/description scripted localisation and GUI localisation.
7. If it needs custom runtime setup, add that branch to `event_cluster_prepare_runtime_context`.
8. If it needs a custom cooldown or one-time state, update `mark_event_cluster_fired_state` and any availability logic in `can_event_cluster_fire`.

Member attributes are parallel arrays in `load_event_cluster_members`:

- `temp_event_cluster_member_event_id_entries`: normal event ID.
- `temp_event_cluster_member_role_entries`: `event_cluster_member_role.required` or `event_cluster_member_role.optional`.
- `temp_event_cluster_member_chance_entries`: participation chance for optional members, usually from `event_cluster_member_participation`.
- `temp_event_cluster_member_min_tier_entries`: minimum chaos tier for that member.
- `temp_event_cluster_member_danger_entries`: display severity in cluster details.

To change a member's behavior, edit those attributes together. Do not reorder one array without the others.

Member severity uses four values:

- Low
- Medium
- High
- Severe

Cluster firing rules:

- Automatic cluster firing happens from `try_fire_event_cluster_for_selected_event` after a member event is selected.
- Automatic firing respects cluster unlock tier, cooldown, one-time state, member eligibility, optional participation rolls, and runtime context.
- Manual firing from Settings uses `force_fire_event_cluster_by_temp_id`. It bypasses tier, cooldown, disabled-state, and member availability checks. Runtime context can still fail if the event cannot build the required scopes.
- Cluster history rows are recorded by `record_events_log_cluster_entry`. Cluster catalogue rows are rebuilt by `rebuild_events_log_cluster_view`.

When inlining a multi-condition scripted trigger inside `NOT`, keep the conditions in an explicit `AND` block; sibling conditions in `NOT` use NOR semantics.
Preserve the original rejection behavior when either a shared precondition or the native legality check fails.
For temporary diagnostics inside a state-scoped effect, check country flags through the intended country scope, such as `ROOT`, rather than the state scope.

### 7. Duration fields and constants

Use `script_constants` for shared tuning, but remember that some duration fields reject both `constant:` and variable tokens.

Before adding or extending `script_constants`, read the installed `common/script_constants/documentation.md` and `documentation/script_concept_documentation.md` (Script Constants), then inspect the existing group.
Every new group must begin with `schema` matching its key and data kinds (`int`, `fixed_point`, or a documented complex schema); new keys in an existing group inherit and must satisfy that schema.
A basic brace parse does not validate schema correctness.

**Variable arithmetic evidence:** Distinguish getter, modifier, normal variable and script constant representations, read installed `documentation\script_concept_documentation.md:184-215` and offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:425-434`, and record precision conflicts rather than inferring a universal normal variable maximum from mathExpr fixed point, modifier-only three-decimal precision or deprecated raw-manpower getter overflow near 2.1 million.
Audit actual source operations with a conservative bounded fixed-point model, explicit rounding/truncation assumptions and independent integer-floor boundary and count-type cases; a later division or clamp does not prove intermediate safety, and passing unbounded Python arithmetic does not prove engine behavior.
Never turn an unsupported numeric maximum into an eligibility gate or no-payment policy, or silently cap actual history.
For integer receipt validation, prefer modulo by one on scratch storage using documented `modulo_temp_variable` (installed `documentation\triggers_documentation.md:6442-6454` and `documentation\effects_documentation.md:4986-4998`) without rounding the receipt or adding maximum/count caps; use ratio quotient/remainder or rational scaled coefficients only when proven equivalent under the stated arithmetic assumptions.
Keep script constant category IDs unique across files so helpers with different schemas cannot redeclare the same category.

Known sensitive fields:

- `set_country_flag = { days = ... }`
- `set_global_flag = { days = ... }`
- any other timed field that throws `Malformed token` for either `constant:category.key` or a variable token

Fields in the list above are the ones that reject variable tokens as well, so they take a file-scoped `@NAME = literal` constant in the same script file passed as `days = @NAME`. Keep the value mirrored with the matching `common/script_constants/` tuning entry, and update both in the same change.

For any other duration field that rejects `constant:category.key`, assign the constant to a normal or temporary variable first and pass that variable to `days =`. A `meta_effect` must be used when the field accepts neither form.

Scripted effects and scripted triggers do not expand `$PARAMETER$` placeholders or accept named argument blocks as a parameter API in HOI4.
Pass inputs through documented variables or tokens and invoke the helper with `= yes`.
For literal-only fields, use `[PARAMETER]` inside `meta_effect` or `meta_trigger` `text` with a matching replacement declared on that meta block; consult installed documentation and a vanilla precedent before relying on a substitution.

Meta replacements are captured while the `text` is built, before its effects execute, so compute a delay or amount before invoking the meta block that consumes it.
If that computation belongs behind a dynamic meta guard, call a small owner helper after the computation inside the guarded text, and let that helper build the literal-consuming meta block.
Preserve eligibility, exactly one random draw, due-record ordering, and duplicate checks; do not move RNG ahead of the guard to resolve capture timing.
Verify dynamic support for the specific effect field against installed documentation, the offline wiki, and vanilla; a `country_event` variable-delay precedent does not establish `state_event` support.

### 8. Super-event integration

If the event shows or drives a super event, wire the whole package:

- choose the slot intentionally
- set `super_event_visible`
- set `global.current_super_event_audio_id`. Every super-event has a unique audio id and unique final track.
- register the final cue as a game-ready WAV under `sound/<event_id>_<event_slug>/...`
- add the base sound definition and required settings-volume soundeffect wrappers to `sound/chaosx_sound.asset`
- play the cue with `play_current_super_event_sound = yes`, the settings-aware sound helper
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

## World threat framework

If an event or mechanic creates an existential external threat that should push other systems toward cooperation, integrate it with the shared world-threat framework instead of inventing a new one-off flag.

Current shared state:

- aggregate flag: `world_in_threat`
- source-count variable: `global.world_threat_source_count`
- per-source flags named `world_threat_source_<source>`; the registered list lives in `refresh_world_threat_state` and `docs/systems/world_threat_mechanic.md`
- per-source read triggers live in `common/scripted_triggers/chaosx_world_threat_triggers.txt`

Implementation pattern:

1. create or reuse a threat-specific source flag
2. write a threat-specific refresh effect that sets or clears that source flag from real gameplay conditions
3. update `refresh_world_threat_state` in `common/scripted_effects/chaosx_dynamic_effects.txt`
4. expose reusable scripted triggers if other systems should read the new source directly
5. document the threat source in the mechanic doc

Do not create a parallel global "cooperation crisis" or "threat active" flag for a single event chain. Everything should fold back into `world_in_threat`. The exact purpose of that flag is not yet planned.

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

### Retiring unused helpers

- Before deleting a scripted effect, trigger, or `defined_text`, search every placeholder constructor (`[ID]`-style `meta_effect`/`meta_trigger` text, `@` token pasting, `[EXTENSION_EFFECT]_apply`) and the GUI, `.gfx`, localisation, and docs for the name; a zero token count alone does not prove the code is dead.
- Delete the comment header attached directly above the removed block, or it will describe the next definition.
- After each removal pass, rescan for helpers, localisation keys, and script-constant keys whose only consumer was the removed code, and repeat until nothing new appears.
- Repository files can mix CRLF and LF line endings; edit them line by line with their own endings instead of splitting on one newline style.

## Event catalog spreadsheet

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

### Event catalog status contract

- Use exactly these status labels: `Playable`, `Partially Available`, `To Be Reworked`, `Unavailable`, and `Needs Testing`.
- `Playable` requires explicit approval and must never be inferred or assigned by default.
- `Partially Available` means the catalog row has a usable implemented surface but still has material unavailable, blocked, or incomplete content. It is not equivalent to `Playable`.
- Events 1–20 awaiting validation use `Needs Testing` unless the user explicitly approves another status.
- A post-20 catalog ID with an actual root definition in the mod (`id = chaosx.nr<ID>.1`) is `To Be Reworked`, including hidden, bridge, or placeholder roots. Do not infer availability from category-array membership alone.
- A post-20 catalog ID without an actual `chaosx.nr<ID>.1` root definition is `Unavailable`.
- Treat the workbook `Legend` sheet as the source for status, Type, Member Severity, evolution-column, and World-End colors. Keep dropdown ranges, conditional-formatting rules, static fills, and exported values synchronized with the Legend.
- These status rules classify catalog entries only and must not silently change runtime registration or enablement.

## Formable nations as event surfaces

When an event can create or empower countries, consider whether it should create formable nation routes. A formable can be a major event payoff, a late-game ambition, a hidden branch, a rare evolution reward, a country package route, or a post-crisis consolidation goal.

Event implementation must keep formables aligned across:

- event flags and route flags
- decision category visibility
- focus unlocks
- scripted triggers for state control
- scripted effects for formation
- cosmetic tags and country names
- flags and portraits
- AI strategy
- achievements
- super-events where the formation changes world order
- cleanup after tag switch, annexation, puppet transfer, civil war, or route failure

Use scripted helpers for formation effects. Do not duplicate formation logic in events, decisions, focuses, scripted GUI buttons, and achievements. The decision can pay the cost and validate requirements, while a shared helper performs the identity change and logs the result.

Hidden formables should still have implementation coverage. They need reveal events, hidden flags, visibility triggers, localisation, assets, AI rules, and cleanup.

When exact state control is the formation proof, use the manifest-driven state-puzzle workflow under `.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/`. Keep the generated state pieces, shared territory helper, formation decision, AI path, and every in-scope decision category synchronized. Complete the companion `category_attachment_audit.md` and list every category that exposes the formable, including shared or phase-specific categories.

When an event declares the strict `all_formable_categories` attachment policy, every in-scope formable category must set `scripted_gui = <generated_state_puzzle_gui_id>` and point to the generated `context_type = decision_category` block for its manifest. A category picture, text-only description, or separate status GUI does not satisfy this rule. A missing or mismatched category row is an incomplete formable surface and must remain a blocker in the handoff.

## Scripted GUI and animated event presentation

Major event mechanics can use scripted GUI windows, decision-category interfaces, animated leader portraits, or custom buttons when they make the system easier to play. Treat that UI as part of the event contract, not as decoration added later. Static or animated category pictures are eligible only for simple categories with a description, an ordinary decision list, and at most basic value tables. Do not add category pictures alongside an existing complex category GUI, meters, extra custom buttons or controls, rich interactive panels, or other animations. Normal decision-list action buttons are allowed, and the category picture itself may be animated when this simple-category gate passes.

Use `chaos-redux-scripted-gui` for every authorized scripted GUI layout change, including parent-owned shared surfaces. Create/select the reference before implementation and record its acceptance basis and native-element mapping under that skill. When the event specifically adds a dedicated scripted GUI or mechanic window, route its bounded layout implementation and visual-quality pass to `chaosx_event_ui_worker`. The worker must use `hoi4.gui_inspect`, thorough `hoi4.gui_render` state/resolution/hierarchy/click-region views and post-change comparison evidence, treat the production render as the one-to-one in-game visual view, fix every defect visible there, and follow the full reference-image, native-layout, and visual-review contract in `chaos-redux-scripted-gui`. Never send the shared event log, event-details framework, settings, super-event framework, shared registries, or unrelated existing UIs to this worker. Eligibility requires accepted spec or source evidence that the named event introduces and owns the UI. Apply authorized reviewed source edits directly or optionally through `gui_rewrite`; its automatic post-write/index validation is not a mandatory gate under `chaos-redux-scripted-gui`.

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

For a formable state puzzle, add the manifest-to-category attachment crosswalk to this contract. Verify every in-scope category metadata block against the generated scripted-GUI identifier and window, then use the actual read-only `mcp__hoi4_agent_tools__hoi4_gui_inspect` and `mcp__hoi4_agent_tools__hoi4_gui_render` routes for the linked category window. Do not claim category coverage from a state-piece render alone.

Every player-clickable GUI button that changes gameplay must validate the same requirements as a normal decision. It must show costs and missing requirements clearly. It must call scripted effects that can also be used by AI, decisions, focuses, and cleanup systems.

Event targets are valid scope pointers inside scripted GUI triggers, effects, and scripted localisation. Preserve `event_target:` usage when a GUI action intentionally carries a country, state, or character pointer across clicks, localisation, or event chains. Audits must verify that the target is referenced in a valid scope and that its lifecycle is safe, including cleanup for global targets and stale-target handling. Do not require migration to variables or remove an event-target GUI pattern merely because a variable could represent the same pointer.

Animated leader portraits, animated route emblems, glow effects, particles, and float effects should be used for major reveals, high-chaos escalation, hidden formables, supernatural leaders, or final transformations. Each animated asset needs a static fallback and manifest entry.

## 3D model and entity integration

When an event creates or changes a 3D unit or building, treat the model as a runtime contract across the event, unit or building definition, entity, `.asset`, `.gfx`, materials, textures, actions, and live map consumer.

The event implementation must use the `chaos-redux-3d-model-pipeline` handoff instead of trying to produce geometry or animations inside event work. The model handoff must include the exact runtime identifiers, processed texture paths, `.mesh`/`.anim` paths, action names, scale crosswalk, provider and Blender evidence, and reimport proof.

For a spawned unit, validate that `create_unit` is executed in a country or other supported scope, that the unit template and sub-unit are registered, that every emitted `unit_<id>_icon_small` text icon exists when required, and that movement uses a real exported action rather than a static substitute.

For a building or map entity, validate that the building has an entity, the entity key resolves in the `.gfx`/`.asset` chain, the province belongs to the specified state, the building command has the correct argument count, and the test province is visible at the intended zoom without an existing building hiding it.

For map-entity allocation, distinguish typed country/state scope references from documented plain numeric IDs, and do not assume `THIS.id` is a displayed state number or country ordinal.
Host fixtures must preserve that distinction and reject undocumented pointer arithmetic instead of seeding scope references with ordinary integers.
Allocate entity IDs from a proven numeric getter or an existing verified literal map ledger, then audit uniqueness and collisions against every existing and proof allocation because `create_entity` replaces an entity with the same ID.
Preserve scope pointers separately for identity and durable target links.
Source/model and collision checks do not prove native playback or save/restore entity identity, and do not establish that every native arithmetic conversion is impossible.

The main event agent owns the gameplay and runtime source wiring, final runtime copy synchronization, province/state placement, and review of live-consumer and in-game evidence supplied by the user. The user performs live-consumer and in-game validation. The 3D worker owns the bounded model package and must not claim event or in-game completion.

## Generated asset handling

Use the `chaos-redux-event-assets` skill whenever an event task requires generated or processed visual assets.

For every generated asset:

1. Create the base artwork by following the official `$imagegen` skill workflow through `chaos-redux-event-assets`.
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

## Final event checklist

After editing report or news text, run `python .tools/report_colour_audit.py` and resolve every colour-bearing parchment key, including scripted localisation output.

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

For helpers that iterate records or scopes, read [Loop break isolation](references/loop-break-isolation.md).
