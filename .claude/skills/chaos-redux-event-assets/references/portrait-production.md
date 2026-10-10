# Portrait production reference

`chaosx_portrait_creator` owns every character portrait from brief to installed runtime asset. Read this reference for every grounded or fictional character portrait, portrait icon, source placeholder, or user-supplied final. It contains the portrait production sequence, source states, family requirements, and independent review rules. Follow the main skill for shared generation, processing, and asset evidence.

## Subject and source modes

### Portrait subject ownership gate

Before sourcing or wiring a real-person token, search installed vanilla and the project for exact/variant names, transliterations, titles, and name order across `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and `localisation/`. A person already defined, recruited, or portrait-owned by a live roster cannot be cloned. Reuse requires an explicit guarded transfer that invalidates origin ownership before target ownership and prevents simultaneous ownership. Otherwise fail closed. Incidental prose, ship names, streets, and equipment are not ownership. Record search terms, roots/ids, matches or no-match evidence, disposition, and any transfer guard in the manifest/handoff. This gate never authorizes a generated grounded person.

### Portrait source-mode gate

Classify every country-leader, commander, operative, named officeholder, or institutional portrait before routing. A grounded identity (`grounded_source_only`) is any real, partly real, restored, separatist, regional, indigenous, dynastic, or otherwise plausibly historical polity/community/institution. It requires `chaosx_portrait_creator` and attributed real-person or authentic institutional source material. If no defensible source exists, mark `blocked` and never invent a grounded face. A generated one-person portrait is allowed only for a truly fictional high-chaos country or impossible/supernatural entity, and must have an extraordinary internally coherent invented motif rather than a generic face, modern prop, meme, gore, mockery, stereotype, or caricature. Record classification, source mode, evidence, and blocked decisions. Missing or contradictory classification fails closed.

### Grounded source mode states

Select the mode in the brief or manifest and record it in the manifest entry.

| Mode | Meaning | Exit condition |
| --- | --- | --- |
| `source_placeholder` | Accepted unchanged attributed source, explicit head-and-shoulders crop, deterministic `156x210` resize, DDS wiring, and preserved identity. | Remains explicitly pending HOI4-style replacement until the user supplies it. |
| `replacement_pending` | An explicit styled-final request is still outstanding. | Allowed only while that request is open. |
| `styled_final` | Independent validation and installation of the user-supplied provider output at the same runtime path. | Requires the locked workflow revision, provider/job evidence, and independent identity/framing/provenance review. |
| `not_needed` | The requirement set carries no portrait row. | No portrait is produced. |
| `blocked` | No defensible grounded source or required evidence exists. | Report the blocker instead of substituting a face. |

No HOI4 repaint is required for `source_placeholder` preparation. A queued job or preview is never `styled_final`, and never open, operate, configure, queue, or monitor RunPod. The user alone runs the provider for grounded HOI4-style finals and supplies the result.

### Fictional portraits

Fictional or impossible portraits use image generation (see [Image-generation route](../SKILL.md#image-generation-route)) through `chaosx_portrait_creator`, never the grounded replacement branch. One-person leaders require `fictional_high_chaos`, full `156x210` HOI4 framing, a memorable invented motif, matching role/gender/name metadata, and no text, watermark, modern UI, meme, gore, stereotype, or caricature. Institutional briefs use an institutional name and may be people-free. A staged group requires explicit authorization and matching constraints. Grounded institutions still require authentic sourced material, and a named person uses one-person rules.

## Production

### Production sequence

1. Inspect the matching installed-vanilla portrait references and lock the runtime basename, canvas, role, and consumers before requesting or producing art.
2. Classify the subject. Grounded people and institutions require attributed Internet source research. Fictional or impossible subjects use image generation.
3. Name the mode in the brief or manifest for a grounded portrait, then follow [Grounded source mode states](#grounded-source-mode-states).
4. For a fictional or impossible portrait, invoke image generation yourself (see [Image-generation route](../SKILL.md#image-generation-route)) and follow [Generate and refine source art](../SKILL.md#generate-and-refine-source-art) for narrow edits, reference roles, accepted-candidate lineage, and full-resolution/native-size review against the brief and vanilla references.
5. Process the approved portrait, convert it to the required PNG/DDS variants, preserve stable runtime identifiers, update portrait-specific `.gfx` and existing character portrait references, and write the manifest and handoff.

Never generate or substitute the identity of a real or grounded person. If no defensible grounded source exists, mark the portrait blocked. Do not edit unrelated gameplay, localisation, or UI.

### Durable portrait source archive

`chaosx_portrait_creator` owns one durable source package for every grounded portrait and archives it without changing runtime identity. Select the mode in the brief or manifest: `source_placeholder` keeps the unchanged source/crop, deterministic `156x210` PNG, DDS, and wiring. `styled_final` is an optional provider branch that starts only after the user explicitly requests it and supplies the result. Never silently repaint, replace, or overwrite provenance.

Store each package together under `docs/assets/portraits/<event_id>_<event_slug>/` (a subject subfolder is allowed), using the exact runtime basename:

```text
<subject>/
  <runtime_portrait_basename>_original.<original_suffix> # untouched original bytes
  <runtime_portrait_basename>_source_crop.png         # lossless crop, before resize/DDS
  <runtime_portrait_basename>_source_crop.json         # exact crop/equality evidence
  <runtime_portrait_basename>_156x210.png              # deterministic processed candidate
  <runtime_portrait_basename>.txt                     # co-located provenance contract
