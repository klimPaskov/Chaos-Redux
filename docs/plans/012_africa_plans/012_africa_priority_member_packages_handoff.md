# Event 012 Africa priority-member country-package overlay handoff

Date: 2026-07-18

## Status

The bounded gameplay overlay for all 16 rows in the priority-member package matrix is implemented. No priority row was merged, rejected, or queued inside this overlay. Parent integration also supplies one dynamically loaded eight-focus package tree and a 35-idea lifecycle: sixteen distinct starting problems, three political-settlement stages, and sixteen distinct mature compacts. This parameterises common structure while preserving package-specific institutions, economies, forces, League roles, overlap settlements, post-settlement programmes, localisation, rewards, and AI priorities.

This is not a whole-country-package completion claim. Formation or release scripts, specialist confirmation of compact territory, leaders or council portraits, national flags, and final visual assets remain parent-owned integration work. All sixteen promoted packages now apply a persistent direct-name cosmetic identity with complete ideology variants while retaining the carrier's original tag, history, government, states, and cores. All current priority-member focus, idea, decision, category, and report-picture sprite IDs are registered under stable final paths, but their DDS files remain unresolved until the asset tranche produces them.

Parent integration on 2026-07-18 connected this overlay to a bounded promotion survey and the live Action 102 gate. The survey recognises all sixteen accepted carrier identities, records the eight formerly missing origin markers, scores the six documented promotion conditions, requires at least three conditions plus the Action 102 local-support floor, and selects the exact country on the existing Charter action card. It creates no tag, transfers no state, grants no core, and changes no relationship stage.

The other 36 Tier A entries in the 52-row Tier A polity catalog are not silently treated as full packages. They remain compact, dormant, cultural, autonomous, associated, or later-promotion candidates under the source specification.

## Owned files

- common/script_constants/012_africa_priority_member_constants.txt
- common/ideas/012_africa_priority_member_ideas.txt
- common/national_focus/012_africa_priority_member_focus.txt
- common/scripted_triggers/012_africa_priority_member_triggers.txt
- common/scripted_effects/012_africa_priority_member_effects.txt
- common/scripted_effects/012_africa_priority_member_force_effects.txt
- common/scripted_effects/012_africa_action_effects.txt
- common/scripted_localisation/012_africa_scripted_localisation.txt
- common/scripted_localisation/012_africa_priority_member_scripted_localisation.txt
- common/decisions/012_africa_decisions.txt
- common/decisions/categories/012_africa_priority_member_categories.txt
- common/decisions/012_africa_priority_member_decisions.txt
- events/012_africa_priority_member_events.txt
- localisation/english/012_africa_priority_member_l_english.yml
- localisation/english/012_africa_priority_member_countries_l_english.yml
- localisation/english/012_africa_priority_member_focus_l_english.yml
- interface/012_africa_priority_member_assets.gfx

Focus texture folder:

- gfx/interface/goals/012_africa/priority_members/

Idea texture folder:

- gfx/interface/ideas/012_africa/priority_members/
- docs/plans/012_africa_plans/012_africa_priority_member_packages_handoff.md

No Event 012 RSA, workbook, specification, or matrix file was edited by this focus-and-lifecycle tranche.

## Sources and implementation guidance used

Repository skills:

- chaos-redux-events
- chaos-redux-subagents
- chaos-redux-improvement-loop
- hoi4-decisions-missions
- hoi4-focus-trees

Required offline wiki pages:

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
- Division modding

Vanilla documentation and precedents:

- documentation/script_concept_documentation.md, especially Script Constants
- common/script_constants/documentation.md
- documentation/effects_documentation.md
- documentation/triggers_documentation.md
- documentation/modifiers_documentation.md
- common/national_focus/generic.txt
- events/BBA_Ethiopia.txt
- common/scripted_effects/006_independence_wave_force_effects.txt
- common/scripted_effects/006_independence_wave_decision_effects.txt
- common/decisions/African_Union_decisions.txt
- common/decisions/categories/African_Union_decision_categories.txt

Event 012 sources:

- spec part 9 priority-member country packages
- priority-member package matrix and notes
- polity catalog
- implementation acceptance and catalog reconciliation
- language, naming, and sensitivity protocol
- Event 012 implementation source map
- Charter relationship state-machine specification

No web research was used.

## Runtime flow

1. A country is formed, released, or otherwise given an exact priority origin.
2. Existing Action 102, promote_priority_member_package, resolves either a full promotion or negotiated compact result.
3. A full result invokes africa_priority_member_register_from_origin. A partial result stops at Protected status for an outside candidate or Associate status for an already Protected candidate, records one access, overlap, or local-ratification obstacle, and does not activate the full package.
4. The bounded requalification decision checks the live obstacle requirement, rebuilds the dossier, and permits another Action 102 attempt. Registration validates the later full result and exact origin, assigns one stable package ID, applies the matching direct public identity without replacing the original tag, creates no territory or core change, and opens the political settlement.
5. The country chooses one of three political routes with a package-specific named council, civic government, or producer institution.
6. The country advances a four-step distinct mechanic and a separate four-step force-reinforcement track.
7. League bargaining uses only the shared africa_apply_relationship_transition state machine.
8. The overlap event records congress, local consent, autonomy, or rivalry without automatic cores, annexation, or maximal borders.
9. Departure supports renewal, a 90-day negotiated withdrawal, or an explicit rival-bloc course.
10. A repeatable post-settlement action remains available after the political, League, and overlap settlements are recorded.
11. Full registration sets the package-selection flag before loading africa_priority_member_focus_tree. Engine `keep_completed` semantics retain only focus IDs shared by the former and replacement trees; the Event 012 host and its continental tree are not touched.
12. The overlay consumes the existing political, distinct-mechanic, force, relationship, overlap, and post-settlement states. It does not create a duplicate legitimacy store or infer a Charter relationship from opinion.
13. Completing the political focus replaces the starting problem with the selected council, civic, or producer settlement idea. Completing the final focus replaces that stage with the package's distinct mature compact.
14. Full registration also defines one package-named force template and raises one understrength primary guard from owned, controlled territory. If the carrier still fields fewer than two divisions after that guard is raised, it receives one package-named reserve. Carriers with established forces retain them and receive only the identity-bearing guard.
15. Starting equipment and manpower factors scale from Action 102's recorded local-support dossier. Initial experience uses the matrix's compact, standard, or trained force base. The existing four-step package reinforcement route remains the only readiness progression.
16. A package promoted while all owned states are occupied does not spawn behind enemy lines. The same bounded initializer retries on the next legal force-reinforcement action.

## Action 102 integration contract

Action 102 is the only promotion gate. Registration requires:

- africa_priority_package_promotion_approved

Registration also requires:

- africa_event_active
- a valid africa_host event target with africa_host_commit_completed
- an exact valid priority origin
- no active priority package already registered

Preferred country-scope API after Action 102 has written its result:

- africa_priority_member_register_from_origin = yes

The normal player and AI path is the direct Action 102 call. It opens africa_priority_member.1200 only when africa_priority_member_can_open_political_settlement is true. The bounded ratification decision uses the same helper and remains available for an idempotent delayed-origin recovery after a full result. A partial result cannot satisfy africa_priority_member_can_register_package.

Low-level explicit-ID API, for a caller that already knows the exact package:

1. Set the temporary africa_priority_requested_package_id to constant:africa_priority_member_package.<key>.
2. Call africa_priority_member_register_requested_package = yes.

The low-level API still validates that the requested ID matches the country's origin. It cannot be used to promote an unrelated tag.

### Missing-identity origin handoff

The bounded survey records these exact carrier-to-package origins before Action 102 validation:

- SOK -> africa_priority_origin_sokoto
- MLI -> africa_priority_origin_manden
- UGA -> africa_priority_origin_buganda
- TIG -> africa_priority_origin_aksum
- HAR -> africa_priority_origin_harar
- SUD -> africa_priority_origin_nubia
- ZIM -> africa_priority_origin_great_zimbabwe
- MAD -> africa_priority_origin_merina

