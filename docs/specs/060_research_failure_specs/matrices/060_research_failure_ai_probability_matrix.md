# Research Failure AI and probability scenario matrix

## Audit contract

Every weighted surface in this file requires a read-only baseline audit through `chaosx_ai_probability_auditor` before balance changes and a comparison audit after the owner applies changes.
The auditor begins with `hoi4.probability_inspect` and names the exact surface, candidate pool, external factors, and scenario ID.

Expected results below are ordering requirements unless the full candidate pool makes an exact probability meaningful.
The auditor must label each result as exact, bounded, sampled, score-only, or unresolved.

## Target selection scenarios

| Scenario ID | Candidate state | Expected ordering or invariant | Starvation or dominance check |
| --- | --- | --- | --- |
| `TGT-01` | One valid player nonmajor and several valid AI majors | All remain eligible, player receives no punitive hidden multiplier | Player must not dominate solely through human control |
| `TGT-02` | Player country is also a major | Country appears once | No duplicate major plus player weight |
| `TGT-03` | One country has active unresolved Research Failure | Active country weight is zero | No repeat hit while unresolved |
| `TGT-04` | One country is inside post-reconstruction immunity | Immune country weight is zero | Immunity persists after reload |
| `TGT-05` | Two-slot player country and five-slot AI major | Both valid, major normally ranks higher when all else is equal | Small player cannot be permanently starved from a repeatable event |
| `TGT-06` | Advanced major and shallow-tech major | Advanced major ranks higher because safe rollback is broader | Shallow target still possible when it is the only valid major |
| `TGT-07` | Country with large residual lost ledger and fully recovered country | Recovered country ranks higher | Residual deficit lowers but does not create permanent zero after immunity |
| `TGT-08` | Naval major and landlocked major with equal general strength | Neither dominates without profile evidence | Domain selection adapts after target selection |
| `TGT-09` | Valid normal country and special nonhuman player actor without owner policy | Normal country valid, special actor weight zero | Player control does not bypass owner safety |
| `TGT-10` | Valid Kruger host with standard research adapter | Kruger host remains eligible | Shared special-country classifier must not suppress valid owner override |
| `TGT-11` | No country meets safe rollback minimum | Event is unavailable | No partial or fake target |
| `TGT-12` | Country is near full annexation with no exile route | Weight strongly reduced or zero by validity | Event should not waste a firing on immediate cleanup |

## Opening response scenarios

| Scenario ID | Country state | Expected option order | Required rejection behavior |
| --- | --- | --- | --- |
| `OPT-01` | Democratic faction member, high stability, trusted research partners | Open emergency first, Academy-compatible follow-up strong | Sealed route remains possible but lower |
| `OPT-02` | Authoritarian country at war with high enemy intelligence | Seal institutions first | Open route not zero when vital ally support exists |
| `OPT-03` | Isolated authoritarian country with archive catastrophe | Central or sealed behavior strong, but extreme archive need raises controlled foreign channel | Secrecy must not dominate despite making recovery impossible |
| `OPT-04` | Peaceful high-capacity civilian state after institutional purge | Open emergency and later Independent Academy favored | Central route should not dominate by ideology alone |
| `OPT-05` | Valid Directorate, six slots at risk, existential war | Kruger mandate first | Owner political threshold can still veto |
| `OPT-06` | Valid Directorate, low authority, stable peace, strong civilian base | Normal open or Academy path first | Kruger option remains visible but low |
| `OPT-07` | Directorate already heavily entrenched from prior bargains | Further mandate requires stronger desperation | No repeated automatic acceptance |
| `OPT-08` | No valid Directorate adapter | Kruger option absent or weight zero | No raw unavailable option for AI |

## Institutional route scenarios

