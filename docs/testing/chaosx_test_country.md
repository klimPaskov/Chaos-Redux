# Chaos Redux Test Country

## National policy laws

The package-owned carrier is the modifier-free hidden idea `national_policy_cxt_extension`; its idempotent setup effect is `national_policy_cxt_extension_apply`. The package registration token is registered by the bounded startup hook and the CXT-only fallback. The fallback may mark registration pending but does not grant laws. Initial CXT setup or a player-triggered package action consumes the registration and applies the fixture; unrestricted warfare is a separate explicit fixture action. See [National policies](../systems/national_policies.md) for the package's authority and [the current implementation report](../plans/famine_and_migration_system_plans/national_policy_panels_implementation.md) for source handoffs and outstanding evidence.

## Purpose

The Chaos Redux Test Directorate is a landless dormant country tag that becomes a complete runtime test harness when invoked from the console.

Its tag is `CXT`, and the console entry point is:

```text
e chaosx_test
```

A literal two-word engine command such as `chaosx test` cannot be registered through release Clausewitz script, so the shortest supported one-line command uses the built-in `effect` alias `e`.

## Transition behavior

The effect records the current country and its capital, then transfers ownership and control of that capital state to activate the dormant CXT tag.
It resolves the CXT country scope through a runtime meta effect after this transfer, sets the recorded capital, queues the hidden triggered-only receiver event `chaosx_test_country.1`, and switches the human player to CXT as the final effect in that country block.
The receiver is queued before the player switch with a one-hour delay, configured by the file-scoped `@CXT_SETUP_DELAY_HOURS`, so it is scheduled while the current scope is still a valid CXT country and runs after the player transfer.
The receiver runs with `ROOT = CXT`, annexes any remaining states of the former country, restores the recorded capital, and invokes the ordinary initialization or refresh helpers only when CXT owns and controls a valid capital.
This country ROOT also supplies the intended target for facility transfers, occupation fixtures, package extensions, and camp registration.
For a one-state origin, the initial capital transfer supplies all of its land and the receiver skips an empty annex.

The annex deliberately uses `transfer_troops = no`, which prevents vanilla divisions from entering the test roster.

After the annex, the harness takes control of one populated non-capital foreign state without annexing it so occupation, coercive-security, protected-administration, and occupied-population test surfaces have a valid target.

If CXT is already initialized, the console effect does not grant additional content. The player uses the debug decision category for replenishment, research, registered packages, or another deployment.

## Unit inventory

The roster covers every installed Chaos Redux land sub-unit: 55 combat battalions and 24 support companies.
Initial setup fields one full division per unit type and retains the distinct package formations, for 199 templates in total: 79 individual showcases, 24 core CXT formations, six Event 014/016/039 formations, and 90 source-package fixtures.
The complete custom-unit source inventory has 112 distinct regiment/support grid compositions, and every one has an exact CXT counterpart.
Parameterized runtime formations are represented by their distinct resolved unit compositions rather than duplicate names for the same grid.
The source-package definitions and registrations live in [chaosx_test_country_package_formation_effects.txt](../../common/scripted_effects/chaosx_test_country_package_formation_effects.txt).

Each combat showcase contains four identical battalions, so its model and counter are visible instead of being hidden by a higher-priority battalion in a mixed formation.
Each support showcase has a compatible combat anchor and exactly one tested support company.
The nine CBRN regimental companies occupy `regimental_support`; armored delivery uses an armor-group robot anchor.
The three HQ sections use an `is_army_hq` template with the native `hq_infantry` anchor, whose installed definition requires Thunder at Our Gates.
The seven Livens companies have separate templates because their `cbrn_offensive_delivery` exclusion prevents stacking them together.
All support-only roles retain their ordinary attached-company presentation; no standalone support division is created.

### Full land-unit list and previous coverage

The before-state is the source captured for this request on 11 October 2026, before the roster edits.
It registered 72 of 79 IDs, put 69 in templates, and used compatible template placement for 60.
Seven Livens definitions were unregistered, three HQ-only definitions had no HQ formation, and nine regimental companies were placed in divisional support slots.
The other families were present, often inside mixed formations that could not display every combat type separately.

| Family | Complete unit IDs | Before-state |
| --- | --- | --- |
| Zombies | `zombies`, `infected_zombies`, `rabid_zombies`, `parasitic_zombies`, `mutant_zombies`, `undead_zombies`, `necrotic_zombies`, `demonic_zombies`, `wendigo_zombies`, `armored_undead_zombies`, `armored_necrotic_zombies`, `armored_demonic_zombies` | Present; individual combat showcases added. |
| Cannibals | `cannibal_scavenger_warband`, `cannibal_feast_guard`, `cannibal_feast_cohort`, `cannibal_bone_guard`, `cannibal_bone_riders`, `cannibal_island_reavers`, `cannibal_siege_eaters`, `cannibal_march_predation_column`, `cannibal_network_cadre` | Present; individual combat showcases added. |
| Africa | `gorilla_heavy_infantry`, `stone_cohorts`, `riverborn`, `forest_giants`, `plague_carriers`, `pan_sappers`, `oracle_recon`, `disaster_wardens`, `chaosx_elephant` | Present; individual combat showcases added. |
| Plague rats | `rat_swarm`, `rat_brutes`, `rat_burrowers`, `rat_carrion_guard`, `rat_dock_stowaways`, `rat_tunnelers` | Present; individual combat showcases added. |
| Clones | `clone_infantry`, `aryan_clone_infantry` | Present; individual combat showcases added. |
| Robots | `autonomous_robot` | Present; individual combat showcases added. |
| Portal raiders | `portal_raider` | Present; individual combat showcases added. |
| Temporal guards | `temporal_guard` | Present; individual combat showcases added. |
| Xenobiological organisms | `xenobiological_assault_organism` | Present; individual combat showcases added. |
| Paleogenetic creatures | `paleogenetic_creature` | Present; individual combat showcases added. |
| Cave broods | `cave_monster_brood`, `cave_stone_phalanx_brood`, `cave_burrow_war_brood`, `cave_scree_tide_brood`, `cave_anchor_guard_brood` | Present; individual combat showcases added. |
| Alien infantry | `alien_infantry` | Present; individual combat showcases added. |
| Assassins | `assassin_cadre`, `shadow_company`, `silent_guard`, `master_assassin`, `mechanized_assassin`, `saboteur_cell` | Present; individual combat showcases added. |
| Death ghost hosts | `death_weak_ghost_host`, `death_hollow_ghost_host`, `death_last_shore_ghost_host` | Present; individual combat showcases added. |
| Chaos assault battalion | `chaos_battalion` | Present; individual combat showcases added. |
| CBRN command and field support | `cbrn_hq_operations_section`, `cbrn_hq_protective_logistics_section`, `cbrn_hq_medical_countermeasure_directorate`, `cbrn_gas_mask_decon_detachment`, `cbrn_chemical_recon_detachment`, `cbrn_chemical_projector_battery`, `cbrn_chemical_ammunition_train`, `cbrn_light_armored_delivery_detachment`, `cbrn_medium_armored_delivery_detachment`, `cbrn_heavy_armored_delivery_detachment`, `cbrn_medical_countermeasure_detachment`, `cbrn_biosecurity_assault_detachment` | Three HQ formations absent; nine regimental companies in incompatible slots. |
| Livens support | `livens_projector_support`, `livens_projector_support_chlorine`, `livens_projector_support_phosgene`, `livens_projector_support_mustard`, `livens_projector_support_lewisite`, `livens_projector_support_sarin`, `livens_projector_support_soman` | All seven absent from the CXT registrations. |
| Coal golems | `coal_golem` | Present; individual combat showcases added. |

