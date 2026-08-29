# Event 014 source recovery specialists v5

Research date: 2026-08-24.

Scope: source-only recovery for `cannibal_island_reavers`, `cannibal_siege_eaters`, and `cannibal_march_predation_column`.

Result: all three roles remain blocked. No source is approved for ImageGen or Meshy.

## Exact role blockers

- `cannibal_island_reavers`: `blocked_exact_role_source_not_found`. Fresh harpoon/coastal-hunter search found a modern stock concept with a harpoon-like spear, but it is a generic fur-clad hunter with decorative script-like markings, no cannibal identity, no exposed feral flesh, no skull/bone kit, and culturally ambiguous styling. The strongest living cannibal references still lack either a readable harpoon/coastal weapon, conspicuous intentional paint, culture-neutral styling, or skull/bone equipment in the same image.
- `cannibal_siege_eaters`: `blocked_exact_role_source_not_found`. Fresh cannibal/brute/maul search found a high-quality living skull-equipped cannibal render, but it is cropped, uses dual cleavers, includes substantial metal/chainmail armor, and has no two-handed maul, sledge, or breaching club or conspicuous intentional paint. The strongest siege-scale Man Eater remains an unpainted beam/harness carrier, while the painted Tooth Wu character uses cleaver/whip weapons.
- `cannibal_march_predation_column`: `blocked_exact_role_source_not_found`. No searched or re-reviewed source combines a lean living marcher, conspicuous culture-neutral paint, exposed flesh, rough scavenged layers, skull/bone kit, bow, quiver/arrow bundle, and secondary close weapon. The Bestiarum comparison image is unpainted and does not visibly contain the required bow/quiver pair; the painted Behance archer is culturally anchored/ambiguous and equipment-incomplete; the Tooth Wu hunter is heavily armored and carries the wrong ranged system.

## Evidence paths

- `docs/assets/014_cannibalism/models_3d/cannibal_island_reavers/refs/source/recovery_v5/source_audit.md`
- `docs/assets/014_cannibalism/models_3d/cannibal_island_reavers/refs/source/recovery_v5/contact_sheet_recovery_v5.png`, SHA-256 `BF33D4D4166530C17E5724269F8ABB13598668AAD86CEA27115482DA6565BE7B`
- `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/refs/source/recovery_v5/source_audit.md`
- `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/refs/source/recovery_v5/contact_sheet_recovery_v5.png`, SHA-256 `806FB62F8317157087D59FFFC89879732B92A89D06593EFC9BC19CBBFB89DF26`
- `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/refs/source/recovery_v5/source_audit.md`
- `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/refs/source/recovery_v5/contact_sheet_recovery_v5.png`, SHA-256 `14843F1B3AA7BB02CEB19DA264CFE58A0EF52D2A1A8E3A0109F93B3D3BF593E5`

The v5 candidate folders contain untouched downloaded bytes or byte-identical comparison copies. Page snapshots, source URLs, attribution, dates, terms, reference-only status, NoAI checks, dimensions, sizes, and SHA-256 hashes are recorded in the per-role audits. Contact sheets are review-only derivatives and all tiles are labelled `REJECTED`.

## Search and policy coverage

Fresh queries covered fantasy cannibal harpoon/coastal spear/body paint/skull-bone character art, painted cannibal raider miniatures, cannibal two-handed maul/sledge/bone armor character art, painted cannibal archer bow/quiver/knife miniatures, game-concept cannibal hunters, and tabletop Man Eaters. Search results were also checked against the earlier strongest near-misses so that the exact failing attributes were re-evaluated visually.

Historical, archival, museum, archaeological, ethnographic, documentary, reenactment, real-cultural, undead, skeleton, goblin/orc, knightly, plate/lamellar, grayscale-as-final, generic fantasy soldier, AI-generated, and explicit NoAI/equivalent-restricted sources were not promoted. No compositing, redesign, ImageGen, Meshy, provider call, gameplay edit, GFX edit, runtime edit, crop, background removal, or DDS processing was performed.

No commit was created because all three exact passes were required for an isolated commit and none passed.

