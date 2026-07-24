# Event 006 HAW David Kalakaua Kawananakoa source-clearance retry 02

Date: 2026-07-24  
Owner: sourced visual asset subagent  
Parent scope: IW-173 Hawaii  
Disposition: **BLOCKED / NO-PASS; no runtime promotion**

## Files added

- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/hawaii_kawananakoa_source_retry_02/source_masters/HAW_david_kalakaua_kawananakoa_1925_original.jpg`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/hawaii_kawananakoa_source_retry_02/source_crops/HAW_david_kalakaua_kawananakoa_1925_head_shoulders.png`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/hawaii_kawananakoa_source_retry_02/metadata/HAW_david_kalakaua_kawananakoa_1925_head_shoulders.json`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/hawaii_kawananakoa_source_retry_02/research/source_clearance.md`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/hawaii_kawananakoa_source_retry_02/research/rejected_adult_candidates_contact_sheet.jpg`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/hawaii_kawananakoa_source_retry_02/manifest.md`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/hawaii_kawananakoa_source_retry_02/gfx_handoff.md`

## Source and crop proof

The copied master is unchanged and byte-identical to the existing Commons-derived source: 1109×1700, SHA-256 `E23304AFA45091FA6B7FF0179CAA688BCD7EE0027306B22E853A14C1344DA909`.

The required crop utility `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` version `1.0` produced crop `(245,170,945,1112)` at 700×942 with file SHA-256 `2B4B96D2E1D3A2398E257A8104CCE4E082D169EFE0749EDB2603D68B4859149A`. Its JSON records decoded-pixel equality `true`, 659400 pixels, and matching master/output RGBA hashes `43d43df2f11f482ae845e343dd453bf5789d3b07c9dc4898cc6dad3765deab3b`.

## Research result

The Commons page <https://commons.wikimedia.org/wiki/File:David_Kalakaua_Kawananakoa.jpg> is the correct 1904–1953 target and has the only defensible archival publication/public-domain basis found, but its forehead and central facial planes are clipped nearly white. The prior source-locked repaint reconstructed missing face geometry and failed exact likeness review.

The sharper 1937 Alamy image is rights-managed and watermarked. The stronger Find a Grave adult images are user uploads with no confirmed photographer, publication, archive, or reuse licence. The public-domain 1908 Commons image shows the target only as a child in a group. Digital Archives results `ark:70111/1BD0`, `ark:70111/1BCX`, and `ark:70111/1CP4` identify the father David Kawānanakoa (1868–1908), not the target. The research-only contact sheet is `research/rejected_adult_candidates_contact_sheet.jpg` (SHA-256 `C3363D21097DC9373A6BB319BE9316E531CA4F36E4EFB71CF0F447AB9EF21489`) and must not ship. No candidate passes both identity and ownership clearance.

## Consumer and ownership evidence

Vanilla HAW history uses the exact leader name and picture token at `history/countries/HAW - Hawaii.txt:60-62`; vanilla maps the token to the generic Asia land leader sprite at `interface/_leader_portraits.gfx:7961-7963`. The Event 006 preservation trigger at `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:37-44` keeps the vanilla ruling leader. Current-mod scans found no HAW character or portrait override, and approved-workshop scans found no exact David Kalakaua Kawananakoa owner. No character/history/GFX/runtime file was edited.

## Required parent action

Keep the vanilla generic HAW portrait active and leave this package blocked. Do not run ImageGen, create a processed portrait or DDS, add `.gfx`, edit the vanilla history or character roster, or create advisor, `_small`, commander, operative, or dossier consumers. Reopen only when an adult target photograph with a defensible rights chain and sufficient un-clipped facial geometry is available.

## Validation performed

- Recomputed master and crop file hashes.
- Reopened the crop metadata and confirmed the normalized command, crop box, dimensions, and decoded-pixel equality proof.
- Inspected the source crop, prior trial evidence, rejected adult candidates, wrong-person archive candidates, and style-only canonical male leader references.
- Recorded exact URLs, public-domain/publication basis, identity distinction, candidate rejection reasons, vanilla consumer, current-mod ownership scan, and approved-workshop ownership scan.

## Simplifications, omissions, and blockers

- No production-safe source was found, so the requested portrait remains blocked.
- No ImageGen repaint, processed preview, DDS, or runtime handoff was created because the source/likeness gate failed and the parent explicitly prohibited promotion. The contact sheet is research-only and contains rejected, rights-unclear candidates.
- The exact 1925 source crop is retained as evidence only and must not be wired.
