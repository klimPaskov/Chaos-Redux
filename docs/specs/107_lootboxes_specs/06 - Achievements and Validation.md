# 107 Lootboxes: achievements and validation

## Achievement purpose

The achievement set recognizes what a country does around the reward system: using an opportunity during a real crisis, developing peacefully, recovering from prolonged dependence, and showing restraint after a jackpot. Receiving access or clicking a chest five times is not an achievement by itself.

All four achievement routes below are part of the accepted event scope: supply during crisis, productive peace, quiet independence, and rare restraint. Their multi-condition structure, attribution requirements, and secrecy rules are required. Timing and progress values remain internal tuning proposals; working labels describe direction, and final titles and descriptions are written during achievement production.

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

**Eligible country.** Any valid recipient that has genuinely received all five rarities through its own paid completed openings, including at least one Legendary. All five must have been possible through the ordinary base pool throughout the campaign. Achievement progress cannot modify those probabilities.

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

## Acceptance strategy

Validation must connect the real source chain to the visible result. A mathematical probability table, a static GUI preview, or an isolated helper test cannot establish the whole feature. The implementation needs matching source, scenario, receipt, visual, and available live-game evidence for the relevant boundary.

The following cases are concrete acceptance targets. Expected values use the final chosen tuning where a planning anchor is adjustable. User-fixed values remain exactly 50 PP, five accepted human activations, and the 200+, 400+, and 600+ evolution eligibility thresholds.

### Access and payment

| ID | Case | Required result |
| --- | --- | --- |
| LB-T01 | Initial access delivered twice to the same country | One permanent category, no state reset or free reward |
| LB-T02 | Recipient has 0 PP at event arrival | Access granted, purchase unavailable, later purchase possible |
| LB-T03 | Buyer has 49, fractional below 50, exactly 50, and above 50 PP | Display and click-time inclusive gate agree, exact payment only at affordability |
| LB-T04 | Black Friday inactive, active, overlapping, and expired | Every Lootboxes quote and actual debit stays exactly 50 |
| LB-T05 | Two purchase requests overlap | One payment and one sealed record, second request harmless |
| LB-T06 | One tier has no certified recipe for the country | No payment, no roll, explicit pool defect in the implementation report |
| LB-T07 | Valid paid box is closed and country falls to 0 PP | Free resumption remains available |
| LB-T08 | Initial-event enablement changes after access | Existing access and paid obligations follow the permanent-access contract, with no silent confiscation |
| LB-T09 | Repeated purchases through the same native decision plus resume, reload, and result replay | Each genuinely new paid purchase samples once with fresh per-purchase randomness; all continuations use the sealed receipt without another sample |
| LB-T10 | Matched fixture copies of one sealed purchase: immediate AI completion and human close/resume before later completion | Both paths use the common resolver and each grants its copy's sealed receipt once; the human retains free timing choice, with no new timeout, payment, or balance rule |

### Opening, saving, and ownership

| ID | Case | Required result |
| --- | --- | --- |
| LB-O01 | Close and resume at stages 0, 1, 2, 3, and 4 | Same paid prize and accepted stage, no influence before completion |
| LB-O02 | Save/reload at every pending stage | Same purchase identity, shell, rarity, exact contents, provider version, and stage |
| LB-O03 | Held input, rapid clicks, and stale stage requests | Each accepted fresh activation advances exactly one visible stage |
| LB-O04 | Fifth activation delivered twice | One complete grant, one history update, one influence charge |
| LB-O05 | Close after commit before the result appears | Resumption reads the completed result and grants nothing again |
| LB-O06 | Reload or reopen a completed result | No repeated material, modifier duration, achievement credit, or omen roll |
| LB-O07 | Campaign paused throughout opening | All five interactions and animations work without advancing game time |
| LB-O08 | Two human countries open different boxes | Correct local windows and sounds, independent state, no global pause |
| LB-O09 | Co-operative control sends simultaneous input | Country and purchase identity serialize accepted stages |
| LB-O10 | Human/AI handover during a pending opening | Same record resolves once through the proper presentation path |
| LB-O11 | Cosmetic change, civil war, annexation, and restoration | One lawful purchase owner, no copied grant rights, supported restoration preserved |
| LB-O12 | A bundle component fails in a supported interruption scenario | Recovery completes only missing components, without declaring partial delivery complete |

### Rewards and probabilities

