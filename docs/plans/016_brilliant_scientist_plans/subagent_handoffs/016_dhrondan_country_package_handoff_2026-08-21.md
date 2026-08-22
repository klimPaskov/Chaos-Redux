# Empire of D’Rhonda country package handoff

Date: 2026-08-21

Owner: `/root/dhr_country`

Status: gameplay implementation complete; final cross-package art and read-only audit confirmation remain external.

No commit was created.

## Scope delivered

This tranche implements the fixed dormant `DHR` tag and its full country/runtime package outside the separately owned national focus tree.

The package includes country identity, dormant history, cosmetic identities, idempotent formation and re-release logic, state transfer, claims and cores, military-asset conservation, initial-force allocation, three regimes, twelve characters, traits, decisions, diplomatic events, non-focus AI strategies, event-detail integration, and the existing-achievement hook.

It does not edit the DHR national focus tree or its support files, the reusable alien-infantry API, Event 019, Events `.40` through `.47`, binary assets, flags, portraits, icons, models, or the event catalog.

## Files created

- `common/country_tags/016_dhrondan_country.txt`
- `common/countries/Empire of D'Rhonda DHR.txt`
- `common/countries/016_dhrondan_cosmetics.txt`
- `history/countries/DHR - Empire of D'Rhonda.txt`
- `history/units/016_dhrondan_dormant.txt`
- `common/script_constants/016_dhrondan_country_constants.txt`
- `common/scripted_triggers/016_dhrondan_country_triggers.txt`
- `common/scripted_effects/016_dhrondan_country_effects.txt`
- `common/scripted_localisation/016_dhrondan_country_scripted_localisation.txt`
- `common/opinion_modifiers/016_dhrondan_opinion_modifiers.txt`
- `common/characters/016_dhrondan_characters.txt`
- `common/country_leader/016_dhrondan_traits.txt`
- `common/decisions/categories/016_dhrondan_country_categories.txt`
- `common/decisions/016_dhrondan_country_decisions.txt`
- `common/ai_strategy/016_dhrondan_country_strategies.txt`
- `events/016_dhrondan_country_events.txt`
- `localisation/english/016_dhrondan_country_l_english.yml`
- `docs/events/016_brilliant_scientist/systems/dhrondan_country.md`

## Existing files updated

- `common/scripted_triggers/016_brilliant_scientist_achievement_triggers.txt`
- `localisation/english/016_brilliant_scientist_evolutions_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`

## Stable public identifiers

The contact chain calls `dhrondan_start_revolt = yes` in the pact-host COUNTRY scope.

The successful transaction sets `dhrondan_rebellion_bridge_called` on that host only after fixed tag `DHR` exists and owns the selected marked state.

The contact-chain owner removed its premature pre-call receipt and now clears `dhrondan_rebellion_triggered` and refreshes its country pulse when the success receipt is absent.

The focus package calls these idempotent DHR COUNTRY-scope regime effects:

- `dhrondan_install_imperial_regime = yes`
- `dhrondan_install_synod_regime = yes`
- `dhrondan_install_covenant_regime = yes`

The runtime consumes focus-owned flags `dhrondan_imperial_route`, `dhrondan_synod_route`, `dhrondan_covenant_route`, `dhrondan_reclamation_declared`, `dhrondan_integration_started`, and `dhrondan_enclave_crisis_active`.

The runtime initializes `dhrondan_alien_infantry_training_forbidden` before the first DHR focus and assigns `dhrondan_landing_equipment_cost` from canonical `constant:alien_infantry_landing.reserve_equipment`.

## Revolt transaction

The transaction captures the host, global marked-state count, host-owned viable capital, and arrival count before ownership changes.

The formula count includes every state carrying `dhrondan_landing_state`, including lost markers that will become DHR claims; capital selection and territorial transfer remain bounded to states owned by the revolting host.

Capital selection prefers the first host-controlled and passable marked state.

If none is controlled, it falls back to the first host-owned and passable marked state even when a third party controls that state.

Every host-owned marked state receives a DHR core without removing its host core.

The offline engine reference documents that `release = DHR` removes the releasing host core from transferred DHR-core states, so the runtime explicitly restores the origin host core on the released capital and after every later marked-state transfer.

Host-controlled markers use `transfer_state_to = DHR` so owner and controller both change.

Third-party-controlled markers use `set_state_owner_to = DHR` so the explicit transfer pass changes ownership without changing the occupier.

Every marked state outside DHR ownership after the transfer pass receives a DHR claim.

The military-conservation pass deletes every host division using template `D’Rhondan Landing Cohort` with `disband = no`, then sends the host’s full `alien_laser_weapon_equipment_1` stockpile to DHR.

