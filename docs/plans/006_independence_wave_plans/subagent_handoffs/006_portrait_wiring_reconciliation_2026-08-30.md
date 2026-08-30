# Event 006 portrait wiring reconciliation

Date: 2026-08-30.

Scope: revalidate the user-supplied Event 006 portrait DDS set, existing runtime basenames, portrait-specific sprite registries, and current handoff after the 2026-08-25 registry consolidation. This is a bounded portrait audit only; no gameplay, character identity, localisation, country setup, event, focus, decision, or unrelated UI surface was changed.

## Result

The source-to-runtime matrix in `006_portrait_wiring_supplied_runtime_2026_08_22.md` remains current and is the exact identity, runtime basename, sprite key, and SHA-256 authority for all 51 selected files.

- All 51 exact user-supplied DDS paths under `C:\Users\klimp\Documents\ComfyUI Workflows\HOI4\hoi4_portraits_output\output\156x210\iw\dds` are present and hash-stable.
- Thirty-eight safe source-to-runtime mappings remain byte-identical, with 38/38 target hashes matching the selected source hashes.
- Thirteen files remain explicitly unresolved and were not copied, renamed, relabelled, or assigned to another real person.
- Every selected source and every installed target is 131,168 bytes, 156x210, legacy `DDS `, 32-bit BGRA, uncompressed, and no-mipmap.
- The selected inputs remain grounded `source_placeholder` assets, not provider-backed styled finals. No `replacement_pending` state is claimed.

## Current portrait sprite ownership

The 38 verified portrait texture registrations are now distributed across the current interface registries as follows:

| Current `.gfx` owner | Verified portrait registrations | Runtime status |
|---|---|---|
| `interface/006_independence_wave_portraits_registry.gfx` | 34 registrations covering WLS J. H. Thomas and George Cornwallis-West, NAV José Antonio Aguirre, AXX Otto Roth, BAX Hristo Silyanov, BBX Georgios Christakis-Zografos and Spyros Spyromilios, BOS Mehmed Spaho, MNT Blazo Jovanović, Mitar Martinović, and Kristo Popović, KOS Ferhat Draga and Miladin Popović, RUT Andriy Brodiy, Augustin Voloshyn, Dmytro Klympush, and Ivan Mondok, BSK Yakov Bykin, YAK Pavel Pevznyak, ARX Emilio Lussu and Vittorio Verne, ASX Luigi Rizzo, Luigi Sturzo, and Pietro Lanza di Scalea, ASY Civic National Assembly and Levies Guardianship, CHU four institutional consumers, COR Adolphe Landry and Jean Chiappe, GLC Alfonso Daniel Castelao, and MAC Metodija Andonov-Cento. | 34/34 texture paths resolve and all hashes match. |
| `interface/006_independence_wave.gfx` | `GFX_portrait_independence_wave_BAY_rupprecht_of_bavaria` and `GFX_portrait_RHI_josef_friedrich_matthes`. | 2/2 texture paths resolve and all hashes match. |
| `interface/006_independence_wave_small_assets.gfx` | `GFX_portrait_DOX_prempeh_ii` and `GFX_portrait_SOK_muhammad_dikko`. | 2/2 texture paths resolve and all hashes match. |

The 2026-08-25 registry consolidation removed the former `interface/006_independence_wave_iw043_iw058_portraits.gfx`, `interface/006_independence_wave_mediterranean_portraits.gfx`, and `interface/006_independence_wave_region_01_portraits.gfx` files after preserving their definitions in `interface/006_independence_wave_portraits_registry.gfx`. No portrait key or runtime texture path changed in that move.

## Exact hash and file authority

The complete 38-row source filename → runtime filename → character/GFX key → SHA-256 matrix is retained in `006_portrait_wiring_supplied_runtime_2026_08_22.md`. The following revalidation results were obtained directly from the current filesystem:

- Source matrix parse: `safe=38`, `blocked=13`, `missing=0`.
- Source-to-runtime hash and DDS contract check: `safe=38`, `safe_bad=0`, `blocked=13`, `blocked_bad=0`, `missing=0`.
- Pairwise `.gfx` key plus texture-path check: `gfx_pair_checked=38`, `gfx_pair_bad=0`.
- The current source folder contains 110 DDS files; only the 51 exact filenames named by the user are in scope. The additional `_00001`/`_00002`, source-crop, and rejected-group variants were not substituted.

The 13 unresolved rows and their exact source SHA-256 values remain:

