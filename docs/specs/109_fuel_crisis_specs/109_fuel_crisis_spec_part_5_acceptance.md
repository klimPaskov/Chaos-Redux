# Fuel Crisis: acceptance and balance review

## What a successful version feels like

Fuel Crisis should create a sharp interruption followed by understandable recovery. The player loses the reserve that supported an existing military plan, sees that ordinary supply still works, and chooses which commitments to sustain while rebuilding room to maneuver.

The same event can be brief for a country with a large surplus and serious for a country with an exposed supply deficit. That variation is part of the design. Balance review should look for a clear cause and a credible response, rather than trying to give every country the same shortage duration.

The Tasks connection adds an optional active challenge to that situation. It should recognize a decision that improves the country's position and use Event 101's established stakes. It must not make the world wipe depend on receiving a mission or redefine recovery for countries without one.

## Non-negotiable outcomes

| Design promise | Acceptance condition | A failure that must be corrected |
| --- | --- | --- |
| Everyone loses stored fuel together | Every existing country's national stockpile is zero at the same event resolution | Exempt players, subjects, special tags, already empty countries, or repeated per-recipient execution |
| The loss happens once | One natural occurrence changes the world once and survives save/load | Clicking an acknowledgment, reopening a popup, loading a save, or duplicate delivery performs another wipe |
| The economy still works | Normal oil access, production, imports, capacity, buildings, and fuel rules retain their prior state | A hidden drain, production debuff, broken agreement, damaged refinery, or delayed recovery lock |
| The military consequence follows the game | Native reserve shortages and local fuel allocation determine operations | Added unit penalties used to force every formation to stop immediately |
| Recovery is ordinary strategic play | Supply improvement and lower demand can restore a buffer under existing rules | A mandatory event stance, invented fuel currency, or recovery button |
| Tasks remains its own system | One selected player can receive a feasible contract and one ordinary Tasks outcome | Global task assignment, AI missions, an Event 109 reward table, or repeated terminal rewards |
| Chaos comes from the actual manifestation | Part 1's one-time scaled world contribution is applied once | An award per country, repeated shortage awards, or duplicate generic-source credit |
| The presentation describes the mechanic | The news and shared log communicate a sudden unexplained reserve loss | A picture or text implying destroyed oil wells, refineries, trade routes, or an identified attacker |

An exact-zero observation belongs at the end of the event resolution. Positive fuel on a later normal update can demonstrate successful recovery. It must not be mistaken for proof that the setter failed.

## Campaign coverage

Use the following contrasting situations to review the complete experience. These are test situations and do not add country-specific rules.

| Situation | What should be visible | Balance question |
| --- | --- | --- |
| Large producer, moderate operations | Reserves disappear and begin rebuilding promptly | Does the event respect the country's real surplus? |
| Large producer, simultaneous intensive operations | New production competes with heavy demand | Can resource wealth coexist with a genuine operating deficit? |
| Dependable importer | Existing delivered supply continues and can refill the reserve | Does the event avoid assuming that all importers recover slowly? |
| Importer under disruption | Actual delivery matters more than the nominal agreement | Can the player understand why a paper supply increase has not solved the shortage? |
| Small economy with one important fuel-using capability | A limited force faces a meaningful allocation choice | Is any offered target scaled to demand and capacity? |
| Country with negligible fuel demand | The reserve loss occurs without an artificial mission | Can the system leave a low-impact case alone? |
| Country already empty | The stockpile remains zero and the occurrence is recorded | Is there no invented positive-loss Chaos contribution from that country? |
| Subject with restricted diplomacy | The wipe applies and its real available responses remain usable | Does Tasks avoid asking for an action the country cannot perform? |
| Multiplayer with several affected humans | Everyone observes one world occurrence | Does acknowledgment timing leave the world result unchanged? |
| A country created after the occurrence | Its normal creation rules apply | Is the historical loss confined to countries that existed at impact? |

If a country's available ordinary actions cannot produce a measurable, achievable task, it should continue recovering without a Fuel Crisis assignment. That is appropriate selection, provided the implementation reports which planned task routes remain unsupported.

## Tasks boundary cases

Part 3 owns the full formulas and contracts. Review must exercise the meaningful boundaries, not only a favorable demonstration.

| Boundary | Expected result |
| --- | --- |
| Stored fuel is already at the proposed reserve target | No reserve assignment for that solved target |
| Unchanged play reaches the target within 60 days | Skip the passive reserve candidate |
| Consumption falls only because fuel is unavailable | No conservation credit |
| A real activity reduction meets the chosen action condition | It can qualify while the frozen reserve target remains unchanged |
| Additional nominal imports are not delivered | No dependable-source success and no supply-improvement credit |
| The country gains a one-time fuel transfer | It can help the reserve quantity but does not prove recurring oil supply |
| Capacity is exactly fourteen days of reference demand | The reserve target is seven days of that demand |
| Capacity is below that eligibility threshold | Reject the reserve template and consider only another independently feasible objective |
| The forecast rounds to 180 days | It can qualify if all other feasibility checks pass |
| The forecast rounds above 180 days | Reject it without shortening the forecast |
| The first target observation qualifies | Hold progress starts at zero elapsed days |
| A later required observation fails | Reset the hold while retaining the original cutoff |
| The final permitted observation completes the contract | Resolve timely success once |
| The first observation after the cutoff would complete it | The expired contract cannot be rescued |
| An ordinary military setback makes success harder | Keep the agreed risk and deadline |
| The task definition or its required measurement becomes invalid | Cancel neutrally through Event 101 |
| Save/load occurs during a hold | Preserve valid recorded progress without inventing missed observations |
| The human leaves the assigned country | Apply the Tasks lifecycle's neutral cancellation |
| The same terminal callback arrives twice | The second callback produces no outcome |

