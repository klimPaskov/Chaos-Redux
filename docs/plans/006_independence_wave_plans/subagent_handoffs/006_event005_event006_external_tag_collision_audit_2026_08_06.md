# Event 005 / Event 006 external tag-collision audit

Audit date: 2026-08-06.

Scope: the Event 005 Soviet Collapse tags and Event 006 Independence Wave tags only. The unrelated base Chaos Redux tags (`ZZZ`, `ZIN`, `REV`, and `DTH`) are outside this audit, as requested. The Random Events Mod is explicitly excluded from the collision decision.

## Result

The audit found **no external country-tag definition or country-history filename collision** for the 34 Event 005 Soviet Collapse tags or the 102 Event 006 Independence Wave tags across the installed vanilla directory, 122 Workshop directories, and sibling local mods other than Chaos Redux.

The scan checked 136 target tags. It inspected literal three-character definitions under `common/country_tags/` and three-character prefixes in `history/countries` filenames. It skipped the Chaos Redux repository itself when deciding external collisions and skipped the configured Random Events Mod directory (`3199436992`, `Random Events Mod`) per scope.

## Excluded non-target hits

The only external hits in the combined raw scan were the unrelated base tags `ZZZ`, `ZIN`, and `REV`:

- `ZZZ` appears in Workshop 1827273767 (Novum Vexillum) and 2438003901 (The New Order: Last Days of Europe).
- `ZZZ`, `ZIN`, and `REV` appear in Workshop 3199436992 (Random Events Mod), which is explicitly excluded from this decision.

None of these tags belongs to Event 005 Soviet Collapse or Event 006 Independence Wave, so they do not change the 136-tag result.

## Event 006 internal reservation note

The broader Event 006 installed audit records 17 apparent collisions for `DJX`, `DMX`, `DNX`, `ENX`, `EXX`, `EYX`, `FPX`, `GDX`, `GGX`, `GHX`, `GLX`, `HHX`, `HMX`, `HQX`, `HTX`, `HWX`, and `HXX`. Every one is a same-repository `history/countries/<TAG> - Unresearched Reservation.txt` filename under the Chaos Redux root, not another mod. Those rows remain package-research and admission blockers where their research disposition says so, but they are not external-mod collisions and no rename is justified by this audit.

## Evidence and limitations

- Event 005 source: `common/country_tags/chaosx_countries.txt`, excluding the four unrelated base tags, 34 tags.
- Event 006 source: `common/country_tags/006_independence_wave_countries.txt`, 102 tags.
- Vanilla root: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`.
- Workshop root: `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360`.
- Sibling local-mod root: the parent `mod` directory, excluding the Chaos Redux root and the explicitly excluded Random Events Mod.
- The scan is literal-source evidence for country tags and history filenames. Dynamically constructed tags, binary archives, and non-standard generated history names require a separate review before any new tag is admitted.

No gameplay, tag, history, localisation, asset, or registry file was changed by this audit. No tag remap is required by the Event 005/Event 006 external-collision result.
