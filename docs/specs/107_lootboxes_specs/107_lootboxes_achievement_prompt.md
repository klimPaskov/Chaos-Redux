# Lootboxes achievement implementation and icon prompt

Read `README.md` for the accepted scope and confirmed identifier map. The four achievement routes below are part of the event design; Part 06 provides their detailed conditions and internal tuning values.

Read current `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-subagents`, the six Lootboxes design parts, and the current achievement registry and consumer patterns. Follow the implementation handoff's source and evidence rules. These are working technical keys and title directions, not final localisation. Preserve the approved final keys once assigned by the parent.

## Achievement purpose

The achievement set recognizes what a country does around the reward system: using an opportunity during a real crisis, developing peacefully, recovering from prolonged dependence, and showing restraint after a jackpot. Receiving access or clicking a chest five times is not an achievement by itself.

The four designs below cover crisis use, productive peace, quiet independence, and rare restraint. Their multi-condition structure, attribution requirements, and secrecy rules are required; numeric thresholds remain internal tuning values. Working labels describe the intended theme, while final titles and descriptions are written during achievement production.

All achievements follow the existing shared eligibility system. They require a human-eligible country with genuine Event 107 access and normal campaign receipts. Debug grants, force-completion helpers, refunded invalid transactions, imported fabricated receipts, and duplicate completion callbacks do not count. An implementation must inspect the current registry and debug eligibility patterns before choosing exact flags.

AI countries retain ordinary gameplay facts needed by the event, but achievements do not change their purchasing or diplomacy. An achievement cannot improve future loot odds, grant Political Power for more purchases, reduce burden, or alter an omen roll.

## Achievement overview

| Technical working key | Working theme | Visibility | Difficulty | Main challenge |
| --- | --- | --- | --- | --- |
| `chaosx_107_supply_and_settlement` | Supply under pressure | Visible after Lootboxes access, without hidden-system text | Hard | Receive a substantial military prize during a genuine defensive crisis, then help secure and sustain peace |
| `chaosx_107_productive_peace` | Productive peace | Visible after access | Hard | Turn an economic opportunity into durable national development while making a real peaceful contribution |
| `chaosx_107_quiet_independence` | Quiet independence | Hidden until earned | Very hard | Recover a deeply exposed country through real peaceful contributions and sustain independence from further drops |
| `chaosx_107_rare_restraint` | Rare restraint | Hidden until a Legendary has been genuinely received, with no burden details | Very hard | Reach the complete rarity collection, then stop buying and make several meaningful peaceful contributions |

## A1. Supply under pressure

**Eligible country.** Any valid recipient in a genuine defensive war, with the original conflict episode and its own defensive participation established by the relevant owner. A country does not become eligible by provoking an artificial war to manufacture the condition.

**Unlock conditions.** During that conflict, receive a fully delivered Epic, Mythic, or Legendary package whose primary family is military equipment, fuel and logistics, manpower, or useful military experience. Remain uncapitulated from delivery through the qualifying settlement. Within an initial target of 180 days after the prize, contribute to an actual qualifying peaceful settlement of that conflict and receive a positive allocated share of its real negative Chaos change. Then sustain 90 days without initiating a new aggressive conflict or completing another box opening.

The achievement recognizes a substantial supply opportunity followed by successful statecraft. It does not claim that individually tracked lootbox rifles won the war. Tracking causal use of each stockpile item is unnecessary and would create unsupported provenance claims.

**Disqualifiers.** A manufactured conflict episode, missing actual settlement proof, zero applied Chaos change, foreign-only settlement credit, capitulation during the qualifying crisis, another completed opening during the final restraint interval, or an aggressive war started by the candidate country. An unrelated foreign attack during the final interval suspends the peaceful-day count until the country is again at peace, preserving earned days and the original genuine settlement.

**Tracking.** Preserve the purchase receipt, sealed primary reward family, rarity, conflict identity, relevant ownership, settlement contribution identity, and the final restraint interval. Evaluate once at the end of that interval using the original country and episode. A later unrelated military prize cannot replace a failed earlier episode unless it starts a new valid candidate.

**64x64 icon direction.** A compact supply chest beside a lowered field weapon and a folded peace document. Use one strong silhouette and readable contrast. The completed icon should suggest readiness turning toward settlement. Grey and not-eligible variants derive through the established achievement templates.

## A2. Productive peace

