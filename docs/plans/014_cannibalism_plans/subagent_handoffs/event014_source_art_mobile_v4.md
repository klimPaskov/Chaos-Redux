# Event 014 sourced 3D input handoff: mobile source-art pass v4

Historical supersession notice: this source-only pass predates the 2026-08-26 decision to use vanilla `sprite = infantry` for Network Cadre and vanilla `sprite = cavalry` for Bone Riders. Its source findings remain lineage evidence only, and neither job is a current custom-model queue.

Research date: 2026-08-24.

Scope: source-only research and archival for exactly `cannibal_network_cadre` and `cannibal_bone_riders`.

No gameplay, GFX, ImageGen derivative, Meshy, provider, runtime wiring, or unrelated repository file was edited. No commit was created because neither requested source passed the corrected exact gate.

## Decision summary

`cannibal_network_cadre` is `blocked_exact_gate_unmet`.

The strongest fictional human/cannibal source is Bestiarum's Man Eaters Fleshmad Hunter miniature family. Hunter 1 supplies the best combined core of living humanoid anatomy, crude bow, arrow bundle/quiver, skull chest piece, rough hide/rope layers, and visible short blade. Hunter 4 has the clearest oversized bow/quiver and hunter silhouette. Both are monochrome unpainted sculpt renders, so neither evidences the user's mandatory obvious face/body paint. Neither is promoted to ImageGen or Meshy.

The painted living candidates were rejected because they are culturally anchored or ambiguous, lack bow/quiver/skull armor, or are named game tribes outside the culturally unanchored fictional gate. Goblin, undead, knightly, polished-armored, generic, and ordinary fantasy archer candidates remain rejected.

`cannibal_bone_riders` is `blocked_no_exact_single_image_source`.

No one modern single artwork was found that simultaneously shows a living four-legged horse with readable tack and skull/rib/long-bone barding, a living painted feral cannibal rider with exposed flesh and rough scavenged gear, a visible sling, and a visible stone/ammunition pouch without a spear/lance/sword substitute.

The strongest newly archived rider near-miss is Bestiarum's Slaughter Chief on Manswine. It has a living fictional Man Eater rider and bone armor, but the mount is a monstrous pig/Manswine rather than a horse and the weapon is a mace/cleaver, with no sling or stone pouch. It is explicitly rejected. House Sanguin supplies only riderless horse-barding views; Awakened Horseman is undead and spear-bearing; Diablo is a riderless mount armor sheet.

No cleaned input exists for either unit.

## Network Cadre source archive and gate result

### Strongest core near-match: Bestiarum Fleshmad Hunter 1

Source file: [network_bestiarum_fleshmad_hunter_1.jpg](../../../assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_bestiarum_fleshmad_hunter_1.jpg).

Relative source path from the mod root: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_bestiarum_fleshmad_hunter_1.jpg`.

Source SHA-256: `22BF8A443F2B423FBF815B3D175958553EF8E4E44A725388C2FC65A112B7B7A0`.

Dimensions: 2000x2000.

Source page: https://bestiarumgames.com/products/flesh-hunters-man-eaters-bestiarum-miniatures-d-d-wargaming-dnd.

Direct image: https://bestiarumgames.com/cdn/shop/files/07_FleshmadHunter1.jpg?v=1749571234.

Archived page: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/source_pages/source_30_bestiarum_fleshmad_hunters.html`, SHA-256 `844DEC930381F4FF4115F8A998AA63B0DF328F66E95F26C2EAAA595AD2294D59`.

Creator/studio: Bestiarum Games / Bestiarum Miniatures; individual sculptor is not stated on the product page.

Rights: copyrighted commercial product imagery with no public reuse license stated; `reference_only_user_authorized` only.

NoAI check: no explicit NoAI, do-not-train, or equivalent restriction was observed in the archived product page or image metadata. This is not permission.

Exact fit: product-level Man Eaters/Fleshmad Hunters are fictional cannibals; the individual is one full-body living humanoid with crude bow, readable arrow bundle/quiver, skull chest piece, rough hide/fur/rope layers, and a short blade.

Exact gaps: gray unpainted sculpt render, so obvious face/body paint is not evidenced; head is horned/rough rather than a distinct skull helmet; opaque studio background and watermarks remain. It is a near-match only and is not approved downstream.

### Second core near-match: Bestiarum Fleshmad Hunter 4

Source file: [network_bestiarum_fleshmad_hunter_4.jpg](../../../assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_bestiarum_fleshmad_hunter_4.jpg).

