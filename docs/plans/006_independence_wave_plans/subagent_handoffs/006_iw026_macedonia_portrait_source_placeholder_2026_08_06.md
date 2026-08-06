# IW-026 Macedonia portrait source-placeholder handoff

Outcome: the grounded Macedonia identity/source gate is PASS for Metodija Andonov-Cento, and a deterministic source-placeholder PNG/DDS chain is archived and portrait-specifically wired to `MAC_independence_wave_vardar_presidium`. The portrait is not a styled HOI4 final, and this handoff does not claim central attestation or whole-country package completion.

## Identity, source, rights, and role verdict

- Selected subject: Metodija Andonov-Cento (1902-1957), real male Macedonian civic-national figure and first president of the Presidium of ASNOM.
- Identity source: Commons `File:Čento-vsv.jpg`, page <https://commons.wikimedia.org/wiki/File:%C4%8Cento-vsv.jpg>, direct original <https://upload.wikimedia.org/wikipedia/commons/e/e4/%C4%8Cento-vsv.jpg>.
- Source metadata: unknown author, `before 1944`, 508x722 JPEG, Commons public-domain terms via `PD-North Macedonia` and `PD-anon-70-EU`; the archived master is byte-for-byte unchanged.
- Period/role corroboration: Commons `File:Средба на Ченто со југословенски пратеници.jpg`, page <https://commons.wikimedia.org/wiki/File:%D0%A1%D1%80%D0%B5%D0%B4%D0%B1%D0%B0_%D0%BD%D0%B0_%D0%A7%D0%B5%D0%BD%D1%82%D0%BE_%D1%81%D0%BE_%D1%98%D1%83%D0%B3%D0%BE%D1%81%D0%BB%D0%BE%D0%B2%D0%B5%D0%BD%D1%81%D0%BA%D0%B8_%D0%BF%D1%80%D0%B0%D1%82%D0%B5%D0%BD%D0%B8%D1%86%D0%B8.jpg>, direct original <https://upload.wikimedia.org/wikipedia/commons/7/76/%D0%A1%D1%80%D0%B5%D0%B4%D0%B1%D0%B0_%D0%BD%D0%B0_%D0%A7%D0%B5%D0%BD%D1%82%D0%BE_%D1%81%D0%BE_%D1%98%D1%83%D0%B3%D0%BE%D1%81%D0%BB%D0%BE%D0%B2%D0%B5%D0%BD%D1%81%D0%BA%D0%B8_%D0%BF%D1%80%D0%B0%D1%82%D0%B5%D0%BD%D0%B8%D1%86%D0%B8.jpg>. Its June 1936 metadata identifies Čento as third from the right in a meeting with Yugoslav deputies and records public-domain status.
- Role adaptation: `MAC_independence_wave_vardar_presidium` is the existing institutional handle. The parent package now supplies this sourced identity as its provisional country-leader and corps-commander consumer and checks it through `has_independence_wave_mac_command_roster`; no generic or invented identity was substituted.
- Exact/variant owner searches for `Metodija`, `Andonov`, `Cento`, `Čento`, and `Ченто` found no existing identity owner or portrait variant in Chaos Redux, installed vanilla, or the approved Kaiserreich roots.

## Files changed

### Source/evidence archive

All files below are under `docs/assets/006_independence_wave/iw026_macedonia_portrait_source_2026_08_06/`.

