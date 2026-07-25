# IW-010 AJX military-role sourced portrait clearance

Date: 2026-07-25.

This bounded package covers only the grounded real-male military-role source search for the existing `AJX_karl_becker` corps-commander consumer. It does not edit gameplay, characters, localisation, interface, `.gfx`, advisor or dossier assets, `_small` portraits, ImageGen output, or DDS files.

## Decision summary

| Consumer | Candidate | Source gate | Role/consumer gate | Disposition |
| --- | --- | --- | --- | --- |
| `AJX_karl_becker` | Friedrich von Rabenau (1884–1945) | PASS: attributed Bundesarchiv photograph, CC BY-SA 3.0 DE, April 1937, uniform, face-visible | PASS for a German Army corps-commander identity; no Saar-specific command is claimed | `source_ready_for_parent_pipeline` / parent may review before identity-preserving portrait work |

The selected source is a period military-role photograph rather than the held postwar courtroom image of Hans von Salmuth. It is a genuine archival photograph of Generalleutnant Friedrich von Rabenau in uniform, with eyes, eyelids, hairline, nose, jaw, both ears, neck, shoulders, and clothing readable. The source is not a generated likeness and has not been repainted or resized.

Before selection, the canonical role reference `assets/vanilla_reference/portraits/commanders/contact_sheet.png` and its catalog entries were inspected. The candidate is being handed off as a full `156x210` commander portrait source, not as an advisor/dossier card or `_small` texture.

The source does not claim that von Rabenau held a Saarbrücken post. The role fit is the broader, historically defensible German Army corps-commander surface requested by the parent. If the parent requires a Saar-specific commander, keep AJX blocked rather than silently relabeling this identity.

## Selected source: Friedrich von Rabenau, Bundesarchiv Bild 183-C05190

The source page is [Bundesarchiv Bild 183-C05190, Friedrich v. Rabenau](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-C05190,_Friedrich_v._Rabenau.jpg).

The direct unchanged original is `https://upload.wikimedia.org/wikipedia/commons/c/c7/Bundesarchiv_Bild_183-C05190%2C_Friedrich_v._Rabenau.jpg` and is retained at `source_masters/friedrich_von_rabenau_1937_dorneth_c05190.jpg`.

The archive caption identifies `Generalleutnant Dr. phil.h.c. Friedrich v. Rabenau` as Chief of the Heeresarchive from 1 April 1937 and dates the image 13 April 1937. It credits `Scherl Bilderdienst` and photographer `Dorneth` (caption reference `4705-37`). The uniform and decorations are source-visible military clothing; no clothing, insignia, face, or background detail was invented.

The source was supplied by the German Federal Archive through the Wikimedia Commons cooperation project and is marked CC BY-SA 3.0 DE. Required attribution is `Bundesarchiv, Bild 183-C05190 / Foto: Dorneth / CC BY-SA 3.0 DE`. The licence deed is [Creative Commons Attribution-ShareAlike 3.0 Germany](https://creativecommons.org/licenses/by-sa/3.0/de/deed.en).

The unchanged master is 581×800, grayscale (`L`) after Pillow decode, 43,869 bytes, SHA-256 `F6B51E6B3A39E35734D67FA4DB4081C6DA26AEB40084569FF6747CD9ACA0480B`.

The explicit head-and-shoulders crop is `source_crops/friedrich_von_rabenau_1937_c05190_head_shoulders.png`. Its half-open decoded-master rectangle is `(left=20, top=30, right=540, bottom=730)`, producing 520×700 pixels. The crop excludes the vertical Bundesarchiv caption strip at the extreme right while retaining the complete visible head, neck, both shoulders, collar, and uniform. It performs no resize, retouch, recolour, sharpening, or clothing alteration.

The crop SHA-256 is `B153E0310340D1EC5ED02484A52049C5D018767FEC6C5C525BA237B5803161E1`. The exact decoded-pixel equality proof is `source_crops/friedrich_von_rabenau_1937_c05190_head_shoulders.json`; it records `decoded_pixels_equal: true`, pixel count `364000`, and matching master/output RGBA digest `fe18eb7636ddc8ec8ac3e078da7746f00bf451822c8c2b0d8e1d071f20be9bb8`.

The crop utility is `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py`; its recorded tool SHA-256 is `14fa178d6df999346874a7033e84f9b3ae988e7d845f3a4b2f8a44755e30641c`.

## Alternate source retained for comparison: Bundesarchiv Bild 183-C05192

The alternate source page is [Bundesarchiv Bild 183-C05192, Friedrich v. Rabenau](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-C05192,_Friedrich_v._Rabenau.jpg), with direct original `https://upload.wikimedia.org/wikipedia/commons/3/39/Bundesarchiv_Bild_183-C05192%2C_Friedrich_v._Rabenau.jpg` and local master `source_masters/friedrich_von_rabenau_1937_dorneth_c05192.jpg`.

It carries the same `Dorneth`, Scherl Bilderdienst, April 1937, Bundesarchiv, and CC BY-SA 3.0 DE provenance. It is retained as a review-only alternate because the visor obscures the hairline and casts a deeper shadow over the eyes; C05190 has cleaner facial geometry for the strict source-locked portrait gate.

The alternate is 580×800, grayscale (`L`) after Pillow decode, 46,721 bytes, SHA-256 `FE8481E1F2961720B8DC8DBC12BD565114843FE47A0765C1CC7454E088775EE3`.

The comparison sheet is `contact_sheets/ajx_friedrich_von_rabenau_source_candidates.png` (review-only, not a runtime texture).

## Ownership audit

The exact and variant terms `Friedrich von Rabenau`, `Friedrich_von_Rabenau`, `Friedrich Rabenau`, `Friedrich_Rabenau`, and `Rabenau` were searched in character definitions, country histories, interface/GFX consumer paths, portrait filenames, and localisation under the current Chaos Redux root, installed vanilla HOI4, Kaiserreich `1521695605`, and approved Workshop mods `2265420196` and `1458561226`.

All five roots returned no text or filename match. No live character, country recruit, leader, corps-commander, operative, officeholder, portrait sprite, portrait texture filename, or localisation consumer for Friedrich von Rabenau was found. There is therefore no active meaningful owner to transfer and no additive-transfer contract is needed. The complete root/file and command record is `ownership_audit.md`.

For context, the same bounded scan also confirmed that the prior package's held Hans von Salmuth source remains unowned in all five roots; it was not selected because its only archive-grade rights-clear image is a 1947–1948 courtroom portrait. The unattributed 1943 uniform image remains research-only and is not silently promoted.

## Parent pipeline boundary

This package stops at source clearance and exact crop evidence. The parent owns the source-locked identity-preserving ImageGen repaint, deterministic 156×210 processing, independent likeness/style/provenance audit, DDS conversion, `.gfx` wiring, localisation alignment, and any decision to accept the broader German military rather than Saar-specific role fit.

Suggested stable large sprite token, if the parent assigns this candidate to the existing consumer, is `GFX_portrait_AJX_karl_becker` (the current character definition already uses this token). No new sprite name or texture path is authorized by this package.

## No simplifications

No generated face, generic stand-in, re-enactment, modern photograph, postwar courtroom substitute, source re-encoding, clothing edit, gameplay edit, or runtime fallback was used. The only open decision is whether a German Army general with documented military command identity is acceptable for the existing AJX corps-commander role; if not, mark the role blocked and retain this source as review evidence.
