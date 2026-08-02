# Event 006 EEX-IAX flag handoff

This handoff is for the eighteen-tag flat flag chunk only. Flags use HOI4's engine filename lookup and do not require `.gfx` sprite definitions.

## Runtime triplets

For each tag, the following files are complete and bottom-left-origin uncompressed 32-bit TGA:

```text
gfx/flags/<TAG>.tga          # 82x52 normal
gfx/flags/medium/<TAG>.tga  # 41x26 medium
gfx/flags/small/<TAG>.tga   # 10x7 small
```

Tags in this handoff: `EEX EHX ERX ESX EWX FAX FBX FDX FLX FNX FOX FSX FUX FVX FXX GBX GCX IAX`.

No `.gfx` change is requested. Preserve existing tag and ideology lookup. These are base/no-suffix ladders only; no ideology variants were created.

## Copy-ready runtime path table

| Tag | Identity | Normal | Medium | Small | Sprite / lookup |
| --- | --- | --- | --- | --- | --- |
| `EEX` | Bunyoro | `gfx/flags/EEX.tga` | `gfx/flags/medium/EEX.tga` | `gfx/flags/small/EEX.tga` | engine country-tag lookup |
| `EHX` | Ankole | `gfx/flags/EHX.tga` | `gfx/flags/medium/EHX.tga` | `gfx/flags/small/EHX.tga` | engine country-tag lookup |
| `ERX` | Ndebele | `gfx/flags/ERX.tga` | `gfx/flags/medium/ERX.tga` | `gfx/flags/small/ERX.tga` | engine country-tag lookup |
| `ESX` | Xhosa | `gfx/flags/ESX.tga` | `gfx/flags/medium/ESX.tga` | `gfx/flags/small/ESX.tga` | engine country-tag lookup |
| `EWX` | Herero State | `gfx/flags/EWX.tga` | `gfx/flags/medium/EWX.tga` | `gfx/flags/small/EWX.tga` | engine country-tag lookup |
| `FAX` | Comoros | `gfx/flags/FAX.tga` | `gfx/flags/medium/FAX.tga` | `gfx/flags/small/FAX.tga` | engine country-tag lookup |
| `FBX` | Mauritius | `gfx/flags/FBX.tga` | `gfx/flags/medium/FBX.tga` | `gfx/flags/small/FBX.tga` | engine country-tag lookup |
| `FDX` | Punjab | `gfx/flags/FDX.tga` | `gfx/flags/medium/FDX.tga` | `gfx/flags/small/FDX.tga` | engine country-tag lookup |
| `FLX` | Travancore | `gfx/flags/FLX.tga` | `gfx/flags/medium/FLX.tga` | `gfx/flags/small/FLX.tga` | engine country-tag lookup |
| `FNX` | Dravidian Federation | `gfx/flags/FNX.tga` | `gfx/flags/medium/FNX.tga` | `gfx/flags/small/FNX.tga` | engine country-tag lookup |
| `FOX` | Assam | `gfx/flags/FOX.tga` | `gfx/flags/medium/FOX.tga` | `gfx/flags/small/FOX.tga` | engine country-tag lookup |
| `FSX` | Himalayan Confederation | `gfx/flags/FSX.tga` | `gfx/flags/medium/FSX.tga` | `gfx/flags/small/FSX.tga` | engine country-tag lookup |
| `FUX` | Minangkabau | `gfx/flags/FUX.tga` | `gfx/flags/medium/FUX.tga` | `gfx/flags/small/FUX.tga` | engine country-tag lookup |
| `FVX` | Riau | `gfx/flags/FVX.tga` | `gfx/flags/medium/FVX.tga` | `gfx/flags/small/FVX.tga` | engine country-tag lookup |
| `FXX` | Bugis State | `gfx/flags/FXX.tga` | `gfx/flags/medium/FXX.tga` | `gfx/flags/small/FXX.tga` | engine country-tag lookup |
| `GBX` | Pattani | `gfx/flags/GBX.tga` | `gfx/flags/medium/GBX.tga` | `gfx/flags/small/GBX.tga` | engine country-tag lookup |
| `GCX` | Shan Federation | `gfx/flags/GCX.tga` | `gfx/flags/medium/GCX.tga` | `gfx/flags/small/GCX.tga` | engine country-tag lookup |
| `IAX` | Mon State | `gfx/flags/IAX.tga` | `gfx/flags/medium/IAX.tga` | `gfx/flags/small/IAX.tga` | engine country-tag lookup |

## Evidence and uncertainty

- Human-readable provenance and design notes: `manifest_eex_iax.md` and `references/eex_iax_design_research.md`.
- Prompt and ImageGen source pairing: `prompts/<TAG>_flag_imagegen_prompt.txt` and `source_png/<TAG>_imagegen_raw.png`.
- Machine-readable dimensions, TGA headers, exact lengths, and hashes: `metadata/eex_iax_flag_validation.json`.
- Source-to-ladder visual review: `contact_sheets/eex_iax_source_and_ladders_contact_sheet.png`.
- Historical/regional uncertainty is documented per tag. Generated civic or formable designs are never labeled as attested 1936 flags, modern flags are not backdated, and no generic replacement was used.
- `EEX EHX ERX ESX EWX FAX FDX FLX FVX GBX GCX IAX` retain some route or community ownership uncertainty; this is recorded honestly in the manifest. `FNX FSX` are formable-only alternate-history designs, `FUX` is high-chaos-only, and `EWX` remains exact-community-sensitive.
