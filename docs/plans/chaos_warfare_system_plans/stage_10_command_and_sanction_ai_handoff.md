# Stage 10 command and sanction AI handoff

## Later surface correction

The twelve generic supply-chain decision variants described below are no longer player- or AI-accessible. Their identifiers and resolver remain migration-only. Current covert ordinary-agent deployment uses native operative operations.

## Status

This tranche implements route-aware Headquarters role arbitration, condemned-target response profiles, automatic sanction participation, radical-route faction shielding, continued biological pressure near victory, and ordinary-release shutdown during national collapse.

Stage 10 and the overall package remain incomplete.

## Headquarters arbitration

`common/ai_templates/cbrn_hq_support.txt` uses the native `upgrade_prio` base-plus-modifier structure.

The centralized priority order is:

| Situation | Priority |
| --- | ---: |
| Baseline eligible role | 1 |
| Defensive or offensive route preference | 3 |
| Strategic overmatch | 4 |
| Active contamination or outbreak response | 6 |

Protected Headquarters receive the defensive priority under a civil-defence posture. Chemical Fireplan Headquarters receive the offensive priority under retaliatory, battlefield, or strategic posture. Contaminated-Theater Headquarters receive the urgent priority only while the country controls contaminated territory. Biological-Containment Headquarters receive the urgent priority only during an actual outbreak. CBRN Overmatch Headquarters receive the strategic priority under strategic or desperate posture.

Urgent response outranks strategic overmatch, and every role retains its exact technology, equipment, doctrine, and situation gates.

## Condemned-target response profiles

Subsystem-private triggers in `common/scripted_triggers/cbrn_ai_posture_triggers.txt` classify a formally censured country from current ideology, industry, import vulnerability, exact Chaos Warfare route, war state, and native surrender progress.

| Profile | Preferred response |
| --- | --- |
| Democratic and import-dependent | Inspections, compensation, non-use pledge, observers, command reform, and exact stock reduction |
| Authoritarian industrial | Denial, partial compliance, autarky, and limited reform |
| Radical high-chaos | Refusal, propaganda, hardline mobilization, black-market procurement, and allied shielding |
| Unrestricted and near victory | Continued valid operations despite formal censure |
| Losing near capitulation without doomsday authority | Exact biological and chemical stock destruction |
| Losing near capitulation with explicit doomsday authority | Ordinary release routes stop; the separate doomsday decision remains the sole biological release choice |

`common/decisions/condemnation_sanctions_decisions.txt` applies the profile factors only to the condemned country's own response decisions.

## Participant sanctions and shielding

Participant-targeted decision AI remains zero because the existing condemned-country recalculation effect already evaluates every relevant participant from the active condemned target's self-scheduling monthly response pulse. Enabling separate decision AI would duplicate sanction application, escalation, withdrawal, abstention, carveout, breach, enforcement, and shielding actions.

The participant loop is not a broad all-country on action. It runs only from a country with an active condemnation response record.

`common/scripted_effects/condemnation_sanctions_effects.txt` retains the ordinary shielding threshold. When the condemned target has the exact radical high-chaos route, an allied or subject participant may shield at the separate radical-route threshold. Shielding still requires a real faction or subject relation, no war between the countries, and the exact political cost.

## Biological operation continuity

The four ordinary strategic raids, four ordinary battlefield raids, four ordinary operative releases, and two Japan-China campaign actions stop receiving AI selection when the actor reaches its own near-capitulation threshold.

An unrestricted actor under formal censure receives the continued-operation factor only while a current enemy has crossed the exact near-victory surrender threshold.

The separate weaponized-zombie operation is not part of this rule.

The doomsday decision remains separate. Ordinary release routes never substitute for it during collapse.

The retired food, water, and medical supply-chain decisions receive no AI selection. Native operative operations remain distinct from strategic and battlefield biological raids.

## Biological potency and raid probability

This tranche preserves the accepted biological weapon-strength order:

`Tularemia < Anthrax < Plague < Smallpox`

Only Smallpox is severe.

All four ordinary strategic raids retain equal base success, critical-success, and disaster factors. All four ordinary battlefield raids retain equal base success factors. Agent selection changes payload logistics and downstream consequences, not native delivery probability.

## Tuning ownership

- AI surrender thresholds: `common/script_constants/cbrn_ai_constants.txt`
- Condemnation response and shielding factors: `common/script_constants/condemnation_sanctions_constants.txt`
- Biological disabled-operation factor: `common/script_constants/biowarfare_constants.txt`
- Headquarters priorities: file-local constants in `common/ai_templates/cbrn_hq_support.txt`

## Scenario expectations

- A censured democratic import-dependent country prefers compliance and exact stock reduction.
- A censured authoritarian industrial country prefers denial, partial compliance, and autarky.
- A censured radical high-chaos country prefers defiance and may receive exact allied or subject shielding.
- A censured unrestricted country close to defeating a current enemy may continue otherwise valid biological operations.
- A country near its own capitulation does not select ordinary biological raids, covert sabotage, ordinary operative release, or Japan-China campaign actions.
- A collapsing country without explicit doomsday authority strongly prefers exact stock destruction.
- A collapsing country with explicit doomsday authority leaves only the separate doomsday decision as its biological release choice.
- An actual controlled outbreak or contaminated theater outranks speculative Headquarters overmatch.

## Validation evidence

All twelve touched gameplay files retain balanced script blocks.

The four strategic `success_factors` blocks normalize to the same SHA-256 value, `FD30667404DA09A6EA0877717221561B3855C32AE05C06C0C516EFA0BDFA44C4`.

The four battlefield `success_factors` blocks normalize to the same SHA-256 value, `F59133533D98AC2B59E1326ED2B780311A6E7726E5F07097273F190FB97980C5`.

The only severe-result assignment used for a release is the Smallpox-only branch in `biological_doomsday_effects.txt`, and the shared lifecycle validator accepts that severe doomsday record only when the active agent is Smallpox.

## Assets

No asset was created or replaced for this AI-only tranche.

Existing biological military-raid icons under `gfx/interface/military_raids` remain in use and were not overwritten.

## Engine boundaries

Near victory uses the native current-enemy surrender-progress trigger. Near capitulation uses the actor's native surrender progress. No war-goal estimator, target estimator, inferred defeat state, alternate target, proxy state, or fallback is used.

The automatic sanction-participant system retains its existing active-target monthly scheduler. No broad daily, weekly, or monthly all-country on action was added.

The connected HOI4 inspection transport remained unavailable. No unsupported behavior was introduced to compensate for it.

The offensive chemical-artillery and armored-delivery template gates now require the named `cbrn_country_has_verified_chemical_force_target` contract in addition to the operation plan, policy, payload, and standing bill. That contract is deliberately fail-closed because the installed country-scope AI/template surface exposes neither the selected native-raid target nor an Army-HQ-to-target-state pointer. A non-capitulated enemy country is not treated as an exact target, and no random, capital, inferred, or proxy target is retained.

## Remaining Stage 10 work

- event-driven regimental template adoption and removal;
- exact target receipt integration for offensive regimental templates;
- final exact operation target-country and relationship audit;
- differentiated country profiles;
- historically sourced national designer and MIO identities;
- full seven-major and three-minor scenario matrix;
- specialist and completion audits.
