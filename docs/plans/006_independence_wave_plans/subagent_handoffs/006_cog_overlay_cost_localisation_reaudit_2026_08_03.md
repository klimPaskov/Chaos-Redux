# Event 006 COG overlay cost localisation re-audit

Date: 2026-08-03

Scope: source-only re-audit of `localisation/english/006_independence_wave_iw101_iw102_iw105_cog_overlays_l_english.yml` after the twelve COG overlay cost displays were changed from repeated literals to script-constant references. The obsolete pasted flag log was excluded.

## Verdict

**PASS for the requested tuning-drift repair, with one pre-existing icon-token risk left for the owning agent.** The twelve cost strings use valid dynamic variable syntax, resolve to the central COG overlay cost schema, and remain aligned with the decision consumers. No gameplay or localisation source was patched by this re-audit, and no runtime/UI/save-load claim is made.

## Required audit output

### Missing keys

- None among the four declared `custom_cost_text` families: cabinet, depot, force, and charter each have the base key plus `_blocked` and `_tooltip` variants.
- The guard cost has no localisation key because the three guard entries are missions without `custom_cost_text`; guard payment is performed by the start-guard effect before mission activation. This is an explicit display opportunity, not a missing consumer key for the repaired twelve-key family.

### Duplicate keys

- None within the target file: 90 parsed keys, 90 unique.
- None across `localisation/**/*.yml` for the twelve exact COG cost keys; each occurs once in the target file.

### Scripted-localisation issues

- None found. These are ordinary localisation values, not `defined_text` calls, and contain no unresolved scripted-localisation namespace/function reference.
- `[?constant:independence_wave_iw_cog_overlay_cost.<field>|0]` is valid variable display syntax. The offline Localisation page documents `[?var|format]`; the vanilla `script_concept_documentation.md` states that scoped variables accept `constant:` fixed-point values, and vanilla localisation contains the same `[?constant:category.key]` form.

### Dynamic-text opportunities

- The four mission-style guard actions consume `guard_*` constants and pay those values in effects, but have no cost display. If a later UI pass wants to expose that payment before activation, add a guard `custom_cost_text`/`_blocked`/`_tooltip` family and wire it in the decision source; this is outside the requested repair.
- The twelve repaired strings already derive displayed amounts from `common/script_constants/006_independence_wave_iw101_iw102_iw105_cog_overlays_constants.txt`, so no further dynamic amount interpolation is required for these decision costs.

### Cross-surface mismatch notes

- `common/decisions/006_independence_wave_iw101_iw102_iw105_cog_overlays_decisions.txt` declares `custom_cost_text = independence_wave_iw_cog_{cabinet,depot,force,charter}_cost` for the nine non-mission actions. Per the offline Decision Modding page, the engine derives `_blocked` and `_tooltip`; all twelve keys are present.
- Constant fields match the affordability triggers and payment effects: cabinet (12 command power, 1500 manpower, 3 trains), depot (16, 2600, 5 trains, 70 support), force (18, 3500, 18 Army Experience, 420 infantry), and charter (5200 manpower, 26 Army Experience, 760 infantry, 150 support). No literal amount remains in the twelve cost strings; `|0` is only the display precision formatter.
- No `cog_cog` key or token appears in the target source or the scanned Event 006 COG surfaces.
- Pre-existing icon-token risk: the target uses bare `£train_equipment`, `£support_equipment`, and `£infantry_equipment`. Vanilla and nearby Chaos Redux cost localisations normally use `£GFX_train_texticon`, `£support_equipment_text_icon`, and `£infantry_equipment_text_icon`; the target's bare forms are not defined as matching text-icon sprite names in the inspected vanilla/repo interface files. This was not changed because the request is limited to constant-reference repair; the owning agent should decide whether to normalize these tokens in a separate, explicit UI/localisation pass.

### File encoding concerns

- Target begins with UTF-8 BOM bytes `EF BB BF` and has the required `l_english:` header.
- Values are single-line quoted strings; line endings are LF in the working copy. No encoding issue was found.

## Recommended follow-up

1. Keep the twelve dynamic constant references as-is; they are source-aligned and remove the prior literal-cost drift.
2. In a separately scoped UI/localisation pass, confirm or normalize the three bare equipment icon tokens noted above and decide whether guard mission costs should receive player-facing cost text.
3. Do not use the obsolete pasted flag log as evidence for this repair.

## Validation performed

- Parsed target localisation keys and checked exact global occurrences across `localisation/**/*.yml`.
- Compared the twelve constant-field references with the COG constants schema and inspected all `custom_cost_text` consumers, affordability triggers, and payment effects.
- Checked target bytes for UTF-8 BOM and searched target/Event 006 COG surfaces for stale `cog_cog` or literal cost drift.

Skipped: live game, UI render, save/load, and runtime localisation validation; those belong to the parent/user and were not available to this source-only audit.
