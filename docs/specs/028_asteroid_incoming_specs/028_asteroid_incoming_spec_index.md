# Event 028: Asteroid Incoming

This folder is the source design package for Event 028, Asteroid Incoming.
It is the package README: it owns the explicit user requirements, the implementation status map, the file index, the open questions and the changelog.

Event 028 is a global fire-once Major event.
A chooser picks one of three locked country and state targets or a genuine near miss.
A strike locks for two days, destroys the chosen state, damages three land-adjacency rings, records civilian deaths, leaves a permanent crater, starts a global atmospheric dust aftermath and opens a phased national recovery category.
At 600 Chaos, fragments strike other regions; at 800 Chaos, crater control grants land-armour bonuses.

Workflow owners: [event integration](../../../.claude/skills/chaos-redux-events/SKILL.md), [decisions and missions](../../../.claude/skills/chaos-redux-decisions-missions/SKILL.md), [subagent routing](../../../.claude/skills/chaos-redux-subagents/SKILL.md) and [asset production](../../../.claude/skills/chaos-redux-event-assets/SKILL.md).

## Source-of-truth map

| Question | Owner |
| --- | --- |
| What the event must do and why | This package (design) |
| What the source currently does | [Event 028 overview](../../events/028_asteroid_incoming/overview.md) and [map presentation](../../events/028_asteroid_incoming/map_presentation.md) |
| Exact tuning values | `common/script_constants/028_asteroid_incoming_constants.txt`, with idea values mirrored as `@` constants in `common/ideas/028_asteroid_incoming_ideas.txt`; the [tuning matrix](028_asteroid_incoming_tuning_matrix.md) records design ranges and change control |
| Implementation decisions and their basis | [Agent decisions 2026-10-04](../../plans/028_asteroid_incoming_plans/agent_decisions_2026-10-04.md) and [finishing decisions](../../plans/028_asteroid_incoming_plans/agent_decisions_2026-10-05.md) |
| Current open gates and evidence | [Current resume](../../plans/028_asteroid_incoming_plans/resume_20261007.md) and [takeover status](../../plans/028_asteroid_incoming_plans/takeover_status_2026-10-06.md) |
| Assets, super-event research and catalog row | `docs/events/028_asteroid_incoming/assets/`, `docs/super_events/028_asteroid_incoming_super_event_research.md`, and the [catalog alignment handoff](../../plans/028_asteroid_incoming_plans/subagent_handoffs/catalog_alignment_20261007.md) |

When the spec and the source disagree, the status table below says which side is ahead.
Implementation evidence proves what exists; it does not by itself make a proposal accepted design.

## Explicit user requirements

These requirements come from the user and are the acceptance core of the event.
They cannot be reduced or replaced without a new user decision.
Every other file points here instead of restating them.

| Requirement | Basis | Owning part |
| --- | --- | --- |
| Event 28, Asteroid Incoming, Major, global and fire-once, no cluster, no world-end scenario | Supplied Event 028 brief | Part 1 |
| Three valid random target countries, each with a suitable state, plus a near-miss option | Brief | Part 2 |
| Prefer states with meaningful land adjacency over isolated empty islands | Brief | Part 2 |
| Roughly two-day trajectory lock before impact | Brief | Part 2 |
| Main state loses all civilian population and all buildings and becomes a permanent crater or wasteland | Brief | Part 3 |
| Direct land neighbours lose about 50 percent of civilians, the second ring about 25 percent and the third ring about 5 percent, with matching building damage, across borders through real adjacency | Brief | Part 3 |
| Civilian losses feed the shared Deaths system and every affected country gets one report | Brief | Part 3 |
| A dynamic global super-event names the target country and region after a strike | Brief | Part 8 |
| Atmospheric dust follows every strike, scales with the destruction, and reduces production, supply, weather quality and Air Cleanliness; it may connect to Event 013 | Brief | Part 4 |
| The near miss causes no impact and no dust | Brief | Parts 1 and 4 |
| Global Fragmentation at 600 Chaos: the main body still strikes, extra fragments strike worldwide with a normal nuclear-scale visual, fragment centres lose about 50 percent of population and buildings, their rings 25 and 5 percent, with deaths, reports and added dust; the main strike keeps the super-event | Brief | Part 5 |
| Extraordinary Minerals at 800 Chaos keeps fragmentation; the main crater gives its controller plus 100 percent land-division armour and each fragment site plus 20 percent, following current control, stacking without a cap; craters become strategic objectives | Brief | Part 5 |
| Thermonuclear and nuclear map effects are presentation only: no nuclear use, damage, ledger, condemnation, retaliation or fallout | Brief plus the later explicit presentation-only instruction recorded in the [map presentation](../../events/028_asteroid_incoming/map_presentation.md) | Parts 3 and 9 |
| Every event from 1 to 40 is playable in the default queue | User instruction recorded in the 2026-10-04 agent decisions (Default queue) | Part 8 |