**Eligible country.** Any valid recipient at peace when it receives a fully delivered Rare-or-higher civilian construction, infrastructure, research, or economic-support prize. The country must have a supported existing nonwar restorative path for its relevant situation.

**Unlock conditions.** Immediately after the reward is fully applied, snapshot the exact set of states that the country owns, controls, and holds as cores. The factory baseline is the sum of usable civilian factory levels within exactly that saved set, excluding all noncore and other excluded states. Accumulate 180 qualifying peaceful days after this snapshot, with no further box opening or initiated aggressive war, while remaining capable of ordinary peaceful development. At completion, the entire saved state set must still be owned and controlled by the same country. Count usable civilian factory levels only within that saved set and require its total to exceed the post-reward baseline by at least three. During the interval, the country must also receive positive actual recovery contribution from at least one verified existing nonwar restorative action.

The factory requirement measures net development after the initial reward. The prize's own factory levels are already in the baseline. Conquered or newly acquired states do not count toward the three additional levels. This is a national development outcome, not a claim that the game can identify the precise source of each factory's construction inputs.

**Disqualifiers.** Another completed box, aggressive war, loss of the qualifying state set that prevents the required retained development, invalid or debug building grants, a nominal negative History row with zero actual change, or credit based only on passive decay. An external attack suspends the peaceful-day count until peace returns, preserving earned days and legitimate development and contribution evidence.

**Tracking.** Preserve the reward receipt, exact saved core-state set, its post-delivery usable civilian factory total, opening-count baseline, own aggressive-war marker, and contribution receipt. Use a bounded country-owned completion check. Do not scan every country or state each day for this achievement.

**64x64 icon direction.** A modest factory and a growing branch emerging beside an opened crate, composed as one clear subject. Avoid miniature building plans, text, or several tiny factory symbols.

## A3. Quiet independence

**Eligible country.** Any valid recipient that has reached at least the Heavy burden band after Bonus Drops is active and has actually experienced a dependence or other influence-owned symptom. This is a hidden condition and receives no public progress meter.

**Unlock conditions.** Starting from that qualified exposure episode, reduce burden to zero using positive actual contributions from at least two distinct, independently valid peaceful actions. The actions must not be duplicate records from one causal outcome or reversals of a self-created arrangement. Complete no new opening after the recovery interval begins. Once burden reaches zero and influence-owned symptoms are removed, sustain 180 days without another completed box and without initiating an aggressive conflict.

The action-count requirement prevents one duplicated callback from masquerading as a recovery route. The zero-burden requirement verifies lasting recovery, while the later interval demonstrates continued independence. Symptom expiry alone does not satisfy this achievement because it does not reduce burden.

**Disqualifiers.** Passive decay, foreign-only actions, settings edits, banked credit earned at zero burden, manufactured wars, reversible arrangement farming, a new completed opening during the interval, or any debug clearance. A legitimate outside attack does not erase already earned recovery. Suspend the final peaceful-day count during that war and resume it after peace, without resetting earned days or changing the contribution's validity.

**Tracking.** Preserve the qualified peak and episode, the burden at the start of the attempt, exact consumed contribution identities, recovery-to-zero date, and completed-opening baseline. Achievement tracking reads authoritative gameplay receipts, never drives them. Its hidden key and wording must not appear in the category, opening window, Event Details, or ordinary symptom tooltips.

**64x64 icon direction.** An opened hand releasing a dark thread that no longer binds a small crate, with a calm pale accent. Suggest regained independence without a literal numerical gauge or a demon portrait. Final title and description should remain indirect and avoid publishing the hidden formula.

## A4. Rare restraint

**Eligible country.** Any valid recipient that has genuinely received all five rarities through its own completed openings, while retaining the listed achievement-specific conditions, including at least one Legendary. All five must have been possible through the ordinary base pool throughout the campaign. Achievement progress cannot modify those probabilities.

**Unlock conditions.** After the collection is complete, begin an initial target interval of 180 days with no further completed opening and no initiated aggressive war. During that interval, earn at least three actual allocated negative Chaos points from at least two distinct qualifying peaceful action episodes. At least one of those actions must be an existing nonwar restorative action. Fractional participant shares count accurately toward the total.

This combines a difficult luck-driven collection with a sustained strategic commitment outside purchasing. It does not unlock merely because Legendary appeared. The player remains free to buy again, but doing so ends the current restraint attempt and allows a later attempt from the already earned collection state.

