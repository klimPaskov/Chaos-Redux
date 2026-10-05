# Event 008: Cluster and Achievement Matrix

Disposition: unresolved design acceptance, with catalog facts and implementation evidence separated below.
The [current source map](../../../plans/008_tensions_rising_plans/documentation_state_2026-10-05.md) and [release audit](../../../plans/008_tensions_rising_plans/subagent_handoffs/event_completion_audit_2026-10-05.md) govern current evidence and limits.

## Cluster: Diplomacy catalog record

The former single-member Low-severity `Diplomatic Panic` note is superseded as a current catalog statement by the parent's direct read-only workbook evidence.
It remains historical source-design direction with unresolved acceptance, and no design promotion is made here.

### Cluster identity

- **Cluster ID:** 3.
- **Cluster name:** Diplomacy.
- **Cluster type:** Repeatable.
- **Catalog status:** Partially Available.
- **Acceptance basis:** unresolved pending the cluster owner's source or explicit acceptance record.

### Current catalog members and reported implementation

| Event | Role | Member severity | Stage gate | Notes |
| --- | --- | --- | --- | --- |
| 8 Tensions Rising | required in retained overview | Medium | not established by this catalog audit | Event 008 root and follow-up implementation exists |
| 17 | not established by this audit | Medium | not established by this catalog audit | retained parent/overview four-member implementation evidence |
| 36 | not established by this audit | High | not established by this catalog audit | retained parent/overview four-member implementation evidence |
| 59 | not established by this audit | High | not established by this catalog audit | retained parent/overview four-member implementation evidence |

### Source contradiction and owner boundary

The pre-reconciliation overview and parent prompt report four-member Diplomacy runtime wiring and retained Diplomatic Panic compatibility aliases.
The reconciliation source read found only `diplomatic_panic = 3` in `common/script_constants/event_cluster_constants.txt:17` and an Event 8 required Low plus random-faction optional Low branch in `common/scripted_effects/chaosx_event_cluster_effects.txt:1327`.
This branch does not verify the reported four-member implementation, and its contradiction with the catalog and overview remains open.
The cluster owner must identify the authoritative definitions or supply a reviewed patch handoff and acceptance basis.
No member wiring, severity, cooldown, unlock, or cluster design was changed by this documentation task.

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
| Thin Wire | Stage III+ peace/full-WT start, player-war invalidation, and `.20` expiry check | Full WT is checked at the endpoints, without continuous full-WT tracking. |
| Only Headlines | Stage II+ peaceful-world counter and unlock hook | Numerical reachability and live unlock behavior remain unverified. |
| Insurance Market | `.5` peaceful-player convoy check and unlock hook | Earlier recent-relation selection can shadow its pool, with scenario evidence pending the probability owner. |
| One Denial | Existing war-relation hook reads recent actor state and global recent-damage state | The 150-day actor selection flag and refreshed global 120-day window do not enforce that actor's own 120-day receipt. |
| Diplomatic Blackout | Global application counter, `.21` delayed decrement, and unlock threshold | Distinct live modifiers, renewals, and stale-expiry receipts are not established. |

Source evidence is in `common/achievements/chaos_redux_achievements.txt`, `common/scripted_effects/008_tensions_rising_effects.txt`, and `events/008_tensions_rising.txt`, with exact reviewed spans in the release audit.
All fifteen achievement DDS headers parse at 64x64, but the deleted historical asset archive has no established replacement provenance/review package.
