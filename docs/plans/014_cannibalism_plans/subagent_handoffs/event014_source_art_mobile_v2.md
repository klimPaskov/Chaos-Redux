# Event 014 sourced 3D input handoff: mobile source-art pass

Historical supersession notice: this source-only pass predates the 2026-08-26 decision to use vanilla `sprite = infantry` for Network Cadre and vanilla `sprite = cavalry` for Bone Riders. Its source findings remain lineage evidence only, and neither job is a current custom-model queue.

Research date: 2026-08-24.

Scope completed: actual Internet-sourced game, fantasy, horror, and tabletop reference research for exactly `cannibal_network_cadre` and `cannibal_bone_riders`.

No gameplay, GFX, ImageGen derivative, Meshy, provider, runtime wiring, or unrelated repository file was edited.

No commit was created.

## Decision summary

`cannibal_network_cadre` remains `needs_user_review_no_exact_candidate`.

The existing Blackguards candidate was validated as a clean full-body anatomy reference with bow, quiver, and sidearm, but it is a generic human fantasy archer and the sidearm reads closer to a short sword than a narrow knife.

The stronger archived visual match is official AFK Arena Ferael artwork, which supplies the requested crouched feral/skull/bone language, full-body silhouette, bow, and clearly readable quiver.

Ferael still lacks a visible knife or short blade and carries embedded AFK Arena title/logo branding, so it is the preferred reference candidate but not an exact accepted source.

`cannibal_bone_riders` is `blocked_no_eligible_exact_source_selected`.

No single source found shows a living horse with skull/rib/long-bone barding, coherent tack, four readable legs, one mounted feral warrior, painted skull helmet, sling, stone ammunition pouch, and no spear.

The strongest Bone Riders near-misses remain Awakened Horseman and the Diablo 4 mount sheet, both rejected for multiple mandatory gates.

## Network Cadre source archive

### Preferred reference candidate: AFK Arena Ferael

- Source file: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_afk_arena_ferael.jpg`.
- Source SHA-256: `87BF4CDABA7CD2FCF2AD94C701DAB029F8E066F1C1279FE4B0487C8A39610475`.
- Dimensions: `1109x1624`.
- Source page: `https://afk-artworks.lilithgames.com/artworks/detail/Ferael`.
- Direct image: `https://afk-artworks.lilithgames.com/v2/wallpapers/Ferael.jpg`.
- Archived page: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/source_pages/source_12_afk_arena_ferael.html`.
- Archived page SHA-256: `E0C996312CF33BE13FC5288D505E10A286E2DCC82AB6B9243E41168D84416DDF`.
- Creator/studio: Lilith Games / AFK Arena; individual artist not stated.
- Rights: official commercial game artwork with no third-party reuse license stated; use only as `reference_only_user_authorized`.
- NoAI check: no explicit NoAI, do-not-train, or equivalent restriction found in the archived official page or direct image metadata; this is not a permission grant.
- Exact fit: full-body crouched archer, horned skull-like face, stitched undead presentation, bone-like armor, bow, quiver, and unsettling feral silhouette.
- Exact gap: no visible knife or short blade; official AFK Arena logo/title are embedded.
- Parent action: if approved, pass the untouched source through native ImageGen for faithful higher-resolution cleanup and genuine alpha isolation before Meshy, without redesigning the character or inventing the missing weapon.

### Ranked alternate 2: Warrior Epic Artwork 1

- Source file: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_gamefragger_warrior_epic_7039.jpg`.
- Source SHA-256: `71691B33283B64E5DB6F6167A586024B4DABC5DE62B1EA573A9BCCDE2C9938B8`.
- Dimensions: `676x1024`.
- Source page: `https://gamefragger.com/pc/massively-multiplayer/warrior-epic/pictures/warrior-epic-artwork-1-i7039`.
- Direct image: `https://gamefragger.com/images/pictures/7039L.jpg`.
- Archived page: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/source_pages/source_7_gamefragger_warrior_epic.html`.
- Archived page SHA-256: `9E2815B60A401E4DDA9E86D59A97141AC7BB802A4F60F068D5F86F77E51C54C9`.
- Creator/studio: Warrior Epic production artwork; individual artist not stated.
- Rights: commercial game/gallery artwork; archived page carries copyright and user-submission/DMCA language but no reuse license; use only as `reference_only_user_authorized`.
- NoAI check: no explicit NoAI or equivalent restriction found; this is not a permission grant.
- Fit: skull-like face/mask, dark crouched archer, bow, quiver, and visible large curved side blade.
- Gaps: shield/framing obscures part of the lower body and blade is not a narrow knife; armor is polished fantasy armor rather than painted bone.

### Ranked alternate 3: Narrow One bone-armored archer

- Source file: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_narrow_one_bone_archer.png`.
- Source SHA-256: `C2F5AAE2CE9C3F435B95AC21C6EE486FA375A822296D1002A36573D19D51A6C5`.
- Dimensions: `2620x1578`.
- Source page: `https://pelicanparty.itch.io/narrow-one`.
- Direct image: `https://img.itch.zone/aW1hZ2UvMTA1MDU4MC84MzIxODYzLnBuZw%3D%3D/original/6crcVY.png`.
- Archived page: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/source_pages/source_10_narrow_one.html`.
- Archived page SHA-256: `0F38C1E21658FFC303B0DA9514EE1E742BF2D2DC7F8D83A5F346E27B44BB1F3C`.
- Creator/studio: Pelican Party Studios; page identifies Jesper and Jurgen as developers, with no individual image artist stated.
- Rights: commercial developer-hosted game screenshot with no third-party reuse license stated; use only as `reference_only_user_authorized`.
- NoAI check: no explicit NoAI or equivalent restriction found; this is not a permission grant.
- Fit: complete full-body archer, bone-spiked shoulder/rib/skull/claw motifs, and a readable bow.
- Gaps: no distinct quiver or knife; distant spear-like prop is not carried by the archer; human face and low-poly screenshot presentation weaken the feral gate.

### Existing Blackguards candidate validation

- Source file: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_gamepro_blackguards_2398929.jpg`.
- Source SHA-256: `86965DD293DB0BAC1F3F983BD9CC90C473BE95B2998792EBF05925608D6AA93E`.
- Dimensions: `1440x810`.
- Source page: `https://www.gamepro.de/galerien/das-schwarze-auge-blackguards%2C96655.html`.
- Direct image: `https://images.cgames.de/images/gsgp/287/das-schwarze-auge-blackguards-artworks_2398929.jpg`.
- Creator/studio: Daedalic Entertainment production art; individual artist not stated.
- Rights: commercial game/gallery artwork with no third-party reuse license stated; `reference_only_user_authorized` only.
- NoAI check: explicit restriction not found in reviewed page/image metadata; this is not a permission grant.
- Fit: complete full-body low crouch, bow, quiver, visible sidearm.
- Gaps: generic human fantasy silhouette, no feral bone/skull treatment, and sidearm reads closer to a short sword than a narrow knife.
- Status: anatomy-safe provisional; visually superseded by Ferael for parent review, not exact.

