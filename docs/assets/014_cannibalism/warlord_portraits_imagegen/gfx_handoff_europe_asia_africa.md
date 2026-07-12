# Event 014 Europe/Asia/Africa Warlord Portrait GFX Handoff

## Runtime delivery

The 24 final DDS files are installed under
`gfx/leaders/014_cannibalism/` using the filenames already referenced by
`interface/014_cannibalism.gfx`:

- Europe: `leader_CBA_warlord.dds` through `leader_CBH_warlord.dds`
- Asia: `leader_CBA_warlord_asia.dds` through
  `leader_CBH_warlord_asia.dds`
- Africa: `leader_CBA_warlord_africa.dds` through
  `leader_CBH_warlord_africa.dds`

No `.gfx` change is needed. Europe keeps both its unsuffixed and explicit
`_europe` sprite aliases pointed at the same unsuffixed texture. Asia and Africa
use their explicit regional registrations.

## Integration review

Before merge, the parent should retain the existing registrations at
`interface/014_cannibalism.gfx:118-177` and merge only the final combined
manifest/contact-sheet surfaces from all regional tranches. No filename in this
handoff overlaps the Middle East, North America, South America, or Oceania
runtime paths.

## Validation evidence

- `europe_asia_africa_manifest.md`
- `europe_asia_africa_hashes.sha256`
- `notes/europe_asia_africa_validation.md`
- `notes/europe_asia_africa_validation.json`
- `contact_sheets/warlord_europe_asia_africa_dds_decoded_contact.png`
