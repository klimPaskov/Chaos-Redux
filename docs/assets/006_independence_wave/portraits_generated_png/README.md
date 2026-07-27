# Event 006 pre-DDS portrait PNG reference shelf

This folder is the central, reference-only shelf for source-based Independence Wave portraits after HOI4-style processing and before runtime wiring. It preserves both the larger repaint masters and the normalized PNGs used for DDS conversion.

## Scope

The shelf contains 132 byte-copied PNGs:

- 49 larger source-locked HOI4 repaint masters in `pre_resize_source_repaints/`, copied from the ImageGen output before deterministic resizing and DDS conversion. Their dimensions remain the native generation dimensions and are recorded in [PRE_RESIZE_MANIFEST.md](PRE_RESIZE_MANIFEST.md). This includes the two protected BAY Rupprecht and RHI Matthes source repaints and the withdrawn IW-093 Prempeh II master.
- 83 normalized PNGs at the native HOI4 large-portrait size of 156x210:

- 44 source-refinish attempts from the dated `sourced_portrait_refinishes_*` packages.
- 3 grounded source-replacement outputs from the `sourced_portrait_replacements_*` packages.
- 27 archival source treatments from `sourced_portrait_treatments_2026_07_22`, retained because they are useful provenance even though that package's visual gate rejected the photographic finish.
- 2 protected approved portraits (BAY Rupprecht and RHI Matthes), copied unchanged.
- 2 withdrawn historical source attempts for IW-093 Asante.
- 1 IW-093 Asante source-locked repaint candidate retained pending the independent likeness/style/provenance gate.
- 1 IW-018 Sardinia Vittorio Vernè source-locked commander repaint candidate retained pending rights, role, and independent likeness/style/provenance gates.
- 1 IW-018 Sardinia Pietro Pinna Parpaglia source-locked crown-route repaint candidate retained pending role, ownership, and independent likeness/style/provenance gates.
- 1 IW-173 Hawai'i Samuel Wilder King source-locked territorial-delegate repaint candidate retained pending independent likeness/style/provenance gates and the package's no-leader-replacement contract.
- 1 IW-177 Fiji Ratu Sir Lala Sukuna source-locked constitutional-statesman repaint candidate retained pending the circa-1940s date decision and independent likeness/style/provenance gates.

Purely generated fictional or institutional portrait packages, raw source photographs, exact source crops, review sheets, contact sheets, DDS files, advisor icons, dossier/small derivatives, and runtime-only decoded DDS previews are intentionally excluded.

## Status and provenance

The subfolders are an evidence boundary, not an automatic runtime approval:

- `approved_or_protected/` contains the current audited AGX trial-02 PNGs and the two protected portraits.
- `source_candidates/` contains sourced refinishes, replacement attempts, and the rejected-style treatment ledger.
- `historical_withdrawn/` contains source-based attempts withdrawn from runtime.

Use [PRE_RESIZE_MANIFEST.md](PRE_RESIZE_MANIFEST.md) for the larger repaint-master provenance and [MANIFEST.md](MANIFEST.md) for the exact original path, SHA-256, dimensions, package kind, and status of every normalized copy. The IW-093 candidate's source/crop/repaint/processor evidence remains under `../iw093_iw098_asset_clearance_2026_07_26/`; its candidate status is not runtime admission. The original package manifests, source masters, crops, prompts, clearance notes, and independent audits remain authoritative for rights, identity, and admission decisions.

When creating another grounded portrait, follow the asset skill's pipeline: attributed archival male source, explicit head-and-shoulders crop, identity-preserving HOI4-style repaint, deterministic 156x210 processing, independent likeness/style/provenance audit, then DDS conversion and wiring. Do not treat a candidate in this shelf as a license to skip those gates.

This shelf has no runtime references and does not authorize advisor or dossier portrait derivatives.
