# Event 012 portrait interface restore handoff 2

Disposition: implemented within the assigned portrait wiring and DDS scope; no commit or push was made.

## Changes and exact sources

`interface/012_africa_leaders_fictional.gfx` now matches the stable six-sprite bindings from `0954fc12af36d355417b1e5168a5dbb7dd897b86` byte-for-byte (SHA-256 `c35729eef4730350bb1bca0e95c2851c619236457cde62ed7ec1ca4f40027e8a`). The corresponding six original DDS files were restored as exact Git LFS object bytes from `d4abbd215b8512f93cb49e08e4eb4ef0a84536f5^`; each installed-file SHA-256 equals its source LFS OID.

| Stable sprite | Restored DDS | SHA-256 | Size |
| --- | --- | --- | --- |
| `GFX_portrait_012_africa_fictional_pan` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_pan.dds` | `a2a5f50ca97bd55cf82ae3330e7b7cc9f32885f5e5c74b084b6909f9f8c81658` | 156×210, 131,168 bytes |
| `GFX_portrait_012_africa_fictional_gorilla_kingdom` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_gorilla_kingdom.dds` | `0b5814bba0af29916a2b2f35aa9ed30a33e6a694885fad024e8c8c88ae0cbe4b` | 156×210, 131,168 bytes |
| `GFX_portrait_012_africa_fictional_the_green` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_the_green.dds` | `6d250f531ce22a16bd30db79849a7cb6415c639fa76157a93e48062f5caecaa8` | 156×210, 131,168 bytes |
| `GFX_portrait_012_africa_fictional_living_rivers` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_living_rivers.dds` | `e720422ebe865177a0f2076592cee71043b9d916813d46642c15f6ef8d0e3577` | 156×210, 131,168 bytes |
| `GFX_portrait_012_africa_fictional_stoneborn` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_stoneborn.dds` | `fed12d66edbcd1dea53831158d98eadd50583cd0e6e469bf3b5c993115c79030` | 156×210, 131,168 bytes |
| `GFX_portrait_012_africa_fictional_ancient_hosts` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_ancient_hosts.dds` | `16b3960f797ed9415b8ee57112100b9b8c411bd0b2e7ef4cffd0142ee60b81e3` | 156×210, 131,168 bytes |

The scoped audit rows resolve as follows:

- `41e6b08dd635`: reverse the six `_v3` fictional portrait bindings to their stable unsuffixed paths.
- `51658be351f6`: reverse the six `_v4` bindings and the `gorilla_kingdom` to `gorilla` filename substitution.
- `5a02ac56e3d9`: reverse Pan’s `_v5` binding. Keep the RSA sprite addition and its separate source portrait unchanged.
- `814b6d18d083f9d0d98785db7ec4fc2eb1e14cc2` and `0bc5faa490282e145820d5d2017bfffafc44012a` were inspected as intermediate binding states; the six stable sprite identifiers remain the same.

The A6 evidence at `.tmp/restore_assets_audio/portraits/final_manifest.json` was checked before restoring assets. None of these six paths is among A6’s 165 restored portrait rows; the six unsuffixed paths appear in its `retired_deleted_paths` exclusions because they were not consumed at that snapshot. They are reactivated here by the explicitly authorized Event 012 binding restore. No A6-restored portrait DDS was overwritten or removed. The current versioned v4/v5 files remain untouched.

## Wiring and review

The six existing character records in `common/characters/012_africa_fictional_characters.txt` still use the same stable sprite identifiers; no character or gameplay file changed. `interface/012_africa_rsa_portraits.gfx` remains byte-identical to `HEAD` (SHA-256 `d98dacc7b35cd2741e706d53105fae53bdc93b9f60447c7ce3f628cb4228670a`). Its runtime RSA DDS remains present with SHA-256 `4644a7911b59625ffc3490b41f274cff9b1c33d63278116e15bcc852e3ad3c46`.

I inspected the matching vanilla-style leader reference `.claude/skills/chaos-redux-event-assets/assets/gfx_references/portraits/leaders/africa_generic_1.png` at native 156×210. A review-only side-by-side of each restored original and the still-present versioned replacement is at `.tmp/interface_restore_handoff2/portrait012/original_vs_versioned_review.png`; the six original identities and compositions match their historical files, and all restored textures use the expected full leader canvas. Hashes, dimensions, and exact-source equality are recorded in `.tmp/interface_restore_handoff2/portrait012/final_verification.json`.

Pre-edit bytes and diffs for both assigned GFX files were captured under `.tmp/interface_restore_handoff2/portrait012/`. No image was generated or reinterpreted, and no PNG/DDS conversion, source research, provenance archive, or portrait production occurred; this was a historical fictional-art restore. The original v4/v5 candidates and RSA DDS were not edited. No game launch or GUI render was performed, as required by the parent scope.

## Remaining limitations

No known wiring or historical-byte blocker remains. Parent review is still required. The live in-game consumer was not launched or tested.
