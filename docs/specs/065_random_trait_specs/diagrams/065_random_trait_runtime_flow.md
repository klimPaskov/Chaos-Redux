# Event 065 Runtime Flow

```text
NORMAL RANDOM EVENT SELECTION
          |
          v
Event 65 selected as Minor Repeatable
          |
          v
Shared event dispatcher calls chaosx.nr65.1 once
          |
          +-----------------------------+
          |                             |
          | Cluster source              | Direct source
          | records member context      | records direct context
          |                             |
          +--------------+--------------+
                         |
                         v
Validate generated registry and active pool
                         |
              +----------+----------+
              |                     |
           invalid                valid
              |                     |
              v                     v
Record blocked result       Resolve highest enabled
Do not mutate world         manifested or available form
                                    |
                                    v
                         Set target traits per leader
                         Baseline 1
                         Evolution I 2
                         Evolution II 3
                         Evolution III 5
                                    |
                                    v
                         Begin one global country pass
                                    |
                                    v
                     Country exists and has active leader?
                              |               |
                             no              yes
                              |               |
                              v               v
                       Count skipped      Resolve recipient role
                                              |
                                              v
                                      For each required slot
                                              |
                                              v
                                      Build eligible source set
                                      Current traits excluded
                                      Event 65 ledger excluded
                                      Earlier firing slots excluded
                                              |
                                  +-----------+-----------+
                                  |                       |
                              empty                   not empty
                                  |                       |
                                  v                       v
                         Count saturation       Draw by stage weights
                                                          |
                                                          v
                                                Apply native source trait
                                                          |
                                               +----------+----------+
                                               |                     |
                                            failed                accepted
                                               |                     |
                                               v                     v
                                        Count failure        Write ledger and
                                        Handle per spec      report index
                                                                     |
                                                                     v
                                                           Continue next slot
                                    |
                                    v
                         Finalize global result counters
                                    |
                                    v
                      Did at least one trait get added?
                              |               |
                             no              yes
                              |               |
                              v               v
                     Record zero result      Grant unclaimed form
                                            manifestation Chaos
                                            Record Evolution history
                                    |
                                    v
                         Record one Event 65 history row
                                    |
                                    v
                         Record cluster member outcome
                         when cluster context exists
                                    |
                                    v
                         Dispatch one report to each
                         human-controlled country
                                    |
                                    v
                         Reports read committed results
                         Acknowledgment does not mutate
```

## Flow invariants

- The trait roll path exists once.
- Direct and cluster paths converge before gameplay mutation.
- Random rolls finish before reports.
- AI countries are changed without visible reports.
- A zero-result firing cannot claim a successful milestone.
- One world pass creates one global history row.
- Report timing cannot change the result.
