# Event 12 African Continental Focus Architecture Handoff

## Status and authority

This is the implementation handoff for the selected Event 12 host's national-focus architecture. It is planning evidence only; it does not claim that the focus tree, decisions, localisation, AI, icons, or runtime transfer are implemented.

The architecture decision is locked:

- Every selected host receives one controlled Event 12 replacement tree.
- The replacement is the intended Event 12 transformation, not a fallback mode.
- There is no additive mode and no host-specific substitute tree.
- The host keeps its tag, original tag, politics, leaders, characters, ideas, laws, technology, equipment, units, controlled territory, diplomacy, public identity, and every effect already executed by completed focuses.
- The host does not keep its former active focus, focus progress, tree navigation, or completed focus IDs that do not exist in the Event 12 tree. The engine cannot retain those IDs across unrelated trees. This limitation must be disclosed in player-facing transition text without implementation jargon and in completion reporting with the exact technical meaning given here.
- Event 12 never restores the pre-Event 12 tree. Recovery restores Event 12 progress, not the former tree.

The selected implementation identifiers are:

| Surface | Identifier |
|---|---|
| Focus file | `common/national_focus/012_africa_continental_focus_tree.txt` |
| Focus tree | `africa_continental_focus_tree` |
| Host flag | `africa_unifier_host` |
| Persistent host target | `event_target:africa_host` |
| Focus-loaded flag | `africa_continental_focus_tree_loaded` |
| Load effect | `africa_load_continental_focus_tree` |
| Layout refresh effect | `africa_refresh_continental_focus_tree_layout` |
| Successor transfer effect | `africa_transfer_continental_focus_tree_to_successor` |
| Tree trigger | `africa_has_continental_focus_tree` |

## Engine finding: why replacement is required

The offline wiki, installed documentation, vanilla source, and repository precedents all point to the same boundary.

1. The offline `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md` states that a focus tree's `country = {}` selection is evaluated before game start and is not a runtime branch-injection mechanism. It also states that `shared_focus = ROOT` statically imports the named root and every shared focus connected through prerequisites. A nonexistent shared root crashes, and a tree cannot consist only of shared focuses.
2. The installed `documentation/effects_documentation.md` documents `load_focus_tree` as the runtime effect that sets a country's active tree. `keep_completed = yes` retains only completed focus IDs that also exist in the new tree. `copy_completed_from` marks focuses completed in the new tree when those same IDs are completed for another valid country.
3. Vanilla `common/national_focus/congo_shared.txt` defines shared focuses, while `common/national_focus/congo.txt` and `common/national_focus/belgium.txt` statically include their shared roots. Vanilla's `unlock_national_focus` use around `CONGO_african_union` unlocks a focus that is already present; it does not inject an absent branch.
4. Repository Event 6 records the limitation and its enforced response. `006_independence_wave_focus_effects.txt` retains a reusable additive assignment mode, but no admitted package relies on detached shared focuses. Registered COR is accepted only while it owns vanilla `generic_focus`, receives the complete Event 6 tree, and restores the generic tree on cleanup; a meaningful external tree fails the setup proof.
5. Repository Event 15 is the correct runtime precedent. It accepts the event, calls `load_focus_tree`, uses one event-owned tree with `default = no` and `reset_on_civilwar = no`, dynamically exposes route branches, and explicitly refreshes layout after route or crisis state changes.

Therefore an arbitrary selected African host cannot receive a meaningful Event 12 branch through `shared_focus`, `unlock_national_focus`, a country flag, or a scripted effect alone. Patching every current and future owning tree would still miss dynamically created countries and would impose permanent cross-event coupling. Controlled runtime replacement is the only engine-safe architecture that gives every selected host the required non-linear tree.

## Runtime replacement contract

### Initial host

`africa_initialize_selected_host` must finish host classification before the tree is loaded. The required order is:

1. Validate `africa_is_eligible_host`.
2. Save the persistent `africa_host` target and set `africa_event_active`, `africa_unifier_host`, and the host-origin ledger flags.
3. Initialise League variables and arrays.
4. Run `africa_apply_mapped_host_playbook` and `africa_classify_host_support`, producing the frozen inputs `africa_host_playbook`, `africa_host_depth`, `africa_regional_overlay`, and `africa_first_proof_type`.
5. Call `africa_load_continental_focus_tree` once.
6. Refresh layout after the tree exists.
7. Continue the delayed first-contact event.

The load helper's semantic core is:

```hoi4
if = {
	limit = {
		NOT = { has_focus_tree = africa_continental_focus_tree }
	}
	load_focus_tree = {
		tree = africa_continental_focus_tree
		keep_completed = no
	}
	set_country_flag = africa_continental_focus_tree_loaded
}
```

`keep_completed = no` is deliberate. Event 12 focus IDs are unique, so `yes` cannot retain unrelated former IDs and would imply preservation that does not occur. Loading the tree does not itself change any non-focus country state. No effect in the load helper may set politics, change tag, replace characters, remove ideas, reset technologies, alter units, or clear non-Event-12 variables.

The tree header should follow the proven Event 15 pattern:

```hoi4
focus_tree = {
	id = africa_continental_focus_tree

	country = {
		factor = @africa_focus_ai_disabled
		modifier = {
			add = @africa_focus_tree_actor_priority
			has_country_flag = africa_unifier_host
		}
	}

	default = no
	reset_on_civilwar = no
}
```

Focus `cost` and focus-file AI values should use file-scoped `@africa_focus_*` constants because that parser pattern is proven by Event 15. Cross-file gameplay thresholds remain in `common/script_constants/012_africa_constants.txt` and are read through explicit `constant:africa_*` tokens.

### What "preserve completed national progress" means

The source specification authorises replacement only if completed progress is retained. The engine divides that requirement into two categories:

- Retained: every reward already applied to country or world state, including ideas, technologies, laws, buildings, factories, equipment, characters, claims, cores, flags, variables, diplomacy, and scripted system state.
- Not retainable across unrelated IDs: the former completed-focus checklist, the former current focus and its partial progress, and the former tree's UI. `keep_completed` only preserves IDs that exist in both trees; Event 12 must not duplicate vanilla or other-mod focus IDs to manufacture a false intersection.

The flag `africa_original_host_preserved` records the retained host identity and applied state. It must never be described as a promise that the old tree can be reopened.

## Focus-tree scale and topology

The target visible campaign is 101 focuses for a compact host and 103 focuses for a full host in an ordinary grounded-constitution run:

| Band | Visible focuses | Structure |
|---|---:|---|
| Shared opening | 16 | Host diagnosis, capacity, corridor, protected partner, congress, constitutional threshold |
| Selected regional overlay | 6 | One of nine six-focus overlays; the other eight occupy the same coordinate template but remain hidden |
| Host signature | 2 compact / 4 full | Universal focus slots dispatch to one of 29 compact or 22 full playbooks; every playbook has bespoke text, effects, events, and proof |
| Selected grounded route | 21 | Nine matrix anchors plus twelve real deliberation, institution, crisis, and proof nodes |
| Route-sensitive support | 36 | Three interlocked lanes; common nodes with route-resolved rewards and gates |
| Formation and post-formation | 20 | Accession, institutions, relationship transitions, review, and final settlement |
| **Ordinary visible total** | **101 compact / 103 full** | Within the specification's target of roughly 85 to 115 meaningful focuses |

