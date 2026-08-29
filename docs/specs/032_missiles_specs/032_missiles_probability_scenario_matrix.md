# Event 32 probability scenario matrix

## Use

This matrix defines the named scenarios that the implementation and `chaosx_ai_probability_auditor` must use.

The implementation may add scenarios. It may not remove a scenario without recording why the surface no longer exists.

## Site selection scenarios

| ID | Surface | Setup | Expected ordering | Forbidden result |
| --- | --- | --- | --- | --- |
| `SITE-01` | First site | Interior core with infrastructure and AA, exposed capital, occupied industrial state | Interior core first, capital second, occupied state zero | Occupied state selected |
| `SITE-02` | First site | One-state minor with one valid state | Sole state selected with certainty | Deferred result |
| `SITE-03` | First site | Connected core, isolated empty island, noncore occupied port | Connected core dominates | Empty island dominates |
| `SITE-04` | Existing upgrade | One active site below cap, two valid new states | Existing site upgrade dominates | New site created without redundancy need |
| `SITE-05` | Secondary site | Primary site and two candidates, one in same strategic region and one protected in another | Protected different-region state first | Frontline same-region state first |
| `SITE-06` | Capture | One compromised captured site and one secure owned site | Secure site used for launch | Compromised site treated as ordinary |

## Target-country scenarios

| ID | Surface | Setup | Expected ordering | Forbidden result |
| --- | --- | --- | --- | --- |
| `TGT-C-01` | Conventional war | Frontline enemy major, distant enemy minor, ally | Frontline enemy major first, distant enemy second, ally zero | Ally receives weight |
| `TGT-C-02` | Retaliation | Confirmed attacker, probable third party, unrelated neutral | Confirmed attacker dominates | Neutral dominates |
| `TGT-C-03` | Uncertain attribution | Two plausible enemies with different evidence | Higher evidence first, verification remains attractive | Random unrelated target |
| `TGT-C-04` | Counterforce | Enemy with launch sites, enemy without program | Missile power first when counterforce selected | Nonprogram target dominates |
| `TGT-C-05` | Reserve floor | Two valid enemies, reserve barely above doctrine floor | No launch or precision only | Saturation launch |

## Target-state scenarios

| ID | Surface | Setup | Expected ordering | Forbidden result |
| --- | --- | --- | --- | --- |
| `TGT-S-01` | Logistics | Supply hub, high railway state, empty state | Supply hub first, railway second, empty zero | Empty state selected |
| `TGT-S-02` | Industry | Dense factory state, small factory state, no-industry state | Dense first | No-industry state dominates |
| `TGT-S-03` | Air suppression | Airfield and radar state, coastal port, inland empty | Airfield and radar first | Inland empty selected |
| `TGT-S-04` | Counterforce | High-capacity launch state, damaged low-capacity site, ordinary factory state | High-capacity site first | Factory state dominates |
| `TGT-S-05` | Collateral restraint | Equal military value, one dense capital and one lower-population industrial state | Lower-population state preferred by restrained profile | Capital always selected |
| `TGT-S-06` | Guidance risk | High-value target next to neutrals, slightly lower value isolated target | Isolated target gains weight under poor guidance | Neutral-adjacent target dominates without urgency |

## Strike-profile scenarios

| ID | Setup | Expected result |
| --- | --- | --- |
| `STRIKE-01` | Low reserve, one supply hub, high readiness | Precision dominates |
| `STRIKE-02` | Moderate reserve, several factories, operational readiness | Strategic barrage dominates |
| `STRIKE-03` | Large reserve, dense defended industry, Saturation active | Saturation dominates but precision remains nonzero |
| `STRIKE-04` | Low readiness and damaged site | Maintenance or no launch dominates |
| `STRIKE-05` | Exposed enemy launch state after enemy first use | Counterforce dominates |
| `STRIKE-06` | Empty low-value target | No launch |
| `STRIKE-07` | Target capital, restrained profile, no urgent threat | Noncapital target or no launch |
| `STRIKE-08` | Target capital threatening immediate defeat | Command strike may become viable |

## Payload scenarios

| ID | Setup | Expected result | Forbidden result |
| --- | --- | --- | --- |
| `PAY-01` | No payload stockpile | Conventional only | Special payload selected |
| `PAY-02` | Chemical stockpile, military target, enemy first use | Chemical gains strong weight | Nuclear without stockpile |
| `PAY-03` | Nuclear stockpile, no enemy first use, high condemnation | Conventional dominates | Nuclear dominant |
| `PAY-04` | Nuclear stockpile, verified nuclear first use, imminent defeat | Nuclear becomes viable | Payload blocked without reason |
| `PAY-05` | Thermonuclear stockpile, uncertain attribution | Verify or conventional response | Automatic thermonuclear launch |
| `PAY-06` | Biological stockpile, poor guidance, neutral adjacency | No biological launch | Biological launch dominates |
| `PAY-07` | Rogue site physically holds chemical payload | Rogue chemical option viable | Payload from another site invented |

## Unreliable Guidance scenarios

