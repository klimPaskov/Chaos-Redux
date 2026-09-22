# 08. Winning, closure, and the fate of assistance

## Immediate victory

A participant wins at the first valid positive completion that reaches 100 Influence. Perform final validity checks, settle the delivered action, update Influence, and execute the takeover in the same non-delayed effect flow. A report may be queued afterward, but answering it cannot determine whether puppeting happens.

There is no second payment, target approval roll, diplomatic acceptance check, minimum lead over the runner-up, or mandatory final mission. A valid sponsor reaching the threshold has met the winning condition. Government popularity below 50% does not prevent that sponsor from winning through other forms of dependence.

The race closes only after the engine confirms the target is an actual puppet of the correct sponsor. A failed or unsupported effect is an implementation failure, not a successful outcome with a missing icon. Keep a failed commit in a distinct diagnostic state and do not award achievements, completion notices, or double-paid assets.

## Required settlement

The target becomes a direct normal puppet of the winning participant. Where the installed game has autonomy levels, choose a supported ordinary puppet state with `is_puppet = yes`, not a looser independent partner. The exact identifier and allowed-state rules must be verified against the installed files. This design does not require an integrated-puppet level or immediate annexation.

The target retains its tag, owned states, cores, national focus content, army, navy, air force, technologies, and existing lawful country systems. Event 79 does not transfer its divisions to the sponsor, grant new cores, or replace the national tree. Normal autonomy and later independence processes remain available.

The target's political setup after settlement is the legitimate state produced by the race immediately before takeover. A completed leadership operation can already have changed it. Otherwise a sponsor may end up controlling a client with a different domestic ideology. Snapshot and restore the intended political setup if the native autonomy effect overwrites party popularity or leadership. Do not restore an obsolete opening government over a valid later transition.

## Factions, guarantees, and wars

Remove or change only relations that must change to establish the actual subject relationship. Existing third-party guarantees are not all deleted merely because their countries lost the contest. Campaign-created relations have explicit ownership records. In the new design, opening a race creates no free guarantees.

A target in a different faction must leave or be reconciled into a legal subject arrangement through a proven native sequence. If it leads a faction, preserve the other members through a valid successor arrangement where the engine supports one. Do not dissolve an unrelated faction by accident. Membership in the winner's faction after puppeting is separate from the winning condition and follows a verified supported path.

A target's unrelated wars are preserved where the engine permits the new relationship. Do not use broad `end_wars = yes` as a convenient cleanup. Direct war between sponsor and target suspends peaceful Influence actions, so no valid normal completion should attempt to puppet an enemy in the middle of their own war. Other contradictory war configurations require exact native preflight and runtime tests.

The required range includes faction-member minors, minor faction leaders, targets in third-party wars, and player sponsors that are subjects. These are explicit proof gates. A coding agent cannot narrow the user's participation rule or silently make global peace to conceal an unsupported edge case.

## Ordering and simultaneous completions

The first valid threshold-crossing effect processed by the authoritative game simulation wins. It sets the race to committing before later effects can mutate it. A second completion in the same tick sees that state and performs only its permitted closure or refund path. Do not rank simultaneous candidates by major status, tag name, faction leadership, or a predetermined historical priority.

Native engine processing order is the unavoidable arbitration rule for truly simultaneous completions. It must be reported as such and tested in multiplayer. Client interface selection, popup timing, and local animation completion must have no authority over the result.

## Material settlement

| Asset or commitment | Successful delivery before closure | Undelivered at closure |
| --- | --- | --- |
| Infantry and support equipment | Remains in the target's stockpile even if its donor lost | Return actual held material to its original payer once, unless a previously confirmed lawful delivery has already occurred |
| Advisory experience | Target retains the experience already delivered | Return an undelivered escrowed experience component once. Spent political and command work follows the action receipt |
| Completed buildings and infrastructure | Remain in the target's states | No building is created merely because the race ended |
| Funded construction work | Completed output remains permanently | Preserve work as target-owned project credit. Release the old donor's future industrial reservation |
| Future factory commitment | Already elapsed capacity is spent | Release unelapsed reserved capacity immediately |
| Political work | Popularity and opinion changes already applied remain | Administrative cancellation refunds use the explicit actual-paid rule below |
| Institutional relationship | Represents the campaign history | Rival-sponsored temporary institutions end when incompatible with the new overlord. Their existing material consequences remain |

After closure, an incomplete investment is visible to the target and its new overlord as one finite completion contract. It requires only the remaining factory-days under the original output contract. It gives no Event 79 Influence and no second takeover award. If nobody resumes it, the credit remains dormant. It does not reserve factories forever or silently complete itself.

## Refund reasons

Use the recorded actual paid component, never the pre-discount advertised amount. Equipment and other undelivered escrowed physical assets are returned at 100% once. Already delivered assets are never refunded.

| Closure or cancellation reason | Uncompleted political-power service component | Future factory reservation |
| --- | --- | --- |
| Sponsor voluntarily cancels | No refund | Released |
| Recipient government becomes invalid during government-support action | 50% actual paid, rounded down | Released where relevant |
| Another participant wins before this action completes | 50% actual paid, rounded down | Released |
| Target becomes human, disappears, or is externally puppeted | 100% of undelivered political service | Released |
| Administrative disabling or validated technical invalidation | 100% of undelivered political service | Released |
| Partial interference blocked by another rival's consumed loss budget | Proportional unused political component, rounded down | Remaining future capacity released |

Command power used to run an already begun operation is spent. Army experience transferred into an undelivered advisory receipt is refunded if it was not delivered. An unsupported refund component remains pending for its owner adapter. It is not marked refunded before the real resource credit happens.

## Diplomatic ending

The winning event, target report, and international news must agree on the target, winner, final political alignment, and major delivered commitments. Present the strongest meaningful route from recorded actions. A sponsor that won through industry receives an economic-dependence account. A sponsor that changed the government receives a political-transition account. A mixed campaign mentions the two largest genuine contributions.

Losing participants can receive one concise report with their final score, paid commitments, and outstanding refund disposition. They receive no free war goal or compulsory declaration of war. Their subsequent response belongs to normal diplomacy or another explicitly connected event.

## Invalidation and history

External puppeting is recorded as an invalidated race with the external overlord identified. It is not awarded to the highest Event 79 score. A human taking control of the target ends the contest without letting other players take away that human's country through an AI-only target mechanic.

Keep a compact archive record with race identity, target, winner or closure reason, dates, stage, score at closure, and meaningful delivery totals. Remove active timers, decision targets, institution expiry work, and factory reservations that no longer belong to active play. Historical entries never re-enter the active ranking array.
