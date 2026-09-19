# Chaos Redux Test Country

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

The static baseline unlocks 87 Chaos Redux land sub-units: 40 combat battalions and 47 support companies. It installs 50 recruitable, multi-battalion templates covering every one of those units and spawns three fully equipped, fully manned, fully experienced divisions per template. The shared count is `chaosx_test_country_count.divisions_per_template` in `common/script_constants/chaosx_test_country_constants.txt`.

The main family compositions follow installed Chaos country or runtime formations: Brainzz Horde, Mutated Zombie Muster, Cave Brood Muster, Rat Brood Muster, Africa Strange Formation, Africa Elephant Guard, Coal Golem Column, Death hosts, and the Event 016 project forces. The test copies omit vanilla support companies so that every unit in their line and support slots belongs to Chaos Redux. CBRN command/protection formations use six `chaos_battalion` combat battalions with compatible custom support companies; armored-delivery variants use `autonomous_robot` as an armor-group anchor. The 18 chemical-tank and seven Livens support variants have separate formations because their shared `cbrn_offensive_delivery` exclusion prevents them from coexisting in one support roster.

Event 014 contributes two valid formations covering its nine irregular infantry sub-units, with the mobile Bone Riders on a separate line. Event 039 contributes two formations covering its five assassin combat units and Saboteur Cell support company, with mechanized assassins on a separate line. Their package-owned setup effects mark every covered token as processed, so the dynamic fallback does not create duplicate templates. Event 016's `alien_infantry` uses a recruitable CXT-only ten-battalion landing cohort matching its normal API formation; ordinary Event 016 recruitment rules remain unchanged.

Each division independently selects a random owned, controlled CXT state, so the roster is dispersed across the Directorate's territory instead of concentrated in the capital. Random selections may coincide, and a country with only one owned, controlled state necessarily places every division there. The debug deployment decision can add another batch without creating duplicate template definitions.

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

The initial stockpile receives 1,000,000 units of every concrete Chaos Redux equipment type plus the vanilla equipment dependencies used by Chaos Redux divisions.

Dedicated light, medium, and heavy chemical-carrier variants use the concrete `light_tank_flame_chassis_3`, `medium_tank_flame_chassis_3`, and `heavy_tank_flame_chassis_3` types in the No Step Back designer system.
Their named domestic variants are created before stockpile grants and unit creation, and stockpile calls identify both the concrete type and variant name.

CXT has no periodic equipment, unit, research, resource, or package grants. Initial setup grants the baseline once. Tag-scoped package daily hooks only register an unseen carrier and mark pending work; they never apply it.

The player-only **Test Directorate** decision category provides repeatable, zero-cost controls:

- **Refill National Resources** adds the configured political power, command power, experience, manpower, fuel, nuclear bombs, stability, and war support.
- **Refill Equipment Stockpile** runs the static and registered-equipment stockpile grants.
- **Complete Research and Projects** reruns the dynamic technology scan and core and registered special-project completion helpers.
- **Apply Registered Systems** consumes package carriers, registered projects, and newly registered unit formations only when selected. It registers new equipment tokens, but stockpile quantities are granted by **Refill Equipment Stockpile**.
- **Deploy Test Formations** adds three more divisions of every installed static and package-owned template without redefining existing templates.

These decisions use the installed vanilla `GFX_decision_category_generic_crisis` and `GFX_decision_generic_research` sprites; no new bitmap assets are required. The category is visible only to a human CXT with `chaosx_test_country_initialized`. The decision scripts are `common/decisions/categories/chaosx_test_country_debug_categories.txt` and `common/decisions/chaosx_test_country_debug_decisions.txt`, and their text is in `localisation/english/chaosx_test_country_l_english.yml`.

CXT receives 50 research slots even though all current technologies are completed during setup.

## Dynamic extension contract

Technology is the only surface here with a documented runtime database array. The technology helper scans every real `global.technology` entry only during initial setup or when **Complete Research and Projects** is selected. HOI4 does not expose equivalent global arrays for special projects, equipment, sub-unit definitions, facilities, doctrines, or general systems, so those remain additive package-owned registrations.

A package that adds one of those surfaces must register an idempotent setup effect and a modifier-free hidden-idea carrier. The carrier id matches the setup effect name before its `_apply` suffix. The package registers the carrier from a bounded existing-country `on_startup` scope and can repeat registration from an additive `on_daily_CXT` fallback. Daily registration sets `chaosx_test_country_registered_sync_pending` when new content appears; it never applies grants. Initial setup consumes all available carriers, and later content waits for **Apply Registered Systems**.

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

