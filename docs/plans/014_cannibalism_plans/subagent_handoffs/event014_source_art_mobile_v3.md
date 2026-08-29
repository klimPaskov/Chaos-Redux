# Event 014 sourced 3D input handoff: mobile source-art pass v3

Historical supersession notice: this source-only pass predates the 2026-08-26 decision to use vanilla `sprite = infantry` for Network Cadre and vanilla `sprite = cavalry` for Bone Riders. Its source findings remain lineage evidence only, and neither job is a current custom-model queue.

Research date: 2026-08-24.

Scope: source-only research and archival for exactly cannibal_network_cadre and cannibal_bone_riders.

No gameplay, GFX, ImageGen derivative, Meshy, provider, runtime wiring, or unrelated repository file was edited.

No commit was created.

## Decision summary

cannibal_network_cadre is needs_user_review_strong_core_match_no_knife.

The prior Blackguards candidate was validated as anatomy-safe, but it is an ordinary human fantasy archer with no feral skull or bone treatment.

The strongest new source is Jason Pierson's attributed Female Goblin Archer illustration.

It is one full-body living fleshy goblin with an aggressive predatory grin, oversized skull helmet, bone collar/chest/belt armor, a fully readable bow, and a packed quiver.

It is materially stronger than the prior AFK Arena Ferael candidate because it is living and fleshy rather than literally undead.

It is not marked exact because no separate knife or short blade is readable, and a long spear-like shaft is strapped diagonally behind the body and must not be silently relabeled as a knife.

cannibal_bone_riders is blocked_no_exact_single_image_source.

The deeper search found no one modern single artwork containing all mandatory Bone Riders features: living four-legged horse, skull/rib/long-bone barding, coherent tack, mounted living feral warrior, painted skull helmet, visible sling, visible stone pouch, and no spear/lance/sword substitute.

The strongest Bone Riders near-misses are Awakened Horseman, the Diablo 4 mount armor sheet, and the new House Sanguin RimWorld horse-bone-armor sheet.

All three are rejected for explicit mandatory gaps, and no composite or generated fallback was made.

## Network Cadre selected core candidate

Source file: docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_artstation_jason_pierson_female_goblin_archer.jpg.

Source SHA-256: 91AC5D91F983480C6F41288E8B3871651AD1FB9C90672C1D98CCE464B00E7143.

Dimensions: 1920x2000.

Source page: https://www.artstation.com/artwork/lVXyrk.

Direct source image: https://cdnb.artstation.com/p/assets/images/images/019/129/225/large/jason-pierson-jasonpierson-fgoblinarcherwide.jpg?1562141562.

Archived attribution/provenance mirrors:
- docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/source_pages/source_17_pinterest_jason_pierson_goblin_archer_original.html, SHA-256 EEE8CFDEDBAF5D0C9D7F06CEBF9BB8173BA949E534E1FB74646BB8D767AFC154.
- docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/source_pages/source_15_pinterest_jason_pierson_goblin_archer.html, SHA-256 8E28A6B02140EF57A87D156F9A41058DFA62DD9978A8BC1AC7F2F99A0571D697.

The ArtStation page itself was Cloudflare-blocked during retrieval; the archived Pinterest mirrors preserve the original ArtStation link, creator title, and direct source-image URL.

Creator: Jason Pierson, credited on-image and in the source filename.

Publisher/studio: independent ArtStation project; archived Pinterest description identifies it as a goblin archer illustration being considered for a tabletop RPG book.

Rights: no reuse license is stated on the ArtStation or Pinterest material. Treat it as copyrighted and use only as reference under reference_only_user_authorized.

NoAI check: no explicit project-specific NoAI, do-not-train, or equivalent restriction was observed in the archived source-page metadata or Pinterest mirror. This is not a permission grant.

Exact fit: living fleshy green goblin, full body with both feet, aggressive feral expression, skull helmet, bone armor, bow, and packed quiver.

Exact gaps: no separate knife or short blade. A long shaft with a broad spear-like metal head is strapped diagonally behind the body, so the parent must disclose it and must not convert it into a knife by prompt or processing. The source also contains a creator watermark and an opaque painted background.

Disposition: strongest Network Cadre core match, needs parent review before any downstream ImageGen cleanup.

## Network ranked alternates

Rank 2 is Michael LaRiccia's Savage Planet card-game illustration.

Source: docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_savage_planet_archer.webp.

SHA-256: 8E1424127CDE750A94A15C6B53A01C2A69DDAC28ED4B763C01EB3CEAC22F482B.

Dimensions: 1200x1637.

Source page: https://www.behance.net/gallery/56479837/Savage-Planet-card-game-illustrations-2.

Direct image: https://mir-s3-cdn-cf.behance.net/project_modules/hd_webp/c6c24656479837.59b0376292b81.jpg.

Archived page: docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/source_pages/source_18_behance_savage_planet.html, SHA-256 553C0A52B853C65629BEF7E8241EB817CD651CED98A43939E420A7E4A55BAD7C.

