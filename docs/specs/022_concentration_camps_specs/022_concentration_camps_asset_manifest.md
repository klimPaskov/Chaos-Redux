# Event 22 Concentration Camps Asset Manifest

## Asset direction

Event 22 uses documentary restraint. Real historical surfaces should use sourced archival images. Abstract gameplay icons should use generated symbolic art through the project ImageGen workflow.

The package excludes graphic bodies, gore, staged victim scenes, generated documentary photographs, fake historical quotations, fake archive text, celebratory perpetrator imagery, and decorative atrocity animation.

## Source-agent routing

- `chaosx_asset_source_researcher` owns real and archival event, news, and category-picture sourcing.
- `chaosx_icon_artist` owns decision, mission, category, idea, state-modifier, and achievement icons.
- `chaosx_generated_event_art` may produce a people-free symbolic panel only when archival sourcing fails and the parent accepts that source-mode change.

Every asset agent must use `fork_context=false` and receive a context-complete prompt.

## Reference folders

Inspect these current project references before production:

- report event images: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/`
- news event images: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/news/`
- decision category icons: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/`
- decision category pictures: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures/`
- decision icons: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions/`
- mission icons: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/missions/`
- idea icons: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/ideas/`
- achievement icons: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/`

The decision-category-picture folder must have a labelled `contact_sheet.png` with filenames and native dimensions. If missing, the asset worker must create it and update the reference README and catalog before locking the Event 22 picture dimensions.

## Working and final folders

Temporary evidence workspace:

```text
docs/assets/022_concentration_camps/
```

Recommended final runtime folders:

```text
gfx/event_pictures/022_concentration_camps/
gfx/interface/decisions/022_concentration_camps/
gfx/interface/ideas/022_concentration_camps/
gfx/interface/achievements/022_concentration_camps/
gfx/interface/event_022/
```

The implementation agent must adapt paths to current repository conventions and record the final sprite names in `gfx_handoff.md`.

Before full event completion, durable provenance, licensing, attribution, review, and sprite facts must be promoted into permanent Event 22 documentation. The temporary event asset workspace is then removed after all runtime references are verified outside it.

## Archival image rules

Archival sources must be:

- attributable to a museum, archive, government repository, library, or other defensible institution
- suitable for reuse under a documented licence, public-domain status, or accepted project policy
- stored with source title, institution, date, source page, licence, download date, and checksum
- non-graphic
- correctly identified by place, date, and subject where known
- cropped without changing historical content
- free of modern watermarks in the final runtime image unless the licence requires attribution and the UI can support it correctly

Do not use a photograph from one camp or country as a false exact depiction of another named event. Generic report use can identify the image as representative in provenance while localisation remains campaign-specific.

## Event and category pictures

| Asset ID | Surface | Size | Source mode | Visual direction | Runtime role | Priority |
| --- | --- | --- | --- | --- | --- | --- |
| `022_category_camp_network` | main decision category picture | match the inspected current vanilla or Chaos Redux category-picture precedent | sourced archival | fence, gate, barracks, transport line, records room, or empty camp infrastructure, no bodies | persistent identity for management category | required |
| `022_report_network_activation` | report event | `210x176` | sourced archival | newly established or operating detention infrastructure, officials or transport allowed, no graphic victims | first firing | required |
| `022_report_forced_labour` | report event | `210x176` | sourced archival | prisoners or forced workers at industrial, construction, extraction, or logistics work, non-graphic and accurately identified | labour-assignment crisis | required |
| `022_report_extermination_escalation` | report event | `210x176` | sourced archival | exterior of a killing center or sealed facility, tracks, gate, or empty structures, no bodies | Evolution I escalation | required |
| `022_report_evidence_discovery` | report event | `210x176` | sourced archival | investigators, records, opened storage, liberated gate, or evidence team | first verified site | required |
| `022_report_liberation_relief` | report event | `210x176` | sourced archival | medics, relief distribution, survivors moving toward care, or liberated grounds, non-graphic | liberation transition | required |
| `022_report_closure_aftermath` | report event | `210x176` | sourced archival | empty barracks, dismantled gate, records transfer, displaced-person center, or reconstruction | transparent closure or long aftermath | recommended |
| `022_news_verified_network` | news event | `397x153`, black and white | sourced archival | broad camp complex, transport network, or documentary evidence with strong horizontal composition | public verification of large network | required |
| `022_news_major_liberation` | news event | `397x153`, black and white | sourced archival | liberation and relief scene with clear scale, no graphic bodies | liberation of major network | required |
| `022_news_accountability` | news event | `397x153`, black and white | sourced archival | tribunal chamber, evidence table, archive, or public accountability process | major tribunal threshold | recommended |

