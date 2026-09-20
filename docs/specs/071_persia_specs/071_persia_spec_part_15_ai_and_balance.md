# 071 Persia: AI and balance review

## Intended strength

The restoration should rapidly create a serious regional power. At baseline, the opening army threatens nearby regional opponents and gives a remnant a real recovery chance. Evolution II supports a major-power-quality regional force. Evolution III can sustain several regional fronts if geography and supply permit.

The design does not promise that baseline Persia defeats a major faction, or that an Evolution III remnant can ignore an impossible supply position. The acceptance test is whether the actual force and logistics match the promised role. If they do not, adjust the real package and support design openly. Do not conceal the failure with a larger tooltip bonus.

## AI decision order

The AI first protects the surviving center and recovers urgent homeland territory. It then establishes replacement production and supply, resolves damaging internal disputes, and chooses a route and regional objective. Opportunistic expansion follows when the military and diplomatic conditions are reasonable.

A high evolution increases ambition and available power. It does not remove the need to assess enemies, access, and supply. A large army trapped in an unsupplied enclave should prioritize opening a corridor, not demand Egypt on its first day.

The AI should generally maintain one principal offensive campaign until the first regional settlement is stable. It can open a second front when it has a genuine local advantage, a working route, and enough reserves. An existing defensive war can override this preference.

## Route preference

Achaemenid preference rises with viable prospective satrapies, multiple connected expansion opportunities, a compatible imperial settlement, and a stable base for long-term administration. Sasanian preference rises with land-frontier threats, a suitable central military settlement, and useful western or eastern command opportunities. Modern preference rises for non-monarchical governments, useful industrial and oil capacity, and willing investment partners.

These are comparative preferences, not fixed probabilities. The final weights must be inspected and evaluated against the actual candidate pool. A government restriction can remove an invalid option before weights are compared. Do not give an AI a strong preference for a route it cannot legally complete.

## War assessment

The AI considers the principal opponent together with its overlord, faction, guarantees, current wars, available fronts, and supply access. It distinguishes an isolated local opponent from a country backed by a major coalition.

A current weak enemy may be a good target even if its country name normally suggests a great power. Conversely, a small state holding one Iranian province may be a bad target if it is securely protected by a much stronger bloc. The assessment must use the current save, not a fixed historical ranking.

A homeland recovery can justify higher risk than a distant prestige campaign. An existential defensive situation can justify a desperate operation. These exceptions must be named and tested rather than hidden in a large generic aggression multiplier.

## Subject and contract behavior

AI Persia should use viable satrapies for distant territory, especially where direct administration would add a long exposed frontier. It should choose obligations that the subject can actually meet and avoid repeated emergency levies against the same fragile partner.

A subject AI evaluates military pressure, protection, autonomy, investment, ideology where relevant, existing alliances, and its actual capacity to deliver. It should sometimes refuse a bad charter, even when Persia is strong. A human subject receives the choice directly.

The modern AI does not promise investment while its own critical construction and replacement programs are starved. The Achaemenid AI should honor a binding charter unless it accepts the visible cost of emergency rule. The Sasanian AI should resolve a dangerous command dispute before expanding that command again.

## Recruitment and production

The AI maintains a replacement plan for the force it actually owns. It does not build only infantry equipment while deploying a large armored and mechanized opening force. It reserves enough guard capacity and material to finish programs already in progress.

A capacity shortage stops new guard recruitment. It does not cause repeated failed clicks or cancel useful existing units. A fuel shortage changes operational and production priorities. It does not trigger an unexplained deletion of the opening tanks.

Air and naval AI must account for valid bases. Landlocked Persia develops access before a large naval program. An airfield shortage causes expansion and reserve management, not the repeated creation of overcrowded wings.

## Named evaluation scenarios

| Case | Expected ordering or behavior | Failure to detect |
|---|---|---|
| Baseline 1936 Iran, full homeland, weak isolated regional rival | Supply and political settlement before a prepared first regional war | Distant global demands or no useful action |
| Baseline remnant, one legal homeland state | Deploy real force, relieve supply, prioritize nearest viable recovery | Most army withheld or immediate unsupplied paralysis |
| Evolution III remnant at war with a major faction | Defend and open a corridor before optional outer claims | Blind simultaneous war declarations |
| Existing industrial Iran after 1943 | Context-scaled conventional package and replacement planning | A 1936-sized force with obsolete unusable equipment |
| Non-monarchical Iran with useful oil and clients | Modern route ranks above incompatible crown routes | Forced emperor or invalid route lock |
| Monarchical Iran with several willing subjects | Achaemenid route remains competitive | Every save selects the same military route |
| Threatened land-frontier Iran with weak naval access | Sasanian preparation ranks strongly | Naval prestige projects starve immediate defense |
| Regional target protected by a strong overlord | Negotiation or preparation outranks reckless attack | Opponent strength counts only the small subject |
| Target holder already at war with Persia | Reuses the existing confrontation | Duplicate declaration or war goal spam |
| Several claims held by the same country | One strategic enemy record and coherent demand | Multiple redundant events to the same recipient |
| Loyal but occupied satrapy misses delivery | Access repair or relief before punitive enforcement | Inability treated as automatic treason |
| Defiant subject after repeated charter breaches | Hearing or explicit enforcement | Endless levies with no political cost |
| Modern client and severe Persian material shortage | Reduced commitment or postponed offer | Unpayable investment contract |
| Guard manpower at its ceiling | Production and regular-force growth before new guard training | Template-copy cap bypass |
| Legitimacy near 20 during a temporary border loss | Crisis begins only after the defined sustained conditions | One-day threshold flicker creates a civil war |
| Legitimacy 80 but no route conclusion | Supremacy remains locked | High meter alone unlocks universal submission |
| Human subject in multiplayer | Recipient choice remains authoritative | AI response replaces the human answer |
| DLC restoration already completed | Root is excluded as equivalent | Duplicate empire, army, or tree rewards |

## Probability tool evidence

The future AI auditor must begin with `hoi4.probability_inspect`, evaluate the named scenarios, sweep threshold boundaries and rank reversals, and compare before and after the implementation. Render matrices or rankings where they make review easier.

Simulation is appropriate only when uncertain inputs are explicitly declared. Sequence analysis is appropriate only for a complete custom pool with declared cadence and state transitions. Neither tool should be used to invent an exact event selection chance from an incomplete pool.

No probability MCP tools were run in this planning session. The table describes expected behavior, not measured results.

## Balance experiments

Test each opening tier at an early and a late campaign date. Compare the delivered field manpower, equipment, operating aircraft, reserves, and supply situation. Confirm that higher tiers are materially stronger even when advanced equipment is unavailable.

Compare a guard formation against a conventional formation of similar manpower and support in its intended terrain. Record attack, defense, organization, supply, reinforcement, and equipment burden. Advanced guards should be strong without making normal infantry obsolete in every task.

Run a supply-stressed remnant case, an industrial Iran case, a landlocked case, and a case with several existing wars. Test the 180-day support expiry and the paid extension. The army should face normal strategic costs after the opening, not an arbitrary collapse caused by a hidden expiration.

Test charter obligations over several settlement periods, including insufficient stocks, broken access, war, subject exit, and a human recipient. Verify that transfers conserve resources and that status changes explain their cause.

## Tuning discipline

Authored tuning should favor round values in multiples of five. Existing project constants, structural counts, dates, identifiers, equipment requirements, and formula-derived results are not forced into that rule when doing so would make them invalid.

The most important adjustments are force composition, replacement capacity, supply relief, mission duration, and diplomatic willingness. Do not solve every balance problem by adding another national spirit. A change must state which observed failure it addresses.