For future frontline registrations without a package-owned grouped builder, the generic fallback creates one six-battalion recruitable formation and three divisions with independent random owned, controlled state selections. For support registrations, it creates six battalions of the supplied combat anchor and one support company. The anchor must already be processed as a combat sub-unit; invalid or missing anchors are not consumed and cannot create a support-only division. Package authors must verify battalion-group compatibility and `same_support_type` exclusions, and should provide a grouped owner-authored formation when several related units arrive together. The processed arrays prevent duplicate templates and initial spawns. The manual deployment decision can reinforce both generic registered formations and the Event 014, 016, and 039 package-owned formations.

A new land sub-unit also needs an explicit Event 19 disposition in the same owner change. A combat unit extends an existing Chaos unit-family provider or receives a complete owner-side provider registration; a support unit is documented as an inseparable provider attachment, a parent-owned support consumer, or a rejected standalone lot with the engine reason. The owner updates `docs/events/019_infantry_spawn/systems/unit_family_coverage.md` and `docs/systems/cbrn_warfare/chaos_unit_family_registry.md`.

Temporary `CXT_SETUP_TRACE` markers remain around the console receiver and setup stages while the earlier activation freeze remains unresolved in `runtime_repairs/20260913_cxt_technology_validation/freeze_repair.md`.

## Special facilities

CXT receives one naval, nuclear, air, land, biowarfare, and chemical-warfare facility.

HOI4 limits special-project facilities in the shared `special_project_facility` group to one per state.
Each type preserves an existing controlled campus or uses an owned, controlled, facility-empty state that passes the installed `can_construct_building` check for that exact building.
When no owned candidate is legal, the bounded allocator considers non-capital foreign candidates, transfers ownership and control, and revalidates construction.
Rejected candidates recover their original owner and controller and are excluded from further attempts for that type; the temporary rejection array is cleared after the search.
Naval candidates require a coast.
If the world has no legal candidate, the allocator terminates and records an explicit per-type missing-campus flag and aggregate provisioning-incomplete flag; it does not attempt illegal construction or substitute another facility.

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

When Chaos Redux adds a technology definition, no CXT inventory edit is required because the runtime technology array is scanned during setup and the manual research decision. Every package that adds a special project, concrete equipment type, land sub-unit, special facility, doctrine, or general system must add its hidden-idea carrier, idempotent `_apply` setup effect, startup registration, and tag-specific registration-only daily fallback in the same change. A new land sub-unit must also complete the Event 19 disposition and provider obligations described above. The explicit 83-project, 71-equipment, and 87-static-sub-unit baselines are reviewable snapshots; package registrations extend them additively when the player applies pending systems. A package with several related units should author one or more valid grouped formations and mark those tokens processed before the generic fallback runs.

The one-time initialization flag is `chaosx_test_country_initialized`.

Event 021's package-owned carrier is `chaosx_cxt_extension_event021_random_civil_war`, its idempotent setup effect is `chaosx_cxt_extension_event021_random_civil_war_apply`, and its inert readiness receipts are the global `random_civil_war_cxt_content_registered` flag plus the CXT-local `random_civil_war_cxt_extension_seen` flag. The carrier is registered from `common/on_actions/021_random_civil_war_cxt_on_actions.txt` and implemented in `common/scripted_effects/021_random_civil_war_cxt_test_effects.txt`; it registers the reusable framework without selecting a target, creating a front, firing Event 021, or spending country resources.

Event 035's package-owned carrier is `chaosx_cxt_extension_event035_great_depression`, its setup effect is `chaosx_cxt_extension_event035_great_depression_apply`, and its inert readiness proof is `great_depression_cxt_fixture_ready`. The carrier is registered from `common/on_actions/035_great_depression_cxt_on_actions.txt` and implemented in `common/scripted_effects/035_great_depression_cxt_effects.txt`; the fixture does not start a depression or modify an economy.

Event 028's package-owned carrier is `chaosx_cxt_extension_event028_asteroid_incoming`, its setup effect is `chaosx_cxt_extension_event028_asteroid_incoming_apply`, and its inert readiness flag is `asteroid_incoming_cxt_fixture_ready`. The carrier is registered from `common/on_actions/028_asteroid_incoming_cxt_on_actions.txt` and implemented in `common/scripted_effects/028_asteroid_incoming_cxt_effects.txt`.

Event 029's package-owned carrier is `chaosx_cxt_extension_event029_riches_found`, its idempotent setup effect is `chaosx_cxt_extension_event029_riches_found_apply`, and its inert readiness flag is `riches_found_cxt_fixture_ready`. The carrier is registered from `common/on_actions/029_riches_found_cxt_on_actions.txt` and implemented in `common/scripted_effects/029_riches_found_cxt_effects.txt`; it initializes the bounded registry for inspection without firing Event 029, creating a mine, paying political power, or activating an evolution.

