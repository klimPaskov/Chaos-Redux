# Event 016 final decision, mission, and raid audit

Date: 2026-08-26.

Status: Read-only audit for the parent agent; no gameplay, localisation, GUI, or balance source was changed by this audit.

Audit anchor: commit `fbd5f6703` (`fix: isolate alien landing registries by country`), with the current shared-worktree source inspected after that anchor.

> Current-status correction after commit `d77afae7e` (`fix: preserve alien landing registry ownership`): the former S1/P1 registry-scope finding below is resolved in the current source by saving the invoking COUNTRY and selected STATE as event targets before mutating the country-owned array.
> The original finding and its pre-correction disposition remain historical audit evidence only and must not trigger another registry-writer patch.
> Current Event MCP evidence is partial rather than a live transfer acceptance claim, and the Portal lifecycle, five D’Rhondan support flags, GUI/MCP limits, probability coverage, and custom-unit model blockers remain open.

## Scope and evidence

The audit covered alien contact and landing decisions, landing reservation/refund/cooldown, Kruger and Mengele expedition paths, the rebellion pulse, D’Rhondan sovereignty decisions, native Portal Warfare raids, AI weights, trigger/effect tooltips, ownership cleanup, and the country-scoped landing registry.

Primary source files were `common/decisions/016_alien_infantry_landing_decisions.txt`, `common/decisions/016_dhrondan_contact_decisions.txt`, `common/decisions/016_dhrondan_country_decisions.txt`, `common/raids/016_brilliant_scientist_portal_raids.txt`, `common/scripted_effects/016_alien_infantry_api_effects.txt`, `common/scripted_effects/016_dhrondan_contact_effects.txt`, `common/scripted_effects/016_dhrondan_country_effects.txt`, `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`, their Event 016 scripted triggers and localisation, and the Directorate scripted GUI files.

Required offline Paradox wiki pages were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, interface modding, and scripted GUI modding.

Vanilla documentation consulted included `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `modifiers_documentation.md`, `common/raids/_documentation.md`, and vanilla raid definitions under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.

The relevant offline and vanilla scope evidence is that regular arrays belong to the current scope, `var:... = {}` enters the variable’s stored scope, `ROOT` is the root scope, and `for_each_scope_loop` changes `THIS` to each array element.

## Severity-ordered issue list

### Resolved source correction: former S1/P1 country-scoped registry finding

The former finding targeted `alien_infantry_register_landing_state` at `common/scripted_effects/016_alien_infantry_api_effects.txt:301-321` after commit `fbd5f6703` changed the registry name but left the nested state-scope write ambiguous.

Commit `d77afae7e` now saves the invoking COUNTRY as `alien_infantry_landing_registry_owner`, saves the selected STATE as `alien_infantry_landing_registry_state`, and performs both `is_in_array` and `add_to_array` from `event_target:alien_infantry_landing_registry_owner` at `common/scripted_effects/016_alien_infantry_api_effects.txt:301-327`.

The API documentation and country-scoped handoff record this owner-target boundary for ordinary landings and the Event 019 provider-508 deferred commit.

Disposition: **RESOLVED at source by `d77afae7e`; dynamic two-provider transfer and live-save acceptance remain unproved.** The prior S1/P1 blocker is not an active implementation task.

The remaining verification target is a two-provider matrix covering duplicate registration, state loss, D’Rhondan revolt-capital selection, release/transfer, claims, and Event 019 deferred landing isolation.

### P2 queued: Portal beachhead state has no assigned containment or expiry consumer

`common/scripted_effects/016_brilliant_scientist_raid_effects.txt:53-60` writes `brilliant_scientist_portal_beachhead_active` and `brilliant_scientist_portal_raid_breach_recorded`.

The raid effect also writes `brilliant_scientist_portal_raid_targeted`, `brilliant_scientist_portal_facility_extracted`, and `brilliant_scientist_portal_factory_extracted` at the extraction and targeting branches.

Repository searches and `016_portal_lifecycle_patch_2026-08-26.md` found no Event 016 consumer that clears, expires, or transitions these markers.

Disposition: **QUEUED for the future Portal containment/spread owner**. The historical extraction markers may intentionally persist, but `brilliant_scientist_portal_beachhead_active` needs an explicit transient-versus-permanent policy before it becomes a launch or target lock.

### P2/P3 queued: AI expedition route priority is deterministic and not probability-proven

`dhrondan_ai_authorize_expedition` in `common/scripted_effects/016_dhrondan_contact_effects.txt:182-206` debits the AI decision’s 50 Political Power and selects Kruger first whenever both the Kruger and Mengele routes are valid; Mengele is selected only when Kruger is unavailable.

This is internally safe and avoids duplicate payment, but it is not a weighted route pool and does not demonstrate that both AI routes receive their intended opportunity share.

Disposition: **QUEUED balance/documentation item**, not a source defect. The accepted design should either document Kruger-first priority or replace it with a bounded explicit pool after a named probability audit.

### P3 queued: Portal raider force bound is minimum-only

Both native raids require `portal_raider = { min = 6 }` in `common/raids/016_brilliant_scientist_portal_raids.txt`, but the definitions do not impose a maximum formation size.

The exact-facility raid also requires a tagged facility in the target province and a valid destination, which is conservative but can make otherwise plausible targets unavailable.

Disposition: **QUEUED for balance review**. No exploit is proven because the source division is destroyed on success and the native raid owns reservation, cancellation, expiry, and outcome handling.

### P3 blocked: Directorate GUI re-inspection could not complete

The decision-owned GUI is `kruger_directorate_container` in `interface/016_brilliant_scientist_directorate.gui`, attached by `brilliant_scientist_directorate_category` and implemented in `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`.

Fresh `mcp__hoi4_agent_tools__hoi4_gui_inspect` and `mcp__hoi4_agent_tools__hoi4_gui_render` calls timed out after 180 seconds for the current `event016_directorate_compact_current` scenario, including a narrow normal-state render.

Historical render evidence exists at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efb93e06f3584a666ca7a109061b9b9a929f3bf3b75e7965d96252280e504cce/fc87e0ae2873caacf7590dc2ee23aecece6c1647c805c55cb1d2ae038822d265/kruger_directorate_container-full.svg`, but historical evidence does not replace a current inspect/render pass.

