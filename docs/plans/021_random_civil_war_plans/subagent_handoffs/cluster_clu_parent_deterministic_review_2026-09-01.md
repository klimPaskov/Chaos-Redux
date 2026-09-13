# Event 021 CLU Parent Deterministic Review

Date: 2026-09-01

This is an owner-run deterministic source review of CLU-01 through CLU-05. It is not an independent probability-auditor certificate and does not claim a live engine sequence.

## Defects found and repaired

Event 021 was correctly registered as Wars row 1003 at Medium severity and Chaos tier 1, but a stale second registration also placed it in Domestic Unrest at Low severity. That duplicate could dispatch Event 021 outside the required Wars collision and pacing contract. The duplicate member row and its unused row-id constant were removed.

The Wars prefire path also did not distinguish Event 004's same-transaction countries from unrelated recent wars. A bounded temporary prefire context now enforces separation only while Event 021 is being prepared as a Wars-cluster member. Calm World and Gathering Storm exclude both Event 004 countries. Rising Chaos and higher may reuse Event 004's target only when it has live external-war evidence and Fractured-or-worse pressure. The Event 004 aggressor remains reserved at every tier.

## Named fixtures

| Fixture | Current deterministic result |
| --- | --- |
| CLU-01 | With enough candidates at Calm World, Event 021 rejects both `random_war_recent_aggressor` and `random_war_recent_target`; Fury actors are rejected by the normal Event 021 target predicate. The three primary roles therefore remain disjoint. |
| CLU-02 | At Rising Chaos or higher, Event 021 may reuse only Event 004's target, and only with live external-war evidence plus Fracture Pressure at or above the centralized Fractured threshold. This preserves an intentional, pressure-backed overlap rather than a generic collision. |
| CLU-03 | `random_civil_war_country_can_be_target` rejects `fury_actor` and `fury_recent_actor`; Fury creates the actor before the delayed Event 021 member prepares its target. A new Fury actor is therefore unavailable to Event 021 in the same transaction. |
| CLU-04 | The Event 006 package finder scans the complete package registry in order, admits only a dormant content-attested carrier with a valid host-owned anchor, and continues after occupied tags or invalid anchors. It stops after the first admitted package, so it rerolls within the package registry or omits the Event 006 route without duplicating a tag or character. |
| CLU-05 | Event 021 is an optional Wars row. A zero-target prefire records `no_eligible_target`, returns no dispatch, and the pending-member processor records a runtime skip while continuing the batch. The cluster-level pacing update occurs once at successful cluster activation, not once per member. |

## Pacing and presentation

`on_event_cluster_global_pacing_update` is called once when the synchronous trigger member commits the cluster. Every member fires under `event_cluster_member_fire_context`, which suppresses member-level pacing. Event 021 skip reasons are stored in the Event 021 snapshot arrays and resolved by `GetEvent021LogClusterSkipReason` to the existing player-facing localisation.

## MCP and local evidence

The installed event analyzer returned partial helper-projection lints for all three changed source surfaces:

- Cluster source: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7acf354683f5889ecae33c3f605a316b09748406faf6c7f8135c2052178b95ee/b9e0c3eeff578659c9e834b8709e1c42c4bfa77b84e4e12485e12c5af19ba52d/event-lint-b8b928ac6119.json`
- Event 021 parent effects: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/38ccede799a6d28de4a887b95b0ee0a6b5add83d06788ade1a503506b7c95ac4/2448e989e552a2c48307f53c420d353fd9d48f2b2d9d025c78c943138fbca2ed/event-lint-b8b928ac6119.json`
- Event 021 triggers: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b34b0aef8a32378b4afdceb79b9428685337dec42034b7ad9a1ed96895457e53/6ffc783f9a7d8d0295878755aab7cdbacf548d048b2972676a4d538e41c6e9f5/event-lint-b8b928ac6119.json`

The analyzer still defers workspace-wide helper projection, so these artifacts are supporting structural evidence rather than runtime proof. The four touched Clausewitz files retain balanced braces.

## Remaining boundary

The Event 021 release gate remains deliberately closed. A live cluster sequence, independent probability certification, and the separate Event 006 additional-front implementation remain required before completion.
