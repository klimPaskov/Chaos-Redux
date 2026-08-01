# Event 012 Africa model requirements and runtime handoff

Date: 2026-08-01

Status: blocked by the explicit no-model instruction. This document records the exact model work that can begin later. No model, entity, `.mesh`, `.anim`, unit template, or readiness flag was created by this handoff.

## Production boundary

Event 012's current gameplay core is model-safe. The model-dependent action selectors remain behind `africa_strange_formation_package_ready`, and the four model-gated achievement rows remain closed. No generic infantry, recoloured vanilla entity, static portrait, or 2D formation substitute is allowed to satisfy these rows.

Use the Chaos Redux 3D model pipeline for every package. Each job needs one approved reference image, a vanilla scale crosswalk, source and final texture evidence, a real exported `.mesh`, a real exported `.anim` for every requested action, reimport evidence, and a parent-owned runtime consumer review. Runtime wiring remains parent-owned after the model handoff.

## Country visual packages

These are six Tier A high-chaos identities from rows 197-202 of `docs/specs/012_africa_specs/matrices/012_africa_asset_animation_matrix.csv`.

| Asset ID | Intended identity | Existing gameplay consumer | Required visual surface | Gate |
|---|---|---|---|---|
| `country_package_pan_high_chaos` | Pan | `africa_strange_formation_package_ready`, Action 76 `organise_pan_sappers`, chaos Pan AI profile | Flag ladder, leader and court/sovereign portrait family, emblem, route identity art, and a distinct ecological-industrial visual language | Keep closed until the fictional high-chaos review and model package are accepted |
| `country_package_gorilla_kingdom` | Gorilla Kingdom | Action 75 `train_gorilla_heavy_infantry`, `africa_ai_profile_chaos_gorilla_is_active` | Flag ladder, decorated sovereign or ruler portrait, emblem, and a mountain-forest identity package | Keep closed until the nonhuman identity and model review are accepted |
| `country_package_the_green` | The Green | Ecological covenant and forest-rampage consumers | Flag ladder, nonhuman or supernatural identity portrait, emblem, and ecological route art | Keep closed until the ecological actor, text, sensitivity, and model review are accepted |
| `country_package_living_rivers` | Living Rivers | Riverborn and flood-control consumers | Flag ladder, identity portrait, emblem, and water-route art | Keep closed until the nonhuman identity and model review are accepted |
| `country_package_stoneborn` | Stoneborn | Action 74 `awaken_stone_cohort`, achievement 40, stone constitutional route | Flag ladder, stone sovereign or representative portrait, emblem, and ruin/charter identity art | Keep closed until rights, constitutional, and model review are accepted |
| `country_package_ancient_hosts` | Ancient Hosts | Ancient formation and relic-site consumers | Flag ladder, identity portrait, emblem, and ancient-host route art | Keep closed until the high-chaos identity and model review are accepted |

The six packages are distinct fictional or nonhuman actors. They must not be represented as caricatures of human African identities, and their art must not replace the sixteen grounded African sovereign portraits.

## Unit and entity packages

These are rows 203-212 of the asset matrix. Each unit needs a complete unit-consumer crosswalk and a real runtime entity rather than an icon-only implementation.

| Asset ID | Gameplay action or consumer | Required model work | Required action roles |
|---|---|---|---|
| `unit_identity_elephant_logistics` | Evolution I elephant logistics | Elephant logistics body, cargo and water equipment, unit emblem, technology/decision art, registered sub-unit consumer | Idle, move, deploy, and supply-load action as required by the selected entity |
| `unit_identity_elephant_shock` | Evolution I elephant shock | Armoured or protected shock elephant silhouette, equipment profile, unit emblem, technology/decision art | Idle, move, attack, and impact action |
| `unit_identity_gorilla_heavy_infantry` | Action 75 | Distinct heavy infantry creature body, weapon/equipment silhouette, unit emblem, technology/decision art | Idle, move, attack, and recovery action |
| `unit_identity_pan_sappers` | Action 76 | Pan sapper silhouette with functional engineering equipment and nonhuman anatomy | Idle, move, sabotage, and construction action |
| `unit_identity_stone_cohorts` | Action 74 and achievement 40 | Stone cohort bodies with readable joints, mass, damage state, and charter-safe identity | Idle, move, attack, and collapse/recovery action |
| `unit_identity_riverborn` | Living Rivers package | Water-formed unit with a readable ground or water contact solution and river-route identity | Idle, move, attack, and water transition action |
| `unit_identity_forest_giants` | The Green package | Ecological giant silhouette with non-caricature anatomy and forest-scale contact | Idle, move, attack, and concealment or emergence action |
| `unit_identity_oracle_recon` | Ancient Hosts or Oracle network route | Recon identity with a readable sensor or divination motif that remains a unit silhouette | Idle, move, recon, and observation action |
| `unit_identity_disaster_wardens` | Natural-disaster and ecological containment consumers | Warden unit with protective equipment, field markers, and disaster-response silhouette | Idle, move, rescue, and containment action |
| `unit_identity_plague_carriers` | Disease high-chaos route | Disease-carrier unit with a readable nonhuman or supernatural silhouette and containment-safe presentation | Idle, move, deploy, and release/containment action |

Every new sub-unit identifier must also receive its emitted `unit_<subunit_id>_icon_small` text icon and any other icon token required by the installed unit registry. A missing text icon is a runtime failure even if the model files exist.

## Required production evidence

For each country or unit package, the future job must retain the one-image source reference, provenance and rights status, provider lineage, Blender checkpoints, measured geometry and material reports, vanilla scale comparison, processed DDS files, exported `.mesh`, exported `.anim` actions, checksums, reimport or parser evidence, and a runtime crosswalk. Any missing action, unavailable exporter, absent reimport proof, or unresolved identity issue keeps the item blocked.

The parent implementation pass must later wire the selected files into the owning entity, `.asset`, `.gfx`, unit or country consumer, localisation, manifest, and acceptance ledger surfaces. Models must not be wired by changing the three formation gates early.

## Explicit omissions

No model generation, paid provider call, Blender job, texture conversion, entity registration, unit-template registration, or gameplay readiness setter was performed in this tranche. The current Event 012 core remains playable without these consumers, with the model-dependent paths closed and documented.
