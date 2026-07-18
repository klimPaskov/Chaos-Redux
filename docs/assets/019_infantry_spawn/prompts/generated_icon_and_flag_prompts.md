# Event 019 Generated Icon and Flag Prompt Record

## Shared icon direction

Each icon atlas used a clean chroma-key green background and an exact row-major grid with no text. The requested style was compact HOI4-era military-political illustration: dark iron, brass, oxblood, field olive, parchment, clear silhouettes, restrained highlights, no real-world insignia, no copyrighted characters, and no embedded frames supplied by the model. Final borders, alpha, dimensions, and DDS conversion were handled locally.

## Focus atlases

The base prompt requested nine distinct 3×3 focus emblems with laurel, shield, medallion, banner, or heraldic silhouettes; every cell had to remain readable at 100×88 and had to differ in composition rather than palette alone.

### A — foundation

1. hold the first ground
2. count the surviving host
3. inventory the seized districts
4. restore a chain of orders
5. name the future host
6. mark the muster depots
7. reopen captured workshops
8. open the living corridor
9. count every obligation

### B — hierarchy

1. crown the claimant
2. assign command estates
3. one voice over the host
4. convene the host council
5. bind the district councils
6. no host abandoned
7. obey the family instinct
8. mark the family domain
9. end the old chain of rule

### C — army expansion

1. quiet the fragmented columns
2. outlast the former state
3. make an army of the host
4. concentrate the host
5. scatter the bands
6. arm the captured auxiliaries
7. a method fit for the host
8. read the neighboring frontiers
9. issue the submission terms

### D — predator and zombie

1. absorb the conquered districts
2. turn the host outward
3. become the regional predator
4. zombie scavenge the abandoned barracks
5. zombie number the devouring bands
6. zombie teach the base dead to muster
7. zombie keep the hunger in column
8. zombie a realm of base dead
9. ghost mark the first anchors

### E — ghost and golem

1. ghost call a second procession
2. ghost bind the procession to place
3. ghost thin the hunger for life
4. ghost a pale dominion
5. golem recover the broken coal
6. golem reconstruct the binding marks
7. golem turn workshops into foundries
8. golem share the living pattern
9. golem a march of living stone

## Decision atlases

The base prompt requested nine distinct 3×3 decision symbols with a compact centered object or action, minimal fine detail, no text, and strong readability at 33×32. Repeated gameplay actions intentionally reuse one processed icon after generation.

### A — core board

1. open muster ledger
2. cycle formation lots
3. audit formation
4. assign territorial roles
5. standardize a formation
6. supervised demobilization
7. emergency integration
8. establish muster district
9. appoint integration staff

### B — preservation and requests

1. preserve specialists
2. recognize emergency reserve
3. training cycle
4. reserve rail corridor
5. request field reinforcement
6. request mobile reserve
7. request territorial defenders
8. request specialist firepower
9. request numbers

### C — anomaly and family

1. request discipline
2. request anything
3. request anomalous family
4. open cantonment
5. appoint liaison
6. restrict deployment
7. sustain family
8. seal breach
9. disperse anomalous lot

### D — claimant and first derivatives

1. recognize claimant
2. accept claimant demand
3. refuse claimant demand
4. counter-command claimant
5. discredit claimant
6. arrest claimant
7. authorize zombie training
8. rally zombie band
9. manifest ghost host

### E — derivative operations

1. bind golem host
2. establish sustainment site
3. integrate conquered district
4. suppress fragmentation
5. break former command net
6. demand submission
7. preserve claimant
8. replace claimant
9. survive former-parent front

## Standalone prototype decision icons

These two decisions were generated as separate square source masters because
they were added after the atlas tranche and require visually distinct player
actions. Both prompts required a flat pure-green chroma background, generous
padding, no lettering or real insignia, and a silhouette that remains legible at
33 by 32.

- `prototype_preservation_source.png`: a compact experimental armored
  powertrain and tracked vehicle held inside a mechanic's caliper and wrench,
  painted in steel blue, gunmetal, aged brass, and one amber workshop light.
- `prototype_cannibalization_source.png`: an advanced tracked powertrain being
  deliberately dismantled into gears and recoverable assemblies by crossed
  wrench and cutting tools, painted in dark steel, rust red, soot black, and
  aged brass.

The official imagegen chroma remover supplies the alpha matte. The Event 19
processor normalizes each source to the native decision canvas, regenerates the
review contact sheet, converts the DDS files, and validates distinct hashes,
dimensions, alpha, and pixel fidelity.

## Idea and UI atlas

The 3×3 idea atlas requested, in row-major order: muster control; army congestion; claimant influence; anomalous saturation; supply strain; command confusion; training saturation; equipment debt; family registry.

The 3×3 category/UI atlas requested: formation-management category; claimant-command category; derivative-operations category; formation-quality marker; formation-coherence marker; dynamic-cost marker; warning marker; cooldown marker; invalid-target marker.

## Cosmetic flag prompts

Every flag request specified flat rectangular vexillology, bold geometry, no lettering, no fabric, no pole, no waving, no real-world flag or insignia, and readability at 82×52.

- Claimant breakaway: oxblood field, charcoal diagonal command sash, sealed open muster ledger, unequal brass batons, and a muted-olive helmet canton.
- Zombie base: bone tally standard and broken rifle on black and dried-blood burgundy.
- Zombie claimant: ivory crown, skull, and single gold baton on crimson and charcoal.
- Zombie collective: three linked helmeted skull profiles around a central ring without a crown.
- Zombie species: bone-white devouring spiral on near-black with a restrained burgundy border.
- Ghost base: three pale figures passing between anchor-gates on midnight blue.
- Ghost claimant: silver crown and baton below a rising spectral flame.
- Ghost collective: three empty masks joined by one circular line.
- Ghost species: pale moon disc, empty doorway, and long icy path.
- Golem base: turquoise binding rune between two stone fists and a broken chain.
- Golem claimant: master-builder compass/crown above a marching stone boot.
- Golem collective: nine interlocking rune tiles forming a larger pattern.
- Golem species: three stone colossi advancing from a mountain arch.

## Animation prompts

Animation-specific generation direction, state progression, separate-frame requirements, timing, fallback, and review criteria are recorded in each package's `brief.md` and `frame_plan.md`. Each final animation uses separately generated source frames, not transformed copies of one still.
