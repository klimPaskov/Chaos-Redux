# Event 014 Cannibal Irregular Unit and 3D Model Plan

## Purpose

Event 014 fields nine gameplay formation families rather than ordinary infantry templates with renamed labels. Seven families retain dedicated bespoke model packages. Bone Riders and Network Cadre are approved vanilla-visual simplifications: Bone Riders uses vanilla `sprite = cavalry`, Network Cadre uses vanilla `sprite = infantry`, and neither requires a custom model consumer. The separate Scavenged Elephant Column uses vanilla `elephantry` and therefore has no new model consumer.

The eight foot families are line sub-units in the infantry group and belong to the normal light-infantry and army categories. Bone Riders uses documented `cavalry = yes` with `type = { infantry }` and `group = mobile`, plus the cavalry and army categories. All nine gameplay families also belong to one shared Event 014 irregular-infantry category.

The common battlefield identity is exceptional foot speed, high soft attack and breakthrough, low organisation, low maximum strength, poor defensive staying power, and a strong preference for attack.

Every gameplay family must exceed installed vanilla cavalry speed, while March Predation Columns remain the fastest family.

## Approved vanilla-visual simplifications

The 2026-08-26 parent decision removes Bone Riders and Network Cadre custom 3D production from the current acceptance surface. Bone Riders resolves to the installed vanilla `sprite = cavalry` entity and animation family, and Network Cadre resolves to the installed vanilla `sprite = infantry` entity and animation family.

Their gameplay profiles, equipment gates, locked templates, CXT registration, localisation, and nine-family counter package remain distinct. No Event 014 mesh, skeletal action set, material package, model entity, provider export, reimport proof, or model-specific audio synchronization is required for either simplified family.

Retained Bone Riders and Network Cadre provider, Blender, source, and generated-model records are historical lineage and failure evidence only. They are not runtime inputs, active work queues, or current 3D blockers, and the parent cleanup removed the corresponding heavy evidence workspaces.

## Cultural and visual boundary

The models depict fictional scavenger hosts assembled from displaced civilians, deserters, dock laborers, siege survivors, and looters in damaged 1930s–1940s workwear, military surplus, and improvised protective gear.

Every bespoke model family has a feral, deliberately nonstandard silhouette built from skull helmets or skull-faced headpieces, rib and bone armour, tooth or bone trophies, crude bindings, and invented streaked skin paint. These devices are battlefield intimidation and scavenged protection, not ceremonial dress. Each dedicated model family must combine them differently so the seven bespoke models remain recognizable at map scale instead of looking like one generic soldier with swapped weapons.

Weapons are practical scavenged primitive arms: scrap-metal spears, plain bows, cleavers, boarding axes, sledgehammers, entrenching tools, and improvised polearms.

The package must not borrow living Indigenous clothing, body-paint patterns, labels, ceremonial forms, sacred motifs, or identifiable cultural weapon decoration. All paint geometry and bone construction must be original, culture-neutral horror design.

Only Island Host, Siege Commune, and March Host origin identities may appear in a unit, model, counter, sound, prompt, manifest, or runtime identifier.

## Shared 3D production contract

