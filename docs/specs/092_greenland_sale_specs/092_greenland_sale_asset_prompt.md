# Asset handoff: Event 092, Greenland Sale

Create the visual assets required by Parts 12 and 13 of `docs/specs/092_greenland_sale_specs/` after reading the full specification index, relevant gameplay parts, the preserved original brief, and current relevant repository sources.
Follow AGENTS, `chaos-redux-event-assets`, and the applicable icon and generated-art subagent definitions.
This is a production handoff, not evidence that art was generated during planning.
The package's reading report identifies external reference files that were not available or visually inspected.

## Reference and consumer gates

Read the canonical asset catalog and manifest, inspect the matching native-size contact sheets, and inspect each actual event, news, category, decision, inline-cost, and achievement consumer before choosing final framing or runtime dimensions.
Verify the current existing Greenland report, news, and category-picture sprites before preserving their names.
Their appearance and licensing were not audited in this planning pass.
Do not treat a filename or a search result as approval to reuse its image.

Use the project's original-source and processing rules.
For every alpha-backed icon or emblem, request native ImageGen transparency initially and preserve alpha through processing and DDS conversion, following the current asset skill.
Background removal is fallback-only and requires recorded edge review.
For fictional auction scenes, create original period-compatible art through the designated native image-generation route.
A genuine archival image may illustrate a generic harbor or construction scene only with relevant provenance, rights, and a clear distinction from a claim that the fictional sale occurred historically.
Do not assume a Danish seller or an American winner.
No final artwork may contain generated readable labels, modern interfaces, watermarks, or a fake transparency checkerboard.

## Planned visual set

The following are logical consumers and proposed identifiers.
Preserve verified existing identifiers where appropriate and record any necessary rename with all affected consumers.

| Asset | Consumer and direction | Canvas or gate |
| --- | --- | --- |
| A01 | Founding report, `GFX_report_event_greenland`, Arctic coastal possession and official auction material without national winner cues. | 210×176 processed documentary report card. |
| A02 | Reinvestment report, proposed `GFX_report_event_greenland_sale_reinvestment`, a real domestic construction consequence rather than a money reward. | 210×176 processed report card. |
| A03 | Greenland result news, existing `GFX_news_greenland_sold` subject to full consumer verification. | 397×153 black-and-white press image. |
| A04 | Consequential regional or strategic transfer news, proposed `GFX_news_greenland_sale_overseas_transfer`. | 397×153 black-and-white press image. |
| A05 | Homeland-sale result news, proposed `GFX_news_greenland_sale_homeland_transfer`, politically weighty border handover. | 397×153 black-and-white press image. |
| A06 | Category picture, existing `GFX_decision_cat_picture_greenland_sale`, unified map, contract, and industrial-backing identity. | Inspect consumer. The reference family is 114×101, not a universal runtime assumption. |
| A07 | Bid action, proposed `GFX_decision_greenland_sale_bid`, unmistakable bidding role. | 32×32 decision family after consumer inspection. |
| A08 | Reserve allocation, proposed `GFX_decision_greenland_sale_allocate`, civilian industry committed to an official purchase. | 32×32 decision family. |
| A09 | Listing action, proposed `GFX_decision_greenland_sale_list`, a specific territorial parcel offered publicly. | 32×32 decision family. |
| A10 | Construction redemption, proposed `GFX_decision_greenland_sale_reinvest`, useful construction from paid proceeds. | 32×32 decision family. |
| A11 | Follow or inspect a lot, proposed `GFX_decision_greenland_sale_follow`, attention to an identified auction. | 32×32 decision family. |
| A12 | Industrial Reserve inline cost icon, proposed `GFX_greenland_sale_industrial_reserve`, visually distinct from PP and native market capacity. | Verify actual inline-cost consumer and small-icon reference. |
| A13–A16 | Four achievement subjects using the exact IDs and conditions in Part 13 and the achievement prompt. | 64×64 source layers and all required runtime triplets. |

The plan contains 16 original visual subjects or compositions, including four achievement subjects.
If all four new achievement subjects are produced through the standard three-state workflow, the complete set has 24 final DDS textures.
These are planned counts, not files already generated.
Native cancel and standard category controls can retain their verified existing artwork rather than acquiring decorative duplicates.

## Achievement production

Use the exact achievement IDs `092_greenland_sale_arctic_development`, `092_greenland_sale_productive_withdrawal`, `092_greenland_sale_connected_acquisitions`, and `092_greenland_sale_homeland_recovery`, subject to collision and registry checks.
Generate one original transparent subject per achievement, with no frame, square background, cross, or text.
Process it into one centered 64×64 color source layer.
Create the grey source deterministically from that layer, preserving position and alpha.
Create the not-eligible source from the grey source with the unchanged canonical overlay at exact alignment.

Use the canonical workflow inputs without alteration:

```text
assets/gfx_references/icons/achievements/template/achievement_template.png
assets/gfx_references/icons/achievements/template/achievement_template_grey.png
assets/gfx_references/icons/achievements/template/overlay.png
```

Verify their hashes against the current supplied skill before use.
Pass all three complete source layers to `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py`.
A single source image is not a valid complete processor input.
Do not regenerate the three visual states independently or feed a previously templated output back as an untreated source.

Final achievement paths are directly under `gfx/achievements/`, using the full registered ID plus `.dds`, `_grey.dds`, and `_not_eligible.dds`.
Do not create an event subfolder for those runtime textures.
Keep the achievement registry's actual root-level ownership and unique-ID convention intact.

## Processing and evidence

Process report images through `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` with the approved documentary tilt, transparent corners, shadow, and sepia black-and-white treatment.
Use the canonical `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` for the other applicable texture conversions.
Do not silently substitute an unrelated converter when a required tool is unavailable or fails.
Achievements use their own canonical processor and its strict composition checks.

Keep event-scoped non-achievement textures under the appropriate existing asset-category folder with the `092_greenland_sale` event folder.
Do not invent an extra project-namespace directory.
The main agent owns final sprite and consumer wiring unless an explicit handoff delegates it.
Provide exact sprite-to-texture, consumer-to-sprite, and achievement-ID-to-triplet relationships.

Retain native source PNGs or archival sources, prompts or URLs, licenses, source-mode rationale, processed PNGs, complete achievement source triplets, review PNGs, hashes, native-size contact sheets, decoded DDS comparisons, and any blocked or needs-review state.
Verify final dimensions, alpha, codec, mip behavior, and pixel alignment according to the skill, not merely by reading a DDS header.
Preview small icons at actual size against relevant backgrounds.
Inspect the actual category consumer and render the assembled presentation through the connected GUI tools when available.

## Completion boundary

Do not produce flags, portraits, focus icons, 3D units, animations, new interface windows, or super-event art without an accepted design amendment that needs them.
Do not hide missing consumer inspection, reference files, licensing, native-size visual review, or game evidence behind a completed asset count.
Keep blocked production material in the event's documented asset workspace until the package is actually accepted and promoted.
Return a consumer-complete manifest and an honest review report to the parent.
