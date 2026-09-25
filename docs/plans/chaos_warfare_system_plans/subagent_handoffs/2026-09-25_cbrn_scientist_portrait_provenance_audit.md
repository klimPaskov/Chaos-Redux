# CBRN Scientist Portrait Provenance Audit

Date: 2026-09-25.

Status: read-only audit complete; per-person portrait provenance remains unresolved because the documented source archives are unavailable in the current workspace.

## Runtime crosswalk

The audit parsed 55 unique IDs in `common/characters/cbrn_historical_scientists.txt` and 12 unique IDs in `common/characters/cbrn_historical_specialists.txt`, for 67 distinct large scientist portraits.

All 67 character `army.large` references resolve through `interface/_scientists_portraits.gfx` to an existing `gfx/leaders/scientists/portrait_<ID>.dds` with a 156x210 DDS header.

All 12 dual-role specialist cards resolve through `interface/cbrn_historical_advisors.gfx` to an existing `gfx/interface/advisors/cbrn/<ID>.dds` with a 65x67 DDS header.

These checks establish runtime path and dimensions only; they do not establish portrait identity, style lineage, or source provenance from filenames.

The [runtime inventory](../../../assets/portraits/cbrn_scientist_runtime_inventory_2026-09-25.md) records every exact sprite path, DDS dimension, and SHA-256 hash reviewed here.

## Provenance gaps

The exact archive paths documented by `docs/systems/cbrn_warfare/cbrn_historical_scientists.md` are absent: `docs/assets/portraits/016_brilliant_scientist/manifest.md`, `input_mapping.json`, `research_sources.md`, and the `subjects/` directory.

The card evidence path cited by `docs/systems/cbrn_warfare/cbrn_historical_advisors.md`, `docs/assets/chaos_warfare_historical_advisors/v2_actual_workflow/`, was also unavailable on final path verification.

Consequently no current per-person record proves portrait-image attribution, rights status, original source bytes, lossless crop coordinates and equality, processed source-placeholder PNG, reviewer/date, or separate identity, framing, and provenance verdicts for any of the 67 large portraits.

The historical character documentation contains general research references, but those references do not identify and license each portrait image.

The 2026-08-14 handoff `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_scientist_portrait_install_2026-08-14.md` reports 66 unique user-supplied portrait finals, says `POL_franciszek_witaszek` remained unchanged, and notes that external redistribution rights for the supplied styled-final bytes were not provided. The current 67-ID runtime roster cannot be reconciled against that count or its claimed source packages because `input_mapping.json` and the archive are absent.

The 67 DDS files are present and wired, but the current evidence does not justify labeling them `source_placeholder` or `styled_final`, and no replacement state can be independently verified.

## CXT Test Director

The fictional `CXT_test_director` package is positively evidenced by `docs/assets/portraits/cxt_test_director/manifest.md`, its retained prompt and ImageGen output, processed portrait, 4x review, character reference, and `interface/chaosx_test_country_portrait.gfx` wiring.

The manifest records native ImageGen source mode `fictional_high_chaos`, a 1080x1456 source, 156x210 processed portrait, 624x840 review, and `gfx/leaders/CXT/leader_cxt_test_director.dds` at 156x210 with SHA-256 `2cd774af2a1119a4742b61141f4edd6c73222c7b6bf8610b324bf3313d53dc7a`.

The manifest reports source, native-size, and 4x review passes; live-game presentation remains user-owned. Grounded-source research and RunPod do not apply to this fictional portrait.

## Scope and remaining work

No portraits, source packages, manifests, or GFX/character changes were produced by this audit.

No RunPod session, Hearts of Iron IV session, or per-person web source research was performed.

Remediation requires restoring the documented 016 per-person archives and source mapping, reconciling the 66-supplied-versus-67-runtime count, and verifying portrait rights and source-placeholder or styled-final status before any completion claim.
