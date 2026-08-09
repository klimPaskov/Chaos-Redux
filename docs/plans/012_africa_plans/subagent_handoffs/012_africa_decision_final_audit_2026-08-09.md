# Event 012 Africa Decision and Mission Final Audit

Audit date: 2026-08-09.

Owner: `event12_decision_final_audit`.

Parent handoff: `/root`.

Scope: Event 012 Africa decision and mission surfaces, action/disease/disaster/diaspora/AI helper files, and narrow Event 012 lifecycle hooks. Focuses, country packages, GUI, localisation, documentation matrices, workbook, assets, and Event 019/shared-provider hunks were outside this audit.

## Accepted narrow patch

The only source file changed by this audit is `common/scripted_effects/012_africa_action_effects.txt`.

The changed helper is `africa_requote_selected_action_against_action_target` (approximately lines 4267–4300 in the audited revision).

Before the patch, the helper cleared the selected quote, rebuilt the action profile and costs, and wrote the action identity, target, family, kernel, phase, target mode, risk, and cost fields, but did not copy `africa_quote_duration_minimum`, `africa_quote_duration_maximum`, `africa_quote_duration_days`, `africa_quote_response_days`, or `africa_quote_objective`.

`africa_clear_action_quote` resets those fields to the instant/none defaults, so a launch-time re-quote could turn a non-instant action into a zero-day quote and discard its response and objective timing.

The helper now copies all five profile fields before setting the quote ready flag, matching `africa_refresh_selected_action_quote` and preserving the duration/response/objective contract through launch.

No other source file was edited for this handoff, and no commit was created.

## Validation of the patch

The source-level field-presence parser reported an empty missing-field set for both `africa_refresh_selected_action_quote` and `africa_requote_selected_action_against_action_target`.

The duration contract consistency check passed after the patch.

The patch is local to quote reconstruction and does not alter action costs, AI weights, target selection, event text, or the shared mission category layout.

## Exact action coverage

The Event 012 decision matrix contains 102 action concepts across 14 families.

The action constants, profile branches, action contract branches, specific validation branches, full disposition branches, partial disposition branches, failure disposition branches, and decision IDs were compared against the matrix.

Every comparison returned 102/102 with no missing or extra matrix action IDs.

Family coverage is:

- Accession: 10.
- Constitutional route crises: 7.
- Diaspora: 8.
- Economy: 10.
- High chaos: 10.
- Host opening: 1.
- Integration: 10.
- Post-unification governance: 1.
- Protection: 10.
- Regional congress: 10.
- Regional congress and restorations: 1.
- Rival blocs: 8.
- Scramble response: 8.
- World order: 8.

The matrix/action ID source is `docs/specs/012_africa_specs/matrices/012_africa_decision_mission_matrix.csv`; the runtime source surfaces are the Event 012 decision and action helper files already owned by this audit.

## Decision and mission lifecycle notes

The shared quote/profile/contract path parameterizes action identity, family, kernel, phase, target mode, duration minimum, duration maximum, duration days, response days, objective, risk, and all resource costs.

Launch revalidation reconstructs the quote against the selected target, rechecks host and capacity state, validates phase/payment/state/action-specific requirements, and rejects stale or unavailable targets before payment and record creation.

Action records snapshot the immutable quote, active duration/objective fields, active target and state arrays, generation, host generation, reservations, and capacity locks.

Four shared mission categories route by duration band: `mission_africa_action_short`, `mission_africa_action_medium`, `mission_africa_action_long`, and `mission_africa_action_epic`.

Each mission uses the active target arrays, derives `days_mission_timeout` from `FROM.africa_active_action_duration_days`, completes into the action resolver, cancels on event-off/generation/contract invalidation, routes cancellation through `africa_cancel_action`, and routes timeout through `africa_timeout_current_action`.

The mission owner is the current action host, the category is the duration-band mission category, the region and target are supplied by the action record arrays, the requirement is the action contract plus revalidated target/state/material gates, the duration is the quoted dynamic duration, success is the full or partial disposition resolver, failure is the failure disposition or timeout response kernel, and duplicate risk is controlled by the single active-action reservation and generation locks rather than by one mission per matrix row.

