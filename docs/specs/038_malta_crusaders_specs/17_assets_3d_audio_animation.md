# Asset, 3D model, audio, and animation specification

## Asset ownership

This file defines the accepted visual and audio requirement set. Actual production uses the correct narrow subagent and asset skill. No asset family should be inferred beyond this register without an accepted spec update.

Temporary evidence belongs under `docs/assets/038_malta_crusaders/` while work is active. Before full event completion, durable provenance and runtime crosswalks move into permanent event documentation, final files move into engine folders, and the temporary workspace is deleted.

## Source mode rules

- real people use attributed archival source images and the portrait worker
- authentic institutions can use sourced institutional material
- fictional or impossible high-Chaos leaders can use native ImageGen through the portrait worker
- historical flags and symbols start with source research, then use ImageGen for the final clean flat design
- fictional flags, emblems, event art, and UI art use ImageGen
- custom icons use separate source art per asset type
- all custom units require 3D model review, sourced audio, and bespoke counters
- super-event audio uses verified licensed or public-domain musical recordings

No unapproved placeholder, recolour, renamed existing icon, or copied counter is accepted.

## Flag families

### Malta Crusader State

Required:

- base flag
- democratic or constitutional variant where route requires it
- non-aligned order-state variant
- fascist Templar or militarized variant if the route uses the ideology
- communist or labour-government variant only if the implementation creates a real government path
- normal, medium, and small sizes

Direction:

- use Maltese and Order of St John geometry and attested symbols as research anchors
- keep flat graphic design
- avoid waving fabric, scenery, gradients, invented fake lettering, and modern logo treatment

### Sovereign Order and Confederation

Separate cosmetic flags for:

- Sovereign Order of Malta
- Confederation of the Military Orders
- Crusader Kingdom of Malta

These are distinct designs, not simple recolours.

### Holy See and Kingdom of God

Use sourced research for Vatican and Papal flag geometry. The Kingdom of God can be a fictional Papal-crusader design grounded in accepted symbols.

### Principalities

Required only for created country actors:

- Kingdom of Jerusalem
- Principality of Antioch
- County of Tripoli
- Crusader Cyprus
- Aegean Crusader State
- Anatolian Order State
- North African March

Each needs normal, medium, and small flags plus government variants that actually appear.

### Hidden route flags

- Teutonic Order faction emblem
- Atlantis German cosmetic flag
- Holy World terminal flag or emblem
- believer alliance emblem
- nonbeliever coalition emblem only if one shared visual identity is implemented

Nazi and extremist imagery requires contextual historical treatment and should not be made celebratory.

## Portrait families

### Grounded people

Potential grounded subjects include:

- Fra' Ludovico Chigi Albani della Rovere
- the current period Pope for the campaign start or the valid dynamic Pope
- real Maltese political, military, or church figures selected by route
- grounded local leaders for principalities and restorations
- real German leaders used by the hidden route

Each subject needs:

- identity ownership search across vanilla and project
- source URL, attribution, rights, and retrieval date
- untouched original
- exact crop and equality evidence
- deterministic 156 by 210 PNG
- DDS
- independent identity, framing, and provenance review
- portrait-specific wiring

The agent never generates a substitute face for a grounded person.

### Institutional portraits

Approved people-free institutions include:

- Council of the Eight Langues
- Crusade Council
- Papal council or curia when no single leader is appropriate
- principality regency councils

They require authentic institutional source material or a generated symbolic high-Chaos presentation only when the institution itself is fictional.

### Fictional or impossible leaders

Possible generated portrait subjects:

- a wholly fictional Blessed Supreme Pope variant when no grounded Pope identity is claimed
- an impossible transformed high-Chaos figure that does not reconstruct a real person's face
- an institutional Atlantis command board

A transformed real Hitler remains a real-person identity and cannot be replaced with a generated fake face. Use sourced portrait material with route-specific overlays or another approved presentation.

## Report and news art

Required scenes:

1. Malta crusader release and banners over the Grand Harbour
2. first Holy Land command report
3. order council assembly
4. convoy and sea-road crisis
5. Jerusalem settlement
6. first principality
7. Eleventh Crusade recovery
8. relic expedition or disputed relic
9. Holy See formation
10. Kingdom of God formation
11. Teutonic negotiations after reveal
12. Atlantis proclamation after reveal
13. Holy World side division after activation
14. terminal victory or defeat where implemented

