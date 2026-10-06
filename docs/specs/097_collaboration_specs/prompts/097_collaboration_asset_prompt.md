# Event 097 Collaboration: Asset Prompt

Use `chaos-redux-event-assets` for every asset in this prompt. Route production through the project subagents named in that skill: `chaosx_generated_event_art` for report, super-event, and category-picture art, and `chaosx_icon_artist` for decision, decision-category, idea, and achievement icons. Every subagent prompt must be self-contained and carry the paths, names, sizes, and rules below.

Read the accepted design before producing anything:

- `docs/specs/097_collaboration_specs/specs/097_collaboration_spec_part_1_core.md`
- `docs/specs/097_collaboration_specs/specs/097_collaboration_spec_part_2_evolutions.md`
- `docs/specs/097_collaboration_specs/specs/097_collaboration_spec_part_3_occupation_capitulation_and_governments.md`
- `docs/specs/097_collaboration_specs/specs/097_collaboration_spec_part_4_decisions_and_responses.md`
- `docs/specs/097_collaboration_specs/specs/097_collaboration_spec_part_6_ai_presentation_achievements.md`

## Global rules

- Inspect the matching canonical reference family and its contact sheet before generating each family. The current skill places the library under `.agents/skills/chaos-redux-event-assets/assets/gfx_references/`, and this checkout still holds it under `assets/vanilla_reference/` in the same skill folder.
- All art is fictional, period-documentary in feel for 1936 to 1945, and shows no real person, no real collaborator, no readable text, and no identifiable real national insignia of a foreign occupying army. Local flags may appear only as unreadable shapes.
- The subject is ordinary people changing sides: officials, police, clerks, managers, local politicians. Do not make paperwork, archives, maps, or staff tables the main subject. Do not depict violence against civilians.
- Icons use native ImageGen transparency, keep the alpha through processing and DDS conversion, and are each designed for their own consumer. Never resize one icon type into another.
- Report images are generated as photographs and then processed locally with the report-event card processor into the `210x176` tilted card.
- Every asset receives a manifest entry, a processed PNG preview, a final DDS, a contact sheet where several assets share a family, and a `gfx_handoff.md` entry. The temporary workspace is `docs/assets/097_collaboration/`.
- All assets are static, because each surface communicates its state through text and a single image.
- Register sprite names in the owning `.gfx` files before requesting art so filenames do not change later.

## Report event images

Size `210x176`, generated, processed with `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`. Final folder `gfx/event_pictures/097_collaboration/`.

| Asset | Sprite | Use | Direction |
| --- | --- | --- | --- |
| `report_event_097_collaboration_opening` | `GFX_report_event_097_collaboration_opening` | Opening report, ordinary variant | A provincial railway station waiting room. A local policeman and a civilian stranger in a good coat share a cigarette on a bench and both watch the platform. Quiet, ordinary, slightly wrong. |
| `report_event_097_collaboration_deep_networks` | `GFX_report_event_097_collaboration_deep_networks` | Deep Networks report and pre-fire opening variant | A factory gate at dawn. A plant manager and a police director talk with a well-dressed visitor while workers pass without looking. |
| `report_event_097_collaboration_seat` | `GFX_report_event_097_collaboration_seat` | Seat report | Town hall steps. District officials in suits wait with a ring of keys as a column of soldiers in nondescript field uniforms enters the square. |
| `report_event_097_collaboration_open_ministries` | `GFX_report_event_097_collaboration_open_ministries` | Open Ministries report | A ministry entrance on a grey morning. Clerks arrive for work and pass sentries in unfamiliar uniforms without breaking stride. |
| `report_event_097_collaboration_fifth_column` | `GFX_report_event_097_collaboration_fifth_column` | Fifth Column spirit acquisition report | A government office with coats still on chairs, a telephone receiver hanging off its desk, and one official in the doorway with his hat on, leaving. |
| `report_event_097_collaboration_open_gates` | `GFX_report_event_097_collaboration_open_gates` | Open Gates reports | A road barrier on the edge of a small town lifted and tied open. Two local gendarmes stand to one side. Distant vehicles approach. |
| `report_event_097_collaboration_prepared_government` | `GFX_report_event_097_collaboration_prepared_government` | Prepared Government event | A requisitioned hotel lobby. A group of civilian politicians in overcoats waits on sofas. Officers of an unnamed army stand at the reception desk. |
| `report_event_097_collaboration_turned_regime` | `GFX_report_event_097_collaboration_turned_regime` | Turned Regime reports | An official in front of a mirror removing one armband and holding another. |
| `report_event_097_collaboration_unmasked` | `GFX_report_event_097_collaboration_unmasked` | Collaborators Unmasked | A courtyard where returning soldiers question a row of seated local officials. Restrained, no violence shown. |

## Super-event image

| Asset | Size | Sprite | Final folder | Direction |
| --- | --- | --- | --- | --- |
| `super_event_097_competing_orders` | `457x328` | `GFX_super_event_097_competing_orders`, registered in `interface/chaosx_super_events.gfx` | the super-event image folder used by existing Chaos Redux super-events | A formal ceremony in a provincial government hall. A newly installed local cabinet stands beneath a flag shape of its own country. Officers of an unnamed foreign army stand at the edge of the frame. Strong central composition and enough contrast for the super-event frame. |

The super-event image is coordinated with `docs/specs/097_collaboration_specs/prompts/097_collaboration_super_event_prompt.md`.

## Decision category picture

