# Stage 7 Japan–China Biological Campaign Validation

Date: 2026-07-24

Status: implemented source tranche; Stage 7 and the overall Chaos Warfare goal remain incomplete.

## Accepted Requirement Coverage

| Requirement | Implementation evidence | Status |
| --- | --- | --- |
| Historically specific Japanese actions in China may use decisions rather than replacing biological raids. | Two exact-state decisions exist under `japan_biological_campaign_category`, while all strategic and battlefield biological raid definitions remain unchanged. | implemented |
| The campaign must use actual agent payload. | Anthrax consumes `anthrax_bomb_1`; Plague consumes `plague_bomb_1`; both also consume Political Power, Support Equipment, and Command Power. | implemented |
| Every release must enter the shared ordinary-agent lifecycle. | Both actions create a deliberate `japan_china_campaign` seed for the selected state and call `bio_lifecycle_dispatch_seed`. | implemented |
| Agent potency and delivery success must be separate. | Both decisions receive the same deterministic release acceptance after their gates pass; Anthrax and Plague retain different canonical lifecycle profiles only after dispatch. | implemented |
| Weapon strength must remain `Tularemia < Anthrax < Plague < Smallpox`, with only Smallpox severe. | The shared lifecycle applies the canonical 0.85, 1.00, 1.15, and 1.30 strength ladder; this campaign does not redefine severity. | implemented |
| The exact selected state must be preserved. | The state-targeted decision supplies `FROM`, the effect saves that scope as `japan_bio_campaign_state_target`, and no target search or replacement branch exists. | implemented |
| The historical route must be explicit and route-aware. | Original Japan, active war with a Chinese country, Pingfang, the Ishii program, Ishii authority, CBRN readiness, strategic-use policy, security, and attribution-control gates are required. | implemented |
| Containment and reform routes must block offensive campaign actions. | Containment, reform, and prisoner-experiment shutdown flags close the route. | implemented |
| AI must use real route, stock, target, and consequence conditions. | Player and AI share the same availability gates; AI separately weighs supply targets, urban targets, doctrine aggression, repeat use, Condemnation, and import vulnerability. | implemented |
| No fallback, estimator, proxy target, or broad periodic pulse may be introduced. | Invalid contexts fail closed, no alternate state is searched, no continuous-air logic is involved, and no daily, weekly, or monthly all-country on-action was added. | implemented |
| Existing raid icons must remain available and unmodified. | The category has an independently produced decision-category icon and both actions reuse existing exact-agent decision sprites; no file under `gfx/interface/military_raids/` or `gfx/interface/raids/` was edited. | implemented |

## Cost and Debit Contract

| Action | Political Power | Agent payload | Support Equipment | Command Power | Base actor cooldown | State cooldown |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Contaminate Supply Networks | 35 | 8 Anthrax Payloads | 35 | 10 | 90 days | 180 days |
| Disperse Plague Vectors | 40 | 10 Plague Payloads | 45 | 14 | 90 days | 180 days |

The custom cost validates and displays all four resources but does not consume them.

The complete effect therefore revalidates every route, target, and resource condition before debiting Political Power, the exact payload model, Support Equipment, and Command Power together in the committed release chain.

This structure follows the installed Decision Modding documentation, which states that `custom_cost_trigger` and `custom_cost_text` do not perform the resource debit and should not be combined with a regular Political Power `cost`.

Theater Contamination doctrine reduces the actor cooldown to 60 days and refunds 2 Command Power after a valid dispatch.

Terminal Hazard doctrine reduces the actor cooldown to 45 days and refunds 4 Command Power after a valid dispatch.

Doctrine never refunds Political Power, payload, or Support Equipment.

## Contract Scenarios

