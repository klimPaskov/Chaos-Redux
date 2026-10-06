# Shared ChaosX super-event asset report

Status: both assigned visual findings are implemented and parent-approved. The AZL replacement is installed at its existing texture path; the distinct Final Silence terminal DDS is installed and wired at a separate path.

## Scope and references

The assigned rows are `GFX_super_event_azl` and `GFX_super_event_final_silence_terminal` from `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md` and `gfx_issues.json`.

Before generation, I inspected the canonical `event_art/super_event/contact_sheet.png` and the exact `457x328` super-event family, plus the installed runtime sources at both target DDS paths.

Both outputs are opaque full-canvas scenes. The AZL output is a fictional illustrated scene, not a historical photograph, and contains no readable text.

## Asset crosswalk

| Sprite | Existing or handoff runtime path | Active super-event surface | Source PNG and SHA-256 | Processed PNG and SHA-256 | Final DDS SHA-256 |
|---|---|---|---|---|---|
| `GFX_super_event_azl` | `gfx/super_events/002_zombie_outbreak/super_event_azl.dds` | `super_event_visible=2`; the AZL leader/faction gate in `common/on_actions/002_zombie_outbreak_on_actions.txt` shows this sprite. | `docs/assets/gfx_fix_shared_chaosx_super_events/source_generated/super_event_azl_candidate_v1_source.png` (`8e5707577b2ee40eabbf863c8922e55712afa89a5d9bb0e84631d2b97531993c`) | `docs/assets/gfx_fix_shared_chaosx_super_events/processed/super_event_azl_candidate_v1.png` (`cc99cff796af8806f89ba89e01dc85dd5cb97305fd4e3ac94c2c957c1f26831c`) | `684b7622f0ccc9c15c03797a61ff8fbf3f60dd557a4dfffd66603f48c5b87871` |
| `GFX_super_event_final_silence_terminal` | New distinct path: `gfx/super_events/003_holy_realm/super_event_the_final_silence_terminal.dds` | Terminal slot `super_event_visible=9`, localized as `GFX_super_event_final_silence_terminal`; `holy_realm_show_super_event` sets it for `holy_realm_super_event.final_silence_thermonuclear`, while `chaosx.nr3.82` runs the terminal wave. | `docs/assets/gfx_fix_shared_chaosx_super_events/source_generated/super_event_the_final_silence_terminal_candidate_v1_source.png` (`ac19c79f48cc0f872125b44e1b1b59a4aeeb489187b099a91236dc54bbd6995a`) | `docs/assets/gfx_fix_shared_chaosx_super_events/processed/super_event_the_final_silence_terminal_candidate_v1.png` (`b1dbf7b11cdcb9bf59150eddc6b79339b6d612607c24658eddc023bedf50d0d3`) | `db8a2d3fb5d5488925f89bc4b9846afe86a4723fc334517f3e43fa667f1b3055` |

The AZL scene preserves the centered undead ranger poster composition and replaces all slogan lettering with continuous forest and sky. Its registered texture path stays the same.

The terminal Final Silence scene keeps the central statue and silence gesture, adding visible physical decay and a darker ash-filled void. The original main-stage `gfx/super_events/003_holy_realm/super_event_the_final_silence.dds` remains byte-for-byte unchanged at SHA-256 `26a14718eb76e85bdc4bd7129087a620ebc4c9f350c08e6fdef944ae71f6aa21`.

## Conversion and review evidence

The two finals were converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` to 457x328, one-level BGRA DDS files. Both pass the repository header check, have alpha 255 throughout, and decode pixel-identically to their processed PNGs.

The before/after parent-review sheet is `docs/assets/gfx_fix_shared_chaosx_super_events/contact_sheets/super_event_candidates_before_after_v2.png` (SHA-256 `b1be81e5b98cabc37182ce91cbe64692642552ad13b0193883b615cfce7c1121`). The final PNG/DDS native round-trip sheet is `docs/assets/gfx_fix_shared_chaosx_super_events/contact_sheets/super_event_dds_roundtrip_v3.png` (SHA-256 `840967c52bafa11ea70bb4df576dc2a4d3d6d1439d896995edac5cc46f653ebd`). The machine-readable header and pixel evidence is `docs/assets/gfx_fix_shared_chaosx_super_events/processed/super_event_dds_roundtrip_v1.json` (SHA-256 `818eec6f04301e5a96203243e224302cd0d8cf9361042556b9fa67ec969a3f77`).

The pre-edit AZL DDS SHA-256 was `94b726bf91d666b0344310c105ceb40cde1f2b8c3329500dce095586c5911ec2`; the pre-edit main Final Silence DDS SHA-256 was `26a14718eb76e85bdc4bd7129087a620ebc4c9f350c08e6fdef944ae71f6aa21`.

## Wiring handoff and live checks

The asset worker changed no `.gfx`, GUI, event, gameplay, or localization files. `GFX_super_event_azl` already targets its updated existing DDS path.

The parent repointed only `GFX_super_event_final_silence_terminal` in `interface/chaosx_super_events.gfx` to `gfx/super_events/003_holy_realm/super_event_the_final_silence_terminal.dds`; `GFX_super_event_final_silence` retains the original main-stage texture.

The image and consumer mapping are source-reviewed and pixel-validated; this asset worker did not perform an in-game super-event preview. The parent owns final wiring/source QA, and the user owns live-game validation.

## Parent integration and validation limits

The parent changed only the terminal sprite texture path in interface/chaosx_super_events.gfx and independently reviewed both final decoded DDS images at their native 457×328 size.
The main-stage sprite still uses its unchanged original texture.
The HOI4 MCP transport closed during this task; no successful shared super-event window render or in-game presentation proof is claimed.
For the orchestrator, use a disposable 1936 USA art fixture with `world_end_fallout` unset.
Run the country-scope test effect `set_global_flag = { flag = super_event_visible value = 2 days = 30 }` and inspect AZL, then close its normal super-event button.
Repeat with `value = 8` for main Final Silence and `value = 9` for terminal Final Silence, closing each display before the next fixture.
Expected results: slot 2 has no poster lettering, slot 8 retains the intact statue, slot 9 shows the visibly cracked statue and ash; all three fill the intended picture area without clipping.
