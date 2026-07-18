# Event 019 achievement completion pass handoff

## Scope and outcome

This pass completed the achievement-owned registry, localisation, exact ledger tracking, narrow Event 019 source hooks, and player-facing documentation for all eleven stable Event 019 custom-achievement identifiers. Achievement logic reads authoritative generation, lot, unit, claimant, derivative, rail, and scenario records rather than country-level approximations.

Four exact-division battle achievements remain deliberately hidden and unawarded because the documented HOI4 combat callbacks do not expose the complete same-battle proof tuple. No fallback or proxy award was introduced.

## Stable identifiers

- `019_infantry_spawn_every_rifle_accounted_for`
- `019_infantry_spawn_one_battalion_wonder`
- `019_infantry_spawn_the_army_has_voted`
- `019_infantry_spawn_order_from_noise`
- `019_infantry_spawn_combined_arms_accident`
- `019_infantry_spawn_no_room_on_the_train`
- `019_infantry_spawn_borrowed_future`
- `019_infantry_spawn_three_false_apocalypses`
- `019_infantry_spawn_barracks_of_babel`
- `019_infantry_spawn_quiet_demobilisation`
- `019_infantry_spawn_every_barracks_a_front`

## Achievement-owned files

- `common/achievements/chaos_redux_achievements.txt`
  - registers all eleven identifiers;
  - keeps the four blocked battle achievements hidden;
  - binds each identifier to its exact completion trigger and tooltip.
- `common/script_constants/019_infantry_spawn_achievement_constants.txt`
  - centralizes generation, control, congestion, battle-significance, integration, survival, and bounded continuity-pulse thresholds.
- `common/scripted_triggers/019_infantry_spawn_achievement_triggers.txt`
  - owns the eleven completion contracts, exact claimant identity, technology-gate tests, rail continuity, and durable scenario history.
- `common/scripted_effects/019_infantry_spawn_achievement_effects.txt`
  - owns generated-division identity history, pre-technology gate pairs, sanctioned-edit disqualification, closeout audits, claimant and derivative proof, rail proof, scenario proof, and the deliberately unwired exact battle bridge.
- `common/on_actions/019_infantry_spawn_achievement_on_actions.txt`
  - records exact capitulation and annexation outcomes;
  - rejects peaceful annexation as claimant major-war proof;
  - reevaluates the defeated country immediately so capitulation disqualification is durable.
- `localisation/english/chaosx_achievements_l_english.yml`
  - supplies one name, one description, and one exact tooltip for every identifier.
- `docs/achievements/019_infantry_spawn_achievements.md`
  - documents all eleven contracts, exploit protections, the exact battle limitation, and the custom-achievement icon convention.

## Narrow source hooks

- `common/scripted_effects/019_infantry_spawn_generation_effects.txt`
  - registers each exact generated division after its authoritative ledger row and obligations exist.
- `common/scripted_effects/019_infantry_spawn_management_effects.txt`
  - deduplicates integrated random lots;
  - disqualifies exact units before standardization unlocks their template;
  - marks both emergency-integration routes;
  - records only successful full supervised teardown;
  - marks teardown failure;
  - evaluates the exact row at generation closeout;
  - starts, verifies, and fails the exact rail proof at its owning mission branches.
- `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt`
  - freezes the exact promoted claimant after takeover.
- `common/scripted_effects/019_infantry_spawn_claimant_effects.txt`
  - marks the claimant revolt source before revolt setup.
- `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt`
  - marks the former parent country with derivative-revolt history only after a valid derivative identity initializes.
- `common/scripted_effects/019_infantry_spawn_pulse_effects.txt`
  - calls the bounded country-scoped achievement continuity pulse before ordinary-versus-derivative routing, so a scenario origin that becomes a derivative still records continuity.
- `common/scripted_effects/019_infantry_spawn_core_effects.txt`
  - reduces only an active rail, claimant-survival, or scenario-origin achievement attempt to a one-day country-scoped delayed pulse; ordinary Event 19 and derivative pulses retain their existing cadence.
- `common/scripted_triggers/019_infantry_spawn_triggers.txt`
  - keeps the existing Event 19 pulse scheduled while rail or claimant-survival proof is pending and accepts the scenario-owned origin pulse flag even when the initiating country is no longer an ordinary Event 19 participant.

## Exact scenario interface

`infantry_spawn_achievement_register_scenario_launch` freezes the initiating country, type, intensity, and survival timer. The scenario implementation calls it only after valid launch inputs are frozen.

Scenario military victory is gated by `infantry_spawn_scenario_launch_has_no_surviving_hostile_actors`. That trigger reads the scenario-owned frozen launch serial and actor roster, requires a nonzero hostile-actor total, excludes only the takeover origin actor, and treats an exact actor as defeated only when capitulated or gone. Defeating the first of several actors cannot award the achievement.

The scenario owns `infantry_spawn_scenario_origin_pulse_active`. Achievement tracking clears that flag on roster victory, survival completion, capitulation, terminal World End, intensity change, or observed country switch, so a completed or invalid attempt cannot leave a permanent pulse behind.

## Exploit and continuity protections

