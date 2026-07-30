# Event 12 Africa MAIN focus tree — 78-row payoff acceptance crosswalk

Date: 2026-07-30

Scope: static acceptance of the MAIN Event 12 tree (`africa_continental_focus_tree`) against the authoritative payoff matrix at `docs/specs/012_africa_specs/matrices/012_africa_focus_route_payoff_matrix.csv`.

The six external world-package focus files were already dirty and remain untouched.

Follow-up tranche (2026-07-30): the previously queued overlay constitution gap is implemented in `common/scripted_effects/012_africa_focus_route_effects.txt` and called from the existing overlay reward in `common/scripted_effects/012_africa_effects.txt`. The route AI plans now weight all nine overlay mandate capstones in `common/ai_strategy_plans/012_africa_focus_plans.txt`. Regional flags, overlay mandate gates, Independence Wave tags, and the original host are unchanged.

## Disposition and status legend

`accepted` means the matrix row has a named MAIN focus group, a completion effect, a gate or action contract where the matrix calls for one, and a route/support AI plan entry. It is source-level acceptance, not a claim that a live campaign was simulated.

`queued` means the MAIN focus/effect exists but a dependent external package, branch-aware runtime render, campaign simulation, or broader art pass is still required before claiming end-to-end acceptance.

`rejected` means no implementation evidence exists. No matrix row is rejected in this pass.

The static acceptance result is 77 accepted rows and 1 queued row (row 78, because its world-order consumers are outside the MAIN tree). The nine overlay lanes are now constitution-sensitive through the bounded route payoff helper; their remaining queue is runtime scenario proof only.

## Route coverage table

| Route | MAIN focus count and source range | Reward helper | Capstone gate | Route AI profile |
|---|---:|---|---|---|
| Charter federalism | 21, `012_africa_continental_focus_tree.txt:1383-1976` | `africa_apply_federal_focus_route_reward` (`012_africa_focus_route_effects.txt:600`) | `africa_focus_can_complete_federal_route` (`012_africa_focus_route_triggers.txt:245`) | `africa_continental_federal_plan` (`012_africa_focus_plans.txt:67-115`) |
| Continental republic | 21, `012_africa_continental_focus_tree.txt:2004-2596` | `africa_apply_republic_focus_route_reward` (`012_africa_focus_route_effects.txt:733`) | `africa_focus_can_complete_republic_route` (`012_africa_focus_route_triggers.txt:254`) | `africa_continental_republic_plan` (`012_africa_focus_plans.txt:118-166`) |
| Council of crowns | 21, `012_africa_continental_focus_tree.txt:2627-3213` | `africa_apply_crowns_focus_route_reward` (`012_africa_focus_route_effects.txt:866`) | `africa_focus_can_complete_crowns_route` (`012_africa_focus_route_triggers.txt:267`) | `africa_continental_crowns_plan` (`012_africa_focus_plans.txt:169-217`) |
| People’s union | 21, `012_africa_continental_focus_tree.txt:3244-3837` | `africa_apply_union_focus_route_reward` (`012_africa_focus_route_effects.txt:999`) | `africa_focus_can_complete_union_route` (`012_africa_focus_route_triggers.txt:280`) | `africa_continental_union_plan` (`012_africa_focus_plans.txt:220-268`) |
| Military continentalism | 21, `012_africa_continental_focus_tree.txt:3868-4473` | `africa_apply_command_focus_route_reward` (`012_africa_focus_route_effects.txt:1132`) | `africa_focus_can_complete_command_route` (`012_africa_focus_route_triggers.txt:293`) | `africa_continental_command_plan` (`012_africa_focus_plans.txt:271-319`) |
| Confederation | 21, `012_africa_continental_focus_tree.txt:4504-5109` | `africa_apply_confederation_focus_route_reward` (`012_africa_focus_route_effects.txt:1266`) | `africa_focus_can_complete_confederation_route` (`012_africa_focus_route_triggers.txt:311`) | `africa_continental_confederation_plan` (`012_africa_focus_plans.txt:322-370`) |
| Hidden Covenant | 18, `012_africa_continental_focus_tree.txt:5142-5632` | `africa_apply_covenant_focus_route_reward` (`012_africa_focus_route_effects.txt:1393`) | `africa_focus_can_complete_covenant_route` (`012_africa_focus_route_triggers.txt:326`) | `africa_continental_covenant_plan` (`012_africa_focus_plans.txt:373-418`) |
| Shared support | 36, `012_africa_continental_focus_tree.txt:5664-6612` | `africa_apply_support_focus_reward` plus `africa_apply_route_sensitive_support_reward` (`012_africa_focus_route_effects.txt:1509,1539`) | Shared lane gates and route action contracts in the MAIN tree | `africa_continental_support_plan` (`012_africa_focus_plans.txt:421-481`) |

The seven route openers are mutually exclusive at commitment. Each opener uses `allow_branch = { africa_focus_shows_<route>_route = yes }`, reciprocal `mutually_exclusive` blocks, and `africa_commit_constitutional_route` (`012_africa_focus_route_effects.txt:107`). The Covenant route is separately revealed and committed through `africa_focus_can_reveal_covenant` and `africa_commit_covenant_route` (`012_africa_focus_route_triggers.txt:127-151`; `012_africa_focus_route_effects.txt:151`).

