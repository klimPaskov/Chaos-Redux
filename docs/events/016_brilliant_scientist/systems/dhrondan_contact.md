# Event 016 D’Rhondan contact chain

## Purpose

This system connects the Event 016 and Mengele scientific routes to the source-counted alien-infantry API, then tracks the pact-host state needed by the Empire of D’Rhonda revolt package. Events `chaosx.nr16.40` through `.47` are ordinary follow-up reports. They do not add an Event 016 evolution or cluster.

## Envoy craft

`sp_dhrondan_envoy_craft` is an air-specialization project with breakthrough cost 5, very-long prototype time, insane complexity, and resource costs of 5 aluminium, 5 tungsten, 5 chromium, and 5 rubber. It becomes visible only through an active Kruger host, KRG sovereignty, an eligible Mengele directorate, or the dedicated `dhrondan_envoy_craft_future_event_access` receipt. Every route still requires one of the accepted five-domain operational mappings before construction. `alien_infantry_contact_receipt_future` is separate and authorizes only the shared contact, equipment, and landing API. It does not expose the craft.

The Kruger and KRG gate requires all five operational domains. Alien Arms, Rocketry, and High Energy use their existing operational deployment triggers. Computation and Advanced Materials require Deployment or later and reject suspended, damaged, dismantled, or stolen family ledgers.

The Mengele bridge requires completed Directorate Alien Arms, Materials, and Computation projects together with `rocket_engines` and `atomic_research`. Those two vanilla technologies are the D’Rhondan-specific stand-ins for operational Rocketry and High Energy because the cloned Directorate portfolio has no identical Event 016 stage ledgers for those families. This mapping does not claim an Event 016 deployment receipt.

An active or later-appointed Kruger host with `antarctica_success` completes the craft once through `dhrondan_try_apply_antarctic_craft_bypass`. The narrow callers are the existing alien-artifact contact reconcile path and the successful Kruger transfer-recipient reconcile path. Event 036 spacecraft evidence is never read by this bypass.

The craft is also registered in both shared Chaos Redux random-project registries. `grant_random_chaos_special_project_available_tech` can complete it only when the current country passes the exact route and operational-work gate. `make_random_directorate_special_project_researchable` and `make_all_directorate_special_projects_researchable` expose the separate Mengele availability receipt rather than completing the project.

## Expedition and pact flow

1. Craft completion fires `chaosx.nr16.40` once.
2. The player authorizes either the Kruger or Mengele expedition for 50 Political Power and 500 fuel. This is the pact authorization choice.
3. The Kruger route applies Mandate +10, Dependence +10, Exposure +5, Independent Capacity +10, and Grievance -5 once across the canonical character’s entire transfer history. It suspends the fixed `KRG_warren_kruger` token through the established role helpers and records `dhrondan_kruger_expedition_obligation` on that character.
4. The Mengele route changes none of the Kruger Directorate measures or character state.
5. A country-scoped mission holds the route for 180 days. A valid return fires `chaosx.nr16.42`, whose sole option revalidates the exact route immediately before establishing the pact. Invalid host, death, transfer, stale audience, cancellation, or world-end conditions use the failure cleanup and award no receipt.
6. A successful Kruger return applies another Mandate +5, Dependence +5, and Independent Capacity +5 once across the canonical character’s entire transfer history, restores the same fixed character, records the completed pact on that character, and calls `alien_infantry_grant_contact` with `constant:alien_infantry_contact_source.kruger_pact`.
7. A successful Mengele return calls the same API with `constant:alien_infantry_contact_source.mengele_expedition` and never touches Kruger’s variables.
8. The public alien-infantry API initializes missing `dhrondan_arrival_count`, `dhrondan_alien_presence`, and `dhrondan_pact_strain` values without overwriting landings recorded through Event 019 or future sources. Pact establishment adds only its source receipt and refreshes the country-scoped rebellion pulse against any preserved history.

Eligible AI countries authorize immediately from the sole craft-report option when they can pay both costs. The visible decisions retain `constant:dhrondan_contact_ai.dominant` as a retry score if affordability becomes valid after the report closes. This makes authorization deterministic at the valid report boundary and effectively dominant in the ordinary decision queue without relying on a global scan.

## Landings, accord, and rebellion

The public alien-infantry API owns the state-targeted landing reservation, equipment conservation, cohort spawn, `dhrondan_landing_state`, `dhrondan_landing_history_recorded`, arrival count, Alien Presence, and Pact Strain. After generic bookkeeping, the API calls `dhrondan_record_successful_landing`. That callback opens the Event 016 landing report only for a host with `dhrondan_pact_established` and refreshes its rebellion pulse. Event 019, DHR sovereignty, and future source receipts therefore keep their generic landing bookkeeping and presentation paths without being forced through the pact-only event trigger.

The compact `dhrondan_contact_status_header` displays Alien Presence and Pact Strain. `Honor the D’Rhondan Accord` costs 75 Political Power, subtracts 10 Pact Strain, clamps the value at zero, and applies a 180-day cooldown.

