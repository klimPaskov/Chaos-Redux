# Fallout country memory assignment

Disposition: implemented (static review; the in-game result for a live campaign is `needs_live_game`). Acceptance basis: round 2 lead item "Assign country memories from source tag and capital geography instead of nine region defaults", taken under the user's grant of design authority and recorded as decision A13 in `agent_decisions_2026-10-04.md`.

Source: `common/scripted_effects/fallout_consolidated_effects.txt` (`fallout_assign_successor_country_memories`, `fallout_generic_assign_country_memory`, the `fallout_country_memory_*_candidate` effects and stage effects) and `common/scripted_triggers/fallout_consolidated_triggers.txt` (`fallout_country_memory_area_<memory>`, `fallout_country_memory_area_is_soviet_periphery`, `fallout_country_memory_candidate_is_protected`).

## Order

Survivor allocation commits every survivor first. Before finalization, each stage runs over every survivor that is still waiting, players first, before the next stage starts:

1. Exact tag, with a homeland condition for empires.
2. Original tag of a civil-war clone.
3. The area that holds the capital, if no other survivor holds that memory.
4. The same area, shared. A protected memory (content written for one identity) is never shared; the survivor receives its neighbour instead.
5. The regional default for `fallout_region_id` (the nine memories used before this change), under the same sharing rule.

Stages 1 to 3 hand out each memory once per Fallout generation. Every live state belongs to exactly one area, so stage 5 is only reached by a capital outside the vanilla state set. The memory is fixed for the generation, and map return keeps it. The NZL Lifeboat State and the USA Federal Continuity package set their own memory before this pass and are counted as holders.

Why sharing is allowed at stage 4: a 1936 world has about ninety land-holding countries, and the 99 memories are bound to places. Giving every survivor a distinct memory would hand Bulgaria or Honduras a memory written for another continent. A second survivor seated in an area therefore shares that area's memory unless the memory carries single-identity content. When a memory gains its own chain or orientation rows, add it to `fallout_country_memory_candidate_is_protected` with a neighbour in `fallout_country_memory_neighbour_candidate`.

## Protected memories and neighbours

| Protected memory | Neighbour for a second survivor in its area |
| --- | --- |
| `federal_continuity_zone` | `atlantic_congressional_remnant` |
| `alpine_redoubt` | `danube_ration_league` |
| `rhine_dead_cities` | `low_countries_polder_authority` |
| `don_steppe_hetmanates` | `ukrainian_bread_bunkers` |
| `mekong_greenhouse_compact` | `malayan_strait_board` |
| `bengal_delta_raft_republic` | `indo_gangetic_relief_authority` |
| `levant_quarantine_cities` | `mesopotamian_water_courts` |
| `congo_green_basin` | `great_lakes_mutant_marsh` |
| `sahel_caravan_wards` | `maghreb_solar_forts` |
| `ethiopian_highland_refuge` | `east_african_rail_union` |
| `atacama_observatory_state` | `andean_sky_republics` |
| `antarctic_listening_government` | `patagonian_food_haven` |
| `west_african_port_confederacies` | `cape_verde_radio_anchor` |
| `manchurian_reactor_keeps` | `yellow_river_famine_councils` |

## Pilot and chain memories in a vanilla 1936 world

The table assumes every 1936 country survives with its 1936 capital. Allocation keeps the frozen capital when it can still host a government; otherwise the survivor is seated in its best surviving state, and the area rules then decide.

| Memory | Content | Who receives it |
| --- | --- | --- |
| `federal_continuity_zone` | Ash-week pilot | USA by tag while seated in North America (AI through the universal package, a human player through the Federal Continuity package). A USA civil-war clone receives `atlantic_congressional_remnant`. |
| `alpine_redoubt` | Ash-week pilot | SWI by tag. AUS by tag only if Switzerland no longer exists. Otherwise the first survivor seated in the Swiss, Tyrolean, South Tyrol, Trentino, Savoy or Alpes states. |
| `rhine_dead_cities` | Ash-week pilot | GER by tag while seated in Europe. Otherwise the first survivor seated in the Rhineland, Ruhr or north German states. |
| `don_steppe_hetmanates` | Ash-week pilot | No 1936 country. A released Don Republic (DON) by tag, or the first survivor seated in Rostov, Stalingrad, Volgodonsk, Millerovo, the Donbas, Krasnodar, Stavropol, Voronezh or Kalmykia, which includes a Soviet Union whose capital moved there. |
| `mekong_greenhouse_compact` | Ash-week pilot | SIA by tag. Otherwise the first survivor seated in Siam, French Indochina or the Shan states. |
| `bengal_delta_raft_republic` | Ash-week pilot | BRM through its capital area (Pegu). A released Bangladesh (BAN) takes it by tag first. The British Raj seated in Bengal takes it when no survivor took it first. |
| `levant_quarantine_cities` | Ash-week pilot | SYR by tag. LEB, PAL and JOR receive `mesopotamian_water_courts` as the neighbour. |
| `congo_green_basin` | Ash-week pilot and four chains | No 1936 country. A released Congo (COG) by tag, or the first survivor seated in the Belgian or French Congo, Gabon, Cameroon, Spanish Guinea or Cabinda (for example Belgium seated in Léopoldville). |
| `sahel_caravan_wards` | Ash-week pilot | No 1936 country. A released Mali (MLI) by tag, or the first survivor seated in the Sahel states (for example France seated in Bamako). |
| `ethiopian_highland_refuge` | Ash-week pilot | ETH by tag. AFA receives `east_african_rail_union` as the neighbour. |
| `atacama_observatory_state` | Ash-week pilot | CHL by tag. |
| `antarctic_listening_government` | Ash-week pilot | No 1936 country. The survivor seated in South Georgia (state 720). |
| `west_african_port_confederacies` | Chain | LIB by tag while Nigeria does not exist; a released Nigeria (NGA) takes it first. Otherwise the first survivor seated on the West African coast. |
| `manchurian_reactor_keeps` | Chain | MAN by tag. Otherwise the first survivor seated in Manchuria or Dalian. |

