# Event 012 Africa AI Profile Audit

## Scope and result

This is a read-only static audit of the Event 12 AI-profile registry, the bounded action controller, the Scramble response event, world-order consumers, and the continental focus plans.

No gameplay, localisation, GUI, model, or asset files were changed.

The declared registry is exactly 64 live profiles, with IDs 1 through 64 and no gaps or duplicates.

Each of the 64 rows has one policy block, one loader, one activation predicate, and one refresh call site.

The current controller statically covers all 102 prepared action profiles: 86 family-selected actions in the early controller plus the 16 Actions 77 through 92 in the late controller.

No profile has an all-zero action policy, and no two of the 64 complete 17-field policy vectors are identical.

## Source evidence

- Registry, policy vectors, risk ceilings, partial-outcome tolerances, retry stances, and controller cadence: `common/script_constants/012_africa_ai_constants.txt`, especially `africa_ai_profile` at lines 11 through 82 and `africa_ai_policy`.
- All 64 profile loaders, reset, merge, refresh, actor snapshot merge, bounded late dispatch, and early dispatch: `common/scripted_effects/012_africa_ai_profile_effects.txt`, identifiers `africa_ai_reset_profile_registry`, `africa_ai_refresh_profile_registry`, `africa_ai_evaluate_requested_action_for_action_target`, `africa_ai_store_host_policy_snapshot`, `africa_ai_run_profiled_late_action_cycle`, and `africa_ai_run_profiled_action_cycle`.
- All 64 activation predicates, risk/refusal/retry gates, late action candidate gates, and bounded-array target filters: `common/scripted_triggers/012_africa_ai_profile_triggers.txt`, identifiers `africa_ai_profile_*_is_active`, `africa_ai_requested_action_risk_is_allowed`, `africa_ai_selected_target_retry_policy_allows_action`, and `africa_ai_selected_target_is_candidate_for_action`.
- Contextual family scoring: `common/mtth/012_africa_ai_profiles.txt`, 14 `africa_ai_<family>_context_factor` entries.
- 102 action-family assignments: `common/scripted_effects/012_africa_action_effects.txt`, `africa_prepare_action_profile`.
- AI controller decision and profile-snapshot consumers: `common/decisions/012_africa_decisions.txt:10-23`, `:1550-1592`, and `:1825-1909`.
- Foreign-response classification and response-option use: `events/012_africa_world_order.txt:22-134` and `africa_ai_classify_scramble_response`.
- World-order target safety and terminal gates: `common/scripted_triggers/012_africa_world_order_triggers.txt`, especially `africa_world_*_target_is_eligible` and `africa_terminal_world_identity_can_commit`.
- Focus-route states and plans: `common/national_focus/012_africa_continental_focus_tree.txt` and `common/ai_strategy_plans/012_africa_focus_plans.txt`.
- Design expectation: `docs/specs/012_africa_specs/matrices/012_africa_ai_route_matrix.csv` and `012_africa_ai_route_matrix_notes.md`.

## Count and integrity checks

| Check | Result |
| --- | --- |
| Declared live profile IDs | 64, exactly 1 through 64 |
| Policy blocks `africa_ai_policy_<key>` | 64 |
| Loader effects `africa_ai_apply_profile_<key>` | 64 |
| Activation triggers `africa_ai_profile_<key>_is_active` | 64 |
| Missing or extra policy, loader, or trigger key relative to registry | None |
| Full-vector duplicates | None |
| Profiles with no positive action-family score | None |
| Prepared action profiles | 102 |
| Early dispatcher action IDs | 86 |
| Late dispatcher action IDs | 16, Actions 77 through 92 |
| Action-family context factors | 14 of 14 |

The static policy parser found 25 rows with one or more intentional zero family weights, primarily foreign-power and relationship profiles.

Those rows still have substantial positive families and should not be classified as dead or flat.

## Row-complete registry audit

Legend: `H` is host composition through `africa_ai_refresh_profile_registry`; `T` is target composition through `africa_ai_evaluate_requested_action_for_action_target`; `F` is direct foreign-response classification in `africa_world_order.1`; `W` is the late Scramble or world-order dispatcher; and `P` is the one-to-one unique policy block in `012_africa_ai_constants.txt`.

