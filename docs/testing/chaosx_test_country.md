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

If CXT has already been initialized in the save, the same command refreshes technologies, equipment, and capped resources without duplicating the 264 test divisions.

## Unit inventory

The roster is generated from the 88 land sub-units defined under `common/units/`.

It contains 41 frontline battalions and 47 support companies.

Every sub-unit is explicitly unlocked and receives a dedicated recruitable template with `force_allow_recruiting = yes`.

Each frontline template contains one instance of its Chaos Redux battalion.

Each support template contains the requested Chaos Redux support company plus a compatible Chaos Redux line anchor, using `autonomous_robot` where the support company excludes infantry groups and `chaos_battalion` otherwise.

Three fully equipped, fully manned, fully experienced divisions are spawned from every template, for 264 divisions in total.

## Technology, projects, and doctrine

The current merged technology inventory contains 663 definitions from installed vanilla and Chaos Redux technology files, and the harness grants every one without popups.

The current special-project inventory contains 83 definitions, including 49 installed vanilla projects and 34 Chaos Redux projects, and the harness completes every one.

The special-project list is intentionally explicit so additions are visible in code review and future inventory audits can detect drift.

The country adopts the Chaos Warfare grand doctrine, assigns `extermination_columns`, `contaminant_firebases`, `chemical_suppression`, and `integrated_chemical_operations`, grants enough mastery to complete every active track, and closes the establishment mission successfully.

All shared CBRN capacities are raised to their maximum, the unrestricted Chaos Warfare use policy is selected, and protection, operations, disease-response, battlefield-operation, payload-logistics, occupation, civil-defence, and doctrine-owned camp surfaces are activated.

The test fixture records a confirmed chemical-attack history and a national respirator reserve so emergency and civil-defence categories remain visible without waiting for a live attack.

## Stockpile and resources

The initial stockpile receives 1,000,000 units of every concrete Chaos Redux equipment type plus the vanilla equipment dependencies used by Chaos Redux divisions.

Dedicated light, medium, and heavy flame-tank variants are registered so the custom chemical tank support companies have valid equipment in the No Step Back designer system.

The tag-specific `on_weekly_CXT` hook replenishes that full stockpile throughout play.

The tag-specific `on_daily_CXT` hook restores political power, command power, army experience, navy experience, air experience, manpower, nuclear bombs, fuel, stability, and war support.

CXT receives 50 research slots even though all current technologies are completed immediately.

Neither refill hook iterates over every country.

## Special facilities

CXT receives one naval, nuclear, air, land, biowarfare, and chemical-warfare facility.

HOI4 limits all special-project facilities in the shared `special_project_facility` group to one per state, so the effect guarantees six distinct facility-empty controlled states and one legal coastal campus.

If the annexed country lacks enough eligible states or a coastal slot, the harness transfers only the additional random states required to satisfy those engine limits.

The facility allocator counts a transferred state only after a valid random-state body executes and terminates safely if the world contains no further legal facility state.

The `anomaly_signal_beacon_pilot` building is excluded because its definition is a non-buildable 3D asset pilot without a special-project specialization.

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

No additional idea, decision, focus, or UI icon is required for the harness.

## Maintenance

When Chaos Redux adds a land sub-unit, technology, special project, or concrete equipment definition, its explicit generated grant file must be refreshed and the documented counts must be updated.

The one-time initialization flag is `chaosx_test_country_initialized`.

The public scripted effect name `chaosx_test` and country tag `CXT` are stable interfaces.

## Future plans

A future audit utility could compare the explicit generated inventories with live definition folders and report only drift without rewriting gameplay files.

A future optional cleanup command could remove the test facility-campus state transfers before returning to a normal country, but it should remain separate from the destructive one-line setup command.

A future naval and air roster extension could spawn Chaos Redux-only ships and aircraft if the mod introduces dedicated custom ship or airframe equipment rather than only land sub-units.
