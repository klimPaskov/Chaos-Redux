# Decision and Mission Map

All action names are working labels. Final localisation should be written during implementation.

## Action map

| Action | Phase | Availability | Primary cost or sacrifice | Exposure effect | Other result | Main risk | AI priority |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Replace Codes and Authentication Tables | Emergency | Cryptologic domain, or Severe and Critical emergency | Command power, support equipment, temporary command friction | Large when cryptologic files active, moderate otherwise | Lowers confidence and personnel risk | Short-term coordination loss | Highest with cryptologic exposure or imminent war |
| Recall Exposed Personnel | Emergency | Personnel Risk active | Operative downtime, operation cancellation, network loss | Moderate with personnel domains | Prevents capture and burned cover | Loss of foreign access | Highest near mission failure |
| Rewrite Compromised Plans | Emergency | Military or mobilization domain active | Relevant XP, temporary readiness loss | Large in selected domain | Reduces matching exploitation and Reliance | Temporary planning or mission weakness | Highest against credible enemy plan |
| Shut Down Vulnerable Channels | Emergency | Network or personnel danger | Network strength, operations, liaison access | Moderate | Strong risk protection | Intelligence blindness and long rebuild | High for weak services |
| Rebuild Cover Identities | Reconstruction | Personnel recalled or cover damaged | Civilian factory burden, support equipment, time | Small to moderate | Restores personnel protection and some access | Resource burden | High after successful recall |
| Reconstitute Foreign Networks | Reconstruction | Agency surface and damaged networks | Operative time and agency capacity | Small | Restores selected network gradually | Long recovery | Medium for strong service, low during war emergency |
| Compartmentalize the Archive | Reconstruction | First emergency action complete or Exposure below Severe | Civilian capacity, administrative or research disruption | Small current effect | Bounded future resilience | Expensive during active war | High in peacetime and after danger falls |
| Restore Trusted Liaison Channels | Reconstruction | Valid friendly partner | Agency capacity, secure communications burden | Small | Reveals one domain or exploiter and repairs relation | Partner may hold incomplete copy | Medium with strong ally |
| Seed Contradictory Orders | Counterplay | Containment proof, Exposure above Fading | Command power, support equipment or relevant XP | Small on success | Lowers confidence and reveals verification behavior | Failure raises Reliance | Medium before full poison route |
| Poison the Leak | Counterplay | Capable target, hostile high-Reliance recipient, one containment proof | Agency capacity, relevant XP, temporary operational burden | Large on success | Enables domain-specific foreign mistake | Failure can raise Exposure and close route | High for strong service with reliable target |
| Stage a False Deployment | Counterplay | Valid domain and credible recipient | Tied formations, fleet, aircraft, fuel or transport | Depends on outcome | Starts Deception Window | Opportunity cost and cancellation failure | High only with matching hostile plan |
| Trace the Source | Reconstruction or counterplay | Incident active, no route result yet | Civilian effort, intelligence capacity, time | Small or none | Returns practical route class and reform bonus | Can end indeterminate | Medium when immediate danger controlled |

## Visibility rules

- The category normally shows three to five primary actions.
- Six is the hard maximum in a rare transition state.
- Domain-invalid actions remain hidden.
- Completed one-shot emergency actions remain hidden unless a new tranche reopens their exact problem.
- Reconstruction actions replace resolved emergency actions.
- A staged false deployment replaces its launch action with the active mission.
- AI can evaluate valid actions without a player-only target selector.
- Blocked actions show the real missing cost or requirement through concise custom tooltips.

## Mission map

| Mission | Trigger | Duration direction | Success | Partial success | Failure | Repeat rule |
| --- | --- | --- | --- | --- | --- | --- |
| Archive Freshness | Every target incident | Baseline 120 to 240 days, longer under evolutions | Remaining special exposure closes at deadline after final processing | Not applicable | Foreign exploiters had more time to act | One per target incident |
| Personnel at Risk | Sensitive domain plus real personnel or generic security risk | 60 to 100 days | Severe personnel result prevented or sharply reduced | Personnel saved while network or operation is sacrificed | One bounded severe personnel outcome | Can reopen once after a proven new tranche |
| Emergency Replan | War or credible invasion plus military domain | 75 to 135 days | Exposure falls and one exploiter loses advantage | Plan changes after some exploitation has occurred | Relevant enemy gains stronger opening use | One per active exposed domain group, with clutter cap |
| Deception Window | Poison route or false deployment begins | 90 to 150 days | Matching high-Reliance recipient acts on false information | Some recipients act or effect is weaker | Deception detected, cancelled, or inconsistent | One main poison campaign per incident |

## Cost budget examples

These are design anchors. Final values must scale and pass the decision audit.

| Action | Example cost package | Cost count | Non-cost requirement | Consequence |
| --- | --- | --- | --- | --- |
| Replace codes | Command power, support equipment | 2 | Incident active | Temporary command friction |
| Rewrite land plan | Army XP | 1 | Land domain active | Temporary planning loss |
| Rewrite naval plan | Navy XP, fuel | 2 | Naval domain and meaningful fleet | Temporary mission disruption |
| Recall personnel | Operative downtime, network loss | 2 | Personnel risk | Foreign access lost |
| Rebuild covers | Civilian factory burden, support equipment | 2 | Personnel recalled or cover burned | Time delay |
| Compartmentalize | Civilian factory burden, temporary administrative or research disruption | 2 | Immediate danger partly controlled | Future resilience cap |
| Stage false naval deployment | Navy XP, fuel | 2 | Valid fleet and recipient | Fleet tied to false posture |
| Trace source | Civilian factory burden, agency capacity | 2 | Investigation unresolved | May return indeterminate |