Later host uprisings transfer into the active fixed tag and do not repeat one-time formation grants.

An annexed DHR is released through the same fixed-tag path, reloads `dhrondan_focus_tree` with completed focuses preserved, restores its route government and leader, and does not duplicate characters or opening grants.

## Initial-force formula and allocation

The exact formula is `max(5, min(15, marked_states + floor(arrivals / 2)))`.

`floor(arrivals / 2)` is implemented as a subtract-by-two loop before the min and max gates.

One-time expedition stores are the calculated cohort count multiplied by canonical `constant:alien_infantry_landing.reserve_equipment`.

The initial force uses the public locked-cohort spawn effect and checks `alien_infantry_landing_spawn_succeeded` before decrementing the persistent remainder.

The allocator defines a controlled disconnected enclave as one passable component in the engine’s state-neighbor graph containing only DHR-owned and DHR-controlled states for which `is_in_home_area = no`, where at least one state carries `dhrondan_landing_state`.

It identifies exact components using repeated DHR `every_owned_state` passes whose frontier test is `any_neighbor_state`, creates at most one cohort at the first marked seed in each component, then concentrates the remaining cohorts at the selected capital.

Persistent per-state deployment receipts prevent a component from receiving a duplicate enclave cohort if the allocation resumes after an incomplete attempt.

For any component count from one through 15, the force formula supplies at least that many cohorts because every component contains at least one marked state.

A mechanical sweep over marked-state counts 1 through 40, arrivals 0 through 40, and every feasible component count up to 15 found zero formula-to-component coverage violations.

If more than 15 controlled disconnected components exist, the requirements to deploy one cohort in every component and to cap the army at 15 are mathematically contradictory.

The implementation preserves the max-15 invariant and serves the first 15 engine-enumerated components without creating an unauthorized sixteenth cohort.

Impassable or uncontrolled components cannot receive a spawned division through the public API and are not claimed as covered by this proof.

## Initial-force telemetry boundary

The shared API now accepts temporary input `alien_infantry_initial_force_mode = 1` only when `alien_infantry_landing_batch_mode = 1` and the caller has a positive `alien_infantry_contact_receipt_dhrondan_sovereignty`.

The DHR runtime sets both inputs only inside `dhrondan_deploy_initial_cohorts` and resets them before returning.

The gated branch preserves target validation, exact canonical 2,000-weapon debit, locked cohort creation, create-unit success proof, failure refund, and `alien_infantry_landing_spawn_succeeded`.

Only the formation-inappropriate telemetry is skipped: `dhrondan_arrival_count`, `dhrondan_alien_presence`, `dhrondan_pact_strain`, `dhrondan_landing_history_count`, and `dhrondan_record_successful_landing`.

Therefore API-spawned initial DHR cohorts intentionally do not increment pact-host arrival, presence, strain, or landing-history counters and do not refresh the ordinary rebellion callback.

## Political identities and characters

The political mappings are fixed:

- Emperor Vael IX uses neutrality and cosmetic tag `DHR_IMPERIAL`.
- First Calculant Sera Qel uses neutrality and distinct cosmetic tag `DHR_SYNOD`.
- Speaker Ilyr Ren uses democratic and cosmetic tag `DHR_COVENANT`.

No fascist or communist DHR government is installed.

`western_european_gfx` and `western_european_2d` are deliberate engine-base graphical cultures for standard terrestrial equipment, diplomacy, construction, and interface consumers.

They are documented as an intentional base rather than an unreported substitute for DHR portraits, flags, event art, unit art, counters, or icons.

The exact character roster is:

- `DHR_emperor_vael_ix`
- `DHR_first_calculant_sera_qel`
- `DHR_speaker_ilyr_ren`
- `DHR_archivist_thaal_ven`
- `DHR_logistics_oracle_nym_vor`
- `DHR_harmonic_envoy_rae_syl`
- `DHR_war_calculant_orr_kesh`
- `DHR_genetic_steward_vel_ara`
- `DHR_shadow_listener_thel_ior`
- `DHR_field_vector_kaal_dren`
- `DHR_enclave_guardian_syr_vek`
- `DHR_orbital_liaison_omn_tal`

The roster provides three regime leaders, five civilian advisors, one high-command advisor, and three corps commanders.

All characters are recruited once onto dormant DHR in `history/countries/DHR - Empire of D'Rhonda.txt`, while route leader roles are attached and promoted idempotently at runtime.

No country-specific DHR character is registered through `history/general` or recruited from a runtime scripted effect.

Portrait sprite names match the separately delivered `interface/016_dhrondan_portraits.gfx` handoff.

## Decisions, events, AI, and Event 016 integration

The `dhrondan_sovereignty_category` includes state reclamation, disconnected-enclave supply bridges, recovered-state integration, and Covenant compact diplomacy.

