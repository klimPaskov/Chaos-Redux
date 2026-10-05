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
The focus tree contains no division creation, template grant, or normal alien-infantry training path, and no focus grants laser weapons outright.
Each landing remains an external API call that must consume the required exotic laser weapons.
The Exoplanetary Materials Board opens one ordinary laser production line that still uses the country's own military factories, and the convention underwriting and the Imperial tithe return lasers only after a paid landing has succeeded.
The other survival milestones are live decision inputs rather than history-only markers: counting landing states, auditing expedition stores, and restoring landing beacons each add a distinct DHR-only landing AI preference, while securing the scattered enclaves increases the AI priority of the existing enclave-supply decision.
These readers are additive and do not make optional survival branches hard prerequisites for the shared landing API.

## Reward and balance model

Opening survival focuses use 21-day and 28-day emergency durations, while ordinary institutional steps use 35-day or 56-day durations and branch capstones use 70 days.
The enclave-crisis sequence uses 49-day choices and a 70-day corridor or final capstone.
Focus reward values are centralized in `common/script_constants/016_dhrondan_focus_constants.txt`, while the landing price comes from the shared alien-infantry API constant; file-scoped constants cover focus duration, graph AI, building levels, research-slot count, and one-use research bonuses where those fields require static tokens.
Regime rewards change how each government uses the landing network, its landing states, and the sovereignty decisions; see [Reward mechanics](#reward-mechanics).
Laboratory rewards alternate factories, research bonuses, production contracts, and a single additional research slot at `DHR_a_two_world_research_complex`.
Army rewards alternate doctrine bonuses, the paid-landing improvements, commander skill, infrastructure, and the staged spirit upgrades.
Orbital rewards alternate air and naval experience, radar and airfield capacity, a coastal dockyard, research bonuses, and the relay lifecycle.
Diplomatic rewards give intelligence over landing-host countries, partner access, and an embassy that improves opinion and opens a second partner accord.
Expansion rewards turn lost landing states into claims, drive the reclamation and integration decisions, and found the Covenant's federation.

## Reward mechanics

Twenty-four focuses that once paid flat Political Power, Stability, Command Power, or experience now change a live system.
Each sets at most one flag, and every flag it sets has a reader.
Values live in `dhrondan_focus_mechanic` and `dhrondan_focus_mechanic_factor` (`common/script_constants/016_dhrondan_focus_constants.txt`); file-scoped mirrors in `016_dhrondan_focus_effects.txt` cover fields that reject constants.
The reward effects are named `dhrondan_focus_<action>` in that file.

Per-landing results run in `dhrondan_apply_landing_dividends`, which `dhrondan_record_successful_landing` calls for DHR after every successful landing while `var:dhrondan_landing_state_id` still names the landed state.
Recovery and descent changes run in `dhrondan_adjust_landing_cooldown` and `dhrondan_adjust_landing_reservation`, which the shared landing API calls only for DHR.

| Focus | Regime or lane | Mechanic | Reader |
| --- | --- | --- | --- |
| Convene the Two-World Throne | Shared | The next successful paid landing returns the lasers it actually cost (the settled reservation amount, otherwise 2,000) | `dhrondan_convention_landing_underwritten`, landing dividends (consumed once), `alien_infantry_landing_settled_amount` |
| Restore the Ninth Diadem | Imperial | Land forts on the border provinces of every owned landing state, and on each later landing state while Vael IX rules | `dhrondan_ninth_diadem_restored`, landing dividends |
| Bind the Landing Lords | Imperial | Each successful landing returns 500 lasers as a tithe | `dhrondan_landing_lords_bound`, landing dividends |
| Codify Imperial Service | Imperial | Integration orders may proceed during war | `dhrondan_imperial_service_codified`, `dhrondan_integration_war_rule_is_met` |
| Crown the Enclave Empire | Imperial | Every owned and controlled landing state becomes a core; -2% stability per state crowned | One-time |
| Audit Every Command Node | Synod | Landing recovery 6 days shorter (floor 6) | `dhrondan_command_nodes_audited`, cooldown adjustment |
| Elevate the First Calculants | Synod | Reclaim, Bridge, and Integrate orders return half their Political Power | `dhrondan_first_calculants_elevated`, `dhrondan_apply_calculant_refund` |
| Replace Decree with Prediction | Synod | +1 infrastructure in disconnected enclaves now; each supply bridge builds a second level | `dhrondan_decree_replaced_by_prediction`, bridge decision |
| Enthrone the Synod | Synod | A civilian factory in up to three landing states | One-time |
| Write the Dual Citizenship Code | Covenant | Landing states gain the state modifier `dhrondan_dual_citizenship_enclave` (+25% non-core manpower, +10% recruitable population), and later landing states receive it | `dhrondan_dual_citizenship_code_written`, landing dividends |
| Elect the Landing Councils | Covenant | Integration also raises 20 manpower per thousand inhabitants and +2% stability | `dhrondan_landing_councils_elected`, `dhrondan_apply_council_integration` |
| Guarantee the Right to Depart | Covenant | A Two-World Compact partner also grants military access and sends 6,000 manpower | `dhrondan_right_to_depart_guaranteed`, Event .49 `dhrondan_apply_compact_focus_terms` |
| Submit the Military to Debate | Covenant | Reclamation can be authorized without perfected predictive warfare; debated war goals last twice as long | `dhrondan_military_submitted_to_debate`, `dhrondan_reclamation_is_authorized` |
| The Exoplanetary Materials Board | Laboratory | A laser production line requesting three military factories, starting at 50% efficiency | One-time |
| Train Human Signal Teams | Army | Signal Company unlock; landings arrive after 4 days instead of 7 | `dhrondan_human_signal_teams_trained`, reservation adjustment and `GetAlienInfantryLandingReservationDays` |
| Rebuild the Expeditionary Cadres | Army | +5 army experience per successful landing | `dhrondan_expeditionary_cadres_rebuilt`, landing dividends |
| The Thousand-Branch Wargame | Army | Advances the military spirit to Predictive Command early | Existing lifecycle |
| Delegate to the Field Calculants | Army | +1 Planning for every army commander | One-time |
| The Foreseen Counterstroke | Army | Landing recovery 4 days shorter in wartime (floor 6) | `dhrondan_foreseen_counterstroke_prepared`, cooldown adjustment |
| Seed the Enclave Network | Diplomacy | 10 civilian and 10 army intel over every country holding a marked landing state | One-time bounded pass over flagged states |
| The Embassy Beyond the Stars | Diplomacy | `dhrondan_extraterrestrial_embassy` opinion with neighbors and partners; one more Terrestrial Partner Accord | `dhrondan_extraterrestrial_embassy_established`, `dhrondan_can_conclude_another_partner_accord` |
| Restore the Imperial Reaches | Imperial expansion | Claims on every marked landing state held by another country, feeding the Reclaim decision | One-time bounded pass over flagged states |
| Federate the Two Worlds | Covenant expansion | Founds the Two-World Federation faction; compact partners join now and on later acceptance | `dhrondan_two_world_federation_ready`, Event .49 |
| Offer a Shared Horizon | Crisis | Disconnected enclaves that are cores count as supported for resolving the crisis | `dhrondan_enclave_reconciliation_chosen`, `dhrondan_all_disconnected_enclaves_supported` |

The Imperial regime fortifies and taxes its landings and annexes by decree, the Synod shortens and refunds its operations, and the Covenant grows through citizenship, councils, consent-based compacts, and a federation.
No reward adds a national spirit: Dual Citizenship is a state modifier, and the Wargame advances the existing military lifecycle.
The Two-World Federation faction uses the deprecated `create_faction` effect, which applies the default faction template when Deeper Factions is active.
Focus IDs, positions, prerequisites, and AI weights are unchanged.

## Cross-system hooks

The focus tree exposes `dhrondan_reclamation_declared`, `dhrondan_integration_started`, `dhrondan_enclave_crisis_active`, and `dhrondan_enclave_crisis_resolved` for the integration, reclamation, and enclave-crisis consumers.
It also exposes `dhrondan_world_order_decisions_unlocked`, `dhrondan_world_order_claim_contract_ready`, and route-specific settlement flags for later decision or event work.
Restore the Imperial Reaches adds claims on lost landing states, and Crown the Enclave Empire cores the landing states the Imperial Continuity holds; no focus transfers ownership of a state.

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
Live acceptance remains for the land-fort placement on border provinces, the starting efficiency of the laser production line, the federation faction under Deeper Factions, and the per-landing results.
The event owner can attach enclave reactions and settlement reports to the stable route and crisis flags.
The asset owner can produce the registered family icon set without renaming gameplay identifiers or paths.
External runtime acceptance remains necessary for release-time tree loading, cosmetic transitions, paid-landing consumption, and state-dependent factory placement.
