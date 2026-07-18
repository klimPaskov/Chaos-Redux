# Event 015 Evolution Consumption Implementation Handoff

Date: 2026-07-15  
Mode: patch-capable bounded implementation, no commit  
Accepted source: Finding 2 / Tranche C of `015_utopia_manifesto_formal_improvement_loop_addendum_2026-07-15.md`, with specification Parts 6 and 7 controlling design and AI.

## Outcome

The five accepted evolution events retain their staged delivery and their existing fifteen choices. Every choice now enters one idempotent interpretation setup dispatcher, exposes one paid interpretation-specific policy action, changes one existing Event 015 system when the action begins, and changes a second existing system when the shared obligation mission resolves.

No evolution stage, alternate reserve system, contradiction meter, free territory, free core, free division, or free equipment grant was added.

## Files changed

New isolated implementation files:

- `common/script_constants/015_utopia_manifesto_evolution_consumption_constants.txt`
- `common/scripted_triggers/015_utopia_manifesto_evolution_consumption_triggers.txt`
- `common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt`
- `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt`
- `localisation/english/015_utopia_manifesto_evolution_consumption_l_english.yml`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/evolution_consumption_implementation_handoff.md`

Minimal shared-file integration:

- `events/015_utopia_manifesto.txt`
  - events `chaosx.nr15.100` through `chaosx.nr15.104` call `utopia_manifesto_apply_prepared_evolution_choice`
  - each option has a visible consequence tooltip
  - static-only option weighting was replaced by route- and state-aware modifiers
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
  - `utopia_manifesto_consume_prefire_evolution_state` consumes an explicit prepared prefire choice token after the setting snapshot is translated
  - all five route setters retry any route-dependent prepared Perfect Island token immediately after the route becomes authoritative
  - `utopia_manifesto_clear_evolution_runtime` calls the evolution-consumption terminal cleanup
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
  - `utopia_manifesto_case_has_lawful_ladder_exception` rejects its crisis bypass while `utopia_manifesto_necessary_shores_peaceful_priority` is active, so the existing lease, settlement, joint-administration, association, and ultimatum gates must read their real attempted-step prerequisites
  - `utopia_manifesto_has_district_aftermath` reads the live completion variable `utopia_manifesto_completed_district_projects`, matching the five decision checks and the increment in `utopia_manifesto_complete_garden_district`

## Shared setup and prefire equivalence

Active delivery prepares `utopia_manifesto_evolution_choice_input` and calls `utopia_manifesto_apply_prepared_evolution_choice`.

The explicit prefire API accepts a generic country variable, `utopia_manifesto_prefire_evolution_choice`, or one explicit token per stage: `utopia_manifesto_prefire_glosses_choice`, `utopia_manifesto_prefire_shores_choice`, `utopia_manifesto_prefire_cities_choice`, `utopia_manifesto_prefire_nowhere_choice`, and `utopia_manifesto_prefire_perfect_choice`. At acceptance, `utopia_manifesto_consume_prepared_prefire_evolution_choice` consumes each supplied route-independent token, validates its live delivery gate, copies it into the same temporary input, calls the same setup dispatcher, and records only the corresponding evolution after setup succeeds. A Perfect Island token is retained while the route is unresolved, then retried by the selected route's setter. Closed Order is accepted only for Closed Island; Refuge Network is accepted only for a non-Closed route; Bounded Self-Sufficiency remains valid for every resolved route.

Ordinary prefire setting flags are not treated as delivered choices. This preserves the existing staged popups: enabling an evolution does not silently choose or record it. The explicit token currently has no producer in the Event 015 snapshot; it is the bounded consumption API for a settings or scenario path that actually supplies a choice.

Five setup markers enforce first-choice-wins behavior. Repeating the same prepared choice is idempotent and does not repeat the original Ledger or League movement. A conflicting later token cannot replace the accepted interpretation.

## Fifteen choice consumers

| Choice flag | Consumer 1: paid action begins | Consumer 2: obligation resolves |
| --- | --- | --- |
| `utopia_manifesto_interpretation_schools_open` | Public audit raises Concord and lowers Assignment | Learning and Care calling pressure receives durable Open Call relief; public audit completion is recorded |
| `utopia_manifesto_interpretation_schools_chartered` | Charter consolidation raises Concord and lowers Assignment | Civic Works pressure receives guaranteed-placement relief; consolidation is recorded |
| `utopia_manifesto_conduct_margins_censored` | Enforcement activates censorship, raises Assignment, and lowers Concord | Cooperative institutions resist at a Concord cost; weak institutions receive the existing data-scandal state |
| `utopia_manifesto_necessary_shores_domestic_alternative` | An active case gains integrity and local support | The active case family receives calling relief and Need falls |
| `utopia_manifesto_necessary_shores_peaceful_priority` | An active case gains integrity and local support; the crisis exception can no longer bypass the existing offer ladder | Peaceful steps are restored, Concord rises, and Assignment falls |
| `utopia_manifesto_necessary_shores_emergency_powers` | An active case trades integrity for local support and Assignment | Concord falls, foreign shortcut opposition is recorded, and an unlocked League loses cohesion |
| `utopia_manifesto_cities_local_charters` | The existing garden-district network is linked and Concord rises | Civic Works pressure falls; an unlocked League gains voluntary cohesion |
| `utopia_manifesto_cities_linked_standard` | The existing district network is linked while Plenty and Assignment rise | Workshop pressure falls; existing data suppression converts into the existing data scandal |
| `utopia_manifesto_cities_foreign_circle` | League cohesion rises | Maritime and Settlement pressure falls and Concord rises |
| `utopia_manifesto_nowhere_law_plural` | Voluntary League cohesion rises | Concord rises, Assignment falls, and the plural obligation is recorded |
| `utopia_manifesto_nowhere_law_sponsored` | Plenty rises while sponsor dependence lowers League cohesion | A written-sponsor obligation spends Plenty and restores cohesion; losing accepted sponsorship cancels it |
| `utopia_manifesto_nowhere_law_route_propaganda` | Assignment rises and Concord falls | Condemnation is recorded and League cohesion falls |
| `utopia_manifesto_perfect_island_refuge_network` | Refuge intake lowers Need, raises Concord, lowers Assignment, and opens an intake obligation | Maritime and Settlement pressure falls while ongoing aid consumes Plenty |
| `utopia_manifesto_perfect_island_bounded_self_sufficiency` | A higher reserve target raises Plenty and Assignment | Provisioning pressure falls; a secure live reserve lowers Need, while an insecure reserve costs Concord |
| `utopia_manifesto_perfect_island_closed_order` | Closed enforcement raises Plenty and Assignment, lowers Concord, and records confinement and reserve hoarding | Defense and Watches pressure falls through assignment; weak Concord causes the existing Assignment Revolt, otherwise an unlocked League loses cohesion |

The action itself is the later player choice. The dynamically timed mission is its second later outcome. Both are gated by the original option flag and current stage support.

## Costs and timing

All actions pay the displayed political-power cost plus one shared material profile through `utopia_manifesto_pay_prepared_decision_cost`:

- civic: 50 support equipment
- transport: 50 support equipment and 5 trains
- diplomatic: 50 support equipment and 10 convoys
- control: 50 support equipment and 10 command power
- security: 500 infantry equipment, 50 support equipment, and 10 command power
- refuge: 100 support equipment, 20 convoys, and 5 trains
- closed order: 1,000 infantry equipment, 50 support equipment, 20 command power, and 2% stability

Affordability uses the negation of a strict shortfall check, so a stockpile exactly equal to the displayed amount is sufficient and the payment effect deducts that same amount.

The shared mission duration is prepared before activation through the existing dynamic duration families:

- Glosses: survey duration
- Necessary Shores: case duration
- Cities: district duration
- Nowhere: League duration
- Perfect Island: island duration

Those helpers already account for war, country size, live Plenty, live Concord, and relevant public offices.

## AI behavior

Evolution options and their unlocked actions use the same preference triggers. Weighting reads:

- selected and preferred route
- Need, Plenty, Concord, and reserve security
- war, occupation, and surrender pressure
- the active Necessary Ground method and prior ladder conduct
- district-network and infrastructure state
- faction, accepted sponsorship, League cohesion, and prior aid conduct
- migration pressure, censorship, data suppression, and foreign opposition

Extreme censorship, emergency, propaganda, and Closed Order interpretations receive crisis multipliers and strong penalties under trusted Concord. Sponsored law is blocked for AI without an accepted written sponsor. Closed Order remains route-locked.

Foreign Municipal Circle remains visible after Cities of One Measure but cannot be purchased until both the district and League systems are unlocked. Its immediate cohesion gain therefore cannot be overwritten by later League initialization.

The repository exposes no Event 015 world-chaos scalar. The accepted actor-scoped crisis inputs—war, occupation, surrender, Need, reserve security, and prior coercive conduct—supply the high-chaos state without a world iteration or a parallel meter.

## Cleanup and disable safety

- Every decision visibility block rechecks its stage delivery gate, so disabling a stage hides its temporary action.
- The shared mission cancel trigger rechecks acceptance, constitutional-crisis state, the chosen flag, the live stage gate, its supporting Event 015 subsystem, and route/sponsor constraints.
- Necessary Shores obligations cancel when their active case closes.
- Sponsored obligations cancel when accepted sponsorship disappears.
- Refuge obligations cancel under Closed Island; Closed Order obligations cancel outside Closed Island.
- Terminal evolution cleanup removes the shared mission, clears its action variables, clears all fifteen option flags and five setup markers, clears the generic and five stage-specific explicit prefire tokens, and clears internal obligation/result flags.
- Durable historical conduct and existing scandal/revolt states remain owned by their established Event 015 resolution and achievement lifecycles.

## Localisation and icons

The isolated English localisation file is UTF-8 with BOM, uses no `:0` keys, and supplies:

- 15 evolution-option consequence tooltips
- 15 decision names, descriptions, and effect tooltips
- 7 complete custom-cost localisation triplets
- the shared mission name, description, and timeout tooltip

No new visual asset was required. The decisions reuse already registered Event 015 sprites:

- `GFX_decision_utopia_publish_accounts`
- `GFX_decision_utopia_constitutional_correction`
- `GFX_decision_utopia_just_cause_review`
- `GFX_decision_utopia_need_case`
- `GFX_decision_utopia_boundary_arbitration`
- `GFX_decision_utopia_ultimatum`
- `GFX_decision_utopia_district_foundation`
- `GFX_decision_utopia_technical_mission`
- `GFX_decision_utopia_recognize_friend`
- `GFX_decision_utopia_league_aid_corridor`
- `GFX_decision_utopia_send_magistrates`
- `GFX_decision_utopia_common_harbor`
- `GFX_decision_utopia_seasonal_reserve`
- `GFX_decision_utopia_household_guard`

No `.gfx` edit or sprite handoff is needed.

## Validation performed

- All fifteen exact option flags have a setup reference, lifecycle gate, visible decision reference, and terminal cleanup reference.
- All fifteen event options call the same setup dispatcher and have a matching visible tooltip.
- The isolated decision file defines 15 decisions and one shared mission; all names, descriptions, custom tooltips, and cost keys resolve in English localisation.
- All seven material profiles match their payment branches and displayed amounts.
- Script constants referenced by the tranche resolve, and every direct Event 015 scripted effect/trigger call resolves to a definition.
- Necessary Shores ordering proof: `utopia_manifesto_case_can_offer_lease` and `utopia_manifesto_case_can_offer_settlement_agreement` require `utopia_manifesto_case_trade_attempted`; joint administration requires a lease or settlement attempt; association requires a joint or settlement attempt; the ultimatum requires the configured peaceful-attempt count and a refusal. Each gate previously shared `utopia_manifesto_case_has_lawful_ladder_exception`; the peaceful-priority flag now disables that bypass, while `utopia_manifesto_record_case_ladder_attempt` remains the sole recorder called by `utopia_manifesto_record_case_offer`.
- District-aftermath variable proof: `utopia_manifesto_complete_garden_district` increments `utopia_manifesto_completed_district_projects`, and the five district decision checks plus `utopia_manifesto_has_district_aftermath` now read that same identifier; the stale inverse-word-order identifier has no remaining script reference.
- Independent event-completion audit identified and the implementation resolved three defects: route-unresolved Perfect Island prefire, pre-League Foreign Municipal Circle payment, and exact-balance affordability. Perfect tokens now defer to all five route setters, Foreign Circle requires the live League gate in both availability and mission support, and all seven cost profiles accept equality without unsupported comparison operators.
- The new localisation file has the UTF-8 BOM byte sequence and no duplicate or `:0` keys.
- The touched scripts remain brace-balanced and `git diff --check` reports no tranche whitespace error.
- Vanilla precedent consulted: China's dynamic countryside mission in `common/decisions/CHI_decisions.txt` uses a variable-backed `days_mission_timeout`, hidden availability, cancel handling, and timeout resolution; the shared obligation follows that structure.

## Risks and follow-up suggestions

- Only one evolution policy obligation can run at once. This deliberately prevents overlapping state changes and duplicated mission timers; the other interpretation actions remain available after the active term resolves and their own cooldown allows them.
- Repeated paid actions can accumulate durable calling-policy adjustment until the existing calling clamp is reached. This is intentional long-campaign depth and remains bounded by material cost, political power, cooldown, one-at-a-time operation, and the central calling limits.
- If a future scenario supplies explicit prefire choices, it should set the matching stage-specific token to one valid `constant:utopia_manifesto_evolution_choice.*` value before acceptance. The generic token remains suitable for a single one-off choice. It must not set any choice token merely because a stage is enabled.
- No current Event 015 source produces an explicit prepared choice token, so the deferred Perfect Island path is structurally wired but remains dependent on future scenario/settings integration to exercise it. Terminal cleanup clears a token if no route is ever selected.
- Future depth should alter these consumers or their existing system hooks, not add a sixth evolution stage or a second obligation framework.

## Simplifications, omissions, and blockers

No design simplification, fallback mechanic, omitted choice, missing localisation, missing AI route, or known implementation blocker is present in this tranche. The explicit prefire token is intentionally producer-neutral because the current prefire snapshot represents stage enablement rather than a delivered choice.

## Skills used

- `chaos-redux-events`
- `chaos-redux-improvement-loop`
- `hoi4-decisions-missions`
- `chaos-redux-subagents`

No skill was created or updated.
