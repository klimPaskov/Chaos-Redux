# Event 019 Infantry Spawn achievements

## Overview

Event 019 has eleven stable custom-achievement identifiers. The achievement definitions live in `common/achievements/chaos_redux_achievements.txt`. Centralized thresholds, proof effects, completion triggers, and one-shot victory hooks live in the Event 019 achievement-owned script files. Generation, management, claimant, rail, and country-pulse effects call narrow achievement helpers at the point where the authoritative Event 019 ledger still identifies the exact generation, lot, unit, claimant, or state.

All ordinary achievements require a human country and reject forced or debug completion history. The triggerable-scenario achievement owns a separate frozen launch record because a scenario is intentionally forced setup. Ready flags never replace the underlying disqualifier checks: claimant seizure, revolt, emergency integration, failed teardown, forced parent merge, leadership interruption, capitulation, intensity changes, and country switching remain durable where their contracts require them.

## Achievement contracts

| Identifier | Proof |
| --- | --- |
| `019_infantry_spawn_every_rifle_accounted_for` | Close an exact generation of at least 30 units with no unresolved lot or obligation, at least 70 Muster Control, congestion below 25, and no claimant takeover or revolt. |
| `019_infantry_spawn_one_battalion_wonder` | An exact surviving generated one-combat-battalion division wins its controlled one-versus-one border trial without composition mutation. |
| `019_infantry_spawn_the_army_has_voted` | The exact promoted claimant remains continuously in power for 365 days or defeats a major while still leading. |
| `019_infantry_spawn_order_from_noise` | At Evolution III, integrate eight distinct unrestricted random lots, then hold at least 85 Muster Control and congestion below 25. |
| `019_infantry_spawn_combined_arms_accident` | An exact generated Evolution III random division with at least eight distinct combat-component types wins its controlled one-versus-one border trial without composition mutation. |
| `019_infantry_spawn_no_room_on_the_train` | Close a generation of at least 20 units with at least 15 integrated units while an exact capital-to-origin rail proof remains live. Rail failure and emergency integration disqualify it. |
| `019_infantry_spawn_borrowed_future` | An exact advanced generated division wins its controlled one-versus-one border trial while one of its recorded technology or project gates is still locked. |
| `019_infantry_spawn_three_false_apocalypses` | One ordinary human country defeats distinct isolated zombie, ghost, and golem derivative countries without a forced parent-event merge. |
| `019_infantry_spawn_barracks_of_babel` | An exact generated Evolution III random division containing camelry, bicycle infantry, amphibious armor, a flame element, artillery, and engineers wins its controlled one-versus-one border trial. |
| `019_infantry_spawn_quiet_demobilisation` | Close a generation of at least 30 units after every lot and unit is removed by supervised demobilisation, all obligations are settled, and Muster Control is at least 70. |
| `019_infantry_spawn_every_barracks_a_front` | The starting human country survives The Generals' Muster or The Impossible Host at Maximum intensity for 365 continuous days or defeats every hostile government raised by that launch, without capitulation, intensity reduction, country switching, or World End. |

Each controlled combat contract has its own Army Experience and Command Power cost, immutable material-quality and coherence thresholds, and live launch strength and organization thresholds. The border-war engine enforces a 14-day minimum engagement, and the shared mission rejects an unresolved trial after 45 days. A shared 90-day cooldown follows every started trial.

## Exact identity and exploit protection

Generated divisions carry their immutable Event 019 unit, lot, generation, and template identifiers. Evolution III manifests retain their original component-token ledger, distinct combat-type summary, Babel component summary, and pre-technology gate pairs. Standardization disqualifies every exact unit in the lot before unlocking its template. Integration and derivative-defeat evidence is deduplicated by stable lot or country identity. Generation closeout is evaluated only while the newly resolved row remains selected, so a generation cannot be counted twice.

Combat trials add a country-local nonce to the exact selected ledger division and freeze its unit, generation, lot, template, attacker state, defender state, defender country, and trial type. The attacker state must contain exactly that one division and no allied or foreign formation. The adjacent defender state must begin completely empty. A peaceful independent AI country receives one locked, temporary infantry detachment with its own nonce-bound identity. Both sides are rechecked as literal sole participants at launch and resolution. `change_state_after_war = no` prevents annexation or microstate loss.

The temporary opponent receives no permanent benefit. Recruitment from its unique locked trial template is disabled. Cleanup first requires exactly one unit carrying the expected defender marker, nonce, attacker identity, and create-unit ID. It deletes through both the unique template name and create-unit ID without disbanding or refund, removes the template, then proves that zero nonce-marked defenders and no trial template remain. Only that proof releases the opponent lock. Missing, duplicate, or residual evidence quarantines the opponent instead. Win, loss, cancellation, mission timeout, ownership change, civil war, outside war, extra-division entry, and identity failure all converge on idempotent cleanup. Scenario host eligibility rejects the active attacker, the locked opponent, and the quarantined cleanup country, while its shared transaction-idle gate rejects any same-tag setup or rollback still in flight. Only an attacker-win callback can set a ready flag, and it can set only the frozen trial type's flag. No generation, lot, death, war, evolution, Event Log, or World End counter is touched.

Claimant leadership interruption and scenario capitulation are durable history, not final-state-only checks. Active rail, claimant-survival, and scenario-origin attempts use a separate lightweight one-day continuity event that evaluates only achievement proof. The full Event 019 and derivative ledger, AI, pressure, and lifecycle pulse retains its normal cadence, and no recurring all-country or world achievement scan is added. The engine has no universal callback for a leader removal and restoration, console tag switch away and back, or railway break and repair completed entirely between two daily samples, so those sub-day transitions are not observable by script.

## Controlled combat-trial route

The ordinary `on_army_leader_won_combat` callback remains unused because it exposes neither an exact participating division nor a same-battle measurement tuple. The approved controlled route does not manufacture casualty or force-ratio values. Four state-targeted decisions select an exact qualifying Event 19 division and a safe empty adjacent AI state, then call one shared launch effect. The same decision and launch path is available to AI Event 19 countries with the same costs, quality checks, state purity, cooldown, and cleanup.

This controlled one-formation combat route is one of Event 19's exactly two
owner-approved engine-constrained substitutes. The other is exact
recorded-formation recreate/prove/delete for natural derivative ownership
transfer. No ordinary country-combat proxy or other achievement fallback is
accepted.

The start transaction revalidates the full immutable component ledger before creating the opponent. It pays only after both trial states report a live border war. The attacker-win callback repeats the ledger, composition, and Borrowed Future technology-gate checks before recording proof. Defender callbacks validate their opponent marker and nonce, then route through the frozen attacker country ID into the same attacker-root handlers, so callback order cannot duplicate awards or cleanup.

## Icon package

Each identifier requires three independent 64 by 64 DDS files loaded by the custom-achievement convention:

- `gfx/achievements/<achievement_id>.dds`
- `gfx/achievements/<achievement_id>_grey.dds`
- `gfx/achievements/<achievement_id>_not_eligible.dds`

The custom-achievement loader can resolve the filename triplets directly, and
Event 019 also registers all 33 explicit aliases in
`interface/chaosx_achievements.gfx` for stable consumer wiring. The Event 019
asset manifest records the source, processed PNG, final DDS paths, hashes, and
visual direction for all eleven triplets.

## Future plans

- Extend trial-opponent templates only through additional locked, uniquely named, nonce-verified packages with equivalent cleanup proof.
- If a future Event 019 template-edit path is added, call the existing lot disqualification helper before any mutation.
- If scenario setup gains post-launch intensity editing or country-transfer actions, call the existing durable invalidation helpers at those exact sources.
