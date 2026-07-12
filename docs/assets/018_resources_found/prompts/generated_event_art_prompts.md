# Event 018 Generated Event Art Prompt Ledger

## Shared visual anchors

All generations used original fictional artwork. The Oth-Kesh anchor was generated first and then supplied as the visual reference for creature scenes, super events, portraits, flags, and animation edits:

```text
Low, extremely heavy subterranean geological species; overlapping slate-black mineral plates; wedge-shaped shield head; four narrow breathing slits; faint amber sensory eyes; rust-red iron seams; coherent quadrupedal anatomy; original split-vein emblem; documentary/painterly 1930s grand-strategy visual language; no text, no copied insignia, no modern objects, no gore.
```

Reference: `source_png/oth_kesh_species_reference_source.png`.

## Report-event prompts

Shared treatment: original 1930s documentary photograph, period clothing and machinery, no text, no modern equipment, no recognizable political insignia, composition readable inside a small report card.

| Identity | Scene direction |
|---|---|
| `resource_discovery` | Surveyors, geologists, and miners gather around an impossible mineral seam at a new extraction shaft. |
| `compound_field` | A wide industrial resource compound with derricks, rail spurs, stockpiles, and work crews expanding across a valley. |
| `sick_workings` | A period doctor examines an ill miner in a cramped underground medical station while worried workers wait. |
| `missing_shift` | An abandoned underground station with idle carts, tools, lamps, and signs that an entire shift vanished. |
| `first_evidence` | Unmarked investigators and miners examine a severed mineral forelimb specimen on a worktable. |
| `perimeter_breach` | Low heavy Oth-Kesh bodies push through shattered supports and fencing as workers flee a resource compound. |
| `evacuation` | Civilians and workers board trucks and trains beside a threatened extraction town. |
| `monster_hunt` | A 1930s anti-tank crew faces one coherent Oth-Kesh body at a mine mouth. |
| `full_seal` | Engineers construct a massive timber-and-concrete bulkhead across a dangerous mine entrance. |
| `anchor_cleanup` | Workers and engineers clear collapsed rail, shattered derricks, and mineralized debris after containment. |

The first `first_evidence` generation was rejected for recognizable insignia and regenerated with entirely unmarked period uniforms.

## News-event prompts

Shared treatment: extra-wide 1930s press photograph, strong central story, period-neutral uniforms, no captions or mastheads, no modern objects, later normalized to true grayscale.

| Identity | Scene direction |
|---|---|
| `global_resource_field` | Delegations overlook a vast new resource basin with mines, cranes, rail, and processing works. |
| `border_crisis` | Two guarded cordons face one another across a disputed extraction border, with tents and trucks behind them. |
| `public_attack` | Coherent Oth-Kesh bodies emerge into an industrial street while civilians run and period cars halt. |
| `cave_country_emergence` | Organized Oth-Kesh columns cross ruined rail beneath Vhorruk and an abstract split-vein standard. |
| `regional_containment` | A sealed cavern stronghold, ruined rails, abandoned artillery, and no intact living creature. |
| `global_defeat` | Multinational engineers, medics, and soldiers rebuild a scarred extraction basin after the final victory. |

## Super-event prompts

Shared treatment: landscape `457:328` composition, original alternate-history wartime illustration, cinematic documentary realism, one dominant readable focal point, no text, no real-world insignia, no modern objects, no gore.

| Role | Scene direction |
|---|---|
| Cave emergence | A colossal chasm opens in an industrial valley; disciplined Oth-Kesh ranks emerge around Vhorruk, identified by a natural split-crown ridge, with human defenders at the edges for scale. |
| World end | A mature organized host occupies a shattered continental refinery and rail city, with multiple distant ruptures and Vhorruk's command silhouette above the columns. |
| Global defeat | At sunrise, engineers, miners, medics, and exhausted soldiers surround a gigantic permanently sealed aperture in a ruined basin; no living Oth-Kesh remain. |

## Portrait prompts

Shared treatment: vertical 3:4 HOI4 upper-body portrait, nonhuman mineral anatomy rather than a human in armour, muted grand-strategy painting, dark period-neutral background, strong small-size silhouette, no frame, no text, no human clothing, no gore.

| Character | Identity direction |
|---|---|
| Vhorruk | Literal sovereign with a biological two-bladed split-crown mineral ridge, four breathing slits, calm amber sensory eyes, command-chamber relief, and strategic authority. |
| Thessik | Stone Phalanx commander; broad square plates, pale repaired fracture scars, low blunt brow, fortified tunnel background. |
| Orrukesh | Burrow War specialist; leaner wedge, long sensory grooves, drill-scarred limestone-dusted plates, survey gallery background. |
| Khalvek | Scree Tide commander; lighter swept plates, chipped cheek plate, alert amber eyes, shattered scree tunnel background. |

The authored names are nonhuman and do not use human gender pools.

## Vhorruk animation-edit prompts

Every prompt instructed the image model to preserve Vhorruk's exact identity, camera, crop, background, lighting direction, and palette while locally redrawing the named state. Whole-image movement, scaling, rotation, warping, blur, and recolor were explicitly forbidden.

| Frame | Redrawn state |
|---:|---|
| 1 | Original neutral generated portrait. |
| 2 | Breathing slits widen; chest plates lift; two dust grains fall. |
| 3 | Full inhale; brighter sensory organs; narrow plate gaps; mineral vapor puff. |
| 4 | Sensory organs shift left; one narrows; chest begins settling; shoulder dust. |
| 5 | Alert hold; face plates tighten; one chest seam glows; crown chip falls. |
| 6 | Exhale; eyes return to center; slits close partway; thin vapor ribbon. |
| 7 | Late exhale; plates settle; vapor becomes particles; chamber seam light dims. |
| 8 | Neutral return; relaxed slit opening; final dust motes; chest spacing matches frame 1. |

## Flag prompts

Shared treatment: original flat national flag filling an `82:52` rectangle; no folds, pole, mockup, letters, words, real-world flags, or human political symbols; bold geometry in charcoal, bone gray, rust red, and amber; readable at `10x7`.

| Identity | Composition direction |
|---|---|
| `DHO` | Centered bone-gray shield plate split by a rust-red vertical mineral vein, with two amber sensory nodes. |
| `DHO_democratic` | Four separate mineral wedges arranged as an open consultative ring around an amber void. |
| `DHO_fascism` | A closed sharp mineral spear composed from nested wedges and rising rust fault lines; no real fascist symbol. |
| `DHO_communism` | Horizontal stepped charcoal strata sharing one bone-gray pressure knot with short amber veins; no diagonal cross, saltire, hammer, or sickle. |
| `DHO_neutrality` | A wide sheltered charcoal cavern band across bone-gray stone, centered on a compact split rust diamond. |
| `DHO_WORLD_BELOW` | A continental rust-red fault network reaching every edge around a dark central rupture and six amber pressure nodes. |

The first communism draft was rejected because its saltire-like layout resembled a real-world flag. The accepted prompt explicitly prohibited diagonal crosses and used horizontal strata.
