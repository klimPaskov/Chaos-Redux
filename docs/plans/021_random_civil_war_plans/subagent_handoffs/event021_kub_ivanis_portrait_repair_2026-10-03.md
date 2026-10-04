# Event021 inherited Event006 KUB Ivanis portrait repair

Date: 2026-10-03.

Status: the source placeholder is independently reviewed, converted, and wired at the existing vanilla large-portrait path. The HOI4-styled final remains pending the user's supplied image; no `styled_final` is claimed.

Scope: only `KUB_ivanis_vasily_nikolaevich`. No character identity, traits, gameplay, localisation, event, focus, country setup, shared UI, or other portrait rows were changed.

The 2026-09-25 portrait audit handoff's row 51 identified the missing NSB large DDS and the separate existing small idea icon. That prior audit file remains unchanged; this dated portrait handoff records the newer Event021 source-placeholder state for KUB Ivanis.

## Changed files

The durable source package and portrait manifest are under `docs/assets/portraits/021_random_civil_war/`:

- `KUB_ivanis_vasily_nikolaevich/portrait_KUB_ivanis_vasily_nikolaevich_original.jpg` is the unchanged 1400x1000 Commons source image.
- `KUB_ivanis_vasily_nikolaevich/portrait_KUB_ivanis_vasily_nikolaevich_source_crop.png` is the manual 146x196 lossless crop.
- `KUB_ivanis_vasily_nikolaevich/portrait_KUB_ivanis_vasily_nikolaevich_source_crop.json` records exact crop bounds and decoded-pixel equality.
- `KUB_ivanis_vasily_nikolaevich/portrait_KUB_ivanis_vasily_nikolaevich_156x210.png` is the deterministic LANCZOS placeholder preview.
- `KUB_ivanis_vasily_nikolaevich/portrait_KUB_ivanis_vasily_nikolaevich_156x210_nearest4x.png` is the 4x nearest-neighbour review image.
- `KUB_ivanis_vasily_nikolaevich/portrait_KUB_ivanis_vasily_nikolaevich_comparison_review.png` compares the source master, archival context page, exact crop, processed placeholder, and canonical role reference.
- `KUB_ivanis_vasily_nikolaevich/portrait_KUB_ivanis_vasily_nikolaevich_native_4x_review.png` compares candidate and vanilla leader reference at exact native size and 4x nearest-neighbour.
- `KUB_ivanis_vasily_nikolaevich/portrait_KUB_ivanis_vasily_nikolaevich_excelsior_1920-09-01.pdf` and `KUB_ivanis_vasily_nikolaevich/portrait_KUB_ivanis_vasily_nikolaevich_excelsior_1920-09-01_page1_context.jpg` preserve the period publication and its page image as identity/date evidence.
- `KUB_ivanis_vasily_nikolaevich/portrait_KUB_ivanis_vasily_nikolaevich.txt` is the provenance and review contract.
- `docs/assets/portraits/021_random_civil_war/manifest.md` records the single portrait row, runtime crosswalk, rights status, and review state.
- `gfx/leaders/KUB/portrait_KUB_ivanis_vasily_nikolaevich.dds` installs the source placeholder at the vanilla-declared texture path.
- This handoff records the bounded repair and its remaining limits.

The repository `.gitignore` ignores `docs/assets/`. The archive and manifest are present in the shared worktree but remain ignored and unstaged. The runtime DDS and this handoff are untracked; nothing was staged or committed, as directed.

## Identity and source evidence

