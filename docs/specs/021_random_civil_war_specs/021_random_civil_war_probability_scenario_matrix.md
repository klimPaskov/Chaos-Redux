# Event 021 Probability and Timing Scenario Matrix

The probability auditor must use the live complete candidate pools and the actual HOI4 MCP probability routes. This file defines expected ordering and behavior. It does not claim exact percentages.

## Target selection

| Scenario ID | Candidate A | Candidate B | Expected relationship |
| --- | --- | --- | --- |
| TGT-01 | Stable minor with no organized opposition | Unstable minor with valid opposition | B materially outweighs A |
| TGT-02 | Unstable minor | Stable major after Evolution I | Minor remains favored unless major pressure is extreme |
| TGT-03 | Stable minor | Unstable major after Evolution I | Major becomes a real candidate but does not automatically dominate the whole pool |
| TGT-04 | Recent Event 021 target | Comparable fresh country | Fresh country strongly favored |
| TGT-05 | Player country | Comparable AI country | Similar weight after valid player and AI factors |
| TGT-06 | Country with one complete actor | Country with three complete actors and similar pressure | Multi-actor country moderately favored after Evolution I |
| TGT-07 | Country near active Event 021 war | Comparable distant country during Evolution II | Neighbor favored |
| TGT-08 | Actual nonhuman country | Normal human country | Nonhuman weight is exactly zero |
| TGT-09 | Human Event 006 country after grace | Comparable ordinary human country | Both remain valid |
| TGT-10 | Country inside incompatible bespoke civil war | Comparable valid country | Incompatible country weight is zero |

## Archetype selection

| Scenario ID | Context | Expected dominant routes |
| --- | --- | --- |
| ARC-01 | Strong excluded ideology, no regional package | Ideological uprising |
| ARC-02 | Disputed succession and two legal institutions | Rival legal government |
| ARC-03 | Low command loyalty and several military districts | Broad command schism |
| ARC-04 | Complete Event 006 package, strong regional movement | Event 006 independence actor |
| ARC-05 | Coherent region, no complete package, autonomy movement | Temporary regional secession |
| ARC-06 | One-state country | Same-tag takeover |
| ARC-07 | Several equally strong political blocs after Evolution I | Multi-front mix without one actor type starving the others |
| ARC-08 | Incomplete Event 006 package | Event 006 route weight is zero |

## Severity

| Scenario ID | Context | Expected band |
| --- | --- | --- |
| SEV-01 | High stability, intact command, no war | Limited |
| SEV-02 | Moderate instability and valid opposition | Serious |
| SEV-03 | Low stability, long external war, occupied cores | Severe |
| SEV-04 | Several valid actors and very low authority after Evolution I | Critical multi-front possible |
| SEV-05 | Stable one-state country | Limited same-tag takeover |
| SEV-06 | Major with extreme pressure | Severe or Critical, not automatic destruction |

## Evolution timing

| Scenario ID | Context | Expected timing direction |
| --- | --- | --- |
| EVO1-01 | Large stalemated war, low State Authority, extra valid actor | Faster Evolution I |
| EVO1-02 | One side near defeat, no extra region | Slow or unresolved Evolution I |
| EVO2-01 | Long border, sponsor routes, surviving independence side | Faster Evolution II |
| EVO2-02 | Early settlement and strong neighbors | Slow or no active spread before war ends |
| EVO3-01 | Evolution III available and a live severe Event 021 war | Normal shared MTTH activation |
| EVO3-02 | Evolution III already active before first Event 021 firing | Prefire global rules with no duplicate evolution record |

## Front count

| Scenario ID | Context | Expected result |
| --- | --- | --- |
| FRT-01 | Small country with one coherent region | Two total belligerents |
| FRT-02 | Medium country with two valid opposition regions | Three total belligerents after Evolution I |
| FRT-03 | Major with four valid actors and capacity | Three to five total belligerents within cap |
| FRT-04 | Large map but only one valid leader | No fake additional actor |
| FRT-05 | Two Event 006 packages with overlapping anchors | One valid package or another archetype, no state collision |

## Sponsor AI

