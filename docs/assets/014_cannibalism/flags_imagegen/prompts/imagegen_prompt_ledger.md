# Event 014 Flag Imagegen Prompt Ledger

## Provenance

- Generation date: 2026-07-12
- Generation mode: built-in `image_gen` tool
- Use-case slug: `stylized-concept`
- Output form: one 1536x1024 source sheet per family, arranged as a 3x2 grid with five occupied cells and one blank cell
- Cell order: base, communism, democratic, fascism, neutrality, blank
- Source mode: generated fictional artwork
- Post-processing boundary: local processing only crops the selected cells, forces opaque RGBA, resizes, writes TGA, assembles contact sheets, and calculates validation data

The final selected CBL sheet is the second CBL generation. The first CBL attempt was rejected because its route pattern could be read as a real national cross. The rejected output was not copied into the project and is not used by any final asset.

## Selected generations

| Family | Built-in output filename | Project source sheet | SHA256 |
|---|---|---|---|
| `CBA` | `exec-901965f1-7b80-4076-805f-31a23efab3b0.png` | `source_sheets/CBA_source_sheet.png` | `F006A92B77044945CDA7BCBAB2D7B1D4656E697001D70E2982A70072F47251CE` |
| `CBB` | `exec-5860641a-afd8-4bd0-a24b-01ef7cf00490.png` | `source_sheets/CBB_source_sheet.png` | `0566E28AA6E747070A7105E7C282BC42BF356B131882975FBC4AD07E48C2C7E0` |
| `CBC` | `exec-b99d936d-a73f-418c-848b-0cc55d71cf3a.png` | `source_sheets/CBC_source_sheet.png` | `A63A8257C497C61066C531CD3A75B9EC03DE13EA9DE1D25083FE93454B9B8FD9` |
| `CBD` | `exec-030bd6c4-7a83-4007-a419-69df7973264f.png` | `source_sheets/CBD_source_sheet.png` | `E386F985709C1EED9D45670D3EE84D022BE3B045F3B481504135E8549FD4170D` |
| `CBE` | `exec-ea22acee-9ee6-4ddf-b4f0-4147c1d7df0a.png` | `source_sheets/CBE_source_sheet.png` | `817747B2134863097ACAFC649B26D80C58BDF162E4554A59EFA3DCE66B211863` |
| `CBF` | `exec-96b93d42-cb20-4b02-9229-896e1ebd39cc.png` | `source_sheets/CBF_source_sheet.png` | `89804991300B77C1B4002ACE4575FA8CD275605B3D6B84DCBEDFE77D0A02C32F` |
| `CBG` | `exec-834e50c9-f2c6-4a1b-80e8-96c31dcb6734.png` | `source_sheets/CBG_source_sheet.png` | `9CEE17362E5CC0250634ECC7FD6E275BE4BE1C16E441D9C6858B2A7CFC85EC7D` |
| `CBH` | `exec-93276c2b-c66a-4e85-aae0-ddd732e1d198.png` | `source_sheets/CBH_source_sheet.png` | `ED401F691DA54C42D70B5D3C12D562B5A59BAC649557D8FA9A19700D3E104BC9` |
| `CBL` | `exec-704ff686-7b0d-4c94-b2f4-b165158a7e40.png` | `source_sheets/CBL_source_sheet.png` | `25B8E54F0E70E388C28EC1EE15C6080FE785FEA7482083D062BF794FA5878AEB` |
| `CBL_CENTRAL_COMMAND` | `exec-e0afa198-7a82-4fcc-acd9-7aa9eddb5832.png` | `source_sheets/CBL_CENTRAL_COMMAND_source_sheet.png` | `0C89516CB81FFB1DCCDA53B7F7506EE92DC4C5F32B81010DDC6690A81195866D` |
| `CBL_HOST_CONFEDERATION` | `exec-ce2bcbc5-1198-42f8-b0cb-6cd7dba2b23d.png` | `source_sheets/CBL_HOST_CONFEDERATION_source_sheet.png` | `FC3EC4420DF5162F59BFA3534A0662530CEFE81F1F7EB0FEEC6ED549BA6002E9` |
| `CBL_RITUAL_STATE` | `exec-f064fee4-e2c8-41b7-864b-7c532910b100.png` | `source_sheets/CBL_RITUAL_STATE_source_sheet.png` | `123D66E783D05A13B125E2095684A36CC976EEE5146D398222CC3A4DD2E6A75B` |
| `ZZZ_CANNIBALISM_HANNIBAL` | `exec-2f79773b-eeea-4bee-9d4e-fc4c21acd5aa.png` | `source_sheets/ZZZ_CANNIBALISM_HANNIBAL_source_sheet.png` | `6F3323E3F6439BDE50A7F4CCE3164C9FEF0DB1D39AEC4C522EBC0D30D78D086B` |