### Models, counters, naval and air inventory

The scan covers every custom `sub_units` definition, the custom-unit-containing history and scripted templates, and all 31 package directories under `gfx/models/units`.
Thirty directories have active mesh consumers; `012_africa_strange_forces` is a shared package directory without another standalone consumer.
Custom meshes resolve for 49 combat types and three attached support types.
Bone Riders, Network Cadre, Aryan clones, coal golems, and Wendigo zombies use their existing intended entities.
The elephant showcase exposes the `chaosx_elephant` subunit's visual binding; its unresolved `elephantry` entity and authorized custom-model replacement are tracked in [the elephant repair handoff](../plans/unit_fix_2026-10/models_1018_elephant_handoff.md).
Armored zombie types share their corresponding zombie models; the rat and cave variants share their family models; all have individual unit showcases and retain their existing counters.
`chaos_battalion` consumes the custom Chaos Assault Battalion model; the empty compatibility file of that name is not another unit definition.
No custom naval or air sub-unit/model consumer exists in the installed mod, including the Event 043 and Event 080 surfaces, so there is no custom fleet or air wing to add to this roster.
Existing equipment and event art are not treated as native ships or air wings.
No models, counters, textures, sound definitions, or ordinary unit stats are changed by this fixture.

### Family-to-province map

CXT starts landless: `history/countries/CXT - Chaos Redux Test Country.txt` assigns no states, and the console receiver inherits the invoking country's land.
Family sites therefore come from territory CXT actually owns and controls after activation, not from fixed foreign provinces.
The one central core-family order is `chaosx_test_country_assign_core_family_sites` in [the deployment effects](../../common/scripted_effects/chaosx_test_country_deployment_effects.txt).
It allocates the 18 families below before the first division is created, independently of package registration order.
Future package families absent from that list allocate through the same gateway without an event-list edit.
Each family's individual showcases, attached-support fixtures, and designed package formations reuse its stored province.

The allocator prefers an unused state, then an existing supply hub, then an owned railway province, then owned land that can receive an owned railway connection.
Numeric state and province IDs break ties deterministically.
The allocation policy and checked Paris/Berlin source anchors are centralized in [the deployment constants](../../common/script_constants/chaosx_test_country_deployment_constants.txt).
Other capitals choose the lowest controlled native capital-state hub, or their sole province when the capital state has only one province.
The existing pure state/province catalogue supplies membership; no duplicate map table is maintained here.
Creation runs inside the recorded state and passes the chosen province to native `prioritize_location` after ownership, control, passability and route checks.
Foreign-controlled provinces are excluded from the railway route; the fixture does not annex land for unit placement.

The table is the source-model result for ordinary 1936 French or German territory inherited by CXT, with the installed map and existing railways.
Each example gives 18 different owned states at existing connected hubs and needs no railway construction.
Actual runtime ownership or another origin changes the selected sites, while the family order and collision checks remain the same.

| Family | Real family token | France province (state) | Germany province (state) |
| --- | --- | --- | --- |
| Zombies | `chaosx_cxt_extension_zombies_showcases` | 3552 (14) | 11531 (42) |
| Cannibals | `chaosx_cxt_extension_event014_cannibalism` | 485 (15) | 9517 (50) |
| Africa | `chaosx_cxt_extension_event012_africa_gods` | 11506 (16) | 587 (51) |
| Plague rats | `chaosx_cxt_extension_rat_broods_showcases` | 9490 (18) | 692 (52) |
| Clones | `clone_infantry` | 9737 (19) | 9515 (53) |
| Robots | `autonomous_robot` | 6613 (20) | 11544 (54) |
| Portal raiders | `portal_raider` | 11834 (21) | 6488 (55) |
| Temporal guards | `temporal_guard` | 6960 (22) | 241 (56) |
| Xenobiological organisms | `xenobiological_assault_organism` | 6657 (23) | 495 (57) |
| Paleogenetic creatures | `paleogenetic_creature` | 512 (24) | 6389 (58) |
| Cave broods | `chaosx_cxt_extension_cave_broods_showcases` | 620 (25) | 3326 (59) |
| Alien infantry | `alien_infantry` | 3594 (26) | 3561 (60) |
| Assassins | `chaosx_cxt_extension_event039_assassin_forces` | 3652 (27) | 321 (61) |
| Death ghost hosts | `chaosx_cxt_extension_death_hosts_showcases` | 678 (28) | 6282 (63) |
| Chaos assault battalion | `chaos_battalion` | 11548 (29) | 3522 (64) |
| CBRN command and field support | `chaosx_cxt_extension_cbrn_unit_family_showcases` | 11465 (30) | 514 (65) |
| Livens support | `chaosx_cxt_extension_livens_projectors_showcases` | 6766 (31) | 9570 (66) |
| Coal golems | `chaosx_cxt_extension_coal_golems_showcases` | 9909 (735) | 11467 (67) |

The country keeps `chaosx_test_country_family_province_@var:<family>`, a separate typed family-state pointer, its numeric state ID, and a reserved-province array.
It revalidates a retained site before spawning; an invalid site releases its reservation and remains eligible for reallocation.
Repeated setup or package application keeps successful initial-spawn receipts, while **Deploy Test Formations** intentionally adds one more division per installed template at the same family sites.
The shared count is centralized in `chaosx_test_country_count.divisions_per_template` and is one.

Distinct sites require at least as many eligible owned land provinces as families.
Malta state 116 has only province 12003 and can host at most one distinct family site; the fixture neither overlaps other families there nor acquires another country's land.
Families without an eligible site remain in `chaosx_test_country_unplaced_families`, and the Test Directorate category displays the count and a source/placement explanation.
A multi-province capital without a resolvable native supply source, unavailable catalogue geometry, or insufficient owned route capacity can leave families waiting.
Railway connectivity is checked; actual supply throughput, conversion timing and later player movement are not claimed by the source model.

## Technology, projects, and doctrine

