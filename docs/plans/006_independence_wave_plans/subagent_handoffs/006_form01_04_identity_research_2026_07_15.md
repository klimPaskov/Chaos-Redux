# Event 006 FORM-01 through FORM-04 identity research handoff

Date: 2026-07-15

Owner: `event6_form01_04_research`

Scope: research and implementation guidance only. This handoff does not register tags, change specifications, wire gameplay, generate images, or certify any formable as operational.

## Recommended identity decisions

| Family | Recommended final player-facing name | Primary X tag | Identity form | Confidence |
|---|---|---|---|---|
| `FORM-01` | `Celtic Congress` | `KCX` | consent-based league identity on the proposing carrier | high for the name, medium for its use as a political identity |
| `FORM-02` | `North Atlantic Union` | `NUX` | maritime federal or league identity on the proposing carrier | medium because the Event 006 membership is narrower than the historical proposal |
| `FORM-03` | `Confederation of the Low Countries` | `LCX` | decentralized confederal identity on Wallonia or Frisia | medium because the exact state name is an alternate-history synthesis |
| `FORM-04` | `Rhenish League` | `RLX` | negotiated Rhine league formed by Rhineland and Saar | high for the league precedent, medium for a 1930s revival |

These names are intentionally different from the four working labels. They also avoid exact vanilla identities. Vanilla already supplies `Benelux Federation`, `United Provinces`, `United Kingdom of the Netherlands`, `Leo Belgicus`, `Rhenish Republic`, `Rheinland-Pfalz`, and several other Rhenish ideology names. The exact vanilla evidence is in:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/localisation/english/countries_cosmetic_l_english.yml:427`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/localisation/english/countries_cosmetic_l_english.yml:808`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/localisation/english/countries_l_english.yml:4644`

No recommended identity may be replaced with one of those vanilla identities. No family may use a fallback tag, fallback state, fallback name, or unresearched flag.

## Cross-install X-tag audit

The candidate audit covered vanilla, all 122 installed Workshop directories, all four local mod directories, the `chaos_redux_music` link target, and all eight installed Workshop ZIP archives. It checked country definitions, tag aliases, static cosmetic assignments, identity localisation namespaces, gameplay references, filenames, flags, and archive entries. The audit found 117 hard-occupied X-ending country tags.

| Family | Primary | Clean reserves | Rejected candidates |
|---|---|---|---|
| `FORM-01` | `KCX` | none assigned | `CCX` is already reserved by Event 6 package `IW-055`; it cannot be reused by a formable identity. |
| `FORM-02` | `NUX` | `NBX`, `NCX` | `NAX` is occupied by Workshop item `1827273767`. `ATX` is Event 006 Venice. `AUX` is a Windows device basename and cannot safely own portable files. `NOX` is technically free but is already a visible TNO Greek route acronym. |
| `FORM-03` | `LCX` | `LFX`, `LWX` | none in the reviewed shortlist |
| `FORM-04` | `RLX` | `RNX`, `RHX` | none in the reviewed shortlist |

Collision evidence for the two most tempting rejected tags:

- `NAX` is defined at `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/1827273767/common/country_tags/00_countries.txt:269` and has its own history, flags, characters, and localisation.
- `ATX` is defined at `common/country_tags/006_independence_wave_countries.txt:22` for `IW-020` Venice.

The clean status is a snapshot of the installed environment on 2026-07-15. Re-run the same full audit immediately before registration because a Workshop or local mod installation can invalidate a reservation.

Parent collision correction: the original research recommendation used `CCX`,
but the accepted 206-row candidate registry already assigns that identifier to
`IW-055`. The corrected `KCX` identity was checked against every candidate
registry proposal/resolution, vanilla, all installed Workshop mods, sibling
mods, tag aliases, cosmetic assignments, localisation namespaces, filenames,
flags, gameplay references, and all eight installed Workshop ZIP archives. No
collision was found. `CCX` remains owned exclusively by `IW-055`.

## Shared integration rules for all four families

The following rules implement the accepted Event 006 formable framework rather than a maximal annexation model:

1. A living country enters the congress ledger only after an explicit invitation and a recorded consent result.
2. A consenting Event 006 member can choose full integration or continued autonomous membership when the family allows both.
3. Full integration can end an Event 006 origin only through the existing bounded formable transaction. It grants immediate cores only on the member's certified compact states.
4. Autonomous members retain their tag, capital, tree, forces, and sovereignty. Their states do not become cores of the carrier.
5. Living vanilla countries and protected route overlays remain autonomous unless a later specification grants explicit authority to do otherwise.
6. Disputed, coarse, mixed, optional, conquered, and extension states receive staged claims, local settlements, or later integration. They do not receive automatic cores at formation.
7. The proposed tag is an identity adapter input. A cosmetic identity on the carrier is preferred when that preserves living members more safely than a new country registration.
8. Missing territory, a missing member, or a missing transport link blocks formation. No nearby state or tag substitutes for it.

## FORM-03 priority research: Confederation of the Low Countries

### Final identity and historical frame

Recommended final name: `Confederation of the Low Countries`

Recommended adjective: `Low Countries`

Recommended primary identity tag: `LCX`

This is a new constitutional name grounded in the historic regional term Low Countries and the project's decentralized member settlement. It is not presented as an attested historical state. The name is preferable to `Low Countries Federation` because `confederation` accurately signals that Belgium, the Netherlands, and Luxembourg can remain sovereign partners.

The [Rijksmuseum Leo Belgicus map](https://www.rijksmuseum.nl/en/collection/object/Map%2Bof%2Bthe%2BSeventeen%2BNetherlandish%2BProvinces%2Bin%2Bthe%2BShape%2Bof%2Bthe%2BBelgic%2BLion--901991b1f47334fff1a8f1f9e69a1a4a) documents a long-standing symbol of desired unity among the Netherlandish provinces. It supports the shared regional frame, but it must not become the new country's name or principal emblem because vanilla already uses `Leo Belgicus` as a unified Netherlands cosmetic identity.

`Benelux` is also unavailable. The official [Benelux history](https://www.benelux.int/en/information-for-citizens/benelux-union/about-us/history/) and the [2019 Benelux prime ministers' declaration](https://www.benelux.int/files/9415/5427/7383/20190402_Decl_Benelux_Summit_EN_Final.pdf) place the customs convention on 5 September 1944. Vanilla already supplies a Benelux faction, unification route, and `Benelux Federation` cosmetic. Event 006 must not duplicate that identity under a new X tag.

### Eligible founders and member logic

The operational carrier must be one of:

- `IW-006` Wallonia, `AFX`, anchored in state 34.
- `IW-007` Frisia, `AGX`, anchored in state 36.

Core congress members are:

- Wallonia, `AFX`.
- Frisia, `AGX`.
- A living Belgium carrying the vanilla `BEL_flanders` overlay as the Flemish member.

Recommended formation gate:

- The carrier is `AFX` or `AGX`.
- At least one additional core congress member consents.
- The carrier has a verified land, river, port, or treaty connection to every consenting member. Wallonia and Frisia alone therefore need access through a consenting Belgian or Dutch corridor rather than silently annexing it.
- The family cannot be formed by the vanilla `BEL`, `HOL`, and `LUX` trio alone. That result belongs to vanilla Benelux or United Netherlands content.

Integration choices:

- `AFX` and `AGX` may fully integrate by consent. Only their certified anchors become immediate cores.
- Belgium with `BEL_flanders` remains Belgium. States 6 and 977 remain Belgian member territory. The overlay, focus tree, living tag, capital, and vanilla route effects remain intact.
- A living Netherlands or Luxembourg may join later as an autonomous associate. They are not founding Event 006 packages and their territory is not transferred.
- A member that withholds consent is excluded from the settlement. Its states are neither annexed nor claimed automatically.

### Exact territory and capital policy

| Status | State IDs | Treatment |
|---|---|---|
| Walloon integrated anchor | 34, Wallonia | immediate core only if `AFX` is carrier or consents to full integration |
| Frisian integrated anchor | 36, Friesland | immediate core only if `AGX` is carrier or consents to full integration |
| Flemish autonomous member | 6, Flanders and 977, Antwerp | never transferred from a living `BEL` under the current preservation rules |
| Dutch autonomous associates | 7, Holland and 35, Brabant | no transfer and no core without a later accepted specification |
| Luxembourg autonomous associate | 8, Luxembourg | no transfer and no core without a later accepted specification |
| Walloon extension candidate | 980, Ardennes | staged local settlement only. It is not an automatic FORM-03 core. |

Capital rule:

- If `AFX` is the carrier, retain state 34 as the capital.
- If `AGX` is the carrier, retain state 36 as the capital.
- Brussels in state 6 can host congress events, but it cannot become the X-tag capital while living Belgium retains the state.

This decentralized rule is deliberate. It keeps the confederation distinct from vanilla Benelux unification and avoids consuming Belgium to obtain a prestigious capital.

### Identity and sensitivity caveats

- State 36 is a coarse HOI4 state. Its vanilla victory points include Utrecht, Arnhem, Groningen, and Leeuwarden. The package name Frisia must not be used to claim that every inhabitant of state 36 is Frisian.
- The constitution needs Dutch, French, West Frisian, and German-speaking rights where those communities enter the member system. The official [Belgian flag and regional symbol page](https://www.belgium.be/en/about_belgium/country/belgium_in_nutshell/symbols/flags) documents distinct Flemish, Walloon, German-speaking, and Brussels symbols. They must remain member symbols rather than being collapsed into one ethnicity.
- The [Friesland flag explanation](https://www.friesland.nl/nl/blog/historie/de-vrijheidsgeest-van-de-friezen) ties the seven pompeblêden to historic Frisian regions and the blue and white stripes to waters. Do not universalize that provincial flag across Wallonia or Flanders.
- `Low Countries` is a regional and geographic identity, not a single ethnic label.

### Flag evidence and ImageGen-ready direction

No attested flag exists for this exact confederation. Do not reuse the Belgian tricolor, the Dutch tricolor, the Frisian provincial flag, a Benelux flag, or a Leo Belgicus flag. Each would either privilege one member or approach an existing vanilla identity.

Recommended official ImageGen brief:

> Create a clean flat vector flag in the exact 41:26 HOI4 proportion. Use a deep river navy field, approximately `#163A5F`. Place one broad white three-armed river fork across the center. Three separate, gently wavy white bands enter from the hoist at one quarter, one half, and three quarters of the flag height. They converge into one white band before reaching the fly. Keep every band thick enough to remain visible at 10 by 7 pixels. Use only two solid colors. No lion, rooster, water-lily leaves, crown, shield, text, map labels, stars, border, gradients, fabric, pole, folds, lighting, scenery, distress, paint texture, or mockup.

