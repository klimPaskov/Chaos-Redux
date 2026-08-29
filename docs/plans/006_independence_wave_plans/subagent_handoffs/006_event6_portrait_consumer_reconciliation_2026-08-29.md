# Event 006 portrait consumer reconciliation handoff

Date: 2026-08-29 (Europe/Kyiv).

Owner: `chaosx_portrait_creator`.

## Result

The eleven newly identified Event 006 portrait consumers reconcile to six existing grounded, source-placeholder identities with complete source/package evidence and exact current supplied-to-runtime DDS matches. No new portrait art, source download, ImageGen result, RunPod operation, PNG, DDS, character definition, or GFX definition was needed or authorized in this tranche.

The existing consolidated registry and current character registry already provide the exact stable wiring. The ideology-specific blocks are aliases of an existing identity and use the same country-leader `civilian.large` sprite. All eleven consumers are male country leaders; no advisor, dossier, commander-small, female, or alternate portrait surface is inferred.

## Consumers reconciled

| Carrier | New consumer IDs | Existing identity | Stable sprite | Character lines | Recruitment lines |
| --- | --- | --- | --- | --- | --- |
| AXX | `AXX_independence_wave_banat_presidium_despotism`, `AXX_independence_wave_banat_presidium_liberalism` | Otto Roth | `GFX_portrait_AXX_independence_wave_otto_roth` | 117, 124 | 164, 165 |
| BOS | `BOS_independence_wave_drina_council_despotism`, `BOS_independence_wave_drina_council_liberalism` | Mehmed Spaho | `GFX_portrait_BOS_independence_wave_mehmed_spaho` | 172, 179 | 186, 187 |
| BBX | `BBX_independence_wave_epirus_council_despotism`, `BBX_independence_wave_epirus_council_liberalism` | Georgios Christakis-Zografos | `GFX_portrait_BBX_independence_wave_georgios_christakis_zografos` | 215, 222 | 178, 179 |
| KOS | `KOS_independence_wave_ferhat_draga_oligarchism` | Ferhat Bey Draga | `GFX_portrait_KOS_independence_wave_ferhat_draga` | 491 | 142 |
| MAC | `MAC_independence_wave_vardar_presidium_despotism`, `MAC_independence_wave_vardar_presidium_liberalism` | Metodija Andonov-Cento | `GFX_portrait_MAC_independence_wave_metodija_andonov_cento` | 585, 592 | 157, 158 |
| BAX | `BAX_independence_wave_thrace_council_despotism`, `BAX_independence_wave_thrace_council_liberalism` | Hristo Silyanov | `GFX_portrait_BAX_independence_wave_hristo_silyanov` | 1328, 1335 | 171, 172 |

The character line references are from the current working tree and the recruitment line references are from `history/general/006_independence_wave_character_recruitment_registry.txt`. Those parent-owned gameplay files were not edited.

## Source, rights, and runtime evidence

The six retained grounded source masters remain in the single flat parent archive `docs/assets/portraits/006_independence_wave/`. The accepted archive cleanup retained source originals at the parent level and kept the `processed/` subfolder for evidence; no per-subject archive folders were recreated.

| Carrier | Retained source master | Source/rights record | Source dimensions and SHA-256 | Current supplied/runtime SHA-256 |
| --- | --- | --- | --- | --- |
| AXX | `iw024_banat_otto_roth_source_placeholder_2026_08_06__portrait_AXX_independence_wave_otto_roth_source.jpg` | Wikimedia Commons, Dr. Otto Roth; circa 1930; unknown author; `PD-RO-photo` and `PD-1996` public-domain record | RGB `627x1026`; `c9ab09e6d7f13d002de703818b47dd5ea91ccdba4526ea23d5bb31c7698448b3` | `1b81c6cc882491d8d19352c13dff93864cd068df21dd43e2c24894995c60245c` |
| BAX | `iw027_thrace_hristo_silyanov_source_placeholder_2026_08_06__portrait_BAX_independence_wave_hristo_silyanov_original.jpg` | Wikimedia Commons, Hristo Silyanov; circa 1903; unknown author; `PD-anon-70-EU` public-domain record | RGB `420x630`; `c7f9efc7c2448b814873249d3724951610626ad4a2eade64815acaa4d3cc38e3` | `c33d80a78f8b086a0449e6bc1946897fa46c60368faa4ca2d99aefb94d78c05f` |
| BBX | `iw028_epirus_georgios_christakis_zografos_source_placeholder_2026_08_06__portrait_BBX_independence_wave_georgios_christakis_zografos_original.jpg` | Wikimedia Commons, Georgios Christakis-Zografos; 1914; credited to Georgios Jakobides; public-domain record | RGB `600x785`; `a980e75d5fd97c90e2026fcd4954a9a696fdff7346d32c6ffde80a09e1e30f45` | `38d0db7147fcf41a31086840bf62d43ed8bfd2b51e0abe60448c11d0c0e01698` |
| BOS | `iw029_bosnia_mehmed_spaho_source_placeholder_2026_08_06__portrait_BOS_independence_wave_mehmed_spaho_source.jpg` | Wikimedia Commons, Mehmed Spaho; 1920s; scan credited to Josip Horvat; public-domain Bosnia/Yugoslav rationale | L `902x1424`; `748f9c2848eb4d936ed0290c4d54f6b712ab15c1d5cc9114a4229723d9e149d0` | `67b35a927ca64a43b97d58652f04ee9bdcca36b5239573c30d54d072ec1ad7b2` |
| KOS | `iw031_kosovo_source_placeholders_2026_08_09__portrait_KOS_independence_wave_ferhat_draga_source.png` | Wikimedia Commons, Ferhat Bey Draga; circa 1920; source credit `kosovapersanxhakun.org`; `PD-Yugoslavia` public-domain record | RGB `249x389`; `1a38811e7d7a95a819a0b7b86acf985d92ef860dcd4cdfb48258960c2cf78103` | `a31fc49eb4156e1bb4942e8982ad4c8623b6c331abd71ba4e36e4c8bb6ab5774` |
| MAC | `portrait_MAC_independence_wave_metodija_andonov_cento_source.jpg` | Wikimedia Commons, `Čento-vsv.jpg`; before 1944; unknown author; `PD-anon-70-EU` and `PD-North Macedonia` public-domain records | RGB `508x722`; `940013e5d7d12e140f4af7c46a1411f9bddb66d313f0bc432365ca55caa286d0` | `1e5794441f15c301659db2e2b3b0f96746b7a6ef1125f552e5635efe0fa17c11` |

