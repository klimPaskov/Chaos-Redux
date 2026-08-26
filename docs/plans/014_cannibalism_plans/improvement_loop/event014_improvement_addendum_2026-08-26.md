# Event 014 Improvement Addendum, 2026-08-26

Status: plan-only accept-or-reject handoff with one narrow design-spec disposition.

Broad expansion remains closed.

This addendum does not authorize gameplay, localisation, asset, GUI, focus, decision, model, portrait, audio, spreadsheet, or cleanup-document edits.

## Executive verdict

The current Event 014 implementation has no newly proven gameplay-depth gap in counterplay, cross-event mechanics, AI behavior, resource pressure, route identity, or lifecycle cleanup.

One narrow specification gap remains under unit identity and progression.

The implemented Warlord and unified Bone Guard action is a fixed three-stage elite contract: the first successful payment fields Bone Riders, the second fields a Scavenged Elephant Column, and later successful payments field ordinary Bone Guards.

All three outcomes count against the shared Bone Guard raised counter and cap.

Current source and player-facing localisation explain that sequence, but the accepted source specs still summarize the action only as `recruit Bone Guard` and do not state the shared-cap consequence.

The recommended disposition is **ACCEPT AND PROMOTE** the existing compact sequence as the intended progression contract without changing gameplay.

If the parent rejects that recommendation, Event 014 should remain incomplete until a separately scoped replacement is accepted because splitting the three outcomes would change decision density, costs, AI, caps, triggers, localisation, and validation rather than merely clarify documentation.

No Event 014 custom 3D work should be reopened.

The 2026-08-26 parent decision that Bone Riders use vanilla `sprite = cavalry` and Network Cadre use vanilla `sprite = infantry` is current authority and removes both old custom-model jobs from the acceptance surface.

## Prior-addendum reconciliation

| Prior plan | Current disposition | Treatment in this addendum |
| --- | --- | --- |
| `2026-07-12_event014_focus_closure_addendum.md` | Its accepted focus findings were implemented, promoted, audited, and closed. | Not repeated. |
| `2026-07-12_event014_post_implementation_closure_addendum.md` | Technology-union and decision-icon work was implemented and promoted. Cross-origin joint operations, route-aware recovery case files, and inspection-access compacts remain explicitly queued, unaccepted, and nonblocking. | Queued optional ideas remain outside this pass and are not reopened. |
| `2026-07-22_event014_gui_focus_improvement_loop_audit.md` | No new GUI or focus expansion was justified. | Closure conclusion retained. |
| `2026-08-25_event014_runtime_closure_handoff.md` | Its broad anti-bloat verdict remains valid. Its two custom-model blockers were superseded by the 2026-08-26 vanilla-visual reuse decision. | Broad closure retained and stale model blockers discarded. |

No accepted prior addendum remains unresolved.

The three optional ideas above are properly queued with a reason, so they do not block this bounded pass and must not be duplicated here.

## Evidence boundary

This conclusion uses the accepted Event 014 specs, current source, current package ledgers, prior bounded MCP artifacts, and fresh read-only MCP attempts.

The main implementation evidence is in these files:

- `common/units/014_cannibalism_irregular_infantry.txt`
- `common/technologies/014_cannibalism_irregular_activation_technologies.txt`
- `common/scripted_effects/014_cannibalism_activation_effects.txt`
- `common/scripted_effects/014_cannibalism_effects.txt`
- `common/scripted_triggers/014_cannibalism_triggers.txt`
- `common/script_constants/014_cannibalism_constants.txt`
- `common/decisions/014_cannibalism_decisions.txt`
- `common/decisions/categories/014_cannibalism_categories.txt`
- `common/national_focus/014_cannibalism_focus.txt`
- `common/ai_strategy/014_cannibalism_warlords.txt`
- `common/mtth/014_cannibalism_mtth.txt`
- `events/014_cannibalism.txt`

The relevant source-spec surfaces are:

- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_4_country_packages.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_6_decisions_missions_and_gui.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_9_ai_balance_and_integrations.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_12_acceptance_criteria.md`

The offline wiki and installed vanilla documentation were used for events, effects, triggers, modifiers, scopes, decisions, focuses, AI, units, and lifecycle behavior.

The concrete vanilla unit precedents are `common/units/cavalry.txt#elephantry`, `common/technologies/infantry.txt#elephantry`, ordinary infantry equipment speed, cavalry categories, locked template behavior, and standard AI strategy structures under the installed game root.

No external historical claim or new regional identity is introduced by this addendum.

The three accepted origin identities already provide the useful regional connection: Island Host emphasizes ports, convoys, amphibious movement, and Reavers, Siege Commune emphasizes cities, forts, relief routes, and Siege Eaters, and March Host emphasizes rail, depots, motorization, and March Predation Columns.

Adding culture-specific dress, ritual, or another regional origin would weaken the established fictional and culture-neutral horror boundary.

## MCP evidence and exact limitations

The fresh read-only event inspection of `chaosx.nr14.1` returned `EVENT_INSPECTED_PARTIAL` in workspace `mod_chaos_redux_ea3b2d67c2c0`, revision `43388d6b2737a1c8e2409f324449210941414fee69c903a1c69d441ca9d33b97c`, graph hash `dd30c3585ea090f05881b49253cfb4212d58091d19729649a292f8ed561ed67c`, and zero blocking diagnostics in the selected boundary.

The event result remains partial because the large workspace deferred helper and lifecycle projections.

The fresh event render timed out after 180 seconds and produced no current render artifact.

Fresh focus inspect and focus render requests for the Event 014 Warlord tree each timed out after 180 seconds.

Prior 2026-08-25 read-only MCP evidence remains available for all three clean Event 014 focus trees with 108 unified focuses, 68 Warlord focuses, 28 Wendigo focuses, and zero crossing or blocking diagnostics, but it is not a substitute for a fresh post-change engine pass.

The fresh `hoi4.probability_inspect` request for `common/decisions/014_cannibalism_decisions.txt` accepted the source contract and then timed out after 180 seconds.

The weighted conclusion was routed to `chaosx_ai_probability_auditor` as required.

No probability compare is authorized because this addendum proposes no weight, factor, gate, or callback change.

The installed package has no Technology Tree Viewer.

The nine hidden activation technologies can be inspected in source, but no fresh technology-tree inspect or render conclusion can be claimed from the currently installed MCP route.

No GUI or map surface is proposed by this addendum, so no GUI or map rewrite, inspection, or render was added to its scope.

No rewrite tool was used.

## Disposition register

