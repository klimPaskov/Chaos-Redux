# IW-043 CHU Mirsaid Sultan-Galiev independent portrait audit v83

Date: 2026-08-01 (Europe/Kyiv).
Reviewer: `/root/event6_chu_mirsaid_portrait_audit_v83`.
Scope: independent audit of the grounded real-person country-leader portrait evidence for `CHU_independence_wave_middle_volga_congress`.
Owned change: this handoff and the temporary package audit at `docs/assets/006_independence_wave/iw043_chu_portrait_source_v58_2026_08_01/audit_v83.md` only. No gameplay, character, localisation, `.gfx`, DDS, advisor, commander-small, or admission file was edited.

## Decision summary

The visual chain passes likeness, HOI4 painted leader style, crop/framing, male identity, artifact, source/crop linkage, era/role, and no-advisor gates. The overall portrait remains `needs_user_review` because the rights/public-domain release gate is held for final user/legal sign-off.

| Gate | Verdict | Exact evidence and finding |
| --- | --- | --- |
| Likeness / identity preservation | PASS | Source master `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/source_masters/volga/chu_mirsaid_sultan_galiev.jpg` (1200x1403 RGB, SHA-256 `4eb3707a50bb6d7ccf193773172b415dd4b1c4f83e09669dd9f2850972e46319`), exact crop, raw repaint, and candidate preserve the broad/high forehead, dark swept hair, strong brows, deep-set eyes, straight nose, narrow moustache, mouth, jaw, age, expression, and high-collared jacket at native and 4x inspection. No generic face or unsupported insignia was introduced. |
| HOI4 painted country-leader style | PASS | Raw `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaints_raw/CHU_middle_volga_congress_mirsaid_sultan_galiev_hoi4_repaint_v1.png` (1080x1456 RGB, SHA-256 `a59601b537e066865ae9151445f2f5389e91f273fc54272078479f0aed2f5a7`) and the 156x210 candidate use restrained painted planes, visible brushwork, muted brown/slate palette, quiet vignette, and readable facial values matching `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png` and the direct `afg_mohammed_zahir_shah.png` / `den_thorvald_stauning.png` references. |
| Crop / framing | PASS | Crop `docs/assets/006_independence_wave/iw043_chu_portrait_source_v58_2026_08_01/source_crops/CHU_middle_volga_congress_mirsaid_sultan_galiev_head_shoulders.png` is 1040x1400 RGB, SHA-256 `2404d3ee57a9047d3693f2f19e5c195c68ad72ef81729b73c89c2a26383c23a7`; JSON `docs/assets/006_independence_wave/iw043_chu_portrait_source_v58_2026_08_01/crop_metadata/CHU_middle_volga_congress_mirsaid_sultan_galiev_crop.json` proves Pillow decoded-pixel equality for `(100,0,1140,1400)`. Candidate is exactly 156x210 with head, shoulders, collar, and buttons inside the frame. |
| Male identity | PASS | Source, repaint, and candidate each show one adult male; there is no female presentation, extra subject, crowd, or ambiguous group. |
| Artifact screen | PASS | Native and 4x review found no text, watermark, logo, UI, border, duplicate face, fantasy feature, weapon, modern prop, or obvious generation seam. Candidate alpha range is 255-255. |
| Source provenance linkage | PASS | Source URL/file identity, Turkdirlik archive attribution, source hash, crop rectangle/equality JSON, raw hash, prompt, and candidate hash are linked in `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/manifest.md`, `docs/assets/006_independence_wave/iw043_chu_portrait_source_v58_2026_08_01/manifest.md`, the crop JSON, `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaint_plans/CHU_middle_volga_congress_mirsaid_sultan_galiev_hoi4_repaint_v1_prompt.md`, and `processing_metadata/CHU_middle_volga_congress_mirsaid_sultan_galiev_156x210.json`. The v58 ownership search records no current vanilla or Chaos Redux person/portrait owner. |
| Rights / public-domain release | HOLD — needs user review | The source ledger records Wikimedia Commons `SultanGaliyev0011.jpg`, `USSR` author, and `PD-Soviet/PD-Russia-2008`, but this package retains no independent Commons API/raw metadata snapshot and only the broad `before 1940` source-date record. Keep attribution and uncertainty attached; obtain final rights sign-off before DDS conversion or runtime admission. |
| Era / role fit | PASS with date uncertainty | The ledger identifies Mirsaid Sultan-Galiev as a Tatar/Volga revolutionary and political figure active before the 1936 baseline, fitting the Middle Volga Congress leader consumer. Exact photographic year is not pinned beyond pre-1940. |
| No advisor treatment | PASS | Prompt `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaint_plans/CHU_middle_volga_congress_mirsaid_sultan_galiev_hoi4_repaint_v1_prompt.md` forbids advisor treatment; processor `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/tools/normalize_mirsaid_portrait.py` performs only Lanczos scaling and RGBA conversion; metadata sets `advisor_art_authorized=false`. No 65x67 card, dossier frame, commander-small texture, or advisor sprite was created. |

## Required parent action

Keep the portrait at `needs_user_review`. Do not convert the candidate to DDS, replace `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_middle_volga_congress.dds`, change a `.gfx` sprite, or admit CHU until the rights/public-domain uncertainty is resolved. No fallback, generic portrait, advisor asset, or invented grounded-person likeness is authorized.

## Validation boundary

The audit independently recomputed source, crop, raw, and candidate dimensions/modes/hashes and decoded crop equality with Pillow. Native and 4x nearest-neighbour visual comparisons were performed against the supplied source chain and canonical leader references. No Hearts of Iron IV process, DDS conversion, live execution, save/load, or runtime wiring was run.