The hidden Covenant adds 18 focuses when revealed, within its target of 12 to 20. It is a constitutional transformation layered onto the recorded grounded origin; it is not presented as a human ethnicity route.

The source file will contain more definitions than the visible total because all seven constitutional routes and all nine overlays must exist statically. Hidden definitions are not filler: every one has a unique gate, reward, AI contract, and localisation.

### Shared opening IDs

The exact 16-focus opening is:

1. `africa_identify_host_problem`
2. `africa_repair_host_administration`
3. `africa_build_host_coalition`
4. `africa_prepare_host_security`
5. `africa_choose_first_corridor`
6. `africa_build_first_corridor`
7. `africa_secure_first_corridor`
8. `africa_select_first_partner`
9. `africa_write_first_guarantee`
10. `africa_protect_first_partner`
11. `africa_prove_the_first_obligation`
12. `africa_publish_the_first_obligation`
13. `africa_invite_regional_delegates`
14. `africa_convene_provisional_congress`
15. `africa_write_provisional_charter`
16. `africa_choose_constitutional_principle`

The opening is not a linear chain. Host administration, coalition, and security form three short lanes after the diagnosis; corridor and partner preparation can proceed in parallel, then converge on the real proof and congress. Constitutional choice remains unavailable until the off-tree host proof succeeds or is recovered.

## Complete 78-row payoff mapping

Every accepted payoff row has one stable focus anchor ID. An anchor can head a short focus cluster or gate a decision/event crisis, but no row may be represented only by flavour text. The exact map follows.

### Shared opening: rows 1-5

| Row | Accepted payoff | Focus anchor | Implementation contract |
|---:|---|---|---|
| 1 | Identify the host problem | `africa_identify_host_problem` | Reads the frozen host playbook and exposes the correct weakness, leverage, rival risk, and regional opening. |
| 2 | The first corridor | `africa_secure_first_corridor` | Concludes the corridor preparation cluster; it unlocks the matching proof mission but does not award proof success. |
| 3 | The first protected partner | `africa_protect_first_partner` | Binds the selected real partner and writes the first obligation; survival or delivery is proved off-tree. |
| 4 | The provisional congress | `africa_convene_provisional_congress` | Requires a viable invitation set and opens delegates, charter drafting, and compact-host promotion inputs. |
| 5 | The constitutional principle | `africa_choose_constitutional_principle` | Requires host proof success or recovered proof and exposes the six grounded route openers. |

### Charter federalism: rows 6-14

| Row | Accepted payoff | Focus anchor | Implementation contract |
|---:|---|---|---|
| 6 | Representation before merger | `africa_federal_representation_before_merger` | Federal route opener; records the grounded origin and locks the other five grounded openers. |
| 7 | Rights of the protected member | `africa_federal_protected_member_rights` | Defines protected-member vetoes, appeal, and staged conversion. |
| 8 | Executive design | `africa_federal_design_the_executive` | Real choice cluster between bounded central executive and rotating federal presidency. |
| 9 | Contribution and equalisation | `africa_federal_contribution_and_equalisation` | Connects contribution burden, regional equality, and common budget capacity. |
| 10 | Court or political arbitration | `africa_federal_court_or_arbitration` | Mutually exclusive court and congress-arbitration children rejoin explicitly. |
| 11 | Common command under law | `africa_federal_common_command_under_law` | Gates military integration behind representation and civilian law. |
| 12 | Federal conversion | `africa_federal_conversion` | Unlocks relationship transitions toward autonomous-federal and integrated-region states. |
| 13 | Deadlock conference | `africa_federal_deadlock_conference` | Decision-backed crisis anchor for action 093; no automatic resolution. |
| 14 | Federation with enforceable limits | `africa_federal_enforceable_limits` | Capstone requires a resolved deadlock and an off-tree member/corridor proof. |

### Continental republic: rows 15-23

| Row | Accepted payoff | Focus anchor | Implementation contract |
|---:|---|---|---|
| 15 | Civic status and staged accession | `africa_republic_civic_status_and_accession` | Republican route opener and citizenship/accession framework. |
| 16 | Political vehicle | `africa_republic_choose_political_vehicle` | Choice between continental party, coalition, and non-party civic congress; branches rejoin explicitly. |
| 17 | Franchise design | `africa_republic_design_the_franchise` | Connects franchise breadth to legitimacy, representation balance, and election risk. |
| 18 | Executive form | `africa_republic_design_the_executive` | Choice cluster for presidency, council executive, or constrained host leadership. |
| 19 | Public service | `africa_republic_build_public_service` | Builds the administration needed to make civic status real beyond the capital. |
| 20 | First continental election | `africa_republic_first_continental_election` | Decision-backed election anchor for action 094; result is not predetermined by focus completion. |
| 21 | Traditional and royal institutions | `africa_republic_settle_royal_institutions` | Choice between protected civic roles, local settlement, and abolition with consequences. |
| 22 | Republican guard | `africa_republic_guard_under_law` | Security institution gated by civilian authority and election settlement. |
| 23 | Republic accepted beyond the capital | `africa_republic_accepted_beyond_capital` | Capstone requires election resolution and regional acceptance proof. |

### Council of crowns: rows 24-32

| Row | Accepted payoff | Focus anchor | Implementation contract |
|---:|---|---|---|
| 24 | Recognition of crowns | `africa_crowns_recognise_living_crowns` | Crowns route opener; uses living institutions and claims rather than inventing a universal dynasty. |
| 25 | Precedence without supremacy | `africa_crowns_precedence_without_supremacy` | Establishes precedence rules with a real regional-equality tradeoff. |
| 26 | Dual chambers | `africa_crowns_build_dual_chambers` | Creates distinct civic and crown representation with explicit deadlock handling. |
| 27 | Succession law | `africa_crowns_write_succession_law` | Opens action 095 and records which succession questions require arbitration. |
| 28 | Land, court, and community rights | `africa_crowns_settle_land_court_community` | Choice cluster that cannot grant land settlement without local consent proof. |
| 29 | Royal service | `africa_crowns_define_royal_service` | Defines military, ceremonial, and administrative obligations. |
| 30 | Republics in the council | `africa_crowns_seat_the_republics` | Prevents the route from excluding non-monarchical members. |
| 31 | Restoration without support | `africa_crowns_restore_without_coercion` | Crisis/recovery anchor; unsupported restoration fails and must use the consent sequence. |
| 32 | Crowns bound by the Charter | `africa_crowns_bound_by_charter` | Capstone requires succession settlement and at least one accepted crown/republic compact. |

### People's union: rows 33-41

| Row | Accepted payoff | Focus anchor | Implementation contract |
|---:|---|---|---|
| 33 | Coalition of revolution | `africa_union_coalition_of_revolution` | Union route opener; coalition composition changes later party/council choices. |
| 34 | Land settlement | `africa_union_settle_the_land` | Real choice between local, cooperative, and central settlement with consent and production costs. |
| 35 | Resource ownership | `africa_union_settle_resource_ownership` | Connects resource sovereignty to processing, revenue, and external pressure. |
| 36 | Planning scale | `africa_union_choose_planning_scale` | Opens the food/industrial planning problem later resolved through action 096. |
| 37 | Party and councils | `africa_union_party_and_councils` | Mutually exclusive institutional children with an explicit rejoin. |
| 38 | Liberation versus consolidation | `africa_union_liberation_or_consolidation` | Strategic split with distinct war-readiness, authority, and burden consequences. |
| 39 | People's defence | `africa_union_build_peoples_defence` | Defence institution respects the chosen party/council and liberation settlement. |
| 40 | Bureaucracy and technical dependence | `africa_union_train_the_new_administration` | Gates the capstone behind resolved action 096 and a trained administration. |
| 41 | Union through social institutions | `africa_union_through_social_institutions` | Capstone requires a delivered food, water, health, or education proof. |

