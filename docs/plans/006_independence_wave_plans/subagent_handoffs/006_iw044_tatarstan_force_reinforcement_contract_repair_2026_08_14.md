# IW-044 Tatarstan force-reinforcement contract repair — 2026-08-14

## Disposition

The admitted IW-044 package now matches its accepted p44 regular-defector force mapping. The repair is limited to the TAT package setup and readiness trigger; central adapter, attestation, preflight, and Join surfaces are unchanged.

## Defect and repair

The accepted TAT mapping in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` requires secure depots, conversion of defecting host units, regional guards, a professional officer corps, and capital-border defense. The shared p44 reinforcement mask is `1550`, which decodes to `2 + 4 + 8 + 512 + 1024`: regional guards, secure depots, convert defectors, professional officers, and capital-border defense.

The TAT setup and prepared trigger previously used integrate militias and terrain units while excluding convert defectors and capital-border defense. `common/scripted_effects/006_independence_wave_tatarstan_package_effects.txt` now adds the convert-defectors and capital-border-defense pathways, and `common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt` requires those flags while excluding integrate militias and terrain units. The five active flags and the p44 mask are now identical.

## Validation boundary

No TAT ideas, decisions, focus hooks, localisation, assets, central dispatcher, content attestation, normal/scenario preflight, or deterministic Join entries were changed by this repair. Run the focused Event MCP scan and the standard allocator, SCN-008, flag, and protected-tag audits after the source edit. No weighted surface changed, so no probability claim is made from this repair.

## Remaining risks

Typed TAT mission fixtures and quantitative AI evidence remain unresolved because the installed probability adapter returns incomplete pools/no weighted strategy surfaces. This force alignment does not change the current Event 006 authority counts or authorize any additional package admission.