CXT history grants the installed technology inventory, initializes a complete zombie research profile, and completes its licensed special projects before console activation.
The history receipt prevents the activation receiver from repeating the core completion pass.
The technology helper captures `global.technology^num`, skips the reserved default database object at index zero, reads every real entry from index one below that count, and passes each database object to native `var:` technology fields with `popup = no`.
The installed engine registers that default object in the global array but initializes its validity flag to false, which both technology consumers reject.
An empty or default-only database produces no technology reads, and the numeric loop has its own initialized break variable.
The repair preserves dynamic coverage of every real technology; the read-only engine contract and validation limits are recorded in `runtime_repairs/20260913_cxt_technology_validation/`.
Technologies are synchronized again before runtime facility placement, so facility permissions exist before construction.

The static special-project inventory retains all 83 definitions: 49 installed vanilla projects and 34 Chaos Redux projects.
Vanilla calls mirror their installed DLC requirements, and the seven country-restricted American chemical and Japanese medical projects explicitly accept CXT alongside their original countries.
Core and registered project grants are idempotent and use `chaosx_test_country_silent_unlocks` to suppress completion reports while retaining their gameplay outputs.
Project condemnation gains remain in CXT's country record during dormant history setup; participant calculations and pulse scheduling wait until it has an owned capital.
Initialization and the existing registered-content bus flush the queued requests after activation, so scoring has valid capital and initialized-country scopes without repeating project completion.
The D’Rhondan craft silent path runs the same authorization helper as its report option; Black Plague completion keeps equipment, technology, condemnation, progress, and achievements.
The zombie fixture records existing research choices with strength 3, infectiousness 3, speed 2, durability 2, cure resistance 2, and obedience 2; its neurobiological, dead, expanded-resource profile uses ordinary refinement and skips field testing.
Ordinary-country project choices, reports, and balance remain unchanged.

HOI4 does not expose a documented global special-project database array. Future projects use the opt-in registry described below; the static baseline remains explicit so omissions are visible in code review and inventory audits.

Core and registered project callers pass an `sp:<project_id>` scope through the temporary variable `chaosx_test_country_current_special_project` and invoke `chaosx_test_country_complete_special_project = yes`.
That country-scoped helper skips completed projects and passes the object to native `complete_special_project` with `show_modifiers = no`; project completion executes the ordinary gameplay outputs and does not add a facility or scientist.
The caller must assign a valid installed project scope before each core call; the registered-project loop supplies its current scope directly.

Facility callers assign the temporary building token `chaosx_test_country_current_facility` before invoking `chaosx_test_country_provision_facility_type = yes`.
The country-scoped helper resolves that explicit token inside one supported `meta_effect` template and places native `can_construct_building` checks directly at all three placement gates with CXT as ROOT.
The shared state trigger checks ownership, control, coast, and separation from other facilities without another runtime expansion.
Naval facilities require coast; the six types use distinct states, rejected foreign acquisitions restore their original owner and controller, and exhausted searches set the existing missing-facility flags.
The temporary input is replaced by each subsequent type call; the rejection array is cleared before and after each search, and the helper grants no technology or project.

The country adopts the Chaos Warfare grand doctrine, assigns `extermination_columns`, `contaminant_firebases`, `chemical_suppression`, and `integrated_chemical_operations`, grants enough mastery to complete every active track, and closes the establishment mission successfully.

The Event 016 carrier also reconciles the Mengele Computation provider's availability and cleans any invalid provider receipt through the same private lifecycle helper.
The harness does not impersonate Mengele's active program, invent Theory or Prototype history from a completed technology, or pay a project twice; the ordinary technology fixture and the provider's paid four-stage progression are distinct test surfaces.

All shared CBRN capacities are raised to their maximum, the unrestricted Chaos Warfare use policy is selected, and protection, operations, disease-response, battlefield-operation, payload-logistics, occupation, civil-defence, and doctrine-owned camp surfaces are activated.

The test fixture records a confirmed chemical-attack history and a national respirator reserve so emergency and civil-defence categories remain visible without waiting for a live attack.

## Stockpile and resources

The initial stockpile receives the configured 1,000,000 units per concrete equipment type, including the vanilla dependencies used by Chaos Redux divisions.
The full 199-template roster requires 2,663,475 manpower; initial resource setup grants 3,000,000 through two 1,500,000 grants, keeping each fixed-point argument representable.
Its largest aggregate equipment demand is 53,567 infantry equipment, below the standard stockpile grant.
Six named CXT Livens variants have the required projectile module, matching stockpile calls, and forced showcase-equipment profiles; chlorine and the basic company use type 1, phosgene type 2, and mustard, lewisite, sarin and soman type 3.

Dedicated light, medium, and heavy chemical-carrier variants use the concrete `light_tank_flame_chassis_3`, `medium_tank_flame_chassis_3`, and `heavy_tank_flame_chassis_3` types in the No Step Back designer system.
Their named domestic variants are created before stockpile grants and unit creation, and stockpile calls identify both the concrete type and variant name.

CXT has no periodic equipment, unit, research, resource, or package grants. Initial setup grants the baseline once. Tag-scoped package daily hooks only register an unseen carrier and mark pending work; they never apply it.

The player-only **Test Directorate** decision category provides repeatable, zero-cost controls:

- **Refill National Resources** adds the configured political power, command power, experience, manpower, fuel, nuclear bombs, stability, and war support.
- **Refill Equipment Stockpile** runs the static and registered-equipment stockpile grants.
- **Complete Research and Projects** reruns the dynamic technology scan and core and registered special-project completion helpers.
- **Apply Registered Systems** consumes package carriers, registered projects, and newly registered unit formations only when selected. It registers new equipment tokens, but stockpile quantities are granted by **Refill Equipment Stockpile**.
- **Deploy Test Formations** adds one more division of every installed static, individual-unit, and package-owned template at its family site without redefining existing templates.

These decisions use the installed vanilla `GFX_decision_category_generic_crisis` and `GFX_decision_generic_research` sprites; no new bitmap assets are required. The category is visible only to a human CXT with `chaosx_test_country_initialized`. The decision scripts are `common/decisions/categories/chaosx_test_country_debug_categories.txt` and `common/decisions/chaosx_test_country_debug_decisions.txt`, and their text is in `localisation/english/chaosx_test_country_l_english.yml`.

CXT receives 50 research slots even though all current technologies are completed during setup.

## Dynamic extension contract

Technology is the only surface here with a documented runtime database array. The technology helper scans every real `global.technology` entry only during initial setup or when **Complete Research and Projects** is selected. HOI4 does not expose equivalent global arrays for special projects, equipment, sub-unit definitions, facilities, doctrines, or general systems, so those remain additive package-owned registrations.

A package that adds one of those surfaces must register an idempotent setup effect and a modifier-free hidden-idea carrier. The carrier id matches the setup effect name before its `_apply` suffix. The package registers the carrier from a bounded existing-country `on_startup` scope and can repeat registration from an additive `on_daily_CXT` fallback. Daily registration sets `chaosx_test_country_registered_sync_pending` when new content appears; it never applies grants. Initial setup consumes all available carriers, and later content waits for **Apply Registered Systems**.

