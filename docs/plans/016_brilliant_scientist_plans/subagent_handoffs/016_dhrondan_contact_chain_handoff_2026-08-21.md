# Event 016 D’Rhondan contact-chain handoff

## Scope completed

This tranche implements the D’Rhondan envoy craft, guarded project access, Antarctic recovery bypass, Kruger and Mengele expeditions, pact receipt calls, ordinary follow-up events `chaosx.nr16.40` through `.47`, compact pact status, accord maintenance, the country-scoped rebellion pulse, and the stable call into the parent-owned DHR revolt effect.

It does not edit the alien-infantry API definitions, Event 019 providers, unit or equipment definitions, tactics, DHR focus or country-package implementation, visual assets, portraits, models, achievements, or the event catalog.

## Files created

- `common/special_projects/projects/016_dhrondan_envoy_project.txt`
- `common/script_constants/016_dhrondan_contact_constants.txt`
- `common/scripted_triggers/016_dhrondan_contact_triggers.txt`
- `common/scripted_effects/016_dhrondan_contact_effects.txt`
- `common/decisions/categories/016_dhrondan_contact_category.txt`
- `common/decisions/016_dhrondan_contact_decisions.txt`
- `events/016_brilliant_scientist_dhrondan_contact_events.txt`
- `localisation/english/016_dhrondan_contact_l_english.yml`
- `docs/events/016_brilliant_scientist/systems/dhrondan_contact.md`

## Existing files updated

- `common/scripted_effects/016_brilliant_scientist_context_effects.txt` calls the Antarctic craft bypass from the existing artifact-contact reconcile effect.
- `common/scripted_effects/016_brilliant_scientist_effects.txt` cleans an active Kruger expedition before transfer and calls the Antarctic bypass after the successful recipient restores Kruger’s roles.
- `common/scripted_effects/cbrn_project_effects.txt` registers guarded craft completion in `grant_random_chaos_special_project_available_tech`.
- `common/script_constants/germany_mengele_constants.txt` adds the equal Directorate registry weight.
- `common/scripted_effects/germany_mengele_effects.txt` registers the craft in both the random and all-project availability helpers.
- `common/scripted_effects/cbrn_scripted_effects.md` documents the shared selector entry and exact gate.
- `docs/events/germany_mengele/overview.md` documents the Directorate registry entry and the D’Rhondan-specific Rocketry and High Energy mapping.
- `docs/events/016_brilliant_scientist/systems/projects.md` documents the operational gate and both shared random registries.

## Locked contracts

The craft project identifier is `sp_dhrondan_envoy_craft`. Its output uses `dhrondan_complete_envoy_craft = yes`.

Kruger pact success sets temporary `alien_infantry_contact_source_id = constant:alien_infantry_contact_source.kruger_pact` and calls `alien_infantry_grant_contact = yes` once. Mengele success uses `constant:alien_infantry_contact_source.mengele_expedition`. No API definition is duplicated.

Future craft access and future alien-infantry contact are deliberately separate receipts. `dhrondan_envoy_craft_future_event_access` exposes the project route but still requires the accepted five operational domains. `alien_infantry_contact_receipt_future` authorizes the shared equipment and landing API but never exposes or completes the craft. Only `antarctica_success` bypasses craft construction.

The public API owns `dhrondan_landing_state`, `dhrondan_landing_history_recorded`, `dhrondan_arrival_count`, `dhrondan_alien_presence`, `dhrondan_pact_strain`, and generic landing presentation/history. It calls `dhrondan_record_successful_landing = yes` only after generic bookkeeping. The Event 016 callback opens `.44` and refreshes rebellion only for a host with `dhrondan_pact_established`.

The Event 016 route-history flags are `dhrondan_kruger_contact_receipt` and `dhrondan_mengele_contact_receipt`. Pact establishment never zeroes shared landing values, so Event 019 and future-source history survives and can immediately activate the rebellion pulse.

The canonical Kruger one-time receipts are character flags on the fixed `KRG_warren_kruger` token: `dhrondan_kruger_authorization_reward_received`, `dhrondan_kruger_return_reward_received`, and `dhrondan_kruger_pact_completed`. The first two make the existing country flags presentation mirrors rather than authoritative duplicate guards. Kruger expedition availability and continued route validity reject the character pact flag, so transferring the canonical token to a fresh host cannot replay the authorization reward, successful-return reward, or Kruger pact. A failed pre-pact expedition may still be retried by a later host without replaying any reward already carried by the character. The final audience authorizer revalidates the exact Kruger or Mengele route immediately before any successful-return reward, pact flag, receipt, or shared API call; invalid stale audience state reaches `dhrondan_fail_expedition` instead of creating a country pact without the fixed-character receipt.

The country-package bridge is `dhrondan_start_revolt = yes` in the current host COUNTRY scope. The caller never pre-sets `dhrondan_rebellion_bridge_called`. Only the parent-owned verified-success branch sets that receipt after DHR owns a viable marked state. A failed transaction clears the unresolved trigger and refreshes the host’s country pulse for a later retry. Territory, claims, capital, units, stockpile, cohorts, and formation news remain parent-owned.

