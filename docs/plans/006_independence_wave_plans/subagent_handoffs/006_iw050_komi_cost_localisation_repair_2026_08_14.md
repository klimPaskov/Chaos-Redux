# IW-050 Komi administrative cost localisation repair

Date: 2026-08-14

## Scope

This narrow repair aligns the six Komi administration-standard project cost labels with the package-local one-factory reservation already enforced by source.

Changed source files:

- `common/decisions/006_independence_wave_komi_decisions.txt`
- `localisation/english/006_independence_wave_komi_l_english.yml`

The package remains local-only and fail-closed. No central adapter list, content attestation, scenario preflight, deterministic Join, portrait, flag, map, or workbook surface was changed.

## Source correction

The Komi decision file reserves one civilian factory through `@CR_SC_INDEPENDENCE_WAVE_KOM_CIVILIAN_FACTORY_USE = 1`, and the package trigger checks the Komi factory floor of zero before allowing the administration projects to start.

The six standard administration projects previously pointed at the shared `independence_wave_cost_administration_standard` string, which displays the shared two-factory constant.

The six `custom_cost_text` references now use `independence_wave_komi_cost_administration_standard`.

The Komi localisation file now supplies the matching base, blocked, and tooltip keys, each displaying `constant:independence_wave_komi_cost.civilian_factory_use`.

The strategic Komi cost triplet and the security cost path were not changed by this repair.

## Evidence

Static source review found six Komi administration-standard references, zero remaining shared administration-standard references in the Komi decision file, and exactly one occurrence of each new base, blocked, and tooltip key.

The Komi localisation file retains its UTF-8 BOM and has 66 unique keys after the addition.

The current focused `hoi4.event_inspect` call for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` at revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b` with zero selected blocking diagnostics.

The corresponding `hoi4.event_render` state view returned `EVENT_RENDERED_PARTIAL` at the same revision with source-linked JSON, SVG, PNG, and HTML artifacts; validation remains partial because the large workspace defers helper and lifecycle projection.

The event artifact boundary is structural evidence only and does not claim live decision rendering or quantitative AI balance.

## Remaining blockers

IW-050 remains absent from central content attestation, normal and scenario preflight, and deterministic Join.

The exact Pavel Murashev portrait source and rights gate remain unresolved, and the neutral Komi flag provenance and ladder stability remain under review.

The mission probability adapter still has an incomplete candidate pool and unresolved campaign-state inputs, so no normalized probability, timing, dominance, or balance claim is made.
