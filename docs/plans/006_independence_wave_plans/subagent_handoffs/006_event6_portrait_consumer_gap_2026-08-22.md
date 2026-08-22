# Event 006 portrait-consumer gap handoff

Date: 2026-08-22.

Status: bounded portrait wiring tranche complete; Event 006 remains partial and fail-closed.

## Decision

Only `IW-051 YAK` Pavel Pevznyak was safe to map. The existing exact vanilla character and country-leader role are retained, the parent-owned identity/rights gate remains required, and the package remains absent from central admission, attestation, preflight, scenario, and Join surfaces.

No duplicate character, generic consumer, global vanilla override, package promotion, identity-gate setter, rights-gate setter, gameplay, localisation, event, country setup, or unrelated UI change was made.

## Exact safe mapping

| Package and identity | Existing exact consumer | Runtime output | Source and review state |
| --- | --- | --- | --- |
| `IW-051 YAK` Pavel Pevznyak | Vanilla `YAK_pavel_pevznyak` country leader in `common/characters/YAK.txt`, civilian large `GFX_portrait_Pavel_Pevznyak`; package roster already requires `has_character = YAK_pavel_pevznyak` and the parent-owned `independence_wave_iw_051_identity_rights_cleared` flag. | `gfx/leaders/006_independence_wave/portrait_YAK_independence_wave_pavel_pevznyak.dds`; `GFX_portrait_YAK_independence_wave_pavel_pevznyak`. | Existing grounded source package records identity, public-domain/provenance, crop/framing, and 1936 Sakha role/date passes. The supplied DDS is a byte-preserving source-placeholder runtime input and remains pending the existing parent/runtime review boundary. |

The new sprite is character-scoped through `set_portraits` only after `independence_wave_yak_roster_checkpoint` and the exact character check. Cleanup and setup retry restore `GFX_portrait_Pavel_Pevznyak` and clear `independence_wave_yak_portrait_override`.

## Source, provenance, and runtime evidence

The attributed source evidence remains under `docs/assets/portraits/006_independence_wave/` with all evidence flat and the only child directory `processed/`.

The Pavel source package is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw051_sakha_yak_portrait_source_research_2026_08_15.md` and its co-located provenance/manifest records the Wikimedia Commons page `https://commons.wikimedia.org/wiki/File:Pevznyak_Pavel_Matveevich_Trim.jpg`, the RGASPI Sakha credit, Public domain/CC-PD-Mark metadata, the 672x920 source master, the 672x905 exact crop, and the source-review crop equality evidence.

Supplied input: `C:/Users/klimp/Documents/ComfyUI Workflows/HOI4/hoi4_portraits_output/output/156x210/iw/dds/iw051_sakha_yak_pavel_pevznyak_source_placeholder_2026_08_15__portrait_YAK_pavel_pevznyak_original_00002.dds`.

The input and installed output are 156x210, 131168 bytes, uncompressed 32-bit BGRA DDS files with SHA-256 `7fcb0b641c7a390cc3f0c38a4028242e6248f24246d3d468ec2b80b99d910e6f`.

No PNG was created or retained, and `convert_to_dds.py` was not run because the user supplied a byte-valid DDS runtime input and the archive policy forbids retaining 156x210 derivatives.

## Changed files

- `common/scripted_effects/006_independence_wave_sakha_package_effects.txt` adds the gated YAK source portrait effect, setup-retry restoration, cleanup restoration, and override flag lifecycle.
- `interface/006_independence_wave_iw051_sakha_portraits.gfx` registers the dedicated runtime sprite.
- `gfx/leaders/006_independence_wave/portrait_YAK_independence_wave_pavel_pevznyak.dds` installs the supplied byte-preserving DDS.
- This handoff records the manifest, provenance, wiring, and unmapped dispositions; no source archive file was added or moved.

## Supplied identities left unmapped

All entries below were independently checked against the supplied `_00002.dds` inputs, exact installed-vanilla or project consumers, package specs, and collision boundaries. No supplied file below was copied or renamed.

