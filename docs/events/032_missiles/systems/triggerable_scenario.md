# Event 032 Triggerable Scenario Runtime

SCN-015, Missile Age, is the Event 032 adapter exposed through the shared Triggerable Scenarios window. It uses raw ID `15`, Fallout remains raw ID `14`, and the existing Global Jihad row remains raw ID `16`. Event 031's current triggerable selector is aligned to Global Jihad at raw ID `16`, while its separate world-end registry reservation remains outside this shared namespace.

## Shared-window contract

The shared window stores the five-profile selector in `triggerable_scenarios_missiles_type` and uses the common four-value `triggerable_scenarios_intensity` selector. The profile labels are Global Proliferation, Saturation War, Command Breakdown, Special Payload Crisis, and Retaliation Network. No Event 032 GUI is introduced.

The row is registered in all four shared sort views. Name sorting places Missile Age between The Hunger Lines and The Unbidden Muster using sort value `5.625`; ID sorting places raw `15` after or before Fallout according to direction. The dispatcher calls `missiles_scenario_launch_unregistered` after the shared confirmation flow.

## Profile and intensity behavior

Global Proliferation applies an ordinary package to valid recipients without selecting an evolution. Saturation War requires a meaningful active war between valid missile recipients and marks belligerents for the saturation package. Command Breakdown requires a vulnerable candidate and marks the bounded guidance and command package. Special Payload Crisis requires a pre-existing supported payload owner and marks integration only for that owner; Event 032 does not create or grant payload stockpiles. Retaliation Network requires at least two valid recipients, establishes warning-ready postures, and marks High and Maximum for bounded warning pressure while Low and Medium retain the no-immediate-launch marker.

Low, Medium, High, and Maximum select the normalized stage, reserve, site capacity, readiness, command control, incident cap, and retaliation-participant targets in `missiles_scenario_scale`. Maximum reaches every valid recipient and the highest supported stage without setting a terminal flag.

## Setup transaction

`missiles_scenario_launch_unregistered` first revalidates the exact profile, intensity, terminal conflict, duplicate, recipient, and profile conditions. It then freezes global runtime inputs, increments one setup receipt, clears the previous failure marker, sets the bounded global setup and bypass flags, processes each valid country once, and clears the country and global bypass state before returning. `missiles_scenario_country_setup_complete` makes country package application idempotent. A package failure marks `missiles_scenario_setup_failed` and prevents a false successful launch receipt while leaving a clean retry path.

The adapter passes these temporary country inputs to the Event 032 core program and technology APIs: `missiles_scenario_package_profile`, `missiles_scenario_package_intensity`, `missiles_scenario_package_share`, `missiles_scenario_package_stage`, `missiles_scenario_package_reserve`, `missiles_scenario_package_site_capacity`, `missiles_scenario_package_readiness`, `missiles_scenario_package_control`, and `missiles_scenario_package_incident_cap`. The core must keep its country mutation atomic and publish `missiles_scenario_package_failed` before the adapter can commit that country.

## Collision and validation boundary

The collision audit found shared raw IDs `1` through `14`, Missile Age at `15`, and the existing worktree-owned Global Jihad row at `16`. Event 031's current triggerable selector is `16`, while its separate world-end registry ID remains `15`; Fallout is unchanged at `14`. The adapter has no world-end branch, no recurring on-action, and no dedicated UI.

The static test surface is `docs/specs/032_missiles_specs/032_missiles_test_matrix.md` under `SCN-015 tests`, including registry collision, profile preflight, intensity scaling, atomic failure, idempotence, save/reload, and terminal-conflict cases. The Event 032 core effects and triggers are present in `common/scripted_effects/032_missiles_effects.txt`, `common/scripted_effects/032_missiles_operations_effects.txt`, `common/scripted_triggers/032_missiles_triggers.txt`, and `common/scripted_triggers/032_missiles_operations_triggers.txt`; engine confirmation remains subject to the mandatory HOI4 MCP pass and the user-owned live-game boundary.
