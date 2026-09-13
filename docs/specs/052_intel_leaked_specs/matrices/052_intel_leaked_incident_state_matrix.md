# Event 052 Incident State Matrix

This matrix is a design reference for one Event 52 sequence. It distinguishes public state, hidden simulation state, entry conditions, player actions, AI behavior, and cleanup.

| State | Public signal | Hidden conditions | Main player actions | Foreign behavior | Exit condition | Cleanup requirement |
| --- | --- | --- | --- | --- | --- | --- |
| Incident creation | Opening report identifies target and broad domains | Valid target selected, sequence identity created, archive profile generated | None before report | Recipients and named exploiters are registered | Opening processing completes | Reject and clear incomplete sequence if target proof fails |
| Critical Exposure | Exposure 76 to 100, urgent status, current domains | High freshness, current plans or personnel, strong recipient confidence | Replace codes, recall personnel, rewrite plans, shut channels | Named exploiters act quickly, Reliance can rise sharply | Exposure falls to 75 or lower | Keep only current target and recipient records |
| Severe Exposure | Exposure 51 to 75 | Archive still current, foreign copies broadly useful | Emergency actions remain, reconstruction begins | Relevant exploiters continue active use | Exposure falls to 50 or lower | Remove resolved domain risks |
| Significant Exposure | Exposure 26 to 50 | Operational detail becoming unreliable | Reconstruction, compartmentation, liaison repair, deception | Exploiters verify files, high-Reliance actors can still act | Exposure falls to 25 or lower | End emergency actions whose risks are gone |
| Fading Exposure | Exposure 1 to 25 | Most archive content obsolete, some recipients retain old assumptions | Finish reform, observe deception, accept expiry | New named exploitation is rare, existing deception outcomes can mature | Exposure reaches zero or timer expires | Remove broad intelligence in exact proportion to committed decline |
| Neutralized | Exposure 0 | No Event 52 special intelligence remains | Closing report when meaningful | No new Event 52 exploitation | Target closure runs | Remove all target-owned temporary state |
| Personnel danger | Warning or Personnel at Risk mission | Sensitive domain plus live asset plus high hidden risk | Recall, close channels, replace codes, cover rebuild | Strong service can attempt network or operative exploitation | Mission succeeds, risk falls, or one bounded failure resolves | Clear risk record and mission after resolution |
| Reconstruction | Category shifts to recovery actions | Emergency action completed or Exposure below Severe | Rebuild covers, networks, compartmentation, liaison | Foreign activity becomes less reliable | Target completes needed repairs or incident ends | Remove temporary reconstruction penalties after their own duration |
| Deception preparation | Poison route available, Deception Window can begin | Containment proof, target capability, high-Reliance hostile recipient | Poison leak, seed contradictions, stage false deployment | Reliant recipients continue using the archive | Recipient acts, window expires, target cancels, or deception is exposed | Clear selected deception profile and tied-force proof |
| Deception success | Report shows foreign mistake or exposed plan | Coherent false profile, matching recipient action, sufficient Reliance | Exploit confirmed result | Affected recipient suffers bounded domain penalty | Result duration expires | Preserve achievement proof, clear temporary penalty |
| Deception partial success | Report identifies limited foreign reliance | Some recipients act, some verify independently | Continue recovery | Only affected recipients receive weaker result | Window ends | Clear unresolved deception targets |
| Deception failure | Report shows detection or contradiction | Weak target capability, inconsistent posture, independent recipient verification | Return to recovery, accept renewed risk | One exploiter gains confidence or avoids future poison | Failure consequence committed | Prevent unlimited retry in same incident |
| Deep Files second tranche | New report, domains and Exposure rise | Deep Files activates during active incident, Exposure above Fading, tranche unused | Renew emergency response | New exploiters or stronger personnel pressure | Tranche processed | Mark tranche consumed once |
| Total Compromise escalation | Additional target reports | Evolution II activates during active incident, valid pool exists, escalation unused | Each human target manages own category | AI targets and exploiters process independently | All target states close | Sequence remains until final target resolves |
| Passive expiry | Archive Freshness reaches deadline | Exposure remains above zero but special value has aged out | None beyond final closing result | Event 52 advantages end | Final expiry processing completes | Remove every temporary intelligence and recipient record |
| Invalid participant | Usually no player report | Target or recipient annexed, removed, or reclassified | None | Invalid actor stops acting | Validation pulse removes actor | Never leave stale target, exploiter, or event target |

## Phase visibility map

| Phase | Required visible information | Normal action set | Normal mission set | Hidden calculations |
| --- | --- | --- | --- | --- |
| Immediate containment | Exposure, stage, domains, personnel warning, next threshold | Replace codes, recall personnel, rewrite plans, shut channels | Archive Freshness, Personnel at Risk, Emergency Replan | Depth, confidence, risk, named-exploiter priorities, recipient Reliance |
| Network reconstruction | Exposure, damaged capacity, current recovery need | Rebuild covers, reconstitute networks, compartmentalize, restore liaison | Archive Freshness, one reconstruction mission when needed | Regional network records, ally cooperation, future resilience cap |
| Optional deception | Exposure, selected deception profile, broad observed reliance | Poison leak, seed contradictions, stage false deployment, trace source | Archive Freshness, Deception Window | Exact recipient Reliance, authenticity checks, outcome weights |
| Closure | Final result and lasting consequences | None | None | Final cleanup proofs and achievement commits |

## Sequence ownership rules

- A baseline sequence owns one target.
- A Total Compromise sequence owns one to four targets.
- Every target has separate Exposure and recovery state.
- The sequence owns one evolution profile and one global report budget.
- Named exploiter state is stored per target and recipient pair.
- A recipient can exploit more than one target under Total Compromise, but each pair has independent Reliance.
- The sequence closes only after every target has reached zero or expired.
- New ordinary Event 52 firing remains unavailable while a sequence is active.
