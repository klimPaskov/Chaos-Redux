# Event 015 Focus Tree Current Atomic Re-audit

Date: 2026-07-15  
Role: `chaosx_focus_tree_auditor`  
Mode: fresh audit of the current source snapshot; gameplay files read-only  
Audited event: 015 — Utopia Manifesto  
Verdict: **PASS**

## Result

The current Event 015 replacement focus tree passes the delegated completion audit. The audited source contains 124 unique focuses and 174 valid prerequisite references, all 124 focuses are structurally reachable, all route and shared-system coverage requested by the specification is present, and no open P0 through P3 focus-tree finding remains.

The late paid-focus patch is complete in the exact current snapshot. All 34 paid focuses fail closed after selection, recheck their live dynamic price at completion, and protect every downstream reward behind the matching payment-success guard. The two state-control cost refreshes are outside the Fallout-only callback guards.

No gameplay, localisation, AI, idea, icon, decision, event, or on-action file was edited by this auditor. The only authored file is this report.

## Frozen current snapshot

The required focus and callback hashes match the parent-provided stable snapshot exactly.

| SHA-256 | Lines | Source |
| --- | ---: | --- |
| `8a905d4b1922ab88bfab97716ba79721fc5b42679863c9543fb04d2cd489fc05` | 4,119 | `common/national_focus/015_utopia_manifesto_focus_tree.txt` |
| `c2b26e499078d0c7782e46db587d377d8d64cee02e372f2ae8e087c7cea7ea81` | 380 | `common/on_actions/015_utopia_manifesto_on_actions.txt` |
| `e6db306460f20b84cb452faafc300d062a318cbd5b48eb01bb8a24da30658cbb` | 288 | `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` |
| `84f1e322ef827edd4eedff68ba99e67ae61e6c4ed1172193cf77eb3f4d05326a` | 488 | `common/ideas/015_utopia_manifesto_ideas.txt` |
| `5dcd41ef8669a4384fedb2efa9761e657fe8a5ff8ea686e45046005fd23d17fd` | 5,708 | `common/decisions/015_utopia_manifesto_decisions.txt` |
| `ed44d3a9892061bb77ebe6e6039be8d7a6a1bcc5f292091c4e5ede32b39d2b8d` | 6,275 | `common/scripted_effects/015_utopia_manifesto_effects.txt` |
| `078ccd44ef44d768e1954b3beb914726417fa742a0fe35f8bc5c5938977998aa` | 496 | `common/scripted_effects/015_utopia_manifesto_country_effects.txt` |
| `da2b2c86a47979dde9b7cae022e4f1798bac6029955858ca90fddd8a9167fa75` | 967 | `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` |
| `d0c304d2b4cd5dccd72b40cff8e9ab4caa3beab58838ce68057eacf31bcfe9af` | 2,882 | `common/scripted_triggers/015_utopia_manifesto_triggers.txt` |
| `c8d34f7e48facc7eac266d64383af3fa66e93c7a9a48d4d46ba2e96a8e570828` | 353 | `localisation/english/015_utopia_manifesto_focus_l_english.yml` |
| `272920625cf3220dd6d67b52bcae0aa5d99d820d6f66bd87593391e9df454749` | 1,845 | `interface/015_utopia_manifesto.gfx` |

Corroborating current audit records:

| SHA-256 | Lines | Record |
| --- | ---: | --- |
| `4d8139f71ee39c8746010e1a59307a27ed0c2f79e246854f9b59a5c28c686533` | 277 | `localisation_completion_current_full_reaudit_2026_07_15.md` |
| `6f20d253fd8b77d29881788bb8ca129d06412dcdf440807c132bcb671445d677` | 296 | `decision_mission_completion_current_reaudit_2026_07_15.md` |
| `cdf8e3fee2091e63a20773c00289cfecdafd9d560c07f337baa0b5ce66e51d20` | 204 | `docs/assets/015_utopia_manifesto/manifest.md` |
| `0b6d359f73b1a3cf7d1cf501fd530349bbc2873ff833689cc06a6999257389cf` | 75 | `docs/assets/015_utopia_manifesto/final_icon_frame_audit.json` |

## Required references consulted

Repository guidance and skills:

