# Event 016 Host-Context Reaction Tranche Addendum

## Status and recommendation

The previous context and first Prototype persistence addendum is resolved in implementation commit `be7f21fe5`.

One further bounded expansion is useful before closure: three career-once report incidents that make the first successful projects provoke local, political, and foreign reactions.

This tranche adds no evolution, cluster, country, focus tree, decision category, scripted GUI, art, animation, or 3D work.

## Event map

| ID | Gate | Design purpose |
| --- | --- | --- |
| `chaosx.nr16.7` | First resolved Prototype report and a valid primary facility | The laboratory district demands terms from the Directorate |
| `chaosx.nr16.8` | Second resolved Prototype report | The host regime decides who legally controls Kruger's working methods |
| `chaosx.nr16.9` | First detected foreign operation resolved after at least one Prototype report | The host answers a named foreign actor without creating a generic diplomacy ladder |

All three use `GFX_report_event_016_brilliant_scientist_directorate_dossier` and remain ordinary report events outside the event log and evolution system.

## Incident `.7`: primary-facility compact

The description names the primary facility state and varies by `brilliant_scientist_context_public_science`, `brilliant_scientist_context_strategic_security`, `brilliant_scientist_context_industrial_mobilization`, or `brilliant_scientist_context_distributed_research`.

The three options use working labels only:

- Civic compact: set state flag `brilliant_scientist_primary_facility_civic_compact`, lower Grievance by one tuning step, and raise Exposure by one tuning step. The accident consequence calculation reduces severity by one step in this state.
- Restricted district: set state flag `brilliant_scientist_primary_facility_restricted_district`, lower Exposure by one tuning step, and raise Grievance by one tuning step. Foreign operation success against this host receives a one-step penalty while this remains the primary facility.
- Industrial charter: set state flag `brilliant_scientist_primary_facility_industrial_charter`, raise Project Capacity and Dependence by one tuning step, and raise accident pressure by one step while this remains the primary facility.

Store the selected result on Kruger with exactly one of `brilliant_scientist_personal_reaction_civic_compact`, `brilliant_scientist_personal_reaction_restricted_district`, or `brilliant_scientist_personal_reaction_industrial_charter`.

## Incident `.8`: custody of the method

Snapshot the family from the second resolved report in `brilliant_scientist_reaction_custody_family` before scheduling the event.

The description varies by democratic, communist, fascist, and non-aligned host context, but no ideology loses an option.

The three options use working labels only:

- Public trust: set `brilliant_scientist_reaction_public_trust`, add the snapshot family to `brilliant_scientist_reaction_public_trust_families`, lower Dependence and Grievance by one step, and raise Exposure by one step.
- Executive reserve: set `brilliant_scientist_reaction_executive_reserve`, add the family to `brilliant_scientist_reaction_executive_reserve_families`, raise Mandate and Dependence by one step, and lower Exposure by one step.
- Patent pool: set `brilliant_scientist_reaction_patent_pool`, add the family to `brilliant_scientist_reaction_patent_pool_families`, raise Project Capacity and Exposure by one step, and raise accident pressure by one step.

These family arrays are persistent history and later text and AI context only.

They do not publish a family, advance a stage, grant independent replication, or repeat the Prototype reward.

Store the selected result on Kruger with exactly one of `brilliant_scientist_personal_reaction_public_trust`, `brilliant_scientist_personal_reaction_executive_reserve`, or `brilliant_scientist_personal_reaction_patent_pool`.

## Incident `.9`: a foreign actor takes notice

Call this event from `brilliant_scientist_foreign_record_resolution` while the existing regular targets `brilliant_scientist_foreign_operation_actor` and `brilliant_scientist_foreign_operation_host` are still valid.

Do not search every country and do not save another global target.

The three options use working labels only:

- Controlled exchange: available only when actor and host are not at war and the resolved operation was neither extraction nor assassination. Copy the host's selected live family into the actor's `brilliant_scientist_foreign_selected_project_family`, call existing `brilliant_scientist_foreign_grant_selected_family_theory`, add a positive bilateral opinion modifier, raise Exposure by one step, and lower Grievance by one step.
- Private warning: add a smaller negative bilateral opinion modifier, lower Exposure by one step, and set actor flag `brilliant_scientist_foreign_reaction_warned` so later foreign operation AI weighs covert action more cautiously.
- Public accusation: add a larger negative bilateral opinion modifier, raise Mandate and Exposure by one step, and raise the actor's foreign-interest score by one step.

Store the result on the host as exactly one of `brilliant_scientist_reaction_controlled_exchange`, `brilliant_scientist_reaction_private_warning`, or `brilliant_scientist_reaction_public_accusation` and mirror it on Kruger with the `brilliant_scientist_personal_` prefix.

If no qualifying detected operation occurs, `.9` does not fire.

There is no generic country substitute.

## Exact scheduling and persistence contract

Add these helpers:

- `brilliant_scientist_try_schedule_primary_facility_reaction`
- `brilliant_scientist_try_schedule_custody_reaction`
- `brilliant_scientist_try_fire_foreign_reaction`
- `brilliant_scientist_clear_host_reaction_pending_state`
- `brilliant_scientist_copy_host_reaction_history_to_recipient`
- `brilliant_scientist_clear_host_reaction_state_on_terminal_exit`

Use these scheduling flags:

- Host flags: `brilliant_scientist_reaction_facility_pending`, `brilliant_scientist_reaction_facility_resolved`, `brilliant_scientist_reaction_custody_pending`, `brilliant_scientist_reaction_custody_resolved`, `brilliant_scientist_reaction_foreign_pending`, and `brilliant_scientist_reaction_foreign_resolved`.
- Kruger character flags: the same six names with the `brilliant_scientist_personal_` prefix.

Call the `.7` and `.8` scheduling helpers at the end of both `brilliant_scientist_record_breakthrough_public` and `brilliant_scientist_record_breakthrough_classified`.

Use named constants under a new `brilliant_scientist_host_reaction_delay` category for the short delays and named constants under `brilliant_scientist_host_reaction_delta` for every variable, accident, foreign-success, foreign-interest, and AI-weight adjustment.

On an ordinary transfer, move unresolved `.7` or `.8` scheduling ownership to the recipient and clear the old host's pending flags.

Resolved state consequences remain on the state and old host, while Kruger's character receipt prevents replay.

On KRG formation, cancel unresolved host-reaction incidents and retain only the character history flags.

On permanent removal or world end, clear all pending host and character flags and `brilliant_scientist_reaction_custody_family`.

## AI contract

Every option uses dynamic `ai_chance` factors.

- Democratic, public-science, low-war hosts prefer the civic compact, public trust, and controlled exchange.
- Fascist or communist hosts at war with a secret Directorate prefer the restricted district, executive reserve, and private warning.
- High Dependence or high Grievance penalizes choices that increase the same pressure.
- High Exposure strongly favors restricted handling and private warning.
- Low Project Capacity with industrial mobilization favors the industrial charter or patent pool unless accident pressure is already high.
- Biological weapons, alien arms, temporal science, and singularity families heavily penalize controlled exchange.

Probability validation must confirm those orderings with the weighted-logic inspector under at least the five scenarios above.

## Localisation and asset surface

Add title, description, option, trigger-tooltip, and effect-tooltip keys for `.7`, `.8`, and `.9`.

Descriptions must expose the primary state name for `.7`, the snapshot project-family name for `.8`, and the named foreign actor plus operation posture for `.9`.

All new text follows Event 016 report prose and is not a final-localisation deliverable in this plan.

No new DDS or `.gfx` registration is required.

Static dossier art is the intended final surface for these administrative incidents.

No animation is proposed, and no transform-only animation or visual fallback is accepted.

Event 016 3D work remains deferred and outside this tranche.

## Acceptance scenarios

1. The first resolved Prototype report schedules `.7` once, scopes the current primary facility, applies exactly one state result, and cannot replay after transfer.
2. The second resolved Prototype report snapshots its family and schedules `.8` once without publishing, advancing, or rewarding that family again.
3. A detected foreign operation resolved after a Prototype fires `.9` against the exact actor through the existing regular event targets.
4. Controlled exchange grants at most Theory knowledge through the existing capped foreign ledger helper.
5. An undetected operation, an operation before the first Prototype, or a campaign with no foreign operation does not manufacture a substitute `.9` target.
6. Ordinary transfer rebinds pending `.7` and `.8` incidents, KRG formation cancels them, and terminal removal leaves no pending flags or custody-family variable.
7. All three events reuse the dossier report asset, remain outside event-log and evolution registration, and create no GUI, focus, decision, tag, animation, or 3D dependency.

## Promotion and closure

If accepted, merge this contract into the Event 016 core and portfolio specs before implementation and mark this addendum promoted.

After this tranche is implemented and audited, broader country-specific incident ladders should be rejected as bloat unless a concrete country package later requires one.

The remaining asset backlog, including bespoke project art and 3D profile work, stays separately queued and does not block this tranche.

## Parent handoff

- Design problem: the Directorate has setup and Prototype governance reports, but its successes do not yet provoke a bounded local, ideological, and named foreign reaction set.
- Proposed expansion: events `.7`, `.8`, and `.9` with exact career-once receipts, transfer behavior, dynamic AI, and existing-system consequences.
- Research basis: MIT Radiation Laboratory mobilization, OSRD university and industrial contracting, Manhattan Project compartmentalization, the Tizard Mission model of bounded technical exchange, and the Franck Report model of scientific political objection as already documented in `016_historical_science_research.md`.
- Implementation surfaces: context events, breakthrough recording helpers, foreign resolution helper, transfer and terminal cleanup, script constants, opinion modifiers, localisation, and the Event 016 specs.
- Prior addendum status: resolved and promoted through implementation commit `be7f21fe5`.
- Open question: none required for implementation. The parent may reject individual option balance values after weighted-scenario inspection without changing the tranche structure.
- Plan status: keep this file in `docs/plans` until accepted, then promote the contract into `docs/specs/016_brilliant_scientist_specs/`.
