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

If CXT has already been initialized in the save, the same command refreshes technologies, registered projects, equipment, and capped resources without duplicating the 261 static test divisions, the locked Event 016 Alien Landing Cohort, or any previously processed registered units.

## Unit inventory

The static roster is generated from the 87 recruitable land sub-units present when the harness baseline was reviewed. Package-owned registrations extend that roster at runtime without regenerating the core helper. Event 016 registers `portal_raider`, `clone_infantry`, `aryan_clone_infantry`, `autonomous_robot`, `paleogenetic_creature`, `xenobiological_assault_organism`, and `temporal_guard` through the ordinary dynamic helper, while `alien_infantry` is handled separately because its battalion is a scripted landing-only unit and must remain locked and untrainable.

Event 014 registers nine additional frontline tokens at runtime, including `cannibal_bone_riders`; its locked `Scavenged Elephant Column` uses the installed vanilla `elephantry` token and therefore does not add a second elephant sub-unit or model.

The static baseline contains 40 frontline battalions and 47 support companies. Runtime registrations add their own frontline or support definitions to that baseline; Event 016 supplies the separate locked Alien Infantry battalion.

Every static sub-unit is explicitly unlocked and receives a dedicated recruitable template with `force_allow_recruiting = yes`. Registered packages may intentionally use a locked, non-recruitable template when their unit is scripted-only; Event 016 does this for Alien Infantry.

Each frontline template contains one instance of its Chaos Redux battalion.

Each support template contains the requested Chaos Redux support company plus a compatible Chaos Redux line anchor, using `autonomous_robot` where the support company excludes infantry groups and `chaos_battalion` otherwise.

Three fully equipped, fully manned, fully experienced divisions are spawned from every static template, for 261 static divisions plus three for every registered unit definition. Event 014 contributes 27 runtime frontline divisions from its nine registered tokens, while Event 016 contributes three locked Alien Landing Cohorts for unit and provider validation.

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

The tag-specific `on_weekly_CXT` hook replenishes that full stockpile throughout play, including equipment supplied through the opt-in registry.

The tag-specific `on_daily_CXT` hook restores political power, command power, army experience, navy experience, air experience, manpower, nuclear bombs, fuel, stability, and war support. It also queues the registered project, equipment, unit, and general-system synchronizers, so additive package registrations are consumed together without a global country iteration. Event 016 registers all eight project-force frontline tokens, seven concrete equipment types, and the D’Rhondan envoy craft through `chaosx_cxt_extension_event016_alien_infantry`; the same setup effect creates the one locked Alien Landing Cohort and lets the generic helper create ordinary test formations for the seven normally trainable families. Event 014 registers all nine custom frontline tokens through one idempotent extension effect on startup and repairs existing saves through the same tag-scoped daily path. Event 026 registers its global sale runtime through the same hidden-carrier contract so the test harness can initialize the cost-source lifecycle without a new recurring world scan. Event 028 registers `chaosx_cxt_extension_event028_asteroid_incoming` and exposes the inert `asteroid_incoming_cxt_fixture_ready` flag after CXT initialization; it never fires the global asteroid or applies impact state. Event 032 registers `chaosx_cxt_extension_event032_missiles` and exposes the inert `missiles_cxt_fixture_ready` flag after initializing only the launch-state ledgers; it never fires Event 032, grants missile technology, creates a launch site, or stocks a reserve. Event 039 registers `chaosx_cxt_extension_event039_assassin_forces`, all five Assassin Forces frontline tokens, the support-only Saboteur Cell, and `assassin_operations_kit_1` through the same hidden-carrier contract. The Event 039 setup is idempotent and only uses the tag-scoped daily fallback to repair an existing CXT save. The famine fixture registers `chaosx_cxt_extension_famine` and places the capital at the supply-strain threshold without severe famine or mortality. The separate migration fixture registers `chaosx_cxt_extension_migration` and gives CXT bounded reception capacity without creating a cohort, route, or population transfer.

CXT receives 50 research slots even though all current technologies are completed immediately.

Neither refill hook iterates over every country.

## Dynamic extension contract

