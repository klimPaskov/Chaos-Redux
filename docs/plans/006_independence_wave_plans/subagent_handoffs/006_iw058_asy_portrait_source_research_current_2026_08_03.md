# IW-058 ASY portrait source research current handoff (2026-08-03)

Research date: 2026-08-03. This bounded source-only pass searched for attributable, period-fitting real-person portraits for the IW-058 Assyria Concordat Council, civic chamber, and Levies/guardianship roster. It did not edit GFX, characters, events, gameplay, localisation, or runtime assets.

## Outcome

The pass adds one well-documented archival candidate for parent review: Yousef VI Emmanuel II Thomas, Chaldean Catholic Patriarch of Babylon from 1900 to 1947. He was alive and serving at the 1936 baseline, and his office is a plausible institutional Concordat Council seat if the parent roster intends to include a Chaldean Catholic delegate. The source is held at `needs_user_review`, not `source_ready_for_runtime`, because Commons' `PD-US-expired` assertion does not identify the underlying image maker and is not a universal legal clearance.

The package is source-only and records `runtime_authorized=false`. No DDS was created and no runtime basename was invented.

## New package

Package root: `docs/assets/006_independence_wave/iw058_portrait_source_research_current_2026_08_03/`.

| Evidence | Path | SHA-256 |
|---|---|---|
| Immutable 1920 source master | `source_masters/ASY_concordat_council_yousef_emmanuel_ii_thomas_1920_hathitrust.jpg` | `ad3f489e9cb2b98f89afe72e831607c03b4440cac70f4fc0a9c6a3b47cf01151` |
| Exact archival crop | `source_crops/ASY_concordat_council_yousef_emmanuel_ii_thomas_1920_exact_crop.png` | `d93040eb00bc2ddfe26223fabcab64efb5391a521876d6b6199d84bf43ace4ba` |
| Exact crop JSON equality evidence | `crop_metadata/ASY_concordat_council_yousef_emmanuel_ii_thomas_1920_exact_crop.json` | `568bb6e02709fce3f043651247afe54c65b846a601c7f5ff6ceb75febca7d3f5` |
| Deterministic 156x210 source placeholder | `processed_png/ASY_concordat_council_yousef_emmanuel_ii_thomas_156x210_source_placeholder.png` | `381f35369c7a25bdfb4b809b7f947ccd03752b61ffbd086fc29c4e456ba97711` |
| Processing record | `crop_metadata/ASY_concordat_council_yousef_emmanuel_ii_thomas_156x210_processing.json` | `d857e282d9eba3f33faf58dfabb0bcbf72b42b486d65346ae223cb7e065dbedf` |
| Candidate comparison sheet | `review/ASY_yousef_emmanuel_ii_thomas_source_candidates_contact_sheet.png` | `92be6b62d97dedeee83779700ee83d79a4825c4206cb5689635db70953d4a4d0` |
| Alternative 1925 source master | `source_masters/ASY_concordat_council_yousef_emmanuel_ii_thomas_1925_commons.jpg` | `626ead387e45ef1f1c5b334166940d466ea72ec9ae08c40f99d2d23a242226be` |

The master is the Wikimedia Commons file [His Beatitude the Chaldean, Patriarch of Babylon.jpg](https://commons.wikimedia.org/wiki/File:His_Beatitude_the_Chaldean,_Patriarch_of_Babylon.jpg), sourced to Joseph Naayem's 1921 *Shall this nation die?* scan at [HathiTrust/Library of Congress](https://babel.hathitrust.org/cgi/pt?id=loc.ark:/13960/t6nz91c0r). Commons records the plate date as 1920 and a `PD-US-expired` status. The printed caption identifies the subject as the Chaldean Patriarch of Babylon. [Catholic-Hierarchy](https://www.catholic-hierarchy.org/bishop/bthomg.html) independently records Yousef VI Emmanuel II Thomas as Patriarch of Babylon from his 1900 confirmation through his 1947 death, establishing 1936 baseline fit.

The exact crop rectangle is `(217, 250, 1127, 1475)` in decoded `1344x2123` master pixels, producing `910x1225`. The crop was made with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py`; its JSON evidence reports decoded-pixel equality. The preview uses Pillow `ImageOps.fit`, LANCZOS, centered, no bleed, no enhancement, recolouring, retouching, or alpha conversion, and is exactly `156x210` RGB.

## Alternative and rejected leads

The retained 1925 Commons source is visually strong but marked `PD-old` with an unknown author and an "own work" upload chain, so it remains an unselected `needs_user_review` alternative. The low-resolution 1914 Gallica scan and anonymous Iraq scan were inspected but not selected because their small/oval presentation loses material identity and clothing detail.

No new defensible civic-chamber standalone portrait was found. Yusuf Salman Yusuf remains a name collision in the approved reference trees, Joel Werda remains blocked, and the existing Gallo Shabo source remains parent-owned and untouched.

No new rights-clear single-person Levies/guardianship portrait was found. Yacob Khoshaba Aboona remains rights-reserved, Daniel Ismail remains a group-source/date/identity review item, and the Haydo source remains `needs_user_review` for provenance and rights-chain review.

Existing historical-role outcomes remain unchanged: Mar Eshai Shimun XXIII is blocked by the 2010 copyrighted-book source with no reuse grant; Mar Benyamin Shimun XXI has a rights-clear circa-1915 source but is dead before the 1936 active-role baseline; Naum Faiq and Agha Petros are legacy-only candidates because they died in 1930 and 1932 respectively. No generated or generic substitute was created for any blocked identity.

## Ignored runtime paths

The following existing runtime and wiring surfaces were intentionally ignored and remain parent-owned:

- `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_concordat_council.dds` remains the existing Barsoum-backed consumer.
- `interface/006_independence_wave_iw043_iw058_portraits.gfx` remains unchanged, including `GFX_portrait_ASY_independence_wave_concordat_council`.
- `common/characters/006_independence_wave_iw043_iw058_characters.txt` remains unchanged, including `ASY_independence_wave_concordat_council`.
- All existing `docs/assets/006_independence_wave/asy_portrait_source_research_v91_2026_08_01`, `asy_portrait_source_retry_v92_2026_08_01`, and later Barsoum promotion packages were preserved and not overwritten.

## Parent action

The parent must independently accept the source rights chain and confirm whether a Chaldean Catholic patriarch belongs in the IW-058 Concordat Council roster. If accepted, the parent chooses the stable runtime basename and owns DDS conversion, GFX, character, localisation, and gameplay wiring. Until then, keep the new package at `needs_user_review` with `runtime_authorized=false` and do not point a sprite or character at the `docs/assets` path.

## Files changed by this handoff

- `docs/assets/006_independence_wave/iw058_portrait_source_research_current_2026_08_03/` (source masters, exact crop, deterministic preview, metadata, manifest, comparison sheet, and GFX boundary note).
- This dated handoff file.

No gameplay or runtime files were changed.
