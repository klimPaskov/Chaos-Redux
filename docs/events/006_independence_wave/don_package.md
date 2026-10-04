# IW-039 Don Host (DON)

The Don Host package releases a provisional Cossack host government at Millerovo when the Independence Wave reaches the lower Don.

## Accepted design

Acceptance basis: on 2026-09-26 the user chose state 245/Millerovo as the Event 006 anchor and capital, state 238/Volgodonsk as optional compact territory, state 218/Rostov outside the package, and mutual exclusion with Event 005's Don Host Republic (DHC) in both event orders (`docs/plans/006_independence_wave_plans/006_event6_iw039_don_package_improvement_addendum_2026-09-26.md`).
Central admission is agent decision D5 in `docs/plans/006_independence_wave_plans/agent_decisions_2026-10-04.md`.

## Release and setup

1. The planner reserves state 245 as the anchor and tries 238 as compact territory; an unavailable 238 is trimmed by the ordinary reservation path, while Event 005 ownership, control or reservation of 218 or 238, or a living DHC, blocks DON.
2. DON shares the `RG-DON-KUBAN` reservation group with IW-040 Kuban, so at most one of the two can appear in a wave.
3. Execution sets the capital to 245, captures the actual former host, and requires that SOV, when it is the host, still owns state 219.
4. Setup removes any vanilla `Kavaleriyskaya Diviziya` units before the single p39 mounted-mobile force application, loads the five reinforcement pathways, assigns the shared focus framework with the constitutional, emergency-military and host-negotiation routes, locks the government route until a settlement is chosen, adds the emergency-stores and unratified-mandate ideas, and starts the founding mission.
5. Final validation proves the complete setup, anchor control, the p39 force for the current generation, and the DHC preflight.

## Play

- Founding mission "Hold the Millerovo Charter Together" (420 days).
- Paid projects: "Audit the Millerovo Railhead" (25 political power) and "Hear the District Petitions" (20 political power), one at a time.
- Government settlements (30 political power): "Elect the Host Assembly", "Ratify the District Compact" (plus 10 command power), or "Establish the Emergency Host Staff", which opens the 90-day mission "Review the Emergency Host Staff" and the decision "Submit the Mandate for Civilian Review" (10 political power).
- Five shared focuses: "Register the Millerovo Authorities", "Survey Rail and Remount Stores", "Hear the Land and Service Claims", "Set the Service Quota", "Ratify the Millerovo Charter".
- Completing the charter grants the chartered-host idea and opens the internal FORM-11 later-gate marker; failure applies the fractured-charter idea.

## AI

Focus and decision weights follow the shared Event 006 scales. The AI strategy registry adds a mounted survival lane, former-host war restraint until the charter is complete, a settled lane afterwards, and a defense lane while the emergency host staff governs (`independence_wave_don_*` in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`).

## Cleanup

`independence_wave_cleanup_iw_039_don` runs only for the same package generation. It removes missions, decisions, ideas and flags, restores neutral politics and the vanilla popularity baseline, and marks the focus layout dirty.

## Assets

DON reuses the vanilla DON flag, the vanilla roster, and existing Event 006 decision and category icons. No new art is required.

## Source

- `common/scripted_effects/006_independence_wave_don_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_don_package_triggers.txt`
- `common/scripted_triggers/005_006_liberations_collision_triggers.txt` (DHC interlock)
- `common/decisions/006_independence_wave_don_decisions.txt`
- `common/national_focus/006_independence_wave_iw039_don_focus.txt`
- `common/script_constants/006_independence_wave_don_constants.txt`
- `localisation/english/006_independence_wave_don_l_english.yml`

## Future plans

- FORM-11 carrier, membership and consent for a DON and KUB host federation across distinct waves.
- A corridor project that rewards actually holding state 238.
