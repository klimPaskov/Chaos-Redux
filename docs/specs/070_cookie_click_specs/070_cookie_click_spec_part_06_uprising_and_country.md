# 070 Cookie Click: the uprising and its country

## A permanent transition

The revolt creates the Cookie Empire inside the host's territory.
The Cookie Monster becomes its leader.
The host's feeding rewards stop permanently.
The Empire immediately fights the host and all valid external neighboring countries, then reacts to new borders as it expands.

The identity is an original animated biscuit creature.
Do not assume the user requested the existing television character with the same general name.
Use the user-provided Cookie Monster and Cookie Empire labels as working names.

The final three-letter country tag must be selected after checking vanilla, Chaos Redux, installed Workshop mods and other local mods.
Use `COOKIE_TAG` in this design until that audit locks an available tag.
It is a planning token, not an engine tag.
Do not copy another mod's existing tag because it appears convenient.

## The strength snapshot

Take one saved snapshot immediately before the uprising commit.
It includes Level, lifetime clicks, evolution, hunger duration, actual consumed value, actual reward value, current host army strength, industrial capacity, population, stocks, supply and territory.
Preparation decisions modify their own recorded component before the final force is calculated.

Use this authored strength index, rounded in 5-point bands.

```text
R =
    min(30, 5 × floor(L / 5))
    + 10 × evolution_number
    + min(10, 5 × floor(lifetime_clicks / 100000))
    + min(10, 5 × floor(reward_value / 5000))
    + min(10, 5 × floor(consumed_value / 500))
    + min(10, 5 × floor(hungry_cycles / 5))

R is clamped to 0 through 100.
```

This combines distinct historical contributions without letting one repeatedly counted variable dominate.
The contribution caps are intentional.
Level, clicks and previous rewards are related, so they cannot each independently multiply the final army without a limit.

Initial field strength targets `20 + 0.5 × R` percent of the host's measured field strength, rounded to 5 percent.
Use a template-strength comparison based on equipment, battalions and combat role, not just division count.
A major with weak one-battalion divisions must not produce a larger uprising than a well-equipped army merely because it has more counters.

A very weak host still produces five light Cookie formations, not five fully equipped elite divisions.
The minimum formation has two Cookie Infantry battalions and no heavy support.
A mature strong uprising upgrades those formations and adds specialist units through the roster rules.
No arbitrary free naval battlefleet appears inland.

## Territory

Target an initial share of `10 + R / 5` percent of eligible host states, rounded to a usable connected group.
The maximum starting share is 30 percent.
A minimum of one state is required.
Keep at least one valid host state and a viable host government.

Select a connected bakery region using actual control, industry, population, supply links and previously exposed anchors.
Prefer an exposed anchor over an unrelated random state.
Prefer a compact front over scattered isolated pockets.
Do not steal territory from another country's occupation simply because the host owns it on paper.

The selected region receives a valid capital, supply route, enough local recruitment capacity and a reason for its industrial strength.
Use an existing town or city in that state.
Do not fabricate a new map province or victory point ID.
A high-strength uprising can take a host capital only if the host receives a valid remaining capital and the outcome was included in the preview.

Small countries may exceed the percentage target because one state is indivisible.
Report that deviation.
The target percentage is not permission to split state ownership through an unverified effect.

At sea, choose a port-connected region when one exists.
An island uprising receives appropriate convoy, transport and coastal production support from its strength budget.
It must eventually be able to leave its island through the naval branch.
An inland uprising has no immediate ship grant and can develop coastal institutions after taking a port.

## Industry and stocks

Transferred industry is counted once.
A factory inside transferred territory is not also granted again as a fresh uprising reward.

The Empire can receive a small startup industrial grant where the selected region cannot support any production.
Its floor is two civilian and two military factories, limited by valid slots and offset against the uprising's industrial budget.
A valid construction queue is required when an immediate level cannot fit.
The floor does not override the state cap.

Give the initial army its required Cookie equipment and a 30-day reserve at its intended operating strength.
The reserve derives from the saved uprising budget and consumed assets.
Do not deduct the same previously eaten stockpile from the host again.
Human host equipment currently present in a transferred national stockpile is a separate immediate transfer and must be recorded as such.

Captured conventional equipment that the Cookie army can use remains usable.
Incompatible equipment enters the conversion decisions.
Do not delete aircraft, trains or ships just because the national identity changed.

