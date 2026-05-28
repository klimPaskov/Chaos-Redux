# Event 005 upside-down fictional flag fix

Date: 2026-05-28

Scope: vertically flip the existing upside-down fictional flag artwork in place, without redesign or regeneration, for the listed Event 005 flags and matching derived size variants.

Changed basenames:
`SZA`, `TNC`, `TSC`, `TSC_communism`, `TSC_democratic`, `TSC_fascism`, `TSC_neutrality`, `UDC`, `UDC_communism`, `UDC_democratic`, `UDC_fascism`, `UDC_neutrality`, `UKR_BLACK_BANNER`, `UWD`, `ARD`, `BAC`, `BBH`, `CFR`, `CFR_communism`, `CFR_democratic`, `CFR_fascism`, `CFR_neutrality`, `GAC`, `ICD`, `IUL`, `KHC`, `KRS`, `KRS_communism`, `KRS_democratic`, `KRS_fascism`, `KRS_neutrality`, `MFR_communism`, `MFR_democratic`, `MFR_fascism`, `MFR_neutrality`, `MRC`, `NLC`, `OGB_communism`, `OGB_fascism`, `OGB_neutrality`, `PRA`, `PRA_communism`, `PRA_democratic`, `PRA_fascism`, `PRA_neutrality`, `RMC`, `RMC_communism`, `RMC_democratic`, `RMC_fascism`, `RMC_neutrality`, `SDZ`, `SDZ_communism`, `SDZ_democratic`, `SDZ_fascism`, `SDZ_neutrality`, `SOG`, `SOG_communism`, `SOG_democratic`, `SOG_fascism`, `SOG_neutrality`

Changed files:
- `gfx/flags/<basename>.tga` for every basename above
- `gfx/flags/medium/<basename>.tga` for every basename above
- `gfx/flags/small/<basename>.tga` for every basename above

Total changed files: 180

Dimensions checked:
- `gfx/flags`: `82x52` on all 60 target files before and after the flip
- `gfx/flags/medium`: `41x26` on all 60 target files before and after the flip
- `gfx/flags/small`: `10x7` on all 60 target files before and after the flip

Validation:
- Used ImageMagick `convert <file> -flip` to apply a pure vertical flip in place via temporary replacement files
- Re-ran `identify -format "%m %wx%h"` on all 180 target files after processing
- Confirmed all target files remain `TGA` and kept their expected HOI4 flag dimensions
- No gameplay, localisation, `.gfx`, GUI, focus, decision, event, history, country, spreadsheet, or skill files were edited as part of this fix

Missing variants:
- None. Every listed basename had matching `gfx/flags/medium/` and `gfx/flags/small/` variants present and processed.

Notes:
- Other unrelated flag-file edits already exist in the worktree outside this basename set. They were left untouched.