The installed character token is `KUB_ivanis_vasily_nikolaevich`, with the vanilla display key `Ivanis Vasily Nikolaevich`. The [Internet Encyclopedia of Ukraine biography](https://www.encyclopediaofukraine.com/display.asp?linkpath=pages%5CI%5CV%5CIvanysVasyl.htm) identifies Vasyl Ivanys, born in 1888, as a Kuban civic leader and acting otaman in 1920. This independently verifies that the game token refers to the historical Vasyl Mykolayovych Ivanys, also rendered Vasily Nikolaevich Ivanis.

The source image is [Government of South Russia 1920 cropped.JPG on Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Government_of_South_Russia_1920_cropped.JPG), 1400x1000, photographer unknown. The [Commons caption](https://commons.wikimedia.org/wiki/File:Government_of_South_Russia_1920_cropped.JPG) orders the seated group left to right and identifies the sixth sitter as deputy Kuban ataman engineer V.N. Ivanis. The [Russian historical-documents archive record](https://www.docs.historyrussia.org/ru/nodes/34349-pravitelstvo-yuga-rossii-sevastopol-avgust-1920-g) independently describes the same group photograph and names Ivanis.

The [Argonnaute scan of the 1 September 1920 *Excelsior* issue](https://argonnaute.parisnanterre.fr/media/b150f84d-cb07-44c4-a40c-dddf783d8646.pdf) provides period publication evidence. Its caption calls this a photograph taken in Sevastopol and names General Ivanis as ataman of the Kuban Cossacks; its `(5)` is the newspaper's figure label, not the sixth-sitter ordering used for the crop.

The Commons record applies Creative Commons Public Domain Mark 1.0. The [PDM deed](https://creativecommons.org/publicdomain/mark/1.0/) is a rights-status mark, not a license, and warns that status can vary by jurisdiction. The [French Intellectual Property Code, Article L123-3](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006278941/2023-04-10) gives anonymous works a 70-year exclusive-right term counted from 1 January after publication. For the 1920 French publication, that term ended on 31 December 1990 if the work remains anonymous. The photographer is uncredited in the checked source records; independent review passed this French anonymous-work basis, while rights status in other jurisdictions remains unresolved.

The earlier one-person `Ivanys V.jpg` candidate was not used because its date, author, and publication evidence remain unknown. The 1920 group photograph was selected because the archival publication and separate group caption provide a verifiable identity position and a dated publication basis.

## Crop and visual review

The crop box is `[700, 495, 846, 691]` in the unchanged 1400x1000 source master, producing a 146x196 grayscale crop. The independent reviewer confirmed that it isolates the sixth seated subject, contains one face, and has no second face; it includes the subject's chest and folded hands plus fragments of adjacent clothing at the edges.

The crop tool recorded `decoded_pixels_equal=true` with matching RGBA hashes and manual-crop mode because the source is a multi-person group. The 156x210 RGB preview is a deterministic Pillow LANCZOS resize. At native size and 4x nearest-neighbour, the portrait is soft and grainy but remains identifiable and is acceptable as a temporary source placeholder.

The inspected canonical reference was `.agents/skills/chaos-redux-event-assets/assets/gfx_references/portraits/leaders/afg_mohammed_zahir_shah.png`, a 156x210 Vanilla HOI4 leader portrait. The reference informed role framing and style comparison only. No small idea icon, portrait backdrop, ImageGen output, or other subject image was used.

Independent read-only reviewer: `chaosx_country_package_auditor` (`Tag Patch One`), 2026-10-03. Separate verdicts: identity PASS; crop/framing PASS; image quality PASS for source-placeholder use; style/framing PASS for a source placeholder only; French anonymous-work rights basis PASS; global jurisdiction status unresolved. The review found the image is not a HOI4-painted final.

Parent visual review inspected the comparison sheet and the exact-native/nearest-4x sheet on 2026-10-03.
The crop contains one identifiable face with surrounding uniform and hands, with grain and archival background visible at native size.
It is accepted only as the sourced placeholder described by this handoff, not as a HOI4-style final or a fully certified worldwide rights result.
The existing small idea icon remains a distinct consumer and was not enlarged or used as the leader image.

## Dimensions and hashes

| Artifact | Dimensions / layout | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| Source master JPEG | 1400x1000, grayscale | 484480 | `95EC10893224D20A63DC624D43BCAE4DD8AD686E56E4A1EB62862F17D3203475` |
| Lossless source crop PNG | 146x196, grayscale | 19714 | `45011F71141F7D7D208DF6C84DFFACC01285CBE1F6FA9AA9CD5962EB72F29E4D` |
| Processed placeholder PNG | 156x210, RGB | 35922 | `387247DCE2D446E1E8E3C23CE59D66F7C976188F9769E9DE59305EA3DBC7223B` |
| Processed 4x review PNG | 624x840, nearest-neighbour | 54290 | `7C3568C6FAD9A543A9391B723CEF1254951C92449912D80FC483EFDBC380A92D` |
| Source-context page JPEG | 3495x4826, RGB | 3661870 | `2C06235964270DCAF9B6496B30858876C55EDDE4306F9B90AE9BC7DA9AD8BA22` |
| Source-context PDF | 6 pages | 21025732 | `B28943024E9E16B759A70F700B6BE633C95C96319C51D64A203C1274A69CE5CB` |
| Comparison review sheet | 2232x1986, RGB | 2323947 | `842B36CB08CAF16F91BCD711BFA0667807532111058C56A22FF1D60A9CDD10A3` |
| Native-and-4x review sheet | 1368x1278, RGB | 253198 | `547F008C5F6B700A82278B417BF054FCF8BBB5A5782DBCDB5F57FD166C7EB539` |
| Runtime source-placeholder DDS | 156x210, one-level BGRA, opaque alpha | 131168 | `C51BB8FC07A5F9D620C8B5DDD05814BE424AD79F3C1980ECFF4BE95B59E5E707` |

The DDS has a valid 128-byte legacy header, BGRA masks, `DDSCAPS_TEXTURE`, zero mipmaps, and alpha range 255-255. Decoding it back to pixels produced exact equality with the processed PNG.

## Runtime wiring and replacement state

Installed vanilla `common/characters/KUB.txt` lines 3–8 already assign the large slot to `GFX_portrait_KUB_ivanis_vasily_nikolaevich` and the small slot to `GFX_idea_KUB_ivanis_vasily_nikolaevich`. Installed No Step Back `interface/nsb_portraits.gfx` lines 394–395 already maps the large sprite to `gfx/leaders/KUB/portrait_KUB_ivanis_vasily_nikolaevich.dds`. That exact large DDS was absent across the installed vanilla game root and recursively within the installed No Step Back folder; no DLC archive was present there. The separate 65x67 idea DDS exists at `gfx/interface/ideas/idea_KUB_ivanis_vasily_nikolaevich.dds`, SHA-256 `C215128B588FFFF5B03FC1885E0619DCC66CAC31798B6CC3B514F48F31A26E93`, and remains unchanged.

The new mod DDS resolves the exact existing vanilla sprite path. No duplicate `.gfx` entry or character file override was needed or added. The source archive is evidence only; no runtime reference points into `docs/assets/`.

Replacement state: `source_placeholder` is wired and pending the user's HOI4-style final. No `styled_final` was supplied, requested from an image provider, or generated. RunPod was never opened, operated, configured, queued, or monitored.

## Skipped checks and remaining limits

- No live HOI4 load/render was performed; the user owns live-game validation.
- Global copyright status was not certified in every jurisdiction; the reviewed public-domain basis is the 1920 anonymous publication under French law, alongside the Commons PDM status mark.
- No contact was made with a rights holder or archive.
- No other Event021/Event006 portrait rows or packages were audited.
- No files were staged, committed, or reverted. Other shared-worktree changes were left untouched.

There is no technical blocker to the reviewed French-law source-placeholder installation. The final portrait remains incomplete until the user supplies the HOI4-style replacement; global rights status remains unresolved outside the cited French basis.
