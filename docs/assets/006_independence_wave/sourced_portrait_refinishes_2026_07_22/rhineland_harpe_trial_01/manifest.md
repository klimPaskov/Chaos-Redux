# Josef Harpe source-locked portrait trial

Status: **candidate awaiting independent visual and provenance audit; not approved for runtime wiring**

This package contains one sourced real-male Rhineland army-command portrait candidate. It creates no advisor, dossier, `_small`, female, fictional, flag, focus, decision, localisation, gameplay, interface, or runtime asset.

## Subject and role

- Event 006 package: IW-008, Rhineland (`RHI` carrier).
- Stable role: `RHI_independence_wave_river_commandant`, army corps commander.
- Subject: Josef Harpe (1887-1968), German Army officer born in Buer, now Gelsenkirchen, North Rhine-Westphalia.
- Role basis: professional army and corps/army command experience; documented Rhineland-Westphalia birth connection.
- Ownership gate: the Event 006 source-research handoff reports no active vanilla or current Chaos Redux character ownership hit. This must be rechecked by the independent audit before approval.

## Archival source and rights

- Attribution page: <https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_146-1981-104-30,_Josef_Harpe.jpg>
- Archive original: <https://bild.bundesarchiv.de/device_barch/dev1/2022/11-28/b2/97/file7nthh588rkij6p2a22kj.jpg>
- Credit: `Bundesarchiv, Bild 146-1981-104-30 / Hoffmann, Heinrich / CC-BY-SA 3.0`.
- Date: 1943. This is later than the 1936 start and must remain disclosed.
- Local unchanged master: `source_masters/RHI_josef_harpe_bundesarchiv_original.jpg`.
- Unchanged master SHA-256: `5353200ABD3584C52A4938F2A79BF62C15D1BE6AAD22D70E0C45F1A4181C1384`.
- Explicit head-and-shoulders crop: `(90, 0, 4547, 6000)` from the `4637x7455` unchanged master.
- Crop SHA-256: `43C0B9A2F23A2253BE9F850EBA816672574B5B239498E1B10F48554F2E41B5E2`.

## Source-locked repaint

The original crop contains a Nazi emblem on the cap crown. The first direct ImageGen edit was rejected by the image safety system. The archival master and unaltered crop remain preserved. A separate moderation input neutralizes only that emblem using a feathered plain-dark cap patch. It is not source or identity evidence and is never a runtime asset.

- Moderation input: `source_crops/RHI_josef_harpe_head_shoulders_emblem_neutralized.png`.
- Moderation input SHA-256: `EA2156CD4C9BCFCF48881EE6004068E5B7D3ECA0463A98C524CB240BA9EDAA8A`.
- Style reference: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png`.
- Prompt: `prompts/RHI_josef_harpe_identity_preserve_trial_01.txt`.
- ImageGen source result: `imagegen_results/RHI_josef_harpe_identity_preserve_trial_01.png`.
- ImageGen source-result SHA-256: `7AD008E1DE5A57F77D10D4FB44FC1AFA76D3B451601AC6439B437A73086A8C`.
- Finish command: skill-local `retired_advisor_card_processor_REMOVED leader`, source kind `real`, explicit crop `(1, 0, 1081, 1454)`, canonical vanilla leader reference directory.
- Processed `156x210` PNG: `processed_png/portrait_RHI_independence_wave_river_commandant.png`.
- Processed PNG SHA-256: `D32AB4E289CC4BB9B2E98ADD0947E388BFD14A3F1040F390253D4AADDA755950`.
- Full comparison sheet: `contact_sheets/RHI_josef_harpe_full_source_result_comparison.png`.
- Processor comparison sheet: `contact_sheets/RHI_josef_harpe_source_result_reference.png`.
- Processor metadata: `metadata/RHI_josef_harpe_processing.json`.

The refinish retains Harpe's face, age, frontal pose, cap and uniform structure while replacing the neutralized cap-crown area with plain wool. The output must be rejected if independent review finds likeness drift, invented identity-bearing detail, insufficient HOI4 brushwork, an ownership collision, or an unacceptable source/rights gap.

## Runtime gate

Do not copy this candidate into `gfx/leaders/006_independence_wave/`, convert it to DDS, register or change a sprite, edit the character, or reopen IW-008 on this package alone. IW-008 also needs a separately approved sourced Karl Jarres civic portrait, exact runtime wiring, protected Matthes hash verification, and a fresh full country-package audit.