- `AGENTS.md`
- `chaos-redux-focus-trees`
- `chaos-redux-subagents`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `docs/specs/015_utopia_manifesto_specs/prompts/subagents/03_focus_tree_auditor_prompt.md`
- all eight Event 015 specification parts and the current completion, country-package, decision/mission, and focus-route matrices

Offline Paradox wiki pages consulted:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding
- National focus modding

Vanilla documentation and source precedents consulted:

- `documentation/script_concept_documentation.md`
- `common/script_constants/documentation.md`
- `common/decisions/_documentation.md`
- `common/on_actions/_documentation.md`
- `common/ai_strategy/_documentation.md`
- relevant official effect and trigger documentation
- vanilla national-focus route, availability, equipment-gated payment, and cancellation precedents, including the Canadian paid-focus structure

The official AI strategy documentation confirms that negative `avoid_starting_wars` values add restraint, while the Event 15 positive escalation value increases aggression in the deliberately escalatory case.

## Graph, depth, and position audit

| Check | Current result |
| --- | ---: |
| Focus blocks | 124 |
| Unique focus IDs | 124 |
| Prerequisite references | 174 |
| Missing prerequisite targets | 0 |
| Structural roots | 1 |
| Structurally reachable focuses | 124/124 |
| Structural terminals | 10 |
| Duplicate coordinate pairs | 0 |
| Non-downward prerequisite edges | 0 |
| Static connector-through-unrelated-node cases | 0 |
| Conservative straight-segment intersections | 53 |
| X span | -2 through 52 |
| Y span | 0 through 16 |
| Longest prerequisite chain | 17 focuses |

The single root is `utopia_manifesto_recover_the_manuscript`. Reachability was evaluated with the documented HOI4 semantics: focus references inside one prerequisite block are alternatives, while separate prerequisite blocks are cumulative requirements.

The ten structural terminals are:

- `utopia_manifesto_a_nation_of_many_skills`
- `utopia_manifesto_surplus_beyond_the_shore`
- `utopia_manifesto_end_the_auxiliary_contract`
- `utopia_manifesto_commonwealth_defense_compact`
- `utopia_manifesto_the_regional_commonwealth`
- `utopia_manifesto_a_commonwealth_of_places`
- `utopia_manifesto_status_by_consent`
- `utopia_manifesto_a_settled_interim_charter`
- `utopia_manifesto_the_regional_proclamation`
- `utopia_manifesto_plenty_in_an_age_of_chaos`

Representative prerequisite-chain depths are 12–13 focuses for the five political route capstones, 14 for `utopia_manifesto_proof_of_the_commonwealth`, and 17 for `utopia_manifesto_plenty_in_an_age_of_chaos`. The tree therefore has substantive route depth and a distinct formation/post-formation continuation rather than a shallow route selector.

The 53 straight-segment intersections are a deliberately conservative source proxy, not a count of engine-routed connector collisions. HOI4 bends connectors according to its layout renderer. The useful static obstruction check is clean: no straight prerequisite segment passes through an unrelated focus coordinate, and no two focuses share a coordinate.

## Required branch and system coverage

| Required surface | Current source proof |
| --- | --- |
| Opening trunk | `utopia_manifesto_recover_the_manuscript` proceeds through survey, store, calling, charter, and `utopia_manifesto_convene_the_interpretive_congress`. |
| Consent of Households | Distinct route identity, rewards, AI, institution stages, League behavior, and `utopia_manifesto_commonwealth_by_consent`. |
| Common Table | Distinct councils, common ownership, workshops, AI, institution stages, and `utopia_manifesto_union_of_tables`. |
| Guardians of Measure | Distinct standards, measured cities, assignment tradeoffs, AI, institution stages, and `utopia_manifesto_perfect_measure`. |
| Closed Island | Distinct compulsion, stores, service formations, auxiliaries, AI, institution stages, and `utopia_manifesto_perfect_island`. |
| The Joke Understood | Hidden/reveal-gated critical-humanist route, mixed property, sunset/audit logic, its own AI, and `utopia_manifesto_good_place_that_admits_its_limits`. |
| Callings | Shared calling shortage and policy lane terminating at `utopia_manifesto_a_nation_of_many_skills`. |
| Common stores | Paid store growth, reserve decisions, store lifecycle, and `utopia_manifesto_two_years_against_hunger`. |
| Garden districts | Map-grounded district choices, garden lifecycle, transport/housing growth, and `utopia_manifesto_a_ring_of_social_cities`. |
| Island variants | Five mutually exclusive geographic variants feeding paid construction and `utopia_manifesto_the_island_made_real`. |
| Defense | Route-sensitive militia/professional/auxiliary choices and `utopia_manifesto_commonwealth_defense_compact`. |
| Foreign commonwealth | Associate, aid, arbitration, League/faction behavior, and `utopia_manifesto_the_regional_commonwealth`. |
| Necessary Ground | Case-gated peaceful and escalatory lane, `utopia_manifesto_the_limit_of_need` versus `utopia_manifesto_the_natural_right`, and `utopia_manifesto_a_commonwealth_of_places`. |
| Stewardship and integration | Stewardship lifecycle and settlement/status outcomes through `utopia_manifesto_status_by_consent`. |
| Crisis correction | Five route-specific corrections converging on `utopia_manifesto_a_settled_interim_charter`. |
| Formation | Route-specific proof trigger, paid proof mission, paid proclamation, identity formation, and `utopia_manifesto_the_regional_proclamation`. |
| Post-formation play | Integration, succession, claim-law, mature defense, and regional-policy focuses ending at `utopia_manifesto_plenty_in_an_age_of_chaos`. |

