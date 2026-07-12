# Event 014 GUI, Animation, and Portrait Production Brief

## Scope

This package implements the exact static and animated asset contract frozen in `docs/plans/014_cannibalism_plans/014_gui_dimension_ledger.md`. It does not edit gameplay, `.gfx`, `.gui`, localisation, spreadsheets, catalogues, or shared manifests.

All new core artwork uses the built-in `image_gen` tool. Generated source PNGs are preserved at full resolution. Static GUI sources also receive OpenRaster (`.ora`) editable masters containing the generated artwork and a separate text-safe guide layer. Final processing is limited to cover cropping, exact resizing, alpha cleanup, sheet assembly, contact sheets, GIF previews, and uncompressed one-mip BGRA DDS conversion.

## Visual progression

- Early containment: dirty khaki, field grey, damaged canvas, rust, mud, dried and fresh blood; no cult leader, unified symbol, supernatural light, or recognizable final silhouette.
- Network: blackened wood, damaged ports and rail paper, field evidence, blood-wet courier cords, prison and island traces; uncertain coordination only, with no recognizable named leader or face.
- Warlord command: improvised military authority, raw cloth, butchered ration stores, cracked steel, blood, bone-white material, and scavenged period fittings.
- Revealed command: centralized black, deep red, bone-white command material, mass-war visual language, and Hannibal Lecter-facing portrait space.
- Wendigo command: cold blue-grey, black, cracked ice, exposed fictional flesh, frozen blood, ruined command machinery, and no living Indigenous traditions, sacred motifs, regalia, runes, headdresses, dreamcatchers, totem poles, feathers, beadwork, or authenticity claims.

## Spoiler boundary

The early and network sources contain no recognizable named leader or face, unique silhouette, personal title, or symbol later assigned uniquely to Hannibal Lecter. Ordinary Hannibal Lecter imagery appears only in the revealed portrait and revealed-command family. Wendigo Hannibal Lecter imagery appears only in the transformed portrait and transformed-command family.

## Reference and engine precedent

- Offline wiki: Graphical Asset Modding, Interface Modding, Scripted GUI Modding, plus the mandatory core pages listed in `AGENTS.md`.
- Vanilla animation precedent: `interface/alerts.gfx`, `interface/countrypoliticsview.gfx`, and `interface/leadergroups.gfx`; horizontal sheets, exact `noOfFrames`, `animation_rate_fps`, looping, and `play_on_show`.
- Existing Event 014 surfaces: `interface/014_cannibalism_frontline_hunger.gui` and `interface/014_cannibalism.gfx` (read-only for this tranche).
- Retained exact semantic sources: `cannibalism_frontline_hunger_seal`, `cannibalism_cult_pressure_warning`, and `cannibalism_island_signal_card`, each used once under its ledger-assigned filename.
- Existing fictional Wendigo language: cold, ruined, black-coated, ice-cracked body horror. No cultural authenticity is claimed.

## Mechanical output contract

- Static GUI finals: 26 exact PNG/DDS pairs under `gfx/interface/014_cannibalism/`, each with a full-resolution generated source, processed PNG, `.ora` master, hashes, format record, and contact-sheet review.
- Non-portrait animation finals: 12 exact static PNG/DDS fallbacks and 12 exact PNG/DDS horizontal sheets under `gfx/interface/animated/014_cannibalism/`.
- Portrait finals: 12-frame ordinary Hannibal Lecter and 16-frame transformed Hannibal Lecter packages under `gfx/leaders/014_cannibalism/`; protected `hannibal.dds` and `hannibal_wendigo.dds` remain untouched.
- DDS: uncompressed 32-bit BGRA/B8G8R8A8 channel masks, one stored image level, exact width and height.

## Text-safe review

Every processed static GUI asset is reviewed at native size with the actual `.gui` text rectangles superimposed in a validation-only contact sheet. Text-safe guides never enter the runtime PNG or DDS.