The other eight packages continue to use their installed Event 6 or accepted carrier identities. All sixteen are eligible only through `africa_selected_targets`, which is filled by an explicit bounded contact refresh rather than a recurring scan. This tranche deliberately does not create new tags or maximal territorial releases.

The survey recomputes, rather than caches, the six promotion conditions:

- viable compact territory under the candidate's ownership and control
- local support or a functioning carrier institution
- an economic or strategic function beyond symbolic restoration
- an unresolved relationship problem with the League
- enough surviving population and infrastructure for meaningful play
- a distinct package identity not already supplied by a neighbour

At least three conditions and the Action 102 local-support floor are required. The dossier exposes the condition count and local-support value. Opinion is not an input. Action 102 runs the evaluator again during launch validation, so a stale survey cannot promote an invalid country.

Do not set an origin flag on a cultural body, temporary transition subject, unrelated cosmetic route, or unreviewed maximal-territory claimant.

## Unity and constitutional-consent contract

Package discovery does not grant continental consent.

The exact helper effects are:

- africa_priority_member_record_constitutional_acceptance
- africa_priority_member_withdraw_constitutional_acceptance

Explicit League acceptance, a negotiated counterproposal, and relationship renewal call the first helper. It sets:

- africa_member_allied_settlement_accepted
- africa_member_continental_constitution_accepted

League refusal, a rival overlap settlement, peaceful-withdrawal initiation, and rival departure call the second helper and clear both flags.

Every cooperative transition uses africa_apply_relationship_transition, which records the current africa_member_host_generation. This satisfies the parent unity predicate without granting acceptance during package discovery.

## Achievement and proof API

A successful non-AI registration:

- sets africa_priority_member_player_origin_validated
- calls africa_achievement_register_valid_priority_player = yes
- sets exactly one africa_priority_player_origin_<key> flag

If an already-registered AI package later becomes the player through an authorised switch, that switch-validation path must call africa_achievement_register_valid_priority_player = yes separately. Registration does not infer later player control.

Stable generic proofs:

- africa_priority_member_package_active
- africa_priority_member_package_id
- africa_priority_member_politics_settled
- africa_priority_member_council_route
- africa_priority_member_civic_route
- africa_priority_member_producer_route
- africa_priority_member_overlap_disposition_recorded
- africa_priority_member_overlap_congress_settlement
- africa_priority_member_overlap_local_consent_settlement
- africa_priority_member_overlap_autonomy_settlement
- africa_priority_member_overlap_rival_settlement
- africa_priority_member_mechanic_complete
- africa_priority_member_force_ready
- africa_priority_member_post_settlement_mature
- africa_priority_member_rival_bloc_victory

Stable package proof patterns:

- africa_priority_member_package_is_<key>
- africa_priority_<key>_mechanic_complete
- africa_priority_<key>_force_ready
- africa_priority_<key>_<mode>_settlement
- africa_priority_<key>_post_settlement_action_completed
- africa_priority_<key>_rival_bloc_victory

The package-country victory hook is:

- africa_priority_member_record_rival_bloc_victory = yes

Call it in country scope from a bounded peace, capitulation, or scripted victory transaction after that package is the victorious rival actor.

Achievement-critical distinct proofs retained exactly:

- africa_priority_aksum_heritage_consent_separated
- africa_priority_harar_corridor_guarantees_diversified
- africa_priority_kilwa_common_customs_arbitrated
- africa_priority_nubia_river_rights_recognised
- africa_priority_luba_mining_revenue_settled
- africa_priority_lunda_cross_border_access_settled
- africa_priority_great_zimbabwe_restoration_mandate_balanced
- africa_priority_luba_public_processing_programme_active
- africa_priority_great_zimbabwe_public_processing_programme_active

## Runtime cleanup API

The full package teardown hook is:

- africa_priority_member_cleanup_runtime = yes

It cancels the withdrawal mission, clears the package ID and three progress variables, and removes live package, overlap, bargaining, withdrawal, and post-settlement-open state. It deliberately preserves origin, political-route, settlement, mechanic-completion, force-completion, player-origin, and rival-victory proofs.

