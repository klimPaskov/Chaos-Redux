# Event 046 acceptance scenarios

These scenarios define source, tool, and later live acceptance work.

This package does not claim that any scenario was executed in game.

## Core transaction scenarios

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `A46-001` | Baseline global firing | Ordinary world, Chaos below 200, all Baseline families valid | One global transaction selects the accepted family share, every human receives one report, AI receives effects, one Event Log entry and one Event 46 Chaos entry exist |
| `A46-002` | Independent countries | Two countries begin with identical old values | Each receives an independent new result, with no forced exchange or paired total |
| `A46-003` | Old amount independence | Two countries have extreme opposite old values but identical legal caps | Their new result distribution uses the same profile and does not favor restoration or compensation |
| `A46-004` | Consecutive family repeat | The same family is eligible on two consecutive firings | The family can be selected twice and the second roll has no prior-selection modifier |
| `A46-005` | No valid family | Every selected family has no valid scope or fails before commit | No gameplay value changes, no firing is consumed, no success report, Event Log entry, or direct Chaos gain appears |
| `A46-006` | Mixed valid and invalid families | Some selected families validate and some reject before commit | Valid families commit fully, rejected families remain untouched, report and debug evidence distinguish them |
| `A46-007` | Duplicate start | Automatic, cluster, or manual source attempts a second start during a live transaction | The second call cannot open, reroll, or consume another firing |
| `A46-008` | Save during transaction | Save after planning or partial commit, then load | Exact original results resume, no reroll, no duplicate Event Log, report, Chaos, or firing consumption |
| `A46-009` | Stale lock | Lock exists without complete transaction proof | Explicit repair blocks a new roll and does not silently clear the lock |

## Scope and exclusion scenarios

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `A46-010` | Human minor | Player controls a small non-major country | Country remains eligible for every ordinary legal family and receives no scale protection |
| `A46-011` | Special Chaos country | Registered special and actual nonhuman actors exist | Ordinary civilian politics and population families exclude them unless an owner adapter proves eligibility |
| `A46-012` | Dormant carrier or system actor | Country scope exists only for framework ownership | It never enters an ordinary gameplay family |
| `A46-013` | Invalid state types | Impassable, terminal wasteland, unowned placeholder, and owner-protected states exist | Each family applies its own exclusion and no invalid state receives a result |
| `A46-014` | Unit in unstable lifecycle | Units are in deployment, transport, owner transfer, or another unsupported state | The unit family excludes them without invalidating stable units |

## Baseline and stores scenarios

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `A46-015` | Percentage extremes | Stability and War Support selected at a high capability | Results can reach legal low and high tails without exceeding bounds |
| `A46-016` | Zero fuel capacity | Country has zero legal fuel capacity | Fuel result is exactly zero and family commit remains valid |
| `A46-017` | Small country huge arsenal | Tiny country enters an Evolution I equipment family | It can receive a huge legal stockpile not scaled to its old size or industry |
| `A46-018` | Unsupported equipment token | Loaded world contains unique or malformed owner-managed equipment | Generic equipment family excludes it and no fake token is created |
| `A46-019` | Equipment-rich and equipment-poor world moods | Run abundance and scarcity family moods | World total can rise or fall sharply with no conservation or recipient pairing |

## State scenarios

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `A46-020` | Population rewrite loss | State receives a much lower absolute population | Population changes exactly, Deaths and migration remain unchanged, recruitable-manpower side effect is reconciled |
| `A46-021` | Population rewrite gain | State receives a much higher absolute population | Population changes exactly without a birth ledger or unintended national manpower grant |
| `A46-022` | Population and industry independence | Both families select the same large state pool | Sparse industrial centers and dense low-industry states occur, with no forced correlation |
| `A46-023` | Shared factory capacity | Civilian, military, and dockyard results would exceed old slots | The preplanned capacity bundle makes the final sum legal or rejects before commit |
| `A46-024` | Inland dockyard | Inland state enters shared factory bundle | Dockyard result is zero or state is excluded from that child family while other factory results remain legal |
| `A46-025` | Coastal building validity | Coastal and inland states receive coastal-fort or naval-base candidate results | Only consumer-valid states and provinces receive the building |
| `A46-026` | Resource rewrite | Ordinary and owner-protected deposits coexist | Ordinary resources change, protected deposits and discovery history remain unchanged, trade refreshes correctly |
| `A46-027` | Supply graph blocked | Supply-hub or railway family lacks complete graph proof | Family remains unavailable and no infrastructure substitute is silently used |

## Politics, research, production, and military scenarios

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `A46-028` | Party-share normalization | Country has every loaded ordinary ideology | New shares total the exact legal amount and no ideology receives an invalid token |
| `A46-029` | Low-support ruling ideology | Conditional ruling-ideology family selects a party with low popularity | Government remains legal, display and AI refresh, generic ideology Chaos does not duplicate Event 46 |
| `A46-030` | Law compatibility | Several law categories and country-specific laws exist | One valid token per selected ordinary category, owner laws excluded without adapter |
| `A46-031` | Active research progress | Country has active and empty research slots | Active progress changes on the same project, empty slots skip, completed graph and slots remain unchanged |
| `A46-032` | Doctrine graph protection | Doctrine progress family selected | Current approved progress changes, completed nodes and mutual exclusions remain intact |
| `A46-033` | Production-line identity | Production numeric family selected | Efficiency or progress changes, item, variant, line, queue identity, and MIO remain unchanged |
| `A46-034` | Unit and commander identity | Units and commanders receive experience results | Names, templates, traits, assignments, owners, and stable identities remain unchanged |
| `A46-035` | Unsupported readiness setter | Organization or strength lacks complete proof | Family remains unavailable without weakening the unit-experience family |