The user also granted the implementing agent full design authority for Event 028 on 2026-10-04 and authority to correct weak design and source logic (G6) on 2026-10-06.
Decisions made under that authority are accepted design with that basis; they are recorded in the plans folder and summarized in the parts.

## Implementation status

Event 028 is enabled in the default event queue, its catalog row is Major with status Needs Testing, and native verification by the user is outstanding.

| Area | Status | Notes |
| --- | --- | --- |
| Target board, confirmation, lock, preparedness, resolver, watchdog (Parts 1 and 2) | Implemented | Native save/reload of a pending board and annexed-chooser paths are live checks. |
| Population rings, Deaths, crater state, unit damage, country reports (Part 3) | Implemented | One native episode reconciled all population receipts exactly. |
| Complete railway and supply-node demolition and queue purge in the main crater (Part 3) | Blocked | See Open question 1. |
| Dust, stages, Air Cleanliness slot, protection, Event 013 secondaries (Part 4) | Implemented | |
| Fragmentation and minerals, site profiles, control refresh (Part 5) | Implemented | |
| Recovery category, 15 decisions, 5 missions, cleanup (Part 6) | Implemented | Mission design scopes follow the G6 dispositions in Part 6. |
| Opening AI, recovery AI, crater front strategy and peace desire (Part 7) | Implemented in source | Probability scenarios are partly evaluated; see the current resume. |
| History, Event Details, evolutions, news, super-event, audio (Part 8) | Implemented | News delivery order (L1) awaits a live check before its temporary receipt is removed. |
| Graphics-only map visuals (Part 9) | Implemented | Native playback, placement and retirement are live checks. |
| All event art, icons, achievement triplets (Parts 9 and 10) | Implemented | 55 mod-owned DDS files plus one vanilla category icon. |
| Five achievements (Part 10) | Implemented | |
| Famine and migration aftermath (Parts 1 and 3) | Proposed, not implemented | Added by the 2026-10-10 audit; needs parent acceptance and a famine-owned adapter. |
| Camp-site reconciliation in the footprint (Part 3) | Proposed, not implemented | Added by the 2026-10-10 audit; needs the camp owner. |
| Chooser condemnation through a non-weapon context (Part 1) | Proposed, not implemented | Added by the 2026-10-10 audit; needs parent acceptance and the condemnation owner. |
| Suitability-weighted target draw (Part 2) | Proposed, not implemented | Added by the 2026-10-10 audit. |
| Global mitigation earned only through the Observation Network (Part 4) | Proposed, not implemented | Added by the 2026-10-10 audit; the source adds one point per protection action and saturates after three. |
| Retiring the modifier-free fragment-material marker ideas (Part 5) | Proposed, not implemented | Added by the 2026-10-10 audit; the dynamic modifier becomes the single fragment surface. |
| "on [continent]" wording in the locked-course bulletin and confirmation (Part 8) | Pending localisation fix | Should read "in [continent]". |
| Event 029 mine reconciliation (Part 3) | Unresolved, not implemented | Cross-owner design shared with the Event 029 package; no attributable acceptance found. |

