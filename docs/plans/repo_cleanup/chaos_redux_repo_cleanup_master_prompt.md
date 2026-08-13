# Chaos Redux repository cleanup master prompt

Do a broad cleanup and maintainability pass across the Chaos Redux repository.

This is a large repository-wide cleanup task. Inspect broadly, but patch carefully. The goal is to make the mod cleaner, more reusable, better organized, better documented, and less duplicated while preserving intended gameplay behavior.

Follow `AGENTS.md` and all relevant repo skills. Use the offline Paradox wiki snapshot, vanilla HOI4 documentation, and vanilla examples when syntax or engine behavior matters. Use project subagents only when their scope helps the work. The parent agent remains responsible for final review, final integration, validation, and completion claims.

## Scope boundary

This cleanup must inspect the general Chaos Redux systems broadly. Do not limit the audit to event files.

General systems remain fully in scope, including:

- random event system
- event registration and event type handling
- event logs
- event details
- evolutions
- clusters
- triggerable scenarios
- settings and manual firing
- chaos meter
- deaths
- condemnation
- air cleanliness
- world threats
- world-end handling
- super-events
- scripted GUI systems
- shared scripted effects
- shared scripted triggers
- shared script constants
- scripted localisation
- localisation
- docs
- shared infrastructure and helper files

Event-specific implementation cleanup is limited to Events 1 through 20.

Do not audit, refactor, clean up, delete, preserve, or improve the old event-specific implementations for Events 21 and higher. Those events are waiting for full rework and their current event-specific code should be treated as obsolete implementation that will be replaced completely.

Events 21 and higher may only be inspected or touched when they appear inside a general shared system and the reference affects shared infrastructure. Examples include event registration arrays, event-log catalog entries, settings lists, triggerable scenario registries, shared helper references, shared localisation selectors, shared docs for the general event system, or stale references that block cleanup of shared systems.

Do not spend time improving old Events 21 and higher event chains, decisions, focus trees, ideas, country packages, assets, or localisation as standalone event content. If a reference belongs only to obsolete event-specific content, leave it for the future event rework or report it as out of scope.

## Main goals

1. Find repeated scripted logic that should become reusable dynamic scripted effects, scripted triggers, shared script constants, scripted localisation helpers, loops, or meta effects.
2. Find dead or unused scripted effects, scripted triggers, variables, flags, localisation keys, event helpers, GUI helpers, scripted GUI entries, decision helpers, and related code paths.
3. Identify dead code that was clearly meant to be used but is not currently wired.
4. Improve file ownership so each system has a logical place instead of scattering logic across giant mixed files.
5. Simplify code where it is safe and useful, especially obviously overcomplicated scripted logic, long condition blocks, repeated branching, manual state arrays, tangled helper chains, and multi-step flows that can be expressed with a clearer existing pattern.
6. Normalize inconsistent workflow patterns so similar systems use clear shared conventions for setup, validation, effects, logging, cleanup, documentation, and localisation.
7. Replace duplication with reusable helpers only when it improves readability and future maintenance.
8. Improve naming, organization, comments, and documentation where needed.
9. Keep gameplay behavior the same unless the cleanup reveals a clear bug.
10. If behavior changes, document exactly why the change is correct.
11. Keep documentation and localisation aligned with any cleanup that changes visible behavior, file ownership, helper behavior, or system wiring.

## Required starting points