| Supplied DDS | SHA-256 | Fail-closed reason |
|---|---|---|
| `iw051_sakha_yak_anatoly_pepelyayev_research_2026_08_15__portrait_YAK_anatoly_pepelyayev_original_00002.dds` | `b01b99c37a3e636db8d860c59693daa735f4593548689ac498cfa70239de2c1b` | Vanilla `YAK_anatoly_pepelyayev` exists, but no admitted Event 006 replacement basename or portrait-specific consumer; a global vanilla override is out of scope. |
| `iw052_bya_ardan_markizov_source_research_2026_08_15__portrait_BYA_ardan_markizov_original_00002.dds` | `a75fc9449bb87cb1d5182cfbf5eb35a8033c016cae172bd9a828c9b0dac1a61f` | No Event 006 BYA character, live portrait consumer, or stable `.gfx` key. |
| `iw052_bya_mikhei_erbanov_source_research_2026_08_15__portrait_BYA_mikhei_erbanov_original_00002.dds` | `72c693e538dcca71ff90a125ef83358107388f147e8b3df8b25221110063a16e` | No Event 006 BYA character, live portrait consumer, or stable `.gfx` key. |
| `iw053_altai_grigory_gurkin_source_original_2026_08_15_00002.dds` | `0d0f4256d1b0bec248af91a34955c46053a6535f74e28f0e8ee441edeeba9ecd` | Vanilla `ALT_grigory_gurkin` exists, but no admitted Event 006 replacement basename or portrait-specific consumer. |
| `iw053_altai_samuil_yufit_source_original_2026_08_15_00002.dds` | `d52e9210c5e799f0a8373eca6952ace9067010d8ee15196ac15d051c921f6952` | Vanilla `ALT_samuil_yufit` exists, but no admitted Event 006 replacement basename or portrait-specific consumer. |
| `iw057_fer_alexander_krasnoshchyokov_source_original_00002.dds` | `d77715b47690703331f14551444ffe4ec3ff201078e3d43afc2705666923e84e` | No admitted FER character, portrait, or runtime consumer; IW-057 remains unadmitted. |
| `iw057_fer_pyotr_nikiforov_source_original_00002.dds` | `7aa7778130b9de37d1e6cecb98e4b70c5c1073ccbff29873702989332e241d95` | No admitted FER character, portrait, or runtime consumer; IW-057 remains unadmitted. |
| `iw060_kur_seyid_riza__portrait_kur_seyid_riza_original_00002.dds` | `5f5c00efac5524eb75f9aa172d63e0f0fd2c08ffcae2f777675d7fe8370ab1a1` | Vanilla `KUR_seyid_riza` exists, but no admitted Event 006 KUR consumer; a global override is out of scope. |
| `portrait_ACX_cornish_port_and_mines_committee_source_00002.dds` | `48755c4c9afe3c20ac9f98c1e9283ad0c976bccf6ee4af0fd8549351525acefd` | An ACX stub exists, but no live character or `.gfx` consumer was admitted. |
| `portrait_ARX_gioacchino_solinas_source_00002.dds` | `8e48f76061e93bca7343e6cb44be2078707292c240edab2f7c0a44a6484781b9` | Evidence-only identity with no admitted runtime consumer; relabelling another ARX person is unsafe. |
| `portrait_FIJ_ratu_sir_lala_sukuna_source_00002.dds` | `00d565861009060937e8ed1a32d2b76c77a80bb59450af6af5c4d3038cf2f542` | No Sukuna character or portrait consumer. |
| `portrait_FIJ_vishnu_deo_source_00002.dds` | `c9c5a7cdfecad00fe72d51e7365aad7edc7e0eaf9aa52fa9e884370ba6080b06` | No Vishnu Deo character or portrait consumer. |
| `portrait_GLC_alexandre_boveda_source_00002.dds` | `4f2a1208be9d4fa772596c9eba9aaa284d8d12ca7926c77da5355bd33e6bd32b` | Existing GLC consumer is Alfonso Daniel Castelao; no Bóveda character or stable key exists, and substitution would relabel a real person. |

## Source evidence, review, and skipped operations

- The durable source archive remains `docs/assets/portraits/006_independence_wave/` with its existing flat parent and single `processed/` child; no new portrait source subfolder or duplicate DDS was created.
- Existing original-source, crop, provenance, attribution, and rights evidence remains the authority for the grounded subjects. User-supplied DDS files do not create a new licence grant or clear unresolved rights/date gates.
- Matching canonical Vanilla leader, commander, and operative reference families were inspected at 156x210. The selected files satisfy the native dimensions and framing contract; this reconciliation makes no new same-person or HOI4-painted styled-final approval claim.
- No PNG outputs were created in this audit because the user supplied valid DDS runtime inputs and the repository already retains source/crop evidence.
- No DDS conversion was run because each selected input and each current runtime target already passes the required legacy BGRA header and exact-length contract. Re-conversion would create an unnecessary derivative.
- RunPod was not opened, operated, configured, queued, or monitored. Native ImageGen was not used because every selected subject is grounded.
- No HOI4 engine launch or MCP runtime-render claim was made; portrait texture and registry checks were performed statically.

## Changed files in this reconciliation

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_portrait_wiring_supplied_runtime_2026_08_22.md` — linked this current reconciliation as the latest audit.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_portrait_wiring_reconciliation_2026_08_30.md` — current exact reconciliation, registry ownership, hashes, validation, review result, and blockers.

No runtime portrait DDS or `.gfx` file required a change. The current working tree contains unrelated changes from other work; only the two files above are in this scoped change and must be committed together.
