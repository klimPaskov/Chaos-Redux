# Event 102 asset production handoff

When asset production is authorized under [Part 1's authority record](102_serial_killer_spec_part_1_core.md#design-authority-and-reading-order), produce the visual assets required by the Serial Killer design. Read all four spec parts, then the current [asset owner skill](../../../.agents/skills/chaos-redux-event-assets/SKILL.md) and relevant [subagent contracts](../../../.agents/skills/chaos-redux-subagents/SKILL.md#asset-routing). The design is a civilian investigation told mainly through event reports, with three evolutions and conditional source connections.

All identifiers, scene labels and icon labels below are **working labels, not final localisation**. They identify production requirements. They are not finished event titles, achievement names or text to paint into an image. The current package plans assets. It does not claim that source images, native textures or engine previews have already been produced.

## Visual direction

Use restrained documentary investigation imagery appropriate to the campaign. Ordinary places should remain recognizable as places where civilians live, work, travel and gather. The unsettling quality comes from deliberate arrangement, interrupted routines and evidence that somebody has manipulated an otherwise familiar setting.

Keep victims and vulnerable civilians dignified. Show absence, abandoned belongings, secured rooms, interrupted work and investigators' comparisons. Avoid graphic mutilation, displayed human remains, glamorous offender portraits and imagery that celebrates cruelty. The Gourmet can be intellectually unsettling through objects and social settings without revealing a supernatural identity.

The four archetypes have different visual vocabularies. The Gourmet uses careful arrangement and respectable interiors. The Cipher Killer uses correspondence, versions and delivery. The Hunter uses ordinary journeys and changing routes. The Ritualist uses deliberately placed ordinary objects and repeated preparations. None is identifiable through a real ethnic, religious or national stereotype.

Locations must remain usable across the selected country pool. Favor objects, interior activity and broadly compatible civilian settings over an unmistakably wrong national landmark or police uniform. When a location genuinely needs a regional visual variant, identify the affected consumer and produce that variant deliberately. Do not treat a single European-looking street as a universal worldwide setting.

## Reference and source preparation

Use the asset owner's [reference library](../../../.agents/skills/chaos-redux-event-assets/SKILL.md#reference-asset-examples), [generation contract](../../../.agents/skills/chaos-redux-event-assets/SKILL.md#generate-and-refine-source-art) and [candidate lineage](../../../.agents/skills/chaos-redux-event-assets/SKILL.md#candidate-lineage-and-review). The canonical libraries are `.agents/skills/chaos-redux-event-assets/assets/gfx_references/` and `assets/visual_components/` beneath that same skill root. Inspect the exact live consumer and each matching contact sheet before fixing canvas, alpha, sprite identity or a permitted component layer. These cases are original fiction, so native ImageGen scene and symbolic icon production is appropriate. Retain actual arguments, sources, hashes, referenced inputs and selected-candidate lineage without inventing tool controls or missing provenance.

If a scene is intentionally based on a real photograph or archival artifact, establish the exact source, identity, rights and transformations. Historical claims need reliable attributed evidence. Do not pass a generated scene off as an archival photograph.

For every alpha-backed consumer, request `transparent_background = true` in the initial native ImageGen call and preserve alpha through processing and DDS conversion under [native transparency and fallback](../../../.agents/skills/chaos-redux-event-assets/SKILL.md#native-transparency-and-background-removal-fallback). Report/news source photographs keep their full scene backgrounds, with report-card transparent corners added by the owner's deterministic processing. Background removal is a recorded fallback for failed native alpha or inherited opaque sources, with preserved source and edge review.

## Required scene slots

Each row is a required logical consumer slot. One source can serve related events when it preserves their meaning and reveal state, with that reuse recorded explicitly. Every row still needs a verified binding. A larger total of unrelated images cannot replace a missing row.

| Working slot | Consumer and reference size | Composition and purpose |
|---|---|---|
| R01 initial civilian inquiry | Report picture, reference 210 by 176 | A secured ordinary civilian room or work area, modest belongings and a serious investigator's comparison. The original archetype remains unrevealed. |
| R02 Gourmet evidence | Report picture, reference 210 by 176 | Borrowed display objects or a carefully arranged reception setting, with food or art associations used as atmosphere. No visible answer, graphic anatomy or Cannibalism identity. |
| R03 Cipher evidence | Report picture, reference 210 by 176 | Correspondence, a newspaper proof and an ordinary collection point. Papers remain readable as objects without generated pseudo-text becoming a puzzle. |
| R04 Hunter evidence | Report picture, reference 210 by 176 | Civilian transport or shift movement observed from a useful distance. A changed route or emptied gathering place communicates disrupted routine. |
| R05 Ritualist evidence | Report picture, reference 210 by 176 | Ordinary objects deliberately arranged in a civilian room, with restrained repetition. The objects are fictional case props rather than borrowed religious insignia. |
| R06 contradicted inquiry | Report picture, reference 210 by 176 | Investigators compare records that expose a mistaken attribution. The visual emphasizes reconsideration and the civilian cost of lost time. |
| R07 regional evidence exchange | Report picture, reference 210 by 176 | A practical exchange of records between two administrations or a checked border journey. Avoid invented borders, flags and exact territorial data. |
| R08 civilian protection | Report picture, reference 210 by 176 | Civilians safely leaving or being guided away from the particular threatened place while investigators remain. Nobody is depicted as bait. |
| R09 cell investigation | Report picture, reference 210 by 176 | A modest refuge, admissions records or courier materials that suggest actual logistics and membership. A cell is more than a dramatic emblem. |
| R10 cell containment | Report picture, reference 210 by 176 | A secured support location with its civilian occupants safe and operational materials preserved as evidence. It communicates the loss of a real refuge or coordination point. |
| R11 escalating local crisis | Report picture, reference 210 by 176 | A more extensive interruption to civilian life, such as closed access and multiple abandoned belongings. Convey severity without increasing gore. |
| R12 Gourmet conclusion | Report picture, reference 210 by 176 | The supported reception, display or collection setting secured, with the anonymous responsible person under custody and the relevant objects preserved. |
| R13 Cipher conclusion | Report picture, reference 210 by 176 | The authenticated correspondence recovered while the identified sender is secured. The paper trail has an ordinary human origin. |
| R14 Hunter conclusion | Report picture, reference 210 by 176 | A safe transit interception or a protected gathering point after the actual traveler has been secured. The route is visibly usable. |
| R15 Ritualist conclusion | Report picture, reference 210 by 176 | A prepared arrangement interrupted, or a corroborated surrender accepted in secure custody. Innocent ceremony participants are visibly separate from the offender. |
| N01 first proven worldwide pattern | Major international news picture, reference 397 by 153 | A wide documentary newsroom or international evidence-exchange scene with material from different journeys. Its meaning is worldwide coordination. Exact countries and proof remain in text. |
| N02 genuine global closure | International news picture, reference 397 by 153 | Completed investigative files and ordinary civilian activity resuming, with a restrained sense of relief. Preserve memory of victims rather than depicting a triumphal celebration. |

Report source scenes receive the current deterministic sepia documentary-card treatment, including the accepted tilt, transparent corners and shadow. News pictures use the current monochrome treatment. Verify the actual consumer before final conversion. Do not treat these reference dimensions as overriding an inspected native slot.

The archetype evidence pictures can be shared across their three case families because every decisive observation is stated in text. A generated image is never evidence that a bowl overlap, clock offset, grid entry or ritual orientation is correct. Any optional schematic used to show those exact facts must be produced with precise native or vector elements and checked against the case fixture, not guessed by ImageGen.

## Conditional connection slots

| Source relationship | Required reveal handling | Preferred visual binding |
|---|---|---|
| Cannibalism shelter or courier | Keep the contact anonymous until the source's Hannibal reveal permits the actual identity | An appropriate approved source-owned network image after its gate, or a neutral shelter/record scene before it |
| Murder Mystery evidence exchange | Keep the political and civilian cases distinct | An approved source inquiry image or a neutral comparison of separate files, without assigning political victims to Event 102 |
| Active Death connection | Respect active source participation, country knowledge and public revelation separately | The source's approved current-state image where permitted, combined through separate event sequencing with the human cult evidence |
| Active outbreak or disaster concealment | Show the actual local crisis and the separate human use of its disruption | An approved source image or a sourced/generated current-setting scene after the relevant owner review |
| Eligible hidden Wendigo connection | Preserve the source's hidden identity until its own discovery gates allow it | Reuse the approved source identity only in the eligible revealed state. Use neutral current case material beforehand. |

Resolve exact source sprites and conditions with the source owner and current source lookup. No public Event 102 adapter or reveal permission was verified during planning. New art cannot be used to bypass that dependency. A source disappearance must leave an appropriate grounded case picture available for the ordinary continuation.

## Native icon families

| Working slot | Consumer | Native source direction |
|---|---|---|
| I01 active civilian disruption | Idea or current verified modifier consumer, reference 64 by 64 | A restrained symbol of interrupted ordinary life and active uncertainty. It must remain legible at native size and not identify the hidden archetype. |
| I02 concentrated local protection | Current verified temporary modifier consumer, reference 64 by 64 | A protected civilian doorway or sheltered route, visually distinct from I01 and from military attack bonuses. |
| D01 reopen the current inquiry | Native decision icon, reference 32 by 32 | A compact evidence-folder or record-comparison symbol, composed specifically for this small decision family. |
| C01 host category for the temporary inquiry decision | Native decision-category icon, dimensions and framing from its inspected owner | Resolve the actual category consumer. Reuse a verified existing category and its current icon when appropriate, recording that binding. If the temporary inquiry needs its own category, this row requires a separately composed category icon using the canonical decision-category family. |

Create each icon family from its own original composition. Do not resize a report picture into an icon or resize the idea icon into the decision icon. Preserve the current reference family's silhouette, framing, alpha and native readability.

C01 is a required consumer binding even when verified reuse satisfies it. Inspect the native category separately from D01 and do not infer its dimensions from the 32 by 32 decision icon. A custom category picture is not part of the accepted requirement set.

Achievement consumers and icon directions belong to [the achievement prompt](102_serial_killer_achievement_prompt.md#art-states-and-wiring), and their exact production contract belongs to [achievement icons](../../../.agents/skills/chaos-redux-event-assets/references/icon-and-ui-families.md#achievement-icons). Bind all five completed, grey and not-eligible triplets to resolved registry identifiers, with final DDS files directly under `gfx/achievements/`.

## Production ownership and acceptance

Use `chaosx_generated_event_art` for fictional scenes, `chaosx_icon_artist` for native icon families and `chaosx_asset_source_researcher` only for a concrete non-portrait sourced requirement. The current design's anonymous people in scenes do not create standalone portrait consumers. If a separately authorized character portrait is required, route its complete package to `chaosx_portrait_creator` under [portrait production](../../../.agents/skills/chaos-redux-event-assets/references/portrait-production.md). The user alone operates RunPod for grounded styled finals. Each worker receives exact approved rows, reveal conditions and bounded paths. The parent owns gameplay, shared presentation and non-portrait GFX integration.

Use [the asset evidence contract](../../../.agents/skills/chaos-redux-event-assets/SKILL.md#manifest-requirements), [DDS conversion](../../../.agents/skills/chaos-redux-event-assets/SKILL.md#dds-conversion) and [requirement-to-runtime crosswalk](../../../.agents/skills/chaos-redux-event-assets/SKILL.md#requirement-to-runtime-coverage-audit). Each R/N/I/D/C and conditional slot must retain source, transformations, final texture, hashes, alpha evidence, sprite, actual consumer and reveal binding. Inspect all native consumers and the relevant complete sheet. Preserve active source evidence until review and follow the owner's [workspace cleanup](../../../.agents/skills/chaos-redux-event-assets/SKILL.md#workspace-cleanup) only after durable evidence and runtime references are reconciled.

Review normal evidence, failure, all four individual conclusions, protection, regional exchange, cell investigation, containment, global announcement, global closure and every enabled source reveal state. Confirm that no art leaks an answer or hidden identity. Document permitted reuse explicitly. Use available native renders within AGENTS.md's retry limit, then source and local consumer review with stated visual limits. User-owned live validation is neither requested nor awaited for delivery.

Deliver the complete accepted source and texture package, consumer manifest and visual review evidence. Report pending rows specifically. A source image or successful conversion alone does not establish that the game uses the correct asset.