| ID | Surface | Disposition recommendation | Implementation owner | Exact implementation IDs and files | Completion effect |
| --- | --- | --- | --- | --- | --- |
| `E014-IL-U1` | Bone Guard elite-contract ordering and shared cap | **ACCEPT AND PROMOTE** the current fixed sequence. Do not split it by default. | Parent Event 014 formation and decision owner for acceptance. Documentation curator for spec promotion after acceptance. | `cannibalism_raise_bone_guard`, `cannibalism_unified_raise_bone_guard`, `cannibalism_execute_warlord_recruitment_transaction`, `cannibalism_unified_execute_recruitment`, `cannibalism_warlord_bone_riders_open`, `cannibalism_warlord_elephantry_open`, `cannibalism_unified_bone_riders_open`, `cannibalism_unified_elephantry_open`, `cannibalism_bone_guard_raised`, `cannibalism_unified_bone_guards_raised`, and `cannibalism_unit_cap.bone_guard_base` or `.bone_guard_upgraded` in the decision, effect, trigger, and constant files listed above. | If accepted, no gameplay change is required. Promote the contract into spec parts 4, 6, and 12. If rejected, queue a new bounded implementation plan and do not claim completion. |
| `E014-IL-C1` | Additional unit-specific counterplay actions | **REJECT** broad expansion. | Parent decision owner only if a later audit proves a specific exploit. | Existing containment and counterwar IDs include `cannibalism_blockade_island_host`, `cannibalism_land_against_island_host`, `cannibalism_rescue_island_host_survivors`, `cannibalism_break_ritual_economy`, `cannibalism_liberate_feeding_state`, `cannibalism_break_network_mission`, `cannibalism_stop_unification_mission`, `cannibalism_stop_transformation_mission`, `cannibalism_identify_transformation_anchor`, `cannibalism_break_wendigo_recruitment_site`, and `cannibalism_break_wendigo_terminal_hunt`. | No new decision, mission, modifier, or GUI row should be added. Preserve current action-density limits. |
| `E014-IL-X1` | Additional cross-event mechanics | **REJECT** broad expansion and retain current bounded integrations. | Parent Event 014 owner and Event 019 registry owner for final evidence only. | Deaths transaction helpers, Event 10 wasteland exclusion, Event 2 Wendigo merge, Chaos Meter milestones, and Event 019 provider `523` through `cannibalism_register_event19_provider` and `chaos_unit_family_provider_523_event19_*`. | No new event coupling should be accepted. Provider normalization and lifecycle proof remain evidence blockers rather than design invitations. |
| `E014-IL-A1` | AI rebalance or new unit AI layer | **QUEUE EVIDENCE ONLY** and reject a speculative patch. | `chaosx_ai_probability_auditor` for read-only evidence. Parent AI owner only if a defect is proven. | `common/ai_strategy/014_cannibalism_warlords.txt`, `common/mtth/014_cannibalism_mtth.txt`, decision `ai_will_do`, focus `ai_will_do`, Event 019 provider weight `chaos_unit_family_event14_cannibal_irregulars.spawn_weight`, and provider `523` eligibility callbacks. | No weight changes are authorized. Any later patch requires the same named scenarios and a mandatory probability compare. |
| `E014-IL-R1` | New resource, upkeep meter, or specialist currency | **REJECT** expansion and accept the existing resource stack with `E014-IL-U1`. | Parent balance owner for final scenario checks. | `cannibalism_unit_cost`, `cannibalism_unit_cap`, the `cannibalism_warlord_can_pay_*` triggers, exact Deaths-backed recruitment, Larder payment, stockpile reserve gates, state cooldowns, and real unit reinforcement needs. | Do not add another currency or passive upkeep loop. Clarify in the promoted contract that equipment is a held reserve gate and then fills the empty spawned formation through ordinary reinforcement. |
| `E014-IL-RT1` | New route-specific unit branches or focus routes | **REJECT** expansion. | Parent focus owner for final MCP evidence only. | `cannibalism_warlord_train_the_origin_specialists`, `cannibalism_warlord_raise_the_bone_guard`, `cannibalism_warlord_train_network_cadres`, `cannibalism_warlord_open_the_courier_routes`, the three mutually exclusive network choices, and their scripted-effect helpers. | Preserve the Island, Siege, March, hierarchy, Larder, and network identities. Do not add a fourth origin or another focus family. |
| `E014-IL-L1` | New lifecycle subsystem | **QUEUE FINAL EVIDENCE ONLY** and reject a new cleanup layer. | Parent completion auditor and Event 019 owner. | `cannibalism_clear_all_current_country_mission_runtime`, `cannibalism_reset_current_country_incarnation_state`, `cannibalism_rollback_current_warlord_creation`, `cannibalism_begin_current_warlord_slot_release`, `cannibalism_reset_event014_activation_technologies`, the ten `delete_unit_template_and_units` calls, `cannibalism_cleanup_complete`, and provider `523` management or cleanup callbacks. | Existing cleanup architecture is sufficient in source. Completion still requires bounded evidence for failure, release, global victory, and Event 019 ownership transitions. |

## `E014-IL-U1` acceptance contract

The current compact sequence should be accepted only with all of the following facts made explicit in the promoted source specs:

1. Completing `cannibalism_warlord_bind_the_guard_to_one_mouth`, `cannibalism_warlord_raise_the_bone_guard`, or the matching unified focus opens a paid contract and does not grant a free unit.
2. The first successful Warlord or unified Bone Guard contract fields Bone Riders and consumes the corresponding `*_bone_riders_open` flag.
3. The second successful contract fields the Scavenged Elephant Column and consumes the corresponding `*_elephantry_open` flag.
4. Later successful contracts field ordinary Bone Guards.
5. Every outcome increments the shared Bone Guard raised counter.
6. The base Warlord Bone Guard cap is two, so the first cap band is deliberately exhausted by Bone Riders and the elephant column. Ordinary Bone Guards appear only after a cap upgrade permits later contracts.
7. The shared Bone Guard Larder, exact population, infantry, support, and artillery threshold is an elite logistics gate for all three outcomes rather than three hidden per-template prices.
8. Units begin with zero equipment and zero manpower, exact Deaths-backed population is converted only after the transaction succeeds, Larder is paid, and ordinary reinforcement draws from the held equipment stockpile.
9. Failed or partial population transactions do not consume either sequence flag.
10. Reusable-slot rollback and release clear both Warlord sequence and transaction flags, delete all ten locked templates, and reset the nine Event 014 activation technologies without resetting vanilla `elephantry`.

This accepted contract preserves a compact six-action Warlord baseline and six-action unified recruitment phase.

It also turns the apparently generic Bone Guard action into visible progression instead of adding two more decisions that would exceed the accepted action-density budget.

If the parent rejects any of points 2 through 7, `E014-IL-U1` must be marked rejected and replaced by a new scoped plan before implementation.

That replacement would need to define whether the outcomes become separate decisions, one state-aware selector, mutually exclusive route choices, or separate cap and cost pools.

This addendum does not choose among those rejected-contract replacements because doing so would be a broader redesign.

## Unit identity and progression finding

The nine custom families already have distinct battlefield identities rather than renamed vanilla infantry.

Scavenger Warband is a cheap raider, Feast Guard is a defensive command cadre, Feast Cohort is an assault line, Bone Guard is an elite fort and urban breacher, Bone Riders is fast low-organisation shock cavalry, Island Reavers is the amphibious specialist, Siege Eaters is the fortified-position breacher, March Predation Column is the fastest motorized pursuit formation, and Network Cadre is a small courier and seeding formation.

All share high attack or movement, low maximum organisation and strength, poor defensive staying power, low reliability, and supply pressure.

The hidden activation technology and locked-template architecture gives real progression gates through `cannibalism_unlock_event014_warlord_package_subunits`, `cannibalism_unlock_event014_warlord_feast_cohort`, `cannibalism_unlock_event014_warlord_bone_guard`, `cannibalism_unlock_event014_warlord_origin_specialist`, `cannibalism_unlock_event014_warlord_network_cadre`, and the unified or Wendigo variants.

No tenth custom family, upgrade technology tree, equipment archetype, or unit-owned GUI is justified.

The Technology Tree Viewer limitation leaves fresh engine visualization of the nine hidden bridge technologies unresolved, but source inspection does not identify a missing activation or cleanup path.

## Counterplay finding

The custom formations already carry inherent battlefield counterplay through low organisation, low strength, poor defence, poor reliability, terrain penalties, fuel or motorized gates where relevant, and unusually high supply pressure.

The event layer adds strategic counterplay through blockade, landing, rescue, victim recovery, ritual-economy disruption, feeding-state liberation, network destruction, unification interruption, anchor identification, recruitment-site destruction, and terminal-hunt counterpressure.

A new anti-Bone-Rider, anti-Cadre, or anti-elephant decision would duplicate ordinary combat, logistics, and existing containment actions.

The recommended disposition is to reject new unit-specific counterplay and validate the existing weaknesses under representative terrain and supply states.

## Cross-event finding

The required cross-event connections are already bounded.

Deaths owns exact population-loss receipts, Event 10 wastelands remain unusable Larder without copying instant island destruction, Event 2 supplies the existing Wendigo country for the alternate terminal merge, Chaos Meter uses milestones rather than daily inflation, and Event 019 provider `523` exposes one spawn-only family lot without copying Event 014 stages, countries, leaders, or progression.

