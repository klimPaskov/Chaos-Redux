# Empire of D'Rhonda Focus Tree

## Overview

The Empire of D'Rhonda uses the dedicated `dhrondan_focus_tree` after the country runtime forms or restores DHR.
The tree turns the scattered landing enclaves into one of three regimes, rebuilds the expedition's laboratory and predictive-war systems, establishes orbital and diplomatic support, settles the two-world political question, and resolves a late enclave crisis.
The tree owns focus progression and stable hooks only.
Country creation, characters, parties, state transfer, claims, cores, decisions, events, the alien landing API, and alien unit definitions remain in their existing owner systems.

## Exact branch inventory

| Branch family | Focus count | Focus range | Primary identity |
| --- | ---: | --- | --- |
| Survival and landing network | 8 | `DHR_beneath_an_alien_sky` to `DHR_convene_the_two_world_throne` | Enclave stabilization and the paid landing contract |
| Imperial Continuity | 8 | `DHR_vael_ix_takes_the_throne` to `DHR_the_unbroken_imperial_line` | Vael IX, oath, service, reclamation, and imperial mandate |
| Predictive Synod | 8 | `DHR_sera_qel_presents_the_calculus` to `DHR_the_government_of_certainties` | Sera Qel, audits, merit, forecast government, and Synod calculus |
| Two-World Covenant | 8 | `DHR_ilyr_ren_opens_the_chamber` to `DHR_the_chamber_of_two_skies` | Ilyr Ren, dual citizenship, elected councils, and representative compact |
| Laboratory economy | 10 | `DHR_relight_the_field_laboratories` to `DHR_a_two_world_research_complex` | Material substitution, component standards, and one research-slot capstone |
| Army and predictive warfare | 12 | `DHR_restore_the_predictive_staff` to `DHR_perfect_predictive_warfare` | Forecast doctrine, signals, logistics, and command lifecycle |
| Orbital, air, and naval support | 8 | `DHR_reassemble_the_orbital_office` to `DHR_make_near_space_ours` | Relays, air corridors, shuttle docks, and descent defense |
| Diplomacy and intelligence | 8 | `DHR_open_the_translation_bureaus` to `DHR_the_embassy_beyond_the_stars` | Translation, trade, access, enclave intelligence, and partners |
| Expansion and world order | 12 | `DHR_define_the_two_worlds_question` to `DHR_a_place_in_the_world_order` | Three regime-specific settlement models and shared integration |
| Crisis and late game | 6 | `DHR_the_enclaves_refuse_the_ledger` to `DHR_the_century_beyond_exile` | Reconciliation or cipher suppression, corridor restoration, and final state |

The total is exactly 88 focuses.

## Political routes

The three regime roots are mutually exclusive in the focus graph.
`DHR_vael_ix_takes_the_throne` sets `dhrondan_imperial_route`, applies `DHR_IMPERIAL`, and calls `dhrondan_install_imperial_regime`.
`DHR_sera_qel_presents_the_calculus` sets `dhrondan_synod_route`, applies `DHR_SYNOD`, and calls `dhrondan_install_synod_regime`.
`DHR_ilyr_ren_opens_the_chamber` sets `dhrondan_covenant_route`, applies `DHR_COVENANT`, and calls `dhrondan_install_covenant_regime`.
The country-runtime effects own leader and party reconciliation, while the focus helpers own the mutually exclusive route flags and cosmetic identity.
Vael IX and Sera Qel both remain within the supported neutrality ideology family but receive different leader, route, cosmetic, national-spirit, AI, expansion, and crisis behavior.
Ilyr Ren uses the democratic Covenant identity.

## Three-slot national-spirit lifecycle

Focuses can maintain no more than three simultaneous DHR focus-created spirits.
The political slot begins with `dhrondan_homeworld_fragmentation`, advances to `dhrondan_homeworld_cohesion`, and ends as exactly one of `dhrondan_imperial_mandate`, `dhrondan_synod_calculus`, or `dhrondan_covenant_compact`.
The military slot begins with `dhrondan_predictive_lag`, advances to `dhrondan_predictive_sight`, and ends with `dhrondan_predictive_command`.
The corridor slot begins with `dhrondan_offworld_isolation`, advances to `dhrondan_offworld_relay`, and ends with `dhrondan_offworld_corridor`.
Every transition clears all ideas in its family before adding the next stage, so revisiting an idempotent helper cannot stack stages.

## Landing and unit boundary

