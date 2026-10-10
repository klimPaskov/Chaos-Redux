# Event 54: Gift from Scientists Specification Pack

## Authority and current workflow

The [source manifest](quality/054_gift_from_scientists_source_review_manifest.md) retains original planning evidence. It does not establish approval of every provider, cluster, or achievement elaboration.
Use current [planning](../../../.claude/skills/chaos-redux-event-planning/SKILL.md), [events](../../../.claude/skills/chaos-redux-events/SKILL.md), [assets](../../../.claude/skills/chaos-redux-event-assets/SKILL.md), and [routing](../../../.claude/skills/chaos-redux-subagents/SKILL.md) guidance.
Unattributed design remains `unresolved`; rediscover current tools and source state before a separately authorized implementation task.

This pack defines the source-design planning handoff for Event 54, Gift from Scientists.

The event is a Minor Repeatable global research incident at Chaos level 1. Every valid research participant receives an independently selected technology from its own safe missing-technology pool. The active grant target rises from one technology to three, five, and ten across the three evolutions. Registered Chaos Redux technologies enter only through an owner-approved contract from Evolution II onward.

## Shared cluster identifier

Scientific Research uses reserved `event_cluster_id = 21` under the [shared identifier registry](../shared_identifier_registry.md).
The reservation is shared with Event 089 and prevents the old provisional ID `9` from colliding with National Breakthroughs.
It approves only the identifier allocation; cluster design, membership and implementation retain their separate acceptance requirements.

## Design decisions

- Every country rolls independently from its own current technology state.
- Draws use equal candidate weight and occur without replacement.
- Technology power is intentionally uneven.
- Ahead-of-time technologies are allowed.
- Doctrines remain under Event 27.
- Mutually exclusive branches and unsafe hidden technologies are excluded or handled by a declared safety profile.
- Custom technologies remain excluded until their owner registers them explicitly.
- A registered grant does not fire, complete, or advance its owning event.
- One bounded world transaction resolves the firing and creates one global pacing event.
- Human recipients receive one consolidated report after grants are committed.
- The Scientific Research cluster supports mixed event types and Event 27's second membership in Military Preparation.
- Presentation uses the standard report event, Event Details, evolution history, and cluster surfaces.

## Package map

### Source specification

1. `specs/054_gift_from_scientists_spec_part_1_core.md`
2. `specs/054_gift_from_scientists_spec_part_2_technology_pool.md`
3. `specs/054_gift_from_scientists_spec_part_3_global_transaction.md`
4. `specs/054_gift_from_scientists_spec_part_4_evolutions_and_chaos.md`
5. `specs/054_gift_from_scientists_spec_part_5_connections_and_cluster.md`
6. `specs/054_gift_from_scientists_spec_part_6_ai_multiplayer_and_balance.md`
7. `specs/054_gift_from_scientists_spec_part_7_presentation_assets_and_achievements.md`

### Design matrices

- `matrices/054_gift_from_scientists_technology_eligibility_matrix.md`
- `matrices/054_gift_from_scientists_probability_scenarios.md`

### Implementation prompts

- `prompts/054_gift_from_scientists_coding_prompt.md`
- `prompts/054_gift_from_scientists_goal_prompt.md`
- `prompts/054_gift_from_scientists_technology_registry_prompt.md`
- `prompts/054_gift_from_scientists_asset_prompt.md`
- `prompts/054_gift_from_scientists_achievement_prompt.md`
- `prompts/054_gift_from_scientists_localisation_audit_prompt.md`
- `prompts/054_gift_from_scientists_probability_audit_prompt.md`
- `prompts/054_gift_from_scientists_catalog_prompt.md`
- `prompts/054_gift_from_scientists_completion_audit_prompt.md`

### Quality and handoffs

- `quality/054_gift_from_scientists_acceptance_criteria.md`
- `quality/054_gift_from_scientists_improvement_loop_closure.md`
- `quality/054_gift_from_scientists_source_review_manifest.md`
- `handoffs/054_gift_from_scientists_catalog_handoff.md`
- `handoffs/054_gift_from_scientists_subagent_routing_review.md`

## Repository location

The source package lives at `docs/specs/054_gift_from_scientists_specs/`.

## Status boundary

This is a planning package. It contains no gameplay implementation, generated assets, workbook edit, MCP validation result, or live-playtest claim.

## Open questions

- `unresolved`: Event 54 and Event 60 selection rule. Recommendation: keep Event 54's equal random draw over the full safe missing pool, as the design decisions above already state, and let Event 60 reconcile a loss only when the random draw happens to return it. A lost-technology priority would add a second selection rule to a no-choice event for a small benefit.
- `unresolved`: protection of gifted technologies from later Event 60 regression. Recommendation: no provenance protection. Gifted nodes become ordinary researched nodes and follow Event 60's normal safety policy, which avoids a permanent per-technology provenance record in every save.

## Changelog

### 2026-10-10 spec audit

- The player report lists only the granted technologies and one plain line when fewer than the stage amount arrived. Registry origin, pool exhaustion, and stage targets were removed from player text because none of them changes a decision and naming the registry explains away the mystery.
- Recipient receipts keep only the firing identity, granted technology identities, and registered provider identities, which are the fields later consumers read; rejection counts and pool data move to development logging.
- Acceptance criteria and the coding prompt match the shorter report.
- Subagent instructions use the Claude-first wording; the two Event 60 interaction choices are recorded above with a recommendation.
