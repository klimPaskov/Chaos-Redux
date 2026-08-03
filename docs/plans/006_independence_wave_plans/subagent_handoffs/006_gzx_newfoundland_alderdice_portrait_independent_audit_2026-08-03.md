# IW-182 GZX Newfoundland Frederick C. Alderdice portrait — independent audit

Audit date: 2026-08-03  
Reviewer: independent asset reviewer (`/root/event6_gzx_portrait_independent_audit`)  
Scope: compare the unchanged source master, exact crop, raw identity-preserving repaint, and the canonical HOI4 country-leader reference family. This is a visual/provenance gate only. No DDS conversion, `.gfx` edit, gameplay edit, localisation edit, or producer overwrite was performed.

## Disposition

**HOLD — do not SAFE/PROMOTE, convert to DDS, or wire at this time.**

The face remains recognisably the sourced subject and the raw repaint is broadly compatible with the HOI4 leader-paint family. The package is not promotion-safe because the named source package does not contain defensible source attribution, rights evidence, source date, or a generation record, and it does not yet contain a deterministic `156x210` candidate or native-size review evidence. The exact crop proof establishes pixel integrity, not ownership or licensing.

## Inputs and integrity evidence

| Item | Path | Dimensions / mode | SHA-256 | Finding |
|---|---|---:|---|---|
| Unchanged source master | `docs/assets/006_independence_wave/gzx_newfoundland_portrait_source_research_2026_08_03/research/alderdice.png` | `510x702`, `P` | `9f1ed97e1a6fbc3ecc9130bb648860739b1701097add724f6c96a31fc2867bb3` | Preserved source; no EXIF/source attribution metadata embedded. |
| Exact source crop | `docs/assets/006_independence_wave/gzx_newfoundland_portrait_source_research_2026_08_03/source_crops/GZX_frederick_c_alderdice_head_shoulders.png` | `430x650`, `P` | `2de7e259356702311b68a1eca7354fb10401ee332c241f836174f6c2c4ebc45f` | **Exact crop verified** by the supplied JSON evidence; crop rectangle `[40, 40, 470, 690]`, decoded RGBA equality `true`. |
| Crop metadata | `docs/assets/006_independence_wave/gzx_newfoundland_portrait_source_research_2026_08_03/crop_metadata/GZX_frederick_c_alderdice_head_shoulders.json` | — | — | Pillow 11.1.0 / extraction tool v1.0 evidence retained. |
| Raw ImageGen repaint | `docs/assets/006_independence_wave/portraits_generated_png/portrait_GZX_frederick_c_alderdice.png` | `1079x1457`, `RGB` | `0a983dcbd2a49611a1f99dac5d19426821488f9083cbeef02de3cedfc2929bea` | Identity-preserving repaint candidate only; not a native runtime texture. |

The crop metadata's output file hash is `2de7e259356702311b68a1eca7354fb10401ee332c241f836174f6c2c4ebc45f`, while its decoded master-crop/output equality hash is `c5129319b2a39a5bf3246aa8b9f9711c81957e20657ae99497e054b1c6b92cd7`; the latter is the relevant pixel-equality proof.

## Canonical leader-family comparison

I inspected the canonical shelf and its contact sheet at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`. The shelf is native `156x210` RGBA country-leader art. The closest role/style controls used for this review were:

- `den_thorvald_stauning.png` (`156x210`, SHA-256 `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6`)
- `ice_sveinn_bjornsson.png` (`156x210`, SHA-256 `860726d268873f21ae0dbd6fb170482f50fad6393882b97b2b7b7a1814189d14`)
- `ire_eamon_de_valera.png` (`156x210`, SHA-256 `ff5f8689f1e8ea75bf88bea4c4a87dcf60518b1e062ea53be4a9ceff3509dcb0`)
- `fin_carl_mannerheim.png` (`156x210`, SHA-256 `7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e`)

The reference images were used for framing, painted surface, facial readability, contrast, and background treatment only. They were not used as identity sources.

## Separate verdicts

### Likeness / identity — PASS (raw-level, conditional)

The raw repaint retains the source's distinctive receding side-parted light hair, broad forehead, heavy eye/brow placement, broad nose, rounded lower face, full pale drooping moustache, slight three-quarter head direction, and civilian suit/tie framing. No face substitution or unrelated person is visible. The repaint adds color and smoother facial modeling to a low-resolution halftone master, so the enlarged result should still be checked after deterministic normalization; this conditional PASS does not waive the independent identity gate.

### HOI4 leader style — PASS (raw-level, conditional)

The repaint is a restrained head-and-shoulders oil-painted portrait with a quiet period civilian presentation, readable face, and no modern props, text, or cinematic effects. It sits in the same broad painted country-leader family as the canonical Stauning, Sveinn Björnsson, de Valera, and Mannerheim references. Its darker textured background and stronger brush texture are a stylistic variation, not an automatic rejection. No native `156x210` candidate exists yet, so this is not a runtime-size approval.

### Source attribution / provenance / rights — HOLD (fail closed)

The named package contains no source URL, author, archive or collection accession, source date or estimated date, license/public-domain statement, or rights-cleared attribution for `alderdice.png`. The PNG has no embedded EXIF attribution. It also contains no ImageGen prompt, model/version/seed or other generation record for the raw repaint. Filenames and visual appearance cannot establish public-domain status or ownership. I therefore make no rights or provenance inference.

### 1936 role fit — PROVISIONAL VISUAL PASS; HISTORICAL ROLE EVIDENCE HOLD

The monochrome period portrait, civilian suit, tie, and adult male presentation are visually plausible for a 1936 Newfoundland civic-leader surface and have no visible anachronism. The named source/package files do not document the subject's 1936 office/title, the photograph's date, or the archival context needed to make that role claim defensible. Treat role fit as provisional until the parent supplies dated source and role evidence.

## Missing promotion evidence

- No deterministic `156x210` processed candidate for Alderdice is present in the named package.
- No native-size or `4x` nearest-neighbour comparison sheet for the Alderdice source/crop/raw result and canonical leader references is retained.
- No source attribution or rights record is retained for the immutable master.
- No ImageGen prompt/generation record is retained for the raw repaint.
- No subject-ownership search or guarded transfer contract is present in the named package; this audit grants no runtime character ownership claim.
- No final DDS exists or is authorized by this audit.

## Required next action

Supply a defensible source citation (URL or archive/collection and accession, author or archive, image date/era, and license or public-domain basis), the raw repaint prompt/generation record, the deterministic `156x210` candidate, and a native/enlarged comparison sheet. Re-run the independent likeness/style/provenance audit after those records exist. Until then the disposition remains **HOLD** and no fallback or substitute portrait is approved.