| Scenario | Expected result | Source proof |
| --- | --- | --- |
| Japan lacks Pingfang, Ishii authority, readiness, strategic-use policy, security, or attribution control. | The category or decisions remain unavailable and no release can begin. | `japan_bio_campaign_route_is_open` |
| Japan takes containment, reform, or prisoner-experiment shutdown. | The offensive campaign closes. | Explicit negative route flags |
| The selected state is not an enemy-controlled Chinese core. | The target is invalid and AI weight is zero. | Common state relationship and homeland triggers |
| The selected state lacks a Japanese or Japanese-subject neighboring occupation link. | The target is invalid rather than replaced. | `japan_bio_campaign_state_has_occupation_link` |
| Anthrax is selected for a state without a real military, supply, port, infrastructure, industrial, or division target. | The target is invalid. | Anthrax target profile |
| Plague is selected for a state without a city, port, capital, or population threshold. | The target is invalid. | Plague target profile |
| Political Power, exact payload, Support Equipment, or Command Power is insufficient. | The custom cost blocks the action and the committed effect revalidation prevents a debit. | Agent-specific cost triggers and selected-agent revalidation |
| Anthrax and Plague each pass their route, target, and cost gates. | Both receive the same successful dispatch acceptance; agent identity does not change deployment success. | Both set `bio_seed_result` to `success` before the same dispatcher call |
| Anthrax releases successfully. | The exact selected state receives an Anthrax incubation using the moderate canonical profile. | Agent parameter and shared lifecycle profile |
| Plague releases successfully. | The exact selected state receives a Plague incubation using the serious canonical profile. | Agent parameter and shared lifecycle profile |
| Theater Contamination is active. | Harm remains governed by the shared doctrine-potency pipeline, the campaign cooldown is 60 days, 2 Command Power is refunded, and no evidence or physical consequence is reduced. | Doctrine parameter helper and lifecycle doctrine profile |
| Terminal Hazard is active. | Harm remains governed by the shared terminal-potency pipeline, the campaign cooldown is 45 days, 4 Command Power is refunded, and no evidence or physical consequence is reduced. | Doctrine parameter helper and lifecycle doctrine profile |
| The same state is selected before its 180-day state cooldown expires. | The state is unavailable. | State cooldown trigger |
| The same state becomes eligible after its cooldown. | The AI applies a 0.25 repeat-target factor but the player may still select it. | State history and AI modifier |
| Japan has both high Condemnation and high import vulnerability. | AI willingness is multiplied by 0.30 without removing player authority. | Sanction-vulnerability AI modifier |
| The shared dispatcher rejects a committed seed after the debit. | Costs remain consumed, a diagnostic history flag is recorded, and no release, substitute evidence, alternate state, or refund is fabricated. | Fail-closed dispatch branch |

## AI Balance Evidence

The decision probability inspector recognized both decisions, all AI factors, every referenced constant, and all scripted helper calls without reporting unsupported constructs.

An invalid Anthrax or Plague target produces an exact score of zero.

For a fresh Anthrax logistics target, the exact source arithmetic is 1.50 at baseline, 2.25 with Theater Contamination, and 3.00 with Terminal Hazard.

For a fresh Plague urban target, the exact source arithmetic is 2.1875 at baseline, 3.28125 with Theater Contamination, and 4.375 with Terminal Hazard.

An eligible repeated state applies a further factor of 0.25.

High Condemnation plus high import vulnerability applies a further factor of 0.30.

These are decision-selection scores, not biological delivery-success probabilities.

The refreshed inspector parsed both decisions, their file-local AI Political Power reservation macros, all weighted modifiers, referenced script constants, and helper calls with zero unresolved constructs.

The current inspector artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b84c27d71f3ca9f436f0e251e95c964e9c7f27fac9d774e85005b6c1b878e8e9/329f4d84df798c3a56a515fe478edf716fd9564b7bc931bdd6057947518ffd13/probability-inspect-54acd120d787.json`.

The scenario evaluation artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9f3cc39e68753ef2e9f123a5c5edfd02e86ea69e3f2d5858e052746f635f4f5a/d8cde6e3745e7c90abb50f423d35ee4a29681207114fc38c1b4543ff88e27629/probability-ef79cef83ee02714acaa4c49.json`.