Relative source path from the mod root: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_bestiarum_fleshmad_hunter_4.jpg`.

Source SHA-256: `6478AF1A9032883ECA63042AAA276857232CF87B6C9A8F3A7F76837B294916F4`.

Dimensions: 2000x2000.

Source page: https://bestiarumgames.com/products/flesh-hunters-man-eaters-bestiarum-miniatures-d-d-wargaming-dnd.

Direct image: https://bestiarumgames.com/cdn/shop/files/07_FleshmadHunter4.jpg?v=1749571234.

Creator/studio, rights, and NoAI posture: Bestiarum Games / Bestiarum Miniatures; individual sculptor not stated; copyrighted commercial reference-only under `reference_only_user_authorized`; no explicit NoAI/equivalent restriction observed, not a permission grant.

Exact fit: clearest oversized crude bow, large arrow bundle/quiver, full living humanoid anatomy, rough hide/rope construction, and aggressive hunter silhouette in the set.

Exact gaps: gray/unpainted, no obvious face/body paint, weaker skull/bone torso language than Hunter 1, and no clear knife. Not approved and no cleaned input exists.

### Painted and fleshy alternates rejected

Vladislav Stain's Behance [Cannibal tribe (2)](https://www.behance.net/gallery/66094001/Cannibal-tribe/modules/386797513) was archived at `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_behance_vladislav_stain_cannibal_tribe.jpg` with SHA-256 `002DCCD27B16AD5F20E8A533219CD121E415B71F3D979675587BEBC9A4FA5A7A` and dimensions 1920x3029. It has obvious white face/body paint, exposed living flesh, rough cloth, a skull shoulder trophy, and a bow, but no clear quiver or knife and reads culturally anchored/ambiguous. It is copyrighted reference-only; no explicit NoAI marker observed. Rejected under the current cultural and equipment gates.

Far Cry Primal's [Ull](https://www.creativeuncut.com/gallery-30/fcp-ull.html) was archived at `network_farcry_primal_ull.jpg` with SHA-256 `7856E9631A3B9CBC535B49393060ADBCF4DD7B09FF781D8E8ABCEA13B9BE3081` and dimensions 900x1300. It supplies a living fleshy named Udam cannibal with blood/paint-like markings, rough fur/hide, rib/skull-like chest protection, and crude knives, but no bow or quiver and fails the culturally unanchored gate. Copyrighted Ubisoft production art; no explicit NoAI marker observed. Rejected.

GACHKOVSKYY's [Savage Cannibal Pack](https://www.gameassetdeals.com/asset/385726/savage-cannibal-pack) was archived at `network_gachkovskyy_savage_cannibal_pack.jpg` with SHA-256 `0227A224806BC18056C1FAA6E7FA02F1F6196D6DC8046C20024C149119C4575C` and dimensions 1200x675. It supplies fleshy living cannibal variants with blood/body-tattoo markings and rough cloth, but no bow, quiver, skull/bone armor, or short blade. Copyrighted paid Unity asset; no explicit NoAI marker observed. Rejected.

The Wagadu Chronicles [Black Ancestor Art](https://www.creativeuncut.com/gallery-42/twc-black-ancestor.html) was archived at `network_wagadu_black_ancestor.jpg` with SHA-256 `B057B2E66140E93933BAD68F378EF1C7B619036F66333BA99608D24EB0B108D3` and dimensions 1000x1250. It supplies paint, skull mask, bow/arrows, and bone/rib elements, but is explicitly tied to an Afro-fantasy setting drawing on living African aesthetics and mythology, with incomplete lower anatomy and no clear quiver or knife. Rejected.

Alexander Chiveli Navarro's [Cannibal: Stylized Character Breakdown](https://80.lv/articles/cannibal-stylized-character-breakdown) was archived at `network_80lv_alexander_chiveli_cannibal_color.jpg` with SHA-256 `3FA9E506E6639D287C28FC373C09404EB10BDD29DDDD199C14F3B9F7904ADAB5` and dimensions 1920x1080. It is a polished melee character with no bow/quiver/paint; rejected.

Hot Goblin search snippets identify a real `Cannibal Tribe Archer` / `Bone Mask Tracker` product at https://www.hotgoblin.jp/jp/RelatedProducts?Product=21082, but the site returned maintenance/403 responses and no image bytes could be archived or inspected. It is an unarchived lead, not an accepted candidate.

The prior Jason Pierson Female Goblin Archer remains rejected because it is a goblin, despite its bow, quiver, skull helmet, and bone armor. Ferael and Iratus remain rejected as literal undead. Blackguards remains an anatomy-safe ordinary fantasy archer, not a feral painted cannibal.

## Bone Riders near-miss archive

### Strongest mounted cannibal near-miss: Bestiarum Slaughter Chief on Manswine

Source file: [bone_bestiarum_slaughter_chief_manswine.jpg](../../../assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/candidates/bone_bestiarum_slaughter_chief_manswine.jpg).

Relative source path from the mod root: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/candidates/bone_bestiarum_slaughter_chief_manswine.jpg`.

Source SHA-256: `F8FB7E86B8AEB41843858BD9AB977EF338D6A702072C62F0F46CF090BABB136C`.

Dimensions: 1080x1080.

Source page: https://bestiarumgames.com/products/mounted-warleader-man-eaters-bestiarum-miniatures-d-d-wargaming-dnd.

Direct image: https://bestiarumgames.com/cdn/shop/files/04_SlaughterChiefonManswine_Front_Scale.jpg?v=1749571882&width=1080.

