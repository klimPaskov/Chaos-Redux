# Event 015 Country Identity and Achievement Implementation Handoff

## Scope and source review

This handoff covers the bounded Event 015 country package: institutional characters and advisors, staged parties and institutions, five cosmetic identities, second-generation succession, and the fourteen accepted achievements with durable evidence APIs. It does not edit Event 015's central lifecycle, focus tree, decisions, events, localisation, interface definitions, generated art, or asset manifests.

The implementation was checked against the required offline wiki pages, installed-game character/effect/trigger documentation, vanilla cosmetic-tag and dynamic-character precedents, the complete accepted Event 015 specification package, and current Event 015 gameplay identifiers. Vanilla confirms that the shared `leader_traits` pool is valid for both advisor and country-leader roles; it uses traits such as `captain_of_industry` and `silent_workhorse` on country leaders itself.

## Files changed

- `common/characters/015_utopia_manifesto_characters.txt` — eight institutional leaders/successors and sixteen recruitable political-advisor offices.
- `common/countries/cosmetic.txt` — five stable cosmetic-tag registrations and route colors.
- `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` — idempotent identity initialization, staged institution/party commitment, formation identities, succession, achievement proof recorders, and permanent disqualifier recorders.
- `common/achievements/chaos_redux_achievements.txt` — all fourteen accepted achievement IDs in the single root registry.

No files were staged or committed. The parent agent requested responsibility for final cross-wiring review and scoped commits.

## Stable identity contract

| Route | Cosmetic tag | Ruling organization | Formation leader | Successor |
| --- | --- | --- | --- | --- |
| Consent of Households | `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH` | Household Cooperative Coalition | `utopia_manifesto_household_assembly` | `utopia_manifesto_commonwealth_council` |
| Common Table | `UTOPIA_MANIFESTO_COUNCIL_UNION` | Congress of Common Tables | `utopia_manifesto_council_of_callings` | `utopia_manifesto_rotating_congress` |
| Guardians of Measure | `UTOPIA_MANIFESTO_PLANNED_UTOPIA` | Planning Movement | `utopia_manifesto_board_of_measure` | `utopia_manifesto_college_of_measure` |
| Closed Island | `UTOPIA_MANIFESTO_CLOSED_ISLAND` | Service and Unity Movement | `utopia_manifesto_stewardship_council` | `utopia_manifesto_directorate_of_service` |
| Joke Understood | `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH` | Humanist Reform Coalition | existing recipient leader retained | constitutional election transition |

The hidden humanist identity deliberately preserves the recipient's ideology group and leader. The other four identities install bounded institutional governing bodies only after formation. No route changes the recipient's base tag.

Public country-scope effects:

- `utopia_manifesto_initialize_identity_package`
- `utopia_manifesto_commit_current_route_identity`
- `utopia_manifesto_form_current_route_identity`
- `utopia_manifesto_advance_current_route_succession`

Initialization is idempotent so a route correction cannot erase achievement evidence or permanent disqualifiers. Formation calls the central `utopia_manifesto_complete_formation`, requires its proof flag, is idempotent, and changes only politics, leader presentation, cosmetic identity, and the final route institution idea. It contains no annexation, state transfer, core, unit, equipment, manpower, reserve refill, or cost-refund effect.

## Required direct character recruitment

The `chaos-redux-events` contract forbids hiding `recruit_character` inside a scripted effect. Add the following direct effects to the accepting option of `chaosx.nr15.1`, after `utopia_manifesto_accept_manifesto = yes` has set `utopia_manifesto_accepted`, and before any route can be selected:

```txt
recruit_character = utopia_manifesto_household_assembly
recruit_character = utopia_manifesto_commonwealth_council
recruit_character = utopia_manifesto_council_of_callings
recruit_character = utopia_manifesto_rotating_congress
recruit_character = utopia_manifesto_board_of_measure
recruit_character = utopia_manifesto_college_of_measure
recruit_character = utopia_manifesto_stewardship_council
recruit_character = utopia_manifesto_directorate_of_service
recruit_character = utopia_manifesto_interpreter
recruit_character = utopia_manifesto_general_provisioner
recruit_character = utopia_manifesto_secretary_of_callings
recruit_character = utopia_manifesto_surveyor_of_shores
recruit_character = utopia_manifesto_civic_engineer
recruit_character = utopia_manifesto_keeper_of_stores
recruit_character = utopia_manifesto_league_envoy
recruit_character = utopia_manifesto_advocate_of_limits
recruit_character = utopia_manifesto_public_auditor
recruit_character = utopia_manifesto_constitutional_jurist
recruit_character = utopia_manifesto_council_organizer
recruit_character = utopia_manifesto_social_workshop_planner
recruit_character = utopia_manifesto_chief_surveyor
recruit_character = utopia_manifesto_standards_engineer
recruit_character = utopia_manifesto_steward_of_service
recruit_character = utopia_manifesto_contract_broker
utopia_manifesto_initialize_identity_package = yes
```

