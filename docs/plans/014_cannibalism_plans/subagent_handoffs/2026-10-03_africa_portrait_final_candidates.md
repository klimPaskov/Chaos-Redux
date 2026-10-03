# Event 014 Africa Portrait Production and Installation Handoff

Date: 2026-10-03.

Owner: `chaosx_portrait_creator`.

Disposition: the parent-approved eight Africa portraits are installed and receipted; the full 56-portrait matrix and cross-region uniqueness review remain open.

## Scope and authority

This handoff covers only the eight Africa regional portrait candidates for CBA-CBH in the shared checkout at `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`.

The user authorized the complete 56 distinct fictional bald feral human male HOI4-style portrait requirement and directed one native ImageGen call per unique asset, with a narrow same-brief retry only after a native failure.

The parent reviewed the eight Africa source masters and decoded DDS sheets, approved the assigned prop, gesture, crop, face, and background for every Africa slot, and recorded the exact accepted DDS hashes in `docs/plans/014_cannibalism_plans/evidence/2026-10-03_africa_portrait_parent_review.json`.

The accepted part 10 and part 12 portrait criteria, the fictional CBA-CBH source-polity classification, and the parent-accepted native fictional route are documented in the manifest under `docs/assets/014_cannibalism/portrait_finals_2026-10-03/africa/`.

The Europe parent-approved eight were used only as style/framing coherence references after inspection of the installed vanilla Africa leader portraits; Asia was reviewed read-only only for cross-region uniqueness.

No reference or backdrop image was used as a source or input to ImageGen, and the canonical Hannibal art was not opened as generation input or modified.

## Files produced

The Africa asset package contains eight untouched native ImageGen source PNGs, eight exact prompts plus the CBE retry prompt, eight full-frame lossless source crops and per-slot crop evidence, eight processed 156x210 PNGs, eight isolated BGRA32 DDS candidates, source/native/4x contacts, DDS-decoded native/4x contacts, processing and preservation audits, reproducible local audit scripts, and `manifest.md`.

The producer source and framing review is `docs/assets/014_cannibalism/portrait_finals_2026-10-03/africa/review/producer_source_review.md`.

The ImageGen prompt, returned-source path, source-copy identity, and CBE safety/retry log is `docs/assets/014_cannibalism/portrait_finals_2026-10-03/africa/route_log/imagegen_call_log.json`.

The per-file source/crop/processed PNG sizes and hashes are in `route_log/processing_audit.json`; DDS sizes, hashes, BGRA32 single-level headers, and exact pixel round trips are in `route_log/dds_roundtrip_audit.json`.

The read-only runtime, existing GFX registration, and protected Hannibal hash receipt is `route_log/runtime_preservation_audit.json`.

The canonical parent-approved Africa installation receipt is `docs/assets/014_cannibalism/portrait_finals_2026-10-03/africa/evidence/runtime_install_receipt.json`; it contains the eight pre-install backups, approved-candidate hashes, and the later disjoint Middle East install attribution.

## Candidate and runtime crosswalk

| Slot | Candidate DDS | Existing sprite in `interface/014_cannibalism.gfx` | Existing runtime DDS path | Existing GFX line |
|---|---|---|---|---:|
| CBA | `candidate_dds/leader_CBA_warlord_africa.dds` | `GFX_portrait_CBA_warlord_africa` | `gfx/leaders/014_cannibalism/leader_CBA_warlord_africa.dds` | 171 |
| CBB | `candidate_dds/leader_CBB_warlord_africa.dds` | `GFX_portrait_CBB_warlord_africa` | `gfx/leaders/014_cannibalism/leader_CBB_warlord_africa.dds` | 179 |
| CBC | `candidate_dds/leader_CBC_warlord_africa.dds` | `GFX_portrait_CBC_warlord_africa` | `gfx/leaders/014_cannibalism/leader_CBC_warlord_africa.dds` | 187 |
| CBD | `candidate_dds/leader_CBD_warlord_africa.dds` | `GFX_portrait_CBD_warlord_africa` | `gfx/leaders/014_cannibalism/leader_CBD_warlord_africa.dds` | 195 |
| CBE | `candidate_dds/leader_CBE_warlord_africa.dds` | `GFX_portrait_CBE_warlord_africa` | `gfx/leaders/014_cannibalism/leader_CBE_warlord_africa.dds` | 203 |
| CBF | `candidate_dds/leader_CBF_warlord_africa.dds` | `GFX_portrait_CBF_warlord_africa` | `gfx/leaders/014_cannibalism/leader_CBF_warlord_africa.dds` | 211 |
| CBG | `candidate_dds/leader_CBG_warlord_africa.dds` | `GFX_portrait_CBG_warlord_africa` | `gfx/leaders/014_cannibalism/leader_CBG_warlord_africa.dds` | 219 |
| CBH | `candidate_dds/leader_CBH_warlord_africa.dds` | `GFX_portrait_CBH_warlord_africa` | `gfx/leaders/014_cannibalism/leader_CBH_warlord_africa.dds` | 227 |

