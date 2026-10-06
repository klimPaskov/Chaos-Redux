# Event001 Portrait Manifest

Design disposition: `accepted and queued` based on the parent-relayed user G6QA acceptance that generic committees may use authentic collective historical material without claiming every country is literally the Moscow Soviet.

Portrait status: `source_placeholder` installed at the stable runtime path on 2026-10-06; the user’s HOI4-style final remains pending.

Source-mode gate: `grounded_source_only`, because the consumers are plausible political institutions in historically grounded country variants; no generated-fictional portrait route was used.

## Consumers and wiring

The existing effects at `common/scripted_effects/001_communism_spread_effects.txt:2367-2370` and `:2460-2463` create `Revolutionary Committee` and `Local Revolutionary Committee` leaders using `GFX_portrait_communist_rebels`.

The sprite at `interface/chaosx_characters.gfx:151-152` already points to `gfx/leaders/001_communism_spread/portrait_communist_rebels.dds`; no `.gfx`, leader, gameplay, event, or country wiring changed.

## Source and rights

Source: [Ispolkom Mossoveta.jpg on Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Ispolkom_Mossoveta.jpg), [pinned Commons record](https://commons.wikimedia.org/w/index.php?title=File:Ispolkom_Mossoveta.jpg&oldid=1109907761), and [direct original JPEG](https://upload.wikimedia.org/wikipedia/commons/0/09/Ispolkom_Mossoveta.jpg).

The Commons record dates the photograph to 1918 and describes members of the first-convocation Moscow Soviet executive committee after the October Revolution; it cites *Krasnaya Moskva, 1917-1920*, a Moscow Soviet publication.

The original photographer is unknown; Commons marks the image Public Domain and displays Public Domain Mark 1.0, but the original author and exact jurisdictional publication basis are not specified, so this record preserves the Commons rights claim and its limits without asserting blanket legal certainty.

The untouched JPEG is `docs/assets/portraits/001_communism_spread/portrait_communist_rebels_original.jpg`, 1830x733 and 920898 bytes, SHA-256 `793b09c272f8fbb8f34e3b7b230a6b8f09bafcdea5a04563d02e3181516d4775`, SHA-1 `bbf14c047474be6e1d16a52e03f64f601724107c`, matching the Commons page checksum.

## Candidate lineage

| Candidate | Disposition | Archived evidence | Notes |
| --- | --- | --- | --- |
| v1 individual crop | Rejected by parent on 2026-10-05. | `candidates/individual_v1/`; crop `[1260,215,1440,457)`, 180x242, SHA-256 `b387655324401090f5be355d30831a38456c806f30a7462c5e026f5c9885b140`; versioned crop JSON SHA-256 `a483179f61b72c41f3e08617d6708dda3a909adfe0d1c2d704c3955ef3607ceb`; 156x210 PNG SHA-256 `d918bbdf74cf47e0119b5c0b912ec0bea444903f6db6f8da14eef556496461a7`; rejected DDS SHA-256 `2106eb41546f1029f40ca68567dbde7a3a73a6ab2117538700e309e8201faff3`. | Parent found that one historical face read as one person and lost the committee context; preserved for lineage and never installed. |
| group_v2 wide exploration | Unselected by producer. | `candidates/group_v2/`; crop `[1330,170,1692,657)`, 362x487, SHA-256 `47d5bad80d15bd6b0d5df8a1264b0ee45f8bb9d3a6515c61b33fdcb95815156b`; preview SHA-256 `40ef361a014777883815cdca41e76a5bfdf179057c1e9d5be1c08637a0567654`. | It included too many partial rear-row figures for the requested three-to-five-member framing and was not submitted for approval. |
| group_v3 collective | Parent approved on 2026-10-05 and installed as the source placeholder. | Canonical root crop `[1410,240,1690,617)`, 280x377, SHA-256 `117918fa06b8e0b2d2bb8bbb098b0506d59303590de321e0c1611851cc69c8fc`; 156x210 PNG SHA-256 `90034f7061cf5b70b300b4bbae1db37d1ec9a732398d2e0a674431864d34a782`. | Three adjacent seated committee members read collectively; source-position mapping is approximate and no personal name is used in game content. |

The canonical root crop JSON is SHA-256 `c3d98dcfa5ad143962906d73aeaf10776c8d1bbcd9062eb222713abe4a93604c`; it records manual crop mode, exact coordinates, and decoded-pixel equality.

The canonical 4x nearest-neighbour review PNG is `portrait_communist_rebels_156x210_4x.png`, 624x840, SHA-256 `c3d231ef327992f995a0c310ed54edaa9afd5570d18e54db3317298f13a873de`.

The canonical archive DDS is `portrait_communist_rebels.dds`, 156x210 uncompressed BGRA with opaque alpha, SHA-256 `059b20336d625906b5debf1545db445e7c361f90745c239b01d7ce704da9d021`; FFmpeg-decoded pixels match the processed PNG exactly.

The prior runtime bytes are archived as `portrait_communist_rebels_unverified_priorversion.dds`, SHA-256 `7e6a0404c9b329b9a3ec4a345132cfad49ee13facc3fb7591e81e394e6c4efcc`.

The canonical review sheet is `portrait_communist_rebels_review.png`, 3032x1920, SHA-256 `4666f201ffa5a865b9d0184f4a65d766eb98db0765cefc37e28262ddfa14c3ac`; it shows the source with v1/v3 crop bounds and 4x comparisons of the old runtime, rejected v1, selected group_v3, and Vanilla style reference.

The canonical provenance contract `portrait_communist_rebels.txt` has SHA-256 `bc402eeedc0d70b95fe5754e00019439328da966ce9c80c2dd04fa5e45b85d74` and records the separate parent-reviewed identity, framing, provenance, installation, and pending-final states.

The source receipt is `source_receipt.json`, SHA-256 `a75bce5d05e7b0000071850e68005cd504753f449a2158b6d6ebab2542d0945e`; the parent accepted the Commons Public Domain Mark for this placeholder while unknown-author and jurisdictional-basis limits remain recorded.

## Review, ownership, and final state

The parent reviewer approved group_v3 on 2026-10-05 as authentic collective institutional reference art; it does not claim that all countries share this specific Moscow committee.

The source crop keeps three readable members and a small source-visible fragment of a fourth at the left edge; parent accepted the framing for the collective portrait.

Ownership searches covered source-row spellings for Rogov, Lisitsin/Lisitsyn, Radzivils/Radzivilov, Nogin, Pevunov, Burovtsev, Belarusov, Zheltov, Bulochnikov, and Fonchenko, including Cyrillic variants, under project and installed-vanilla `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and English localisation; no exact or spelling/transliteration matches were found.

The canonical country-leader contact sheet and installed Vanilla `gfx/leaders/Africa/Portrait_Africa_Generic_1.dds` were inspected as style controls only; that installed DDS SHA-256 is `aab299a84022eb5f96fde1510bcf651ed2ff507fc63d0436eab8982504255cec`, and its decoded 156x210 pixels match canonical `africa_generic_1.png` SHA-256 `f37a9ab2ca9460b86df5e5db7491b0ba80a405a8e402ae2c0ffb0cb087b03f1d`.

The portrait-backdrop contact sheet was inspected after vanilla leader references and supplied no identity source or candidate pixels.

The runtime DDS `gfx/leaders/001_communism_spread/portrait_communist_rebels.dds` has SHA-256 `059b20336d625906b5debf1545db445e7c361f90745c239b01d7ce704da9d021`, matching the canonical archive DDS.

The source placeholder is installed and remains pending the user’s HOI4-style final; no RunPod interaction or HOI4 launch occurred.

The repository ignores `docs/assets/` at `.gitignore:80`; the archive is on disk but omitted from ordinary Git status, and no files were staged.