### Category picture dimension blocker

The supplied planning sources do not contain the native dimension of the repository's current decision-category-picture precedent. Do not guess it. The asset worker must inspect the canonical reference family and one live Chaos Redux category consumer, then record the exact native size before production.

This is a bounded asset-dimension lock, not a gameplay-design gap.

## Category icons

Target size: `32x32`, subject to current repository precedent.

| Asset ID | Visual direction | Use |
| --- | --- | --- |
| `022_category_icon_management` | fenced document folder with a small state seal, readable silhouette | camp network management category |
| `022_category_icon_relief` | open gate with medical cross and registration card | liberated-site relief category |

Source mode: generated symbolic through ImageGen. Transparent background. No text.

## Decision and mission icon family

Target size: `32x32`.

| Asset ID | Visual direction | Main consumers |
| --- | --- | --- |
| `022_decision_close` | open padlock on a gate | freeze intake, closure |
| `022_decision_review` | inspection clipboard and magnifier | review, registration, inspection |
| `022_decision_food_medical` | ration container and medical case | food and medicine, epidemic mission |
| `022_decision_forced_labour` | chained gear and work tool, symbolic and restrained | labour policy and intensity |
| `022_decision_industry` | factory gear behind fence line | industrial assignment |
| `022_decision_construction` | rail tie and construction tool behind fence line | construction assignment |
| `022_decision_extraction` | mine cart or resource crate behind fence line | extraction assignment |
| `022_decision_logistics` | railway switch and guarded transport | logistics assignment and transfer |
| `022_decision_expand` | map with one new fenced state marker | state expansion |
| `022_decision_guard` | watchtower and shield | guard reinforcement |
| `022_decision_evidence` | protected document and camera or seal | evidence preservation and discovery |
| `022_decision_coverup` | torn or burned document with warning mark | falsify or destroy records |
| `022_decision_escape` | cut fence and route arrow | escape and resistance mission |
| `022_decision_epidemic` | barracks silhouette with medical warning | epidemic mission |
| `022_decision_extermination` | extinguished human-rights candle behind a sealed gate, no skull or gore | extermination conversion and halt |
| `022_decision_chemical` | sealed chemical cylinder with hazard frame, no procedural apparatus | restricted chemical site |
| `022_decision_retreat` | railway route leaving a threatened site | evacuation and retreat crisis |
| `022_decision_liberation` | broken lock and relief marker | secure liberated site |
| `022_decision_resettlement` | route lines toward a home and shelter | safe accommodation and return |
| `022_decision_tribunal` | evidence file and judicial scale | tribunal and accountability |

A single icon can serve closely related decisions. Do not create one icon for every small action when the visual role is the same.

## Country idea icons

Target size: `64x64`.

| Asset ID | Visual direction | Idea family |
| --- | --- | --- |
| `022_idea_administrative_burden` | overfilled files, rails, and guarded gate | Camp Network Administrative Burden |
| `022_idea_forced_labour_economy` | chained industrial gear and transport wheel | Forced-Labour War Economy |
| `022_idea_security_ascendant` | watchtower above cabinet seal | Security Apparatus Ascendant |
| `022_idea_network_review` | magnifier over site register | Network Under Review |
| `022_idea_dismantlement` | opened gate with construction removal tool | National Dismantlement Program |
| `022_idea_exposed_atrocities` | documents and site marker under public light | Publicly Exposed Atrocities |
| `022_idea_survivor_relief` | medical kit, shelter, and registry card | Survivor Relief and Resettlement |
| `022_idea_tribunal_pressure` | document stack and judicial scale | Tribunal and Documentation Pressure |

Generated symbolic through ImageGen, with a clean people-free composition, no embedded text, and no graphic imagery.

## State-modifier icons

Target size: `64x64`, unless current state-modifier convention uses another verified size.

| Asset ID | Visual direction | State statuses covered |
| --- | --- | --- |
| `022_state_active_detention` | fenced barracks | active detention site |
| `022_state_labour_industry` | fenced factory gear | industrial assignment |
| `022_state_labour_construction` | fenced rail and tool | construction assignment |
| `022_state_labour_extraction` | fenced mine cart | extraction assignment |
| `022_state_labour_logistics` | fenced railway switch | logistics assignment |
| `022_state_extermination` | sealed gate and extinguished candle | extermination site |
| `022_state_overcrowded` | compressed barracks rows and warning frame | overcrowding |
| `022_state_workforce_exhausted` | broken gear and empty barracks | labour pool exhausted |
| `022_state_inspection` | open register and magnifier | under inspection |
| `022_state_closing` | gate opening with removal tool | site closing |
| `022_state_abandoned` | damaged empty watchtower | abandoned site |
| `022_state_liberated` | broken lock and relief cross | liberated site |
| `022_state_evidence_preserved` | sealed evidence box | evidence preserved |
| `022_state_evidence_destroyed` | burned file with warning border | evidence destroyed |
| `022_state_contaminated` | sealed barracks with chemical warning | contaminated site |
| `022_state_relief_center` | shelter, medical, and registry symbols | survivor relief center |

