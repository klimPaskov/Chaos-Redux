# IW-184 California William D. Stephens portrait trial 01

Status: `candidate_requires_independent_audit`.

This package applies the mandatory grounded-person portrait chain to William Dennison Stephens for the existing Event 6 California civic-convention consumer.

It proposes a guarded player-facing identity transfer from the fictional working name `Daniel Mercer` to William D. Stephens while retaining the stable script character and sprite.

No DDS is authorized or wired until an independent reviewer separately passes provenance, likeness, HOI4 leader style, role fit, male-only scope, ownership, and the no-advisor/no-`_small` boundary.

## Stable consumer

| Field | Value |
|---|---|
| Package | IW-184 California, carrier `HBX` |
| Character | `HBX_independence_wave_civic_convention_chair` |
| Sprite | `GFX_portrait_HBX_independence_wave_civic_convention` |
| Runtime DDS after approval | `gfx/leaders/006_independence_wave/portrait_HBX_independence_wave_civic_convention.dds` |
| Role family | Civic country leader and constitutional-convention chair |
| Gender gate | Male |
| Authorized surface | Full-size `civilian.large` only |

This package contains no advisor, dossier, operative, commander, female, or `_small` asset.

## Subject and alternate-history role

William D. Stephens served as governor of California from 1917 to 1923, as a United States congressman and lieutenant governor, and as director of the Los Angeles Chamber of Commerce from 1902 to 1911.

He was alive in 1936 and died in Los Angeles in 1944.

Those state and civic roles make him a plausible alternate-history chair for an emergency California constitutional convention.

The package does not claim that Stephens chaired a real convention in 1936.

## Immutable archival source

| Field | Value |
|---|---|
| Archive object | <https://www.loc.gov/pictures/item/2014715011/> |
| Persistent handle | <https://hdl.loc.gov/loc.pnp/ggbain.34859> |
| Direct unchanged JPEG | <https://cdn.loc.gov/service/pnp/ggbain/34800/34859v.jpg> |
| Retained master | `source_masters/HBX_william_stephens_loc_master.jpg` |
| Dimensions and mode | `743x1024`, grayscale |
| Master SHA-256 | `5BA60D2FD0FAB9A0DCF6A47B08A89BED486E35E5C14FC200C7FC6204B8652B5D` |
| Archive title | `Wm. D. Stephens` |
| Collection | George Grantham Bain Collection, Library of Congress |
| Date | Circa 1920 to 1925 |
| Rights | Library of Congress advisory: no known restrictions on publication |
| Role and life evidence | <https://governors.library.ca.gov/24-Stephens.html> |
| Secondary identity cross-check | <https://commons.wikimedia.org/wiki/File:William_D._Stephens_LCCN2014715011_(cropped).jpg> |

The retained master is the unchanged Library of Congress JPEG.

The Commons derivative is identity cross-check evidence only and is not an input.

The Library of Congress rights advisory is retained as written and is not upgraded to a Creative Commons or public-domain claim.

## Exact head-and-shoulders crop

| Field | Value |
|---|---|
| Crop | `source_crops/HBX_william_stephens_head_shoulders.png` |
| Crop record | `source_crops/HBX_william_stephens_head_shoulders.json` |
| Master rectangle | `(75,130,685,940)` |
| Dimensions | `610x810` |
| Crop SHA-256 | `D87F5FE6773844B597A4A1175DD26A6016A5A9DF87A6295CE074F92D33EA2085` |
| Crop record SHA-256 | `103998C275BACFBA65D8598CE01EE027EE797F2D3F99228C101855715CB57BFB` |
| Decoded-pixel equality | `true`; master rectangle and lossless crop both hash to `3D3D617EEFFF51F0FC629625A41A36C167D35F26C98239CCD81E3EE36A82F883` |

The skill-local crop utility removed the negative's handwritten catalog marks while preserving the full face, collar, tie, and shoulders without resizing, enhancement, recolouring, or retouching.

## Source-locked ImageGen repaint

| Field | Value |
|---|---|
| Identity input | The exact archival crop above |
| Style-only references | `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/den_thorvald_stauning.png` and `ire_eamon_de_valera.png` |
| Prompt | `identity_repaint_prompt.md` |
| Raw repaint | `imagegen_results/HBX_william_stephens_identity_preserve_trial_01.png` |
| Raw dimensions | `1080x1456` |
| Raw SHA-256 | `9E52BFEBC1DFCA49FFB08AAD3CB4742242685770AD6F443F07A8C05F67B84CCC` |

The archival crop remains the sole identity, anatomy, age, pose, clothing, and composition authority.

The two HOI4 portraits are style-only references and may not transfer identity or clothing.

## Deterministic 156x210 processing

| Field | Value |
|---|---|
| Processor | `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py` |
| Positional mode | `leader` |
| Role family | `leader` |
| Source kind | `real` |
| Raw repaint crop | `(0,1,1080,1455)` |
| Candidate | `processed_png/portrait_HBX_independence_wave_civic_convention.png` |
| Candidate dimensions | `156x210` |
| Candidate SHA-256 | `6BAC5F87D3DF3AEB4FD9B92BAE2C51A204739ECE11BA820C28E49A2DE3362154` |
| Candidate domain-separated decoded RGBA SHA-256 | `C51843BD453CD9C08764AC2BF23EC475B4A1667B9250ADB9854280C1A620FAE9` |
| Metadata | `processed_png/portrait_HBX_independence_wave_civic_convention.png.json` |
| Metadata SHA-256 | `4BBE5BF4556EDEEE102C03477A8325B36B24D14EE2BEAC242E4999BAD2FA750C` |
| Style sheet | `review/HBX_william_stephens_leader_style_sheet.png` |
| Style-sheet SHA-256 | `DF014FC2965D688A4E3281CB5D1AEA1AFE3562BCB3C6E21D4D1FFA9C70B436CF` |

The processor uses the canonical leader reference family and performs deterministic crop, grade, and export only.

The metadata's decoded hash uses the documented domain prefix and encoded dimensions.

## Ownership and transfer boundary

Current project, vanilla, Kaiserreich `1521695605`, and approved references `2265420196` and `1458561226` contain no exact or variant William D. Stephens character or portrait owner.

Hiram Johnson is not a fallback because Kaiserreich owns `ACC_hiram_johnson`.

The stable Event 6 character and sprite may be rebound to William D. Stephens only after the independent portrait audit passes.

The parent must then update the player-facing name and description in the same runtime promotion.

## Independent audit gate

The reviewer must compare the unchanged master, exact crop and equality JSON, raw ImageGen repaint, native `156x210` candidate, prompt, metadata, and canonical leader references at native size and a disposable nearest-neighbour enlargement.

The reviewer must return separate verdicts for archive identity and rights, crop equality, historical and alternate-history role, likeness, HOI4 leader style, framing, male-only scope, ownership and guarded transfer, and absence of advisor, dossier, operative, commander, and `_small` derivatives.

The likeness verdict must specifically test the high forehead and bald crown, sparse side hair, unequal heavy-lidded eyes, eyebrow geometry, nose, lips, cheek lines, ears, jaw, chin, apparent age, expression, head angle, neck, and stout shoulder proportions.

If every gate passes, the parent may update localisation to William D. Stephens, convert this exact candidate to the stable DDS, prove decoded-pixel equality, and request a fresh IW-184 country-package audit.

Any failed gate leaves the candidate export-only.
