# IW-155 Bali portrait research handoff (2026-08-13)

## Disposition

IW-155 (`BLI`) remains **HOLD / fail-closed** for portrait admission. No source-placeholder package was created, no source image was copied, no crop or resize was run, and no PNG, DDS, `.gfx`, character, localisation, or gameplay file was changed.

The accepted research row requires a sourced real male period incumbent or claimant, or authentic archival material depicting the actual Balinese regency/royal council. It explicitly forbids an invented dynasty member, generated officeholder, generic council, or neighboring Indonesian ruler. The current evidence identifies plausible living-in-1936 Balinese claimants, but none has both an exact 1936 institutional role and a rights-cleared, role-appropriate portrait source ready for the unchanged-source portrait gate.

## Accepted row and runtime boundary

- Accepted row: `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`, `IW-155`.
- Identity: Bali; registered tag `BLI`; current-map compact anchor is state `1052` (historical baseline row references coarse state `667` with a Bali substate).
- Leadership rule: sourced real male period incumbent or claimant; if no safe claimant exists, authentic archival material for the actual institutional regency or royal council; otherwise block.
- Existing vanilla consumer is preserved: `INS_dewa_geg` remains the BLI country leader/advisor character and its existing portrait consumer. The Indonesian transfer path `indonesia_transfer_BLI` remains untouched.
- No Event 006 roster or guarded transfer was accepted by this handoff.

## Candidate review

### Conditional claimant: Tjokorda Gde Raka Soekawati (Sukawati)

Identity and date evidence: the Indonesian biography identifies Tjokorda Gdé Raka Soekawati (15 January 1899–1967) as a Balinese noble and records his 1919 appointment as Punggawa of Ubud, 1924–1927 Volksraad service, and 1931–1932 European study. He was therefore alive in 1936 and is a defensible named Balinese institutional claimant, but the checked evidence does not establish that he was the incumbent of all Bali or of the BLI release institution in 1936.

