# 068 ZIN: AI, balance and acceptance

## AI design priorities

An AI colony must first keep its capital and supply viable, then fulfill accepted obligations, then pursue its political route. Optional expansion follows those commitments. It must not accept five distant contracts with the same rare host or spend its last equipment on an unnecessary diplomatic gift.

Country-specific preference directions are in the country registry and route documents. These directions are not measured probabilities. Peaceful elves, mercenary Dondor, independent northern clans, Afrit's institutions and Volgan's command structure need different strategy logic.

## Probability audit worlds

Evaluate at least the following named worlds against actual implemented pools: peaceful low-Chaos Earth, a weak former owner, a strong former owner, a remote island arrival, a cold creature in a warm state, Rush with high Unity and low Influence, Rush with low Unity and high Influence, evidence preserved, evidence destroyed, no viable successor outpost, early Afrit crown before Worshipdom, Volgan before usurpation, Afrit after full consolidation, a disabled evolution, a missing anchor, a lower-Chaos post-Reckoning victory, and a forced manual setup.

The probability auditor begins by inspecting the real option pools, prerequisites and MTTH modifiers. Use the verified inspect, evaluate, sweep, simulate and compare routes exposed by the actual installed tooling. Keep exact, bounded, sampled and unresolved results distinct. Do not turn AI preference weights into percentages by summing unrelated focus choices.

Test ordering as well as eventual probabilities. A colony must not declare an offensive war while still neutral. A ruler's death must not depend on whether its AI happens to select a cosmetic focus. A timed offer must not be accepted after its target changed hands.

## Combat and economy acceptance

Compare meaningful complete country packages with matching game version, technology, doctrine, terrain, supply, weather, commanders and division composition recorded. Use several battles and strategic deployments. A unit's raw attack number alone does not prove its intended strength.

Record effective attack, defense, organization, losses, reinforcement time, supply demand, movement and replacement availability for the reference human formation and each major creature family. Use those results to meet the qualitative hierarchy and the proposed benchmarks in the military document.

Test the canonical Rush as the strongest complete baseline colony, Volgan as initially far stronger than Afrit, and an actually consolidated Afrit-held Rush as capable of a clear advantage. Preserve very strong rare beings. Do not fix every difficult battle by making all creatures ordinary infantry.

The economy must support starting forces beyond the temporary bridge through real construction, trade or service. Test large and small inherited industry, damaged ports, interrupted corridors, unavailable equipment and a colony isolated by war. No founding army should survive solely through the old daily free-unit and free-nuke behavior.

## Acceptance cases

Each row is a required future test, not a claim of a successful run. The same records are available in JSON for the implementation handoff.