The anti-zombie cure payload package registers concrete `zombie_cure_bomb_1` through `chaosx_cxt_extension_zombie_cure_payload_apply` and its modifier-free carrier. Initial setup completes `sp:zombie_cure_bomb`, then the registered equipment stockpile pass grants the normal CXT fixture amount. When the carrier is discovered later, the player uses **Apply Registered Systems** to add the token and **Refill Equipment** to grant stock; repeated application only registers the same token once.

The setup effect may publish a special-project object, equipment token, frontline token, or support token through these helpers:

```text
set_temp_variable = { var = chaosx_test_country_registration_special_project value = sp:my_project }
chaosx_test_country_register_special_project = yes

set_temp_variable = { var = chaosx_test_country_registration_equipment value = token:my_equipment }
chaosx_test_country_register_equipment = yes

set_temp_variable = { var = chaosx_test_country_registration_frontline_subunit value = token:my_battalion }
chaosx_test_country_register_frontline_subunit = yes

set_temp_variable = { var = chaosx_test_country_registration_support_subunit value = token:my_support_company }
set_temp_variable = { var = chaosx_test_country_registration_support_anchor value = token:my_compatible_chaos_battalion }
chaosx_test_country_register_support_subunit = yes
```

The `sp:<id>` value is an installed special-project scope, not a custom token. The hidden idea is never applied to a country and needs no modifiers, localisation, or icon. It exists because ideas are a documented tokenizable database type; the dispatcher uses its token key to call the matching package `_apply` effect.

For frontline registrations the shared builder creates a four-battalion homogeneous recruitable showcase and one initial division.
For support registrations it uses an explicit registered combat anchor and the appropriate divisional, regimental, or HQ grid.
An anchor must be processed before the support builder runs.
The processed-unit arrays track coverage, while separate successful-dispatch arrays track initial showcase deployment; template existence never suppresses a still-missing initial spawn.
The player-triggered deployment pass bypasses initial-spawn receipts deliberately.
The registered project-completion and equipment-grant passes reset their private temporary break variables before each traversal, so a nonzero break value left by an earlier callback cannot truncate either pass.

Before registering related units, the package supplies a real family token:

```text
set_temp_variable = { var = chaosx_test_country_current_unit_family value = token:my_hidden_idea_carrier }
```

The carrier dispatcher resets that optional input between packages, so a future package that omits it uses the individual unit token instead of inheriting another package's family.
Frontline and support family arrays are appended exactly once beside their unit arrays; support anchors form a third aligned array.
Regimental and HQ-only supports also publish their token to the corresponding `global.chaosx_test_country_regimental_support_showcase_subunits` or `global.chaosx_test_country_army_hq_showcase_subunits` classification array.
Those classification arrays affect the test template region, not the ordinary sub-unit definition.

A package-owned formation defines `CXT Package - <real_token_key>` once and registers its real token plus its family:

```text
set_temp_variable = { var = chaosx_test_country_registration_package_formation value = token:my_formation_marker }
set_temp_variable = { var = chaosx_test_country_registration_package_family value = token:my_hidden_idea_carrier }
chaosx_test_country_register_package_formation = yes
```

`my_formation_marker` is a modifier-free hidden idea used only as a token key; it is not registered as another extension-effect carrier.
The source-package fixture has one actual carrier, `chaosx_cxt_extension_source_package_formations`, and 90 such template markers.
Its initial and manual passes use the same registry and paired family metadata.
The seven unit-family carriers are zombies, death hosts, cave broods, plague rats, coal golems, CBRN support, and Livens; Event 012, 014, 016 and 039 retain their existing package carriers for their own unit families.
The unit carrier declarations and bounded hooks are [unit extension ideas](../../common/ideas/chaosx_test_country_unit_extension_ideas.txt) and [unit extension on-actions](../../common/on_actions/chaosx_test_country_unit_extension_on_actions.txt).

For a reviewed registered package template, the country-scoped deployment gateway is:

```text
set_temp_variable = { var = chaosx_test_country_current_family value = token:my_hidden_idea_carrier }
set_temp_variable = { chaosx_test_country_family_spawn_succeeded = constant:chaosx_test_country_deployment.zero }
set_variable = { global.chaosx_test_country_spawn_template = token:cxt_template_package_formation }
set_variable = { global.chaosx_test_country_spawn_formation = token:my_formation_marker }
chaosx_test_country_spawn_family_template = yes
```

Custom scripted effects do not accept named parameter blocks or expand `$PARAMETER$` in HOI4.
The gateway is called with `= yes` and reads a real token selector from `global.chaosx_test_country_spawn_template`.
Fixed template selectors and equipment-profile selectors are modifier-free hidden idea markers in `common/ideas/chaosx_test_country_template_selector_ideas.txt`.
The native creation meta block obtains its literal template name from `GetChaosxTestCountryTemplateName`, defined in `common/scripted_localisation/chaosx_test_country_template_names.txt`.
For individual showcases, callers also publish `global.chaosx_test_country_spawn_subunit`; package callers publish `global.chaosx_test_country_spawn_formation`.
Their name strings use those payloads' `GetTokenKey` getters, not unresolved `[UNIT]` or `[FORMATION]` placeholders.
The exact names and forced variant blocks are in `localisation/english/chaosx_test_country_template_names_l_english.yml`, preserving English template identity in the native OOB string.
The caller initializes any output it needs before invoking the nested helper and does not scope temporary variables.
`chaosx_test_country_family_spawn_succeeded` indicates guarded native creation dispatch, not an observed engine result, because `create_unit` has no documented success return.
Only a successful dispatch consumes the initial-spawn receipt; an unavailable placement remains retryable through **Apply Registered Systems**.
Livens support callers also supply their current support token so the internal native creator forces the matching named equipment variant.
All other callers clear that selector, preventing a previous support profile from leaking into another formation.


A new land sub-unit also needs an explicit Event 19 disposition in the same owner change. A combat unit extends an existing Chaos unit-family provider or receives a complete owner-side provider registration; a support unit is documented as an inseparable provider attachment, a parent-owned support consumer, or a rejected standalone lot with the engine reason. The owner updates `docs/events/019_infantry_spawn/systems/unit_family_coverage.md` and `docs/systems/cbrn_warfare/chaos_unit_family_registry.md`.

Temporary `CXT_SETUP_TRACE` markers remain around the console receiver and setup stages while the earlier activation freeze remains unresolved in `runtime_repairs/20260913_cxt_technology_validation/freeze_repair.md`.

## Special facilities

CXT receives one naval, nuclear, air, land, biowarfare, and chemical-warfare facility.

