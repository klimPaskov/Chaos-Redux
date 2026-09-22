# Event 81 coding-agent implementation prompt

Implement the complete British Tax specification in `docs/specs/081_british_tax_specs/`. Read README, all ten numbered specification parts, the research notes, and every separate prompt in that folder before editing. Follow AGENTS.md, CHAOS_REDUX_MECHANICS.md, the full event, decision-mission, asset, super-event, subagent, and improvement-loop skills, and every applicable must-read reference. Read the actual installed-game documentation and current checkout rather than treating this planning snapshot as a complete checkout.

The source specification is an authored design handoff. It is not implemented code, a passed independent audit, or permission to restart the user's game. Keep iterating until the full specification is implemented to its fullest extent. Do not claim completion until the implemented files actually satisfy it. Report anything that cannot be implemented cleanly without silently replacing the design with a simpler approximation.

## Non-negotiable behaviour

Event 81 is British Tax, Minor Fire-Once, Chaos level 1, Negative Economy High. ENG is the beneficiary and must exist. Never tax ENG. Every other valid civilian-economy country is assessed, including allies, dependencies, enemies, and all human participants under their distinct permissions.

British subjects and dependent chains ending in ENG are automatically taxed and cannot refuse, reduce, cancel, negotiate away the tax, or access resistance until genuinely independent. Independent British-led allies can reduce only to Nominal and cannot refuse or cancel while ENG leads. Other independents can accept or refuse. Use the explicit non-British dependent resolution in Part 1.

A valid refusal or cancellation immediately removes all Event 81 tax, British trade privileges, and corresponding British benefits, adds the British embargo and severe bilateral opinion consequences, and applies the special entitlement automatically for a minor OR a human-controlled country. An independent AI major receives no automatic Event 81 goal. Britain chooses whether to fight. Do not revert to the old optional-response goal logic or declare war automatically.

Implement the full industrial, consumer-goods, and two-direction bilateral trade system, the safeguards and actual-receipt accounting, both ordered Evolutions, all expanded claims, the twelve domain projects, four consolidations, British actions, partner assistance, settlements, eight achievements, sixty-one planned image consumers, mature-order super-event, and every mapped Chaos consequence and reversal.

## First inspect the real baseline

The inspected snapshot is commit `879b3007d3b6bf75c726c11635473fccda45c569` in `klimPaskov/Chaos-Redux`. Inspect current versions of `events/081_england_tax.txt`, `common/ideas/081_england_tax_ideas.txt`, associated localisation and news, root dispatch, selection eligibility, Evolution settings, cluster registries, event history, and the shared economic helper and cost surface.

The legacy implementation excludes allies and enemies, applies a one-year idea, awards flat reply effects, and makes the goal optional. Replace those behaviours deliberately. Preserve identifiers or provide a clear migration where an existing consumer requires it. Keep `chaosx.nr81.1` as the established root entry unless an actual repository-wide contract requires another coordinated migration.

Use the established validity classifier, including `uses_normal_civilian_systems` where it is the actual current shared contract. Do not classify every special tag as a non-human economy. Inspect all current country identity and subject-chain helpers before creating a duplicate helper.

## Mandatory engine feasibility gates

Verify targeted civilian and military capacity transfers for independent countries and dependent residual economies. The existing names are `cic_to_target_factor` and `mic_to_target_factor`, but presence in the legacy idea does not prove their current scope or their interaction with ordinary autonomy transfers. Prove the debit and credit, economic denominator, reversibility, rounding, and treatment of damaged or occupied capacity.

Verify current consumer-goods units and floors. The source uses desired effective percentage points and actual factory equivalents. Do not paste these numbers directly into `consumer_goods_factor` without proving its current semantics. Britain's relief must be bounded by actual foreign extra occupation and its own native requirement. Never create negative consumer goods or use an unrelated generic construction bonus as a substitute.

Verify both directions of targeted trade. The inspected offline description says the target purchases the modifier owner's resources. Britain buying cheaply therefore requires the appropriate discount on each taxpayer as exporter. Taxpayers buying dearly require a separate premium on ENG as exporter against that specific taxpayer. Prove dynamic pairwise targeting and removal for arbitrary supported country identities. A global British price modifier or trade-influence modifier is not an acceptable substitute. Check other cost systems and prevent non-positive final prices.

Verify an actual reversible dockyard-output debit and recipient credit, safe fuel and idle-convoy transfers, recipient storage bounds, and resource concessions that respect ownership and ceilings. Do not invent unsupported script commands or create off-map factories, finished ships, or equipment as a quiet replacement. If exact support is absent, name the blocked channel and seek a deliberate revised design before claiming implementation complete.

Verify embargo creation, bilateral trade interruption, goal issuance, goal expiry, selective removal, and coexistence with unrelated identical restrictions. Inspect DLC and installed-version dependencies. Only owned Event 81 restrictions may be removed during settlement. Do not remove an unrelated goal or embargo to make a test appear clean.

