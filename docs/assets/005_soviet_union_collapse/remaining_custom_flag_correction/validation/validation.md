# Event 005 Remaining Custom Flag Correction Validation

## Commands Run

```bash
identify -format '%f %wx%h %[channels]\n' gfx/flags/{BBH,UKR_BLACK_BANNER,TNC,ALA,GAC,UWD,IUL,ICD,ARD,NLC}.tga gfx/flags/medium/{BBH,UKR_BLACK_BANNER,TNC,ALA,GAC,UWD,IUL,ICD,ARD,NLC}.tga gfx/flags/small/{BBH,UKR_BLACK_BANNER,TNC,ALA,GAC,UWD,IUL,ICD,ARD,NLC}.tga
```

```bash
sha256sum gfx/flags/{FTH,BBH,UKR_BLACK_BANNER,BSC,TNC,ALA,GAC,DSC,UWD,IUL,ICD,NRF,ARD,NLC}.tga
sha256sum gfx/flags/medium/{FTH,BBH,UKR_BLACK_BANNER,BSC,TNC,ALA,GAC,DSC,UWD,IUL,ICD,NRF,ARD,NLC}.tga
sha256sum gfx/flags/small/{FTH,BBH,UKR_BLACK_BANNER,BSC,TNC,ALA,GAC,DSC,UWD,IUL,ICD,NRF,ARD,NLC}.tga
```

TGA headers were inspected for the replaced outputs. Every replaced normal, medium, and small TGA reported image type `2`, bpp `32`, descriptor `8`, and expected dimensions.

## Results

- Replaced output dimensions:
  - normal: `82x52`
  - medium: `41x26`
  - small: `10x7`
- Target duplicate base groups after replacement:
  - `gfx/flags`: no duplicate hashes in target set
  - `gfx/flags/medium`: no duplicate hashes in target set
  - `gfx/flags/small`: no duplicate hashes in target set
- User-named active base/ideology sets plus `OGB`:
  - `OGB`, `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `SOG`, `ALN`, `KHW`, `KZR` each reported `duplicate_hashes=0` in normal, medium, and small directories.
- Orientation:
  - `duplicate_groups_normal_after.png`, `duplicate_groups_medium_after.png`, and `duplicate_groups_small_after.png` decode upright.
  - `user_named_plus_ogb_normal_flags.png`, `user_named_plus_ogb_medium_flags.png`, and `user_named_plus_ogb_small_flags.png` decode upright.
  - `ogb_normal_before.png`, `ogb_medium_before.png`, and `ogb_small_before.png` decode upright; no current `OGB` upside-down file was found.

## Notes

- `FTH`, `BSC`, `DSC`, and `NRF` were preserved as the first identity in their duplicate groups.
- No vanilla country default flag override was added.
- No gameplay, `.gfx`, localisation, focus, decision, history, country, spreadsheet, or non-asset docs were edited as part of this sidecar.
