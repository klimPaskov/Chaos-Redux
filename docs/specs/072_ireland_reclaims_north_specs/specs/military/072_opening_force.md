# Opening force and permanent military foundation

## Delivered strength

The opening grant consists of fully formed divisions plus separately accounted replacement stocks, available manpower, logistics, and Army Experience.
The force is assembled in supplied Irish-controlled southern provinces.
No formation appears inside hostile Northern Ireland.
Only the amount that the northern approach can supply should deploy directly on the front.
Additional formations gather in reserve locations with explicit AI staging priorities.

| Entitlement | Baseline | Evolution I | Evolution II | Evolution III |
| --- | ---: | ---: | ---: | ---: |
| Line infantry divisions | 4 | 7 | 10 | 12 |
| Assault infantry divisions | 1 | 2 | 3 | 5 |
| Motorized reserve divisions | 0 | 1 | 2 | 3 |
| Total new divisions | 5 | 10 | 15 | 20 |
| Replacement infantry equipment | 5,000 | 10,000 | 15,000 | 25,000 |
| Replacement artillery | 250 | 500 | 1,000 | 1,500 |
| Replacement support equipment | 500 | 1,000 | 1,500 | 2,500 |
| Replacement trucks | 250 | 750 | 1,500 | 2,500 |
| Replacement trains | 5 | 10 | 15 | 20 |
| Convoys | 10 | 20 | 30 | 40 |
| Available manpower after formation | 20,000 | 40,000 | 65,000 | 100,000 |
| Fuel | 10,000 | 20,000 | 35,000 | 50,000 |
| Army Experience | 50 | 100 | 150 | 200 |

These are cumulative tier entitlements, not four stackable packages.
Formation personnel and equipment are additional to the explicitly listed replacement stocks, but must be charged to one supply ledger.
An implementation that creates fully equipped units must not also deposit their full initial equipment cost into the stockpile.
An implementation that pulls units from stockpiles must first fund those exact costs.
The same distinction applies to manpower.
The available-manpower row describes the intended final reserve after all new formations are filled.

The line formation uses ordinary infantry with engineers and support artillery when the event's selected coherent technology floor permits them.
The assault formation adds a stronger artillery component and the support appropriate to a short land offensive.
The motorized formation uses ordinary motorized infantry, engineers, artillery, and logistics, with a truck reserve that can actually reinforce it.
Final battalion composition is chosen against the installed combat and equipment definitions.
Do not hardcode a supposedly optimal combat width into the design.
Templates must remain editable after emergency status ends.

## Quality and era

A weak Ireland receives a coherent infantry and support floor adequate for the current game phase.
Do not grant future-generation technology, complete doctrine trees, every designer unlock, or an unrestricted copy of the opponent's technology.
Use verified early, middle, and late equipment bands based on the campaign year and Ireland's existing technologies.
Grant the minimum missing unit and support unlocks needed to use the package, with a clear list.
Do not downgrade an already more advanced Irish army.

New formations arrive trained enough to be usable, with modest veteran elements in the assault component.
Evolution upgrades increase professional competence and logistical preparation as well as numbers.
They must not start every soldier at the highest experience level or confer invulnerability.
Replacement stocks use a coherent set of variants and can be produced afterward.
Captured or foreign-origin variants require verified production and reinforcement handling.

The first balance target is that a poorly prepared Ireland can take a normally defended North through competent play.
A heavily fortified late-game North remains harder.
No force size can guarantee victory against every possible army without removing the challenge.
Live tests must distinguish a playable opportunity from an automatic result.
If the baseline package is inadequate against the ordinary fixture, adjust the entitlement and support together.
Do not solve it with hidden damage multipliers aimed at a human opponent.

## Emergency logistics

The package provides trains and trucks, a fuel reserve, and a temporary reduction in supply consumption through the Defense Establishment spirit family.
Baseline emergency supply reduction is 10 percent, then 15, 20, and 25 percent by tier.
A 5 percent planning benefit at baseline grows to 10, 15, and 20 percent.
These effects apply to the Irish military under the emergency family and expire at the earlier of the campaign's end plus 15 days or the final 270-day attempt limit.
The normal 180-day attempt limit applies when an extension was not purchased.
Do not add invisible recurring equipment deliveries.

A damaged staging railway or port may receive a one-time repair allocation where the installed effect can repair the relevant structure without free development of unrelated regions.
The plan must record exactly which Irish-owned locations qualify.
It may not set every national infrastructure value to a fixed level or build northern facilities before capture.
Use an immediately useful transport package even where direct repair is unsupported.

## Command

Reuse available Irish commanders and avoid cloning them.
Only add a commander when the available roster cannot command the intended force competently.
Use verified existing characters when appropriate to the campaign date.
A newly authored fictional officer may fill a genuine shortage, with identity marked as fictional in the development manifest and with an original portrait.
Do not present an invented person as a historical officer.
No national leader replacement is required by the opening.

The officer pool should cover infantry operations, logistics, and mobile reserves as the tier grows.
Traits must support a role and have a bounded total value.
Commander count and skill levels must obey engine field limits and the project's numeric conventions with explicit technical exceptions where needed.
Names and portraits are assigned only after the character inventory audit.

## Evolution increments

The grant ledger records cumulative units, equipment, personnel, and experience already delivered by the event.
If the tier rises while the reclamation is active, issue only the difference between the new cumulative entitlement and the earlier one.
Losses do not reset the delivered count.
A player cannot obtain replacements by destroying the opening force before an upgrade.

After success, the opening-grant ledger closes permanently.
Later Evolution changes unlock training contracts, higher formation limits for paid missions, broader doctrine alternatives, and industrial capacity.
After failure, neither immediate force upgrades nor campaign branches continue.
Tier flags remain historical data and never reopen the attempt.

## Transition to a standing force

The first military focus group inventories the emergency army, opens paid retraining, and selects a standing-force or reserve-heavy establishment.
A standing force has higher support costs and better readiness.
The reserve establishment releases part of the manpower burden through voluntary demobilization of explicitly selected event formations and retains a paid mobilization route.
Do not delete unrelated pre-existing divisions or remove their equipment.

A trained-assault route improves existing infantry and supports artillery production.
A mobile route requires domestic truck production, fuel access, and maintenance.
An amphibious route requires landing capacity, escorts, and naval air preparation.
An island-defense route provides useful preparation without forcing expeditionary play.
Each route must include at least one meaningful production choice and one operational use beyond a temporary modifier.
