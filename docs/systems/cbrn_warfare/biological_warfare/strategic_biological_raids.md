# Strategic Biological Raids

## Overview

Strategic biological raids provide four distinct ordinary-pathogen operations: Anthrax, Plague, Tularemia, and Smallpox. Each operation reserves its own payload model, uses tactical or strategic bombers, targets one exact selected state, and feeds any real release into the ordinary biological lifecycle.

Weaponized-zombie strikes and the anti-zombie cure raid are separate systems. They do not call the ordinary-pathogen raid resolver or lifecycle helpers.

## Preparing an Operation

The attacker must:

1. Complete the matching biological special project.
2. Hold a CBRN Use Policy that authorizes strategic release, or possess valid retaliation authority.
3. Designate a Biological Raid Staging Complex through `bio_designate_strategic_raid_staging_state`.
4. Remain at war with the target country and select an inhabited, non-wasteland, non-zombie state controlled by that enemy.
5. Supply the required tactical-bomber or strategic-bomber formation, Command Power, and exact payload stockpile.

The staging decision costs 25 Political Power and normally has a 90-day relocation cooldown. An exact-state control-change hook clears the lost complex marker and the former controller's matching state pointer immediately. A lost or otherwise invalid complex can be replaced without waiting for the relocation cooldown.

The designated state is a secured handling, storage, inspection, and loading complex. It is the only state eligible for an attacker handling accident. It is not presented as the actual launch airbase because the current raid API does not expose that state to outcome script.

## Agent Profiles

| Agent | Agent potency tier | Canonical strength | Preparation | Command Power | Tactical bombers | Strategic bombers | Payload reservation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Tularemia | low | 0.85 | 21 days | 8 | 15 | 5 | 100 Tularemia Bombs |
| Anthrax | moderate | 1.00 | 28 days | 10 | 25 | 10 | 200 Anthrax Bombs |
| Plague | serious | 1.15 | 35 days | 15 | 50 | 20 | 100 Plague Bombs |
| Smallpox | severe | 1.30 | 45 days | 25 | 25 | 10 | 50 Smallpox Bombs |

Overall weapon strength is strictly `Tularemia < Anthrax < Plague < Smallpox`, and only Smallpox belongs to the severe tier.

All four agents use the same native base result factors: 0.50 success, 0.12 critical success, and 0.10 disaster.

Each selected state has a 120-day raid cooldown through the native state-target contract. Aircraft experience, defence, agility, reliability, air superiority, interception, anti-air, radar, and intelligence feed the native raid result. Agent identity does not alter those delivery probabilities. Once a release is accepted, the four agents retain their distinct canonical strength, incubation, growth, spread, detection, medical, mortality, persistence, and countermeasure profiles in the lifecycle.

## Reservation, Consumption, and Refunds

`essential_equipment` is the exact native reservation debit made when the raid is created. The resolver never creates an alternate payload and never estimates a debit.

- Failed delivery consumes a bounded 40-80 percent of the reservation.
- Partial contamination consumes 75-100 percent.
- Hidden contamination, detected seed, successful seed, and attacker accident consume the full reservation.
- Only unused units of the exact reserved equipment model are refunded.
- If the hostile relationship, native target, policy, project, or staging context becomes invalid after creation, the already-collected exact reservation is recorded as physically lost. This rejection creates no release, contamination, deaths, evidence, attribution, biological-use history, retaliation, or Condemnation.
- The raid result panel evaluates that same current context. Invalid operations show the no-release result for both countries instead of displaying an outcome that the resolver rejects.
- A lifecycle dispatch failure loses the full collected reservation. It does not refund material or invent contamination, evidence, or a substitute state.

Chaos Warfare doctrine may refund part of the Command Power cost after a resolved operation. It never refunds or erases payload consumption, release history, deaths, contamination, medical saturation, evidence, attribution, or confirmed-use history.

## Six Outcomes

The native raid engine exposes four operational delivery results. These are not weapon-severity ratings. The resolver maps them to the accepted six-outcome biological model:

1. `failed_delivery`: no release enters the target lifecycle. Investigators can still recover evidence and Condemnation can follow.
2. `partial_contamination`: a weaker seed enters the selected state and begins incubation.
3. `hidden_contamination`: a viable seed enters with stronger concealment and lower initial evidence.
4. `detected_outbreak_seed`: a viable seed enters and is forced into detection when incubation activates.
5. `successful_outbreak_seed`: a stronger critical-result seed enters incubation. This still does not guarantee an outbreak or change the agent’s weapon-severity tier.
6. `attacker_accident`: the full payload is released in the designated staging complex and enters the accident lifecycle there.

Native failure selects between failed delivery and attacker accident according to the actor's biological-security level, handling technologies, Headquarters preparation, and sealed-bomb-bay designer capability. Native success selects between hidden and detected seeding according to attribution control, precision-release capability, and the defender's surveillance and response technologies.

## Lifecycle Order

Every actual ordinary-pathogen release follows the same state-scoped order:

1. Validate actor, victim, route, agent, result, exact state, and positive payload debit.
2. Load the agent and route profile.
3. Apply Chemical Readiness weaponization and Chaos Warfare doctrine to the authorized seed, growth, spread, deaths, duration, and medical-pressure multipliers. Evidence and protected consequence records remain unchanged.
4. Store or strengthen the agent-specific incubation record in the exact selected state.
5. Record deliberate-use history once for the delivery resolution.
6. Schedule incubation through an exact-state delayed event.
7. On activation, attempt or force detection, then schedule state-owned lifecycle ticks.
8. Progress intensity, exposed share, medical saturation, deaths, evidence, attribution, spread, containment, treatment, modifiers, and cleanup.
9. Release probable or confirmed Condemnation only when evidence and detection support it.

