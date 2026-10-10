# Event 008: Cluster and Achievement Matrix

Disposition: unresolved design acceptance, with catalog facts and implementation evidence separated below.
The [current source map](../../../plans/008_tensions_rising_plans/documentation_state_2026-10-05.md) and [release audit](../../../plans/008_tensions_rising_plans/subagent_handoffs/event_completion_audit_2026-10-05.md) govern current evidence and limits.

## Cluster record

The cluster record is unresolved; two sources disagree and neither has a recorded acceptance basis.

| Field | Current source | Workbook catalog |
| --- | --- | --- |
| ID and name | 3, `Diplomatic Panic` (`event_cluster_constants.txt`) | 3, `Diplomacy` |
| Type and status | repeatable, unlock tier 0, 120-day cooldown | repeatable, `Partially Available` |
| Members | Event 8 required, Event 17 Random Faction optional | Events 8, 17, 36, 59 |
| Severities | Low, Low | Medium, Medium, High, High |

The earlier overview's four-member runtime claim is not verified by the source branch in `chaosx_event_cluster_effects.txt`, and the single-member Low note from planning is superseded by both records.
The cluster owner must pick the authoritative definition and supply its acceptance basis; a severity proposal is in the README's open questions.
This documentation changes no member wiring, severity, cooldown, unlock, or cluster design.

## Achievement matrix

The following conditions are retained source-design requirements with unresolved expanded-design acceptance.
All five definitions, tracking hooks, localisation, and icon triplets exist in source, but the release audit does not establish full condition fidelity.
These entries do not claim observed unlocks or final artwork acceptance.

### `achievement_tensions_thin_wire`

**Title:** The Thin Wire  
**Visibility:** visible  
**Difficulty:** hard  
**Eligible player:** any country  
**Unlock:** After Event 8 has reached Stage III or IV, remain at peace for 180 days while global world tension is `100%`.  
**Disqualifier:** player enters any war during the 180-day window.  
**Why it is interesting:** rewards restraint in a world designed to panic.  
**Icon direction:** a taut telegraph wire over a dark diplomatic map, no text.

### `achievement_tensions_only_headlines`

**Title:** Only Headlines  
**Visibility:** hidden  
**Difficulty:** very hard  
**Eligible player:** any country  
**Unlock:** See three Stage II+ Event 8 firings while there are no active wars globally.  
**Disqualifier:** any active war begins before the third qualifying firing.  
**Why it is interesting:** rare campaign-state achievement, tension without war is hard to maintain.  
**Icon direction:** stacked newspapers under a silent clock, no readable text.

### `achievement_tensions_insurance_market`

**Title:** The Insurance Market Knows  
**Visibility:** visible  
**Difficulty:** medium  
**Eligible player:** any country with a convoy pool or trade/naval relevance.  
**Unlock:** Trigger the `Insurance Rates Jump in Neutral Ports` follow-up while owning at least a threshold convoy count and not being at war.  
**Disqualifier:** player at war when the follow-up fires.  
**Why it is interesting:** rewards a specific delayed follow-up and peaceful naval/trade posture.
**Icon direction:** marine insurance ledger, ship silhouette, red wax seal, no text.

### `achievement_tensions_one_denial`

**Title:** One Denial Too Many  
**Visibility:** hidden  
**Difficulty:** hard  
**Eligible player:** any country.  
**Unlock:** A recently affected Event 8 relation actor enters a war relation within 120 days after Event 8 applies relation damage.
**Disqualifier:** none beyond invalid tracking, implementation should avoid false positives from unrelated history if possible.  
**Why it is interesting:** rewards observing Event 8 feeding later tension through the existing war-relation hook without Event 8 creating the war.
**Icon direction:** denied stamp over sealed cable, no readable generated text.

### `achievement_tensions_blackout`

**Title:** Diplomatic Blackout  
**Visibility:** visible  
**Difficulty:** hard  
**Eligible player:** any country.  
**Unlock:** Ten distinct Event 8 timed opinion modifiers are active globally at once.  
**Disqualifier:** none.  
**Why it is interesting:** requires repeated evolved firings and validates relation-pair spread.  
**Icon direction:** blacked-out embassy facade with ten small lit windows.

## Achievement tracking notes

- Use global counters and flags, not player-only hidden assumptions, unless the existing achievement system requires a player scope.
- Avoid relying on raw event log entries if faster direct flags are safer.
- Achievement icon production belongs to asset work, grey/not-eligible variants follow existing achievement workflow.

## Current tracking evidence and gaps

| Achievement | Implementation evidence | Remaining limitation |
| --- | --- | --- |
| Thin Wire | Stage III+ peace and full-WT start, one `.20` callback chain with a 180-day date deadline, immediate war-hook cancellation | Daily sampling can miss a dip and recovery between checks; restart and ordering behavior are unobserved. |
| Only Headlines | Counts once per report batch whose first effectful displayed stage is Stage II+ in a peaceful world | Numerical reachability and live unlock behavior remain unverified. |
| Insurance Market | `.5` peaceful-player convoy check and unlock hook | The Stage II+ recent-damage branch usually shadows the only pool containing `.5`, so the achievement is rarely reachable; see the README proposal. |
| One Denial | Every selected pair refreshes each actor's own 120-day eligibility flag, read by the war-relation hook | Actor expiry and unrelated-pair refresh scenarios are unobserved. |
| Diplomatic Blackout | Unique directed stage-and-partner entries with per-direction `.21` expiry | Native expiry, duplicate delivery, and cross-stage behavior are unobserved. |

Source evidence is in `common/achievements/chaos_redux_achievements.txt`, `common/scripted_effects/008_tensions_rising_effects.txt`, and `events/008_tensions_rising.txt`, with exact reviewed spans in the release audit.
All fifteen achievement DDS headers parse at 64x64, but the deleted historical asset archive has no established replacement provenance/review package.