## Seven-axis payoff proof

The route bases are distinct seven-axis vectors, and later nodes move the same live variables through route-specific step logic rather than a generic modifier stack. Initialisation is `africa_initialize_constitutional_payoff_axes` (`012_africa_focus_route_effects.txt:30-101`); progression is `africa_apply_constitutional_axis_progression` (`012_africa_focus_route_effects.txt:339`); dispatch is `africa_apply_constitutional_route_focus_reward` (`012_africa_focus_route_effects.txt:322`). Some coordinates intentionally coincide between routes, but the complete vectors and node/trade-off rules are route-specific.

| Route | Representation | Executive power | Resources | Command | Withdrawal protection | Crisis resilience | Post-unification rule |
|---|---:|---:|---:|---:|---:|---:|---:|
| Federal | 65 | 55 | 60 | 55 | 70 | 55 | 65 |
| Republic | 60 | 65 | 55 | 50 | 55 | 60 | 70 |
| Crowns | 55 | 45 | 50 | 55 | 70 | 60 | 60 |
| People’s union | 60 | 70 | 80 | 65 | 45 | 60 | 65 |
| Military command | 35 | 85 | 55 | 90 | 25 | 75 | 40 |
| Confederation | 75 | 30 | 40 | 45 | 90 | 50 | 60 |
| Covenant | 60 | 40 | 70 | 65 | 80 | 85 | 55 |

The base constants are in `common/script_constants/012_africa_focus_route_constants.txt:192-266`. Route helpers then set distinct institutional flags and route action contracts; for example federal begins with chamber representation and deadlock, republic with civic/election institutions, crowns with succession, union with planning and food balance, command with staff/commander loyalty, confederation with withdrawal/free-rider crises, and Covenant with breach/obligation handling.

### Overlay scenario-check (static)

The following matrix was extracted from `africa_apply_constitutional_overlay_payoff` and checks one overlay milestone sequence under all seven routes. Each cell lists the major axis first and the minor axis second. Every route covers all seven axes across six milestones, and every route signature differs.

| Route | Settle authority | Build corridor | Bind partner | Settle local terms | Convene council | Prove mandate |
|---|---|---|---|---|---|---|
| Federal | representation / executive | resources / command | withdrawal / crisis | post-rule / representation | crisis / executive | post-rule / command |
| Republic | representation / executive | command / resources | crisis / withdrawal | executive / representation | post-rule / resources | crisis / post-rule |
| Crowns | withdrawal / representation | executive / resources | crisis / command | post-rule / withdrawal | representation / executive | crisis / resources |
| People’s union | resources / representation | command / resources | crisis / withdrawal | executive / representation | resources / post-rule | post-rule / command |
| Military command | command / executive | resources / crisis | crisis / representation | executive / withdrawal | command / post-rule | post-rule / resources |
| Confederation | withdrawal / representation | command / resources | crisis / executive | representation / post-rule | executive / withdrawal | post-rule / crisis |
| Covenant | crisis / representation | resources / withdrawal | command / executive | post-rule / resources | withdrawal / crisis | representation / command |

## 78-row acceptance crosswalk

### Shared opening (rows 1-5)

| # | Matrix focus group | Status | MAIN focus evidence | Effect, gate, AI, or localisation evidence |
|---:|---|---|---|---|
| 1 | Identify the host problem | accepted | `africa_identify_host_problem`; supporting `africa_repair_host_administration`, `africa_build_host_coalition`, `africa_prepare_host_security` (`012_africa_continental_focus_tree.txt:43-105`) | Opening reward `africa_apply_opening_focus_reward`; host dossier and overlay selection are set before route choice. All 276 active focus title/description keys resolve across Event 12 English localisation files. The regional overlay mutation queue is recorded below. |
| 2 | The first corridor | accepted | `africa_choose_first_corridor`, `africa_build_first_corridor`, `africa_secure_first_corridor` (`012_africa_continental_focus_tree.txt:106-154`) | Opening corridor reward creates reach, dependency, and proof state; the first-protection path cannot skip the corridor evidence. |
| 3 | The first protected partner | accepted | `africa_select_first_partner`, `africa_write_first_guarantee`, `africa_protect_first_partner`, `africa_prove_the_first_obligation` (`012_africa_continental_focus_tree.txt:155-231`) | Obligation flags feed overlay mandate and route capstone gates through `africa_focus_first_proof_satisfied` and the first-obligation triggers. |
| 4 | The provisional congress | accepted | `africa_publish_the_first_obligation`, `africa_invite_regional_delegates`, `africa_convene_provisional_congress`, `africa_write_provisional_charter` (`012_africa_continental_focus_tree.txt:232-299`) | Congress availability uses the scripted opening/congress trigger; completion sets consent and equality inputs used by all seven route openers. |
| 5 | The constitutional principle | accepted | `africa_choose_constitutional_principle` (`012_africa_continental_focus_tree.txt:300-321`) | Route selection commits one grounded constitution or exposes Covenant later; route-aware strategy plans begin at the seven opener IDs. |

### Charter federalism (rows 6-14)

All listed federal blocks dispatch `africa_apply_constitutional_route_focus_reward` with federal route context (`012_africa_continental_focus_tree.txt:1383-1976`), and all IDs are weighted in `africa_continental_federal_plan`.