### Military continentalism: rows 42-50

| Row | Accepted payoff | Focus anchor | Implementation contract |
|---:|---|---|---|
| 42 | Emergency or permanent mandate | `africa_command_define_the_mandate` | Command route opener; records whether emergency rule has an enforceable end. |
| 43 | General staff or regional commands | `africa_command_general_staff_or_regions` | Mutually exclusive command architecture with explicit rejoin. |
| 44 | Army integration | `africa_command_integrate_the_armies` | Requires actual member forces and common logistics, not an unconditional army bonus. |
| 45 | Protectorate doctrine | `africa_command_define_protectorates` | Defines protection obligations and prevents silent annexation. |
| 46 | Logistics first | `africa_command_logistics_first` | Connects corridors, stockpile, and operational reach. |
| 47 | Officer corps settlement | `africa_command_settle_the_officer_corps` | Resolves host dominance versus regional promotion. |
| 48 | The successful commander | `africa_command_the_victorious_commander` | Opens action 097 and records the commander's live loyalty problem. |
| 49 | Handover or permanent command | `africa_command_handover_or_permanence` | Crisis outcome is gated by action 097; permanent command accumulates emergency-rule debt. |
| 50 | Command of Africa | `africa_command_of_africa` | Capstone requires common-command proof and a resolved mandate. |

### Confederation of African states: rows 51-59

| Row | Accepted payoff | Focus anchor | Implementation contract |
|---:|---|---|---|
| 51 | Sovereignty reservation | `africa_confederation_reserve_sovereignty` | Confederation route opener and explicit reserved-powers settlement. |
| 52 | Voting rule | `africa_confederation_write_voting_rule` | Choice among unanimity, weighted rule, and qualified majority with different free-rider risks. |
| 53 | Secretariat | `africa_confederation_build_secretariat` | Builds limited capacity without silently centralising the confederation. |
| 54 | Common defence | `africa_confederation_common_defence` | Defines opt-in, guarantee, and contribution obligations. |
| 55 | Market and corridors | `africa_confederation_markets_and_corridors` | Connects sovereignty reservations to usable access and common standards. |
| 56 | Foreign policy coordination | `africa_confederation_coordinate_foreign_policy` | Determines when members may diverge and when the League speaks jointly. |
| 57 | Withdrawal rules | `africa_confederation_write_withdrawal_rules` | Creates leaving-member state and a lawful exit sequence. |
| 58 | Free rider and divergent war crisis | `africa_confederation_free_rider_crisis` | Decision-backed crisis anchor for action 098. |
| 59 | Africa in concert | `africa_confederation_in_concert` | Capstone requires a ratified emergency action or an accepted lawful refusal. |

### Covenant with the land and nonhuman congress: rows 60-68

| Row | Accepted payoff | Focus anchor | Implementation contract |
|---:|---|---|---|
| 60 | Recognition of the impossible | `africa_covenant_recognise_the_impossible` | Hidden transformation opener; requires the reveal trigger and a recorded grounded origin. |
| 61 | Consent across incompatible actors | `africa_covenant_define_consent` | Establishes explicit consent rules for human, nonhuman, and ecological actors. |
| 62 | Favor and wrath | `africa_covenant_favour_and_wrath` | Links benefits to obligations and ecological wrath rather than granting a free supernatural bonus. |
| 63 | Boundaries | `africa_covenant_draw_boundaries` | Defines protected zones, settlement limits, and jurisdiction. |
| 64 | Warfare doctrine | `africa_covenant_write_warfare_doctrine` | Limits when nonhuman or ecological force can be used. |
| 65 | Nonhuman forces | `africa_covenant_define_nonhuman_forces` | Creates command, consent, and containment obligations. |
| 66 | Human government under covenant | `africa_covenant_preserve_human_government` | Preserves accountable human institutions; the route is not an ethnic transformation. |
| 67 | Containment breach or member revolt | `africa_covenant_containment_or_revolt` | Decision-backed crisis anchor for action 099. |
| 68 | Charter that includes the impossible | `africa_covenant_include_the_impossible` | Capstone requires a resolved obligation review and a live consent proof. |

### Shared support lane: rows 69-78

| Row | Accepted payoff | Focus anchor | Implementation contract |
|---:|---|---|---|
| 69 | Corridor philosophy | `africa_support_choose_corridor_philosophy` | Shared anchor whose reward and AI resolve through the active constitution and overlay. |
| 70 | Resource settlement | `africa_support_settle_resources` | Connects ownership, processing, revenue shares, and anti-extraction enforcement. |
| 71 | Food, water, and health | `africa_support_food_water_health` | Opens real delivery projects and supplies proof for social capstones. |
| 72 | Military purpose | `africa_support_define_military_purpose` | Applies route-specific civilian, royal, council, command, confederal, or Covenant limits. |
| 73 | Diaspora programme | `africa_support_open_diaspora_programme` | Separates travel, citizenship, skills, capital, and local-consent choices. |
| 74 | Intelligence purpose | `africa_support_define_intelligence_purpose` | Defines counter-subversion and external intelligence boundaries. |
| 75 | Restoration sequence | `africa_support_restore_by_consent` | Hosts restoration proof and action 102 promotion; never creates an empty or unsupported polity. |
| 76 | Scramble response | `africa_support_answer_the_scramble` | Choice between diplomatic front, guarantees, pressure relief, and military preparation. |
| 77 | Constitutional review | `africa_support_postwar_constitutional_review` | Post-unification action 100 can amend route state only through explicit correction/rejoin topology. |
| 78 | External continent sponsorship | `africa_support_sponsor_another_continent` | Requires a stable League, capacity, a valid external partner, and a real sponsored project. |

## Decision-backed focus crises

The last ten accepted action concepts bind to focus state as follows:

| Matrix action | Proposed decision/mission ID | Focus linkage |
|---:|---|---|
| 93 | `africa_action_093_convene_federal_deadlock_conference` | Opened by row 13; its outcome gates row 14. |
| 94 | `africa_action_094_conduct_first_continental_election` | Opened by row 20; its result gates row 23. |
| 95 | `africa_action_095_arbitrate_continental_succession` | Opened by row 27; failure/recovery affects rows 31-32. |
| 96 | `africa_action_096_balance_food_and_industrial_plan` | Opened by row 36; resolution gates rows 40-41. |
| 97 | `africa_action_097_review_victorious_commander_loyalty` | Opened by row 48; result selects row 49's outcome and gates row 50. |
| 98 | `africa_action_098_ratify_confederal_emergency_action` | Opened by row 58; ratification or lawful refusal gates row 59. |
| 99 | `africa_action_099_review_covenant_obligation` | Opened by row 67; result gates row 68. |
| 100 | `africa_action_100_hold_postwar_constitutional_review` | Opened by row 77; changes route law only through a declared correction focus. |
| 101 | `africa_action_101_recover_failed_host_proof` | Available after opening proof failure; retries the same proof family and never grants success on activation. |
| 102 | `africa_action_102_promote_priority_member_package` | Opened by row 75 and the congress system; requires every package-proof input before promotion. |