| Asset | Consumer | Sprite | Direction |
| --- | --- | --- | --- |
| `decision_category_097_collaboration_divided_loyalties_picture` | Divided Loyalties category picture | `GFX_decision_category_097_collaboration_divided_loyalties_picture` | A ministry corridor at night. A few officials work by lamplight. At the end of the corridor one figure waits by a half-open door. No buttons, meters, or text. |

Inspect the decision-category picture reference family and its `contact_sheet.png` first. The current skill names it `assets/gfx_references/icons/decision_categories/pictures/`, and this checkout holds it at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures/`. Use whichever folder exists when the picture is produced. If the contact sheet is missing, create it, label each reference with filename and native dimensions, and update the reference README and catalog before producing the picture. The reference family uses `114x101`, but the final size follows the active category-picture consumer the implementation agent wires.

## Decision category icons

| Asset | Sprite | Direction |
| --- | --- | --- |
| `decision_category_097_collaboration_divided_loyalties` | `GFX_decision_category_097_collaboration_divided_loyalties` | A lapel badge split into two halves of different colours |
| `decision_category_097_collaboration_prepared_governments` | `GFX_decision_category_097_collaboration_prepared_governments` | An empty armchair behind a desk under a hanging lamp |

Use the decision-category consumer size of the active Chaos Redux category surface.

## Decision icons

Size `32x32`, transparent. Final folder `gfx/interface/decisions/097_collaboration/`.

| Asset | Decision | Direction |
| --- | --- | --- |
| `decision_097_collaboration_loyalty_commissions` | A1 | A desk lamp turned toward an empty chair |
| `decision_097_collaboration_arrest_officials` | A2 | A pair of handcuffs over an official's hat |
| `decision_097_collaboration_evacuate_ministries` | A3 | A covered truck loaded with crates |
| `decision_097_collaboration_commissars` | A4 | An officer's cap resting on a civilian desk |
| `decision_097_collaboration_charter_exile` | A5 | A suitcase in front of a ship's silhouette |
| `decision_097_collaboration_seat_government` | B1 | A ceremonial sash laid across a chair |
| `decision_097_collaboration_arm_administration` | B2 | A rifle beside a plain armband |

## Idea and national spirit icons

Size `64x64`, transparent. Final folder `gfx/interface/ideas/097_collaboration/`.

| Asset | Spirit | Direction |
| --- | --- | --- |
| `idea_097_collaboration_vetting_campaign` | Vetting Campaign | A magnifier over a row of identity photographs, small and plain |
| `idea_097_collaboration_loyalty_commissions` | Loyalty Commissions | Three chairs facing one table under a single lamp |
| `idea_097_collaboration_fifth_column` | Fifth Column | Four marching silhouettes outside a wall and a fifth inside it |
| `idea_097_collaboration_imposed_administration` | Installed Administration, Imposed | A sash on a stiff collar, with a hand on the shoulder from outside the frame |
| `idea_097_collaboration_entrenched_administration` | Installed Administration, Entrenched | A comfortable office chair with a coat hung on it |
| `idea_097_collaboration_contested_administration` | Installed Administration, Contested | A sash pulled from two sides |
| `idea_097_collaboration_abandoned_administration` | Installed Administration, Abandoned | An empty office with an open window and papers blowing out |
| `idea_097_collaboration_purge` | Purge penalty after Collaborators Unmasked | A row of empty office desks with their name plates turned face down |

The Fifth Column spirit uses one icon for every band, because the band name carries the state. The prepared-cadres state modifier from Part 3 and the Amnesty state modifier from Part 4 need state-modifier icons from the matching reference family:

| Asset | Use | Direction |
| --- | --- | --- |
| `state_modifier_097_collaboration_prepared_cadres` | Prepared cadres state modifier | A ring of keys on a nail beside a door |
| `state_modifier_097_collaboration_amnesty` | Amnesty state modifier after Collaborators Unmasked | A desk lamp still lit in a damaged office, with a coat on the chair |

## Achievement icons

Follow the achievement workflow in `chaos-redux-event-assets` exactly: one generated transparent subject per achievement, then the deterministic grey and not-eligible states built with `process_achievement_icons.py`. Final DDS files go directly under `gfx/achievements/` as `<id>.dds`, `<id>_grey.dds`, and `<id>_not_eligible.dds`, with sprites `GFX_achievement_<id>`, `GFX_achievement_<id>_grey`, and `GFX_achievement_<id>_not_eligible` registered in `interface/chaosx_achievements.gfx`. The ids below follow the repository convention `<id>_<slug>_<name>`. The implementation agent confirms that none collides with an existing id before production.

| Achievement key | Motif |
| --- | --- |
| `097_collaboration_open_doors` | A row of three open doors, each with light spilling out, on a dark ground |
| `097_collaboration_clean_ministries` | A closed ministry door with a heavy bar across it |
| `097_collaboration_three_continents` | Three small flagpoles on a globe without readable flags |
| `097_collaboration_turned_regime` | A ceremonial armband split between two colours |
| `097_collaboration_return_from_exile` | A suitcase with travel labels on a desk in front of a window |
| `097_collaboration_quiet_capitulation` | A telephone receiver off its cradle on a field desk |

## Manifest and coverage

Before completion, build the requirement-to-runtime crosswalk from every row above: requirement, source package, final DDS, sprite, owning `.gfx`, live consumer, and state binding. Promote durable provenance into `docs/events/097_collaboration/` and delete the temporary workspace only when the event goal is complete.