| ID | Case | Required result |
| --- | --- | --- |
| LB-R01 | First ordinary box before any evolution | All five tiers positive and correctly ordered |
| LB-R02 | Every form and poor-result pressure state after engine quantization | Probabilities normalize and remain strictly ordered |
| LB-R03 | Common sequence reaches and exceeds the assistance cap | Common decreases then plateaus, all other tiers rise, no guaranteed promotion |
| LB-R04 | Interleaved non-Common outcomes | History eases once per completed box, independent of burden and bundle size |
| LB-R05 | Different influence at matched form and reward history | Identical rarity probabilities |
| LB-R06 | All supported Premium incidences | Ordinary remains possible, aggregate rarity order preserved |
| LB-R07 | Small, major, landlocked, unusual-equipment, and mature research countries | Useful certified candidates exist in every tier |
| LB-R08 | Fuel or XP becomes full after purchase | Complete sealed amount reaches the actual usable native holding |
| LB-R09 | Building slots fill or intended state ownership changes | Original building type and full quantity follow the sealed legal placement policy |
| LB-R10 | Research opportunity completes or an older bonus exists | New sealed benefit remains useful and preserves earned older value |
| LB-R11 | Repeated timed-support rewards | Full earned duration or contribution retained within the supported stack policy |
| LB-R12 | Mythic compared with Legendary at a matched country snapshot | Legendary has the higher total useful benefit budget |
| LB-R13 | Bonus Drops package has several components | One opening history update and one influence increase |
| LB-R14 | Chaos equipment provider is eligible | Genuine stock or support arrives without invoking another event's formation or lifecycle chain |
| LB-R15 | Fuel Crisis interaction | Full genuine fuel delivery, no Event 107 clawback or cargo-loss omen |

### Evolution entry paths

| ID | Case | Required result |
| --- | --- | --- |
| LB-E01 | Shared threshold boundary at 199/200, 399/400, and 599/600 | Eligibility follows the shared evolution owner and its enablement |
| LB-E02 | Evolution is eligible but not yet unlocked | No premature reward or hidden-family activation |
| LB-E03 | Each evolution unlocks after access | New purchases gain the correct cumulative capabilities |
| LB-E04 | Event first arrives after each evolved state is already active | Correct direct initialization without duplicate reports, gifts, or state resets |
| LB-E05 | A paid box waits through one or several unlocks | Its shell and full reward snapshot remain unchanged |
| LB-E06 | Chaos later falls | Shared evolution persistence respected, burden not passively cleansed |

### Hidden influence and peaceful recovery

| ID | Case | Required result |
| --- | --- | --- |
| LB-H01 | Paid box remains unopened indefinitely | No opening exposure or false completed history |
| LB-H02 | Long all-Common run after evolution | Heavy and severe consequences remain genuinely possible |
| LB-H03 | Lucky high-burden sequence | Quiet results remain possible, no deterministic punishment count |
| LB-H04 | Immediate and delayed consequence paths | Combined opening-level risk matches the chosen model and stays below certainty |
| LB-H05 | New opening during an active dependence symptom | Short relief possible, full burden added, original symptom expiry preserved |
| LB-H06 | Country stops opening | Finite effects expire, one delayed opportunity terminates, no recursive withdrawal |
| LB-H07 | Multiple accepted omens | Family and combined magnitude caps hold, no unlimited stacking |
| LB-H08 | Partial recovery and recovery to zero | Appropriate weakening, complete removal at zero, no new omen roll |
| LB-H09 | Ordinary UI, stat breakdowns, report text, and Event Details | Truthful visible effects without burden, odds, hidden thresholds, or curse linkage |
| LB-C01 | Request -3 while global Chaos is 1 | At most 1 actual point is available for allocation |
| LB-C02 | Negative request at zero, disabled, or locked writer | Zero lasting recovery credit, finite symptoms still expire |
| LB-C03 | Monthly decay or another country's action | No private recovery for the test country |
| LB-C04 | Single actual contributor | Exact eligible allocation and one private reduction |
| LB-C05 | Capped settlement with several contributors | Shares sum to no more than actual applied reduction |
| LB-C06 | One action emits overlapping source callbacks | One causal contribution, no duplicate recovery |
| LB-C07 | Beneficiary differs from liberator or releaser | Credit follows the verified actor contribution |
| LB-C08 | Join/leave cycle, puppet-release cycle, or manufactured war | Reversal farming rejected even when callbacks and row ids are new |
| LB-C09 | A later independent attack or liberation | New genuine episode can qualify, no permanent same-neighbor ban |
| LB-C10 | Delayed durability check and reload | Original due date and bounded old-burden eligibility preserved |
| LB-C11 | Environmental fractional conversion with passive and foreign inputs | Only proven attributable actual negative amount is credited |
| LB-C12 | Already peaceful independent country outside a faction | Verified existing nonwar recovery route works without a new Lootboxes action |

### AI, presentation, and achievements