| Scenario ID | Sponsor state | Expected behavior |
| --- | --- | --- |
| SPN-01 | Rich neutral major, one aligned viable side | Moderate support |
| SPN-02 | Sponsor in desperate war with low equipment | Little or no support |
| SPN-03 | Two rival sponsors and two viable sides | Competitive support within commitment caps |
| SPN-04 | Side has no administration or survival path | Recognition and large aid suppressed |
| SPN-05 | Neutral mediator profile | Military support suppressed, mediation favored |

## Strange incidents

| Scenario ID | Context | Expected behavior |
| --- | --- | --- |
| STR-01 | New baseline side at Rising Chaos | Very low chance |
| STR-02 | Long-lived side, low authority, high chaos | Higher but still bounded chance |
| STR-03 | Side already has active incident | New incident chance zero |
| STR-04 | Incident cooldown active | New incident chance zero |
| STR-05 | Evolution disabled | Incident chance zero |

## Settlement AI

| Scenario ID | Context | Expected behavior |
| --- | --- | --- |
| SET-01 | Government dominant and high authority | Military or firm negotiated settlement |
| SET-02 | Independence actor controls homeland and has recognition | Independence or autonomy favored |
| SET-03 | Several equal fronts and exhausted country | Coalition, partition, or separate peace favored |
| SET-04 | Hardliner government with low legitimacy | Repression possible, with recurrence cost |
| SET-05 | Negotiator government and enforceable guarantees | Durable agreement favored |
| SET-06 | Settlement would leave side with no viable state | Invalid |

## Recurrence

| Scenario ID | Context | Expected relationship |
| --- | --- | --- |
| REC-01 | Negotiated settlement, completed disarmament, high authority | Very low recurrence |
| REC-02 | Harsh settlement, surviving underground networks, low authority | High recurrence after cooldown |
| REC-03 | Recent victory inside successor grace | Recurrence weight zero |
| REC-04 | Resolved partition with maintained armistice | Low to moderate, based on violations |
| REC-05 | Broken autonomy guarantee | Strong increase |
| REC-06 | Actual nonhuman successor | Event 021 recurrence zero |

## Global queue

| Scenario ID | Country | Expected order |
| --- | --- | --- |
| GLB-01 | Critical country with valid major crisis | Early queue |
| GLB-02 | Fractured country with no valid actor | Cannot enter launch queue |
| GLB-03 | Stable country | Long review, no launch |
| GLB-04 | Critical country blocked by theater cap | Remains visibly Critical and launches after capacity |
| GLB-05 | Annexed queued country | Removed |
| GLB-06 | Human Event 006 country after grace | Valid |
| GLB-07 | Actual nonhuman country | Excluded |

## Cluster

| Scenario ID | Chaos and state | Expected behavior |
| --- | --- | --- |
| CLU-01 | Calm World, enough countries | Events 004, 007, and 021 use different targets |
| CLU-02 | Rising Chaos, high-pressure external-war target | Intentional Event 004 and 021 overlap possible |
| CLU-03 | New Fury actor | Same-transaction Event 021 target normally blocked |
| CLU-04 | Event 006 tag reserved by another member | Event 021 package rerolls or skips |
| CLU-05 | No valid Event 021 target | Event 021 skipped with reason, cluster can continue |

## Scenario intensity

| Scenario ID | Type and intensity | Expected coverage |
| --- | --- | --- |
| SCN-01 | Political Fracture Low | About 10 percent, mostly minors, one opponent |
| SCN-02 | Independence Cascade Medium | About 25 percent, regular Event 006 use |
| SCN-03 | Command Collapse High | About 50 percent, majors and multi-front command wars |
| SCN-04 | Universal Fragmentation Maximum | Every eligible normal human country committed |
| SCN-05 | Any type, actual nonhuman country | Excluded |
| SCN-06 | Any type, one-state human country | Same-tag takeover |
| SCN-07 | Maximum measured stall | Same locked plans finish in deterministic batches within seven game days |

## Required evidence labels

The probability audit should label results as:

- exact
- bounded
- sampled
- score-only
- unresolved

The auditor should not report exact automatic event probability unless every competing event, weight, cap, cooldown, and external factor is included.