- `portrait_MAC_metodija_andonov_cento_source_master.jpg`: RGB 508x722, 68,415 bytes, SHA-256 `940013e5d7d12e140f4af7c46a1411f9bddb66d313f0bc432365ca55caa286d0`.
- `portrait_MAC_metodija_andonov_cento_source_crop.png`: RGB 506x681, 328,440 bytes, SHA-256 `6f90d894c09f340f2762a6270edf0e6fd9b277332824152f22b9a99e467a2300`.
- `portrait_MAC_metodija_andonov_cento_source_crop.json`: crop receipt, 2,519 bytes, SHA-256 `9efe73db881c41db6062107f927ff807594ecc48a1c878953fca20d27d790e81`.
- `portrait_MAC_independence_wave_metodija_andonov_cento.png`: RGB 156x210 source placeholder, 55,862 bytes, SHA-256 `0439c245ec695462dc20befe3fc0c13a34b49a8a128fe695a0cc12967af063ab`.
- `portrait_MAC_independence_wave_metodija_andonov_cento.dds`: RGBA32 156x210, 131,168 bytes, SHA-256 `4761961c13c61d0abbd5e58db6f13260effbcc5a014364557634a2c943f29b97`.
- `portrait_MAC_metodija_andonov_cento_role_reference_1936.jpg`: RGB 774x532, 78,121 bytes, SHA-256 `e05adfc5d2ad286eefbab31f2123d349d9ce0a1bd2470931341697f79b153ef9`.
- `portrait_MAC_metodija_andonov_cento_role_reference_1936_crop.png`: RGB 145x195, 22,879 bytes, SHA-256 `dd1acc060ef79e24aa6298ed4c8b256eddb7553926b5b378aa45162a9253d02d`.
- `portrait_MAC_metodija_andonov_cento_role_reference_1936_crop.json`: role-reference crop receipt, 2,576 bytes, SHA-256 `12860dfa2bffd9604f71839b5841c553049e4d717c1f59f649845eef91dabc5`.
- `review_identity_framing_4x.png`: 1312x1760 visual review sheet, 543,813 bytes, SHA-256 `03bcd8f1f58622d9fc5245aa885cb26b5b9a4cf40413702f37d2fcb110b7df63`.
- `source_provenance.md`, `processing_record.md`, `asset_manifest.md`, and `gfx_handoff.md`: provenance, processing, byte manifest, and runtime handoff records.

### Durable/runtime wiring

- `docs/assets/portraits/006_independence_wave/portrait_MAC_independence_wave_metodija_andonov_cento_source.jpg`: durable unchanged source copy, SHA-256 `940013e5d7d12e140f4af7c46a1411f9bddb66d313f0bc432365ca55caa286d0`.
- `docs/assets/portraits/006_independence_wave/portrait_MAC_independence_wave_metodija_andonov_cento.png`: durable processed source-placeholder copy, SHA-256 `0439c245ec695462dc20befe3fc0c13a34b49a8a128fe695a0cc12967af063ab`.
- `gfx/leaders/006_independence_wave/portrait_MAC_independence_wave_metodija_andonov_cento.dds`: runtime DDS, SHA-256 `4761961c13c61d0abbd5e58db6f13260effbcc5a014364557634a2c943f29b97`.
- `interface/006_independence_wave_macedonia_portraits.gfx`: defines `GFX_portrait_MAC_independence_wave_metodija_andonov_cento` and the stable DDS texture path.
- `common/characters/006_independence_wave_macedonia_characters.txt`: portrait consumer for `MAC_independence_wave_vardar_presidium`; the parent package owns the provisional country-leader/corps-commander role blocks and roster gate.

## Processing and review evidence

- Exact source crop used rectangle `(1,0,507,681)` with `decoded_pixels_equal=true` and matching RGBA SHA-256 `a6709b818d5f93c3019735c4226140c6c5b4f658b7259bf3438eca3ad4765deb`.
- The candidate was resized from the exact crop with Pillow 11.1.0 LANCZOS to RGB 156x210, with no repaint, retouch, recolour, padding, or synthetic fill.
- DDS header was checked as uncompressed RGBA32 at 156x210 with exact 131,168-byte length; decoding its payload reproduced PNG RGBA SHA-256 `e4f9025a117d8d83e2febff8e1f57978c23451d2f8d561f82b8ecb97dd0943eb` exactly.
- The visual review sheet compares source master, explicit crop, 4x source-placeholder candidate, and the installed vanilla leader reference `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/fin_carl_mannerheim.png`. The candidate is attributable and suitably head-and-shoulders/bust framed for source-placeholder use, while its archival/low-resolution appearance is retained rather than hidden.

## State, skipped checks, and remaining gates

- Portrait state: `source_placeholder`; no `styled_final` was requested or supplied, so `replacement_pending` is not asserted.
- No RunPod operation, ImageGen call, repaint, or provider-backed replacement was performed.
- No advisor, high-command, dossier, small-portrait, female, generic, or generated asset was created.
- No central attestation row, country history, country setup, localisation, event, focus, decision, AI, trait, or unrelated UI file was changed by this portrait handoff.
- No game launch or in-game consumer test was run; portrait-only work does not require the event/focus/map MCP routes.
- Parent remains responsible for the MAC country-package admission, independent country-package audit, central attestation decision, and user-side live validation. The portrait source/rights/role evidence itself is complete and contains no fallback substitution.

## Simplifications and blockers

The only simplification is the explicitly selected grounded `source_placeholder` mode: the archival source remains visibly low-resolution and is not repainted into a HOI4-style final. This is intentional and authorized by the current workflow. No other omission, genericization, rights fallback, or unapproved substitute was used.
