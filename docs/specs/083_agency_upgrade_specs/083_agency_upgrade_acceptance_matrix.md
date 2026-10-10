# Event 83 acceptance matrix

These are implementation acceptance conditions. The accompanying model report states separately which semantic cases were exercised outside the game. Nothing in this matrix is marked as an in-game pass by this planning package.

| Test ID | Case | Required observation |
| --- | --- | --- |
| U01 | Agency absent, baseline | Agency created first, then one real upgrade or conversion, one permanent slot, and one immediately recruitable operative |
| U02 | Agency absent, Intelligence States | Full five-part award after creation, with all five fixed temporary benefits |
| U03 | Agency already exists | Name, emblem, existing upgrades, and existing operatives preserved |
| U04 | Package boundaries | 199/200, 399/400, and 599/600 use the correct package |
| U05 | Package isolation | A five package is not a twelve package |
| U06 | Independent evolution controls | Highest enabled qualifying evolution selected, including skipped lower disabled evolutions |
| U07 | Threshold crossed by own Chaos | The same firing retains its pre-award package |
| U08 | Delayed report acknowledgment | No later package, reroll, or additional award |
| U09 | Complete upgrade registry | Every effective valid purchase increment represented, with country, feature, prerequisite, and level rules |
| U10 | Successive upgrade draws | Owned and newly granted increments excluded, newly unlocked successors eligible |
| U11 | Two remaining upgrades at III | Exactly two grants and three conversions, plus the guaranteed package |
| U12 | Exhaustion at each tier | Every otherwise missing roll converts at 1, 2, 3, and 5 |
| U13 | Registry mismatch or failed grant | Report a failure, never misclassify as a completed tree |
| U14 | Under-construction award | Correct completed level and released future commitment, without invented refunds |
| U15 | Native upgrade milestones | Native additional rewards remain additional to the explicit Event 83 package |
| R01 | Five instant recruits | Human can claim all five without successive native recruitment waits |
| R02 | Existing candidate opportunities | Existing normal recruits and cooldown progress are not consumed or damaged |
| R03 | Repeated unclaimed recruits | Distinct claims accumulate without duplication, replacement, or a hidden cap |
| R04 | Conversion slot | One capacity added, no unauthorized extra immediate recruit |
| R05 | Other capacity owners | Removing or adding another owner's capacity does not overwrite Event 83's contribution |
| R06 | AI recipient | Receives and can claim the same personnel package |
| B01 | Evolution II specialty | One usable family, correct value and 180-day clock |
| B02 | Exhausted roll | Each exhausted roll adds exactly one permanent slot and no recruit |
| B03 | Repeat stacking | A second firing's 180-day grants add to the first and expire on their own clock |
| B04 | Intelligence States suite | +50/+50/+25/+25/+25 percentages applied to the intended five native quantities |
| B05 | Preparation speed | Changes preparation rate, not construction time, cost, or operation execution duration |
| B06 | Counter-intelligence | True percentage behavior, including a changed native base, with no self-amplifying feedback |
| B07 | Encryption with agency system | Actual agency-era protection changes, no inactive legacy substitution |
| B08 | Mixed 90/180-day grants | Exact independent expirations and permanent capacity retained |
| B09 | Staggered repeats | Older clocks unchanged, new grants keep their own deadlines |
| B10 | Foreign modifier owner | Another event's benefits survive Event 83 expiration |
| C01 | Country coverage | Majors, minors, subjects, humans, AI, and supported active exiles receive the same package size |
| C02 | Recipient isolation | Another country's agency, rolls, personnel, and receipt are never modified through wrong scope |
| C03 | Country identity changes | Cosmetic or government change preserves identity, annexation does not transfer rewards to conqueror |
| C04 | Multiplayer | Single host-authoritative award, consistent save state, no client-local reward rolls |
| C05 | Idempotence | Duplicate recipient, history, expiry, and acknowledgment callbacks do not duplicate or subtract rewards twice |
| C06 | Save and reload | Claims, package identity, expiry dates, achievement state, and once-per-firing guards preserved |
| C07 | Unsupported capabilities | Preflight failure does not silently award substitutes or consume the incident |
| C08 | Cluster identity | Intelligence uses ID 20 from the central ledger linked in Part 1; Diseases retains ID 8, with no membership or behavior change implied by identity alignment |
| C09 | Cluster lifecycle | Incident counted once, member-specific once/repeatable rules preserved |
| C10 | Chaos ownership | +5 once per committed worldwide firing, no per-country or per-operative multiplication |
| C11 | Cross-event integration | Uses actual current capability, no free leak, purge, or stale expired-bonus contribution |
| A01 | Achievement A1 | All qualifying and disqualifying paths from Part 5 proven with actual operation evidence |
| A02 | Achievement A2 | Exact two-target simultaneous interval, real home assignment, one-attempt operation credit |
| A03 | Test-mode eligibility | Manual and debug reward paths cannot earn either pursuit |
| V01 | Result receipt | Actual upgrades, recruits, conversions, and clocks visible without exposing foreign secret data |
| V02 | Modifier presentation | One tile, correct permanent contribution and independently expiring components |
| V03 | History | Selected package recorded before baseline defaults can overwrite it |
| V04 | Assets | Eight final DDS files, native dimensions, alpha, sprite bindings, and live consumers validated |
| V05 | Localisation | Final text follows direction, premise-only Details, exact mechanics in tooltips, no key leaks |
| G01 | Required independent review | Actual probability audit and improvement-loop handoff, with dispositions and evidence |
| G02 | Feature and live-game completion | Installed feature matrix resolved and user-supplied live evidence reviewed under project rules |
