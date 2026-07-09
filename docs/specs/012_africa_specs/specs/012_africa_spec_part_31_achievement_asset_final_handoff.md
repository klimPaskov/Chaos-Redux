# 012 Africa spec part 31, achievement and asset final handoff

This file consolidates achievement tracking and asset handoff needs for the canonical package. Achievement titles remain direction-only. Working ids are implementation identifiers, not final player-facing titles.

## Achievement tracker rules

Achievements should be difficult, route-aware, and not automatic. No achievement should unlock just because Event 012 fired. Every achievement needs a visible or hidden tracking plan, disqualifiers, icon direction, and route coverage.

## Canonical achievement set

| Working id | Visibility | Eligible player | Required route or state | Unlock conditions | Disqualifiers | Icon motif |
| --- | --- | --- | --- | --- | --- | --- |
| `012_africa_charter_without_chains` | visible | Africa unifier | Federal Charter | federate major regions through voluntary or autonomous member routes | coercive annexation, member secession war | charter seal over open hands |
| `012_africa_congress_of_liberation` | visible | Africa unifier | Revolutionary Congress | liberate at least five colonial-held African countries and keep League cohesion positive | puppet all liberated states, fail liberation defense | printing press and broken chain |
| `012_africa_crowns_many_oaths` | visible | Africa unifier | Crown of the Continent | restore ten polities and integrate or federate them without succession collapse | use unvetted extra obscene names, force all restored polities into direct annexation | crown above regalia and stela |
| `012_africa_continental_command` | visible | Africa unifier | Continental Command | win a continent-scale war and complete command district integration | lose command obedience crisis, trigger three rival blocs | field radio and crossed supply lines |
| `012_africa_sacred_soil_no_burnt_fields` | visible | Africa unifier | Sacred Soil | complete rural legitimacy and land protection while keeping extraction backlash low | Deep Green disaster weaponization, coerced land seizure | field, river, and tree line |
| `012_africa_black_star_safe_harbor` | visible | Africa unifier | Black Star Return | complete three diaspora return lanes without settlement failure | land seizure, major lane collapse | black star above dock crane |
| `012_africa_dockworkers_two_oceans` | hidden | Africa unifier | Black Star Return | operate Atlantic and Indian Ocean lanes together | lose either lane to blockade | two anchors and a star |
| `012_africa_league_of_equals` | visible | Africa unifier | Federal or mixed route | keep five strong members as autonomous federal members while unifying Africa | direct annexing all members | ring of regional shields |
| `012_africa_no_scramble_left` | visible | Africa unifier | any grounded route | secure all African regions and survive outside-power reaction without losing a region | accept old colonial partition settlement | torn treaty and continental shield |
| `012_africa_askum_to_kilwa` | visible | Africa unifier or restored polity route | regional restoration | have Aksum and Kilwa both active as respected League members or federated regions | annex either before confidence threshold | stela and dhow |
| `012_africa_rivers_remember` | hidden | Africa unifier | Nile, Niger, Congo, Zambezi project | complete integration projects on four major river-region groups | fail any river project twice | four river lines |
| `012_africa_the_ports_stayed_open` | visible | Africa unifier | diaspora or Swahili route | keep five strategic ports supplied during a major war | lose convoy lane or port mission | port light and convoy |
| `012_africa_south_africa_reconciled` | visible | RSA continental side | RSA branch | win the Allied RSA civil war and force peace with the Allies through continental side | loyalist victory or postwar purge route | split shield restored |
| `012_africa_the_allies_signed` | hidden | RSA continental side | RSA branch | win civil war while Allied great power is still active and secure peace without full Allied conquest | exploit by leaving Allies before event | treaty pen and southern shield |
| `012_africa_ten_thrones_no_prison` | hidden | Crown route | restored polities | restore ten major polities and keep them out of direct annexation for a fixed review period | any restored polity revolt | ten small crowns |
| `012_africa_desert_did_not_break` | visible | Africa unifier | Sahel and Sahara | integrate Sahara and Sahel routes with low attrition mission failure | fail water or caravan projects repeatedly | oasis and rail |
| `012_africa_federation_under_fire` | visible | Africa unifier | Federal Charter | maintain League cohesion during a great-power war | member exit during war | shield under artillery burst |
| `012_africa_no_foreign_collars` | visible | Africa unifier | independent diplomacy | unify without becoming a puppet, dominion, or client of outside power | high patronage dependency | broken foreign collar |
| `012_africa_green_door` | hidden | Africa unifier | Deep Green | open Deep Green route after grounded Sacred Soil route without ordinary AI enabling it | reveal nonhuman route before high-chaos gate | forest door glow |
| `012_africa_not_a_caricature` | hidden technical audit achievement or test flag | development only unless desired | high-chaos safety | all nonhuman countries use actual nonhuman classification and generated assets | any human restored polity uses nonhuman template | mask crossed out |
| `012_africa_stone_host_marches` | hidden | high-chaos route | Living statue route | activate living-statue host and win a defensive war in heritage region | use host outside allowed region before gate | stone bird and spear |
| `012_africa_fever_stayed_fictional` | hidden | high-chaos route | disease route | contain fictional disease blowback after using disease pressure | real pathogen naming or uncontrolled self-collapse | sealed green vial, no real label |
| `012_africa_world_is_one` | hidden | final continent power | world-end | become the terminal world identity after all required continent unifiers exist and fight | bypass continent unifier requirements | globe seal |
| `012_africa_one_without_cores` | hidden | Africa unifier | any route | reach full continental political control before all regions become full cores | instant continent core shortcut | continent with staged rings |
| `012_africa_every_member_counted` | visible | Africa unifier | League system | process every African League member through a final outcome state | stale member flags or unresolved target states | ledger with shields, no readable text |