HOI4 limits special-project facilities in the shared `special_project_facility` group to one per state.
Each type preserves an existing controlled campus or uses an owned, controlled, facility-empty state that passes the installed `can_construct_building` check for that exact building.
When no owned candidate is legal, the bounded allocator considers non-capital foreign candidates, transfers ownership and control, and revalidates construction.
Every special-project facility declares `need_supply`, so a borrowed foreign candidate must border territory CXT already controls, and the construction pass tries an owned, controlled state that is already supply-connected (the capital, a supply node or a railway, through `chaosx_test_country_state_is_supply_connected`) before any other owned state.
Native `can_construct_building` still decides every placement; the supply rule only narrows and orders the candidates.
Rejected candidates recover their original owner and controller and are excluded from further attempts for that type; the temporary rejection array is cleared after the search.
Naval candidates require a coast.
If the world has no legal candidate, the allocator terminates and records an explicit per-type missing-campus flag and aggregate provisioning-incomplete flag; it does not attempt illegal construction or substitute another facility.

Scripted completion of CXT's Anthrax, Plague, Tularemia, and Smallpox projects does not run their facility-state effects. After special facilities are provisioned and the initial stockpile is filled, CXT registers an arsenal only when exactly one owned, controlled, inhabited, eligible state has a positive biowarfare-facility level. The registration records that exact state as the scripted-project facility, refreshes risk, and starts the existing idempotent country monitor. Zero or multiple eligible campuses set `chaosx_test_country_bio_arsenal_registration_blocked` and leave the monitor unstarted; a prior designation or designation history is never replaced. This fixture uses existing CBRN facility and monitor assets and needs no new icon or sprite.

The `anomaly_signal_beacon_pilot` building is excluded because its definition is a non-buildable 3D asset pilot without a special-project specialization.

Facilities, doctrines, and general systems do not use the project, equipment, or sub-unit definition arrays. A future package exposes a package-owned idempotent `_apply` helper and registers its hidden-idea carrier through the extension bus. The helper checks a stable package flag or the relevant building/system state before applying direct effects such as `set_building_level`, doctrine completion, or system bootstrap.

## Camp systems

The shared genocide and camp-repression systems are initialized and activated for CXT.

The capital receives a concentration camp, an extermination camp converted from the second concentration level, and a gulag labor-camp network, leaving the concentration and extermination buildings active together.
The fixture assigns the capital's responsible-country pointer to CXT before registration, including when the transferred capital already contains a camp pointer belonging to the former country.

The managed camp ledger, genocide decisions, gulag decisions, extreme doctrine authority, monthly active-site registry, and ordinary-country camp variables are active.

CXT is intentionally not classified as a special Chaos country because that classification would invoke the camp scrub path.

## Country and flag assets

Country wiring is defined in:

- `common/country_tags/chaosx_test_country.txt`
- `events/chaosx_test_country.txt`
- `common/countries/Chaos Redux Test Country.txt`
- `history/countries/CXT - Chaos Redux Test Country.txt`
- `localisation/english/chaosx_test_country_l_english.yml`

The original flag package is stored under `docs/assets/country_flags/cxt_test_country/`.

Runtime flags are installed as `gfx/flags/CXT.tga`, `gfx/flags/medium/CXT.tga`, and `gfx/flags/small/CXT.tga`.

The debug category uses the installed vanilla `GFX_decision_category_generic_crisis` sprite, and its five decisions use `GFX_decision_generic_research`. Both sprites are defined in the game's `interface/decisions.gfx`; CXT adds no bitmap or mod `.gfx` file. Modifier-free hidden ideas remain token carriers with no visible icon.

## Maintenance

When Chaos Redux adds a technology definition, no CXT inventory edit is required because the runtime technology array is scanned during setup and the manual research decision. Every package that adds a special project, concrete equipment type, land sub-unit, special facility, doctrine, or general system must add its hidden-idea carrier, idempotent `_apply` setup effect, startup registration, and tag-specific registration-only daily fallback in the same change. A new land sub-unit must also complete the Event 19 disposition and provider obligations described above. The explicit project/equipment inventory and 79-sub-unit source inventory are reviewable snapshots; package registrations extend them additively when the player applies pending systems. A package with several related units keeps individually fielded showcases as well as its valid owner-authored formations and assigns both to one real family token.

The one-time initialization flag is `chaosx_test_country_initialized`.

Event 012 Gods uses the existing package-owned carrier `chaosx_cxt_extension_event012_africa_gods` and idempotent setup effect `chaosx_cxt_extension_event012_africa_gods_apply` in `common/scripted_effects/012_africa_gods_cxt_test_effects.txt`, registered through `common/on_actions/012_africa_gods_cxt_on_actions.txt`.
The setup retains `gods_of_africa_cxt_fixture_ready` and adds only the inert readiness flag `gods_of_africa_cxt_industry_fixture_ready` for the accepted industrial record contract and does not create damage, grant factories, acquire a Gods host, fire Event 012, move CPP, install repair service or erase active receipts.
This flag marks fixture readiness and is not native repair or timer proof.

Event 021's package-owned carrier is `chaosx_cxt_extension_event021_random_civil_war`, its idempotent setup effect is `chaosx_cxt_extension_event021_random_civil_war_apply`, and its inert readiness receipts are the global `random_civil_war_cxt_content_registered` flag plus the CXT-local `random_civil_war_cxt_extension_seen` flag. The carrier is registered from `common/on_actions/021_random_civil_war_cxt_on_actions.txt` and implemented in `common/scripted_effects/021_random_civil_war_cxt_test_effects.txt`; it registers the reusable framework without selecting a target, creating a front, firing Event 021, or spending country resources.

Event 035's package-owned carrier is `chaosx_cxt_extension_event035_great_depression`, its setup effect is `chaosx_cxt_extension_event035_great_depression_apply`, and its inert readiness proof is `great_depression_cxt_fixture_ready`. The carrier is registered from `common/on_actions/035_great_depression_cxt_on_actions.txt` and implemented in `common/scripted_effects/035_great_depression_cxt_effects.txt`; the fixture does not start a depression or modify an economy.

Event 028's package-owned carrier is `chaosx_cxt_extension_event028_asteroid_incoming`, its setup effect is `chaosx_cxt_extension_event028_asteroid_incoming_apply`, and its inert readiness flag is `asteroid_incoming_cxt_fixture_ready`. The carrier is registered from `common/on_actions/028_asteroid_incoming_cxt_on_actions.txt` and implemented in `common/scripted_effects/028_asteroid_incoming_cxt_effects.txt`.

Event 037's package-owned carrier is `chaosx_cxt_extension_event037_mysterious_people`, its idempotent setup effect is `chaosx_cxt_extension_event037_mysterious_people_apply`, and its receipt is the `mysterious_people_cxt_fixture_initialized` country flag. The carrier is registered from `common/on_actions/037_mysterious_population_on_actions.txt` and implemented in `common/scripted_effects/037_mysterious_population_cxt_effects.txt`. The fixture gives the capital one measured newcomer grant so the category, hotspot actions, pressure and the Newcomers modifier can be inspected, without firing Event 37, recording history or adding Chaos.

