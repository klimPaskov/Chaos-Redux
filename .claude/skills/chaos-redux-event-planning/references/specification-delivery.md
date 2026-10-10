# Specification delivery, prompts, and review

Read this reference before packaging a specification, splitting a large specification, preparing continuation or implementation prompts, or completing final review. Apply the formation and UI questions when those systems are present.

## Specification shape

Do not force the specification into a fixed template.

Choose the structure that best fits the event idea.

The specification should still be easy for a coding agent to use. Use clear headings, explain the logic in a natural order, and make sure important design decisions are not buried.

For major events, split the spec into parts if needed. Do not compress deep design just to fit one file.

Only include sections for surfaces that exist or that need design. If a world-end scenario, manual triggerable scenario, super-event, focus tree, custom country, achievement set, or asset family is absent, omit that section instead of writing that it is absent, because negative notes create noise and can mislead later agents into thinking the absence is a designed feature.

## Depth, file splitting, and continuation prompts

Do not compress the spec so much that important ideas become shallow.

The goal is depth, not speed.

Think through the event as far as the idea can reasonably go. If the event has multiple branches, evolutions, rare variants, custom countries, focus trees, UI elements, super-events, or major system connections, treat each of those as deserving real design space.

Large events should be written across multiple spec files and multiple chat responses when needed. Split at clean design boundaries such as core loop, evolutions, focus trees, decisions, country packages, assets, super-events, achievements, AI, research, or acceptance criteria.

Each part and file should be complete enough to be useful on its own. Stop at a clean section or subsection boundary when possible. If a large surface must continue, stop after a complete paragraph, table, route, country package, or list item instead of cutting a thought in half.

Do not summarize later sections because the current response is getting long. Continue in another part and save that part as another specification file for the final package. Use the available response space for real specification content.

### Temporary continuation prompt

When a large event specification cannot fit into one response, end the current part with a temporary continuation prompt for the next iteration. This prompt is a working chat handoff. It is not part of the final specification, downloadable package, event docs, prompt files, or repository source.

The continuation prompt should be concise and precise. It should include:

- the event id, event name, event slug, and current part number when known
- the exact section and subsection where the previous part stopped
- the last completed heading, route, table, country package, or file
- the next file, heading, table, route, country package, decision family, asset group, research task, or prompt file to write
- the files already completed or updated
- constraints that must continue to apply, including direction-only localisation, country naming rules, source rules, tag collision rules, animation rules, and the user's core event idea
- unresolved research needs, blockers, and accepted assumptions
- a reminder to continue with full-depth design and not summarize missing sections
- a reminder to avoid repeating completed sections except for the short context required to continue cleanly

Use the heading `Temporary continuation prompt, not part of the spec`. Keep it outside saved specification content. Every later part must create an updated prompt that reflects the new stopping point. Do not reuse an older prompt after the design has moved forward.

When the final part is complete, do not write another continuation prompt. Provide the completed package and completion summary.

### Optional resume packet

For very large work, compaction, interruption, or handoff to another agent, a separate `resume_packet.md` may be created as a working file. It belongs under `docs/plans/<event_id>_<event_slug>_plans/` after extraction, not inside the source specification files.

A resume packet should include:

- event id, event slug, and intended source spec folder
- files already written or updated
- exact section, subsection, route, table, or country package where work stopped
- next file, heading, route, decision family, country package, asset group, research brief, or prompt file to write
- constraints that must continue to apply
- unresolved research needs, blockers, and accepted assumptions
- a reminder to continue with full-depth design and avoid repeating completed sections

A resume packet may remain in a plan-only package when it is useful for later work. Temporary continuation prompts must never remain in the final source spec package.

For major events, the final combined specification may be extremely long. A 10,000 line, 50,000 line, or 100,000+ line specification is valid when the event needs that detail. Do not compress focus trees, rare variants, or decision webs into summaries to keep the package short.

Avoid filler. Every section should add useful design, player-facing detail, implementation clarity, asset direction, research evidence, or system connection.