Provider `523` requires `cannibalism_system_active`, rejects `cannibalism_cleanup_complete`, marks native eligibility only for an Event 014 cannibal country, keeps Evolution IV nonnative, forbids training, and disables new spawn or sustainment management after Event 014 cleanup.

Its normalized provider share and complete lifecycle cannot be proven by the installed probability adapter because the dynamic registry and meta-dispatched callbacks are unresolved.

That is an evidence blocker, not a reason to add another cross-event system.

The recommendation is to retain the current provider contract and reject further event coupling.

## AI finding

The current AI package already covers army construction, infantry and support equipment, origin-specific convoy, artillery, motorized, fort, naval-base, and infrastructure priorities, focus-route preferences, decision affordability, and unified or Wendigo target scoring.

The prior completed probability audit found no P0 through P3 balance defect and recorded exact conditional pools only where normalization was supported.

The fixed elite sequence creates no extra AI choice because Bone Riders, the elephant column, and Bone Guards share one paid action and one cap.

No unit-specific AI decision layer is needed unless a later audit proves that the AI repeatedly opens the route without meeting its Larder, state-population, or stockpile threshold.

The fresh decision probability inspect timed out and the required current auditor pass is therefore an open evidence gate.

No AI patch is authorized by this addendum.

## Resource-pressure finding

The event already uses Larder, exact state population, Deaths receipts, infantry equipment, support equipment, artillery, motorized equipment, convoys, fuel, command power, army experience, state control, recruitment cooldowns, formation caps, and the finite productivity of consumed states.

The elite sequence's shared gate is expensive enough to remain rare and communicates that the Host must hold a complete elite logistics reserve before any specialist contract can resolve.

The spawned formations begin empty, so the held reserve is not a free equipment grant and is still drawn down by ordinary reinforcement.

Another resource or per-unit upkeep meter would duplicate Larder, supply, equipment, and cap pressure.

The recommendation is to reject a new resource system and promote the shared-gate interpretation with `E014-IL-U1`.

## Route-specific-choice finding

Route identity is already carried by three origin overlays, three hierarchy branches, three Larder branches, and three Evolution II network choices.

Origin specialist recruitment maps directly to Island Reavers, Siege Eaters, or March Predation Column.

Network Cadre recruitment is tied to the network progression and receives route-aware AI preference.

The elite Bone Riders and Scavenged Elephant sequence is deliberately shared rather than a fourth origin or route.

Adding a Bone Rider branch, elephant branch, or fourth origin would dilute the established route map and create another focus and decision maintenance surface.

The recommendation is to reject new route-specific expansion.

The fresh focus MCP timeout means the parent must retain the final focus evidence gate and must not treat this source review as a fresh engine-rendered route proof.

## Lifecycle-cleanup finding

Current source has dedicated cleanup for mission runtime, reusable country incarnation flags and variables, focus contracts, activation technologies, ten locked unit templates, spread ledgers, arrays, event targets, and global terminal state.

Warlord rollback and slot release clear `cannibalism_warlord_bone_riders_open`, `cannibalism_warlord_elephantry_open`, `cannibalism_warlord_bone_riders_transaction_active`, and `cannibalism_warlord_elephantry_transaction_active` before the slot can be reused.

Provider `523` has no Event 014 derivative additions, so its provider-specific derivative cleanup callbacks are intentional no-ops while Event 019 retains generic ownership of its generated lot and ledger cleanup.

No new cleanup subsystem is justified.

The parent should keep lifecycle validation open until bounded failure and cleanup scenarios prove the current source contract.

## Required final scenarios

These are evidence scenarios, not new mechanic proposals:

1. A Warlord opens the elite route, completes one valid paid contract, fields Bone Riders, increments `cannibalism_bone_guard_raised`, and leaves the elephant flag available.
2. The same Warlord completes the second valid contract, fields the Scavenged Elephant Column, increments the same raised counter, and reaches the base cap of two.
3. The base-cap Warlord cannot field an ordinary Bone Guard until `cannibalism_warlord_bone_guard_cap_upgraded` raises the cap to five.
4. A failed exact population transaction leaves Larder, counters, and both sequence flags unchanged.
5. The unified route repeats the same Rider, elephant, Bone Guard ordering through `cannibalism_unified_execute_recruitment` and `cannibalism_unified_bone_guards_raised`.
6. Warlord rollback or reusable-slot release clears both sequence flags, both transaction flags, all ten locked templates, and the nine Event 014 bridge technologies.
7. Event 019 provider `523` is spawn-only, enters native automatic selection only for an Event 014 cannibal country, remains nonnative under Evolution IV alone, and stops new spawn or sustainment management after `cannibalism_cleanup_complete`.
8. Island, Siege, and March AI preserve their origin focus and operation preferences under low and adequate Larder scenarios without starving route completion.
9. Bone Riders and March Predation Columns lose their advantage when stalled by poor supply, unfavorable terrain, or inadequate fuel and motorized support.
10. The current event, focus, decision, mission, AI, and lifecycle surfaces receive fresh bounded MCP evidence where the installed adapters support them.

## Scope that should not be added

- No tenth custom unit family.
- No fourth origin.
- No Bone Rider or Network Cadre custom model reopening.
- No custom elephant model, counter, equipment archetype, or sub-unit.
- No unit-owned scripted GUI.
- No additional anti-unit decision category.
- No new Larder-adjacent currency or upkeep meter.
- No new cross-event cluster membership.
- No speculative AI weight patch.
- No second cleanup framework.

## Promotion and closure rule

This file should remain under `docs/plans/014_cannibalism_plans/improvement_loop/` until the parent explicitly accepts or rejects `E014-IL-U1`.

If accepted, promote the fixed sequence, shared-cap consequence, shared logistics gate, and failure or cleanup guarantees into spec parts 4, 6, and 12, then mark this addendum implemented and promoted without changing gameplay.

If rejected, keep this addendum as the rejection record and create one new bounded replacement plan before touching decision, trigger, constant, AI, localisation, or action-density surfaces.

After `E014-IL-U1` is disposed and the queued MCP, probability, lifecycle, live-consumer, and parent-review gates are resolved, another broad improvement-loop pass should not be run.

The parent should finish final validation and mark the Event 014 goal complete only if no audit blocker, unaccepted replacement plan, or unresolved accepted addendum remains.

## Parent handoff

Design problem: the current fixed Bone Guard elite-contract progression is implemented and localized but not fully promoted into the accepted source specs, especially the fact that its base cap of two is consumed by Bone Riders and the Scavenged Elephant Column before ordinary Bone Guards become available.

Proposed disposition: **ACCEPT AND PROMOTE `E014-IL-U1`**, reject all broad expansions in `E014-IL-C1`, `E014-IL-X1`, `E014-IL-R1`, and `E014-IL-RT1`, and queue evidence-only closure work in `E014-IL-A1` and `E014-IL-L1`.

Research basis: current Event 014 source, accepted specs, current handoffs and ledgers, offline wiki guidance, installed vanilla documentation, vanilla cavalry and `elephantry` precedents, current read-only MCP evidence, and the required probability-auditor route.

Historical or regional connection: the existing Island, Siege, and March origins already connect geography, logistics, military tradition, and formation identity without borrowing real cultural dress or ritual.

Files written: `docs/plans/014_cannibalism_plans/improvement_loop/event014_improvement_addendum_2026-08-26.md` only.

Implementation surfaces affected if the recommendation is accepted: documentation promotion into spec parts 4, 6, and 12 only.

Implementation surfaces affected if the recommendation is rejected: decisions, triggers, constants, effects, AI, localisation, action-density matrices, and validation, all under a separate accepted plan.

Open questions: parent acceptance or rejection of `E014-IL-U1`, current probability-auditor evidence, fresh event or focus render availability, Event 019 provider normalization and lifecycle evidence, and parent-owned live consumer review.

Prior addendum status: no accepted prior addendum remains unresolved, and the three old optional ideas remain explicitly queued and nonblocking.

Plan promotion status: keep in `docs/plans` until `E014-IL-U1` is accepted, then promote its contract into `docs/specs` and close this plan.
