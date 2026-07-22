# IW-018 ARX Sardinia portrait source retry handoff

**Date:** 2026-07-22
**Scope:** source-only replacement research for the two remaining grounded
Sardinia identities in Event 006.
**Mode:** no crop, resize, image processing, face generation, advisor/dossier
asset, DDS conversion, `.gfx` edit, or gameplay edit.

## Result

- `ARX_gavino_piras` / `GFX_portrait_ARX_independence_wave_gavino_piras`:
  Gioacchino Solinas is the strongest sourced commander candidate, but remains
  `needs_review`. He was born in Bonorva (Sassari province) in 1892 and was a
  decorated Bersaglieri commander alive and active in 1936. The exact Commons
  binary is dated 1943, only 181x278, and carries a Public Domain Italy claim
  without an explicit PD-1996/US statement. Parent's vanilla audit found no
  `Solinas` ownership hit. No runtime output exists.
- `ARX_sardinian_crown_consultative_council` /
  `GFX_portrait_ARX_independence_wave_vittorio_pala`: `blocked`. No defensible
  non-vanilla-owned dynastic/crown officeholder portrait was found. The old
  name-only `Vittorio Pala` identity cannot be treated as evidence, and no
  generated or generic face may fill the role.

## Exact source files

All files are unchanged originals under
[`sardinia_crown_command_retry`](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/sardinia_crown_command_retry/).
The package manifest contains direct URLs, archive/author/date notes, rights
uncertainty, dimensions, bytes, and SHA-256 values. The primary commander
source is:

- `source_masters/sardinia/arx_gioacchino_solinas_1943_original.png` — 181x278,
  54,141 bytes, SHA-256
  `AF9D453444A7C8EE3F4F75089EEC9104748E19D4C8ADBB0F2F2BF150E1A0EA15`;
  [Commons source](https://commons.wikimedia.org/wiki/File:Gioacchino_Solinas.png),
  [direct binary](https://upload.wikimedia.org/wikipedia/commons/4/49/Gioacchino_Solinas.png),
  [identity/role record](https://www.roma8settembre1943.it/i-personaggi/i-personaggi-di-parte-italiana/gen-brig-gioacchino-solinas/).

Savoy/Aosta and Savoy-Genova binaries are preserved only as collision evidence:

- Aimone di Savoia-Aosta: `arx_aimone_savoy_aosta_duca_di_spoleto_original.png`,
  389x456, 231,898 bytes, SHA-256
  `EAE7D502784F0876B808CC5C0B33D854E6CB627157169B989A7D0C540E027B6D`;
  vanilla `ITA_prince_aimone` is recruited at game start.
- Amedeo di Savoia-Aosta: `arx_amedeo_savoy_aosta_1931_original.jpg`, 2784x4296,
  732,079 bytes, SHA-256
  `73B558F19F1786CF8C558FF794C93B0A07449406610F500446CF5FE3EDA7DC11`;
  vanilla `AOI_prince_amedeo` is recruited by Italian East Africa, and the
  postcard has embedded lettering.
- Filiberto di Savoia-Genova: 1928, 1938, and 1915-25 source binaries are
  listed in the manifest and `source_hashes.sha256`; vanilla defines and
  recruits `ITA_prince_filiberto`.
- Ferdinando Umberto di Savoia-Genova was not copied; parent found
  `ITA_ferdinando_umberto_filippo` in Turkey's character/history/focus surfaces.

Raimondo Carta Raspi (Oristano 1893-Cagliari 1965) remains a cultural/traditional
lead only. His Commons portrait is Public Domain Italy plus PD-1996, but bears a
large signature and he was a historian/editor, not a documented dynastic/crown
officeholder. He cannot satisfy the current crown role without a design change.

## Parent actions and blockers

1. Keep the ARX crown/council role fail-closed; do not substitute Carta Raspi,
   a generic, generated, or name-only face.
2. If the commander is to proceed, obtain an independent review record for the
   Solinas binary that addresses rights, post-opening image date, source
   anonymity, and native 156x210 suitability. Until then it is not `source_ready`.
3. Preserve the exact source binaries and hashes; do not process or convert them
   in this handoff.
