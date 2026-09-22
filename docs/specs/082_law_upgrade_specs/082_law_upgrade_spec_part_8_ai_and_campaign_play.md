# Law Upgrade
## Part 8. AI behavior and campaign play

## Equal compulsory treatment

The global firing has no AI acceptance choice. Human and AI countries receive the same War Support, category progression, structural checks, and cap behavior.

The AI cannot delay the effect by leaving an event open. It cannot refuse on political grounds, receive a cheaper forced result, or substitute another law.

## Decisions after mobilization

The AI should evaluate the difference between keeping its current law and taking a particular available exit. It must account for the other extreme law if both are held.

The relevant state is the actual campaign: equipment and manpower shortages, existing forces, war prospects, support, available Political Power, civilian recovery needs, resources, and the price of the contemplated change.

The AI should not simply choose the greatest law level because it has the word “upgrade”. Stronger mobilization is a direction, not a universal improvement.

## Voluntary extreme entry

Voluntary entry remains available under Part 3, but the AI treats it as exceptional.

For Totalen Krieg!!!, the strongest case is a substantial functioning military industry, an active and consequential war, and equipment production that is materially constraining the war effort. It should consider whether resource shortages or bombing make the promised output increase largely unusable.

For Totalen Menschen!!!, the strongest case is genuine reinforcement or deployment failure caused by manpower exhaustion while the country still has equipment or a credible way to obtain it. A large equipment deficit with ample manpower is a reason against entry.

At peace, AI voluntary entry has zero eligibility under the proposed war gate. Neither the AI nor the human bypasses the 80% War Support condition for voluntary entry.

An existing extreme law is not automatically abandoned simply because the country would no longer qualify to buy it. Ongoing need and the consequences of exit still matter.

## Reversal priorities

The AI considers the two exits independently.

It should favor leaving Totalen Menschen!!! when the legal manpower ceiling is no longer essential and recovering the workforce would materially improve the war effort. The evaluation includes the fact that already-deployed forces are not automatically destroyed by lowering the law.

It should favor leaving Totalen Krieg!!! after peace or when civilian construction, repairs, research, and political recovery matter more than the wartime bonus. It must not count wartime bonuses that are currently inactive.

Under both laws, the AI compares the marginal recovery from each action. It does not presume that leaving both is affordable or that the first action's price remains the second action's price.

## Saving Political Power

When a reversal becomes a sustained priority, the AI should reserve enough Political Power for that action and avoid optional spending that repeatedly prevents it. Necessary emergency actions remain eligible according to their owners.

There is no AI-only discount, Political Power grant, automatic bankruptcy escape, or silent waiver.

The price estimate is refreshed when modifiers or discounts change. An action that was affordable before another purchase may no longer be affordable at confirmation.

## Starting preference model

The following is a proposed relative-priority model for reversible actions. It is not a set of percentages or a claim about observed game probabilities.

| Situation | Leave economy extreme | Leave conscription extreme |
| --- | ---: | ---: |
| Base priority while holding the relevant law | 20 | 20 |
| At peace | +100 | +100 |
| War Support below 50% | +40 | +40 |
| War Support below 25%, additional | +40 | +40 |
| Serious civilian reconstruction need | +40 | +20 |
| Equipment shortage with no manpower shortage | -20 | +100 |
| Critical reinforcement manpower shortage | 0 | -100 |
| Defensive war against a stronger enemy | -20 | -20 |
| Other extreme law also held | Evaluate marginal recovery | Evaluate marginal recovery |

A negative total becomes zero. Unaffordable actions cannot execute, but their strategic priority may still justify reserving Political Power.

“Serious reconstruction”, “equipment shortage”, “critical manpower shortage”, and “stronger enemy” must be bound to documented and testable country-level inputs in the implementation handoff. The probability scenarios specify starting thresholds.

The priority model must be evaluated in the real candidate pool, including other available spending choices. Dividing one action's score by only the two reversal scores would not establish its actual selection probability.

## Avoiding repeated mistaken choices

The AI should use its ordinary bounded reevaluation cadence and respond to significant changes in law, war, support, shortages, and price.

A newly forced law is not an order to preserve it for a mandatory waiting period. An immediately sensible paid reversal remains permitted.

Conversely, the AI should not voluntarily buy an extreme law and immediately buy its exit under unchanged conditions. The entry and exit evaluations must share the same assessment of need and recovery.

No new global daily AI scan is authorized by this package.

## Campaign situations to test

### A peaceful democracy at low support

The compulsory event still advances normal laws. If Evolution III forces an extreme law, the country receives the full 50 percentage points before the extreme penalties are evaluated. The AI should then recognize the peacetime cost of retaining that law and save for an appropriate reversal.

### A major power with equipment shortages

The economy extreme can be useful, especially with high support and functioning resource imports. The conscription extreme should be unattractive when manpower is already adequate.

If both were forced, leaving the conscription extreme may be the most effective way to increase actual equipment production.

### A minor country in a losing defensive war

The normal law steps matter even before an extreme is reachable. At the conscription endpoint, keeping the exceptional pool may be defensible when reinforcements are the binding constraint.

The AI must not assume that being a minor makes mobilization useless or makes the exit cost affordable.

### An isolated importer

Trade closure elsewhere can remove imports while its own trade law advances. The AI must evaluate real resource constraints instead of valuing theoretical factory output alone.

The event does not promise that an isolated country can sustain the extreme economy.

### A country recovering after victory

The war-dependent economic bonuses stop at peace. The AI should prioritize demobilization and reconstruction while preserving the same doubled reversal costs a player would pay.

### A subject or a government in exile

The country remains part of the global wave and follows its real available law systems. The AI's priorities reflect its own accessible economy and population rather than fictional full control over its overlord's resources.

### A country with both laws at maximum support

The AI still sees serious civilian penalties. The world's most enthusiastic government should not consider the package harmless.

## Verification limits

The supplied probability-auditor role could not be invoked in this session, and the HOI4 probability tools were not available. These priorities and timing parameters remain design proposals.

The separate probability-scenario file defines the required inspector, evaluation, sweep, simulation, and comparison evidence. No score in this specification is represented as a verified selection chance or cumulative MTTH probability.