`DHR_reopen_the_orbital_channel` enables `dhrondan_landing_network_enabled` and assigns `dhrondan_landing_equipment_cost` from the generic API's `constant:alien_infantry_landing.reserve_equipment`. The shared API uses that network flag to shorten ordinary post-landing recovery to `constant:alien_infantry_landing.cooldown_days_network` (24 days); `DHR_guard_the_descent_windows` and `DHR_make_near_space_ours` add the guarded-descent and near-space tiers of 18 and 12 days respectively. The one-time sovereignty bootstrap batch never sets or consumes these recovery tiers.
That constant is exactly 2,000.
`DHR_feed_the_landing_reserve` sets the consumed reserve-priority flag but does not reserve equipment, create a unit, or add equipment.
The focus tree contains no division creation, template grant, stockpile grant, equipment production line, or normal alien-infantry training path.
Each landing remains an external API call that must consume the required exotic laser weapons.
The other survival milestones are live decision inputs rather than history-only markers: counting landing states, auditing expedition stores, and restoring landing beacons each add a distinct DHR-only landing AI preference, while securing the scattered enclaves increases the AI priority of the existing enclave-supply decision.
These readers are additive and do not make optional survival branches hard prerequisites for the shared landing API.

## Reward and balance model

Opening survival focuses use 21-day and 28-day emergency durations, while ordinary institutional steps use 35-day or 56-day durations and branch capstones use 70 days.
The enclave-crisis sequence uses 49-day choices and a 70-day corridor or final capstone.
Focus reward values are centralized in `common/script_constants/016_dhrondan_focus_constants.txt`, while the landing price comes from the shared alien-infantry API constant; file-scoped constants cover focus duration, graph AI, building levels, research-slot count, and one-use research bonuses where those fields require static tokens.
Political rewards emphasize stability, political power, command power, and route flags.
Laboratory rewards alternate factories, research bonuses, production contracts, and a single additional research slot at `DHR_a_two_world_research_complex`.
Army rewards alternate doctrine bonuses, experience, command power, infrastructure, and two staged spirit upgrades.
Orbital rewards alternate air and naval experience, radar and airfield capacity, a coastal dockyard, research bonuses, and the relay lifecycle.
Diplomatic rewards create future-facing partner, access, intelligence, and embassy hooks rather than direct territorial outcomes.
Expansion rewards expose reclamation, integration, and regime-specific world-order contracts for the decision and event owners.

## Cross-system hooks

The focus tree exposes `dhrondan_reclamation_declared`, `dhrondan_integration_started`, `dhrondan_enclave_crisis_active`, and `dhrondan_enclave_crisis_resolved` for the integration, reclamation, and enclave-crisis consumers.
It also exposes `dhrondan_world_order_decisions_unlocked`, `dhrondan_world_order_claim_contract_ready`, and route-specific settlement flags for later decision or event work.
No focus directly changes claims, cores, owned states, or event outcomes.

## AI behavior

The opening strategy plan prioritizes the eight survival focuses and aborts once a regime flag is present.
Inline route weights make Vael more attractive in wartime or high-war-support conditions, make Sera more attractive during stable peace, and make Ilyr more attractive when a peaceful state needs legitimacy.
The Imperial strategy plan prioritizes predictive warfare, orbital security, coercive reclamation, and cipher suppression.
The Synod strategy plan prioritizes laboratories, predictive warfare, calculated reclamation, and cipher suppression.
The Covenant strategy plan prioritizes diplomacy, research, orbital support, negotiated federation, and crisis reconciliation.
All support and late-game focuses retain inline AI weights so the country can continue sensibly when a strict strategy-plan target is temporarily unavailable.

## Navigation, filters, and layout

Ten Focus Navigation shortcuts target survival, the three regimes, laboratory economy, predictive warfare, orbital support, diplomacy and intelligence, expansion, and the enclave crisis.
Every focus uses one or more current vanilla search-filter keys matching its primary gameplay role.
The authored tree places the survival trunk at the top center, the three political routes in symmetric central lanes, laboratory and army support to the left, orbital and diplomatic support to the right, expansion beneath the regimes, and the crisis beneath the convergence.

## Icon registry and asset handoff

`interface/016_dhrondan_focus_icons.gfx` registers one base sprite and one shine sprite for every focus before binary art production.
All focus DDS paths use `gfx/interface/goals/016_dhrondan_focus/<family>/goal_<focus_id>.dds`.
The family folders are `survival`, `imperial`, `synod`, `covenant`, `laboratory`, `army`, `orbital`, `diplomacy`, `expansion`, and `crisis`.
The intended palettes are survival amber, Imperial violet-gold, Synod cyan-silver, Covenant teal-white, laboratory electric blue, army crimson, orbital indigo, diplomacy green, expansion gold-red, and crisis white-magenta.
The same registry defines the eleven lifecycle idea sprites under `gfx/interface/ideas/016_dhrondan_focus/<idea_id>.dds`.
No binary art is part of this focus implementation.

## Future plans

The decision owner can consume the paid landing, partner-selection, world-order, reclamation, integration, and crisis flags without changing focus IDs.
The event owner can attach enclave reactions and settlement reports to the stable route and crisis flags.
The asset owner can produce the registered family icon set without renaming gameplay identifiers or paths.
External runtime acceptance remains necessary for release-time tree loading, cosmetic transitions, paid-landing consumption, and state-dependent factory placement.