Event 029's package-owned carrier is `chaosx_cxt_extension_event029_riches_found` and its idempotent setup effect is `chaosx_cxt_extension_event029_riches_found_apply`.
The carrier is registered from `common/on_actions/029_riches_found_cxt_on_actions.txt` and implemented in `common/scripted_effects/029_riches_found_cxt_effects.txt`.
Initial setup or the player-triggered **Apply Registered Systems** action creates one valid capital-state mine fixture, marked by `riches_found_cxt_fixture_mine` and the country guard `riches_found_cxt_fixture_initialized`.
The fixture uses the bounded registry, regulated operation, public-development policy, state presentation, and current-controller aggregate.
It does not fire the discovery event or pay its 1,000 political power.
The daily CXT hook only registers unseen content and marks it pending for the player-triggered action.

Event 032's package-owned carrier is `chaosx_cxt_extension_event032_missiles`, its idempotent setup effect is `chaosx_cxt_extension_event032_missiles_apply`, and its inert readiness flag is `missiles_cxt_fixture_ready`. The carrier is registered from `common/on_actions/032_missiles_cxt_on_actions.txt` and implemented in `common/scripted_effects/032_missiles_cxt_effects.txt`; it initializes only the Event 032 launch-state ledgers without firing the event, granting missile technology, creating a site, or stocking a reserve.

Event 023's package-owned carrier is `sov_nuclear_bombs_cxt_extension_event023`, its idempotent setup effect is `sov_nuclear_bombs_cxt_extension_event023_apply`, and its registration receipt is `sov_nuclear_bombs_cxt_content_registered`. The carrier is modifier-free in `common/ideas/023_sov_nuclear_bombs_cxt_extension_ideas.txt`; bounded startup and `on_daily_CXT` registration live in `common/on_actions/023_sov_nuclear_bombs_cxt_on_actions.txt`, and the setup effect lives in `common/scripted_effects/023_sov_nuclear_bombs_cxt_test_effects.txt`. The fixture initializes only the neutral Event 023 ledger contract. It does not fire Event 023, grant the 100-device opening, grant nuclear technology, create reactors or storage sites, authorize a launch, or execute a physical device transaction.

Event 027's package-owned carrier is `chaosx_cxt_extension_event027_doctrine_research`, and its idempotent setup effect is `chaosx_cxt_extension_event027_doctrine_research_apply`. The carrier is registered from `common/on_actions/027_doctrine_research_cxt_on_actions.txt` and the setup dispatcher is implemented in `common/scripted_effects/027_doctrine_research_cxt_effects.txt`; it initializes the Event 027 adapter and ledger only for the CXT fixture and never creates a research batch.

Event 016's existing `chaosx_cxt_extension_event016_alien_infantry_apply` also reconciles only CXT's registered Portal beachheads and rebuilds only already-recorded physical Singularity sites.
Invalid pending construction receipts remain with the native callback or project cleanup; this CXT pass does not fabricate sites.
Its Singularity pass also rebuilds existing private Directorate site rows through their own ledger and does not grant a command node, power link, project stage, or terminal request.
The same carrier grants the six conventional Weaponization packages through the provenance-free core only when their durable receipt is missing and then reconciles their existing modifiers.
This exposes the ordinary Wonder-Technology Operations category without assigning Kruger, creating a native project ledger, fabricating event-source history, or executing a paid directive.
The shared computation-slot marker keeps repeated extension synchronization idempotent.
It does not select a biological agent, create a breach, start a raid, produce a payload, authorize a release, or clear a pending biological operation.
The existing package carrier and startup/tag-specific registration hooks own this coverage; no additional global tick is introduced.

`chaosx_test_country_event016_mengele_provider_fixture_decision` is a separate player-triggered CXT setup for exercising the real Mengele provider decision category.
It calls `chaosx_cxt_event016_enable_mengele_provider_fixture` in `common/scripted_effects/016_alien_infantry_cxt_test_effects.txt`; it adds no carrier or on-action hook.
It sets the existing Mengele scenario-country marker and test-state idea, opens the existing provider registry, initializes the private receipt arrays, and reconciles project availability only when CXT is selected and initialized.
The fixture writes no Theory, Prototype, Deployment, Weaponization, component, or native-project completion receipts and spends no project resources.
The test-country setup is a test-only provider path; it does not create a Kruger host identity or change any model or model asset.
Enable this fixture before using the broad “Complete Research and Projects” debug decision when checking native clocks, callbacks, or provider decision costs.
That broad completion shortcut bypasses native project clocks and payments, so its resulting project inventory is observation data rather than native transaction evidence.
After fixture activation, use the existing provider decisions and real special-project UI in separate Gotterdammerung-present and Gotterdammerung-absent sessions.
The CXT scenario does not certify the exact Rocketry alternative callback, Electronics technology callback, provider timer race, six-agent raid transactions, DHR five-receipt matrix, six-component de-duplication, or Fallout retry; those remain separate acceptance cases.

### Event 016 native inventory probe

`chaosx_cxt_event016_probe_native_inventory` is a separate, explicit country-scope console effect for an initialized CXT, invoked as `e chaosx_cxt_event016_probe_native_inventory` while CXT is selected.
It has no parameters or gameplay outputs and is never called by the normal package carrier.
Each invocation clears and rebuilds three CXT-only observation arrays: `chaosx_cxt_event016_observed_native_families` contains the thirteen directly mapped native families plus Biological Weapons only when all six agent projects are completed and Singularity only when all six component projects are completed; `chaosx_cxt_event016_observed_biological_agents` contains the six project-backed agent IDs; and `chaosx_cxt_event016_observed_singularity_components` contains the six project-backed component IDs.
The values are the existing `brilliant_scientist_project_family`, `brilliant_scientist_biological_agent`, and `brilliant_scientist_singularity_component` constants, and the three arrays are observations rather than provider receipts or registration inputs.
The probe also refreshes `chaosx_cxt_event016_probe_dlc_available` for Gotterdammerung and `chaosx_cxt_event016_probe_provider_gate_closed` when no Kruger current-host flag or Mengele provider receipt initializer exists and the Mengele provider gate is false.
For a country other than initialized CXT, the effect has no side effects; repeated invocation is idempotent.

This probe verifies installed native project inventory and the ordinary CXT provider-gate boundary only.
CXT's generic setup already completes the native projects, including the six Singularity components, before an authentic Mengele provider can own their callbacks; the probe cannot establish native clock/payment, provider Theory through Weaponization receipts, cancellation/refund, DHR positive five-receipt behavior, or provider cleanup.
Those scenarios require real provider decision and native-project lifecycles in both DLC states, so a populated observation array must never be read as provider completion history.
No second Singularity registration, Kruger host identity, provider stage history, biological raid reservation, or periodic grant is created here.

