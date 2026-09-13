# Gods of Africa acceptance matrix

## Use

This matrix defines implementation acceptance cases. It does not claim that any case has been executed in the active planning environment.

Each case should receive one of these final statuses during implementation review:

- pass
- failed
- blocked
- needs user review
- not applicable

## Activation and ownership

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `ACT-01` | Event 012 ownership | Inspect registration and namespace | Gods of Africa has no normal event registration and uses only Event 012 ownership |
| `ACT-02` | Event 070 remains free | Inspect event files, details, and workbook | No Gods code or catalog identity remains assigned to Event 070 |
| `ACT-03` | Evolution I missing | African unifier exists without Evolution I | System does not activate |
| `ACT-04` | Consolidation incomplete | Evolution I active before 180-day delay | System does not issue demands |
| `ACT-05` | Normal activation | All conditions valid after delay | System activates once, Strength initializes, participants register |
| `ACT-06` | Unifier disappears before activation | Remove or invalidate unifier during delay | Activation cancels cleanly and no participant category appears |
| `ACT-07` | Weak unifier activation | Valid but militarily weak Africa | System activates with low Strength and limited punishment ceiling |
| `ACT-08` | Duplicate activation call | Call activation helper twice | Second call has no effect |
| `ACT-09` | Event 012 final state already reached | Secured-Africa proof exists before delayed call | Tribute cycle does not begin |
| `ACT-10` | Evolution disabled after timer starts | Disable Evolution I before activation | Activation fails closed and no recorded milestone leaks |

## Participant registry

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `REG-01` | Major participant | Normal major at activation | Registered once |
| `REG-02` | Player-controlled minor | Human minor at activation | Registered once despite non-major status |
| `REG-03` | African unifier | Unifier is major and player-controlled | Excluded from participant registry |
| `REG-04` | Dual qualification | Major is also player-controlled | One record only |
| `REG-05` | Later major | Country becomes major after activation | Registered through bounded onboarding |
| `REG-06` | Later player control | Human takes control of unregistered minor | Registered once and receives introduction |
| `REG-07` | Major status lost | Registered major becomes minor | Remains a participant |
| `REG-08` | Annexed participant | Participant ceases to exist | Removed from active queue and mission cleaned |
| `REG-09` | Save and reload | Save after registration | Registry and dispatch order persist |
| `REG-10` | Special invalid actor | Event 012 excluded special actor qualifies by rank | Excluded or routed according to accepted Event 012 rule |

## Strength

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `STR-01` | Weak army and industry | Small fragmented Africa | Strength stays in limited band |
| `STR-02` | Large unsupplied army | Many divisions with poor equipment and logistics | Strength remains below a supplied equivalent |
| `STR-03` | Continental industrial power | Broad control, strong industry, supply, air, and navy | Strength reaches global or extreme band |
| `STR-04` | High Chaos only | Weak Africa at World Collapse Chaos | Chaos does not lift Strength to extreme by itself |
| `STR-05` | Capital loss | Africa loses main institutional capital | Strength falls materially |
| `STR-06` | Continental liberation | Africa secures major Event 012 state groups | Strength rises after confirmation |
| `STR-07` | Severe surrender pressure | Africa nears capitulation | Strength falls quickly |
| `STR-08` | Ordinary daily fluctuation | Small factory or division changes | Value does not oscillate excessively |
| `STR-09` | One owner calculation | Inspect runtime scope | No per-participant full Strength recalculation |
| `STR-10` | Band persistence | Save at threshold | Value and band remain consistent after reload |

## Wrath and hidden history

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `WRA-01` | Full compliance | Pay standard demand | Wrath falls once and hidden compliance rises |
| `WRA-02` | Direct refusal | Refuse valid standard demand | Wrath rises once and refusal history updates |
| `WRA-03` | Deadline failure | Let mission expire | Wrath rises once and punishment evaluates once |
| `WRA-04` | Broken transfer | Commit then invalidate promised payment | Larger Wrath gain and broken-agreement mark |
| `WRA-05` | Voluntary emergency aid | Send meaningful aid during real African crisis | Wrath falls and exceptional positive mark records |
| `WRA-06` | Tiny aid farming | Repeat low-value offers | No repeated hidden relationship farming |
| `WRA-07` | Active war floor | Pay tribute while still at war | Wrath does not fall below war floor |
| `WRA-08` | Occupation floor | Hold African core territory and comply | Wrath remains above occupation floor |
| `WRA-09` | Participant isolation | Player A refuses, Player B complies | Each Wrath changes independently |
| `WRA-10` | Last-minute payment | Hostile participant pays once before final settlement | Permanent history prevents automatic Favored outcome |