Event 032's package-owned carrier is `chaosx_cxt_extension_event032_missiles`, its idempotent setup effect is `chaosx_cxt_extension_event032_missiles_apply`, and its inert readiness flag is `missiles_cxt_fixture_ready`. The carrier is registered from `common/on_actions/032_missiles_cxt_on_actions.txt` and implemented in `common/scripted_effects/032_missiles_cxt_effects.txt`; it initializes only the Event 032 launch-state ledgers without firing the event, granting missile technology, creating a site, or stocking a reserve.

Event 023's package-owned carrier is `sov_nuclear_bombs_cxt_extension_event023`, its idempotent setup effect is `sov_nuclear_bombs_cxt_extension_event023_apply`, and its registration receipt is `sov_nuclear_bombs_cxt_content_registered`. The carrier is modifier-free in `common/ideas/023_sov_nuclear_bombs_cxt_extension_ideas.txt`; bounded startup and `on_daily_CXT` registration live in `common/on_actions/023_sov_nuclear_bombs_cxt_on_actions.txt`, and the setup effect lives in `common/scripted_effects/023_sov_nuclear_bombs_cxt_test_effects.txt`. The fixture initializes only the neutral Event 023 ledger contract. It does not fire Event 023, grant the 100-device opening, grant nuclear technology, create reactors or storage sites, authorize a launch, or execute a physical device transaction.

Event 027's package-owned carrier is `chaosx_cxt_extension_event027_doctrine_research`, and its idempotent setup effect is `chaosx_cxt_extension_event027_doctrine_research_apply`. The carrier is registered from `common/on_actions/027_doctrine_research_cxt_on_actions.txt` and the setup dispatcher is implemented in `common/scripted_effects/027_doctrine_research_cxt_effects.txt`; it initializes the Event 027 adapter and ledger only for the CXT fixture and never creates a research batch.

Event 016's existing `chaosx_cxt_extension_event016_alien_infantry_apply` also reconciles only CXT's registered Portal beachheads, rebuilds only already-recorded physical Singularity sites while settling an invalid pending construction receipt without fabricating a site, and selects the Anthrax operational agent once that native technology is present and no selection or transaction exists.
The same carrier grants the six conventional Weaponization packages through the provenance-free core only when their durable receipt is missing and then reconciles their existing modifiers.
This exposes the ordinary Wonder-Technology Operations category without assigning Kruger, creating a native project ledger, fabricating event-source history, or executing a paid directive.
The shared computation-slot marker keeps repeated extension synchronization idempotent.
It does not create a breach, start a raid, produce a payload, authorize a release, or clear a pending biological operation.
The existing package carrier and startup/tag-specific registration hooks own this coverage; no additional global tick is introduced.

Event 039's package-owned carrier is `chaosx_cxt_extension_event039_assassin_forces`, its setup effect is `chaosx_cxt_extension_event039_assassin_forces_apply`, and its complete unit-family provider is `chaos_unit_family_provider_524`. The provider is registered from `common/on_actions/039_murder_mystery_on_actions.txt` and implemented in `common/scripted_effects/039_murder_mystery_event19_effects.txt` with the full thirteen-callback Event 019 contract.

Event 024's package-owned carrier is `chaosx_cxt_extension_event024_video_game_in_sweden`, and its idempotent setup effect is `chaosx_cxt_extension_event024_video_game_in_sweden_apply`. The carrier is modifier-free and is registered by `common/on_actions/024_video_game_in_sweden_cxt_on_actions.txt`; the setup effect is implemented in `common/scripted_effects/024_video_game_in_sweden_cxt_effects.txt`. The fixture exposes only `video_game_in_sweden_cxt_fixture_ready` and the documented event and Reliance bounds after CXT initialization; it never fires Event24, selects a Swedish host, grants the staged ideas, creates a commander trait, opens the decision category, or spends country resources.

The public scripted effect name `chaosx_test` and country tag `CXT` are stable interfaces.

## Future plans

A future audit utility could compare the explicit non-enumerable baselines and registered-content call sites with live definition folders and report only drift without rewriting gameplay files.

A future optional cleanup command could remove the test facility-campus state transfers before returning to a normal country, but it should remain separate from the destructive one-line setup command.

A future naval and air roster extension could add similarly scoped registration helpers if the mod introduces dedicated custom ship or airframe equipment rather than only land sub-units. No native runtime enumeration for those surfaces was found in the installed documentation.
