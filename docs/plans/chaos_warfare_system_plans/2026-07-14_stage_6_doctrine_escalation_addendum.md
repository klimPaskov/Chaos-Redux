# Stage 6 doctrine escalation addendum

Status: implemented; package-wide goal remains in progress

## Accepted user direction

Chaos Warfare is an escalation doctrine. Its offensive postures make supplied CBRN operations faster to prepare, more potent, more contaminating, more lethal, and more attractive to an already eligible aggressive AI route. Doctrine may reduce Condemnation impact. It may not reduce payload debit, protection requirements, evidence, attribution, recorded deaths, contamination history, medical history, resistance trauma, domestic penalties, confirmed-use history, or public-harm floors.

Terminal Hazard may improve killing efficiency at an independently existing camp network. This is a conditional effect inside the camp system's own death calculation, not a doctrine-owned camp route.

## Source conflicts and resolution

- Numbered specification 02 describes Terminal Hazard as increasing Condemnation, while the user's explicit design decision requires reduced political consequences. The implemented 0.80 multiplier applies before the existing confirmed strategic and mass-casualty public-harm floors. The conflict is recorded without removing any consequence surface.
- Numbered specifications 02 and 08 and the coding prompt keep camps, extermination buildings, experiment sites, and occupation-law ownership outside doctrine. The user's camp-efficiency direction is implemented only as a 1.25 multiplier on an existing active camp network when its stored responsible country has Terminal Hazard and still authorizes Unrestricted Chaos Warfare. Doctrine does not create, unlock, select, or authorize the site.
- No estimator, proxy, fallback, free payload, passive air contamination, or broad periodic pulse is introduced.

## Central tuning

| Posture | Prepared effect | Contamination | Duration | Deaths | Medical saturation | Offensive HQ preparation | Condemnation | Existing camp deaths |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Theater Contamination | 1.10 | 1.15 | 1.10 | dose-derived | dose-derived | 0.90 | unchanged beyond the institution ladder | unchanged |
| Terminal Hazard | 1.15 | 1.25 | 1.15 | 1.25 after dose | 1.20 after dose | 0.80 | 0.80 before public floors | 1.25 while Unrestricted policy remains active |

All values live in `common/script_constants/cbrn_doctrine_constants.txt`. The shared chemical calculation owns the operational multipliers. The Headquarters helper is called only by Prepare Chemical Offensive and Combined CBRN Overmatch. The camp multiplier is applied after the camp system resolves its normal additive inputs and before its existing 3.50 cap.

## AI boundary

Theater first-use and Terminal unrestricted-use weights remain additive to zero-base, route-gated policy decisions. Offensive Headquarters posture weights apply only after the full player-equivalent activation trigger has already passed. No AI receives payload, readiness, policy, equipment, command-power, or target-selection exemptions.

## Acceptance checks

- Every chemical delivery route still enters one shared exposure pipeline.
- Theater and Terminal posture effects are mutually exclusive and centrally tuned.
- Only Condemnation receives a political mitigation multiplier; confirmed public-harm floors remain downstream.
- Camp killing efficiency requires a real active camp, a stored responsible country, Terminal Hazard, and current Unrestricted policy.
- Doctrine never creates or unlocks camp infrastructure.
- Protective, decontamination, medical, and containment Headquarters preparations are not accelerated by the offensive posture helper.
