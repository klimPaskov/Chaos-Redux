# Event 080: Achievement implementation and art prompt

Implement all eight achievements in Part 6 of the Airship source specification. Read their full table, the passenger conservation rules, evolution exposure rules, validation matrix, and asset prompt. The IDs below are proposed registered identifiers. Verify uniqueness and the project's exact ID convention before registration. Keep any approved rename synchronised across tracking, localisation, sprites, files, and documentation.

The neutral condition summaries are title and description directions, not finished player-facing text. The localisation pass must write final names and descriptions. No invented achievement phrase may be reused as the final super-event title or quotation.

| Proposed ID | Title and description direction | Player and required evidence | Disqualifiers, difficulty, visibility | Icon subject |
|---|---|---|---|---|
| chaosx_080_clean_voyage | A fully completed civilian voyage with all people accounted for alive | USA, 121 completed transitions, no voyage-related civilian deaths, all missing cases closed alive, at least 300 passengers on 90 steps | No crash, unresolved loss, or unbacked manifest. Demanding, visible | Airship and completed circular route |
| chaosx_080_repaired_return | Recovery from a genuine critical incident followed by a safe return | USA, a non-manufactured serious incident reaches Condition 25 or lower, paid actual restoration to at least 75, complete route with no subsequent deaths | No deliberate self-sabotage or false repair credit. Recovery challenge, visible | Repaired hull and small return motif |
| chaosx_080_international_programme | A substantial international programme with resolved diplomatic issues | USA, qualified Grand Tour, five programme stops in distinct foreign countries, two real protocol disputes settled peacefully, delegations accounted for | No repeated one-stop credit, manufactured disputes, or unresolved detention. Diplomacy challenge, visible | Boarding stair, invitation, small globe |
| chaosx_080_verified_trials | Several different useful experiments brought home safely | USA, three different useful trial families, actual result recovery or transmission, completed route without experimental death | No inconclusive or duplicate-family substitutions and no unrecovered data. Technical challenge, visible | Instruments and airship silhouette |
| chaosx_080_city_homecoming | Sustained operation and safe return of the populated Flying City | USA, thirty city-form steps, ten above 5,000 aboard, three scaled service stops, complete route, at least 95% survival of distinct boarded people | Missing people are not proven survivors. No empty or last-minute city claim. High difficulty, visible | Large hull with a few clear compartments |
| chaosx_080_foreign_rescue | A foreign country conducts a substantial real rescue | Foreign rescue controller, at least 500 actual living people recovered, paid material help, valid settlement or return | Crash instigator, duplicate people, or unresolved rescue cannot qualify. High difficulty, hidden until a qualifying crash | Rescue rope and small hull fragment |
| chaosx_080_reliable_host | Sustained helpful hosting that contributes to a complete expedition | Foreign country, two successful original stop visits, a funded delivered major repair, no deliberate hostile incident, voyage completed | No flyover, cancelled work, repeated reward claim, or self-created damage credit. Resource challenge, visible | Mooring mast and service wrench |
| chaosx_080_wartime_passage | A complete civilian passage through several actual war zones | USA, ten verified local combat-zone steps across three distinct controllers, full route, no onboard confirmed death or unresolved missing group | Remote wars and retroactive declarations do not count. High difficulty, hidden until wartime exposure | Airship above a broken front line |

## Tracking

Use the actual voyage identity, completed steps, delivered services, unique host visits, proven incident causes, backed cohort identities, trial outcomes, and physical-form exposure. Do not infer these from the final Condition, the current evolution flag, or how many times a popup was opened.

Track distinct people so the same traveller disembarking and reboarding does not inflate a survival denominator or a rescue total. Births enter the correct denominator and population history once. People still missing cannot satisfy an all-alive condition. Extinct or changed controllers must not erase legitimate previous service evidence or transfer achievement ownership to a different player.

Achievement checks occur after the relevant actual transitions. Loading, opening the map, receiving a duplicate report, or re-running terminal cleanup must not award additional progress. Keep achievement tracking separate from repeatable economic rewards and generic event-pool firings.

## Registration and localisation

Inspect the existing achievement registry pattern and preserve any single root-level `unique_id` contract. Group event-owned entries under the proper owner section without inventing a separate incompatible registry. Update the actual `common/achievements/` owner, English achievement localisation, `interface/chaosx_achievements.gfx`, final DDS paths, and documentation consistently.

Give the player accurate visibility and difficulty. A route that lacks enough suitable visits need not make every objective attainable in that campaign. Do not generate artificial stops or weaken a condition to make it unlock automatically.

## Artwork

Use one original transparent subject per achievement under the canonical achievement references. Preserve the exact `achievement_template.png`, `achievement_template_grey.png`, and `overlay.png` files and verify their hashes from the current asset skill. Derive new grey and not-eligible source layers deterministically. Use the mandatory achievement processor with the complete triplet.

Provide all three 64 by 64 runtime DDS files directly under `gfx/achievements/`, named from the final registered ID with base, `_grey`, and `_not_eligible` suffixes. Do not add an event subfolder. Inspect native-size readability, exact decoded compositing, template integrity, alpha, and final sprite resolution. Submit the complete contact sheet to the parent for review before declaring assets ready.

## Acceptance

Create a positive fixture and at least one meaningful near-miss fixture for every achievement. Include deliberate-crash rescue farming, empty-city completion, a late physical refit, duplicate host visits, missing people, untransmitted data, and population movement across a controller change. Have the completion auditor verify both the runtime evidence and the final art triplets. A localisation key or image alone does not prove a working achievement.
