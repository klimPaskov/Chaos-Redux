# Chemical and Biological Weapons Convention

This file is the architecture summary and ownership map.
Each topic has one owning file, and this summary never overrides it.

## Event promise

Event 036 is a global diplomatic reordering that makes chemical and biological warfare increasingly legitimate among participating governments.

Its opening is a Minor Fire-Once event, but the convention persists as a treaty network, a source of recurring conference rounds, a modifier of Condemnation and AI behaviour, and a late gateway to registered Chaos weapon special projects.

The player decides what their country publicly defends and what it prepares in private, influences whether first use becomes normal, and may join or oppose an international program that opens weapon projects normally tied to separate Chaos events.

The convention changes incentives, permissions, research priorities, cooperation, inspections, AI behaviour, and Condemnation handling.
It never grants weapons, payloads, technologies, or special projects on entry.

## Five layers

1. **National posture.**
   Every eligible ordinary country takes one public posture at the opening: Full Ratification, Chemical Accession Only, Retaliation Reservation, or Public Rejection, with Public Rejection optionally backed by a covert program.
   Owner: [02](02_national_postures_and_membership.md) and [the posture matrix](matrices/national_posture_matrix.md).
2. **Convention Standing and recurring conferences.**
   Standing (Provisional, Divided, Established, Dominant) sets conference cadence and pressure, and one agenda at a time asks members to ratify a treaty family.
   Owner: [01](01_event_identity_and_playable_promise.md#convention-standing) for Standing and [04](04_recurring_conventions_and_treaty_families.md) with [the treaty matrix](matrices/treaty_family_matrix.md) for conferences.
3. **Condemnation and CBRN integration.**
   The convention relieves the weapon base of eligible new Condemnation sources according to posture and ratified treaties, and never touches deaths, contamination, evidence, attribution, atrocity, or cover-up.
   Owner: [03](03_condemnation_normalization_and_cbrn_integration.md).
4. **Evolutions.**
   Evolution I (`200+` Chaos) opens first-use treaties, Evolution II (`400+`) opens integrated doctrine and nuclear targeting treaties, and Evolution III (`600+`) opens the Arsenal Without Limits and the International Chaos Weapons Program.
   Owners: [05](05_evolution_i_first_use_becomes_acceptable.md), [06](06_evolution_ii_strategic_wmd_doctrine.md), [07](07_evolution_iii_arsenal_without_limits.md).
5. **International Chaos Weapons Program.**
   One shared project at a time, chosen with exactly equal probability among registered eligible providers, funded by member contributions, granting only the registered special-project access to active contributors, and cancelled at once if the weapon becomes available through its normal route.
   Owner: [08](08_international_chaos_weapons_program.md).

## Public information budget

The decision category header shows three values:

- National Posture, with one derived line naming what the country's ratified treaties permit (retaliation only, chemical first use, chemical and biological first use, or unrestricted use)
- Convention Standing
- Current Agenda, shown as the agenda name, the ratification count against the quorum, and the deadline, or, while a project is active, the project name, its research stage, its percentage, and whether the country has contributed

Everything else stays internal: weights, multipliers, candidate pools, contribution formulas, internal progress units, sponsor scores, and AI calculations.
Owner: [09](09_decisions_missions_costs_and_visibility.md#status-header).

## Shared-system rule

Event 036 reuses the existing CBRN use policy, CBRN action ledger, Retaliation Authority, Condemnation source helper, CBRN diplomacy actions, protection equipment, Deaths, Air Cleanliness, and native special projects.
It adds no parallel first-use state, inspection system, evidence ledger, protection value, or death reason.
Event-owned orchestration lives in Event 036 files, and shared owners receive only narrow adapters that the owning system documents.
Owner: [12](12_chaos_impact_and_cross_event_connections.md).

## Ownership map

| Topic | Owning file |
| --- | --- |
| Identity, setup, eligibility, multiplayer, Standing, pacing, legacy retirement | [01](01_event_identity_and_playable_promise.md) |
| Postures, covert program, membership, accession, revision, withdrawal, suspension | [02](02_national_postures_and_membership.md) |
| Condemnation relief, floors, retaliation, reservation breach, opening normalization, evidence | [03](03_condemnation_normalization_and_cbrn_integration.md) |
| Conference scheduler, responses, quorum, treaty families, failure, collapse | [04](04_recurring_conventions_and_treaty_families.md) |
| Evolutions | [05](05_evolution_i_first_use_becomes_acceptable.md), [06](06_evolution_ii_strategic_wmd_doctrine.md), [07](07_evolution_iii_arsenal_without_limits.md) |
| Chaos weapon program, provider contract, contributions, completion, cancellation | [08](08_international_chaos_weapons_program.md) |
| Category, header, decisions, missions, costs, exploit controls | [09](09_decisions_missions_costs_and_visibility.md) |
| AI rules | [10](10_ai_behavior_and_probability_contract.md), scenarios in [the AI matrix](matrices/ai_probability_scenarios.md) |
| Event chain, logs, Event Details, writing direction | [11](11_event_chain_reactions_and_localisation_direction.md) |
| Event-owned Chaos, shared systems, other events, cluster | [12](12_chaos_impact_and_cross_event_connections.md) |
| Achievements | [13](13_achievements.md) |
| Assets | [14](14_asset_requirements.md) |
| Event-specific completion surfaces and save contract | [15](15_acceptance_and_completion_contract.md), scenarios in [the acceptance matrix](matrices/acceptance_scenarios.md) |
| State lifecycle and cleanup | [the state matrix](matrices/event_state_and_cleanup_matrix.md) |

## Non-negotiable boundaries

- No free weapon, payload, technology, or special project on entry or through any posture.
- No source event fired, advanced, or recorded by the program.
- Exactly equal project selection among unique eligible providers.
- No convention relief for thermonuclear use, Final Silence, doomsday releases, atrocity, or cover-up sources.
- No whole-world daily or monthly country scan, because later work iterates registered members, the active agenda, and project participants.
- Evolution activation changes no Chaos.