These are decisions or missions with focus prerequisites, not focus rewards disguised as timers. Every associated focus tooltip must state the trigger, deadline or risk, success result, failure result, and capstone consequence.

## Nine regional overlays and 51 host playbooks

The existing `africa_apply_mapped_host_playbook` effect is the sole classification authority. The focus tree must not repeat tag lists. Each overlay's `allow_branch` calls a scripted trigger that compares `africa_regional_overlay` with its `constant:africa_overlay.*` value. Proposed trigger IDs are:

- `africa_focus_uses_maghreb_sahara_overlay`
- `africa_focus_uses_west_atlantic_overlay`
- `africa_focus_uses_sahel_lake_chad_overlay`
- `africa_focus_uses_nile_horn_overlay`
- `africa_focus_uses_congo_basin_overlay`
- `africa_focus_uses_great_lakes_overlay`
- `africa_focus_uses_swahili_indian_ocean_overlay`
- `africa_focus_uses_southern_africa_overlay`
- `africa_focus_uses_madagascar_islands_overlay`

Exactly one trigger is true for a selected host. All nine branches use the same coordinate template, because their visibility is mutually exclusive.

### Overlay-to-host proof

This table mirrors the implemented playbook assignments rather than making a new regional judgement.

| Overlay | Full playbooks | Compact playbooks |
|---|---|---|
| Maghreb and Sahara | Morocco, Algeria, Tunisia, Libya | Mauritania |
| West Atlantic | Liberia, Nigeria, Gold Coast, Senegal/French West Africa, Sierra Leone | Portuguese Guinea, Cape Verde, Gambia, Cote d'Ivoire, Dahomey, Togo, Sao Tome |
| Sahel and Lake Chad | None | French Sudan/Mali, Niger, Upper Volta, Chad |
| Nile and Horn | Ethiopia, Egypt, Sudan, Somali territories | Eritrea, Djibouti |
| Congo Basin | Belgian Congo, Angola, French Equatorial Africa | Cameroon, Gabon, Equatorial Guinea |
| Great Lakes | Uganda | Ruanda-Urundi, represented by either Rwanda or Burundi as the same playbook |
| Swahili and Indian Ocean | Kenya, Tanganyika | Mozambique, Zanzibar |
| Southern Africa | South Africa, Southern Rhodesia | Northern Rhodesia, Nyasaland, Bechuanaland, Basutoland, Swaziland |
| Madagascar and Islands | Madagascar | Mauritius, Comoros, Seychelles, Reunion |

The count is 22 full plus 29 compact playbooks. Rwanda and Burundi are alternate tags for one Ruanda-Urundi playbook. Sao Tome, Seychelles, and Reunion use the existing signature flags because no stable vanilla original tag exists for those accepted packages.

### Exact overlay focus IDs

#### Maghreb and Sahara

1. `africa_maghreb_sahara_face_divided_sovereignty`
2. `africa_maghreb_sahara_join_coast_and_caravan`
3. `africa_maghreb_sahara_prepare_the_first_guarantee`
4. `africa_maghreb_sahara_reconcile_port_and_interior`
5. `africa_maghreb_sahara_seat_the_desert_council`
6. `africa_maghreb_sahara_prove_a_northern_mandate`

#### West Atlantic

1. `africa_west_atlantic_a_mandate_from_ports_and_hinterlands`
2. `africa_west_atlantic_open_port_and_inland_route`
3. `africa_west_atlantic_protect_the_first_neighbour`
4. `africa_west_atlantic_make_export_wealth_public`
5. `africa_west_atlantic_seat_coasts_and_interior`
6. `africa_west_atlantic_prove_the_atlantic_mandate`

#### Sahel and Lake Chad

1. `africa_sahel_lake_chad_secure_food_and_water`
2. `africa_sahel_lake_chad_open_the_mobile_corridor`
3. `africa_sahel_lake_chad_guard_the_first_partner`
4. `africa_sahel_lake_chad_settle_pasture_and_market`
5. `africa_sahel_lake_chad_convene_the_lake_council`
6. `africa_sahel_lake_chad_prove_the_inland_mandate`

#### Nile and Horn

1. `africa_nile_horn_settle_river_and_highland_authority`
2. `africa_nile_horn_open_nile_and_red_sea_access`
3. `africa_nile_horn_answer_the_first_horn_obligation`
4. `africa_nile_horn_reconcile_court_civic_and_frontier`
5. `africa_nile_horn_convene_basin_and_horn_delegates`
6. `africa_nile_horn_prove_the_northeastern_mandate`

#### Congo Basin

1. `africa_congo_basin_transfer_authority_from_concessions`
2. `africa_congo_basin_open_the_river_rail_spine`
3. `africa_congo_basin_protect_the_first_basin_partner`
4. `africa_congo_basin_return_resource_revenue`
5. `africa_congo_basin_convene_regional_councils`
6. `africa_congo_basin_prove_the_river_mandate`

#### Great Lakes

1. `africa_great_lakes_settle_kingdom_and_civic_authority`
2. `africa_great_lakes_open_lake_and_rail_access`
3. `africa_great_lakes_protect_the_first_lake_partner`
4. `africa_great_lakes_share_land_and_producer_revenue`
5. `africa_great_lakes_convene_the_kingdom_council`
6. `africa_great_lakes_prove_the_lake_mandate`

#### Swahili and Indian Ocean

1. `africa_swahili_indian_ocean_settle_port_and_mainland_authority`
2. `africa_swahili_indian_ocean_open_the_maritime_corridor`
3. `africa_swahili_indian_ocean_guard_the_first_convoy_partner`
4. `africa_swahili_indian_ocean_write_common_customs`
5. `africa_swahili_indian_ocean_convene_coast_and_islands`
6. `africa_swahili_indian_ocean_prove_the_maritime_mandate`

#### Southern Africa

1. `africa_southern_africa_break_the_exclusionary_order`
2. `africa_southern_africa_secure_rail_port_and_mine`
3. `africa_southern_africa_guarantee_the_first_neighbour`
4. `africa_southern_africa_settle_land_and_labour`
5. `africa_southern_africa_convene_the_southern_council`
6. `africa_southern_africa_prove_the_reconstruction_mandate`

#### Madagascar and Islands

1. `africa_madagascar_islands_settle_island_authority`
2. `africa_madagascar_islands_open_the_convoy_network`
3. `africa_madagascar_islands_protect_the_first_island_partner`
4. `africa_madagascar_islands_join_highland_and_coast`
5. `africa_madagascar_islands_convene_the_islands_council`
6. `africa_madagascar_islands_prove_the_ocean_mandate`

### Full and compact host signature slots

Regional content cannot substitute for host identity. Four focus slots are visible when `africa_host_depth` is full or promoted:

1. `africa_host_signature_confront_origin_crisis`
2. `africa_host_signature_use_origin_leverage`
3. `africa_host_signature_contain_origin_rival`
4. `africa_host_signature_prove_origin_mandate`

Two focus slots are visible when `africa_host_depth` is compact, and remain visible as origin history after promotion:

1. `africa_compact_signature_secure_distinct_role`
2. `africa_compact_signature_prove_viable_host`

The shared slot IDs are a rendering mechanism, not generic content. Every one of the 51 values in `africa_host_playbook` needs an explicit scripted-localisation case, a playbook-specific completion-effect case, a proof condition, AI modifiers, and the accepted event package. Full playbooks receive two to four host events; compact playbooks receive their accepted signature event treatment. Missing a case is a missing host package, not permission to show generic text.

Action 102 changes an accepted compact package to `africa_host_depth.promoted`. Promotion retains the two compact-origin slots and reveals the four full-treatment continuation slots; it does not erase completed compact history or reclassify the origin playbook. A promoted campaign therefore exposes four additional meaningful focuses after its package proof.

Suggested helper families are `africa_focus_apply_host_problem`, `africa_focus_apply_host_leverage`, `africa_focus_apply_host_rival_settlement`, `africa_focus_apply_host_mandate`, `africa_focus_apply_compact_distinct_role`, and `africa_focus_apply_compact_viability`. Each helper switches on the numeric playbook variable and is documented in the existing dynamic-effects documentation if implemented as a reusable dynamic effect.

## Seven constitutional routes

The live route is the existing numeric `africa_constitution` variable. The six grounded values are `federal_union`, `continental_republic`, `council_of_crowns`, `peoples_union`, `military_continentalism`, and `continental_confederation`; the hidden value is `ancestral_covenant`.

The six grounded opener anchors are rows 6, 15, 24, 33, 42, and 51. Their mutual exclusions must be symmetric. Each branch root uses an `allow_branch` trigger that is true while the constitution is uncommitted, while that route is current, or while that route's grounded-origin flag is recorded. Completion calls `africa_commit_constitutional_route` with a temporary input, sets exactly one origin flag, then calls `africa_refresh_continental_focus_tree_layout`.

Proposed origin flags are:

- `africa_origin_route_federal_union`
- `africa_origin_route_continental_republic`
- `africa_origin_route_council_of_crowns`
- `africa_origin_route_peoples_union`
- `africa_origin_route_military_continentalism`
- `africa_origin_route_continental_confederation`

Each grounded route contains its nine accepted anchors plus twelve additional nodes. Those twelve are not padding: they implement three genuine institutional choices, three consequence/proof nodes, two crisis outcomes, two explicit rejoin nodes, one regional mutation, and one host-playbook mutation. Each route therefore exposes 21 meaningful focuses.

The Covenant contains its nine anchors plus nine additional consent, boundary, obligation, and containment nodes, exposing 18 focuses.

### Route branch and correction rules

- Every mutually exclusive split is symmetric.
- A rejoin that accepts either outcome uses one prerequisite block containing both outcome focus IDs. Separate prerequisite blocks are reserved for requirements that must all be completed.
- Route changes caused by decisions or events never rely on a flag change alone. A statically present correction focus becomes available, is completed through the declared route, and rejoins through an explicit alternative prerequisite.
- `unlock_national_focus` may unlock a statically present focus. It is never treated as an API for inserting a missing focus or branch.
- Crisis decisions set outcome flags and variables; they do not silently award the capstone.
- Every capstone requires one off-tree proof tied to a member, corridor, congress, election, defence obligation, social delivery, or consent settlement.

### Covenant reveal and transformation

`africa_covenant_recognise_the_impossible` is not one of the six initial mutually exclusive openers. Its branch uses `africa_focus_can_reveal_covenant` and requires:

1. A grounded origin route already recorded.
2. The accepted high-chaos world condition.
3. A real nonhuman, ecological, or impossible actor/pressure in scope.
4. No terminal world actor or resolved-world state that makes the route meaningless.
5. No prior Covenant rejection lock.

Revelation sets `africa_covenant_route_revealed` and refreshes the layout. Completing row 60 changes the current constitution to `ancestral_covenant` while retaining the grounded-origin flag. Previously completed grounded focuses remain visible as history. Unfinished grounded-route focuses become unavailable, while the Covenant branch appears in a separate coordinate lane. This avoids hiding completed history or stranding the player behind prerequisites whose branch vanished.

The Covenant's crisis outcome at row 67 has explicit alternatives for containment, renegotiation, and member revolt. Every alternative rejoins row 68; changing `africa_constitution` or a crisis flag alone is insufficient.

## Route-sensitive shared support lanes

Support content is shared in source but not constitution-neutral in play. The tree contains three visual lanes:

- Material settlement: rows 69-72.
- Social legitimacy: rows 73-75.
- Continental strategy: rows 76-78.

The exact 36 visible support IDs are:

### Corridor philosophy cluster, 4

- `africa_support_choose_corridor_philosophy`
- `africa_support_corridor_local_guarantees`
- `africa_support_corridor_continental_standards`
- `africa_support_prove_common_passage`

### Resource settlement cluster, 4

- `africa_support_settle_resources`
- `africa_support_resource_contracts`
- `africa_support_resource_revenue_shares`
- `africa_support_anti_extraction_court`

### Food, water, and health cluster, 5

- `africa_support_food_water_health`
- `africa_support_food_network`
- `africa_support_water_compact`
- `africa_support_continental_health_service`
- `africa_support_survival_proof`

### Military purpose cluster, 4

- `africa_support_define_military_purpose`
- `africa_support_command_relationship`
- `africa_support_common_logistics`
- `africa_support_civilian_oversight`

### Diaspora programme cluster, 4

- `africa_support_open_diaspora_programme`
- `africa_support_diaspora_right_of_return`
- `africa_support_diaspora_skills_and_capital`
- `africa_support_diaspora_local_consent`

### Intelligence purpose cluster, 3

- `africa_support_define_intelligence_purpose`
- `africa_support_intelligence_charter`
- `africa_support_regional_intelligence_bureaux`

### Restoration sequence cluster, 3

- `africa_support_restore_by_consent`
- `africa_support_restoration_claims`
- `africa_support_restoration_proof`

### Scramble response cluster, 3

- `africa_support_answer_the_scramble`
- `africa_support_scramble_diplomatic_front`
- `africa_support_anti_partition_guarantees`

### Constitutional review cluster, 3

- `africa_support_postwar_constitutional_review`
- `africa_support_review_convention`
- `africa_support_review_settlement`

### External sponsorship cluster, 3

- `africa_support_sponsor_another_continent`
- `africa_support_choose_external_partner`
- `africa_support_external_sponsorship_mandate`

Each anchor calls a route-aware helper rather than duplicating seven nearly identical reward blocks. Proposed helpers are `africa_focus_resolve_corridor_philosophy`, `africa_focus_resolve_resource_settlement`, `africa_focus_resolve_social_provision`, `africa_focus_resolve_military_purpose`, `africa_focus_resolve_diaspora_programme`, `africa_focus_resolve_intelligence_purpose`, `africa_focus_resolve_restoration_sequence`, `africa_focus_resolve_scramble_response`, `africa_focus_resolve_constitutional_review`, and `africa_focus_resolve_external_sponsorship`.

Those helpers branch on `africa_constitution`, then on `africa_regional_overlay` and the host playbook only where the accepted payoff calls for host variation. They modify the existing League values and unlock decisions; they do not create duplicate numeric state or infer route from completed focus IDs.