| # | Matrix focus group | Status | MAIN focus evidence | Effect, gate, AI, or localisation evidence |
|---:|---|---|---|---|
| 6 | Representation before merger | accepted | `africa_federal_representation_before_merger`, `africa_federal_equal_member_chamber`, `africa_federal_population_chamber`, `africa_federal_balanced_two_chambers`, `africa_federal_reconcile_the_chambers` | Federal reward helper nodes 1-5 set chamber flags and `africa_federal_chamber_model`; representation axis moves through federal progression. |
| 7 | Rights of the protected member | accepted | `africa_federal_protected_member_rights`, `africa_federal_prove_member_rights` | Rights flags and member-confidence/autonomy effects are applied by the federal helper; capstone still requires a proven first obligation and accession candidate. |
| 8 | Executive design | accepted | `africa_federal_design_the_executive` | Federal helper sets the executive model and executive/capacity axes; focus has a route-specific localisation key and plan factor. |
| 9 | Contribution and equalisation | accepted | `africa_federal_contribution_and_equalisation`, `africa_federal_deliver_equalisation` | Equalisation helper nodes mutate authority, regional equality, and resource governance; federal plan elevates delivery. |
| 10 | Court or political arbitration | accepted | `africa_federal_court_or_arbitration` | Federal helper records arbitration model and crisis-resilience progression. |
| 11 | Common command under law | accepted | `africa_federal_common_command_under_law`, `africa_federal_prove_civilian_command` | Federal helper records command integration and civilian-command proof; route AI keeps this below the federal deadlock lane until needed. |
| 12 | Federal conversion | accepted | `africa_federal_conversion`, `africa_federal_empower_regional_chambers` | Conversion and chamber empowerment flags feed member autonomy and representation outcomes. |
| 13 | Deadlock conference | accepted | `africa_federal_deadlock_conference`, `africa_federal_accept_deadlock_compromise`, `africa_federal_rewrite_deadlocked_institutions`, `africa_federal_close_the_deadlock` | Federal helper opens the `convene_federal_deadlock_conference` action contract; capstone accepts full action evidence or `africa_federal_deadlock_rewritten` (`012_africa_focus_route_triggers.txt:245`). |
| 14 | Federation with enforceable limits | accepted | `africa_federal_enforceable_limits` | Federal capstone flag is set only through the route reward and the capstone trigger; enforceable limits, amendment, and withdrawal wording are localised. |

### Continental republic (rows 15-23)

All listed republican blocks dispatch the republic helper (`012_africa_continental_focus_tree.txt:2004-2596`; `012_africa_focus_route_effects.txt:733`) and are weighted in `africa_continental_republic_plan`.

| # | Matrix focus group | Status | MAIN focus evidence | Effect, gate, AI, or localisation evidence |
|---:|---|---|---|---|
| 15 | Civic status and staged accession | accepted | `africa_republic_civic_status_and_accession` | Republic helper records civic status and consent/accession values. |
| 16 | Political vehicle | accepted | `africa_republic_choose_political_vehicle`, `africa_republic_build_continental_party`, `africa_republic_coalition_of_parties`, `africa_republic_nonpartisan_constitutional_convention`, `africa_republic_unite_the_civic_campaign` | Political-vehicle enum and coalition flags are route-specific; AI factors distinguish party, coalition, and convention choices. |
| 17 | Franchise design | accepted | `africa_republic_design_the_franchise` | Republic helper changes representation/election legitimacy and opens civic registration. |
| 18 | Executive form | accepted | `africa_republic_design_the_executive` | Executive model and coup-risk trade-off are recorded in the republic reward path. |
| 19 | Public service | accepted | `africa_republic_build_public_service`, `africa_republic_register_the_regions`, `africa_republic_prove_public_service_reach` | Public-service reach proof feeds regional equality and the republic capstone minimum. |
| 20 | First continental election | accepted | `africa_republic_first_continental_election`, `africa_republic_certify_contested_election`, `africa_republic_call_regional_runoff`, `africa_republic_seat_the_elected_government` | Republic helper opens `conduct_first_continental_election`; capstone accepts full election evidence or correction (`012_africa_focus_route_triggers.txt:254`). |
| 21 | Traditional and royal institutions | accepted | `africa_republic_settle_royal_institutions` | Royal-institution settlement mutates crowns confidence and republican legitimacy without opening the crowns route. |
| 22 | Republican guard | accepted | `africa_republic_guard_under_law`, `africa_republic_secure_peaceful_transfer` | Guard and transfer flags preserve civilian control; peaceful-transfer outcome is included in the capstone gate. |
| 23 | Republic accepted beyond the capital | accepted | `africa_republic_distribute_the_capital`, `africa_republic_submit_host_to_common_law`, `africa_republic_accepted_beyond_capital` | Capstone sets the republic route flag after election correction/full evidence and regional equality threshold. |

### Council of crowns (rows 24-32)

All listed crowns blocks dispatch the crowns helper (`012_africa_continental_focus_tree.txt:2627-3213`; `012_africa_focus_route_effects.txt:866`) and are weighted in `africa_continental_crowns_plan`.