| Supplied identity and DDS SHA-256 | Exact-consumer result | Precise blocker |
| --- | --- | --- |
| `IW-051 YAK` Anatoly Pepelyayev — `b01b99c37a3e636db8d860c59693daa735f4593548689ac498cfa70239de2c1b` | Vanilla `YAK_anatoly_pepelyayev` exists. | The source is a 1918 White Army portrait and the accepted evidence does not establish a 1936 Sakha country-leader role; the package roster correctly excludes this character. |
| `IW-052 BYA` Ardan Markizov — `a75fc9449bb87cb1d5182cfbf5eb35a8033c016cae172bd9a828c9b0dac1a61f` | No exact BYA Markizov character or portrait consumer exists. | The source package records Markizov as a period-valid regional officeholder/delegation member rather than the selected top regional leader, and the parent-owned BYA identity/rights decision remains open; no character or generic role was invented. |
| `IW-052 BYA` Mikhei Erbanov — `72c693e538dcca71ff90a125ef83358107388f147e8b3df8b25221110063a16e` | No exact BYA Erbanov character or portrait consumer exists. | The only source candidate is a group crop held for independent framing and jurisdiction-specific rights review; the package currently checkpoints installed `BYA_seymon_ignatyev`/`BYA_bidia_dandaron`, not a new Erbanov consumer. |
| `IW-053 ALT` Grigory Gurkin — `0d0f4256d1b0bec248af91a34955c46053a6535f74e28f0e8ee441edeeba9ecd` | Vanilla `ALT_grigory_gurkin` exists. | Archived source evidence marks unknown-rightsholder fair-use status and fails the exact 1936 Altai country-leader role/date; the identity/rights and Gurkin/Yufit roster gates remain fail-closed. |
| `IW-053 ALT` Samuil Yufit — `d52e9210c5e799f0a8373eca6952ace9067010d8ee15196ac15d051c921f6952` | Vanilla `ALT_samuil_yufit` exists. | Archived source evidence is unknown-rightsholder fair-use material dated after the 1936 opening and fails the exact 1936 Altai country-leader role/date; the identity/rights and roster gates remain fail-closed. |
| `IW-057 FER` Alexander Krasnoshchyokov — `d77715b47690703331f14551444ffe4ec3ff201078e3d43afc2705666923e84e` | No exact FER character or accepted portrait consumer exists. | IW-057 remains package-local and unadmitted, with no accepted institutional roster; the package explicitly does not create or reuse a character for this DDS. |
| `IW-057 FER` Pyotr Nikiforov — `7aa7778130b9de37d1e6cecb98e4b70c5c1073ccbff29873702989332e241d95` | No exact FER character or accepted portrait consumer exists. | IW-057 remains package-local and unadmitted, with no accepted institutional roster; the package explicitly does not create or reuse a character for this DDS. |
| `IW-060 KUR` Seyid Riza — `5f5c00efac5524eb75f9aa172d63e0f0fd2c08ffcae2f777675d7fe8370ab1a1` | Vanilla `KUR_seyid_riza` is the exact 1936 opening country leader. | The archived source is a strong role/date match but remains rights-review blocked because its author/source chain is not independently attributable; the parent-owned KUR identity/rights, map/capital, force, and package-admission gates remain untouched. |
| `IW-003 ACX` Cornish Port and Mines Committee — `48755c4a9afe3c20ac9f98c1e9283ad0c976bccf6ee4af0fd8549351525acefd` | No live ACX character or `.gfx` consumer exists. | ACX is a reserved dormant shell without a legal unique contiguous state binding or complete runtime package; the readiness-stub DDS cannot be promoted into a filler consumer. |
| `ARX` Gioacchino Solinas — `8e48f76061e93bca7343e6cb44be2078707292c240edab2f7c0a44a6484781b9` | No exact Solinas character or portrait consumer exists. | Existing ARX consumers are Emilio Lussu, Luigi Mella Santelia, and Gavino Piras/Verne; relabelling any of them would create a real-person identity collision. |
| `IW-177 FIJ` Ratu Sukuna — `00d565861009060937e8ed1a32d2b76c77a80bb59450af6af5c4d3038cf2f542` | No exact Sukuna character or portrait consumer exists. | The current FIJ consumer is an institutional founding-congress chair, while the strongest Sukuna source is circa 1940s and outside the strict 1936 gate; adapter-only status and source/date gates remain unchanged. |
| `IW-177 FIJ` Vishnu Deo — `c9c5a7cdfecad00fe72d51e7365aad7edc7e0eaf9aa52fa9e884370ba6080b06` | No exact Vishnu Deo character or portrait consumer exists. | The period source is not an accepted 1936 Legislative Council consumer and remains an anonymous/rights/role hold; the existing FIJ chair is not a safe substitute. |
| `IW-015 GLC` Alexandre Bóveda — `4f2a1208be9d4fa772596c9eba9aaa284d8d12ca7926c77da5355bd33e6bd32b` | No exact Bóveda character or portrait consumer exists. | The existing GLC consumer is Alfonso Daniel Castelao as a corps commander; relabelling that character or sprite would substitute a different real person, and GLC remains adapter-only. |

## Validation, review, and skipped checks

- Collision review found the new GFX key and runtime basename absent from the mod and vanilla trees before installation; the only exact YAK character owner is the installed vanilla `YAK_pavel_pevznyak`.
- The installed DDS header is `DDS ` with a 124-byte header, 156x210 dimensions, 624-byte pitch, no FOURCC compression, 32-bit RGBA masks, and exact file length `128 + 156*210*4`.
- The runtime texture path resolves from the new `.gfx` file, and the portrait effect applies only to the existing exact character after the package-local roster checkpoint.
- Setup retry and package cleanup restore the vanilla GFX token and clear the portrait override flag.
- Archive audit found only the existing `processed/` child directory, zero retained 156x210 files, and zero DDS files under `docs/assets/portraits/006_independence_wave/`.
- Source crop/framing review is inherited from the attributed Pavel provenance handoff; no source identity was generated, repainted, genericized, or substituted.
- No live HOI4 load, RunPod operation, ImageGen operation, MCP portrait inspection, or user-owned styled-final review was performed.

Remaining risk: the supplied DDS is installed as a source-placeholder runtime input, but the parent-owned IW-051 identity/rights clearance flag and all central Event 006 admission gates remain required before the package can use it in runtime.