| ID | Group | Case | Required outcome |
| --- | --- | --- | --- |
| Z68-T001 | Opening and placement | Weak host | A strong colony receives its full ordinary founding package even when the former owner is weak. |
| Z68-T002 | Opening and placement | Last state | Ordinary allocation rejects a state whose loss would erase the former owner. |
| Z68-T003 | Opening and placement | Capital relocation | An otherwise valid former capital is transferred only with a proved legal relocation. |
| Z68-T004 | Opening and placement | Existing colony territory | Ordinary arrival cannot overwrite any state owned by an active ZIN colony. |
| Z68-T005 | Opening and placement | Contested state | An unsupported owner-controller war conflict is skipped without partial transfer. |
| Z68-T006 | Opening and placement | No carrier | No state, population, log or Major consumption occurs when the carrier cannot be admitted. |
| Z68-T007 | Opening and placement | Island port | A maritime package starts only with a valid operational port and actual fleet route. |
| Z68-T008 | Opening and placement | Two concurrent arrivals | Reservations prevent both requests from using the same state or carrier. |
| Z68-T009 | Opening and placement | Population receipt | Civilian and military arrivals are credited once and existing Earth residents remain accounted. |
| Z68-T010 | Opening and placement | Public knowledge | The first news does not reveal the common ZIN identity or a hidden future alignment. |
| Z68-T011 | Defensive peace | Adjacent demand | Only aggressor-owned states neighboring current colony-owned states enter the demand. |
| Z68-T012 | Defensive peace | Nonadjacent capital | A remote aggressor with no adjacent owned state receives an empty-set white peace demand, never a capital demand. |
| Z68-T013 | Defensive peace | Changed border | An outdated offer expires and is recalculated without stale transfer. |
| Z68-T014 | Defensive peace | Several aggressors | Each bilateral demand targets that aggressor and does not give away a third country's territory. |
| Z68-T015 | Defensive peace | Separate war | Accepting a colony peace does not end unrelated wars. |
| Z68-T016 | Defensive peace | Offensive colony war | The provocation demand rule is not used as a reward for the colony's own offensive declaration. |
| Z68-T017 | Rush succession | One initial state | Rush has one state at opening and creates a real later outpost before the structural civil-war commitment. |
| Z68-T018 | Rush succession | Outpost lost | The readiness problem is explicit and cannot silently become a peaceful succession. |
| Z68-T019 | Rush succession | Low influence | Afrit still causes the king's death, while his claimant foothold is weak or absent. |
| Z68-T020 | Rush succession | High influence | Actual footholds and high Influence strengthen Afrit and can give him the capital. |
| Z68-T021 | Rush succession | Unselected death focus | The mandatory death is not postponed forever by focus selection. |
| Z68-T022 | Rush succession | Unit partition | Every existing ordinary and specialist formation goes to exactly one valid camp or remains with its actual external owner. |
| Z68-T023 | Rush succession | Few states | Compatible good groups can share a territorial camp, while Afrit never becomes their compulsory coalition partner. |
| Z68-T024 | Rush succession | Einendil dismissed | The one-time refusal permanently closes his route. |
| Z68-T025 | Rush succession | Einendil accepted | He first offers service, remains one unique commander and can become non-royal chosen leader only after the good victory conditions. |
| Z68-T026 | Rush succession | Lost evidence | A failed investigation does not fabricate a replacement truth or disclose Afrit prematurely. |
| Z68-T027 | Rush succession | Free Dominion result | Actual states and units follow the accepted federal constitution. |
| Z68-T028 | Rush succession | Regency result | Civil, military and treasury choices retain their different obligations and never claim to be Einendil's chosen leadership. |
| Z68-T029 | Rush succession | Afrit crown | Rush and Worshipdom do not create two Afrits or duplicate the starting armies. |
| Z68-T030 | Rush succession | Monster boundary | Independent orcs, goblins, trolls and ogres are not automatically inherited with the Rush crown. |
| Z68-T031 | Rush succession | Lost Cause handover | A viable good member takes leadership after Rush defects, without immediate automatic faction defeat. |
| Z68-T032 | Rush succession | Multiplayer choice | No player camp selection displaces another human or clones a unique leader. |
| Z68-T033 | Glo and units | Actual castle | Horos arrival includes the real visible province building and its state binding. |
| Z68-T034 | Glo and units | Occupation | Glo moves to the current controller immediately when the state control changes. |
| Z68-T035 | Glo and units | Split province control | The stored state controller receives Glo even when the castle province has another tactical controller. |
| Z68-T036 | Glo and units | Capital moves | The castle does not move, duplicate or disappear when the country capital moves. |
| Z68-T037 | Glo and units | Annexation and liberation | Exactly one controller receives the effect across both transactions. |
| Z68-T038 | Glo and units | Castle destruction attempt | Generic cleanup or damage does not remove the sole artifact anchor. |
| Z68-T039 | Glo and units | Typed recruitment | Earth manpower and captured harnesses cannot produce unlimited elves, giants or dragons. |
| Z68-T040 | Glo and units | Disband and convert | Template changes and disbanding conserve surviving typed personnel and do not duplicate recruitment permits. |
| Z68-T041 | Glo and units | Dragon access | Only eligible elven and Afrit routes admit dragon hosts, with no dragon tag. |
| Z68-T042 | Glo and units | Hero destruction | The one guard follows the stated recovery route and no second Einendil appears. |
| Z68-T043 | Glo and units | Necromancy accounting | Only new qualifying civilian deaths advance the bounded opportunity and the same deaths are never debited again. |
| Z68-T044 | Glo and units | Undead feedback | Destroyed undead cannot feed the next grave tranche. |
| Z68-T045 | Glo and units | Three-power balance | Volgan is initially much stronger than Afrit and a genuinely consolidated Afrit-held Rush can overtake him. |
| Z68-T046 | Glo and units | Maritime capture | A prize reward refers to a real supported ship transaction or remains unavailable. |
| Z68-T047 | Evolutions and global war | Threshold pause | An uncommitted stage pauses below its own Chaos gate, without deleting already admitted countries. |
| Z68-T048 | Evolutions and global war | Disabled stage | A disabled pool is not added through a hidden completion or downstream shortcut. |
| Z68-T049 | Evolutions and global war | One coordinator | More colonies do not multiply the global ordinary arrival loop. |
| Z68-T050 | Evolutions and global war | Unique defeated ruler | A later ordinary arrival never resets a defeated unique ruler with a full new army. |
| Z68-T051 | Evolutions and global war | Three real anchors | Normal Reckoning needs viable actual powers and does not silently enable a disabled lord pathway. |
| Z68-T052 | Evolutions and global war | Neutral Earth | Peaceful neutral Earth is not automatically classified as hostile opposition that must be conquered. |
| Z68-T053 | Evolutions and global war | Holdout | A harmless isolated remnant can be resolved after the defined interval, while one effective rare host remains significant. |
| Z68-T054 | Evolutions and global war | Simultaneous victory | Only one faction can commit a final ending from current proof. |
| Z68-T055 | Evolutions and global war | Independent endings | Each world-end branch obeys its own toggle without disabling siblings or the main event. |
| Z68-T056 | Evolutions and global war | Lower Chaos | No terminal latch exception is applied without approval, and the strict nonterminal fallback remains visibly disclosed. |
| Z68-T057 | Evolutions and global war | Other world end | An already committed foreign terminal state is not overwritten by a stale ZIN callback. |
| Z68-T058 | Scenarios and presentation | Four presets | All four named setups exist with the specified type and intensity behavior. |
| Z68-T059 | Scenarios and presentation | Latest confirmation | Launch uses the current selected controls and not an earlier stale click. |
| Z68-T060 | Scenarios and presentation | Atomic scenario | Insufficient required states or carriers stops before partial setup. |
| Z68-T061 | Scenarios and presentation | Scenario replay | Repeated confirmation cannot duplicate committed colonies, rulers, armies or Glo. |
| Z68-T062 | Scenarios and presentation | Forced provenance | Scenario-created outcomes cannot earn ordinary natural-progression achievements. |
| Z68-T063 | Scenarios and presentation | Correct maps | Every arrival uses its actual homeland source, with Worshipdom and Yeldenne unresolved until approved. |
| Z68-T064 | Scenarios and presentation | Map preservation | All thirteen original source files retain their recorded checksums. |
| Z68-T065 | Scenarios and presentation | UI knowledge | Hidden agents and unproven murder responsibility stay out of public ledgers. |
| Z68-T066 | Scenarios and presentation | UI density | A normal active phase shows at most six primary actions and one to three missions. |
| Z68-T067 | Scenarios and presentation | Cost parity | GUI, ordinary decisions and AI pay the same exact costs and respect the same commitments. |
| Z68-T068 | Scenarios and presentation | Asset consumer | The selected DDS, model and sound hashes match actual runtime references. |
| Z68-T069 | Scenarios and presentation | No fake completion | Missing model, audio, icon, native render or engine evidence remains a disclosed production gate. |

