# Event 006 NAV and GLC user-supplied portrait output audit

Status: `COMPLETE` for the bounded portrait audit and portrait-only runtime manifest update; Event 006 gameplay/package admission remains outside this handoff and is not cleared by the portrait result.

Date: `2026-08-26`.

## Scope and decision

The audited inputs were the three exact user-supplied `00002` DDS files in `C:\Users\klimp\Documents\ComfyUI Workflows\HOI4\hoi4_portraits_output\output\156x210\iw\dds\`, with their matching PNGs in the parent `iw` directory.

All three supplied pairs are painted `156x210` HOI4-style outputs rather than unchanged archival source crops. The NAV filename retains the historical `_source_placeholder_` token, but its pixels are a painted output and the token is not treated as a current placeholder state.

NAV/Aguirre and GLC/Castelao have exact existing Event 006 consumers and pass the portrait-specific file, pixel, framing, and consumer checks, so their stable runtime DDS files are retained and their portrait state is recorded as `styled_final` (user supplied).

GLC/Bóveda also passes the file and pixel checks, but no exact Event 006 character, stable runtime basename, or portrait `.gfx` consumer exists for him. It remains an unmapped user-supplied styled output and is not relabelled onto the Castelao consumer.

The GLC duplicate-identity package gate remains unresolved because vanilla `GLC - Galicia.txt` owns Alfonso Daniel Castelao as a country leader while the existing Event 006 character registry also owns the real person as an additive corps commander. This portrait-only handoff makes no transfer, reuse, or distinct-identity decision.

## Source and process evidence

Each matching PNG is an RGB `156x210` image with embedded `prompt` and `workflow` metadata. The workflow metadata records `workflow_id=hoi4_portrait_batch`, `revision=0`, `master_size=1024x1365`, `game_size=156x210`, `base_model=flux-2-klein-9b-fp8.safetensors`, `style_lora=hoi4_portrait_flux2_klein_9b_lora_000002500.safetensors`, `dds.format=A8R8G8B8`, `dds.mipmaps=false`, Adonis passes `adonis_base.safetensors` and `adonis_post.safetensors`, and frontend version `1.47.11`.

The prompt metadata records `Hoi4BatchInput`, the style instruction `make this portrait hoi4_portrait style`, `KSampler` seed `893029968453789` with four steps and Euler/simple sampling, and `Hoi4SaveDDS` `argb8888` output. No provider or job receipt was supplied in the inspected files, and no RunPod operation was performed by this worker.

The source-placeholder archive remains the attributed source and crop evidence; the user-supplied styled outputs were not copied into that archive. The existing flat archive contract is preserved: original source files remain directly under `docs/assets/portraits/006_independence_wave/`, `processed/` remains the sole child directory, and no source subfolder or duplicate final DDS archive was added.

## Supplied output ledger

| Candidate | Supplied PNG | PNG dimensions / hash | Supplied DDS | DDS hash / decoded RGBA hash | Runtime result |
| --- | --- | --- | --- | --- | --- |
| NAV / José Antonio Aguirre | `C:\Users\klimp\Documents\ComfyUI Workflows\HOI4\hoi4_portraits_output\output\156x210\iw\iw013_nav_jose_antonio_aguirre_source_placeholder_2026_08_13__portrait_NAV_jose_antonio_aguirre_original_00002.png` | `156x210` RGB; SHA-256 `96067c011e30ba720d4d11ad49e2067b1b4e1ffa0c86dd393ef30e3419ab9a4d` | `iw013_nav_jose_antonio_aguirre_source_placeholder_2026_08_13__portrait_NAV_jose_antonio_aguirre_original_00002.dds` | file SHA-256 `19bed96acca3728eaf7cb79f861b097f1e12c3af4fabab8962af843f6e16ac7c`; decoded RGBA SHA-256 `83f74be0afbaa042596284920324f3cb301328a4649dc214193155dc309f90b5` | Existing `gfx/leaders/006_independence_wave/portrait_NAV_jose_antonio_aguirre.dds` is 131168 bytes and byte-identical to the supplied DDS. |
| GLC / Alexandre Bóveda | `C:\Users\klimp\Documents\ComfyUI Workflows\HOI4\hoi4_portraits_output\output\156x210\iw\portrait_GLC_alexandre_boveda_source_00002.png` | `156x210` RGB; SHA-256 `f31915ef8dfae9356d239555bcc6b944b6300058a5c126df2f04d5c6a7d2bd3f` | `portrait_GLC_alexandre_boveda_source_00002.dds` | file SHA-256 `4f2a1208be9d4fa772596c9eba9aaa284d8d12ca7926c77da5355bd33e6bd32b`; decoded RGBA SHA-256 `9bc4aa35ccf5579925d352f99db37cb085488aa600014a8276cff72f8bbe626d` | Valid styled output, but no safe Event 006 consumer, runtime basename, or sprite exists; no copy or wiring was made. |
| GLC / Alfonso Daniel Castelao | `C:\Users\klimp\Documents\ComfyUI Workflows\HOI4\hoi4_portraits_output\output\156x210\iw\portrait_GLC_alfonso_daniel_castelao_source_00002.png` | `156x210` RGB; SHA-256 `5b99fdf9002e571a74d7e5d0b15ce3785f6e27cef878a69d55cde4706b418465` | `portrait_GLC_alfonso_daniel_castelao_source_00002.dds` | file SHA-256 `15f9ca69d7536439d2421dd8d55c96e94b5c56f9cdeb5ae5ee6a6210aaf25237`; decoded RGBA SHA-256 `7299c7af5cf5e6ada7dc01d448d11835f54c25e8b9f3da131c3888928f102537` | Existing `gfx/leaders/006_independence_wave/portrait_GLC_alfonso_daniel_castelao.dds` is 131168 bytes and byte-identical to the supplied DDS. |

All three PNG-to-DDS decoded pixel comparisons are equal. The exact supplied DDS files pass the legacy uncompressed portrait contract: `DDS ` magic, 124-byte header, width `156`, height `210`, pitch `624`, zero mipmaps, 32-bit pixel format, flags `65`, no FourCC compression, masks `0x00ff0000/0x0000ff00/0x000000ff/0xff000000`, `DDSCAPS_TEXTURE` `0x1000`, payload `131040` bytes, total `131168` bytes, and alpha range `255..255`.

The existing NAV and Castelao runtime DDS files were not rewritten because their bytes already match the supplied outputs. `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` conversion was therefore skipped for those two valid user-provided DDS files; no lossy or alternate conversion was introduced.

## Provenance and rights status

NAV Aguirre remains grounded in the archived Commons source page <https://commons.wikimedia.org/wiki/File:Jose_Antonio_Agirre,_Aberri_Eguna_1933.jpg> and direct media <https://upload.wikimedia.org/wikipedia/commons/2/2c/Jose_Antonio_Agirre%2C_Aberri_Eguna_1933.jpg>, credited to Pascual Marín, Marín Collection, GureGipuzkoa photo 1112433, Aberri Eguna 1933 in Donostia-San Sebastián.

The NAV source rights record remains `PASS_WITH_CAVEAT / NEEDS_USER_REVIEW` because the Commons page body and category state CC BY-SA 3.0 while the machine-readable license link advertises CC BY-SA 4.0. No public-domain or new redistribution claim is made for the styled derivative.

GLC Castelao remains grounded in the archived Commons source page <https://commons.wikimedia.org/wiki/File:Castelao_Vida_Gallega_442.png> and direct media <https://upload.wikimedia.org/wikipedia/commons/9/91/Castelao_Vida_Gallega_442.png>, a `Vida gallega` issue 442 scan dated 10 March 1930 from Galiciana/Biblioteca Dixital de Galiza with the original author recorded as unknown.

The Castelao source rights record remains `PASS_WITH_CAVEAT / NEEDS_USER_REVIEW` because Commons marks the scan Public domain / CC-PD-Mark while the original author and scan-chain jurisdiction remain unknown. No new rights status is inferred from the supplied styled output.

GLC Bóveda remains grounded in the archived Commons source page <https://commons.wikimedia.org/wiki/File:Alexandre_B%C3%B3veda_1933.jpg> and direct media <https://upload.wikimedia.org/wikipedia/commons/9/96/Alexandre_B%C3%B3veda_1933.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original>, credited to `Vida Gallega`, 20 March 1933, page 38.

The Bóveda source rights record remains `NEEDS_USER_REVIEW` because Commons records `CC-PD-Mark`, `PD-scan (PD-old-80)`, and author-died-more-than-80-years-ago categories while the underlying publication and jurisdiction chain still require independent review. Bóveda's 17 August 1936 execution date also keeps any country-leader use date-limited; the supplied portrait does not clear that gameplay gate.

## Framing and identity review

The supplied NAV output is a coherent painted head-and-shoulders portrait with Aguirre's swept hair, moustache, speaking expression, suit, lapel details, and hand gesture retained as recognizable identity cues from the archived source. Its full-canvas framing is valid for the existing corps-commander `army.large` consumer and aligns with the inspected vanilla commander and leader `156x210` reference sheets.

The supplied Castelao output is a coherent painted head-and-shoulders portrait with dark hair, round glasses, bow tie, and dark jacket retained as recognizable identity cues from the archived source. Its framing is valid for the existing corps-commander `army.large` consumer and aligns with the inspected vanilla commander and leader `156x210` reference sheets.

The supplied Bóveda output is a coherent painted head-and-shoulders portrait with frontal face, dark hair, suit, and red tie; its framing and pixels pass the same review, but no independent identity reviewer was assigned and no consumer admission is claimed.

The visual review was performed at native size and enlarged nearest-neighbour scale from decoded DDS pixels. No malformed alpha, edge loss, aspect-ratio drift, or DDS round-trip geometry change was observed. A separate independent rights/package reviewer remains unassigned.

## Consumer and wiring audit

The existing NAV consumer is `NAV_independence_wave_jose_antonio_aguirre` in `common/characters/006_independence_wave_characters_registry.txt`, using `army.large = GFX_portrait_NAV_jose_antonio_aguirre` as an existing `corps_commander`.

The existing GLC consumer is `GLC_independence_wave_alfonso_daniel_castelao` in `common/characters/006_independence_wave_characters_registry.txt`, using `army.large = GFX_portrait_GLC_alfonso_daniel_castelao` as an existing additive `corps_commander`.

The portrait registry keeps the stable definitions `GFX_portrait_NAV_jose_antonio_aguirre` and `GFX_portrait_GLC_alfonso_daniel_castelao` pointing to `gfx/leaders/006_independence_wave/portrait_NAV_jose_antonio_aguirre.dds` and `gfx/leaders/006_independence_wave/portrait_GLC_alfonso_daniel_castelao.dds` respectively.

The existing localisation keys `NAV_independence_wave_jose_antonio_aguirre`, `NAV_independence_wave_jose_antonio_aguirre_desc`, `GLC_independence_wave_alfonso_daniel_castelao`, and `GLC_independence_wave_alfonso_daniel_castelao_desc` remain accurate and were not changed.

The consumer search found no `Alexandre Bóveda`, `Alexandre Boveda`, `portrait_GLC_alexandre_boveda`, or `GFX_portrait_GLC_alexandre_boveda` consumer under current mod `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, or English localisation. The existing Castelao consumer is not a safe substitute.

