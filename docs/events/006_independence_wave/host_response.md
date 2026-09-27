# Former-host response

The former-host response gives each country that loses territory to an Event 006 release one aggregate decision after the public report and the released countries' opening postures.

## Accepted design

Acceptance basis: on 2026-09-27 the user accepted Event 006-only loss measurement, one response per distinct host, dispatch after report acknowledgement and country openings, and deterministic AI selection from tier and live host ledgers, then selected the recommended thresholds.

Count distinct states whose committed release owner is `liberation_plan_owner.independence_wave`, whose role is anchor, compact, or extended, and whose recorded former host matches the response country.

Divide that count by the host's aligned pre-release owned-state snapshot.

Limited response applies below 50 percent of the snapshot, severe response applies at 50 percent or more, and the remnant override takes priority when the host owns only its protected state or no longer owns its original capital while owning no more than two states.

Event 005 rows, Join conversions, repeated state rows, and unrelated release origins do not contribute to the numerator.

## Event flow

1. Public report `chaosx.nr6.2` raises the shared report and reset barrier before its option is selected.
2. The report option queues one generation-checked opening for each valid Event 006 country and retains the barrier while those openings resolve.
3. The final opening choice freezes the host-response cohort from the committed release arrays; if the report has no opening responses to queue, the `.2` option starts this host phase directly.
4. The host router waits two days after the last opening so the one-day IW-043 and IW-058 introductions can appear first.
5. Hidden event `chaosx.nr6.63` checks each host receipt and sends a human host to limited `.60`, severe `.61`, or remnant `.62`, while AI hosts resolve through deterministic scripted logic.
6. A human host event times out after 13 days and resolves its first option if the player does not choose an option.
7. Each completed or invalid host receipt decrements the queue once, and the final receipt clears the plan arrays and releases the report/reset barrier.

The queue is admitted as a cohort only after every distinct Event 006 state row, target country row, and host row aligns with the committed transaction.

The original capital remnant check tests current ownership of the frozen original-capital state, and the protected-state check requires that the host own exactly one state and that it be the frozen protected state.

## Host choices and outcomes

| Tier and event | Choice | State claims | Country and bilateral effects |
| --- | --- | --- | --- |
| Limited `.60` | Seek a border conference | Removes the host's claims on its transferred Event 006 states | Lowers immediate bilateral claim, hostility, obligation, pressure, and reconquest values and records guarded coexistence for each matching primary-host country |
| Limited `.60` | Keep the new frontier under pressure | Retains or adds claims on anchor states and releases compact or extended claims | Raises bilateral hostility and pressure around the new frontier |
| Limited `.60` | Prepare a reclamation campaign | Claims every transferred Event 006 state attributed to this host | Records reclamation as policy and applies the temporary reclamation burden; it does not declare war |
| Severe `.61` | Put army command first | Retains or adds anchor claims and releases compact or extended claims | Records reclamation conflict and applies the shared partition-crisis idea |
| Severe `.61` | Put relief and debt settlement first | Preserves anchor claims and releases compact or extended claims | Reduces selected bilateral pressure and hostility values and applies the shared partition-crisis idea |
| Severe `.61` | Recognize the new borders | Removes the host's claims on transferred Event 006 states | Records recognized separation and applies the shared partition-crisis idea |
| Remnant `.62` | Preserve legal continuity | Retains or adds anchor claims and releases compact or extended claims | Sets the legal-continuity route and opens the outside-guarantee opportunity flag |
| Remnant `.62` | Adopt a regional charter | Removes the host's claims on transferred Event 006 states | Records recognized separation, sets the regional-identity route, and opens the outside-guarantee opportunity flag |

The limited reclamation choice applies the reclamation idea for 180 days.

Each severe choice applies the partition-crisis idea for 180 days.

Each remnant choice applies the emergency-government idea for 365 days.

The AI resolver uses only current-wave primary-host rows with matching generations, aligned host-relation arrays, current hostility and domestic-pressure values, and the host's current war state.

