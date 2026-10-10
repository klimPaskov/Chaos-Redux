# Event 011 Secret Alliance Planning Package

This package is the retained source design for Chaos Redux Event 011, **Secret Alliance**.
The event is implemented; this package explains the intended design, and source plus the owner records below decide what the game currently does.

## Status and authority

- Accepted source design: the five spec parts under `specs/` and the matrices under `matrices/`.
  The July 2026 improvement-loop resolution (`docs/plans/011_secret_alliance_plans/011_secret_alliance_improvement_resolution.md`) records the accepted addendum as fully disposed, and the parent's final completion audit (`docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md`, FINAL CLEAN at the July static freeze) is the acceptance record for the implementation of this design.
- Explicit user rule: any active pact member entering a normal hostile war with the fixed target reveals the pact immediately and calls every valid active member into that war (Part 4, "Hostile war reveal").
- Parent acceptances recorded after the July freeze (`docs/plans/011_secret_alliance_plans/agent_decisions_2026-10-05.md`):
  - every paid action charges at most four resource types and shows at most three amounts inline, with the full bundle on hover;
  - phase and irrelevance gates keep at most six decision rows visible, with one accepted seven-row exception after border routes are mapped (2026-10-06);
  - existing faction leaders stay outside the valid-member roster, so the hostile-war reveal moves followers but never transfers another faction's leader (2026-10-06).
- Parent acceptance on 2026-10-08 of the Part 5 Event 008 and Event 012 connection rules (`docs/plans/repo_cleanup/specification_improvements_2026-10-08/handoffs/007_012.md`).
- Current implementation summary: `docs/events/011_secret_alliance/overview.md`.
- Current release state: the October 2026 release repairs are implemented in source, while current event-chain and GUI render evidence, post-gate probability certification, and asset provenance remain open in the October decision record.
  Numbers in this package are design intent; `common/script_constants/011_secret_alliance_constants.txt` and the file-local `@` values in `common/decisions/011_secret_alliance_decisions.txt` and `common/ideas/011_secret_alliance_ideas.txt` are the tuning authority.

The event remains a Minor Fire-Once event.
Its core identity is a hidden anti-player coalition that begins with three countries, recruits additional members, interferes with the target country, and becomes a real faction when secrecy fails or the coalition enters its final escalation.

## Recommended reading order

1. `specs/011_secret_alliance_spec_part_1_core_and_hidden_pact.md`
2. `specs/011_secret_alliance_spec_part_2_progression_and_evolutions.md`
3. `specs/011_secret_alliance_spec_part_3_counterplay_and_decisions.md`
4. `specs/011_secret_alliance_spec_part_4_reveal_war_and_scenario.md`
5. `specs/011_secret_alliance_spec_part_5_ai_presentation_and_acceptance.md`
6. The matrices under `matrices/`
7. The research notes under `research/`
8. The historical build prompts under `prompts/` (fulfilled; never rerun them as open work)
9. The review and architecture handoffs under `handoffs/`

## Design boundaries

The event uses existing countries.
It does not create a new country tag and it does not replace national focus trees.
The coalition is event-owned and is expressed through hidden membership, operations, decisions, ideas, AI strategies, and a reveal faction.
This keeps the event compatible with any player country and ideology and prevents a minor event from overwriting unrelated national identities.

Final localisation is authoritative over the working labels in this package.
The reveal super-event (slot 73, audio ID 43) is documented in `docs/super_events/011_secret_alliance/research.md`.

No date gate exists in the design or in source.
Evolutions open by Chaos tier and dynamic pacing, which already satisfies the 10 Oct 2026 user rule that dates only influence weights while gameplay conditions decide.

## Package status

The source reading, design, research, architecture, decision and mission review, localisation review, asset routing, improvement-loop review, and source-package completion review are represented in this package.
Their planning-era pending instructions are fulfilled or superseded and must not be rerun as open work.
The planning-era specialist passes were applied manually because the planning environment had no subagent spawn interface; `handoffs/subagent_role_application.md` records that limitation.
Current subagent routing lives in [chaos-redux-subagents](../../../.claude/skills/chaos-redux-subagents/SKILL.md).

## Verification files

- `source_inventory.md` records the original supplied source files and their reading status (historical provenance).
- `manifest.md` records the original 33-file package and its historical hashes; those hashes are not current checksums.
- `handoffs/documentation_state.md` maps each surface to its current owner record.
- `handoffs/completion_audit.md` keeps the source-package audit findings and their resolutions.
- `handoffs/improvement_loop_closure.md` records the depth and anti-bloat conclusion.

## Open questions

Each item below is proposed (spec audit 2026-10-10) or unresolved; none is accepted design until the user or parent records acceptance.

