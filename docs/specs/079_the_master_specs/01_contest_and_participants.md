# 01. Opening the contest and joining it

## Choosing a target

Each successful Event 79 firing selects exactly one existing, independent, AI-controlled minor. The target must own a usable country position and must not already be the target of an unresolved Event 79 race. A subject cannot be selected. Dormant tags, empty testing tags, and countries that cannot sustain the normal civilian political contest are not valid targets.

Do not use the initiating country's factory count as a ceiling. A player-controlled microstate can compete for a larger minor. Do not exclude a country simply because it belongs to a faction or is fighting a third party. Existing faction and war relationships must be handled by the takeover contract in Part 08.

Selection uses the project's ordinary local-crisis weighting when that shared mechanism applies to a target-owned crisis. Existing local crises can reduce selection weight and the shared target crisis-cap adapter can make a target unavailable. Participation as a foreign sponsor does not itself consume a separate domestic-crisis slot for every contested country. This avoids making the Great Game incompatible with normal campaign participation.

All otherwise equivalent candidates are selected randomly. Seed calculations happen after the target is chosen and cannot be used to choose a country that a preferred major is certain to win. Existing politics can make a particular result more likely, but the selector must not inspect a hidden intended winner.

## Who participates

Every major country and every player-controlled country is registered once per race. Registration has no joining fee and is not a guarantee, faction invitation, or diplomatic action. It establishes a score row and permission to use valid actions. All countries are evaluated through the same score and payment rules.

Player minors are explicitly included. A participant does not disappear merely because it loses major status after registration. A new major or newly player-controlled country can join an existing race once, receiving a seed based on the conditions at its actual entry time. It receives no backdated actions or compensation for elapsed time. Changing controllers cannot create a second seed in the same race.

A participant can remain registered while temporarily unable to act. Direct war against the target prevents actions that would build a peaceful client relationship and prevents takeover completion. Its score stays visible as suspended. When peace restores valid relations, the same record resumes. War against some other country does not suspend participation by itself.

The user brief includes player countries that are already subjects. They remain part of the design. Whether the installed engine can give such a country a direct puppet is a critical implementation proof requirement. The coding agent must not silently exclude these players, free them, or award their success to their current overlord. The exact engine limitation and a proposed design change must be brought back for approval if the required relationship cannot be represented.

## Registration and initial knowledge

Opening information identifies the target, its actual ruling ideology, the leading initial contestant, and the main reasons for that contestant's advantage. The player's detailed breakdown is public. The full ranking can be expanded. Intelligence can improve operations, but it does not conceal the numerical finish line or allow an AI-only hidden lead.

Historical hostility and intelligence presence appear only when supported by an actual provider. An unavailable provider is identified in developer diagnostics. It is not converted into a fabricated relationship or a random bonus.

A registered country initially watches the contest without spending. The first action is the commitment point. It receives no free political power for acknowledging the opening event. All free guarantees created by the legacy event are removed from the new design.

## Remaining active, withdrawing, and returning

Withdrawal cancels future campaigns and hides routine notices for that target. It does not erase the entry record, delivered assets, political effects, completed action history, or interference history. A returning participant resumes the same score after any inactivity decay. Rejoining cannot reset saturation, grant a second seed, or refund previously delivered aid.

After 60 days without a completed positive action or a still-funded material project in that target, the participant loses 5 Influence for every further 30 days of inactivity, to a floor of zero. A paused or unaffordable project does not maintain activity. Interference alone does not keep an otherwise abandoned foreign position alive. This is a public time rule and applies equally to AI and players.

The contest has no automatic winner at a fixed date. The highest score below 100 is still insufficient. If everyone withdraws, the target remains independent and the race stays available to returning sponsors. A 90-day inactive contest receives a renewed-interest notice and AI reevaluation, not a free score grant. This preserves the threshold rule and avoids manufacturing a winner simply to free a slot.

## Target changes during play

If the target is annexed, becomes a subject through another process, becomes player-controlled, or loses the country position needed for the contest, close the race without an Event 79 winner. Retain historical records and delivered assets. Reconcile open commitments under Part 08.

Becoming a major after opening does not invalidate the target. The opening chose a minor, and successful foreign investment should not abruptly cancel that race. A civil war keeps the existing race attached to the original government tag if it remains a valid independent AI country. Newly created civil-war tags do not inherit duplicate Influence records. If the original government ceases to exist, close the old race.

A released former target can be selected again only when independent and otherwise eligible. It receives a new race identity and fresh scores. Old completion awards cannot be farmed through repeated liberation of the same client.