## Formation and post-formation band

The exact 20-focus final band is:

1. `africa_charter_league_declared`
2. `africa_seat_the_first_member_council`
3. `africa_write_accession_law`
4. `africa_build_the_continental_secretariat`
5. `africa_fund_the_common_budget`
6. `africa_open_the_charter_court`
7. `africa_ratify_common_defence`
8. `africa_launch_continental_infrastructure`
9. `africa_balance_host_and_regions`
10. `africa_convert_protected_members`
11. `africa_admit_the_first_chartered_member`
12. `africa_create_autonomous_federal_regions`
13. `africa_integrate_a_proven_region`
14. `africa_answer_a_leaving_member`
15. `africa_break_a_rival_bloc`
16. `africa_publish_the_continental_record`
17. `africa_call_the_postwar_convention`
18. `africa_settle_the_second_generation`
19. `africa_open_the_african_century`
20. `africa_one_continent_many_peoples`

The route capstone and the support lanes converge on `africa_charter_league_declared`. Relationship-state focuses call the existing atomic relationship-transition effects; they do not set opinion thresholds or grant integration directly. `africa_integrate_a_proven_region` requires the full relationship and proof gate. `africa_one_continent_many_peoples` is a settlement capstone, not a tag-change shortcut or a claim that all 215 candidate polities have been spawned.

## Host proof, failure, and recovery

Focus completion may prepare, finance, or authorise proof. It may not declare that a corridor worked, a partner survived, a guarantee held, or a war was mediated. The existing `africa_first_proof_type` selects exactly one of seven real mission families:

| Proof constant | Proposed mission ID | Success evidence |
|---|---|---|
| `defended_partner` | `africa_host_proof_defended_partner` | The bound partner survives the threat window and the promised support/guarantee condition is actually met. |
| `aid_corridor` | `africa_host_proof_aid_corridor` | A selected corridor reaches a valid partner and the required aid is delivered before expiry. |
| `diplomatic_recognition` | `africa_host_proof_diplomatic_recognition` | The named state or accepted coalition grants recognition after the required diplomatic work. |
| `punitive_expedition` | `africa_host_proof_punitive_expedition` | The bounded expedition meets its war objective without turning into unrestricted conquest. |
| `transport_link` | `africa_host_proof_transport_link` | The selected rail, road, river, port, air, or convoy connection is operational in the named scopes. |
| `preserved_guarantee` | `africa_host_proof_preserved_guarantee` | The protected state remains sovereign and the host continues to satisfy the guarantee obligation. |
| `mediated_war` | `africa_host_proof_mediated_war` | The named conflict reaches the accepted mediated settlement rather than merely timing out. |

The proof state contract is:

- `africa_first_proof_pending`: initial state, already set by the opening initializer.
- `africa_first_proof_succeeded`: the original mission achieved its real success trigger.
- `africa_first_proof_failed`: the mission timed out, aborted, lost its target, or violated its obligation.
- `africa_first_proof_recovery_active`: action 101 has begun a bounded retry.
- `africa_first_proof_recovered`: the retry achieved its real success trigger.

`africa_focus_first_proof_satisfied` is true only for original success or recovered success. It gates `africa_choose_constitutional_principle` and later host-mandate capstones.

Action 101 is not a pay-to-clear button. It must:

1. Require `africa_first_proof_failed` and no active recovery.
2. Revalidate or deliberately replace the failed target through a visible choice.
3. Preserve the original proof family recorded in `africa_first_proof_type`.
4. Apply the accepted extra political, capacity, time, or trust cost.
5. Start a new mission with success, failure, and target-loss outcomes.
6. Set `africa_first_proof_recovered` only when that mission succeeds.

Success, failure, and recovery completion all call the layout-refresh helper because opening and route availability changes. None of these effects runs from a daily, weekly, or monthly all-country on action.

## One-time host succession and focus recovery

Host succession is Event 12 continuity, not a new Event 12 roll. It may occur once, governed by the global flag `africa_host_successor_consumed`.

The transfer must execute while the old host remains a valid country scope. The old host pointer must be retained through the same effect chain, or through a temporary global target that is explicitly cleared. The required order is:

1. Validate the accepted successor gate and confirm `africa_host_successor_consumed` is absent.
2. Preserve the current host as `event_target:africa_previous_host` before clearing `africa_host`.
3. Select one eligible successor from the accepted relationship/member pool. The successor must have a proven relationship, usable territory, functioning government, and no incompatible terminal identity.
4. Copy the Event 12 state ledger: constitutional value, grounded-origin flag, host-origin playbook and overlay, proof state, League measures, relationship bookkeeping, route/crisis outcomes, active obligations, and accepted arrays/targets. Do not rerun `africa_initialize_selected_host`, because it would erase that state.
5. Load `africa_continental_focus_tree` on the successor with `keep_completed = no` and `copy_completed_from = event_target:africa_previous_host`.
6. Set `africa_unifier_host` and `africa_continental_focus_tree_loaded` on the successor, clear `africa_unifier_host` from the previous host, retarget global `africa_host`, and set `africa_host_successor_consumed`.
7. Refresh layout on the successor after variables and completed-focus state are present.
8. Clear any temporary global previous-host or successor target.

The semantic core of the tree transfer is:

```hoi4
event_target:africa_successor = {
	load_focus_tree = {
		tree = africa_continental_focus_tree
		keep_completed = no
		copy_completed_from = event_target:africa_previous_host
	}
}
```

Installed engine documentation explicitly defines `copy_completed_from` for a valid country. Here both event targets point to valid country scopes. This copies completion state for Event 12 focus IDs; it does not rerun their rewards and does not copy variables, flags, arrays, targets, decisions, or ideas. Those surfaces require the explicit state-ledger transfer in step 4.

The origin remains frozen. The successor does not call `africa_apply_mapped_host_playbook` over the inherited values. `africa_host_playbook`, `africa_host_depth`, `africa_regional_overlay`, and the grounded-origin route continue to describe the Event 12 project's origin; a separate successor-local flavour value may describe the new public host if the country package needs it. The successor keeps its own tag, politics, leaders, and public identity.

If an annexation or deletion effect would invalidate the previous host before step 5, that ordering must be corrected. There is no authorised substitute that guesses completed focuses after the source country is gone.

Civil war does not reset the tree because `reset_on_civilwar = no`. A civil-war winner is not automatically the constitutional successor; it must pass the same accepted one-time transfer gate.

## AI architecture

Every visible focus needs an `ai_will_do` block. Route validity, proof state, current war obligations, capacity, and actual targets must affect AI choices; flat weights across an entire band are not acceptable.

### AI priority composition

AI weighting uses six layers:

1. **Phase:** opening survival, proof, constitutional settlement, support, crisis, or post-formation.
2. **Regional overlay:** one of the nine values already stored in `africa_regional_overlay`.
3. **Host playbook:** one of the 22 full profiles; compact playbooks use the regional base plus their explicit compact-signature modifiers.
4. **Constitution:** one of seven route profiles, with invalid grounded routes receiving factor zero after commitment.
5. **Live urgency:** proof deadline, partner threat, food/health failure, active war, member departure, free rider, Covenant breach, or commander crisis.
6. **Feasibility:** real target exists, action capacity exists, corridor or access is possible, and required state is not terminal.