It is a full-body living tribal archer with fur and bone ornaments, bow, and quiver, but it lacks a distinct skull helmet and visible knife and reads more human than goblin or explicit cannibal.

The direct URL ends in .jpg but the downloaded bytes identify as WebP; the local extension records the actual container without altering the bytes.

No reuse license or explicit NoAI restriction is stated, so it is copyrighted reference-only under reference_only_user_authorized.

Rank 3 is Dmitriy Poskrebyshev's commercial Unity Goblin Archer in Bone Armor render.

Source: docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_unity_goblin_bone_armor_1.jpg.

SHA-256: 31B5F87E21C289E2D4DE0EDAF97B9FCFF28501520134C45F600BAC0423FE8853.

Dimensions: 1200x675.

Source page: https://www.gameassetdeals.com/asset/205545/goblin-archer-in-bone-armor.

Direct image: https://assetstorev1-prd-cdn.unity3d.com/package-screenshot/331fc058-7f8d-4131-a664-95e7e50f6f8c_scaled.jpg.

Archived page: docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/source_pages/source_19_gameassetdeals_goblin_bone_armor.html, SHA-256 6BFE0FBF3263177EE87241EE10C86431F6EB2CCCC5014E1387649536FACEB9CC.

It is a full-body living goblin with bone chest/limb armor, skeletal bow construction, and quiver, but has a neutral asset-render stance, hood rather than a skull helmet, no knife, and black studio background.

The listing is a paid commercial asset with no free reuse license or explicit NoAI restriction stated, so it is reference-only under reference_only_user_authorized.

Rank 4 is Warrior Epic Artwork 1.

Source: docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_gamefragger_warrior_epic_7039.jpg.

SHA-256: 71691B33283B64E5DB6F6167A586024B4DABC5DE62B1EA573A9BCCDE2C9938B8.

Dimensions: 676x1024.

Source page: https://gamefragger.com/pc/massively-multiplayer/warrior-epic/pictures/warrior-epic-artwork-1-i7039.

Direct image: https://gamefragger.com/images/pictures/7039L.jpg.

It has a skull-like mask, bow, quiver, and side blade, but lower anatomy is obscured, the blade is not a narrow knife, and the armor reads polished fantasy rather than living tribal bone.

Rank 5 is the existing Blackguards gallery image.

Source: docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_gamepro_blackguards_2398929.jpg.

SHA-256: 86965DD293DB0BAC1F3F983BD9CC90C473BE95B2998792EBF05925608D6AA93E.

Dimensions: 1440x810.

Source page: https://www.gamepro.de/galerien/das-schwarze-auge-blackguards%2C96655.html.

Direct image: https://images.cgames.de/images/gsgp/287/das-schwarze-auge-blackguards-artworks_2398929.jpg.

The source page could not be freshly archived on 2026-08-24 because the request returned HTTP 403; the direct image bytes remain archived and the page/direct URLs are recorded.

It remains the cleanest generic full-body human anatomy reference with bow, quiver, and sidearm, but is visually superseded by Jason Pierson.

Rank 6 is the existing Narrow One bone-armored archer.

Source: docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_narrow_one_bone_archer.png.

SHA-256: C2F5AAE2CE9C3F435B95AC21C6EE486FA375A822296D1002A36573D19D51A6C5.

Dimensions: 2620x1578.

Source page: https://pelicanparty.itch.io/narrow-one.

Direct image: https://img.itch.zone/aW1hZ2UvMTA1MDU4MC84MzIxODYzLnBuZw%3D%3D/original/6crcVY.png.

It supplies full-body living bone motifs and a bow, but no distinct quiver or blade and has a human face.

The prior Ferael and Iratus candidates are explicitly rejected in this v3 pass because they are literal undead, even though they show bow, quiver, and bone/skull language.

## Bone Riders near-miss archive

### Rank 1: Awakened Horseman

Source: docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/candidates/bone_awakened_horseman.jpg.

SHA-256: 90325F751B1F1BF1B9E7D9FD00F103221ED47A89E43D4C9E518FA5C926390BAD.

Dimensions: 720x664.

Source page: https://wiki.guildwars.com/wiki/File:Awakened_Horseman_concept_art.jpg.

Direct image: https://wiki.guildwars.com/images/e/e7/Awakened_Horseman_concept_art.jpg.

Creator: Doug Williams, as credited by the Guild Wars Wiki art category.

Gaps: undead horse, prominent spear, no sling, no stone pouch, no painted skull helmet, and one leg occluded.

Rights and NoAI: no reuse license or explicit NoAI restriction stated; copyrighted reference-only under reference_only_user_authorized.

### Rank 2: Diablo 4 mount armor sheet

Source: docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/candidates/bone_diablo_mount.jpg.

SHA-256: 5AD6EEC5C0410A78EE092CEFDF85C7C48C8CC27FE3EAF259449E9A998328C27A.

Dimensions: 4500x2531.