## Owner-adapter scenarios

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `A46-036` | Valid public adapter | Active owner mechanic exposes one current pressure | Result stays inside owner range, stage and AI refresh, report shows public label, history remains protected |
| `A46-037` | Hidden adapter | Owner exposes an internal value that supports a public total | Value can change when safe but no raw report row leaks it |
| `A46-038` | Incomplete lifecycle | Adapter target or owner proof is missing | Instance or family rejects before commit and no fallback scope is used |
| `A46-039` | Unfavorable result veto attempt | Owner dislikes a legal planned result | Owner cannot veto for balance or convenience |
| `A46-040` | Adapter save recovery | Save during adapter commit and reconciliation | Exact planned result resumes and owner cleanup runs once |
| `A46-041` | Protected ledger audit | Owner exposes current value beside history arrays | Only current value changes, every historical row and first-discovery proof remains byte or value identical |

## Evolution and World Collapse scenarios

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `A46-042` | Evolution before first firing | Reach 200 or 400, wait for enabled evolution, Event 46 has never fired | Evolution can record and the first firing uses its family domain |
| `A46-043` | Disabled evolution | Threshold met with one evolution disabled | No record, no family unlock, earlier capability still works |
| `A46-044` | Evolution V with post-threshold picker | Live framework selects events until terminal world end | Evolution V activates immediately and Event 46 remains normally selectable until terminal commitment |
| `A46-045` | Evolution V with immediate freeze | Live framework freezes automatic events at 1000 | One bounded enabled pre-freeze Event 46 opportunity exists, fires at most once, and never bypasses an existing terminal state |
| `A46-046` | Evolution V maximum pool | Every core family and several adapters valid | Every non-conflicting mandatory family participates, total eligible coverage reaches at least 90 percent, report remains concise |

## Chaos and shared-system scenarios

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `A46-047` | One direct Chaos entry | Many families and scopes commit | One bounded Event 46 history change represents the transaction |
| `A46-048` | First manifestation | First successful firing then a later comparable firing | One-time premium applies only to the first and remains inside its band |
| `A46-049` | No Deaths double count | Population falls across many states | Deaths totals and death-generated Chaos do not change from the rewrite |
| `A46-050` | No ideology double count | Several ruling ideologies change | Generic ideology-change Chaos is suppressed for the transaction only |
| `A46-051` | Later real consequence | A shuffled country later starts or ends a real war | The later generic source records normally |
| `A46-052` | Protected framework snapshot | Capture Chaos, event, log, scenario, cluster, world-end, settings, and ledger state before firing | Only intended Event 46 history, direct Chaos, achievement proof, and gameplay values change |

## Cluster and catalog scenarios

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `A46-053` | One-member Randomizations cluster | Event 46 is the only valid member | One Great Shuffle transaction and no duplicate member effect |
| `A46-054` | Multi-member Randomizations cluster | Add a valid second member | Shared cluster pacing and member history work without changing Event 46 result count |
| `A46-055` | Event 21 dual membership | Wars and Domestic Unrest both registered | Both relationships remain visible and usable, with relation-specific severity when supported |
| `A46-056` | Catalog export | Workbook updated and exporter run | Event 46, Randomizations, Domestic Unrest, Event 2, Event 21, and resolved Event 43 rows agree with runtime and no CSV was edited by hand |

## Reports, multiplayer, and persistence scenarios

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `A46-057` | Two human players | Multiplayer game with two countries | One shared world result, one personalized report per human, no local rerolls |
| `A46-058` | Player disconnect | One human disconnects during staged transaction | Transaction completes and reconnect does not duplicate report or result |
| `A46-059` | Tag switch during report timing | Human changes controlled country at the allowed time | Exactly one report uses the finalized controlled scope and no second transaction opens |
| `A46-060` | Report prioritization | Many player-owned values change | Report shows largest actionable rows by family-normalized score and an omitted count, without raw debug data |
| `A46-061` | Event Details | Open event detail before and after each evolution | Premise, type, level, cluster, severity, fired count, weight, toggle state, and evolution descriptions stay aligned |

## Achievement scenarios

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `A46-062` | Shuffle veteran | Five natural successful firings on one country, then survive 365 days | Achievement completes once and cannot be shuffled |
| `A46-063` | Empty depots recovery | Qualifying three-part loss, then full recovery and war victory inside 730 days | Achievement completes only when every condition is met |
| `A46-064` | Impossible geography | Crossed state rankings then 365 days of control and supply | Proof survives ordinary later development and fails on occupation or loss |
| `A46-065` | Government rebuilt | Qualifying political collapse then recovery inside 540 days | Owner exclusions and all thresholds work, no force path qualifies |
| `A46-066` | World redealt | Maximum Evolution V transaction and 180-day survival | Coverage denominator excludes invalid and conflicting families correctly |
| `A46-067` | Three reversals | Exact top, bottom, top sequence and later war victory | Family comparability, consecutive sequence, and disqualifiers work |

## Performance scenarios

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `A46-068` | Baseline stress | Maximum ordinary country count | One-shot transaction completes without periodic processing or stale buffers |
| `A46-069` | State stress | Every valid state with population, factories, buildings, and resources | Planning and commit stay deterministic and practical, report remains bounded |
| `A46-070` | Adapter stress | Large owner-adapter registry with many active instances | Registry, selection, and cleanup remain bounded and no adapter starves unexpectedly |
| `A46-071` | Evolution V stress | Maximum safe family and scope pool | Transaction uses approved batching when needed, preserves exact plan, and reports any blocked conditional family honestly |