Call it only after final achievement and ending evaluation has consumed the active package ID. It is not a normal settlement completion effect because packages are intended to remain playable.

## Event range

The namespace africa_priority_member is unique in the repository. The range africa_priority_member.1200 through .1299 is reserved for this layer.

| Event | Purpose |
|---|---|
| africa_priority_member.1200 | package-specific political settlement |
| africa_priority_member.1210 | League bargaining, counterproposal, refusal, or departure referral |
| africa_priority_member.1220 | congress, consent, autonomy, or rival overlap settlement |
| africa_priority_member.1230 | renewal, negotiated withdrawal, or rival departure |

Each event has 16 conditional direct-name descriptions. All 14 options have explicit AI weights.

## Package ledger

The common dependencies listed after this table apply to every row.

| ID | Key and public name | Origin validation | Distinct mechanic proof | Overlay disposition |
|---:|---|---|---|---|
| 1 | asante, Asante | original_tag DOX, or africa_priority_origin_asante | africa_priority_asante_stool_council_legitimacy_built | implemented |
| 2 | oyo, Oyo | original_tag DSX, or africa_priority_origin_oyo | africa_priority_oyo_corridor_city_compact_operational | implemented |
| 3 | sokoto, Sokoto | africa_priority_origin_sokoto required | africa_priority_sokoto_emirate_reform_compact_operational | implemented |
| 4 | kanem_bornu, Kanem-Bornu | original_tag DUX, or africa_priority_origin_kanem_bornu | africa_priority_kanem_bornu_lake_caravan_covenant_operational | implemented |
| 5 | manden, Manden | africa_priority_origin_manden required | africa_priority_manden_assembly_legitimacy_built | implemented |
| 6 | kongo, Kongo | original_tag COG with COG_kingdom_of_kongo, or africa_priority_origin_kongo | africa_priority_kongo_cross_border_consent_recorded | implemented |
| 7 | buganda, Buganda | africa_priority_origin_buganda required | africa_priority_buganda_kingdom_federal_balance_recorded | implemented |
| 8 | aksum, Aksum | africa_priority_origin_aksum required | africa_priority_aksum_heritage_consent_separated | implemented |
| 9 | harar, Harar | africa_priority_origin_harar required | africa_priority_harar_corridor_guarantees_diversified | implemented |
| 10 | kilwa, Kilwa | original_tag EMX, or africa_priority_origin_kilwa | africa_priority_kilwa_common_customs_arbitrated | implemented |
| 11 | nubia, Nubia | africa_priority_origin_nubia required | africa_priority_nubia_river_rights_recognised | implemented |
| 12 | luba, Luba | original_tag DYX, or africa_priority_origin_luba | africa_priority_luba_mining_revenue_settled | implemented |
| 13 | lunda, Lunda | original_tag DZX, or africa_priority_origin_lunda | africa_priority_lunda_cross_border_access_settled | implemented |
| 14 | great_zimbabwe, Great Zimbabwe | africa_priority_origin_great_zimbabwe required | africa_priority_great_zimbabwe_restoration_mandate_balanced | implemented |
| 15 | merina, Merina | africa_priority_origin_merina required | africa_priority_merina_island_confidence_recorded | implemented |
| 16 | zulu, Zulu | original_tag EQX, or africa_priority_origin_zulu | africa_priority_zulu_crown_land_labour_balance_recorded | implemented |

Every implemented row has:

- exact origin and package-ID triggers
- three political choices with a named package institution
- one four-stage distinct mechanic
- one four-stage force-reinforcement action
- one preferred League clause
- acceptance, counterproposal, refusal, withdrawal, and rivalry
- four overlap dispositions with package-specific proof
- one repeatable post-settlement action
- AI weights and direct-name localisation

## Balance and tuning

All shared values are centralized in common/script_constants/012_africa_priority_member_constants.txt.