Reclamation gives its target state a timed `dhrondan_reclamation_wargoal_issued` receipt for the same duration as the generated war goal, preventing duplicate demands while preserving retry after an unused authorization expires.

The compact decision clears any stale delivery marker, sets `dhrondan_diplomatic_offer_active`, and keeps that active receipt until exactly one recipient outcome or the delayed invalid-delivery cleanup clears it.

Event `.49` sets `dhrondan_diplomatic_offer_delivered` on DHR in its `immediate` block before the recipient can answer.

Hidden `.52` clears only an active, undelivered offer, while accept and refusal each clear both active and delivered receipts; a player popup left open across multiple game days therefore cannot reopen duplicate offers.

An accepting recipient receives `dhrondan_two_world_compact_partner`, which removes that country from future compact targets while leaving refused partners eligible after the normal cooldown.

Event `chaosx.nr16.49` has an event-level actor and active-receipt validity trigger.

Its refusal modifier applies only below opinion `-25`; friendly opinion above `25` favors acceptance, and a democratic recipient further favors the Covenant proposal.

Hidden event `.52` requires an active receipt and no delivery receipt, so it neither clears an already resolved offer a second time nor races a delivered player popup.

News event `.48` is one-time formation presentation, `.49` is the recipient compact offer, `.50` and `.51` report acceptance or refusal, and `.52` is invalid-delivery cleanup.

Events `.48` through `.52` are follow-up events and are not Event 016 evolutions.

The focus-owned `common/ai_strategy_plans/016_dhrondan_focus_ai.txt` is the sole national-focus plan surface because it includes the opening plan, broader route support lanes, and route focus factors.

The duplicate country-plan draft was removed rather than leaving two simultaneously enabled route queues.

Three AI force strategies use vanilla `role_ratio` identifiers and never assign the locked alien template to normal production.

The Event 016 details localisation appends a DHR sovereignty clause only after `dhrondan_sovereignty_formed`.

The root Event 016 event-log history row deliberately retains the accepted Kruger host as actor because it records his original arrival.

DHR formation does not rewrite that historical actor; `.48` through `.52` are consequence popups under Event 016, while the existing Event Details row gains the conditional sovereignty aftermath.

The existing `Not From Here` trigger accepts the original provenance route or the completed DHR route.

No achievement definition was added, and the Event 016 localisation registry still contains exactly 17 achievement names.

## Asset wiring

The country package consumes these exact sprites:

- `GFX_news_event_016_dhrondan_sovereignty`
- `GFX_report_event_016_dhrondan_diplomatic_compact`
- `GFX_decision_category_dhrondan_sovereignty`
- `GFX_decision_dhrondan_reclamation`
- `GFX_decision_dhrondan_enclave_supply`
- `GFX_decision_dhrondan_state_integration`
- `GFX_decision_dhrondan_two_world_compact`

Purpose-built DDS binaries exist for both event pictures and all five decision/category surfaces, but these seven tokens are not yet present in an `interface/*.gfx` source.

The parent’s active DHR icon/art audit owns the missing sprite-definition wiring.

No fallback sprite or vanilla icon was introduced.

## Validation evidence

- All 16 DHR-owned Clausewitz script files have balanced braces after moving the fixed roster into the country-history file and removing the duplicate national-focus plan.
- The owned scripts contain no unsupported `<=` or `>=` operator and no unary negation of variable tokens.
- `016_dhrondan_country_l_english.yml`, the patched Event 016 details localisation, and the patched achievement localisation all retain UTF-8 BOM encoding.
- The DHR localisation file contains 115 unique keys and no duplicate key.
- Event IDs `.48` through `.52`, tag `DHR`, the three cosmetic tags, and all twelve character IDs have one source definition each.
- Every focus ID named by the sole focus-owned DHR AI plan file exists in `common/national_focus/016_dhrondan_focus_tree.txt`; the country package contributes no duplicate national-focus plan.
- Vanilla AI strategy precedents confirm `infantry`, `armor`, `mountaineers`, and `marines` as valid `role_ratio` identifiers.
- Vanilla country-leader precedents confirm every DHR leader and advisor modifier used by the package.
- Source-derived `.49` scores are 210 accept to 30 refuse for a democratic recipient at opinion `+50`, 70 to 30 for a neutral non-democratic recipient, and 70 to 90 for a non-democratic recipient at opinion `-50`, corresponding to complete-pool expectations of 87.5/12.5, 70/30, and 43.75/56.25 percent.
- The localisation auditor’s five findings were corrected and rechecked: provisional neutrality/news identity, all four decision tooltip connections, repeat-safe compact wording, explicit `The Century Beyond Exile` achievement guidance, and completed-state Event Details prose.
- The event-completion auditor verified one-time formation news, `.49` event-level validity, delivered-versus-active compact cleanup, no `.48-.52` evolution registration, retained Kruger-host event-log actor, and exactly 17 Event 016 achievements.
- The project country-tag audit reported zero external country-definition collisions and zero external identity-surface collisions, but its broader Event 006 check stopped on an unrelated pre-existing `BLX` cosmetic registry mismatch.