- Owner: `014_cannibalism`.
- Profile: `humanoid_unit`.
- Provider: Meshy 7 exclusively through the verified repository-owned MCP route.
- Provider input: exactly one approved full-body input derived from actual Internet-sourced or user-supplied modern artwork at `docs/assets/014_cannibalism/models_3d/<asset_slug>/refs/original/meshy_input.png` for each of the seven dedicated model families. ImageGen may only perform faithful resolution, alpha, background, padding, or edge cleanup and may not redesign the source or invent missing components.
- Current Feast Guard source exception: use the user-supplied `docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/refs/source/untouched.png` and faithful approved input SHA-256 `C67AF852A27E1379590BD84C5175C378D449AE226F895A2D326B45099040D8C9`. The prior generated or substantially redesigned Feast Guard input is rejected evidence.
- Vanilla scale reference: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`, object `polySurface106`, measured source height `7.351824797689915`, forward axis `-Y`, up axis `+Z`.
- Vanilla entity reference: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset#infantry_rifle_entity`, entity scale `0.8`, effective runtime height `5.881459838151932`.
- Runtime model root: `gfx/models/units/014_cannibalism/<asset_slug>/`.
- Runtime entity registries: `gfx/entities/014_cannibalism_units.gfx` and `gfx/entities/014_cannibalism_units.asset`.
- Required actions for every dedicated model family: idle, move, attack, defend, support attack, retreat, training, and death.
- Actions are real skeletal actions with smooth transition and loop evidence; static or transform-only substitutes are forbidden.
- Materials use the inspected infantry shader and packed PDX channels, with a maximum texture dimension of 1024 pixels.
- Every exported `.mesh` and `.anim` requires locked `io_pdx_mesh` export, byte-level checksum evidence, and reimport proof.
- Planned generation, rigging, remeshing, animation, conversion, and all failure-recovery credits are pre-authorized without a ceiling or confirmation pause.
- Runtime files must never be referenced from `docs/assets/`.

## Family matrix

| Formation template | Sub-unit and sprite token | Stable model slug | Weapon and silhouette | Distinct attack action |
| --- | --- | --- | --- | --- |
| Scavenger Warband | `cannibal_scavenger_warband` | `cannibal_scavenger_warband` | Lean painted runner with a broken skull cap, jawbone shoulder pieces, torn civilian workwear, and a long scrap-metal spear | Fast two-handed spear thrust followed by an uncontrolled forward recovery |
| Feast Guard | `cannibal_feast_guard` | `cannibal_feast_guard` | Stocky command guard under a hornless animal-skull helmet, rib plates, butcher apron, broad cleaver, and boiler-plate shield | Shield-first rush and close cleaver strike |
| Feast Cohort | `cannibal_feast_cohort` | `cannibal_feast_cohort` | Ragged assault infantry with a long skull hood, spine trophies, scavenged webbing, and a fork-headed improvised polearm | Braced polearm lunge with an aggressive second shove |
| Bone Guard | `cannibal_bone_guard` | `cannibal_bone_guard` | Scarred elite guard almost enclosed by layered skull, rib, and long-bone armour, carrying a heavy bone-handled poleaxe without ceremonial markings | Heavy overhead poleaxe chop with readable recoil |
| Bone Riders | `cannibal_bone_riders` | `vanilla cavalry sprite (no custom model)` | Horse-mounted pursuit rider gameplay profile; bespoke 3D production is intentionally omitted under the approved vanilla-visual simplification | Vanilla cavalry entity and action family |
| Island Reavers | `cannibal_island_reavers` | `cannibal_island_reavers` | Rope-harnessed coastal raider with a low skull helmet, exposed rib cage armour, damaged naval workwear, harpoon spear, and boarding axe | Harpoon jab followed by a short boarding-axe slash |
| Siege Eaters | `cannibal_siege_eaters` | `cannibal_siege_eaters` | Dust-covered breacher with a battered skull-faced helmet, compact rib protection, canvas wraps, sledgehammer, and entrenching tool | Full-body sledgehammer swing aimed at a close obstacle or defender |
| March Predation Column | `cannibal_march_predation_column` | `cannibal_march_predation_column` | Extremely light pursuit runner with stark invented face paint, tooth trophies, torn coat, plain self bow, quiver, and machete | Rapid bow draw, release, and immediate forward step |
| Network Cadre | `cannibal_network_cadre` | `vanilla infantry sprite (no custom model)` | Gaunt crouched courier gameplay profile; bespoke 3D production is intentionally omitted under the approved vanilla-visual simplification | Vanilla infantry entity and action family |

Every dedicated model reference must show one complete character with separated limbs, complete hands and feet, one coherent rear silhouette, weapon geometry thick enough to survive model generation and map-scale reduction, and generous transparent padding.