## Save, reload and cleanup

Repeat the important lifecycle tests across a save and reload, host-country annexation, controller change, cosmetic identity change and a legitimate country-carrier reuse. Durable identities must survive these operations, while short-lived targets and canceled reservations must not leak into a later transaction.

Use sparse registered country and state processing. A source inspection must prove that no new unbounded daily, weekly or monthly whole-world scan is hiding behind a convenient helper. The main arrival coordinator, active contract set, actual war receipts and castle-control seam supply the bounded work.

Remove the legacy daily army grants, blanket enemy punishment and free nuclear strikes from the reworked ownership path. Retire old events and references safely so the legacy and new systems cannot both run. Keep compatibility with existing saves explicit. A development migration cannot silently create a new army or erase a live country's history.

## Independent review and closure

Use the project's improvement-loop planner after the routes, decisions and consequences exist. Give it the complete accepted design and actual implementation evidence. It should find missing playable consequences, contradictory ownership, shallow route payoffs and unnecessary extra mechanics. Its accepted changes must be merged into the source spec or implementation, not left as an untracked second truth.

Use the focus, decision, country-package, localization, probability, asset and engine audit roles where available. Each review reports its actual tool access and evidence. A single main-agent consistency pass is useful, but it is not an independent subagent audit.

The current package received document and registry consistency checks only. No HOI4 game session, installed-map inspection, probability engine, custom GUI renderer, Blender export or independent project subagent ran here. The accompanying reading and validation report states the exact boundary.
