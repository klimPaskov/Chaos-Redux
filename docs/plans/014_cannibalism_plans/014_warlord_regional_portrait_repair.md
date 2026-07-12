# Event 014 Regional Warlord Portrait Repair

Status: implementation wiring complete, all 56 replacement assets pending production and validation.

## Finding

The original eight CBA-CBH portraits were fixed to origin slots while names were selected from the actual spawn state's regional pool. Visual review found that the portraits read as European, so a non-European state could receive a regional name paired with the wrong face. A second visual review rejected all eight originals because they looked too calm, posed, and conventionally human for Event 014. Both findings violate the source specification: portrait, male name pool, state origin, and feral route identity must agree.

## Accepted implementation

- Keep CBA-CBH as the eight reusable country slots and keep their four origin pairs.
- Replace the existing eight portraits with independently generated Europe variants; none of the original calm portraits may remain active.
- Add six independently generated regional variants for every slot: Asia, Africa, Middle East, North America, South America, and Oceania.
- Select the portrait through the exact stored `cannibalism_warlord_region` and `cannibalism_warlord_slot_index`.
- Reject states outside the seven supported HOI4 continent scopes before warlord formation. There is no generic portrait fallback.
- Carry the stored region through unification so a submitted warlord retains the same face and name as a CBL corps commander.
- Every replacement portrait must be a distinct generated fictional bald male, visibly bloodied, in invented rough clothing plus scavenged 1930s-1940s gear. Each must read as feral, crazed, predatory, and less conventionally human through posture, expression, asymmetry, scars, pallor, bloodshot eyes, damaged teeth, or similarly grounded human-origin traits. At least one portrait must hold a skull and lick blood from it; the remaining portraits need different aggressive behaviors and props rather than repeating that composition. Regional appearance may be represented, but clothing must not copy living ceremonial, sacred, tribal, Indigenous, African, or Pacific regalia.
- No portrait may resemble Hannibal Lecter or use an actor likeness.

## Frozen 56-asset ledger

The European runtime paths remain `leader_<SLOT>_warlord.dds` and are aliased by the `GFX_portrait_<SLOT>_warlord_europe` sprites, but their image content must be replaced.