<runtime_portrait_path>/<runtime_portrait_basename>.dds
```

The original source, lossless crop, processed PNG, JSON, and `.txt` contract are mandatory and must never be split across folders. The contract records subject, source URL/attribution/license, crop coordinates, mode/state, reviewer/date, and separate identity/framing/provenance verdicts. Preserve original-format bytes and a lossless PNG copy when needed. The archive is evidence only: no `.gfx`, character, GUI, event, focus, idea, or decision may reference `docs/assets/portraits/`, and cleanup of temporary event workspaces must not delete it.

## Portrait families

### Country-leader, commander, operative, and named-officeholder portraits

`chaosx_portrait_creator` owns every portrait from source/brief through runtime handoff. Grounded portraits use an attributed unchanged source and the selected `source_placeholder` or explicitly requested `styled_final` mode. Fictional/impossible portraits use image generation. Automated checks never replace independent visual review. Never generate or reconstruct real-person identity: use an unchanged attributed archival photograph (male subject: archival male photograph), preferably public-domain or clearly licensed and period-compatible. Reject illustrations, statues, reenactors, actors, text descriptions, modern or era-incompatible images, and unverified crops; ffmpeg/ImageMagick cropping alone does not prove decoded-pixel equality. Female-presenting portraits require matching female metadata/name pools, male-presenting portraits matching male metadata/name pools, and councils/boards institutional names. A wired `source_placeholder` remains explicitly pending until the user supplies its HOI4-style replacement; selecting this mode does not complete the portrait.

Run the automatic source package tool from the mod root (or pass `--crop` for measured recovery):

```powershell
python -B .claude/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py `
	<archival_master.jpg> <subject_source_crop.png>
```

Automatic mode uses bundled YuNet to require exactly one face, computes a portrait-aspect head-and-shoulders crop, saves the untouched original, exact lossless crop, `156x210` RGB PNG, JSON equality/model/hash evidence, and a co-located provenance `.txt` contract under `docs/assets/portraits/<event_id>_<event_slug>/` (subject subfolders are allowed). Missing model/OpenCV support, zero/multiple faces, unsafe geometry, or write collisions fail closed. Use `--model` or an explicit `--crop` recovery. Both routes write the complete package. Manual JSON is labelled `manual_crop_override` and reports no face box or YuNet detection. The JSON must retain source/crop/processed dimensions, hashes, exact crop coordinates, equality result, and normalized command (plus detector evidence only for automatic mode). Never accept an alternate crop without equivalent decoded-pixel equality evidence.

Convert and wire a grounded portrait only after an independent audit PASS; a pending or failed identity gate is `needs_user_review` or `blocked`, never wired. Use the processed PNG as `source_placeholder` when selected. `replacement_pending` is allowed only after an explicit styled-final request remains outstanding. When supplied, the user-provided output goes to `chaosx_portrait_creator` for independent validation, DDS conversion, and replacement at the same runtime path. Never operate RunPod.

Before DDS conversion, keep the untouched original, lossless crop, processed PNG, JSON, and provenance contract together under the exact runtime basename. The archive never replaces source evidence and never becomes a runtime reference.

Choose the canonical reference family by role before starting:

- country leader: `portraits/leaders/`
- army or navy commander: `portraits/commanders/`
- operative: `portraits/operatives/`
- named officeholder: the canonical family owned by its consuming leader, commander, operative, advisor, or high-command surface