## Country identity

The Cookie Monster holds the head-of-government and leader role as an institutional ruler.
It uses no random human name pool.
Its animated portrait has an approved static fallback.
Its political identity is fixed-purpose, centered on appetite and conquest, with internal methods chosen through the focus tree.

Use a supported existing ideology category and a new localized ruling organization.
The plan does not require a new global ideology group.
Elections do not replace the Monster through ordinary party turnover.
The country leaves incompatible normal diplomatic commitments during setup.

The starting government has 50 Stability and 75 War Support before permitted setup modifiers.
Use a suitable mobilization and economic law for a new wartime actor.
Do not grant every strongest law regardless of its documented conditions.
Give two research slots initially, with two further slots available through major programs under a four-slot ordinary ceiling.
The rare pet reward does not transfer an extra slot automatically.

## Leaders and institutions

The Monster is the only required named individual.
Three additional institutional advisor roles are authorized for this country package: a bakery administration, a logistics command and a military shaping office.
They use symbolic institution portraits and institutional labels.
Their exact final names remain localization work.

The bakery administration improves sustainable food conversion and factory efficiency.
The logistics command improves rail, convoy and supply operations.
The shaping office develops specialist Cookie formations.
Only one advisor in each ordinary allowed role is active.
Hiring one does not create another national spirit.

Commanders may use a small fictional Cookie-officer pool with original portraits when the active army requires them.
Define six commander identities as a finite asset target.
Use original biscuit or dough forms, not invented historical humans.
Generated personal names, when used, must match the selected fictional presentation.
The Monster should remain recognizable as the sole supreme ruler.

## Starting problems and national spirits

The Empire starts with two evolving spirits.

| Spirit lifecycle | Starting effect | Route interaction |
| --- | --- | --- |
| Unstable appetite | Strong short-term fighting ability while fed, severe supply and organization penalties while empty | Government methods and food policy reshape it |
| Improvised bakery network | Weak industrial efficiency and costly reinforcement | Industrial and logistics branches replace its stages |
| Military shaping doctrine | Not present at setup | Added through the military branch and developed without adding a fourth spirit |

At most three Event 070 country-package national spirits are active simultaneously.
Temporary pet rewards are removed from the host when their contractual duration ends and do not copy into the Empire.
Advisor traits and ordinary native laws remain distinct, but must not be used to hide a pile of equivalent event spirits.

## Country classification

The Cookie Empire is a special Chaos country with nonhuman armed forces.
Its conquered human civilians still participate in civilian loss, famine, migration and occupation systems where those systems apply.
Do not classify every person inside its borders as nonhuman to bypass humanitarian accounting.

Cookie forces use their own reinforcement and equipment rules.
Converted population and consumed population have distinct outcomes.
Conversion supplies the Empire through an actual debit and its defined return.
Consumption records actual deaths.
The same people cannot be both converted into reserve manpower and counted as eaten.

## Immediate diplomacy

Break inappropriate guarantees, faction membership and military access during setup.
The Empire cannot remain protected by a normal faction while declaring war on its members.

Declare the host war and wars against all valid external neighbors in the commit sequence.
A guaranteed neighbor can pull in additional powers through normal consequences.
Do not suppress that response merely to keep the uprising small.

The Sweet Empire branch requires actual subjects.
An existing Cookie-aligned subject is part of the Cookie political domain and is excluded from the external-neighbor war rule.
This is an explicit interpretation needed to reconcile the requested subject branch with automatic border aggression.
A merely friendly, same-ideology, neutral or allied human country is not exempt.

The Empire can create a Cookie-domain faction only when at least one eligible subject or converted administration exists.
It does not create an empty one-member faction as decoration.
Membership means obedience to the Monster's war policy and real resource obligations.
There is no separate public faction-cohesion meter.

## Commit safety

Before mutation, verify the country identity, host, complete territory set, capital, troop locations, template and equipment availability, diplomatic targets and player-control choice.
The mutation order must never create a playable country without a valid capital or leave transferred states without an owner.

After commitment, repeated callbacks only repair missing setup components.
They do not add another army, duplicate factories, repeat rewards or restart the focus tree.
The saved instance ID and setup-stage flags determine repair.
If preflight fails, preserve the host and pet state and show the structural reason.
Do not pretend a partial transfer is a successful uprising.