| # | Matrix focus group | Status | MAIN focus evidence | Effect, gate, AI, or localisation evidence |
|---:|---|---|---|---|
| 24 | Recognition of crowns | accepted | `africa_crowns_recognise_living_crowns` | Crown recognition sets claimant legitimacy and restoration values. |
| 25 | Precedence without supremacy | accepted | `africa_crowns_precedence_without_supremacy`, `africa_crowns_rotating_chair`, `africa_crowns_first_among_equals`, `africa_crowns_council_without_singular_crown`, `africa_crowns_settle_council_precedence` | Precedence model is an explicit route enum with distinct rotation, first-among-equals, and no-singular-crown flags. |
| 26 | Dual chambers | accepted | `africa_crowns_build_dual_chambers`, `africa_crowns_prove_living_institutions` | Mixed crown/civic chamber and living-institutions proof affect representation and restoration axes. |
| 27 | Succession law | accepted | `africa_crowns_write_succession_law`, `africa_crowns_accept_local_succession`, `africa_crowns_impose_continental_arbitration`, `africa_crowns_close_succession_crisis` | Crowns helper opens `arbitrate_continental_succession`; capstone accepts full action or succession correction (`012_africa_focus_route_triggers.txt:267`). |
| 28 | Land, court, and community rights | accepted | `africa_crowns_settle_land_court_community` | Land/court/community flags mutate restoration legitimacy and regional confidence. |
| 29 | Royal service | accepted | `africa_crowns_define_royal_service` | Royal service model changes readiness and officer-loyalty effects. |
| 30 | Republics in the council | accepted | `africa_crowns_seat_the_republics`, `africa_crowns_prove_republican_equality` | Republican equality is a named crowns reward and blocks monarchy-only completion. |
| 31 | Restoration without support | accepted | `africa_crowns_restore_without_coercion`, `africa_crowns_prove_local_restoration_consent`, `africa_crowns_seat_regional_crown_councils`, `africa_crowns_subject_host_crown_to_charter` | Restoration consent and charter-bound host crown flags are explicit; AI elevates consent proof. |
| 32 | Crowns bound by the Charter | accepted | `africa_crowns_bound_by_charter` | Crowns capstone requires succession action evidence, first proof, and restoration legitimacy threshold. |

### People’s union (rows 33-41)

All listed union blocks dispatch the union helper (`012_africa_continental_focus_tree.txt:3244-3837`; `012_africa_focus_route_effects.txt:999`) and are weighted in `africa_continental_union_plan`.

| # | Matrix focus group | Status | MAIN focus evidence | Effect, gate, AI, or localisation evidence |
|---:|---|---|---|---|
| 33 | Coalition of revolution | accepted | `africa_union_coalition_of_revolution` | Union helper records coalition flags and consent/revolutionary cohesion. |
| 34 | Land settlement | accepted | `africa_union_settle_the_land` | Land settlement mutates central capacity, food continuity, and regional equality inputs. |
| 35 | Resource ownership | accepted | `africa_union_settle_resource_ownership` | Resource sovereignty and technical-dependence variables are route-specific. |
| 36 | Planning scale | accepted | `africa_union_choose_planning_scale`, `africa_union_central_plan`, `africa_union_regional_plans`, `africa_union_sector_compacts`, `africa_union_ratify_the_plan` | Planning model enum and food/industrial action contract are explicit; AI gives crisis weight to choosing the scale. |
| 37 | Party and councils | accepted | `africa_union_party_and_councils`, `africa_union_prove_council_consent` | Party/council balance and consent proof mutate representation, executive power, and crisis axes. |
| 38 | Liberation versus consolidation | accepted | `africa_union_liberation_or_consolidation` | Liberation/consolidation choice records the external-support and reconstruction trade-off. |
| 39 | People’s defence | accepted | `africa_union_build_peoples_defence` | People’s defence model changes readiness, officer loyalty, and civilian burden. |
| 40 | Bureaucracy and technical dependence | accepted | `africa_union_train_the_new_administration`, `africa_union_prove_trained_administration`, with food continuity follow-ups `africa_union_prove_food_continuity`, `africa_union_prioritise_food_outcome`, `africa_union_slow_industrial_targets`, `africa_union_restore_food_industry_balance`, `africa_union_devolve_regional_plans`, `africa_union_end_host_privilege` | Union helper opens `balance_food_and_industrial_plan`; capstone trigger accepts full action or plan correction (`012_africa_focus_route_triggers.txt:280`). |
| 41 | Union through social institutions | accepted | `africa_union_through_social_institutions` | Union capstone flag and post-unification rule axis are set only after food/administration evidence and route gate. |

### Military continentalism (rows 42-50)

All listed command blocks dispatch the command helper (`012_africa_continental_focus_tree.txt:3868-4473`; `012_africa_focus_route_effects.txt:1132`) and are weighted in `africa_continental_command_plan`.