| Scenario ID | Country state | Expected route order | Balance check |
| --- | --- | --- | --- |
| `RTE-01` | Stable allied democracy with research-sharing network | International Consortium first, Academy second | Consortium dependence must have material cost |
| `RTE-02` | Authoritarian industrial major in existential war | Central Authority first | Academy remains possible after war state changes |
| `RTE-03` | Peaceful state recovering from purge with strong civilian industry | Independent Academy first | Slow early reward must not make route globally inferior |
| `RTE-04` | Weak small country with trusted major ally and few civilian factories | International Consortium first | Foreign aid does not grant full recovery for free |
| `RTE-05` | Weak isolated small country | Central or Academy based on war and stability | No route becomes impossible through fixed major-power costs |
| `RTE-06` | Kruger mandate active | Directorate route first or owner-approved limitation route | Ordinary routes cannot clear Event 16 authority silently |
| `RTE-07` | Consortium partner dies or leaves faction before selection | Recalculate and hide invalid route if no replacement | AI cannot choose dead partner route |
| `RTE-08` | Country shifts from war to peace before route choice | Weights update | Initial opening response does not permanently lock all normal routes |

## Emergency action scenarios

| Scenario ID | Main problem | Expected top action | Secondary action | Invalid action behavior |
| --- | --- | --- | --- | --- |
| `ACT-01` | Physical destruction, high occupation risk | Secure laboratories | Mobile laboratories or records recovery | Foreign archive help does not replace site security |
| `ACT-02` | Archive catastrophe, stable territory | Recover records | Standards or foreign archive channel | Security action lower unless actual threat exists |
| `ACT-03` | Specialist dispersal and friendly host | Protect and recall specialists | Foreign archive or education project | Coercive action low when it damages net recovery |
| `ACT-04` | Verification collapse and active industrial penalties | Emergency standards | Archive verification | Rushed archive action reduced |
| `ACT-05` | Knowledge Collapse with one slot | Preserve last research core | Stabilization mission support | Expensive secondary projects delayed |
| `ACT-06` | Severe war and equipment shortage | Security and one military-relevant domain | First slot project when affordable | AI keeps minimum war production |
| `ACT-07` | Peace and large civilian economy | Archive, education, and slot projects | Long resilience investments | AI should not leave projects idle |
| `ACT-08` | No convoys and overseas partner | Domestic action first | Foreign action waits or selects land route | AI cannot click unaffordable aid route |

## Lost-domain research priority scenarios

| Scenario ID | Lost domains and country profile | Expected primary priority | Expected secondary priority |
| --- | --- | --- | --- |
| `RES-01` | Industry, electronics, infantry lost, broad army | Industry or electronics | Infantry equipment |
| `RES-02` | Armour generations lost, active tank production, war | Armour after minimum industry prerequisites | Electronics or industry |
| `RES-03` | Naval hulls lost, large fleet and dockyards | Naval | Industry or electronics |
| `RES-04` | Naval losses in landlocked country with no fleet | Industry or land domain | Naval low or zero until maritime strategy changes |
| `RES-05` | Airframes lost, large air force and production | Air | Electronics or industry |
| `RES-06` | Radar and encryption lost under bombing and intel pressure | Electronics or radar | Industry |
| `RES-07` | Many new unlost ahead-of-time technologies available | Lost prerequisites remain preferred | Ahead-of-time weight reduced |
| `RES-08` | Lost domain fully recovered | Priority removed or reassigned | No stale weight |
| `RES-09` | Owner-protected special technology missing from normal pool | Never selected by generic research strategy | Owner route handles it |

## Foreign actor selection scenarios