| ID | Profile | Activation and reachability | Current consumer | Static result |
| ---: | --- | --- | --- | --- |
| 1 | `host_maghreb_sahara` | Current African host plus Maghreb-Sahara overlay | H, P | Reachable |
| 2 | `host_west_atlantic` | Current African host plus West Atlantic overlay | H, P | Reachable |
| 3 | `host_sahel_lake_chad` | Current African host plus Sahel-Lake Chad overlay | H, P | Reachable |
| 4 | `host_nile_horn` | Current African host plus Nile-Horn overlay | H, P | Reachable |
| 5 | `host_congo_basin` | Current African host plus Congo Basin overlay | H, P | Reachable |
| 6 | `host_great_lakes` | Current African host plus Great Lakes overlay | H, P | Reachable |
| 7 | `host_swahili_indian_ocean` | Current African host plus Swahili-Indian Ocean overlay | H, P | Reachable |
| 8 | `host_southern_africa` | Current African host plus Southern Africa overlay | H, P | Reachable |
| 9 | `host_madagascar_islands` | Current African host plus Madagascar-Islands overlay | H, P | Reachable |
| 10 | `route_charter_federalism` | Host constitution is `federal_union` | H, P | Reachable |
| 11 | `route_continental_republic` | Host constitution is `continental_republic` | H, P | Reachable |
| 12 | `route_council_of_crowns` | Host constitution is `council_of_crowns` | H, P | Reachable |
| 13 | `route_peoples_union` | Host constitution is `peoples_union` | H, P | Reachable |
| 14 | `route_military_continentalism` | Host constitution is `military_continentalism` | H, P | Reachable |
| 15 | `route_continental_confederation` | Host constitution is `continental_confederation` | H, P | Reachable |
| 16 | `route_high_chaos_covenant` | Covenant constitution plus Evolution III, reveal, commitment, and valid actor | H, P | Safely route-locked |
| 17 | `member_outside_threatened` | Valid outside relationship target with war, relief, protection, or request evidence | T, P | Reachable |
| 18 | `member_outside_strong` | Valid strong, independent outside target without threat profile | T, P | Reachable |
| 19 | `member_protected_partner` | Current-generation protected relationship | T, P | Reachable |
| 20 | `member_associate_member` | Current-generation associate relationship | T, P | Reachable |
| 21 | `member_chartered_member` | Current-generation chartered relationship | T, P | Reachable |
| 22 | `member_federal_member` | Current-generation autonomous-federal or integrated relationship | T, P | Reachable |
| 23 | `member_resistant_member` | Current-generation resistant, leaving, or occupied-settlement relationship | T, P | Reachable |
| 24 | `member_rival_bloc_leader` | Current-generation rival-bloc relationship | T, P | Reachable |
| 25 | `power_negotiated_withdrawal` | Weak base-holder or treaty and withdrawal evidence | F, T, W, P | Reachable |
| 26 | `power_containment_sanctions` | Coalition member not escalated to expedition | F, T, W, P | Reachable |
| 27 | `power_expedition_coalition` | Coalition member with expedition, planner, or host war evidence | F, T, W, P | Reachable |
| 28 | `power_recognition_partner` | Non-coalition partner with recognition evidence | F, T, W, P | Reachable |
| 29 | `power_opportunist_patron` | Non-coalition patronage or rivalry evidence, including classifier fallback | F, T, W, P | Reachable |
| 30 | `chaos_pan` | Evolution III high-chaos actor with Pan-sapper evidence | T, P | Safely evolution-locked |
| 31 | `chaos_gorilla` | Evolution III high-chaos actor with Gorilla force evidence | T, P | Safely evolution-locked |
| 32 | `chaos_green` | Evolution III actor or ecological site with Green compact evidence | T, P | Safely evolution-locked |
| 33 | `chaos_stoneborn` | Evolution III high-chaos actor with Stone cohort evidence | T, P | Safely evolution-locked |
| 34 | `chaos_rain_drought` | Evolution III high-chaos actor with oracle, rain, or drought evidence | T, P | Safely evolution-locked |
| 35 | `chaos_disease_cult` | Evolution III high-chaos actor with disease evidence | T, P | Safely evolution-locked |
| 36 | `world_middle_east` | Valid external actor with Middle East capital and world order open | T, W, P | Reachable |
| 37 | `world_europe` | Valid external actor with European capital and world order open | T, W, P | Reachable |
| 38 | `world_asia` | Valid external actor with Asian capital and world order open | T, W, P | Reachable |
| 39 | `world_north_america` | Valid external actor with North American capital and world order open | T, W, P | Reachable |
| 40 | `world_south_america` | Valid external actor with South American capital and world order open | T, W, P | Reachable |
| 41 | `world_oceania` | Valid external actor with Australian-continent capital and world order open | T, W, P | Reachable |
| 42 | `world_africa_world` | Current host after unity with authority, manageable burden, and world state | H, W, P | Safely terminal-locked |
| 43 | `host_ethiopia_specific` | Host playbook is Ethiopia | H, P | Reachable |
| 44 | `host_egypt_specific` | Host playbook is Egypt | H, P | Reachable |
| 45 | `host_sudan_specific` | Host playbook is Sudan | H, P | Reachable |
| 46 | `host_morocco_specific` | Host playbook is Morocco | H, P | Reachable |
| 47 | `host_algeria_specific` | Host playbook is Algeria | H, P | Reachable |
| 48 | `host_tunisia_specific` | Host playbook is Tunisia | H, P | Reachable |
| 49 | `host_libya_specific` | Host playbook is Libya | H, P | Reachable |
| 50 | `host_liberia_specific` | Host playbook is Liberia | H, P | Reachable |
| 51 | `host_nigeria_specific` | Host playbook is Nigeria | H, P | Reachable |
| 52 | `host_gold_coast_specific` | Host playbook is Gold Coast | H, P | Reachable |
| 53 | `host_senegal_fwa_specific` | Host playbook is Senegal-FWA | H, P | Reachable |
| 54 | `host_sierra_leone_specific` | Host playbook is Sierra Leone | H, P | Reachable |
| 55 | `host_belgian_congo_specific` | Host playbook is Belgian Congo | H, P | Reachable |
| 56 | `host_angola_specific` | Host playbook is Angola | H, P | Reachable |
| 57 | `host_french_equatorial_africa_specific` | Host playbook is French Equatorial Africa | H, P | Reachable |
| 58 | `host_kenya_specific` | Host playbook is Kenya | H, P | Reachable |
| 59 | `host_uganda_specific` | Host playbook is Uganda | H, P | Reachable |
| 60 | `host_tanganyika_specific` | Host playbook is Tanganyika | H, P | Reachable |
| 61 | `host_somali_specific` | Host playbook is Somali Territories | H, P | Reachable |
| 62 | `host_madagascar_specific` | Host playbook is Madagascar | H, P | Reachable |
| 63 | `host_south_africa_specific` | Host playbook is South Africa | H, P | Reachable |
| 64 | `host_southern_rhodesia_specific` | Host playbook is Southern Rhodesia | H, P | Reachable |