| # | Matrix focus group | Status | MAIN focus evidence | Effect, gate, AI, or localisation evidence |
|---:|---|---|---|---|
| 42 | Emergency or permanent mandate | accepted | `africa_command_define_the_mandate` | Mandate choice changes emergency-rule debt, authority, and war readiness. |
| 43 | General staff or regional commands | accepted | `africa_command_general_staff_or_regions`, `africa_command_central_general_staff`, `africa_command_regional_commands`, `africa_command_dual_command`, `africa_command_unify_the_architecture` | Command architecture enum distinguishes central, regional, and dual command. |
| 44 | Army integration | accepted | `africa_command_integrate_the_armies`, `africa_command_prove_common_logistics` | Logistics proof precedes integration and changes command/readiness axes. |
| 45 | Protectorate doctrine | accepted | `africa_command_define_protectorates` | Protectorate mode records autonomy, resistance, and authority trade-offs. |
| 46 | Logistics first | accepted | `africa_command_logistics_first` | Route reward prioritises the active supply architecture and action burden. |
| 47 | Officer corps settlement | accepted | `africa_command_settle_the_officer_corps` | Officer settlement records retention/vetting/replacement model and loyalty. |
| 48 | The successful commander | accepted | `africa_command_the_victorious_commander`, `africa_command_rotate_the_commander`, `africa_command_constitutionalise_the_commander`, `africa_command_settle_commander_crisis` | Command helper opens `review_victorious_commander_loyalty`; route AI gives crisis/outcome weights to commander correction. |
| 49 | Handover or permanent command | accepted | `africa_command_handover_or_permanence`, `africa_command_prove_officer_loyalty`, `africa_command_prove_civilian_mandate` | Handover/civilian mandate proof and emergency debt bound the capstone (`012_africa_focus_route_triggers.txt:293`). |
| 50 | Command of Africa | accepted | `africa_command_empower_regional_staffs`, `africa_command_limit_host_general_staff`, `africa_command_of_africa` | Command capstone requires war-readiness minimum, loyalty action evidence, and emergency-debt ceiling. |

### Confederation (rows 51-59)

All listed confederation blocks dispatch the confederation helper (`012_africa_continental_focus_tree.txt:4504-5109`; `012_africa_focus_route_effects.txt:1266`) and are weighted in `africa_continental_confederation_plan`.

| # | Matrix focus group | Status | MAIN focus evidence | Effect, gate, AI, or localisation evidence |
|---:|---|---|---|---|
| 51 | Sovereignty reservation | accepted | `africa_confederation_reserve_sovereignty` | Reserved-powers model changes consent and central capacity without silently converting to federalism. |
| 52 | Voting rule | accepted | `africa_confederation_write_voting_rule`, `africa_confederation_unanimity`, `africa_confederation_qualified_majority`, `africa_confederation_regional_concurrence`, `africa_confederation_ratify_voting_compact` | Voting model enum and regional safeguard branches are explicit. |
| 53 | Secretariat | accepted | `africa_confederation_build_secretariat` | Secretariat strength changes project capacity and sovereignty concern. |
| 54 | Common defence | accepted | `africa_confederation_common_defence`, `africa_confederation_prove_collective_defence` | Defence obligation reliability and collective proof are route-specific. |
| 55 | Market and corridors | accepted | `africa_confederation_markets_and_corridors`, `africa_confederation_prove_corridor_treaty` | Corridor treaty proof and market model mutate reach and sovereignty axes. |
| 56 | Foreign policy coordination | accepted | `africa_confederation_coordinate_foreign_policy` | Foreign-policy coordination opens joint recognition and anti-intervention actions. |
| 57 | Withdrawal rules | accepted | `africa_confederation_write_withdrawal_rules` | Withdrawal model is a named route payoff and feeds the live withdrawal axis. |
| 58 | Free rider and divergent war crisis | accepted | `africa_confederation_free_rider_crisis`, `africa_confederation_ratify_bounded_emergency`, `africa_confederation_honour_lawful_refusal`, `africa_confederation_settle_divergent_war`, `africa_confederation_resolve_disagreement_without_force` | The capstone accepts any declared emergency/refusal/divergent-war repair flag plus relationship action target and consent threshold (`012_africa_focus_route_triggers.txt:311`). |
| 59 | Africa in concert | accepted | `africa_confederation_empower_regional_compacts`, `africa_confederation_audit_host_secretariat`, `africa_confederation_in_concert` | Confederal capstone sets route state after voluntary-cooperation evidence; no federal conversion is hidden in the reward. |

### Hidden Covenant (rows 60-68)

All listed Covenant blocks dispatch the Covenant helper (`012_africa_continental_focus_tree.txt:5142-5632`; `012_africa_focus_route_effects.txt:1393`) and are weighted in `africa_continental_covenant_plan`.