- Research source: [Tjokorda Gde Raka Soekawati, Indonesian Wikipedia](https://id.wikipedia.org/wiki/Tjokorda_Gde_Raka_Soekawati).
- Rights-cleared portrait lead: [Tjokorda Gde Rake Sukawati (1947), Commons](https://commons.wikimedia.org/wiki/File:Tjokorda_Gde_Rake_Sukawati_(1947).jpg). Commons metadata identifies Harry Sagers / Anefo, Nationaal Archief credit, 28 January 1947, 2036x2036 JPEG, and Public Domain status.
- Rights-cleared portrait lead: [Tjokorda Gde Raka Soekawati, Pendidikan Politik Rakjat p.4, Commons](https://commons.wikimedia.org/wiki/File:Tjokorda_Gde_Raka_Soekawati,_Volume_I_of_Pendidikan_Politik_Rakjat,_p4.jpg). Commons metadata identifies the Ministry of Information of East Indonesia, 1949 publication, 662x818 JPEG, and Public Domain status.
- Additional conditional source: [KITLV 157666, Commons](https://commons.wikimedia.org/wiki/File:Tjokorda_Gde_Raka_Soekawati_(links)_wordt_be%C3%ABdigd_als_president_van_de_staat_Oost-Indonesi%C3%AB_tijdens_de_Conferentie_te_Denpasar,_KITLV_157666.tiff). The KITLV/Nederlands-Indische Government Information Service image is dated 1946 and CC BY 4.0, but depicts his postwar East Indonesia presidency and is not a 1936 office portrait.

Disposition: **not admitted**. These sources can support a future identity package only after the parent accepts the claimant route, confirms the exact 1936 role/route label, and independently approves use of a postwar identity photograph as a source-placeholder. Do not label a 1946–1949 image a 1936 portrait, and do not infer a Bali-wide kingship from the Ubud Punggawa record.

### Role-valid but image-blocked: Tjokorda Gde Agung Sukawati

The Indonesian biography identifies Tjokorda Gde Agung Sukawati (1910–1978) as Raja Ubud and records his 1936 Pita Maha founding role with his brother, Walter Spies, Rudolf Bonnet, and I Gusti Nyoman Lempad. This is a stronger 1936 institutional connection than the postwar sources above, but the checked archival/Commons search produced no attributable, rights-cleared portrait image tied to him. A modern or unlabeled image cannot be substituted.

- Research source: [Tjokorda Gde Agung Sukawati, Indonesian Wikipedia](https://id.wikipedia.org/wiki/Tjokorda_Gde_Agung_Sukawati).
- Status: **source gap / blocked** until an archival portrait with a source page, date or date range, creator/archive, and license or public-domain rationale is found.

### Excluded from the 1936 opening leader

- Ide/Ida Anak Agung Gde Agung (1921–1999) is documented as Raja of Gianyar only from 1943, after his father Anak Agung Ngurah Agung. He was alive in 1936 but was not the period incumbent at the opening date; available Commons images checked were postwar or later. Do not backdate him to 1936.
- Anak Agung Ngurah Agung is identified as the preceding Raja of Gianyar, but no attributable, rights-cleared portrait was found in the checked source search. Do not use a descendant's image or a generic Balinese royal portrait as a substitute.
- No council, court, temple, sacred emblem, or generic “Bali regency” portrait was accepted. Institutional imagery without a named, period-specific source would fail the identity and ownership gate.

## Ownership and consumer checks

The repository search covered `Tjokorda`, `Cokorda`, `Sukawati`, `Soekawati`, `Raka`, `Ngurah Agung`, `Gianyar`, `Ubud`, `Pita Maha`, and related transliterations across `common/characters/`, `history/countries/`, `gfx/`, `interface/`, `localisation/`, and Event 006 docs. No Chaos Redux character or portrait token for these subjects was found.

Installed vanilla references inspected:

- `common/characters/INS.txt`: `INS_dewa_geg` uses `GFX_portrait_INS_dewa_geg` and `GFX_portrait_INS_dewa_geg_small`, with despotism/country-leader and Indonesian political-advisor roles.
- `history/countries/BLI - Bali.txt`: capital state `1052`, two research slots, and `recruit_character = INS_dewa_geg`.
- `history/countries/INS - Indonesia.txt`: `BLI` remains in `INS_releasables`.
- `common/scripted_effects/INS_scripted_effects.txt`: `indonesia_transfer_BLI` transfers `INS_dewa_geg` when BLI exists and has a fallback search when it does not.
- Vanilla runtime source exists at `gfx/leaders/INS/portrait_INS_dewa_geg.dds`; it is not copied or replaced.

Matching role references inspected before any production: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/` and its `contact_sheet.png`; all displayed leader references are native `156x210` HOI4 leader portraits. No reference image was used as a face source.

## Required next gate if the parent reopens the package

1. Parent must choose an exact route label and role: e.g. named Ubud claimant/regency, named Gianyar regency, or a sourced council institution. “Bali king” or “Balinese council” is insufficient.
2. Obtain an archival portrait source with exact subject attribution, source/archive identifier, date or date range, creator, and license/public-domain rationale. A later identity photograph may be considered only with explicit parent approval; it must not be described as contemporaneous with 1936.
3. Run the portrait worker's unchanged-source pipeline under `docs/assets/portraits/006_iw155_bali/` only after acceptance: original bytes, exact lossless crop and JSON equality evidence, deterministic `156x210` candidate, provenance contract, independent identity/framing/provenance review, DDS conversion with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, and a portrait-specific `.gfx` handoff.
4. Preserve `INS_dewa_geg` and `indonesia_transfer_BLI` unless the parent accepts a separate origin-gated character-transfer contract. No source archive may be a runtime path.

## Checks and blockers

- Required offline Paradox Wiki pages were consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Required installed vanilla documentation was consulted under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including effects, triggers, modifiers, script concepts, dynamic variables, and localisation-related references.
- Matching installed-vanilla leader portrait contact sheet and catalog shelf were inspected.
- No RunPod or provider workflow was opened, queued, configured, or monitored.
- No DDS conversion, crop, resize, independent visual audit, `.gfx` registration, or runtime wiring was attempted because the source/role gate did not pass.
- HOI4 MCP engine evidence is not claimed for this portrait-only research task; the existing IW-155 compatibility audit records the separate `ARTIFACT_MANIFEST_INVALID` workspace blocker for its map/event/probability calls.

**Final state:** `IW-155 BLI` remains fail-closed. Preserve vanilla `INS_dewa_geg` as the current consumer. No portrait package is ready for installation.