| Slot | Origin | Region | Source PNG | Processed PNG | Runtime DDS | Sprite | Origin cue |
|---|---|---|---|---|---|---|---|
| CBA | Island Host | Europe | `leader_CBA_warlord_source.png` | `leader_CBA_warlord.png` | `gfx/leaders/014_cannibalism/leader_CBA_warlord.dds` | `GFX_portrait_CBA_warlord_europe` | night pier and rope harness |
| CBB | Island Host | Europe | `leader_CBB_warlord_source.png` | `leader_CBB_warlord.png` | `gfx/leaders/014_cannibalism/leader_CBB_warlord.dds` | `GFX_portrait_CBB_warlord_europe` | breakwater and sailcloth armor |
| CBC | Siege Commune | Europe | `leader_CBC_warlord_source.png` | `leader_CBC_warlord.png` | `gfx/leaders/014_cannibalism/leader_CBC_warlord.dds` | `GFX_portrait_CBC_warlord_europe` | brick breach and field wire |
| CBD | Siege Commune | Europe | `leader_CBD_warlord_source.png` | `leader_CBD_warlord.png` | `gfx/leaders/014_cannibalism/leader_CBD_warlord.dds` | `GFX_portrait_CBD_warlord_europe` | concrete workshop and engineering plate |
| CBE | March Host | Europe | `leader_CBE_warlord_source.png` | `leader_CBE_warlord.png` | `gfx/leaders/014_cannibalism/leader_CBE_warlord.dds` | `GFX_portrait_CBE_warlord_europe` | road column and cavalry webbing |
| CBF | March Host | Europe | `leader_CBF_warlord_source.png` | `leader_CBF_warlord.png` | `gfx/leaders/014_cannibalism/leader_CBF_warlord.dds` | `GFX_portrait_CBF_warlord_europe` | motor column and tyre-chain gear |
| CBG | Prison Host | Europe | `leader_CBG_warlord_source.png` | `leader_CBG_warlord.png` | `gfx/leaders/014_cannibalism/leader_CBG_warlord.dds` | `GFX_portrait_CBG_warlord_europe` | broken keys and barred corridor |
| CBH | Prison Host | Europe | `leader_CBH_warlord_source.png` | `leader_CBH_warlord.png` | `gfx/leaders/014_cannibalism/leader_CBH_warlord.dds` | `GFX_portrait_CBH_warlord_europe` | intake room and stripped prison cloth |
| CBA | Island Host | Asia | `leader_CBA_warlord_asia_source.png` | `leader_CBA_warlord_asia.png` | `gfx/leaders/014_cannibalism/leader_CBA_warlord_asia.dds` | `GFX_portrait_CBA_warlord_asia` | night pier and rope harness |
| CBA | Island Host | Africa | `leader_CBA_warlord_africa_source.png` | `leader_CBA_warlord_africa.png` | `gfx/leaders/014_cannibalism/leader_CBA_warlord_africa.dds` | `GFX_portrait_CBA_warlord_africa` | night pier and rope harness |
| CBA | Island Host | Middle East | `leader_CBA_warlord_middle_east_source.png` | `leader_CBA_warlord_middle_east.png` | `gfx/leaders/014_cannibalism/leader_CBA_warlord_middle_east.dds` | `GFX_portrait_CBA_warlord_middle_east` | night pier and rope harness |
| CBA | Island Host | North America | `leader_CBA_warlord_north_america_source.png` | `leader_CBA_warlord_north_america.png` | `gfx/leaders/014_cannibalism/leader_CBA_warlord_north_america.dds` | `GFX_portrait_CBA_warlord_north_america` | night pier and rope harness |
| CBA | Island Host | South America | `leader_CBA_warlord_south_america_source.png` | `leader_CBA_warlord_south_america.png` | `gfx/leaders/014_cannibalism/leader_CBA_warlord_south_america.dds` | `GFX_portrait_CBA_warlord_south_america` | night pier and rope harness |
| CBA | Island Host | Oceania | `leader_CBA_warlord_oceania_source.png` | `leader_CBA_warlord_oceania.png` | `gfx/leaders/014_cannibalism/leader_CBA_warlord_oceania.dds` | `GFX_portrait_CBA_warlord_oceania` | night pier and rope harness |
| CBB | Island Host | Asia | `leader_CBB_warlord_asia_source.png` | `leader_CBB_warlord_asia.png` | `gfx/leaders/014_cannibalism/leader_CBB_warlord_asia.dds` | `GFX_portrait_CBB_warlord_asia` | breakwater and sailcloth armor |
| CBB | Island Host | Africa | `leader_CBB_warlord_africa_source.png` | `leader_CBB_warlord_africa.png` | `gfx/leaders/014_cannibalism/leader_CBB_warlord_africa.dds` | `GFX_portrait_CBB_warlord_africa` | breakwater and sailcloth armor |
| CBB | Island Host | Middle East | `leader_CBB_warlord_middle_east_source.png` | `leader_CBB_warlord_middle_east.png` | `gfx/leaders/014_cannibalism/leader_CBB_warlord_middle_east.dds` | `GFX_portrait_CBB_warlord_middle_east` | breakwater and sailcloth armor |
| CBB | Island Host | North America | `leader_CBB_warlord_north_america_source.png` | `leader_CBB_warlord_north_america.png` | `gfx/leaders/014_cannibalism/leader_CBB_warlord_north_america.dds` | `GFX_portrait_CBB_warlord_north_america` | breakwater and sailcloth armor |
| CBB | Island Host | South America | `leader_CBB_warlord_south_america_source.png` | `leader_CBB_warlord_south_america.png` | `gfx/leaders/014_cannibalism/leader_CBB_warlord_south_america.dds` | `GFX_portrait_CBB_warlord_south_america` | breakwater and sailcloth armor |
| CBB | Island Host | Oceania | `leader_CBB_warlord_oceania_source.png` | `leader_CBB_warlord_oceania.png` | `gfx/leaders/014_cannibalism/leader_CBB_warlord_oceania.dds` | `GFX_portrait_CBB_warlord_oceania` | breakwater and sailcloth armor |
| CBC | Siege Commune | Asia | `leader_CBC_warlord_asia_source.png` | `leader_CBC_warlord_asia.png` | `gfx/leaders/014_cannibalism/leader_CBC_warlord_asia.dds` | `GFX_portrait_CBC_warlord_asia` | brick breach and field wire |
| CBC | Siege Commune | Africa | `leader_CBC_warlord_africa_source.png` | `leader_CBC_warlord_africa.png` | `gfx/leaders/014_cannibalism/leader_CBC_warlord_africa.dds` | `GFX_portrait_CBC_warlord_africa` | brick breach and field wire |
| CBC | Siege Commune | Middle East | `leader_CBC_warlord_middle_east_source.png` | `leader_CBC_warlord_middle_east.png` | `gfx/leaders/014_cannibalism/leader_CBC_warlord_middle_east.dds` | `GFX_portrait_CBC_warlord_middle_east` | brick breach and field wire |
| CBC | Siege Commune | North America | `leader_CBC_warlord_north_america_source.png` | `leader_CBC_warlord_north_america.png` | `gfx/leaders/014_cannibalism/leader_CBC_warlord_north_america.dds` | `GFX_portrait_CBC_warlord_north_america` | brick breach and field wire |
| CBC | Siege Commune | South America | `leader_CBC_warlord_south_america_source.png` | `leader_CBC_warlord_south_america.png` | `gfx/leaders/014_cannibalism/leader_CBC_warlord_south_america.dds` | `GFX_portrait_CBC_warlord_south_america` | brick breach and field wire |
| CBC | Siege Commune | Oceania | `leader_CBC_warlord_oceania_source.png` | `leader_CBC_warlord_oceania.png` | `gfx/leaders/014_cannibalism/leader_CBC_warlord_oceania.dds` | `GFX_portrait_CBC_warlord_oceania` | brick breach and field wire |
| CBD | Siege Commune | Asia | `leader_CBD_warlord_asia_source.png` | `leader_CBD_warlord_asia.png` | `gfx/leaders/014_cannibalism/leader_CBD_warlord_asia.dds` | `GFX_portrait_CBD_warlord_asia` | concrete workshop and engineering plate |
| CBD | Siege Commune | Africa | `leader_CBD_warlord_africa_source.png` | `leader_CBD_warlord_africa.png` | `gfx/leaders/014_cannibalism/leader_CBD_warlord_africa.dds` | `GFX_portrait_CBD_warlord_africa` | concrete workshop and engineering plate |
| CBD | Siege Commune | Middle East | `leader_CBD_warlord_middle_east_source.png` | `leader_CBD_warlord_middle_east.png` | `gfx/leaders/014_cannibalism/leader_CBD_warlord_middle_east.dds` | `GFX_portrait_CBD_warlord_middle_east` | concrete workshop and engineering plate |
| CBD | Siege Commune | North America | `leader_CBD_warlord_north_america_source.png` | `leader_CBD_warlord_north_america.png` | `gfx/leaders/014_cannibalism/leader_CBD_warlord_north_america.dds` | `GFX_portrait_CBD_warlord_north_america` | concrete workshop and engineering plate |
| CBD | Siege Commune | South America | `leader_CBD_warlord_south_america_source.png` | `leader_CBD_warlord_south_america.png` | `gfx/leaders/014_cannibalism/leader_CBD_warlord_south_america.dds` | `GFX_portrait_CBD_warlord_south_america` | concrete workshop and engineering plate |
| CBD | Siege Commune | Oceania | `leader_CBD_warlord_oceania_source.png` | `leader_CBD_warlord_oceania.png` | `gfx/leaders/014_cannibalism/leader_CBD_warlord_oceania.dds` | `GFX_portrait_CBD_warlord_oceania` | concrete workshop and engineering plate |
| CBE | March Host | Asia | `leader_CBE_warlord_asia_source.png` | `leader_CBE_warlord_asia.png` | `gfx/leaders/014_cannibalism/leader_CBE_warlord_asia.dds` | `GFX_portrait_CBE_warlord_asia` | road column and cavalry webbing |
| CBE | March Host | Africa | `leader_CBE_warlord_africa_source.png` | `leader_CBE_warlord_africa.png` | `gfx/leaders/014_cannibalism/leader_CBE_warlord_africa.dds` | `GFX_portrait_CBE_warlord_africa` | road column and cavalry webbing |
| CBE | March Host | Middle East | `leader_CBE_warlord_middle_east_source.png` | `leader_CBE_warlord_middle_east.png` | `gfx/leaders/014_cannibalism/leader_CBE_warlord_middle_east.dds` | `GFX_portrait_CBE_warlord_middle_east` | road column and cavalry webbing |
| CBE | March Host | North America | `leader_CBE_warlord_north_america_source.png` | `leader_CBE_warlord_north_america.png` | `gfx/leaders/014_cannibalism/leader_CBE_warlord_north_america.dds` | `GFX_portrait_CBE_warlord_north_america` | road column and cavalry webbing |
| CBE | March Host | South America | `leader_CBE_warlord_south_america_source.png` | `leader_CBE_warlord_south_america.png` | `gfx/leaders/014_cannibalism/leader_CBE_warlord_south_america.dds` | `GFX_portrait_CBE_warlord_south_america` | road column and cavalry webbing |
| CBE | March Host | Oceania | `leader_CBE_warlord_oceania_source.png` | `leader_CBE_warlord_oceania.png` | `gfx/leaders/014_cannibalism/leader_CBE_warlord_oceania.dds` | `GFX_portrait_CBE_warlord_oceania` | road column and cavalry webbing |
| CBF | March Host | Asia | `leader_CBF_warlord_asia_source.png` | `leader_CBF_warlord_asia.png` | `gfx/leaders/014_cannibalism/leader_CBF_warlord_asia.dds` | `GFX_portrait_CBF_warlord_asia` | motor column and tyre-chain gear |
| CBF | March Host | Africa | `leader_CBF_warlord_africa_source.png` | `leader_CBF_warlord_africa.png` | `gfx/leaders/014_cannibalism/leader_CBF_warlord_africa.dds` | `GFX_portrait_CBF_warlord_africa` | motor column and tyre-chain gear |
| CBF | March Host | Middle East | `leader_CBF_warlord_middle_east_source.png` | `leader_CBF_warlord_middle_east.png` | `gfx/leaders/014_cannibalism/leader_CBF_warlord_middle_east.dds` | `GFX_portrait_CBF_warlord_middle_east` | motor column and tyre-chain gear |
| CBF | March Host | North America | `leader_CBF_warlord_north_america_source.png` | `leader_CBF_warlord_north_america.png` | `gfx/leaders/014_cannibalism/leader_CBF_warlord_north_america.dds` | `GFX_portrait_CBF_warlord_north_america` | motor column and tyre-chain gear |
| CBF | March Host | South America | `leader_CBF_warlord_south_america_source.png` | `leader_CBF_warlord_south_america.png` | `gfx/leaders/014_cannibalism/leader_CBF_warlord_south_america.dds` | `GFX_portrait_CBF_warlord_south_america` | motor column and tyre-chain gear |
| CBF | March Host | Oceania | `leader_CBF_warlord_oceania_source.png` | `leader_CBF_warlord_oceania.png` | `gfx/leaders/014_cannibalism/leader_CBF_warlord_oceania.dds` | `GFX_portrait_CBF_warlord_oceania` | motor column and tyre-chain gear |
| CBG | Prison Host | Asia | `leader_CBG_warlord_asia_source.png` | `leader_CBG_warlord_asia.png` | `gfx/leaders/014_cannibalism/leader_CBG_warlord_asia.dds` | `GFX_portrait_CBG_warlord_asia` | broken keys and barred corridor |
| CBG | Prison Host | Africa | `leader_CBG_warlord_africa_source.png` | `leader_CBG_warlord_africa.png` | `gfx/leaders/014_cannibalism/leader_CBG_warlord_africa.dds` | `GFX_portrait_CBG_warlord_africa` | broken keys and barred corridor |
| CBG | Prison Host | Middle East | `leader_CBG_warlord_middle_east_source.png` | `leader_CBG_warlord_middle_east.png` | `gfx/leaders/014_cannibalism/leader_CBG_warlord_middle_east.dds` | `GFX_portrait_CBG_warlord_middle_east` | broken keys and barred corridor |
| CBG | Prison Host | North America | `leader_CBG_warlord_north_america_source.png` | `leader_CBG_warlord_north_america.png` | `gfx/leaders/014_cannibalism/leader_CBG_warlord_north_america.dds` | `GFX_portrait_CBG_warlord_north_america` | broken keys and barred corridor |
| CBG | Prison Host | South America | `leader_CBG_warlord_south_america_source.png` | `leader_CBG_warlord_south_america.png` | `gfx/leaders/014_cannibalism/leader_CBG_warlord_south_america.dds` | `GFX_portrait_CBG_warlord_south_america` | broken keys and barred corridor |
| CBG | Prison Host | Oceania | `leader_CBG_warlord_oceania_source.png` | `leader_CBG_warlord_oceania.png` | `gfx/leaders/014_cannibalism/leader_CBG_warlord_oceania.dds` | `GFX_portrait_CBG_warlord_oceania` | broken keys and barred corridor |
| CBH | Prison Host | Asia | `leader_CBH_warlord_asia_source.png` | `leader_CBH_warlord_asia.png` | `gfx/leaders/014_cannibalism/leader_CBH_warlord_asia.dds` | `GFX_portrait_CBH_warlord_asia` | intake room and stripped prison cloth |
| CBH | Prison Host | Africa | `leader_CBH_warlord_africa_source.png` | `leader_CBH_warlord_africa.png` | `gfx/leaders/014_cannibalism/leader_CBH_warlord_africa.dds` | `GFX_portrait_CBH_warlord_africa` | intake room and stripped prison cloth |
| CBH | Prison Host | Middle East | `leader_CBH_warlord_middle_east_source.png` | `leader_CBH_warlord_middle_east.png` | `gfx/leaders/014_cannibalism/leader_CBH_warlord_middle_east.dds` | `GFX_portrait_CBH_warlord_middle_east` | intake room and stripped prison cloth |
| CBH | Prison Host | North America | `leader_CBH_warlord_north_america_source.png` | `leader_CBH_warlord_north_america.png` | `gfx/leaders/014_cannibalism/leader_CBH_warlord_north_america.dds` | `GFX_portrait_CBH_warlord_north_america` | intake room and stripped prison cloth |
| CBH | Prison Host | South America | `leader_CBH_warlord_south_america_source.png` | `leader_CBH_warlord_south_america.png` | `gfx/leaders/014_cannibalism/leader_CBH_warlord_south_america.dds` | `GFX_portrait_CBH_warlord_south_america` | intake room and stripped prison cloth |
| CBH | Prison Host | Oceania | `leader_CBH_warlord_oceania_source.png` | `leader_CBH_warlord_oceania.png` | `gfx/leaders/014_cannibalism/leader_CBH_warlord_oceania.dds` | `GFX_portrait_CBH_warlord_oceania` | intake room and stripped prison cloth |

## Required package proof

- 56 distinct generated source PNGs.
- 56 exact-size 156 by 210 processed RGBA PNGs.
- 56 uncompressed one-mip 32-bit BGRA DDS files at the frozen runtime paths.
- Source, processed, actual-size, and DDS-decoded contact sheets grouped by region and slot.
- Prompt ledger, generation-attempt notes, crop ledger, SHA-256 ledger, manifest, validation report, and GFX handoff.
- Pixel-decoded comparison proving every DDS matches its processed PNG.
- Manual review confirming 56 distinct faces and compositions, region-name compatibility, origin gear, visible gore, bald male presentation, visibly feral behavior, period compatibility, at least one skull-licking portrait, and the absence of sacred or living-cultural motifs.
- Updated original portrait handoff and manifest must stop claiming that one region-neutral face can represent every origin state.