| # | Matrix focus group | Status | MAIN focus evidence | Effect, gate, AI, or localisation evidence |
|---:|---|---|---|---|
| 60 | Recognition of the impossible | accepted | `africa_covenant_recognise_the_impossible`, `africa_covenant_recognise_sovereign_actor`, `africa_covenant_create_protected_territory`, `africa_covenant_treat_actor_as_bounded_power` | Reveal gate requires current host, grounded origin, Evolution III log, valid Covenant actor, and no terminal actor flags (`012_africa_focus_route_triggers.txt:127`). |
| 61 | Consent across incompatible actors | accepted | `africa_covenant_mixed_consent_tribunal`, `africa_covenant_define_consent` | Consent mediator/tribunal flags alter Covenant legitimacy and ordinary human confidence. |
| 62 | Favor and wrath | accepted | `africa_covenant_favour_and_wrath` | Favor/wrath and ecological values are route-specific and consumed by Covenant actions. |
| 63 | Boundaries | accepted | `africa_covenant_draw_boundaries` | Boundary model records habitat, sacred-zone, corridor, and containment obligations. |
| 64 | Warfare doctrine | accepted | `africa_covenant_write_warfare_doctrine` | Warfare doctrine mutates condemnation, chaos, readiness, and disaster exposure. |
| 65 | Nonhuman forces | accepted | `africa_covenant_define_nonhuman_forces` | Force-control model distinguishes guardians, supervised formations, and direct command. |
| 66 | Human government under covenant | accepted | `africa_covenant_preserve_human_government` | Human-government preservation keeps ordinary civil institutions in the Covenant end state. |
| 67 | Containment breach or member revolt | accepted | `africa_covenant_prove_reciprocal_obligation`, `africa_covenant_containment_or_revolt`, `africa_covenant_contain_the_breach`, `africa_covenant_renegotiate_the_bargain`, `africa_covenant_protect_member_withdrawal`, `africa_covenant_restore_bounded_coexistence` | Covenant helper opens the obligation-review action; capstone accepts breach containment, renegotiation, or protected withdrawal and a live Covenant actor (`012_africa_focus_route_triggers.txt:326`). |
| 68 | Charter that includes the impossible | accepted | `africa_covenant_include_the_impossible` | Covenant capstone sets route state only after bounded obligations and human safeguards; no terminal fallback is inserted. |

### Shared support lane (rows 69-78)

All support IDs below call `africa_apply_support_focus_reward` (`012_africa_continental_focus_tree.txt:5664-6612`; `012_africa_focus_route_effects.txt:1539`). The ten anchor nodes call `africa_apply_route_sensitive_support_reward` (`012_africa_focus_route_effects.txt:1509`), which stores the active constitution in each support model variable and mutates the matching constitutional axis.

| # | Matrix focus group | Status | MAIN focus evidence | Effect, gate, AI, or localisation evidence |
|---:|---|---|---|---|
| 69 | Corridor philosophy | accepted | `africa_support_choose_corridor_philosophy`, `africa_support_corridor_local_guarantees`, `africa_support_corridor_continental_standards`, `africa_support_prove_common_passage` | Stores `africa_corridor_governance_model = africa_constitution`; corridor proof is weighted very high in the support AI plan. |
| 70 | Resource settlement | accepted | `africa_support_settle_resources`, `africa_support_resource_contracts`, `africa_support_resource_revenue_shares`, `africa_support_anti_extraction_court` | Stores `africa_resource_settlement_model = africa_constitution`; resource axis receives route-sensitive major gain. |
| 71 | Food, water, and health | accepted | `africa_support_food_water_health`, `africa_support_food_network`, `africa_support_water_compact`, `africa_support_continental_health_service`, `africa_support_survival_proof` | Stores `africa_survival_service_model = africa_constitution`; crisis-resilience axis and survival proof are wired. |
| 72 | Military purpose | accepted | `africa_support_define_military_purpose`, `africa_support_command_relationship`, `africa_support_common_logistics`, `africa_support_civilian_oversight` | Stores `africa_common_defence_model = africa_constitution`; command axis and civilian oversight are route-sensitive. |
| 73 | Diaspora programme | accepted | `africa_support_open_diaspora_programme`, `africa_support_diaspora_right_of_return`, `africa_support_diaspora_skills_and_capital`, `africa_support_diaspora_local_consent` | Stores `africa_diaspora_constitutional_model = africa_constitution`; withdrawal-protection axis receives the route-sensitive mutation. |
| 74 | Intelligence purpose | accepted | `africa_support_define_intelligence_purpose`, `africa_support_intelligence_charter`, `africa_support_regional_intelligence_bureaux` | Stores `africa_intelligence_constitutional_model = africa_constitution`; crisis-resilience and threat-purpose values are consumed by intelligence actions. |
| 75 | Restoration sequence | accepted | `africa_support_restore_by_consent`, `africa_support_restoration_claims`, `africa_support_restoration_proof` | Stores `africa_restoration_constitutional_model = africa_constitution`; restoration/withdrawal axis and priority-member stages are preserved. |
| 76 | Scramble response | accepted | `africa_support_answer_the_scramble`, `africa_support_scramble_diplomatic_front`, `africa_support_anti_partition_guarantees` | Stores `africa_scramble_constitutional_model = africa_constitution`; route-specific response remains in the shared lane and is AI weighted. |
| 77 | Constitutional review | accepted | `africa_support_postwar_constitutional_review`, `africa_support_review_convention`, `africa_support_review_settlement` | Stores `africa_postwar_review_model = africa_constitution`; post-unification rule axis receives the route-sensitive mutation and action 100 is gated by review evidence. |
| 78 | External continent sponsorship | queued | `africa_support_sponsor_another_continent`, `africa_support_choose_external_partner`, `africa_support_external_sponsorship_mandate` | Stores `africa_external_sponsorship_model = africa_constitution` and has `africa_continental_support_plan` factors, but its Evolution IV/world-order consumers are in six external focus packages outside this pass. No external package file was edited; runtime sponsorship acceptance remains queued. |

## Nine regional overlays: explicit audit

The MAIN tree contains nine overlay lanes, six focuses each (`012_africa_continental_focus_tree.txt:322-1247`), with mutually exclusive `allow_branch` predicates and a shared mandate gate `africa_focus_can_prove_overlay_mandate` (`012_africa_focus_route_triggers.txt:530`). Their regional branches are real: `africa_apply_overlay_focus_reward` sets nine distinct regional flags and regional outcomes (`012_africa_effects.txt:1540-1627`).