Event 039's package-owned carrier is `chaosx_cxt_extension_event039_assassin_forces`, its setup effect is `chaosx_cxt_extension_event039_assassin_forces_apply`, and its complete unit-family provider is `chaos_unit_family_provider_524`. The provider is registered from `common/on_actions/039_murder_mystery_on_actions.txt` and implemented in `common/scripted_effects/039_murder_mystery_event19_effects.txt` with the full thirteen-callback Event 019 contract.

Event 024's package-owned carrier is `chaosx_cxt_extension_event024_video_game_in_sweden`, and its idempotent setup effect is `chaosx_cxt_extension_event024_video_game_in_sweden_apply`. The carrier is modifier-free and is registered by `common/on_actions/024_video_game_in_sweden_cxt_on_actions.txt`; the setup effect is implemented in `common/scripted_effects/024_video_game_in_sweden_cxt_effects.txt`. The fixture exposes only `video_game_in_sweden_cxt_fixture_ready` and the documented event and Reliance bounds after CXT initialization; it never fires Event24, selects a Swedish host, grants the staged ideas, creates a commander trait, opens the decision category, or spends country resources.

The public scripted effect name `chaosx_test` and country tag `CXT` are stable interfaces.

## Unit roster verification — 11 October 2026

Acceptance basis: the user requested complete CXT unit and package-formation coverage, family co-location, retained idempotence and package-owned registration, without changes to ordinary units.
Implementation evidence is the unit registry, seven unit-family carriers, the existing four event carriers, the source-package carrier and its 90 fixture definitions, the central 18-family allocation list, and the Livens variant/stockpile profiles.
An independent country-package review checked registration, template placement, family keys, receipt handling, supply-site policy and equipment profiles; the parent applied the identified source and formatting fixes.
An independent localisation review checked the category status, integer count, branch priority, and deployment descriptions.
A final independent deployment review confirmed the supported token selectors, 30 fixed names, 169 dynamic names and six Livens profiles, with no concrete defect found.

The final source checks cover all 79 definitions, 120 concrete templates plus the 79 resolved individual templates, every referenced custom/vanilla sub-unit and equipment dependency, support/HQ compatibility, and all 112 distinct source formation grids.
The model scan covers the named requested unit families and every custom unit-model directory; existing art and counter wiring are reused.
The France/Germany source scenarios check land membership, inherited ownership, existing rail reachability, stable family order and 18 distinct hub-state reservations.
The one-time 3,000,000 manpower fixture exceeds the calculated 2,663,475 roster requirement, and aggregate equipment demands remain below the configured grants.
There is no AI-weight or ordinary-unit balance change.

`hoi4.script_validate` was run through the configured 4.0.0 coding MCP.
File-mode validation was inconclusive: the deployment files returned partial root-scope coverage, while whole harness, unit, stockpile and constants requests timed out after 180 seconds.
The failed file-mode capability was retired rather than retried for every remaining file.
Corrected scoped requests covered the native harness dispatch and resource grant, unit registry and template bodies, four existing event-package effects, stockpiles, family allocation and STATE creators, 90 package fixtures, bounded on-action effects, and status/template-selector triggers.
They returned partial checks with unchecked native argument blocks and unresolved custom-helper calls; no error-severity finding was returned by those retained scoped requests.
These results do not certify meta-effect expansion, full file schemas, equipment-module semantics or observed engine spawning.
The final local review parses all 18 changed script files, resolves all 199 concrete templates, checks the 38 template/profile selector markers and their exact names, and verifies both affected English localisation files.
Ideas, script-constants tables, on-action wrappers and scripted-localisation wrappers are source-reviewed against their installed schemas; a successful MCP validation of every whole changed file is not claimed.
The independent map inspection timed out, so the retained map catalogue and installed map files support the placement check.
The request receipts and one-off checks are retained under ignored `.tmp/cxt_all_units/`; no tooling was added to maintained paths.

The requested isolated Linux run was not performed by this job because `sonnet_log_gate` holds `/tmp/hoi4_wsl.lock` and the active Linux game slot.
The shared capture board records that ownership and the queued menu-logo job; this job acquired no lease and did not disturb either job.
The earlier Clausewitz preflight rejected ELF `a4971c9e8ac9a6f2487dea109e01f9839ee59db7`, while reviewed offsets require `2a79e51358b8b71c09cfb5ddefa0c03649067a4b`.
That refusal blocks native attachment only: the ordinary isolated launcher can run the game, so it is not evidence that the Linux game itself is unavailable.
The connected HOI4 Live Tools route targets Windows and cannot verify that Linux process.
No console command, fresh `error.log`, observed division placement, equipped-variant result or live supply-flow result is claimed by this job.

### Changed files

The existing harness and fixtures were updated in `common/scripted_effects/chaosx_test_country_effects.txt`, `chaosx_test_country_unit_effects.txt`, `chaosx_test_country_stockpile_effects.txt`, `012_africa_gods_cxt_test_effects.txt`, `014_cannibalism_cxt_test_effects.txt`, `016_alien_infantry_cxt_test_effects.txt`, and `039_murder_mystery_cxt_test_effects.txt`.
The central tuning files are `common/script_constants/chaosx_test_country_constants.txt` and `chaosx_test_country_deployment_constants.txt`; allocation and creation live in `common/scripted_effects/chaosx_test_country_deployment_effects.txt`.
Package fixtures live in `common/scripted_effects/chaosx_test_country_package_formation_effects.txt`.
Modifier-free unit, source-formation and template-selector tokens live in `common/ideas/chaosx_test_country_unit_extension_ideas.txt`, `chaosx_test_country_package_formation_ideas.txt`, and `chaosx_test_country_template_selector_ideas.txt`.
Bounded registration is in `common/on_actions/chaosx_test_country_unit_extension_on_actions.txt` and `chaosx_test_country_package_formation_on_actions.txt`.
Status and meta-effect strings use `common/scripted_localisation/chaosx_test_country.txt`, `chaosx_test_country_template_names.txt`, `localisation/english/chaosx_test_country_l_english.yml`, and `chaosx_test_country_template_names_l_english.yml`.
This guide and the canonical `.claude/skills/chaos-redux-units-divisions/SKILL.md` hold the inventory, maps, extension contract and reusable placement rules.
These 22 task paths reuse the existing model and counter assets without changing unit definitions, art or ordinary gameplay balance.

### Simplifications, omissions, and blockers

No unit type, source-package grid, existing model or counter was omitted, and no gameplay simplification or substitute unit was used.
No custom naval/air model unit exists to spawn.
Live Linux verification is unavailable to this job while another job holds the game lease; it is a validation limitation rather than a reduced roster.
Finite territory and a missing capital supply source are explicit placement constraints: waiting families remain registered, visible in the category status, and eligible for later player-triggered application.
The HQ-only unit dependency on Thunder at Our Gates remains the installed engine dependency, and no ordinary sub-unit definition is weakened to bypass it.

