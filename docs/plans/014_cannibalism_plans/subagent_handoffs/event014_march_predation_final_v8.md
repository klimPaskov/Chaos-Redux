# Event 014 March Predation Column 3D handoff — final v8

## Outcome

The v8 reference refinement is rejected and no paid Meshy work was performed against it.

The technically clean transparent input at SHA-256 `3A0F19C7329FD433C538F6D1BCE3A97C5CDE72EBEF52B3D5270AA151E41C740A` retained too much of the conventional and culturally anchored fantasy-archer identity. Parent review specifically rejected the weak skull/bone headgear and trophy silhouette and the culturally legible markings and jewelry.

Internet source research was reopened under the stricter requirement for an already monstrous or cannibal fictional human archer with bow/quiver, paint, and strong bone kit. The first shortlist failed that standard: the parent explicitly rejected the goblin candidate as the wrong species and identity. Continued research found Bestiarum Games' *Fleshmad Hunters | Man Eaters*, an official culturally neutral grimdark tabletop line that explicitly describes human cannibal archers using great bows to mark the best cuts of flesh. Hunter 1 clears the human, cannibal, bow/quiver, skull/bone gear, and cultural-neutrality gates, but its official source is a gray resin presentation with red rim lighting rather than a fully painted color illustration. ImageGen and Meshy remain paused pending parent approval of that source and of faithful material colorization within the cleanup-only boundary.

## Source and refinement lineage

- Rejected source: `refs/source/recovery_v7/candidates/conan_fashion_contest_painted_archer.png`
- Rejected source SHA-256: `8AEB254BA8D7BF61F35439D037E84EC4FB205610C10FE458ABADE9D7E76BAED6`
- Source mode: `reference_only_user_authorized`; no explicit NoAI or no-derivatives restriction was found in the archived v7 source evidence.
- Native ImageGen moderation request ID: `b49a8842-024f-482d-bbd9-bae5ecea4561`
- Parent-approved moderation recovery: a minimal distressed hide/leather chest wrap covering the nipples, without armor or modern clothing.
- Native transparency failed twice by returning a baked checkerboard. The retained fallback used rembg 2.0.61 followed by boundary-only neutral-white cleanup.
- Rejected refined path: `refs/original/meshy_input.png`
- Rejected refined SHA-256: `3A0F19C7329FD433C538F6D1BCE3A97C5CDE72EBEF52B3D5270AA151E41C740A`
- Comparison image: `refs/derived/source_to_refinement_comparison_v8.png`
- Comparison SHA-256: `B5343605993175091236EDCA8C4BF76FBB07C0720FA72F60D2D5333CC658BCF3`
- Parent approval: rejected on 2026-08-24; exact reason and provider-stop instruction are recorded in `history.jsonl` and `refs/original/input_manifest.json`.

## Replacement source research

The full candidate record, URLs, terms checks, hashes, and fit gaps are in `refs/source/recovery_v8/source_shortlist.json`.

1. `bestiarum_fleshmad_hunter_1.jpg`, SHA-256 `9E0028B6458CFD4876D347A44EEBD0FB4B533DDF71F10ABA6B73E42D3F0F668F`, is the recommended source. Bestiarum Games explicitly identifies the Fleshmad Hunters as Man Eater cannibals who use great bows to mark the best cuts of flesh. Hunter 1 is human, full-body, feral, and culturally neutral, with a bone-spike crown, skull breast trophy, bone and feather kit, bone greatbow, barbed shaft, and back quiver. The unresolved gap is its gray resin presentation rather than a fully painted color source.
2. `bestiarum_fleshmad_hunter_4.jpg`, SHA-256 `779D77B631E8B0F51EAF4B4911DE193285EF0F0ACE5BA3093C4A0894976C367D`, is the skull-mask alternate. It has a full skull mask, drawn bone greatbow, quiver, bone necklace, and explicit Man Eater lineage, but the firing pose self-occludes more of the body and it has no unambiguous body-paint color.
3. `goblin_archer_bone_armor.jpg`, SHA-256 `505E9B7A2A8A0834A1422ACDCA96420194416D7A105B7C07187B133C6F8643DA`, was rejected by the parent because a goblin is the wrong species and still misses the explicit cannibal and skull-headgear identity gate.
4. `behance_cannibal_tribe_archer.jpg`, SHA-256 `002DCCD27B16AD5F20E8A533219CD121E415B71F3D979675587BEBC9A4FA5A7A`, is *Cannibal tribe* by Vladislav Stain. It has explicit cannibal identity, paint, bow/arrows, and a skull trophy, but is rejected because its human styling remains too culturally anchored.
5. `orcquest_archer_secondary.jpg`, SHA-256 `57F64ABFA75122E0327B7F2CDFBCD8AE0B4A5B2A6B590C7BFAD97225E096CC01`, is OrcQuest promotional art attributed to Daniel Zrom / Maze Games. It is fictional and carries paint, bow/quiver, and skull trophies, but reads as a conventional fantasy hero, is not explicitly cannibal, lacks skull headgear, and the archived byte is only a secondary copy.