## Shared prompt contract

Every selected generation used the following production contract, with minor sentence-order differences between the parallel batches:

```text
Use case: stylized-concept
Asset type: source sheet for five fictional Hearts of Iron IV country flag compositions
Create one clean 3-by-2 production source sheet containing exactly five separate, fully painted flag designs; leave the sixth cell empty dark gray.
The five occupied cells are read left-to-right, top-to-bottom and map exactly to:
1 base ideology-neutral form,
2 communism collective command,
3 democratic civic resistance,
4 fascism rigid militarization,
5 neutrality warlord neutrality.
Every panel must be a genuinely different composition and object arrangement, not a palette swap or the same emblem rearranged.
Use a neutral charcoal-gray sheet with wide uniform gutters. Every occupied cell is an isolated complete flag artwork with no label and no content crossing gutters.
Use image-generated painted cloth flag designs, bold heraldic silhouettes, distressed 1930s screen-print texture, and a fictional gore-heavy atmosphere without depicting a person or victim.
Keep each central silhouette broad, high-contrast, and legible when reduced to 10x7 pixels.
Use soot black, dried-blood red, bone ivory, tarnished metal, and the named family accent. Color balance may vary, but compositions and objects must differ.
Hard constraints: exactly five occupied panels and one blank sixth panel; no readable text, letters, numbers, labels, captions, watermarks, people, faces, bodies, victims, recognizable persons, real political emblems, extremist insignia, national coats of arms, Indigenous regalia, sacred imagery, tribal symbols, recognizable national symbols, swastikas, stars, sickles, fasces, eagles, laurels, borrowed heraldry, or leader portraits.
Avoid palette swaps, duplicated emblems, simple geometric placeholder flags, gradients-only designs, tiny detail, faux UI, and panel labels.
```

## Family prompt blocks

### CBA

```text
Family: CBA, fictional cannibal Island Host.
Motifs: island reef, heavy hooked butcher blade, torn convoy rope, blood-red surf.
Panel 1: reef enclosing a hook above red surf.
Panel 2: multiple torn ropes converging on one hook and reef.
Panel 3: broken convoy rope forming a defensive harbor around the reef, smaller hook pushed outward.
Panel 4: vertical hook dominating crossed rope lines and jagged reef stakes.
Panel 5: lone oversized hook and snapped rope over storm surf.
Accent: deep ocean blue-gray.
```

### CBB

```text
Family: CBB, fictional Black Lighthouse Island Host.
Motifs: black lighthouse, jaw-shaped harbor, signal lamp, broken chain.
Panel 1: black lighthouse centered inside a blunt jaw-shaped harbor, one broken chain below.
Panel 2: four broken chains converge into a shared signal lamp beneath the lighthouse.
Panel 3: harbor walls and multiple small signal lamps resist an inward-closing jaw; lighthouse offset but still clear.
Panel 4: severe vertical lighthouse beam splits a rigid jaw-harbor, chain links aligned like barricades.
Panel 5: lone leaning lighthouse and one huge snapped chain over a dark blood-red tide.
Accent: cold signal-amber.
```

### CBC

```text
Family: CBC, fictional Breach Siege Commune.
Motifs: breached wall, ration bowl, siege stakes, blood-marked masonry.
Panel 1: wide breached wall cradling one empty ration bowl above a red masonry stain.
Panel 2: several bowls linked behind a shared broken wall, siege stakes radiating outward.
Panel 3: repaired civic wall segments circle a bowl while outward-facing stakes guard the breach.
Panel 4: tall parallel siege stakes dominate a narrow wall breach and regimented masonry blocks.
Panel 5: solitary bowl balanced on a jagged breach with two massive warlord stakes.
Accent: ash-gray stone.
```

