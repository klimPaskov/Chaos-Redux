# Event 013 physical-geography data handoff

Date: 2026-07-11
Mode: read-only geography and data audit
Implementation owner: parent agent
Gameplay, localisation, assets, spreadsheets, and source specifications edited by this subagent: none

## Verdict

Event 013 needs a fail-closed physical-geography registry. The current hard predicates use resources, infrastructure, agriculture, coastal status, and prior disaster history as substitutes for physical geography. Those values are useful scores, but they cannot prove that a state contains a volcanic vent, a steep slope, cyclone exposure, a heat-capable climate, or a tsunami receptor.

This handoff supplies exact state and strategic-region identifiers for the vanilla 1.19.2 map currently installed. It deliberately prefers a reviewed false negative over a fabricated physical location. The central invariants are:

- a non-volcanic state never passes volcanic eruption, lahar, or massive eruption;
- every Siberian, arctic, or other reviewed cold region fails heat wave;
- coast alone never proves cyclone, tsunami, or storm surge;
- flat terrain never proves dry or wet mass movement;
- ashfall and tsunami require a validated physical origin, not only a permissive receptor state;
- every corridor segment is an adjacent state in the same physical domain.

The identifiers below are map data, not tuning constants. Put the trigger definitions in `common/scripted_triggers/013_natural_disasters_geography_triggers.txt`. Do not turn the lists into startup flags and do not add a periodic world scan.

## Sources and method

### Repository and engine references

Consulted before this audit:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- all Event 013 source specifications relevant to target resolution and the 25 family playbooks
- the live Event 013 scripted triggers and effects
- offline wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, State modding, and Map modding
- vanilla `documentation/triggers_documentation.md`, `documentation/effects_documentation.md`, and `documentation/script_concept_documentation.md`
- vanilla `history/states`, `map/strategicregions`, `map/definition.csv`, `map/provinces.bmp`, and `common/terrain/00_terrain.txt`

The vanilla trigger documentation confirms that `region = <id>` is valid in state scope and tests the current state's strategic region. It also documents `has_terrain` as a country-scope trigger. Therefore a state terrain classifier must use reviewed `state = <id>` data, not a country-scope `has_terrain` test.

### Smithsonian volcano authority

Primary volcano sources:

- [Smithsonian GVP web services](https://volcano.si.edu/database/webservices.cfm)
- [official Holocene volcano list](https://volcano.si.edu/volcanolist_holocene.cfm)
- [official country list](https://volcano.si.edu/volcanolist_countries.cfm)
- [official region list](https://volcano.si.edu/volcanolist_regions.cfm)
- [official Holocene Volcano WFS GeoJSON](https://webservices.volcano.si.edu/geoserver/GVP-VOTW/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=GVP-VOTW%3ASmithsonian_VOTW_Holocene_Volcanoes&outputFormat=application%2Fjson)
- [Volcanoes of the World DOI](https://doi.org/10.5479/si.GVP.VOTW5-2025.5.3)

The WFS returned 1,196 georeferenced features during the audit. The public list reported 1,215 volcanoes. The registry uses WFS records with positive elevation, excludes Antarctica because vanilla has no playable Antarctic land state, and excludes negative-elevation submarine vents. Representative profile checks include [Etna 211060](https://volcano.si.edu/volcano.cfm?vn=211060), [West Eifel Volcanic Field 210010](https://volcano.si.edu/volcano.cfm?vn=210010), [Popa 275080](https://volcano.si.edu/volcano.cfm?vn=275080), [Jombolok 302060](https://volcano.si.edu/volcano.cfm?vn=302060), [Udokan Plateau 302030](https://volcano.si.edu/volcano.cfm?vn=302030), [Halla 306040](https://volcano.si.edu/volcano.cfm?vn=306040), [Abu 283001](https://volcano.si.edu/volcano.cfm?vn=283001), and [Sanbesan 283002](https://volcano.si.edu/volcano.cfm?vn=283002).

The official page citation at audit time was Global Volcanism Program, 2025, *Volcanoes of the World*, version 5.3.6 dated 26 May 2026, compiled by Edward Venzke and distributed by the Smithsonian Institution under the DOI above.

WFS coordinates were registered to the vanilla province raster, then boundary-sensitive matches were reviewed against state components and known administrative geography. Terrain lists use the vanilla province terrain tokens and land-pixel area. The terrain thresholds used only to materialize these static lists are:

- slope: hills plus mountain cover at least 25 percent of state land, or at least two hill/mountain provinces and at least 10 percent of state land;
- wildfire fuel: forest plus jungle cover at least 20 percent of state land, or at least two forest/jungle provinces and at least 10 percent of state land;
- floodplain: plains plus marsh cover at least 40 percent of state land, or a coastal state with at least 20 percent plains/marsh;
- tornado anchor: plains cover at least 40 percent, intersected with a reviewed severe-convection strategic region;
- desert terrain: desert covers at least 20 percent of state land.

These thresholds are provenance for the frozen identifier lists. They are not proposed gameplay variables.

## Exact low-level trigger bodies

### Holocene land-volcano vent states

Use this exact state-scope trigger for `volcanic_eruption`. No resource, coast, infrastructure, history flag, or score may bypass it.

```txt
natural_disaster_state_is_volcanic_vent_zone = {
	OR = {
		state = 2 state = 26 state = 42 state = 100 state = 115 state = 117
		state = 164 state = 165 state = 175 state = 178 state = 186 state = 187
		state = 230 state = 231 state = 266 state = 268 state = 271 state = 277
		state = 282 state = 284 state = 286 state = 288 state = 293 state = 297
		state = 302 state = 304 state = 305 state = 306 state = 308 state = 312
		state = 313 state = 314 state = 316 state = 317 state = 327 state = 328
		state = 330 state = 335 state = 339 state = 348 state = 350 state = 376
		state = 377 state = 378 state = 379 state = 380 state = 382 state = 385
		state = 386 state = 387 state = 463 state = 471 state = 473 state = 475
		state = 476 state = 477 state = 478 state = 481 state = 483 state = 484
		state = 485 state = 492 state = 494 state = 506 state = 507 state = 508
		state = 511 state = 512 state = 514 state = 515 state = 517 state = 523
		state = 524 state = 526 state = 528 state = 532 state = 533 state = 534
		state = 535 state = 536 state = 546 state = 547 state = 548 state = 549
		state = 550 state = 551 state = 555 state = 564 state = 565 state = 591
		state = 621 state = 623 state = 624 state = 625 state = 627 state = 628
		state = 629 state = 634 state = 636 state = 637 state = 645 state = 646
		state = 649 state = 659 state = 667 state = 668 state = 672 state = 679
		state = 697 state = 698 state = 702 state = 703 state = 706 state = 708
		state = 713 state = 714 state = 717 state = 720 state = 726 state = 733
		state = 734 state = 737 state = 738 state = 747 state = 767 state = 773
		state = 775 state = 800 state = 827 state = 828 state = 835 state = 837
		state = 842 state = 843 state = 855 state = 856 state = 872 state = 887
		state = 890 state = 903 state = 904 state = 905 state = 908 state = 914
		state = 947 state = 948 state = 949 state = 950 state = 951 state = 952
		state = 953 state = 954 state = 955 state = 960 state = 979 state = 992
		state = 1018 state = 1019 state = 1020 state = 1026 state = 1027
		state = 1031 state = 1042 state = 1048 state = 1049 state = 1050
		state = 1051 state = 1052 state = 1053 state = 1056 state = 1058
		state = 1070 state = 1071 state = 1072 state = 1079
	}
}
```

Representative evidence by map area, all from the official WFS above:

| Map area | State IDs and representative GVP features |
|---|---|
| Europe and Mediterranean | 2 Colli Albani, 26 Chaine des Puys, 42 West Eifel Volcanic Field, 100 Icelandic systems, 115 Etna, 117 Vesuvius/Campi Flegrei, 164 Nisyros, 165 Olot, 175 Calatrava, 178 Canary Islands, 186 Methana, 187 Santorini/Milos |
| Caucasus, Anatolia, Iran | 230 Aragats/Ghegham, 231 Samsari, 266 Damavand, 339 Kula, 348 Erciyes/Hasandag, 350 Karaca Dag, 800 Nemrut/Tendurek/Ararat, 827 Elbrus, 828 Kazbek |
| Mexico and Central America | 277 Toluca/Chichinautzin, 304 Baru, 312 Honduras fields, 313 Guatemala arc, 314 El Salvador arc, 316 Costa Rica arc, 317 Nicaragua arc, 475 Chiapas, 476 Oaxaca, 477 Veracruz, 478 Jalisco, 481 Durango, 483 Pinacate, 484 Baja California fields, 485 Guerrero fields |
| North America | 376 Zuni-Bandera/Carrizozo, 377 San Francisco field, 378 California vents, 379 Lunar Crater, 380 Black Rock Desert, 382 Dotsero, 385 Oregon Cascades/Newberry, 386 Washington Cascades, 387 Craters of the Moon, 463 Alaska/Aleutians, 471 Edziza, 473 Garibaldi |
| Andes and South America | 302 Bolivian Altiplano, 305 Ecuador arc, 306 Colombian arc, 492 Arequipa, 494 Quimsachata, 506 Antofagasta, 507 Magallanes volcanoes, 508 northwest Argentina, 511 Mendoza, 512 northern Patagonia, 947 Tacna-Moquegua, 949 Aysen, 950 Araucania, 951 Arica-Tarapaca, 952 Atacama, 953 Fueguino, 954 Pali-Aike, 955 Chubut fields, 960 San Juan-La Rioja |
| Atlantic and Caribbean islands | 308 Lesser Antilles, 697 Madeira, 698 Azores, 702 Fogo/Brava, 703 Ascension, 706 Piton de la Fournaise, 708 Karthala, 720 South Sandwich component, 948 Rapa Nui |
| Africa, Red Sea, Arabia | 268 Ardoukoba/Djibouti, 271 Ethiopian highlands, 293 Yemen/Red Sea islands, 297 Pico Basile, 514 Atakor/Tahalra, 515 Tibesti, 546 Tanzania systems, 547 and 904 Kenyan Rift, 548 Uganda fields, 549/551/767/887 Sudan-Darfur fields, 550 Eritrea, 659 Yemen, 679/855/856 Arabian harrats, 773 Cameroon, 775 Chad, 835/837/842/843 Ethiopian fields, 890 Virunga, 903 Marsabit, 905 Chyulu, 908 Afar, 992 Aden |
| Northeast Asia and Japan | 282 Kanto/Fuji area, 328 Longgang/Changbaishan area, 526 Io-Torishima, 528 Kyushu systems, 532 Tokai/Fuji, 533/1019 Tohoku, 534 Koshinetsu, 535 Hokuriku, 536 Hokkaido, 555 Kurils, 564 Jombolok, 565 Udokan Plateau, 621 Honggeertu, 637 Kamchatka, 714 Wudalianchi, 717 Changbaishan/Jingbohu area, 1018 southern Kyushu, 1020 Abu/Sanbesan, 1031 Halla |
| South and Southeast Asia | 286 Ly Son, 288 Popa, 327/623/624/625/627/628/1026/1027 Philippine systems, 335/667/668/672/738/1048/1049/1050/1051/1052/1053/1056/1058 Indonesian systems, 523/979 New Guinea, 524 Taiwan, 591 Hainan, 733 Barren Island, 737 Bismarck, 747 Tengchong/Dali, 1042 Ashi-San |
| Pacific and Australasia | 284/1079 North Island New Zealand, 517 Newer Volcanics Province, 629 Hawaii, 634/734/1070 Solomon and Bougainville arcs, 636 Fiji, 645 Ioto, 646 Marianas, 649 Galapagos, 713 Kerguelen, 726/1072 Samoa, 872 McBride Volcanic Province, 1071 Vanuatu |

### Massive-eruption-capable subset

This is deliberately narrower than the vent list. It retains large calderas, major stratovolcanoes, large shield/fissure systems, and major arc complexes. A small Holocene monogenetic field does not pass merely because it is a valid ordinary vent state.

```txt
natural_disaster_state_is_massive_eruption_zone = {
	OR = {
		state = 100 state = 115 state = 117 state = 178 state = 187 state = 266
		state = 277 state = 282 state = 284 state = 302 state = 305 state = 306
		state = 308 state = 313 state = 314 state = 316 state = 317 state = 327
		state = 328 state = 335 state = 348 state = 385 state = 386 state = 463
		state = 471 state = 473 state = 475 state = 477 state = 478 state = 492
		state = 506 state = 507 state = 508 state = 511 state = 512 state = 523
		state = 528 state = 532 state = 533 state = 534 state = 535 state = 536
		state = 546 state = 550 state = 555 state = 623 state = 624 state = 625
		state = 627 state = 628 state = 629 state = 634 state = 637 state = 645
		state = 646 state = 667 state = 668 state = 672 state = 698 state = 706
		state = 708 state = 717 state = 737 state = 747 state = 800 state = 827
		state = 837 state = 890 state = 904 state = 947 state = 949 state = 950
		state = 951 state = 952 state = 979 state = 1018 state = 1019 state = 1020
		state = 1026 state = 1027 state = 1031 state = 1048 state = 1049
		state = 1050 state = 1051 state = 1052 state = 1053 state = 1056
		state = 1058 state = 1070 state = 1071 state = 1079
	}
}
```

High-confidence anchors in this subset include Campi Flegrei and Vesuvius in 117, Santorini in 187, Taupo in 1079, Toba in 1049, Krakatau-area systems in 1058, Aso in 528, Changbaishan in 717/328, Kamchatka in 637, Alaska/Aleutians in 463, the Cascades in 385/386, Ilopango in 314, Taal in 327, and the Andean arcs represented by 492/506/947/949/950/951/952.

### Lahar-capable vent states

Lahar is not the intersection of `wet history` and a resource proxy. It requires a validated vent origin in this reviewed steep, ice-capped, or wet stratovolcano subset. The higher-level resolver must also require the current lahar to originate from the same eruption sequence.

```txt
natural_disaster_state_is_lahar_zone = {
	OR = {
		state = 100 state = 115 state = 117 state = 178 state = 187 state = 230
		state = 266 state = 277 state = 282 state = 284 state = 297 state = 304
		state = 305 state = 306 state = 308 state = 313 state = 314 state = 316
		state = 317 state = 327 state = 328 state = 335 state = 348 state = 385
		state = 386 state = 463 state = 471 state = 473 state = 475 state = 477
		state = 478 state = 492 state = 506 state = 507 state = 508 state = 511
		state = 512 state = 523 state = 524 state = 528 state = 532 state = 533
		state = 534 state = 535 state = 536 state = 546 state = 547 state = 548
		state = 550 state = 555 state = 623 state = 624 state = 625 state = 627
		state = 628 state = 634 state = 636 state = 637 state = 645 state = 646
		state = 667 state = 668 state = 672 state = 697 state = 698 state = 702
		state = 706 state = 708 state = 717 state = 726 state = 737 state = 738
		state = 747 state = 800 state = 827 state = 828 state = 837 state = 890
		state = 904 state = 947 state = 949 state = 950 state = 951 state = 952
		state = 979 state = 1018 state = 1019 state = 1020 state = 1026
		state = 1027 state = 1031 state = 1048 state = 1049 state = 1050
		state = 1051 state = 1052 state = 1053 state = 1056 state = 1058
		state = 1070 state = 1071 state = 1072 state = 1079
	}
}
```

### Volcanic plume receptor domain

Ashfall differs from eruption. A non-volcanic state may receive ash, but only from a validated vent origin. A static plume trigger may identify the broader receptor domain, but it must never authorize a free-standing ashfall call.

Static plume-region domain:

```txt
natural_disaster_state_is_volcanic_plume_zone = {
	OR = {
		region = 7 region = 17 region = 20 region = 23 region = 25 region = 32
		region = 33 region = 34 region = 41 region = 45 region = 47 region = 48
		region = 51 region = 53 region = 61 region = 62 region = 64 region = 76
		region = 83 region = 84 region = 85 region = 87 region = 91 region = 93
		region = 94 region = 101 region = 102 region = 105 region = 109 region = 118
		region = 123 region = 124 region = 127 region = 129 region = 134 region = 145
		region = 152 region = 154 region = 157 region = 158 region = 160 region = 161
		region = 167 region = 178 region = 184 region = 186 region = 187 region = 193
		region = 199 region = 201 region = 202 region = 204 region = 205 region = 210
		region = 216 region = 217 region = 218 region = 219 region = 227 region = 228
		region = 235 region = 236 region = 237 region = 239 region = 242 region = 243
		region = 244 region = 248 region = 249 region = 256 region = 257 region = 273
		region = 274 region = 283 region = 284 region = 287 region = 295 region = 299
		region = 300 region = 302
	}
}
```

Required runtime rule:

1. resolve and save a state that passes `natural_disaster_state_is_volcanic_vent_zone`;
2. ash may strike the origin, an adjacent land state, or a reviewed state in the origin's plume strategic region;
3. preserve the origin event target through the sequence;
4. reject a direct ash call that supplies only an arbitrary receptor and no valid vent origin.

This permits Calabria to receive Etna ash when the sequence explicitly originates in Sicily without falsely classifying Calabria as a vent.

### Cold-wave regions

This list uses the current vanilla winter minima, with false ocean-island artifacts removed and Patagonia, the Southern Andes, Tosando, and South Island added after physical review.

```txt
natural_disaster_state_is_cold_zone = {
	OR = {
		region = 3 region = 5 region = 6 region = 7 region = 8 region = 10
		region = 11 region = 12 region = 13 region = 14 region = 16 region = 21
		region = 22 region = 24 region = 26 region = 27 region = 33 region = 36
		region = 37 region = 38 region = 39 region = 40 region = 45 region = 87
		region = 88 region = 118 region = 120 region = 121 region = 122 region = 129
		region = 130 region = 131 region = 132 region = 133 region = 134 region = 135
		region = 136 region = 137 region = 138 region = 143 region = 144 region = 145
		region = 146 region = 147 region = 148 region = 149 region = 150 region = 151
		region = 152 region = 155 region = 161 region = 162 region = 186 region = 191
		region = 192 region = 197 region = 198 region = 199 region = 200 region = 212
		region = 213 region = 214 region = 219 region = 220 region = 221 region = 222
		region = 233 region = 234 region = 235 region = 242 region = 243 region = 244
		region = 245 region = 250 region = 251 region = 252 region = 255 region = 256
		region = 257 region = 258 region = 259 region = 260 region = 261 region = 262
		region = 263 region = 264 region = 265 region = 266 region = 267 region = 268
		region = 269 region = 270 region = 275 region = 276 region = 277 region = 278
		region = 283 region = 284 region = 289 region = 299 region = 301
	}
}
```

The removed false cold IDs are 47, 51, 57, and 170. Their negative values come from sea weather or old broad-region data, while their represented land is Madeira, the Azores, mid-Atlantic islands, or Florida.

### Blizzard regions

The core is every current vanilla strategic region with a positive `blizzard` probability. New England, the Canadian Maritimes, Patagonia, the Southern Andes, Tosando, and South Island are reviewed physical additions.

```txt
natural_disaster_state_is_blizzard_zone = {
	OR = {
		region = 1 region = 2 region = 3 region = 4 region = 6 region = 7
		region = 8 region = 10 region = 11 region = 12 region = 13 region = 14
		region = 21 region = 22 region = 24 region = 26 region = 27 region = 36
		region = 37 region = 38 region = 39 region = 40 region = 120 region = 121
		region = 122 region = 130 region = 131 region = 132 region = 133 region = 136
		region = 137 region = 138 region = 144 region = 145 region = 146 region = 147
		region = 148 region = 149 region = 150 region = 151 region = 152 region = 155
		region = 161 region = 162 region = 186 region = 191 region = 192 region = 197
		region = 199 region = 200 region = 212 region = 213 region = 220 region = 221
		region = 222 region = 233 region = 234 region = 235 region = 242 region = 243
		region = 250 region = 251 region = 252 region = 255 region = 256 region = 257
		region = 258 region = 259 region = 260 region = 261 region = 262 region = 263
		region = 264 region = 265 region = 266 region = 267 region = 268 region = 269
		region = 270 region = 275 region = 276 region = 277 region = 278 region = 283
		region = 284 region = 289 region = 299 region = 301
	}
}
```

### Heat-wave regions and mandatory cold exclusion

The heat predicate must use a positive allowlist and the cold-zone exclusion. Previous heat history, agriculture, resources, or high population never create heat eligibility.

```txt
natural_disaster_state_is_heat_zone = {
	AND = {
		OR = {
			region = 17 region = 20 region = 23 region = 25 region = 28 region = 29
			region = 31 region = 34 region = 35 region = 41 region = 53 region = 60
			region = 68 region = 69 region = 71 region = 76 region = 78 region = 83
			region = 84 region = 85 region = 91 region = 93 region = 94 region = 95
			region = 97 region = 99 region = 101 region = 102 region = 105 region = 109
			region = 116 region = 117 region = 119 region = 123 region = 124 region = 125
			region = 126 region = 127 region = 128 region = 139 region = 140 region = 141
			region = 142 region = 153 region = 154 region = 156 region = 158 region = 159
			region = 160 region = 163 region = 164 region = 165 region = 167 region = 169
			region = 172 region = 178 region = 179 region = 180 region = 181 region = 182
			region = 183 region = 184 region = 185 region = 187 region = 188 region = 189
			region = 190 region = 193 region = 194 region = 195 region = 196 region = 205
			region = 208 region = 209 region = 210 region = 211 region = 215 region = 216
			region = 218 region = 223 region = 225 region = 226 region = 227 region = 228
			region = 229 region = 230 region = 231 region = 232 region = 236 region = 237
			region = 238 region = 239 region = 240 region = 241 region = 246 region = 247
			region = 248 region = 249 region = 253 region = 254 region = 271 region = 272
			region = 273 region = 274 region = 280 region = 281 region = 282 region = 285
			region = 286 region = 287 region = 288 region = 290 region = 291 region = 292
			region = 293 region = 294 region = 295 region = 296 region = 297 region = 298
			region = 300 region = 303 region = 304
		}
		NOT = { natural_disaster_state_is_cold_zone = yes }
	}
}
```

This explicit `NOT` guarantees that regions 147 through 151 and 255 through 266 cannot receive heat. It also protects the mandatory minimum cold exclusions 138, 147, 148, 149, 150, 151, and 255 through 266. Keep the existing Event 051 overlap exclusion as a separate runtime guard.

### Drought regions

Drought is broader than dust. The list includes arid climates, Mediterranean climates, monsoonal dry-season climates, savanna, the North American interior, Australia, and the southern South American dry belt. It excludes the reviewed polar and continuously cold domains.

```txt
natural_disaster_state_is_drought_zone = {
	OR = {
		region = 17 region = 20 region = 23 region = 25 region = 28 region = 31
		region = 34 region = 35 region = 41 region = 116 region = 119 region = 123
		region = 124 region = 125 region = 126 region = 127 region = 128 region = 129
		region = 135 region = 136 region = 137 region = 139 region = 140 region = 141
		region = 142 region = 144 region = 145 region = 152 region = 153 region = 156
		region = 158 region = 163 region = 164 region = 165 region = 181 region = 182
		region = 183 region = 184 region = 185 region = 187 region = 188 region = 189
		region = 190 region = 193 region = 194 region = 195 region = 196 region = 198
		region = 204 region = 205 region = 210 region = 211 region = 215 region = 216
		region = 218 region = 223 region = 224 region = 225 region = 226 region = 227
		region = 228 region = 229 region = 230 region = 231 region = 232 region = 236
		region = 237 region = 238 region = 239 region = 240 region = 241 region = 244
		region = 245 region = 246 region = 247 region = 248 region = 249 region = 253
		region = 254 region = 267 region = 268 region = 269 region = 270 region = 271
		region = 272 region = 273 region = 274 region = 280 region = 281 region = 282
		region = 283 region = 284 region = 285 region = 286 region = 287 region = 288
		region = 289 region = 290 region = 291 region = 292 region = 293 region = 294
		region = 295 region = 296 region = 297 region = 298 region = 302 region = 303
		region = 304
	}
}
```

Use agriculture, water stress, infrastructure, and prior heat only as scoring or intensity inputs after this physical gate passes.

### Dust and sandstorm regions

The direct core consists of vanilla regions with a positive sandstorm weather probability, except region 134. Region 134 is a Caucasus data anomaly and has no desert provinces. The secondary group has reviewed desert terrain and must also pass the exact desert-state trigger in the terrain appendix.

```txt
natural_disaster_state_is_arid_zone = {
	OR = {
		OR = {
			region = 28 region = 126 region = 127 region = 128 region = 162
			region = 182 region = 183 region = 195 region = 196 region = 216
			region = 225 region = 232 region = 236 region = 237 region = 238
			region = 254 region = 289
		}
		AND = {
			OR = {
				region = 35 region = 116 region = 136 region = 137 region = 139
				region = 144 region = 145 region = 146 region = 152 region = 200
				region = 204 region = 215 region = 219 region = 226 region = 240
				region = 241 region = 244 region = 245 region = 250 region = 252
				region = 267 region = 268 region = 269 region = 270 region = 273
				region = 274 region = 283 region = 296 region = 297
			}
			natural_disaster_state_is_desert_terrain_zone = yes
		}
	}
}
```

### Seismic exposure

This is a reviewed high and moderate exposure domain. It covers the Ring of Fire, Alpine-Himalayan belt, East African Rift and Red Sea, Iceland/Azores, Caribbean/Central America, New Madrid/Charleston, Basin and Range, New Zealand, and the Andes. Any exact vent state also passes, which closes small volcanic-field gaps without allowing every land state.

```txt
natural_disaster_state_is_seismic_zone = {
	OR = {
		natural_disaster_state_is_volcanic_vent_zone = yes
		OR = {
			region = 17 region = 21 region = 23 region = 25 region = 33 region = 34
			region = 35 region = 41 region = 45 region = 51 region = 53 region = 76
			region = 83 region = 84 region = 87 region = 93 region = 94 region = 95
			region = 97 region = 105 region = 109 region = 116 region = 117 region = 118
			region = 119 region = 120 region = 123 region = 124 region = 129 region = 134
			region = 135 region = 143 region = 144 region = 145 region = 146 region = 154
			region = 157 region = 158 region = 160 region = 161 region = 162 region = 165
			region = 167 region = 178 region = 186 region = 187 region = 198 region = 199
			region = 200 region = 201 region = 202 region = 204 region = 205 region = 217
			region = 218 region = 219 region = 227 region = 235 region = 239 region = 240
			region = 241 region = 244 region = 245 region = 246 region = 247 region = 249
			region = 250 region = 251 region = 252 region = 257 region = 273 region = 274
			region = 283 region = 284 region = 289 region = 292 region = 295 region = 297
			region = 298 region = 299 region = 300 region = 301
		}
	}
}
```

### Tropical cyclone basins

Define basin subtriggers so path continuation and surge can preserve the resolved basin. A cyclone target must also satisfy `is_coastal = yes`. A state cannot pass from coast alone.

```txt
natural_disaster_state_is_north_atlantic_cyclone_basin = {
	OR = {
		region = 34 region = 53 region = 117 region = 124 region = 170
		region = 197 region = 205 region = 211 region = 213
	}
}

natural_disaster_state_is_northeast_pacific_cyclone_basin = {
	OR = {
		region = 34 region = 105 region = 106 region = 107 region = 109
		region = 123 region = 204 region = 205 region = 218
	}
}

natural_disaster_state_is_western_north_pacific_cyclone_basin = {
	OR = {
		region = 76 region = 78 region = 87 region = 90 region = 93 region = 94
		region = 95 region = 96 region = 154 region = 158 region = 159 region = 160
		region = 164 region = 167 region = 177 region = 178 region = 180 region = 186
		region = 228 region = 229 region = 242 region = 243 region = 248 region = 249
		region = 299 region = 300
	}
}

natural_disaster_state_is_north_indian_cyclone_basin = {
	OR = {
		region = 60 region = 71 region = 72 region = 73 region = 75 region = 99
		region = 101 region = 104 region = 141 region = 142 region = 188 region = 189
		region = 190 region = 196 region = 228 region = 230 region = 231 region = 236
		region = 238 region = 290 region = 291 region = 293 region = 294 region = 296
	}
}

natural_disaster_state_is_southwest_indian_cyclone_basin = {
	OR = {
		region = 60 region = 71 region = 74 region = 85 region = 99
		region = 102 region = 103 region = 181 region = 185 region = 223
	}
}

natural_disaster_state_is_australian_south_pacific_cyclone_basin = {
	OR = {
		region = 81 region = 82 region = 83 region = 84 region = 91 region = 92
		region = 93 region = 94 region = 95 region = 97 region = 99 region = 105
		region = 156 region = 158 region = 159 region = 167 region = 172 region = 178
		region = 179 region = 180 region = 193 region = 194 region = 195 region = 302
		region = 303 region = 304
	}
}

natural_disaster_state_is_tropical_storm_basin = {
	OR = {
		natural_disaster_state_is_north_atlantic_cyclone_basin = yes
		natural_disaster_state_is_northeast_pacific_cyclone_basin = yes
		natural_disaster_state_is_western_north_pacific_cyclone_basin = yes
		natural_disaster_state_is_north_indian_cyclone_basin = yes
		natural_disaster_state_is_southwest_indian_cyclone_basin = yes
		natural_disaster_state_is_australian_south_pacific_cyclone_basin = yes
	}
}
```

Target rule:

```txt
AND = {
	is_coastal = yes
	natural_disaster_state_is_tropical_storm_basin = yes
}
```

The western North Pacific list contains cold fringe regions only because tropical systems can recurve into them. Do not reuse that fact as heat eligibility.

Some coarse vanilla states and regions, especially Central America and island groups, legitimately appear in two basin triggers. Resolve one basin at sequence creation, store that basin as sequence data, and never change it during path continuation. Dual membership permits either physically adjacent ocean origin, not a mid-sequence cross-basin switch.

### Tsunami basin and coast rule

Tsunami is origin dependent. There is no physically safe standalone `is_coastal = yes` target. First save a seismic, volcanic, or ocean-impact origin, assign it one of the following basin groups, then select only a coastal receptor in the same group. A direct user call without a compatible saved origin rejects.

```txt
natural_disaster_state_is_pacific_tsunami_basin = {
	OR = {
		region = 33 region = 34 region = 76 region = 78 region = 79 region = 80
		region = 81 region = 82 region = 83 region = 84 region = 86 region = 87
		region = 88 region = 89 region = 90 region = 91 region = 92 region = 93
		region = 94 region = 95 region = 96 region = 97 region = 98 region = 105
		region = 106 region = 107 region = 108 region = 109 region = 110 region = 111
		region = 112 region = 113 region = 114 region = 115 region = 118 region = 123
		region = 124 region = 154 region = 157 region = 158 region = 159 region = 160
		region = 167 region = 171 region = 172 region = 175 region = 176 region = 177
		region = 178 region = 179 region = 180 region = 186 region = 187 region = 193
		region = 194 region = 201 region = 204 region = 218 region = 235 region = 242
		region = 243 region = 248 region = 249 region = 257 region = 280 region = 281
		region = 282 region = 283 region = 284 region = 299 region = 300 region = 301
		region = 302 region = 303 region = 304
	}
}

natural_disaster_state_is_indian_tsunami_basin = {
	OR = {
		region = 31 region = 60 region = 71 region = 72 region = 73 region = 74
		region = 75 region = 81 region = 82 region = 85 region = 86 region = 91
		region = 92 region = 93 region = 99 region = 101 region = 102 region = 103
		region = 104 region = 141 region = 142 region = 156 region = 157 region = 159
		region = 167 region = 181 region = 185 region = 187 region = 188 region = 189
		region = 190 region = 193 region = 194 region = 196 region = 223 region = 228
		region = 229 region = 230 region = 231 region = 236 region = 238 region = 248
		region = 249 region = 271 region = 272 region = 274 region = 290 region = 291
		region = 292 region = 293 region = 294 region = 295 region = 296 region = 302
		region = 303 region = 304
	}
}

natural_disaster_state_is_atlantic_tsunami_basin = {
	OR = {
		region = 1 region = 2 region = 3 region = 4 region = 16 region = 17
		region = 18 region = 19 region = 20 region = 34 region = 35 region = 36
		region = 42 region = 43 region = 44 region = 45 region = 46 region = 47
		region = 48 region = 49 region = 50 region = 51 region = 52 region = 53
		region = 54 region = 55 region = 56 region = 57 region = 58 region = 59
		region = 61 region = 62 region = 63 region = 64 region = 65 region = 66
		region = 67 region = 117 region = 119 region = 124 region = 125 region = 126
		region = 127 region = 128 region = 139 region = 140 region = 158 region = 163
		region = 169 region = 170 region = 171 region = 173 region = 174 region = 181
		region = 182 region = 183 region = 184 region = 185 region = 197 region = 205
		region = 208 region = 209 region = 210 region = 211 region = 212 region = 213
		region = 215 region = 220 region = 223 region = 224 region = 225 region = 226
		region = 227 region = 233 region = 234 region = 235 region = 271 region = 272
		region = 280 region = 281 region = 282 region = 283 region = 284 region = 285
		region = 286 region = 287 region = 288
	}
}

natural_disaster_state_is_mediterranean_tsunami_basin = {
	OR = {
		region = 23 region = 25 region = 29 region = 68 region = 69 region = 129
		region = 134 region = 135 region = 169 region = 202 region = 232
	}
}

natural_disaster_state_is_black_sea_tsunami_basin = {
	OR = {
		region = 26 region = 27 region = 30 region = 130 region = 134 region = 135
	}
}

natural_disaster_state_is_ocean_exposed_coast = {
	AND = {
		is_coastal = yes
		OR = {
			natural_disaster_state_is_pacific_tsunami_basin = yes
			natural_disaster_state_is_indian_tsunami_basin = yes
			natural_disaster_state_is_atlantic_tsunami_basin = yes
			natural_disaster_state_is_mediterranean_tsunami_basin = yes
			natural_disaster_state_is_black_sea_tsunami_basin = yes
		}
	}
}
```

Receptor rule: `is_coastal = yes`, basin equality with the saved origin, and either the origin state itself or a bounded adjacent/same-basin search. Caspian-only coasts do not pass an ocean-origin tsunami.

### Storm-surge coast rule

Storm surge requires coast plus an active cyclone or an extratropical storm-coast domain. Cyclone basin equality must be preserved where the primary family is tropical cyclone.

```txt
natural_disaster_state_is_extratropical_surge_coast = {
	AND = {
		is_coastal = yes
		OR = {
			region = 1 region = 2 region = 3 region = 4 region = 16 region = 18
			region = 19 region = 36 region = 42 region = 43 region = 44 region = 45
			region = 46 region = 47 region = 48 region = 49 region = 50 region = 51
			region = 52 region = 53 region = 54 region = 55 region = 56 region = 57
			region = 58 region = 89 region = 117 region = 118 region = 121 region = 122
			region = 166 region = 170 region = 171 region = 173 region = 174 region = 197
			region = 208 region = 211 region = 213 region = 220 region = 233 region = 234
			region = 235 region = 275 region = 276 region = 277 region = 278 region = 279
			region = 301 region = 302
		}
	}
}

natural_disaster_state_is_storm_surge_coast = {
	AND = {
		is_coastal = yes
		OR = {
			natural_disaster_state_is_tropical_storm_basin = yes
			natural_disaster_state_is_extratropical_surge_coast = yes
		}
	}
}
```

### Tornado outbreak anchors

This is the exact intersection of vanilla states with at least 40 percent plains land and reviewed severe-convection regions. Mountain, jungle, and desert anchors fail unless they are reached as a separately validated secondary family.

```txt
natural_disaster_state_is_tornado_zone = {
	OR = {
		state = 6 state = 10 state = 16 state = 18 state = 24 state = 27
		state = 29 state = 34 state = 35 state = 36 state = 37 state = 56
		state = 57 state = 58 state = 60 state = 61 state = 62 state = 67
		state = 86 state = 87 state = 91 state = 92 state = 98 state = 99
		state = 137 state = 188 state = 189 state = 192 state = 193 state = 196
		state = 197 state = 198 state = 199 state = 200 state = 201 state = 202
		state = 203 state = 204 state = 205 state = 206 state = 207 state = 217
		state = 221 state = 225 state = 227 state = 239 state = 241 state = 243
		state = 245 state = 251 state = 259 state = 261 state = 265 state = 275
		state = 282 state = 285 state = 300 state = 361 state = 363 state = 364
		state = 365 state = 367 state = 369 state = 370 state = 372 state = 373
		state = 374 state = 375 state = 383 state = 384 state = 389 state = 390
		state = 392 state = 393 state = 394 state = 395 state = 396 state = 401
		state = 430 state = 431 state = 502 state = 504 state = 517 state = 518
		state = 542 state = 583 state = 590 state = 598 state = 606 state = 607
		state = 608 state = 609 state = 613 state = 614 state = 652 state = 763
		state = 807 state = 815 state = 819 state = 834 state = 873 state = 882
		state = 909 state = 911 state = 912 state = 945 state = 946 state = 977
		state = 1034 state = 1035 state = 1037 state = 1038 state = 1041
	}
}
```

Every moving outbreak segment uses `any_neighbor_state` from the preceding segment and must pass this trigger. If no eligible neighbor exists, stop. Never run a new global state draw.

## Terrain-derived exact state domains

### Desert terrain

This list is used only by the secondary dust-region branch. The direct vanilla sandstorm-weather regions do not require it.

```txt
natural_disaster_state_is_desert_terrain_zone = {
	OR = {
		state = 268 state = 269 state = 273 state = 287 state = 288 state = 291
		state = 292 state = 293 state = 294 state = 302 state = 322 state = 350
		state = 376 state = 377 state = 379 state = 380 state = 385 state = 402
		state = 404 state = 406 state = 407 state = 410 state = 411 state = 413
		state = 414 state = 415 state = 416 state = 418 state = 421 state = 433
		state = 443 state = 445 state = 446 state = 447 state = 449 state = 451
		state = 452 state = 453 state = 454 state = 455 state = 456 state = 457
		state = 462 state = 480 state = 482 state = 483 state = 484 state = 512
		state = 513 state = 514 state = 515 state = 547 state = 551 state = 552
		state = 554 state = 557 state = 559 state = 583 state = 584 state = 585
		state = 586 state = 587 state = 588 state = 589 state = 601 state = 604
		state = 611 state = 612 state = 616 state = 617 state = 618 state = 621
		state = 622 state = 656 state = 658 state = 659 state = 661 state = 662
		state = 663 state = 665 state = 674 state = 675 state = 676 state = 677
		state = 678 state = 679 state = 680 state = 681 state = 699 state = 746
		state = 753 state = 755 state = 756 state = 757 state = 758 state = 759
		state = 760 state = 765 state = 767 state = 775 state = 782 state = 786
		state = 817 state = 818 state = 823 state = 830 state = 831 state = 832
		state = 835 state = 836 state = 854 state = 855 state = 857 state = 858
		state = 859 state = 871 state = 873 state = 881 state = 893 state = 898
		state = 903 state = 904 state = 907 state = 908 state = 951 state = 952
		state = 954 state = 955 state = 958 state = 989 state = 1002 state = 1003
		state = 1007 state = 1008 state = 1009 state = 1010 state = 1013
		state = 1014 state = 1015 state = 1016 state = 1040 state = 1043
		state = 1044 state = 1046 state = 1074 state = 1075
	}
}
```

### Physical slope states

Both dry and wet mass movement use this immutable slope list. Their moisture condition is separate:

- dry mass movement also requires arid/drought/heat/fire/earthquake context;
- wet mass movement also requires flood/cyclone/thunderstorm/rain/mud context;
- neither context can rescue a state that fails this slope trigger.

```txt
natural_disaster_state_is_slope_zone = {
	OR = {
		state = 1 state = 2 state = 3 state = 4 state = 9 state = 15
		state = 17 state = 18 state = 20 state = 21 state = 22 state = 26
		state = 28 state = 31 state = 32 state = 39 state = 41 state = 44
		state = 47 state = 48 state = 49 state = 50 state = 52 state = 54
		state = 59 state = 60 state = 65 state = 66 state = 69 state = 70
		state = 71 state = 72 state = 73 state = 74 state = 76 state = 78
		state = 81 state = 82 state = 83 state = 84 state = 88 state = 89
		state = 90 state = 100 state = 101 state = 102 state = 103 state = 104
		state = 105 state = 106 state = 107 state = 108 state = 112 state = 113
		state = 114 state = 115 state = 117 state = 118 state = 119 state = 120
		state = 121 state = 122 state = 123 state = 129 state = 130 state = 131
		state = 133 state = 134 state = 135 state = 136 state = 142 state = 143
		state = 144 state = 151 state = 152 state = 153 state = 156 state = 157
		state = 158 state = 159 state = 160 state = 161 state = 162 state = 165
		state = 166 state = 167 state = 168 state = 169 state = 170 state = 171
		state = 172 state = 173 state = 174 state = 175 state = 176 state = 178
		state = 180 state = 181 state = 182 state = 183 state = 184 state = 185
		state = 186 state = 205 state = 212 state = 217 state = 219 state = 229
		state = 230 state = 231 state = 232 state = 233 state = 234 state = 235
		state = 236 state = 237 state = 239 state = 250 state = 255 state = 256
		state = 261 state = 263 state = 266 state = 267 state = 269 state = 271
		state = 275 state = 277 state = 278 state = 279 state = 282 state = 283
		state = 285 state = 286 state = 288 state = 289 state = 290 state = 292
		state = 293 state = 294 state = 302 state = 303 state = 305 state = 306
		state = 312 state = 314 state = 315 state = 317 state = 319 state = 321
		state = 322 state = 323 state = 324 state = 325 state = 328 state = 329
		state = 330 state = 335 state = 339 state = 340 state = 342 state = 343
		state = 344 state = 345 state = 346 state = 347 state = 348 state = 349
		state = 352 state = 353 state = 354 state = 355 state = 356 state = 357
		state = 358 state = 360 state = 361 state = 362 state = 363 state = 368
		state = 369 state = 372 state = 373 state = 374 state = 375 state = 376
		state = 377 state = 378 state = 379 state = 380 state = 381 state = 382
		state = 383 state = 385 state = 386 state = 387 state = 388 state = 389
		state = 391 state = 392 state = 394 state = 395 state = 398 state = 401
		state = 405 state = 408 state = 409 state = 410 state = 411 state = 412
		state = 413 state = 414 state = 415 state = 416 state = 417 state = 419
		state = 420 state = 421 state = 422 state = 423 state = 425 state = 426
		state = 429 state = 431 state = 432 state = 433 state = 434 state = 435
		state = 436 state = 438 state = 440 state = 441 state = 442 state = 444
		state = 445 state = 448 state = 450 state = 451 state = 453 state = 455
		state = 456 state = 457 state = 458 state = 459 state = 460 state = 461
		state = 462 state = 463 state = 465 state = 468 state = 470 state = 471
		state = 473 state = 475 state = 477 state = 478 state = 479 state = 480
		state = 481 state = 482 state = 483 state = 484 state = 485 state = 488
		state = 489 state = 492 state = 493 state = 496 state = 499 state = 501
		state = 502 state = 503 state = 506 state = 507 state = 508 state = 511
		state = 512 state = 513 state = 516 state = 517 state = 518 state = 519
		state = 521 state = 522 state = 523 state = 524 state = 527 state = 528
		state = 529 state = 530 state = 531 state = 532 state = 533 state = 534
		state = 535 state = 536 state = 537 state = 540 state = 541 state = 543
		state = 546 state = 547 state = 550 state = 553 state = 554 state = 560
		state = 562 state = 563 state = 564 state = 565 state = 573 state = 574
		state = 581 state = 582 state = 584 state = 586 state = 588 state = 592
		state = 593 state = 594 state = 595 state = 596 state = 597 state = 599
		state = 600 state = 601 state = 602 state = 603 state = 604 state = 605
		state = 606 state = 607 state = 608 state = 610 state = 611 state = 614
		state = 615 state = 617 state = 618 state = 619 state = 620 state = 621
		state = 622 state = 623 state = 627 state = 637 state = 640 state = 644
		state = 649 state = 651 state = 652 state = 654 state = 655 state = 659
		state = 663 state = 666 state = 669 state = 670 state = 671 state = 672
		state = 673 state = 676 state = 677 state = 679 state = 681 state = 689
		state = 697 state = 714 state = 715 state = 716 state = 717 state = 719
		state = 723 state = 724 state = 731 state = 732 state = 735 state = 736
		state = 741 state = 742 state = 744 state = 745 state = 747 state = 748
		state = 749 state = 750 state = 751 state = 752 state = 753 state = 754
		state = 755 state = 756 state = 757 state = 759 state = 760 state = 761
		state = 764 state = 770 state = 771 state = 773 state = 783 state = 787
		state = 789 state = 790 state = 791 state = 792 state = 793 state = 794
		state = 799 state = 800 state = 801 state = 802 state = 803 state = 804
		state = 805 state = 806 state = 814 state = 816 state = 817 state = 818
		state = 820 state = 821 state = 826 state = 827 state = 828 state = 829
		state = 830 state = 835 state = 836 state = 837 state = 838 state = 839
		state = 840 state = 841 state = 842 state = 843 state = 845 state = 846
		state = 847 state = 848 state = 850 state = 851 state = 852 state = 853
		state = 855 state = 856 state = 864 state = 869 state = 870 state = 871
		state = 874 state = 877 state = 883 state = 891 state = 892 state = 893
		state = 894 state = 896 state = 904 state = 905 state = 908 state = 914
		state = 917 state = 918 state = 920 state = 921 state = 922 state = 923
		state = 924 state = 925 state = 931 state = 934 state = 935 state = 936
		state = 943 state = 944 state = 947 state = 949 state = 950 state = 951
		state = 952 state = 953 state = 954 state = 955 state = 958 state = 959
		state = 960 state = 970 state = 972 state = 976 state = 978 state = 979
		state = 982 state = 983 state = 984 state = 985 state = 986 state = 987
		state = 988 state = 990 state = 992 state = 993 state = 994 state = 997
		state = 998 state = 999 state = 1000 state = 1001 state = 1002
		state = 1003 state = 1004 state = 1005 state = 1006 state = 1007
		state = 1008 state = 1012 state = 1016 state = 1017 state = 1018
		state = 1019 state = 1020 state = 1022 state = 1024 state = 1026
		state = 1027 state = 1028 state = 1029 state = 1030 state = 1031
		state = 1032 state = 1033 state = 1037 state = 1038 state = 1039
		state = 1041 state = 1042 state = 1044 state = 1045 state = 1048
		state = 1050 state = 1051 state = 1055 state = 1056 state = 1057
		state = 1058 state = 1059 state = 1061 state = 1062 state = 1063
		state = 1064 state = 1065 state = 1073 state = 1079 state = 1080
		state = 1081
	}
}
```

The separate aliases may be simple wrappers:

```txt
natural_disaster_state_is_dry_slope_zone = {
	natural_disaster_state_is_slope_zone = yes
}

natural_disaster_state_is_wet_slope_zone = {
	natural_disaster_state_is_slope_zone = yes
}
```

Do not put moisture history inside these immutable map-data wrappers. Require the dry or wet initiating context in the family target predicate and in every chain/spread continuation.

### Wildfire fuel states

This list is derived from forest/jungle province coverage. The final line adds reviewed coarse-map exceptions for California, Oregon, Victoria, Tasmania, South Australia, the Northern Territory, and North Queensland, where the vanilla terrain abstraction understates chaparral, eucalypt, or savanna fire fuel.

```txt
natural_disaster_state_is_wildfire_fuel_zone = {
	OR = {
		state = 4 state = 5 state = 8 state = 9 state = 11 state = 12
		state = 13 state = 14 state = 17 state = 18 state = 19 state = 20
		state = 24 state = 25 state = 26 state = 27 state = 31 state = 33
		state = 34 state = 35 state = 38 state = 40 state = 42 state = 43
		state = 46 state = 50 state = 51 state = 52 state = 53 state = 54
		state = 55 state = 57 state = 59 state = 60 state = 61 state = 62
		state = 63 state = 64 state = 65 state = 66 state = 68 state = 69
		state = 70 state = 74 state = 75 state = 76 state = 79 state = 80
		state = 81 state = 86 state = 88 state = 89 state = 90 state = 91
		state = 93 state = 94 state = 95 state = 96 state = 97 state = 98
		state = 99 state = 107 state = 108 state = 109 state = 110 state = 111
		state = 112 state = 123 state = 126 state = 132 state = 134 state = 139
		state = 140 state = 141 state = 146 state = 147 state = 148 state = 149
		state = 150 state = 155 state = 165 state = 171 state = 172 state = 175
		state = 181 state = 189 state = 190 state = 191 state = 192 state = 193
		state = 195 state = 199 state = 203 state = 205 state = 206 state = 207
		state = 208 state = 209 state = 210 state = 211 state = 212 state = 213
		state = 215 state = 216 state = 217 state = 219 state = 220 state = 221
		state = 222 state = 223 state = 224 state = 226 state = 228 state = 232
		state = 238 state = 241 state = 242 state = 243 state = 244 state = 245
		state = 246 state = 247 state = 248 state = 249 state = 250 state = 251
		state = 252 state = 253 state = 254 state = 255 state = 256 state = 257
		state = 259 state = 260 state = 262 state = 263 state = 264 state = 265
		state = 272 state = 274 state = 276 state = 280 state = 284 state = 286
		state = 289 state = 295 state = 296 state = 297 state = 298 state = 301
		state = 304 state = 305 state = 307 state = 309 state = 310 state = 311
		state = 312 state = 313 state = 316 state = 317 state = 327 state = 328
		state = 329 state = 330 state = 331 state = 333 state = 334 state = 336
		state = 351 state = 357 state = 358 state = 359 state = 360 state = 362
		state = 363 state = 365 state = 366 state = 367 state = 369 state = 370
		state = 371 state = 372 state = 373 state = 374 state = 375 state = 386
		state = 388 state = 391 state = 393 state = 394 state = 395 state = 397
		state = 398 state = 399 state = 400 state = 401 state = 403 state = 409
		state = 424 state = 426 state = 427 state = 429 state = 430 state = 432
		state = 435 state = 436 state = 437 state = 438 state = 463 state = 464
		state = 465 state = 467 state = 470 state = 472 state = 473 state = 474
		state = 476 state = 477 state = 478 state = 479 state = 486 state = 487
		state = 488 state = 489 state = 490 state = 491 state = 493 state = 494
		state = 495 state = 496 state = 497 state = 499 state = 500 state = 501
		state = 502 state = 503 state = 504 state = 505 state = 509 state = 510
		state = 516 state = 520 state = 521 state = 522 state = 523 state = 527
		state = 533 state = 538 state = 539 state = 540 state = 543 state = 544
		state = 545 state = 546 state = 548 state = 556 state = 558 state = 560
		state = 561 state = 562 state = 563 state = 564 state = 566 state = 567
		state = 568 state = 569 state = 570 state = 571 state = 572 state = 573
		state = 574 state = 575 state = 576 state = 577 state = 578 state = 579
		state = 580 state = 581 state = 591 state = 592 state = 594 state = 609
		state = 610 state = 611 state = 623 state = 624 state = 625 state = 626
		state = 627 state = 628 state = 634 state = 637 state = 640 state = 651
		state = 652 state = 653 state = 654 state = 657 state = 660 state = 664
		state = 666 state = 667 state = 668 state = 669 state = 670 state = 671
		state = 672 state = 673 state = 682 state = 687 state = 688 state = 700
		state = 701 state = 706 state = 707 state = 709 state = 711 state = 712
		state = 714 state = 715 state = 718 state = 721 state = 724 state = 728
		state = 737 state = 740 state = 741 state = 761 state = 762 state = 768
		state = 769 state = 770 state = 771 state = 772 state = 773 state = 774
		state = 776 state = 777 state = 779 state = 780 state = 784 state = 785
		state = 790 state = 795 state = 796 state = 806 state = 807 state = 808
		state = 809 state = 810 state = 811 state = 812 state = 813 state = 814
		state = 815 state = 816 state = 820 state = 824 state = 825 state = 833
		state = 834 state = 845 state = 851 state = 860 state = 862 state = 863
		state = 864 state = 865 state = 866 state = 867 state = 868 state = 869
		state = 870 state = 872 state = 873 state = 875 state = 876 state = 877
		state = 878 state = 879 state = 880 state = 882 state = 885 state = 887
		state = 888 state = 889 state = 890 state = 891 state = 896 state = 897
		state = 900 state = 902 state = 913 state = 915 state = 916 state = 917
		state = 918 state = 919 state = 920 state = 921 state = 922 state = 926
		state = 927 state = 928 state = 929 state = 930 state = 937 state = 938
		state = 939 state = 940 state = 941 state = 942 state = 943 state = 944
		state = 950 state = 956 state = 957 state = 961 state = 962 state = 963
		state = 964 state = 965 state = 966 state = 967 state = 968 state = 969
		state = 974 state = 977 state = 978 state = 979 state = 980 state = 981
		state = 984 state = 994 state = 995 state = 996 state = 997 state = 1017
		state = 1022 state = 1023 state = 1024 state = 1026 state = 1033
		state = 1047 state = 1048 state = 1049 state = 1052 state = 1053
		state = 1054 state = 1055 state = 1056 state = 1057 state = 1060
		state = 1061 state = 1062 state = 1063 state = 1064 state = 1066
		state = 1067 state = 1068 state = 1069 state = 1070 state = 1073
		state = 1077 state = 1078 state = 1079 state = 1081
		state = 378 state = 385 state = 517 state = 518 state = 519
	}
}
```

Fuel is necessary but not sufficient. Require a dry, heat, wind, lightning, drought, or existing-fire context for ignition and continuation. This deliberately permits cold Siberian forest wildfire while the same state still fails heat wave.

### Flood-exposed states

This is the static floodplain, marsh, lowland, and coastal-lowland domain from vanilla terrain. A slope state outside this list may receive a flash-flood follow-up only when the same sequence carries a validated cyclone, thunderstorm, or extreme-rain origin. That exception does not reclassify the state as a floodplain.

```txt
natural_disaster_state_is_flood_exposed_zone = {
	OR = {
		state = 1 state = 5 state = 6 state = 7 state = 9 state = 10
		state = 14 state = 15 state = 16 state = 18 state = 19 state = 21
		state = 22 state = 23 state = 24 state = 27 state = 29 state = 30
		state = 31 state = 32 state = 33 state = 34 state = 35 state = 36
		state = 37 state = 40 state = 43 state = 44 state = 45 state = 46
		state = 47 state = 56 state = 57 state = 58 state = 59 state = 60
		state = 61 state = 62 state = 63 state = 67 state = 75 state = 77
		state = 78 state = 79 state = 84 state = 86 state = 87 state = 91
		state = 92 state = 93 state = 94 state = 98 state = 99 state = 101
		state = 103 state = 109 state = 110 state = 111 state = 113 state = 115
		state = 116 state = 119 state = 120 state = 121 state = 122 state = 123
		state = 124 state = 125 state = 126 state = 127 state = 128 state = 129
		state = 130 state = 131 state = 133 state = 134 state = 135 state = 136
		state = 137 state = 138 state = 140 state = 141 state = 145 state = 146
		state = 149 state = 154 state = 155 state = 158 state = 159 state = 160
		state = 161 state = 163 state = 164 state = 168 state = 169 state = 170
		state = 174 state = 177 state = 179 state = 180 state = 182 state = 187
		state = 188 state = 189 state = 192 state = 193 state = 194 state = 195
		state = 196 state = 197 state = 198 state = 199 state = 200 state = 201
		state = 202 state = 203 state = 204 state = 205 state = 206 state = 207
		state = 209 state = 211 state = 213 state = 214 state = 217 state = 218
		state = 221 state = 222 state = 223 state = 225 state = 227 state = 232
		state = 234 state = 235 state = 236 state = 237 state = 238 state = 239
		state = 240 state = 241 state = 243 state = 245 state = 251 state = 252
		state = 255 state = 256 state = 257 state = 258 state = 259 state = 260
		state = 261 state = 265 state = 270 state = 272 state = 275 state = 278
		state = 281 state = 282 state = 285 state = 291 state = 299 state = 300
		state = 304 state = 307 state = 308 state = 312 state = 313 state = 315
		state = 316 state = 318 state = 319 state = 320 state = 331 state = 332
		state = 337 state = 338 state = 339 state = 340 state = 341 state = 342
		state = 344 state = 345 state = 347 state = 348 state = 349 state = 353
		state = 355 state = 357 state = 359 state = 361 state = 363 state = 364
		state = 365 state = 366 state = 367 state = 369 state = 370 state = 371
		state = 372 state = 373 state = 374 state = 375 state = 383 state = 384
		state = 389 state = 390 state = 391 state = 392 state = 393 state = 394
		state = 395 state = 396 state = 399 state = 400 state = 401 state = 403
		state = 408 state = 409 state = 422 state = 423 state = 424 state = 425
		state = 426 state = 427 state = 428 state = 429 state = 430 state = 431
		state = 437 state = 438 state = 439 state = 440 state = 443 state = 447
		state = 448 state = 454 state = 458 state = 461 state = 466 state = 467
		state = 468 state = 469 state = 475 state = 476 state = 481 state = 483
		state = 485 state = 498 state = 499 state = 502 state = 504 state = 507
		state = 510 state = 516 state = 517 state = 518 state = 519 state = 521
		state = 522 state = 524 state = 525 state = 526 state = 527 state = 528
		state = 536 state = 537 state = 541 state = 542 state = 544 state = 549
		state = 553 state = 555 state = 556 state = 557 state = 559 state = 570
		state = 571 state = 572 state = 577 state = 579 state = 580 state = 582
		state = 583 state = 590 state = 591 state = 596 state = 597 state = 598
		state = 606 state = 607 state = 608 state = 609 state = 610 state = 611
		state = 613 state = 614 state = 624 state = 626 state = 629 state = 630
		state = 631 state = 632 state = 633 state = 635 state = 636 state = 637
		state = 638 state = 639 state = 641 state = 642 state = 643 state = 644
		state = 645 state = 646 state = 647 state = 648 state = 650 state = 651
		state = 652 state = 655 state = 657 state = 664 state = 667 state = 677
		state = 683 state = 684 state = 685 state = 686 state = 689 state = 690
		state = 691 state = 692 state = 693 state = 694 state = 695 state = 696
		state = 698 state = 702 state = 703 state = 704 state = 705 state = 708
		state = 710 state = 713 state = 715 state = 716 state = 717 state = 720
		state = 722 state = 725 state = 726 state = 727 state = 730 state = 731
		state = 733 state = 734 state = 738 state = 739 state = 741 state = 761
		state = 763 state = 766 state = 774 state = 778 state = 781 state = 785
		state = 788 state = 791 state = 793 state = 797 state = 798 state = 801
		state = 807 state = 809 state = 815 state = 819 state = 822 state = 824
		state = 825 state = 826 state = 831 state = 834 state = 844 state = 849
		state = 860 state = 861 state = 866 state = 867 state = 868 state = 870
		state = 871 state = 872 state = 873 state = 874 state = 882 state = 883
		state = 884 state = 886 state = 887 state = 892 state = 894 state = 895
		state = 896 state = 898 state = 899 state = 901 state = 902 state = 903
		state = 905 state = 906 state = 909 state = 910 state = 911 state = 912
		state = 913 state = 921 state = 925 state = 926 state = 928 state = 931
		state = 932 state = 933 state = 935 state = 936 state = 937 state = 945
		state = 946 state = 948 state = 956 state = 971 state = 973 state = 974
		state = 975 state = 977 state = 982 state = 983 state = 984 state = 991
		state = 996 state = 998 state = 1011 state = 1025 state = 1027
		state = 1031 state = 1033 state = 1034 state = 1035 state = 1037
		state = 1038 state = 1041 state = 1047 state = 1049 state = 1051
		state = 1052 state = 1053 state = 1058 state = 1066 state = 1071
		state = 1072 state = 1076 state = 1077
	}
}
```

Flood spread uses the same trigger on every neighbor. A previous flood flag is not permission to spread into a physically excluded state. The flash-flood exception is limited to a validated wet storm sequence and still requires the slope trigger.

## Complete 25-family geography contract

| # | Family | Immutable physical gate | Context and continuation rule |
|---:|---|---|---|
| 1 | earthquake | `natural_disaster_state_is_seismic_zone` | Spread and aftershocks recheck the seismic gate. A history flag only scores. |
| 2 | flood | `natural_disaster_state_is_flood_exposed_zone` | A slope-only flash flood needs a validated wet storm origin. Every spread state rechecks its branch. |
| 3 | tropical cyclone | `is_coastal = yes` and `natural_disaster_state_is_tropical_storm_basin` | Lock the resolved basin. Every path segment is an eligible neighbor in the same basin. |
| 4 | extreme wind | `natural_disaster_state_is_windstorm_zone` below | Physical domain is broad. Coast, blizzard, cyclone, and severe-convection zones are accepted. |
| 5 | tornado outbreak | exact `natural_disaster_state_is_tornado_zone` | Every segment is an eligible neighboring plains anchor. |
| 6 | thunderstorm | inhabited, non-impassable land outside the polar exclusion below | Warmth, rain, agriculture, and population score severity but are not substitutes for runtime validity. |
| 7 | hailstorm | thunderstorm domain plus temperate/highland, tornado, or cold-fringe domain | Exclude polar ice and use agriculture/urban density only as score. |
| 8 | blizzard | exact `natural_disaster_state_is_blizzard_zone` | No desert, tropical, or history-based bypass. |
| 9 | cold wave | exact `natural_disaster_state_is_cold_zone` | No infrastructure, history, or population bypass. |
| 10 | heat wave | exact positive heat regions and `NOT cold_zone` | Keep the separate Event 051 exclusion. Siberia always fails. |
| 11 | drought | exact `natural_disaster_state_is_drought_zone` | Water stress and agriculture score after the climate gate. |
| 12 | dust/sandstorm | `natural_disaster_state_is_arid_zone` | Secondary regions also require exact desert terrain. Region 134 fails. |
| 13 | wildfire | exact `natural_disaster_state_is_wildfire_fuel_zone` | Require dry/heat/wind/lightning/fire context for ignition. Cold forest may burn while remaining heat-ineligible. |
| 14 | dry mass movement | exact `natural_disaster_state_is_slope_zone` | Also require drought/heat/dust/fire/earthquake context. Flat land always fails. |
| 15 | wet mass movement | exact `natural_disaster_state_is_slope_zone` | Also require flood/cyclone/thunderstorm/rain/mud context. Flat land always fails. |
| 16 | volcanic eruption | exact `natural_disaster_state_is_volcanic_vent_zone` | No coast/resource/history alternative. |
| 17 | ashfall | static plume receptor domain plus saved valid vent origin | Target only origin, a bounded adjacent state, or reviewed same-plume-region receptor. |
| 18 | lahar | exact `natural_disaster_state_is_lahar_zone` plus saved valid vent origin | Same eruption sequence only. Wet/resource history alone always fails. |
| 19 | tsunami | `is_coastal = yes`, saved seismic/volcanic/ocean origin, and same tsunami basin | Originless direct call rejects. Inland targets always fail. |
| 20 | storm surge | `natural_disaster_state_is_storm_surge_coast` | Preserve cyclone basin or extratropical storm-coast context. Coast alone fails. |
| 21 | meteor impact | generic valid inhabited land, or an explicitly modeled ocean-impact origin | Ocean mode must not fabricate a land impact state. Physical secondary tsunami still uses the basin rule. |
| 22 | meteor shower | generic valid inhabited land | Multi-state shower hits use bounded neighbors. No stale or global replacement target. |
| 23 | whole-earth rupture | generic valid inhabited land origin | This fictional global family may originate anywhere, but earthquake, slope, and tsunami derivatives each use their own gate. |
| 24 | massive eruption | exact `natural_disaster_state_is_massive_eruption_zone` | Ordinary vent states outside the subset fail. No fallback to ordinary eruption or meteor. |
| 25 | moving storm corridor | cyclone, tornado, or windstorm start | Every later state is adjacent and passes the locked derived family and basin. Stop at a dead end. |

Broad atmospheric helpers:

```txt
natural_disaster_state_is_windstorm_zone = {
	OR = {
		is_coastal = yes
		natural_disaster_state_is_tropical_storm_basin = yes
		natural_disaster_state_is_blizzard_zone = yes
		natural_disaster_state_is_tornado_zone = yes
	}
}

natural_disaster_state_is_convective_storm_zone = {
	NOT = {
		OR = {
			region = 36 region = 45 region = 87 region = 88 region = 150
			region = 222 region = 257 region = 258 region = 259 region = 260
			region = 263 region = 264
		}
	}
}

natural_disaster_state_is_hail_zone = {
	AND = {
		natural_disaster_state_is_convective_storm_zone = yes
		OR = {
			natural_disaster_state_is_tornado_zone = yes
			natural_disaster_state_is_cold_zone = yes
			natural_disaster_state_is_slope_zone = yes
		}
	}
}

natural_disaster_state_is_storm_corridor_zone = {
	OR = {
		natural_disaster_state_is_tropical_storm_basin = yes
		natural_disaster_state_is_tornado_zone = yes
		natural_disaster_state_is_windstorm_zone = yes
	}
}
```

`natural_disaster_state_is_convective_storm_zone` is intentionally broad because thunderstorms are physically possible across almost every inhabited climate. Its purpose is to remove the persistent polar/ocean-weather artifacts, not to turn population or agriculture into climate. Hail adds terrain and severe-weather exposure so the cold-zone branch cannot admit a flat polar state unless the state also has a valid slope or tornado exposure.

## Dispatch body

The family dispatch should call only geography predicates. Existing resource, infrastructure, building, agriculture, history, and severity logic belongs in the scorer.

```txt
natural_disaster_is_family_geographically_eligible = {
	OR = {
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.earthquake } natural_disaster_state_is_seismic_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.flood } natural_disaster_state_is_flood_exposed_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.tropical_cyclone } is_coastal = yes natural_disaster_state_is_tropical_storm_basin = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.extreme_wind } natural_disaster_state_is_windstorm_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.tornado_outbreak } natural_disaster_state_is_tornado_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.thunderstorm } natural_disaster_state_is_convective_storm_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.hailstorm } natural_disaster_state_is_hail_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.blizzard } natural_disaster_state_is_blizzard_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.cold_wave } natural_disaster_state_is_cold_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.heat_wave } natural_disaster_state_is_heat_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.drought } natural_disaster_state_is_drought_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.dust_and_sandstorm } natural_disaster_state_is_arid_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.wildfire } natural_disaster_state_is_wildfire_fuel_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.dry_mass_movement } natural_disaster_state_is_dry_slope_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.wet_mass_movement } natural_disaster_state_is_wet_slope_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.volcanic_eruption } natural_disaster_state_is_volcanic_vent_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.ashfall } natural_disaster_state_is_volcanic_plume_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.lahar } natural_disaster_state_is_lahar_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.tsunami } is_coastal = yes natural_disaster_state_is_ocean_exposed_coast = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.storm_surge } natural_disaster_state_is_storm_surge_coast = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.meteor_impact } always = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.meteor_shower } always = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.whole_earth_rupture } always = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.massive_eruption } natural_disaster_state_is_massive_eruption_zone = yes }
		AND = { check_variable = { natural_disaster_current_family = constant:natural_disaster_family.moving_storm_corridor } natural_disaster_state_is_storm_corridor_zone = yes }
	}
}
```

`natural_disaster_state_is_ocean_exposed_coast` is only the static receptor half. Keep compatible origin proof and basin equality as mandatory siblings in `natural_disaster_is_valid_family_target` and chain resolution. The standalone helper must never be called as proof of a complete tsunami target.

## Confidence, exclusions, and accepted map false negatives

### Confidence levels

| Dataset | Confidence | Reason |
|---|---|---|
| Cold, blizzard, heat, drought, and direct dust region IDs | High | Parsed from the active vanilla strategic-region weather and reviewed against current region names and physical climate. |
| Volcano mainland and large-island assignments | High | Positive-elevation GVP WFS point falls within or unambiguously belongs to the current vanilla state geometry. |
| Remote grouped-island assignments 720 and 738 | Medium-high | Vanilla groups South Sandwich with state 720 and the Banda component with state 738 even though the state names are South Georgia and Aru Islands. Province components were inspected. |
| Southern Andes split 507/949/950/951/952/953/954/955 | Medium-high | WFS points and current province raster agree, but the HOI map is coarse along the Chile-Argentina border. The lists are safe for state-scale gameplay. |
| Terrain-derived slope, flood, fuel, desert, and tornado IDs | High for vanilla terrain, medium for real-world microtopography | Exact against current province terrain and raster area. Small valleys, rivers, chaparral, and volcano relief can be coarser than the real world. Reviewed exceptions are explicit. |
| Massive-eruption subset | Conservative high | Requires a valid GVP vent state and a reviewed large caldera, stratovolcano, shield/fissure, or major arc complex. Small monogenetic fields fail. |

No identifier in the implementation lists is retained at insufficient confidence. A candidate that could not be assigned safely to current vanilla state geometry was excluded and recorded below instead of being left as a placeholder or nearest-state guess.

### Explicit exclusions

These are deliberate and must not be silently re-added as broad fallbacks:

| Excluded state or feature | Reason |
|---|---|
| 51 Rhineland as West Eifel | West Eifel maps to state 42 Moselland in the current vanilla geometry. State 51 is not a vent state. |
| 156 Calabria as an Aeolian vent | The vanilla state contains only mainland Calabria provinces. The tiny Aeolian islands are not painted state components. Sicily 115 remains valid through Etna. Calabria may receive ash from a saved Sicily origin. |
| 329 Tannu Tuva as Jombolok | Jombolok is in Buryatia and maps to state 564. |
| 419 West Azerbaijan as Tendurek | Tendurek maps to state 800 Van. |
| 518 Tasmania as Newer Volcanics Province | The official WFS point is in Victoria and maps to 517. Tasmania has no GVP Holocene land feature. Tasmania remains a wildfire/flood/tornado-terrain state where appropriate. |
| 521 Queensland as McBride | McBride Volcanic Province maps to state 872 North Queensland. |
| 529 Sanyo and 530 Shikoku | Abu and Sanbesan both map to state 1020 San'in in the current geometry. The WFS has no Shikoku Holocene feature. |
| 638 Guam | Its matched GVP records are Forecast Seamount and other negative-elevation submarine vents. |
| 641 Tahiti | Teahitia and Rocard are submarine. Positive-elevation Mehetia is not one of state 641's painted province components. |
| 704 Saint Helena | The GVP Holocene dataset has no Saint Helena land volcano. Ascension is state 703 and remains valid. |
| 1030 Gyeongsang as Ulleungdo | The current state has no Ulleungdo province component. Halla is explicitly represented by Jeju in state 1031. |
| Antarctica | No vanilla playable land state exists. |
| Tonga and several tiny ocean islands | No current vanilla state component contains the WFS point. Do not force these points into Samoa, Fiji, or another nearby state. |
| All negative-elevation WFS features | Submarine vents are not land eruption targets. They may later support an explicitly modeled ocean-origin tsunami system, not a fake state eruption. |

These are accepted map-representation false negatives, not placeholder work. If the mod later adds state geometry for Mehetia, Ulleungdo, Tonga, the Aeolians, or other omitted islands, rerun and review the registry rather than assigning them to the nearest current land state.

## Validation sample matrix

| Scenario | Expected geography result | Evidence tested |
|---|---|---|
| volcanic eruption in state 115 Sicily | Pass | Etna, GVP 211060. |
| volcanic eruption in state 64 Brandenburg/Berlin | Fail | State 64 is absent from the vent list. Population and urban buildings cannot rescue it. |
| volcanic eruption in state 366 Florida | Fail | Coast is not a vent. |
| volcanic eruption in state 42 Moselland | Pass | West Eifel Volcanic Field, GVP 210010. |
| volcanic eruption in state 51 Rhineland | Fail | Corrected West Eifel state assignment is 42. |
| massive eruption in state 115 Sicily | Pass | Etna is in the reviewed massive subset. |
| massive eruption in state 2 Lazio | Fail | Colli Albani supports ordinary eruption but is excluded from the conservative massive subset. |
| lahar in state 115 with saved Sicily eruption origin | Pass | Valid lahar state and same physical origin. |
| lahar in state 64 after generic rain | Fail | No vent, regardless of wet history. |
| ashfall in state 156 with saved state 115 origin and plume relation | Pass | Receptor is permitted without calling Calabria a vent. |
| ashfall in state 156 with no saved vent origin | Fail | Plume geography alone is insufficient. |
| heat wave in state 637 Kamchatka | Fail | State is in reviewed cold region 257, even though it is volcanic. |
| heat wave in state 563 Chita | Fail | Transbaikal cold region 256. |
| heat wave in a reviewed tropical or subtropical state | Pass | Positive heat region and not cold. Event 051 still rechecks separately. |
| blizzard in state 514 Algerian Desert | Fail | Region 127 is not a blizzard region. |
| cold wave in state 366 Florida | Fail | Florida's sea-weather artifact region 170 was removed from cold. |
| dust in state 514 Algerian Desert | Pass | Direct sandstorm region 127 and exact desert terrain. |
| dust in state 890 Kivu | Fail | Humid Congo region and no dust-domain branch. |
| dust in Caucasus region 134 | Fail | Explicit vanilla weather anomaly exclusion. |
| cyclone in inland state 330 Mongolia | Fail | Not coastal and not a cyclone receptor. |
| cyclone on an eligible Caribbean coast | Pass | Coastal plus North Atlantic basin. |
| cyclone on a generic Baltic coast | Fail | Coast alone is insufficient. |
| storm surge in state 366 Florida during North Atlantic cyclone | Pass | Coastal and basin-compatible. |
| storm surge in inland state 383 | Fail | Not coastal. |
| tsunami on California coast from Pacific seismic/ocean origin | Pass | Coastal, Pacific basin, compatible saved origin. |
| tsunami in inland Mongolia | Fail | Inland and wrong basin. |
| tsunami on arbitrary coast with no origin | Fail | Static receptor helper never proves a complete tsunami. |
| tornado outbreak in Texas plains state 375 | Pass | Exact plains/severe-convection anchor list. |
| tornado outbreak in mountain state 323 Nepal | Fail | Not an exact tornado anchor. |
| dry mass movement in slope state 382 with drought/earthquake context | Pass | Exact slope plus dry initiating context. |
| dry mass movement in flat plains state 383 | Fail | Context cannot rescue missing slope. |
| wet mass movement in slope state 323 with cyclone/flood context | Pass | Exact slope plus wet initiating context. |
| wet mass movement in flat plains state 383 | Fail | Context cannot rescue missing slope. |
| wildfire in state 378 California during heat/wind | Pass | Reviewed chaparral exception plus ignition context. |
| wildfire in state 514 Algerian Desert | Fail | Hot barren desert is not wildfire fuel. |
| wildfire in Siberian forest after lightning/drought | Pass | Fuel may burn, while heat-wave eligibility remains false. |
| flood in an exact floodplain state | Pass | Static flood domain. |
| flood spread into an excluded arbitrary mountain state | Fail | Neighbor rechecks the flood domain. |
| flash flood in a slope state from validated cyclone/thunderstorm chain | Pass through the explicit flash-flood branch only | Does not classify the state as a general floodplain. |
| whole-earth rupture in ordinary valid land | Pass origin | Each derived earthquake, mass movement, or tsunami rechecks its own physical rule. |
| moving storm corridor reaches no eligible neighbor | Stop | No teleport and no global replacement draw. |

## Implementation and audit notes

- The hard geography dispatch must be called by initial targeting, repeat targeting, regional spread, path continuation, chain-family resolution, and delayed execution.
- A state history flag can score recurrence or escalation, but can never manufacture physical eligibility.
- Random family retry may change a random family candidate inside the authorized family pool. It may not widen a selected state, country, or region and may not turn an invalid volcano into a meteor.
- A direct origin-dependent family call must either supply a compatible validated origin or reject. Do not solve the missing origin by accepting any receptor state.
- Keep the registry version header tied to vanilla 1.19.2 and rerun it after a map update.
- The WFS/list count difference is not an invitation to nearest-state-fill missing geometry. Features without safe current state geometry stay excluded and documented.

## Files and handoff status

File written by this subagent:

- `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-11_event013_physical_geography_data_handoff.md`

Files intentionally not edited:

- gameplay script
- localisation
- visual assets
- spreadsheets and presentations
- Event 013 source specifications

No fallback state, synthetic nearest-coast volcano, or unreported simplification was used. The only omissions are the explicit current-map false negatives listed above. Parent implementation and final integration validation remain required.