Source page: https://www.windowscentral.com/gaming/diablo-4-blizzard-president-clarifies-how-mounts-work.

Direct image: https://cdn.mos.cms.futurecdn.net/8bpBNBz2hHEmp7xWTvQHQD.jpg.

Creator/studio: Blizzard Entertainment production art.

Gaps: rider absent, no sling, no stone pouch, no painted skull helmet, multi-view riderless sheet, and spear-like equipment visible.

Rights and NoAI: no reuse license or explicit NoAI restriction stated; copyrighted reference-only under reference_only_user_authorized.

### Rank 3: House Sanguin RimWorld horse bone armor sheet

Source: docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/candidates/bone_rimworld_house_sanguin_horse_bone_armor.jpg.

SHA-256: 5EB2696D0D1C18923881F85BA1C16E5563DA30F201E5BB7B8C0AE277E163BF2E.

Dimensions: 1202x676.

Source page: https://rimworldbase.com/%E2%86%81-house-sanguin-mod/.

Direct image: https://steamuserimages-a.akamaihd.net/ugc/2027217558437046681/01F6F7971C55FE95E5E9BB223E511B690985F9D6/?ima=fit&imcolor=&imh=5000&impolicy=Letterbox&imw=5000.

Archived page: docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/source_pages/source_7_rimworld_house_sanguin_mod.html, SHA-256 327AD3677050B222558183A5008AF592799665526931C8F35022161B310CDA8A.

Creator/studio: House Sanguin RimWorld mod artwork, author not identified on the mirror; image hosted via Steam user content.

Fit: living-looking dark horse designs with long-bone, rib, spine, and skull-like barding, bridles, and saddles.

Gaps: three riderless designs, no mounted warrior, no painted skull helmet, no sling, no stone pouch, and no single four-leg mounted composition.

Rights and NoAI: no reuse license or identified rights holder is stated; provenance is uncertain and use is reference-only under reference_only_user_authorized. No explicit NoAI/equivalent marker was observed.

## Bone Riders search conclusion

Search coverage included mounted slinger fantasy art, game concept art, tabletop miniatures, skull barding, bone horse armor, horse rider sling, stone pouch, mounted skirmisher, ArtStation, MobyGames, DeviantArt, and related game-art queries.

The search returned mostly undead mounts, spear/lance cavalry, generic cavalry, riderless barding sheets, separate miniature parts, historical or ethnographic imagery, and AI-generated or provenance-uncertain material.

No single source showed all required living-horse, four-leg, bone-barding, tack, mounted-warrior, painted-skull-helmet, sling, stone-pouch, and no-spear features.

No exact Bone Riders source is archived or approved.

## Contact sheets and manifests

Network comparison sheet: docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/contact_sheet_network_candidates_2026-08-24_v4.png.

Network contact-sheet SHA-256: F47E2AFDE8D9D9711B43634DCF0E6836EC4D4EAD74351B23BAD5678A3821025C.

Network sheet order is Jason Pierson, Savage Planet, Unity Goblin Archer, Warrior Epic, Blackguards, Narrow One, Ferael, and Iratus.

Bone Riders comparison sheet: docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/contact_sheet_bone_candidates_2026-08-24_v2.png.

Bone Riders contact-sheet SHA-256: D9C42D548E2F0CF110FE2FFECB126D49005A73379E120B43C98171F4BFF341D.

Bone Riders sheet order is Awakened Horseman, Diablo 4 mount armor, and House Sanguin horse bone armor.

Full v3 provenance manifests:
- docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/provenance_addendum_2026-08-24_v3.json.
- docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/provenance_addendum_2026-08-24_v3.json.

Full v3 search logs:
- docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/source_search_2026-08-24_v3.md.
- docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/source_search_2026-08-24_v3.md.

## Processing and parent boundary

All source bytes are untouched.

No ImageGen, crop, redraw, compositing, background removal, Meshy submission, provider operation, runtime wiring, GFX change, PNG derivative, or DDS derivative was performed.

If the parent approves the Jason Pierson Network source, it must be sent through native ImageGen for faithful higher-resolution cleanup and genuine alpha isolation before Meshy, without redesigning the goblin, inventing a knife, or silently removing the strapped long weapon.

Bone Riders has no approved source to pass downstream.

The source subagent does not own or use any Meshy provider task or live @meshy-ai/meshy-mcp-server process.

Proposed runtime basenames, only if the parent later approves suitable exact sources, are cannibal_network_cadre and cannibal_bone_riders.

## Simplifications, omissions, and blockers

Network Cadre is not exact because the strongest living candidate lacks a visible knife or short blade and includes a strapped spear-like long weapon.

The former source search recorded Bone Riders as blocked because no single image satisfied the full living horse, bone barding, mounted warrior, sling, stone pouch, and no-spear gate; that custom-model gate is superseded by the approved vanilla `sprite = cavalry` decision.

No generated, composited, undead, historical, ethnographic, documentary, or explicit NoAI-restricted fallback was used.