The analyzer cannot independently model several different `FROM` expressions within one declared scope value and does not resolve the script-constant right-hand side of the two sanction-threshold `check_variable` blocks.

Those analyzer limits leave valid-target scores partially symbolic, so the exact arithmetic above was checked directly from the parsed source factors.

No gameplay estimator or approximation was added in response to the analyzer limitation.

## Specialist Audit Resolution

The decision and mission auditor recorded two high findings, one medium finding, and one low presentation finding in `docs/plans/chaos_warfare_system_plans/audits/2026-07-24_japan_china_biological_campaign_decision_audit.md`.

| Finding | Resolution |
| --- | --- |
| Doctrine Command Power refunds were treated as prohibited. | Rejected as a design conflict. Numbered Spec 06 explicitly permits a bounded post-resolution Command Power refund, and the user directed Chaos Warfare doctrine to make CBRN deployment easier while reducing only Condemnation among consequence records. The 2/4 refund remains, payload and Support Equipment remain fully consumed, and both player-facing effect tooltips now disclose the exact refund. |
| A non-Chinese enemy controller could pass the Chinese-core target gate. | Accepted and fixed. The exact selected-state controller must now be CHI, PRC, SHX, GXC, YUN, XSM, or SIK in addition to being at war with Japan and outside Japan's alliance. |
| `ai_hint_pp_cost` script-constant parsing was not proven. | Resolved with a file-local `@` macro, which preprocesses to the fixed 35 or 40 literal required by this engine-only AI reservation field. Actual cost checks and debits remain sourced from shared script constants. |
| Custom costs do not show agent payload text icons. | No suitable agent-payload text icon is registered. The exact payload names and quantities remain explicit rather than introducing a placeholder or cross-type substitute. |

The audit's older requirement-text note is superseded by the current localisation, which lists Political Power alongside payload, Support Equipment, and Command Power.

## Historical Confidence

Japan's Unit 731 program, plague-vector weaponization, and deliberate plague releases in China are well attested.

The Plague action has high historical confidence, including the documented Ningbo release in 1940.

Japanese Anthrax weaponization capability is well attested, while the exact supply-network targeting profile is a medium-confidence gameplay abstraction rather than a claim about one named operation.

The occupation-link gate, target thresholds, costs, cooldowns, and AI weights are gameplay tuning rather than quantitative historical estimates.

The research links and confidence notes are recorded in `docs/systems/cbrn_warfare/biological_warfare/japan_china_biological_campaign.md`.

## Asset Audit

The category sprite `GFX_decision_category_japan_biological_campaign` points to `gfx/interface/decisions/biowarfare/japan_china/decision_category_japan_biological_campaign.dds`.

The final asset is a 52×40 BGRA DDS with real alpha, generated source masters, transparent processing evidence, an exact-size preview, a contact sheet, a manifest, and a production handoff.

The Anthrax and Plague actions reuse their established exact-agent decision sprites.

No placeholder, cross-type resize, or military-raid icon replacement was used.

## Engine Limits

The current state-targeted decision contract supplies the exact state as `FROM`, so the implementation preserves the selected state without an estimator.

The shared lifecycle requires a real current victim controller, so these campaign decisions target Chinese enemy-controlled states adjacent to a real Japanese or Japanese-subject occupation zone rather than Japanese-occupied states.

The implementation does not infer an active combat province, a historical operation state, a current aircraft mission, or an alternate target.

## Remaining Stage 7 Work

The complete surveillance, containment, countermeasure, and treatment package, remaining biological designers, differentiated country AI closure, remaining biological assets and final localisation, cross-route package scenarios, improvement-loop review, and mapped specialist audits remain open.

This validation does not claim Stage 7 or overall goal completion.