The full fourteen-day reserve used by the achievement is deliberately stricter than the minimum reserve template. [Part 4's complete achievement contract](109_fuel_crisis_spec_part_4_presentation_and_achievement.md) governs its eligibility, imported-flow requirement, observed hold, cutoffs, and genuine Tasks success hook. A valid task success can earn its normal reward without earning the achievement. The achievement must have a feasible demonstrated campaign case under its complete conditions before it can be considered implemented.

## Selection and timing review

Fuel Crisis has a deterministic world effect. Any probability analysis concerns the shared event pool or Event 101's existing recipient and objective selection. The specification does not assign new numeric selection odds because the complete live candidate pool and all external eligibility factors were unavailable during planning.

| Named scenario | Selection or timing expectation | Evidence needed during implementation |
| --- | --- | --- |
| Natural eligible world | A reconciled, enabled, eligible 109 can participate through existing shared selection | Inspected registration, candidate pool, and existing weights |
| Natural consumed world | Ordinary selection cannot choose 109 again | The same scenario with the consumed state changed and shared eligibility reevaluated |
| Deliberate force replay | A deliberate new force request can create a fresh admitted occurrence | The supported force path and its explicit bypass conditions |
| Force before natural selection | The first committed occurrence consumes the natural slot and remains achievement-ineligible | Persistent owner state, shared fired membership, and frozen origin |
| Duplicate delivery | The existing occurrence performs no repeated effect or accounting | The same occurrence receipt delivered twice |
| Tasks selected player eligible | The existing Tasks selector may consider a feasible Fuel Crisis objective | Actual recipient and objective-pool definitions with verified context |
| Tasks selected player ineligible | Event 101 retains its own other-objective or no-valid-objective behavior | No multiplayer reroll introduced solely to force this connection |
| Tasks already active or disabled | Existing admission limits remain authoritative | The relevant existing Tasks settings and lifecycle states |
| Tasks offer window expired | No new assignment from that context, while a previously active task retains its own cutoff | Boundary observations at the verified owner date convention |

The probability auditor should compare matched before-and-after sources and named scenarios. Report conditional weights separately from actual probabilities. Do not invent a uniform multiplayer choice, a custom retry pool, or an exact wait time from incomplete evidence. Deterministic forecast deadlines in Part 3 are not random timers.

The achievement accepts eligible ordinary shared selection and normal non-force manual dispatch. Deliberate forced and raw direct-debug occurrences cannot earn it. Existing campaign validity also applies. This restriction uses the occurrence's frozen origin and leaves ordinary Tasks rewards under Event 101's rules.

## Presentation and discoverability

Part 4 supplies the visible surfaces and their production requirements. Acceptance should review the actual announcement, shared history, any assigned task, and achievement state at their native sizes.

The announcement needs to answer what was lost, whether fuel can return, and where the player can act. The shared Event Details entry remains a concise premise description. The task must show a specific action and measurable target, observed hold progress, and deadline. Detailed fuel rates belong in the game's existing fuel information.

The two scene crops should remain legible independently. The report treatment and the news treatment use their own processing rules and actual consumers. The completed, grey, and not-eligible achievement icons must be recognizable at 64 by 64 pixels. Generated scene art must be identified honestly in the source record.

## Compatibility and performance

The core uses the ordinary national fuel system. Future implementation must confirm that behavior with the supported base game and active DLC or mod combinations that change a relevant consumer or recovery action. It must not require a particular DLC simply to apply the stockpile wipe.

A task action that relies on an unavailable campaign feature is excluded by its real eligibility. Other independently supported actions remain available. The implementation report must name unsupported actions and the affected combinations so that partial support is visible.

The required world work is one pass per admitted occurrence. Ongoing task observations belong to Event 101 and only its active contracts. A country-wide recovery scan running every day, week, or month is unnecessary. High game speed and multiplayer must not create additional occurrences, advance holds without observations, or multiply notifications and rewards.

## Completion evidence

Planning is complete when the design, numerical assumptions, presentation, dependency boundaries, source record, review dispositions, and implementation instructions agree. This package completes that design task. Its final review record identifies the review performed and any corrections made before delivery.

Gameplay completion is a later claim. It requires implemented files, the verified native and Tasks interfaces, finished localisation and assets, supported source and MCP evidence, and the user's live-game observations. The separate implementation handoff assigns those checks and their owners.

Retain the requested **To Be Reworked** status during this planning handoff. Report the core, each Tasks route, achievement, assets, integration, and validation separately during implementation. A functioning world wipe cannot stand in for the rest of the accepted feature.
