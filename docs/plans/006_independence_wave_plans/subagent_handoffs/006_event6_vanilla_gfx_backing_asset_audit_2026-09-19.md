# Event 006 vanilla GFX backing-asset audit — 2026-09-19

Disposition: implemented audit-tooling improvement; no gameplay, GFX, portrait, or asset files changed.

## Scope

The existing `.tools/audit_asset_wiring_static.py` checked mod-owned `.gfx` texture paths and treated vanilla GFX registration as sufficient reach-through evidence. That left one important failure class invisible: a mod-referenced vanilla GFX name whose installed vanilla declaration points at a missing DLC texture.

The checker now performs a narrow second pass over vanilla `.gfx` definitions whose `GFX_` names are referenced by the mod. It reports the declared texture path, vanilla `.gfx` file, and owning GFX name when the backing file is absent. The pass does not lint unrelated vanilla content and does not alter runtime wiring.

## Evidence

The new pass was exercised against the installed No Step Back directory with the two IW-040 Kuban Ivanis tokens. It reports the missing `gfx/leaders/KUB/portrait_KUB_ivanis_vasily_nikolaevich.dds` from `dlc/dlc034_no_step_back/interface/nsb_portraits.gfx` while resolving the existing 65x67 idea DDS. This independently reproduces the portrait gap documented by `006_iw040_kuban_portrait_gap_2026-09-19.md`.

The modified script passes `python -B -m py_compile .tools/audit_asset_wiring_static.py`. No fallback artwork, source placeholder, runtime DDS, or portrait registry entry was created. The existing flat portrait archive contract remains unchanged.

## Remaining limits

This is source/tooling evidence only. It does not establish DLC entitlement, repair the absent vanilla texture, promote IW-040, or close the whole-event HOLD / PARTIAL boundary. A replacement or override still requires an explicit identity and rights decision.