### CBD

```text
Family: CBD, fictional Tunnel Siege Commune.
Motifs: tunnel lamp, chained gate, buried knives, collapsed city arch.
Panel 1: one tunnel lamp burning under a collapsed arch above a chained gate.
Panel 2: multiple buried knives point inward to a shared lamp behind broken communal chain links.
Panel 3: opened chain gate and two lamps guide a path through the collapsed arch, knives turned outward.
Panel 4: rigid vertical gate bars, one hard lamp, and buried knives aligned like teeth under the arch.
Panel 5: lone lamp hanging from a broken arch, oversized buried knife and snapped gate chain below.
Accent: smoky lamp amber.
```

### CBE

```text
Family: CBE, fictional Scavenged March Host.
Motifs: scavenged wagon wheel, marching blade, torn field map with no readable markings, muddy track.
Panel 1: broken wagon wheel rolling over a muddy track with one short marching blade through its hub.
Panel 2: several mismatched wheel spokes and blades converge into one shared wheel above intersecting muddy tracks.
Panel 3: split wheel becomes two protective half-wheels around an open muddy road; blades face outward and map scraps sit behind.
Panel 4: rigid upright marching blade bisects a severe wagon wheel, straight track bands below.
Panel 5: lone crooked wheel, oversized cleaver-like marching blade, and one torn blank map corner on a winding track.
Accent: mud brown.
```

### CBF

```text
Family: CBF, fictional Rail March Host.
Motifs: rail spike, horse jaw bone, depot flame, severed transport line represented only as a broken rail.
Panel 1: horse jaw bone grips one rail spike above a broken transport rail and depot flame.
Panel 2: multiple rail spikes form a rough shared ring around one flame, jaw fragments binding the ring.
Panel 3: two open jaw halves guard a repaired rail gap while small depot flames mark either side.
Panel 4: one towering rail spike and regimented parallel rails dominate a compressed jaw silhouette.
Panel 5: lone angled jaw bone, huge spike, broken rail ending in a wild depot flame.
Accent: furnace orange.
```

### CBG

```text
Family: CBG, fictional Prison Host.
Motifs: barred mouth as an abstract iron jaw, key, prison tower, cut transfer ledger shown as torn blank paper with no writing.
Panel 1: barred iron mouth beneath one prison tower, key crossing a torn blank ledger sheet.
Panel 2: several keys and torn blank ledger sheets converge on a shared barred mouth and central tower.
Panel 3: opened barred mouth frames a key pointing outward from the prison tower, ledger halves pushed aside.
Panel 4: rigid vertical prison tower and bars dominate; identical keys aligned below like teeth.
Panel 5: lone tilted prison tower, oversized key, snapped mouth bar and one torn blank paper corner.
Accent: oxidized prison green-gray.
```

### CBH

```text
Family: CBH, fictional Transfer Prison Host.
Motifs: abstract shackled gauntlet hand, transport gate, stamped file represented by a bold blank wax-like blot with no glyph, broken guard baton.
Panel 1: armored gauntlet clenches a broken shackle before a transport gate; one snapped baton below.
Panel 2: several shackles converge around a shared gauntlet and blank file blot, gate reduced to a low arch.
Panel 3: opened transport gate, broken shackle halves and an outward-pointing snapped baton frame a blank file sheet.
Panel 4: rigid gate bars dominate vertically, one gauntlet and aligned baton fragments below.
Panel 5: lone oversized gauntlet, one hanging shackle and diagonal snapped baton over a tilted gate.
Accent: bruised purple-gray.
```

### CBL