Suggested focus-file constants are `@africa_focus_ai_disabled`, `@africa_focus_ai_low`, `@africa_focus_ai_normal`, `@africa_focus_ai_elevated`, `@africa_focus_ai_high`, `@africa_focus_ai_urgent`, and `@africa_focus_tree_actor_priority`. Tuning values referenced outside the focus file belong in a new `africa_focus_ai` category in `012_africa_constants.txt`.

### Required AI behaviour

- Before first proof, AI prioritises host capacity, corridor, partner, and the active proof mission. It does not select a constitution early.
- On proof failure, action 101 and the required recovery focuses outrank unrelated support content.
- At the constitutional threshold, the six grounded openers use route-specific validity and desire. An invalid route is factor zero, not merely a small preference.
- After commitment, all other grounded route bodies are factor zero and hidden after layout refresh.
- Crisis focus/decision pairs outrank their capstone and block it until resolution.
- The Covenant is factor zero before reveal. After reveal, it remains a costly choice whose weight depends on actual nonhuman/ecological pressure, consent commitment, ecological wrath, host profile, and current grounded route.
- AI never chooses a focus that lacks a real decision target merely because the focus is available.
- Active defensive obligations increase proof, logistics, food/health, and common-defence priorities. They do not create a universal war-route preference.
- Weak hosts prioritise capacity and narrow regional obligations. Strong hosts receive less free assistance and prioritise suspicion, representation, and burden management.
- Compact hosts prioritise distinct-role and viability proof before action 102 promotion.
- Post-formation AI responds to live relationship counts: protected, associate, chartered, autonomous-federal, integrated, resistant, leaving, and rival-bloc. Opinion values are never substituted for those states.

The 64-row AI acceptance matrix remains the behavioural source of truth. Focus implementation must prove coverage for all nine regional profiles, all 22 full host profiles, all seven constitutional profiles, the compact-signature layer, relationship states, crisis states, and outside actors. A single default block does not satisfy that matrix.

### AI scenario audit

At minimum, record outcomes for:

- all 51 host playbooks loading the same tree with the correct overlay and signature depth;
- all nine regional overlays;
- all six grounded route selections and the hidden Covenant transformation;
- original proof success, each of the seven proof failures, and action 101 recovery;
- weak, regional, and strong host support classes;
- peace, defensive war, offensive war, and threatened partner states;
- compact promotion eligible and ineligible states;
- each route crisis action 093-099 and postwar action 100;
- one-time successor transfer before and after route commitment;
- Covenant disabled, revealed, accepted, contained, renegotiated, and revolted states.

The audit must identify focus IDs selected and the live modifiers responsible. "The AI eventually progressed" is not sufficient evidence.

## Layout contract and focus audit

### Coordinate bands

Use these coordinate envelopes as the first implementation layout:

| Band | Coordinate envelope | Notes |
|---|---|---|
| Shared opening | `x = 24..46`, `y = 0..9` | Three early lanes converge on proof and congress. |
| Regional overlay | `x = 6..20`, `y = 2..9` | All nine overlays reuse one mutually exclusive six-node template. |
| Host signature | `x = 50..62`, `y = 3..9` | Two compact or four full slots; never overlap the active overlay. |
| Grounded route openers | `x = 8,18,28,38,48,58`, `y = 11` | All six are visible before commitment; only the chosen body appears. |
| Grounded route body | `x = 8..46`, `y = 12..25` | All six bodies reuse one mutually exclusive template. |
| Covenant body | `x = 52..70`, `y = 12..25` | Separate because grounded history and Covenant may be visible together. |
| Support lanes | `x = 4..68`, `y = 26..36` | Three interlocked lanes, with controlled cross-lane rejoins. |
| Formation/post-formation | `x = 18..54`, `y = 37..46` | Centered convergence and final settlements. |

Set `initial_show_position` around the opening center and place `continuous_focus_position` outside the final band's connector field.

### Layout rules

- Simultaneously visible focuses never share coordinates.
- Same-row focuses keep at least two x units of separation unless the renderer proves the icons and text do not collide.
- Every child is below its parent.
- No connector passes through a focus node.
- Route openers form one contiguous row and every `mutually_exclusive` relation is symmetric.
- An inactive overlay or route may reuse the active branch's coordinates only when their `allow_branch` predicates are provably mutually exclusive.
- Covenant coordinates never reuse grounded-route body coordinates because both histories may be visible.
- Route choice, proof resolution, Covenant reveal/commitment, crisis correction, compact promotion, formation transition, and host succession all call `africa_refresh_continental_focus_tree_layout`.
- No focus becomes reachable only because another branch was hidden; availability and prerequisites must independently prove reachability.

### Event 15 lessons applied

The Event 15 final audit found that dynamic `allow_branch` state needs explicit layout refresh, crisis-driven route changes need alternative prerequisites and rejoins, AI modifiers must use correct live scopes, and layout success requires more than unique coordinates. Event 12 adopts all four findings. Its final audit must report focus count, connector count, coordinate collisions, parent-below-child errors, asymmetric exclusions, connector-through-node incidents, dangling prerequisites, unreachable nodes, and route-specific visible counts.

The installed HOI4 focus inspection/render tool should be used after the tree exists. An attempted inspection during this planning pass returned `ARTIFACT_STORAGE_LIMIT` for both the Event 6 and Event 15 reference trees; manual source inspection was completed instead. The implementation audit must retry `hoi4.focus_inspect`, render, and lint after artifact storage is available. This tooling failure is not evidence that the future tree is valid.

## Reward and balance contract

Focus rewards call scripted helpers and existing atomic relationship effects. They do not duplicate the League state kernel in the focus file.

Only three permanent national-spirit families may originate from the focus tree:

1. `africa_constitutional_framework`
2. `africa_continental_development_compact`
3. `africa_continental_service`

Routes and capstones upgrade or exchange those families; they do not accumulate one permanent spirit per payoff row. Other rewards use the existing League measures, decision unlocks, timed modifiers, relationship transitions, technology or doctrine bonuses, bounded construction, equipment tied to a real programme, and event consequences.

Balance review must inspect:

- weak, regional, and strong host scaling;
- the action, selected-target, dossier, and living-core-project caps;
- authority, reach, burden, colonial pressure, consent, central capacity, regional equality, emergency-rule debt, ecological wrath, and war-readiness interactions;
- route choice costs and capstone proof requirements;
- focus duration against the timed proof and crisis missions;
- industry, manpower, equipment, technology, and doctrine totals for each visible 101/103-focus campaign;
- AI focus timing in peace and war;
- the three-spirit cap and every spirit upgrade path.

No focus may use a hardcoded tag to determine reward scale. Host variation reads the stored playbook/depth/overlay values. File-scoped duration constants should distinguish emergency, short, standard, institution, crisis, and capstone focuses so timing remains tunable in one place.

## Localisation and focus-icon handoff

Every focus ID needs a title and description in a UTF-8-with-BOM English localisation file, without `:0`. Descriptions state the institution, world-state consequence, real choice, and tradeoff; they do not mention implementation history, caps, hardcoding, or rework.

The six shared host-signature slots require scripted-localisation cases for all 51 playbooks. Missing cases must display a deliberate error key during development, not generic final text. Route and regional names use the accepted specification wording, including `People's Union`, `Council of Crowns`, and `Covenant with the Land and Nonhuman Congress`.