1. **World threat direction (proposed, conflicts with Part 5's original direction).**
   Part 5 originally let a revealed pact become a source of the shared world-threat state; source has no such hook.
   The [world-threat framework](../../systems/world_threat_mechanic.md) exists for existential threats and tells other systems to calm ordinary geopolitics while `world_in_threat` is set.
   Proposal: Event 011 becomes a consumer, not a source.
   While `world_in_threat` is set, `secret_alliance_operation_interval` in `common/mtth/011_secret_alliance_mtth.txt` gains a lengthening factor, new invitations pause, and the pact AI defers a controlled reveal; the hostile-war reveal rule is unchanged.
   The framework owner changes nothing, and the original source direction would be rejected.
2. **Pacts cluster (unresolved, cluster-system owner).**
   The cluster catalogue (`docs/systems/event_system/event_clusters.md` and the clusters CSV export) lists a Pacts cluster whose only member is Event 011 at Chaos level 3, while the runtime registry in `common/script_constants/event_cluster_constants.txt` and `common/scripted_effects/chaosx_event_cluster_effects.txt` registers no Pacts cluster and the Event 011 overview says the event belongs to no cluster.
   A one-member cluster cannot change pacing beyond the ordinary fire-once event, so the proposal is that the cluster owner either adds a second genuine pact event or retires the row.
   Event 011 needs no cluster-specific code either way, because cluster dispatch must use the ordinary fireability gates (fixed target, three valid minor founders, drained callbacks).
3. **Migration options listed for Event 011 (proposed disposition for the Famine and Migration owner).**
   [Famine and Migration Part 7](../famine_and_migration_system_specs/famine_and_migration_system_spec_part_7_cross_system_connections.md) keeps four Event 011 options open: sponsoring a refugee route, consuming proven survivor intelligence, exploiting displacement politically, and closing borders to protect secrecy.
   Proposal: reject secrecy-border closure and political displacement exploitation, because no Event 011 rule reads population movement and both would be effects without consequence; displacement from the coalition war already belongs to Migration's ordinary front and control-change handling.
   Keep survivor intelligence unresolved: it would be justified only if Migration exposes an arrival receipt naming the origin country, which Event 011 could turn into one `human`-class clue through its existing source-aware clue path.
4. **Pre-fire Evolution II founding (proposed: keep the implementation).**
   Part 2 asked for a major-led opening in which an eligible major founds the pact.
   Source opens with three minor founders, higher starting values, and a scheduled sponsor approach (`secret_alliance_open_evolution_ii` calls `secret_alliance_schedule_sponsor_approach`) that the major can refuse on strategic grounds.
   Proposal: accept the implemented behaviour, because it honours Part 2's own rule that a major never joins only because a slot opened.
5. **Event 052 adapter (accepted and queued in the Event 052 package, adapter shape proposed).**
   The [Event 052 interaction matrix](../052_intel_leaked_specs/matrices/052_intel_leaked_cluster_and_interaction_matrix.md) owns one bounded Evidence or Pact Readiness change per leak sequence.
   Proposal: Event 011 exposes one public adapter that registers an external clue through the same source-aware path as `secret_alliance_register_operation_clue`, so a leak about a member cannot farm a class that the dossier already holds, and a leak about the target adds readiness once.
6. **Alertness threshold (proposed source cleanup).**
   The `high_alertness_factor` modifier in `secret_alliance_operation_interval` compares Pact Alertness against `secret_alliance_band.preparedness_guarded`.
   Proposal: give Alertness its own band constant so tuning Preparedness never silently retunes operation pacing.

## Changelog

- 2026-10-10 spec audit
  - Rewrote the status section to name the acceptance records, the explicit hostile-war user rule, and the October parent acceptances (four-resource cost ceiling, six-row visibility with one seven-row exception, faction-leader participant boundary), and stated that constants are the tuning authority.
  - Replaced the ignored `.agents/skills/` link with the canonical `.claude/skills/` path.
  - Reconciled spec and matrix numbers with source: Evolution II membership 6 to 8, Total Chaos naming for tier 4, three-founder pre-fire openings, scenario intensity rosters, mission timeouts, confidence band labels, and the accepted cost and visibility limits.
  - Recorded dispositions for every Part 5 cross-event hook and documented the shared systems Event 011 deliberately does not feed (Chaos Meter packet, Deaths, Condemnation, Famine and Migration, camps, CBRN) with the source reason.
  - Condensed duplicated hash tables, evidence tables, and lifecycle notes in `handoffs/documentation_state.md` and `handoffs/completion_audit.md` to pointers; git history keeps the originals.
  - Added the open questions above; none changes accepted design.
  - Reviewed the counter-network panel's value set (exact Evidence and Preparedness, two broad hidden-state bands, up to three suspect cards, War Pressure at Evolution III, band-only tooltips) and retained it, because each value gates a decision or reveal outcome.
