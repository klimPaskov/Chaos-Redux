# Chaos Redux Test Country

## Purpose

The Chaos Redux Test Directorate is a landless dormant country tag that becomes a complete runtime test harness when invoked from the console.

Its tag is `CXT`, and the console entry point is:

```text
e chaosx_test
```

A literal two-word engine command such as `chaosx test` cannot be registered through release Clausewitz script, so the shortest supported one-line command uses the built-in `effect` alias `e`.

## Transition behavior

The effect records the current country and its capital, switches the human player to CXT, annexes the former country, and restores that capital to CXT.

The annex deliberately uses `transfer_troops = no`, which prevents vanilla divisions from entering the test roster.

After the annex, the harness takes control of one populated non-capital foreign state without annexing it so occupation, coercive-security, protected-administration, and occupied-population test surfaces have a valid target.

If CXT has already been initialized in the save, the same command refreshes technologies, registered projects, equipment, and capped resources without duplicating the 264 static test divisions or any previously processed registered units.

## Unit inventory

The static roster is generated from the 88 land sub-units present when the harness baseline was reviewed. Package-owned registrations extend that roster at runtime without regenerating the core helper.

The static baseline contains 41 frontline battalions and 47 support companies. Runtime registrations add their own frontline or support definitions to that baseline.

Every sub-unit is explicitly unlocked and receives a dedicated recruitable template with `force_allow_recruiting = yes`.

Each frontline template contains one instance of its Chaos Redux battalion.

Each support template contains the requested Chaos Redux support company plus a compatible Chaos Redux line anchor, using `autonomous_robot` where the support company excludes infantry groups and `chaos_battalion` otherwise.

Three fully equipped, fully manned, fully experienced divisions are spawned from every template, for 264 static divisions plus three for every registered unit definition.

## Technology, projects, and doctrine

The technology grant enumerates the engine's `global.technology` database at runtime and grants every installed vanilla and Chaos Redux technology without popups. New technology definitions loaded by the game are therefore included without editing a generated CXT list.

The current static special-project inventory contains 83 definitions, including 49 installed vanilla projects and 34 Chaos Redux projects, and the harness completes every one.

HOI4 does not expose a documented global special-project database array. Future projects use the opt-in registry described below; the static baseline remains explicit so omissions are visible in code review and inventory audits.

The country adopts the Chaos Warfare grand doctrine, assigns `extermination_columns`, `contaminant_firebases`, `chemical_suppression`, and `integrated_chemical_operations`, grants enough mastery to complete every active track, and closes the establishment mission successfully.

All shared CBRN capacities are raised to their maximum, the unrestricted Chaos Warfare use policy is selected, and protection, operations, disease-response, battlefield-operation, payload-logistics, occupation, civil-defence, and doctrine-owned camp surfaces are activated.

The test fixture records a confirmed chemical-attack history and a national respirator reserve so emergency and civil-defence categories remain visible without waiting for a live attack.

## Stockpile and resources

The initial stockpile receives 1,000,000 units of every concrete Chaos Redux equipment type plus the vanilla equipment dependencies used by Chaos Redux divisions.

Dedicated light, medium, and heavy flame-tank variants are registered so the custom chemical tank support companies have valid equipment in the No Step Back designer system.

The tag-specific `on_weekly_CXT` hook replenishes that full stockpile throughout play, including equipment supplied through the opt-in registry.

The tag-specific `on_daily_CXT` hook restores political power, command power, army experience, navy experience, air experience, manpower, nuclear bombs, fuel, stability, and war support. It also runs the registered project, equipment, and unit synchronizers, so an additive package registration is consumed without a global country iteration.

CXT receives 50 research slots even though all current technologies are completed immediately.

Neither refill hook iterates over every country.

## Dynamic extension contract

Technology is the only surface in this harness with a documented runtime database array. The technology helper uses `for_each_loop` over `global.technology` and guards each `set_technology` call with `has_tech`, so recurring weekly synchronization does not reapply already-completed technology effects.

The installed HOI4 documentation and offline wiki do not expose global arrays for special projects, equipment types, sub-unit definitions, special facilities, doctrines, or general systems. Their static CXT inventories therefore remain honest baselines, and future content opts in through one package-owned setup effect.

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

The dynamic unit helpers create one recruitable template and three fully equipped divisions for each newly registered token, then record the token in a CXT-local processed array to prevent duplicate spawns. They do not enumerate or infer sub-unit definitions on their own.

## Special facilities

CXT receives one naval, nuclear, air, land, biowarfare, and chemical-warfare facility.

HOI4 limits all special-project facilities in the shared `special_project_facility` group to one per state, so the effect guarantees six distinct facility-empty controlled states and one legal coastal campus.

If the annexed country lacks enough eligible states or a coastal slot, the harness transfers only the additional random states required to satisfy those engine limits.

The facility allocator counts a transferred state only after a valid random-state body executes and terminates safely if the world contains no further legal facility state.

The `anomaly_signal_beacon_pilot` building is excluded because its definition is a non-buildable 3D asset pilot without a special-project specialization.

Facilities, doctrines, and general systems do not use the project, equipment, or sub-unit definition arrays. A future package exposes a package-owned idempotent `_apply` helper and registers its hidden-idea carrier through the extension bus. The helper checks a stable package flag or the relevant building/system state before applying direct effects such as `set_building_level`, doctrine completion, or system bootstrap.

## Camp systems

The shared genocide and camp-repression systems are initialized and activated for CXT.

The capital receives a concentration camp, an extermination camp converted from the second concentration level, and a gulag labor-camp network, leaving the concentration and extermination buildings active together.

The managed camp ledger, genocide decisions, gulag decisions, extreme doctrine authority, monthly active-site registry, and ordinary-country camp variables are active.

CXT is intentionally not classified as a special Chaos country because that classification would invoke the camp scrub path.

## Country and flag assets

Country wiring is defined in:

- `common/country_tags/chaosx_test_country.txt`
- `common/countries/Chaos Redux Test Country.txt`
- `history/countries/CXT - Chaos Redux Test Country.txt`
- `localisation/english/chaosx_test_country_l_english.yml`

The original flag package is stored under `docs/assets/country_flags/cxt_test_country/`.

Runtime flags are installed as `gfx/flags/CXT.tga`, `gfx/flags/medium/CXT.tga`, and `gfx/flags/small/CXT.tga`.

No additional player-facing idea, decision, focus, or UI icon is required for the harness. Modifier-free hidden ideas are used only as token carriers for registered package setup effects.

## Maintenance

When Chaos Redux adds a technology definition, no CXT inventory edit is required because the runtime technology array is scanned. Every package that adds a special project, concrete equipment type, land sub-unit, special facility, doctrine, or general system must add its hidden-idea carrier, idempotent `_apply` setup effect, startup registration, and tag-specific daily repair call in the same change. The explicit 83-project, 71-equipment, and 88-static-sub-unit baselines remain reviewable snapshots; package registrations extend them additively at runtime.

The one-time initialization flag is `chaosx_test_country_initialized`.

The public scripted effect name `chaosx_test` and country tag `CXT` are stable interfaces.

## Future plans

A future audit utility could compare the explicit non-enumerable baselines and registered-content call sites with live definition folders and report only drift without rewriting gameplay files.

A future optional cleanup command could remove the test facility-campus state transfers before returning to a normal country, but it should remain separate from the destructive one-line setup command.

A future naval and air roster extension could add similarly scoped registration helpers if the mod introduces dedicated custom ship or airframe equipment rather than only land sub-units. No native runtime enumeration for those surfaces was found in the installed documentation.
