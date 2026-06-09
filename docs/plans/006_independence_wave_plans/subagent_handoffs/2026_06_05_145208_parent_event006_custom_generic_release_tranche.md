# Event 006 Custom Generic Release Tranche

Timestamp: 2026_06_05_145208 UTC

## Scope

Parent-side gameplay wiring for four high-chaos niche Independence Wave releases requested by the user direction to add more Africa/South America countries that break free through Event 006 and share the generic Independence Wave focus tree.

This tranche does not expand Kuban or Altai.

## Tags Added

- `ASN` - Asante Council
- `KBN` - Kanem-Bornu Authority
- `PLM` - Palmares Council
- `AYM` - Aymara Highland Congress

## Gameplay Behavior

- Registered the four tags in `common/country_tags/chaosx_countries.txt`.
- Added country setup files under `common/countries/`.
- Added history files under `history/countries/` with council-style leaders, basic technologies, politics, and research slots.
- Added high-chaos temporary core seeding in `independence_wave_seed_niche_generic_candidates`.
- Added cleanup in `independence_wave_restore_temporary_package_cores` so unreleased temporary cores are removed after the wave.
- Kept all four releases on the shared Event 006 release setup and `independence_wave_liberation_provisional_tree`.
- Added `independence_wave_restore_niche_generic_release_identity` so niche generic candidates keep ordinary package identity after package scoring and do not auto-promote into city, protectorate, historical-return, local-polity, strange, or formable package lanes.
- Did not add bespoke package overlays, formation decisions, or package-specific focus routes in this tranche.

## Anchor States

- `ASN`: state `274` Ghana/Kumasi.
- `KBN`: state `774` Chad and state `901` Borno.
- `PLM`: state `936` Pernambuco and state `498` Rio Grande do Norte.
- `AYM`: state `947` Tacna-Moquegua, state `951` Arica y Tarapaca, and state `506` Antofagasta.

The release resolver still applies the Event 006 host-survival rule before any release, so these candidates are skipped if no valid weakened host can release them safely.

## Asset Handoff

Flag assets were produced by the bounded asset subagent and committed separately as `95a4a21c Add Event 006 niche country flags`.

Asset handoff:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_144741_event006_niche_country_flag_asset_handoff.md`

The parent reviewed the combined contact sheet:

- `docs/assets/006_independence_wave/flags/event006_niche_country_flags_contact_sheet.png`

The flags are upright and readable in the contact sheet.

## Files Changed By Parent

- `common/country_tags/chaosx_countries.txt`
- `common/countries/Asante Council.txt`
- `common/countries/Kanem-Bornu Authority.txt`
- `common/countries/Palmares Council.txt`
- `common/countries/Aymara Highland Congress.txt`
- `history/countries/ASN - Asante Council.txt`
- `history/countries/KBN - Kanem-Bornu Authority.txt`
- `history/countries/PLM - Palmares Council.txt`
- `history/countries/AYM - Aymara Highland Congress.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `localisation/english/chaosx_countries_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`

## Validation

- Brace balance OK for:
  - `common/country_tags/chaosx_countries.txt`
  - new `common/countries/*.txt` files
  - new `history/countries/*.txt` files
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `events/006_independence_wave.txt`
- No trailing whitespace found in touched parent text files.
- `localisation/english/chaosx_countries_l_english.yml` remains UTF-8 with BOM.
- New leader portrait sprite ids were checked against vanilla `_scientists_portraits.gfx`.
- New flag files exist for base, democratic, communism, fascism, and neutrality variants in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.

## Remaining Gaps

- These are high-chaos generic releases, not bespoke country packages.
- Asante, Kanem-Bornu, Palmares, and Aymara should remain in the ordinary generic lane unless a later accepted design explicitly promotes one of them into a researched package/formable overlay.
- The full Event 006 goal remains incomplete.
