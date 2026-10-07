# Validation matrix and evidence status

## Evidence classes

DESIGN: parent-reviewed written rule.
MODEL: a small Python reference model of that rule.
SOURCE: directly read project or repository content.
MCP: actual HOI4 service validation.
RUNTIME: user-run game or save evidence.
ASSET: produced and inspected final consumer assets.

Only DESIGN, selected MODEL checks, and the explicitly listed SOURCE reads are available in this package. No MCP, RUNTIME, or ASSET result is claimed.

## Acceptance fixtures

| ID | Fixture | Required result | Evidence still required beyond design/model |
| --- | --- | --- | --- |
| V01 | Three-country directed grant | Six pairs, no self-pairs, independent values | Native SOURCE, MCP, RUNTIME |
| V02 | Existing asymmetric networks | Equal increments, unequal final totals preserved | Native readback |
| V03 | Native cap at 95 and 100 | Actual gains 5 and 0 on normalized scale | Units and cap proof |
| V04 | Replay versus new firing identity | Replay pays zero, later legitimate firing pays once | Save/load and MP evidence |
| V05 | Democracy, subject, no-agency country | Native grant works without political exemption | DLC and ideology matrix |
| V06 | Country appears after snapshot | No retroactive layers | Live country creation |
| V07 | Grant tier/toggle combinations | 10/20/25 according to actual capabilities | Shared evolution source and tools |
| V08 | I disabled and III enabled | Baseline grant plus III, no leaked I/II benefits | Shared settings integration |
| V09 | C45/50/60 early capture | No offer, F70, F80 | Native pre-capitulation compliance |
| V10 | Current compliance already above F | No reduction, offer still spent | Native state readback |
| V11 | Recapture after compliance loss | No old-floor restoration | Control lifecycle and receipts |
| V12 | Network raises F70 to F80 after recapture | Only new difference 10, not reset to 80 | Native receipt persistence |
| V13 | Ally transfer, own core, colony, competing cores | Correct exclusions and target identity | Verified ownership callbacks |
| V14 | Native post-capitulation conversion stronger than offer | Preserve native result | Native conversion timing |
| V15 | Proximity immediately below/at 75% | Only qualified threshold passes | Actual T and P availability |
| V16 | Second stage before/after five days | Never immediate, live recheck after separation | Native date encoding |
| V17 | Recovery, peace, sponsor removal | No stale award | Save/load and lifecycle |
| V18 | Several qualifying sponsors | Same incident snapshot, no faction-wide copy | Deterministic MP behavior |
| V19 | Native government with real state set | Native subject, no stolen territory | Actual government route |
| V20 | Democratic government creation | Narrow exception, unrelated rules preserved | Rule isolation and DLC evidence |
| V21 | Postponed offer after state restoration | Invalidated without creation | Current ownership revalidation |
| V22 | Rival governments and occupied fragments | Native legal identities and disjoint bundles only | Native duplicate rules |
| V23 | Event 095 restoration | Claimant can return, old queued effects close | Accepted 095 contract |
| V24 | Event 093 treaty roles | Separate sponsor networks and government credit | Accepted treaty contract |
| V25 | Manifestation Chaos breadth | One +5 or +10, target deduplication | Shared Chaos/log integration |
| V26 | Capitulation and government overlap | No duplicate native consequence accounting | Current shared source trace |
| V27 | AI score examples | Correct preference after legality | Native choice surface and probability tools |
| V28 | Achievement continuous state/government cohorts | True continuity, reset, no substitution | Observable native changes |
| V29 | Achievement war-entry snapshots | Original values, no retrospective guessing | Save fixtures and history |
| V30 | Achievement optional dependencies | Broken/unimplemented route not advertised as live | Shared eligibility UI |
| V31 | All five report images and dynamic localization | Processed, wired, readable, correct actors | ASSET and user UI evidence |
| V32 | Six achievement triplets | Eighteen valid 64x64 states with real consumers | Processor audit and native display |
| V33 | Large country count and coalition war | Bounded workload, no permanent all-pairs poll | Source complexity and user timing evidence |
| V34 | Open report during save/load | Effects not repeated | Saved native state comparison |
| V35 | Interrupted Fifth Column delay | Correct time remaining and generation | Saved pending-state inspection |
| V36 | Native capability unavailable | Explicit blocked status, no generic fallback | Evidence-backed decision record |

## User-run game plan

Use the debug-playtest and save-inspection skills and obtain the user's live evidence rather than launching the game automatically. Record installed version, active DLCs, mod revision, starting countries, event settings, exact stimulus, observed result, and relevant error log lines.

Build paired saves immediately before and after a minimal global grant, an early handover, a Fifth Column breakthrough, and a native government creation. Add reload copies for the same cases. Inspect the actual saved collaboration, compliance, identities, and receipts through the supported tools.

Use small deterministic country fixtures first. Then test a normal campaign and a large-country-count save. Do not substitute a large uncontrolled playthrough for proving the small directional cases.

## Stop conditions

A mismatched sponsor/target, unsupported native route, missing country identity, unwired achievement state, fabricated callback, repeated grant, unproven democratic exception, or unreviewed mandatory agent finding prevents implementation completion. A clean custom Python model does not override any of those failures.