Major powers in 1936: USA `federal_continuity_zone`, ENG `british_emergency_isles`, FRA `french_loire_continuity`, GER `rhine_dead_cities`, ITA `italian_apennine_communes`, SOV `ural_continuity_directorate`, JAP `japanese_shelter_archipelago`, CHI `yellow_river_famine_councils`.

## Every 1936 survivor

| Survivor | Memory | Stage |
| --- | --- | --- |
| AFA | `east_african_rail_union` | neighbour of a taken memory |
| AFG | `persian_tunnel_ministries` | shared area |
| ALB | `balkan_mountain_wards` | shared area |
| ARG | `la_plata_port_compact` | exact tag |
| AST | `australian_grain_shield` | exact tag |
| AUS | `danube_ration_league` | shared area |
| BEL | `low_countries_polder_authority` | shared area |
| BHU | `himalayan_shelter_belt` | shared area |
| BOL | `andean_sky_republics` | shared area |
| BRA | `brazilian_interior_leagues` | exact tag |
| BRM | `bengal_delta_raft_republic` | capital area |
| BUL | `balkan_mountain_wards` | shared area |
| CAN | `northern_shield_shelters` | exact tag |
| CHI | `yellow_river_famine_councils` | exact tag |
| CHL | `atacama_observatory_state` | exact tag |
| COL | `colombian_mountain_corridors` | exact tag |
| COS | `yucatan_cenote_compact` | capital area |
| CUB | `caribbean_port_chain` | exact tag |
| CZE | `danube_ration_league` | shared area |
| DEN | `scandinavian_cold_councils` | shared area |
| DOM | `caribbean_port_chain` | shared area |
| ECU | `andean_sky_republics` | shared area |
| ELS | `yucatan_cenote_compact` | shared area |
| ENG | `british_emergency_isles` | exact tag |
| EST | `baltic_forest_brotherhoods` | exact tag |
| ETH | `ethiopian_highland_refuge` | exact tag |
| FIN | `finnish_forest_army` | exact tag |
| FRA | `french_loire_continuity` | exact tag |
| GER | `rhine_dead_cities` | exact tag |
| GRE | `greek_island_synods` | exact tag |
| GUA | `yucatan_cenote_compact` | shared area |
| GXC | `canton_port_commune` | exact tag |
| HAI | `caribbean_port_chain` | shared area |
| HOL | `low_countries_polder_authority` | exact tag |
| HON | `yucatan_cenote_compact` | shared area |
| HUN | `danube_ration_league` | exact tag |
| ICE | `scandinavian_cold_councils` | shared area |
| INS | `indonesian_rice_archipelago` | exact tag |
| IRE | `irish_maritime_refuge` | exact tag |
| IRQ | `mesopotamian_water_courts` | exact tag |
| ITA | `italian_apennine_communes` | exact tag |
| JAP | `japanese_shelter_archipelago` | exact tag |
| JOR | `mesopotamian_water_courts` | neighbour of a taken memory |
| KUW | `arabian_fuel_emirates` | shared area |
| LAT | `baltic_forest_brotherhoods` | shared area |
| LEB | `mesopotamian_water_courts` | neighbour of a taken memory |
| LIB | `west_african_port_confederacies` | exact tag |
| LIT | `baltic_forest_brotherhoods` | shared area |
| LUX | `low_countries_polder_authority` | shared area |
| MAL | `malayan_strait_board` | exact tag |
| MAN | `manchurian_reactor_keeps` | exact tag |
| MEN | `mongolian_nomad_grid` | shared area |
| MEX | `sonoran_water_board` | exact tag |
| MON | `mongolian_nomad_grid` | exact tag |
| NEP | `himalayan_shelter_belt` | shared area |
| NIC | `yucatan_cenote_compact` | shared area |
| NOR | `scandinavian_cold_councils` | shared area |
| NZL | `polynesian_lifeboat_confederacy` | exact tag |
| OMA | `arabian_fuel_emirates` | shared area |
| PAL | `mesopotamian_water_courts` | neighbour of a taken memory |
| PAN | `colombian_mountain_corridors` | shared area |
| PAR | `paraguay_river_holdfast` | exact tag |
| PER | `persian_tunnel_ministries` | exact tag |
| PHI | `philippine_island_radio_kingdoms` | exact tag |
| POL | `polish_ash_republics` | exact tag |
| POR | `iberian_sun_shelters` | shared area |
| PRC | `yellow_river_famine_councils` | shared area |
| PRU | `andean_sky_republics` | exact tag |
| RAJ | `indo_gangetic_relief_authority` | exact tag |
| ROM | `balkan_mountain_wards` | shared area |
| SAF | `south_african_continuity_mines` | exact tag |
| SAU | `arabian_fuel_emirates` | exact tag |
| SHX | `yellow_river_famine_councils` | shared area |
| SIA | `mekong_greenhouse_compact` | exact tag |
| SIK | `steppe_convoy_republics` | capital area |
| SOV | `ural_continuity_directorate` | exact tag |
| SPR | `iberian_sun_shelters` | exact tag |
| SWE | `scandinavian_cold_councils` | exact tag |
| SWI | `alpine_redoubt` | exact tag |
| SYR | `levant_quarantine_cities` | exact tag |
| TAN | `baikal_monastic_line` | exact tag |
| TIB | `himalayan_shelter_belt` | exact tag |
| TUR | `anatolian_plateau_remnant` | exact tag |
| URG | `la_plata_port_compact` | shared area |
| USA | `federal_continuity_zone` | exact tag |
| VEN | `venezuelan_fuel_remnant` | exact tag |
| XSM | `himalayan_shelter_belt` | shared area |
| YEM | `arabian_fuel_emirates` | shared area |
| YUG | `balkan_mountain_wards` | exact tag |
| YUN | `sichuan_interior_shelter` | capital area |

## Stage 1: exact tag rules

