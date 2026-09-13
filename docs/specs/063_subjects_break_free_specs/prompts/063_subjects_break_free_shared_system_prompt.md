# Shared system prompt: Event 063 Subjects Break Free

Use `chaosx_scripted_system_architect` and `chaosx_repo_explorer` to design and implement the neutral liberation-origin contract and the Event 063 release transaction. Follow `AGENTS.md`, `chaos-redux-events`, `CHAOS_REDUX_MECHANICS`, `chaosx_dynamic_triggers`, and `chaosx_dynamic_effects`.

Read:

- `docs/specs/063_subjects_break_free_specs/specs/063_subjects_break_free_spec_part_1_core.md`
- `docs/specs/063_subjects_break_free_specs/specs/063_subjects_break_free_spec_part_3_network_and_pact.md`
- `docs/specs/063_subjects_break_free_specs/specs/063_subjects_break_free_spec_part_4_evolutions_clusters_and_connections.md`
- `docs/specs/063_subjects_break_free_specs/diagrams/063_subjects_break_free_flow.md`
- `docs/specs/063_subjects_break_free_specs/quality/063_subjects_break_free_acceptance_matrix.md`

## Ownership rule

The neutral layer may answer cross-event questions and store shared provenance. It must not perform owner-specific releases.

Event 063 owns existing-subject selection, independence, settlement, cooldowns, and the Event 063 Liberation Pact.

Event 006 owns its release ledger, country candidates, state anchors, country packages, formables, and congress systems.

Event 005 owns Soviet republic and splinter release, authority, successor packages, Free Republics' League, and terminal collapse behavior.

Do not write Event 006 or Event 005 private variables from an Event 063 helper. Do not move Event 063 country release into the Event 006 ledger.

## Frozen transaction

Implement one Event 063 transaction generation per firing.

Required phases:

1. build a complete valid subject pool
2. freeze snapshots
3. determine target count
4. select without replacement
5. reserve all selected subjects and relations through the Liberation Release Coordinator
6. prepare frozen fallbacks
7. release valid countries in place
8. resolve settlement
9. write shared origin data once
10. publish and log
11. clear temporary state

The first release cannot change the later selection pool. Before the first release, failed reservations can use frozen fallbacks. After execution begins, a late invalid candidate is skipped and earlier releases remain.

Every selected subject needs one reservation record, one completed-release guard, one origin-write guard, and one cleanup state. Save and reload must not repeat a release or origin write.

## Candidate validity

Keep Event 063 owner-specific validity with Event 063. Use neutral dynamic triggers only for stable cross-system classifications, such as ordinary country eligibility or active liberation-origin status.

A candidate must be an existing valid subject with territory and a safely removable subject relation. Exclude countries held by another protected release, split, annexation, civil-war, or replacement transaction. Exclude actual nonhuman and incompatible special actors through the approved shared classifier.

Unusual autonomy types should be blocked by owner-provided compatibility where needed. Do not maintain a broad hardcoded autonomy blacklist in the neutral registry.

## Shared liberation-origin record

Store or expose the minimum neutral contract needed by several owner systems:

- first liberation origin
- first liberation date
- latest liberation event
- latest liberation date
- former overlord or host for latest liberation
- latest separation mode
- generation count
- active or suspended network state
- Event 063 Pact membership and partner status through an Event 063-owned adapter

First origin is write-once. Latest origin changes after a later valid liberation. Becoming a subject suspends active network status without erasing history. Country loss clears active status. A valid restoration and later independence can reactivate the record.

Provide neutral queries for:

- valid liberation origin
- currently active independent network state
- compatibility for recognition or support
- eligibility for Event 063 Pact member, partner, or observer review
- whether a one-time cross-event opportunity has already been consumed

Compatibility queries can use live wars, claims, subject status, faction state, and special-country classification. Keep event-specific thresholds and decision rules with their owner.

## Pact ownership

The Liberation Pact is Event 063-owned. Its faction, founder, roster, cohesion, leadership, invitations, partners, censure, suspension, and dissolution should remain in Event 063 files or a clearly named Event 063 system file.

The neutral registry only exposes eligible origins and active status. It does not merge or replace Event 006 congresses or the Event 005 Free Republics' League.

## Cluster coordination

Register Event 063 as a Medium member of Liberations, Cluster ID 2. During a cluster firing, create one shared coordinator generation before member release effects execute.

Each member:

- builds its own candidate set
- reserves its own relations, tags, anchors, or states
- receives collision results before release
- executes its own effects
- records its own event history and provenance

The cluster records one pacing event and one joint summary. Event 063 must skip cleanly when no valid subject exists.

Domestic Unrest has no stable ID in the supplied catalog. Do not guess one. Add secondary integration only after a real registry row exists.

## Performance and cleanup

Avoid permanent daily whole-world scans. Update active records through owner events, subject-status transitions, country loss, war and peace outcomes, faction changes, decisions, and bounded periodic maintenance where no event hook exists.

Every array and parallel registry needs documented alignment, initialization, cleanup, and recovery after missing or stale countries. Add debug output only through the existing opt-in logging pattern.

## Required validation

- transaction with one, several, and large subject pools
- reservation conflict with Event 006 and Event 005
- candidate invalidation before and after the first release
- save and reload during a pending human settlement
- Event 006 first origin followed by Event 063 latest origin
- Soviet successor origin followed by Event 063 latest origin
- subject suspension and later reactivation
- country annexation and restoration
- Pact partner state for a factioned country
- cluster firing with all three liberation members
- cluster firing with Event 063 ineligible
- cleanup of every temporary transaction and registry row
- absence of writes into another event's private ledger

Provide a shared ownership table, helper inventory, caller list, collision test results, save-compatibility notes, and a clear report of any owner contract that could not be kept.