Technology is the only surface in this harness with a documented runtime database array. The technology helper uses an indexed loop over every real `global.technology` entry and guards each `set_technology` call with `has_tech`, so recurring weekly synchronization does not reapply already-completed technology effects.

The installed HOI4 documentation and offline wiki do not expose global arrays for special projects, equipment types, sub-unit definitions, special facilities, doctrines, or general systems. Their static CXT inventories therefore remain honest baselines, and future content opts in through one package-owned setup effect. Event 016 is the first package-owned registration that deliberately keeps a registered combat sub-unit locked and non-recruitable.

Registration values are temporary variables containing a special-project object scope or a documented tokenizable database value. The global registries persist for the save, duplicate entries are ignored, and the CXT daily/weekly hooks consume them. A package's idempotent setup effect uses the definition helpers it needs:

```text
# Inside the package-owned CXT setup effect:
set_temp_variable = { var = chaosx_test_country_registration_special_project value = sp:my_project }
chaosx_test_country_register_special_project = yes

set_temp_variable = { var = chaosx_test_country_registration_equipment value = token:my_equipment }
chaosx_test_country_register_equipment = yes

set_temp_variable = { var = chaosx_test_country_registration_frontline_subunit value = token:my_battalion }
chaosx_test_country_register_frontline_subunit = yes

set_temp_variable = { var = chaosx_test_country_registration_support_subunit value = token:my_support_company }
set_temp_variable = { var = chaosx_test_country_registration_support_anchor value = token:infantry }
chaosx_test_country_register_support_subunit = yes

# Register the package setup dispatcher through a modifier-free hidden idea.
set_temp_variable = { var = chaosx_test_country_registration_extension_effect value = token:package_cxt_extension }
chaosx_test_country_register_extension_effect = yes
```

The `sp:<id>` form in the first example is intentional. The offline wiki defines `sp:<special_project>` as a dedicated special-project scope, and the official `complete_special_project` and `is_special_project_completed` documentation accepts `var:` targets. Arrays persist database-object values, so the registered value can be read as `var:chaosx_test_country_current_special_project` by the completion loop. The official token-valued-variable list covers equipment and script-enum sub-unit values but does not prescribe `token:<id>` for special projects; changing the first example to `token:<id>` would therefore be an unsupported inference.

The special-project and equipment helpers are `chaosx_test_country_register_special_project` and `chaosx_test_country_register_equipment`. The unit helpers are `chaosx_test_country_register_frontline_subunit` and `chaosx_test_country_register_support_subunit`; support registrations must provide a compatible line anchor. The package wrapper registers a hidden-idea carrier such as `package_cxt_extension`, and the matching country-scoped setup effect must be named `package_cxt_extension_apply`.

Facilities, doctrine branches, and general systems use the same package setup-effect extension registry because they are not database-token arrays. A package wrapper sets `chaosx_test_country_registration_extension_effect` to its modifier-free hidden-idea carrier and calls `chaosx_test_country_register_extension_effect`; CXT resolves the documented idea token with `GetTokenKey`, appends `_apply`, and dispatches the matching setup effect through `meta_effect` before completing registered projects, refilling equipment, or creating registered unit templates. Each setup effect must apply its direct facility, doctrine, or system changes behind a stable flag or state check so the daily repair bus is idempotent.

The hidden idea is never applied to a country and needs no modifiers, localisation, or icon. It exists solely because ideas are a documented tokenizable database type; the dispatcher does not rely on unsupported raw tokenization of custom scripted-effect names.

Every package calls the same idempotent extension-registration wrapper from an additive `on_startup` block using a bounded existing-country scope, for example `random_country = { limit = { exists = yes } package_register_cxt_content = yes }`, and retains a guarded `on_daily_CXT` block that calls the wrapper. `chaosx_test_country_register_extension_effect` returns `chaosx_test_country_extension_registration_added = 1` only when it inserts a new carrier, so the package daily fallback calls `chaosx_test_country_sync_registered_content = yes` only behind that check; the core CXT daily hook owns ordinary recurring synchronization. The global registry does not require that the startup scope be CXT, which avoids assuming that a landless dormant tag is instantiated. Startup registration gives the first `e chaosx_test` invocation immediate coverage, while the tag-specific daily path repairs existing saves without a whole-world iteration. The built-in `on_weekly_CXT` block performs the technology scan and full stockpile replenishment.

