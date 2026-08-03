# Event 012 priority-member male portrait source re-audit

Scope: source-only review of the sixteen priority-member sovereign portraits after the male-only, dramatic-but-grounded direction. No gameplay, character, localisation, or `.gfx` file was edited.

## Runtime conclusion

The current runtime gate is sufficient for the accepted implementation surface: the three promoted historical male rows are Kanem-Bornu (`GFX_portrait_012_africa_priority_kanem_bornu_sovereign`), Harar (`GFX_portrait_012_africa_priority_harar_sovereign`), and Kongo (`GFX_portrait_012_africa_priority_kongo_sovereign`). Their runtime files remain the separately reviewed source-locked HOI4-style repaints documented by the parent handoff. The six fictional high-chaos portraits (Pan, Gorilla Kingdom, The Green, Living Rivers, Stoneborn, and Ancient Hosts) are already clearly classified and remain dormant model-required assets; they must not fill historical rows.

## High-confidence source candidates found

- Buganda: Daudi Cwa II, named in Jules Leclercq's 1913 public-domain plate. Exact source crop and evidence files are present. It still needs a source-locked repaint and independent review before promotion.
- Merina: Radama II, named male subject in a circa-1862 USC Libraries portrait. This is the safe male replacement candidate for the earlier female Ranavalona III row, but outside-US rights and actor/date eligibility remain open.
- Sokoto: Sir Siddiq Abubakar III, named 1959 Eliot Elisofon/Smithsonian image. Identity is strong, but Smithsonian permission metadata blocks promotion.
- Lunda: Mwaantayaav Mbaku Citend, named 1957 Daniel Biebuyck photograph. Identity and visible regalia are documented; photographer permission is required.
- Luba: Albert Kalonji, named circa-1960 portrait. Rights/provenance are not strong enough for promotion without review.
- Zulu: Dinuzulu kaCetshwayo, named March 1908 James Stuart CC0 photograph. Source is strong, but actor eligibility is blocked and this row must never be relabelled Solomon kaDinuzulu.

## Explicit blockers

Asante is blocked by Event 006 ownership for Prempeh II and uncertain individual placement in the Prempeh I group image. Oyo's OGL image names only the office and obscures the rider's face. Manden, Aksum, Kilwa, Nubia, and Great Zimbabwe have no defensible named male photographs for their pre-photography identities. No fictional or generic portrait is an acceptable substitute.

## Exact package outputs

- Machine-readable source manifest: `docs/assets/012_africa_world_order/manifests/012_africa_priority_male_portrait_sources_manifest.json`.
- Rights and uncertainty notes: `docs/assets/012_africa_world_order/manifests/012_africa_priority_male_portrait_sources_licence_notes.md`.
- Source evidence/GFX handoff: `docs/assets/012_africa_world_order/gfx_handoff.md` (historical male section appended; fictional section retained).
- Candidate contact sheet: `docs/assets/012_africa_world_order/contact_sheets/portraits/priority_male_source_candidates_contact_sheet.png`.
- Source masters, exact crop JSON, processed 156x210 PNG evidence, and converter-produced DDS evidence are under `docs/assets/012_africa_world_order/{source_masters,source_crops,processed_png,final_dds}/portraits/`.

All evidence DDS files are deliberately outside the runtime `gfx/leaders/` tree. The parent owns any future repaint, `.gfx` wiring, character identity change, and actor eligibility decision.
# Superseding parent note (2026-08-03)

The source-only review below is retained as dated provenance. The current parent tranche has sourced and installed direct source placeholders for all sixteen male-only identities, including Mansa Musa's Catalan Atlas image, the Kilwa 1572 map panel, the Taharqa statue reconstruction, the Great Zimbabwe Bird artifact, the Oyo office photograph, and Radama II. See `docs/assets/portraits/012_africa/source_locked_runtime_mapping.md` for the current runtime map and explicit artifact/map identity treatment.