Use role-specific references as style controls only, never as a face source. Compare unchanged master, exact crop, deterministic candidate, any supplied provider output, runtime candidate, and references at native size and ≥4x nearest-neighbour.

Preserve facial geometry, asymmetry, age, expression, hair, pose, and source-visible clothing. Reject genericization, beautification, symmetrization, face substitution, invented detail, unsupported insignia, weak likeness, or filtered photos. Record source URL/attribution/license, crop coordinates, role references, comparison sheet, reviewer/date, separate likeness/framing/provenance verdicts, mode/state, DDS path, sprite, and gender/name-pool metadata. Missing evidence blocks the portrait.

Country-leader, commander, operative, and named-officeholder candidates are deterministic `156x210` portraits. Commander references remain full `156x210` even when displayed smaller. Advisor/high-command cards use [Advisor and high-command portrait icons](#advisor-and-high-command-portrait-icons)'s separate native `65x67` workflow after the shared identity gate. Operatives use the full pipeline and cataloged owning sprite.

Every portrait follows [references/portrait-production.md](portrait-production.md): the five-step portrait sequence, the grounded source-placeholder or explicitly requested provider-backed styled-final branch with its `replacement_pending` state, the fictional/impossible image-generation branch, and the separate no-advisor-icons authorization boundary in [Advisor and high-command portrait icons](#advisor-and-high-command-portrait-icons).

### Advisor and high-command portrait icons

Advisor, theorist, military-high-command, and officer-corps portrait icons are a separate asset type. Inspect `assets/gfx_references/portraits/advisors/` before work. The final target is native `65x67`, with a recognisable HOI4-styled head-and-shoulders portrait, a dark irregular dossier frame where the approved reference family uses one, and transparent outer corners. Do not infer this family from a character or small-portrait consumer; it must be present in the accepted requirement set.

Apply the fail-closed [Portrait source-mode gate](#portrait-source-mode-gate) to advisor and high-command subjects. For a fictional subject in the allowed class, `chaosx_portrait_creator` uses image generation to create a distinct full-resolution portrait master. Never reuse a leader crop. For real people, complete the shared source and provenance gate before preparing the native card; [Country-leader, commander, operative, and named-officeholder portraits](#country-leader-commander-operative-and-named-officeholder-portraits) governs the portrait handoff and fallback. Institutional or collective briefs must state whether the result is people-free or includes a governing group, and never imply that invented faces are sourced historical individuals.

Keep a repo-contained provenance manifest for every native card. Record the source mode, source and candidate dimensions, exact crop or composition notes, generation or editing inputs, attribution or image-generation record, reviewer, date, and runtime path. Keep each source, processed PNG, review sheet, and metadata file in a distinct path; do not split out or bypass an individual source to weaken provenance.

Use `.claude/skills/chaos-redux-event-assets/tools/create_advisor_icon.py` for native `65x67` advisor-template composition. Use the canonical `portraits/advisors/advisor_template.png` as one exact, untouched top layer rather than reconstructing its frame, paper, or shadows from separate elements. Load the complete approved source canvas without pre-cropping or pre-warping it. Measure the opening center, rotated width and height, and angle from the actual template. Canonical cards must use that exact opening-fill plane, match the angle within `0.05` degrees, and use a `0 0` center offset.

Never clip the portrait to the exact visible opening. The canonical frame contains translucent antialiased inner-edge pixels, so exact-opening clipping can leave those pixels without underlying portrait coverage and expose an alpha seam. The visible opening is the audit region, not the portrait's final mask boundary.

Use one uniform aspect-preserving cover scale with no anisotropic resize or stretching. Extend the measured opening-fill plane before cover fitting with the tool's centralized `UNDER_FRAME_BLEED_PIXELS` value, currently `2` px, and `PORTRAIT_EDGE_GUARD_PIXELS`, currently `1` px. The tool adds `2 * (bleed + guard)` to each opening dimension. Do not duplicate these values in event-specific or per-person instructions. Build the safe bleed mask by expanding the opening mask with the centralized bleed value, and fail closed if any expanded pixel reaches a fully transparent exterior template pixel. Mask the portrait to this verified safe bleed mask, then composite the canonical template unchanged as the final top layer.

The covering scale is `max(under_frame_fill_width / source_width, under_frame_fill_height / source_height)`, and the source aspect ratio must remain unchanged. The only content-area clipping is the symmetric aspect-ratio excess recorded in `frame_clip_pixels`. Never substitute an exact-opening clip for the under-frame bleed. `source_pre_crop=false` means no pre-scale source crop, not that the portrait may stop at the visible opening.

Generate and retain a separate placement study for every person and inspect the face, head, and shoulders at native size and `4x` nearest-neighbour enlargement. The alignment overlay must show the measured opening in red, the opening-fill plane in green, and the uniformly scaled covering portrait in yellow. The yellow bounds may show the centralized bleed/guard extension and recorded symmetric cover excess, but the runtime portrait must remain inside the safe bleed mask. The selected transform must match the retained study candidate. Near-zero rotation is rejected by default. Use the explicit override only for an independently reviewed alternative template whose measured opening is actually unrotated.

Retain transform metadata for the source, template, measured opening geometry, selected placement, `opening_fill_size`, `under_frame_fill_size`, `covering_content_size`, `covering_content_center`, `frame_clip_pixels`, `under_frame_bleed_pixels`, and `resampling_edge_guard_pixels`, together with the explicit fit flags `source_pre_crop=false`, `frame_clip=true`, and `stretch=false`, plus the study, alignment overlay, processed PNG, and runtime DDS. Automated evidence must report `opening_alpha_gap_pixels=0`, `inner_edge_alpha_gap_pixels=0`, and `exterior_alpha_leak_pixels=0` in the alpha-coverage record. Review the native card and nearest-neighbour enlargement against contrasting solid backgrounds and checker backgrounds, and compare subject scale and frame integrity with the vanilla advisor/high-command references. Keep this workflow generic. Event-specific advisor names belong in the asset manifest or handoff, never in this reusable skill. The reusable command contract and review checklist are documented under `tools/README.md` in the advisor and high-command dossier section.

Do not shrink, pad, or directly wire a `156x210` leader, commander, or operative portrait. Compose the subject independently inside the native card, through the `create_advisor_icon.py` workflow above when the accepted design calls for the shared `advisor_template.png` surface or otherwise with a deterministic, task-specific/manual workflow, and retain the exact crop, face placement, dimensions, and review evidence. Do not draw replacement frame, paper, seal, bevel, patina, emblem, writing, or shadow artwork from primitive geometry.

Check the native `65x67` candidate against the canonical advisor and high-command references. Confirm composition, face readability, frame silhouette and palette, paper geometry and opacity where present, transparent corners, texture continuity, and the absence of holes or fringe. Record any deterministic dimension or alpha checks as evidence, but treat visual approval as a separate human gate.

When a character explicitly defines a `portraits = { army = { small = ... } }` sprite, the small slot remains a native `65x67` dossier portrait while `army.large` remains the full `156x210` commander portrait. Do not create a plain `50x67` resize or crop for the army-small slot, and do not replace or downsize the approved full commander texture. Keep the large and small sprite names stable, record both runtime paths and provenance, and validate both textures separately.

The independent visual review must compare the candidate with the canonical advisor and high-command references at native `65x67` and at `4x` nearest-neighbour size. Automated dimension and alpha checks produce evidence only, and the producer cannot self-approve the candidate. Convert only an independently approved PNG with `python -B .claude/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <approved.png> --output <runtime.dds> --width 65 --height 67`.

## Parallel portrait receipts and final selection

Parallel portrait workers report only their bounded tranche's files and independent acceptance evidence/status.
Global completion counts belong to the parent; cite them only from a current authoritative parent inventory with its revision and observation time, never copy an earlier parent count.
A missing or parse-failed receipt leaves another owner's status unknown, not unproduced or pending.
Preserve timestamped pre/post snapshots, observed changed paths, and known concurrent changes in disjoint regions without resetting shared work or attributing another owner's changes to yourself.
A later global count must not rewrite historical pre/post facts.

Record whether current runtime DDS bytes match the selected candidate separately from art acceptance; a matching hash alone never proves final approval.
Source versions and canonical PNG packages may retain unselected alternates, so final global review must follow the explicit selected source/version and processed PNG -> candidate DDS -> runtime paths mapping, never the first glob match or an unsuffixed filename.
When moving receipts to canonical paths, update pointers in every referring manifest, handoff, and referenced metadata record while preserving immutable original source/candidate lineage and the receipt's original path/revision.
