# Event 006/Soviet reusable country namespace handoff — 2026-07-28

## Scope

This tranche makes the Event 006 carriers reusable by later Chaos Redux events
and protects the Event 005 Soviet Collapse carriers from real country-tag
collisions. HOI4 country identifiers remain three-character engine tags; the
cross-event API is the `chaosx_country_*` collection namespace, not a literal
long country tag.

The current user scope audits Event 006 and Soviet Collapse only. Cannibalism,
Zombie Outbreak, The Revolution, and other event-only namespaces are not
renamed or used as collision blockers in this pass. The Random Events Mod is
explicitly excluded because its tags are event-only compatibility content.

## Reviewed remap

| Legacy Soviet tag | Current tag | Carrier |
| --- | --- | --- |
| `ALA` | `AAX` | Alash Restoration Authority |
| `ALN` | `ABX` | Alan Pass Principality |
| `BAC` | `ADX` | Birobidzhan Autonomous Commune |
| `BSC` | `AEX` | Basmachi Confederation |
| `KHW` | `ANX` | Khwarazmian Oasis Authority |
| `KRS` | `AOX` | Kronstadt Free Soviet |
| `KZR` | `INX` | Khazar Toll Khaganate |
| `OGB` | `IJX` | Old Great Bulgaria |
| `RMC` | `IKX` | Red Martyrs Resurrection Cult |
| `TSC` | `ILX` | Tunguska Star Committee |
| `APX` | `INX` | Khazar Toll Khaganate (intermediate carrier id) |
| `MRC` | `IMX` | Mountain Republic of the Caucasus |

The replacement tags are used consistently in `common/country_tags`, history
filenames, country setup, Soviet Collapse gameplay/localisation, unit history,
leader/flag filenames, interface paths, and documentation. The old tags are
absent from live Chaos Redux references except for reviewed migration tables.

## API surfaces

- `common/script_constants/chaosx_country_registry_constants.txt` owns the
  all-mod, Soviet, and Africa lookup arrays.
- `common/collections/chaosx_country_collections.txt` exposes
  `chaosx_country_all`, Event 006 owned/registered/all views, African overlap
  and regional views, `chaosx_country_soviet_collapse`, and 14 Event 006
  region aliases.
- `docs/systems/006_independence_wave_country_registry.md` documents the
  collection contract, provenance boundary, Africa use, and collision policy.

Collections are active scope views. A consuming event must still prove its own
origin, package identity, anchor/state reservation, map binding, and content
readiness before loading its own setup or focus overlay.

## Collision evidence

`.tools/audit_chaosx_country_tags.py --write-report` scans actual engine
country definitions under `common/country_tags` in vanilla, sibling local
mods, and Workshop mods. The 2026-07-28 run covered 102 Event 006 tags plus 34
Soviet Collapse tags, skipped one Random Events Mod root by policy, and found
zero external country-definition collisions. A companion scoped rescan covered
aliases, cosmetic blocks, `set_cosmetic_tag` calls, localisation keys, history
filenames, and flag stems; it found and retired the five non-Random Soviet
surface collisions (`OGB`, `RMC`, `TSC`, `APX`, `MRC`). The report is
`tag_audit/006_chaosx_country_tag_collision_audit.md`.

## Validation and remaining scope

The static registry arrays match all 165 country definitions currently declared
by Chaos Redux. Event 006 allocator validation remains the existing source of
truth for package readiness and still fail-closes the 14/20 upper automatic
bands when a sufficient set of attested packages is unavailable. This handoff
does not claim live game, save/load, or runtime collection evidence.
