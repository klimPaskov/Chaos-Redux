# Law Upgrade: acceptance matrix

Every case below is **planned, not executed in HOI4**. The supplemental arithmetic model tests only abstract rules and cannot mark these integration cases passed.

Record game build, repository revision, actual loaded DLC/mod set, fixture, observed result, logs, and relevant live evidence for each executed case. Static inspection, pure arithmetic, and live engine proof must remain separate evidence classes. The user retains control over launching and validating the game.

| ID | Fixture | Required result |
| --- | --- | --- |
| F01 | Baseline, low laws, support 20% | Economy +1, conscription +1, support 30%, trade unchanged |
| F02 | Baseline, economy at cap, conscription below cap | Economy unchanged, conscription +1, no replacement PP |
| F03 | Every participating category capped and support 100% | No new law, PP, manpower, equipment, or overflow reward |
| F04 | I active, support 20% | Exactly +25 pp, not +35 pp, all I categories visited once |
| F05 | II active, support 20% | Exactly +50 pp, not +85 pp, prior categories still one step |
| F06 | III active, both ordinary caps | Both extreme endpoints entered, +50 pp once |
| F07 | III active, each family one below ordinary cap | Advance to ordinary caps only, no extreme in same firing |
| F08 | III active, economy capped, conscription two steps below cap | Enter economy extreme, conscription only +1 |
| F09 | Two registered aliases for the same category | Only one actual change |
| F10 | Country at 80% support under III | Support becomes 100%, no stored overflow |
| F11 | Human leaves notification open | Changes already applied, no second change on acknowledgment |
| F12 | Several simultaneous human recipients | One world selection, consistent profile and snapshot |
| F13 | Two legitimate separate firing tickets on the same day | Two legitimate waves, each once, not falsely coalesced |
| F14 | Same firing ticket delivered twice | Second delivery does not change laws or support |
| F15 | Category has unsupported current law | Preserve it, no fake cap result, other categories proceed |
| F16 | Ordinary political purchase gates fail | Forced step still occurs |
| F17 | Required institution or DLC absent | That category does not materialize, other results unaffected |
| F18 | One category's step unlocks another's structural prerequisite | No within-firing cascade from changed prerequisites |
| E01 | Chaos 199/200, 599/600, 799/800 | Correct eligibility boundaries, no law change merely at crossing |
| E02 | Previously unfired Event 82, Chaos 850 | Highest enabled eligible opening profile, still one step |
| E03 | Already-running lifecycle crosses threshold | Uses shared dynamic timing, not immediate automatic activation |
| E04 | Active evolution followed by lower Chaos | History retained, no automatic law reversal |
| E05 | Disabled lower evolution | Higher dependent profiles do not apply |
| E06 | Disable and re-enable event or evolution | No replayed activation, exits and current penalties remain correct |
| E07 | Evolution activates without a firing | Zero War Support grant, zero law steps, zero activation Chaos |
| L01 | Economy extreme, at war, without conscription extreme | Full replacement law payload, no old Total Mobilization residue |
| L02 | Economy extreme enters peace | War benefits inactive, continuing civilian penalties remain |
| L03 | Economy extreme and consumer-goods modifiers/floors | 1% law baseline represented as intended, actual allocation honestly displayed, no global-floor mutation |
| L04 | Conscription extreme with no other recruitment effects | 99% legal law setting, ordinary mobilization, no instant grant |
| L05 | Conscription extreme with positive recruitment bonuses | Legal ceiling not above 99%, no duplicated population |
| L06 | Conscription extreme with noncore, subject, or occupation restrictions | Existing population permissions preserved |
| L07 | Conscription entry, exit, and re-entry after casualties | No resurrection or repeat grant |
| L08 | Exit conscription with already-deployed troops | No Event 82 forced disband or death, native reserves reconcile |
| L09 | Both laws, support 0/25/50/75/100 | Formula and combined table match their owned contributions |
| L10 | Support drops after extreme entry | Penalties worsen within required refresh bound, not entry-locked |
| L11 | Support rises after extreme entry | Penalties improve monotonically but remain severe |
| L12 | Repeated effect refresh | No repeated Stability loss, growth mutation, or duplicate carriers |
| L13 | Unrelated national bonus also active | Event 82 combines only its own terms, unrelated contribution preserved |
| L14 | Remove only one extreme law | Only its contribution disappears, remaining law refreshes correctly |
| L15 | Baseline normal nation, both laws, optional PP spending stopped | A viable saving route exists, no Event 82 permanent income lock |
| C01 | Ordinary adjacent price 150 | Exit quote and debit 300 |
| C02 | Ordinary discounted adjacent price 75 | Exit quote and debit 150, no second discount |
| C03 | Ordinary resolved price 113 | Exit quote and debit 226, not 225 |
| C04 | Ordinary price legitimately zero | Exit price zero, no artificial minimum after doubling zero |
| C05 | PP one point below full exit quote | No partial debit and no law change |
| C06 | Exactly enough PP | One successful debit, correct predecessor restored |
| C07 | Discount or cost modifier changes before confirmation | Fresh accepted quote matches current debit |
| C08 | Both reversals clicked in succession | Independent quotes and affordability, no free second exit |
| C09 | Attempt direct native selection below extreme | No cheaper bypass and no skip of required predecessor |
| C10 | Voluntary extreme entry at peace or below 80% support | Unavailable through ordinary purchase |
| C11 | Voluntary extreme entry at war, support 80%, immediate predecessor | Ordinary one-step price, same law effects as forced entry |
| C12 | Forced demobilization, annexation, or inheritance | No hidden manual exit charge |
| C13 | Price provider cannot prove native current price | Explicit implementation blocker, not hardcoded substitute |
| S01 | Country created after start-of-firing snapshot | No retroactive grant, included at next firing |
| S02 | Annexed dormant tag | No new country or artificial law installation |
| S03 | Existing subject or government in exile | Participates through actual available categories |
| S04 | Human unusual country and true nonhuman country | No blanket unusual-tag exclusion, no human institution invented |
| S05 | Civil war inheritance | Correct law effects, no replayed world support gain |
| S06 | Save and reload while holding both laws | Same current law effects, prices, achievement history, one-shot records |
| S07 | Tag transformation during extreme-law tenure | Owner identity and penalty reconciliation preserved |
| S08 | Pre-rework save with a pending legacy report | No duplicate event effect or accidental PP cap reward |
| S09 | Hotjoin or repeated multiplayer notification delivery | No duplicate world ticket, grants, or achievements |
| K01 | First real law advance | One +5 Chaos milestone |
| K02 | First Event 82 Closed Economy entry | One +5 Chaos milestone |
| K03 | First entry into each extreme family, many countries same wave | One +5 per family globally, not per country |
| K04 | Repeated entry, capped firing, activation, or reload | No repeated milestone award |
| K05 | Last genuine demobilization followed by 30 days without holders | One eligible -5 family recovery |
| K06 | Last holder annexed, or holder returns before 30 days | No successful recovery credit |
| K07 | War, annexation, deaths, or contamination caused elsewhere | No duplicate generic Chaos accounting |
| A01 | Defined AI scenario matrix and full candidate pool | Inspector-backed results, no score-as-probability claims |
| A02 | AI saving and unchanged-state entry/exit behavior | No avoidable spending starvation or immediate contradictory purchase loop |
| H01 | Achievement A full valid and one-condition-short paths | Only actual qualifying survival plus victory awards |
| H02 | Achievement B equipment recovery and mass-disband attempt | Valid retained-force recovery awards, disband shortcut does not |
| H03 | Achievement C both paid exits and 90-day civilian recovery | Forced removal alone cannot satisfy paid history |
| H04 | Debug fixture or console setup | No normal campaign achievement award |
| V01 | Four applied report profiles and unchanged/capped outcomes | Artwork, actual results, and text direction agree |
| V02 | Two law and reversal tooltips | Current effects and accepted price match actual mechanics |
| V03 | 17 planned final assets | Correct consumers, sizes, states, sprites, alpha, and manifests |
| V04 | Event Details, logs, and event/cluster catalog | Correct scope, role, names, no numeric Details bloat or duplicate firing |
| V05 | Clean and altered UI scale, long localization values | No clipping, misleading truncation, or unreadable price |

## Required installed-game evidence

The first release must include a no-DLC core fixture, representative country-specific replacement-law fixtures, each actually supported DLC family, and an unsupported-owner negative fixture. Do not claim exhaustive DLC support from a sample. Record all installed eligible families in the compatibility inventory.

Effect proof must inspect actual construction, production, repair, research, Stability, population growth, legal recruitment, reserves, and price behavior. A matching icon or tooltip does not prove these consumers.

Cost evidence must include normal modifiers, active cost sources in different registration orders, fractional ordinary prices, expiry between viewing and clicking, and reload. Population evidence must include deployed troops, unused reserves, positive and negative external recruitment effects, and previously suffered casualties.