### Additional ranked alternates

- `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_steamdb_iratus_undead_archer.jpg` is the Iratus undead archer source, SHA-256 `E52FAB5B801228AB4311E8B4F5EB6677029CA17B9001B5B858994E445E7C101C`, dimensions `1920x1080`, source page `https://store.steampowered.com/app/807120/Iratus_Lord_of_the_Dead/`, direct image `https://shared.fastly.steamstatic.com/community_assets/images/items/807120/bf82ef13c11f2925ca63ae1bf8869c38d8d7d839.jpg`, and archived page `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/source_pages/source_8_steam_iratus_store.html` with SHA-256 `BB019108FB66EAFEB97CAF19B6DCB66F32EDD2AC57B2471676B1A0738984EFEA`; it has bow/quiver/full body and bone/branch armor but no knife and reads as composed undead rather than feral skull hunter.
- `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_alphacoders_bonehelm_huntress_267566.jpg` is the AlphaCoders Bone-Helm Huntress source, SHA-256 `597BC616BACEF616C62B875A6B33E99AE25C54A1EBAA6C03A72CC4E00D0925F7`, dimensions `1920x1080`, source page `https://wall.alphacoders.com/big.php?i=267566`, direct image `https://images4.alphacoders.com/267/thumb-1920-267566.jpg`, and archived page `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/source_pages/source_9_alphacoders_bonehelm.html` with SHA-256 `A5194309BF193893B0D27BF751F66645A0398E56C88AF6C6E26E413D70976046`; it has a strong skull helm and bow but is a tight crop without readable full body, quiver, or knife, and its private-use/contact-artist wording leaves rights uncertain.
- `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_magicartworld_archer_fantasy.jpg` remains a provenance-uncertain hooded archer alternate, SHA-256 `2D16DA4A8E7A605F80B885B01964900C87FF4D3077861FF3AA7981D18F0CEDEE`, dimensions `750x1365`, source page `https://magicartworld.com/female-warriors-inspiration-art/`, direct image `https://magicartworld.com/wp-content/uploads/2019/08/Archer-Fantasy.jpg`; it has bow/quiver and two narrow blade-like knives but no bone/skull treatment and uncertain original attribution.