Recruiting the institutional characters does not replace the existing leader. Leader roles are attached only by formation or succession.

## Required lifecycle wiring

1. After every successful route setter, call `utopia_manifesto_commit_current_route_identity = yes`. This applies to the five initial route focuses and all five constitutional-crisis correction focuses. Place it immediately after `utopia_manifesto_set_*_route = yes`, so the institution flag, party name, and route founding idea agree with the final route.
2. The actual formation action must call `utopia_manifesto_form_current_route_identity = yes`, not call `utopia_manifesto_complete_formation` separately. The wrapper delegates to that central helper and performs the identity only when proof succeeds.
3. In `utopia_manifesto_the_second_generation`, call `utopia_manifesto_advance_current_route_succession = yes` immediately after setting `utopia_manifesto_second_generation`.
4. Do not call the initialization effect on a route swap. Its idempotence is a safety net, not a substitute for correct lifecycle ordering.

## Achievement registry and evidence API

All accepted IDs are registered exactly once:

- `utopia_manifesto_no_place_but_home`
- `utopia_manifesto_need_not_greed`
- `utopia_manifesto_every_calling_chosen`
- `utopia_manifesto_two_year_table`
- `utopia_manifesto_archipelago_of_small_places`
- `utopia_manifesto_inland_island` (hidden)
- `utopia_manifesto_gold_for_common_use`
- `utopia_manifesto_the_joke_understood` (hidden)
- `utopia_manifesto_consent_of_the_governed`
- `utopia_manifesto_the_perfect_measure`
- `utopia_manifesto_closed_circle` (hidden)
- `utopia_manifesto_no_foreign_hands`
- `utopia_manifesto_the_stores_remain` (hidden)
- `utopia_manifesto_no_one_in_chains`

The final triggers recheck live route, identity, Ledger, reserve, institution, independence, and conduct state. Historical requirements use durable evidence rather than inferring past conduct from a present-day trigger.

### Required proof call sites

| Evidence effect | Required call point |
| --- | --- |
| `utopia_manifesto_record_achievement_peaceful_case_resolution` | At the start of `utopia_manifesto_record_external_case_completion`, before the active case is cleared; also in the domestic-substitution event before `utopia_manifesto_renounce_active_need_case`. The helper stores distinct target IDs. |
| `utopia_manifesto_record_achievement_obsolete_case_renunciation` | Immediately after setting `utopia_manifesto_case_renounced_when_need_ended`, before clearing the active case. That source flag still needs a concrete obsolete-case choice. |
| `utopia_manifesto_record_achievement_callings_sustained` | Only at successful completion of the long-duration Choice/Concord/Plenty calling challenge, after its duration has elapsed. |
| `utopia_manifesto_record_achievement_reserve_challenge_survived` | Only after the completed two-year reserve survives the major-war, blockade, or equivalent severe-supply challenge; ordinary reserve construction alone must not call it. |
| `utopia_manifesto_refresh_achievement_league_proofs` | After membership, shared-reserve, shared-defense, or independence proof counters change. |
| `utopia_manifesto_record_achievement_inland_supply_challenge_survived` | After the Inland Island capital-supply challenge survives a major war. |
| `utopia_manifesto_record_achievement_common_use_financed_provision` | After anti-luxury/common-use proceeds actually pay for emergency imports or public provision. |
| `utopia_manifesto_record_achievement_status_vote` | In `utopia_manifesto_return_stewardship`, after `utopia_manifesto_partner_autonomy_retained` is set and before case target/runtime cleanup. |
| `utopia_manifesto_refresh_achievement_planned_district_proof` | After any of the six country-level district-role proof flags changes. |
| `utopia_manifesto_record_achievement_closed_major_war_survived` | At the verified end of the Closed Island major-war defense challenge. |
| `utopia_manifesto_record_achievement_stronger_attacker_defeated` | At verified defensive-war victory after a start-of-war major/faction strength snapshot proved the attacker stronger. |
| `utopia_manifesto_record_achievement_crisis_recovery` | After a constitutional correction has restored stable Ledger values and again after final formation, so it can record only a complete recovery. |

### Permanent disqualifier call sites

- `utopia_manifesto_record_achievement_offensive_war` when the actor starts an offensive war after acceptance.
- `utopia_manifesto_record_achievement_unrelated_case_annexation` when case settlement annexes land outside the recorded case.
- `utopia_manifesto_record_achievement_assignment_overreach` when a non-emergency assignment quota exceeds the permitted limit.
- `utopia_manifesto_record_achievement_reserve_reset` when a player-facing reset/restart could bypass the reserve challenge.
- `utopia_manifesto_record_achievement_league_member_annexation` when the founder annexes a league member.
- `utopia_manifesto_record_achievement_early_coast_acquisition` whenever ownership changes could give an originally inland actor a coast before variant selection.
- `utopia_manifesto_record_achievement_island_reopened` when the Closed Island project is reopened.
- `utopia_manifesto_record_achievement_regime_collapse` when the Closed Island regime actually collapses.
- `utopia_manifesto_record_achievement_auxiliaries_hired` when any auxiliary contract is accepted, even if it is later demobilized.
- `utopia_manifesto_record_achievement_forced_relocation` when households are forcibly relocated.
- `utopia_manifesto_record_achievement_total_repeal` when crisis resolution abandons all public-provision institutions.