Disposition: **BLOCKED MCP evidence only**. Source review shows a compact 500x360 panel with a collapsed header, portrait, four meter values, role text, and collapse/expand controls; it has no gameplay-changing buttons or spendable costs. No `hoi4.gui_rewrite` was used.

### P3 queued: five D’Rhondan focus support flags have no current decision consumer

`dhrondan_alien_components_standardized`, `dhrondan_laboratory_route_complete`, `dhrondan_predictive_warfare_perfected`, `dhrondan_orbital_office_reassembled`, and `dhrondan_access_map_exchange_ready` are set by `common/national_focus/016_dhrondan_focus_tree.txt` but have no current downstream consumer.

Disposition: **QUEUED documentation or future-route ownership item**. This audit does not add duplicate decisions or invent lifecycle mechanics.

## Resolved source findings

The alien landing path is lifecycle-complete at source level with the owner-target registry correction present. `alien_infantry_call_landing` in `common/decisions/016_alien_infantry_landing_decisions.txt:9-59` requires aggregate contact, a controlled owned non-impassable state, no pending landing or cooldown, and 2,000 laser weapons. It reserves exactly 2,000 weapons, stores the selected state, starts `alien_infantry_landing_mission`, and uses a seven-day timeout.

`alien_infantry_cancel_landing_reservation` clears the pending flag before refunding exactly one 2,000-weapon reserve, removes the mission, clears the duration variable, and clears the saved state target. The timeout path uses the same single-cohort spawn helper and is guarded against duplicate pending materialization.

The ordinary cooldown ladder is 30 days by default and 24, 18, or 12 days for the accepted D’Rhondan network upgrades. The Event 019 deferred commit path records the committed debit and applies telemetry only after its enclosing transaction succeeds.

The Kruger route is isolated from Mengele. Kruger requires the canonical active, uninjured, unconfined Kruger character, envoy craft, no route or transaction lock, and no pact. It suspends the canonical role, records the obligation, debits 500 fuel, stores a 180-day duration, activates `dhrondan_kruger_expedition_mission`, and restores the role only on valid return or failure cleanup.

The Mengele route has its own availability, receipt, mission, and 180-day duration. It does not mutate Kruger variables or the canonical Kruger obligation.

Both expedition decisions spend 50 Political Power and expose 500 fuel as a separate custom trigger tooltip. Their cancel triggers revalidate the route and fuel, and their failure helper clears route flags, duration, audience state, and invalid obligations.

`dhrondan_rebellion_pulse_mission` is country-scoped, gated by the pact, six or more arrivals, Pact Strain 30 or more, Chaos 600 or more, no world end, and no prior trigger. It runs for 90 days, cancels when the gate falls below threshold, and resolves the accepted 10/20/40 tier ladder in `dhrondan_resolve_rebellion_pulse`.