`africa_cleanup_action` removes the active mission, target/state arrays, state locks, reservations and capacity, disease/disaster/diaspora receipts, flags, variables, and cooldown state, then fires result event `chaosx.nr12.220` through the existing result path.

`africa_cleanup_annexed_action_target` is generation-safe for current and stale records and is called from the Event 012 annex lifecycle hook before an annexed target disappears.

Host transfer and stale generation checks are present in action validation, mission cancellation, action cleanup, and result handling.

No new recurring world-scan on-action was added; the existing targeted lifecycle hooks remain the bounded cleanup mechanism.

## Cost, requirements, and feature gates

The central quote/profile/contract path covers political power, command power, equipment, manpower, factories, trains, convoys, experience, support, legitimacy, supply, cooldown, capacity, and map-objective requirements through parameterized fields and action-specific branches.

Actions 71–76 retain Evolution III, disease or manifest prerequisites, action caps, cooldowns, owned-state requirements, and exact package/model/entity/counter/audio manifest checks for strange-force paths.

Disease actions use the native ordinary-pathogen authorization, containment, research, weaponization, full/partial/failure, and backfire lifecycle while Event 012 cleans only its own receipts.

Elephant unlock and spawn are idempotent and require a valid host, owned and controlled state, package availability, stockpile/template guards, and the relevant unlock path.

Voluntary diaspora actions require target-owned acceptance or counterterms, revocable standing consent, fresh emergency consent for emergency evacuation, capacity, registry, housing/jobs/education, and usable target checks.

Diaspora actions do not force population movement, country tags, ownership, or sovereignty changes.

Natural-disaster actions use maintained selected enemy rosters from relationship, world, scramble, sponsorship, and war-partner lanes rather than opinion-only integration or an unbounded target scan.

The natural-disaster bridge supplies Event 013 with the selected country target, bounded strength bands and scales, caller ID 12, backfire and cooldown receipts, and target-legitimacy state.

No cost or balance target was invented during this audit.

## AI validity and route locks

The early AI family picker covers 87 action IDs.

The late candidate-weight and dispatch path covers the remaining 16 action IDs.

The union is exactly 102/102, and both paths use the shared target, quote, validation, and begin-action flow.

Late IDs are `seek_international_recognition`, `prepare_anti_sanctions_network`, `answer_foreign_ultimatum`, `mobilise_continental_defence`, `disrupt_expedition_planning`, `offer_base_withdrawal_treaty`, `call_global_anti_colonial_conference`, `break_intervention_coalition`, `sponsor_continent_unifier`, `mediate_continent_union`, `prepare_continental_war`, `force_continent_submission`, `form_dynamic_two_continent_union`, `declare_the_world_is_one`, `administer_world_regions`, and `contain_terminal_high_chaos`.

AI target validity follows the same owned, controlled, alive, war, route, consent, capacity, state, and generation checks as the player launch path.

No AI weight, probability-bearing modifier, MTTH, target ranking, or balance target was patched by this audit.

## Tooltip and localisation notes

Existing decision surfaces expose dynamic quote, cost, requirement, target, duration, response, and objective information through the existing Event 012 localisation and tooltip paths.

Existing mission complete, failure, timeout, cancellation, and Event 220 result paths are wired to the current dynamic text surfaces.

No localisation file was touched because the accepted defect was a runtime quote-contract omission and a safe text-only change was not required.

No player-exposed raw trigger gap was found that could be patched without crossing the parent-owned localisation scope.

## Cleanup and exploit-risk notes

The launch path does not pay or reserve resources until quote, host, capacity, phase, target, state, and action-specific validation succeeds.

Action records have one active generation and one reservation/capacity lane, preventing duplicate mission activation and free repeated launches.

Completion, partial resolution, failure, timeout, cancellation, annex, and stale-generation paths converge on cleanup and release their target, state, reservation, receipt, and cooldown data.

Event `chaosx.nr12.220` is the cancellation/result notification path and performs no additional gameplay effect in its host-facing option.