- Ready flags do not override current or durable disqualifiers.
- Claimant leadership interruption and country capitulation permanently cancel the survival and major-victory proof paths.
- Zombie, ghost, and golem derivative defeats are frozen once per family and must use three distinct exact derivative country identities.
- Parent-event actors cannot satisfy derivative flags.
- Rail proof uses the exact origin state and rechecks a live capital-to-origin railway at start, mission completion, pulse, and generation closeout.
- Emergency recognition and emergency integration both disqualify rail and quiet-demobilisation proofs.
- A failed or broken rail proof clears its active continuity flag; a later mission begins a fresh exact attempt instead of leaving a permanent daily pulse.
- Successful supervised teardown is recorded before the exact closeout row resolves; failed or specialist-only teardown cannot count.
- Scenario proof rejects capitulation, terminal World End, intensity change, and player-country discontinuity.
- Scenario launch marks forced history, so it cannot be reused to unlock ordinary Event 19 achievements.

## Meaningful validation performed

- All eleven achievement identifiers have exactly one registry definition, one `_NAME`, one `_DESC`, one completion-trigger definition, and one achievement-tooltip binding.
- Exactly four Event 19 registry entries are hidden, matching the four blocked battle achievements.
- The exact battle recorder has no external caller; none of the four battle-ready flags can be set by a weaker callback.
- Closeout evaluation runs while the just-resolved generation UID and ledger row are still available.
- The three derivative-family branches symmetrically reject already-recorded country IDs regardless of defeat order.
- The scenario victory branch requires the complete frozen hostile launch roster to be defeated.
- The achievement on-action file adds no daily, weekly, monthly, all-country, or world pulse. Rare active continuity attempts use only the existing country-delayed Event 19 pulse at a one-day cadence.
- Localisation remains UTF-8 with BOM.

An optional `hoi4.event_inspect` lint attempt could not create its linked artifact because the shared artifact store reported `ARTIFACT_STORAGE_LIMIT`. This was a tooling-storage failure, not evidence about the source, and no completion claim relies on that tool.

## Simplifications, omissions, and blockers

### Exact battle bridge

The following achievements remain hidden and cannot currently award:

- `019_infantry_spawn_one_battalion_wonder`
- `019_infantry_spawn_combined_arms_accident`
- `019_infantry_spawn_borrowed_future`
- `019_infantry_spawn_barracks_of_babel`

The documented `on_army_leader_won_combat` callback exposes the unit leader and owner country, not the exact participating division, enemy-strength ratio, combat duration, and enemy casualties from the same battle. No documented installed iterator closes that gap. The shared effect `infantry_spawn_achievement_record_exact_division_significant_victory` remains available for a future exact bridge and requires all four inputs before it can set any ready flag.

### Manual template substitution

Every sanctioned Event 19 standardization path disqualifies the exact lot before the template unlocks. HOI4 script does not expose a reliable callback for an undetected manual switch to a separately cloned superset template, so the implementation does not claim to observe that unsupported path.

### Sub-day continuity transitions

HOI4 exposes no generic exact callback for every country-leader replacement, player console tag switch, or railway interruption. The implementation calls explicit Event 19 invalidation sources and samples only active attempts with a bounded one-day country pulse. A removal and restoration, tag switch away and back, or rail break and repair entirely between two daily samples is not script-observable and therefore remains a false-positive risk. No global daily scan was substituted.

### Claimant revolt dependency

At this handoff snapshot, the achievement disqualifier called an undefined
parent-owned claimant-revolt effect. Parent integration subsequently removed
that invalid call, closed natural revolt eligibility with an explicit false
capability trigger, and clears retained warnings without revolt or achievement
credit. Exact recorded-formation transfer remains an Event 19 completion
blocker, but the live source no longer contains an undefined helper.

### Dormant future disqualifier hooks

The helpers for debug completion and forced parent-event merge remain unwired because the current Event 19 implementation has no such source path. Any future source must call its helper at the source; no heuristic scan was added.

## Assets

The companion achievement asset pass owns the eleven independent 64-by-64 DDS triplets and `docs/assets/019_infantry_spawn/manifest.md`. At this handoff, all 33 DDS files are present: filenames exactly match the stable identifiers and their `_grey` and `_not_eligible` suffixes, every header reports 64 by 64, and every triplet has three distinct hashes. The asset subagent is still writing the final manifest and its hash table; that manifest remains a cross-surface dependency.

## Cross-surface dependencies at handoff

- Scenario launch implementation is still in progress. It must freeze and copy `infantry_spawn_scenario_launch_serial`, populate `global.infantry_spawn_scenario_actor_countries`, maintain a nonzero hostile-actor total, set `infantry_spawn_scenario_origin_pulse_active` on the initiating country, and call `infantry_spawn_achievement_register_scenario_launch = yes` after type/intensity freeze. The achievement-side trigger and terminal cleanup are already wired to that contract.
- The companion asset subagent must finish `docs/assets/019_infantry_spawn/manifest.md`; the final DDS triplets themselves are already present and validated as described above.
- Exact recorded-formation transfer remains approval-blocked. Natural revolt
  eligibility is fail-closed and grants no achievement credit while the engine
  contract is unavailable.

## Git handoff

No subagent commit was created. The shared worktree contains simultaneous parent and sibling changes outside this scope, so the parent agent must review and commit the completed plan without staging unrelated files.
