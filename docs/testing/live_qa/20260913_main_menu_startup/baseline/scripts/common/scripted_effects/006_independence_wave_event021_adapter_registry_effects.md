# Event 006 / Event 021 Adapter Registry

`independence_wave_initialize_event021_adapter_registry` is the Event 006-owned compatibility contract consumed by Event 021.

- Scope: any.
- Inputs: none.
- Output: idempotently publishes `global.independence_wave_event021_complete_package_ids` and sets `independence_wave_event021_adapter_registry_initialized`.
- Contents: only source-attested, complete human Event 006 packages that pass the Event 021 adapter preflight.
- Side effects: none beyond the adapter registry. It does not fire Event 006, alter its weight or cap, advance evolutions, enroll league members, publish released-package rows, or initialize a country.
- Consumer: `event021_parent_find_event6_package` performs the per-host anchor, carrier, identity, and final package validation before use.

When a complete Event 006 package is added or removed, update this Event 006-owned registry rather than copying the package list into Event 021.

`independence_wave_capture_event021_adapter_actor` owns the matching package-to-carrier mapping.

- Scope: Event 021 host country.
- Input: `independence_wave_event021_adapter_package_id`.
- Output: regular event target `random_civil_war_event6_selected_actor` when that carrier exists.
- Side effects: none; it does not create, activate, or enroll the carrier.

`independence_wave_release_event021_adapter_actor` owns the matching package-to-release mapping.

- Scope: Event 021 host country.
- Input: `independence_wave_event021_adapter_package_id`.
- Output: releases the registered static carrier only when that carrier does not already exist.
- Side effects: country release only; package setup, Event 006 history, evolution, league, and network state remain untouched.

`independence_wave_event021_dormant_package_available` is defined in `common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt` and owns the matching package-to-anchor/carrier admission table.

- Scope: proposed Event 021 host country.
- Inputs: Event 021's shared minimum population and infrastructure constants.
- Output: true when at least one admitted package has its exact controlled anchor and a dormant reusable carrier.
- Side effects: none.
