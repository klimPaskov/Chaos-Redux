# Event 008: Cluster and Achievement Matrix

## Proposed cluster: Diplomatic Panic

This cluster is optional but recommended. It gives Event 8 a way to create a wider diplomatic incident without turning it into a direct war event.

### Cluster identity

- **Cluster ID:** implementation should choose the next available stable ID.
- **Cluster name:** Diplomatic Panic.
- **Cluster type:** Repeatable.
- **Unlock:** Rising Chaos or Event 8 Stage II.
- **Cooldown:** moderate to long, this cluster should be notable, not constant.

### Member plan

| Event | Role | Member severity | Stage gate | Notes |
| --- | --- | --- | --- | --- |
| 8 Tensions Rising | required | core | Stage II+ | always applies Event 8 effects |
| 10 Spirit of War/Peace | optional | mood | Stage II+ | if implemented and available, shows public mood split |
| 11 Secret Alliance | optional | intrigue | Stage II+ | if implemented and valid, secret-diplomacy echo |
| 4 Random War | indirect only | high | Stage III+ | do not make it a member unless cluster system supports cross-cluster safety, temporarily raise its weight instead |

### Cluster story

A Diplomatic Panic firing should feel like several departments reacting to the same set of rumours. It should count as one global pacing incident while still applying member effects through the cluster pipeline.

## Achievement matrix

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
**Why it is interesting:** rewards a specific hidden follow-up and peaceful naval/trade posture.  
**Icon direction:** marine insurance ledger, ship silhouette, red wax seal, no text.

### `achievement_tensions_red_line`

**Title:** The Red Line Disappears  
**Visibility:** visible  
**Difficulty:** medium-hard  
**Eligible player:** any country.  
**Unlock:** Witness the first Event 8 Stage IV super-event while no world-end scenario is active.  
**Disqualifier:** world-end already active.  
**Why it is interesting:** marks seeing the event’s final non-terminal form.  
**Icon direction:** a broken red cord across a dark embassy window.

### `achievement_tensions_one_denial`

**Title:** One Denial Too Many  
**Visibility:** hidden  
**Difficulty:** hard  
**Eligible player:** any country.  
**Unlock:** A Secret Alliance or Random War event fires within 120 days after Event 8 applies relation damage.  
**Disqualifier:** none beyond invalid tracking, implementation should avoid false positives from unrelated history if possible.  
**Why it is interesting:** rewards observing the hidden event-ecosystem connection.  
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
