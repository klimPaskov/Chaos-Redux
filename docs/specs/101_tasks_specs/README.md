# Event 101 Tasks: complete planning package

Event 101 gives an eligible human country one feasible timed commitment drawn from its actual campaign.
The country completes it through normal play, receives a strong related reward for success and faces a bounded consequence for failure.

This package contains seven source-design parts, five future task prompts and their technical and historical evidence companions.
It does not contain gameplay code or finished art.
The package is installed at `docs/specs/101_tasks_specs/`.

## Current authority and workflow

The user authorized extraction and documentation reconciliation on 10 October 2026, and later the same day a spec audit under the user's planning-package brief.
Neither request executes the embedded implementation or production prompts.
The imported authoring parent's acceptance records in [review disposition](101_tasks_review_disposition.md) describe the package's historical design reconciliation.
They do not establish fresh user approval, current implementation or acceptance of an owner substitution.
Design changes made by the audit are accepted within the user's planning-package brief and are recorded in the review disposition and the revision log below.
Preserve the design pending a separately authorized implementation task, and keep conflicting or missing acceptance unresolved.

The seven parts and [implementation contract](101_tasks_implementation_contract.md) are the source-design baseline.
The five prompts derive future work from that baseline.
[Source coverage](101_tasks_source_coverage.md), the dated repository excerpts in [validation and evidence](101_tasks_validation_and_evidence.md), and the original artifact checks in [review disposition](101_tasks_review_disposition.md) are historical receipts.
New working notes belong under `docs/plans/101_tasks_plans/`.

Current import conclusions and per-document dispositions are in [the import review](../../plans/101_tasks_plans/subagent_handoffs/101_import_review_2026-10-10.md).
Current checkout hashes, root and catalog checks and identifier evidence are in [the parent evidence record](../../plans/101_tasks_plans/101_import_evidence_2026-10-10.json).
Those records describe the imported files and supersede historical present-tense status claims for the checkout.

The parent checked the canonical workbook and current source on 10 October.
Tasks 101 remains Unavailable with blank Type, Chaos and cluster fields and no `chaosx.nr101.*` definitions.
Inflation 100 is To Be Reworked, but its root in `events/100_unknown.txt` has response reports without inflation mechanics.
Fuel crisis 114, IMRO 115 and Warlords 127 are Unavailable, and bounded owner searches found no Fuel Crisis or IMRO lifecycle API.
Warlords 127 has no root, and the armed-warlord subtype in Event 014 belongs to Cannibalism.
Famine and Migration are implemented systems, which is why the crisis family starts with live cards on those two owners.

Future prompts follow current [AGENTS.md](../../../AGENTS.md), [events](../../../.claude/skills/chaos-redux-events/SKILL.md), [decisions and missions](../../../.claude/skills/chaos-redux-decisions-missions/SKILL.md), [asset production](../../../.claude/skills/chaos-redux-event-assets/SKILL.md), [subagent routing](../../../.claude/skills/chaos-redux-subagents/SKILL.md) and [improvement cadence](../../../.claude/skills/chaos-redux-improvement-loop/SKILL.md).
These owners govern mutable production and routing rules.
Subagent prompts are self-contained, name exact allowed files and an event-plans handoff, and preserve concurrent work.
Shared event-log, settings, registries and final non-portrait wiring remain parent-owned.
The probability and completion auditors remain read-only.

Discover current MCP exposure and schemas before using the listed routes.
For an unavailable, unsupported or inconclusive read-only capability, allow the initial request and at most one useful corrected retry, then review the pertinent local references and source and run useful local checks.
Source-derived balance calculations for named scenarios are valid when an analyzer fails, with scores, probabilities and engine timing distinguished.
An unavailable optional render or tool limits verification, while a missing exact measurement adapter is missing functionality.
Agents neither request nor await user-owned live-game validation.

## Reading order

| File | Content |
| --- | --- |
| [Part 1: Core](101_tasks_spec_part_1_core.md) | Identity, human-only loop, commitment, outcomes and campaign continuity |
| [Part 2: Selection and scaling](101_tasks_spec_part_2_selection_and_scaling.md) | Four-stage selection, history rules, contextual weighting, capacity and deadline formulas |
| [Part 3: War and preparation](101_tasks_spec_part_3_war_and_preparation.md) | Four offensive, three defensive and four preparation archetypes |
| [Part 4: Industry and diplomacy](101_tasks_spec_part_4_industry_and_diplomacy.md) | Four industrial and four diplomatic archetypes with exact outcome and action rules |
| [Part 5: Crisis tasks](101_tasks_spec_part_5_crisis_tasks.md) | Two live-owner cards, six pending-owner cards and the admission rule for further owners |
| [Part 6: Rewards, failure and evolutions](101_tasks_spec_part_6_rewards_failure_and_evolutions.md) | Frozen quotes, the signature reward and setback of every card, partial work, expiry rules, rest and I/II/IV evolution behavior |
| [Part 7: Presentation and achievements](101_tasks_spec_part_7_presentation_and_achievements.md) | One native mission, text direction, full visual inventory and seven difficult achievements |
| [Implementation contract](101_tasks_implementation_contract.md) | Ownership, file map, helpers, identity, receipts, timer, measurements, cleanup and migration |
| [Usage maps](101_tasks_usage_maps.md) | Future specialist and MCP routing and the W01 to W19 weighted scenarios |
| [Validation and evidence](101_tasks_validation_and_evidence.md) | Source authority, repository evidence, validation limits and V01 to V25 acceptance gates |
| [Review disposition](101_tasks_review_disposition.md) | All improvement and probability findings, architecture decisions, package checks and the 10 October audit |
| [Source coverage](101_tasks_source_coverage.md) | Historical 91-group, 133-path source reading and complete-byte comparison record |