Most scenes are fictional alternate history and should use generated period-authentic documentary or painted wartime presentation. Real locations can use sourced reference material, but the final fictional event scene should not claim to be a real photograph.

## Focus icons

Each major route and anchor focus needs its own 94 by 86 focus art. Coordinated families include:

- opening crusade and council
- Malta fortress and ports
- Hospitallers
- Templars
- Teutonic traditions
- Saint Lazarus
- Naval Orders
- Siege Brotherhoods
- Armored Knights
- Mounted Knights
- Archers and Crossbows
- Siege Hosts
- engineers
- principalities
- Papal route
- Holy See
- Kingdom of God
- Eleventh Crusade
- Final Crusade
- Holy World preparation

Hidden route icons remain unrevealed until route conditions. Every icon needs its own focus-specific source art. Do not resize idea or decision icons into focus icons.

## Idea and national-spirit icons

Required idea families include:

- Fortress Without a Hinterland
- The Orders Recalled
- An Army Out of Time
- route-specific transformed versions
- dominant-order institutions
- confederation
- Holy See government
- Kingdom of God
- Atlantean Delusion
- Supreme Armoured Program
- War Against the Human Map
- Holy World terminal ideas

Idea icons are separate 64 by 64 art and must not be resized focus icons.

## Decision and mission icons

Required families:

- order demands
- council arbitration
- headquarters
- convoy escort
- rail repair
- fortified port
- air bridge
- raise formation
- foreign volunteers
- equipment conversion
- siege workshop
- regional target selection
- invasion preparation
- settlements
- relic expeditions
- principality obligations
- Eleventh Crusade phases
- Holy World preparation
- terminal contribution and campaign actions

Decision icons must remain readable at the actual 32 by 32 or inspected consumer size. Mission icons follow the separate mission reference family.

## Decision category presentation

### Crusade Council

A dedicated event-owned GUI is planned. It needs:

- full background panel
- three meter frames and fill states
- six order emblems
- dominant, marginalized, warning, and demand frames
- sacred-center status icons
- demand card art
- territorial or relic card frame
- available and blocked button states
- close, target, and detail controls

The UI worker owns layout and MCP visual evidence after the gameplay helpers exist.

### Other categories

Mediterranean Campaigns, Principalities, Eleventh Crusade, and Holy World can use strong static or animated category pictures unless a separate full GUI is proven necessary.

Category pictures must not paint fake buttons, meters, or ledger rows.

## Animation requirements

Use animation only for meaningful state.

Approved candidates:

- subtle Crusade Council active seal
- warning pulse when Authority or Cohesion enters collapse
- order demand card emphasis
- disputed relic shimmer or instability
- Holy World Ready seal
- leader portrait overlays for route-specific supernatural or blessed presentation
- super-event-adjacent route emblems

Every animation requires real per-frame source art, processed frames, horizontal sheet PNG and DDS, static fallback, GIF preview for review, manifest, and GFX handoff.

Transform-only movement, glow, recolour, blur, or scaling of one still cannot be final animation.

## Achievement icons

Each implemented achievement requires the full state triplet:

- unlocked
- grey
- not eligible

Achievement files remain directly under the engine achievement root and use the full achievement ID in the filename.

## 3D model inventory

### Armored Knight

**Profile:** humanoid unit

**Reference direction:** grounded professional medieval-modern concept art with full subject, 1936 to 1945 ordinary equipment, no anime presentation, no cropped weapon.

**Vanilla calibration:** installed infantry mesh and entity, exact source height, entity scale, forward axis, and ground contact.

**Required actions:** idle, walk, run where used, melee or firearm attack according to final unit design, hit where supported, death.

**Materials:** metal armour, cloth, leather, weapon, and order markings through PDX packed materials.

### Mounted Knight

**Profile:** nonhumanoid articulated or mounted unit requiring a dedicated rig plan.

**Reference direction:** complete rider and horse relationship, full equipment, no hidden limbs or cropped mount.

**Scale:** explicit rider, horse, source, provider, and runtime crosswalk.

**Actions:** idle, walk, run or charge, attack, death or collapse.

If the production toolchain cannot produce a valid mounted rig and animation set, the package is blocked. An infantry model with a horse icon is not a substitute.

### Archer and Crossbow

The implementation must decide whether one humanoid base model with distinct equipment and animation variants can represent both families at runtime. If their map presentation cannot be distinguished, create separate models.

