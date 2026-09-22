# Events, news, and writing direction

All labels below are working references.
Write final localisation only after checking the active actors, actual effects, and any historical or cultural references.
The game text must never expose this package's implementation notes, pending research, internal lifecycle tokens, or developer instructions.

## Main presentation sequence

| Reference | Surface | Trigger and viewpoint | Information and writing direction |
| --- | --- | --- | --- |
| EV01 | Irish opening report | The commitment transaction succeeds | Irish government and mobilized forces announce the attempt. State the limited objective, practical military help, and earned tree reward. Use resolve and political irony without a generic staff-table scene. |
| EV02 | Holder report | The holder enters the recorded war | The current government must respond to an actual Irish offensive. Explain the five-day full-objective settlement rule. Use current country and leader titles only when valid. |
| EV03 | Public opening news | The war is committed | Show mobilization, northern disruption, and reactions. Do not report victory, a completed union, or an empire. |
| EV04 | Reclamation difficulty | Day 150 with valid extension opportunity | Present the continuing military situation and the actual extension cost. Avoid inventing progress when Ireland holds no northern ground. |
| EV05 | Settlement report | Objective proof and successful peace | Explain the northern transfer and the end of event hostilities. Mention other wars only when needed to avoid implying a worldwide peace. |
| EV06 | Reunification news | Success is committed once | Show the larger civic and political consequences of reunification through celebrations, protests, returning services, and the work now facing the government. This is the campaign's major opening milestone. |
| EV07 | Failed attempt | Permanent failure | Report the real outcome, surviving government or defeat, and the absence of the new campaign reward. Do not invent a civil war or say peace was signed if hostilities remain. |
| EV08 | Constitutional decision | U02 is reached | Present the actual institutional choices and the people affected. Explain tradeoffs in effects and tooltips. Keep civilian disagreement distinct from armed wrongdoing. |
| EV09 | Security and service dispute | The once-only early integration test | Show a specific administrative or security dispute. Offer review, negotiated compliance, or central intervention with their real costs. |
| EV10 | Northern settlement maturity | U08 completes | Present institutions that now function and agreements that were honored or imposed. Avoid claiming that all local political disagreement disappeared. |
| EV11 | Scottish offer or independence outcome | A valid relationship changes | Use the Scottish viewpoint as well as the Irish offer. State whether sovereignty is retained, shared, or explicitly transferred. |
| EV12 | Welsh alignment | A Welsh government accepts a substantive relationship | Show Welsh priorities and terms. Cultural connection alone is not the cause of automatic annexation. |
| EV13 | Breton participation | A valid Breton relationship is accepted | Focus on the actual maritime, cultural, or institutional agreement. Do not reuse Welsh or Scottish text with only a tag swap. |
| EV14 | Gaelic Empire proclamation | Imperial formation succeeds | Present the imperial government's claim, its Irish-Scottish foundation, and the commitments it has taken on. Do not list every possible future conquest as already accomplished. |
| EV15 | Celtic league | The initial league forms | Announce a real alliance and its accepted obligations. Reserve federal language for the later constitution. |
| EV16 | Federal constitution | The full federal bloc qualifies and forms | Show the participating governments and the common institutions they have agreed. Keep their retained sovereignty clear. |
| EV17 | Federal dispute or withdrawal | A concrete obligation fails or a member leaves | Name the actual dispute and practical loss of common capacity. Avoid treating withdrawal as a scripted Irish annexation. |
| EV18 | Atlantic recognition | T07 completes | Show maintained shipping, air and naval capacity, and the actual access network or domestic long-range alternative. Recognition follows achieved capability. |
| EV19 | Overextension | A first relevant burden threshold is crossed | Show the specific ports, garrisons, contracts, or commitments that are overloading the state. Do not announce an abstract meter as the story. |
| EV20 | Northern loss and recovery | An earned campaign loses and then restores the North | Reflect the established government and its prior choices. Recovery does not pretend the original event fired again. |

## Choices and humor

Use sharp political irony, institutional self-interest, and culturally researched remarks in option writing where the situation permits them.
An aggressive imperial government may speak with overconfidence and an opposition voice may question the actual cost.
The humor should come from a recognizable choice or contradiction in policy.
Do not insert ethnic caricatures, repetitive potato jokes, drunken stereotypes, generic internet memes, or profanity.
Avoid making every option either an identical serious sentence or a random joke disconnected from the effect.

A refusal by a Scottish or Welsh human player should have a firm, plausible political voice.
Do not insult the player for declining an Irish offer.
A northern civilian dispute should not use the language of a supernatural crisis or imply that all opponents are criminals.
Gaelic cultural references require source checking and correct spelling before they become finished text.

## Dynamic text

The holder, legal owner, member countries, actual states, selected constitution, route, and treaty type are dynamic.
Use localisations that are valid when Britain is absent or not the holder.
Do not cache a stale holder name across a war succession.
A recipient that no longer exists needs a controlled cancellation message, not a broken country token.

The description must agree with the effect.
Access is called access, a lease is described only if the engine implements its promised rules, and a sovereignty transfer is explicit.
A formation tooltip describes which country's control qualifies each state.
An ally holding Scottish territory does not turn the imperial puzzle green unless the actual formation policy allows it.
This package's policy does not.

## Focus and decision writing

For each focus, explain the intended institution, operational change, or investment and the practical action it unlocks.
Avoid repeating a generic national greatness claim across dozens of descriptions.
Political groups emphasize institutions and tradeoffs.
Military groups emphasize equipment, training, production, or operations.
Diplomatic groups explain what the other government gains and what it must accept.

Decision tooltips show the exact quoted cost, relevant time, target, requirement, outcome, and interruption rule.
Use native text icons for costs.
Do not place a long engineering explanation in the category description.
Keep the current objective and two public custom values readable, with detailed conditions in their factual tooltips.

## Event details, catalogs, and logging

Event-detail text explains the immediate war, the victory-gated tree, the three Evolutions, and the major strategic possibilities without spoiling every later incident.
The catalog summary is finalized only after effects and localisation are stable, and is mirrored to the authoritative workbook before exporting CSV.
The existing event log records the initial firing, success or failure, Evolution changes, and major route outcomes through its existing schema.
Repeated progress checks and individual state-piece redraws are not log entries.
