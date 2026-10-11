# Shard 5 report artwork bindings

Disposition: implemented within the user request to place accepted named report artwork on current visible event surfaces.

Four independently reviewed report images now serve five existing report popups.
The original art files and original generic sprites remain untouched. The Event 050 image was copied byte-for-byte from its accepted candidate into its event-scoped runtime folder.
The changes define four event-specific sprites and update only the picture field on the mapped event popups.

| Owner | Requirement | Runtime DDS | Sprite and registry | Existing visible consumer | Source SHA-256 |
|---|---|---|---|---|---|
| 050 | report_opening_isolation | gfx/event_pictures/050_the_great_embargo/report_event_opening_isolation.dds | GFX_report_event_050_great_embargo_opening_isolation in interface/050_the_great_embargo_assets.gfx | chaosx.nr50.2 in events/050_the_great_embargo.txt | 4d03e91aaa685de82cf749bbbda3f07832d1b5f0ecdf32b4f5f350bd279074b5 |
| 054 | report_event_054_gift_from_scientists | gfx/event_pictures/054_gift_from_scientists/report_event_054_gift_from_scientists.dds | GFX_report_event_054_gift_from_scientists in interface/054_gift_from_scientists_assets.gfx | chaosx.nr54.1 in events/054_random_tech.txt | da060f1318539da39c3cb7aae4f97456b3115a1ab3a8bdad1f50c2cf51609e8b |
| 058 | report_event_058_random_buildings | gfx/event_pictures/058_random_buildings/report_event_058_random_buildings.dds | GFX_report_event_058_random_buildings in interface/058_random_buildings_assets.gfx | chaosx.nr58.2 in events/058_free_civs.txt | f0cf21a0955a2e5e9677b348341dce89ee947068639a565447c1e8ff8cad18f0 |
| 062 | report_event_062_allies_backstab | gfx/event_pictures/062_allies_backstab/report_event_062_allies_backstab.dds | GFX_report_event_062_allies_backstab in interface/062_allies_backstab_assets.gfx | chaosx.nr62.2, chaosx.nr62.3 in events/062_allies_backstab.txt | aa4c886f1e431916d448b57ed4e4d81177b677be36b451c364b137097b707d09 |
| 054 | report_event_054_gift_from_scientists | gfx/event_pictures/054_gift_from_scientists/report_event_054_gift_from_scientists.dds | GFX_report_event_054_gift_from_scientists in interface/054_gift_from_scientists_assets.gfx | chaosx.nr54.1 in events/054_random_tech.txt | da060f1318539da39c3cb7aae4f97456b3115a1ab3a8bdad1f50c2cf51609e8b |
| 058 | report_event_058_random_buildings | gfx/event_pictures/058_random_buildings/report_event_058_random_buildings.dds | GFX_report_event_058_random_buildings in interface/058_random_buildings_assets.gfx | chaosx.nr58.2 in events/058_free_civs.txt | f0cf21a0955a2e5e9677b348341dce89ee947068639a565447c1e8ff8cad18f0 |
| 062 | report_event_062_allies_backstab | gfx/event_pictures/062_allies_backstab/report_event_062_allies_backstab.dds | GFX_report_event_062_allies_backstab in interface/062_allies_backstab_assets.gfx | chaosx.nr62.2, chaosx.nr62.3 in events/062_allies_backstab.txt | aa4c886f1e431916d448b57ed4e4d81177b677be36b451c364b137097b707d09 |
| 054 | report_event_054_gift_from_scientists | gfx/event_pictures/054_gift_from_scientists/report_event_054_gift_from_scientists.dds | GFX_report_event_054_gift_from_scientists in interface/054_gift_from_scientists_assets.gfx | chaosx.nr54.1 in events/054_random_tech.txt | da060f1318539da39c3cb7aae4f97456b3115a1ab3a8bdad1f50c2cf51609e8b |
| 058 | report_event_058_random_buildings | gfx/event_pictures/058_random_buildings/report_event_058_random_buildings.dds | GFX_report_event_058_random_buildings in interface/058_random_buildings_assets.gfx | chaosx.nr58.2 in events/058_free_civs.txt | f0cf21a0955a2e5e9677b348341dce89ee947068639a565447c1e8ff8cad18f0 |
| 062 | report_event_062_allies_backstab | gfx/event_pictures/062_allies_backstab/report_event_062_allies_backstab.dds | GFX_report_event_062_allies_backstab in interface/062_allies_backstab_assets.gfx | chaosx.nr62.2, chaosx.nr62.3 in events/062_allies_backstab.txt | aa4c886f1e431916d448b57ed4e4d81177b677be36b451c364b137097b707d09 |

## Review evidence

The Event 050 opening-isolation sample was inspected at source and native size; all three report DDS outputs passed strict BGRA header, dimension, transparent-corner and decoded-PNG equality checks.
The combined 054/058/062 batch was sampled on the departing-liaison scene; all three DDS files passed strict BGRA header, 210x176 dimensions, 147,968-byte payload, transparent-corner and decoded-PNG equality checks.
Review records are in `docs/assets/shard_5_review_20261011/current_review.json`, batches `batch050_reports` and `batchshipping_reports_054_058_062`.
The 050 candidate source was copied to the new runtime path with identical bytes. New artwork source, processed preview and earlier files remain in the existing asset workspaces.

## Current mapping

Event 050 `chaosx.nr50.2` is the only current consumer for opening isolation. The two evolution report candidates remain unbound because matching visible evolution popup IDs are not implemented.
Event 054 `chaosx.nr54.1` displays the scientists prototype discovery scene.
Event 058 `chaosx.nr58.2` displays the randomized construction scene.
Event 062 `chaosx.nr62.2` and `.3` display the same approved betrayal scene to the victim country.
No AI, event trigger, effect, decision, cost or localization behavior changed.

The offline event-modding reference defines the event `picture` field as a sprite lookup and the graphical asset reference gives the sprite texture path semantics. The installed event source precedent is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/BBA_italy.txt`.
The installed documentation directory has no dedicated event-picture/sprite section. Current reference MCP calls were unavailable, so the offline local references and vanilla source were used; this report makes no live engine claim.
All review and strict container checks are asset evidence, not an in-game visual check.

Remaining spec rows 050 secondary-sanctions and fragmented-trade remain candidate files for future evolution popup consumers. Other unfinished spec rows are outside these four report requirements.

Skills used: `chaos-redux-event-assets`, `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`.

## Engine references

- Offline event-modification wiki: `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`, lines 76-90, SHA-256 `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
- Offline graphical asset wiki: `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, lines 30-75, SHA-256 `f8e3d4ad382f4e5f8e170492a484d090bad62e3711cabfb5d3bf84e58ab32dd9`.
- Installed event picture precedent: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/BBA_italy.txt`, lines 29-33, SHA-256 `a7f3c9d747d772cd59b143d2b8784e17731e72f6d6712b0a19d04990722f5431`.