The rebellion resolver is a country-scoped 90-day mission. It becomes eligible only at six arrivals, Pact Strain 30, and chaos 600. The exact roll tiers are:

| Tier | Conditions | Revolt probability per pulse |
| --- | --- | ---: |
| Low | Any eligible state outside the medium and high tiers, including six or seven arrivals at the base gates and at least ten arrivals with chaos 600 to 799 and Pact Strain 30 to 49 | 10 percent |
| Medium | Eight or nine arrivals, Pact Strain at least 50, or chaos at least 800, unless the high tier also applies | 20 percent |
| High | At least ten arrivals and chaos at least 800 | 40 percent |

The resolver checks the high tier before the medium tier and derives the no-revolt weight from a 100-point total. A failed roll reactivates only that host’s mission. Landing and Accord refresh calls never restart an already-active pulse, so each live mission retains its original 90-day deadline. There is no daily, weekly, or monthly country scan.

The otherwise uncovered state with at least ten arrivals, chaos 600 to 799, and Pact Strain 30 to 49 is explicitly locked to the 10-percent low tier. The medium arrival clause remains exactly eight or nine rather than broadening to every value above eight.

On rebellion, `chaosx.nr16.47` calls `dhrondan_start_revolt = yes` in the pact-host country scope. Only the parent-owned verified-success branch sets `dhrondan_rebellion_bridge_called` after DHR exists and owns a viable marked state. If formation cannot commit, the caller clears the unresolved trigger and refreshes the country pulse so the transaction can retry without a false success receipt. The country effect reads the locked landing-state and host ledgers and owns all DHR creation, transfer, claim, capital, unit, stockpile, initial-force, and formation-news side effects.

## Runtime identifiers

- Craft completion: `dhrondan_envoy_craft_completed`
- Pact: `dhrondan_pact_established`
- Event 016 route receipts: `dhrondan_kruger_contact_receipt`, `dhrondan_mengele_contact_receipt`
- Canonical Kruger one-time receipts: `dhrondan_kruger_authorization_reward_received`, `dhrondan_kruger_return_reward_received`, `dhrondan_kruger_pact_completed`
- Public API receipts: `alien_infantry_contact_receipt_kruger_pact`, `alien_infantry_contact_receipt_mengele_expedition`
- Landing states: `dhrondan_landing_state`, `dhrondan_landing_history_recorded`
- Pact-host values: `dhrondan_arrival_count`, `dhrondan_alien_presence`, `dhrondan_pact_strain`
- Rebellion state: `dhrondan_rebellion_triggered`, `dhrondan_rebellion_bridge_called`
- Country-package bridge: `dhrondan_start_revolt = yes`

The three canonical Kruger receipts above live on the fixed `KRG_warren_kruger` character. Country flags for authorization and return remain local mirrors only. A failed pre-pact expedition may be retried after transfer, but the new host cannot replay an authorization reward already carried by the character. Once the character carries `dhrondan_kruger_pact_completed`, no later host can start a second Kruger expedition or receive another Kruger pact.

## Files

- `common/special_projects/projects/016_dhrondan_envoy_project.txt`
- `common/script_constants/016_dhrondan_contact_constants.txt`
- `common/scripted_triggers/016_dhrondan_contact_triggers.txt`
- `common/scripted_effects/016_dhrondan_contact_effects.txt`
- `common/decisions/categories/016_dhrondan_contact_category.txt`
- `common/decisions/016_dhrondan_contact_decisions.txt`
- `events/016_brilliant_scientist_dhrondan_contact_events.txt`
- `localisation/english/016_dhrondan_contact_l_english.yml`

## Icons and report art

The project uses `GFX_sp_dhrondan_envoy_craft`. The decision category uses `GFX_decision_category_dhrondan_contact`. Decisions use `GFX_decision_send_kruger_to_dhronda`, `GFX_decision_send_mengele_to_dhronda`, `GFX_decision_dhrondan_ufo_landing`, and `GFX_decision_honor_dhrondan_accord`.

The event report sprites are:

- `.40`: `GFX_report_event_016_dhrondan_craft_authorized`
- `.41`: `GFX_report_event_016_dhrondan_envoy_departure`
- `.42`: `GFX_report_event_016_dhrondan_planetary_audience`
- `.43`: `GFX_report_event_016_dhrondan_pact_return`
- `.44`: `GFX_report_event_016_dhrondan_ufo_landing`
- `.45`: `GFX_report_event_016_dhrondan_expedition_failure`
- `.46`: `GFX_report_event_016_dhrondan_revolt_warning`
- `.47`: `GFX_report_event_016_dhrondan_rebellion`

## Future plans

- Add future-event craft access only through `dhrondan_envoy_craft_future_event_access` and a separately proven five-domain mapping. Grant any shared alien-infantry access independently through the public future-source receipt. Do not infer either access surface from the other or from unrelated alien evidence.
- Add further pact maintenance choices through the same Pact Strain ledger and country-scoped refresh effect rather than a periodic world scan.
- Keep any later DHR diplomatic or counter-rebellion mechanics behind the parent-owned country-package API so the Event 016 chain never duplicates tag initialization or territorial transfer logic.
