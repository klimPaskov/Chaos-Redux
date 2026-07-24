# Jules Destrée source-locked portrait trial 01

Status: **independently approved and wired to the existing full-size civic consumer**

This package contains one sourced real-male civic portrait candidate for IW-006 Wallonia. It contains no advisor, dossier, `_small`, female, fictional, flag, focus, decision, localisation, gameplay, interface, or runtime asset.

## Subject and role

- Event 006 package: IW-006, Wallonia (`AFX`).
- Stable role: `AFX_walloon_provisional_assembly`, civic country leader.
- Subject: Jules Destrée (1863-1936), Walloon movement leader, lawyer, minister, and an exact living Walloon civic identity in January 1936.
- Ownership gate: the existing Event 006 token already carries Jules Destrée's name. This is the intended same consumer, not a second character or transfer. Accepted source research found no separate active vanilla owner. Independent audit must recheck current ownership before approval.

## Archival source

- Commons page: <https://commons.wikimedia.org/wiki/File:Jules_Destr%C3%A9e_(1863-1936).jpg>.
- Publication: `Le Patriote Illustré`, 12 January 1936; author unknown.
- Rights basis recorded by the accepted source package: public-domain historical press image with explicit publication/date provenance.
- Unchanged master: `source_masters/AFX_jules_destree_1936.jpg`, `891x1216`.
- Master SHA-256: `8EB02ADFC33A4FB0BA5D2750B342993C0EA81139C48CEDBEE54516555EEEEA27`.
- Explicit head-and-shoulders/profile crop `(0, 0, 891, 1200)`: `source_crops/AFX_jules_destree_1936_head_shoulders.png`.
- Crop SHA-256: `0EBFA04EE442DE9971DB2F3584B0434682111166FF1173890D3C0C76CFA8502F`.

## Source-locked repaint

- Image 1: January 1936 Destrée identity/profile crop.
- Image 2 style-only reference: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`.
- Prompt: `prompts/AFX_jules_destree_identity_preserve_trial_01.txt`.
- Retained ImageGen result: `imagegen_results/AFX_jules_destree_identity_preserve_trial_01.png`.
- ImageGen result SHA-256: `B07EF2D6A77C6D4F86314638B7F352D3488B9F396E566E8B04D21298E49922B7`.
- Finish command: skill-local `advisor_icon_processing.py leader`, source kind `real`, explicit crop `(0, 1, 1080, 1455)`, canonical vanilla leader reference directory.
- Processed `156x210` candidate: `processed_png/portrait_AFX_walloon_provisional_assembly.png`.
- Processed candidate SHA-256: `7F1D43F8D3B350040B59630E44F1D7F8A7635883E7A067DCC5901ABDE2FC75BE`.
- Full source/result sheet: `contact_sheets/AFX_jules_destree_full_source_result_comparison.png`.
- Processor/style sheet: `contact_sheets/AFX_jules_destree_processor_style_comparison.png`.
- Processor metadata: `metadata/AFX_jules_destree_processing.json`.

The repaint intentionally preserves the source's strict left profile rather than reconstructing an unseen frontal face.

Independent audit: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_sco_wls_afx_civic_portrait_visual_provenance_audit_2026_07_22.md`.

- Source, role, and date: `PASS_WITH_RIGHTS_CAVEAT`.
- Identity and likeness at full and native size: `PASS`.
- HOI4 painted style: `PASS`.
- Ownership and consumer boundary: `PASS`.
- Approved consumer: `AFX_walloon_provisional_assembly` through `GFX_portrait_AFX_walloon_provisional_assembly`.
- Runtime DDS: `gfx/leaders/006_independence_wave/portrait_AFX_walloon_provisional_assembly.dds`.
- Runtime DDS dimensions and format: `156x210`, one-level uncompressed 32-bit BGRA, opaque alpha.
- Runtime DDS SHA-256: `7D8612CA9B6B82A1A4AE39156F9465891684345219BC3C7C8D84AB5A673DC75A`.
- Pixel verification: the runtime DDS decodes pixel-identically to the approved processed PNG.
- Rights caveat retained: the source is attributed to the 12 January 1936 issue of *Le Patriote Illustré*, author unknown, with the recorded Commons public-domain historical-press basis and unresolved territorial nuance.

## Runtime gate

This approved portrait is wired only to the existing full-size civic consumer. IW-006 remains closed until a sourced real Walloon army commander passes independent review, the fictional `Marcel Delcourt` commander identity is replaced with a role-correct researched man, exact runtime DDS files are pixel-verified, and a fresh full package audit passes. Albert Devèze is a civilian role mismatch; Émile Dossin de Saint-Georges remains rights/timing blocked; Victor van Strydonck de Burkel and Raoul Van Overstraeten are active vanilla-owned identities.
