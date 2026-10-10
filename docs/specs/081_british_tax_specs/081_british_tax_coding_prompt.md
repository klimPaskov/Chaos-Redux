# Event 81 coding-agent implementation prompt

Implement the complete British Tax specification in `docs/specs/081_british_tax_specs/`. Read the README, all ten numbered parts, the research notes, and every separate prompt in that folder before editing. Follow `CLAUDE.md`, `CHAOS_REDUX_MECHANICS.md`, and the events, decisions-missions, event-assets, super-events, subagents, MTTH, and improvement-loop skills. Read the installed-game documentation and the current checkout.

Keep iterating until the full specification is implemented to its fullest extent. Do not claim completion until the implemented files satisfy it. Report anything that cannot be implemented cleanly instead of silently replacing the design with a simpler approximation.

## Non-negotiable behaviour

Event 81 is British Tax, Minor Fire-Once, Chaos level 1, Negative Economy High. ENG is the beneficiary and must exist. Never tax ENG. Every other valid civilian-economy country is assessed, including allies, dependencies, enemies, and all human participants under their distinct permissions.

British subjects and dependent chains ending in ENG are automatically taxed and cannot refuse, reduce, cancel, negotiate away the tax, or access resistance until genuinely independent. Independent British-led allies can reduce only to Nominal and cannot refuse or cancel while ENG leads. Other independents can accept or refuse. Use the explicit non-British dependent resolution in Part 1.

A valid refusal or cancellation immediately removes all Event 81 tax, British trade privileges, and corresponding British benefits, adds the British embargo and severe bilateral opinion consequences, and applies the special entitlement automatically for a minor OR a human-controlled country. An independent AI major receives no automatic Event 81 goal. Britain chooses whether to fight. Do not revert to the old optional-response goal logic or declare war automatically.

Implement the industrial, consumer-goods, and two-direction bilateral trade system with its safeguards and actual-receipt accounting, both ordered Evolutions, the fuel and idle-convoy levies, the twelve domain projects with automatic stage advance, the final settlement, British actions, famine remission, partner assistance, settlements, eight achievements, sixty-one planned image consumers, the mature-order super-event, and every mapped Chaos consequence and reversal. The assessment is the schedule row plus the British-led-ally adjustment; do not add scale, strength, or Chaos-step multipliers.

## First inspect the real baseline

Inspect `events/081_england_tax.txt`, `common/ideas/081_england_tax_ideas.txt`, their localisation and news, root dispatch, selection eligibility, Evolution settings, cluster registries, event history, and the shared economic helper and cost surface. The legacy implementation excludes allies and enemies, applies a one-year idea, awards flat reply effects, and makes the goal optional; replace those behaviours deliberately. Keep `chaosx.nr81.1` as the root entry. Use the established validity classifier, including `uses_normal_civilian_systems` where it is the current shared contract, and the existing country identity and subject-chain helpers.

## Engine feasibility gates

Verify targeted civilian and military capacity transfers for independent countries and dependent residual economies. `cic_to_target_factor` and `mic_to_target_factor` appear in the legacy idea, but that does not prove their current scope or interaction with autonomy transfers. Prove the debit and credit, economic denominator, reversibility, rounding, and treatment of damaged or occupied capacity.

Verify current consumer-goods units and floors before using `consumer_goods_factor`. Britain's relief must be bounded by actual foreign extra occupation and its own native requirement; never create negative consumer goods or use a construction bonus as a substitute.

Verify both directions of targeted trade. The documented trade-cost modifier describes what the target pays for the modifier owner's resources, so Britain buying cheaply needs a discount on each taxpayer as exporter, and taxpayers buying dearly need a separate premium on ENG as exporter against that taxpayer. Prove dynamic pairwise targeting and removal; a global British price or trade-influence modifier is not a substitute. Prevent non-positive final prices.

Verify safe fuel and idle-convoy transfers with recipient storage bounds. Verify embargo creation, goal issuance and expiry, and selective removal that leaves unrelated identical restrictions intact. Name any blocked channel instead of inventing script commands or off-map substitutes.

## Accounting and scheduling

Keep one event-owned participant registry and one ledger owner. Bind ENG explicitly and each taxpayer by durable country identity. The initial assessment performs the global enrolment once; afterwards use scoped participant reviews and lifecycle hooks, never a new periodic every-country scan. A 30-day review updates ordinary assessment and a 90-day schedule handles fuel and convoys. Exit, ENG disappearance, ownership changes, and direct war remove invalid benefits immediately. Maintain aggregate receipts with idempotent, save-safe deltas so simultaneous multiplayer replies cannot overwrite another target's contribution. Use a non-Event-81 base where the spec requires one, and let normal puppet claims precede Event 81's residual claim.

## Decisions, Evolutions, and history

Follow the decision and mission prompt for action and mission budgets, permissions at every stage, frozen quotes, inclusive affordability, and release of continuing commitments on every termination path. Active Evolutions are delayed, settings-aware, and condition-sensitive under the MTTH skill; they never reset a country's stage or refire the root. Keep event history and detail records aligned through the shared wrappers, and implement Part 10's guards and reversals without double-counting shared war, peace, tension, casualty, or annexation Chaos.

## Assets, localisation, achievements, and super-event

Follow the asset, achievement, and super-event prompts. Write final localisation from the spec's directions, not from working labels. Unresolved rights or unresearched allusions are blockers. Keep Event 81 at two visible ideas per country within the project maximum of three.

## Subagents and completion

Use project subagents with self-contained prompts for exploration, scripted-system architecture, decisions, assets, localisation, probability review, completion review, documentation, and the workbook. Run `chaosx_ai_probability_auditor` over the Part 8 scenario matrix. Near completion, run `chaosx_improvement_loop_planner`, integrate accepted changes into the spec and implementation, and dispose of the rest explicitly.

Update Event 81 and its Negative Economy High membership in the authoritative workbook, then run `.tools/export_event_catalog_csv.py`. Keep status To Be Reworked until the project completion standard is met. Cover economy conservation, both trade directions, subject and ally locks, all human participants, stale completion, save reload, successor identity, collection suspension, hostile and peaceful cleanup, and achievement histories. Deliver a completion report with changed files, tools and subagents used, verified scenarios, unresolved engine dependencies, asset acceptance, audio rights, catalog handling, and remaining blockers.