If evidence crosses directly into confirmed attribution, the lifecycle settles the unreleased probable share before the confirmed share. Rapid forensic confirmation therefore cannot erase latent Condemnation or its domestic political cost.

Doctrine can increase seed potency, growth, spread, deaths, duration, and medical pressure while reducing only the Condemnation component. Physical payload debit, evidence, attribution, deaths and death history, contamination and contamination history, medical saturation and medical history, confirmed-use history, domestic war-support penalties, biological-use counters, accident records, resistance trauma, treaties, and public-harm floors remain intact.

Ordinary lifecycle scheduling is state-owned. The current implementation has no `common/on_actions/chaosx_on_actions_biowarfare.txt` file and no startup or weekly calls to `initialize_smallpox_vaccination_protection`, `progress_smallpox_vaccination`, or `check_all_states_for_contamination_cleanup`.

The lifecycle reads `smallpox_vaccination_program_idea` directly from the affected country's current ideas when calculating agent-specific growth, spread, and death multipliers. Recovery calls `bio_lifecycle_cleanup_state_response_if_no_ordinary_episode` for the exact state. That helper removes field hospitals, quarantine, stale legacy protection state, and the quarantine modifier only after the state has no remaining ordinary biological episode.

No global biological daily, weekly, or monthly country pulse performs progression or response cleanup.

## Failed-Attempt Evidence

A failed delivery creates a state-owned forensic lead without contaminating the state. The state retains the strongest responsible-country lead, combines repeated evidence from that same actor, and decays the lead through delayed exact-state callbacks. A weaker attempt by another actor cannot replace or refresh the dominant lead.

## AI Use

AI use passes one common authorization gate and then applies route-aware weighting:

- Retaliation and confirmed enemy biological use strongly increase willingness.
- First-use and unrestricted doctrine routes increase willingness.
- The Japan-China theater receives its bounded historical preference.
- Defensive CBRN profiles strongly reduce willingness.
- A prepared domestic handling and response program increases willingness.
- Shared borders reduce willingness because of blowback.
- Surveillance, rapid response, integrated control, and active outbreaks reduce target value.
- Population, capital status, industry, and major-country status increase target value.
- High Condemnation combined with import vulnerability sharply reduces ordinary use.
- An unrestricted actor under formal censure receives a continuation preference only when a current enemy has crossed the exact near-victory surrender threshold.
- An actor whose own surrender progress reaches the near-capitulation threshold stops selecting ordinary strategic biological raids.

The ordinary safety floor requires Pathogen Handling Protocols and Rapid Outbreak Response. The authorization gate retains a desperate safety waiver for an unrestricted route with extreme-use authority, but Stage 10 AI does not select an ordinary raid during the actor's own near-capitulation state. An explicitly authorized doomsday route leaves the separate doomsday decision as the only biological release choice during collapse. Neither route can create policy authority, projects, payloads, aircraft, or a staging complex.

## Engine Limits

Current-version raid outcome script exposes the actor, victim, selected state, and selected province when the target type supplies one. These raids use the documented native state target, so their cooldown and lifecycle both identify the same selected state. The API does not expose the actual launch-airbase state or a documented weather value. Therefore:

- Contamination always uses the exact native selected state.
- Attacker accidents use the explicitly designated handling complex.
- No launch-state inference or weather estimator exists.
- No ordinary continuous-air mission can seed biological contamination.
- Idle biological-capable aircraft never contaminate a region.

If a future game version documents a real eligible-activity or weather hook, it must be verified against installed documentation and vanilla use before integration. It must not be approximated.

## Files and Identifiers

Gameplay:

- `common/raids/biological_raids.txt`
- `common/raids/biological_zombie_cure_raid.txt`
- `common/decisions/biological_raid_staging_decisions.txt`
- `common/on_actions/chaosx_on_actions.txt`
- `common/script_constants/biological_raid_constants.txt`
- `common/scripted_effects/biological_raid_effects.txt`
- `common/scripted_triggers/biological_raid_triggers.txt`
- `common/scripted_effects/biological_lifecycle_effects.txt`
- `common/scripted_triggers/biological_lifecycle_triggers.txt`
- `events/biological_lifecycle_events.txt`

Player-facing wiring:

- `localisation/english/biological_strategic_raids_l_english.yml`
- `localisation/english/chaosx_raids_l_english.yml`
- `interface/biological_warfare.gfx`
- `interface/chaosx_raids.gfx`

Stable raid IDs are `anthrax_strike`, `plague_strike`, `tularemia_strike`, and `smallpox_strike`. The separate cure-delivery ID is `zombie_cure_strike`.

## Assets

- Staging decision icon: `gfx/interface/decisions/biowarfare/bio_designate_strategic_raid_staging_state.dds`, registered as `GFX_decision_bio_designate_strategic_raid_staging_state` in `interface/biological_warfare.gfx`. Source and validation package: `docs/assets/chaos_warfare_system/stage_7_biological_warfare/`.
- Raid map icons: the existing Chaos Redux files at `gfx/interface/military_raids/map_icons/raid_type_icon_{anthrax,plague,tularemia,smallpox}_strike.dds`, registered through the corresponding `GFX_raid_type_icon_*` sprites in `interface/chaosx_raids.gfx`.

The strategic biological raids retain and use the pre-existing military-raid icons at their stable paths. This tranche does not replace them with generated art or cross-type substitutes.

## Future Extensions

- Add player-facing state intelligence summaries for incubation, evidence, and countermeasure pressure only if the UI can expose the real lifecycle variables without leaking hidden information.
- Add an actual launch-base or weather interaction only after a current-version documented raid hook exposes that state or condition.
- Keep any future operative, battlefield, sabotage, or doomsday delivery method on the same ordinary-pathogen lifecycle contract with its own exact payload debit and route profile.