Archived page: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/source_pages/source_8_bestiarum_slaughter_chief_manswine.html`, SHA-256 `24312B16C3778F8BD255DE9DAE474EF0EE3C5B7474D7383A070055A5A72DE816`.

Creator/studio: Bestiarum Games / Bestiarum Miniatures; individual sculptor is not stated.

Rights: copyrighted commercial imagery with no public reuse license stated; `reference_only_user_authorized` only.

NoAI check: no explicit NoAI/equivalent restriction observed; this is not permission.

Exact fit: one living fictional Man Eater rider with fleshy modeled anatomy, rough hide/rope construction, strong skull/bone armor, and a coherent harnessed mount.

Exact gaps: mount is a monstrous pig/Manswine, not a living horse; weapon is a large mace/cleaver-like melee item; no visible sling; no stone/ammunition pouch; gray render does not evidence obvious paint. Rejected and must not be converted into a horse/slinger by ImageGen, compositing, or prompt.

The companion [Butcherguard on Manswine group](https://bestiarumgames.com/products/mounted-warleader-man-eaters-bestiarum-miniatures-d-d-wargaming-dnd) is archived at `bone_bestiarum_butcherguard_manswine_group.jpg` with SHA-256 `81C541D4F3331710D4EC6526DC8CDA3994F76B214AA2CC4EC78270CFD2B7A328` and dimensions 1080x1080. It is a group of pig-mounted cannibals with cleavers/axes and no sling/pouch, so it is rejected.

House Sanguin RimWorld horse-bone armor is archived at `bone_rimworld_house_sanguin_horse_bone_armor.jpg` with SHA-256 `5EB2696D0D1C18923881F85BA1C16E5563DA30F201E5BB7B8C0AE277E163BF2E` and dimensions 1202x676. It supplies riderless horse barding, bridles, saddles, and rib/long-bone/skull motifs but no rider, paint, sling, or stone pouch. Rejected.

Awakened Horseman is archived at `bone_awakened_horseman.jpg` with SHA-256 `90325F751B1F1BF1B9E7D9FD00F103221ED47A89E43D4C9E518FA5C926390BAD` and dimensions 720x664. It is an undead/skeletal horse and rider with a prominent spear, no sling or pouch. Rejected.

The Diablo IV mount armor sheet is archived at `bone_diablo_mount.jpg` with SHA-256 `5AD6EEC5C0410A78EE092CEFDF85C7C48C8CC27FE3EAF259449E9A998328C27A` and dimensions 4500x2531. It is a riderless multi-view horse armor sheet with no living painted cannibal, sling, or pouch, plus spear-like equipment. Rejected.

## Search coverage and blocker evidence

Queries covered living horse skull bone barding mounted slinger fantasy art, mounted sling warrior horse bone armor game concept, horse rider sling stone pouch, fantasy miniature mounted slinger bone horse barding, tabletop horse bone armor rider sling, living horse rib armor feral rider, skull barding horse game character, mounted cannibal slinger, mounted primitive warrior sling, and related modern game, professional portfolio, ArtStation, and miniature terms.

The deeper search returned undead or skeletal horses, spear/lance cavalry, polished knights, generic cavalry, riderless armor diagrams/sheets, wrong mounts such as pigs and big cats, text-only references, and culturally anchored imagery. Historical, ethnographic, documentary, reenactment, archaeological, generated, and explicit NoAI/equivalent-restricted sources were not archived.

No single source showed all mandatory features in one coherent artwork. The former Bone Riders source gate was blocked; the custom-model requirement is superseded by the approved vanilla `sprite = cavalry` decision, so no riderless sheet, wrong mount, spear-bearing substitute, composite, or generated invention is an active input.

## Contact sheet

Comparison sheet: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/contact_sheet_bone_candidates_2026-08-24_v3.png`.

Contact-sheet SHA-256: `30AA0EE85B6EC09DB549AF3453E211107A459E50D16888E0F9F4A18FA1C58417`.

Order: Bestiarum Slaughter Chief on Manswine, Bestiarum Butcherguard on Manswine group, Awakened Horseman, Diablo IV mount armor, House Sanguin horse bone armor.

Parent review rejected all tiles under the corrected gate: Manswine mounts are pigs, Awakened Horseman is undead and spear-bearing, Diablo is riderless, and House Sanguin is riderless. The sheet is comparison-only and does not replace or modify source bytes.

## Processing boundary

All archived source bytes are untouched.

No ImageGen, background removal, crop, redraw, compositing, Meshy submission, provider operation, runtime wiring, GFX change, PNG derivative, or DDS derivative was performed.

No cleaned input exists. If a future exact source is found, the parent may pass one untouched approved artwork through native ImageGen for faithful higher-resolution cleanup and genuine alpha isolation before Meshy, without inventing or compositing the horse, rider, paint, bone armor, sling, stone pouch, or weapon choice.

## Simplifications, omissions, and blockers

Network Cadre has no exact accepted source because the strongest fictional cannibal archer renders are unpainted and the painted options are culturally anchored or equipment-incomplete.

Bone Riders has no exact accepted source because the required living horse, bone barding, living painted cannibal rider, sling, stone pouch, and no-spear combination was not found in one image.

No generated, composited, undead, goblin, knightly, historical, ethnographic, documentary, reenactment, or explicit NoAI-restricted fallback was used.