Read and follow:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md` when cleanup reveals shallow or disconnected design
- `.agents/skills/chaos-redux-event-assets/SKILL.md` only when asset references or `.gfx` wiring need cleanup
- `.agents/skills/chaos-redux-super-events/SKILL.md` when super-event wiring, text, audio, image references, or docs are affected
- relevant offline Paradox wiki pages in `paradox_wiki/`
- relevant vanilla documentation in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`
- relevant vanilla examples under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`

Inspect existing reusable helper and tuning files before creating new helpers:

- `common/scripted_effects/chaosx_dynamic_effects.txt`
- `common/scripted_effects/chaosx_dynamic_effects.md`
- `common/scripted_triggers/chaosx_dynamic_triggers.txt`
- `common/scripted_triggers/chaosx_dynamic_triggers.md`
- relevant `common/script_constants/` files
- relevant subsystem-specific scripted effects, scripted triggers, scripted localisation, scripted GUI, decision, event-log, settings, cluster, scenario, chaos meter, and event files

## Scope to inspect

Inspect relevant gameplay text files, including:

- `events/` only for Events 1 through 20 event-specific implementations, plus shared event-system references to Events 21 and higher when they affect shared infrastructure
- `common/scripted_effects/`
- `common/scripted_triggers/`
- `common/script_constants/`
- `common/on_actions/`
- `common/decisions/`
- `common/decisions/categories/`
- `common/scripted_guis/`
- `common/scripted_localisation/`
- `common/national_focus/` only for Events 1 through 20 or shared hooks, not obsolete Events 21 and higher event-specific trees
- `common/ideas/` only for Events 1 through 20 or shared systems, not obsolete Events 21 and higher event-specific ideas
- `common/ai_strategy/`
- `common/ai_templates/` when relevant
- `history/` when country, state, setup, or tag references are involved for Events 1 through 20 or shared systems
- `interface/` and `.gfx` only where UI, GUI button logic, sprite references, or asset references need cleanup
- `localisation/` where keys, dynamic text, tooltips, event names, docs-facing labels, or player-facing text need cleanup
- `docs/` where system docs, event docs for Events 1 through 20, helper docs, plans, manifests, prompt files, or README-style docs need alignment
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` only through the spreadsheet worker when catalog fields need alignment with in-game wording

Do not inspect binary assets, DDS files, audio files, generated images, presentations, or spreadsheets unless a script, docs, `.gfx`, or manifest reference makes them relevant.

## Repository map pass

Start by building a practical map of the main systems and likely ownership boundaries.

At minimum, identify files and ownership for:

- core random event logic
- event registration and event type handling
- event log, event detail, evolution, and cluster display
- settings and manual event firing
- triggerable scenarios
- chaos meter, air cleanliness, condemnation, and deaths
- super-events
- world threats
- shared special-country and nonhuman classification
- formable handling
- decision systems and decision categories
- scripted GUI systems
- focus tree hooks
- country package hooks
- shared dynamic helpers
- shared script constants
- documentation and helper docs

This map does not need to become a huge report unless useful, but it should guide safe cleanup.

## Reusable logic audit

Search for duplicated or near-duplicated patterns such as:

- dynamic cost setup, payment, display, and cleanup
- eligibility checks
- event target setup, use, and cleanup
- selected-target decision patterns
- event-created country checks
- special chaos country checks
- nonhuman country checks
- formable eligibility and formation effects
- chaos tier and chaos value scaling
- AI willingness calculations
- cooldown and duration scaling
- timer scaling
- unit spawn packages
- starting force setup
- event-log context setup
- evolution-log context setup
- triggerable scenario setup
- world-threat refresh logic
- scripted GUI button requirement and effect logic
- stale variable, flag, mission, and event target cleanup
- repeated scripted localisation selectors
- repeated localisation tooltips for dynamic values
- overcomplicated condition trees that can be replaced by existing scripted triggers
- long repeated effect chains that can use an existing or new helper
- inconsistent event, decision, focus, GUI, or localisation workflow patterns
- scattered setup, effect, cleanup, logging, and documentation logic for the same subsystem
- one-off helper variants that do the same job with different names, scope assumptions, or cleanup behavior

For each candidate, decide one outcome:

- reuse an existing helper
- add a new helper and migrate safe call sites
- add or consolidate script constants
- move logic to an existing dedicated file
- create a new dedicated subsystem file when no good home exists
- fix an inconsistency only
- leave unchanged because the logic is genuinely one-off or clearer in place
- defer to a written plan because migration is broad, risky, or design-changing

## Helper extraction rules

Use existing helpers first. Add a new helper only when the pattern is repeated, likely to recur, or dynamic enough that future systems should reuse it.

Effects belong in scripted effects. Reusable triggers belong in scripted triggers. Shared thresholds, caps, ratios, AI weights, cost anchors, and tuning ladders belong in script constants when supported.

Use meta effects or meta triggers when dynamic injection is needed.

Do not over-generalize. A helper should make the code easier to read, safer to reuse, or easier to tune. Do not hide readable one-off logic behind an abstract helper.

