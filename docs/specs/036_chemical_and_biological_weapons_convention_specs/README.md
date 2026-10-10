# Event 036: Chemical and Biological Weapons Convention specification package

This package is the design source for Event 036, a Minor Fire-Once diplomatic event in which governments sign a convention that makes chemical and biological warfare legitimate among its members, then argue in recurring conferences over first use, integrated doctrine, unrestricted arsenals, and a shared program that opens event-gated Chaos weapon projects.

Workflow owners: [event integration](../../../.claude/skills/chaos-redux-events/SKILL.md), [decisions and missions](../../../.claude/skills/chaos-redux-decisions-missions/SKILL.md), [subagent routing](../../../.claude/skills/chaos-redux-subagents/SKILL.md), [assets](../../../.claude/skills/chaos-redux-event-assets/SKILL.md), and `CLAUDE.md`.

## Status

Not implemented.
Slot 36 holds the Alien Spacecraft stub (`events/036_alien_spacecraft.txt`), whose receipts feed Event 016 and Event 025, and [01](01_event_identity_and_playable_promise.md#legacy-alien-spacecraft-relocation) owns moving its alien jet recovery into Event 025.
No plans folder exists for this event.

The workbook lists Event 036 as a High-severity member of cluster 3, Diplomacy, while its event row still describes Alien Spacecraft as Minor Repeatable.
The runtime cluster registry has no Event 036 member row yet.
[The spreadsheet prompt](prompts/spreadsheet_alignment_prompt.md) records the exact catalog state.

[The coding prompt](prompts/coding_prompt.md) is the implementation entry point.

## Acceptance basis

- Recorded catalog facts: Event 036 is a High-severity member of cluster 3, Diplomacy, with Chaos level 1, as the authoritative workbook lists it.
- Original concept carried by the imported package, whose source brief is not in the repository: the convention replaces Alien Spacecraft, the event is Minor Fire-Once, five national answers, three evolutions at `200+`, `400+`, and `600+` Chaos, and an International Chaos Weapons Program with the Zombie Weapon and Black Plague Weapon as examples, exactly equal project selection, immediate cancellation when a weapon becomes normally available, and no source-event activation.
  This audit keeps every one of these intact, but no attributable user decision is recorded for them, so their disposition stays `unresolved`.
- Parent acceptance, 2026-10-10 (release orchestrator, under the user's 2026-10-10 brief section 2.2 authority, recorded in the release ledger): the package design and the five shared-system hooks listed under "Shared-owner adapters" are accepted; the orchestrator owns those shared systems for this milestone.
  The alien jet recovery is not retired but relocated into Event 025 as its entry, keeping its receipt names, because Events 016 and 025 consume those receipts.
  Disposition: `accepted and queued` for the Event 036 implementation owner.
- The Event 076 link remains a proposal.
- The 2026-10-10 changes were made under the user's 2026-10-10 audit brief, which authorized substantial rework to remove redundant values, repeated decisions, and parallel systems.
  They change the unresolved design and promote nothing to accepted.

## Package map

| File | Owns |
| --- | --- |
| [00 Master spec](00_master_spec.md) | Architecture summary, public information budget, ownership map, boundaries |
| [01 Identity](01_event_identity_and_playable_promise.md) | Catalog identity, Alien Spacecraft retirement, setup, eligibility, multiplayer, Standing, pacing, tone |
| [02 Postures](02_national_postures_and_membership.md) | Postures, covert program, registries, accession, revision, withdrawal, suspension |
| [03 Condemnation](03_condemnation_normalization_and_cbrn_integration.md) | Relief placement, contexts, multipliers, retaliation, reservation breach, normalization, evidence, checks |
| [04 Conferences](04_recurring_conventions_and_treaty_families.md) | Scheduler, responses, quorum, the ten treaty families, failure, collapse |
| [05](05_evolution_i_first_use_becomes_acceptable.md), [06](06_evolution_ii_strategic_wmd_doctrine.md), [07](07_evolution_iii_arsenal_without_limits.md) Evolutions | Evolution pacing, changes, integrated doctrine, hard limits |
| [08 Program](08_international_chaos_weapons_program.md) | Grants, known candidates, provider contract, selection, lifecycle, contributions, completion, cancellation |
| [09 Decisions](09_decisions_missions_costs_and_visibility.md) | Header, visibility, decisions, missions, costs, exploit controls |
| [10 AI](10_ai_behavior_and_probability_contract.md) | AI rules |
| [11 Event chain](11_event_chain_reactions_and_localisation_direction.md) | Namespace, news, logs, Event Details, writing direction |
| [12 Chaos and connections](12_chaos_impact_and_cross_event_connections.md) | Event-owned Chaos, shared systems, other events, cluster |
| [13 Achievements](13_achievements.md) | Seven achievements |
| [14 Assets](14_asset_requirements.md) | Asset inventory and direction |
| [15 Completion](15_acceptance_and_completion_contract.md) | Event-specific surfaces, discovery list, save contract |
| [Posture matrix](matrices/national_posture_matrix.md) | Per-posture rights and transitions |
| [Treaty matrix](matrices/treaty_family_matrix.md) | Per-family table and retired families |
| [State matrix](matrices/event_state_and_cleanup_matrix.md) | State lifecycle and cleanup |
| [Acceptance scenarios](matrices/acceptance_scenarios.md) | Test scenarios |
| [AI scenarios](matrices/ai_probability_scenarios.md) | Named probability scenarios |
| [Prompts](prompts/) | Coding, goal, decisions, achievements, assets, localisation, completion audit, spreadsheet |
| [Improvement-loop closure](quality/improvement_loop_closure.md) | Historical planning-loop record |
| [Research](research/historical_and_institutional_anchors.md) | Historical and institutional anchors |

## Main design decisions

- Four public postures, with the fifth opening answer recorded as Public Rejection plus a covert program flag.
- The player reads three header values: posture with its permission line, Standing, and the current agenda or project.
- Relief applies only to the weapon base at the doctrine mitigation point, so civilian deaths, contamination, public-harm floors, and repeat use need no extra convention rules.
- First-use permission is the existing CBRN use policy plus ratified clauses, and retaliation is the existing Retaliation Authority ledger.
- Evidence, inspections, and decontamination aid reuse the existing CBRN diplomacy actions, which makes the Inspection Protocol a real trade-off for countries hiding camps or programs.
- Ten treaty families, each with a distinct mechanical effect.
- A program grant is an access flag in the provider's special-project trigger, following the Mengele directorate precedent.

## Scope boundaries

Event 036 has no focus tree, country tag, super-event, world-end scenario, manual scenario, scripted GUI, custom unit, portrait, animation, or 3D asset.
The public decision category and ordinary events carry every choice, and the program reuses native special projects.

## Open questions

### Decisions needed from the user

None open.
The alien recovery and package acceptance were decided on 2026-10-10 (see Acceptance basis).

### Conflicts with recorded decisions

None.
No recorded user decision conflicts with the audit changes, so no proposal is held back for that reason.

### Shared-owner adapters awaiting owner acceptance

Each is part of the design but changes a system Event 036 does not own:

1. The convention hook at the chemical doctrine mitigation point and in `condemnation_add_source` ([03](03_condemnation_normalization_and_cbrn_integration.md#where-relief-applies)).
2. A neutral helper that applies the pledge-breach consequence for a reservation breach without the `condemnation_non_use_pledge` flag ([03](03_condemnation_normalization_and_cbrn_integration.md#reservation-breach)).
3. One participant-score term in `condemnation_recalculate_participants` ([03](03_condemnation_normalization_and_cbrn_integration.md#sanction-reactions)).
4. Treaty eligibility bases for `cbrn_demand_inspections` and `cbrn_sponsor_decontamination_mission` ([04](04_recurring_conventions_and_treaty_families.md#baseline)).
5. Access flags read by `black_plague_weaponization_directorate_has_access` and the `weaponize_the_zombies` visibility trigger, plus cancellation calls in their normal routes ([08](08_international_chaos_weapons_program.md#known-candidates)).

### Proposals awaiting acceptance

1. Event 076 USA Tests Weapons: when the United States runs an unconventional weapons test, the test reads its Event 036 posture, so a Full Ratification test is a declared trial and a Reservation or Rejection test counts as a hidden program for inspection purposes.
   Event 076 is a specification without this hook, so the connection waits for both packages.

## Changelog

### 2026-10-10 orchestrator review

- Recorded the parent acceptance of the package design and the five shared-system hooks, and changed the Alien Spacecraft path from retirement to relocation into Event 025 with unchanged receipt names (parts 01, 12, 14, 15, the acceptance matrix, and the coding and completion prompts).

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:

- Replaced the stale catalog warning: cluster 3 is now named Diplomacy (formerly Diplomatic Panic) and already lists Event 036 at High severity, so the specs require only the runtime member row and the event-row update.
- Added the missing Alien Spacecraft retirement section, because the current slot-36 stub feeds Event 016 and Event 025 receipts that the package never mentioned.
- Replaced `AGENTS.md`, `.agents/skills`, ImageGen, and mandatory-MCP wording with `CLAUDE.md`, `.claude/skills`, and the current image route, and removed the "repository not mounted" and Codex-era subagent claims.
- Deleted `PACKAGE_MANIFEST.md` (original upload hashes and ZIP extraction contract), `quality/source_audit.md` (original environment and TOML read receipts), and `quality/catalog_alignment_handoff.md` (stale supplied-export state, now in the spreadsheet prompt).
- Merged `matrices/condemnation_tuning_matrix.md` into 03 and `matrices/chaos_weapon_registry_contract.md` into 08, because both repeated tables already in those files.
- Deleted `prompts/improvement_loop_prompt.md` and `prompts/international_chaos_weapons_program_prompt.md`, folding the program steps into the coding prompt and leaving improvement routing to `CLAUDE.md`.
- Gave each topic one owner, turned the master spec into a summary and ownership map, cut the prompts and 15 to event-specific points, and reflowed every file to one sentence per line.
- Fixed the tone direction to the events skill, which rejects conference paperwork and formal diplomatic phrasing as the emotional center.
- Recorded the acceptance basis: catalog facts, the original concept requirements, and the rest as `unresolved`.

Pass 2, design improvement:

- Replaced the five-state first-use policy with the existing CBRN use policy plus ratified clauses, and the three-level integration state with one binary integrated doctrine, removing two parallel systems.
- Moved relief to the weapon base at the doctrine mitigation point, which let the chemical civilian floor, the repeat-use column, the action snapshot receipt, and the bucket floors go, and mapped every floor to a real Condemnation context.
- Added a combined floor so doctrine mitigation and convention relief cannot erase chemical Condemnation, and tied retaliation to the existing Retaliation Authority ledger and reservation breach to the existing pledge-breach consequence.
- Cut opening normalization to the chemical and biological buckets, because nuclear reductions of 5 to 10 percent changed no decision, and required the option tooltip to show the resulting tier.
- Folded Retaliation Guarantee, Biological Mobilization Articles, and Allied CBRN Command Compact into other families (thirteen to ten), cut national responses from five to three, and replaced the support label with the ratification count against the quorum.
- Replaced duplicated decisions (Publish Evidence, Offer Protective Assistance, Prepare for Inspection, Demand a Reservation Clause, the ratification mission) with the existing CBRN actions or the response event, giving the Inspection Protocol a real camp and covert-program cost.
- Defined Standing, the coordinator, and the Opposition Leader concretely, removed membership generations, simplified the program to four states with a Charter lapse rule, and defined a grant as a special-project access flag with two named candidates.
- Dropped the `-10` repudiation Chaos row, because no repeal agenda ever produced it, and kept the single `-5` collapse row.
- Made the covert program record hidden cover-up evidence through the existing disclosure path, so exposure follows real evidence.
- Fixed achievements that relied on proofs the game does not record (a nuclear first-use row, a casualty-mitigation receipt, a provider stockpile threshold) and updated them to the merged families.
- Stated explicitly why Event 036 has no famine, migration, Deaths, fallout, or world-threat link, and kept the Air Cleanliness Treaty conflict as a real choice.