## Demand generation

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `DEM-01` | One active demand | Participant already has active contract | No second ordinary demand is created |
| `DEM-02` | Invalid family | Target has no aircraft or compatible transfer path | Aircraft family receives zero validity |
| `DEM-03` | African surplus | Africa has excessive rifles and lacks fuel | Fuel weight rises and rifle demand is suppressed |
| `DEM-04` | Target hardship | Target is near capitulation with empty reserves | Demand is delayed, reduced, or moved to valid nonmaterial family |
| `DEM-05` | Strong target | Industrial great power with large surplus | Demand scales above weak-major amount |
| `DEM-06` | Protected floor | Payment would breach operating reserve | Normal demand amount is clamped or family rejected |
| `DEM-07` | Punitive floor pressure | High Wrath and high Strength | Demand may approach reserve floor but remains explicit and valid |
| `DEM-08` | Equipment amount rounding | Calculated amount is fractional | Final amount rounds to readable whole step |
| `DEM-09` | Deadline differentiation | Compare ceremonial, equipment, and withdrawal demands | Durations differ by action and logistics |
| `DEM-10` | Recent family repetition | Same family fired recently | Weight is reduced unless African need strongly requires repetition |
| `DEM-11` | DLC absent | DLC-specific mechanic unavailable | Base-game route remains or family is safely excluded |
| `DEM-12` | Subject restrictions | Target cannot perform requested diplomacy | Invalid diplomatic demand is excluded |
| `DEM-13` | Territorial precision | Target controls several African cores | Demand names exact states or clear state group |
| `DEM-14` | Active war | Target at war with Africa | Ordinary demand pauses and wartime route takes over |
| `DEM-15` | Multiplayer dispatch | Several human participants qualify same day | Demands are staggered and do not produce one-day popup storm |

## Payment and negotiation

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `PAY-01` | Exact material transfer | Pay equipment demand | Target debited once and Africa credited same amount |
| `PAY-02` | Click-time capacity change | Spend stockpile before clicking fulfill | Action blocks or recalculates safely without negative stockpile exploit |
| `PAY-03` | Partial payment | Pay first tranche | Remaining amount persists and only remainder is due |
| `PAY-04` | Reload partial contract | Save after partial payment | Family, amount, paid total, and deadline persist |
| `PAY-05` | Substitute set frozen | Open substitute offers, reload | Same valid offers remain |
| `PAY-06` | Valuable substitute | Offer family Africa needs at equivalent burden | Acceptance weight is high |
| `PAY-07` | Useless substitute | Offer obsolete surplus Africa does not need | Acceptance weight is low or zero |
| `PAY-08` | Extension accepted | Low Wrath and good history | Deadline changes once with declared burden |
| `PAY-09` | Repeated extension | Extension already used | Second ordinary request is blocked |
| `PAY-10` | Stale contract click | Old decision remains after new contract | Contract identity prevents wrong demand resolution |

## Punishment ceiling

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `PUN-01` | Weak Africa, maximum Wrath | Strength below 20, Wrath 100 | Applied punishment cannot exceed Tier I |
| `PUN-02` | Regional Africa, maximum Wrath | Strength 20 to 39 | Applied punishment cannot exceed Tier II |
| `PUN-03` | Continental Africa, maximum Wrath | Strength 40 to 59 | Applied punishment cannot exceed Tier III |
| `PUN-04` | Global Africa, high Wrath | Strength 60 to 79 | Tier IV possible only with escalation proof |
| `PUN-05` | Extreme Africa, low Wrath | Strength above 80, Wrath low | Extreme punishment does not occur |
| `PUN-06` | First ordinary refusal | High Strength, no prior offense | Tier IV and Tier V blocked |
| `PUN-07` | Repeated serious failure | High Strength, high Wrath, repeated failures | Escalation reaches higher valid tier |
| `PUN-08` | Tier V full gate | Extreme Strength, very high Wrath, high Chaos, major offense | Emergency ultimatum sequence becomes eligible |
| `PUN-09` | Tier V missing Chaos | Same setup with low Chaos | Tier V blocked |
| `PUN-10` | Tier V Africa collapsing | Same setup with Africa near defeat | Tier V blocked |
| `PUN-11` | Recent extreme cooldown | Target recently suffered Tier V | New Tier V blocked |
| `PUN-12` | Family repetition | Recent disaster family already used | Selector prefers another valid family |
| `PUN-13` | Target near capitulation | Valid high-tier intent against collapsing target | Effect scales to meaningful nonduplicate damage unless extreme route explicitly qualifies |
| `PUN-14` | Punishment reroll attempt | Save before result and reload | Committed result does not reroll |
| `PUN-15` | Failed manifestation | Disaster gateway rejects call | No direct disaster is applied and fallback stays inside current tier |