| Surface | Tuning |
|---|---|
| registration | 10 political power |
| politics | 40 political power |
| distinct mechanic | 35 political power, 120-day re-enable, four 25-point steps |
| force reinforcement | 30 political power, 90-day re-enable, requires more than 5,000 manpower and consumes 5,000, four 25-point steps |
| League bargaining | 20 political power, 90-day re-enable |
| overlap settlement | 30 political power |
| departure terms | 10 political power |
| negotiated withdrawal | 90-day mission |
| post-settlement action | 25 political power, 180-day re-enable |

Mechanic rewards are package-specific and use modest equipment, experience, stability, political power, or Charter-value changes. Each package can build only one midpoint project. Kilwa requires an owned and controlled coastal state and receives no inland substitute dockyard. Force actions consume manpower and provide equipment rather than spawning free fantasy armies. AI weights are centralized and route-aware through confidence, constitution, preferred clauses, and rival or refusal state.

League bargaining stops when the package reaches its preferred relationship. An autonomy-review block remains unavailable until the shared autonomous-federal prerequisites become valid, preventing repeated failed offers from becoming a reward loop.

## Asset production contract

There are no generic visual fallbacks in the owned script. The current custom identifiers are defined in the sprite file below, but their final DDS textures have not yet been produced. Until the asset tranche supplies them, presentation is incomplete and the whole package layer must not be reported complete.

Sprite-definition file:

- interface/012_africa_priority_member_assets.gfx

Decision texture folder:

- gfx/interface/decisions/012_africa/priority_members/

Report-picture texture folder:

- gfx/event_pictures/012_africa/priority_members/

Focus icons should be final 95x85 DDS assets with registered shine sprites. Idea icons should be final 64x64 DDS assets. Decision icons should be final 32x32 DDS assets designed for decision use. Report pictures should be final 210x176 DDS assets consistent with the Event 012 asset matrix.

### Shared focus assets

The eight final focus files and their stable sprite IDs use the same suffixes:

- compact_country
- political_settlement
- distinct_institution
- economic_function
- league_role
- national_force
- overlap_question
- post_settlement

For each suffix `<key>`, the base ID is `GFX_goal_012_africa_priority_<key>`, the shine ID is `GFX_goal_012_africa_priority_<key>_shine`, and the final file is `goal_012_africa_priority_<key>.dds`.

### Lifecycle idea assets

The three shared settlement ideas use `GFX_idea_africa_priority_<route>_settlement` and `idea_africa_priority_<route>_settlement.dds` for `council`, `civic`, and `producer`.

Every package key in the 16-row matrix uses both:

- `GFX_idea_africa_priority_<package>_problem` -> `idea_africa_priority_<package>_problem.dds`
- `GFX_idea_africa_priority_<package>_mature` -> `idea_africa_priority_<package>_mature.dds`

### Shared decision and category assets

| Sprite identifier | Final filename |
|---|---|
| GFX_decision_012_africa_priority_member_category | decision_012_africa_priority_member_category.dds |
| GFX_decision_012_africa_priority_member_ratification | decision_012_africa_priority_member_ratification.dds |
| GFX_decision_012_africa_priority_member_political_settlement | decision_012_africa_priority_member_political_settlement.dds |
| GFX_decision_012_africa_priority_member_league_bargain | decision_012_africa_priority_member_league_bargain.dds |
| GFX_decision_012_africa_priority_member_overlap_settlement | decision_012_africa_priority_member_overlap_settlement.dds |
| GFX_decision_012_africa_priority_member_departure_terms | decision_012_africa_priority_member_departure_terms.dds |
| GFX_decision_012_africa_priority_member_withdrawal_recall | decision_012_africa_priority_member_withdrawal_recall.dds |
| GFX_decision_012_africa_priority_member_withdrawal_mission | decision_012_africa_priority_member_withdrawal_mission.dds |

### Package decision assets

The mechanic identifier and filename pattern matches the existing Event 012 asset matrix. Force and post-settlement assets use parallel stable names.