The D’Rhondan state decisions revalidate their selected state both at availability and during their native timer. `dhrondan_reclaim_landing_site` issues a 365-day wargoal with a 90-day decision repeat cooldown. `dhrondan_establish_enclave_supply_bridge` adds infrastructure and resolves the crisis only when all disconnected enclaves are supported. `dhrondan_integrate_reclaimed_landing_site` is postwar, adds the DHR core, and cancels if war resumes.

`dhrondan_offer_two_world_compact` validates an independent, non-warring, non-subject, non-NAP partner and stores the partner in `dhrondan_diplomatic_offer_target`. Events `chaosx.nr16.49` through `.52` validate the actor and target and call `dhrondan_clear_diplomatic_offer` on accept, refusal, or invalidation.

The native Portal raid pair is structurally bounded. `brilliant_scientist_portal_facility_raid` targets a hostile controlled state with an eligible industrial, military, dockyard, rocket, or nuclear installation. `brilliant_scientist_portal_special_project_facility_raid` targets an exact tagged facility in a target province.

Both native raids use seven preparation days, 30-day target re-enable, 10 Command Power, 60 Teleportation Equipment, six minimum raiders, and native `available`, `launchable`, and `cancel_trigger` gates. Success levels cover failure, limited success, success, and critical success.

Success creates one Portal Breach Cadre and destroys the source raider division. State-target critical success intentionally calls the state extraction helper twice, while exact-facility critical success extracts the selected facility plus one state installation; this matches `docs/events/016_brilliant_scientist/systems/portal_raider_api.md` and is not treated as an exploit.

## Category lifecycle and cognitive-load notes

`alien_infantry_landing_category` exposes one state-targeted action and one hidden mission, so it stays below the six-action limit and below the active-mission limit. The visible cost is one equipment type and the tooltip gives the seven-day reservation/refund behavior and cooldown consequence.

`dhrondan_contact_category` exposes a status row, two mutually exclusive expedition actions, one accord action, and one hidden expedition mission per route plus one hidden pulse mission. The status row is not actionable; at most one Kruger or Mengele expedition is valid at a time because the route and transaction locks are explicit. The rebellion mission is the only additional active pulse and has visible 10/20/40 thresholds.

`dhrondan_sovereignty_category` has four primary actions, with three state-targeted timers and one country-targeted compact offer. Requirements are separated into target trigger tooltips and consumed Political Power costs.

The Portal surface has two native raid actions, each with two spendable cost types and native preparation/reservation history. There is no custom Portal decision GUI in this scope.

The Directorate GUI displays four meters and profile/role state, but the source-defined labels explain the values through dynamic localisation. Current visual fidelity remains unverified because the fresh MCP inspect/render timed out.

No audited visible value is a raw unexplained number dump. The remaining significance gap is the unresolved transient policy for `brilliant_scientist_portal_beachhead_active` and the unproved live transfer behavior after the owner-target registry correction.

## Mission quality audit

| ID | Owner/category/region | Requirement and duration | Success | Failure/cancel | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `alien_infantry_landing_mission` | Landing country, `alien_infantry_landing_category`, selected controlled state | Contact, valid state, pending reserve; 7 days | One locked landing cohort, telemetry, cooldown, history, registry insertion | Loss of control or invalid target refunds one reserve and clears mission/target | Pending flag, target pointer, and one-cohort guard block overlap |
| `dhrondan_kruger_expedition_mission` | Host country, `dhrondan_contact_category`, D’Rhondan route | Valid Kruger route and envoy craft; 180 days | Audience/pact authorization and canonical role restoration | Route failure clears obligation, role suspension, duration, and pending audience | Route, obligation, expedition, and transaction locks |
| `dhrondan_mengele_expedition_mission` | Mengele directorate country, `dhrondan_contact_category`, D’Rhondan route | Valid Mengele route and envoy craft; 180 days | Independent audience/pact receipt | Route failure clears route and pending state without touching Kruger | Own route and expedition lock; no shared Kruger variables |
| `dhrondan_rebellion_pulse_mission` | Pact host, `dhrondan_contact_category`, country-wide pulse | Pact, arrivals, strain, Chaos, and world-end gates; 90 days | One weighted revolt outcome at the accepted tier | Falls below gate or resolves once; prior-triggered flag prevents repeat | Single active mission plus `dhrondan_rebellion_triggered` |
| `dhrondan_reclaim_landing_site` | DHR, `dhrondan_sovereignty_category`, selected state | Marked landing state and active claim contract; native 30-day timer | 365-day state wargoal and state claim marker | Target invalidation cancels; 90-day repeat cooldown | State marker and active wargoal marker |
| `dhrondan_establish_enclave_supply_bridge` | DHR, sovereignty category, selected state | Disconnected supported enclave and crisis flag; native 30-day timer | Infrastructure, completion flag, crisis resolution when all supported | Target invalidation cancels | Per-state completion marker |
| `dhrondan_integrate_reclaimed_landing_site` | DHR, sovereignty category, selected state | Reclaimed marked state, DHR control, peace; native 60-day timer | DHR core, completion flag, war support | War or target invalidation cancels | State core/completion checks |
| `brilliant_scientist_portal_facility_raid` and `brilliant_scientist_portal_special_project_facility_raid` | Actor raid category, hostile state/province target | War, control, destination, readiness, 6 raiders, 60 equipment, 10 Command Power; 7-day preparation | Native four-level outcome; successful levels establish breach/extract and destroy source division | Native cancellation, expiry, and failure history | Native operation lock, 30-day target re-enable, and source division destruction |