| ID | Technology | Readiness | Site | Range | Barrage | Expected |
| --- | --- | --- | --- | --- | --- | --- |
| `GUIDE-01` | Mature | `90` | Secure | Short | Precision | High on-target rate, severe accident very low |
| `GUIDE-02` | Early | `45` | Damaged | Long | Strategic | Meaningful degraded and failure rate |
| `GUIDE-03` | Mature | `70` | Secure | Medium | Saturation | At least one failure becomes plausible |
| `GUIDE-04` | Early | `25` | Compromised | Long | Saturation | Launch should often be blocked or highly dangerous |
| `GUIDE-05` | Mature | `80` | Secure | Medium | Special payload | Slightly worse than conventional |
| `GUIDE-06` | Mature | `80` | Secure | Medium | Precision after maintenance | Better than identical case without maintenance |
| `GUIDE-07` | Any | any | any | any | any | Neutral and self-strike remain minority failure outcomes |

## Rogue Launch Commands scenarios

| ID | Setup | Expected |
| --- | --- | --- |
| `ROGUE-01` | Stability high, control `90`, one secure site, small reserve | Incident likelihood very low |
| `ROGUE-02` | Civil war, control `25`, two contested sites | Incident likelihood high |
| `ROGUE-03` | Captured site, special payload, low security | Severe custody incident favored |
| `ROGUE-04` | Foreign intelligence access, stable state, code compromise | Bribery or forged-order incident viable |
| `ROGUE-05` | No foreign actor | Foreign-bribery incident zero |
| `ROGUE-06` | No reserve | Unauthorized launch incident zero |
| `ROGUE-07` | Recent code rotation | Incident pressure materially lower |
| `ROGUE-08` | One active crisis already | Second ordinary crisis blocked |

## Retaliation posture scenarios

| ID | Setup | Expected |
| --- | --- | --- |
| `POSTURE-01` | Restrained profile, control `90`, low threat | Supervised favored |
| `POSTURE-02` | High threat, control `90`, several hardened sites | Delegated or Automatic viable |
| `POSTURE-03` | Control `30` | Automatic zero |
| `POSTURE-04` | One vulnerable site, decapitation threat | Delegated may beat Supervised |
| `POSTURE-05` | Recent false warning | Stronger automation weight reduced |
| `POSTURE-06` | Recent verified special-payload attack | Stronger posture weight increased |

## Warning-response scenarios

| ID | Setup | Expected | Forbidden result |
| --- | --- | --- | --- |
| `WARN-01` | Confirmed attacker, high severity, reserve available | Retaliation or deliberate stand-down according to profile | Unrelated target |
| `WARN-02` | Uncertain actor, seven-day window, good intelligence | Verify first | Immediate automatic launch under Supervised |
| `WARN-03` | Conflicting signals, poor control | Sever or isolate gains weight | Full launch dominates |
| `WARN-04` | False signal proven | Stand-down | Launch |
| `WARN-05` | Network compromised at one site | Isolate site favored | All sites trusted |
| `WARN-06` | Root already processed by country | No second response | Duplicate retaliation |
| `WARN-07` | Generation cap reached | Chain stops | New linked response |
| `WARN-08` | No surviving site | No launch | Virtual launch without site |

## Evolution MTTH scenarios

| ID | Track | Setup | Expected |
| --- | --- | --- | --- |
| `EVO-01` | Rogue | Gathering Storm, widespread instability | Shorter than base |
| `EVO-02` | Rogue | Stable world, one secure program | Longer than base |
| `EVO-03` | Unreliable | Many launches and low readiness | Shorter than base |
| `EVO-04` | Unreliable | Few launches and high readiness | Longer than base |
| `EVO-05` | Saturation | Chaos Tier, many mature programs | Near target MTTH |
| `EVO-06` | Saturation | Few early programs | Longer or ineligible |
| `EVO-07` | Special Warheads | No payload owner | Ineligible |
| `EVO-08` | Special Warheads | Several payload owners | Eligible |
| `EVO-09` | Automatic | Below `900` chaos | Ineligible |
| `EVO-10` | Automatic | At least `900` chaos, no active world end, hostile missile pair | Eligible |
| `EVO-11` | Any | Evolution disabled | Zero chance and no record |
| `EVO-12` | Any | Already recorded | Zero chance |

## SCN-015 setup scenarios

| ID | Profile | Intensity | Required proof |
| --- | --- | --- | --- |
| `SCN15-01` | Global Proliferation | Low | Limited program coverage, no forced incident |
| `SCN15-02` | Global Proliferation | Maximum | Every valid recipient, bounded reserve |
| `SCN15-03` | Saturation War | High | Existing safe war and belligerent saturation setup |
| `SCN15-04` | Saturation War | Any | Preflight fails cleanly when no safe conflict exists |
| `SCN15-05` | Command Breakdown | Maximum | Active-incident cap respected |
| `SCN15-06` | Special Payload Crisis | Any | Unavailable without supported payload owner |
| `SCN15-07` | Retaliation Network | Low | No immediate destructive incident |
| `SCN15-08` | Retaliation Network | Maximum | One bounded warning chain, no terminal flag |
| `SCN15-09` | Any | Any | Repeat launch blocked or idempotent |
| `SCN15-10` | Any | Any | Preflight failure leaves no partial program mutation |

## Comparison requirement

Any patch to a weighted value must be followed by `hoi4.probability_compare` using the same scenario IDs that established the baseline.

The final audit should include:

- source revision before
- source revision after
- scenario hash
- candidate pool completeness
- expected ordering
- baseline result
- final result
- unresolved limitation
