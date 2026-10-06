# Event001 Portrait Source and Installation Handoff

Disposition: `implemented` for the parent-approved grounded `source_placeholder`, installed on 2026-10-06 after the parent’s 2026-10-05 source/framing approval; the user-supplied HOI4-style final remains pending.

The accepted design basis is the parent-relayed user G6QA decision that generic committees may use authentic collective historical material without claiming every country is literally the Moscow Soviet.

## Source, review, and mode

The consumers at `common/scripted_effects/001_communism_spread_effects.txt:2367-2370` and `:2460-2463` retain the institutional leader names `Revolutionary Committee` and `Local Revolutionary Committee`; both use `GFX_portrait_communist_rebels`.

The parent approved group_v3 on 2026-10-05 as authentic collective institutional reference art; the frame shows three adjacent seated members and a small fragment of a fourth, and the accepted meaning is representative committee art rather than a literal Moscow identity for every country.

The selected crop `[1410,240,1690,617)` is 280x377 RGB and remains a decoded-pixel-exact manual crop of the source; its processed portrait is 156x210 RGB, with the 4x review image at 624x840 nearest-neighbour.

Source: [Ispolkom Mossoveta.jpg on Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Ispolkom_Mossoveta.jpg), [pinned Commons revision 1109907761](https://commons.wikimedia.org/w/index.php?title=File:Ispolkom_Mossoveta.jpg&oldid=1109907761), and [direct original JPEG](https://upload.wikimedia.org/wikipedia/commons/0/09/Ispolkom_Mossoveta.jpg).

The 1918 image depicts the first-convocation Moscow Soviet executive committee after the October Revolution; the Commons record cites *Krasnaya Moskva, 1917-1920*, a Moscow Soviet publication.

Commons marks the image Public Domain and displays Public Domain Mark 1.0; the original photographer and exact jurisdictional publication basis remain unknown and are retained as provenance limits accepted for this source-placeholder use.

The archived original is 1830x733 JPEG, 920898 bytes, SHA-256 `793b09c272f8fbb8f34e3b7b230a6b8f09bafcdea5a04563d02e3181516d4775`, and SHA-1 `bbf14c047474be6e1d16a52e03f64f601724107c`, matching the Commons record.

Portrait ownership searches for source-row spellings of Rogov, Lisitsin/Lisitsyn, Radzivils/Radzivilov, Nogin, Pevunov, Burovtsev, Belarusov, Zheltov, Bulochnikov, and Fonchenko found no exact or transliteration matches in project or installed-vanilla character, history, portrait, interface, and English-localisation roots; no character token or roster transfer was added.

## Installed asset and preserved lineage

The selected root PNG `docs/assets/portraits/001_communism_spread/portrait_communist_rebels_156x210.png` has SHA-256 `90034f7061cf5b70b300b4bbae1db37d1ec9a732398d2e0a674431864d34a782`; its 624x840 4x review PNG has SHA-256 `c3d231ef327992f995a0c310ed54edaa9afd5570d18e54db3317298f13a873de`.

The canonical archive DDS `docs/assets/portraits/001_communism_spread/portrait_communist_rebels.dds` is 156x210 uncompressed BGRA with opaque alpha, SHA-256 `059b20336d625906b5debf1545db445e7c361f90745c239b01d7ce704da9d021`.

The installed DDS at `gfx/leaders/001_communism_spread/portrait_communist_rebels.dds` has the same SHA-256; FFmpeg round-trip pixels match the processed PNG exactly.

The former runtime bytes are preserved at `docs/assets/portraits/001_communism_spread/portrait_communist_rebels_unverified_priorversion.dds`, SHA-256 `7e6a0404c9b329b9a3ec4a345132cfad49ee13facc3fb7591e81e394e6c4efcc`.

The prior-runtime hash string in the earlier handoff contained 65 hex characters; Python hashlib and PowerShell measured the valid 64-character SHA-256 recorded above for both the pre-install runtime and its archived copy.

The parent-rejected v1 individual files were snapshotted under `candidates/individual_v1/` with a rejected-candidate record; group_v2 remains under `candidates/group_v2/` as an unselected wide composition.

The stable sprite `GFX_portrait_communist_rebels` at `interface/chaosx_characters.gfx:151-152` remains unchanged and points to the installed runtime path; no `.gfx`, character, gameplay, localisation, event, focus, decision, or country wiring changed.

## Parent force-add paths

The repository ignores `docs/assets/` at `.gitignore:80`; the paths below are the exact portrait archive paths selected for a parent-scoped `git add -f`. No files were staged by this task.

Canonical installed source-placeholder package:

- `docs/assets/portraits/001_communism_spread/portrait_communist_rebels_original.jpg`
- `docs/assets/portraits/001_communism_spread/portrait_communist_rebels_source_crop.png`
- `docs/assets/portraits/001_communism_spread/portrait_communist_rebels_source_crop.json`
- `docs/assets/portraits/001_communism_spread/portrait_communist_rebels_156x210.png`
- `docs/assets/portraits/001_communism_spread/portrait_communist_rebels_156x210_4x.png`
- `docs/assets/portraits/001_communism_spread/portrait_communist_rebels.dds`
- `docs/assets/portraits/001_communism_spread/portrait_communist_rebels_review.png`
- `docs/assets/portraits/001_communism_spread/portrait_communist_rebels.txt`
- `docs/assets/portraits/001_communism_spread/source_receipt.json`
- `docs/assets/portraits/001_communism_spread/portrait_communist_rebels_unverified_priorversion.dds`

Rejected v1 and unselected group_v2 version evidence:

- `docs/assets/portraits/001_communism_spread/candidates/individual_v1/portrait_communist_rebels_original.jpg`
- `docs/assets/portraits/001_communism_spread/candidates/individual_v1/portrait_communist_rebels_source_crop.png`
- `docs/assets/portraits/001_communism_spread/candidates/individual_v1/portrait_communist_rebels_source_crop.json`
- `docs/assets/portraits/001_communism_spread/candidates/individual_v1/portrait_communist_rebels_156x210.png`
- `docs/assets/portraits/001_communism_spread/candidates/individual_v1/portrait_communist_rebels_source_placeholder_candidate.dds`
- `docs/assets/portraits/001_communism_spread/candidates/individual_v1/portrait_communist_rebels_review.png`
- `docs/assets/portraits/001_communism_spread/candidates/individual_v1/portrait_communist_rebels.txt`
- `docs/assets/portraits/001_communism_spread/candidates/individual_v1/portrait_communist_rebels_v1_rejected_record.md`
- `docs/assets/portraits/001_communism_spread/candidates/group_v2/portrait_communist_rebels_original.jpg`
- `docs/assets/portraits/001_communism_spread/candidates/group_v2/portrait_communist_rebels_source_crop.png`
- `docs/assets/portraits/001_communism_spread/candidates/group_v2/portrait_communist_rebels_source_crop.json`
- `docs/assets/portraits/001_communism_spread/candidates/group_v2/portrait_communist_rebels_156x210.png`
- `docs/assets/portraits/001_communism_spread/candidates/group_v2/portrait_communist_rebels.txt`

The duplicate group_v3 production directory is retained locally but omitted from the selected force-add paths because its selected files are promoted into the canonical root package.

## Validation limits

The installed Vanilla country-leader reference `gfx/leaders/Africa/Portrait_Africa_Generic_1.dds` was inspected as style control only; its SHA-256 is `aab299a84022eb5f96fde1510bcf651ed2ff507fc63d0436eab8982504255cec`, and its decoded 156x210 pixels match canonical `africa_generic_1.png` exactly.

No RunPod interaction or HOI4 launch occurred; live consumer validation remains with the user, and the installed source placeholder is pending the user’s HOI4-style final.
