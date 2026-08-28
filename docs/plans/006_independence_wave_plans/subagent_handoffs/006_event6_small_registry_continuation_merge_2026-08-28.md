# Event 006 small-registry continuation merge — 2026-08-28

## Scope

This bounded source-layout pass consolidates two remaining small Event 006 parser files into their existing canonical registries. It does not change gameplay logic, package admission, formable readiness, evolution timing, or pre-event visibility.

## Files changed

- `common/countries/cosmetic.txt` now contains the 17 formable and route cosmetic definitions formerly parsed from `common/countries/006_independence_wave_formable_cosmetics.txt` under a source marker.
- `common/mtth/chaosx_mtth_variables.txt` now contains the `independence_wave_evolution_interval` entry formerly parsed from `common/mtth/006_independence_wave_evolution_mtth.txt` under a source marker.
- `docs/events/006_independence_wave/form39_melanesian_federation.md` and `docs/events/006_independence_wave/evolutions.md` point to the canonical receivers.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` record the current source authority.
- The standalone `common/countries/006_independence_wave_formable_cosmetics.txt` and `common/mtth/006_independence_wave_evolution_mtth.txt` parser files are removed.

## Preservation checks

- All 17 cosmetic identifiers (`KCX`, `NUX`, `LCX`, `RLX`, `MIX`, `PFX`, `MFX`, the five CHU/Volga identities, and the five ASY/Mesopotamian identities) remain present with their original colour values.
- `independence_wave_evolution_interval` retains its base and seven modifiers, including the World Collapse, Totalen Chaos, chaos-tier, network-density, and minimum-network conditions.
- A source-body comparison after comment and line-ending normalization is exact for both moved payloads. No duplicate cosmetic identifier or MTTH entry was introduced.
- The removed files were standalone parser inputs only; no country tag, effect, trigger, event, decision, or localization reference required a gameplay edit.
- The merge removes two parser files and saves 111 bytes across the four affected source paths after header consolidation.

## Validation and limits

The maintained Event 006 allocator, country API, strict flag-family, FORM-16, and SCN-008 checks remain the required post-merge validation. This handoff is source-layout evidence only. No Hearts of Iron IV executable, save, live formable, evolution timing distribution, or MCP runtime result is claimed.

## Simplifications, omissions, and blockers

None introduced by this merge. Existing Event 006 package, probability, rights, asset, and runtime-evidence holds remain unchanged.