Disease receipts, natural-disaster receipts, diaspora consent/response receipts, and strange-force spawn markers are cleared or consumed through their owning lifecycle helpers.

No recurring world scan or free-unit loop was introduced or observed in the audited Event 012 decision/action surfaces.

## MCP evidence and limitations

### Event inspection

Broad `hoi4_event_inspect` scan for `chaosx.nr12.1` returned status `EVENT_INSPECTED_PARTIAL` with artifact URI:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/717cacc774b53064ed8a0f6e05f243a4254c770f3e4f38b098af684703684a8e/29de74eb266bd92f7fb279449c311e9537b7e9f37741b69c05f02507d0aaa25c/event-scan-73e269b481e4.json`

The scan reported 9497 events, 14687 options, 1059 entries, 37040 edges, 2129 diagnostics, 8243 unresolved references, and zero blocking issues.

The MCP reports that helper and lifecycle projections were deferred on this large workspace, so this artifact is evidence of partial event inspection rather than a complete lifecycle proof.

Focused inspection of `chaosx.nr12.220` returned status `EVENT_INSPECTED_PARTIAL` with artifact URI:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2e25821109eae54ea4a7b190438171f23681555e591e80cd9604a85d7c598110/47ff75ab989c8d1d7fa05f5485271b39d2b17e6b028f3c9606ef1f11afe507ed/event-scan-b7bdb56ace91.json`

The focused scan inherited the same partial workspace counts and deferred helper/lifecycle limitation, with zero blocking issues.

An event compare was attempted against a fresh inspect artifact but returned the exact blocker `EVENT_GRAPH_ARTIFACT_INVALID` with message `Event graph artifact uses an unsupported schema version`.

Because of that schema blocker, source inspection is not represented as equivalent event compare evidence.

### Probability inspection and comparison

Baseline `hoi4_probability_inspect` used adapter `decision_ai_will_do` against `common/decisions/012_africa_decisions.txt` and returned artifact URI:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f04ed7e4dd242910cf7ea18ad1027a3f85fe4f8068606e1672434fd3f073bbc9/fb7b473bd48a8c955cfde0e53d5ba696fca1672b913f18c5654052629e01b775/probability-inspect-bee8b7ec3e4e.json`

The baseline reported 207 candidates, 23 required inputs, zero unresolved inputs, and `poolComplete=false`.

The required post-patch `hoi4_probability_compare` used the same decision source before and after the patch with scenario ID `event12_action_baseline_after_duration_contract_patch` and returned artifact URI:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ee0cb5007334d8b61d41d4c9a7f7fed8857980a08c82f0652ab102c6018e50a/0a17032faaccafee97b1855250afe2ad6d6f591bb9ea0890d1e046a2a9314841/probability-83c64cb22919349f3df2f43b.json`

The compare returned `PROBABILITY_ANALYZED_PARTIAL`, `comparisonChanges=0`, 400 unresolved resources, 37 diagnostics, and scenario hash `69695b3826a797ac1b846d6bafb931332697e748fef67930f2e3f593e7eb6a90`.

The empty-state scenario left late profiled cycles, selected host/country actions, and world-package decisions ineligible, and unresolved SVG/PNG resources remain in the MCP projection.

This is bounded scenario evidence and an analysis limitation, not a reason to invent AI weights or declare a balance target.

## Simplifications, omissions, and remaining limitations

No requested Event 012 action concept, family, mission lifecycle, cost contract, feature gate, AI route, or cleanup branch was simplified or omitted in the audited source.

The only implementation change is the narrow quote-contract field copy described above.

The MCP event graph compare is blocked by the unsupported artifact schema, and event inspect remains partial because helper/lifecycle projections are deferred.

The MCP probability comparison is bounded by an intentionally empty scenario and unresolved resource projections; it does not constitute full gameplay balance validation.

In-game testing, new-save runtime validation, visual mission behavior, and final player-facing balance judgment remain user-owned and were not claimed here.

No additional plan was created because the remaining issues are tooling/runtime validation limitations rather than a newly designed mechanic.
