# Event 016 final unit and equipment rework handoff

Date: 2026-09-01

## Scope

This tranche closes the reusable battalion, equipment, AI-production, Event 019, CXT, and counter surfaces required by the accepted Event 016 closure contract. It does not change or regenerate any 3D geometry. Final skeletal actions, effects, sounds, entities, export/reimport evidence, and runtime model manifests remain owned by the later no-regeneration 3D tranche.

## Implemented behavior

- `clone_infantry` remains a 2-width, 1,000-manpower battalion requiring 90 infantry weapons and one clone cohort. The editable default division remains ten battalions and 20 width. Its 70 organisation and 20 HP preserve the intended high-organisation, weak-body base identity.
- The physical `clone_equipment` stockpile is the sole reserve-manpower authority. `clone_refresh_reserve_manpower` recomputes the whole stockpile and applies exactly ten weekly manpower per whole stored cohort. Captured or lost stock changes the next reconciliation directly; no transfer ledger or duplicate ownership receipt exists.
- Kruger's clone refinement and weaponization remain separate from Mengele's standard and Aryan refinements. `aryan_clone_infantry` retains the normal German infantry entity mapping.
- `autonomous_robot` now consumes zero human manpower and uses its real robot and support-equipment production bill. Its unit and equipment constants match the existing very-high armor, hardness, piercing, breakthrough, reliability, recovery, and mobility package.
- The remaining reusable battalion consumers are the generic `paleogenetic_creature`, `xenobiological_assault_organism`, and `temporal_guard` identifiers. Their subunit sprite tokens, hidden-technology unlocks, CXT names, Event 019 documentation, and durable 3D manifests no longer point at retired Kruger-specific consumers.
- The hidden operational technologies explicitly enable all normally trainable custom battalions. Alien Infantry deliberately lacks an `enable_subunits` grant and remains landing-only.
- Package-owned example templates are locked, but artificial division caps were removed from Clone Infantry, Autonomous Robots, Paleogenetic Creatures, Xenobiological Assault Organisms, Portal Raiders, and Temporal Guards. Their normal scaling constraints are the actual manpower, equipment, fuel, and industrial contracts. Only one-time scripted starting-force receipts remain bounded.
- Generic AI target templates and equipment-production floors are gated by the exact hidden access technology. Alien Infantry is absent from both AI files because its exact landing transaction owns formation creation.
- Event 019 providers 504-510 and 522 preserve the complete thirteen-callback contract. Normal generated formations enter the central standing-obligation ledger with their exact per-battalion manpower and equipment totals. Provider-management payment remains a separate request transaction. Provider 508 uses only the source-counted alien contact and exact landing-reservation API, and cleanup revokes only Event 019's source receipt.
- The Event 016 CXT carrier registers the D'Rhondan envoy craft, seven concrete equipment types, and all eight frontline consumers. The seven ordinary families recognize the installed legacy CXT templates before the dynamic roster pass so they cannot duplicate; the registered fallback remains able to create them if a later CXT baseline drops those static entries. Alien Infantry records the same country-local processed array after installing its one locked, non-recruitable cohort, preventing the shared dynamic helper from exposing a trainable alien template.

## Exact Event 019 standing obligations before start-factor scaling

| Provider | Formation obligation |
| --- | --- |
| 504 Clone Infantry | 10,000 manpower, 900 infantry equipment, 10 clone equipment |
| 505 Autonomous Robot | 0 manpower, 200 autonomous robot equipment, 40 support equipment |
| 506 Paleogenetic Creature | 1,500 manpower, 165 paleogenetic creature equipment, 45 support equipment |
| 507 Xenobiological Assault Organism | 900 manpower, 150 xenobiological organism equipment, 60 support equipment |
| 508 Alien Infantry | No standing training row; one independently reserved 2,000-laser landing transaction |
| 509 Portal Raider | 4,000 manpower, 40 teleportation equipment, 400 infantry equipment |
| 510 Temporal Guard | 2,800 manpower, 180 temporal guard equipment, 240 infantry equipment, 60 support equipment |
| 522 Aryan Clone Infantry | 10,000 manpower, 900 infantry equipment, 10 clone equipment |

## Assets

The existing large and map counters for Clone Infantry, Aryan Clone Infantry, Autonomous Robots, Portal Raiders, and Alien Infantry remain installed. Six bespoke vanilla-green counter strips complete the Paleogenetic Creature, Xenobiological Assault Organism, and Temporal Guard consumers at the exact vanilla `152x42` large and `60x12` on-map dimensions. `interface/016_brilliant_scientist_generic_counters.gfx` registers the nine required two-frame aliases. The parent reviewed the native-size contact sheet and decoded DDS round-trip; hashes, prompts, alpha evidence, and exact files are recorded in the adjacent counter-completion handoff.

## Validation and evidence

- All touched Clausewitz files have balanced braces, and every AI technology, battalion, and equipment archetype token resolves to an installed definition.
- The provider owner file contains registration plus all thirteen required runtime callbacks for provider IDs 504-510 and 522.
- The project-force rebuild contains no ordinary `set_division_template_cap` calls and clears only legacy cap state.
- A mandatory `hoi4.tech_inspect` retry for the custom subunit unlock surface failed immediately with the exact MCP error `Transport closed`. This is an external tool-transport blocker; source review is not presented as equivalent technology MCP evidence. The last available Portal Raider technology artifact remains `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8f85cee417bf37e514753258564845409f90138f1a3d57279a03c2adf2359718/305b328fc49ef866f42f55ea3a7823164f77696b772298dd7f0fc4940a2a5213/technology-explain-1ebacb793e4e.json`.
- A current `chaosx_country_package_auditor` and `chaosx_ai_probability_auditor` were dispatched for this tranche. Both remained non-responsive after their tool calls were stopped and two finalize-only instructions were sent, so they were interrupted without producing handoffs. The parent therefore reviewed the source, exact callback census, token definitions, CXT transaction order, AI gates, counter consumers, and obligation totals directly. This is not specialist acceptance: both named audits and the required probability comparison remain mandatory in the final closure tranche.

## Remaining boundary

- The seven existing model packages still require the accepted no-regeneration runtime completion tranche. Nothing here is evidence that the models have passed exporter, actual-byte reimport, firearm, particle, sound, counter, or in-game consumer gates.
- Live Hearts of Iron IV acceptance belongs to the user after repository and MCP gates are complete.