## Shared-system integration

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `SYS-01` | Event 013 gateway | Valid natural disaster punishment | Owner passes valid inputs and consumes returned proof |
| `SYS-02` | Event 013 rejection | Invalid target or input | Call fails closed with no queued disaster work |
| `SYS-03` | Exact population loss | Extreme punishment wave | State population falls by applied amount and protected floor remains |
| `SYS-04` | Recruitable manpower reconciliation | Apply state civilian loss | No unintended positive manpower credit remains |
| `SYS-05` | Deaths entry | Apply population loss | Deaths logs exact applied amount once |
| `SYS-06` | Chaos duplication | Deaths and disaster already produce Chaos | Gods system does not add the same generic source again |
| `SYS-07` | Migration handoff | Punishment creates proven displacement | Migration receives valid request and does not debit same people again |
| `SYS-08` | Famine handoff | Punishment damages food security | Famine receives valid incident without duplicate event-pool entry |
| `SYS-09` | Condemnation | Direct attributable African atrocity or CBRN action | Existing Condemnation rules apply |
| `SYS-10` | Ambiguous disaster | No proof of African action | Africa does not receive automatic condemnation |

## Protection and reciprocity

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `PRO-01` | Reliable partner | Low Wrath and strong positive history | Protection can become available |
| `PRO-02` | Defiant target | Permanent defiance | Normal protection blocked |
| `PRO-03` | Weak Africa | Partner needs large aid, Africa lacks capacity | Aid scales down or uses diplomatic route |
| `PRO-04` | Strong Africa | Favored partner in major war | Large valid aid or expeditionary support possible |
| `PRO-05` | Disaster mitigation | Reliable partner faces Event 013 disaster | Accepted mitigation or reconstruction API is used |
| `PRO-06` | Real African cost | Africa protects a partner | Africa loses the committed resources or units |
| `PRO-07` | Protection cooldown | Same partner recently helped | Repeated aid is delayed |
| `PRO-08` | Abuse by Africa | Reciprocal doctrine repeatedly punishes compliant partner | AI and hidden relationship reflect doctrine breach or design audit flags imbalance |

## Defiance and reconciliation

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `DEF-01` | Declare defiance | Valid participant confirms action | Ordinary demands stop and high Wrath floor applies |
| `DEF-02` | Punishment after defiance | Defiant participant at high Wrath | Punishment review continues within Strength ceiling |
| `DEF-03` | Demand leakage | Defiant participant reaches cooldown | No ordinary demand is created |
| `DEF-04` | Defensive decisions | Defiant participant faces sabotage risk | Relevant preparation actions appear with real costs |
| `DEF-05` | Cheap reversal attempt | Defiant participant seeks normal demand route immediately | Reentry blocked |
| `DEF-06` | Reconciliation prerequisites | War ended, land returned, political change, reparations ready | Reconciliation mission can begin |
| `DEF-07` | Reconciliation completion | Complete full settlement | Ordinary participation resumes at high manageable Wrath with prior-defiance mark |
| `DEF-08` | Reconciliation failure | Miss settlement deadline | Defiance remains and Wrath rises or floor persists |

## War and defeat

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `WAR-01` | War begins during demand | Active demand then war with Africa | Ordinary contract pauses, converts, or cancels once according to family |
| `WAR-02` | Territory occupation | Participant takes African core | Wrath floor and offender proof apply |
| `WAR-03` | Territory returned | Participant returns all demanded states | Large Wrath reduction and positive history mark |
| `WAR-04` | Participant capitulates Africa | Participant is victor | Gods system ends for victor and pending punishment stops |
| `WAR-05` | Africa destroyed globally | Unifier ceases to exist | System ends for all participants |
| `WAR-06` | African successor survives | Event 012 valid successor exists | Normal authority does not automatically return without re-legitimation |
| `WAR-07` | African restoration | Authorized Event 012 restoration completes | New generation initializes without stale active contracts |

