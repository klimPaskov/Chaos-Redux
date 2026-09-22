# Player presentation, AI, and writing

## Player decisions during the event

The player's main decisions concern where to place real divisions, which frontier can afford losses, and how much attention to remove from other wars.
The native border battle provides the combat surface.
Event 078 does not replace it with an abstract strength comparison or a paid decision that resolves the state award.

The opening communication identifies all of the country's admitted disputes in one country-level notice.
It explains that only the named disputed state is at stake in each battle and that other wars do not remove these commitments.
A player acknowledges the notice without approving, refusing, or delaying the battles.
Closing the notice is not a military action and has no political-power, stability, or war-support effect.

## Native information category

Use a compact informational decision category while the country has active Event 078 disputes or pending achievement and containment holds.
Its purpose is to help the player find active fronts, read stakes, and understand why an apparent continuation ended.
It does not introduce an event-specific resource or a separate interactive scripted GUI.

The country overview shows active disputes, the applicable wave profiles, and pending hold objectives.
Each dispute entry identifies the opponent, disputed state, attacking side, current stage, and chain depth when relevant.
A state-targeted native interaction should select or center the relevant state through a verified existing consumer.
If that consumer cannot support the interaction safely, retain a clear native state-targeted display and do not add a paid placeholder action.

For a country involved in several waves, show the wave identity on the relevant entry.
Do not combine the same opponent's distinct state disputes into one misleading combat record.
The category may group entries by opponent for readability, but every underlying stake remains inspectable.
There is no arbitrary rule that only the first five conflicts are visible.

Progress entries for a hold objective show its subject, remaining duration, and the conditions that can still invalidate it.
They do not allow the player to reset a failed hold for a fee.
The category closes once it has no meaningful live information.
Historical records remain in the shared history interface.

## State information and tooltips

At the start, name the target's owner and the attacking country.
Explain that attacking victory transfers this target and defending victory retains it.
The staging state is visible as a combat endpoint, with no implication that it is a second stake.
Use the same territorial explanation in result notices and the information category.

A chain entry distinguishes its current battle from the territory already captured.
When a chain stops because no new adjacency exists, the explanation refers to the frontier no longer offering a valid advance.
When it stops because another conflict occupies the required state, the explanation refers to an unavailable next front.
A technical result-identity failure is reported as an unresolved or cancelled dispute, never as a military victory.

Whole-number game values use the project's dynamic formatting conventions.
Costs, durations, thresholds, and chances must come from the same gameplay values used by the event.
Final localization is written during implementation and is outside this planning package.

## Notices and history

The opening report is aggregated per affected country and wave.
One world-news item introduces a wave that actually starts native fighting.
A wave with no successful starts has no false outbreak headline.
The shared event log records the event firing once, subject to the framework's existing distribution rules.
It does not advance the main event countdown for every border battle.

Country result notices may aggregate results from the same game day.
Aggregation must not delay ownership transfer, momentum, or the release of reservations.
Every aggregated result preserves the opponent, stake, outcome, and wave identity in its detail data.
An attacking capture, a successful defense, and a cancellation cannot share an ambiguous generic victory message.

Applied evolutions receive their own framework-supported history record after the mutation takes effect.
The shared Event Details text remains narrative-only.
Its job is to describe what happened, not to duplicate a rules manual or expose internal counters.
Mechanical information belongs to ordinary gameplay tooltips and the event's informational category.

## Writing briefs and key inventory

These are writing purposes, not finished player-facing localization.
Retain the existing runtime namespace only where it remains an intentional compatibility boundary.
Use event-owned descriptive localization keys for new surfaces and verify the final naming with the repository's current conventions.

| Surface | Writing purpose | Required dynamic subjects |
| --- | --- | --- |
| Country opening | Reports that several local disputes have become actual border battles | Country, wave, opponent and state list |
| World news | Describes a widespread outbreak without claiming a declared world war | Confirmed participating countries or neutral worldwide summary |
| Attacking victory | Confirms acquisition of the single disputed state | Winner, former owner, state |
| Defensive victory | Confirms retention and, when true, the end of an advancing chain | Defender, attacker, retained state |
| Cancelled dispute | Explains the relevant change without assigning a military winner | Pair, state, cancellation reason |
| Momentum continuation | Connects a new battle to the latest capture | Advancer, opponent, captured staging state, new target |
| Chain conclusion | Summarizes the completed advance and reason it ended | Opponent, captured states, terminal outcome |
| Evolution application | Describes the actual change to the wave's border fighting | Wave and applied evolution |
| Information category | Makes all live stakes and holds easy to inspect | Active dispute count, individual targets, hold progress |
| Achievement progress | States the remaining real conditions without exposing debug counters | Required opponents, captures, held states, duration |

Required key families include opening title and description, outcome-specific descriptions, continuation and termination reasons, evolution descriptions, category labels, per-dispute labels, hold progress, achievement names and descriptions, and all relevant tooltips.
Outcome descriptions need separate capture and retention branches.
Names of countries and states always come from the current scoped objects or validated historical subjects as appropriate.
Do not hardcode a historical country pairing into a worldwide event.

The writing tone can be dry and mildly ironic in an acknowledgement option.
Military losses and territorial consequences still need plain descriptions.
Avoid fabricated historical quotations and avoid calling every clash an invasion or a declared war.
There are no researched quotations or super-event remarks to fill.

## AI intent

The global allocator applies the same eligibility and random stake rules to player-controlled and AI countries.
There is no event acceptance option to bias, because participating in the allocated battle is mandatory.
AI acknowledgment has no outcome selection.
The information category carries no purchasable strategic actions and does not need artificial decision willingness scores.

Native troop commitment and battle behavior must remain functional when an AI country has several Event 078 fronts and an unrelated normal war.
The intended behavior is for real border armies to fight under ordinary native constraints, including losses and competing commitments.
Do not create free border divisions, teleport distant armies, or reset organization to make the AI appear successful.

If native behavior leaves AI participants unable to engage valid simultaneous fronts, document the exact scenario and engine behavior before proposing an event-owned AI intervention.
Any proposed intervention must stay within the available native mechanics, be bounded to the active conflict, and be audited separately.
A broad permanent AI strategy change is not part of this specification.

## Accessibility and practical presentation

The ordinary battle, target-state identity, and outcome must remain understandable without opening the shared history window.
Use text labels alongside icons.
Do not rely on color alone to distinguish attack, defense, continuation, and cancellation.
Long country names and several simultaneous disputes must fit through native text and list behavior, not through shrinking all text.

The UI acceptance review uses actual game screens at the project's supported resolutions and UI scales.
A written layout plan, a mock image, or a successful script parse does not establish usability.
The presentation work remains unvalidated until those consumer checks are completed.