## Cost and requirement clarity

The cost-count audit found no gameplay-changing decision or raid with more than four distinct spendable types.

`alien_infantry_call_landing` spends one type: exactly 2,000 `alien_laser_weapon_equipment_1`, displayed with `£GFX_alien_laser_weapon_equipment_medium`.

`dhrondan_send_kruger_to_dhronda` and `dhrondan_send_mengele_to_dhronda` each spend two types: 50 Political Power and 500 fuel, displayed with `£pol_power` and `£fuel_texticon`.

`dhrondan_honor_accord` spends one type: 75 Political Power, displayed with `£pol_power`.

The three state decisions and `dhrondan_offer_two_world_compact` each spend one Political Power cost. Non-consumed state, route, peace, partner, and world-end requirements are exposed through separate custom trigger tooltips rather than being concatenated into cost prose.

Portal raids each spend two types: 10 Command Power and 60 Teleportation Equipment, displayed with `£command_power` and `£teleportation_equipment_1_text_icon`.

The static localisation scan found all referenced custom cost, trigger, effect, target, preparation, launch, and outcome keys in the Event 016 localisation files. No literal spendable resource name was found in the audited cost strings.

## AI validity and route locks

Alien landing AI only scores valid controlled state targets and respects equipment, contact, pending, cooldown, and world-end gates. The state target helper rejects impassable or uncontrolled states.

Kruger AI requires a live canonical holder and an eligible route; Mengele AI requires its own eligible country and route. D’Rhondan route triggers reject missing craft, existing pact, active expedition, obligation, transaction locks, and world end.

DHR sovereignty AI only targets states or countries that pass the same target validation as the player decision. Compact partner checks reject dead, subject, warring, NAP, and already compacted targets.

Portal AI zeroes invalid actor or target candidates and applies the accepted Kruger-host, Kruger-state, major-target, capital, and facility factors. A full live outcome probability remains unproven because the probability route timed out and the historical Portal inspect returned no weighted candidates.

## Localisation and tooltip gaps

No missing custom localisation key was found for the audited decisions, missions, raids, or Directorate scripted GUI.

The strongest remaining presentation gap is not a missing key but an unverified blocked-row reason for the Directorate and route-specific decision surfaces because current GUI inspect timed out. The source has route and fuel custom tooltips, but visual blocked-state fidelity is queued until MCP evidence is available.

The rebellion mission description explicitly states six, eight/nine, and ten-plus arrival thresholds, Pact Strain thresholds, Chaos thresholds, and the 10/20/40 outcomes.

## Cleanup and exploit-risk notes

Alien reservation cleanup is idempotent and refunds only a proven pending 2,000-weapon debit. Event 019 deferred rollback deletes the exact cohort and refunds only its recorded debit after the provider ledger confirms deletion.

Kruger cleanup is route-specific and restores the canonical character only when the obligation and active uninjured/unconfined holder conditions are still valid. Mengele cleanup does not restore or mutate Kruger.

The compact offer has an explicit invalidation monitor and clears the persistent global target through `dhrondan_clear_diplomatic_offer`.

Portal success destroys the source division, so the native raid does not create a free repeating raider loop. Exact facility extraction uses province-specific removal and destination capacity checks.

The owner-target registry correction removes the material source-level ownership risk, but its live DHR-transfer behavior remains unproved. The unresolved Portal beachhead marker is the material stale-state risk. No free equipment, core spam, war-goal spam, or cooldown bypass was proven in the reviewed source.

## MCP evidence and blockers

Fresh Event 016 state-flow inspection completed with `mcp__hoi4_agent_tools__hoi4_event_inspect` for `chaosx.nr16.47`, `state_flow`, both directions, helper expansion, depth 8, 300 edges, and 300 nodes.

