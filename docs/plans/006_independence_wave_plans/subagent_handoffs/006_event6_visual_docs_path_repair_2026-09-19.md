# Event 006 visual documentation path repair, 2026-09-19

## Scope and source-of-truth map

This bounded pass reconciles current Event 006 visual-asset documentation only. It does not change source design, gameplay, GFX, image files, animation, portraits, flags, or dated handoffs. The parent retains final integration and review, and this pass makes no gameplay-completion claim.

| Surface | Current source evidence | Documentation disposition |
| --- | --- | --- |
| Package-local small non-portrait sprites | `interface/006_independence_wave_small_assets.gfx` retains package source markers and the live definitions. | Current ownership claims point to the consolidated registry. Removed package-local filenames remain historical provenance only. |
| IW-093/IW-098 focus sprites | `interface/006_independence_wave_iw093_iw098_focus.gfx` remains live for 35 focus base and 35 shine sprites. | The package doc and icon manifest distinguish this live focus registry from the 22 small-asset base sprites in the consolidated registry. |
| Shared Event 006 idea/decision icons and animation aliases | `interface/006_independence_wave.gfx` contains the shared icons and four `frameAnimatedSpriteType` aliases with `play_on_show = yes`. | The Iceland reuse manifest points to the shared registry. The overview no longer reports a current `play_on_show` mismatch. |
| Formable emblems | `interface/006_independence_wave_small_assets.gfx` registers `GFX_independence_wave_formable_form_05` and `GFX_independence_wave_formable_form_48`. | ASSET-046 stays blocked for broader coverage, without claiming that every emblem is absent or that FORM-48 is reachable. |
| Portraits | `interface/006_independence_wave_portraits_registry.gfx` remains separate. | Portrait documentation was outside this non-portrait ownership repair and was left unchanged. |

## Files changed and exact claims reconciled

- `docs/events/006_independence_wave/overview.md`: removed the stale animation `play_on_show` mismatch from current open findings, recorded four `yes` aliases and the still-open dynamic GUI visibility/click-region gate, and qualified incomplete ASSET-046 coverage against the two registered emblems.
- `docs/events/006_independence_wave/systems/iw093_iw098_signature_packages.md`: replaced the removed four-file wildcard claim with the live focus registry plus consolidated decision/category/idea registry split.
- `docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md`: kept ASSET-046 `blocked` while naming registered FORM-05 and FORM-48 emblems, broader missing coverage, and FORM-48 reachability gating.
- `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/manifest.md`: changed the current Wallonia/Frisia registration claim from the removed package file to the consolidated source block.
- `docs/assets/006_independence_wave/iw012_ice_package_2026_07_28/manifest.md`: changed the reused shared idea/decision icon owner from removed `custom_icons.gfx` to `interface/006_independence_wave.gfx`.
- `docs/assets/006_independence_wave/iw043_iw058_focus_icons_2026_07_18/manifest.md`: replaced the obsolete suggested package-local focus registry as a current target with the consolidated IW-043/IW-058 source block, preserving the old suggestion only as historical production direction.
- `docs/assets/006_independence_wave/iw093_iw098_icons_2026_07_18/manifest.md`: added the live 35-focus/22-small split and replaced 22 category, decision, and idea row-level suggestions with the current consolidated owner. The remaining focus-row path is live and unchanged.
- `docs/assets/006_independence_wave/pacific_focus_icons_2026_07_18/manifest.md`: changed current Pacific focus registration from the removed package-local file to the consolidated Pacific source block.
- `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/manifest.md`: changed the current registration-owner summary and 26 row-level owning-file fields from the removed Rhineland/Bavaria file to the consolidated source block.
- This handoff records the bounded repair. The six `docs/assets/` manifests are ignored by `.gitignore:80` and do not appear in ordinary `git diff`; the parent must decide whether to force-add them when committing. Nothing was staged or committed here.

## Dispositions, contradictions, and scope limits

| Item | Disposition and basis |
| --- | --- |
| Removed package-local GFX references in current ownership prose | Superseded by the exact live registry named above. Historical source markers in `interface/006_independence_wave_small_assets.gfx`, dated handoffs, and original asset-production records were not rewritten. |
| ASSET-046 | Still `blocked` in the checklist. FORM-05 and FORM-48 sprite registration is implementation evidence for two emblems only, not an acceptance or completion claim for all formable identities or live FORM-48 reachability. |
| ASSET-039 animation/GUI gate | Still `needs_user_review`; source aliases specify `play_on_show = yes`, but this pass did not render or validate dynamic visibility, playback, or click regions. |
| Plans and historical handoffs | No plan disposition changed. Dated handoffs remain evidence, not current registry owners. |

No current-doc contradiction remains among the edited ownership claims. No documents were merged or deleted. No current prompt instruction was changed; the examined asset prompt requests a target GFX/GUI surface but does not assert a removed registry as current owner. The animation manifest already stated `play_on_show = yes` and was left unchanged. Deliberate Markdown structure was preserved; no unrelated hard-wrap cleanup was attempted in this bounded pass.

## Validation and remaining blockers

- Targeted `rg` found no remaining removed package-local registry claims or stale `play_on_show` mismatch in the searched current event, spec, super-event, and six edited manifest surfaces. Dated asset handoffs and provenance were intentionally excluded from replacement.
- Source inspection found both emblem aliases in `interface/006_independence_wave_small_assets.gfx`, 26 Rhineland/Bavaria manifest rows and 22 IW-093/IW-098 small-icon rows updated, and four live `play_on_show = yes` aliases in `interface/006_independence_wave.gfx`.
- Read-only `hoi4.focus_inspect` returned `FOCUS_INSPECTED` for `independence_wave_focus_tree` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b546904c208aa915c19344667d0783c8510d3607fc3ff53a95a0c2eb4e7edcc7/fe5ad88a7eb9fba286944dba5b97961438a1e1d028c81de5c772e9ea0ce373ce/focus-inspect.dde45306307dab08.json`. Its broad diagnostics include an unrelated vanilla focus syntax error; this pass did not re-audit focus gameplay.
- Read-only `hoi4.gui_inspect` returned `GUI_INSPECTED` for `independence_wave_status_window` under scenario `event006_visual_docs_registry_check`, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/38a5eabecb62230e6a8062df911c09abe440ed06b0679a1d6c4db0bd00ba17dd/55fce9d16ab9180cc612ba71d99231904c5ffbe30d4060f4f5e4cc36124e5561/gui-inspect.facd09be6bd67bac.json`. The inspector reports panel-overlap warnings; no render/compare or live consumer proof was in this docs-only assignment.
- No binary asset decoding, visual review, live-game test, broad asset coverage audit, or full plan/prompt disposition audit was run because this assignment only repaired current path/status wording.

Parent review should confirm the nine edited docs fit the ongoing visual-asset audit, decide whether the ignored manifests belong in the commit, and keep the unresolved ASSET-039, ASSET-046, FORM-48, and super-event 23 gates in the broader event report. No new emblem or fallback was introduced.