**Disqualifiers.** Counted rarity from a refunded or fabricated box, duplicate reveal, foreign credit, natural global decay, nominal rather than applied reductions, one action split into several records, a new opening during the interval, or an aggressive conflict initiated by the country. A third-party attack does not turn earlier contributions into ineligible acts.

**Tracking.** Keep five completed-rarity presence facts, the collection-complete date, the current restraint attempt, distinct contribution identities, exact allocated amount, and its nonwar contributor marker. Displayed progress before eligibility must not reveal influence, pressure, or a recovery threshold. Final wording describes restraint and real peaceful contribution without disclosing the concealed causal system.

**64x64 icon direction.** Five distinct seal shapes arranged around a closed clasp, with the brightest seal restrained rather than bursting outward. Keep the geometry legible at native size and use the existing achievement frame.

## Shared achievement rules

All challenge periods use original absolute due dates or a clearly specified pause/resume rule. Reloading cannot shorten them. A result replay cannot restart a more favorable timer. A country-control change preserves the candidate's owner and eligibility according to the shared achievement system.

Where a third-party attack interrupts a required peaceful period, use one consistent treatment across this set: preserve completed reward and contribution facts, suspend accumulation of qualifying peaceful days while the country is at war, and resume when it is again at peace. Initiating an aggressive conflict fails the current attempt. The implementation must be able to distinguish these cases through genuine conflict provenance rather than guessing from current war membership.

The thresholds above are internal achievement design constants. They are separate from burden and reward tuning. A later balance adjustment must update the spec, tracking, localisation direction, test fixtures, and icon eligibility behavior together. No hidden achievement should appear as an extra purchase or cleansing objective in the Lootboxes category.

Every achievement needs completed, grey, and not-eligible 64x64 outputs using the current project templates and exact registry keys. Icons are original family-appropriate compositions. A scaled decision icon does not fulfill this requirement. The separate achievement prompt carries the full tracking and production handoff.

## Implementation and production work

Wire all four achievements through the existing shared registry. The parent owns shared registry integration and any single unique-id field. Keep Event 107 tracking country-owned and driven by genuine completed-opening and peaceful-contribution receipts. The achievement worker cannot create a new Chaos credit, alter reward odds, encourage AI to expose itself, or make a hidden progress value visible in the Lootboxes UI.

For accepted routes, implement bounded candidate lifecycles with original dates, exact country identity, distinct action provenance, and the consistent defensive-interruption rule. Verify that a completed receipt is fresh before counting it. Preserve fractional allocated contribution accurately. Keep debug, compensated, fabricated, and duplicate records ineligible. Do not infer victory from a white-peace command or meaningful contribution from a History actor alone.

Write final titles and descriptions from the stated themes. Visible achievements may describe their strategic challenge without diagnosing hidden influence. Hidden achievements must not reveal their conditions through category text, Event Details, raw keys, progress values, locked-icon tooltips, or public event options. Even after reveal, avoid publishing exact influence, omen, or recovery formulas.

Route icons through `chaosx_icon_artist` and the current event-assets skill. Produce one original transparent 64x64 completed composition per key, then its exact grey and not-eligible variants with the current supplied templates and supported achievement-processing tool. Preserve source images, exact generation arguments, candidate lineage, template hashes, final selected master, decoded alpha, native-size review, and all three final DDS consumers. Use the exact final key for the root `gfx/achievements` triplet. A smaller copy of a chest-window drawing or decision icon does not satisfy this separate icon family.

Use meaningful source checks for legitimate, near-miss, duplicate, debug, interruption, reload, and country-control cases for each accepted achievement. Part 6 cases LB-X01 through LB-X06 are the minimum candidate scenario set. Include its Productive peace fixture that separates the saved core-state factory baseline from noncore industry and later state acquisitions. Add the accepted threshold and third-party-attack boundaries. Source-only checks do not establish native achievement or save behavior; unavailable MCP routes are evidence limits rather than completion gates. Agents do not launch HOI4, request a user-run session, or wait for live-game evidence.

Return the exact keys and files, required-versus-implemented condition table, current localisation and icon crosswalk, source and scenario evidence, and all remaining gaps. Report changed or substituted conditions explicitly. Do not mark an achievement complete merely because its icon or registry row exists. Final approval of the integrated set remains with the parent.