The selected supplied files are under `C:/Users/klimp/Documents/ComfyUI Workflows/HOI4/hoi4_portraits_output/output/156x210/iw/dds` and were read only. Each selected `_00002.dds` is byte-identical to the current runtime file under `gfx/leaders/006_independence_wave/`. All twelve files are 131168-byte legacy one-level uncompressed BGRA DDS files at `156x210`, with zero mipmaps and opaque alpha.

The prior source handoffs retain the deterministic crop, processed-PNG, and historical DDS evidence. The crop records are: AXX `[18,5,609,800]` to `591x795`; BAX `[70,20,350,397]` to `280x377`; BBX `[150,55,450,459]` to `300x404`; BOS `[101,10,801,955]` to `700x945`; KOS `[0,0,249,389]` unchanged; and MAC `[1,0,507,681]` to `506x681`. The historical processed candidates are canonical `156x210` outputs recorded in the source manifests, and the current supplied/runtime bytes—not a newly generated fallback—are the selected runtime evidence.

Rights and identity review is recorded in the dated source/package handoffs. The records preserve the historical identities and source-visible facial geometry, age, expression, clothing, and tonal structure. The matching vanilla leader reference family was inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`, including the native `156x210` contact sheet. No conflicting live vanilla or Chaos Redux person owner was found for these six identities.

## Existing wiring and checks

The authoritative GFX registry is `interface/006_independence_wave_portraits_registry.gfx`. The six stable sprite definitions occur exactly once at lines 26 (AXX), 35 (BAX), 43 (BBX), 56 (BOS), 82 (KOS), and 159 (MAC), and each resolves to the event-scoped runtime path. The dated per-package GFX files are absent after the accepted registry consolidation, so no duplicate definition or stale path was added.

Read-only source checks passed for all eleven IDs: each new character block is defined, has `gender = male`, has the expected `civilian.large` sprite, and has a matching recruitment call. The six GFX names are unique and their six runtime textures exist. The strict DDS check passed for all six supplied/runtime pairs with the dimensions, masks, pitch, mip, alpha, length, and byte-equality conditions recorded in the durable manifest.

The required `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` conversion was not rerun because no new candidate was admitted and the current runtime DDS already exactly matches the selected supplied output. The historical source packages record prior use of the required converter.

## State, scope, and blockers

All eleven consumers remain `source_placeholder`. None is `styled_final` or `replacement_pending`. The user remains the only party authorized to supply a later HOI4-style grounded replacement. No RunPod page, workflow, provider job, queue, or result was opened or operated, and no ImageGen likeness was created.

This tranche changed only these two documentation files:

- `docs/assets/portraits/006_independence_wave/processed/portrait_consumer_reconciliation_2026_08_29.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_portrait_consumer_reconciliation_2026-08-29.md`

No character, recruitment, gameplay, GFX, PNG, DDS, or unrelated file was changed. The unresolved supplied candidates documented by the existing Event 006 portrait closure remain unmapped and were not used as fallbacks.

AXX, BAX, and BBX have source-attested current package closure in their existing handoffs; KOS has a source-level package gate pass and central attestation. BOS and MAC have central source attestation, while their existing package records retain conditional typed-AI/runtime evidence gates. The full Event 006 completion remains parent-owned and `HOLD/PARTIAL` pending live engine/MCP evidence, typed probability evidence, and the broader package gates. The global source-of-truth map and quality checklist remain parent-owned and were not edited in this bounded tranche.

The durable evidence manifest is `docs/assets/portraits/006_independence_wave/processed/portrait_consumer_reconciliation_2026_08_29.md`.