Rules are tried top to bottom. A guarded rule applies only while its condition holds.

| Tag | Condition | Memory |
| --- | --- | --- |
| USA | capital on north_america | `federal_continuity_zone` |
| CAN | capital on north_america | `northern_shield_shelters` |
| MEX | none | `sonoran_water_board` |
| QUE | none | `quebec_winter_republic` |
| YUC | none | `yucatan_cenote_compact` |
| HAW | none | `hawaiian_relay_kingdom` |
| CUB | none | `caribbean_port_chain` |
| BRA | capital on south_america | `brazilian_interior_leagues` |
| ARG | none | `la_plata_port_compact` |
| CHL | none | `atacama_observatory_state` |
| PRU | none | `andean_sky_republics` |
| COL | none | `colombian_mountain_corridors` |
| VEN | none | `venezuelan_fuel_remnant` |
| PAR | none | `paraguay_river_holdfast` |
| GYA | none | `guiana_rain_stations` |
| ENG | capital on europe | `british_emergency_isles` |
| SCO | none | `scottish_hydro_parliament` |
| IRE | none | `irish_maritime_refuge` |
| SWI | none | `alpine_redoubt` |
| AUS | no SWI | `alpine_redoubt` |
| GER | capital on europe | `rhine_dead_cities` |
| BAY | none | `bavarian_shelter_state` |
| HOL | capital on europe | `low_countries_polder_authority` |
| FRA | capital on europe | `french_loire_continuity` |
| BRI | none | `breton_port_league` |
| SPR | capital on europe | `iberian_sun_shelters` |
| CAT | none | `catalan_emergency_commune` |
| ITA | capital on europe | `italian_apennine_communes` |
| SWE | none | `scandinavian_cold_councils` |
| FIN | none | `finnish_forest_army` |
| POL | none | `polish_ash_republics` |
| HUN | none | `danube_ration_league` |
| YUG | none | `balkan_mountain_wards` |
| GRE | none | `greek_island_synods` |
| EST | none | `baltic_forest_brotherhoods` |
| SOV | capital outside the Soviet periphery areas | `ural_continuity_directorate` |
| UKR | none | `ukrainian_bread_bunkers` |
| DON | none | `don_steppe_hetmanates` |
| GEO | none | `caucasus_shelter_states` |
| KAZ | none | `steppe_convoy_republics` |
| FER | none | `vladivostok_radio_port` |
| MON | none | `mongolian_nomad_grid` |
| TAN | none | `baikal_monastic_line` |
| TUR | none | `anatolian_plateau_remnant` |
| PER | none | `persian_tunnel_ministries` |
| IRQ | none | `mesopotamian_water_courts` |
| SAU | none | `arabian_fuel_emirates` |
| SYR | none | `levant_quarantine_cities` |
| EGY | none | `nile_food_command` |
| SUD | none | `upper_nile_cattle_federation` |
| MOR | none | `maghreb_solar_forts` |
| ETH | none | `ethiopian_highland_refuge` |
| NGA | none | `west_african_port_confederacies` |
| LIB | no NGA | `west_african_port_confederacies` |
| MLI | none | `sahel_caravan_wards` |
| COG | none | `congo_green_basin` |
| UGA | none | `great_lakes_mutant_marsh` |
| KEN | none | `east_african_rail_union` |
| SAF | none | `south_african_continuity_mines` |
| MAD | none | `madagascar_isolation_state` |
| JAP | capital in the Japanese home islands or Hokkaido | `japanese_shelter_archipelago` |
| KOR | none | `korean_tunnel_armies` |
| MAN | none | `manchurian_reactor_keeps` |
| CHI | capital on asia | `yellow_river_famine_councils` |
| PRC | no CHI | `yellow_river_famine_councils` |
| GXC | none | `canton_port_commune` |
| TIB | none | `himalayan_shelter_belt` |
| SIA | none | `mekong_greenhouse_compact` |
| PHI | none | `philippine_island_radio_kingdoms` |
| INS | none | `indonesian_rice_archipelago` |
| MAL | none | `malayan_strait_board` |
| RAJ | capital in the Indo-Gangetic area | `indo_gangetic_relief_authority` |
| BAN | none | `bengal_delta_raft_republic` |
| PAK | none | `indus_water_commands` |
| HYD | none | `deccan_greenhouse_states` |
| AST | capital on australia | `australian_grain_shield` |
| NZL | none | `polynesian_lifeboat_confederacy` |
| PNG | none | `papua_highlands_shelters` |

## Stage 2: civil-war clone rules

| Original tag | Condition | Memory |
| --- | --- | --- |
| USA | capital on north_america | `atlantic_congressional_remnant` |
| CAN | capital on north_america | `quebec_winter_republic` |
| MEX | capital on north_america | `yucatan_cenote_compact` |
| ENG | capital on europe | `scottish_hydro_parliament` |
| GER | capital on europe | `bavarian_shelter_state` |
| FRA | capital on europe | `breton_port_league` |
| SPR | capital on europe | `catalan_emergency_commune` |
| SOV | capital outside the Soviet periphery areas | `volga_ash_host` |
| JAP | capital on asia | `hokkaido_snow_administration` |
| CHI | capital on asia | `sichuan_interior_shelter` |
| RAJ | capital on asia | `deccan_greenhouse_states` |
| BRA | capital on south_america | `amazon_altered_basin` |
| ARG | capital on south_america | `patagonian_food_haven` |

## Stage 3 and 4: capital areas

Areas are tested in this order. The Ural area also holds the Russian heartland around Moscow and Leningrad.