Existing event choices already set several accepted disqualifiers directly (`coercive_case`, `auxiliary_abuse`, `colonial_repression`, `forced_households`, `league_coercion`, and `stale_claim`). Those direct flags agree with the achievement triggers and must remain permanent.

Do not implement any of these checks with a daily, weekly, or monthly all-country iteration. War and ownership evidence should use narrowly scoped lifecycle/on-action hooks or the existing actor-scoped system.

## Localisation keys required

Character/advisor names use their exact tokens as localisation keys (all twenty-four `utopia_manifesto_*` character IDs listed in the recruitment block).

Party keys:

- `utopia_manifesto_household_cooperative_party` and `_long`
- `utopia_manifesto_congress_of_common_tables_party` and `_long`
- `utopia_manifesto_planning_movement_party` and `_long`
- `utopia_manifesto_service_and_unity_movement_party` and `_long`
- `utopia_manifesto_humanist_reform_coalition_party` and `_long`

Each cosmetic tag needs its generic country-name triplet (`TAG`, `TAG_DEF`, `TAG_ADJ`) and any ideology-specific variants selected by the final localisation design.

Each achievement needs `<achievement_id>_NAME`, `<achievement_id>_DESC`, and the exact tooltip key used in the registry: `achievement_<achievement_id>_tooltip`.

## Art dependencies still pending

The character file intentionally references stable portrait sprites that are not yet defined locally:

- `GFX_portrait_utopia_manifesto_household_assembly`
- `GFX_portrait_utopia_manifesto_council_of_callings`
- `GFX_portrait_utopia_manifesto_board_of_measure`
- `GFX_portrait_utopia_manifesto_stewardship_council`

Successors reuse the matching route portrait. The hidden humanist route retains the recipient portrait.

Required cosmetic flag triplets, all TGA at base/medium/small sizes:

- `gfx/flags/UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH.tga`
- `gfx/flags/UTOPIA_MANIFESTO_COUNCIL_UNION.tga`
- `gfx/flags/UTOPIA_MANIFESTO_PLANNED_UTOPIA.tga`
- `gfx/flags/UTOPIA_MANIFESTO_CLOSED_ISLAND.tga`
- `gfx/flags/UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH.tga`

Each needs matching files under `gfx/flags/medium/` and `gfx/flags/small/`.

Stable league-emblem sprite IDs supplied to the asset producer:

- `GFX_utopia_manifesto_household_congress_emblem`
- `GFX_utopia_manifesto_congress_of_common_tables_emblem`
- `GFX_utopia_manifesto_network_directorate_emblem`
- `GFX_utopia_manifesto_island_hierarchy_emblem`
- `GFX_utopia_manifesto_plural_compact_emblem`

All fourteen achievement DDS triplets remain required under `gfx/achievements/`, using each exact achievement ID as the filename stem with completed, `_grey`, and `_not_eligible` variants.

## Validation and unresolved integration risks

- Structural audit: all four touched Clausewitz files have balanced braces; the Event 015 registry contains exactly fourteen unique achievement IDs; every referenced identity character and cosmetic tag resolves to a definition.
- Semantic audit: all five routes have one distinct party/institution/cosmetic identity; four have an institutional leader and successor; the humanist route preserves the recipient leader and gains constitutional elections.
- Formation-effect audit: no annexation, owner transfer, core, unit, equipment, manpower, reserve refill, or refund effect occurs in the identity package.
- Vanilla precedent audit: `set_cosmetic_tag`, partial `set_politics`, dynamic `add_country_leader_role`/`remove_country_leader_role`, and the selected leader/advisor traits all have installed-game precedents.

Outstanding before completion:

1. The lifecycle and evidence calls above are not yet wired because their owner files are outside this subtask.
2. `utopia_manifesto_data_scandal` and `utopia_manifesto_assignment_revolt` are referenced by the existing Guardians formation trigger and the Perfect Measure achievement, but no current Event 015 effect sets either flag. Their actual incident/failure sources must be implemented or the promised disqualifiers are inert.
3. The stronger-attacker, major-war, blockade/supply, and offensive-war achievements require start/end snapshots from narrow war hooks; present-state war checks are not sufficient proof.
4. Portrait sprites, cosmetic flag triplets, league emblems, achievement icons, and all listed localisation remain external dependencies.

No fallback or silent simplification was introduced in this package. It must not be presented as fully integrated until the outstanding lifecycle, art, localisation, and audit work is complete.
