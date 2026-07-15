# Event 006: Scotland and Wales Packages

This document owns the gameplay contract for Independence Wave packages IW-001 Scotland (`SCO`) and IW-002 Wales (`WLS`). Both reuse their installed vanilla tags, country definitions, history, characters, cores, and ideology flag families. Event 006 does not replace a living Scotland or Wales, and neither package is part of the Soviet-collapse system.

## Runtime setup

The regional allocator retains the existing package geography:

| Package | Tag | Anchor and capital | Compact territory | Extended territory | Archetype | Depth |
|---|---|---|---|---|---|---|
| IW-001 Scotland | `SCO` | 121 Lothian | 133 Lanark | 120 Highlands, 136 Aberdeenshire, 933 Shetland | port or island | regional |
| IW-002 Wales | `WLS` | 122 Wales | none | none | mountain or frontier | regional |

The setup adapters run only after the shared origin transaction has published the exact package, anchor, and former-host scopes. Each adapter then:

1. verifies the original tag, package ID, region, depth, archetype, owned and controlled anchor, living former host, and exact capital;
2. creates its institutional council and territorial commander only when those tokens do not already exist, then reapplies the exact HOI4-painted portrait set;
3. ensures civilian economy, export focus, and volunteer-only laws without overwriting other history content;
4. initializes package politics and party names;
5. assigns the reviewed full Event 006 focus framework in place of the vanilla generic tree;
6. publishes constitutional, popular/labor, traditional/cultural, and emergency-military routes while explicitly withholding patron-client and radical-sovereignty routes;
7. publishes all four former-host policy routes, a distinct internal power struggle, league participation, and the accepted formable families;
8. loads and materializes the package's existing force mapping only after the guarded command-roster proof succeeds;
9. enables the origin-locked AI profile; and
10. recruits the package's three distinct institutional advisors; and
11. proves every package field again before the shared transaction may mark runtime setup successful.

IW-001 verifies the existing p1 territorial-defense package with military tradition 70, including its audited navy and air inheritance behavior. IW-002 verifies the existing p2 mountain-frontier package with military tradition 60.

## Institutional authority and command

Scotland uses `SCO_independence_wave_civic_convention` as its multi-route civic institution and `SCO_independence_wave_territorial_commandant` as its emergency head and corps commander. Wales uses `WLS_independence_wave_national_council` and `WLS_independence_wave_mountain_commandant` in the equivalent roles.

These are guarded runtime institutions, not replacements for vanilla characters. Setup applies exact sprites with `set_portraits`, including separate `156x210` large commander portraits and `50x67` army thumbnails. All eight masters were generated independently in a restrained HOI4-painted style, processed through the canonical leader workflow, decoded from their installed DDS files, and reviewed against the canonical vanilla portrait references.

Scotland also recruits a Shipping Authority Commissioner, Industrial Reconstruction Secretary, and Territorial Defense Planner. Wales recruits a Bilingual Civil Service Commissioner, Coal and Rail Organizer, and Mountain Defense Planner. Each advisor has a distinct `65x67` dossier card produced from its own ImageGen master by the advisor-card processor, a substantial role-specific trait, a concrete hiring cost, and route-aware AI weighting.

The static advisor records are recruited by hidden setup event `chaosx.nr6.10` inside the frozen release chain. The calling package adapter then proves all three records exist before it can publish setup success; no scripted effect or on action contains `recruit_character`.

## Founding pressures and lifecycle ideas

All tuning lives in `common/script_constants/006_independence_wave_scotland_wales_constants.txt`.

Scotland exposes `independence_wave_sco_shipping_authority`, starting at 35 and stabilizing at 65. Below the threshold it carries `sco_divided_coastal_command`; at or above the threshold it carries `sco_north_atlantic_state_service`.

Wales exposes `independence_wave_wls_north_south_integration` and `independence_wave_wls_bilingual_service`, starting at 30 and 40. Both must reach 65 to replace `wls_divided_valleys_administration` with `wls_bilingual_coal_and_rail_compact`.

Each package can hold at most one lifecycle idea and one selected-government idea. Changes clamp between 0 and 100 and immediately refresh the lifecycle.

The decision-category descriptions show these package pressures beside the shared Event 006 Legitimacy, Recognition, Capacity, Security, and Instability values.

## Government settlements

The shared focus framework chooses one government route. A package-owned timed decision then installs the corresponding government, public party name, authority, popularities, and idea.

| Route | Scotland | Wales |
|---|---|---|
| constitutional | Constitutional Convention | Constitutional National Council |
| popular/labor | Workers' Commonwealth Charter | Workers' Valleys Charter |
| traditional/cultural | Crown and Convention Settlement | Cultural Guardians Settlement |
| emergency military | Emergency Territorial Directorate | Emergency Mountain Directorate |

Scotland registers `traditional_authority_vs_assembly` as its internal power struggle. Wales registers `labor_councils_vs_ministries`.

## Package projects

