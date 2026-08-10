# Event 005 Patron Rivalry and Reconsolidation

Status: Implemented. No further Event 005 implementation is required for Patron Rivalry or Reconsolidation and Aftermath in this scope. Later unrelated events may consume the persistent flags emitted by these chains, but those consumers do not reopen or own this implementation.

## Patron Rivalry

The Patron Rivalry chain records the first German, British, Japanese, French, American, Turkish, Persian, Polish, Romanian, and Finnish aid channel opened for each Event 005 successor.
The registration runs through the existing foreign-aid recipient effects, so it introduces no recurring all-country scan and cannot create a second intervention scheduler.

The first contact from each patron fires events `chaosx.nr5.50` through `chaosx.nr5.59`.
Two or more distinct channels fire the general collision event `chaosx.nr5.60` once.
German-British, American-Japanese, Turkish-Persian, Polish-Romanian, and French-American overlaps fire the bounded pair events `chaosx.nr5.61` through `chaosx.nr5.65` once per republic.
Volunteer overlaps use separate channel flags and fire events `chaosx.nr5.66` through `chaosx.nr5.70` once per qualifying pair.

The player can impose a common ledger, auction access, assert neutrality, create a joint board, militarize a pair of channels, merge volunteer rolls, auction volunteer precedence, or nationalize the rolls.
Each outcome changes live recognition, depot control, patronage risk, League support, manpower, equipment, stability, war support, or Soviet foreign pressure.
The chosen policy also changes later general-aid or volunteer deliveries through shared scripted effects.

All gameplay values and AI thresholds live in `soviet_collapse_patron_rivalry` in `common/script_constants/005_soviet_collapse_constants.txt`.
AI event choices react to patronage pressure, recognition, depot control, League support, stability, and war state.

## Reconsolidation and Aftermath

The `Declare the Union Territory Recovered` decision no longer resets the crisis immediately.
It first copies Moscow Authority, Military Obedience, Republic Confidence, Depot Vulnerability, Foreign Appetite, League Cohesion, Old Movement pressure, total collapse threat, months active, and breakaway count into persistent aftermath variables.

Event `chaosx.nr5.96` then converts those surviving pressures into one of three settlements:

- restored command preserves `soviet_collapse_union_restored` and places surviving successors under renewed central-command pressure;
- a federal charter preserves `soviet_collapse_new_union_negotiations` and gives surviving successors a standing federal and League-coordination framework;
- a guarded frontier preserves `soviet_collapse_legal_restoration_claim` and treats surviving successors as lasting frontier states.

Every surviving entry in `global.soviet_collapse_breakaway_countries` receives a matching country flag, lasting spirit, and the triggered follow-up event `chaosx.nr5.97` before the breakaway registry is cleared.
Only after propagation does the existing reconquest cleanup disable crisis missions, intervention boards, release schedulers, temporary targets, pressure values, and original-Union state markers.

All AI weights and snapshot thresholds live in `soviet_collapse_reconsolidation_aftermath` in the Event 005 script-constants file.

## Visual Assets

These mechanics reuse the registered `GFX_report_union_crisis` report image and the existing, semantically matching final idea icons for Union Restored, New Union Negotiations, Legal Restoration Claim, Defensive Coordination, and Republic League Coordination.
No new sprite identifier or unwired visual asset is required.

## Future Plans

No further Event 005 implementation is required for these chains. The implemented chain is self-contained: every choice has immediate gameplay consequences, persistent state, successor propagation, localisation, and AI behavior. Later unrelated events may consume the settlement and aftermath flags as persistent inputs.