## Final settlement

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `FIN-01` | Secured continent | Event 012 victory proof commits | New demands stop and active contracts cancel |
| `FIN-02` | Favored | Long compliance, voluntary aid, no disqualifier | Major reciprocal settlement |
| `FIN-03` | Respected | Mixed but cooperative history | Limited cooperation settlement |
| `FIN-04` | Distrusted | Inconsistent history without major enmity | Little or no reward and remembered suspicion |
| `FIN-05` | Enemy | War, occupation, betrayal, or permanent defiance | Hostile settlement and exclusion routes |
| `FIN-06` | Last-minute payment | Major hostile history followed by one payment | Outcome does not jump to Favored |
| `FIN-07` | World Is One input | Final relationship then World Is One route | Invitations and resistance use stored outcome |
| `FIN-08` | Save after settlement | Reload final state | Demands do not restart |

## Focus and decision presentation

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `UI-01` | Two-value limit | Inspect every Gods surface | No third public meter or numeric loyalty display |
| `UI-02` | No active demand phase | Open participant category | Only relevant relationship and preparation actions appear |
| `UI-03` | Active demand phase | Open category during demand | Up to five primary actions and one mission |
| `UI-04` | Negotiation phase | Open substitute selection | Up to three offers and one return action |
| `UI-05` | Defiance phase | Declare defiance | Demand actions replaced by relevant defensive actions |
| `UI-06` | Meter clarity | Inspect Strength and Wrath | Value, band, trend, threshold, and concise cause tooltip are clear |
| `UI-07` | Blocked action | Lack required material | Exact amount and correct texticon appear in blocked state |
| `UI-08` | Selected target | Africa selects participant | Only valid target actions appear and stale selection clears |
| `UI-09` | Category clutter | Inspect every phase | No more than six primary actions and normally three to five |
| `UI-10` | No fake controls | Inspect category picture | Art contains no fake buttons, meters, or readable text |

## AI and probability

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `AI-01` | Affordable demand, strong Africa | Cooperative major with surplus | Compliance scores above refusal |
| `AI-02` | Crippling demand, weak Africa | Strong rival with low Wrath | Refusal or substitute scores above compliance |
| `AI-03` | Occupier | Target holds African cores | Defiance and hostility weight increase |
| `AI-04` | Loyal ally | Partner has strong history and common enemy | Compliance and emergency aid dominate |
| `AI-05` | Africa needs fuel | Several valid families | Fuel selection outranks surplus rifle request |
| `AI-06` | Repeated family | Same family recently used | Alternative valid family gains relative weight |
| `AI-07` | Weak Africa punishment | High Wrath | Tier I families are the entire normalized pool |
| `AI-08` | Full Tier V gate | Extreme scenario | Tier V becomes possible but does not become automatic |
| `AI-09` | Protect useful partner | Strong positive history and real African capacity | Protection target ranks above neutral participant |
| `AI-10` | Avoid self-destruction | Africa near collapse | AI prioritizes emergency aid and pauses broad escalation |

## Assets, logs, and documentation

| ID | Scenario | Setup | Required result |
| --- | --- | --- | --- |
| `DOC-01` | Event 012 docs | Inspect public docs | Gods system described under Event 012 |
| `DOC-02` | Event 070 catalog | Inspect authoritative XLSX | Old Gods assignment removed and ID remains available |
| `DOC-03` | CSV export | Save workbook | Export script updates all three CSV snapshots |
| `DOC-04` | Event Log volume | Run several demand cycles | Routine payments do not flood global history |
| `DOC-05` | Major milestone log | Trigger activation or Tier V | Event 012 milestone appears with correct actor context |
| `DOC-06` | Asset coverage | Inspect accepted inventory | Every required asset has final runtime consumer and manifest evidence |
| `DOC-07` | Icon separation | Compare focus, idea, and decision art | No icon family is satisfied by simple resizing of another type |
| `DOC-08` | Cultural review | Inspect art and text | No false universal African pantheon or decontextualized sacred collage |
| `DOC-09` | Super-event threshold | Activate weak system | Normal news appears and super-event waits for credibility threshold |
| `DOC-10` | Super-event package | Reach threshold | Unique image, sourced quote, licensed music, and settings-aware audio align |

## Completion rule

A failed case blocks completion when it affects:

- Event 012 ownership
- Event 070 release
- the two-value limit
- real tribute transfer
- demand validity
- punishment ceiling
- participant isolation
- exact population accounting
- final settlement
- AI validity
- required assets
- required documentation or workbook alignment

A blocked tool route must be reported by name with the missing evidence. It cannot be treated as a pass.