## Design boundaries

These expansions were rejected as bloat during the original design review and stay rejected unless the user asks for them.

- A dedicated asteroid scripted GUI window
- A target-country focus tree, new crater nations or new tags
- A third evolution or a terminal world-end route
- Ocean impacts and tsunami geometry
- Named character death rolls
- A custom asteroid or crater 3D model
- Several competing dust currencies or a private air-quality meter
- A manually triggerable scenario
- A world-threat source: the impact is a one-off disaster, and registering it as an existential threat would calm wars for the whole dust period without a gameplay reason

## Files

| File | Purpose |
| --- | --- |
| `028_asteroid_incoming_spec_part_1_core.md` | Event promise, full flow, fixed rules and shared-system connections |
| `028_asteroid_incoming_spec_part_2_targeting_and_trajectory.md` | Target board, confirmation, lock, preparedness, capital relocation and ring geometry |
| `028_asteroid_incoming_spec_part_3_impact_damage_and_aftermath.md` | Damage profiles, buildings, units, Deaths, crater state, reports and cross-owner aftermath |
| `028_asteroid_incoming_spec_part_4_dust_and_global_recovery.md` | Dust Load, stages, Air Cleanliness, protection, mitigation and decay |
| `028_asteroid_incoming_spec_part_5_evolutions.md` | Global Fragmentation, Extraordinary Minerals, site profiles and transfer rules |
| `028_asteroid_incoming_spec_part_6_decisions_and_missions.md` | Recovery category, phases, actions, missions, prices, AI and cleanup |
| `028_asteroid_incoming_spec_part_7_ai_multiplayer_and_balance.md` | Opening AI, crater AI, multiplayer, probability scenarios and anti-exploit rules |
| `028_asteroid_incoming_spec_part_8_events_logs_and_text_direction.md` | Event chain, news, history, Event Details, evolution views and writing direction |
| `028_asteroid_incoming_spec_part_9_visual_and_audio_direction.md` | Map visuals, art direction, icon families and audio |
| `028_asteroid_incoming_spec_part_10_achievements_and_acceptance.md` | Achievements, acceptance criteria and validation scenarios |
| `028_asteroid_incoming_tuning_matrix.md` | Implemented values against design ranges, and tuning change control |
| `028_asteroid_incoming_research_basis.md` | Scientific and historical research with abstraction limits |
| `028_asteroid_incoming_coding_prompt.md` | Remaining-work implementation prompt |
| `028_asteroid_incoming_goal_prompt.md` | Compact goal prompt pointing to the coding prompt |
| `028_asteroid_incoming_decision_mission_prompt.md` | Decision and mission audit prompt |
| `028_asteroid_incoming_ai_probability_prompt.md` | Probability audit prompt |
| `028_asteroid_incoming_achievement_prompt.md` | Achievement audit prompt |
| `028_asteroid_incoming_asset_prompt.md` | Asset status and reopening rules |
| `028_asteroid_incoming_super_event_prompt.md` | Super-event research status and reopening rules |

## Open questions

Each item needs a parent or user decision before implementation.

1. **Main-crater network demolition.**
   The brief requires the main state to lose all buildings.
   Ordinary provincial and state buildings are removed, but railways and supply nodes are only wrecked and suppressed (no repair, minus 100 percent construction speed, wasteland category), and queued construction or special projects are not proven cancelled.
   Proposal: accept the wrecked-and-suppressed network as meeting the requirement if the live check shows no usable railway or supply node remains; otherwise keep the item blocked.
   Because it would narrow a user requirement, it needs user approval.
