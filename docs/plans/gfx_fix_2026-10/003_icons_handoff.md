# Event 003 static icon handoff

Disposition: implemented for the delegated static-asset scope. Parent-owned `.gfx` path wiring and final integration review remain pending. The parent accepted both fresh BoP icons on 2026-10-06 after reviewing their native and smooth 4x previews, and the accepted candidates have now been converted and round-trip validated.

The package contains 14 accepted final DDS outputs covering 15 source findings: the shared 34x34 dhyana seal; eight Buddha-power glyphs and one teaching glyph at 34x34; two dedicated 72x88 BoP icons; and the final-ledger and doctrine-balance category icons at 52x40. The two accepted BoP images are an aged lantern with blank letter and a book with bomb; both have 3px clear transparent margins. Their rejected focus-art crops remain in the archived rejected-candidate folders. Full prompts, ImageGen lineage, processed previews, runtime paths, hashes, contact sheets, and audit details are in `docs/assets/gfx_fix_holy_resume/manifest.md` and its linked evidence.

## Runtime outputs

The existing static `holy_realm_dhyana_seal.dds` path now contains the accepted 34x34 gold lotus and thin ring with transparent outer canvas and petal gaps. The parent's exact-consumer audit found no `.gui` consumer for the static alias and parent-owned decision edits route the five concentration decisions to that static sprite. The 1152x96 animation sheet remains unchanged.

The eight power DDS files and the teaching DDS keep their existing paths under `gfx/interface/decisions/003_holy_realm/powers/`. The final-ledger category keeps its path. The dedicated doctrine-balance category output is at `gfx/interface/decisions/003_holy_realm/decision_category_holy_doctrine_balance.dds`.

The accepted BoP files are `gfx/interface/decisions/003_holy_realm/bop/holy_realm_bop_vow_against_annihilation_side.dds` and `gfx/interface/decisions/003_holy_realm/bop/holy_realm_bop_final_silence_side.dds`. The previous crop candidates were archived before these accepted files replaced the reserved runtime paths. The original focus textures remain unchanged.

## Parent follow-up

The parent owns all `.gfx` and decision-file edits. Existing sprites `GFX_bop_THR_vow_against_annihilation_side` and `GFX_bop_THR_final_silence_side` should point to the dedicated BoP paths above. Existing `GFX_decision_category_holy_doctrine_balance` should point to the new doctrine-balance DDS. The parent already routed the five concentration decision rows to `GFX_decision_holy_realm_dhyana_seal`; the worker did not edit those decisions.

## Evidence and limits

All 14 runtime DDS outputs passed the standard converter, strict legacy BGRA8 header checks, target-size and file-length checks, nontrivial alpha checks, and pixel-identical round trips. See `docs/assets/gfx_fix_holy_resume/evidence/dds_roundtrip_audit.json`. The two old BoP crops have a separate audit and are recorded as rejected, not as final assets.

The all-assets review sheet is `docs/assets/gfx_fix_holy_resume/contact_sheets/003_static_icons_qa_contact_sheet.png`. Focused native, 4x, and round-trip BoP comparisons are in `docs/assets/gfx_fix_holy_resume/contact_sheets/003_bop_side_final_qa.png`; the three-background alpha sheet is `docs/assets/gfx_fix_holy_resume/contact_sheets/003_alpha_contrast_qa.png`.

No `.gfx`, GUI, gameplay, decision, localisation, event, animation, or spreadsheet source files were edited by this worker. No game was launched. The repository `.gitignore` excludes `docs/assets/`, so the parent should account for that if those evidence files need to be staged; runtime DDS assets and this plan handoff are outside that ignored folder.