Do not create helpers without real call sites unless explicit scaffolding is justified and documented.

Every new or changed dynamic effect or trigger must be documented in the matching markdown file with:

- helper name
- purpose
- expected scope
- inputs
- outputs or variables set
- defaults
- side effects
- cleanup responsibility
- call sites
- usage example
- known limitations

## File organization rules

Audit whether logic is in the right place.

Prefer dedicated subsystem files when they already exist. Create a new dedicated file only when it improves ownership, reuse, and future maintenance.

Good candidates for dedicated ownership include:

- event log logic
- settings logic
- triggerable scenario logic
- cluster logic
- chaos meter logic
- condemnation logic
- deaths logic
- air cleanliness logic
- world threat logic
- formable logic
- shared country classification
- decision target selectors
- scripted GUI button logic
- reusable cost logic
- reusable unit-spawn logic
- reusable event-target cleanup logic

Do not move large systems just to make the diff look tidy. Do not split out tiny files for a few lines unless the logic clearly belongs to a distinct subsystem.

When moving code:

- update every call site
- preserve loadability under HOI4 folder conventions
- keep names stable unless renaming is part of the cleanup
- update docs and comments
- check dynamic references and meta-effect calls
- check scripted localisation and GUI references
- avoid behavior changes unless fixing a clear bug

Every new script file must have a short overview at the top and follow existing naming and folder patterns.

## Workflow consistency rules

Audit the actual workflow shape of each subsystem, not only individual helpers. Similar systems should follow the same lifecycle unless a real engine, scope, or gameplay reason requires a different path.

Look for ad hoc variants of the same flow, especially setup, target selection, eligibility checks, cost checks, effect execution, event-log recording, evolution-log recording, scenario launch, GUI click handling, super-event playback, localisation selection, docs updates, and cleanup.

When a workflow is clearly scattered across unrelated files, or when several files solve the same lifecycle in different ways, normalize the pattern if the migration is safe and bounded. Prefer an existing repo convention. Add a helper, trigger, script constant, or dedicated subsystem owner only when it makes the lifecycle easier to follow and all relevant call sites can be updated in the same change.

Do not force symmetry for its own sake. Keep a one-off path when it is genuinely simpler in place, when a different scope requires it, or when unifying it would change gameplay. Report the reason when an obvious inconsistency is intentionally kept.

## Dead code rules

Search for references before deleting anything.

Check:

- direct references through `rg`
- dynamic references through meta effects, meta triggers, scripted localisation, and constructed names
- event IDs and namespaces
- GUI references
- `.gfx` sprite references
- localisation keys
- scripted GUI names
- decision category and decision IDs
- focus IDs
- idea IDs
- character IDs
- tag references
- state group references
- docs, plans, manifests, and spreadsheet references

If something appears unused but may be called dynamically, investigate before removing it.

If uncertain, leave it in place and document the uncertainty. Do not delete it.

Do not remove intentional placeholders, future hooks, templates, examples, or planned content unless the repo clearly marks them as obsolete.

For Events 21 and higher, do not perform event-specific dead-code cleanup. Treat their old event-specific implementation as out of scope unless a reference affects shared infrastructure.

If obsolete code is still useful as a pattern, move it to a clearly documented reference location or mark it as a retained template. Do not silently delete useful examples.

If dead code was meant to be used, decide whether it should be wired, documented as planned, or removed as obsolete. Report the decision.

## Documentation and localisation cleanup

Update docs when helpers are created, renamed, moved, removed, or changed.

Update docs when a subsystem becomes better organized.

Update event docs for Events 1 through 20 when event-specific cleanup changes how an event is wired.

Do not update old Events 21 and higher event docs as standalone event cleanup unless the document is part of shared-system documentation or creates confusion in shared infrastructure.

Update helper markdown files when dynamic effects or triggers change.

Update scripted localisation and localisation when keys, dynamic values, display text, GUI text, or tooltips change.

Keep docs written as if the system has always worked this way. Do not use update-history wording such as newly added, reworked, now changed, or fixed because of this cleanup.

Use `chaosx_documentation_curator` when docs, plans, handoffs, manifests, prompt files, or README files are stale, duplicated, contradictory, or too numerous.

