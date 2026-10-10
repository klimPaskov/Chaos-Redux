# Event 080: Airship planning package

## Use

Read the numbered specifications in order. For implementation, start with the coding prompt and its linked specialist prompts. The goal prompt is ready to copy as a `/goal` instruction and stays under 4,000 characters.

This is a rework design for the legacy `events/080_airship.txt` and is not implemented. The user's catalog entry, existing route, 121 two-day transitions, controller-based host rules, real deaths, immediate foreign-controller war, and named evolutions are fixed user requirements. Balance values, capacities, story situations, reward conditions, and the rare Flying City super-event are authored design, accepted within the original planning brief and revised by the 10 Oct 2026 spec audit under the user's planning-package brief. They are not playtested.

## Specifications

| Part | File | Content |
|---|---|---|
| 1 | [Core voyage](080_airship_spec_part_1_core.md) | Identity, launch, route, timing, stops, diversions, phases, and endings |
| 2 | [Condition and operations](080_airship_spec_part_2_condition_and_operations.md) | Condition, incident model, risk band, standing orders, services, missions, and AI |
| 3 | [Passengers and hosts](080_airship_spec_part_3_passengers_and_hosts.md) | Boarding-group manifest, deaths, 36 passenger situations, 24 host situations, and story continuity |
| 4 | [War, crashes, and rescue](080_airship_spec_part_4_war_crashes_and_rescue.md) | Combat encounters, capture, casualty profiles, state damage, immediate war, fires, and rescue |
| 5 | [Evolutions and experiments](080_airship_spec_part_5_evolutions_and_experiments.md) | Grand Tour, Experimental Flight, Flying City, four trial families, and exposure-based rewards |
| 6 | [Rewards, Chaos, and achievements](080_airship_spec_part_6_rewards_chaos_and_achievements.md) | Success and failure results, host rewards, Chaos map, shared connections, and eight achievements |
| 7 | [Map and presentation](080_airship_spec_part_7_map_and_presentation.md) | Existing map, native interface, ship forms, scene inventory, news, super-event, and writing direction |

## Prompts

| Prompt | File |
|---|---|
| Main implementation | [Coding prompt](080_airship_coding_prompt.md) |
| Goal instruction | [Goal prompt](080_airship_goal_prompt.md) |
| Visual production | [Asset prompt](080_airship_asset_prompt.md) |
| Operations and AI audit | [Decision and mission prompt](080_airship_decision_mission_prompt.md) |
| Achievement implementation and icons | [Achievement prompt](080_airship_achievement_prompt.md) |
| Rare catastrophe presentation research | [Super-event prompt](080_airship_super_event_prompt.md) |

## Supporting documents

The [implementation handoff](080_airship_implementation_handoff.md) defines owner boundaries, integration contracts, and specialist routing. The [validation matrix](080_airship_validation_matrix.md) holds 64 functional fixtures, 16 probability scenario groups, and the fixed-Condition reference arithmetic. The [route crosswalk](080_airship_route_crosswalk.md) preserves the legacy region predicates for indices 0 through 121; exact geographic binding remains required. The [research and source report](080_airship_research_and_source_report.md) records legacy evidence, historical leads, and the release gates.

No `docs/plans/080_airship_plans/` companion exists yet; implementation records belong there.

## Revision log

### 2026-10-10 spec audit

Basis: 10 Oct 2026 spec audit under the user's planning-package brief.

- Replaced population-backed travel custody with a boarding-group manifest: travellers stay resident in their origin state and only deaths are debited, once, from origin states. This keeps the user's real-deaths requirement, removes the travel-custody release gate, and makes births, stowaways, and detention population-neutral (Parts 3, 4, handoff, validation).
- Unresolved disappearances end as presumed losses registered once when the voyage closes, instead of a permanent missing-person ledger (Parts 1, 2, 3, 4, 6).
- Reduced standing services from six to four by moving provisions and extended programmes into story and reception choices, and merged six trial families into four with no hidden one-off protections (Parts 2 and 5).
- Replaced the host's 90-day state construction bonus with a USA opinion modifier, and removed the +2 dispute and crowd-accident Chaos rows and the small crash reversals (Part 6).
- Added a four-step risk band so players see the danger and its main cause instead of incident percentages (Parts 1 and 2).
- Deleted `080_airship_supplied_source_read_ledger.json` (obsolete archive-reading evidence), `080_airship_risk_arithmetic.md` (moved into the validation matrix), and `080_airship_specialist_handoffs.md` (routing moved into the implementation handoff); removed archive-session narration from the README and research report.

## Open questions

- The 084 Peace Movement package still describes Airship boarding as removing people from their origin state (its Part 10 world-denominator paragraph and acceptance case QA59). Under the boarding-group model that proof gate is satisfied automatically; the 084 owner should simplify those lines.