## MCP evidence and blockers

The installed HOI4 MCP exposed callable `hoi4.event_inspect`, `hoi4.event_compare`, and `hoi4.map_inspect` routes.

A focused `.49` trace returned `EVENT_INSPECTED_PARTIAL` at revision `641888481c1a01768798a266ac9e444348a73e8b0b9e1cbe5b49f9e413cd06f6`, graph hash `0116289c85b9d780e6cfc0bf50a7a9d678190ebc8c668e1e1a53fdd1e5634ad1`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1aec799e1f17c63d02911a6fffa3c04d68e4dda0fa68cef7272b57a7e6583ce4/ad77d3b9bc1cd1722e8f0e26f77ca1e2e7a74e4c427071bec178612fd0903f30/event-trace-641888481c1a.json`.

The file-scoped event scan and render overview each timed out after 180 seconds, and the partial trace deferred workspace-wide helper and lifecycle projections.

The map inspector timed out after 180 seconds when limited to bootstrap state `1`.

No meaningful before/baseline revision exists for this newly created event file, so there is no valid pair for `hoi4.event_compare`.

No separate runtime state-transfer inspect or compare route was exposed.

No declarative map source changed, so there was no valid `map_rewrite` operation to submit.

Probability inspection found the complete `.49` option pool, and a same-source `probability_compare` completed with `comparisonChanges=0`.

The compare artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6582120f42c54fbcdda6d8add43bd54fc0a526c59a739d4c0cf18d3770b20136/62eb76db8b82d4e893f2d32fe172642bbe6bc4475cf1f984a3a44e4a7e113a51/probability-d248554c251923ea00a58884.json`; the initial inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ecb53f1395f2b0d0820a8c4c7a005a78de062ee6ec5310100ed96be4723ddde/512e5eaf910df87d21db2c7f5b3999f228757c3e5c3ce27cfb867544d50ec448/probability-inspect-414413ca3c1b.json`.

The scenario adapter could not declare `event_target:dhrondan_diplomatic_actor`, scoped `has_opinion`, or `has_government`, so it reported accept as ineligible and left conditional probabilities null in all three named scenarios.

That is a fixture limitation rather than an in-game eligibility finding; the source-derived scores above are not presented as MCP-certified campaign probabilities.

The decision adapter found only the compact decision and returned `poolComplete=false` for the other three targeted decisions; route strategy inspection returned `INTERNAL_ERROR`, and the sole focus-plan inspection timed out after 180 seconds.

The offline Paradox wiki’s `release` reference explicitly states that owned-but-not-controlled states transfer to the released country but remain uncontrolled by it, and its `set_state_owner_to` reference states that ownership changes without controller transfer.

That authoritative source contract closes the occupied-capital controller question for both first release and later transfers.

The same reference documents release-time loss of the releasing country’s core, which led to the source correction that restores the origin host core after the capital release and every explicit landing-state transfer.

MCP state-transfer comparison evidence remains unavailable because the map route timed out and no separate runtime state-transfer inspect/compare route was exposed; this is an evidence-route limitation, not an unresolved engine semantic.

## Remaining risks and required follow-up

1. Carry the probability fixture limitation forward: `.49` source scores are verified and same-source compare completed, but scoped actor/opinion/government inputs prevented MCP certification of normalized real-campaign probabilities; decision candidate discovery was incomplete and route/focus inspection failed or timed out.
2. Confirm the seven event and decision sprite definitions from the active DHR icon/art audit without adding fallback art.
3. Align the Event 16 row in the catalog workbook with the current Event Details text and conditional D’Rhondan sovereignty clause, then re-export the catalog CSVs; this tranche was explicitly forbidden from editing the catalog.
4. Carry the partial event trace and the MCP map/state-transfer evidence-route blockers into the parent completion report without reopening the controller semantic resolved by the offline engine reference.
5. Retain the explicit more-than-15 enclave contradiction and the uncontrolled or impassable spawn limitation in every acceptance report.
6. Retain the portrait handoff’s explicit user-review status for the nine nonleader characters and their role cards; no placeholder or approval claim is introduced here.

No gameplay simplification was made for any feasible one-through-15 controlled passable enclave configuration.

The more-than-15 contradiction and unavailable MCP comparison evidence are reported boundaries, not silently substituted behavior.
