# Event 013 Natural Disasters, dependency order and subagent sequence

This file gives the implementation order that best preserves the expanded design while avoiding duplicate logic and late rewrites.

## Phase 0, live repository mapping

Purpose: discover exact implementation touchpoints before editing.

Required work:

1. Read the live repository `AGENTS.md`, required repo skills, offline wiki pages, vanilla documentation, and local precedent files.
2. Map Event 013 event script locations, random event registration, event-log display, cluster files, triggerable scenario files, shared dynamic effects, decisions, categories, scripted localisation, GUI, GFX, achievements, assets, docs, and spreadsheet ownership.
3. Search for existing Event 013, Event 046, Event 051, and Event 099 logic.
4. Mark old Event 013 and old Earth Earthquake logic as deleted, placeholder, or blocked from reuse.
5. Identify reusable dynamic helpers already present in the repository before creating new helpers.

Recommended subagent:

- `chaosx_repo_explorer` only if the file map is unclear or the repository has changed enough that direct mapping would be risky.

Exit gate:

- The parent has exact files and identifiers for the first implementation tranche.

## Phase 1, scripted architecture

Purpose: build the reusable system once before family content multiplies.

Required work:

1. Define script constants for severity bands, delay bands, news policy thresholds, death scaling factors, building damage bands, regional spread caps, aftermath duration bands, AI willingness bands, and scenario intensity stops.
2. Design the disaster sequence state, with one Event 013 history row at sequence start.
3. Define the call contract helper or helper family.
4. Define target selection and target validation helpers.
5. Define warning, impact, report, aftermath, chain, and cleanup helper boundaries.
6. Define event targets or variable storage for current family, current country, current state, current severity, sequence id, sequence index, and caller policy.
7. Document helper side effects and cleanup.

Recommended subagent:

- `chaosx_scripted_system_architect`.

Exit gate:

- A single caller can request one family, one target, one severity, and one report policy without copy-pasting damage logic.

## Phase 2, baseline vertical slice

Purpose: prove the whole contract with one family before expanding the catalogue.

Recommended vertical slice:

1. Choose earthquake or flood as the first full slice because both exercise population loss, building damage, report flow, aftermath, and possible follow-up.
2. Trigger an Event 013 sequence.
3. Record exactly one history row.
4. Schedule delayed warning if applicable.
5. Apply impact to a valid state.
6. Feed population loss through the Deaths system.
7. Damage family-relevant buildings.
8. Deliver the affected-country report after the designed delay.
9. Open or refresh the aftermath category and notification.
10. Show an aftermath card with family, severity, state, damage, deaths, recovery needs, and cleanup state.
11. Let the player or AI complete a basic recovery action.
12. Clean the card and any temporary state after recovery or expiry.

Exit gate:

- The baseline vertical slice proves one-row logging, delayed reports, visible notification, deaths integration, and cleanup.

## Phase 3, ordinary family expansion

Purpose: implement the family catalogue without changing the system contract.

Recommended order:

1. Geological families: earthquake, tsunami, volcanic eruption, dry mass movement, wet mass movement.
2. Water and coastal families: flood, cyclone, extreme wind, thunderstorm, hailstorm.
3. Temperature and exposure families: blizzard, cold wave, drought, heat, wildfire.
4. Dust and sky families: sandstorm, dust storm, meteor precursor, storm corridor precursor if needed.

Implementation rule:

- Each family adds family-specific scoring, warning, impact, report direction, aftermath card fields, state modifier direction, chain route, AI priority, and news policy while reusing the shared helpers.

Exit gate:

- Every implemented family can be directly triggered and can participate in random selection.

## Phase 4, aftermath decisions and missions

Purpose: build the recovery layer after real impact data exists.

Required work:

1. Create the aftermath category with visible notification behavior.
2. Add card state logic for active, warning, recovering, degraded, chained, closed, and expired cards.
3. Implement early rescue actions and emergency missions.
4. Implement middle stabilization actions and chain-prevention missions.
5. Implement late reconstruction actions and repeated recovery pressure.
6. Add active mission caps and priority scoring.
7. Add partial success and failure routes.
8. Add foreign relief with cost, dependence, convoy, war, ideology, distance, and AI factors.
9. Add cleanup for annexation, tag death, state invalidation, recovery completion, and sequence expiry.

Recommended subagent:

- `chaosx_decision_mission_auditor` after the first complete decision tranche.

Exit gate:

- The category is usable, staged, capped, and not a political-power store.

## Phase 5, Evolution I and Evolution II

Purpose: widen the event safely after baseline content works.

Evolution I work:

1. Expand family pools.
2. Increase sequence activity.
3. Keep severity only slightly stronger.
4. Preserve meaningful but throttled news.

Evolution II work:

1. Add regional spread from anchor states into neighboring valid states.
2. Add stronger death and damage scaling.
3. Enable chained aftermaths.
4. Add supply, refugee, famine, disease, stability, and war support pressure where family identity supports it.
5. Make recovery speed influence chain risk.
6. Keep news meaningful and throttled.

Exit gate:

- Evolution II changes scale, regional spread, and aftermath chains without breaking one-row sequence logging.

## Phase 6, Event 099, Event 051, Event 046, cluster, and scenario links

Purpose: align surrounding events and catalogue surfaces.

Required work:

1. Keep Event 046 inactive and unknown.
2. Remove or quarantine old Earth Earthquake logic.
3. Bridge or placeholder Event 099 so sandstorm calls route into Event 013 only through the reusable system.
4. Add heat non-stacking checks with Event 051.
5. Register Natural Disasters cluster behavior with repeated Event 013 entries and tiered severity.
6. Implement Disaster Barrage scenario with type choices and intensity stops.
7. Keep Disaster Barrage from creating a world-end branch.

Exit gate:

- Related events do not duplicate Event 013 logic or contradict the specs.

## Phase 7, abnormal controller and GUI

Purpose: add Evolution III after the normal controller and recovery layer are stable.

Required work:

1. Implement abnormal family state for meteor shower, massive rupture, volcanic crisis, tsunami chain, and moving storm or tornado corridor.
2. Create the abnormal map state model.
3. Build the scripted GUI panel, map layers, path cards, impact queue, coming-next cards, and recovery summary.
4. Wire animation sprites through frame sheets, not GIFs.
5. Add static fallbacks for every animated element.
6. Add AI equivalents for meaningful player actions.
7. Add GUI cleanup when the abnormal disaster ends, becomes invalid, or is superseded.

Recommended subagents:

- `chaosx_icon_artist` for small animated UI sprites.
- `chaosx_generated_event_art` for fictional abnormal event art or UI panels.
- `chaosx_asset_source_researcher` only if a source image is explicitly required.

Exit gate:

- Evolution III moving disasters show readable direction, next-hit regions, and card state without requiring the player to inspect hidden variables.

## Phase 8, super-event research and wiring

Purpose: keep major presentation moments source-backed and not placeholder.

Required work:

1. Use the super-event handoff matrix to decide which abnormal moments actually deserve super-event treatment.
2. Research main quotes and cultural remarks through the text researcher.
3. Research, download, convert, and document audio through the audio researcher.
4. Produce or source super-event images through the correct asset route.
5. Wire each completed super-event with slot, image, text, quote, button, audio id, settings-aware playback, docs, and spreadsheet after source work exists.

Recommended subagents:

- `chaosx_super_event_text_researcher`.
- `chaosx_super_event_audio_researcher`.
- `chaosx_generated_event_art` or `chaosx_asset_source_researcher` by source mode.

Exit gate:

- No super-event uses default, undocumented, unlicensed, unresearched, or placeholder presentation.

## Phase 9, achievements and asset finalization

Purpose: complete visible identity and mastery goals.

Required work:

1. Implement achievement triggers, disqualifiers, and tracking flags or variables.
2. Produce completed, grey, and not-eligible icons where the achievement system requires them.
3. Produce decision, category, report, news, idea, state modifier, and GUI assets.
4. Keep final DDS files in valid mod folders and source material under documentation asset paths.
5. Update manifest and GFX handoffs.

Recommended subagent:

- `chaosx_icon_artist` for achievement and small gameplay icons.

Exit gate:

- Every visible asset is complete, handed off, wired, or reported as blocked.

## Phase 10, localisation, docs, spreadsheet, and audits

Purpose: finish the feature without stale text or hidden simplifications.

Required work:

1. Write final player-facing localisation from direction notes.
2. Audit localisation for keys, encoding, duplicate keys, raw triggers, dynamic values, and style.
3. Update event docs from implemented behavior.
4. Update spreadsheet only after final in-game wording exists.
5. Run decision, localisation, completion, and documentation audits as needed.
6. Report every simplification, missing asset, missing AI behavior, missing super-event package, or skipped meaningful validation.

Recommended subagents:

- `chaosx_localisation_auditor`.
- `chaosx_documentation_curator` if docs became stale or duplicated.
- `chaosx_spreadsheet_doc_worker` after final wording exists.
- `chaosx_event_completion_auditor` before claiming completion.

Exit gate:

- The feature can be reported as complete only if audits and implementation evidence show that accepted specs are satisfied.
