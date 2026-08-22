# IW-045 Bashkiria — Yakov Bykin source-placeholder runtime handoff

Date: 2026-08-14.

Status: deterministic `source_placeholder` runtime asset installed, portrait-specific GFX registered, and parent consumer/cleanup gates satisfied. The Event 006 portrait archive is consolidated: no IW-045 156x210 PNG is retained under its parent or `processed/` folder.

## Scope and source mode

This handoff owns only the IW-045 Bashkiria Yakov Borisovich Bykin grounded portrait asset package.

The selected mode is `source_placeholder`, so the unchanged attributed source crop is the runtime candidate and no HOI4 repaint or identity substitution was made.

RunPod was not opened, operated, configured, queued, or monitored, and no styled-final output was requested or supplied.

## Grounded source and rights

The source is the Wikimedia Commons photograph [“Быкин Яков Борисович, 1912”](https://commons.wikimedia.org/wiki/File:%D0%91%D1%8B%D0%BA%D0%B8%D0%BD_%D0%AF%D0%BA%D0%BE%D0%B2_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87,_1912_.jpg), uploaded by `MDobrom` and declared `CC BY-SA 4.0`.

The source package preserves the attribution and share-alike obligation and does not claim public-domain status.

English and Russian biographical records plus Wikidata Q15064831 corroborate Bykin’s identity, dates, and Bashkir Regional Committee role.

The durable source archive is the consolidated [Event 006 portrait package](../../../assets/portraits/006_independence_wave/), with the IW-045 original at `iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin_original.jpg` and the master/crop plus metadata under `processed/`.

## Source, crop, and PNG evidence

`iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin_original.jpg` is the retained `1986x3178` RGB source master with SHA-256 `882608cf2ea282f5a603cc1c917f2b13a8b813d5c79857ee3d3e6a6c4fd02ddb`; the lossless crop and metadata remain in `processed/`.

`processed/iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin_source_crop.png` is the co-located lossless `1125x1514` RGB crop with SHA-256 `0b8bc295b95910e750944ac48a41644ffae74e327764d5aa36b735961e1993e3`.

The crop rectangle is `[372,401,1497,1915]`, YuNet found exactly one face at `[810,676,250,306]`, and the crop JSON records decoded RGBA equality with matching hash `474dbf8c8e566f393d68292f62d9a6004705fd39c3002cbec7df3aecec78ca77`.

The deterministic RGB `156x210` Pillow LANCZOS candidate has SHA-256 `470c6d4f6213c3ca7a0451e3440a5534b1e50333eec456f43cab204ad3644f34`; it is reconstructed in memory from the exact crop for DDS validation and is intentionally not retained as a PNG in the consolidated parent/processed archive.

The canonical installed leader reference family at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/` and its contact sheet were inspected before processing.

## Runtime DDS

Installed runtime texture: `gfx/leaders/006_independence_wave/portrait_BSK_independence_wave_yakov_bykin.dds`.

The DDS is `156x210`, 131168 bytes, and SHA-256 `bf2b9e89ad6279b6d566370fa1efda72b78f97f22793c44ac909bca9f089d13d`.

The converter output passed the legacy one-level BGRA checks: `DDS ` magic, `DDS_HEADER` size `124`, pixel format at offset `76` with size `32`, flags `65`, fourCC `0`, 32-bit masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, `DDSCAPS_TEXTURE = 0x1000`, one mip level, and exact length `128 + 156*210*4`.

The alpha range is `255..255`, as expected for the opaque country-leader candidate.

Pillow decoded the DDS at `156x210`, and its RGBA pixels exactly equal the RGB candidate plus opaque alpha; the raw BGRA payload equality also passed.

## Portrait-specific GFX wiring

Added [interface/006_independence_wave_iw045_bashkiria_portraits.gfx](../../../../interface/006_independence_wave_iw045_bashkiria_portraits.gfx).

The stable sprite token is `GFX_portrait_BSK_independence_wave_yakov_bykin`.

The sprite points to `gfx/leaders/006_independence_wave/portrait_BSK_independence_wave_yakov_bykin.dds`.

The global vanilla `GFX_portrait_Yakov_Borisovich_Bykin` in `interface/_leader_portraits.gfx` was not overridden, and no Event 005 institutional `GFX_portrait_BSK_oilfield_workshop_council` art was reused.

## Parent-owned wiring gate

Vanilla `common/characters/BSK.txt` still binds `BSK_yakov_bykin` to the global vanilla token, and no character file was edited in this asset lane.

The parent has implemented the safe consumer binding through a character-scoped `set_portraits` call, with an idempotent `independence_wave_bsk_portrait_override` flag that prevents simultaneous global ownership and does not mutate unrelated vanilla consumers.

The exact hidden checkpoint is `chaosx.nr6.350` in `events/006_independence_wave.txt:186`, where the BSK branch at lines `307-325` requires `is_independence_wave_bashkiria_package = yes` and `has_independence_wave_bsk_command_roster = yes`, sets `independence_wave_bsk_roster_checkpoint`, applies `GFX_portrait_BSK_independence_wave_yakov_bykin` to `BSK_yakov_bykin`, and records `independence_wave_bsk_portrait_override`.

The BSK package effect calls `country_event = { id = chaosx.nr6.350 }` before consuming that checkpoint to set `independence_wave_command_roster_ready`; the portrait override is now part of that checkpoint.

The parent-owned event/.350 consumer checkpoint is satisfied. BSK cleanup at `common/scripted_effects/006_independence_wave_bashkiria_package_effects.txt:428-440` restores `GFX_portrait_Yakov_Borisovich_Bykin` and clears `independence_wave_bsk_portrait_override`, so route-specific cleanup/reference removal is guarded and satisfied.

## State, review, and blockers

Portrait state is `source_placeholder`, `styled_final` is not requested, and `replacement_pending` is false.

Identity, framing, provenance, runtime DDS/GFX, parent `.350` consumer, and guarded cleanup reviews are PASS for the source-placeholder candidate. Archive-consolidation exception: the 156x210 candidate PNG is not retained; exact crop equality plus deterministic reconstruction and DDS pixel roundtrip are retained instead.

No gameplay, character identity, traits, history, event, decision, central adapter, attestation, Join, localisation, or unrelated UI files were changed.

Skipped checks are live in-game portrait display and central admission/attestation; no game launch is permitted and central Event 006 admission remains parent-owned.

No fallback, generic replacement, generated portrait, or styled-final simplification was used.