2. **Mission failure consequences (simplification).**
   An expired mission currently applies five consequences: rescue-failure deaths, returned local damage for 90 days, a state failure-pressure modifier, the full national burden for 90 days, and a 25 percent repair surcharge for 180 days.
   Proposal: drop the separate repair surcharge and its price-refresh callback (`chaosx.nr28.12`), because the returned damage and burden already make failure costly and the surcharge is a hidden multiplier the player cannot plan around.
   This changes behaviour accepted under the user's design authority, so it needs parent acceptance.
3. **Chooser condemnation.**
   Part 1 proposes a non-weapon condemnation context for the country that directs a strike, so the strike carries a diplomatic cost and the near miss stays credible.
   It needs parent acceptance and the condemnation owner, because it adds a context to the shared ledger.
4. **Famine and camp aftermath.**
   Parts 1 and 3 propose an asteroid famine adapter and camp-site reconciliation.
   Both need parent acceptance and their system owners.
5. **Collateral exposure of guarantees and non-aggression partners.**
   The strike AI protects guaranteed and non-aggression targets directly, but its friendly-ground check (the 0.25 factor) does not count their states in the first two rings.
   Proposal: include them, since Part 7 already treats those relationships as protected.
   Left open because the probability audit recorded it as a design decision without a disposition.
6. **Frozen target identity.**
   The accepted F06 decision keeps live country pointers instead of a name and flag snapshot, so a cosmetic rename during the two-day lock shows the new name.
   The current resume still lists the snapshot contract as unresolved; the parent should confirm F06 as final or reopen it.

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:

- Made this index the package README with a source-of-truth map, one explicit-requirements table, an implementation status table, open questions and this changelog.
- Fixed dead skill links (`.agents/skills` to `.claude/skills`), replaced `AGENTS.md` with `CLAUDE.md`, and removed Codex-specific `fork_turns` instructions and the stale "repository and MCP not mounted" review claims.
- Deleted `028_asteroid_incoming_design_review.md`; its rejected-bloat list moved to Design boundaries and its remaining findings were superseded by the implementation.
- Deleted `028_asteroid_incoming_source_crosswalk.md`; the brief-to-part mapping is now the explicit-requirements table.
- Deleted `028_asteroid_incoming_catalog_reconciliation.md`; the catalog row was aligned on 2026-10-07 and the remaining spreadsheet rule lives in Part 8.
- Reconciled every part with the implemented source: event IDs, board validity flag, resolver watchdog, F06 identity decision, capital fallback tiers, unit damage, per-province building rounding, site profiles, recovery prices, mission scopes, local emergency closure, graphics-only visuals, crater AI strategy and peace desires, two-line history rows and default enablement.
- Rewrote the tuning matrix to show implemented values beside design ranges, with the constants file as the value owner.
- Reduced the coding, goal, decision, AI, achievement, asset and super-event prompts to remaining work and pointers, removing restated rules.

Pass 2, design improvement:

- Proposed famine aftermath through a famine-owned asteroid adapter, so impact damage and dust reach food security through the existing Famine category instead of a new asteroid food value; migration follows through the famine-owned survivor flight.
- Proposed reconciling registered camp sites in the footprint with the camp owner, so destroyed camps do not leave stale detainee ledgers.
- Proposed a non-weapon condemnation context for the chooser, giving the strike a real diplomatic cost without a false weapon record.
- Proposed a suitability-weighted country draw, so boards stay random but more often offer targets whose rings matter.
- Proposed earning global dust mitigation only through the Observation Network, because the source's one point per protection action saturates after three actions worldwide and blurs national protection with global help.
- Proposed retiring the modifier-free fragment-material marker ideas, which duplicate the fragment armour modifier on the national spirits bar.
- Removed fairy dust from the design: rival intelligence reports about the armour advantage, linked-disaster warning delays and resilience that have nothing to act on, post-opening secondary-disaster dust, and the frozen name/flag snapshot field.
- Stated that the dust stage, national protection and recovery phase are the decision-driving values, and that the numeric Dust Load is a record value shown only in Event Details.
- Recorded two simplification proposals that conflict with accepted implemented behaviour as open questions instead of overriding them.