## Expedition behavior

The player authorizes the expedition through the route decision. There is no second voluntary rejection at the valid planetary audience. Both routes cost exactly 50 Political Power and 500 fuel and activate a 180-day country mission.

Kruger authorization applies Mandate +10, Dependence +10, Exposure +5, Independent Capacity +10, and Grievance -5 once per canonical character history. Successful return applies Mandate +5, Dependence +5, and Independent Capacity +5 once per canonical character history. The fixed `KRG_warren_kruger` token receives `dhrondan_kruger_expedition_obligation`, loses its advisor and scientist roles through the existing helpers, and is restored idempotently on valid success or failure. Transfer removes the active mission and reaches the same failure cleanup before nationality mutation, while the three character receipts travel with the token and prevent cross-host replay.

The Mengele route uses its own mission and contact receipt and never calls either Directorate-measure effect or any Kruger character helper.

Eligible AI countries authorize from the sole `.40` option immediately when they can pay. If affordability is delayed, the decisions use `constant:dhrondan_contact_ai.dominant = 10000`, making the valid expedition effectively dominant over ordinary decision choices.

## Project and access behavior

The craft is an air-specialization project with breakthrough cost 5, very-long prototype time, insane complexity, and 5 each aluminium, tungsten, chromium, and rubber.

Kruger and KRG require operational Alien Arms, Rocketry, High Energy, Computation, and Advanced Materials. The first three use existing operational deployment triggers. Computation and Materials require Deployment or later and reject suspended, damaged, dismantled, or stolen family entries. Prototype flags alone do not pass.

Mengele requires completed Directorate Alien Arms, Materials, and Computation work plus `rocket_engines` and `atomic_research`. This is documented as the accepted D’Rhondan-specific bridge for its missing matching Rocketry and High Energy stage ledgers, not as an identical Event 016 deployment receipt.

An active or later-appointed Kruger host with `antarctica_success` completes the craft exactly once. The narrow callers are the appointment-time artifact reconcile, Event 025’s existing artifact reconcile call, and the successful transfer-recipient reconcile. Event 036 evidence is not read.

## Pact and rebellion behavior

`Honor the D’Rhondan Accord` costs 75 Political Power, subtracts 10 Pact Strain, clamps at zero, and applies a 180-day country cooldown.

The rebellion pulse is a country-scoped 90-day mission. It requires at least six arrivals, Pact Strain 30, and global chaos 600. The resolver applies exactly:

- 10 percent at the qualifying base tier.
- 20 percent for eight or nine arrivals, Pact Strain at least 50, or chaos at least 800, unless the high tier applies.
- 40 percent for at least ten arrivals together with chaos at least 800.

The no-revolt branch is derived from a 100-point total and reactivates the same country’s mission. `dhrondan_refresh_rebellion_pulse` checks `NOT = { has_active_mission = dhrondan_rebellion_pulse_mission }` before assigning the duration and activating, so later landings and Accord actions cannot reset a live 90-day clock. Ineligibility still removes the mission and clears its timer. No daily, weekly, or monthly world scan was added.

## Event and presentation invariants

Events `.40` through `.47` are triggered-only ordinary follow-ups. Source inspection finds each identifier exactly once. No Event Log entry, evolution entry, cluster entry, or catalog row was added. The existing evolution file still contains exactly four evolution report pictures for Evolutions I through IV, and Event 016 remains the existing minor fire-once event.

All code references the locked purpose-built sprites. The generated purpose-built DDS binaries are present through the external art packages. The localisation audit found that the matching project, category, decision, and eight report `.gfx` sprite definitions were not yet present under `interface/`. This remains a parent or asset-owner wiring dependency, and no generic fallback was substituted.

## Validation evidence

Targeted source checks found balanced braces in all seven new Clausewitz files, unique `.40` through `.47` definitions, no prohibited `<=` or `>=`, no global daily, weekly, or monthly scan, the explicit active-mission guard around the sole rebellion-pulse activation site, and a UTF-8 BOM byte sequence `239,187,191` on the new localisation file. Targeted `git diff --check` reported no whitespace errors.

The public API source was inspected after its concurrent implementation. It defines receipt constants 1 and 2, initializes missing landing values without overwriting existing values, performs generic landing bookkeeping before the Event 016 callback, and exposes the state-targeted landing decision separately from this category.

## HOI4 MCP evidence and blocker

The mandatory event inspection route was attempted with the corrected selector `{ kind = event, eventId = chaosx.nr16.40 }`, downstream direction, helper expansion disabled, depth 8, and 80 nodes. `hoi4.event_inspect` failed with `tool call failed for hoi4_agent_tools/hoi4.event_inspect` caused by `timed out awaiting tools/call after 180s`. A namespace trace with `kind = namespace` also timed out after 180 seconds.

