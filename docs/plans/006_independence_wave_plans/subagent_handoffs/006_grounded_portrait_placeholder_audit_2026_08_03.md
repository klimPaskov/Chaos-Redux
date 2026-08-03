# Event 006 grounded portrait source-placeholder audit

Date: 2026-08-03.

Scope: read-only audit of the 15 promoted grounded portrait source placeholders, their durable source masters, crop metadata, processed PNGs, and runtime DDS files. No `.gfx`, character, event, country, localisation, gameplay, or runtime wiring was edited. No portrait was generated, repainted, recoloured, retouched, or styled.

## Audit result

All 15 source-to-crop records are independently reproducible `exact_source_crop_verified` records. For every row, the master and crop file hashes match the JSON, the Pillow-decoded master crop equals the emitted crop, the processed candidate is RGB `156x210`, and the runtime DDS decodes pixel-identically to that candidate. Every DDS is the repository-valid one-level uncompressed BGRA layout: `156x210`, `131168` bytes, 32-bit masks, opaque alpha, and no mipmaps.

The crosswalk is mechanically complete. The current handoff only stores hash prefixes and does not carry the full source/provenance ledger, processing metadata, or a current contact sheet. Those are documentation gaps, not byte-chain failures.

## Per-row crosswalk and disposition

`PASS` means the current source-placeholder byte chain and the retained identity/provenance evidence are sufficient for this tranche. `NEEDS_REVIEW` means the bytes are intact but the current source admission or identity/rights record must be resolved before treating the row as fully cleared. Runtime names are exact paths under `gfx/leaders/006_independence_wave/`.

| Verdict | Identity / role | Durable source master | Current processed candidate | Runtime DDS |
| --- | --- | --- | --- | --- |
| PASS | ARX Emilio Lussu | `portrait_ARX_independence_wave_emilio_lussu_source.jpg` | `portrait_ARX_independence_wave_emilio_lussu.png` | `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_emilio_lussu.dds` |
| PASS | ARX Luigi Arborio Mella Sant'Elia | `portrait_ARX_luigi_mella_santelia_source.gif` | `portrait_ARX_luigi_mella_santelia.png` | `gfx/leaders/006_independence_wave/portrait_ARX_luigi_mella_santelia.dds` |
| PASS | ARX Vittorio Vernè | `portrait_ARX_vittorio_verne_source.jpg` | `portrait_ARX_vittorio_verne.png` | `gfx/leaders/006_independence_wave/portrait_ARX_vittorio_verne.dds` |
| PASS | ASX Luigi Rizzo | `portrait_ASX_luigi_rizzo_source.jpg` | `portrait_ASX_luigi_rizzo.png` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_luigi_rizzo.dds` |
| PASS | ASX Luigi Sturzo | `portrait_ASX_luigi_sturzo_source.jpeg` | `portrait_ASX_luigi_sturzo.png` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_luigi_sturzo.dds` |
| PASS | ASX Pietro Lanza di Scalea | `portrait_ASX_pietro_lanza_di_scalea_source.jpg` | `portrait_ASX_pietro_lanza_di_scalea.png` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_pietro_lanza_di_scalea.dds` |
| PASS | ASX Vincenzo Di Benedetto | `portrait_ASX_vincenzo_di_benedetto_source.gif` | `portrait_ASX_vincenzo_di_benedetto.png` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_vincenzo_di_benedetto.dds` |
| PASS | BAY Rupprecht of Bavaria | `portrait_BAY_rupprecht_of_bavaria_source.jpg` | `portrait_BAY_rupprecht_of_bavaria.png` | `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds` |
| PASS | COR Adolphe Landry | `portrait_COR_adolphe_landry_source.jpg` | `portrait_COR_adolphe_landry.png` | `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_adolphe_landry.dds` |
| PASS | COR Jean Chiappe | `portrait_COR_jean_chiappe_source.jpg` | `portrait_COR_jean_chiappe.png` | `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_jean_chiappe.dds` |
| PASS (source placeholder only) | DOX Nana Otumfuo Agyeman Prempeh II | `portrait_DOX_prempeh_ii_source.jpg` | `portrait_DOX_prempeh_ii.png` | `gfx/leaders/006_independence_wave/portrait_DOX_prempeh_ii.dds` |
| PASS | RHI Josef Friedrich Matthes | `portrait_RHI_josef_friedrich_matthes_source.jpg` | `portrait_RHI_josef_friedrich_matthes.png` | `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds` |
| NEEDS_REVIEW | SOK Muhammadu Dikko | `portrait_SOK_muhammad_dikko_source.jpg` | `portrait_SOK_muhammad_dikko.png` | `gfx/leaders/006_independence_wave/portrait_SOK_muhammad_dikko.dds` |
| PASS | WLS George Cornwallis West, mountain commandant role | `portrait_WLS_george_cornwallis_west_source.jpg` | `portrait_WLS_george_cornwallis_west.png` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` |
| PASS | WLS J.H. Thomas, national council role | `portrait_WLS_j_h_thomas_source.jpg` | `portrait_WLS_j_h_thomas.png` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` |

### Identity and provenance notes