### Reference evidence

Installed game root: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
The coding MCP was discovered through the configured local stdio connection and reported version 4.0.0.
The wiki citations are the repository's offline snapshot.

- Installed `documentation/effects_documentation.md`, create_unit 3278–3310, stockpile 1252–1266, railway 2535–2571, and numeric loop 4312–4330; revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- Installed `documentation/triggers_documentation.md`, province building queries 1621–1642, railway construction 1884–1919, control 2320–2328, and railway connection 4603–4627; revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
- Installed `documentation/script_concept_documentation.md` 216–222, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`, and `common/script_constants/documentation.md` 1–34, revision `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.
- Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, create_unit 3366 and stockpile 2253, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
- Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, typed values 425–434 and targeted variable names 547–554, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- Offline `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, scripted text 656–705, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`; native precedent `common/scripted_localisation/AAT_Denmark_scripted_loc.txt` uses `localization_key`.
- Native template/spawn precedents: `common/decisions/AUS.txt` 542–567, `history/general/taog_hq_template.txt`, `common/units/hq_support.txt`, and `history/units/AFG_1936_nsb.txt` for OOB variant forcing.
- The reused state catalogue retains map revision `34b40fa7ff00cf49602d57615f525b0ec820972e86e8c1676f6779eef2a99f6f`; current installed state/definition/supply/rail files were checked for the modeled French and German sites.

Skills used: units/divisions, equipment, map/states, subagents, shared Git commit, and the explicitly requested debug-playtest availability check.
The canonical units/divisions skill was extended with the reusable CXT family, showcase, support-placement, receipt and supported helper-input requirements; its generated mirror is the existing junction to that source.

## Future plans

A future audit utility could compare the explicit non-enumerable baselines and registered-content call sites with live definition folders and report only drift without rewriting gameplay files.

A future optional cleanup command could remove the test facility-campus state transfers before returning to a normal country, but it should remain separate from the destructive one-line setup command.

A future naval and air roster extension could add similarly scoped registration helpers if the mod introduces dedicated custom ship or airframe equipment rather than only land sub-units. No native runtime enumeration for those surfaces was found in the installed documentation.

### Event016 exact native ownership observation

The existing player-triggered chaosx_cxt_event016_probe_native_inventory also invokes chaosx_cxt_event016_probe_native_ownership.
The ownership probe copies the four current selections, exact output-observed and retired flags into chaosx_cxt_event016_observed_selected_*, observed_output_* and observed_retired_* debug flags.
It copies Cloning, Rocketry and Electronics exact source and settlement mode into chaosx_cxt_event016_cloning_native_source/mode, chaosx_cxt_event016_rocketry_native_source/mode and chaosx_cxt_event016_electronics_native_source/mode.
Source codes are none0, Cloning1, FlyingBomb2, JetEngine3, Radar4, and mode codes are none0, freshOutput1, adoptedCompleted2.
High Energy and Biological Weapons are also copied into chaosx_cxt_event016_high_energy_native_source/mode and chaosx_cxt_event016_biological_weapons_native_source/mode.
Their source codes are Reactor5, Anthrax6, Plague7, Tularemia8, Smallpox9, WeaponizedZombies10 and BlackPlague11; chaosx_cxt_event016_observed_reused_* snapshots the seven source-observation flags.
The fixed family source codes are Computation12, Materials13, Biomedical14, Teleportation15, Robotics16, Paleogenetics17, XenobiologicalSynthesis18, AlienArms19 and Temporal20.
Each exposes chaosx_cxt_event016_<family>_native_source/mode and chaosx_cxt_event016_observed_output_<family>, retaining the existing family names and indices.
Singularity exposes chaosx_cxt_event016_singularity_<component>_native_mode and chaosx_cxt_event016_observed_output_singularity_<component> for all six existing component names.
Its dense mode slots use component ID minus one, independently of sparse receipt order, and an absent mode remains none without inventing historical provenance.
These are debug observations and never authorize a stage, complete a project, select a source, refund a payment, or alter provider history.
Missing or short arrays report none rather than creating receipts.
The existing carrier/setup contract is unchanged and the probe adds no periodic registration or grant hook.
CXT's ordinary completed-project fixture covers exact adoption and historical ambiguity, and does not prove a fresh native research clock or payment.
The full native/provider lifecycle matrix and native cancellation/reselection proof remain part of the Event016 completion contract.
The same player-triggered probe calculates the ordinary weekly clone output and records chaosx_cxt_event016_clone_base_weekly_output, chaosx_cxt_event016_clone_deployment_weekly_bonus and chaosx_cxt_event016_clone_total_weekly_output.
This read-only production projection initializes its consumed temporary outputs, clears its weekly mode and grants no equipment, manpower, programme state or periodic CXT replenishment.
The same player-triggered probe observes the existing KRG Portal fabrication transaction through `chaosx_cxt_event016_probe_portal_transit_receipt`.
It records transaction/serial, expected/delivered equipment, actual PP/support/fuel and fresh quote values under `chaosx_cxt_event016_portal_*`, plus actor-exists, funded, output-pending, refund-pending and quote-valid debug flags.
An absent KRG clears those observations; a malformed component array supplies no inferred actual payment.
This observation invokes the pure quote in trigger context with caller-owned temporary outputs and never starts, funds, refunds, completes or replenishes a project.
The probe also evaluates CXT's current capital-state province catalogue through `chaosx_cxt_event016_probe_transit_state_catalog`, recording `chaosx_cxt_event016_transit_catalog_state_id`, `chaosx_cxt_event016_transit_catalog_province_count` and the `chaosx_cxt_event016_transit_catalog_loaded` flag.
These are read-only geometry observations; current supply-node, health, control and route proof are not inferred from the catalogue.
The same player-triggered native ownership probe observes CXT's private Paleogenetics pair through `chaosx_cxt_event016_probe_paleogenetics_deployment`.
It records selected-pair, authenticated-payment, completed-pair, recovery-ready and payment/construction-uncertain debug flags, plus the serial, both measured construction deltas and the actual PP/support/fuel debit amounts under `chaosx_cxt_event016_paleogenetics_*`.
The observer grants no stage, building, equipment, payment, refund or provider identity and adds no recurring hook.
It shares the existing Event016 CXT package and its player-triggered probe entry point, with no new content carrier or periodic grant.
The staffing extension has the modifier-free carrier `chaosx_cxt_extension_event016_paleogenetics_staff` and matching `_apply` helper in the staffing owner source.
Its bounded GER startup and CXT-only daily fallback register the token and mark pending work, while player-triggered setup marks `paleo_staff_cxt_fixture_ready` without granting personnel, stores or payment history.
The same ownership probe observes `chaosx_cxt_event016_staff_held`, `staff_released`, `staff_fee_due`, `staff_transaction` and qualified/release-pending flags.
Those observations never fund, train, release or acknowledge a production receipt.