The Bestiarum product and terms pages were archived under `refs/source/recovery_v8/pages/`. No explicit NoAI or no-derivatives restriction was found on the inspected pages. The source remains all rights reserved and is eligible only under the user's reference-only authorization; no purchased STL or source pixels may ship.

Wendigo-derived designs were excluded despite superficially strong monster and skull traits because that route would re-anchor the unit in a living Indigenous cultural tradition.

## Dependency and route verification

The repository-owned verification gate passed before provider work:

- Official Meshy MCP package: `@meshy-ai/meshy-mcp-server` 0.4.0
- Meshy SDK: 1.29.0
- Required generation identifier: exact `meshy-7`
- Repository Blender HOI4 adapter: `chaosx_blender_hoi4` 1.10.0
- Blender: 5.1.2, build `ec6e62d40fa9`
- `io_pdx_mesh`: 0.91.0, checksum beginning `A683DF`
- Blender adapter socket: `127.0.0.1:9876` listening after the clean verification pass
- `.tools/3d_pipeline/verify_environment.py --probe-meshy`: final pass returned no findings

No route substitution or version downgrade was used.

## Paid operations and costs

- ImageGen calls: one moderation-blocked edit, one successful moderation-recovery edit, and one transparency/framing repair.
- Meshy paid calls after the v8 rejection: 0
- Meshy credits estimated after the v8 rejection: 0
- Meshy credits consumed after the v8 rejection: 0
- Provider task IDs created for this rejected v8 input: none

## Files created or changed

- `refs/original/meshy_input.png` — rejected provider input retained as non-shipping evidence
- `refs/original/input_manifest.json` — updated with parent rejection and provider-stop state
- `refs/source/provenance_v8.json`
- `refs/source/recovery_v8/source_shortlist.json`
- `refs/source/recovery_v8/source_shortlist.md`
- `refs/source/recovery_v8/candidates/goblin_archer_bone_armor.jpg`
- `refs/source/recovery_v8/candidates/behance_cannibal_tribe_archer.jpg`
- `refs/source/recovery_v8/candidates/orcquest_archer_secondary.jpg`
- `refs/source/recovery_v8/candidates/bestiarum_fleshmad_hunter_1.jpg`
- `refs/source/recovery_v8/candidates/bestiarum_fleshmad_hunter_2.jpg`
- `refs/source/recovery_v8/candidates/bestiarum_fleshmad_hunter_3.jpg`
- `refs/source/recovery_v8/candidates/bestiarum_fleshmad_hunter_4.jpg`
- `refs/source/recovery_v8/pages/bestiarum_fleshmad_hunters.html`
- `refs/source/recovery_v8/pages/bestiarum_terms.html`
- `refs/briefs/imagegen_prompt_v8.md`
- `refs/derived/source_to_refinement_comparison_v8.md`
- `refs/derived/source_to_refinement_comparison_v8.png`
- `refs/derived/meshy_input_superseded_pre_v8.png`
- `refs/derived/imagegen_checker_failed_native_alpha_v8.png`
- `refs/derived/rembg_no_matting_candidate_v8.png`
- `refs/derived/rembg_postprocessed_candidate_v8.png`
- `evidence/process_checker_alpha_v8.py`
- `history.jsonl`
- this handoff

## Meaningful validation

- The rejected reference was confirmed as 1122×1402 RGBA with genuine binary alpha, no partial-alpha pixels, and visible bounds `[79, 113, 1075, 1269]`.
- All three replacement candidates were visually inspected at original resolution rather than assessed from search text alone.
- Candidate source pages and direct image URLs were recorded before downloading.
- The rejected input manifest, source shortlist JSON, and appended history records parse successfully.

## Blockers and remaining parent work

- `needs_parent_source_and_colorization_approval`: Bestiarum Fleshmad Hunter 1 clears the human cannibal, bow/quiver, skull/bone gear, horror, and cultural-neutrality gates. The parent must decide whether the gray official render may receive faithful material colorization, isolation, base removal, native transparency, and only the previously approved small sheathed bone close weapon.
- ImageGen may not alter the Fleshmad identity, anatomy, pose, bone crown, skull trophy, bow, quiver, silhouette, or add new cultural motifs.
- Meshy generation, geometry review, rigging, all eight real Meshy actions, Blender scale calibration against `western_european_infantry.mesh`, PDX texture derivation, `.mesh`/`.anim` export and reimport, previews, sourced 44100 Hz sound package, and final runtime/GFX/sound handoff are not started for v8.
- Existing counter art remains consumer-only and was not modified.
- Parent-owned runtime wiring and live in-game validation remain untouched.

## Simplifications, omissions, and blockers

No unapproved simplification was used. The package is incomplete because source/colorization approval is unresolved, and downstream paid/model work is intentionally blocked rather than filled with a weaker substitute.