- ARX Emilio Lussu remains supported by the Senate source ledger, CC BY 3.0 IT, and the pre-1958 source record.
- ARX Mella is the Luigi Arborio Mella di Sant'Elia source. Keep that identity in the source ledger and retire any old `Vittorio Pala` wording; the current source bytes themselves are correct.
- ARX Vernè is the Commons 1930s source with the recorded public-domain rationale. His Sardinia connection is a role/route link, not a claim that he was Sardinian-born.
- ASX Rizzo, Sturzo, Lanza, and Di Benedetto retain the earlier source-ledger evidence (Commons/Senate/Albert Kahn/Mario Nunes Vais records and the documented fictional or retired-role adaptations). The candidate-to-runtime stem changes are explicit aliases, not missing files.
- BAY Rupprecht retains the Franz Grainer circa-1916 PD-Art/source-country evidence. The current DDS is a new source placeholder and must not be described as the older painted output.
- COR Landry and Chiappe retain the Gallica/Agence Meurisse 1917 and 1927 public-domain evidence and the Corsican-born role fit.
- DOX Prempeh II has strong TNA CO 1069/44/12, 31 January 1935, OGL v1.0 provenance. The current row is admitted only as an unchanged source placeholder; the previously rejected/gated repaint remains unavailable and must not be implied by this PASS.
- RHI Matthes retains the LOC Bain News Service, 22 November 1923, no-known-restrictions source record and the separatist/republic route lock. The current DDS supersedes, rather than proves, the older painted byte hash.
- SOK Dikko is mechanically complete, but v51 source research still records the TNA album pages as early/era-sensitive and the 1921 Commons reproduction as having an unresolved underlying rights chain. Keep this row `NEEDS_REVIEW` until the exact current source URL, rights basis, and era-fit admission are written into the source ledger; do not call it a cleared styled portrait.
- WLS Cornwallis West retains the Henry Walter Barnett circa-1900–1910 PD-Art caution and Welsh-born Scots Guards role evidence. The mountain-commandant label is a route adaptation, not a claim of a specialist historical Welsh mountain command.
- WLS J.H. Thomas retains the Bain/LOC `ggbain.29625`, circa-1920, public-domain source and Welsh civic-leader role evidence.

## Previously attested package evidence

No source evidence was lost for the six previously attested package families ARX, ASX, BAY, COR, RHI, and WLS. Their source masters, exact-crop JSONs, processed candidates, current DDS files, and prior identity/provenance audits remain present. The old styled-output approvals and hashes are historical evidence only; they do not describe the current source-placeholder bytes.

## Normalization required before final source-package promotion

1. Add a durable per-row manifest (or extend the current handoff) with the full SHA-256 for source master, crop, processed PNG, and DDS, plus source URL/archive id, author/date, licence or rights basis, era fit, role adaptation, ownership guard, and the exact candidate-to-runtime alias.
2. Keep the temporary candidate stems and runtime stems as an explicit mapping. ASX candidates use subject stems while runtime files use `independence_wave` role stems; COR and WLS do the same. This is intentional but currently undocumented outside the table above.
3. Do not use the durable archive PNGs as current source-placeholder evidence without replacement or relabelling. The archive currently mixes old 156x210 RGBA painted files (ARX Emilio/Mella/Vernè, BAY, COR Landry/Chiappe, RHI), exact crop copies (ASX Rizzo/Sturzo/Lanza, SOK Dikko, WLS J.H. Thomas), and non-crop or stale files (ASX Di Benedetto, DOX Prempeh II, WLS Cornwallis West). The authoritative current candidates are the 15 files under `docs/assets/006_independence_wave/source_placeholder_2026_08_03/processed_png/` and the DDS crosswalk above.
4. The 15 durable archive `.txt` files still contain generic `hoi4_portrait` repaint prompts. They conflict with the source-placeholder policy and must be marked superseded, moved to the old styled-evidence workspace, or replaced by source/provenance notes before calling the durable package self-describing. Do not claim those prompts describe the current runtime.
5. Normalize status wording to `source_placeholder`, matching `SOURCE_PLACEHOLDER_POLICY.md`. The older `historical_source_placeholder` label may remain as an alias in historical notes but should not be the current disposition value.
6. Generate a current contact sheet and record the deterministic resize method if the parent wants a visually reviewable promotion packet. No visual identity failure was found in this byte audit, but a byte audit is not an independent human likeness review.

## Audited evidence paths

- Durable sources: `docs/assets/portraits/006_independence_wave/`.
- Current crop metadata and crops: `docs/assets/006_independence_wave/source_placeholder_2026_08_03/crops/` and `metadata/`.
- Current processed candidates: `docs/assets/006_independence_wave/source_placeholder_2026_08_03/processed_png/`.
- Runtime DDS: `gfx/leaders/006_independence_wave/`.
- Source-placeholder policy: `docs/assets/portraits/006_independence_wave/SOURCE_PLACEHOLDER_POLICY.md`.
- Existing conversion handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_historical_portrait_source_placeholder_2026_08_03.md`.
- Canonical vanilla references: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`.

Conclusion: the 15 current source-to-crop-to-PNG-to-DDS chains are intact. Twelve rows are clear for source-placeholder use on retained provenance, DOX is clear only as an unchanged source placeholder, and SOK Dikko remains `NEEDS_REVIEW` for rights/era admission. The principal remaining work is manifest/alias normalization and removing the stale styled-prompt ambiguity from the durable archive; no gameplay or GFX change is required for this audit.