Where the interface can reuse a decision or idea icon without confusion, prefer reuse over a redundant asset.

## Achievement icons

Target size: `64x64` completed master, with grey and not-eligible states from the achievement workflow.

| Asset ID | Direction |
| --- | --- |
| `022_achievement_close_every_gate` | open iron gate with daylight |
| `022_achievement_names_restored` | restored ledger and seal |
| `022_achievement_evidence_survives` | damaged document protected in evidence frame |
| `022_achievement_no_one_disappears_twice` | broken transport chain before closed gate |
| `022_achievement_machine_stopped` | split gear and relief or justice emblem |
| `022_achievement_government_answers` | opened archive and judicial scale |
| `022_achievement_safe_harbor` | harbor light and shelter routes |
| `022_achievement_against_order` | illegal order torn above secured keys |
| `022_achievement_from_camps_to_care` | barracks transformed into clinic and home |
| `022_achievement_no_second_operator` | barred responsibility-transfer arrow between seals |
| `022_achievement_long_return` | return routes converging on home and family record |

Achievements should remain symbolic. Do not depict prisoners, corpses, gas chambers, or execution imagery.

## Existing-building asset audit

The project already defines:

- `concentration_camp`
- `extermination_camp`
- `gulag_labor_camp_network`

Before creating any new building icon or map asset:

1. inspect current building definitions and sprite consumers
2. verify all three have readable icons and map representation where expected
3. verify extermination and concentration camps are visually distinct
4. verify the gulag icon remains Soviet-specific
5. check transparent background and native dimensions
6. reuse them if they pass

A missing or unusable icon can be added through `chaosx_icon_artist` after parent approval. Do not create a second building family merely for Event 22.

## Content restrictions

- do not generate victim scenes
- do not use graphic liberation photographs
- do not paint death counters into event art
- do not place fake UI buttons or meters inside the category picture
- use Nazi, Soviet, Japanese, or other regime symbols only in an accurate country-specific context, never as generic decorative branding

## Processing requirements

For every selected archival image:

- preserve original download
- record checksum
- create crop plan
- keep aspect ratio
- avoid AI restoration that changes historical content
- use only mechanical crop, resize, tonal correction, and format conversion unless the parent authorizes restoration
- document any removal of border, caption, or archive margin
- retain a readable source preview
- convert to the required PNG and DDS through repository tools

For every generated icon:

- retain ImageGen source evidence
- record prompt and source mode
- use transparent background
- remove white matte or opaque square artifacts
- create contact sheet
- inspect at native size and `4x`
- verify silhouette, alignment, padding, and palette against references
- convert to DDS through repository workflow

## Review gates

### Archival review

Reviewer confirms:

- source is correctly identified
- use is non-graphic and appropriate
- licence or public-domain status is documented
- crop does not misrepresent the subject
- event usage does not falsely claim exact place or date
- final image remains readable at runtime size

### Icon review

Reviewer confirms:

- no text
- no graphic imagery
- no white matte
- transparent background
- central symbol readable at native size
- style matches the correct vanilla reference family
- related icons remain distinct
- no unrelated asset was resized and reused as a fake final

### Runtime review

Parent confirms:

- sprite path and name
- correct event or decision consumer
- no missing texture
- correct aspect ratio
- category picture does not cover controls or text
- report and news crop displays correctly
- achievements show completed, grey, and not-eligible states

## Asset handoff fields

For every final asset, record:

- asset ID
- source mode
- source institution or ImageGen prompt record
- licence and attribution
- source checksum
- processed PNG path and checksum
- final DDS path and checksum
- target size
- sprite name
- owning GFX file
- runtime consumer
- crop and processing notes
- reviewer
- native and `4x` approval
- status
- remaining blocker

## Asset production priority

1. main category picture and icon
2. network activation report image
3. evidence discovery report image
4. liberation relief report image
5. core decision icons for closure, labour, expansion, evidence, extermination, retreat, and relief
6. country idea icons
7. state-modifier icons required by implemented statuses
8. verified-network and major-liberation news images
9. achievement icons
10. optional closure, accountability, and additional assignment images