Projects use the shared Event 006 cost and duration tables. Civil work consumes command power, manpower, and a civilian factory; security work consumes command power, equipment, manpower, or army experience according to its tier; diplomacy consumes command power and convoys or trains; regional congresses pay the strategic bundle. Package projects serialize, occupy time, cancel if the exact package or capital proof fails, and apply explicit failure pressure where work can collapse.

Scotland reconnects the central belt, organizes Firth convoys, settles British asset ledgers, and unifies territorial command. Its regional choice can remain with the Celtic Cooperation State or pivot to the North Atlantic Compact before formable discovery. A later maritime conference publishes the shared formation request.

Wales reconnects north-south rail, establishes bilingual services, guards coalfield corridors, and settles the British property board. Its accepted family is the Celtic Cooperation State, followed by a Celtic council and shared formation request.

The conference effects publish a bounded shared formable operation through the selected-family registry. The shared registry keeps FORM01 and FORM02 fail-closed until their exact X-ending identity adapters, complete flag triplets, territory policies, and integration transactions are certified; the package does not invent a fallback tag.

## Package focus branches

The full Event 006 tree contains five origin-gated focuses for each package.

Scotland's branch reconnects the central belt, charters North Atlantic shipping, settles crown and convention, convenes a Celtic maritime conference, and founds the North Atlantic State Service.

Wales's branch reconnects north and south, charters coal and rail, establishes the bilingual service, secures mountain corridors, and convenes the Celtic Council.

These branches supplement rather than replace the shared framework's government, economy, defense, diplomacy, former-host, league, formable, and high-chaos lanes. Their rewards change package pressures and shared values; they do not provide repeating free formations.

## AI behavior

Scotland prioritizes infantry, support equipment, artillery, trains, convoys, infrastructure, and dockyards, restrains early war declarations, and raises coastal defense and army priority under severe former-host threat.

Wales prioritizes infantry, support equipment, artillery, trains, infrastructure, and mountain defense, follows the same founding restraint, and raises army and fortification priority under severe former-host threat.

Both profiles are locked to the exact original tag, package ID, setup-complete flag, and package AI flag.

## Vanilla preservation

No country, history, character, flag, state-history, or portrait file is overridden. Scotland and Wales continue using their installed ideology flag triplets. The Welsh flag family carries the documented caveat that its familiar green-white layout was officially adopted in 1959; reuse here is the accepted registered-tag behavior, not a claim of 1936 authenticity.

The package files never activate, remove, duplicate, or rename vanilla `WLS_restore_y_wladfa_decision`. Its standalone vanilla decision category therefore coexists with the narrowly visible Event 006 Wales category.

## Visual assets and sprite wiring

The package reuses these already registered Event 006 interface sprites:

- ideas: `independence_wave_founding_identity`, `independence_wave_improvised_government`, and `independence_wave_fragmented_command` from the existing Event 006 idea interface definitions;
- decisions: `GFX_decision_independence_wave_government_actions`, `GFX_decision_independence_wave_depot_border_actions`, `GFX_decision_independence_wave_former_host_negotiations`, `GFX_decision_independence_wave_army_integration_actions`, and `GFX_decision_independence_wave_formable_proclamation`;
- focuses: `GFX_goal_independence_wave_founding_administration`, `GFX_goal_independence_wave_infrastructure_authority`, `GFX_goal_independence_wave_recognition_diplomacy`, `GFX_goal_independence_wave_constitutional_state`, `GFX_goal_independence_wave_army_integration`, and `GFX_goal_independence_wave_league_congress`.

The unique package portraits are registered in `interface/006_independence_wave_region_01_portraits.gfx` and installed under `gfx/leaders/006_independence_wave/`. The advisor dossier sprites are registered in `interface/006_independence_wave_nwe_advisors.gfx` and installed under `gfx/interface/ideas/006_independence_wave/advisors/`. The authoritative user-directed HOI4 portrait pass, including source portraits, processed PNGs, DDS decodes, reference review sheets, hashes, and manifests, lives under `docs/assets/006_independence_wave/portrait_regeneration_2026_07_15/`; advisor production evidence lives under `docs/assets/006_independence_wave/nwe_advisor_dossiers_2026_07_15/`.

Scotland and Wales retain their installed vanilla flag triplets because these are reused vanilla countries, not newly created Event 006 tags. Any future royal Scottish cosmetic route must remain traditional-route-only. Wales receives no invented pre-1959 fallback.

## Readiness and future work

Gameplay adapters, projects, focus hooks, ideas, AI, localisation, exact setup validation, unique leaders, commander thumbnails, and complete advisor boards are implemented. Readiness remains intentionally withheld from the static package registry because FORM01 and FORM02 still require certified X-ending identity adapters, complete ImageGen flag triplets, exact territory policies, and operational integration transactions. Wales's installed vanilla flag retains its 1959-layout caveat in the asset audit. No dormant vanilla history file receives a content-readiness flag.

Future depth can add bilateral Scottish-Welsh conference events and route-specific cabinet succession without bypassing the package gate or replacing living countries.
