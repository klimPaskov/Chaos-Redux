# Soviet Collapse extended-surface collision rescan — 2026-07-28

This focused rescan covers the current 34 Soviet Collapse carriers only. Random Events Mod Workshop item `3199436992` is excluded by the accepted scope decision, and Cannibalism/Event 014 carriers are outside this tranche. Vanilla, the four sibling local mods, and the installed Workshop roots were checked for aliases, top-level cosmetic blocks, `set_cosmetic_tag` calls, base localisation keys, country-history filename stems, and root/medium/small flag stems.

The five non-Random collisions were retired in the live Chaos Redux namespace:

| Retired carrier | Current carrier | External surface | Source |
| --- | --- | --- | --- |
| `OGB` | `IJX` | Russian base localisation key | Workshop `3291386312`, `localisation/russian/mod_countries_l_russian.yml:17` |
| `RMC` | `IKX` | Alias, cosmetic block, `set_cosmetic_tag`, and root/medium/small flags | Workshop `3365515312` |
| `TSC` | `ILX` | Cosmetic blocks | Workshops `1085252317`, `2076426030`, `2797023884`, `3165065717`, `3473395369` |
| `APX` | `INX` | Base localisation key | Workshop `2815832636`, `localisation/english/RF_France_l_english.yml:549` |
| `MRC` | `IMX` | Root and medium flags | Workshop `2227081070` |

The seven original Soviet legacy migrations remain `ALA→AAX`, `ALN→ABX`, `BAC→ADX`, `BSC→AEX`, `KHW→ANX`, `KRS→AOX`, and `KZR→INX`. The intermediate `APX` carrier is also mapped to `INX` so stale pre-migration references cannot resurrect the collision.

The focused direct-definition audit is `.tools/audit_chaosx_country_tags.py`. Its 2026-07-28 run reports 102 Event 006 tags plus 34 Soviet carriers, zero external country-definition collisions, and one skipped Random Events root. The current live namespace has no remaining non-Random extended collision among those 34 Soviet carriers.

This handoff does not claim live game, save/load, or runtime event evidence. It records the installed-source collision gate and the synchronized tag/asset/reference migration only.