| Package | Mechanic sprite and filename | Force sprite and filename | Post-settlement sprite and filename |
|---|---|---|---|
| asante | GFX_decision_012_africa_priority_member_mechanic_asante, decision_012_africa_priority_member_mechanic_asante.dds | GFX_decision_012_africa_priority_member_force_asante, decision_012_africa_priority_member_force_asante.dds | GFX_decision_012_africa_priority_member_post_settlement_asante, decision_012_africa_priority_member_post_settlement_asante.dds |
| oyo | GFX_decision_012_africa_priority_member_mechanic_oyo, decision_012_africa_priority_member_mechanic_oyo.dds | GFX_decision_012_africa_priority_member_force_oyo, decision_012_africa_priority_member_force_oyo.dds | GFX_decision_012_africa_priority_member_post_settlement_oyo, decision_012_africa_priority_member_post_settlement_oyo.dds |
| sokoto | GFX_decision_012_africa_priority_member_mechanic_sokoto, decision_012_africa_priority_member_mechanic_sokoto.dds | GFX_decision_012_africa_priority_member_force_sokoto, decision_012_africa_priority_member_force_sokoto.dds | GFX_decision_012_africa_priority_member_post_settlement_sokoto, decision_012_africa_priority_member_post_settlement_sokoto.dds |
| kanem_bornu | GFX_decision_012_africa_priority_member_mechanic_kanem_bornu, decision_012_africa_priority_member_mechanic_kanem_bornu.dds | GFX_decision_012_africa_priority_member_force_kanem_bornu, decision_012_africa_priority_member_force_kanem_bornu.dds | GFX_decision_012_africa_priority_member_post_settlement_kanem_bornu, decision_012_africa_priority_member_post_settlement_kanem_bornu.dds |
| manden | GFX_decision_012_africa_priority_member_mechanic_manden, decision_012_africa_priority_member_mechanic_manden.dds | GFX_decision_012_africa_priority_member_force_manden, decision_012_africa_priority_member_force_manden.dds | GFX_decision_012_africa_priority_member_post_settlement_manden, decision_012_africa_priority_member_post_settlement_manden.dds |
| kongo | GFX_decision_012_africa_priority_member_mechanic_kongo, decision_012_africa_priority_member_mechanic_kongo.dds | GFX_decision_012_africa_priority_member_force_kongo, decision_012_africa_priority_member_force_kongo.dds | GFX_decision_012_africa_priority_member_post_settlement_kongo, decision_012_africa_priority_member_post_settlement_kongo.dds |
| buganda | GFX_decision_012_africa_priority_member_mechanic_buganda, decision_012_africa_priority_member_mechanic_buganda.dds | GFX_decision_012_africa_priority_member_force_buganda, decision_012_africa_priority_member_force_buganda.dds | GFX_decision_012_africa_priority_member_post_settlement_buganda, decision_012_africa_priority_member_post_settlement_buganda.dds |
| aksum | GFX_decision_012_africa_priority_member_mechanic_aksum, decision_012_africa_priority_member_mechanic_aksum.dds | GFX_decision_012_africa_priority_member_force_aksum, decision_012_africa_priority_member_force_aksum.dds | GFX_decision_012_africa_priority_member_post_settlement_aksum, decision_012_africa_priority_member_post_settlement_aksum.dds |
| harar | GFX_decision_012_africa_priority_member_mechanic_harar, decision_012_africa_priority_member_mechanic_harar.dds | GFX_decision_012_africa_priority_member_force_harar, decision_012_africa_priority_member_force_harar.dds | GFX_decision_012_africa_priority_member_post_settlement_harar, decision_012_africa_priority_member_post_settlement_harar.dds |
| kilwa | GFX_decision_012_africa_priority_member_mechanic_kilwa, decision_012_africa_priority_member_mechanic_kilwa.dds | GFX_decision_012_africa_priority_member_force_kilwa, decision_012_africa_priority_member_force_kilwa.dds | GFX_decision_012_africa_priority_member_post_settlement_kilwa, decision_012_africa_priority_member_post_settlement_kilwa.dds |
| nubia | GFX_decision_012_africa_priority_member_mechanic_nubia, decision_012_africa_priority_member_mechanic_nubia.dds | GFX_decision_012_africa_priority_member_force_nubia, decision_012_africa_priority_member_force_nubia.dds | GFX_decision_012_africa_priority_member_post_settlement_nubia, decision_012_africa_priority_member_post_settlement_nubia.dds |
| luba | GFX_decision_012_africa_priority_member_mechanic_luba, decision_012_africa_priority_member_mechanic_luba.dds | GFX_decision_012_africa_priority_member_force_luba, decision_012_africa_priority_member_force_luba.dds | GFX_decision_012_africa_priority_member_post_settlement_luba, decision_012_africa_priority_member_post_settlement_luba.dds |
| lunda | GFX_decision_012_africa_priority_member_mechanic_lunda, decision_012_africa_priority_member_mechanic_lunda.dds | GFX_decision_012_africa_priority_member_force_lunda, decision_012_africa_priority_member_force_lunda.dds | GFX_decision_012_africa_priority_member_post_settlement_lunda, decision_012_africa_priority_member_post_settlement_lunda.dds |
| great_zimbabwe | GFX_decision_012_africa_priority_member_mechanic_great_zimbabwe, decision_012_africa_priority_member_mechanic_great_zimbabwe.dds | GFX_decision_012_africa_priority_member_force_great_zimbabwe, decision_012_africa_priority_member_force_great_zimbabwe.dds | GFX_decision_012_africa_priority_member_post_settlement_great_zimbabwe, decision_012_africa_priority_member_post_settlement_great_zimbabwe.dds |
| merina | GFX_decision_012_africa_priority_member_mechanic_merina, decision_012_africa_priority_member_mechanic_merina.dds | GFX_decision_012_africa_priority_member_force_merina, decision_012_africa_priority_member_force_merina.dds | GFX_decision_012_africa_priority_member_post_settlement_merina, decision_012_africa_priority_member_post_settlement_merina.dds |
| zulu | GFX_decision_012_africa_priority_member_mechanic_zulu, decision_012_africa_priority_member_mechanic_zulu.dds | GFX_decision_012_africa_priority_member_force_zulu, decision_012_africa_priority_member_force_zulu.dds | GFX_decision_012_africa_priority_member_post_settlement_zulu, decision_012_africa_priority_member_post_settlement_zulu.dds |