Network comparison sheet: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/contact_sheet_network_candidates_2026-08-24_v3.png` with SHA-256 `2404F15CD95A60487041B151F3C6DECFEC013F03D149034C3C4C05CDD979168D`.

Network full provenance addendum: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/provenance_addendum_2026-08-24.json`.

Network search log: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/source_search_2026-08-24.md`.

## Bone Riders source archive and block

### Near-miss 1: Awakened Horseman

- Source file: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/candidates/bone_awakened_horseman.jpg`.
- Source SHA-256: `90325F751B1F1BF1B9E7D9FD00F103221ED47A89E43D4C9E518FA5C926390BAD`.
- Dimensions: `720x664`.
- Source page: `https://wiki.guildwars.com/wiki/File:Awakened_Horseman_concept_art.jpg`.
- Direct image: `https://wiki.guildwars.com/images/e/e7/Awakened_Horseman_concept_art.jpg`.
- Creator/studio: Doug Williams, as credited by the Guild Wars Wiki art category.
- Archived pages and SHA-256: `source_5.html` (`2F911EE5A6E167C5440EEF93AF527A2A5C521C7E67B044B319163E0C7360B045`) and `source_6.html` (`57B6B88B7454716DDCE8EFE041AAF34FA489803A3DF03C43FF65773ADFD90858`).
- Rights: commercial Guild Wars artwork with no third-party reuse license stated; `reference_only_user_authorized` only.
- NoAI check: explicit NoAI/equivalent restriction not found; this is not a permission grant.
- Fit: one rider/horse, bone structure, saddle, reins, and strong mounted silhouette.
- Gaps: undead horse, prominent spear, no sling, no stone pouch, no painted skull helmet, one horse leg occluded.

### Near-miss 2: Diablo 4 mount armor sheet

- Source file: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/candidates/bone_diablo_mount.jpg`.
- Source SHA-256: `5AD6EEC5C0410A78EE092CEFDF85C7C48C8CC27FE3EAF259449E9A998328C27A`.
- Dimensions: `4500x2531`.
- Source page: `https://www.windowscentral.com/gaming/diablo-4-blizzard-president-clarifies-how-mounts-work`.
- Direct image: `https://cdn.mos.cms.futurecdn.net/8bpBNBz2hHEmp7xWTvQHQD.jpg`.
- Creator/studio: Blizzard Entertainment production art; individual artist not stated.
- Archived page: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/source_pages/source_2.html` with SHA-256 `3894E41C001BED5F97F1FAE3F86859F01BCB585F434059CB7BC6C6ED5C336EFD`.
- Rights: commercial Diablo production art with no third-party reuse license stated; `reference_only_user_authorized` only.
- NoAI check: explicit NoAI/equivalent restriction not found; this is not a permission grant.
- Fit: living-looking central horse, skull/bone-like head and segmented armor, saddle/reins/tack cues.
- Gaps: rider absent, sling absent, pouch absent, skull helmet absent, multi-view sheet, spear-like equipment visible, no single four-leg mounted composition.

Bone Riders comparison sheet: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/contact_sheet_bone_candidates.png` with SHA-256 `985F98A7D52CF94D1E9F7BEBB8A683DAB72894EFE8E2900BF6697ED0B57B3FFC`.

Bone Riders full provenance addendum: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/provenance_addendum_2026-08-24.json`.

Bone Riders search log: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/source_search_2026-08-24.md`.

### Bone Riders exhaustive search conclusion

Searches covered mounted slinger fantasy art, game concept art, tabletop miniatures, skull barding, bone horse armor, horse rider sling, stone pouch, mounted skirmisher, ArtStation, MobyGames, DeviantArt, and related game-art queries.

Search results were rejected when they showed undead horses, riderless sheets, generic cavalry, spear-bearing substitutes, separate components, historical/ethnographic material, or no visible sling and ammunition pouch.

No exact Bone Riders source is archived or approved.

## Processing boundary

Source bytes are untouched.

The newly archived Network candidates have no processed PNG or DDS derivatives by this source-only task scope.

Existing evidence PNG/DDS files remain non-runtime comparison outputs.

The parent must pass any approved Internet source through native ImageGen for faithful high-resolution cleanup and genuine alpha isolation before Meshy.

This handoff does not authorize redesign, invented weapons, compositing, ImageGen calls, Meshy submission, GFX edits, or runtime wiring.

Proposed runtime basenames if the parent eventually approves exact sources are `cannibal_network_cadre` and `cannibal_bone_riders`.
