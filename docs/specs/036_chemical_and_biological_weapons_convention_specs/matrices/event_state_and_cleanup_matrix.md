# Event state and cleanup matrix

| State | Created by | Ends when | Cleanup |
| --- | --- | --- | --- |
| Event 036 active flag | Canonical entry | Never | None |
| Coordinator | Opening setup | Coordinator becomes invalid | Bounded replacement ([01](../01_event_identity_and_playable_promise.md#global-setup-sequence)) |
| Country posture variable and posture idea | Opening response, accession, revision | Next valid change, withdrawal, expulsion, invalid country | Replace idea, AI strategy, and registry entry atomically |
| Covert program flag | Covert response or Begin Covert Program | End, exposure, accession, invalid country | Hide covert decisions, keep hidden evidence, set exposed memory on exposure |
| Convention Standing | Membership-changing transaction | Next such transaction | Replace the value once |
| Opposition Leader | Membership-changing transaction | Leader joins, becomes invalid, or loses top weight | Reselect |
| Active agenda | Scheduler | Resolution, sponsor or capability loss, Provisional Standing | Clear deadline, count, and conference decisions |
| Treaty ratification | Resolution | Withdrawal, expulsion, Charter lapse, invalid country | Remove future benefits and obligations, keep history |
| Suspension | Breach | 180 days, expulsion, withdrawal | Restore voting and contributions or expel |
| Evolution state | Evolution event | Never | Disabled evolutions block activation only |
| Integrated doctrine idea | Doctrine Integration success | Withdrawal, Charter loss, fewer than two usable families | Remove idea and drop relief stage |
| Opening normalization flag | Opening normalization | Never | Prevents a second application |
| Chaos outcome flags | Each one-time outcome | Never | Prevent farming |
| Program state | Charter, selection, pause, dormancy | Charter lapse returns to Inactive | Clear selection, progress, participants, and decisions |
| Selected project and progress | Selection, contributions | Completion, cancellation, lapse | Write history, reset active values |
| Contribution receipt and mission | Contribution decision | Mission end, pause, cancellation, invalid country | Apply once or not at all, never refund |
| Project history row | Completion or cancellation | Never | Prevents reselection and duplicate grants |
| Access flag | Completion grant | Never | The country keeps project access |
| Achievement snapshots and disqualifiers | Relevant transaction | Never | Survive save and reload |

## Invalid-country cleanup order

1. Fail its open missions without applying results.
2. Remove it from members, opponents, ratifier arrays, and participants, keeping history.
3. Recalculate Standing and reselect the coordinator and Opposition Leader when needed.
4. Recheck the active agenda's capability gate and the program quorum.
