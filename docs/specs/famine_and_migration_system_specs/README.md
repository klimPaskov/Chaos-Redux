# Famine and Migration Mechanics Planning Package

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context.
> The current implementation uses independent `famine_*` and `migration_*` mechanics, `famine_decision_category` and `migration_decision_category`, and `famine_state_map_mode` and `migration_state_map_mode`.
> Use [improvement_plan_2026-10-10.md](../../plans/famine_and_migration_system_plans/improvement_plan_2026-10-10.md) for current status and design; the [6 October takeover status](../../plans/famine_and_migration_system_plans/takeover_status_2026-10-06.md) is historical evidence.
> The inherited round-3 gameplay drafts are published, and the older checkpoint reports remain explicitly historical evidence.

This folder preserves source design for the separate famine and migration mechanics connected by neutral conservation primitives. Neither mechanic has a random-event identity.

> **Superseded incident-layer note (2026-08-25):** Any historical wording in this package about incident events, event-option probability, `famine_incident.1`, `migration_incident.1`, `fm_*`, or combined `famine_migration_*` planning IDs is superseded. The two register helpers are accounting/presentation seams only, the incident event files and constants were deliberately deleted, and current runtime names are separate `famine_*`, `migration_*`, or narrow neutral primitives.

The design joins four related gameplay layers:

1. State food security and famine severity.
2. Exact civilian population losses recorded through the shared Deaths system.
3. Internal displacement, cross-border flight, evacuation, deportation, reception, return, and integration.
4. Occupation, atrocity, outbreak, bombing, nuclear, environmental, diplomatic, and event adapters that feed the same shared model.

The central design rule is that famine and migration remain dynamic. Historical cases provide pressure profiles, triggers, policy patterns, and regional memory. They never impose a fixed death total or a fixed migration total.

## Current authority and continuation

Begin with [the 10 October improvement plan](../../plans/famine_and_migration_system_plans/improvement_plan_2026-10-10.md), the single current plan and status record for both systems; [takeover status, 6 October](../../plans/famine_and_migration_system_plans/takeover_status_2026-10-06.md) and [the continuation decision log](../../plans/famine_and_migration_system_plans/agent_decisions_2026-10-05.md) are historical. Current behaviour is documented in [the famine system](../../systems/famine_system.md) and [the migration system](../../systems/migration_system.md). The accepted national-policy laws and their famine/migration management panels are documented separately in [National policies](../../systems/national_policies.md); the accepted UI and policy integration addendum is [Part 9](national_policy_panels_part9.md), and the current implementation record is [the panel implementation report](../../plans/famine_and_migration_system_plans/national_policy_panels_implementation.md). The August 25 split and event-free clarification above is retained recorded design; [the dated source map](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) preserves its earlier acceptance and source evidence. Further matrix or source-part claims need their own attributable acceptance; neither a spec location nor a prompt establishes it. Original matrix terms such as shared system, combined adapters or Event 149 conversion alternatives are historical planning labels; they do not override independent owners, the current event-free contract or recorded retirement. Do not modify other system owners or restart completed work from the original prompts.

Use [the subagent skill](../../../.agents/skills/chaos-redux-subagents/SKILL.md) for routing, [the event skill](../../../.agents/skills/chaos-redux-events/SKILL.md) for accepted adapters, [the state-ledger reference](../../../.claude/skills/chaos-redux-map-states/references/state-ledgers.md) for transfer contracts, and [the GUI skill](../../../.agents/skills/chaos-redux-scripted-gui/SKILL.md) for mandatory current-source visual evidence. Subagent templates require a self-contained parent prompt with exact remaining scope and no inherited context.

Working plans and audit handoffs belong under:

```text
docs/plans/famine_and_migration_system_plans/
```

## Source specification files

- `famine_and_migration_system_spec_part_1_core.md`
- `famine_and_migration_system_spec_part_2_famine_food_security.md`
- `famine_and_migration_system_spec_part_3_displacement_migration_return.md`
- `famine_and_migration_system_spec_part_4_deaths_occupation_atrocity.md`
- `famine_and_migration_system_spec_part_5_historical_profiles.md`
- `famine_and_migration_system_spec_part_6_decisions_ai_presentation.md`
- `famine_and_migration_system_spec_part_7_cross_system_connections.md`
- `famine_and_migration_system_spec_part_8_balance_acceptance.md`
- `national_policy_panels_part9.md` (accepted 2026-10-15 policy and management-panel integration; this does not revise the famine or migration core design)

## Supporting design records