| ID | Case | Required result |
| --- | --- | --- |
| LB-A01 | AI just below and exactly at price plus reserve | Budget invariant holds and payment remains 50 |
| LB-A02 | Stable surplus compared with urgent law or crisis | Strategic obligations appropriately suppress discretionary buying |
| LB-A03 | Repeated callbacks and high PP income | One opportunity and bounded cadence, no catch-up purchase burst |
| LB-A04 | Same public state with different hidden burden and omen risk | Identical purchase policy, normal independent outcome rules |
| LB-A05 | Human and AI with matched reward context | Same price, reward distribution, exposure, and recovery rules |
| LB-U01 | Every shell and saved damage stage | Coherent genuine frames, no pre-reveal rarity signal |
| LB-U02 | All five reveal tiers | Distinct art and sound, Legendary strongest and Mythic second |
| LB-U03 | Full bundle and long localisation at supported resolutions | Every real benefit readable, no clipping or hidden rows |
| LB-U04 | Muted effects, interrupted tails, rapid rejected input | Settings respected, no false successful hit cue or foreign audio |
| LB-U05 | Keyboard or reduced-motion route where verified | Five deliberate stages and identical gameplay outcome |
| LB-U06 | Final runtime asset inspection | Correct sheets, frame bindings, alpha, dimensions, fallbacks, and licensed sources |
| LB-X01 | Each achievement's complete legitimate route | One unlock under the exact tracked conditions |
| LB-X02 | Partial or near-threshold achievement route | No premature unlock |
| LB-X03 | Duplicate reward or contribution callback | No extra progress |
| LB-X04 | Debug, compensated, or invalid receipt | No eligible progress |
| LB-X05 | Achievement interval across save and control changes | Correct owner and elapsed peaceful duration |
| LB-X06 | Hidden achievements before unlock | No secret mechanics revealed through labels, progress, or icon tooltips |

### Probability fixture detail

LB-R02 includes ordinary and Premium at fresh, midpoint, and maximum poor-result pressure. LB-R06 includes the illustrative 20% and 35% Premium incidences and the full final supported incidence range. Compare each mixture with the corresponding shell-weighted distribution at the same history coordinate. LB-R03 includes a finite all-Common sequence beyond the cap. LB-R04 includes alternating outcomes and a long pause, proving that elapsed time alone does not change poor-result history.

LB-R07 supplies complete actual within-tier recipe pools for the small country, major, landlocked country, country without usable air or naval consumers, country without eligible Chaos equipment, and mature research country. Each fixture lists included and excluded providers with their exact eligibility cause and proves all five tiers remain populated. A list of broad reward families alone does not satisfy the later native fixture requirement.

LB-H02 through LB-H04 include disabled evolutions, each actual unlocked evolution, low and high current Chaos, burden just below and at 25, 60, and 120, positive fractional burden below 5, and concentrated versus spread-out cadence. At matched supported state, greater burden and higher Chaos cannot reduce intended risk, while the full episode probability remains below certainty and quiet stays possible. A pre-purchase snapshot is not used as the completion-time consequence context. LB-H06 includes high burden with no further purchases and proves all work terminates after its finite horizon.

LB-A01 through LB-A04 compare actual eligibility and willingness scores at 49 PP, 50 PP, just below price plus reserve, exact price plus reserve, and larger surpluses. Add urgent-obligation, shortage, cooldown-expiry, and identical-public-state/different-private-burden fixtures. A protected urgent obligation cannot increase discretionary willingness by itself. Hidden burden and omen risk cannot change purchase policy at otherwise identical public and policy state. Report native scores as scores until a complete adapter establishes a probability model.

### Achievement fixture detail

LB-X01 and LB-X02 include Productive peace with 10 usable civilian factory levels in the saved core-state set and 7 in owned noncore states immediately after reward delivery. The baseline must be 10. Three additional noncore factory levels cannot satisfy the growth condition. Reaching 13 usable civilian levels in the same saved, still-owned-and-controlled core-state set satisfies the factory condition when the other achievement requirements also pass. Newly acquired or newly cored states outside the saved set do not enter either count.

The same achievement fixtures cover an external attack that suspends qualifying peaceful days and then resumes their accumulation without resetting earned days. The original reward, factory baseline, state set, and legitimate contribution evidence remain unchanged. A country-initiated aggressive conflict fails the current attempt under the shared rule.

## Evidence classification

For each scenario, distinguish a planning proof, source-level result, MCP analysis, rendered GUI review, and live-game observation. Record the exact source revision and scenario identity. A missing optional MCP route or live-game observation limits that evidence claim; it does not by itself block otherwise complete source work. If source or an available check demonstrates that required behavior is unsupported or incorrect, report the concrete implementation gap. Never describe source review as observed native behavior.

The assigned `chaosx_ai_probability_auditor` owns read-only numerical checks, representative weighted scenarios, and any requested probability comparison. Do not independently repeat that audit or change weights without parent coordination. If weighted implementation changes are authorized, preserve immutable pre-edit source copies and scenario fixtures for the auditor's comparison; a current file compared with itself is not before-and-after evidence. The same source-identity discipline applies to GUI fixtures, reward receipt cases, and shared Chaos actor mapping.

Full event lifecycle checks must cover the actual helper chain and cleanup paths. Technology or research-bonus changes require the matching technology inspection, render, and comparison workflow. Asset evidence needs actual current runtime bindings and viewed native-size output. Sound licensing, sound playback, and visual timing are separate checks.

The user operates live HOI4 under the project's normal workflow. Agents do not launch the game, request a run, or wait for user evidence. This planning package does not claim game execution, multiplayer testing, native GUI timing, cap support, or final asset production. The implementation handoff records source questions and evidence limits without making optional tools or user testing completion gates.
