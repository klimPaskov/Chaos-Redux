# Event 027: Doctrine Research research notes

## Purpose

This note records the doctrine-system facts and design inferences behind the specification, and how the implementation answered the engine questions the original package left open.
The four specification parts define behaviour; this file is supporting evidence.

## Catalog origin

The original catalog row described Doctrine research as a Minor Fire-Once event giving one major country a complete military doctrine.
The user's brief replaced it with a global, Minor Repeatable, choice-based, evolution-scaled event, and the workbook row now carries the new Event Details and evolution text with its status change queued in `docs/plans/027_doctrine_research_plans/catalog_changes_pending.md`.

## Official Hearts of Iron IV findings

- Grand Doctrines and subdoctrines: a country without a Grand Doctrine selects one first, Grand Doctrines expose category tracks, and each track holds one subdoctrine (Developer Diary: Doctrines, 30 September 2025).
- Army, Navy, and Air moved to this model in the 1.17 release family (No Compromise, No Surrender release notes, 20 November 2025).
- Grand Doctrines can have any number of tracks, and 1.17.1 added `max_track_columns` and `max_track_rows` for multi-row layouts (NCNS Patch 1.17.1, 26 November 2025), so adapters must never assume four tracks or one row.
- Mastery is track-specific practical experience from combat, training, attachés, faction sharing, focuses, and decisions, each level grants rewards, and per-level costs are arbitrary.
- Mastery can be banked while a track has no subdoctrine or its branch is complete.
- Milestone names the Grand Doctrine reward for completing a track, and replacing a completed subdoctrine can remove it.
- Selecting a Grand Doctrine or subdoctrine normally costs the relevant military experience.
- 1.17.1 fixed a crash in `has_mastery_level` when given a bad subdoctrine, which supports the fail-closed adapter design.
- The native Doctrine of Choice achievement requires mastering every subdoctrine of a Grand Doctrine (Arts and Achievements publication, November 2025).

## Design inferences

These resolve the brief against the current doctrine model; they are not official statements.

- **Domain-scoped choices.** Scoping each choice to one domain lets a country with an Army doctrine still adopt a Navy doctrine, which the brief's "choose a doctrine or subdoctrine" leaves open.
- **Empty-track assignment grants the first step.** An active Grand Doctrine can hold empty tracks, so a choice can assign a subdoctrine and advance it, while adoption stays the only action that spends a choice without mastery, as the brief requires.
- **Free actions.** Charging experience after granting a choice would make some choices unusable, so the event waives the cost of its own action and refunds nothing.
- **No compensation.** A substitute reward would favour countries already ahead in doctrine.
- **Queued curricula.** A repeatable global event can fire while earlier choices remain open in multiplayer, so each country owns an ordered queue.
- **Tier mapping.** The brief gives sizes but no tiers, so each rising Chaos tier from Gathering Storm to Totalen Chaos unlocks one stage.
- **Medium severity.** The event is global and reaches five direct steps.

## Engine questions and their answers

| Question | Answer in the implementation | Remaining live check |
| --- | --- | --- |
| Which effects adopt, assign, read, and advance? | `set_grand_doctrine`, `set_sub_doctrine` with folder and numeric track index, `has_mastery_level` and `has_completed_track` readbacks, and `add_mastery`. `add_mastery` rejects the numeric `index` filter in HOI4 1.19.2, so grants filter by folder and subdoctrine, plus track type outside Special Forces. | Same-effect readback after `add_mastery`. |
| Can one level be granted directly? | No direct level grant exists, so the step adds one point at a time and re-reads the level, with a guard at the level's reward cost (100, 60 for Special Forces, 50 for People's War levels 1, 2, and 4) scaled for negative mastery gain factors and capped at twice the cost. | Whether `add_mastery` applies gain factors. |
| How does the bank resolve on assignment? | The level is re-read after assignment and stored as the step's starting level; a bank that completes the branch leaves the assignment standing without spending a choice. | `set_sub_doctrine` on an empty track and the readback after it. |
| Which domains exist? | Army, Navy, Air, Special Forces, and Chaos Warfare; Chaos Warfare shares the `land` folder with Army. | None beyond DLC combinations. |
| Is Special Forces compatible? | Yes, with per-subdoctrine grants and readbacks because each subdoctrine can occupy either track. | Two tracks never holding the same subdoctrine. |
| Which native AI preferences can be reused? | Every vanilla `ai_will_do` factor for Grand Doctrines and subdoctrines, mirrored in `doctrine_research_ai_native_*` constants. | Real-campaign mixes. |
| How do pages show doctrine icons? | Native doctrine sprites as text icons in option names. | None. |
| How is curriculum state stored? | Country-owned aligned arrays for curricula and receipts, global firing envelopes, and flags for the active curriculum and open pages. | Save and reload recovery. |
| How do controller changes route pages? | Lifecycle and tag-switch callbacks reconcile only countries with pending work. | Tag-switch callbacks. |
| Which cluster ID is free? | `9`, now National Breakthroughs in the runtime registry and the workbook. | None. |
| Which achievement IDs are free? | `027_doctrine_research_first_lesson`, `_single_school`, `_joint_curriculum`. | None. |
| Which report sprite convention applies? | `GFX_report_event_027_doctrine_research` in an event-scoped GFX file. | None. |

## Sources

- Hearts of Iron IV, Developer Diary | Doctrines, 30 September 2025.
- Hearts of Iron IV, No Compromise, No Surrender release notes, 20 November 2025.
- Hearts of Iron IV, NCNS Patch 1.17.1, 26 November 2025.
- Hearts of Iron IV, Arts and Achievements publication with Doctrine of Choice, November 2025.
- Vanilla `common/defines/00_defines.lua`, `common/doctrines/`, and `documentation/modifiers_documentation.md`, as cited in `docs/plans/027_doctrine_research_plans/agent_decisions_2026-10-04.md`.