| Area memory | States | Shared or neighbour |
| --- | --- | --- |
| `alpine_redoubt` | 3 Swiss Plateau, 151 Eastern Swiss Alps, 845 Jura Mountains, 846 Ticino, 847 Western Swiss Alps, 153 Tyrol, 848 Vorarlberg, 39 South Tyrol, 850 Trentino, 735 Savoy, 32 Alpes | neighbour `danube_ration_league` |
| `rhine_dead_cities` | 51 Rhineland, 42 Moselland, 55 Hessen, 57 Westfalen, 978 Baden, 28 Alsace-Lorraine, 56 Weser-Ems, 58 Holstein, 59 Hannover, 909 Schleswig, 61 Mecklenburg, 62 Vorpommern, 64 Brandenburg | neighbour `low_countries_polder_authority` |
| `bavarian_shelter_state` | 52 Oberbayern, 53 Niederbayern, 54 Franken, 50 Württemberg, 60 Thüringen, 65 Sachsen | shared |
| `low_countries_polder_authority` | 7 Holland, 35 Brabant, 36 Friesland, 6 Flanders, 34 Wallonia, 977 Antwerp, 980 Ardennes, 8 Luxembourg | shared |
| `scottish_hydro_parliament` | 120 Scottish Highlands, 121 Lothian, 133 Lanark, 136 Aberdeenshire, 933 Shetland Islands | shared |
| `irish_maritime_refuge` | 113 Leinster, 134 Connaught, 135 Munster, 119 Northern Ireland | shared |
| `british_emergency_isles` | 122 Wales, 123 South-West England, 125 East Anglia, 126 Greater London Area, 127 Sussex, 128 West Midlands, 129 East Midlands, 130 Yorkshire, 131 Northumberland, 132 Lancashire, 338 Gloucestershire, 931 Cumbria, 932 Isle of Man | shared |
| `breton_port_league` | 14 Brittany, 15 Normandy | shared |
| `french_loire_continuity` | 16 Ile de France, 17 Franche-Comte, 18 Champagne, 19 Aquitaine, 20 Rhone, 21 Bouches-du-Rhône, 22 Languedoc, 23 Poitou, 24 Centre, 25 Limousin, 26 Auvergne, 27 Bourgogne, 29 Nord-Pas-de-Calais, 30 Loire, 31 Midi Pyrenees, 33 Centre-Sud, 785 Picardy, 806 Pyrénées-Atlantiques, 851 Var, 1 Corsica | shared |
| `catalan_emergency_commune` | 165 Catalonia, 177 Islas Baleares | shared |
| `iberian_sun_shelters` | 41 Madrid, 166 Western Aragón, 167 Valencia, 168 Murcia, 169 Sevilla, 170 Extremadura, 171 Galicia, 172 Navarra, 173 Granada, 174 León, 175 Ciudad Real, 176 Burgos, 788 Salamanca, 789 Córdoba, 790 Asturias, 791 Valladolid, 792 País Vasco, 793 Guadalajara, 794 Eastern Aragón, 112 Lisbon, 179 Beja, 180 Porto, 181 Guarda, 795 Santarém, 118 Gibraltar | shared |
| `finnish_forest_army` | 111 Uusimaa, 145 Åland, 146 Karjala, 147 Salla, 148 Lappi, 149 Vaasa, 150 Kuopio, 722 Petsamo, 926 Turku, 927 Häme, 928 Kymi, 929 Oulu, 930 Mikkeli | shared |
| `arctic_listening_posts` | 213 Murmansk, 214 Arkhangelsk, 262 Pechora, 516 Dudinka, 824 Yamalia, 825 Nenets, 878 Khatangsky, 822 Chukotka, 875 Chukchi Peninsula, 877 Verkhoyansk, 924 Troms, 925 Finnmark, 914 Jan Mayen, 101 Greenland, 683 Nunavut | shared |
| `scandinavian_cold_councils` | 124 Gotland, 138 Skåne, 139 Småland, 140 Västergötland, 141 Södermanland, 38 Gävleborg, 666 Norrbotten, 913 Östergötland, 915 Bohuslän, 916 Dalarna, 917 Jämtland, 918 Västerbotten, 919 Värmland, 110 Oslofjord, 142 Vestlandet, 143 Trøndelag, 144 Nordland, 920 Opplandene, 921 Telemark, 922 Agder, 923 Helgeland, 37 Sjaelland, 910 Bornholm, 911 Fyn, 912 Southern Jutland, 99 Jutland, 337 Faroe Islands, 100 Iceland | shared |
| `polish_ash_republics` | 10 Warsaw, 762 Katowice, 784 Vilna, 807 Gdynia, 85 Danzig, 86 Poznań, 87 Łódz, 88 Kraków, 89 Stanisławów, 90 Kielce, 91 Lwów, 92 Lublin, 93 Wołyn, 94 Polesie, 95 Nowogródek, 96 Wilejka, 97 Białystok, 98 Płock, 63 Hinterpommern, 5 Ermland-Masuren, 763 Königsberg, 66 Lower Silesia, 67 Upper Silesia, 68 Ostmark | shared |
| `danube_ration_league` | 4 Lower Austria, 152 Upper Austria, 975 Burgenland, 976 Steiermark-Kärnten, 154 Transtisza, 155 North Transdanubia, 43 Northern Hungary, 973 Bács-Kiskun, 974 South Transdanubia, 9 Bohemia, 75 Moravia, 69 North Sudetenland, 74 Sudeten Silesia, 972 South Sudetenland, 70 Western Slovakia, 71 Eastern Slovakia, 664 Southern Slovakia, 73 Carpathian Ruthenia, 72 Trans-Olza | shared |
| `baltic_forest_brotherhoods` | 13 Pärnu, 191 Tartu, 811 Saaremaa, 812 Harju, 813 Virumaa, 12 Vidzeme, 190 Kurzeme, 808 Rīga, 809 Zemgale, 810 Latgale, 11 Kaunas, 188 Memel, 189 Žemaitija, 814 Sūduva, 815 Aukštaitija, 194 Mozyr, 204 Bobruysk, 206 Minsk, 207 Vitebsk, 241 Gomel | shared |
| `balkan_mountain_wards` | 102 North Slovenia, 103 Dalmatia, 104 Bosnia, 105 Montenegro, 106 Macedonia, 107 Serbia, 108 Morava, 109 Croatia, 45 Vojvodina, 764 West Banat, 802 Kosovo, 803 Southern Serbia, 804 Herzegovina, 853 Ljubljana, 970 Debar, 44 Central Albania, 805 Northern Epirus, 934 Shkodër, 211 Burgas, 212 Plovdiv, 48 Sofia, 801 Moesia, 46 Muntenia, 76 North Transylvania, 766 Southern Bessarabia, 77 Dobrudja, 78 Bessarabia, 79 Moldova, 80 Bucovina, 81 Oltenia, 82 Banat, 83 Crisana, 84 Transylvania, 971 Northern Dobruja | shared |
| `greek_island_synods` | 182 Crete, 184 Thrace, 185 Epirus, 186 Peloponnese, 187 Aegean Islands, 47 Attica, 731 Central Macedonia, 164 Dodecanese | shared |
| `italian_apennine_communes` | 2 Lazio, 117 Campania, 156 Calabria, 157 Abruzzo, 158 Piedmont, 159 Lombardy, 160 Veneto, 161 Emilia Romagna, 162 Tuscany, 849 Puglia, 114 Sardinia, 115 Sicily, 736 Litorale, 852 Istria, 163 Zadar, 116 Malta | shared |
| `ukrainian_bread_bunkers` | 137 Crimea, 192 Odessa, 193 Chernigov, 196 Kherson, 197 Mykolaiv, 198 Vinnytsia, 199 Proskuriv, 200 Zaporozhe, 201 Zhytomyr, 202 Kiev, 203 Cherkasy, 221 Kharkov, 225 Sumy, 226 Dnipropetrovsk, 259 Poltava, 834 Balta-Tiraspol | shared |
| `don_steppe_hetmanates` | 218 Rostov, 217 Stalingrad, 238 Volgodonsk, 245 Millerovo, 227 Stalino, 228 Voroshilovgrad, 234 Krasnodar, 235 Stavropol, 260 Voronezh, 237 Kalmykia | neighbour `ukrainian_bread_bunkers` |
| `volga_ash_host` | 239 Saratov, 251 Kuybyshev, 250 Ulyanovsky, 249 Kazan, 252 Gorky, 236 Astrakhan, 401 Balakovo, 402 Akhtubinsk, 829 Engels-Marxstadt, 256 Chuvashia, 833 Mari El, 255 Penza | shared |
| `caucasus_shelter_states` | 229 Azerbaijan, 230 Armenia, 231 Georgia, 232 Dagestan, 233 Sochi, 821 Chechnya-Ingushetia, 826 Abkhazia, 827 Kabardino-Balkaria, 828 North Ossetia | shared |
| `ural_continuity_directorate` | 581 Northern Urals, 582 Magnitogorsk, 653 Sverdlovsk, 572 Chelyabinsk, 573 Zlatoust, 398 Perm, 399 Udmurtia, 651 Ufa, 652 Orenburg, 195 Leningrad, 205 Kaluga, 208 Luga, 209 Pskov, 210 Nevel, 215 Onega, 216 Olonets, 219 Moscow, 220 Kursk, 222 Orel, 223 Tula, 224 Bryansk, 240 Belgorod, 242 Smolensk, 243 Roslavl, 244 Volkhov, 246 Rzhev, 247 Kalinin, 248 Yaroslavl, 253 Ivanovo, 254 Ryazan, 257 Tambov, 258 Lipetsk, 263 Novgorod, 264 Tikhvin, 265 Mikhaylovka, 351 Vologda, 397 Syktyvkar, 400 Kirov, 879 Kargopol, 880 Kotlas | shared |
| `siberian_rail_spine` | 571 Omsk, 570 Novosibirsk, 578 Tomsk, 568 Krasnoyarsk, 569 Khakassia, 40 Altai Krai, 654 Oyrot Region, 403 Tyumen, 580 Tobolsk, 577 Surgut, 579 Salekhard, 576 Yeniseisk, 567 Bratsk, 565 Bodaybo, 575 Kirensk, 574 Yakutsk, 876 Udachny | shared |
| `baikal_monastic_line` | 566 Irkutsk, 564 Buryatia, 563 Chita, 329 Tannu Tuva, 820 Khövsgöl | shared |
| `vladivostok_radio_port` | 408 Vladivostok, 409 Khabarovsk, 657 Birobidzhan, 561 Amur, 560 Nikolayevsk, 562 Okhotsk, 637 Kamchatka, 644 Kolyma, 874 Magadan, 655 North Sakhalin | shared |
| `steppe_convoy_republics` | 583 Kostanay, 584 Ashkhabad, 585 Navoi, 586 Alma-Ata, 587 Ust Urt, 588 Semipalatinsk, 589 Ayaguz, 590 Akmolinsk, 404 Kyzyl Orda, 405 Tashkent, 406 Guryev, 407 Ural'sk, 732 Pamir, 742 Stalinabad, 823 Karakalpakstan, 830 Bukhara, 831 Khiva, 832 Tashauz, 881 Karagandy, 882 Pavlodar, 1042 Khotan, 287 Taklamakan, 617 Urumqi, 618 Dzungaria, 619 Yarkand, 759 Kunlun Shan, 760 Dabancheng, 1040 Alxa, 756 Jiuquan, 1044 Wuwei | shared |
| `mongolian_nomad_grid` | 330 Ulaanbaatar, 817 Gobi, 818 Khovd, 819 Dornod, 1043 Pailingmiao, 611 Chahar, 612 Xilingol | shared |
| `manchurian_reactor_keeps` | 328 Kirin, 610 Jehol, 714 Heilungkiang, 715 Liaobei, 716 Liaoning, 717 Sungkiang, 761 Hulunbuir, 745 Dalian | neighbour `yellow_river_famine_councils` |
| `korean_tunnel_armies` | 1028 Hamgyong, 1029 Gangwon, 1030 Gyeongsang, 1031 Chungcheong-Jeolla, 525 Gyeonggi, 527 Pyongan-Hwanghae | shared |
| `taiwan_shelter_command` | 524 Taiwan | shared |
| `hokkaido_snow_administration` | 536 Hokkaido, 537 South Sakhalin, 555 Kuril Islands | shared |
| `japanese_shelter_archipelago` | 282 Kanto, 1018 Minami Kyūshū, 1019 Minami Tohoku, 1020 San'in, 528 Kitakyūshū, 529 San'yo, 530 Shikoku, 531 Kansai, 532 Tokai, 533 Kita-Tohoku, 534 Koshinetsu, 535 Hokuriku, 526 Okinawa | shared |
| `micronesian_storm_ports` | 633 Marshall Islands, 645 Iwo Jima, 646 Saipan, 647 Palau, 648 Marcus Island, 684 Caroline Islands, 638 Guam | shared |
| `sichuan_interior_shelter` | 605 Sichuan, 1037 Chongqing, 1041 Chengdu, 751 Liangshan, 752 Ganzi, 603 Guizhou, 748 Zunyi, 325 Yunnan, 747 Dali, 602 Hunan, 620 Hubei, 1036 Wuhan, 750 Changde | shared |
| `canton_port_commune` | 592 Guangzhou, 593 Guangdong, 594 Nanning, 599 Guangxi, 591 Hainan, 1033 Nanlu, 326 Hong Kong, 728 Guangzhouwan, 595 Fujian, 729 Macau | shared |
| `shanghai_glasshouse_syndicate` | 613 Shanghai, 1034 Suzhou, 598 Jiangsu, 596 Zhejiang, 1035 Nanjing, 606 Anhui, 600 Jiangxi, 749 Huangshan | shared |
| `yellow_river_famine_councils` | 607 Henan, 597 Shandong, 1038 Jinan, 614 Hebei, 608 Beiping, 1039 Hebei-Chahar, 609 East Hebei, 743 Qingdao, 744 Xian, 1032 Yan'an, 1046 Yulin, 622 Shaanbei, 615 Shanxi, 621 Suiyuan, 746 Ordos, 616 Ningxia, 283 Gansu, 1045 Guyuan | shared |
| `himalayan_shelter_belt` | 323 Nepal, 324 Bhutan, 985 Sikkim, 441 Kashmir, 787 Northern Kashmir, 434 Arunachal Pradesh, 322 Nagqu, 601 Chamdo, 757 Shigatse, 758 Ngari, 604 Qinghai, 753 Gannan, 754 Golog, 755 Haixi | shared |
| `mekong_greenhouse_compact` | 1076 Bangkok State, 1077 Central Siam, 1078 Eastern Siam, 289 Western Siam, 724 Southern Siam, 868 Isan, 869 Lanna, 1017 Da Nang, 1066 Cochinchina, 1067 Battambang, 1068 Bassac, 1069 Lan Chang, 286 South Annam, 670 Laos, 671 Tonkin, 741 Cambodia, 993 Kentung and Yawnghwe, 999 Federated Shan | neighbour `malayan_strait_board` |
| `philippine_island_radio_kingdoms` | 1025 Zamboanga, 1026 Northern Mindanao, 1027 Bataan, 327 Manila, 623 Luzon, 624 Central Islands, 625 Eastern Visayas, 626 Palawan, 627 Davao, 628 Western Visayas | shared |
| `indonesian_rice_archipelago` | 1022 Interior Borneo, 1047 Bangka-Belitung, 1048 Padang, 1049 Medan and Riouw, 1050 Atjeh, 1051 East Java, 1052 Bali, 1053 East Nusa Tenggara, 1054 Dutch Timor, 1055 East Kalimantan, 1056 Manado, 1058 Batavia, 334 Kalimantan Barat, 335 West Java, 667 West Nusa Tenggara, 668 The Moluccas, 672 South Sumatra, 673 Sulawesi, 738 Aru Islands, 721 East Timor | shared |
| `malayan_strait_board` | 1023 Brunei, 1024 Sabah, 1059 Limbang, 1060 Johor, 1061 Perlis-Kedah, 1062 Kelantan-Terengganu, 1063 Pahang, 1064 Perak, 333 Sarawak, 336 Kuala Lumpur, 1021 Singapore, 1065 Penang | shared |
| `papua_highlands_shelters` | 1073 Interior Papua, 523 Papua, 979 New Guinea, 737 Bismarck, 1070 Bougainville, 669 Dutch New Guinea, 1057 Dutch Papua | shared |
| `bengal_delta_raft_republic` | 430 East Bengal, 431 West Bengal, 995 Pegu, 996 Irrawaddy, 288 Magwe, 640 Mandalay, 998 Sagaing, 994 Tenasserim, 997 Arakan | neighbour `indo_gangetic_relief_authority` |
| `indus_water_commands` | 440 West Punjab, 443 Sind, 442 Peshawar, 986 East Punjab, 989 Bahawalpur, 987 Waziristan, 444 South Baluchistan, 445 Sibi, 988 North Baluchistan, 1012 Kalat | shared |
| `deccan_greenhouse_states` | 427 Hyderabad, 983 Kolhapur and Deccan, 425 Mysore, 423 Southern Madras, 424 Northern Madras, 982 Madras States, 429 Bombay, 428 Gujarat, 436 Central Provinces, 984 Bastar, 321 Goa, 320 French India | shared |
| `indo_gangetic_relief_authority` | 439 Delhi, 438 United Provinces, 435 Bihar, 433 Rajahsthan, 437 Central India, 991 Gwalior, 426 Orissa, 432 Assam, 990 Manipur | shared |
| `indian_ocean_island_arc` | 422 Ceylon, 281 Maldives, 707 Mauritius, 709 Seychelles, 710 Diego Garcia, 706 Reunion, 708 Comoro Islands, 733 Andaman, 711 Christmas Island, 712 Cocos Islands | shared |
| `anatolian_plateau_remnant` | 339 Izmir, 340 Bursa, 341 Edirne, 342 Antalya, 343 Afyon, 344 Malatya, 345 Mersin, 346 Konya, 347 Izmit, 348 Kayseri, 349 Sivas, 350 Diyarbakır, 352 Hakkari, 353 Tunceli, 354 Trabzon, 355 Samsun, 356 Kastamonu, 49 Ankara, 797 Istanbul, 798 Amasya, 800 Van | shared |
| `persian_tunnel_ministries` | 1000 East Azerbaijan, 1001 Kurdistan, 1002 Yazd, 1003 South Khorasan, 1004 North Khorasan, 266 Tehran, 410 Sistan, 411 Isfahan, 412 Fars, 413 Khuzestan, 414 Kerman, 416 Khorasan, 417 Hamadan, 418 Semnan, 419 West Azerbaijan, 420 Gilan, 421 Ilam, 1005 Qataghan, 1006 Khyber Pass, 1007 Maymanah, 1008 Qandahar, 1009 Farah, 267 Kabul, 415 Herat | shared |
| `mesopotamian_water_courts` | 1010 Al Anbar, 1011 Al Basrah, 291 Baghdad, 675 Al Hajara, 676 Mosul, 680 Deir-az-Zur | shared |
| `levant_quarantine_cities` | 554 Damascus, 677 Aleppo, 799 Hatay, 553 Lebanon, 454 Palestine, 455 Jordan, 183 Cyprus | neighbour `mesopotamian_water_courts` |
| `arabian_fuel_emirates` | 292 Nejd, 678 Rub al Khali, 679 Madinah, 854 Jawf, 855 Tabuk, 856 Asir-Makkah, 857 Al-Qassim, 858 Najiran, 859 Dammam, 293 North Yemen, 1013 Musandam, 1015 Oman, 1016 Dhofar, 294 Muscat, 656 Kuwait, 659 South Yemen, 992 Province of Aden, 658 Abu Dhabi, 765 Qatar, 1014 Bahrain, 906 Socotra | shared |
| `nile_food_command` | 907 Cairo, 446 Suez, 447 Alexandria, 452 Matrouh, 453 Sinai, 456 Aswan, 457 Eastern Desert, 551 Khartoum, 552 Western Desert | shared |
| `maghreb_solar_forts` | 458 Tunisia, 459 Algiers, 460 Constantine, 461 Casablanca, 462 Marrakech, 513 Tlemcen, 514 Algerian Desert, 665 Gabès, 448 Tripoli, 449 El Agheila, 450 Benghasi, 451 Derna, 661 Tripolitania, 662 Sirte, 663 Cyrenaica, 273 Libyan Desert, 290 Spanish Africa, 783 Sidi Ifni | shared |
| `upper_nile_cattle_federation` | 884 Upper Nile, 885 Bahr al Ghazal, 886 Blue Nile, 883 Kassala, 549 Kurdufan | shared |
| `sahel_caravan_wards` | 556 Bamako, 557 Mauritania, 786 Mauritanian Desert, 781 Niger, 782 Tombouctou, 898 Gao, 899 Kayes-Koulikoro, 778 Upper Volta, 774 Chad, 775 B.E.T., 515 Southern Sahara, 901 Borno, 902 Sokoto, 767 North Darfur, 887 South Darfur, 699 Rio de Oro | neighbour `maghreb_solar_forts` |
| `west_african_port_confederacies` | 272 Senegal, 780 Guinea, 779 Ivory Coast, 777 Togo, 776 Dahomey, 274 Ghana, 558 Lagos, 700 Sierra Leone, 701 Gambia, 298 Liberia, 296 Portuguese Guinea, 900 Benue | neighbour `cape_verde_radio_anchor` |
| `ethiopian_highland_refuge` | 271 Shewa, 835 Hararghe, 836 Bale, 837 Sidamo, 838 Illubabor-Kaffa, 839 Welega, 840 Gojjam, 841 Begemder, 842 Tigray, 843 Wello, 550 Eritrea, 908 Afar | neighbour `east_african_rail_union` |
| `congo_green_basin` | 295 Léopoldville, 538 Coquilhatville, 718 Stanleyville, 888 Lusambo, 889 Elisabethville, 890 Costermansville, 772 Middle Congo, 539 Gabon, 660 Equatorial Africa, 773 Cameroon, 297 Equatorial Guinea, 796 Cabinda | neighbour `great_lakes_mutant_marsh` |
| `great_lakes_mutant_marsh` | 768 Rwanda, 769 Burundi, 548 Uganda, 904 Nyanza-Rift Valley | shared |
| `east_african_rail_union` | 547 Nairobi, 546 Tanganyika, 905 Mombasa, 903 Garissa, 559 Somaliland, 844 Jubaland, 269 British Somaliland, 268 French Somaliland, 770 Malawi | shared |
| `south_african_continuity_mines` | 275 Transvaal, 541 Khomas, 681 Cape, 719 Natal, 893 Karas, 894 Kunene, 895 Otjozondjupa, 545 Rhodesia, 542 Bechuanaland, 981 Barotseland, 771 Zambia, 544 Lourenço Marques, 896 Manica e Sofala, 897 Zambezia-Moçambique, 891 Zambesi, 892 South West Angola, 540 Luanda | shared |
| `madagascar_isolation_state` | 543 Madagascar | shared |
| `cape_verde_radio_anchor` | 702 Cape Verde, 697 Madeira, 698 Azores, 178 Islas Canarias, 703 Ascension, 704 Saint Helena, 705 Sao Tome | shared |
| `alaska_listening_command` | 463 Alaska, 650 Attu Island, 864 Yukon Territory | shared |
| `quebec_winter_republic` | 468 Saint Lawrence, 466 Nord du Quebec, 860 Côte-Nord, 861 Saguenay, 862 Ouest du Quebec, 863 Maurice | shared |
| `northern_shield_shelters` | 682 Northern Ontario, 866 Districts of Ontario, 472 N.W Territories, 464 Nova Scotia, 465 New Brunswick, 331 Newfoundland, 332 Labrador, 730 St Pierre and Miquelon | shared |
| `cascadian_hydro_league` | 385 Oregon, 386 Washington, 387 Idaho, 473 British Columbia, 740 Vancouver Island, 739 Haida Gwaii, 471 Prince Rupert | shared |
| `california_aqueduct_republic` | 378 California, 379 Nevada | shared |
| `sonoran_water_board` | 376 New Mexico, 377 Arizona, 380 Utah, 483 Sonora, 482 Chihuahua, 484 Baja California, 480 Coahuila, 481 Durango, 277 Mexico City, 478 Jalisco, 479 Tamaulipas, 485 Guerrero, 476 Oaxaca, 477 Veracruz | shared |
| `texan_oil_fortresses` | 375 Texas, 374 Oklahoma, 371 Louisiana, 370 Mississippi, 372 Arkansas | shared |
| `great_lakes_ice_authority` | 393 Michigan, 394 Wisconsin, 395 Illinois, 396 Indiana, 261 Ohio, 391 Minnesota, 276 Southern Ontario | shared |
| `prairie_grain_authority` | 383 Kansas, 384 Nebraska, 389 North Dakota, 390 South Dakota, 392 Iowa, 388 Montana, 381 Wyoming, 382 Colorado, 373 Missouri, 467 Manitoba, 469 Saskatchewan, 470 Alberta, 865 N. Saskatchewan, 867 Northern Manitoba | shared |
| `appalachian_tunnel_compact` | 360 Pennsylvania, 816 West Virginia, 369 Kentucky, 368 Tennessee, 363 North Carolina, 364 South Carolina, 365 Georgia, 367 Alabama | shared |
| `atlantic_congressional_remnant` | 357 New England, 358 New York, 359 New Jersey, 361 Maryland, 362 Virginia, 366 Florida | shared |
| `hawaiian_relay_kingdom` | 629 Hawaii, 630 Johnston Atoll, 631 Midway Island, 632 Wake Island | shared |
| `caribbean_port_chain` | 315 Cuba, 318 Haiti, 319 Dominican Republic, 686 Puerto Rico, 689 Jamaica, 690 Northern Bahamas, 693 Southern Bahamas, 691 Trinidad, 692 Windward Islands, 308 Leeward Islands, 694 French Caribbean, 695 Curaçao, 696 Bermuda | shared |
| `yucatan_cenote_compact` | 474 Yucatan, 475 Chiapas, 313 Guatemala, 311 British Honduras, 312 Honduras, 314 El Salvador, 317 Nicaragua, 316 Costa Rica | shared |
| `colombian_mountain_corridors` | 306 Cundinamarca, 486 Meta, 493 La Libertad, 304 Panamá, 685 Panamá Canal | shared |
| `venezuelan_fuel_remnant` | 307 Miranda, 488 Bolivar, 489 Zulia | shared |
| `guiana_rain_stations` | 309 Suriname, 310 French Guiana, 687 British Guyana | shared |
| `atacama_observatory_state` | 506 Antofagasta, 951 Arica y Tarapacá, 952 Atacama | neighbour `andean_sky_republics` |
| `andean_sky_republics` | 303 Lima, 492 Arequipa, 947 Tacna-Moquegua, 302 La Paz, 305 Ecuador, 649 Galapagos Islands, 279 Santiago, 508 Tucumán, 511 Mendoza, 959 Los Andes, 960 San Juan y La Rioja, 487 Santa Cruz | shared |
| `amazon_altered_basin` | 495 Amazonas, 961 Amazon, 962 Amazon, 963 Amazon, 964 Amazon, 965 Amazon, 966 Amazon, 967 Amazon, 968 Amazon, 969 Rio Branco, 938 Pará, 939 Amapá, 940 Acre, 942 Guaporé, 491 Loreto, 494 Ucayali, 490 Pastaza | shared |
| `patagonian_food_haven` | 507 Magallanes, 949 Aysén, 950 Araucanía, 512 Río Negro, 953 Tierra del Fuego, 954 Santa Cruz, 955 Chubut, 299 Falkland Islands | shared |
| `la_plata_port_compact` | 278 Buenos Aires, 300 Montevideo, 956 Santa Fe, 510 Región Mesopotámica, 958 San Luis y La Pampa, 945 Cerro Largo, 946 Paysandú | shared |
| `paraguay_river_holdfast` | 301 Paraguay, 504 Punta Porá, 509 Chaco Austral, 957 Formosa, 688 Chaco Boreal | shared |
| `brazilian_interior_leagues` | 280 Mato Grosso, 496 Minas Gerais, 497 Maranhão, 498 Rio Grande do Norte, 499 Bahia, 500 Rio de Janeiro, 501 São Paulo, 502 Rio Grande do Sul, 503 Santa Catarina, 505 Goiás, 935 Ceará, 936 Pernambuco, 937 Piauí, 941 Tocantins, 943 Espírito Santo, 944 Paraná | shared |
| `australian_grain_shield` | 285 New South Wales, 517 Victoria, 518 Tasmania, 519 South Australia, 520 Northern Territory, 521 Queensland, 522 Western Australia, 674 Central Australia, 870 North West Australia, 871 South West Australia, 872 North Queensland, 873 South West Queensland, 1074 Central Western Australia, 1075 West Queensland | shared |
| `polynesian_lifeboat_confederacy` | 726 Samoa, 1072 American Samoa, 636 Fiji, 641 Tahiti, 948 Easter Island, 270 Pitcairn Island, 1079 Auckland, 1080 Marlborough, 1081 Otago, 284 Wellington, 723 Canterbury | shared |
| `pacific_radio_chain` | 642 Phoenix Island, 727 Line Islands, 1071 Vanuatu, 635 New Caledonia, 634 Solomon Islands, 734 Santa Cruz Islands, 725 Nauru, 639 Gilbert Islands, 643 Ellice Islands | shared |
| `antarctic_listening_government` | 720 South Georgia | neighbour `patagonian_food_haven` |
| `kerguelen_weather_state` | 713 Kerguelen | shared |
