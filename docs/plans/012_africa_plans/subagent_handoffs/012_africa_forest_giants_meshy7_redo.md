# Event 012 Africa — Forest Giants Meshy 7 redo handoff

Date: 2026-08-27. Status: `blocked_fresh_meshy7_identity_loss_insufficient_recovery_balance`.

## Outcome

The current hard gate, dependency lock, exact-model schema, Blender bridge, and approved-reference gates all passed. Fresh exact-`meshy-7` task `01a04333-952c-7726-a8c9-8e9ae388049a` used only `refs/original/meshy_input.png` SHA-256 `24CAB4399F694DAA0390AC8AD91FC48B8ED5FF260878BA883F0B714345F1DA41`. It consumed 30 credits, reducing balance from 43 to 13. GLB SHA-256 `60E01F77E07E0EFD6E2FF00F76A34184DEEE606AF2307C5C17C6122F5C4923B1` and FBX SHA-256 `DA62B06EF8170C53E3A7F18BC31653E47D28FF7CE144DFB03E9BF5D63D35ECD6` were downloaded immediately.

Blender adapter request `59d61aa6bc25416baa9653c3271523d2` produced a technically clean 25,000-triangle T-pose candidate with one object, 12,474 vertices, valid UVs, ground contact 0, and zero degenerates, non-manifold edges, loose boundaries, negative-scale objects, or zero-length normals. Seven-view inspection nevertheless rejected the geometry because it entirely omitted both defining components: the broad held axe and bound-log offhand implement. Rejected geometry was not rigged, animated, texture-packed for PDX, exported, reimported, or selected for runtime. A fresh recovery costs 30 credits and cannot proceed with balance 13.

The previous natural-remesh/direct-rig/donor-transfer lineage remains rejected evidence only. Direct provider rigging returned HTTP 422 with no provider task; all sanctioned donor weight-transfer methods catastrophically deformed the natural body. No donor, generic humanoid, local-rig final-motion, static, transform-only, semantic-alias, or locally authored action fallback was used.

## Dependency and scale evidence

- Official Meshy MCP `@meshy-ai/meshy-mcp-server` 0.4.0, git `d8c77d1cb897e345eb41d38b510b8391b1664346`, SDK 1.29.0, schema compatibility `meshy-7-v5`.
- Blender 5.1.2 build `ec6e62d40fa9`; repository adapter `chaosx_blender_hoi4` 1.10.14; `127.0.0.1:9876` separately listening; io_pdx_mesh 0.91.0 SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Lock checksums: dependencies `C27768297FB7AD5ACC9C555E7C83DC77856908E2C628BF16D9A420095C64266A`; schema `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`; adapter config `4BC97CA0B07580F5AA04B49E7B9FBD1C07EC88DF5C4D56CD3BA8846E630117AB`.
- Vanilla reference `refs/vanilla/asian_infantry.mesh` SHA-256 `ACCB5F74E3E3484496BF27F6DF1F510AF382B0B3EF7A93FEF22E02826636938A`: 7.516802847 m source height at entity scale 0.8 = 6.013442278 m effective height. Forest target: 18.792008 m at scale 1.0. +Z up, -Y forward.

## Requirement disposition

| Requirement | Status | Evidence or blocker |
| --- | --- | --- |
| Approved modern-art source and source-informed input | `complete` | DM Stash “Trostaka the Vengeful,” reference-only user authorization, source SHA `45A412...35F15`, parent-approved refined SHA `24CAB4...DA41`, non-shipping. |
| Fresh Meshy 7 generation/download | `complete attempt` | Task, request/response, balance, download hashes, maps, and checksums recorded. |
| Identity-faithful geometry | `blocked` | Fresh T-pose omitted axe and bound logs; seven immutable views retained. |
| Provider rig and weights | `blocked` | Rejected geometry not rigged; insufficient balance for another generation. |
| Idle, move, axe attack, emergence, death at 30 FPS | `blocked` | No accepted provider rig or action lineage. No final replacement motion authored locally. |
| PDX material and DDS | `blocked` | Maps preserved only with rejected provider geometry; not promoted. |
| `.mesh` and five `.anim` export/reimport | `blocked` | No accepted geometry, rig, or actions. Existing legacy outputs remain rejected. |
| Non-firing audit | `complete` | Zero firing state/effect/light/locator/sound requirements. |
| Sourced audio | `complete candidates` | Public-domain ambience and CC BY 4.0 quern sources retained; six `pcm_s16le` 44.1 kHz mono candidates and ffprobe/hash receipts added. Action synchronization is blocked. |
| Bespoke large/map counters | `needs_user_review` | Delegated `chaosx_icon_artist` redo; parent contact-sheet review and runtime promotion required. |
| Runtime source-to-destination hashes | `blocked` | None selected or copied; parent must not wire current model/action artifacts. |

## Parent-owned remaining work

Do not wire a Forest Giants `.mesh` or `.anim` from the current package. After credits become sufficient, a future worker must generate a materially different exact-Meshy-7 candidate that retains axe/log identity, pass multi-view identity and technical QA, obtain an accepted provider rig, generate all five distinct substantive provider actions, clean/bake/export/reimport them through the locked adapter, validate contacts and deformation, and then record selected source-to-runtime hashes. Parent must review the counter contact sheets, choose audio candidates only after action phases exist, wire `.asset`/entity/GFX/sound/gameplay/localisation, synchronize copied hashes, and perform live consumer/in-game validation.

Package manifest: `docs/assets/012_africa/models_3d/forest_giants/manifest.md`. Runtime handoff: `docs/assets/012_africa/models_3d/forest_giants/runtime/handoff.md`. QA rejection: `docs/assets/012_africa/models_3d/forest_giants/validation/meshy7_generation_4_tpose_rejection.md`.

No simplification or unapproved fallback was used. The package is incomplete and blocked; no in-game completion is claimed.