No required route, shared support lane, crisis correction, formation step, or post-formation continuation is represented by a generic fallback focus.

## Mutual exclusions, route locks, and dynamic visibility

The source contains 68 directed mutual-exclusion references. Every reference has its reverse reference. They form seven complete components:

1. the five political openers — 20 directed arcs;
2. council autonomy versus emergency central planning — 2 arcs;
3. useful freedom versus exact obedience — 2 arcs;
4. the five island variants — 20 arcs;
5. no glory in the field versus necessary victory — 2 arcs;
6. the limit of need versus the natural right — 2 arcs;
7. the five constitutional-crisis corrections — 20 arcs.

The hidden Joke route is not publicly available as an ordinary sixth opener. Its opener requires the dedicated reveal state or its matching crisis correction; downstream focuses continue to require the route/reveal state. `utopia_manifesto_admit_the_book_was_a_question` commits the route and explicitly unlocks its opener.

The route setters, crisis transitions, and island selection helpers call `utopia_manifesto_refresh_focus_visibility`, which uses `mark_focus_tree_layout_dirty = yes` for an accepted, non-disabled actor. Dynamic `allow_branch` changes therefore have an explicit layout refresh path instead of relying on stale focus-tree visibility.

## Public availability, bypass, and localisation

Independent source parsing found:

- 94 `available` blocks;
- 5 `bypass` blocks;
- 15 `allow_branch` blocks;
- 99 public availability/bypass tooltip references;
- 99 unique referenced tooltip keys;
- zero availability or bypass blocks without a public wrapper;
- zero missing public tooltip keys;
- 124/124 focus names and 124/124 focus descriptions present.

The current localisation re-audit further confirms that the 99 public tooltip values are distinct, do not expose internal scripted identifiers, and retain UTF-8 BOM encoding. Player-facing conditions cover payment, route, geographic, proof, formation, and post-formation restrictions rather than exposing raw implementation predicates.

## Paid-focus atomicity

There are exactly 34 paid focuses: 26 institutional and 8 military.

The focus names in the inventory table omit the shared `utopia_manifesto_` prefix for readability.

| Payment family | Tier | Count | Focuses |
| --- | --- | ---: | --- |
| Institutional | foundation | 12 | `the_first_common_store`, `cooperative_land_trusts`, `social_workshops`, `standard_houses`, `the_closed_store`, `penal_works`, `a_mixed_commonwealth`, `schools_of_calling`, `the_capital_store`, `useful_industry`, `rail_road_and_common_ground`, `restore_the_route` |
| Institutional | network | 10 | `commonwealth_by_consent`, `union_of_tables`, `cities_in_series`, `reform_without_paradise`, `good_place_that_admits_its_limits`, `a_nation_of_many_skills`, `regional_storehouses`, `a_ring_of_social_cities`, `common_reserve_council`, `integrate_the_ring` |
| Institutional | capstone | 4 | `perfect_measure`, `cut_the_channel`, `build_the_island`, `plenty_in_an_age_of_chaos` |
| Military | foundation | 3 | `households_of_service`, `the_citizen_watch`, `engineers_before_generals` |
| Military | network | 2 | `a_small_army_well_housed`, `mutual_defense_without_mastery` |
| Military | capstone | 3 | `perfect_island`, `commonwealth_defense_compact`, `the_commonwealth_at_war` |