## Tracking flags and variables

| Tracking item | Purpose |
| --- | --- |
| `africa_achievement_coercion_used` | disqualifies consensual routes |
| `africa_achievement_member_exit_happened` | tracks League instability |
| `africa_achievement_return_lane_failed` | blocks safe harbor route |
| `africa_achievement_land_seizure_used` | blocks settlement route |
| `africa_achievement_rsa_continental_won` | RSA civil war branch |
| `africa_achievement_allies_peace_signed` | Allied peace branch |
| `africa_achievement_deep_green_opened` | high-chaos route |
| `africa_achievement_nonhuman_audit_safe` | development or hidden safety check |
| `africa_achievement_world_route_valid` | terminal route sanity |
| `africa_achievement_region_project_count` | counts completed region projects |
| `africa_achievement_restored_polity_count` | counts active restored polities |
| `africa_achievement_voluntary_member_count` | counts voluntary federal members |
| `africa_achievement_lane_count` | counts completed return lanes |
| `africa_achievement_port_security_count` | counts protected strategic ports |
| `africa_achievement_river_project_count` | counts major river projects |

## Asset families

Every visible route and achievement needs assets. Do not derive all icons from one master image. Focus icons, idea icons, decision icons, and achievement icons are separate asset types.

### Focus icon families

| Family | Focus groups | Motif | Count direction |
| --- | --- | --- | --- |
| continental opening | shared opening, route congress, League call | continent seal, congress, rail, port | 8 to 12 |
| federal charter | federal route, member votes, autonomy guarantees | charter, shields, handshake, assembly | 10 to 14 |
| revolutionary congress | liberation, anti-colonial courts, worker and soldier organs | press, red-green banners, rifles, courts | 10 to 14 |
| crown route | restored polities, court diplomacy, regnal gates | crown, stool, stela, regalia | 10 to 14 |
| command route | army districts, depots, war planning | radio, depot, field column, supply road | 10 to 14 |
| sacred soil | rural legitimacy, land protection, human spiritual route | river, field, tree, shrine, local guard | 8 to 12 |
| Black Star | shipping, return, settlement, industry | star, ship, crane, workshop | 10 to 14 |
| Deep Green | high-chaos forest, nonhuman, disaster | storm, forest door, animal silhouette, oracle | 8 to 12 |
| post-unification | Scramble, continent wars, world route | treaty, globe, continent emblems | 8 to 12 |

### Idea and spirit icons

| Idea family | Motif | Source mode |
| --- | --- | --- |
| early legitimacy stress | cracked seal, crowded hall, supply ledger without text | generated |
| League cohesion | ring of shields, shared standard | generated |
| autonomy guarantee | local shield under continental seal | generated |
| coercion backlash | clenched fist and broken district marker | generated |
| diaspora settlement | house, toolkit, dock, school | generated |
| high-chaos blowback | storm forest, sealed vial, cracked river stone | generated |
| RSA civil war | split southern shield | generated |
| restored polity pride | region-specific symbol based on source research | sourced or generated depending on evidence |

### Decision and category icons

| Category | Size | Motif |
| --- | --- | --- |
| Charter League | 32x32 and category size from repo pattern | charter seal |
| Regional integration | 32x32 | staged rings and rail |
| Diaspora lanes | 32x32 | ship and star |
| Scramble reaction | 32x32 | torn treaty |
| High-chaos demands | 32x32 | storm leaf or oracle eye |
| RSA civil war | 32x32 | split shield |
| Restored polity management | 32x32 | small crown and regional shield |

### Super-event images

| Working key | Source mode | Direction |
| --- | --- | --- |
| `se_012_africa_continental_reveal` | generated period documentary | congress, soldiers, workers, flags, rail or port, no map-only scene |
| `se_012_africa_black_star_return` | generated or sourced if using real Garvey material | port arrival and settlement work |
| `se_012_africa_scramble_reaction` | generated or sourced diplomatic art | old powers reacting to lost colonial structure |
| `se_012_africa_deep_green_reveal` | generated high-chaos | impossible forest weather and nonhuman forces |
| `se_012_africa_world_is_one` | generated world-end | globe seal and continent powers |

### Flags and portraits

Historical flags and portraits must be sourced when real or attested. Fictional route flags, high-chaos flags, nonhuman portraits, and symbolic councils can be generated.

| Group | Source mode |
| --- | --- |
| existing country base flags | preserve vanilla or repo flags unless route transformation requires cosmetic tag |
| restored historical flags | source or historically grounded, document uncertainty |
| fictional ideology variants | generated or designed as alternate-history flags |
| real leaders | sourced portraits only |
| fictional leaders and councils | generated portraits |
| nonhuman leaders | generated portraits |
| route emblems | generated |
| achievement icons | generated, with grey and not-eligible variants in implementation |

## Asset acceptance

Asset handoff is incomplete unless every asset has a source file, processed PNG, final DDS path, sprite name, target size, source mode, manifest entry, and GFX handoff. Achievement icons need completed, grey, and not-eligible variants if the achievement system requires them.