## Lifecycle, scope, risk, and refusal notes

`africa_ai_reset_profile_registry` resets all 14 family weights, risk, partial tolerance, retry stance, active-profile count, and each layer ID before every refresh.

`africa_ai_refresh_profile_registry` then composes one regional overlay, one constitutional route, one relationship state, one foreign state, one high-chaos state, one world state, and one specific host playbook where their scoped predicates pass.

Relationship, foreign, chaos, world, and host-specific layers are ordered `else_if` selections where mutual exclusivity matters.

The target evaluator checks both `has_event_target = africa_action_target` and `event_target:africa_action_target = { exists = yes }` before composition.

The global `africa_host` target is cleared and reassigned on initial host selection and RSA successor transfer, and is cleared in the no-successor terminal branch.

`africa_action_target` is a regular event target created inside the active quote or dispatcher chain, so it does not require global-target cleanup.

Risk is not decorative: `africa_ai_requested_action_risk_is_allowed` compares prepared action risk against the composed maximum risk ceiling before an action can become valid.

Partial and failure repeat behavior is also live: `africa_ai_selected_target_retry_policy_allows_action` reads the immutable last-action record, only permits a retry after the stored profile stance allows it, and requires recovery thresholds for the recovery-only stance.

The high-chaos profiles and actions remain blocked before Evolution III through both action-family and MTTH context gates.

World-order Actions 85 through 92 use maintained candidate arrays and `africa_action_target_is_usable`, with Action 87 also requiring a valid declaration target and Action 91 requiring a controlled non-active capital state.

## Decision category and mission notes

The profile controller is an AI-only zero-cost cadence decision, not a player-facing political-power store.

`africa_ai_run_profiled_late_action_cycle` is visible and available only when `africa_ai_action_controller_is_active` confirms AI host, active Event 12, open action capacity, and no active first proof.

Its 14-day cooldown is centralized as `africa_ai_controller.cycle_days`.

The four Scramble missions are sequential lifecycle windows rather than duplicate checklists.