The installed files preserve the exact eight existing runtime basenames and GFX sprite names, and their SHA-256 values equal the parent-approved candidates.

No `.gfx` entry or character portrait reference was edited; the existing registrations already consume the eight approved runtime paths.

## Verification and replacement state

All source masters are opaque RGB at 1080-1082x1454-1456; every processed PNG and candidate DDS is 156x210.

All eight isolated DDS candidates are 131168-byte uncompressed BGRA32 files with one image level, and every decoded DDS pixel buffer equals its processed PNG exactly.

All eight processed PNG pixel hashes and all eight DDS-decoded pixel hashes are unique.

The required converter used its FFmpeg BGRA fallback because `texconv` was not available on PATH; no alternate generation or conversion tool was used.

The install script snapshotted all 60 current Event 014 leader DDS files and the current portrait GFX/character definition before replacement, then backed up only the eight Africa originals.

The eight Africa backups match the parent-approved pre-install hashes, the installed Africa DDS hashes match the approved candidates exactly, and the other 52 DDS files and both definitions match the current pre-install snapshot.

The two static Hannibal portraits and both canonical animated Hannibal sheets remain byte-identical to the current pre-install snapshot.

The eight approved candidates remain archived under `docs/assets/014_cannibalism/portrait_finals_2026-10-03/africa/candidate_dds/`; the exact backups, current before/after snapshots, and installation receipt are in the same Africa package.

The pre-install worktree snapshot showed no other dirty paths in the portrait DDS/GFX/character scope; the immediate Africa post-install snapshot showed exactly the eight authorized Africa runtime DDS paths changed.

The Middle East owner later installed eight disjoint DDS paths; `docs/assets/014_cannibalism/portrait_finals_2026-10-03/middle_east/evidence/runtime_install_receipt.json` matches all eight current hashes to its parent-approved candidates, and `route_log/runtime_install_final_audit.json` attributes this later change without resetting those files.

That final audit snapshots all 60 current Event 014 DDS files, confirms the remaining 44 paths and GFX/character definitions did not drift, and confirms Africa still matches its approved candidates.

No commit was created by this worker; the parent owns the required shared-tree commit.

## Parent review and remaining queue

The producer and parent reviewed all eight Africa faces and compositions at source and 156x210 sizes, with every assigned prop/action visible in the generated candidate set.

Parent source, framing, and DDS approval is complete for this bounded eight-portrait set; evidence is in `review/producer_source_review.md` and the parent receipt.

The parent reviewed the cross-region near-collision observations in the producer review and accepted the distinct Africa actions, gestures, and backdrops within this bounded set; the final cross-56 uniqueness review remains open.

The parent approved CBG's pay-token gesture at native size.

CBE's first output was rejected with HTTP 400, `moderation_blocked`, output-stage `violence`, request ID `d202df39-8ff6-4240-9853-1dcefec4472f`; retry 01 narrowed only graphic wording, preserved the exact four-cartridge-case counting action, and succeeded.

Europe, Asia, Africa, and the Middle East each have eight installed regional DDS portraits; the other 24 accepted slots across North America, South America, and Oceania remain with active region owners and were not read or modified by this worker.

Full 56-portrait uniqueness across the active regions and full Event 014 completion remain open.

## Constraints and omitted checks

No RunPod, Meshy, Blender, generation CLI, or API fallback was opened or used.

No grounded-source research was performed because all eight subjects are fictional and use the accepted native fictional route.

No other active-region workspaces were opened beyond the accepted Europe and Asia review sheets used for coherence and the bounded uniqueness comparison.

No HOI4 process or live-game validation was run; the user retains live-game validation.

No source identity, GFX, character, gameplay, localisation, event, focus, decision, country, spreadsheet, or unrelated UI file was changed; only the eight authorized Africa runtime DDS paths were installed.