### Event report assets

| Sprite identifier | Final filename |
|---|---|
| GFX_report_event_012_africa_priority_member_political_settlement | report_event_012_africa_priority_member_political_settlement.dds |
| GFX_report_event_012_africa_priority_member_league_bargain | report_event_012_africa_priority_member_league_bargain.dds |
| GFX_report_event_012_africa_priority_member_overlap_settlement | report_event_012_africa_priority_member_overlap_settlement.dds |
| GFX_report_event_012_africa_priority_member_departure | report_event_012_africa_priority_member_departure.dds |

The expanded registration now covers the package focus and idea icons in addition to these 60 decision and report references. National flags, ideology variants, and leader or council portraits are separate unresolved rows in the Event 012 asset tranche.

## Validation evidence

Matrix coverage audit:

- 16 priority rows inspected
- 16 package ID triggers
- 16 origin triggers
- 16 distinct-mechanic decisions
- 16 force decisions
- 16 post-settlement decisions
- 64 conditional event descriptions
- 16 package-specific mechanic, force, post-settlement, and overlap proof families
- result: 16 passed, 0 failed

Decision and event inventory:

- 55 decisions total
- 54 selectable actions with cost, completion effect, and AI behavior
- 1 activated timed mission
- 16 mechanic, 16 force, and 16 post-settlement decisions
- 4 triggered-only country events
- 14 event options with 14 AI chance blocks
- 56 unique custom decision or category GFX references
- 4 unique custom report-picture references

Focus and lifecycle inventory:

- 1 dynamically loaded priority-member focus tree
- 8 non-linear focus nodes with package-aware text, rewards, and AI weighting
- 16 distinct starting-problem ideas
- 3 mutually exclusive political-settlement ideas
- 16 distinct mature-compact ideas
- 9 scripted-localisation selectors with 16 package branches apiece
- 103 unique gameplay sprite references registered without generic fallbacks
- 8 additional focus-shine sprite registrations

Starting-force inventory:

- 16 direct-English template names
- 16 primary formation names and 16 reserve formation names
- 5 matrix-derived template structures: royal, river, mobile-frontier, highland-engineer, and coastal-island guards
- 3 package experience bands and 3 local-support equipment/manpower bands
- 1 guaranteed identity-bearing primary formation per full package
- at most 1 compact reserve, created only while the carrier remains below the two-division floor
- no fixed province, foreign territory, enemy-state spawn, heavy-industry grant, or second readiness store

Country-identity inventory:

- 16 package-specific cosmetic identities
- 16 direct base names, definitions, and adjectives
- 16 complete democratic, communist, fascist, and non-aligned name families
- 240 localisation keys with no administrative placeholder names
- original tags, country histories, governments, territory, and cores preserved beneath each cosmetic identity

Reference integrity:

- 83 priority-member script constants defined
- 83 referenced
- 0 missing
- 0 unused
- all 94 Africa-prefixed callable references resolve to scripted trigger or effect definitions
- 264 expected localisation keys
- 264 present
- 0 missing
- 0 duplicate

Static path checks confirmed:

- Action 102 result without a valid origin cannot register
- valid origin without an Action 102 result cannot register
- registration changes neither territory nor relationship state
- an outside accepting country becomes Protected before later accession
- constitutional acceptance is explicit and revocable
- overlap options contain no annexation or automatic core grants
- withdrawal is timed and preserves the country's playable package
- no recurring world scan, opinion-based promotion, forced-diaspora effect, or all-country on-action was introduced
- starting formations require owned, controlled territory and retry only through the existing bounded reinforcement path

The HOI4 focus inspector accepted the authored tree and resolved all eight focus titles, descriptions, and registered icon IDs. Deterministic rendering was attempted, but the MCP artifact store returned ARTIFACT_STORAGE_LIMIT before it could write the render outputs. Local focus topology, prerequisites, load references, scripted payloads, icon registration, and localisation checks therefore remain the visual-review evidence for this tranche.

The HOI4 event-inspection MCP could not complete because its artifact store returned ARTIFACT_STORAGE_LIMIT. Local event namespace, ID, description, option, trigger, reference, and localisation audits were completed instead. This tooling limit is not evidence that the missing custom GFX assets exist.

## Simplifications, omissions, and blockers

Owned gameplay overlay:

- no priority row was merged, rejected, or queued
- no generic relationship store or duplicate Charter state machine was introduced
- no logic fallback is present

Whole package layer remains incomplete until the parent integrates:

- final specialist confirmation of the accepted compact carrier territories; the current survey never expands them
- leader or council characters and portraits
- national flags for `AFRICA_PRIORITY_<PACKAGE>` at the base, medium, and small flag sizes, plus all 103 custom priority-member DDS assets in this handoff
- asset manifests; the sprite definitions and final paths are registered, but the DDS files are not yet produced
- parent victory or peace callsites for africa_priority_member_record_rival_bloc_victory
- authorised post-registration player-switch callsites for africa_achievement_register_valid_priority_player
- parent terminal cleanup callsite after achievement and ending evaluation
- final country-package, localisation, decision/mission, and asset audits

## Future extension suggestions

After the missing core package dependencies are implemented:

1. Let package force-readiness alter shared defence actions, not create duplicate military systems.
2. Use the package overlap-mode flags in regional congress and peace-resolution content.
3. Add bounded pair interactions for Luba and Lunda, and for Kongo basin or Nile settlements, only after both participating identities are valid.
4. Let post-settlement mature flags unlock one durable regional contribution rather than an unbounded equipment loop.
5. Route every asset request through the Event 012 asset workflow and retain the stable GFX names above.

## Git

The original bounded overlay was delivered without a subagent commit. Parent integration records each accepted tranche in the repository history.
