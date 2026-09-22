# Event 82 achievement implementation and asset prompt

Implement the three Law Upgrade achievements from Part 10 in `docs/specs/082_law_upgrade_specs/`. Read the complete event specification, AGENTS, current achievement patterns, the full asset skill, the canonical achievement registry, and all relevant tracking and icon consumers before editing.

Use the single canonical root owner `common/achievements/chaos_redux_achievements.txt`. Inspect its actual current schema and naming conventions. Do not create a separate Event 82 achievement root, alternate award system, or easy event-fired achievement.

The identities below are proposed stable planning identities. Check collisions before final registration.

## A. `law_upgrade_endure_extremes`

Title direction: enduring total mobilization and surviving a desperate defensive war. Description direction: convey the sustained burden and actual victory rather than merely adopting two laws.

Eligible country: any player-controlled country using both compatible extreme-law families. No country tag, ideology, or DLC requirement.

Unlock: hold both laws continuously for 90 game days during a real defensive war against a major. After qualification, defeat the qualifying major opponent or opponents in that war without having capitulated during the qualifying interval or before victory. A white peace is not a win. Demobilization after the 90-day qualification is permitted.

Disqualifiers or reset conditions: not a defending participant, interruption of both-law tenure or qualifying defensive war during the 90-day interval, capitulation, synthetic fixture, or invalid victory evidence. Losing the laws after qualification does not invalidate an otherwise legitimate later victory.

Difficulty: very hard. Visibility: visible once Event 82's evolution information is discoverable under existing achievement rules. It is not trivial because it requires sustained destructive laws and a real military outcome.

Icon: intact but exhausted industrial and military command surviving the mobilization apparatus. Avoid real-person portraits and nationality-specific flags.

Track: qualifying country identity, qualifying war and major opponents, continuous interval, qualification completion, capitulation history, verified outcome, and one-time award.

## B. `law_upgrade_restore_workforce`

Title direction: restoring productive capacity while continuing the war. Description direction: explain that exceptional recruitment was reversed while the extreme industrial commitment remained.

Eligible country: any player country with both laws during a real war, using a verified weighted equipment-fulfillment provider.

Unlock: begin with at least a 20% weighted deployed-land-force equipment deficit, pay to reverse Totalen Menschen!!!, retain Totalen Krieg!!! and the war, then reach at least 95% weighted equipment fulfillment for 30 continuous days. Retain at least 75% of deployed land-force manpower recorded at reversal throughout the recovery interval.

Disqualifiers or resets: peace, re-entering the conscription extreme, leaving the economy extreme, falling below the required retained-force manpower, falling below equipment fulfillment during the final interval, zero equipment requirements, test fixtures, or unverified equipment weighting. The qualifying paid reversal must be genuine.

Difficulty: hard. Visibility: visible after the player has encountered both extreme laws. It is not trivial because simply deleting the army does not satisfy the recovery requirement.

Icon: civilian tools restored to a working war factory while the recruitment apparatus is taken apart.

Track: paid transaction, starting shortage, deployed-force baseline, current weighted fulfillment, continuous interval, law and war continuity, and award state. Do not equate all equipment units. Use verified owner-supported cost or equivalent weights.

## C. `law_upgrade_restore_civilian_life`

Title direction: a country returning to civilian life after extreme mobilization. Description direction: emphasize both deliberate reversals and sustained recovery.

Eligible country: any player country that has held both laws and completed the two manual exit transactions. A legitimate zero-price ordinary law transaction remains valid.

Unlock: after both paid exits, maintain peace, economy at or below Partial Mobilization, conscription at or below Limited Conscription, Stability at least 60%, and control of the national capital for 90 consecutive game days.

Disqualifiers or resets: forced removal alone cannot supply paid-exit history. Any failed current condition resets the 90-day interval. Test fixtures cannot award.

Difficulty: medium-hard. Visibility: visible after an extreme law has been encountered. It is not trivial because the country must pay for both reversals, lower ordinary laws further, and sustain stable peace.

Icon: an ordinary civilian workshop and restored civil administration after withdrawal of an extreme mobilization notice.

Track: real both-law history, each manual reversal result, current law tiers, Stability, peace, capital control, interval, country-identity continuity, and award.

## Common implementation requirements

Use the existing canonical progress, visibility, award, save, and player-country mechanisms. Preserve identity through legitimate cosmetic or country changes without borrowing another country's history. No duplicate awards on reload, multiplayer delivery, tag change, or re-entry.

Write final localized titles and descriptions from these directions after inspecting project style. Use accurate conditions, no raw identifiers, and no claim that the report click itself awards anything.

Coordinate all three subjects and their three standard visual states with the icon artist. The nine final outputs follow the canonical 64×64 achievement pipeline and exact existing state naming. Do not fabricate frame templates.

Add positive and near-miss tests for every condition, artificial debug disqualification, zero denominators, paid-versus-forced exit distinctions, interval resets, and save/load continuity. Keep provider or war-outcome uncertainty as a blocker instead of substituting easy conditions.

Deliver registration, tracking documentation, localization, wired icons, actual evidence, and unresolved issues to the parent. Do not claim completion until every declared condition and visual state works through the canonical system.