| Scenario ID | Diplomatic state | Expected partner | Expected rival | Invariant |
| --- | --- | --- | --- | --- |
| `FOR-01` | Faction with one research-sharing leader | Leader or strongest valid research partner | Actual hostile intel actor | One country can fill both roles only with clear separate logic |
| `FOR-02` | No allies, one neutral technical power | Neutral offer possible | Rival from hostile relations | Event remains playable without ally |
| `FOR-03` | Specialist diaspora hosted by friend | Host selected for return or joint institute | Different rival preferred | Cohort cannot be offered twice |
| `FOR-04` | Specialist diaspora hosted by rival | Rival can retain or exploit cohort | Same actor may fill host and rival with one combined event | No duplicate reward |
| `FOR-05` | Potential partner has active Research Failure | Lower aid weight or invalid for major commitment | Another partner preferred | Damaged partner cannot provide impossible records |
| `FOR-06` | Black Market member with no public ally | Covert intermediary possible | Membership remains hidden from outsiders | No public organization reveal |
| `FOR-07` | Multiplayer foreign player selected | Real timed choice | AI fallback after timeout | Target cannot be blocked indefinitely |

## Secondary incident scenarios

| Scenario ID | State | Expected incident ordering | Starvation check |
| --- | --- | --- | --- |
| `INC-01` | Failed stabilization and low security | Second laboratory loss high | Other incidents remain possible after security improves |
| `INC-02` | Rushed archive and weak standards | False archive high | Deterministic stored outcome avoids reload reroll |
| `INC-03` | Large diaspora and rich foreign host | Foreign appointments high | Same cohort fires once |
| `INC-04` | Sealed response and recent Intel Leaked | Concealment exposed high | Exposure not guaranteed without proof path |
| `INC-05` | Long maximum spending and low stability | Reconstruction fatigue high | It does not fire repeatedly without cooldown |
| `INC-06` | Legacy tank production family active | Prototype without a method can select armour | Family selection follows real live consumer |
| `INC-07` | No eligible live consumer | Prototype incident weight zero | No fake family event |

## Active-evolution timing scenarios

| Scenario ID | Incident state | Expected timing direction | Invariant |
| --- | --- | --- | --- |
| `EVO-01` | Baseline incident, Chaos below 200 | Lost Archives unavailable | No pending job applies later after invalid setup |
| `EVO-02` | Chaos 200+, failed stabilization, low Archive Recovery | Lost Archives faster than base | Still MTTH-based unless accepted instant condition exists |
| `EVO-03` | Chaos 200+, strong recovery and secured archives | Lost Archives slower | Cannot become permanently impossible while incident remains deeply damaged unless design says so |
| `EVO-04` | Evolution disabled | Weight zero and no recorded state | No gated content unlock |
| `EVO-05` | Lost Archives active, Chaos 400+, war and false archive | Scientific Dark Age faster | Applies only additional severity |
| `EVO-06` | Scientific Dark Age active, Chaos 600+, Capacity near zero | Knowledge Collapse faster | Slot reconciliation occurs once |
| `EVO-07` | Capacity above 90 and slots almost restored | Higher evolution strongly suppressed or invalid | Recovery cannot be erased arbitrarily at completion line |
| `EVO-08` | Pre-fire event at high Chaos with enabled evolution | Opening begins at highest valid severity | Lower severity damage not applied as separate duplicate transactions |

## Probability tool routing

| Evidence need | Preferred tool |
| --- | --- |
| Map candidates, factors, external dependencies | `hoi4.probability_inspect` |
| Compare option or decision scores under one scenario | `hoi4.probability_evaluate` |
| Check thresholds across stability, war, slots, or Capacity ranges | `hoi4.probability_sweep` |
| Check random target and incident frequency with a complete pool | `hoi4.probability_simulate` |
| Check evolution timing with scheduled state changes | `hoi4.probability_evaluate` or timing render, and sequence only when the full cadence contract exists |
| Compare pre-patch and post-patch behavior | `hoi4.probability_compare` |
| Present timing, matrix, sensitivity, or unresolved evidence | `hoi4.probability_render` |

## Acceptance conditions

- No country, option, route, or action dominates every plausible scenario without a design reason.
- Invalid targets and dead partners have zero weight.
- Human control does not create duplicate target weight.
- AI can recover without free hidden effects.
- AI retains enough economy and equipment to survive while rebuilding.
- Technology priority follows actual production and war needs.
- Every patched weighted surface has baseline and comparison evidence under the same scenario IDs.
