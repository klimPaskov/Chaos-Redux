# 12. Asset manifest and consumers

All asset identifiers in this manifest are proposed stable identifiers. Descriptive labels are working labels, not final localisation. Every row is planned, not generated or validated.

## Required assets

| Asset family and ID | Count | Final size | Proposed path | Consumer and visual role |
| --- | --- | --- | --- | --- |
| `the_master_report_opening` | 1 | 210×176 | `gfx/event_pictures/079_the_master/the_master_report_opening.dds` | Opening diplomatic report, external powers competing around a small state |
| `the_master_report_alignment` | 1 | 210×176 | `gfx/event_pictures/079_the_master/the_master_report_alignment.dds` | Government realignment report, institutional change without a fabricated identifiable leader |
| `the_master_report_takeover` | 1 | 210×176 | `gfx/event_pictures/079_the_master/the_master_report_takeover.dds` | Winner and target reports, establishment of a dependent government |
| `the_master_news_takeover` | 1 | 397×153 | `gfx/news_event_pictures/079_the_master/the_master_news_takeover.dds` | Black-and-white international diplomatic news |
| `the_master_category` | 1 | Native category consumer size to verify | `gfx/decisions/079_the_master/the_master_category.dds` | Category emblem distinct from the action icons |
| `the_master_propaganda` | 1 | 32×32 | `gfx/decisions/079_the_master/the_master_propaganda.dds` | Public political persuasion |
| `the_master_investment` | 1 | 32×32 | `gfx/decisions/079_the_master/the_master_investment.dds` | Factory or public-works commitment |
| `the_master_military_aid` | 1 | 32×32 | `gfx/decisions/079_the_master/the_master_military_aid.dds` | Material and advisory military assistance |
| `the_master_government` | 1 | 32×32 | `gfx/decisions/079_the_master/the_master_government.dds` | Incumbent support |
| `the_master_opposition` | 1 | 32×32 | `gfx/decisions/079_the_master/the_master_opposition.dds` | Opposition organization |
| `the_master_interference` | 1 | 32×32 | `gfx/decisions/079_the_master/the_master_interference.dds` | Targeted rival operation |
| `the_master_foreign_campaigns` | 1 | 64×64 | `gfx/ideas/079_the_master/the_master_foreign_campaigns.dds` | One consolidated target campaign spirit where an idea is actually needed |
| Event-owned board decorative elements | Native pieces only as needed | Fit actual UI consumer | `gfx/interface/079_the_master/` | Reuse native bars, frames, flags, and buttons before adding new textures |
| Six achievement subjects | 6 source subjects, 18 runtime states | 64×64 final | `gfx/achievements/<achievement_id>.dds`, `_grey.dds`, `_not_eligible.dds` | Shared achievement registry and eligibility display |

A sponsor's factory commitment can use an event-owned dynamic modifier if the installed consumer supports the required reservation. It must be visible in the payment UI. Do not add one visible national spirit per target and another per action. Consolidate event-owned visible status to stay within the project's three-spirit ceiling for a package on a country.

## Source and production modes

Generated symbolic art is appropriate for the action icons, category emblem, idea icon, achievement subjects, and non-identifying alternate-history report scenes. Existing native country flags and leader portraits supply country identity. Do not generate a historical person's face to fill a generic diplomatic image. Report scenes must not contain fake text, slogans, country names, Influence bars, or an HOI4 window, and the black-and-white news crop must remain readable at 397×153.

Reference inspection, native transparency, processing, DDS conversion, achievement triplet derivation from the immutable templates, and the production manifest all follow [the current asset contract](../../../../.agents/skills/chaos-redux-event-assets/SKILL.md). Each icon must remain distinct from the other action families at its 32-pixel display size. The art worker delivers paths, sizes, conversions, and a contact sheet; the parent owns runtime sprite registration.
