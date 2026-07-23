# IW-001 Scotland — Victor Fortune trial 01 independent asset audit

Audit scope is the source-locked real-person package at `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/scotland_fortune_trial_01/` from commit `c06f38736e7b76d8132116b0d17ce9d6f1b48d3f`.

Disposition: **source, provenance, role, and visual gates pass with disclosures; runtime admission remains on hold until the parent completes the IW-001 package gate and creates the final DDS**.

The subject is Major-General Sir Victor Morven Fortune, a grounded real male Scottish/Black Watch officer, and the proposed consumer is `SCO_independence_wave_territorial_commandant` as emergency head and army corps commander.

The [Commons record](https://commons.wikimedia.org/wiki/File:Fortune_Victor_Morven.jpg) identifies the unchanged 200x250 image as Victor Fortune, Imperial War Museum London, 1940, author unknown, and explicitly applies the public-domain mechanical-scan and UK-government (`PD-scan`/`PD-UKGov`) basis.

The [51st Highland Division archive record](https://51hd.co.uk/photos/img110) independently identifies the same man as Major General Fortune, dates the context to 12 June 1940, and records his Black Watch, 52nd (Lowland) Division, and 51st (Highland) Division commands; its `Copyright: IWM RML 342` line is retained as context provenance rather than asserted as a separate runtime licence.

The 1940 date is later than the 1936 scenario start and is correctly disclosed in the package; it must not be presented as an earlier uniform photograph.

The close master is `source_masters/SCO_victor_fortune_iwm_1940_portrait.jpg` (`200x250`, SHA-256 `830f175712988c825a604e48464584dc0b71cd61b51ab423e2badc0c1a46d049`).

The explicit head-and-shoulders crop is the complete unchanged rectangle `(0,0,200,250)` at `source_crops/SCO_victor_fortune_head_shoulders.jpg`, with the identical SHA-256, so crop provenance is exact even though the close source is low resolution.

The same-person context master is `source_masters/SCO_victor_fortune_51hd_mid_1940.jpg` (`580x609`, SHA-256 `6f2a686283bb796b6cd81003efd12a4c40135709eafee3c0e4e50e438f5f3392`) and is sufficient corroboration that the low-resolution close face is Fortune rather than a generic officer.

At full result size (`1086x1448`, SHA-256 `a9033e201a25a3d8412feab6d4b50480729e2adf3eb811820967c357f972e16f`), the edit preserves the broad rectangular face, heavy upper cheeks, deep-set asymmetric eyes, straight nose, firm closed mouth, compact moustache, strong jaw/chin, three-quarter pose, serious slightly weary expression, cap silhouette, and service-dress structure visible in both archival views.

At the processed `156x210` size, `processed_png/portrait_SCO_independence_wave_territorial_commandant.png` remains readable as the same broad-faced, moustached, cap-wearing officer and follows the full commander-portrait canvas; alpha is fully opaque.

No medals, text, flag, watermark, modern object, advisor frame, or `_small` treatment was added, and the restrained painted background and brush texture match the canonical HOI4 commander family inspected under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/`.

The cap badge is retained in the source position and broad silhouette with no added medal set, but its fine heraldic detail is necessarily reconstructed beyond a 200x250 source and remains the only visual-review uncertainty.

Age is period-consistent with the 1940 source, with only mild de-aging uncertainty at full result size; the direct source/context comparison does not show identity replacement, beautification, symmetry correction, or genericization.

Integrity checks match the manifest: processed PNG SHA-256 `aa9a8e267444dc01b49c942e2c2d74c4ed9c90fb12f7f38f5c0fcf26941cfb7d`, source/result sheet SHA-256 `a940c3b0b1d6585ff2aac934111d8f282ed67b5252919d19e7ff50357f0db86d`, archival/result sheet SHA-256 `0e10380de0a9b1021996c4fe7165801cbefc3339b50aa0debcde266a55554f2b`, and metadata artifact hashes agree with the files on disk.

The package preserves the prompt, unchanged source masters, generated result, processed PNG, two review sheets, manifest, and processor metadata as separate evidence files.

The metadata records `mode: leader` and the canonical `portraits/leaders` review directory even though the consumer is a corps commander; the output is visually commander-compatible, but the parent should correct or explicitly justify this role label before final acceptance.

The package contains no final DDS; this is correct for a candidate awaiting audit and means the asset is not complete under the ordinary runtime-asset completion gate.

The current runtime file `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant.dds` exists with SHA-256 `04d0ed792885b6149ec0eb5257e906b69279dd57cf52ead32d0f68b9230e8eaf` and a `2026-07-22 12:51` timestamp, predating this `23:10` trial commit; it is a stale prior runtime artifact, not this source-locked candidate.

`interface/006_independence_wave_region_01_portraits.gfx` still points the stable sprite `GFX_portrait_SCO_independence_wave_territorial_commandant` at that stale DDS, and no runtime/GFX/gameplay/localisation file was changed by this audit.

There is no current runtime `_small` sprite or `_small` DDS for this target, and the trial package has no advisor, dossier, high-command, theorist, or other derivative asset.

Exact and variant searches (`Victor Fortune`, `Victor Morven Fortune`, `victor_fortune`, `victor_morven_fortune`, `fortune_victor`) across installed vanilla `common/characters`, `history/countries`, `gfx/leaders`, `interface`, and `localisation`, plus the corresponding current Chaos Redux roots, found no pre-existing vanilla or current-project character/portrait owner; the local Event 006 token and sprite are the intended target consumer only.

Any same-person use in mutually exclusive reference mods is disclosure-only and grants no permission to copy art or source files; this package contains no such copied art/source.

If the parent accepts the disclosed cap-detail and processor-role uncertainties, convert only the processed PNG to the repository-standard `156x210` commander DDS, keep the runtime path guarded by the full IW-001 audit, and do not create advisor or `_small` derivatives.
