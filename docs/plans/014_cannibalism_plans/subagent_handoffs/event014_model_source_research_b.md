# Event 014 model-source research handoff B

Date: 2026-08-22.

Owner: `chaosx_asset_source_researcher` scope, sourced visual-reference research only.

## Current status

One defensible public-domain or clearly reusable Internet source has been acquired for each requested 3D job. Originals, native-resolution PNG previews, repository-standard DDS evidence copies, archived source pages or access notes, a comparison contact sheet, a provenance manifest, and this handoff are present. Each source is `source_status: complete` and `review_status: needs_user_review`; the parent agent must approve the exact adapted one-image model input before any Meshy work.

No ImageGen or Meshy call was made. No gameplay, runtime, GFX, unit, event, localisation, or existing production manifest was edited.

## Candidate 1: `cannibal_bone_guard`

Source: [Wikimedia Commons — Swabian School, *Knight in Armor, Holding a Halberd*, c. 1500](https://commons.wikimedia.org/wiki/File:Swabian_School,_Knight_in_Armor,_Holding_a_Halberd,_c._1500,_NGA_75855.jpg).

Institutional record: [National Gallery of Art object 75855](https://purl.org/nga/collection/artobject/75855).

Direct downloadable original: [NGA Open Access image via Wikimedia upload](https://upload.wikimedia.org/wikipedia/commons/b/b5/Swabian_School%2C_Knight_in_Armor%2C_Holding_a_Halberd%2C_c._1500%2C_NGA_75855.jpg).

Creator and date: Swabian School, individual artist not named, circa 1500.

License: CC0 1.0 / National Gallery of Art Open Access as stated by the Commons file record.

Archived original: `docs/assets/014_cannibalism/models_3d/cannibal_bone_guard/refs/sourced/original/swabian_school_knight_in_armor_halberd_nga_75855.jpg`.

SHA-256: `78004D92EEE571BB5B6A83BD14D17A042484BB77FAA4A3DD52D36A64DD085930`.

Dimensions: 1723 × 4000 pixels.

Fit: full-body three-quarter plate armor, articulated limbs, layered waist/hip protection, and a long polearm grip support the requested towering heavy silhouette and axe/poleaxe stance.

Review blocker: the halberd is primarily one-handed and its upper head exits the canvas; the adapted design must create a complete massive two-handed axe/poleaxe and independently add fictional bone trophies. It supplies no skull/rib/spine material logic.

## Candidate 2: `cannibal_island_reavers`

Source: [Wikimedia Commons — *Soldier with shield and lance*](https://commons.wikimedia.org/wiki/File:Soldier_with_shield_and_lance_(NYPL_b14896507-92914).tiff).

Institutional record: [New York Public Library Digital Collections item](https://digitalcollections.nypl.org/items/510d47d9-8cf8-a3d9-e040-e00a18064a99).

Direct downloadable original: [NYPL scan via Wikimedia upload](https://upload.wikimedia.org/wikipedia/commons/1/12/Soldier_with_shield_and_lance_%28NYPL_b14896507-92914%29.tiff).

Creator and date: original artist and exact date are not stated; the sheet is attributed to the NYPL Vinkhuijzen Collection of Military Uniforms, with Eighty Years' War context only.

License: public-domain scan / Public Domain Mark as stated by the Commons record, which describes a mechanical scan of a public-domain original with no known restrictions.

Archived original: `docs/assets/014_cannibalism/models_3d/cannibal_island_reavers/refs/sourced/original/soldier_with_shield_and_lance_nypl_b14896507_92914.tiff`.

SHA-256: `35D33D203119C12F5652B27F0787539294304BE2FC6CC6348DC2B5843108D79B`.

Dimensions: 2320 × 2694 pixels.

Fit: full-body offset stance, diagonal lance/spear, turned torso, and shield-bearing arm give an agile raider silhouette and clear long-weapon hand relationship; the source is free of modern reenactment cues, living Indigenous regalia, sacred motifs, and culture-specific paint.

Review blocker: visible book/plate edges remain, the shield is larger than a compact boarding shield, and there is no boarding axe or harpoon barb; the exact artist/date are unknown and must not be invented. Adapt the stance and hand relationship rather than copying the sheet as final art.

## Candidate 3: `cannibal_siege_eaters`

Source: [The Metropolitan Museum of Art — Domenico Beccafumi, *Hercules, Standing with a Club*](https://www.metmuseum.org/art/collection/search/336114).

Institutional API record: [Met collection API object 336114](https://collectionapi.metmuseum.org/public/collection/v1/objects/336114).

Direct downloadable original: [Met primary image](https://images.metmuseum.org/CRDImages/dp/original/DP-22565-001.jpg).

Creator and date: Domenico Beccafumi (Italian, 1484–1551), 1530–1540.

License: Met Open Access / CC0 1.0; the API record explicitly identifies the object as public domain.

Archived original: `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/refs/sourced/original/hercules_standing_with_a_club_met_dp22565_001.jpg`.

SHA-256: `EB9356C83251AAAF718B29CAB9BEE11BD32A7FBFCEA5E8A2CB0748793313D43D`.

Dimensions: 2519 × 4000 pixels.

Fit: full-body broad torso, bent-knee weight-bearing posture, and long club establish mass, balance, and heavy-tool silhouette for the breacher role.

Review blocker: this is a nude mythological study rather than an armored combatant and the club is not a sledgehammer. Adapt anatomy and tool pose only, then independently design the ram-skull mask, asymmetrical dark segmented arm armor, ragged waist cloth, and sledgehammer/maul. Do not treat the nude source as final costume direction.

## Package paths and validation

- Full provenance manifest: `docs/assets/014_cannibalism/models_3d/sourced_reference_manifest.md`.
- Runtime/GFX boundary handoff: `docs/assets/014_cannibalism/models_3d/gfx_handoff.md`.
- Combined contact sheet: `docs/assets/014_cannibalism/models_3d/sourced_reference_contact_sheet.png`.
- Each job has `refs/sourced/original/`, `refs/sourced/processed/`, `refs/sourced/dds/`, and `refs/sourced/source_pages/` directories.
- PNGs are native-resolution RGBA decodes without crop or stretch.
- DDS files have a legacy `DDS ` header, native source dimensions, and one-level uncompressed BGRA/B8G8R8A8 output from `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

## Parent next steps

Review the contact sheet and manifest, then approve or reject each source as the single adapted reference for its job. If approved, create a derivative or ImageGen adaptation that preserves the source's pose/material logic while adding only the fictional requested design, and record lineage to the immutable original. Keep the production manifests and all runtime wiring parent-owned. Do not wire the evidence DDS files as sprites or model runtime assets.

The excluded path `C:/Users/klimp/AppData/Local/Temp/codex-clipboard-59672c99-c6a5-4728-9ab5-71e311186bd4.png` was not opened or used.
