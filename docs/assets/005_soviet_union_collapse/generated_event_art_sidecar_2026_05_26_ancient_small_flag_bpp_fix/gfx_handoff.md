# Event 005 Ancient Small Flag BPP Fix Handoff

This sidecar corrected only HOI4 country flag TGA outputs. No `.gfx` sprite definitions are needed for country flags.

Final paths:

- `gfx/flags/small/KZR.tga`
- `gfx/flags/small/KZR_communism.tga`
- `gfx/flags/small/KZR_democratic.tga`
- `gfx/flags/small/KZR_fascism.tga`
- `gfx/flags/small/KZR_neutrality.tga`
- `gfx/flags/small/SOG.tga`
- `gfx/flags/small/SOG_communism.tga`
- `gfx/flags/small/SOG_democratic.tga`
- `gfx/flags/small/SOG_fascism.tga`
- `gfx/flags/small/SOG_neutrality.tga`
- `gfx/flags/small/KHW.tga`
- `gfx/flags/small/KHW_communism.tga`
- `gfx/flags/small/KHW_democratic.tga`
- `gfx/flags/small/KHW_fascism.tga`
- `gfx/flags/small/KHW_neutrality.tga`
- `gfx/flags/small/ALN.tga`
- `gfx/flags/small/ALN_communism.tga`
- `gfx/flags/small/ALN_democratic.tga`
- `gfx/flags/small/ALN_fascism.tga`
- `gfx/flags/small/ALN_neutrality.tga`

Proposed sprite name: not applicable.

Suggested `.gfx` file: not applicable.

Use notes: the files are small country flags for the custom ancient-restoration Event 005 tags `KZR`, `SOG`, `KHW`, and `ALN`. They were rebuilt from the current normal-size flag art and exported as `10x7`, 32 bpp, bottom-origin TGAs. Normal and medium flags were not changed, and no vanilla-supported existing-country base flags were created or edited.

Validation: `notes/tga_header_audit.tsv` confirms all 20 final small TGAs are `10x7`, 32 bpp, bottom-origin, descriptor `0x08`.
