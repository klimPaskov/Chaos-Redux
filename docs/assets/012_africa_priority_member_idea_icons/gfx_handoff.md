# GFX handoff â€” Event 012 Africa priority-member idea icons

The sprite registrations already exist in `interface/012_africa_priority_member_assets.gfx`; this asset subagent did not edit that file. Keep the existing sprite names and texture paths exactly as registered.

Suggested target file: `interface/012_africa_priority_member_assets.gfx` (already registered).

Texture root: `gfx/interface/ideas/012_africa/priority_members/`.

Target size: 60x68 pixels, one-level uncompressed 32-bit BGRA DDS with alpha. All 35 paths below resolve and have decoded-pixel equality with their processed PNGs.

```text
GFX_idea_africa_priority_council_settlement -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_council_settlement.dds
GFX_idea_africa_priority_civic_settlement -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_civic_settlement.dds
GFX_idea_africa_priority_producer_settlement -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_producer_settlement.dds
GFX_idea_africa_priority_asante_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_asante_problem.dds
GFX_idea_africa_priority_asante_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_asante_mature.dds
GFX_idea_africa_priority_oyo_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_oyo_problem.dds
GFX_idea_africa_priority_oyo_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_oyo_mature.dds
GFX_idea_africa_priority_sokoto_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_sokoto_problem.dds
GFX_idea_africa_priority_sokoto_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_sokoto_mature.dds
GFX_idea_africa_priority_kanem_bornu_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_kanem_bornu_problem.dds
GFX_idea_africa_priority_kanem_bornu_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_kanem_bornu_mature.dds
GFX_idea_africa_priority_manden_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_manden_problem.dds
GFX_idea_africa_priority_manden_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_manden_mature.dds
GFX_idea_africa_priority_kongo_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_kongo_problem.dds
GFX_idea_africa_priority_kongo_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_kongo_mature.dds
GFX_idea_africa_priority_buganda_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_buganda_problem.dds
GFX_idea_africa_priority_buganda_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_buganda_mature.dds
GFX_idea_africa_priority_aksum_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_aksum_problem.dds
GFX_idea_africa_priority_aksum_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_aksum_mature.dds
GFX_idea_africa_priority_harar_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_harar_problem.dds
GFX_idea_africa_priority_harar_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_harar_mature.dds
GFX_idea_africa_priority_kilwa_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_kilwa_problem.dds
GFX_idea_africa_priority_kilwa_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_kilwa_mature.dds
GFX_idea_africa_priority_nubia_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_nubia_problem.dds
GFX_idea_africa_priority_nubia_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_nubia_mature.dds
GFX_idea_africa_priority_luba_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_luba_problem.dds
GFX_idea_africa_priority_luba_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_luba_mature.dds
GFX_idea_africa_priority_lunda_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_lunda_problem.dds
GFX_idea_africa_priority_lunda_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_lunda_mature.dds
GFX_idea_africa_priority_great_zimbabwe_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_great_zimbabwe_problem.dds
GFX_idea_africa_priority_great_zimbabwe_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_great_zimbabwe_mature.dds
GFX_idea_africa_priority_merina_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_merina_problem.dds
GFX_idea_africa_priority_merina_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_merina_mature.dds
GFX_idea_africa_priority_zulu_problem -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_zulu_problem.dds
GFX_idea_africa_priority_zulu_mature -> gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_zulu_mature.dds
```

Main-agent action: no sprite-definition changes are needed unless a registration diff is intentionally introduced later. If any texture is replaced, rerun the two validation scripts in `validation/` and update the manifest/provenance hash evidence.
