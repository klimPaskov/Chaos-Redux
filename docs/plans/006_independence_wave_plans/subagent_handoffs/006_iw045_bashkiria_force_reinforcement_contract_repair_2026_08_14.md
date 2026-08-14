# IW-045 Bashkiria force-reinforcement contract repair — 2026-08-14

## Disposition

The admitted IW-045 package now matches its accepted p45 force mapping. The repair is limited to the BSK package setup and readiness trigger; central adapter, attestation, preflight, and Join surfaces are unchanged.

## Defect and repair

The accepted BSK mapping in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` requires secure depots, conversion of defecting host units, regional guards, terrain units, and professional officers. The shared p45 reinforcement mask is `654`, which decodes to `2 + 4 + 8 + 128 + 512`: regional guards, secure depots, convert defectors, terrain units, and professional officers.

The BSK setup and prepared trigger previously used integrate militias and excluded convert defectors. `common/scripted_effects/006_independence_wave_bashkiria_package_effects.txt` now adds `independence_wave_add_reinforce_convert_defectors`, and `common/scripted_triggers/006_independence_wave_bashkiria_package_triggers.txt` requires the corresponding flag while excluding integrate militias. The five active flags and the p45 mask are now identical.

## Validation boundary

No BSK ideas, decisions, focus hooks, localisation, assets, central dispatcher, content attestation, normal/scenario preflight, or deterministic Join entries were changed by this repair. Run the focused Event MCP scan and the standard allocator, SCN-008, flag, and protected-tag audits after the source edit. No weighted surface changed, so no probability claim is made from this repair.

## Remaining risks

The package’s independent portrait/flag review and current typed probability evidence remain the governing admission gates. This force alignment does not change the current Event 006 authority counts or authorize any additional package admission.