Before saving the final files, run a cleanup pass. Remove generic safeguards, obvious implementation boilerplate, empty labels, repeated wording, admin audit sections, temporary continuation prompts, and temporary compaction notes that do not belong in the final package.

### Improvement-loop expansion specs

When `chaos-redux-improvement-loop` produces an expansion addendum, treat it as proposed event-planning input until its acceptance basis is recorded. Fold accepted design into the main spec pack with the same seriousness as the original user idea. Record the explicit user decision or parent acceptance within the user-authorized scope that supports each accepted claim. A spec path, status label, old handoff, or implementation evidence does not establish approval. Keep unsupported or conflicting claims unresolved and use the AGENTS.md Specs and Plans dispositions.

An improvement-derived spec can be shaped freely. It does not need to copy the section order of this skill. It should still make the design concrete. A useful addendum explains the playable promise, the route or mechanic that feels shallow, the deeper player loop, the choices that change outcomes, the AI behavior, the visual and localisation needs, and the surfaces that must align.

The planning agent should preserve the open structure of the addendum where that helps the idea. Use tables, route maps, prose, diagrams, or country package matrices only when they make the design easier to implement. Do not convert every improvement into a rigid checklist.

When an accepted improvement addendum includes formables, scripted GUI, animated sprites, animated portraits, or hidden routes, the final spec pack should carry that accepted design into the relevant files instead of leaving it isolated. The core spec explains why the expansion matters. The decision and focus files explain how the player reaches it. The asset prompt explains the static and animated visual work. The coding prompt and goal prompt tell the implementation agent to wire and validate it.

## Output rules

The event specification itself should be created as Markdown files.

Full event specification output belongs under `docs/specs/<event_id>_<event_slug>_specs/`. This is the source-of-truth design folder for the event spec pack.

Subagent planning addenda, audit follow-up plans, implementation notes, and temporary handoffs belong under `docs/plans/<event_id>_<event_slug>_plans/`. The plans folder is a working area. Accepted plan content should be folded into the relevant spec under `docs/specs/` when the final source-of-truth spec is updated.

Do not create new event specs, addenda, prompt packages, or extracted handoffs under `docs/planning/`, `planning/`, or any other planning folder. If a prompt says "planning folder", interpret that as `docs/plans/` for subagent plans and `docs/specs/` for source specs unless the user explicitly provides a different path.

The spec file should contain only the event specification.

Do not put the asset prompt, super-event prompt, coding-agent prompt, or goal prompt inside the spec file.

Keep planning files readable as design handoffs, not implementation blueprints. Prefer route purpose, player-facing behavior, balance intent, asset direction, AI intent, and acceptance criteria. Avoid long technical tables, exact constant lists, full scripted-effect recipes, exhaustive file inventories, parser-level implementation notes, and detailed code wiring. The specs you create are not implementation oriented. You do not give implementation guidance, you are just handing off ideas.

Create sequential files:

- `<event_id>_<event_slug>_spec_part_1_core.md`
- `<event_id>_<event_slug>_spec_part_2_<theme>.md`
- `<event_id>_<event_slug>_spec_part_3_<theme>.md`
- and more as needed

Do not repeat earlier sections unless needed for clarity.

### Final ZIP package requirement

The final chat-facing output must be delivered as one ZIP file containing every necessary file for the planning handoff. Individual files may also be linked for convenience, but the ZIP is the main deliverable.

The ZIP should include, when relevant:

- all specification Markdown files
- focus-tree path specification parts
- route diagrams or focus-tree sketches
- the asset prompt
- the super-event research prompt
- the achievement prompt
- the decision and mission prompt
- the coding-agent prompt
- the goal prompt
- research notes and bibliography files
- country package matrices, AI matrices, probability scenario matrices, decision maps, technology graph notes, 3D model briefs, and acceptance criteria created separately
- an optional resume packet for plan-only or interrupted work

Do not include temporary chat continuation prompts in the ZIP.

Use a clear package name such as:

`<event_id>_<event_slug>_planning_package.zip`

The ZIP should be directly extractable into the repository. For a completed source-spec package, use one top-level folder named:

```text
<event_id>_<event_slug>_specs/
```

That folder is intended for `docs/specs/`. Use descriptive repo-ready filenames inside it, for example:

```text
<event_id>_<event_slug>_spec_part_1_core.md
<event_id>_<event_slug>_spec_part_2_<theme>.md
<event_id>_<event_slug>_asset_prompt.md
<event_id>_<event_slug>_super_event_prompt.md
<event_id>_<event_slug>_achievement_prompt.md
<event_id>_<event_slug>_decision_mission_prompt.md
<event_id>_<event_slug>_coding_prompt.md
<event_id>_<event_slug>_goal_prompt.md
```

Use a top-level `<event_id>_<event_slug>_plans/` folder only when the ZIP contains subagent plans, follow-up handoffs, audits, blocked reports, or resume packets rather than the accepted source spec.

Do not force generic packaging-only folders such as `specs/`, `prompts/`, `research/`, or `matrices/` when descriptive repo-ready files in the event folder are clearer. Subfolders are allowed when a very large package genuinely benefits from them.

The goal prompt inside the package follows the character limits in [Goal prompt file](#goal-prompt-file).

## Final prompt files

Only after the full specification is complete, create separate prompt files outside the spec file and include them in the final ZIP package.

Required prompt files:

- `<event_id>_<event_slug>_asset_prompt.md`
- `<event_id>_<event_slug>_super_event_prompt.md` when the event has one or more super-events
- `<event_id>_<event_slug>_achievement_prompt.md`
- `<event_id>_<event_slug>_decision_mission_prompt.md` when the event has large decision or mission systems
- `<event_id>_<event_slug>_coding_prompt.md`
- `<event_id>_<event_slug>_goal_prompt.md`

The final answer should point to the final ZIP package as the deliverable and briefly summarize what the package contains.

### Asset prompt file

Create an asset prompt for `chaos-redux-event-assets`.

The prompt should cover all required visual assets, progression-state variants, final asset packaging, reference folders, source modes, and manifest requirements.

### Super-event prompt file

Create a super-event prompt for `chaos-redux-super-events` if the event has one or more super-events.

The prompt should cover title direction, description direction, quote research, cultural remark research, audio research, image direction, source documentation, licensing notes, and coordination with asset work.

The prompt must not provide unresearched final titles, button text, quotes, slogans, lyric fragments, cultural references, or final audio choices. Use research gates and role labels instead. It must tell the super-event researcher to produce the final text package only after source checks.

### Achievement prompt file

Create a separate achievement prompt file for the coding and asset agents.

The achievement prompt must include every planned achievement with id, title direction or working label, description direction, eligible countries, unlock conditions, disqualifiers, difficulty, hidden or visible status, why it is not trivial, icon direction, and all required tracking notes.

The achievement prompt should tell the implementation agent to inspect existing achievement patterns, implement the achievements, wire localisation and icons, create any required tracking flags or variables, document them, and avoid easy unlocks.

### Coding-agent prompt file

Create a coding-agent implementation prompt that summarizes the finished event spec.

The prompt must tell the coding agent to:

- implement the event according to the spec
- implement all mapped decisions, variants, evolutions, focus trees, custom tags, country packages, achievements, assets, and super-events included in the spec
- implement the complete Chaos impact map, including first manifestation, movement success, special Chaos-country power milestones, spread, concrete consequences produced by evolved behavior, failed containment, reversal sources, dynamic scaling, repeat guards, and shared-source overlap without double counting generic Chaos systems
- implement the mapped cost and sacrifice model, avoiding boring political power or command power only decisions when the spec calls for XP, equipment, manpower, stability, war support, fuel, supply, units, local support, foreign access, or other concrete costs
- preserve the public-facing mechanic value budget from the spec, preferring one or two persistent visible values, using three when the mechanic genuinely needs them, and never exposing more than four persistent values that the player must actively track across the entire mechanic. Keep supporting simulation values hidden when the player does not need to manage them directly
- implement focus trees according to the path design, with coherent non-linear branches, route locks, side paths, convergence nodes, hidden routes, focus filter tags or search categories, varied reward types, proper icons, final localisation written from the spec direction, AI behavior, event integration, and no filler shortcuts
- implement any planned focus inlay window through `chaos-redux-focus-trees`, reserve its space in the tree layout, and keep it clear of focuses and tree controls
- create the final exact focus layout and connections cleanly in implementation while preserving the spec's path logic
- implement every country package from the spec, including tag, history, names, cosmetic names, ideology names, ruling parties, leaders, leader changes, flags, route-specific identity changes, starting divisions, dynamic unit packages, force-growth decisions and focuses, volunteer routes, decisions, ideas, AI behavior, localisation, assets, and docs
- implement the full AI strategy matrix from the spec, including route preferences, foreign influence behavior, focus choices, unit-raising choices, decision choices, faction behavior, and high-chaos exceptions
- perform the full vanilla, Chaos Redux, Workshop, and local-mod tag collision audit before creating a new country tag, reuse existing vanilla identities when they already exist, and preserve living vanilla countries and meaningful existing trees
- use `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` when technologies, doctrines, folders, prerequisites, unlocks, grants, or research bonuses are involved
- route weighted behavior through one bounded `chaosx_ai_probability_auditor` pass with named representative scenarios and before/after source comparison; prefer targeted MCP tools and use source/helper evaluation when unsupported
- route required 3D model and skeletal animation production through `chaosx_3d_model_pipeline` with Codex `collaboration.spawn_agent` using `fork_turns="none"`, then implement and validate the final `.asset`, entity, `.gfx`, unit or building consumer, placement, and animation, and review available user-supplied live in-game evidence
- follow the flat reference-constrained image-generation rule for every flag and the sourced identity-preserving portrait rule for every grounded polity and real person
- follow `AGENTS.md`
- follow `chaos-redux-events`
- use `chaos-redux-event-assets` if visual assets are required
- use `chaos-redux-super-events` if super-events are required
- write final player-facing event, decision, focus, achievement, GUI, event-detail, and spreadsheet-facing localisation from the direction in the spec. Do not expect the planning spec to provide finished copy
- treat unresearched super-event titles, button text, quotes, cultural remarks, slogans, allusions, and audio choices as blockers, not as implementation-ready localisation
- keep all Chaos Redux systems aligned
- report anything that cannot be implemented cleanly
- keep iterating until the full spec is implemented to its fullest extent
- perform one bounded depth review where useful, through `chaosx_improvement_loop_planner` or the parent, and resolve actual design findings without repeated closure reports
- avoid fallbacks, simplifications, temporary versions, and good-enough approximations
- not claim completion until the implemented files satisfy the spec

### Goal prompt file

Create a separate `/goal` prompt file.

The goal prompt should be between 3500 and 4000 characters when the task needs that detail, and it must never exceed 4000 characters.

The goal prompt should not contain the whole spec or all long instructions. It should point to the spec files and the other prompt files, then state the most important pass or fail requirements.

The goal prompt must tell the implementation agent to keep iterating until the goal is accomplished to its fullest extent. It must also say not to claim completion until the implemented files satisfy the spec.

A good goal prompt should include:

- the spec folder and specification file paths
- the coding prompt file path
- the asset prompt file path
- the super-event prompt file path when relevant
- the achievement prompt file path
- the required skills or docs to follow
- the top design non-negotiables
- the requirement to implement every mapped Chaos source and reversal, including special Chaos-country growth and anti-farming guards, and to prove that generic Chaos sources are not double counted
- the requirement to create all required static and animated assets, static fallbacks, tags, starting divisions, reinforcement pathways, non-linear focus trees based on the mapped paths, focus filter tags, decisions, evolutions, achievements, and docs
- the requirement to research and source final super-event titles, button text, quotes, cultural remarks, and audio through the proper super-event workflow when super-events exist
- bounded depth review and disposition of accepted current-scope findings, with parent review when delegation is unavailable
- the requirement to audit all installed tag sources before adding custom tags and to reuse existing vanilla identities when applicable
- the requirement to use the technology graph tools when technology content exists
- bounded probability auditing of actual weights, helpers, and representative scenarios, with source comparison when tool support is unavailable
- the requirement to route and validate 3D model or skeletal animation work through `chaosx_3d_model_pipeline` when relevant
- the requirement to provide a concrete completion report

If the goal prompt is near 4000 characters, shorten it by pointing to files instead of repeating details.

## Cleanup and quality gate

### Review before completion

After the main design is assembled, review event specs, large addenda, country packages, focus-tree plans, decision systems, super-event plans, asset-heavy plans, formable plans, custom UI plans, and implementation handoffs for depth and unnecessary complexity.
Inspect the current spec, accepted plans, unresolved handoffs, asset needs, AI plans, mechanic surfaces, and implementation handoff needs.
Find remaining shallow systems, disconnected mechanics, missing route depth, missing AI behavior, missing asset states, missing aftermath, and scope bloat.

When delegation is allowed and useful, use `chaosx_improvement_loop_planner` with a self-contained `fork_turns="none"` prompt naming the event id, event slug, current goal, user constraints, spec and plan paths, known unresolved decisions, and exact question.
Otherwise the parent performs this review; missing delegation alone does not leave the spec incomplete.

Resolve an expansion addendum by folding accepted design into `docs/specs/<event_id>_<event_slug>_specs/`, implementing or queuing it with a clear reason, or rejecting it with a clear reason.
If the review recommends stopping expansion, record that conclusion in the existing handoff and finish the identified checks and fixes.
Accepted current-scope design must not remain unresolved at completion.
Recheck actual fixes; another full review needs new design work or a distinct unresolved design gap, not an unchanged report status.

Tiny known-file text edits, narrow typo fixes, and direct one-line skill updates need no design review when they do not change event design, mechanics, focus trees, decisions, country packages, assets, super-events, or implementation handoff rules.

### Formation and UI questions for planning passes

Before finishing a major event spec, ask:

- Can any country created or empowered by the event form a larger state later?
- Are there regional, ideological, hidden, or high-chaos formables that should be locked behind focuses, decisions, or events?
- Does each formable have concrete map requirements and a clear post-formation identity?
- Do formation rewards avoid free core spam, free war-goal spam, and instant runaway snowballing?
- Which presentation layer should each category use: ordinary category, static picture, animated picture, compact display, or full scripted GUI?
- Does the category pass the same eligibility gate for static and animated pictures, and if so, would a picture communicate the category more clearly than a complex custom window?
- If exact state control is central to a formable, does the plan use exact state shapes as grey and green dynamic puzzle pieces and keep them synchronized with real eligibility?
- If the named event introduces a full UI, does the plan route only the event-owned window to `chaosx_event_ui_worker` with exact identifiers and bounded visual checks and available before/after evidence while excluding shared interfaces?
- Are animated sprites, leader portraits, particles, glow, warning states, selected states, or button states planned only where motion makes a changing state clearer?
- Does the asset prompt include eligible category pictures, formable state pieces, sprite names, state logic, static fallbacks, and frame-sheet needs where animation is actually used?
- Does the goal prompt tell the implementation agent to verify formables, category-picture eligibility, state-puzzle eligibility, justified UI windows, and any animated sprite handoffs?

Before saving the final files, perform a strict review.

Reject the draft if it has any of these problems:

- vague placeholder decisions
- vague rare variants
- vague country paths
- custom tags without full country identity, assets, politics, leaders, flags, AI, and content expectations
- new or modified countries without country package matrices when they matter
- fixed or bounded countries whose territorial identity needs a capital and backup-capital plan but has none
- dynamic countries whose premise selects or renames a city but does not define how a valid capital, backup capital, and naming pool are chosen
- culture-changing routes that leave relevant city, victory-point, port, or regional names unchanged without a clear reason
- intelligence agencies, MIOs, advisors, theorists, high command, scientists, or operatives added only to fill a roster instead of supporting identity or gameplay
- countries whose naval or air role matters but whose starting forces, bases, variants, commanders, production, reinforcement, and AI behavior are not planned
- persistent playable countries without exact or dynamically derived starting research slots, technologies, economy, production, stockpiles, laws, subject status, and equipment identity
- events that cannot start, progress, finish, clean up, or remain balanced with no DLC or with a relevant DLC missing
- newly appearing crisis countries without dynamic starting unit packages or a clear reason why they start without troops
- country-created crisis specs without decisions, focuses, objectives, depots, volunteers, or faction systems that let those countries gain more units later
- new fighting countries without starting force plans, dynamic unit scaling, or reinforcement pathways
- new military country archetypes whose armies use only renamed vanilla division templates without an explicit unit-type assessment and a concrete mechanical and visual justification
- new custom unit families without a voice and Internet-sourced sound design pass, runtime sound roles, licensing/provenance direction, synchronization needs, bespoke counters for every consumer, exact installed-vanilla counter inspection, sampled vanilla green evidence, and icon-artist handoff
- long-lived new countries without dynamically scaled starting units or credible reinforcement routes
- newly appearing or transformed countries without mapped starting divisions, unit templates, equipment/manpower assumptions, and dynamic scaling factors
- countries with no designed way to gain, improve, convert, or coordinate more units through focuses, decisions, objectives, volunteers, depots, or faction mechanics
- generic repeated unit focuses or unit decisions that hand out identical divisions without story, route identity, or conditional requirements
- historical countries or movements with invented flag designs, uncited references, or unverified flat reconstructions
- real historical leaders planned as generated portraits instead of sourced portraits
- playable countries without clear focus-tree path maps
- focus tree sections that list only branch names without explaining path logic, mutual exclusions, rewards, and connections
- focus tree plans that give only vague samples without enough path detail for implementation
- focus trees where most focuses grant a new idea or national spirit without a clear reason
- focus trees with repeated new ideas where modifying or upgrading an existing idea would be better
- focus trees without an idea audit when many ideas or national spirits are used
- focus rewards that are mostly political power, stability, war support, or repeated flat modifiers
- focus trees missing varied reward types such as factories, forts, anti-air, airbases, railways, supply hubs, units, decisions, missions, advisors, leaders, identities, claims, or diplomacy where those rewards would fit
- major focus paths without focus filter categories or search categories
- major focus trees without a focus filter taxonomy or path category table
- major countries without separate political, military, industry, diplomacy, and expansion or special-mechanic sections when those sections fit the country
- focus trees that are too small, generic, linear, or boring for the country role
- focus trees missing distinct political, industry, and expansion branches
- important country trees with isolated branches that do not affect each other
- major branches without clear payoff
- political branches that do not change politics, leaders, advisors, parties, laws, names, flags, or country identity where relevant
- industry branches that do not change the map, production, logistics, construction, or resources
- expansion branches that do not create claims, cores, war goals, leagues, protectorates, settlement decisions, or external diplomacy
- expansion routes without postwar handling
- industry routes without geographic grounding where relevant
- major routes without route-specific AI behavior or localisation tone
- large events without a special mechanic or clear reason for not needing one
- special mechanics without clearly named public-facing values
- main mechanics that expose more than four persistent public-facing values the player must actively monitor or remember
- mechanics that use four public-facing values when one, two, or three could preserve the same meaningful choices more clearly
- value-heavy mechanics that split counters across tabs, tooltips, categories, focus inlays, Event Details, popups, or secondary windows to evade the mechanic-wide value budget
- hidden calculation components exposed as separate persistent counters when a public total, qualitative state, icon, trend, or concise cause summary would communicate the same information
- mechanic values without dynamic focus, decision, mission, event, war, state-control, foreign-influence, or AI hooks
- public-facing mechanic values without consistent visual identity or clear cause, consequence, threshold, and player response
- focus trees or decision systems disconnected from the mechanic values they should affect
- event-created factions without goals, rules, membership logic, shared decisions, AI behavior, rewards, or success and failure states
- special mechanics without a defined player-facing presentation surface
- decision categories with no documented presentation choice
- eligible simple propaganda, ideology, civil-war, preparedness, treaty, faction, or territorial categories expanded into full scripted GUI windows when a category picture would be clearer
- static or animated category pictures added alongside complex UI, meters, additional custom buttons or controls, rich interactive panels, or other animations
- basic formatted value tables or ordinary decision-list buttons treated as reasons to exclude category pictures or require rich GUI
- scripted GUI mechanics that genuinely need progress meters, status frames, variants, or animation but define only static text
- formable routes whose central proof is exact state control but have no exact-shape state-puzzle display or explicit reason for using an eligible static territorial picture
- special mechanics that hide basic visible cause and effect
- generic playable country packages with no specific identity, map role, military style, economy, diplomacy, AI, or mechanic
- shared trees with no country-specific localisation, route names, decisions, AI weights, leaders, or rewards
- AI routes that can choose invalid, impossible, or unavailable branches
- important mechanic values scattered as magic numbers instead of script constants or documented tuning
- reward dump design used as the main pattern
- balance plans without exploit checks for free units, factory loops, equipment farming, influence farming, puppet abuse, war-goal spam, claim or core spam, advisor stacking, bypass abuse, or repeatable decision abuse
- decision systems that show every possible action at once instead of using phases, caps, priorities, pools, route locks, thresholds, or crisis filters
- factions that form too easily without minimum membership, crisis pressure, ideological compatibility, war state, or diplomatic preparation
- routes with no visible game evidence beyond hidden variables or tiny modifiers
- large trees with no early, middle, and late pacing
- routes with no tradeoff or failure state
- overuse of mutual exclusions where support branches should coexist
- localisation that reveals hidden effects, secret outcomes, or future surprises instead of visible baseline effects
- route-unlocked advisors that do not match route identity
- major focus trees without achievement hooks
- completion prompts missing a route coverage table requirement
- meaningful design gaps left unreviewed or unresolved
- unresolved accepted current-scope design requirements or missing disposition of an expansion proposal
- focus trees where unit rewards are repeated generic division spawns instead of route-specific military institutions, decisions, templates, or mobilization systems
- unit-granting focuses that exist only as filler or repeated free divisions with no story, route logic, or constraints
- major focus trees that read like one vertical checklist instead of a branching system
- focus tree sections without an architecture map or path plan showing route locks, optional branches, convergence points, hidden routes, crisis branches, and late-game branches where relevant
- branches where every focus simply follows the previous one without a strong story reason
- expansion trees that are only linear claim ladders instead of ideology, trauma, patron, military, economic, or chaos-driven ambitions
- strange or destabilizing events with no direct Chaos source at first meaningful manifestation and no documented reason for the omission
- event-created movements that can become nationally or internationally powerful without any mapped Chaos gain at meaningful success thresholds
- special Chaos countries that can gain major territory, industry, population, subjects, strategic objectives, special capabilities, or regional reach without event-owned Chaos milestones
- concrete consequences produced by dangerous evolutions, failed containment, cross-border spread, or major event interactions that materially worsen the crisis but never feed the Chaos Meter
- repeated event Chaos sources with no threshold, cooldown, diminishing-return, first-area, or other anti-farming guard
- Chaos granted for evolution eligibility, activation, logging, stage advancement, or branch unlock when no concrete destabilizing consequence has occurred
- event-specific Chaos gains that simply duplicate shared war, annexation, deaths, contamination, nuclear, world-tension, or other generic Chaos sources without a distinct abnormal-significance reason
- containment or defeat routes that remove a major event-created source of instability but never consider a proportional Chaos reduction
- evolutions that are really just ordinary stages
- evolution specs that do not define whether each evolution enters through active-event evolution, pre-fire evolved opening, or both
- active-event evolutions that do not state what changes immediately for existing active actors
- pre-fire evolved openings that do not state how the first firing changes before the ordinary baseline starts
- triggerable scenarios with prerequisites, such as Chaos Meter state, event progression, evolution unlocks, date gates, global flags, or prior campaign state, unless the user explicitly requested a locked scenario
- triggerable scenarios that do not create instant chaos directly from setup controls, intensity sliders, or scenario options
- fixed cooldowns or pressure values without dynamic factors
- decision, mission, or focus cost plans that rely mostly on political power or command power when concrete costs such as XP, equipment, manpower, fuel, stability, war support, supply, local support, foreign access, or unit commitments would fit better
- achievements missing from a major event spec
- achievements that unlock too easily or only reward the obvious route
- achievements without conditions, disqualifiers, icon directions, or tracking notes
- missing asset handoff for required assets
- major mechanic, formable, hidden reveal, high-chaos route, scripted GUI, or dramatic leader transformation with no presentation-choice pass
- animated asset plan that lacks static fallback, state logic, frame-sheet handoff, target surface, sprite names, or `chaos-redux-frame-animation` ownership
- missing asset coverage for country names, cosmetic identities, ideology flags, focus-route flags, leader changes, portraits, faction emblems, decisions, focuses, ideas, achievements, and UI where relevant
- missing AI route matrix for major events, country-creation events, or foreign-influence systems
- missing super-event handoff for required super-events
- final event titles, event options, event descriptions, report prose, news prose, decision names, decision descriptions, focus names, focus descriptions, achievement titles, achievement descriptions, GUI labels, event-detail text, or spreadsheet-facing wording written as pasteable localisation when the spec should give direction only
- sample, possible, temporary, or placeholder player-facing text included in the spec when the coding agent should write the final wording
- super-event title, button text, quote, cultural remark, slogan, lyric fragment, allusion, or audio choice written as final content without research and source documentation
- placeholder, sample, or working super-event text that could be pasted into localisation
- role labels, asset names, achievement titles, or prompt filenames reused as final super-event localisation without research
- coding prompt or goal prompt that lets unresearched super-event text be implemented instead of treating it as blocked
- goal prompt over 4000 characters
- goal prompt that tries to contain the whole spec instead of pointing to files
- missing final zip package containing all required spec files, prompt files, route diagrams if used, research notes, and matrices
- new country tags created without inventorying vanilla, Chaos Redux, installed Workshop mods, and other local mods
- duplicate country identities created when a valid vanilla identity already exists
- living vanilla countries or meaningful existing trees overwritten without an explicit event requirement
- technology or doctrine changes without `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` requirements in the coding prompt
- weighted AI or event behavior without named probability scenarios and the correct inspection, evaluation, sweep, comparison, or rendering workflow
- visible 3D units, buildings, creatures, vehicles, aircraft, naval objects, or map entities without an asset profile, vanilla scale reference, source geometry measurement, action plan, provider lineage, export and reimport proof, wired consumer, and any available user-supplied screenshot evidence, with absent live proof reported as a limitation
- a side-profile sheet, turnaround board, collage, or multi-view board planned as a Meshy input instead of one clean reference image
- requested skeletal animations replaced by a static mesh or render
- historical or grounded flags that skip cited design research, flat reconstruction, or manual geometry comparison
- grounded polities assigned invented substitute people
- real leaders planned without sourced attribution, licensing notes, head-and-shoulders crop, identity preservation, and role-specific outputs
- temporary continuation prompts included in a saved specification, prompt file, or final ZIP package
- admin audit sections inside the spec
- major event ideas or spirits whose main effect is a tiny modifier with no meaningful strategic role
- obvious system plumbing repeated as design

The spec should be ambitious, detailed, researched, and usable. Do not stop at a conservative minimum when the idea supports more.