The core and package daily requests mark pending work and reuse one queued `chaosx_test_country.2` receiver.
The receiver runs one hour after scheduling, after the additive daily hooks have finished registering their carriers, and consumes the complete extension, project, equipment, and unit registries.
Separate queued and pending-work flags let an explicit refresh consume current work immediately while retaining the scheduled receipt for any later registration; that later registration does not schedule a duplicate receiver.
Initial setup and explicit console refresh invoke the same apply body immediately.

Temporary `CXT_SETUP_TRACE` markers cover console entry, the activation receiver, origin annexation, capital validation, every setup stage, facility types, extension carriers, and the first queued daily application.
The trace flag clears after a queued application completes; an unfinished setup keeps it enabled.
These diagnostics are intended to identify the blocking stage of the reported Germany-origin freeze before test units appeared; the freeze itself remains unresolved, as recorded in `runtime_repairs/20260913_cxt_technology_validation/freeze_repair.md`.

Event 039's package-owned carrier is `chaosx_cxt_extension_event039_assassin_forces`, its setup effect is `chaosx_cxt_extension_event039_assassin_forces_apply`, and its provider registration is `murder_mystery_register_event19_assassin_provider`. The carrier is modifier-free in `common/ideas/039_murder_mystery_ideas.txt`; the startup and daily registration hooks live in `common/on_actions/039_murder_mystery_on_actions.txt`, and the idempotent CXT dispatcher lives in `common/scripted_effects/039_murder_mystery_cxt_test_effects.txt`.

Event 012 registers `chaosx_cxt_extension_event012_africa_gods` through the modifier-free carrier in `common/ideas/012_africa_gods_cxt_extension_ideas.txt`, with startup and tag-scoped daily repair in `common/on_actions/012_africa_gods_cxt_on_actions.txt` and the idempotent setup effect in `common/scripted_effects/012_africa_gods_cxt_test_effects.txt`. The fixture registers the existing `chaosx_elephant` frontline token and `chaosx_elephant_equipment_1`, publishes `gods_of_africa_cxt_fixture_ready` after CXT initialization, and never fires Africa Is One, creates a host, or starts the Gods tribute loop; the unit continues to resolve its visual through vanilla `sprite = elephantry`.

The dynamic unit helpers create one recruitable template and three fully equipped divisions for each newly registered token, then record the token in a CXT-local processed array to prevent duplicate spawns. Event 016 uses that helper for its seven normally trainable generic families and handles `alien_infantry` in its package `_apply` effect instead, creating one locked template with `force_allow_recruiting = no` before recording the token as processed. The helpers do not enumerate or infer sub-unit definitions on their own.

Every new land sub-unit also requires an explicit Event 19 disposition in the same owner change. A combat unit either extends an existing Chaos unit-family provider or receives one new owner-side provider registration with the complete thirteen-callback Event 19 API. A support unit is recorded as an inseparable provider attachment, an explicitly parent-owned support consumer, or a rejected standalone lot with the engine reason documented. The owner must update `docs/events/019_infantry_spawn/systems/unit_family_coverage.md` and the authoritative registry contract in `docs/systems/cbrn_warfare/chaos_unit_family_registry.md`. A future family must not add an Event 19 family list, custom-equipment switch, localisation switch, or second Event 19 registry file.

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

No additional player-facing idea, decision, focus, or UI icon is required for the harness. Modifier-free hidden ideas are used only as token carriers for registered package setup effects.

## Maintenance

When Chaos Redux adds a technology definition, no CXT inventory edit is required because the runtime technology array is scanned. Every package that adds a special project, concrete equipment type, land sub-unit, special facility, doctrine, or general system must add its hidden-idea carrier, idempotent `_apply` setup effect, startup registration, and tag-specific daily repair call in the same change. A new land sub-unit must also complete the Event 19 disposition and provider obligations described above. The explicit 83-project, 71-equipment, and 87-static-sub-unit baselines remain reviewable snapshots; package registrations extend them additively at runtime. Event 014's nine-token extension and Event 016's eight-token project-force extension are documented in the unit inventory above and do not alter those static baselines.

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