Accepted focus asset families 97-138 and route-capstone seal family 239 are the icon source of truth. Proposed wiring is:

- DDS sources: `gfx/interface/goals/012_africa/`
- Sprite definitions: `interface/012_africa_focus_icons.gfx`
- Sprite ID pattern: `GFX_goal_africa_<accepted_asset_family_slug>`

Opening nodes use host proclamation, legitimacy, protection, aid, and representation families. Constitutional nodes use federal accession, crown charter, republican citizenship, people's union, military command, confederal sovereignty, high-chaos nature/nonhuman, and capstone-seal families. Support and formation use congress, restoration, resource, food, corridor, defence, intelligence, diaspora, rival-bloc, Scramble, sponsorship, union, and world families.

No generic icon may be presented as final for an accepted family whose asset remains pending. Focus implementation, `.gfx` registration, DDS production, localisation references, asset manifest, and documentation must agree on the final filenames before completion is claimed.

## Proposed implementation surfaces

The main implementation should touch these Event 12 surfaces together:

| Surface | Required work |
|---|---|
| `common/national_focus/012_africa_continental_focus_tree.txt` | Tree header, all focus definitions, coordinates, prerequisites, exclusions, availability, bypasses, rewards, and AI. |
| `common/scripted_effects/012_africa_effects.txt` | Load, layout refresh, route commit, Covenant reveal/commit, focus rewards, proof outcomes, compact promotion, and successor-ledger transfer. |
| `common/scripted_triggers/012_africa_triggers.txt` | Tree, overlay, route, proof, capstone, successor, and AI feasibility triggers. |
| `common/script_constants/012_africa_constants.txt` | Cross-file focus thresholds, AI tuning, proof/recovery tuning, and successor constraints. |
| Event 12 decisions and missions | The seven proof families, actions 093-102, support projects, capstone proofs, and failure/recovery. |
| `events/012_african_union.txt` | Route choices, crises, host events, proof outcomes, hidden layout refresh if required, and successor transition. |
| Event 12 AI strategy files | Regional, host, route, relationship, crisis, and outside-actor behaviour from the 64-row matrix. |
| Event 12 localisation | All focus, decision, mission, event, tooltip, dynamic host-signature, and scripted-localisation keys. |
| `interface/012_africa_focus_icons.gfx` and assets | Registered icon families and route seals. |
| Event 12 documentation and logs | Mechanic documentation, event details, evolution/log mappings, asset manifest, and completion report. |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Update only after implementation facts and in-game wording exist, then run `.tools/export_event_catalog_csv.py`; never edit exports directly. |

If focus rewards require a new reusable dynamic effect, add it to `common/scripted_effects/chaosx_dynamic_effects.txt` and document purpose, scope, inputs, outputs, defaults, side effects, and an example in `chaosx_dynamic_effects.md` in the same change.

## Implementation order

1. Add focus constants, overlay/route/proof triggers, and the load/layout helpers.
2. Wire controlled replacement into `africa_initialize_selected_host` after playbook classification.
3. Implement the 16-focus opening and seven proof mission families, including action 101 recovery.
4. Implement all nine overlays and the full/compact signature slots with all 51 playbook cases.
5. Implement the six grounded routes, their decision crises 093-098, and explicit correction/rejoin topology.
6. Implement the three support lanes and action 102 promotion.
7. Implement Covenant reveal, its 18-focus route, action 099, and grounded-origin retention.
8. Implement the 20-focus formation/post-formation band and action 100.
9. Implement one-time successor transfer with completed-focus copying and explicit state-ledger transfer.
10. Add AI, localisation, final icons, event logs/details, mechanic documentation, and spreadsheet alignment.
11. Run focus inspection/render/lint, route and host scenario audits, balance review, specialist focus audit, localisation audit, and Event 12 completion audit.

## Completion checklist

The focus architecture is not complete until all statements below have evidence:

- [ ] One controlled load occurs for every eligible selected host and no additive assignment path remains.
- [ ] All 78 payoff anchors exist exactly once and have gameplay, choice/consequence, AI, localisation, and icon coverage.
- [ ] All nine overlays are statically defined, exactly one is visible, and all 51 playbooks map to the implemented overlay table.
- [ ] All 22 full and 29 compact playbooks have explicit signature text, reward, proof, event, and AI cases.
- [ ] The six grounded routes expose 21 meaningful focuses each; the Covenant exposes 18.
- [ ] All constitutional splits have symmetric exclusions and explicit rejoins.
- [ ] Actions 093-102 are implemented and bound to the listed anchors.
- [ ] All seven proof mission families can succeed, fail, lose their target, and use the bounded action 101 recovery path.
- [ ] Route choice is impossible before proof, and route capstones require real off-tree evidence.
- [ ] Covenant reveal and acceptance refresh layout without hiding or stranding grounded history.
- [ ] The support band exposes all 36 IDs and resolves rewards through all seven constitutions.
- [ ] The formation band exposes all 20 IDs and uses atomic relationship-state transitions.
- [ ] Every focus has a reviewed `available`, `bypass`, `completion_reward`, `ai_will_do`, title, description, effect tooltip, and registered icon.
- [ ] Ordinary compact and full campaigns expose 101 and 103 focuses respectively; high-chaos adds 18 Covenant focuses.
- [ ] Focus inspection reports no duplicate IDs, dangling prerequisites, unreachable nodes, asymmetric exclusions, coordinate collisions, inverted connectors, or connector-through-node incidents.
- [ ] All 51 host, nine overlay, seven route, proof/recovery, crisis, compact-promotion, civil-war, and successor scenarios have recorded results.
- [ ] Balance review covers the full reward totals, values, caps, timings, AI behaviour, and three-spirit limit.
- [ ] Focus, event, decision, mission, AI, localisation, assets, logs/details, documentation, and workbook wording agree.
- [ ] The specialist focus-tree, localisation, and Event 12 completion audits report no unresolved completion blocker.

## Blockers, risks, and simplifications

### Current blockers and risks

- The focus tree and its supporting decisions, AI, localisation, and assets did not exist when this handoff was authored; this document is not implementation evidence.
- HOI4 MCP inspection of the Event 6 and Event 15 reference trees failed with `ARTIFACT_STORAGE_LIMIT`. Manual source and documentation review established the architecture, but the implemented Event 12 tree still requires a successful inspect/render/lint pass.
- Completed focus IDs from the pre-Event-12 tree cannot be retained unless the same IDs exist in the new tree. Duplicating unrelated IDs is unsafe and prohibited. The authorised replacement preserves already-applied effects and the host-origin ledger, not the former focus checklist.
- Successor completion copying requires the previous host to remain a valid country scope through `load_focus_tree`. Transfer must precede any effect that invalidates that scope.
- Final focus icon families are accepted in the asset matrix but remain implementation work. Placeholder or generic final icons would block completion.

### Simplifications

No design row, host playbook, regional overlay, constitution, proof family, route crisis, support lane, or post-formation band was omitted or replaced with a fallback in this architecture. Shared host-signature focus slots are intentionally dynamic rendering slots, but their contract still requires bespoke cases for every one of the 51 playbooks; they are not permission to provide generic content.

The controlled replacement itself is not a simplification. It is the source-authorised Event 12 transformation selected after additive shared-focus feasibility was disproved against the engine, vanilla, and the repository's own Event 6 precedent.