Dedicated model references must avoid crowds, terrain bases, cinematic backgrounds, text, logos, modern tactical equipment, culture-specific costume, supernatural Wendigo anatomy, antlers, glowing eyes, extra limbs, floating props, collages, side-profile sheets, and turnaround boards.

## Unit behavior contract

The nine gameplay sub-units use only documented internal unit types and the standard infantry or mobile group. Vanilla `elephantry` remains the installed elephant sub-unit used by the locked Scavenged Elephant Column and is not a new Event 014 model family. Bone Riders and Network Cadre use their approved vanilla sprite consumers rather than dedicated Event 014 model entities.

Their irregular classification is expressed through one registered custom sub-unit category shared by all nine gameplay types, alongside the documented front-line, light-infantry, cavalry, all-infantry, and army categories where compatible.

The new sub-units continue to consume real vanilla infantry, support, artillery, or motorized equipment through the existing Event 014 recruitment gates.

No new equipment archetype is required merely to obtain a distinct model.

Every locked Event 014 division template must contain a plurality of its matching custom sub-unit so the template resolves the intended sprite token.

Support companies and role-specific artillery may remain, but ordinary infantry, cavalry, marine, or motorized battalions must not outnumber the matching custom cannibal battalion inside the template.

The CXT test-country extension must unlock all nine custom sub-units, create one test template per type, spawn the standard test roster without duplication, and update the documented inventory count through the additive CXT initialization contract. The vanilla elephantry technology and Scavenged Elephant Column remain equipment-bound and are covered by the same Event 014 gameplay access contract without adding another custom sprite token.

## Counter handoff

Every family requires its own large division-template counter, small on-map counter, and text icon.

The counters use the exact installed vanilla infantry counter definitions and decoded DDS files as the consumer reference, plus the matching skill-local land-counter family under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/`.

Final paths use `gfx/interface/counters/divisions_large/unit_<subunit>_icon.dds`, `gfx/interface/counters/divisions_small/onmap_unit_<subunit>_icon.dds`, and `gfx/texticons/unit_<subunit>_icon_small.dds`, with definitions in `interface/chaosx_subuniticons.gfx` and `interface/chaosx_texticons.gfx`.

Each icon uses ImageGen source art, the sampled vanilla green palette, native alpha, the exact frame and state contract, decoded DDS round-trip evidence, and a native-size contact sheet.

No family may reuse another family’s icon or a renamed vanilla counter.

## Sound handoff

Each bespoke model family requires legally reusable Internet-sourced audio for selection or acknowledgement, movement, idle, weapon attack, impact, and death roles.

Entity-state audio remains family-specific through each of the seven bespoke model entities and its action synchronization points. Bone Riders and Network Cadre do not require model-specific entity-state audio under the approved vanilla-visual simplification.

Selection follows the installed hardcoded `<TAG>_infantry_idle` and related country-voice consumers for `CBA` through `CBH` and `CBL`; it is a country-level binding shared by that country’s infantry rather than a false per-subunit consumer.

All final voice WAV files use signed 16-bit PCM, 44100 Hz, mono, with source URLs, creators, licenses, immutable originals, transformation recipes, checksums, and `ffprobe` receipts.

## Runtime acceptance

Acceptance requires nine live gameplay sub-unit consumers, seven dedicated custom sprite tokens, seven distinct `.mesh` exports, seven complete action sets, seven material packages, seven reimport proofs, nine bespoke three-surface counter packages, sourced audio coverage for the required consumers, runtime `.gfx` and `.asset` wiring for the seven bespoke model families, localisation, CXT coverage, documentation, and parent review. Bone Riders uses vanilla `sprite = cavalry` and Network Cadre uses vanilla `sprite = infantry`, so neither requires a custom model/action/entity/provider output. The vanilla `elephantry` consumer and Scavenged Elephant Column require no additional Event 014 model or counter output.

In-game visual and playback validation remains user-owned and must not be inferred from provider previews or export success.

## Future plans

Future Event 014 expansion could add a transformed Wendigo overlay model family, but the ordinary cannibal package must remain visually human-derived and separate from the preserved Event 002 Wendigo units.