| Overlay | MAIN focus span | Regional variation present | Constitution-sensitive variation | Disposition |
|---|---:|---|---|---|
| Maghreb-Sahara | 322-424 | Divided sovereignty, coast/caravan, desert council, northern mandate | `africa_apply_constitutional_overlay_payoff` maps all six milestones to the federal/republic/crowns/union/command/confederation/Covenant axis table; pre-commit flags replay at route commit | accepted source-level; runtime scenario queued |
| West Atlantic | 427-529 | Port/hinterland, export formula, Atlantic mandate | Same route-sensitive helper; route plan weights its mandate capstone | accepted source-level; runtime scenario queued |
| Sahel-Lake Chad | 532-634 | Food/water mobility, pasture/market, inland mandate | Same route-sensitive helper; regional food/water flags preserved | accepted source-level; runtime scenario queued |
| Nile-Horn | 637-739 | River/highland, Nile/Red Sea, basin/Horn mandate | Same route-sensitive helper; river/Red Sea flags preserved | accepted source-level; runtime scenario queued |
| Congo Basin | 742-844 | Company authority, river/rail, resource return, river mandate | Same route-sensitive helper; resource-return flags preserved | accepted source-level; runtime scenario queued |
| Great Lakes | 847-949 | Kingdom/civic authority, lake/rail, land/revenue, lake mandate | Same route-sensitive helper; kingdom council flags preserved | accepted source-level; runtime scenario queued |
| Swahili-Indian Ocean | 952-1049 | Port/mainland, maritime corridor, customs, maritime mandate | Same route-sensitive helper; maritime customs flags preserved | accepted source-level; runtime scenario queued |
| Southern Africa | 1057-1154 | Exclusionary order, rail/port/mine, land/labour, reconstruction mandate | Same route-sensitive helper; land/labour flags preserved | accepted source-level; runtime scenario queued |
| Madagascar-Islands | 1162-1259 | Island authority, convoy network, highland/coast, ocean mandate | Same route-sensitive helper; convoy/island flags preserved | accepted source-level; runtime scenario queued |

The source-level gap is closed by `africa_apply_constitutional_overlay_payoff` (`012_africa_focus_route_effects.txt:111-179`). It applies a distinct major/minor axis pair for each of six overlay milestones under all seven constitutions, replays completed pre-commit overlay flags at `africa_commit_constitutional_route` and `africa_commit_covenant_route` (`012_africa_focus_route_effects.txt:184-192,196-258`), and runs immediately for post-commit overlay completions from `africa_apply_overlay_focus_reward` (`012_africa_effects.txt:1540-1630`).

## Missing, simplified, and queued content

- No payoff-matrix row is missing or rejected in the MAIN source. Row 78 is queued only because its world-order consumers are outside this focus scope.
- The nine regional overlays now carry route-sensitive representation, executive, resources, command, withdrawal, crisis, and post-unification axis consequences. A live host/constitution scenario sweep is still queued.
- Route-specific capstone art is represented by the shared 13-family icon palette; no icon reference is broken, but the matrix’s seven distinct route seals are a visual deepening queue.
- Evolution IV sponsorship, dormant world-order focus surfaces, and their cross-package runtime interactions remain queued in the external package handoffs.
- MCP layout diagnostics remain queued for branch-aware validation. The duplicated overlay coordinates are intentional under mutually-exclusive `allow_branch` predicates and are not a source-level route lock defect.

## High-priority fixes first

1. Run a host/constitution scenario matrix for one overlay through all six milestones under all seven routes, then verify axis deltas and no duplicate replay.
2. Run a branch-aware focus render or campaign smoke matrix for all seven route openers and nine overlays, then separate true visible intersections from the current mutually-exclusive coordinate diagnostics.
3. Finish and runtime-test the six external world-package consumers for row 78 before marking Evolution IV sponsorship complete.
4. If the visual pass remains funded, register seven route seal families while retaining the 13 shared families for fallback-safe focus icon coverage.
5. Run route-aware AI campaign/balance sweeps after the overlay and world-order surfaces are wired; static route-plan capstone coverage is now present.

## Icon coverage table

| Surface | Evidence | Result |
|---|---|---|
| Active MAIN focuses | 276 focus blocks, 276 `icon` fields (`012_africa_continental_focus_tree.txt`) | Complete |
| Registered GFX families | 13 unique `GFX_goal_africa_focus_family_*` refs; each has base and shine entries in `interface/012_africa.gfx:9-34` | Complete |
| DDS payloads | 13 matching files under `gfx/interface/goals/012_africa/` | Complete |
| Route-specific seals | Route blocks reuse the 13 shared family IDs rather than seven unique route-seal families | Queued visual deepening; no missing reference |
| Dormant world-order focus art | External world package surfaces are outside this MAIN pass | Queued with row 78 package work |

## Localisation and reward mismatch list

