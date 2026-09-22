# Acceptance matrix

Every case below is an acceptance requirement, not a passed result.
All runtime and independent-review statuses are **Not run** in this planning package.
Create reproducible setup notes, version information, observations, screenshots or logs, and pass/fail outcomes under the plans folder during implementation.
Use the debug-playtest skill and current user authority before launching the game or making runtime changes.
Static checks do not stand in for live supply, movement, defender safety, or AI evidence.

| ID | Area | Setup or action | Expected result | Current evidence |
| --- | --- | --- | --- | --- |
| T001 | Eligibility and dispatch | Japan exists, USA exists, bilateral war active | Successful legal preflight can commit the event. | Not run |
| T002 | Eligibility and dispatch | Japan has no effective navy or naval supremacy | The opening remains eligible and does not run a naval-invasion success roll. | Not run |
| T003 | Eligibility and dispatch | Japan has empty national equipment and high surrender progress | The complete promised opening still appears with valid embedded resources. | Not run |
| T004 | Eligibility and dispatch | Japan has capitulated but still exists in the same war | No extra noncapitulation gate is added. Actual native creation/control behavior is proved or reported blocked. | Not run |
| T005 | Eligibility and dispatch | Japan or USA does not exist | No effects, invalid scopes, news, or consumed root. | Not run |
| T006 | Eligibility and dispatch | Bilateral war is absent | No landing and no newly declared war. | Not run |
| T007 | Eligibility and dispatch | Event setting disabled or fire-once already consumed | No second material effect or hidden alternate entry. | Not run |
| T008 | Eligibility and dispatch | Placement becomes invalid before shared dispatch commits | No phantom history, consumed selection, or duplicate timer processing. | Not run |
| T009 | Eligibility and dispatch | Another neutral country owns every legal mainland Pacific candidate | Defer unconsumed without annexation or a nonmainland fallback. | Not run |
| T010 | Eligibility and dispatch | Human closes Japanese acknowledgement late | USA warning and army do not wait, and no material grant is tied to acknowledgement. | Not run |
| T011 | Geography and defenders | California and northern alternatives all legal | Choose a valid California profile first. | Not run |
| T012 | Geography and defenders | California legally unusable, Oregon legal | Use Oregon with correct targets and wording. | Not run |
| T013 | Geography and defenders | Only Washington is legal | Use Washington with no California-specific false report. | Not run |
| T014 | Geography and defenders | Selected province contains American defenders | Preserve defender formations and ownership and prove legal battle or displacement behavior. | Not run |
| T015 | Geography and defenders | Selected state is partially controlled by both sides | Only approved footprint control changes and only qualified support applies. | Not run |
| T016 | Geography and defenders | A neutral or nonhostile ally controls part of a target state | Do not seize that territory or create an unauthorized war. | Not run |
| T017 | Geography and defenders | Japan already controls a valid American coastal pocket | Reinforce legally without repeated new-front Chaos when an established front already exists. | Not run |
| T018 | Geography and defenders | Tier III has only one legal large profile | Issue the full authorized immediate force, prove capacity, and keep the multi-region super-event gate unmet. | Not run |
| T019 | Geography and defenders | Several initial profiles are used | All simultaneous entry points belong to one episode and have legal distributed deployment. | Not run |
| T020 | Geography and defenders | Map IDs differ from legacy state 378 | Use verified current profiles or report blocked, never assume the legacy ID proves geography. | Not run |
| T021 | Army and accounting | Baseline factor 1.00 | Create 30 immediate divisions and reserve a lifetime total of 40. | Not run |
| T022 | Army and accounting | Tier I factor 1.00 | Create 60 immediate divisions with a lifetime ceiling of 75. | Not run |
| T023 | Army and accounting | Tier II factor 1.00 | Create 100 immediate divisions with a lifetime ceiling of 125. | Not run |
| T024 | Army and accounting | Tier III factor 1.00 | Create 150 immediate divisions with a lifetime ceiling of 180. | Not run |
| T025 | Army and accounting | Every factor step 1.00 through 1.50 | Round immediate and lifetime totals coherently and conserve role batches. | Not run |
| T026 | Army and accounting | USA division counts just around 100 and each subsequent 50 | The frozen factor changes only at the defined complete threshold and never exceeds 1.50. | Not run |
| T027 | Army and accounting | USA raises divisions or Japan loses units after landing | No factor reroll and no replacement entitlement from losses. | Not run |
| T028 | Army and accounting | Native create_unit consumes stockpile or supplies embedded resources | Grant compensation only for actual native debit, never a duplicated formation manifest. | Not run |
| T029 | Army and accounting | Requested division equipment is unavailable to low-tech Japan | Use the verified ordinary grant profile or mark the capability blocked, never create empty formations. | Not run |
| T030 | Army and accounting | No suitable named commander is available | No clone or resurrection and no missing army. Use valid ordinary command behavior. | Not run |
| T031 | Army and accounting | High-tier aircraft exceed local airfield capacity | Deploy only safe usable wings and label remaining aircraft as national reserves. | Not run |
| T032 | Army and accounting | Aircraft designer DLC is enabled and disabled | All issued aircraft have valid equipment and mission-capable configurations. | Not run |
| T033 | Army and accounting | National stocks are diverted to another front | Do not claim local ring-fencing or refill consumed resources automatically. | Not run |
| T034 | Army and accounting | Opening and delayed loose-reserve lots are issued | Total cumulative issue never exceeds the tier allowance after rounding. | Not run |
| T035 | Supply and reinforcement | Japan has no working trans-Pacific supply route | The immediate army is supplied by the validated finite opening preparation. | Not run |
| T036 | Supply and reinforcement | Large tier III force is distributed across valid profiles | Measured capacity supports the formation demand without severe designed-in overcrowding. | Not run |
| T037 | Supply and reinforcement | American troops remain in a partially Japanese-controlled state | They do not receive the event-owned Japanese supply contribution. | Not run |
| T038 | Supply and reinforcement | Principal port is damaged after landing | Damage remains meaningful and no recurring maximum-level repair runs. | Not run |
| T039 | Supply and reinforcement | One pocket loses access while another survives | Pause only affected deliveries and taper the isolated pocket correctly. | Not run |
| T040 | Supply and reinforcement | All access lost for 7 days | Local taper and blocked deliveries match the stated clock. | Not run |
| T041 | Supply and reinforcement | Access restored on day 29 of continuous loss | Resume only unused support before its original absolute expiry. | Not run |
| T042 | Supply and reinforcement | All access lost for 30 continuous days | Special support closes permanently and pending grant lots expire. | Not run |
| T043 | Supply and reinforcement | A port is retaken after permanent support closure | Normal supply can operate but no free support, evolution or scripted army restarts. | Not run |
| T044 | Supply and reinforcement | Support reaches day 180, 240, 300 or 360 for its tier | Exceptional benefits end at the correct absolute episode age. | Not run |
| T045 | Supply and reinforcement | J01 is requested normally or through J-M1 acceleration | The 30-day cadence and single 15-day exception apply without overlapping batches. | Not run |
| T046 | Supply and reinforcement | A delayed reserve lot becomes due without access | It stays pending only while support remains open and never issues twice. | Not run |
| T047 | Supply and reinforcement | Late active evolution raises material allowance | Issue cumulative due minus actual issued, not a fresh complete reserve package. | Not run |
| T048 | Supply and reinforcement | Special support expires while Japan holds an operating front | Ordinary campaign, paid operations and appropriate AI priority can continue. | Not run |
| T049 | Decisions and missions | Each of the nine action families is purchased | Displayed, affordable, reserved and debited costs match, with at most four spendable types. | Not run |
| T050 | Decisions and missions | J01 or U01 is canceled before valid deployment | Refund the exact recorded reservation once and create no units. | Not run |
| T051 | Decisions and missions | A completed J01 or U01 batch is destroyed | No refund, replay or replacement grant. | Not run |
| T052 | Decisions and missions | A paid field project loses its target after work starts | Cost remains spent and enemy territory receives no completion benefit. | Not run |
| T053 | Decisions and missions | Cost modifiers change during a reserved operation | Refund the historical payment and never recompute it under the new modifier. | Not run |
| T054 | Decisions and missions | U01 assembly becomes hostile during its 20-day organization | Bounded legal reselection or exact cancellation refund, with no spawn in enemy territory. | Not run |
| T055 | Decisions and missions | A repaired port is damaged again | Its one emergency-completion receipt remains and ordinary repair is required. | Not run |
| T056 | Decisions and missions | J03 or U03 route contains a hostile gap | No through-enemy construction or false connection. | Not run |
| T057 | Decisions and missions | J04 and U04 overlap repeatedly | Only the permitted local operation applies and no global or stacked benefit appears. | Not run |
| T058 | Decisions and missions | J-M1 or U-M1 grants early access | Only a waiting date is removed, no extra project, batch or resource ceiling is created. | Not run |
| T059 | Decisions and missions | A continuous-hold objective is lost near completion | The hold resets without moving the absolute deadline. | Not run |
| T060 | Decisions and missions | J-M3 continues after special supply expires | It can complete through ordinary fighting, with no revival of expired grant rewards. | Not run |
| T061 | Decisions and missions | High-tier detached pockets exist | Japan shows at most two simultaneous missions and connecting them requires actual land control. | Not run |
| T062 | Decisions and missions | U-M2 deadline changes through an active evolution | Use the higher absolute deadline from the original landing date. | Not run |
| T063 | Decisions and missions | A mission target is externally invalidated | Report cancellation or reselection distinctly from military failure, with no free success. | Not run |
| T064 | Evolutions and cleanup | Starting Chaos is 199, 200, 399, 400, 599 or 600 | Select the highest enabled eligible starting tier exactly. | Not run |
| T065 | Evolutions and cleanup | A lower stage is disabled but a higher stage is enabled | Higher eligible opening works without lower-stage grants or history. | Not run |
| T066 | Evolutions and cleanup | Chaos jumps from below 200 to above 600 during support | Only the next enabled active stage is eligible and upgrades do not burst in one update. | Not run |
| T067 | Evolutions and cleanup | Chaos falls below a pending stage threshold | Pause eligible timing and do not erase completed stages. | Not run |
| T068 | Evolutions and cleanup | Units are lost before an upgrade | Grant only the positive cumulative entitlement difference. | Not run |
| T069 | Evolutions and cleanup | Support is permanently closed before upgrade | No active evolution occurs even if Chaos rises. | Not run |
| T070 | Evolutions and cleanup | Japan ceases to exist | No revived tag, invalid callbacks, new armies or invented exile state. | Not run |
| T071 | Evolutions and cleanup | USA capitulates in the existing war | Use the native result and do not launch a scripted peace treaty. | Not run |
| T072 | Evolutions and cleanup | Bilateral war ends, then restarts | Respect settlement and do not reopen the fire-once landing or support. | Not run |
| T073 | Evolutions and cleanup | Cleanup overlaps another event on the same state | Remove only Event 074 contributions and preserve unrelated systems. | Not run |
| T074 | Evolutions and cleanup | Support ends but a later achievement remains possible | Keep bounded required achievement tracking without preserving expired grants. | Not run |
| T075 | Chaos, presentation and achievements | Initial landing creates a genuinely new theater | Credit only the appropriate initial-front pressure once. | Not run |
| T076 | Chaos, presentation and achievements | A shared war, army-buildup, annexation or deaths source also fires | No duplicate event-owned payment for that same generic source. | Not run |
| T077 | Chaos, presentation and achievements | Territorial milestone is captured, recovered and recaptured | One positive credit, one bounded reversal and no recapture farming. | Not run |
| T078 | Chaos, presentation and achievements | Neutral occupation removes Japanese control | Do not describe it as American recovery or pay an unsupported recovery reversal. | Not run |
| T079 | Chaos, presentation and achievements | Reports fire during an Oregon or Washington fallback | Names, art directions and quantities describe the actual operation. | Not run |
| T080 | Chaos, presentation and achievements | Tier III is selected with insufficient realized geography or issue | No premature super-event. | Not run |
| T081 | Chaos, presentation and achievements | The realized multi-region tier III gate becomes true twice | One researched super-event and no replay after reload. | Not run |
| T082 | Chaos, presentation and achievements | Any achievement is tested only by initial free territory | Compound normal-conquest and hold conditions prevent trivial unlocks. | Not run |
| T083 | Chaos, presentation and achievements | A03 recovery occurs after day 240 | Do not unlock its time-limited achievement. | Not run |
| T084 | Chaos, presentation and achievements | A04 recovery is followed by direct control of the original Japanese capital | Unlock only within 730 days and continuing-war requirements. | Not run |
| T085 | Chaos, presentation and achievements | A05 expedition is isolated, support closes, then it reconnects normally | Use both hold durations and the 60-day recovery window without a new landing. | Not run |
| T086 | Chaos, presentation and achievements | Final art and achievement states are exported | Verify actual DDS bytes, size, alpha, templates, consumer paths and provenance. | Not run |
| T087 | Save, multiplayer and AI | Save reload immediately before and after commitment | Exactly one opening and one history record. | Not run |
| T088 | Save, multiplayer and AI | Save reload during reservation, reserve-lot wait, hold timer or evolution | Persistent receipts and dates reconcile without repeated effects. | Not run |
| T089 | Save, multiplayer and AI | Japan and USA are controlled by different human players | Both receive timely truthful reports and neither acknowledgement gates the other. | Not run |
| T090 | Save, multiplayer and AI | Shared versus independent multiplayer event mode | One global landing episode and correct shared framework selection behavior. | Not run |
| T091 | Save, multiplayer and AI | AI country becomes human or human becomes AI | No overwritten human orders, repeated grants or frozen cost recalculation. | Not run |
| T092 | Save, multiplayer and AI | Observe Japanese AI on days 1, 3, 7, 30 and 90 | Useful orders, supply-aware operations and no systematic return of the new army to Asia. | Not run |
| T093 | Save, multiplayer and AI | Observe USA with a distant major war | Mainland urgency rises without a scripted global force teleport. | Not run |
| T094 | Save, multiplayer and AI | Run probability scenario P01 through P12 | Use actual auditor tool evidence or mark it unresolved, with no invented probability claims. | Not run |
| T095 | Save, multiplayer and AI | Run parser, localisation, script and asset checks | No new errors, duplicate IDs, missing key consumers or unjustified completion labels. | Not run |
| T096 | Save, multiplayer and AI | Run independent near-completion and completion reviews | Findings have explicit dispositions and unavailable reviews remain blocked. | Not run |

Total: 96 acceptance cases.
