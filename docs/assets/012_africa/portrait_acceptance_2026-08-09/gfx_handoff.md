# Event 012 portrait GFX and runtime handoff

Date: 2026-08-09

The runtime DDS and portrait-specific GFX registrations were promoted in commit `380b9aa04` (`Update Event 012 portrait sources and wiring`); this acceptance commit adds the durable source, crop, prompt, and round-trip evidence. Every runtime DDS is 156x210, 32-bit BGRA, one mip, and was produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. The final decoded review is `contact_sheets/dds_roundtrip_contact_v2.png`.

## Sprite registrations

- Historical priority members: `interface/012_africa_priority_member_characters.gfx` → `gfx/leaders/012_africa/priority_members/portrait_012_africa_priority_<package>_sovereign_source_locked.dds` → existing `GFX_portrait_012_africa_priority_<package>_sovereign` character references.
- Fictional sovereigns: `interface/012_africa_leaders_fictional.gfx` → six stable `GFX_portrait_012_africa_fictional_*` sprites. Pan points exactly to `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_pan_v5.dds` (the file exists); Gorilla Kingdom, The Green, Living Rivers, Stoneborn, and Ancient Hosts remain on their accepted v4 DDS packages, with no stale Pan v4 path in the active GFX entry.
- Symbol-only evolutions: `interface/012_africa_evolutions.gfx` → v3-replaced runtime base DDS files for Regional Council, Continental Secretariat, and World Pole Delegation.
- RSA branch: `interface/012_africa_rsa_portraits.gfx` adds `GFX_portrait_012_africa_rsa_mgolombane_sandile` → `gfx/leaders/012_africa/rsa/portrait_012_africa_rsa_mgolombane_sandile.dds`.

## RSA identity handoff

`common/scripted_effects/012_africa_rsa_effects.txt` creates `King Mgolombane Sandile` with the dedicated sprite. `localisation/english/012_africa_rsa_l_english.yml` names the same documented Xhosa king in the branch notice. This is the approved alternate-history casting for the requested fictional Archie Velile Sandile because no direct archival image for Archie was found; the rationale and source URL are recorded in `manifest.md` and `docs/plans/012_africa_plans/subagent_handoffs/012_africa_rsa_final_2026-08-09.md`. The prior `GFX_portrait_generic_africa_male_01` reference is removed from this branch.

## Evidence and review

- Historical sources and crop metadata: `docs/assets/portraits/012_africa/` and `metadata/crops/`.
- Processed source placeholders and DDS conversion outputs: `processed_png/` and `final_dds/`.
- Six fictional source/prompt pairs: `docs/assets/portraits/012_africa/portrait_012_africa_fictional_*_v3_source*.png/.txt` and Pan v5 native ImageGen evidence.
- Symbol-only ImageGen prompt/source pairs: `portrait_012_africa_evolution_*_v3_source_gen.png/.txt`; contact sheet review confirms no people or silhouettes.
- Contact sheets: `priority_source_locked_processed_contact_v2.png`, `evolution_pan_processed_contact_v3.png`, and `dds_roundtrip_contact_v2.png`.
- RSA source archive and rights note: `source_master_rsa_mgolombane_sandile_archival.jpg`, `portrait_012_africa_rsa_mgolombane_sandile_source_crop.png`, and `portrait_012_africa_rsa_mgolombane_sandile.txt`.

No RunPod operation was performed. Historical source placeholders remain explicitly pending any future user-supplied HOI4-style finals; fictional and symbol-only assets are complete for this handoff.