Every row above has all of the following properties in its full focus block:

- the public `available` block calls the matching institutional or military foundation/network/capstone affordability trigger;
- the completion block writes the same tier to `utopia_manifesto_growth_tier_input`;
- military focuses also write a concrete formation input;
- `cancel_if_invalid = yes` is explicit;
- no paid focus uses `select_effect`;
- no paid focus sets `continue_if_invalid = yes`, so the documented default remains fail closed;
- the payment helper refreshes the current tier price and capacity and rechecks affordability immediately before payment;
- deductions happen before the paid unit or institutional proof is created;
- every gameplay reward after the helper is inside an `if` whose limit rejects the matching payment-failure flag;
- the helper clears its temporary inputs on both success and failure.

The automated block audit returned 34 paid focuses, the expected 26/8 family split, the expected tier distribution, and zero gate, cancellation, continuation, or success-guard defects.

### State-control price refresh

`on_state_control_changed` keeps narrow changed-country behavior. In the current 380-line on-action source:

- the ROOT accepted-actor `utopia_manifesto_refresh_dynamic_costs` call is outside all Fallout guards;
- the FROM accepted-actor `utopia_manifesto_refresh_dynamic_costs` call is outside all Fallout guards;
- the case/association snapshot work and the later Ledger/island reconciliation remain Fallout-guarded where intended;
- no daily, weekly, monthly, or equivalent all-country repair scan was introduced.

The refresh helper recomputes the foundation, network, and capstone snapshots from the actor's current controlled-state count, so a state-control change updates all three live price tiers.

## Reward diversity and fairy-dust audit

The focus rewards are not a sequence of generic political-power or stability grants. The tree uses route flags and identities, Ledger deltas, staged institution helpers, paid growth, calling and reserve unlocks, district and island projects, defense formations, associate/League mechanics, Necessary Ground cases, stewardship, constitutional correction, formation proof, succession, and post-formation policy.

The focus source itself contains zero direct `create_unit`, `division_template`, `add_equipment_to_stockpile`, `add_core_of`, state-core, annexation, or state-owner-transfer effects.

The only Event 15 unit creation reached by paid focuses is inside `utopia_manifesto_deploy_paid_formation`, called by the paid military executor after it has deducted dynamically prepared manpower, army experience, infantry equipment, and support equipment. The apparent `add_equipment_to_stockpile` calls in that executor use explicitly negated cost variables and are deductions, not grants. Institutional paid growth likewise deducts manpower, political power, and support equipment before writing its proof.

No Event 15 core-grant effect exists in the audited focus/effect/event formation chain. Formation changes proof flags, politics, institutional presentation, cosmetic identity, and evolution availability; it does not annex League members, transfer states, add cores, create units, or grant equipment.

## Decision, mission, geography, and formation integration

The focus tree calls all seven intended decision-unlock APIs: calling, reserve, district, Necessary Ground, stewardship, League, and formation. Each API sets a dedicated unlock flag, and the decision/category source consumes the corresponding flag either directly or through the matching scripted trigger. The current independent decision/mission re-audit corroborates an inventory of 121 decisions and 43 missions with no open integration finding.

The formation chain is explicit and non-free:

1. `utopia_manifesto_proof_of_the_commonwealth` requires a political route capstone, island/district proof, the first associate, and the route-specific `utopia_manifesto_can_form_current_route` proof.
2. Its reward refreshes proof, unlocks the formation category, and advances the decision phase.
3. `decision_utopia_prove_the_commonwealth` charges political power, support equipment, trains, and motorized equipment, then activates a variable-duration proof mission.
4. Mission completion re-evaluates the route proof and records formation proof.
5. `decision_utopia_proclaim_the_commonwealth` charges political power, support equipment, trains, and convoys, then fires `chaosx.nr15.10`.
6. Event option `.10.a` rechecks the proof and calls `utopia_manifesto_form_current_route_identity`.
7. The identity helper calls the central formation helper and applies one of five route-specific political/cosmetic identities only after `utopia_manifesto_commonwealth_formed` and `utopia_manifesto_formation_proof_met` are present.

The five island focuses are a complete mutual-exclusion set. Their availability triggers are geographically distinct:

- existing island: owned, controlled, core island capital;
- archipelago network: the configured count of owned, controlled, core island states;
- leased island: a live qualifying foreign island target plus the maritime/settlement shortage threshold;
- coastal refuge: an owned, controlled, core coastal state;
- inland island: a landlocked country with an owned, controlled, core capital.

`utopia_manifesto_build_the_island` additionally requires the selected variant's site-readiness proof, and `utopia_manifesto_the_island_made_real` requires the completed project proof. A geography label therefore cannot be selected or completed solely from flavour text.

## Staged idea lifecycle

The idea source contains 50 unique idea definitions using 12 unique live pictures. Independent source comparison found:

- all 50 ideas appear in lifecycle clear coverage;
- all 50 ideas appear in lifecycle add coverage;
- all 50 have global Event 15 name/description coverage;
- all 12 picture handles resolve to installed `64x64` DDS textures.

The lifecycle helpers clear a whole family before adding its next form. The opening manifesto, public-knowledge, inherited-property, five route institutions, common-store, garden-district, auxiliary, and stewardship families therefore advance through founding, mitigation, failure, final, or route-specific forms instead of adding one permanent spirit per focus.

Cross-family substitutions are also explicit: common stores replace the unmeasured-country slot; auxiliaries temporarily replace the current route institution and restore its recorded stage; stewardship temporarily replaces the garden/property slot and restores the correct family on resolution. Post-formation succession clears the obsolete opening spirits. No focus reward bypasses these lifecycle APIs to stack a duplicate stage.

## AI audit

- 124/124 focuses contain an explicit `ai_will_do` block.
- Every `@utopia_*` token referenced by the focus source resolves to a file-scoped definition in that same file.
- The Event 15 AI strategy source contains 12 unique strategy packages.
- All 12 packages contain `allowed`, `enable`, and `abort_when_not_enabled = yes`.
- Every `@utopia_ai_strategy_*` reference resolves locally.
- The five route packages have distinct construction, army, volunteer, and war-restraint behavior.
- The Closed Island escalation package activates only with a valid case and uses the documented positive aggression value.
- Ledger-band recovery strategies respond to low Plenty, high Need, and low Concord.
- Constitutional crisis and mature-commonwealth strategies have separate activation and automatic abort paths.

The focus and strategy AI therefore covers route selection, route conduct, crisis recovery, geography/shared-lane progression, formation, and mature play rather than relying on a single generic factor.

## Focus icon audit

Independent current-source parsing, separate from the asset manifest, found:

- 124 focus icon usages;
- 74 unique focus sprites;
- 74/74 base sprite definitions present;
- 74/74 matching `_shine` sprite definitions present;
- 0 base/shine texture mismatches;
- 0 missing referenced DDS files;
- 74/74 referenced textures are `94x86` according to their DDS headers.

The current asset authority index and machine-readable icon/frame audit report the same 124/74 inventory. The archipelago and leased-island additions have independent registered source records and final textures; neither is a placeholder or a reused missing-file fallback.

## Findings and disposition

| Priority | Open findings |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |
| P3 | 0 |

No small local source defect was found, so the auditor did not patch shared gameplay files and did not create a broad-gap plan.

## Evidence boundary and validation limits

This is a source-level completion audit of the exact hashes above. It proves graph structure, route/interlock definitions, focus conditions, payment ordering and guards, callback placement, source integration, AI definitions, idea lifecycle coverage, localisation references, and file-backed icon resolution.

The installed HOI4 domain MCP tools were not exposed in this agent's tool inventory. A fresh engine-backed render of the exact 124-focus snapshot, live tooltip wrapping, focus-connector routing, AI choice distribution, mission scheduling, and multiplayer interleaving could therefore not be observed in this pass. Those are validation limits, not inferred source defects. The conservative static layout metrics, exact hashes, direct source traces, and current independent localisation/decision records are recorded above so a later engine run can be compared without ambiguity.

## Simplifications, omissions, fallbacks, and blockers

- Simplifications: none.
- Omissions: none within the delegated focus-tree scope.
- Implementation fallbacks: none.
- Blockers: none.
- Remaining open P0–P3 findings: none.
- Gameplay files changed by this auditor: none.
- Commit: none; parent agent retains commit ownership.

## Skills used

- `chaos-redux-focus-trees`
- `chaos-redux-subagents`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`

No skill was created or updated during this audit.