Installed vanilla `GLC - Galicia.txt` creates `Alfonso Daniel Castelao` with `GFX_portrait_Alfonso_Daniel_Castelao`, so the duplicate real-person identity gate remains visible and unresolved; this handoff does not alter vanilla or mod gameplay files.

## Files changed

- `interface/006_independence_wave_portraits_registry.gfx` received a portrait-comment-only update identifying NAV Aguirre and GLC Castelao as user-supplied HOI4-style outputs while preserving both sprite names and texture paths.
- `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/manifest.md` received a dated amendment that separates the immutable source-placeholder archive from the supplied styled outputs and records current states, hashes, rights caveats, and blockers.
- `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/gfx_handoff.md` received a dated runtime handoff update for the two installed outputs and the unmapped Bóveda output.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_iw015_user_supplied_portrait_final_audit_2026-08-26.md` records this complete audit and evidence ledger.

No runtime DDS binary changed because the two unambiguous runtime files already matched the supplied final DDS byte-for-byte. No portrait-specific localisation, character, gameplay, package-admission, AI, decision, route, flag, event, or country-setup file was edited.

## Skipped checks and blockers

No RunPod or other external provider was opened, operated, configured, queued, or monitored. No HOI4 process was launched.

No `convert_to_dds.py` rewrite was needed because each supplied DDS passed the required header/pixel contract and NAV/Castelao already matched their runtime files exactly.

No provider/job receipt beyond the embedded ComfyUI PNG workflow metadata was supplied, so this handoff does not claim a provider identity or external job provenance.

No independent rights or likeness reviewer was assigned; the worker performed bounded native/enlarged framing and pixel review and records the unresolved rights caveats explicitly.

GLC package admission remains blocked by the existing duplicate Castelao identity ownership between the Event 006 additive corps commander and vanilla GLC country leader.

GLC Bóveda remains unmapped because no exact Event 006 consumer exists, and its date-limited availability and source-rights review remain unresolved.

No staging or commit was performed, per the parent task request.