- Static title/description scan found 276/276 active focus IDs with both localisation keys resolved across `localisation/english/*012*africa*.yml`; no duplicate Event 12 focus keys were found.
- All 276 active blocks dispatch either the constitutional route helper or the support helper; no route block was found with a missing completion dispatcher.
- No direct focus-name versus reward mismatch was identified in the source-level pass. The route-specific helper flags and model variables are the stronger evidence for the mechanics described by the matrix.
- The remaining wording risk is semantic rather than missing-key: shared family icons and generic overlay prose do not name every axis consequence. The gameplay mutation is now explicit, while bespoke route art remains queued.

## AI behavior gaps

- Static route AI coverage is present: grounded route plans, Covenant plan, support plan, formation plan, and the existing 22 host-specific plans are registered in `common/ai_strategy_plans/012_africa_focus_plans.txt`.
- The seven route plans include route-specific factor ladders for openers, dilemmas, crisis nodes, corrections, and capstones. Support anchors likewise have elevated/very-high factors for proof and review nodes.
- Most route focus blocks retain a shared local `ai_will_do` normal factor. This is safe only because the strategy plans carry the route policy; a campaign simulation should verify plan loading and that mutual exclusions prevent an AI from queueing a hidden route.
- The nine overlay mandate capstones now have route-plan factors in `common/ai_strategy_plans/012_africa_focus_plans.txt`: elevated for federal/union, high for republic/crowns/Covenant, urgent for command, and normal for confederation. The six pre-mandate overlay focuses retain host-plan factors so the existing host dossiers remain authoritative.
- No campaign simulation or balance sweep was run; live AI acceptance remains queued by repository policy.

## MCP and static validation evidence

`hoi4.focus_inspect` completed after the overlay patch against `common/national_focus/012_africa_continental_focus_tree.txt` with revision `cee69a16afeaf6b23c022589200847caee151117ea3610f02609c60585b4b132` and 276 focuses. The artifact is [focus-inspect.cee69a16afeaf6b2.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79142d05b2140ae09d955deb926f18724a663ff265491799452a7838d33d91b3/d9bde5992d83a06d6fad0474ed20e0407667017c0862b351b5893e51c50895bb/focus-inspect.cee69a16afeaf6b2.json).

`hoi4.focus_render` completed after the overlay patch with HTML, SVG, JSON, source-map, and plan artifacts. The HTML render is [africa_continental_focus_tree.focus.html](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ea6023aa4f8f6694e4fd3a6f8fa92797a525871a600bc68f6024f94d2253133/28b09e62392dcae91b95086bd7d0dfb8f76cfa89d1c8d35129404dcd65d73b92/africa_continental_focus_tree.focus.html); the SVG is [africa_continental_focus_tree.focus.svg](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0c01703c94ff27baed53590e37862cee4a6e30a276306d4ad2227bdc2f2d00b3/faa2d979162c42c04048405f4b8967227517f09cb120e85f4f01b558f1cf85a4/africa_continental_focus_tree.focus.svg).

The inspect/render diagnostics report 570 blocking layout diagnostics, including 448 connector crossings, 1,028 node intersections, 55 too-close pairs, and 37 long connectors. The duplicate-coordinate and coordinate-conflict diagnostics are concentrated in the nine overlay lanes, which intentionally reuse the same six positions under mutually exclusive `allow_branch` predicates. They are not nine simultaneously visible branches in a campaign. Static source review found no broken prerequisite, reciprocal mutual exclusion, or route visibility defect. A branch-aware runtime render is still required before clearing the diagnostic queue; no coordinate rewrite was made in this bounded pass.

There is no separate `hoi4.focus_lint` tool exposed in the installed MCP tool catalogue. `hoi4.focus_inspect` returned the validation/diagnostic payload and was used as the lint-equivalent check; no game executable was launched.

Additional read-only checks completed:

- 276 focus blocks and 276 unique focus IDs in the MAIN tree.
- 21 blocks each for six grounded routes, 18 Covenant blocks, 36 support blocks, and 54 overlay blocks.
- 276/276 active focus icons, 13/13 base GFX definitions, 13/13 shine definitions, and 13/13 DDS files.
- 276/276 active focus title/description pairs resolved in Event 12 English localisation.
- 21/21 route blocks per grounded route, 18/18 Covenant blocks, and 36/36 support blocks dispatch the expected scripted reward helper.
- Overlay scenario parser found seven constitution branches × six milestones, all seven axes covered per route, and seven distinct axis signatures; route-plan parser found 9/9 overlay mandate factors in each of the seven route plans.

## Changed files, skipped work, and remaining risks

Changed by this subagent: `common/scripted_effects/012_africa_focus_route_effects.txt` (route-sensitive overlay payoff and pre-commit replay), `common/scripted_effects/012_africa_effects.txt` (one call from the existing overlay reward), `common/ai_strategy_plans/012_africa_focus_plans.txt` (nine mandate factors in each route plan), and this handoff file. No focus source, trigger, localisation, icon, or external world-package file was edited. No commit was created.

Skipped meaningful validation: live campaign simulation, AI balance sweeps, branch-aware runtime layout, and Evolution IV world-order consumer testing. A static seven-route by six-step overlay scenario matrix was run; live replay/no-duplicate and campaign outcomes still require the game/runtime or external package state.

Remaining high-priority risks are live overlay replay/no-duplicate proof, route-specific visual seals, the queued external sponsorship/world-order package, and clearing the MCP layout queue with a branch-aware renderer. The authoritative matrix itself has no rejected rows and no fallback route was introduced.