## Accounting and scheduling architecture

Keep one event-owned participant registry and one clear ledger owner. Bind ENG explicitly, and bind each taxpayer by durable country identity. Initial assessment can perform the user-requested global enrolment once. Thereafter use scoped participant reviews, dirty updates, and actual lifecycle hooks. Do not add a new daily, weekly, or monthly every-country scan to rediscover the same participants.

A 30-day participant review updates ordinary assessment. A 90-day schedule handles fuel and convoy claims. Exit, ENG disappearance, ownership changes, and direct war must remove invalid benefits immediately. Maintain aggregate receipts by replacement or subtract-and-add deltas with idempotence and save-safe state. Simultaneous multiplayer replies cannot overwrite another target's contribution.

Use a coherent snapshot with Event 81 contributions excluded where the source requires a non-Event-81 base. Do not compound British strength from its own receipts within one update or double-count consumer-goods contributions as additional industry. Normal puppet claims precede Event 81's residual claim. No native transfer plus duplicate off-map grant is allowed.

Use verified installed variable and constant syntax. Do not assume cross-file `@` constants work because a different file uses them. Shared factory-grant calculators calculate an amount and are not proof of a genuine tax transfer. Stockpile debit helpers can mutate negative inputs, so reinitialise each call from a clean quantity and inspect the actual helper contract.

## Decisions and Evolution integration

Invoke the separate decision-mission prompt. Keep the primary-action and active-mission budgets. Enforce every permission at visibility, click, reply, and completion. Quote and freeze costs once, use inclusive affordability, and release continuing commitments on every termination path. Preserve completed work and use the low-industry or domestic-substitution routes when appropriate.

Active Evolutions are delayed, settings-aware, and condition-sensitive. They do not reset a country’s stage or refire the root. Distinguish high-Chaos initial entry from active escalation. Respect actual enabled flags, predecessor conditions, and stale-queue invalidation. Use the actual current MTTH skill and tool references, which were not included in the planning archive.

Keep event history and detail records aligned through the shared wrappers. Include the actual event ID, actor ENG, target, current Evolution, and outcome where required. A record or an announcement does not by itself award Chaos. Implement Part 10's guards and reversals and demonstrate that generic war, peace, tension, casualties, and annexation effects are not counted twice.

## Assets, localisation, achievements, and super-event

Follow the separate asset, achievement, and super-event prompts in full. Write final player-facing localisation from the spec's directions, not from working labels. Research and source final super-event title, button, quotation, cultural remark, and recording. Unresolved rights or an unresearched allusion are blockers. Do not use temporary music or placeholder art.

Use the ordinary decision categories and the current shared presentation framework. Verify actual consumers before assigning assets or a super-event slot. Maintain the two-idea Event 81 design and the project maximum of three visible national spirits. Produce and review every required achievement state directly under the correct runtime achievement folder.

## Bounded subagent workflow

Use actual `collaboration.spawn_agent` with `fork_turns="none"` and self-contained bounded prompts when the environment provides it. Route relevant repository exploration, scripted-system architecture, decisions, assets, generated report art, icons, localisation, probability review, completion review, documentation, and spreadsheet alignment through the supplied roles. Do not launch irrelevant production work simply because a role definition exists.

Spawn `chaosx_ai_probability_auditor` and use the current probability inspection, evaluation, sweep, and comparison tools over the source's scenario matrix. Render where the tool workflow calls for it. Simulate only genuinely uncertain-input cases and use sequence tools only with a complete selection pool. A Python preference score or a source-only review is not equivalent evidence.

Before claiming the work is near complete, spawn `chaosx_improvement_loop_planner` and resolve its actual addendum or closure handoff. Integrate accepted changes into the canonical spec and implementation, and explicitly dispose of rejected or blocked proposals. Do not fabricate this required independent handoff from a main-agent self-review.

## Catalog, documentation, and validation

The source CSVs are export-only snapshots. Inspect the authoritative workbook, update Event 81 and the Negative Economy High membership without disturbing other rows, and run `.tools/export_event_catalog_csv.py`. Keep status To Be Reworked until the actual project completion standard is met. The planning package itself does not justify a completed catalog status.

Use available installed-document checks and the relevant HOI4 inspectors with their actual schemas. Cover economy conservation, both trade directions, subject and ally locks, all human participants, stale completion, save reload, successor identity, collection suspension, hostile and peaceful cleanup, and achievement histories. Do not autonomously launch or restart the game. Follow the debug skill only under explicit authorisation and the user's live-testing workflow.

Deliver a concrete completion report listing changed files, actual tools and subagents used, verified scenarios, unresolved engine dependencies, asset acceptance, audio rights, catalog handling, and remaining blockers. Missing capabilities must be named rather than hidden behind a claim that the full package is implemented.
