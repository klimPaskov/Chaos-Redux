# Achievement handoff: Event 092, Greenland Sale

Read the full specification, especially Parts 02, 04, 09, 11 and 13, the original brief, the source and decision register, and the current achievement rules in AGENTS and `chaos-redux-event-assets`.
Use the supplied icon-artist, localisation-auditor, documentation, and completion-auditor role definitions through actual subagent execution when that tool is available.
No achievement implementation or production art exists in this planning package.

## Gameplay authority

Part 13 is the authority for all conditions below.
The working themes are not final player-facing titles.
Use the exact proposed IDs only after checking the current registry for collisions and its ownership convention.

| Proposed ID | Actor and mastery | Essential evidence |
| --- | --- | --- |
| `092_greenland_sale_arctic_development` | Player founding-lot buyer defeats genuine competition, retains all purchased Greenland holdings for 365 days, completes two new increments in two building families, and has a usable port and airfield. | At least two independent, genuinely funded competing countries, completed founding sale, continuous ownership and control, post-purchase paid or ordinary completed construction. |
| `092_greenland_sale_productive_withdrawal` | Player sells a non-core overseas lot, reinvests at least 75 percent of its actual receipt in retained-home construction within 180 days, including a civilian factory, and retains its protected country. | Actual sale receipt, nonduplicated attribution of delivered construction, state ownership and control, retained capital and inhabited home. |
| `092_greenland_sale_connected_acquisitions` | Player buys at least two lots from independent sellers, joins them into one genuinely connected overseas holding with a usable port, and retains the purchased states for 180 days after the second purchase. | Paid distinct sales, seller independence at publication and settlement, owned-land or verified map connection, continuous ownership and control. |
| `092_greenland_sale_homeland_recovery` | Player sells a homeland lot under genuine severe pressure, fulfills the fixed reconstruction objective, survives 180 days with its protected country, and restores stability to at least its pre-sale level and at least 50 percent. | Pressure snapshot at publication, actual homeland sale, completed mission, survival, stable pre-sale comparison, terminal stability. |

Do not award for rejected bids, canceled lots, dummy same-controller competitors, observers, free debug transfers, expired missions, or pre-purchase building levels.
An achievement need not be possible on every campaign map or fully developed lot.
Do not create assets, building space, or qualifying competitors merely to make all four unlockable in every scenario.
Achievements grant recognition only, with no reserve, free cores, auction advantage, or extra Chaos reward.

## Text and display

Write final titles and concise descriptions from the thematic direction in Part 13 after checking the actual implemented conditions.
A description must not claim that merely buying Greenland is sufficient.
Explain the meaningful actor, competition, construction, continuity, and recovery requirements through the proper achievement surface.
Keep hidden proof fields out of ordinary player prose while making every consequential condition discoverable.

Use the existing shared achievement registry and localisation structure.
Where a root-level registry owns one `unique_id`, preserve that ownership instead of creating an incompatible independent registry file.
Keep exact IDs aligned across the registry, localisation, sprites, texture triplets, documentation, and tests.

## Art

Follow the separate asset prompt for each original 64×64 subject and its deterministic three-state source triplet.
Completed, grey, and not-eligible runtime textures belong directly in `gfx/achievements/` under the full achievement ID.
Use the unchanged canonical backgrounds and overlay, the required processor, retained review images, native-size contact sheet, and DDS pixel-equality evidence.
No final titles or text belong inside the images.

## Validation

Prove every achievement from a near-miss and a valid fixture.
Include one wrong actor, one externally changed owner, one interrupted continuity period, one insufficient or duplicated receipt attribution, and a reload near the final award.
Test a partially owned Greenland lot rather than assuming the entire island was purchased.
Test the exact 180-day and 365-day boundaries.
Prove one-time awards and no award from a replayed terminal callback.
Report native engine and save evidence separately from source checks or abstract model tests.