```text
Family: CBL, ordinary unified cannibal identity revealed publicly.
Core motif in every panel: one visibly empty rectangular command table connected to several thick blood-red routes.
Show no weapons, bowls, chairs, maps, map outlines, crosses, circular rings, sunbursts, shields, or religious/national-looking layout.
Panel 1: asymmetrical empty table low-left, three unequal routes bend sharply toward three different edges.
Panel 2: empty table centered high, seven unequal routes converge from staggered edge points like a rough network.
Panel 3: empty table centered low, routes arc outward in an open broken fan, leaving a broad unbound gap.
Panel 4: empty table centered, five routes forced into strict parallel vertical channels above and below, but do not form a cross.
Panel 5: tilted empty table at far left, one thick winding route dominates toward the right while three smaller routes terminate abruptly.
Accent: dark route red on mostly charcoal and muted bone fields. Keep route layouts asymmetrical and avoid any flag pattern resembling a real national flag.
```

### CBL_CENTRAL_COMMAND

```text
Family: CBL_CENTRAL_COMMAND, rigid unified command cosmetic identity.
Core motif: one blade and one chain binding every route into a rigid vertical command.
Panel 1: one upright broad blade over an empty junction, with a single chain binding four routes.
Panel 2: many route ends converge into one chain ring around the shared vertical blade.
Panel 3: broken outer chain links open paths away from a central blade laid horizontally as a defensive barrier.
Panel 4: dominant vertical blade and taut chain ladder force every route into strict parallel columns.
Panel 5: one massive crooked blade, one heavy chain and a single dominant route crushing smaller broken routes.
Accent: cold steel. No map shapes or political emblems.
```

### CBL_HOST_CONFEDERATION

```text
Family: CBL_HOST_CONFEDERATION, fictional unified Host Confederation cosmetic identity.
Core motif: four unequal Host weapons—heavy hook, broad cleaver, rail spike, snapped guard baton—joined around one common empty table while retaining clearly different shapes.
Panel 1: four unequal weapons point inward toward a small empty table from four uneven angles.
Panel 2: weapons overlap into a rough shared knot above the table, with four separate handles still visible.
Panel 3: table forms an open shelter; the four weapons face outward at different angles, leaving an unclosed gap.
Panel 4: weapons forced into a rigid stacked vertical rack through the table, each silhouette still distinct.
Panel 5: one large hook dominates near a tilted table while the other three mismatched weapons remain separate at the margins.
Accent: muted host ochre.
```

### CBL_RITUAL_STATE

```text
Family: CBL_RITUAL_STATE, fictional administrative punishment state; no borrowed sacred imagery.
Motifs: state ledger shown as thick blank book with no writing, punishment table, sealed bowl closed by a plain iron lid with no emblem, ordered chains.
Panel 1: closed blank ledger above an empty punishment table, plain lidded bowl and one ordered chain below.
Panel 2: several chain ends converge on a shared blank ledger resting beside the sealed bowl on the table.
Panel 3: open blank ledger and unlocked chain frame the table; the sealed bowl is pushed outward as a civic barrier.
Panel 4: strict vertical ledger, table, lidded bowl, and parallel chain ranks aligned like an administrative column.
Panel 5: lone tilted punishment table with oversized closed ledger, heavy chain, and sealed bowl off balance.
Accent: dull ledger blue-gray. No seals with symbols, runes, altars, ritual circles, religious forms, or readable marks.
```

### ZZZ_CANNIBALISM_HANNIBAL

```text
Family: ZZZ_CANNIBALISM_HANNIBAL, fictional public Wendigo-merge command cosmetic identity.
Do not depict a creature, person, portrait, antlers, headdress, mask, totem, dreamcatcher, feather, rune, or Indigenous/sacred motif.
Motifs: frost-cracked animal jaw bone, winter command chain, ruined road, dark red ice.
Panel 1: frost-cracked jaw bone arches over a ruined road while one chain disappears into dark-red ice.
Panel 2: several frozen chain ends converge through a shared jaw around a central broken road junction.
Panel 3: split jaw halves and broken chain open a guarded passage along the ruined winter road.
Panel 4: rigid vertical frozen chain dominates, jaw fragments lock the road into straight icy ranks.
Panel 5: lone tilted jaw bone, one massive snapped chain and a winding ruined road vanishing into blood-dark ice.
Accent: glacial blue-gray and dark-red ice.
```