## Implementation prompts

| File | Recipient and purpose |
| --- | --- |
| [Coding prompt](101_tasks_coding_prompt.md) | Parent implementation agent, complete Event 101 delivery |
| [Decision and mission prompt](101_tasks_decision_mission_prompt.md) | Native mission implementation and bounded mission audit |
| [Asset prompt](101_tasks_asset_prompt.md) | Icon and generated-art workers, exact paths, source modes, dimensions and production evidence |
| [Achievement prompt](101_tasks_achievement_prompt.md) | Coding parent and icon worker, all seven exact goals and twenty-one state variants |
| [Goal prompt](101_tasks_goal_prompt.md) | Compact implementation goal referring to the complete package, 3,947 characters |

## Principal decisions

Event 101 remains Minor Repeatable, Chaos level 1, with no cluster.
The shared random-event system owns scheduling and recovery.
One firing selects one eligible human country uniformly, then selects family, archetype and target with the specified contextual weights.
Each country can have one active task, including one shared task for a co-op country.

The public experience is one ordinary category, one automatically completed mission, one progress or status measure and the native countdown.
There are no Event 101 gameplay buttons, entry fees, extensions or rerolls.

The inventory has nineteen ordinary archetypes across five families and a sixth, crisis family.
The crisis family has two cards on live owners (L1 famine relief and L2 migration settlement), six cards that wait for their owners (C1 to C6) and an admission rule for further real owners.
Every card has its own signature reward and setback, tied to the system the task was about and checked for a live consumer at assignment.
Targets, work, time and outcomes are fixed when assigned, and the generator proves practical authority, capacity, access and measurement before a candidate receives weight.

The supplied evolutions remain I Higher Stakes at 200+, II Trials Under Pressure at 400+ and IV Chaos Tasks at 600+.
No III is invented.
Evolutions affect future assignments, while an active task keeps its original terms.

Ordinary industrial tasks reward new usable capacity and explicitly allow lawful post-assignment grants.
The separate construction achievement requires recipient-funded commissioning evidence.
Strict defense requires actual loss history.
A convenient daily snapshot, stockpile change or global owner flag cannot substitute for the promised work.

Success has a strong related temporary benefit.
Failure has a bounded temporary consequence and, where appropriate, a clamped confidence loss.
Partial useful work reduces the penalty.
Receipt and expiry rules prevent replay, duration accumulation and uncontrolled simultaneous capabilities.
All direct Event 101 Chaos changes are zero.

## Production inventory

The visual plan contains 23 original subjects or compositions and 37 runtime DDS outputs: six mission icons, one category icon, one static category picture, two outcome idea icons, six report cards and seven achievement triplets.
The category reference canvas must be checked against the actual production consumer.
All images remain production requirements, and none has been generated or wired.

## Open questions

These are proposals and unresolved items from the 10 October 2026 audit.
None touches a recorded user decision.

- **O2 as a separate card.** O2 needs province-level control proof, which the engine may not supply. If no adapter exists at implementation, O2 stays disabled and O1 may offer a victory-point anchor as a variant. Unresolved until an adapter is inspected.
- **Selection arithmetic.** The weighted-mean evolution factor in Part 2 is the probability review's fix for boosts spilling onto unqualified siblings. If it proves too costly to script, a simpler family-level factor needs a new probability review. Unresolved.
- **Condemnation and fallout cards.** A condemnation-compliance card and a fallout-recovery card are queued candidates in Part 5, accepted and queued pending a read of each owner contract.
- **Achievement frequency.** The thresholds follow a planning budget of at most six natural successes per country, with no measured campaign frequency. The W15 scenario must confirm them against the real shared pool before release.

## Revision log

### 2026-10-10 spec audit

- Pass 1: skill links point at the tracked `.claude/skills/`, Codex-specific spawn wording is removed, the usage map no longer narrates the original planning roles, the README no longer repeats archive-verification receipts and duplicated reward and outcome-stacking text in the implementation contract is replaced by pointers.
- Pass 2: the family-level reward matrix is replaced by a signature reward and setback for every card, with a live-consumer gate on each quote and a rule that the reward acts on the system the task was about.
- Pass 2: the crisis family gains L1 famine relief and L2 migration settlement on the implemented Famine and Migration systems, so Chaos Tasks and the crisis achievements have content before any pending owner exists.
- Pass 2: the six-family achievement needs two Demanding or Exceptional successes instead of three, and the kept-commitments streak is three tasks with two at that grade instead of five Demanding or Exceptional tasks, to fit the slow repeatable pace.
- Pass 2: scenarios W18 and W19 cover live-owner timing and the reward consumer gate.
- Basis for all design changes: 10 Oct 2026 spec audit under the user's planning-package brief.
- 2026-10-10 spec audit: pass 2 incomplete. The revision log above lists the changes that landed; the remaining checks were not finished.