| Mission | Owner and category | Region and requirement | Duration | Success or timeout behavior | Duplicate risk |
| --- | --- | --- | ---: | --- | --- |
| `africa_scramble_recognition_window` | Host, Charter Council | Shock phase | 90 days | Timeout advances to coalition phase | Low |
| `africa_scramble_coalition_window` | Host, Charter Council | Coalition phase | 120 days | Timeout advances to intervention phase | Low |
| `africa_scramble_intervention_window` | Host, Charter Council | Intervention phase | 150 days | Timeout launches unresolved expedition then advances to aftermath | Low |
| `africa_scramble_aftermath_window` | Host, Charter Council | Aftermath phase | 180 days | Ratifies when valid or prolongs negotiations and pressure | Low |

The sequential phase triggers, distinct durations, cancel triggers, and different timeout effects avoid a duplicated-mission loop.

## Findings, sorted by severity

### Medium: the acceptance ledger and the older 77-92 handoff are stale

`docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` rows 293 onward and `012_africa_ai_actions_77_92_handoff_2026_07_18.md` state that Actions 1 through 76 and 93 through 102 lack live profile dispatch.

Current code disproves that statement: `africa_ai_run_profiled_action_cycle` selects 86 early actions through `africa_ai_pick_action_in_selected_family`, while `africa_ai_run_profiled_late_action_cycle` handles the remaining 16.

The documentation should be reconciled to say that static source coverage now reaches all 102 actions, while campaign simulations and independent scenario audits remain open.

### Medium: profile values do not directly influence focus-plan selection

The matrix notes require a full host profile to alter first focus priorities.

The continental focus tree and `012_africa_focus_plans.txt` key their AI plans to `africa_constitution` and local focus-state flags, but they contain no direct `africa_ai_profile_*`, refresh, snapshot, or family-weight consumer.

Constitution selection does activate the route profile for actions, so route differentiation is live in the decision controller.

Country-specific profile differentiation is not, however, propagated into focus `ai_will_do` or `focus_factors`.

This is a design-depth gap rather than a safe local patch because focus strategy plans cannot directly execute the refresh effect in an `ai_will_do` block.

### Low: persistent snapshot inputs can lag a profile-changing state transition

The Scramble advance decisions and three world-route decisions consume persistent `africa_ai_snapshot_*` variables.

Those snapshots are refreshed when the 14-day controller executes, not when the phase or route transitions.

Their base AI scores prevent a dead route, but modifiers can see an old profile for up to the next controller cycle after a transition or state change.

### Low: no static dead profile or unsafe target scope found

All 64 rows have one-to-one source coverage and positive behavior space.

The 25 intentional zero-family profiles are specialization vectors, not inactive rows.

No world-order target branch scanned all countries or created substitute targets.

## Recommended narrow follow-up patches

1. In `common/scripted_effects/012_africa_ai_profile_effects.txt`, add a narrow host helper that refreshes the profile registry and immediately stores `africa_ai_snapshot_*` values.

2. Call that helper from the Scramble phase-transition effects in `common/scripted_effects/012_africa_world_order_effects.txt` and immediately before or inside the three AI world-route selection effects in `common/decisions/012_africa_decisions.txt`.

3. Update `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` and supersede the relevant open-work wording in `docs/plans/012_africa_plans/012_africa_ai_actions_77_92_handoff_2026_07_18.md`.

4. Create a separately scoped focus-AI design addendum before changing focus plans, defining how each specific host profile changes focus choice without duplicating the full 64-row action matrix into every focus.

## Validation performed

- Parsed registry IDs, policy block keys, loader keys, and activation-trigger keys and compared them by name.
- Parsed all 64 policy vectors and checked full-vector duplication and all-zero action policies.
- Counted all 102 action-family assignments, 86 early dispatcher choices, 16 late dispatcher choices, and 14 contextual MTTH factors.
- Traced target, risk, partial, retry, world-order, and global-host event-target guards through the actual source consumers.

## Skipped meaningful validation and remaining uncertainty

No campaign-state probability evaluation or in-game test was run because this was a read-only audit and live validation belongs to the parent and user.

Static evidence proves source reachability and bounded target filtering, but it cannot prove that every event-created roster array is populated in every intended campaign state.

No GUI inspection was required because the audited profile controller has no decision-owned scripted GUI surface.

## Changed files

- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_ai_profile_audit_2026-07-29.md` only.

## Parent disposition

- Accepted the exact 64-profile and 102-action source coverage findings.
- Added `africa_ai_refresh_host_policy_snapshot` and called it at Scramble initialization, every Scramble phase transition, world-order opening, and the Africa-only deferred closure. This closes the reported snapshot-cadence lag.
- Superseded the stale missing-dispatch wording in `012_africa_ai_actions_77_92_handoff_2026_07_18.md`.
- Kept country-specific focus-plan differentiation open for a separately reviewed implementation tranche.