Required firing actions must show complete weapon relationship, aim, release, recoil or reset, and recovery.

### Siege engine

**Profile:** articulated attachment or vehicle-like static unit.

Possible model: trebuchet, catapult, or mixed siege train according to final gameplay family.

Required actions: idle, movement if visible, firing cycle, impact synchronization, destruction where consumed.

### Crusader Engineer

A separate map model is required only if the support company has a visible consumer. Otherwise its asset package is limited to icon, counter involvement, sound role where applicable, and parent-unit presentation.

### Mechanized Knight Carrier

**Profile:** land vehicle.

Requires vehicle geometry, PDX materials, movement, firing or non-firing declaration, destruction, exact scale, and runtime entity.

### Atlantean Supreme tank

**Profile:** land vehicle.

Requires unique design, model, textures, sounds, counters, equipment art, movement, firing, and destruction. It cannot be a recoloured vanilla tank.

### Papal terminal variants

Use texture, emblem, and entity variants when sufficient. Create new geometry only when the visual silhouette and gameplay role require it.

## 3D source and provider rules

Every 3D job requires:

- nonblank `MESHY_API_KEY` before any path discovery or work
- repository dependency bootstrap and lock
- Meshy 7 only
- live balance check before paid work
- one approved ImageGen-prepared source image
- Internet-sourced modern designed artwork with rights review
- hard non-anime gate
- period-fit review
- complete firearm relationship for firing units
- immediate provider download and checksum
- Blender checkpoints
- local vanilla calibration
- PDX material processing
- Meshy rig and `meshy_animate` actions
- export and reimport proof
- runtime handoff

No model job can use archival photographs or historical paintings as the direct modern-designed-artwork source candidate under the current 3D skill.

## Custom unit audio

Each custom unit package needs Internet-sourced audio with clear licensing.

### Armored Knight roles

- selection
- acknowledgement
- armored movement
- weapon attack
- metal impact
- death or collapse

### Mounted Knight roles

- selection
- acknowledgement
- horse movement
- charge
- attack
- death or fall

### Archer and Crossbow roles

- selection
- acknowledgement
- movement
- draw or mechanism
- release
- impact
- death

### Siege roles

- selection
- movement or machinery loop
- tension and release
- launch
- impact
- destruction

### Vehicle roles

- selection
- engine idle
- movement
- weapon fire
- impact
- destruction

The audio worker or 3D worker preserves source downloads, URLs, titles, creators, licenses, checksums, derivatives, and animation synchronization points. Generated or synthesized sounds are forbidden.

## Custom counters

Required counter surfaces depend on the final consumer. At minimum, every standalone unit family needs:

- large land-unit counter where used
- map counter where used
- division-template emblem if the family is player-selectable there

Counter design must inspect exact installed-vanilla source definitions and skill-local references. Use sampled vanilla green, correct canvas, frame order, alpha, border, silhouette, shading, and contrast.

## Equipment and technology art

Separate required families:

- knight armour equipment
- war bow equipment
- crossbow equipment
- siege engine equipment
- mechanized knight carrier
- Atlantean Supreme tank
- anti-tank lance
- related technologies and special projects

Equipment art and technology icons are separate surfaces. Do not resize one into the other.

## Faction emblems

Required:

- Teutonic Order
- Holy World believer alliance
- any persistent nonbeliever coalition identity

Use native transparency, clean heraldic design, readable small silhouette, and no fake text.

## Super-event images and audio

Detailed roles are in `18_super_events.md`. Every completed super-event needs:

- unique image
- unique title, description, button, and sourced quote
- unique licensed musical track
- unique audio ID
- final WAV under `sound/038_malta_crusaders/`
- base sound and volume wrappers
- settings-aware playback
- audio catalog row

No default or reused track without explicit approval.

## Asset manifest fields

Every asset row records:

- stable asset ID
- asset type
- route and consumer
- source mode
- source or prompt evidence
- dimensions
- alpha mode
- final path
- sprite or entity name
- variants
- producer
- reviewer
- approval state
- runtime consumer
- blocker or exception

## Asset completion boundary

An asset package is complete only when:

- final runtime file exists
- correct engine path is used
- sprite, entity, sound, or portrait wiring exists
- gameplay consumer is live
- provenance and manifest are complete
- visual review passes at native and in-game size
- no runtime reference points into temporary docs assets

A provider output, preview PNG, GIF, blend file, or DDS without a consumer is not complete.
