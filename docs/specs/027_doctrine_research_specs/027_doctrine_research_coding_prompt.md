# Coding prompt: Implement Event 027 Doctrine Research

Implement the complete Event 027 rework from the source specification package at:

`docs/specs/027_doctrine_research_specs/`

Treat every mapped rule, evolution, adapter, AI behavior, achievement, asset, log surface, documentation field, and catalog field as acceptance criteria. Do not replace the design with a smaller Army-only event, a flat military-experience grant, a fixed mastery-point dump, a fire-once event, or a one-country event.

## Required reading

Read in full before editing:

- `AGENTS.md`
- every file in `docs/specs/027_doctrine_research_specs/`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md` for the event-page clarity and scripted-system rules that apply to interactive actions
- the current Chaos Warfare documentation and source
- the current event, evolution, event-log, cluster, achievement, doctrine, technology, AI, GFX, localization, and workbook sources touched by the feature

Consult the required offline Paradox wiki pages and installed vanilla documentation listed by `AGENTS.md`. Inspect current vanilla doctrine definitions and at least one verified direct mastery-grant precedent. Use the current repository and vanilla files as authority for syntax and engine behavior.

## Mandatory MCP evidence

Use the installed HOI4 MCP routes for every supported surface.

For the event chain:

- use narrow `hoi4.event_inspect`
- render the entry, human branch, AI branch, queue continuation, evolution, and cluster paths with `hoi4.event_render`
- compare the final event structure with the pre-change source through the available event comparison route

For doctrine and technology behavior:

- use `hoi4.tech_inspect` on Army, Navy, Air, conditional Special Forces content, Chaos Warfare, and every registered custom domain
- inspect Grand Doctrines, tracks, subdoctrines, prerequisites, exclusivity, mastery levels, grants, native Milestones, references, and assets
- use `hoi4.tech_render` for each affected folder or branch and the asset view
- use `hoi4.tech_compare` after implementation

For weighted AI and cluster participation:

- route the baseline and final audit through `chaosx_ai_probability_auditor`
- start with `hoi4.probability_inspect`
- use the named scenarios in `027_doctrine_research_probability_scenarios.md`
- use evaluation, sweeps, seeded simulation, sequence analysis, comparison, and rendering only under their declared evidence conditions
- distinguish score-only, exact, bounded, sampled, and unresolved evidence

If a required MCP route is unavailable, record the exact blocker. Do not treat source-only review as equivalent evidence.

## Subagent routing

Spawn project subagents with `fork_context=false` and context-complete prompts.

Use:

- `chaosx_repo_explorer` when the current Event 027, doctrine, cluster, achievement, or asset paths remain uncertain after direct inspection
- `chaosx_scripted_system_architect` for the doctrine-domain adapter, exact one-step mastery transaction, batch ledger, queue, receipt, and reusable helpers
- `chaosx_ai_probability_auditor` before and after weighted source changes
- `chaosx_generated_event_art` for the report image
- `chaosx_icon_artist` for the three achievement icon triplets
- `chaosx_localisation_auditor` after broad visible text is written
- `chaosx_event_completion_auditor` before the completion claim
- `chaosx_spreadsheet_doc_worker` after implementation facts and final in-game wording exist
- `chaosx_documentation_curator` when the implementation produces several handoffs or stale design records that need reconciliation

Every patch-capable subagent writes its handoff under:

`docs/plans/027_doctrine_research_plans/subagent_handoffs/`

The parent owns integration, final review, validation, documentation, workbook alignment, commit, and the completion claim.

## Event identity

Keep the canonical entry identity `chaosx.nr27.1` unless the live source proves an established compatible namespace that must remain stable.

Register Event 027 as Minor Repeatable. Replace the stale fire-once classification everywhere, including default enable state, event type lookup, Event Details, debug name, history name, documentation, and catalog.

Recommend Calm World as normal eligibility. Use the accepted evolution eligibility and pacing from the specification.

## Global firing

One Event 027 firing snapshots every live country with at least one valid doctrine action.

Create one country-owned batch for each participant. Use one bounded fanout from the event firing. Do not add a recurring whole-world on-action.

Countries created after the snapshot receive no retroactive batch. Countries removed before resolution lose their active and queued batches. Unused choices never transfer.

Human countries receive the chained event flow. AI countries resolve silently through the same valid pool.

Record one global Event 027 History row with no actor. Do not record each country page as another random event.

## Doctrine-domain adapter

Implement a safe adapter registry that covers:

- Army
- Navy
- Air
- current Special Forces doctrine content only when the local graph proves a compatible mastery model
- Chaos Warfare
- future custom doctrine domains through a documented extension contract

Use the complete contract in `027_doctrine_research_doctrine_registry_matrix.md`.

A broken custom adapter must fail closed without removing valid ordinary domains. Never pass an unknown subdoctrine identity into a mastery trigger or effect.

Do not use `union_compatible_researched_technologies_from_donor`, Kruger technology helpers, military experience, research bonuses, or generic technology grants as substitutes.

## One-choice transaction

Each choice selects one domain.

When the domain has no active Grand Doctrine:

- show every eligible Grand Doctrine
- adopt one through the verified native or owner-system route
- waive the selected action's normal experience cost
- consume one choice
- grant zero Event 027 mastery steps
- never replace an active Grand Doctrine

When the domain has an active Grand Doctrine:

- show every track able to receive one event mastery step
- if a track has an active subdoctrine below maximum, advance it exactly one level
- if a track is empty, show every eligible subdoctrine, select one, preserve native banked mastery, and grant the first event mastery step in the same choice when the verified engine transaction supports it
- consume a choice only after one successful event-attributed action

Revalidate at confirmation time. Navigation, pagination, invalidation, and failed transactions consume no choice.

Do not implement a flat mastery amount that can cross multiple unknown thresholds. Prove the exact next-level operation or calculate the exact amount required for one level without event-attributed spillover.

Document the local banked-mastery order. If empty-track selection plus one event step cannot be performed safely, stop with the exact engine blocker. Do not silently split it into two choices or grant experience.

## Batch ledger and queue

Each batch stores:

- stable batch identity
- owner country
- firing date
- evolution stage at firing
- total choices
- remaining choices
- achievement action ledger

Doctrine options rebuild before every choice. Batch size never changes after creation.

A country can hold one active batch and an ordered queue. Later firings append distinct batches. Never merge or overwrite them.

Use a one-time transaction receipt so save, reload, duplicate event pages, or delayed continuations cannot apply one action twice.

Preserve active and queued batches through save, reload, cosmetic tag changes, ideology changes, subject changes, and control changes. Clean them on final closure or country removal.

Route unresolved choices to the current controller. AI resolves through a bounded continuation path. Human control opens the next valid page for that country.

## Human event flow

Implement the complete flow from `027_doctrine_research_spec_part_2_choice_flow.md`:

- opening report
- domain selection
- Grand Doctrine selection for empty domains
- track selection for active doctrines
- active-subdoctrine confirmation
- empty-track subdoctrine selection
- successful result
- next-choice continuation
- final batch summary
- no-option closure
- pagination and back navigation

Every page shows remaining choices and the current doctrine context. Every consuming option states its result. Grand Doctrine adoption text states that it grants no mastery step.

Use dynamic localization for doctrine names, track names, subdoctrine names, current level, next level, maximum level, completion, and native Milestone state. Do not expose raw IDs or variables.

Keep final prose in-world and follow the project writing rules. Use military schools, field exercises, manuals, command institutions, and after-action study as the event frame.

## Evolutions

Implement one global evolution track:

- Baseline: one choice
- Evolution I: two choices
- Evolution II: three choices
- Evolution III: four choices
- Evolution IV: five choices

Use normal evolution pacing with centralized dynamic tuning. Follow the recommended chaos-tier eligibility unless current accepted project tuning requires a documented adjustment.

Support pre-fire evolved opening and post-fire evolution. An evolution changes future batches and does not grant an immediate free batch.

Snapshot batch stage and size. A later evolution cannot enlarge an active or queued earlier batch.

Every evolution checks its own enable state. Disabled lower stages cannot block higher enabled stages and cannot set progression flags used by later content.

Record one global evolution row with no actor. Keep ordinary choices out of the evolution log.

## AI

Use the human-valid option pool.

Score domains, Grand Doctrines, tracks, and subdoctrines from current force composition, production, war state, geography, theater, enemy pressure, focus and strategy route, continuity, branch completion value, and owner-system factors.

Implement the full intent in the specification and scenario file:

- Army relevance from land forces, fronts, land production, and land plans
- Navy relevance from coastline, fleets, dockyards, convoys, naval war, and maritime plans
- Air relevance from aircraft production, wings, air bases, air war, and air plans
- conditional Special Forces relevance from verified doctrine content and special-force plans
- Chaos Warfare relevance from actual CBRN readiness, formations, equipment, policy, threats, and operations

Reuse native or country-specific doctrine preferences where possible. Do not build a disconnected strategy table that ignores existing AI plans.

Recalculate after every choice. Allow stacking under a clear score lead and diversification under close scores. Finish near-complete relevant branches. Do not let completion value overpower severe strategic mismatch.

Use bounded randomness among top valid candidates. Invalid candidates receive zero participation.

Complete the baseline and final probability audits with the named scenarios.

## Chaos Warfare

Use the current owner-system source and documentation.

Support the four public tracks and established compatibility identities. Grand Doctrine establishment remains gated by the owning requirements. A mastery step enters through the owning transition and updates every state the owner system expects.

Do not directly grant downstream units, equipment, technologies, policies, operations, ideas, readiness, or Condemnation effects.

A mastery level may exist while a separate downstream requirement remains unmet. Preserve that gate.

## National Breakthroughs cluster

Audit and reserve a free cluster ID. Numeric `9` is provisional only.

Register National Breakthroughs when the runtime cluster has valid implemented members. Map Event 027 as a Medium member with Calm World minimum tier.

When Event 027 is the selected event, its fanout occurs once. When it joins another selected member as optional, its fanout occurs once. Cluster inclusion grants no extra choices.

Use the complete implemented member pool for participation tuning. Keep cluster status honest while other proposed members remain unreworked.

Cluster firing counts as one global pacing event. Country pages do not add timer pressure or major-event gain.

## Achievements

Implement the full achievement prompt:

- `027_first_lesson`
- `027_single_school`
- `027_joint_curriculum`

Use stable batch, domain, track, and subdoctrine identities plus event-attributed receipts. Do not infer progress from final doctrine state.

Add final localization, root registry entries, tracking, disqualifiers, documentation, and complete icon triplets.

## Assets

Use the accepted asset prompt.

Produce and wire:

- one final period-authentic report-event image
- three achievement icon triplets

Reuse verified doctrine-owned icons for domain and branch pages. Missing assets are blockers, not permission to substitute unrelated icons.

The parent owns final non-portrait GFX and event wiring. Preserve temporary asset evidence while work is active, then follow the project promotion and cleanup rules before a full completion claim.

## Event Logs, details, and localization

Wire:

- event name and debug name
- one global history row
- no-actor mapping
- Event Details premise
- all four evolution previews
- main evolution history
- related evolution history
- enabled and disabled state
- cluster member display
- current stage and batch size text

Keep the history and catalog surfaces distinct. Do not add fake dates or indexes to Event Details previews.

Broad visible text requires `chaosx_localisation_auditor` before completion.

## Documentation and workbook

Create or update the permanent Event 027 documentation with final implemented behavior, doctrine coverage, AI, evolutions, cluster membership, assets, achievements, validation evidence, and known limits.

Keep accepted design under `docs/specs/027_doctrine_research_specs/`. Place implementation handoffs under `docs/plans/027_doctrine_research_plans/`.

After final in-game wording exists, use `chaosx_spreadsheet_doc_worker` to update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. Replace the stale Event 027 row and add or update National Breakthroughs. Run `python .tools/export_event_catalog_csv.py`. Never edit the CSV exports directly.

## Completion

Run the complete criteria in `027_doctrine_research_acceptance_criteria.md`.

Use `chaosx_event_completion_auditor` for the final spec-versus-implementation pass. Carry every blocker, missing asset, unresolved adapter, unsupported DLC graph, missing probability result, or simplification into the completion report.

Do not claim completion while any accepted Event 027 route is missing, any doctrine domain is silently omitted, one-step mastery is unverified, banked mastery is unresolved, AI evidence is missing, the queue is unsafe, achievements or assets are incomplete, Event Details is stale, or the authoritative workbook is unaligned.

Create a focused Git commit only after the complete change is ready and the final diff contains no unrelated work.