The mandatory narrow `.40` options render was attempted with the same event selector, depth 2, and 20 nodes. `hoi4.event_render` failed with `tool call failed for hoi4_agent_tools/hoi4.event_render` caused by `timed out awaiting tools/call after 180s`. The independent event completion auditor’s later narrow render returned `INTERNAL_ERROR` with blocker message `Unexpected internal error`, no artifacts, and failed validation.

These timeouts are recorded as exact blockers. Source review is not treated as equivalent engine evidence.

## Audit handoffs

The read-only probability auditor captured a fresh pre-craft CBRN `random_list` inspection against HEAD `6fe06c2bf438b4396126bd20279a1d6eb2e4a326`. The baseline pool contained eight candidates with weights 10, 10, 8, 6, 8, 8, 8, and 6. The artifact SHA-256 was `9bc8002e578e2bb990a0b6dff1c416313e7550edd775a4e06e05c5e268805ccf`, and the source revision was `0eb674574af1cfac69152c656d5b1f1de3e596e5cc67325640b081609b710f30`. The working change adds the guarded craft at weight 8. The baseline Mengele pool contains twelve equal weight-100 entries, and the change adds the craft as the thirteenth equal entry.

The auditor declared scenarios `E016_DHR_CHAOS_NONE_COMPLETED`, `E016_DHR_CHAOS_ALL_BUT_ONE_COMPLETED`, `DHR_REBELLION_LOW_6_30_600`, `DHR_REBELLION_MEDIUM_8_30_600`, `DHR_REBELLION_HIGH_10_30_800`, `E016_DHR_SHARED_CHAOS_PREPOST_2026_08_21`, `E016_DHR_REBELLION_PULSE_CONTRACT_2026_08_21`, and `E016_DHR_REBELLION_SEQUENCE_2026_08_21`.

Every current post-change probability inspect, evaluate, sweep, compare, and sequence route then timed out after 180 seconds or returned `Transport closed`. A later render returned `PROBABILITY_ANALYSIS_NOT_CACHED`. No post-change probability, ranking, sequence, sensitivity, or comparison artifact is claimed. Decision AI evidence remains source-level score evidence only: expedition base 10000, Honor Accord base 25 and score 100 at Pact Strain 50 or above.

The probability audit identified the boundary with at least ten arrivals, chaos 600 to 799, and Pact Strain 30 to 49. Parent review explicitly locked that state to the 10-percent low tier. The medium arrival clause remains exactly eight or nine, while Pact Strain 50 or chaos 800 still independently activates medium and ten arrivals together with chaos 800 activates high. The current source already implements this ruling without broadening the medium arrival trigger.

The localisation audit handoff is `016_dhrondan_contact_localisation_audit_handoff_2026-08-21.md`. It found all 58 expected keys present and unique, preserved the dynamic Alien Presence and Pact Strain tokens, confirmed the UTF-8 BOM, and patched player-facing text to expose exact expedition, return, accord, and rebellion values without internal receipt, ledger, bookkeeping, or bridge language. Owner review then made three multi-source and precision corrections: `.44` states +1 Alien Presence and +5 Pact Strain, `.45` does not claim all contact is locked after this route fails, and `.46` states the exact six-arrival, 30-strain, and 600-chaos gates. The decision auditor’s low-severity icon-first finding was also resolved by adding the Political Power and fuel texticons to secondary expedition, craft-report, and accord cost prose.

The decision and mission audit handoff is `2026-08-21_dhrondan_decision_mission_audit.md`. It found no P0 or P1 gameplay defect and confirmed the exact route costs, character lifecycle, Mengele isolation, pact API ordering, accord, parent-locked probability tiers, bridge retry, bounded mission lifecycle, and dominant authorization score. Its `hoi4.probability_inspect`, `hoi4.gui_inspect`, and `hoi4.gui_render` attempts each timed out after 180 seconds. No callable `hoi4.decision_inspect` route was exposed.

The decision auditor’s canonical-character follow-up confirmed the authorization and return character guards, host-local mirrors, pact availability lock, and idempotent failed-expedition retry. It identified a conditional stale-audience risk because the final option did not independently revalidate the route. Owner hardening resolved it by requiring the exact Kruger or Mengele remains-valid trigger both at the authorizer boundary and inside route selection, rejecting an already-completed Kruger pact during continued validity, and sending invalid audience state through the ordinary failure cleanup before any reward, pact, receipt, or public API call.

The read-only event completion audit found no remaining material source defect. It confirmed `.40` through `.47` connectivity, both project registries, Antarctic and Event 036 separation, the API/callback boundary, exact pact and rebellion behavior, the safe DHR bridge, Event 016’s sole fire-once registration, exactly Evolutions I through IV, and no cluster registration. It wrote no file because its role was read-only.

## Simplifications, omissions, and blockers

No gameplay simplification or generic visual fallback was introduced. Mandatory event MCP inspect/render evidence is blocked by repeated 180-second server timeouts. Purpose-built DDS binaries exist, but their stable `.gfx` definitions remain an external parent or asset-owner wiring blocker outside this handoff’s edit scope.

No commit was created.
