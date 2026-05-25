# Event 005 Generated-Art First Batch Manifest

Event id: `005`

Event slug: `soviet_collapse`

Package date: 2026-05-25

Scope: generated-art sidecar audit for fictional/council leader portraits and fictional, alternate-history, route, or ideology flags. This pass creates review evidence and handoff notes only. It does not edit `.gfx`, localisation, GUI, event, focus, idea, decision, scripted effect, scripted trigger, on_action, history, country, spreadsheet, or active gameplay asset files.

## References Inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- `.agents/skills/chaos-redux-event-assets/assets/news_event_images/`
- `.agents/skills/chaos-redux-event-assets/assets/report_event_images/`
- `.agents/skills/chaos-redux-event-assets/assets/super_event_images/`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_7_assets_achievements_validation.md`
- `common/country_tags/chaosx_countries.txt`
- `history/countries/* - *.txt` for active Event 005 custom successor leader references
- `gfx/leaders/005_soviet_collapse/`
- `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`
- `docs/assets/005_soviet_union_collapse/manifest.md`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_25_current_review/`
- Offline Paradox wiki core pages required by `AGENTS.md`
- Vanilla documentation under `/home/klim/projects/Hearts of Iron IV/documentation/`

## Asset Decision

No `$imagegen` call was made in this first batch. The active Event 005 country files already reference council or symbolic leaders, and final `156x210` DDS files exist for the active custom successor scope audited here. The active custom and route flag files also exist at normal, medium, and small sizes.

The only deterministic issue found is not missing generated artwork. It is a TGA export-format issue on 50 active small flags that are already dirty in the worktree. Re-exporting them in place would overwrite unrelated active work, so this sidecar records the exact priority list and blocks active replacement until the parent asset owner allows that overwrite or asks for an isolated replacement package.

## Portrait Scope

Target size: `156x210` DDS.

Final folder checked: `gfx/leaders/005_soviet_collapse/`.

Audit file: `validation/leader_portrait_audit.tsv`.

Contact sheet: `contact_sheets/active_council_leaders.png`.

Status: `complete_existing`.

Checked active council or symbolic leader portraits:

`CFR`, `MFR`, `KRS`, `FTH`, `BBH`, `BSC`, `TNC`, `ALA`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`, `OGB`, `KZR`, `SOG`, `KHW`, `ALN`, `RMC`, `DSC`, `NRF`, `PRA`, `TSC`, and `ICD`.

No missing DDS or wrong-size portrait was found in this scoped batch.

## Flag Scope

Target sizes:

- normal: `82x52`
- medium: `41x26`
- small: `10x7`

Audit file: `validation/flag_format_audit.tsv`.

Normal flag contact sheet: `contact_sheets/active_custom_flags_normal.png`.

Problem small-flag contact sheet: `contact_sheets/problem_small_flags_current.png`.

Existing vanilla-supported no-suffix base flags remain out of scope and were not created or overwritten. This includes `UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`, `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN`. The explicit route/cosmetic flag target `UKR_BLACK_BANNER` is in scope because it is not a default `UKR` override.

Historical-restoration tags `OGB`, `KZR`, `SOG`, `KHW`, and `ALN` are not treated as purely fictional generated flags when new art is needed. If their visible designs need replacement rather than only re-export, route that work to source-research/historically grounded asset handling instead of fictional generation.

## Prioritized Asset Work

### Priority 1: Re-export Active Dirty Small Flags

Status: `blocked`.

Reason: active files are dirty before this sidecar, and overwriting them would risk clobbering unrelated asset work.

Exact files: `validation/problem_small_flags.txt`.

Affected tag families:

- `CFR`
- `KRS`
- `UDC`
- `SDZ`
- `KZR`
- `SOG`
- `KHW`
- `ALN`
- `RMC`
- `TSC`

Each family includes base, `_communism`, `_democratic`, `_fascism`, and `_neutrality`, for 50 total small flags.

Required final format if promoted: `10x7` 32bpp true-color TGA with descriptor byte `0x08`, matching vanilla small flag pattern. Current problem files are `10x7` 8-bit color-mapped TGAs with descriptor byte `0x00`.

Orientation confirmation: normal and medium files for these families are `82x52` and `41x26` with descriptor `0x08`; the small flag contact sheet decodes visibly upright in this environment, but the export format does not match the vanilla-compatible pattern. Re-export should preserve current visible orientation and artwork.

### Priority 2: No New Fictional/Council Portrait Generation

Status: `not_needed`.

The active Event 005 custom successor/council portrait surface already has final DDS files at the required size. If the parent later rejects visual quality for a specific portrait, regenerate that single portrait as a targeted replacement with a new source PNG, processed PNG, final DDS, prompt, and handoff row.

### Priority 3: No New Fictional Flag Concept Generation

Status: `not_needed`.

The active custom and cosmetic flag families audited here are present. If the parent later rejects visible design quality for a specific fictional tag, regenerate that one tag family as a full normal/medium/small package. Do not create default no-suffix flags for existing vanilla-supported countries.

## Files Created

- `manifest.md`
- `gfx_handoff.md`
- `contact_sheets/active_council_leaders.png`
- `contact_sheets/active_custom_flags_normal.png`
- `contact_sheets/problem_small_flags_current.png`
- `validation/contact_sheet_identify.txt`
- `validation/flag_format_audit.tsv`
- `validation/leader_contact_inputs.txt`
- `validation/leader_portrait_audit.tsv`
- `validation/normal_flag_contact_inputs.txt`
- `validation/problem_small_flags.txt`

## Blockers And Simplifications

- Blocker: active small flag replacement is blocked because the affected `gfx/flags/**` files are already dirty from other work.
- Simplification: no source PNG, processed PNG, final DDS, or final TGA replacements were generated in this first batch. The audit found no missing generated-art concept; it only found the small-flag export-format issue.
- Uncertainty: this pass did not visually judge every flag design as final-quality art. It confirms presence, dimensions, format status, dirty-file risk, and preservation rules.