Use `chaosx_localisation_auditor` when localisation, scripted localisation, missing keys, duplicate keys, dynamic text, encoding, or cross-surface wording needs focused cleanup.

Use `chaosx_spreadsheet_doc_worker` only when the event catalog workbook needs updates.

## Skill maintenance

Use skills actively during this cleanup.

If the cleanup reveals a reusable workflow, validation pattern, naming rule, a common mistake, use `chaosx_skill_maintainer` or update the relevant skill.

Prefer updating an existing skill when the workflow belongs there. Create a new skill only when the workflow is distinct and reusable.

Never put event-specific context, temporary implementation details, or one-off cleanup history into skills.

At the end, report which skills were used, created, or updated.

## Patch limits

Patch only bounded improvements.

Do not rewrite whole systems in one pass.

Do not change gameplay design.

Do not use fallbacks.

Do not leave partial refactors.

Do not create placeholder replacements.

Do not leave undocumented helpers.

Do not leave broken references.

If a migration touches many unrelated files, replaces a large system, changes mechanic design, or carries high risk, write a migration plan under an appropriate `docs/plans/` path and defer the implementation.

Keep cleanup changes grouped by subsystem so the diff is reviewable.

## Process

1. Build a repo map of main systems and ownership boundaries.
2. Inventory existing dynamic effects, dynamic triggers, shared constants, subsystem files, and helper docs.
3. Search for duplicated logic, overcomplicated code, and scattered subsystem workflows.
4. Search for likely dead code and unused references.
5. Verify references carefully before changing anything.
6. Patch safe cleanup in coherent subsystem groups.
7. Use existing helpers before creating new ones.
8. Document every new or changed helper.
9. Update docs and localisation when needed.
10. Re-scan changed systems for broken references.
11. Run meaningful validation checks.
12. Continue through the repo until the broad cleanup pass is complete within the defined scope.
13. Create commits according to `AGENTS.md`, grouped by coherent cleanup units.

Do not stop after one subsystem or a few easy cleanup items. Keep iterating until the broad analysis and useful cleanup are complete.

## Meaningful validation

Run validation that directly affects confidence in the cleanup.

At minimum, check:

- new helpers have call sites
- changed helpers have updated docs
- migrated call sites use the correct scope
- moved logic still has every old caller updated
- new files are loaded by HOI4 path conventions
- removed duplicate patterns are really gone or intentionally kept
- simplified overcomplicated code still preserves intended behavior
- normalized workflows still use the correct setup, effect, logging, cleanup, and documentation path
- deleted code has no remaining real references
- retained uncertain code is documented
- renamed keys, IDs, helpers, or files have no stale references
- docs do not describe old behavior after cleanup
- localisation and scripted localisation still cover visible keys
- no unsupported operators were introduced
- no broad on-action iteration was added without explicit permission
- no placeholder or fallback was introduced
- Events 21 and higher were not treated as standalone event cleanup targets

Avoid final-report noise. Mention validation only when it is task-specific, could realistically fail, found a problem, changed the implementation, or gives useful evidence.

## Final report

The final report must include:

- systems inspected
- Events 1 through 20 event-specific surfaces inspected
- Events 21 and higher shared-system references touched, if any
- files changed
- reusable helpers created or updated
- scripted triggers created or updated
- constants created or updated
- duplicated logic removed
- overcomplicated code simplified
- workflow patterns normalized
- code moved between files
- new dedicated files created
- dead code removed
- dead code kept, with reason
- dead code wired because it was clearly intended to be used
- inconsistencies fixed
- docs updated
- localisation updated
- spreadsheet updates, if any
- skills used, created, or updated
- meaningful validation performed
- skipped meaningful validation, if any, with reason
- behavior changes, if any, with justification
- rejected cleanup candidates with reasons
- deferred broad migrations with plan paths or explanations
- remaining risks or uncertain references
- simplifications, omissions, and blockers

Do not claim completion if any accepted helper extraction, documentation update, file-organization fix, safe inconsistency fix, or safe dead-code cleanup remains unfinished.

If no simplifications were made, say that directly and provide evidence from changed files, audits, docs, validation, and rejected candidates.