The current event artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/314c37a4ca98f885a184258990a628a5d3f1eba884402ddfa9cdc79d54d2beb2/a49ecc61d1395cf8d3b7f2e007108381bbf9bc60b40d12e5d0ba02299620e0bc/event-state_flow-f588a2607444.json`.

It returned `EVENT_INSPECTED_PARTIAL` with `MCP_INLINE_FILES_TRUNCATED` and large-workspace unresolved nodes; it is useful event-chain evidence but cannot prove variable/array runtime scope.

There is no callable `chaosx_ai_probability_auditor` in the current tool inventory. The direct `mcp__hoi4_agent_tools__hoi4_probability_inspect` attempt for `common/decisions/016_dhrondan_contact_decisions.txt` timed out after 180 seconds, both with `decision_ai_will_do` and with the default adapter. Therefore no current `probability_compare` pass can be claimed.

Historical probability evidence remains in `016_dhr_probability_audit_2026-08-25.md`, including the rebellion evaluation artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dfa838f159810ca6f095235a1cabd42cf180cf5fcbb486ac6deeb0f6e4d66c73/9b7f24f7e1b5706ef83b53d9eed196e42eaeae20cb2a124f3bcac7107506c32c/probability-fedc30a49c5461669eb47b59.json` and its ranking, matrix, sensitivity, and threshold SVG artifacts. Those artifacts support the 10/20/40 tier math but are not a fresh post-anchor compare.

The historical landing probability artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ba5df215c4597dc8b93ed286e3ef8a68f9de8030ef0db45a30451759f9c70bb/c77bf302d219c97c7c01d6cd5f37f42bb13ab7f3d5f0bd7df3da6df2dcd64919/probability-inspect-ee65b59c5aeb.json`; it left nested target and stockpile inputs unresolved.

Current `mcp__hoi4_agent_tools__hoi4_gui_inspect` for `kruger_directorate_container` returned `GUI_INSPECTED` with 22 Event 016 elements, but the shared graph retained truncated global diagnostics in artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac982a59753151c4e08404fce5807fb7bbae7a1b628eeb6ba8a15b00860b8cbc/126cd885185d595e3aea7f6be9679b4403aef0c8097e94faad34716dfc7c539d/gui-inspect.b4279d9e180ba8bb.json`.

A narrow current `hoi4.gui_render` retry for the same window and scenario returned `INTERNAL_ERROR` with no artifact, so the historical render remains useful evidence but no current before/after comparison is claimed.

No decision-specific, mission-specific, or native-raid-specific MCP inspector was exposed in the current tool inventory. Source review and the event graph were used for those surfaces, with this limitation recorded rather than treated as engine equivalence.

## Recommended owner actions

1. Run the two-provider registry acceptance matrix against the owner-target implementation in `d77afae7e`, covering ordinary and Event 019 deferred landing, duplicate registration, DHR capture, release/transfer, state loss, and provider isolation.

2. Add a two-country registry acceptance scenario covering ordinary landing, Event 019 deferred landing, DHR capture, DHR release/transfer, and isolation from a second provider country.

3. Assign a Portal containment/spread owner and decide whether `brilliant_scientist_portal_beachhead_active` is transient, while documenting permanent extraction/history markers.

4. Run the named `chaosx_ai_probability_auditor` when the route becomes callable, using the same rebellion, landing, expedition, and Portal scenarios, then compare AI route priority and target weighting.

5. Re-run `hoi4.gui_inspect` and `hoi4.gui_render` for `kruger_directorate_container` at compact/full resolutions and blocked/hover states after the current MCP render route is responsive; current inspect success does not close the global-diagnostics or render-artifact limit.

6. Keep the five D’Rhondan focus support flags as documented future hooks or give them an accepted consumer; do not add duplicate decision surfaces during this audit.

## Validation and handoff

Meaningful validation completed: source-level trigger/effect/AI/cleanup review, offline wiki and vanilla documentation review, native raid precedent review, Event 016 event state-flow inspection, and a static localisation reference scan.

Skipped meaningful validation: live HOI4 execution, savegame playtest, current GUI artifact generation, decision/mission/raid-specific MCP inspection where no route was exposed, and named probability-auditor/probability-compare execution because the custom auditor was unavailable and direct inspection timed out.

Changed files: only this handoff file. No gameplay source, localisation, GUI, raid, decision, mission, or scripted effect was patched.

Remaining risk: the country-scoped registry writer is corrected in source, but Event 016 DHR landing transfer still needs the two-provider engine/live acceptance matrix; Portal beachhead lifecycle, five D’Rhondan support flags, GUI/MCP limits, probability coverage, and custom-unit model blockers remain open.

Plan handoff path: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_decision_audit_2026-08-26.md`.
