# Event 6 Dangerous Super-Event 6002 Architecture Handoff

**Date:** 2026-07-16
**Scope:** Read-only architecture audit for Event 6, Independence Wave
**Reserved runtime identity:** display slot `24`, audio id `6002`
**Dangerous super-event:** **Every Border a Casus Belli**
**Original audit verdict:** **NOT READY for gameplay implementation**
**Parent closeout:** **RESOLVED; the implemented contract in `docs/super_events/006_independence_wave/research.md` is authoritative**

The architecture and bounded call sites are mapped, and the final image/audio packages are ready. Runtime implementation must not begin until the five blocking contracts in [Blocking decisions](#blocking-decisions) are resolved. In particular, the present Event 6 state cannot prove the accepted “immediate coordinated claims” or “aggressive bloc center” conditions without inventing semantics, and no safe policy currently exists for player-scoped audio or a busy shared super-event display.

No gameplay, localisation, interface, asset, audio, or spreadsheet file was edited during this audit. Super-event `6001` remains blocked and untouched.

> Parent resolution, 2026-07-16: the five former blockers and the busy-window
> policy were resolved after this read-only audit. Post-commit real claims,
> exact league leadership, a transaction-bound scenario war batch, a dedicated
> league-sponsorship history counter, and the existing shared FIFO now provide
> the required proof. Future-tense statements below are retained as historical
> audit evidence and are superseded by the canonical implementation note.

## Authorities reviewed

The accepted design authority is:

- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md`, especially the dangerous-milestone contract at lines 570–614 and the scenario exclusions at lines 794–800.
- `docs/plans/006_independence_wave_plans/super_event_research/006_super_event_text_verification.md`, lines 123–137.
- `docs/plans/006_independence_wave_plans/super_event_research/006_super_event_audio_verification.md`.
- `docs/assets/006_independence_wave/super_events/audio/production_manifest.md`.
- `docs/assets/006_independence_wave/generated_event_scenes_manifest.md`, entry `ASSET-006`.

The audit also followed `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, and `chaos-redux-super-events`; the required offline wiki core, localisation, interface, scripted-GUI, music, and sound pages; vanilla script-concept, script-constant, effects, triggers, dynamic-variable, localisation, collection, music, and sound documentation; and bounded vanilla super-event/audio precedents.

The accepted dangerous milestone is a global-alarm outcome reached through **any one** of five eligible packages:

1. a radical league adopts an offensive charter and reaches sufficient membership and military strength;
2. a high-chaos ten-country wave begins with several armed or radical governments and immediate coordinated claims;
3. several Event 6 countries launch synchronized wars against their former hosts;
4. a hidden high-chaos formable becomes the center of an aggressive bloc;
5. the league sponsors enough new breakaways to create a visible cascade.

The accepted exclusions are binding: an ordinary release wave, weak consultative congress, isolated regional formable, routine host war, or ordinary league election must never fire `6002`. A Maximum-intensity scenario may qualify only when the actual package state satisfies one of the five predicates; scenario selection alone is not proof.

## Current runtime inventory

### Existing but inert danger trigger

`common/scripted_triggers/006_independence_wave_triggers.txt:246-257` defines `can_independence_wave_trigger_danger_milestone`, but no source calls it. `independence_wave_danger_super_event_fired` is only read there and is never set.

The current trigger is not the accepted five-package contract. It requires a durable radical league for every case, then accepts either revisionist actions or the global sponsorship count. This conflates packages 1 and 5 and excludes packages 2–4. It also cannot establish that sponsored releases came from league members.

Implementation must replace or refactor this predicate into five independently auditable package triggers and a final OR aggregator. Do not retain its outer durable-radical-league gate around all packages.

### Durable Event 6 state already available

- Active-origin predicate: `is_independence_wave_active_country` in `common/scripted_triggers/006_independence_wave_triggers.txt:9-14`.
- Live former-host pointer: country variable `independence_wave_former_host`, validated by `has_independence_wave_living_former_host` at lines 99–102.
- Active-country registry: `global.independence_wave_active_countries`, with aligned generation entries and active count, maintained in `common/scripted_effects/006_independence_wave_effects.txt:1488-1550`.
- Frozen wave history: `global.independence_wave_presentation_country_count`, `_chaos_band`, `_armed_count`, `_host_count`, `_region_count`, `_date`, and `independence_wave_latest_actor`, committed by `independence_wave_commit_wave_history` in `common/scripted_effects/006_independence_wave_package_planner_effects.txt:837-942`.
- League state: phase, route, leader, members, member count, cohesion, common cause, shared reserve, revisionist actions, and league flags.
- Sponsorship records: published sponsored states plus committed release-side sponsor country/generation data.
- Scenario war state: successful active host-war counter and a per-release `independence_wave_scenario_host_war_active` flag.
- Formable state: method, discovery mode, active/committed flags, and transaction state.

Any scan of `global.independence_wave_active_countries` must still filter every entry through `is_independence_wave_active_country`; cached membership or count alone is not proof of a living Event 6 country.

## Package-to-state mapping

### Package 1 — radical offensive league

**Existing exact witnesses**

- `has_independence_wave_durable_league = yes`.
- `global.independence_wave_league_route = constant:independence_wave_league_route.radical_revisionist`.
- `global.independence_wave_league_member_count >= constant:independence_wave_league.danger_members` (`7`).
- `global.independence_wave_league_common_cause >= constant:independence_wave_league.danger_common_cause` (`75`).
- `global.independence_wave_league_shared_reserve >= constant:independence_wave_league.danger_shared_reserve` (`60`).
- Offensive-charter/operational proof through either `independence_wave_radical_charter_active`, `independence_wave_reclamation_fronts_coordinated`, or the accepted route plus `global.independence_wave_league_revisionist_actions >= constant:independence_wave_league.danger_revisionist_actions` (`3`).

The route and threshold constants are centralized in `common/script_constants/006_independence_wave_mechanics_constants.txt:311-386`. DM-58 coordinates reclamation fronts and increments revisionist actions in `common/decisions/006_independence_wave_decisions.txt:3113-3175`; DM-59 sets the radical charter/route, adjusts the membership array, increments the action count, and applies the final league deltas at lines 3177–3244.

**Required predicate**

`has_independence_wave_6002_radical_offensive_league`

It must require all strength witnesses and one explicit offensive witness. A route label by itself is insufficient if the accepted reading of “adopts an offensive charter” requires an enacted charter; resolve this in Blocking Decision 1.

**Safe bounded evaluation sites**

- End of the complete effects for DM-58 and DM-59, after all counter/array/value mutations (`decisions.txt:3154` and `:3224` boundaries), not in the middle of their transaction.
- End of canonical league mutation helpers that can newly cross the thresholds: formal proclamation, consultative-to-formal upgrade, durable transition, member registration, route mutation, and centralized league-value changes.

The evaluator is idempotent, so it may be called from all these bounded transaction ends. No daily/weekly polling is needed.

### Package 2 — high-chaos ten-country armed/radical immediate-claims wave

**Existing exact witnesses**

- `global.independence_wave_presentation_country_count = 10` after `independence_wave_commit_wave_history`.
- `global.independence_wave_presentation_chaos_band >= constant:independence_wave_chaos_band.totalen_chaos`.
- `global.independence_wave_presentation_armed_count`, derived from the committed plan rows.
- Planner tuning already assigns target `10` plus armed/high-chaos force at chaos tiers 4 and 5 in `common/scripted_effects/006_independence_wave_package_planner_effects.txt:15-55`.
- Each new origin stores force level, origin chaos band, and former host in `common/scripted_effects/006_independence_wave_effects.txt:336-469`.

**State that is not exact proof**

- `independence_wave_open_sovereignty_applied` and `independence_wave_high_chaos_route_revealed` only make the radical-sovereignty route available. They do not prove that the government selected `constant:independence_wave_government_route.radical_sovereignty`.
- The default `independence_wave_host_claim_intensity = 70` is a bilateral pressure value, not proof that a map claim, coordinated claim schedule, or opening ultimatum was created.
- A Maximum-intensity or radical scenario type is not itself an eligible witness.

**Missing witness**

There is no committed ledger for “immediate coordinated claims.” Actual `add_claim_by` effects occur later through individual border decisions, while birth-time route state is initially undecided. The package therefore cannot be implemented faithfully from current state.

After design approval, add an exact frozen witness such as:

- `global.independence_wave_presentation_immediate_claim_country_count`, populated only when a released country received a real opening claim/ultimatum contract; and
- `global.independence_wave_presentation_radical_government_count`, counting selected radical governments only, never route availability.

If the accepted “armed or radical” condition is disjunctive, an armed count can satisfy it without a radical count, but “several” still needs a central threshold.

**Required predicate**

`has_independence_wave_6002_high_chaos_claim_wave`

It should require the committed ten-country history, total-chaos-or-higher band, a centrally defined minimum number of armed/radical governments, and a centrally defined minimum number of certified immediate coordinated claim actors.

**Safe bounded evaluation site**

Immediately after the successful standalone/joint transaction has committed all origins and `independence_wave_commit_wave_history` has frozen the presentation ledger. The standalone success boundary is in `common/scripted_effects/006_independence_wave_execution_effects.txt:590-671`, after its committed state at approximately lines 632–635. Any scenario adapter that adds opening claims must finish before this evaluation.

### Package 3 — synchronized wars against former hosts

**Existing exact witnesses**

`independence_wave_scenario_start_current_host_war` in `common/scripted_effects/006_independence_wave_scenario_effects.txt:795-827`:

- scopes the Event 6 country to its saved former host;
- validates both countries and absence of an existing war;
- declares the host/reconquest war;
- increments `global.independence_wave_scenario_active_war_count` only on successful declarations; and
- sets `independence_wave_scenario_host_war_active` on the released country.

`independence_wave_scenario_start_all_host_wars` at lines 829–834 is bounded to `global.independence_wave_scenario_country_entries`. Scenario type application occurs at lines 976–995 and the committed scenario transaction applies it at approximately line 1221.

**Required predicate**

`has_independence_wave_6002_synchronized_former_host_wars`

It must require a central minimum of distinct active Event 6 aggressor/host pairs that successfully entered war in the same committed scenario transaction. Validate the per-release success flag and living former-host pointer; the aggregate counter alone is insufficient because invalid/already-at-war cases are converted to missions rather than declarations.

**Safe bounded evaluation site**

Immediately after `independence_wave_scenario_start_all_host_wars` / final scenario type application completes, not after each individual war declaration. This preserves the synchronized batch boundary and excludes a routine single host war.

No bounded non-scenario synchronization ledger exists. Supporting emergent wars outside the scenario would require a new Event 6-specific dated ledger and unique-pair accounting at Event 6 war-start helpers. It must not be approximated through a global recurring country scan or generic `on_declare_war` without an Event 6 filter and an approved bounded design.

### Package 4 — hidden high-chaos formable as aggressive-bloc center

**Existing exact witnesses**

- `independence_wave_formable_method = constant:independence_wave_formable_method.hidden_high_chaos_proclamation`.
- Hidden discovery through `constant:independence_wave_formable_discovery.hidden_high_chaos` and its reveal/high-chaos action requirements in `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:34-60`.
- `independence_wave_formable_active` and `independence_wave_formable_committed` country flags.
- `independence_wave_formable_transaction_state = constant:independence_wave_formable_transaction_state.committed`.
- Successful identity/integration commit in `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:1345-1380`.

**Missing witness**

There is no dedicated `aggressive_bloc`, `bloc_center`, or real-faction state in Event 6. Event 6 does not create a HOI4 faction. The closest durable abstraction is the Event 6 league:

- formed country is the exact `global.independence_wave_league_leader`;
- it is an active league member;
- league route is `radical_revisionist` (or, only if explicitly accepted, `armed_liberation`);
- league membership/strength meets danger thresholds.

This is valid only if the accepted word “bloc” means the Event 6 league. If it means an actual faction or a distinct aggressive coalition, a new state contract/mechanic is required.

**Required predicate**

`has_independence_wave_6002_hidden_formable_aggressive_bloc`

It must combine the committed hidden-high-chaos formable proof with the approved bloc-center witness. Formation or hidden discovery alone must never qualify.

**Safe bounded evaluation sites**

- After the successful formable transaction has committed identity and integration (`formable_registry_effects.txt:1373-1380`), never at reveal or proposal time.
- After later league leadership, route, or membership mutations that could turn an already committed hidden formable into the bloc center.

### Package 5 — league-sponsored breakaway cascade

**Existing exact witnesses**

- DM-57 publishes sponsorship in `common/decisions/006_independence_wave_decisions.txt:3056-3111`.
- `common/scripted_effects/006_independence_wave_decision_effects.txt:360-375` records sponsor country/generation/route and the sponsored state.
- Lines 422–452 attach `independence_wave_sponsored_release`, `independence_wave_sponsor_country`, sponsor generation, and related data to the committed release.
- `independence_wave_consume_committed_breakaway_sponsorships` at lines 454–515 verifies committed/aligned plan state and increments `global.independence_wave_successful_sponsored_releases` at line 510.
- Existing central threshold: `constant:independence_wave_league.danger_sponsored_releases = 3`.

**Current false-positive risk**

DM-57 is available to qualifying Event 6 countries outside the league. `global.independence_wave_successful_sponsored_releases` therefore counts all successful sponsors and cannot prove “the league sponsors” the cascade.

Add a distinct historical counter, for example `global.independence_wave_successful_league_sponsored_releases`, incremented only when the committed release’s saved sponsor:

- exists and matches the saved sponsor generation;
- is an active Event 6 origin;
- was a league member at the committed sponsorship boundary; and
- belongs to a formal/durable league, not merely a consultative congress.

A historical committed counter is preferable to recounting only surviving releases, because the accepted event describes a visible cascade that occurred and should not be erased by later annexation.

**Required predicate**

`has_independence_wave_6002_league_breakaway_cascade`

Require formal/durable league state and the league-qualified counter at `constant:independence_wave_league.danger_sponsored_releases`. Do not add the package-1 radical route or military-strength requirements unless the design explicitly changes; package 5 is an independent accepted route.

**Safe bounded evaluation site**

End of `independence_wave_consume_committed_breakaway_sponsorships`, after the complete consumption loop (`decision_effects.txt:513-515`), or immediately after its committed transaction caller in `common/scripted_effects/006_independence_wave_execution_effects.txt:539`. Both standalone and collision execution paths already converge through the consumer.

## Proposed trigger architecture

Create five narrow scripted triggers and one aggregator:

```text
has_independence_wave_6002_radical_offensive_league
has_independence_wave_6002_high_chaos_claim_wave
has_independence_wave_6002_synchronized_former_host_wars
has_independence_wave_6002_hidden_formable_aggressive_bloc
has_independence_wave_6002_league_breakaway_cascade
can_independence_wave_fire_danger_super_event_6002
```

The final trigger contract is conceptually:

```text
not independence_wave_danger_super_event_fired
and one of the five package triggers
```

Each package trigger owns its own exclusions. Do not add a shared durable-league requirement above the OR. Do not infer radical government from route availability, coordinated claims from claim-intensity values, synchronized wars from a single war, bloc center from formable creation, or league sponsorship from the existing all-sponsor counter.

The evaluator should be one effect:

```text
independence_wave_try_fire_danger_super_event_6002
```

It may be called from all bounded mutation boundaries listed above. It performs no world iteration and no recurring polling. If eligible, it must atomically set the one-shot guard before any display/audio/log side effect.

## Central constants

Use a dedicated category in `common/script_constants/006_independence_wave_mechanics_constants.txt`, or a dedicated Event 6 super-event constant file if the parent prefers subsystem separation. The implementation needs centrally named values for:

- `display_slot = 24`;
- `audio_id = 6002`;
- visible duration (no accepted number exists yet);
- `high_chaos_wave_country_count = 10`;
- minimum armed/radical governments (“several”; unresolved);
- minimum certified immediate-claim actors (unresolved);
- minimum synchronized former-host wars (“several”; unresolved);
- aggressive-bloc minimum member/strength rules (may intentionally reuse league danger constants);
- sponsored-cascade minimum (reuse `independence_wave_league.danger_sponsored_releases` rather than duplicate `3`).

Use explicit `constant:category.key` access. If the timed global-flag `days` field rejects a constant token, first copy the constant to an unscoped temporary variable and pass that variable. Do not introduce file-scoped duplicated `@` values or hardcoded thresholds in effects.

## Firing order, scope, and cleanup

The final firing effect must be atomic and ordered as follows:

1. Re-evaluate the aggregate trigger at the bounded transaction end.
2. Set `independence_wave_danger_super_event_fired` immediately.
3. Persist a compact package-reason enum/flags for audit, event-log text, and achievement eligibility; do not store truth as numeric `0/1` variables.
4. Set any Event 6 dangerous-milestone state used by log/achievement surfaces.
5. Set the shared super-event slot to display slot `24` for the approved duration.
6. Set `global.current_super_event_audio_id = 6002`.
7. Invoke `play_current_super_event_audio = yes` only from the player-country scope required by the settings helper.
8. Append the approved Event 6 log/evolution/milestone record and run the relevant achievement check.

The one-shot flag persists permanently. Transient package-counting arrays or temporary variables must be cleared at their transaction boundary. A pending-display flag, if approved, must clear only after slot 24 is actually presented. Do not use event targets inside scripted GUI logic.

## Display, sprite, localisation, and audio audit

### Display slot 24

Slot `24` is collision-free in the audited source, but it is not wired. No current `super_event_visible = 24`, `chaosx_super_event.24.*`, or slot-24 image/title/quote/remark/description mapping was found.

Implementation must add slot `24` to all five defined-text dispatchers in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`:

- `GetSuperEventImage`;
- `GetSuperEventTitle`;
- `GetSuperEventQuote`;
- `GetSuperEventRemark`;
- `GetSuperEventDesc`.

The final verified localisation is:

- `chaosx_super_event.24.t: "Every Border a Casus Belli"`
- `chaosx_super_event.24.d: "New-state governments coordinate claims, ultimatums, arms shipments, and mobilization schedules across several regions. Their border commands follow shared timetables, and governments pledge arms or troops to support one another's territorial demands.\n\nFormer hosts reinforce several fronts as they prepare for wars that may begin on the same day."`
- `chaosx_super_event.24.a: "They have sown the wind."`
- `chaosx_super_event.24.q: "\"For they have sown the wind, and they shall reap the whirlwind...\"\n §Y-Hosea 8:7, King James Version-§!"`

These keys must be added in a UTF-8-with-BOM localisation file without `:0` suffixes.

### Image sprite

The image is ready and already registered:

- sprite: `GFX_super_event_006_asset_006_revisionist_milestone`;
- registry: `interface/006_independence_wave_event_pictures.gfx:26-29`;
- runtime DDS: `gfx/super_events/006_independence_wave/super_event_006_asset_006_revisionist_milestone.dds`.

Slot 24’s image dispatcher must return this exact sprite token.

### Audio id 6002

The final production files are ready:

- `sound/006_independence_wave/super_event_006_02_every_border_a_casus_belli.wav` (~109.99 seconds, 44.1 kHz);
- `sound/006_independence_wave/super_event_006_02_every_border_a_casus_belli.wav`.

Registries already exist:

- `sound/chaosx_sound.asset:846-852`: six setting variants `chaosx_super_event_6002_sound_0_5` through `_3_0`;
- `sound/chaosx_sound.asset:264-266`: zero-chance representative track;
- `sound/chaosx_sound.asset:278-283`, raw sound near line 428, and setting wrappers at lines 2045-2051.

No collision exists in the super-event audio namespace. An unrelated unit priority using the number `6002` is a separate parser namespace and is not a collision. No runtime Event 6 source currently sets audio id `6002` or displays slot `24`.

`music/chaosx_music_track_list.html` has no Event 6/6002 attribution row and must be updated atomically when runtime wiring is implemented.

### Settings-aware path

`play_current_super_event_audio` in `common/scripted_effects/chaosx_settings_effects.txt:4874-4927` dynamically dispatches the sound wrappers from `global.current_super_event_audio_id` and the current country’s user settings. Its comments and behavior require the current scope to be the player country that should hear the event.

The Event 6 mutation transactions can run in an AI coordinator or released-country scope. Calling the helper directly from those effects is unsafe. The architecture must not silently add a world iteration: `on_daily`/`on_weekly` scans are forbidden, and even a one-shot `every_country` player search requires explicit parent approval under the repository rule.

An implementation must therefore either:

- use an existing durable player-country pointer/bounded player dispatch supplied by the shared super-event system; or
- receive explicit approval for the established one-shot `every_country = { limit = { is_ai = no } ... }` dispatch pattern.

Until one is selected, audio wiring is blocked even though the files and wrappers are ready.

## Shared-display collision policy

`common/scripted_guis/chaosx_scripted_gui_super_events.txt:1-28` uses the single global `super_event_visible` slot and clears both visibility and `global.current_super_event_audio_id` on close. `interface/chaosx_super_events.gui:127-207` renders the dynamic image/title/description/quote/button.

The Event 6 package can become eligible while another super-event is visible. Overwriting `super_event_visible` would replace the current presentation. Merely adding `NOT = { has_global_flag = super_event_visible }` avoids replacement but can permanently lose 6002 if no later Event 6 mutation retries the evaluator.

Implementation needs an explicit approved policy:

- extend the shared close/dispatcher with a one-entry or general queued super-event contract; or
- use a durable `independence_wave_danger_super_event_pending` state and an approved bounded retry hook.

Do not adopt an unapproved overwrite or drop-on-busy fallback.

## Event-log and achievement hooks

The Event 6 root log already resolves its actor through global event target `independence_wave_latest_actor`: `events/006_independence_wave.txt:11-40` sets `independence_wave_event_log_actor_ready`, and `common/scripted_effects/chaosx_events_log_effects.txt:238-244` consumes that actor for Event 6. Event 6 evolution previews/details are present around `chaosx_events_log_effects.txt:2001-2029` with matching scripted localisation.

No dedicated dangerous-milestone `6002` log append was found. The firing effect should preserve the qualifying actor at its transaction boundary and append an Event 6 evolution/milestone detail whose wording matches the verified super-event/state package. It must not reuse a stale `independence_wave_latest_actor` after a later wave commits.

The achievement design matrix reserves `chaosx_006_radical_bloc` for triggering the dangerous milestone through a revisionist league and surviving the containment response (`docs/specs/006_independence_wave_specs/matrices/006_achievement_matrix.csv:13`). Its final icon triplet exists, but no matching runtime achievement definition/predicate or `independence_wave_danger_milestone` hook was found in `common/achievements/chaos_redux_achievements.txt`.

Therefore:

- firing package 1 should set a distinct revisionist-league qualification flag, not award the achievement immediately if survival of containment is still required;
- packages 2–5 must not accidentally satisfy the revisionist-league achievement;
- the containment-response completion must consume that flag through a separate approved achievement predicate; and
- general `independence_wave_danger_super_event_fired` remains the shared one-shot for all five packages.

## Proposed implementation touch map

This is a future touch map only; none of these files were edited by this audit.

- `common/script_constants/006_independence_wave_mechanics_constants.txt` — slot/audio/duration and unresolved package thresholds.
- `common/scripted_triggers/006_independence_wave_triggers.txt` — five package predicates plus aggregate trigger.
- `common/scripted_effects/006_independence_wave_effects.txt` or a dedicated documented Event 6 super-event effect file — centralized idempotent fire/pending effect.
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt` and execution effects — frozen wave claim/radical witnesses and post-commit evaluation.
- `common/scripted_effects/006_independence_wave_scenario_effects.txt` — post-batch synchronized-war evaluation.
- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` — post-commit formable evaluation.
- `common/scripted_effects/006_independence_wave_decision_effects.txt` — exact league-sponsor counter and post-consumer evaluation.
- `common/decisions/006_independence_wave_decisions.txt` — post-DM-58/DM-59 evaluation boundaries.
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` — all five slot-24 dispatch entries.
- Event 6/super-event localisation — verified `.24.t/.d/.a/.q` text.
- `common/scripted_guis/chaosx_scripted_gui_super_events.txt` or an approved shared dispatcher — pending presentation policy only; no event targets.
- `common/scripted_effects/chaosx_events_log_effects.txt` plus matching localisation — dangerous-milestone history record.
- `common/achievements/chaos_redux_achievements.txt` plus achievement localisation/registry as required — revisionist-league qualification and containment survival.
- `music/chaosx_music_track_list.html` — Event 6 track attribution row.
- Event 6 mechanic documentation, event details/log documentation, asset/audio manifests, and the source workbook/exported catalogs as required by the event skill.

If a new reusable dynamic scripted effect is added to `common/scripted_effects/chaosx_dynamic_effects.txt`, update `chaosx_dynamic_effects.md` in the same change. Prefer a subsystem-local effect if the logic is Event 6-specific.

## Validation scenarios required before completion

### Positive package tests

1. Durable radical-revisionist league crosses all member/common-cause/reserve and offensive-action thresholds at a single bounded mutation; slot 24 fires once.
2. Committed ten-country total-chaos wave includes the approved minimum armed/radical governments and certified immediate coordinated claims; slot 24 fires after commit, not during planning.
3. A single scenario transaction successfully starts the approved minimum distinct former-host wars; failed declarations converted to missions do not count.
4. A committed hidden-high-chaos formable later becomes the approved aggressive-bloc center; neither reveal nor formable commit alone fires it.
5. The approved minimum league-qualified sponsorships commit; non-league sponsorships do not advance the qualifying counter.

### Exclusion and robustness tests

- Calm/Rising normal wave, including ten countries only if some debug/override creates that count, does not qualify without every package-2 witness.
- Consultative congress and ordinary formal league do not qualify.
- Ordinary election/leadership change without the full radical offensive package does not qualify.
- One regional formable, including a hidden formable without bloc-center proof, does not qualify.
- One routine former-host war and a batch with fewer than the threshold successful wars do not qualify.
- Maximum-intensity scenario selection alone does not qualify.
- Three successful non-league sponsors do not qualify package 5.
- Two eligible packages reached in the same transaction still produce one display, one audio dispatch, one log append, and one persistent one-shot flag.
- Eligibility while another super-event is visible follows the approved queue/defer policy without overwriting or dropping either event.
- Each user volume setting selects the correct `6002` sound wrapper; muted volume remains silent; dispatch occurs from player scope.
- Closing slot 24 clears only shared transient display/audio state, not the Event 6 one-shot or achievement qualification.
- Slot 24 resolves the exact image and verified four localisation strings at supported resolutions.
- `6001` remains absent from runtime firing, image dispatch, text dispatch, and audio playback.

## Blocking decisions

Runtime implementation is **NOT READY** until the parent/user resolves all of the following without fallback:

1. **Offensive charter proof:** decide whether radical-revisionist route plus three revisionist actions is sufficient, or whether `independence_wave_radical_charter_active` / coordinated reclamation fronts is mandatory.
2. **Package-2 exact semantics:** choose central values for “several” armed/radical governments and immediate-claim actors, and define the concrete birth-time claim/ultimatum action that certifies `immediate coordinated claims`. Host-claim intensity alone is not accepted proof.
3. **Package-3 threshold:** choose the central number meant by “several” synchronized successful former-host wars. The architecture recommends no numeric fallback.
4. **Aggressive-bloc meaning:** approve the Event 6 radical league as the abstract bloc and define its leader/strength gate, or require a distinct real-faction/bloc-center mechanic.
5. **Shared presentation/audio scope:** approve a busy-slot queue/defer contract and a player-country audio dispatch path. The current bounded Event 6 actor scope is not guaranteed to be the player.

The display slot, final text, image, audio files, wrapper registries, five bounded evaluation boundaries, and one-shot architecture are otherwise evidence-ready. `6001` is explicitly outside this handoff and remains blocked.

## Parent resolution and reachability reconciliation

The parent resolved the five architecture decisions in the runtime tranche:
the offensive proof uses the exact radical route and three completed actions;
the high-chaos wave requires three distinct verified post-commit former-host
claims; synchronized wars require three distinct successful declarations in
one accepted Maximum batch; the aggressive bloc is the exact durable radical
league led by the formable carrier; and presentation uses the existing
settings-aware FIFO with player-country audio dispatch.

These semantic blockers are closed, but runtime reachability is not complete.
Packages 1, 2, 3, and 5 have reachable producers. Package 4's predicate and
publisher are wired, but the only `hidden_high_chaos` registry families are
FORM-42 and FORM-48, both of which remain fail-closed without implemented
carriers. No readiness flag, ordinary formable, or weakened predicate is an
accepted substitute. The Radical Bloc achievement definition and its later
containment-survival award path also remain outside this tranche.
