# RHI Gustav-Adolf von Zangen source-locked portrait trial 01

Date: 2026-07-24.
Event/package: IW-008 Rhineland.
Stable consumer: `RHI_independence_wave_river_commandant`.
Source mode: `grounded_source_only`.
Status: `independently_approved_and_wired`.

## Mandatory transformation chain

The unchanged archival master is `source_masters/RHI_gustav_adolf_von_zangen_bundesarchiv_1944.jpg`, copied byte-for-byte from the attributed source package and retained at its native `548x800` grayscale JPEG dimensions.
Its SHA-256 is `B3A829FC739F43262057C91F146FF03561508708208C6F350A36158D4AF78C0D`.
The source is Bundesarchiv Bild 183-H28061, dated November 1944, with attribution `Bundesarchiv, Bild 183-H28061 / CC-BY-SA 3.0` under <https://creativecommons.org/licenses/by-sa/3.0/de/deed.en>.
The source page is <https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-H28061,_Westfront,_Gustav_v._Zangen,_Albert_Speer.jpg>.
The direct master is <https://upload.wikimedia.org/wikipedia/commons/9/99/Bundesarchiv_Bild_183-H28061%2C_Westfront%2C_Gustav_v._Zangen%2C_Albert_Speer.jpg>.

The explicit source-pixel crop is `source_crops/RHI_gustav_adolf_von_zangen_head_shoulders.png`, cropped from the master at `(180,140,365,330)` without resampling or retouching.
It is a native `185x190` grayscale PNG with SHA-256 `FC9C5F986F37C4F040A31F909FD5C03AF6C594D54BE295CA25373EAEC82C4D38`.

The official ImageGen repaint used the exact crop as the sole identity input.
The exact prompt is retained at `prompts/RHI_gustav_adolf_von_zangen_identity_preserve_trial_01.txt`.
The raw result is `imagegen_results/RHI_gustav_adolf_von_zangen_identity_preserve_trial_01.png`, native `1023x1537`, and its SHA-256 is recorded in `hashes.sha256`.
The prompt preserves face geometry, asymmetry, age, expression, hairline, pose, and uniform silhouette while neutralizing explicit political emblems, Nazi symbols, decorations, rank insignia, and award shapes into unmarked fabric.

The deterministic finish used `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py leader`, which is the repository's full `156x210` export mode for leaders and commanders.
The raw-result crop was `(0,100,1023,1477)`, `source_kind` was `real`, and the built-in processor sheet used canonical leader references only as a finishing control.
The processed candidate is `processed_png/portrait_RHI_independence_wave_river_commandant.png`, an opaque `156x210` RGBA image.
The exact processor record is `metadata/RHI_gustav_adolf_von_zangen_processing.json`.

## Independent-review evidence

`comparisons/RHI_gustav_adolf_von_zangen_identity_style_chain.png` shows the archival master, exact crop, raw repaint, processed candidate, and three canonical commander references.
`comparisons/RHI_gustav_adolf_von_zangen_native_4x_identity_comparison.png` shows the exact source crop, raw repaint, and processed candidate with nearest-neighbor enlargement for identity review.
`comparisons/RHI_gustav_adolf_von_zangen_processor_leader_review.png` is the deterministic processor review sheet.
The canonical commander references are `ger_erwin_von_witzleben.png`, `ger_erich_von_manstein.png`, and `ita_pietro_badoglio.png` under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/`.
Reference portraits are style evidence only and were not copied, recolored, traced, or used as identity sources.

## Role and ownership boundary

Zangen was alive in 1936, entered Wehrmacht service that year, had earlier service in the 9th Rheinische Infanterie-Regiment Nr. 160, and later held Westfront and 15th Army commands.
The alternate role is a Rhenish emergency river-corridor commandant, not a claim that he historically led the fictional RHI government.
The source is late-war evidence and its explicit political and award symbolism was deliberately neutralized; the person's face and uniform geometry remain the archival identity anchor.
The prior source research found no exact or variant owner in current Chaos Redux, installed vanilla, Kaiserreich `1521695605`, or approved references `2265420196` and `1458561226`.
The independent audit and transfer re-audit rechecked those roots and passed exclusive ownership for the stable Event 006 consumer.

`identity_transfer.md` records the parent-owned transfer of the stable generated Event 006 token from its prior Josef Harpe display identity to Gustav-Adolf von Zangen.
The English localisation implements that transfer while IW-008 remains fail-closed outside runtime content attestation.
The transfer creates no second historical character and authorizes only the token's existing full `civilian.large` and `army.large` consumers.
The independent visual audit is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_von_zangen_trial01_independent_audit_2026_07_24.md`.
The independent transfer re-audit is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_von_zangen_trial01_transfer_reaudit_2026_07_24.md`.
Together they pass provenance, exact identity, HOI4 commander style, role fit, and exclusive ownership for the authorized consumers.

## Runtime wiring

The approved PNG was converted to `final_dds/portrait_RHI_independence_wave_river_commandant.dds` and copied byte-identically to `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant.dds`.
Both DDS copies are legacy one-level opaque BGRA at `156x210`, SHA-256 `F8F99F0D3EF38601DA687B9A2CEA63EDBDE629017076E26E46B26B4B762E0DF2`, and decode pixel-identically to the approved PNG.
The stable sprite already points to the runtime path, and the male token uses only the approved `civilian.large` and `army.large` slots.
IW-008 remains outside runtime content attestation until a full post-wiring country-package audit passes.
No advisor, dossier, `_small`, high-command, theorist, operative, female, navy, alternate, or fallback asset is authorized.
