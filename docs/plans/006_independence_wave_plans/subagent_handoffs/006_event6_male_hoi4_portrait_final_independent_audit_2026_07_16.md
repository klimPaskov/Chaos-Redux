# Event 006 male HOI4 portrait final independent audit

Date: 2026-07-16

Auditor: independent final portrait-package auditor (`portrait_package_final_audit`), separate from the producing workers.

## Verdict

**PASS.** The audited package contains twenty distinct regenerated male large portraits and ten matching commander-small dossiers. All thirty regenerated runtime textures pass the requested dimensions, complete legacy BGRA DDS-header contract, exact byte length, and PNG-to-DDS pixel comparison. The two protected historical portraits remain byte-identical to both their approved hashes and `HEAD`. No Event 006 advisor icon file or advisor sprite reference is live.

The two non-blocking caveats are recorded below: ACX/AEX are deliberately unregistered readiness-pool art, and five second-tranche small metadata records retain removed OS-temporary `reference_dir` strings even though their actual review sheets, canonical comparisons, hashes, and pinned v4.3 inputs remain independently verifiable.

## Scope audited

- Package: `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/`
- Runtime: `gfx/leaders/006_independence_wave/`
- Runtime registrations and consumers under `interface/`, `common/characters/`, and `common/scripted_effects/`
- Canonical skill references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/`
- Vanilla restore registrations and characters under the installed Hearts of Iron IV tree

## Independent inventory result

| Surface | Independently counted | Result |
|---|---:|---|
| Prompt records | 20 | PASS |
| Raw ImageGen masters | 20 | PASS |
| Processed large PNGs | 20 | PASS |
| Processed commander-small PNGs | 10 | PASS |
| Saved runtime large DDS decodes | 20 | PASS |
| Saved runtime small DDS decodes | 10 | PASS |
| Processing metadata records | 30: 20 `leader`, 10 `advisor` dossier-render mode | PASS |
| Individual review sheets | 30 | PASS |
| Regenerated runtime large DDS | 20 | PASS |
| Regenerated runtime commander-small DDS | 10 | PASS |
| Protected runtime historical DDS | 2 | PASS |
| Total DDS files in the Event 006 leader folder | 32 | PASS |

The prompt, raw-master, processed-large, and regenerated runtime-large stem sets match exactly. The ten `_small` stems map one-to-one to the ten commander masters.

## Raw masters and prompts

- All twenty raw files have distinct SHA-256 values.
- Hashing decoded RGBA pixels independently also produced twenty distinct values, so uniqueness is not an artifact of PNG metadata or encoding.
- A 256-bit difference-hash comparison found no near duplicate; the closest pair was `portrait_ACX_cornish_port_and_mines_committee` versus `portrait_SCO_independence_wave_civic_convention`, at 53 differing bits.
- Raw dimensions are `1080x1456`, `1080x1457`, or `1081x1455`; every output is subsequently normalized to its required runtime size.
- The twenty-entry `hashes/raw_master_sha256.sha256` ledger matches the files independently.
- Every prompt has the matching runtime stem and explicitly specifies a fictional male subject, a Hearts of Iron IV portrait, `156x210`, late-1930s/period treatment, and no text.
- Visual review confirms twenty different adult male subjects; the ten small files visibly preserve their matching commander's identity.

## Processing metadata and retained evidence

- All thirty JSON records identify processor version `4.3` and processor SHA-256 `c300a0acc6ca91beb98d5ae62fcb6c98ad61c39bb7c271491c761295ca11b411`.
- All thirty metadata `source`, `output`, and `review_sheet` paths resolve, and every recorded `source_sha256` matches its raw master.
- All ten commander-small records point to the matching new commander raw master and hash.
- All thirty processor statuses remain `candidate_requires_visual_approval`; this independent audit supplies the separate final visual verdict without altering the metadata.
- The five BAY/BRI/RHI/SCO/WLS small records contain absolute `reference_dir` and embedded overlay paths from the removed private OS-temporary v4.3 copy. This is a portability defect in those strings, not lost decisive evidence: their individual review sheets embed all six canonical comparisons; the current canonical reference directory is present; and the exact v4.3 inputs remain hash-verifiable from Git `HEAD` (`babaf57fb0a454229d3a018c09924095640ddbd4`). Independently recomputed `HEAD` hashes are:
  - processor: `c300a0acc6ca91beb98d5ae62fcb6c98ad61c39bb7c271491c761295ca11b411`;
  - overlay manifest: `be1ff82d3f460ca1e0572ff3cb23853fdd87d2a0a8444f20cdad6565cacd2d2f`;
  - frame source / overlay: `77857264f8f6e36c75c675969f73e5ba5ee936f38599c6d843e2e07c527c0740` / `950596dd88da0b58861af9e58cacdaa80b2e6308af9168dd98ad390ae42aea79`;
  - paper source / overlay: `5d5f5c76e0a290c848cc71e8ff8f102a87e47227d32c9902350bc7f1eb00d491` / `e5db0602b4b5d82ba148552bfa2a6c7b6e00c6a91137de2b3baec404535210a0`.

## DDS and pixel audit

All thirty-two runtime DDS files were parsed independently rather than accepted from the package report. Every file has:

- `DDS ` magic and a 128-byte total header;
- header size `124`;
- pixel-format block at byte 76 with size `32`, flags `65`, fourCC `0`, and bit count `32`;
- BGRA masks `00FF0000`, `0000FF00`, `000000FF`, and `FF000000`;
- `DDSCAPS_TEXTURE` (`0x1000`) at byte 108;
- zero mipmaps and exact `width * 4` pitch;
- exact total byte length `128 + width * height * 4`.

Results by class:

| Class | Count | Dimensions | Exact bytes each | Alpha extrema | Pixel result |
|---|---:|---:|---:|---:|---|
| Regenerated large | 20 | 156x210 | 131,168 | 255/255 | All equal to processed PNG and saved runtime decode |
| Protected historical large | 2 | 156x210 | 131,168 | 255/255 | Protected by exact byte hash |
| Commander-small | 10 | 65x67 | 17,548 | 0/255 | All equal to processed PNG and saved runtime decode |

The fifteen retained second-tranche DDS files are also byte-identical to their installed runtime copies.

## Protected historical files

Independent current-file, approved-value, and Git-`HEAD` comparisons agree exactly:

| Protected file | Current SHA-256 | `HEAD` SHA-256 | Result |
|---|---|---|---|
| `portrait_BAY_rupprecht_of_bavaria.dds` | `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b` | same | PASS |
| `portrait_RHI_josef_friedrich_matthes.dds` | `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2` | same | PASS |

Neither protected file is modified in the worktree.

## Runtime registration and consumer coverage

- AFX, AGX, AJX, RHI, BAY, SCO, and WLS large/small sprites are registered in `interface/006_independence_wave_region_01_portraits.gfx` and consumed by their Event 006 character or scripted-effect packages.
- BRI large/small sprites are registered in `interface/006_independence_wave_brittany_portraits.gfx` and consumed by `common/scripted_effects/006_independence_wave_brittany_package_effects.txt`.
- The protected Event 006 sprites are registered in `interface/006_independence_wave.gfx` as `GFX_portrait_RHI_josef_friedrich_matthes` and `GFX_portrait_independence_wave_BAY_rupprecht_of_bavaria`, then consumed by the route-owned portrait effects.
- The restore helper's `GFX_portrait_RHI_josef_matthes` and `GFX_portrait_BAY_rupprecht_of_bavaria` names are valid vanilla aliases, not unresolved Event 006 sprites. Authoritative evidence is in vanilla `interface/_leader_portraits.gfx` at lines 8758 and 8786; vanilla `common/characters/RHI.txt` and `common/characters/BAY.txt` consume those aliases at line 10. The Event 006 helper intentionally restores the vanilla portraits through those engine-loaded definitions.

### Readiness-pool caveat

The six ACX/AEX files—two large and one small for each tag—have no Event 006 sprite registration or live character consumer. This is consistent with the authoritative `docs/assets/006_independence_wave/manifest.md`, which explicitly classifies ACX and AEX portrait art as readiness-pool assets rather than package-readiness claims. Their regeneration, format, pixels, metadata, and visual quality pass; they must be registered when those country packages are admitted. They are not counted as currently live consumer coverage.

## Advisor-icon boundary

- Runtime Event 006 custom advisor-icon files: **0**.
- Advisor sprite definitions or texture references for Event 006: **0**.
- Advisor-named image files inside this regeneration package: **0**.

The ten metadata records using processor mode `advisor` are commander `army.small` dossier cards at 65x67. Their actual character/effect consumers use the army-small slot; the mode name identifies the shared dossier renderer and does not make them advisor icons.

## Independent visual review

I inspected the actual-runtime decode sheets rather than relying on the written acceptance report:

- `contact_sheets/all_runtime_large_156x210_contact_sheet.png`;
- `contact_sheets/all_runtime_large_canonical_comparison.png`;
- `contact_sheets/all_runtime_commander_small_65x67_contact_sheet.png`;
- representative individual large and small review sheets from both production tranches.

I also inspected the canonical skill-local leader, commander, and advisor contact sheets directly. All twenty regenerated large portraits visibly present as male, remain distinguishable from one another, use readable head-and-shoulders framing, restrained period clothing/backgrounds, controlled value ranges, and a matte painted vanilla-HOI4 treatment. The ten small dossiers remain recognizable at native size, preserve transparent corners and the expected dark-frame/pale-paper silhouette, and compare acceptably with the canonical Paulus, von Kluge, Rommel, and generic dossier family.

## Simplifications, omissions, and blockers

- Simplifications or omitted requested portrait files: none.
- Blocking asset defects: none.
- Non-blocking caveats: the deliberate ACX/AEX readiness-pool registration state and five stale OS-temporary `reference_dir` strings described above.

## Changed file

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_male_hoi4_portrait_final_independent_audit_2026_07_16.md` only.

## Parent provenance resolution

After this audit, the parent retained the exact seventeen-file v4.3 processor/input bundle as Git blob bytes from commit `6729ad0cd74e0ed294a0b603a0eb677a0533099c`, rebased all thirty processor paths and all ten commander-small embedded input paths to that permanent package-local bundle, and reran path and hash checks with zero failures. This resolves the stale OS-temporary-path caveat without changing any image, DDS, processor pin, or runtime consumer. The resolution evidence is `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/validation/frozen_v4_3_input_resolution.md`.
