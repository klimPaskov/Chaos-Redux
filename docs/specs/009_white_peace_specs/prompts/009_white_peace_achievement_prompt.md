# Achievement Prompt — Event 009 White Peace

Implement the planned Event 009 achievements only after the core event, dynamic weight model, settlement branches, and event-history tracking exist. Achievement tracking must prove that the unlock came from Event 009 and not from ordinary peace conferences or unrelated scripted peace.

## Achievement list

### `achievement_white_peace_status_quo_ante`

- Title: Status Quo Ante
- Visibility: visible
- Eligible country: player-controlled minor country.
- Unlock condition: the player is a minor country whose war is ended by Event 009 after the war has lasted long enough to count as prolonged. The player remains independent and is not in a major-led faction when the settlement fires.
- Disqualifiers: player is a major, player is a subject, settlement comes from non-Event-009 peace, player receives territory from the war.
- Difficulty: medium; requires a real minor war and a rare event alignment.
- Icon: unchanged border with sealed paper between two flags.
- Tracking notes: set a country flag when Event 009 settles a player-owned minor war and verify no territorial reward was granted by this event.

### `achievement_white_peace_no_winner`

- Title: No Winner, No Spoils
- Visibility: visible
- Eligible country: any player country directly involved in an Event 009 settlement.
- Unlock condition: Event 009 ends a war where neither selected country has lost its capital to the other, and both selected countries still exist and are independent 180 days later.
- Disqualifiers: either selected country capitulates, is annexed, or becomes a subject before the 180-day check.
- Difficulty: medium-hard; requires post-settlement survival tracking.
- Icon: empty hands lowering weapons beside a blank treaty page.
- Tracking notes: use timed flags or delayed check event; store the pair safely if the achievement system supports pair tracking.

### `achievement_white_peace_chain_of_tables`

- Title: A Chain of Tables
- Visibility: hidden
- Eligible country: any player country in a campaign where Event 009 is active.
- Unlock condition: in one campaign, Event 009 settles at least six separate minor-country pairs before any major-country settlement branch fires.
- Disqualifiers: a major-country settlement branch fires before the sixth minor-pair settlement.
- Difficulty: hard; requires many safe minor wars without the stronger branch intervening.
- Icon: several negotiation tables receding into shadow.
- Tracking notes: global counter for Event 009 minor pairs settled; global flag once a major-country settlement branch fires.

### `achievement_white_peace_silence_of_giants`

- Title: Silence of Giants
- Visibility: hidden
- Eligible country: player-controlled major country.
- Unlock condition: the player is part of a major-country settlement branch after a long war, and Event 009 grants no conquered territory to the player.
- Disqualifiers: settlement branch is not the major-country branch, player gains states from the war through the event, or the war was too short.
- Difficulty: hard; requires evolved stage and major-war conditions.
- Icon: two large artillery silhouettes lowered beneath a paper seal.
- Tracking notes: branch-specific flag on Event 009 major settlement; ensure no state transfer from Event 009.

### `achievement_white_peace_the_circular`

- Title: The Circular Reaches Every Desk
- Visibility: hidden
- Eligible country: any player country in a campaign where Event 009 is active.
- Unlock condition: one broad diplomatic settlement branch ends at least three separate safe conflicts or at least five safe pairs from one firing.
- Disqualifiers: branch settles fewer than the required count or uses any protected conflict.
- Difficulty: very hard; requires late-stage war clutter and safe broad-branch execution.
- Icon: circular telegraph/stamp motif over several envelopes.
- Tracking notes: store settled pair count and separate-war count during the Event 009 branch; unlock after the branch finishes and validation confirms no protected war was touched.

## Implementation requirements

- Add achievement localisation and icons according to existing achievement system patterns.
- Track Event 009 settlement branch type explicitly.
- Track minor pair count, major branch fired, and broad branch settled count.
- Avoid achievements that unlock only because the event fired once.
- Include the achievement IDs and tracking variables in the completion report.
- If the repository achievement system does not support one of these conditions cleanly, report the exact blocker and queue that achievement rather than simplifying it into an easy unlock.