At peace with low pressure and hostility, an AI remnant chooses regional identity; a remnant under pressure chooses legal continuity.

An AI severe host prioritizes command during war or high pressure and chooses relief otherwise.

An AI limited host prepares reclamation during war, maintains frontier pressure at high hostility or domestic pressure, and negotiates otherwise.

An optional-state secondary host with no primary-host ledger receives a non-escalatory choice from its tier.

An invalid or missing primary-host ledger closes the AI host receipt without applying an outcome.

## Assets and localisation

All host events reuse `GFX_report_event_006_asset_002_host_crisis`, registered in `interface/006_independence_wave_small_assets.gfx` and backed by `gfx/event_pictures/006_independence_wave/report_event_006_asset_002_host_crisis.dds`.

The partition-crisis and reclamation ideas reuse `independence_wave_fragmented_command`, wired as `GFX_idea_independence_wave_fragmented_command` in `interface/006_independence_wave.gfx`.

The remnant-government idea reuses `independence_wave_improvised_government`, wired as `GFX_idea_independence_wave_improvised_government` in `interface/006_independence_wave.gfx`.

No new art or icon is required for this mechanic.

Event, idea, and dynamic capital-status text lives in `localisation/english/006_independence_wave_host_response_l_english.yml` and `common/scripted_localisation/006_independence_wave_host_response_localisation.txt`.

## Implementation and evidence

Event definitions are in `events/006_independence_wave_host_response_events.txt`.

Queue arithmetic and deterministic AI are in `common/scripted_effects/006_independence_wave_host_response_effects.txt` and its matching trigger file.

The option effects and plan barrier are in `common/scripted_effects/006_independence_wave_host_response_option_effects.txt` and `common/scripted_effects/006_independence_wave_host_response_orchestration_effects.txt`.

Tier and action IDs are in `common/script_constants/006_independence_wave_host_response_constants.txt`, while dispatch and idea durations are in `common/script_constants/006_independence_wave_host_response_timing_constants.txt`.

MCP event lint and render evidence is recorded in the [2026-09-27 implementation handoff](../../plans/006_independence_wave_plans/subagent_handoffs/006_host_response_implementation_2026-09-27.md).

The focused MCP projection is partial and does not expand scripted helpers or prove callback delivery, AI behavior, timeout behavior, save/reload persistence, or in-game balance.

## Later work and possible extensions

The outside-guarantee opportunity flag is a hook for the accepted foreign-reaction tranche; this page does not claim that foreign petitions or guarantees are already implemented.

The accepted Event 006 foreign-reaction and subsequent border-conflict systems should consume the host route and current bilateral ledgers without duplicating the release-state accounting.

Future extensions may add region-specific settlement language, additional border-conference terms, and long-term political consequences tied to repeated losses across separate Event 006 waves.

These extensions remain suggestions unless separately accepted in the relevant specification.

## Reference evidence

The offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md` snapshot, revision `96327B896298420D84058394A44ED08BE7EB518726B8F207B392FEA71F05D43D`, documents event options and timeouts at lines 151–203.

The offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` snapshot, revision `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`, documents event targets at lines 263–268 and `num_owned_states` at line 1524.

Installed `documentation/effects_documentation.md`, revision `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`, documents `add_claim_by` at lines 876–883, `remove_claim_by` at lines 5887–5894, `add_timed_idea` at lines 2244–2266, delayed `country_event` at lines 2951–2967, and `save_event_target_as` at lines 6496–6503.

Installed `documentation/triggers_documentation.md`, revision `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`, documents `has_war` at lines 5024–5032 and `is_owned_by` at lines 6088–6095.

Installed `documentation/dynamic_variables_documentation.md`, revision `538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA`, documents `num_owned_states` at lines 670–671.

Vanilla `events/Baltic.txt`, revision `CEA8147949C85A11256D07D6EFA57F5397F54EF7E3D2F708960BA2BE0431E686`, supplies the Soviet ultimatum event-option precedent at lines 7–118.