- `famine_and_migration_system_research_bibliography.md`
- `famine_and_migration_system_historical_profiles.csv`
- `famine_and_migration_system_integration_matrix.csv`
- `famine_and_migration_system_death_reason_ownership.csv`
- `famine_and_migration_system_probability_scenarios.csv`
- `famine_and_migration_system_decision_map.csv`
- `famine_and_migration_system_asset_matrix.csv`
- `famine_and_migration_system_input_manifest.csv`
- `famine_and_migration_system_output_manifest.csv`
- `famine_and_migration_system_implementation_surface_map.md`
- `famine_and_migration_system_subagent_routing.md`
- `famine_and_migration_system_subagent_execution_status.md`
- `famine_and_migration_system_improvement_loop_closure.md`

## Implementation prompt files

- `famine_and_migration_system_asset_prompt.md`
- `famine_and_migration_system_achievement_prompt.md`
- `famine_and_migration_system_decision_mission_prompt.md`
- `famine_and_migration_system_coding_prompt.md`
- `famine_and_migration_system_goal_prompt.md`

Context-complete prompts for the relevant project subagents are under `subagent_prompts/`.

## Non-negotiable design outcomes

- Famine is a state system with visible severity and meaningful deaths when ignored.
- Deaths use real state population loss and the shared Deaths ledger.
- The Deaths breakdown includes `From famine`.
- Migration moves population between real states. Movement is not counted as death.
- Route deaths are tracked separately and only occur when a route is dangerous or people are trapped.
- An island under wartime blockade receives strong famine pressure only when isolation, port, convoy, and corridor evidence supports that result.
- Air Cleanliness affects food production, transport, recovery, and nuclear-winter risk.
- Occupation policy, camps, gulags, deportation, forced labor, genocide, bombing, nuclear attacks, outbreaks, natural disasters, sanctions, and relevant events all use shared adapters.
- Ideology affects flight and destination choice as one bounded factor. Direct persecution, atrocity, bombing, famine, and route safety can outweigh ideology.
- Famine and migration remain separate mechanics. For player presentation, accepted [Part 9](national_policy_panels_part9.md) provides quiet-accessible management panels; crisis, local pressure, capacity, cost, and pending-work facts gate the operational actions inside them. Native AI missions retain their existing paths. Register helpers record accounting/presentation context only; no incident event layer exists. Sustained displacement remains an operational issue gate, not a condition for opening the panel.
- AI receives the same usable response paths as the player.
- The system uses event-driven and active-registry processing. It does not require a whole-world daily, weekly, or monthly scan.
- Preserve the recorded Event 149 `Immigrations` retirement so the mod has one migration model.

## Historical manifests and reading limits

The input manifest is a receipt for the original supplied planning sources, including external `/mnt/data/` paths. The output manifest is the original package-generation receipt, not a validator for the current repository files; its recorded hashes and sizes are preserved rather than rewritten as historical evidence. Use the current checkout and audit handoff for current file coverage. No package-integrity validator or gameplay completion is asserted by these receipts.

## Original planning-environment reading proof and limitations

The input manifest records every supplied project file and every extracted subagent definition with size and SHA-256. All listed files were fully read before this package was written.

The original planning environment did not expose the Windows Chaos Redux repository, the offline Paradox wiki snapshot, installed vanilla game files, the HOI4 MCP server, or a callable custom-subagent runtime. The package therefore contains repository-ready design, research, matrices, and context-complete subagent prompts. The coding prompt requires the implementation agent to perform the mandatory local source, wiki, vanilla, MCP, and probability passes before editing or claiming completion.

## Revision log

### 2026-10-10 spec audit

- Aligned the source parts with the 10 October rework (commit 839850b0d) without changing its design: the Part 6 decision families now match the implemented inventory (Import Food absorbs foreign relief requests, Evacuate Civilians absorbs preparation and the vulnerable and worker lanes, phases lock no decision, host-relieving actions stay available when overloaded).
- Part 1 records the famine country registry; Part 2 adds the national food crisis and the bounded Conceal Hunger and Continue Requisitions shocks; Part 3 states the single evacuation decision; Part 7 records the Hunger Lines launch-day stage commit, special Chaos front flight, and the queued Condemnation donor link.
- Maritime evacuation, abandoning a state, prioritized entry and internment reception are listed in Part 6 as unresolved source proposals outside the current inventory.
- The decision and mission prompt's family list matches the merged decisions; pass 2 design changes were not applied because another agent's rework owns the current design.

## Current C11 authority

The owner’s 13 October instruction restores the removed decision roles exactly from `839850b0d^` and supersedes the merged-action descriptions recorded in the dated 10 October alignment above. The restored roles use the requested local-pressure gates and fuel/conditional-convoy costs, retaining genuinely added famine mechanics and original equipment requirements. Current evidence and limits are in [the C11 history report](../../plans/migration_famine_history_2026-10-13.md).