The three branches represent the Rhine, Meuse, and Scheldt delta and the continued existence of separate member institutions. This is an explicitly alternate-history design, not a claimed historical flag.

Distinct route or ideology flags: none supported. Use one confederal flag for every accepted route. Do not create a Benelux, United Provinces, United Netherlands, or Leo Belgicus variant.

### FORM-03 unresolved facts

- The exact constitutional name is an evidence-based design synthesis rather than an attested state title.
- The family remains blocked until the parent accepts the autonomous Belgium rule and implements a corridor test that does not seize Belgian or Dutch territory.
- State 36 remains a coarse gameplay compromise. No narrower installed state binding was found.
- No final flag has been generated or reviewed at HOI4 sizes.

## FORM-01: Celtic Congress

### Final identity and historical frame

Recommended final name: `Celtic Congress`

Recommended adjective: `Celtic`

Recommended primary identity tag: `KCX`

The [National Library of Wales Celtic Congress archive](https://archives.library.wales/index.php/celtic-congress-archive-2) records that the idea arose in 1900, the association was re-established in 1917, and E. T. John renamed it the Celtic Congress. It promoted the languages and cultures of the six Celtic countries, had no central organization, and moved its annual congress among member countries. The [National Library of Ireland catalogue](https://catalogue.nli.ie/Record/vtls000510979) also preserves the 1901 Pan-Celtic Congress material and its multi-country representation.

This evidence supports `Celtic Congress` only as a consent-based league or congress identity. It does not support a unitary `Celtic Cooperation State`, a single Celtic ethnicity, or compulsory territorial union.

### Eligible founders and member logic

Certified Event 006 founding packages:

- `IW-001` Scotland, `SCO`.
- `IW-002` Wales, `WLS`.
- `IW-004` Brittany, `BRI`.
- `IW-003` Cornwall, `ACX`, only after a unique installed state binding is accepted.

Recommended formation gate:

- At least three founding councils consent.
- At least one Gaelic-side council is represented by Scotland.
- At least one Brythonic council is represented by Wales, Brittany, or a valid Cornwall.
- Every fully integrating package has a valid compact territory and every autonomous member has a valid diplomatic relation to the carrier.

Ireland and the Isle of Man were part of the historical six-country concept, but neither is an Event 006 founding package in the accepted FORM-01 row. A living Ireland may be invited later as an autonomous associate only after the specification explicitly adds that route. The Isle of Man has no certified package or unique state here. Neither absence may be concealed in localisation.

Integration choices:

- A consenting Event 006 member can fully integrate its certified compact states.
- A council can instead remain an autonomous member with access, guarantees, and congress participation.
- The congress must not core a member that remains autonomous.
- The event text should describe national councils, language guarantees, maritime defense, and rotating sessions. It should not describe tribes, racial unity, or an ancient restored empire.

### Exact territory and capital policy

| Package | Integrated compact | Staged or excluded territory |
|---|---|---|
| Scotland | states 121, Lothian and 133, Lanark | states 120, Scottish Highlands, 136, Aberdeenshire, and 933, Shetland Islands remain staged Scottish extensions |
| Wales | state 122, Wales | none beyond a separately accepted settlement |
| Brittany | state 14, Brittany | none beyond a separately accepted settlement |
| Cornwall | no current certified state | state 123 is `South-West England` in the installed build and cannot be used as a unique Cornish core |

Capital rule:

- Retain the proposing carrier's capital.
- If an identity adapter requires an explicit capital reset, use state 121 for a Scottish carrier, state 122 for a Welsh carrier, or state 14 for a Breton carrier.
- Do not invent a permanent pan-Celtic capital. Congress sessions can rotate through member capitals in event text.

### Flag evidence and ImageGen-ready direction

No prewar flag recognized by all Celtic Congress branches was found. A secondary vexillological summary of the [Pan-Celtic flag](https://www.crwflags.com/fotw/flags/int-celt.html) dates the best-known Robert Berthelier design to the 1950s, which makes it unsuitable as a 1936 historical flag. The same source reports that the 1901 Congress adopted heather as a Celtic flower. Use the heather only as a documented shared symbol and clearly label the resulting flag as alternate history.

Recommended official ImageGen brief:

> Create a clean flat vector flag in the exact 41:26 HOI4 proportion. Use three vertical panels with width ratio 1:2:1. The two outer panels are deep forest green, approximately `#22543D`. The wide center panel is warm ivory, approximately `#F1E8CF`. Center one oversized, highly simplified heather-purple cluster, approximately `#70456C`, made from three broad bell-shaped blossoms on one short dark green stem. The emblem must read as heather, not a generic five-petal flower. Keep the cluster large enough for a 10 by 7 pixel reduction. No triskele, Celtic knot, harp, cross, crown, shield, text, runes, member flags, gradient, fabric, pole, folds, lighting, scenery, distress, painterly texture, or mockup.

Distinct route or ideology flags: none supported. A crown, labor, emergency, or cultural route does not justify inventing a different pan-Celtic flag.

### FORM-01 unresolved facts

- The name is authentic for a cultural congress, not for a centralized sovereign state. If the implementation demands a unitary annexing country, the final name is unresolved and must return to design.
- The historic Ireland and Isle of Man participation is not represented by accepted founding packages.
- Cornwall remains ineligible until a unique current-map state exists.
- No final flag has been generated or reviewed at HOI4 sizes.

## FORM-02: North Atlantic Union

### Final identity and historical frame

Recommended final name: `North Atlantic Union`

Recommended adjective: `North Atlantic`

Recommended primary identity tag: `NUX`

The [Library of Congress Clarence K. Streit papers](https://findingaids.loc.gov/repositories/19/resources/3337) document Streit's advocacy of an Atlantic Union of democracies and Federal Union, Inc. beginning in 1939. Cambridge's [history of Streit and the Atlantic federal movement](https://www.cambridge.org/core/books/clarence-streit-and-twentiethcentury-american-internationalism/57FD4A714BCE2E15F5E0642D20DC379F) describes `Union Now` as a 1939 proposal for a federation of North Atlantic democracies. A 1950 [United States Department of State memorandum](https://history.state.gov/historicaldocuments/frus1950v03/d128) uses the phrase North Atlantic Union directly.

The historical proposal was much broader than the Event 006 island network. The name is therefore grounded, but the membership is alternate history and must not be described as Streit's actual plan.

### Eligible founders and member logic

Certified or conditionally certified founders:

- `IW-012` Iceland, `ICE`, state 100, only when `ICE` is not already living as another identity.
- `IW-011` Faroe Islands, `AKX`, state 337 in the current installed map, still restricted to its accepted scenario route.
- `IW-182` Newfoundland, `GZX`, state 331.
- `IW-001` Scotland, `SCO`, compact states 121 and 133.

No other island package is certified for FORM-02 in the reviewed matrix. Shetland is a Scottish extension state, not a separate founding country. Acadia belongs to a different Atlantic family direction and must not be silently added.

Recommended formation gate:

- At least three eligible members consent.
- Newfoundland is represented so the result has a real western Atlantic member.
- At least two of Iceland, the Faroes, and Scotland are represented.
- Every member has a port and the carrier has a verified convoy connection to every member.

The member-count rule is an implementation recommendation rather than a historical fact. It keeps the union from collapsing into a bilateral annexation and gives the shared convoy, air, and naval defense systems a real network.

Integration choices:

- Full integration transfers only the consenting package compact.
- Autonomous membership preserves the country and grants the agreed shipping, basing, and defense relations without cores.
- A living `ICE` cannot be overwritten by a duplicate Iceland package.
- The scenario-only Faroe package cannot be promoted to automatic release by this formable.

### Exact territory and capital policy

| Package | Integrated compact | Staged or excluded territory |
|---|---|---|
| Iceland | state 100, Iceland | none |
| Faroe Islands | state 337, Faroe Islands | scenario-only participation under the current package disposition |
| Newfoundland | state 331, Newfoundland | state 332, Labrador, only when already lawfully attached to `GZX` or accepted through a later settlement |
| Scotland | states 121, Lothian and 133, Lanark | states 120, 136, and 933 remain staged Scottish extensions |

Capital rule for a fully integrated union tag:

1. State 100, Reykjavík, if Iceland fully integrates.
2. State 331, St. John's, if Newfoundland fully integrates and Iceland does not.
3. State 121, Edinburgh, if Scotland fully integrates and neither earlier state is available.
4. State 337, Tórshavn, only in the accepted Faroe scenario and only if no earlier capital is available.

If the carrier remains a league identity with autonomous members, retain the carrier's existing capital instead. No historical fixed capital was found for this narrower island union.

### Flag evidence and ImageGen-ready direction

No common flag for the Event 006 member set was found. The design must therefore be an openly alternate-history synthesis based on documented member flags:

- The [Government of the Faroe Islands](https://www.government.fo/en/foreign-relations/representations-of-the-faroe-islands-abroad/the-representation-of-the-faroe-islands-in-london/flag-of-the-faroe-islands) dates Merkið to 1919 and its British recognition to 25 April 1940.
- [Alþingi's official Icelandic flag colors](https://www.althingi.is/lagas/156a/2016032.html) document the blue, white, and red palette.
- The [Scottish Government](https://www.gov.scot/publications/scotlands-future/pages/15/) identifies the Saltire as Scotland's national flag.
- Memorial University's [Newfoundland pre-Confederation flag history](https://www.heritage.nf.ca/articles/society/pre-confederation-flags.php) records the Union Jack as Newfoundland's official flag from 1931.

Recommended official ImageGen brief:

> Create a clean flat vector flag in the exact 41:26 HOI4 proportion. Use a deep Atlantic navy field, approximately `#102E4A`. Add one broad white saltire from corner to corner. Overlay one narrow red Nordic cross, approximately `#B72F3B`, with its vertical arm centered at one third of the flag width and its horizontal arm centered at one half of the flag height. The red Nordic cross remains above the white saltire at every intersection. Use only three solid colors and hard edges. The strokes must remain distinct at 10 by 7 pixels. No stars, compass, ship, anchor, crown, coat of arms, text, member badges, gradient, fabric, pole, folds, lighting, scenery, distress, painterly texture, or mockup.

This combines the Saltire and Union-derived geometry with the Nordic cross tradition without copying any one member flag.

Distinct route or ideology flags: none supported. The union flag should remain a shared maritime symbol across constitutional, neutral, labor, and emergency routes.

### FORM-02 unresolved facts

- No historical union had this exact island membership.
- The historical federal-union proposal included much larger democracies and cannot be quoted as an island-state blueprint.
- The Faroes remain scenario-only despite state 337 existing in the current installed map.
- No historical common flag or fixed capital was found.
- No final flag has been generated or reviewed at HOI4 sizes.

## FORM-04: Rhenish League

### Final identity and historical frame

Recommended final name: `Rhenish League`

Recommended adjective: `Rhenish`

Recommended primary identity tag: `RLX`

The Landschaftsverband Rheinland history portal records the [1254 Rheinischer Städtebund](https://rheinische-geschichte.lvr.de/chronicle/1254), founded by Mainz, Worms, Oppenheim, and Bingen for public peace and later expanded to other cities and princes. This is a stronger basis for a negotiated river league than either the working `Rhine Federation` or the Napoleonic Confederation of the Rhine.

The 1923 separatist episode supplies a modern Rhenish autonomy context, but not a popular mandate. The [German Historical Museum](https://www.dhm.de/lemo/kapitel/weimarer-republik/innenpolitik/separatistenbewegung) records the proclamation of a Rhenish Republic, French support, and decisive opposition from much of the local population. Event writing must preserve that controversy.

`Rhenish Republic` cannot be used. It is the existing vanilla democratic name for `RHI`.

### Eligible founders and member logic

Certified founders:

- `IW-008` Rhineland, `RHI`, state 51.
- `IW-010` Saar, `AJX`, state 42, only when its compact is valid and the German host retains a protected remnant.

Recommended formation gate:

- Both `RHI` and `AJX` are living and consent.
- Both certified states are controlled by the consenting members.
- The Rhine corridor and the member capitals remain connected.
- A stronger living Germany does not dominate the corridor under the matrix's exclusion rule.

Bavaria is not a FORM-04 founder. No additional Rhine state is certified in the reviewed package matrix. States in Hesse, Westphalia, Alsace-Lorraine, or the Palatinate must not be added without a new package and state-binding decision.

Integration choices:

- A negotiated full league can integrate states 51 and 42 and core both after consent.
- A member that remains autonomous keeps its state, tag, and capital. The carrier then receives a league identity rather than the member's territory.
- A military settlement does not create automatic cores on conquered German states. Occupied extensions remain claims or integration projects.

### Exact territory and capital policy

| Status | State IDs | Treatment |
|---|---|---|
| Rhineland founder | 51, Rhineland | immediate core after full consensual integration |
| Saar founder | 42, Moselland in current English state localisation | immediate core after full consensual integration. This state is much broader than the Saar alone. |
| Any other Rhine state | none certified | excluded until a later specification names and researches it |

Recommended capital: state 42, using Koblenz as the constitutional congress seat. The current vanilla state history places province 3423, Koblenz, in state 42. The [Rhineland-Palatinate archive exhibition](https://www.landeshauptarchiv.de/fileadmin/user_upload/Gemeinsame_Dateien/Download/Ausstellungen/Banner_9.pdf) documents the 23 October 1923 proclamation in front of the Koblenz palace. The choice is historically intelligible but remains a gameplay decision inside a coarse state that also contains Trier and Saarbrücken.

### Flag evidence and ImageGen-ready direction

The Bad Kreuznach city archive preserves a [green, white, and red 1923 separatist flag](https://www.bad-kreuznach.de/buergerservice/politik-und-verwaltung/haus-der-stadtgeschichte-und-stadtarchiv/projekte/publikationen/demnaechst-im-haus-der-stadtgeschichte/die-ebernburger-separatistenfahne-von-1923/). Its three horizontal bands are also the basis of vanilla `RHI_democratic.tga`, so the Event 006 league must not copy that arrangement.

Recommended official ImageGen brief:

> Create a clean flat vector flag in the exact 41:26 HOI4 proportion. Use three equal vertical bands, green at the hoist, warm white in the center, and red at the fly. Use approximately `#16834A`, `#F2F0E6`, and `#C52D34`. Place one thick cobalt-blue vertical wavy line, approximately `#245B86`, down the center of the white band to represent the Rhine. The blue line must be wide enough to remain one clear pixel at 10 by 7 pixels. Use only four solid colors and hard edges. No horizontal tricolor, eagle, crown, shield, fasces, city seal, French emblem, text, border, gradient, fabric, pole, folds, lighting, scenery, distress, painterly texture, or mockup.

This is an alternate-history league design derived from the sourced Rhenish colors and the river corridor. It is intentionally different from the vanilla RHI flag.

Distinct route or ideology flags: none supported. The 1254 city league, the 1658 alliance, the 1806 Confederation of the Rhine, and the 1923 separatists were different political projects. Mixing their emblems into route flags would manufacture a false continuity.

### FORM-04 unresolved facts

- The 1254 league's first named cities were Mainz, Worms, Oppenheim, and Bingen. They do not map neatly onto the certified Event 006 states 51 and 42. `Rhenish League` is therefore a documented constitutional model for revival, not a claim that FORM-04 restores the exact medieval membership.
- State 42 is a coarse Moselland state and is not a unique Saar state.
- The 1923 green, white, and red colors have a separatist and French-protectorate association. Event text and asset notes must not present them as a universally accepted Rhenish symbol.
- The high-chaos route has no defensible separate historical identity or flag.
- No additional Rhine member state is certified.
- No final flag has been generated or reviewed at HOI4 sizes.

## Asset production handoff

All four final flags must be created later with the official ImageGen workflow required by `chaos-redux-event-assets`. Historical files and web images are reference inputs, not final shipped art.

For every accepted tag:

1. Generate a clean flat source in the exact flag proportion.
2. Remove any ImageGen shading, texture, edge noise, fake lettering, or unintended symbols during the approved asset-processing pass.
3. Verify the design at normal 82 by 52, medium 41 by 26, and small 10 by 7 sizes.
4. Export the required TGA triplet under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.
5. Add ideology-specific files only when an implemented route actually selects a defensible separate flag. No distinct ideology design is supported by this handoff.
6. Record the source links, prompt, generated source, processed PNG, DDS or TGA outputs, contact sheet, and checksum in the Event 006 asset manifest.

No prompt may ask for cloth, waving fabric, folds, a flagpole, sky, battlefield, painted canvas, distressed paper, photorealism, fake text, or invented heraldry.

## Required local implementation references consulted

Primary Event 006 sources:

- `docs/specs/006_independence_wave_specs/matrices/006_formable_family_registry.csv`
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`
- `docs/specs/006_independence_wave_specs/research/006_tag_collision_and_reuse_audit.md`
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_current_installed_map_binding_audit_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_nwe_package_implementation_map.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_nwe_country_package_audit_2026_07_15.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wallonia_frisia_package_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_formable_registry_architect_handoff_2026_07_15.md`

Offline Paradox wiki pages consulted:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding
- Country creation
- Cosmetic tag modding
- Graphical asset modding

Vanilla documentation and precedents consulted:

- `documentation/script_concept_documentation.md`
- `documentation/effects_documentation.md`
- `documentation/triggers_documentation.md`
- vanilla country-tag and cosmetic-tag definitions
- vanilla `set_cosmetic_tag`, release, and event-target precedents
- vanilla state history and English state localisation for every state listed above

## Completion boundary

This research tranche answers the identity, membership, territory, capital, tag-candidate, and flag-direction questions for FORM-01 through FORM-04. It does not make any family operational. No gameplay file, localisation file, specification, skill, catalog, spreadsheet, or image was changed.

Remaining implementation blockers are the parent decision on each recommended identity, formal tag reservation, family-specific identity and integration adapters, final localisation, official ImageGen flag production, asset manifest wiring, and family-specific validation.

No research fallback or fabricated historical identity was used. Every point that lacks direct historical support is labeled as an alternate-history design recommendation or an unresolved fact.
