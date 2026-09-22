# Validation matrix

Every row below is pending implementation unless explicitly identified as a planning-package check in the final package report.
The table is not a record of successful gameplay tests.
A source inspection, a static asset render, a probability evaluation, and a live HOI4 run are different forms of evidence.
Record each under its own heading.

| Test | Fixture | Required observation |
| --- | --- | --- |
| V01 | Ireland absent | No event consumption, no assets, no war |
| V02 | Ireland already controls the North | Unavailable even if another country owns it |
| V03 | Ireland already at war with holder | No new attempt or free force for the old war |
| V04 | Ordinary Ireland and Britain | One force grant and real declaration, no refusal civil war |
| V05 | Britain in an unrelated war | Limited peace leaves the unrelated war and ownership unchanged |
| V06 | Britain as faction leader with participating allies | Required supported limited settlement, no faction destruction |
| V07 | Valid non-British holder | Same northern objective and peace, no British-only text or tag gate |
| V08 | Owner and controller differ | Only supported consent and settlement case can commit, otherwise no consumption |
| V09 | Independent northern country loses its final state | Valid transfer and terminal-war handling even if holder ceases to exist |
| V10 | Ireland subject or unable to declare | No accidental independence or force grant |
| V11 | Southern Ireland separately partitioned | Declined under explicit reunification availability interpretation |
| V12 | Irish-owned southern state occupied in unrelated war | Northern objective does not expand to unrelated southern reconquest |
| V13 | Belfast held but part of North not held | Hold timer does not complete |
| V14 | All North held, then one province lost | Five-day continuous timer resets |
| V15 | Ally occupies North | No success until actual qualifying Irish control |
| V16 | Target changes before commitment | Revalidation prevents stale war and resource payment |
| V17 | Target changes during attempt | Safe successor or explicit interruption, no theft from unrelated owner |
| V18 | Qualified objective | Automatic resolution, no paid extra victory click |
| V19 | Settlement effect fails a postcondition | No success marker and no new tree |
| V20 | Day 180 with no victory or extension | Permanent failure, safe exit attempted, true remaining-war status reported |
| V21 | Day 150 extension and exact resources | One 90-day extension, correct payment, no repeat |
| V22 | Ireland capitulates | Failure cleanup, previous tree, surviving normal consequences |
| V23 | Failed event followed by later ordinary northern conquest | New tree remains unavailable |
| V24 | Successful event followed by northern loss | Earned tree remains, territorial capstones pause |
| V25 | All four starting tiers | Correct cumulative entitlement, real equipped formations and separate reserves |
| V26 | Upgrade during war after losses | Only tier difference, losses do not replenish the ledger |
| V27 | Upgrade after success | Additional route capacity, no second opening package |
| V28 | Evolutions disabled | Complete baseline routes, no stage flags falsely completed |
| V29 | Chaos threshold crosses during attempt | Timed shared Evolution behavior, no automatic instant jump |
| V30 | Save/reload at every lifecycle step | No duplicate units, payments, transfer, tree load or presentation |
| V31 | Multiplayer duplicate acknowledgements | Once-only authoritative effects and same outcome for all clients |
| V32 | Existing active Irish focus | Tested progress transition, no duplicate rewards or unexplained progress loss |
| V33 | Advanced Ireland | Existing superior technology and industry preserved |
| V34 | All constitutional paths | Distinct paid consequences and no fourth spirit |
| V35 | Broken promise and later repair | Correct Settlement and charged/reversed Chaos guards |
| V36 | Costs at one below, exact and one above | Identical display, availability and debit behavior |
| V37 | Recipient changes after offer | No stale territory transfer or resource loss |
| V38 | Worksite occupied or capacity lost | Appropriate pause/cancel and release of future capacity |
| V39 | Existing Scotland, Wales or Brittany | No duplicate country, army or replacement of living unique tree |
| V40 | New Celtic release | Coherent capital, country setup, army, economy and independent choices |
| V41 | Human refuses union or federation | Sovereignty preserved and no hidden AI fallback |
| V42 | Empire owns only part of required Scotland | Cannot form, all displays agree |
| V43 | Empire's subject holds Scotland | Cannot substitute subject control for Irish ownership |
| V44 | Full empire formation | Identity, ideas, flags and branches applied once, no blanket foreign cores |
| V45 | Scottish core integration | Both qualifying time and paid work required, only approved states |
| V46 | Federal members own their own states | Member policy qualifies without Irish annexation |
| V47 | Essential federal member withdraws | Shared capacity updates, possible league demotion, no annexation |
| V48 | Optional Brittany unavailable | Complete baseline federation and no impossible required focus |
| V49 | Atlantic access refused | Alternative candidate or domestic long-range route remains usable |
| V50 | Foreign port changes holder | Treaty result updates and no phantom sovereign ownership |
| V51 | Full industrial slots | Predefined visible alternate reward, no repeated building grant |
| V52 | Base game and normal DLC fixtures | Usable equipment, research, ship and aircraft alternatives |
| V53 | Every exact-state category | Correct attachment, live owner/control/core hover and shared eligibility |
| V54 | Required UI resolutions and long text | No clipping, overlap, stale states or fake clickable pieces |
| V55 | Native-size PNG and DDS round trip | Dimensions, alpha, headers and pixel equality match contract |
| V56 | Both super-events | Source-verified final text and licensed audio, once-only trigger |
| V57 | Every achievement | All positive and negative conditions, intervals and provenance proven |
| V58 | Generic and custom Chaos together | No duplicate war, peace, liberation, faction or casualty charge |
| V59 | Repeated treaty breach/reconstitution | Custom Chaos and achievements cannot be farmed |
| V60 | Event 009, 060, 062, 063 and 064 interactions | Relevant actual changes respected without broad immunity or overwrites |

For V05 and V06, include a machine-readable before/after war-relation and territory report plus live evidence.
For V25, include formation equipment totals and final stockpile/personnel values.
For V53 and V54, retain actual map and GUI inspection/render artifact references.
For V57, do not accept a manually set achievement flag as proof of its tracking logic.
