# Occupation policy strip repair

Disposition: implemented texture repair.
Acceptance basis: the graphics-fix task requests a painted final occupation-law frame.

`GFX_occupation_policy_icon_strip` remains a 540×30 strip with 18 frames.
The first 17 frames are pixel-identical to the pre-edit mod texture and match the installed vanilla family; only frame 18 was replaced.
The former flat grey skull is a shaded olive/bronze painted skull with cream highlights, complete edges and transparent margin.
The existing sprite registration in `interface/countryoccupationview.gfx`, lines 245–249, requires no change.
The installed vanilla file registers the same family with 17 frames; its DDS was decoded and visually inspected before production.

## Evidence

Native ImageGen source: `docs/assets/gfx_fix_shared_ui/occupation_source.png`, original basename `exec-1fac7f04-8914-4bef-8a8a-63d44a2dd5b7.png`.
The prompt requests one shaded olive skull miniature for a 30×30 occupation policy frame, readable at 26×26, native transparency, no glow, text or scenery.
Processed strip: `docs/assets/gfx_fix_shared_ui/occupation_processed.png`.
Runtime: `gfx/interface/occupation/occupation_policy_icon_strip.dds`, SHA-256 `35716ab1b6dac70edbb51f9f4869b60f0337b3f58b602330338118287e549da2`.
The standard skill converter produced the DDS; decoded runtime pixels exactly match the processed PNG.
The complete strip and final frame were reviewed against the native vanilla strip; `validation.json` records the first-17-frame equality assertion.
The group contact sheet is retained in `docs/assets/gfx_fix_shared_ui/contact_sheets/countryoccupationview_1.jpg` with its old review sheet alongside the workspace.
The same offline sprite documentation citations recorded in `mapmodes_interface_report.md` apply to the unchanged 18-frame strip contract.

## Orchestrator live check

Use a country with occupied territory and open Occupied Territories, then the occupation-law chooser.
Inspect the mod's final skull law and several neighbouring vanilla laws at UI scale 1.
The skull must show olive painted shading with readable dark sockets, fit its 30×30 cell, and leave neighbouring vanilla icons unchanged.

No omissions, substituted subjects, or frame-count changes were made in this group.
