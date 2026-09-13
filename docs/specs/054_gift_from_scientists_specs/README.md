# Event 54: Gift from Scientists Specification Pack

This pack defines the accepted planning handoff for Event 54, Gift from Scientists.

The event is a Minor Repeatable global research incident at Chaos level 1. Every valid research participant receives an independently selected technology from its own safe missing-technology pool. The active grant target rises from one technology to three, five, and ten across the three evolutions. Registered Chaos Redux technologies enter only through an owner-approved contract from Evolution II onward.

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

## Extraction target

The ZIP preserves the repository-relative path `docs/specs/054_gift_from_scientists_specs/`. Extract it at the repository root.

## Status boundary

This is a planning package. It contains no gameplay implementation, generated assets, workbook edit, MCP validation result, or live-playtest claim.
