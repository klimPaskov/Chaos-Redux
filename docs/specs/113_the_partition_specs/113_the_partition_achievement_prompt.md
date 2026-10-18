# 113 The Partition: Achievement implementation and art handoff

Implement the six accepted Event 113 achievements below through the existing Chaos Redux achievement owner and complete all eighteen required 64×64 icon states through `chaos-redux-event-assets`.
These are difficult campaign achievements for defense, foreign protection, policy reversal, recovery, mediation, and aggressive coalition victory.
Each unlock is a conjunction of real events, recorded contributions, exact territorial facts, and a continuous aftermath condition.
An opening event, a signature, one cheap delivery, a favorable final map without history, or the rare super-event's display cannot replace the stated conditions.

Read the current `AGENTS.md`, `.agents/skills/chaos-redux-event-planning/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, and the relevant event, state-ledger, save-inspection, localisation, and subagent guidance before implementation.
Read the accepted Parts 5, 6, 7, 8, 9, and 10 and the asset and coding prompts, with Part 10 as the source design for the achievement conditions.
The complete contracts are repeated here so that the coding and icon workers can receive a self-contained assignment.
All achievement labels, title directions, description directions, and prospective tracking terms are working planning language, not final localisation.
The implementation owner writes final text only after the actual conditions and registered identifiers are verified.

## Inspect and retain the existing owner

Inspect the current files under `common/achievements/`, their enablement and player-identity rules, the owning evaluation and save behavior, and the existing Event 113 ID space before editing.
Inspect `localisation/english/chaosx_achievements_l_english.yml` and `interface/chaosx_achievements.gfx` together with the actual registered icons and state selection.
Retain current source paths, relevant definitions, revisions or hashes, and a collision result for each exact ID.
If the achievement registry has one root `unique_id`, retain that single root-level registry file and add an Event 113 section inside it.
Do not duplicate the root `unique_id` across new event-specific registry files or split the owner merely to match the event's documentation folder.
Keep global enablement, completed-state behavior, and ordinary achievement presentation with that existing owner.

The required achievement IDs are exactly `chaosx_113_unbroken_frontier`, `chaosx_113_three_shields`, `chaosx_113_renounced_share`, `chaosx_113_map_restored`, `chaosx_113_three_settlements`, and `chaosx_113_division_held`.
An existing collision requires an explicit owner disposition before overwriting an achievement or renaming its assets.
Keep a single authoritative ID-to-registry-to-localisation-to-sprite-to-DDS mapping.
Do not invent a working `.gfx` or achievement schema from this prompt.
Use the exact current owner pattern and verify its supported fields against the required local references.

The coding owner implements the registry entries, final localisation, tracking, evaluation, cleanup, and integration.
The `chaosx_icon_artist` produces the six original subjects and complete state triplets, with no gameplay, localisation, GUI, or `.gfx` edits in its asset-only scope.
The main agent reviews the icon sheets, wires the exact existing achievement presentation, and verifies every consumer.

## Shared definitions

An opening form is the form selected when the wave first fires.
Baseline means the original Event 113 opening, Partition Fever is the 200+ evolved opening, and Grand Partitions is the 600+ evolved opening.
An active wave can evolve later without changing its recorded opening form or adding targets.
Every referenced crisis belongs to one immutable wave and one actual target identity generation.
Majors remain ineligible as partition targets, while eligible majors may participate as claimants or protectors.

Opening states are the exact states owned by the target at that crisis's opening.
Opening population and physical industry are frozen facts from that set, with physical industry using the event's civilian and military factory definition rather than trade, occupation, or borrowed industrial capacity.
If opening industry is zero, ignore an industrial ratio test wherever specified and retain the population and other conditions.
Existing cores used by an achievement must be recorded before the crisis opens.
Later manufactured cores, expanded proposals, or newly acquired states cannot replace the stated baseline.

Full prevention is the proven crisis outcome in which the continuing target remains independent, retains all opening states, controls its capital and valid threatened states, has no outstanding award, and faces no remaining relevant partition aggression.
Full prevention by defense additionally requires the actual qualifying partition war and its real end.
The 180-day achievement holds below are stricter than the minimum control facts needed to recognize the event outcome where they expressly require all opening states to be fully controlled.
A completed limited settlement uses actual executed awards, the permitted remnant, and fulfilled obligations.
An interrupted settlement records only the awards that actually happened and must have a concluded loss before a recovery attempt begins.
Complete partition requires actual loss of all target territory to at least two independent recorded claimant beneficiaries under the event's outcome contract.
Single-power conquest and unrelated outside annexation remain distinct outcomes.

Actual delivery means a completed, credited event package backed by matched donor and recipient receipts and the actual resource amounts paid and received.
An accepted promise, displayed fee, failed equipment transfer, returned package, or circular shipment supplies no new delivery credit.
Actual war participation means verified legal entry into the target's relevant defensive or offensive conflict with the stated participants.
A goal, intervention pledge, unrelated war against one claimant, or nominal presence in a merged conflict without the target and relevant attackers cannot supply that history.

The achievement tracker may observe its own qualifying events without requiring a matching Task 101 attachment.
The one-active-Partition-Task limit remains unchanged.
Where an achievement uses the Task D war-participation standard, adopt its observable military rule as stated below rather than requiring the player to hold three Tasks or receive three Task rewards.

## A1 Independent defense

**Exact ID:** `chaosx_113_unbroken_frontier`.
**Working label:** Independent defense, not final localisation.
**Eligible player country:** The continuing target of a baseline opening crisis, independent and minor at opening, outside every faction.
**Visibility:** Visible under the achievement owner's ordinary rules.
**Difficulty:** Hard.

The title direction emphasizes a small country preserving its frontier through its own war effort.
The description direction must identify the baseline target role, multiple actual claimants including a major, independent defense, prohibited event protection, intact territory, and the 180-day hold.
Use compact wording with a fuller requirement tooltip where the current owner supports one.
Receiving an ultimatum must not appear to count as completion progress by itself.

### Required unlock conjunction

1. The attempt begins from a valid baseline crisis against the player's continuing country identity, with a real proposed loss and at least two accepted original claimants.
2. The target is an independent minor outside all factions when that crisis opens.
3. At least two original claimants actually enter war against the target.
4. At least one of those claimants is a major at its actual entry into the target's partition war.
5. The player achieves the verified full-prevention-by-defense outcome.
6. The player remains independent and outside all factions throughout the crisis and qualifying aftermath.
7. No foreign country enters that war on the target's defensive side during the qualifying defense.
8. The target accepts no Event 113 outside protection commitment during the attempt.
9. After the last relevant aggression ends, the target owns and fully controls every opening state for 180 consecutive days.

The target may use its own emergency preparations, supply preparations, and counterproposals.
Ordinary preexisting trade and equipment acquisition are not retroactively classified as prohibited Event 113 protection.
If the active crisis later evolves, retain the baseline opening classification and the actual increased difficulty.
A major claimant defeated through an unrelated outside war does not establish the player's defensive contribution unless its own qualifying partition war and full-prevention outcome occurred.

### Disqualifiers and tracking

Capitulation, subject status, faction membership, acceptance of event protection, or a foreign defensive belligerent disqualifies this attempt.
Any loss of ownership or full control of an opening state during the 180-day postwar hold permanently fails this crisis's attempt.
Restoring that state later does not restart the failed attempt's timer.
A later eligible crisis is a separate attempt subject to the normal 540-day reselection protection.

Record the opening player and target identity generation, opening state set, minor and faction facts, first valid demand, original claimants, real war participants, each claimant's major status at entry, accepted protection history, capitulation history, relevant aggression end, and hold start or interruption.
Do not reconstruct these histories from current guarantees or a final war roster after the evidence has disappeared.

The challenge requires the player to defeat an actual multi-country war while declining the event's direct foreign protection route and then keep the whole frontier intact.
The completed icon is an intact border marker behind a battered field shield, with an undivided map line.
Its palette and texture should convey endurance and cost rather than effortless triumph.

## A2 Three simultaneous shields

**Exact ID:** `chaosx_113_three_shields`.
**Working label:** Three simultaneous shields, not final localisation.
**Eligible player country:** An independent country that is neither a target nor a claimant in the qualifying wave.
**Visibility:** Visible under the achievement owner's ordinary rules.
**Difficulty:** Extreme.

The title direction suggests one foreign power holding several independent countries together through a wider crisis.
The description direction must state three distinct targets from the same Grand opening wave, actual defense of all three, one material delivery, and intact independent survival through the common hold.
The wording must distinguish protecting three countries from winning three battles around one target.

### Required unlock conjunction

1. Three distinct crises come from one wave that opened as Grand Partitions.
2. The player accepts a legal defensive commitment to each while that target's crisis remains unresolved.
3. The player is not a target or claimant in that wave.
4. The three commitments obey the ordinary three-commitment cap and occupy its three available slots.
5. Every protected target enters an actual partition war against at least two recorded claimants.
6. At least one actual attacking claimant across the three wars is a major.
7. The player legally enters the defense of every target and satisfies the Task D actual-war-participation standard for each distinct crisis.
8. After accepting a relevant commitment, the player completes a credited arms delivery to at least one of the three targets.
9. All three targets obtain verified full prevention.
10. Beginning after the last of the three qualifying wars ends, all three targets remain independent and own and fully control every opening state for the same 180 consecutive days.
11. The protector remains independent during that common hold.

For the military participation rule, require actual continued participation for at least 30 days before that target's resolution.
The exception applies only when the entire relevant war lasts less than 30 days, the player enters within five days of the first verified crisis attack, and it stays until the relevant aggression ends.
A merged war can satisfy more than one crisis record only when each protected target and its relevant attackers are actually present and the dates satisfy that target's contribution rule.
The single required arms delivery is additional to the military participation across all three targets.
It does not replace a missing defensive entry.

### Disqualifiers and tracking

Any qualifying target's extinction, subjection, concluded territorial loss, or incomplete defense breaks the attempt.
A pledge without actual entry, a war elsewhere against an otherwise relevant country, or three records attached to one target cannot qualify.
Losing the protector's independence during the common hold prevents completion.

Track one wave ID, three distinct crisis and target identity records, each accepted commitment date, actual entry and exit dates, first attack dates, rosters, attacking major evidence, the arms delivery receipt, all three full-prevention outcomes, and the common hold start and interruptions.
Keep the outcomes distinct even if their wars merge.
This independent achievement observer does not create or consume extra Task slots.

The challenge is to distribute real military and material support across three fronts and preserve every protected country intact.
The completed icon shows three distinct small shields beneath one larger defensive canopy, with no annexation symbolism.
Keep all three subjects readable at 64×64 without turning them into a numbered label.

## A3 Renunciation followed by protection

**Exact ID:** `chaosx_113_renounced_share`.
**Working label:** Renunciation followed by protection, not final localisation.
**Eligible player country:** An independent accepted claimant in a Partition Fever or Grand Partitions crisis.
**Visibility:** Hidden until the qualifying full renunciation is recorded.
**Difficulty:** Very hard.

The title direction expresses a costly reversal of policy without celebrating the original coercion.
The description direction must identify the abandoned preexisting core demand, full withdrawal, delayed target-approved protection, both actual aid deliveries, and durable survival.
The hidden reveal should expose an earned route opportunity rather than disclose an automatic reward for pressing withdraw.

### Required unlock conjunction

1. The player begins as an accepted claimant in an evolved crisis.
2. The first valid public demand is a complete partition with at least three claimants.
3. At least one other claimant is a major.
4. The player's initial assigned share contains at least one state that was already its core before the crisis opened.
5. Before receiving any award, the player fully withdraws every territorial demand through C4.
6. That full withdrawal closes claimant reentry for this crisis and starts the ordinary renunciation period.
7. At least 15 days later, the target explicitly accepts the former claimant as a legal protector under V3.
8. The player then delivers both one credited arms package and one credited transport package from its actual reserves.
9. The target obtains full prevention or a completed limited settlement that preserves its capital and at least 50% of both opening population and opening physical industry.
10. Ignore the industrial percentage only if the opening industry total was zero.
11. The target remains independent and those outcome or settlement conditions hold for 180 consecutive days after the relevant outcome.
12. The player receives none of the target's opening states by any method from crisis opening through the qualifying hold.

The arms and transport packages remain separate actual actions with their ordinary caps, quotes, and delivery receipts.
The protection relationship requires the target's explicit consent and the real legal route after the 15-day separation.
A core gained after opening, an unassigned state wanted only after joining, or a partial demand reduction cannot create the qualifying renunciation.
The event's ordinary 540-day renunciation policy and the permanent closure of claimant reentry for this crisis remain in force.

### Disqualifiers and tracking

A direct award, later acquisition of any qualifying opening state, renewed claimant role, aggression against the target, unpaid delivery, or target extinction disqualifies the attempt.
The player cannot withdraw a valueless late claim, reuse an undelivered pledge, or claim credit for a target's success without the subsequent accepted protection and both real packages.
During the 180-day hold, a broken settlement, loss of the target's retained capital control, or failure of its required independence, retained-population floor, or applicable industry floor permanently fails this attempt.
Restoring those conditions later does not restart the failed attempt's timer.

Track the preopening core facts, first valid public complete allocation, original claimant count, other major claimant, withdrawal timestamp, closed claimant authority, target protection acceptance, both delivery receipts, retained ratios, every recipient of an opening state, outcome date, and hold record.
Keep that negative ownership history through the hold instead of checking only the final map.

The challenge combines abandoned territorial value, real aid expenditure, a target's voluntary acceptance, and a durable result.
The completed icon combines a folded territorial demand and open protective hand, with a broken seal as a secondary motif.
Use an ordinary human hand as symbolic art without turning the icon into an identifiable person.

## A4 Recover the opening map

**Exact ID:** `chaosx_113_map_restored`.
**Working label:** Recover the opening map, not final localisation.
**Eligible player country:** The continuing independent target identity surviving an evolved limited partition or concluded interrupted settlement.
**Visibility:** Visible after a qualifying actual loss.
**Difficulty:** Very hard.

The title direction communicates recovery from an executed partition.
The description direction must identify the substantial real loss, at least two recipients, an actual recovery war, the 1,080-day restoration deadline, and the subsequent 180-day hold.
The player should understand that cancelling an unexecuted proposal or receiving a free restoration cannot satisfy the challenge.

### Required unlock conjunction

1. An evolved crisis concludes with a limited or interrupted settlement that leaves the player's continuing target identity independent.
2. Its actually awarded states contain at least 25% of opening population or at least 50% of opening physical industry.
3. Ignore the industrial branch when its denominator is zero.
4. At least two distinct recorded claimants receive target states in that concluded loss.
5. Within 1,080 days of the loss conclusion, the player owns and fully controls every opening state.
6. At least one originally awarded state returns through the player's actual war against a recorded recipient and the resulting native occupation or peace outcome.
7. From the completed restoration, every opening state remains owned and fully controlled for 180 consecutive days.
8. The player retains the same country identity and independence from the concluded partition through that hold.

Additional ordinary territory is permitted and cannot substitute for a missing opening state.
A purely diplomatic return of every lost state does not satisfy the military recovery condition.
Restored ownership without actual full control begins no hold.
The event supplies neither free cores nor an automatic territorial restoration for the achievement.
A restoration completed before the 1,080-day deadline may finish its 180-day hold afterward.

### Disqualifiers and tracking

Extinction followed by recreation cannot continue the original attempt.
Subject status, identity substitution, missing the restoration deadline, or a later loss during the qualifying hold prevents completion of that attempt.
An unrelated map change that happens to return all states supplies no recovery-war provenance by itself.

Track opening and awarded state sets, snapshot loss population and industry, original recipient identities, loss conclusion date, actual recovery-war participants and territorial provenance, full restoration date, deadline, and continuous hold.
Keep the record through the full recovery window even after the crisis's active negotiation and war rows close.
Retain exact dates so a late interface refresh can recognize a restoration that actually occurred before the deadline without rewarding one that occurred afterward.

The challenge turns a substantial defeat into a long campaign objective that requires military recovery and continued sovereignty.
The completed icon shows torn map pieces rejoined around the original capital marker with restrained restoration light.
Its torn and repaired structure should remain readable without a labeled map or an exact country silhouette.

## A5 Three durable settlements

**Exact ID:** `chaosx_113_three_settlements`.
**Working label:** Three durable settlements, not final localisation.
**Eligible player country:** An independent target-invited mediator receiving no territory from the three qualifying targets.
**Visibility:** Visible under the achievement owner's ordinary rules.
**Difficulty:** Extreme.

The title direction evokes repeated difficult diplomacy across one regional crisis.
The description direction must state three distinct targets from the same evolved opening wave, a complete-partition threat, an actual major claimant, the mediator's material improvements, prevention of partition war during negotiation, and the common 180-day hold.
A meeting, invitation, inherited concession, or unsigned proposal must not read as a finished settlement.

### Required unlock conjunction

1. Three distinct target crises come from one wave that opened as Partition Fever or Grand Partitions.
2. Each target invites the player as mediator, and all three roles are accepted before any of their final settlements are ratified.
3. At least one first valid public demand is a complete partition.
4. At least one actual claimant across the three crises is a major.
5. For every target, the player produces the material improvement required by Task S against the immutable first valid public demand, bound when mediation is accepted.
6. The credited proposal also materially improves the then-current offer after the player's own mediation acceptance.
7. Every target obtains a completed limited settlement or an all-party binding no-transfer withdrawal.
8. Every limited settlement preserves the capital and at least 50% of opening population and physical industry, with a zero industrial denominator ignored.
9. No partition aggression begins against any of the three targets from the player's mediation acceptance through final ratification of that target's agreement.
10. All three results hold for 180 consecutive days after the last final agreement is executed.
11. Each target remains independent and every due treaty promise is fulfilled during the hold.
12. The player receives none of the three targets' opening states from the first mediation acceptance through the hold and never participates as a claimant anywhere in the qualifying wave.

For the improvement rule, the proposal must remove at least one demanded state, replace complete partition with a viable limited settlement, or secure an all-claimant no-transfer withdrawal.
Bind the original first public demand rather than a harsher proposal created after the player joins.
Retain the then-current offer at participation as separate evidence that the mediator made a new material contribution.
Repeating another negotiator's completed concession cannot qualify.
A no-transfer withdrawal qualifies only when every remaining claimant renounces its current demand and the outcome record proves full prevention.
Unrelated ordinary wars elsewhere do not automatically invalidate the diplomacy route.

### Disqualifiers and tracking

Claimant participation in the wave, a new partition war during the specified negotiation interval, incomplete awards, broken material promises, target extinction, or the player's receipt of an opening state disqualifies the attempt.
Three records for one target, observer attendance, duplicate signatures, and improvements authored before the player joined cannot supply the required contribution.

Track the three target invitations, role acceptance dates, first valid public demand and then-current offer for each, player-authored material improvements, required consents, partition-war timelines, final ratification and execution dates, executed awards and material promises, all recipients of opening states, and the common hold.
Keep the three outcome records distinct even when the same claimant or mediator appears in all of them.
No extra Task attachment or reward is required for this achievement observer.

The challenge requires coordinating several signatory groups before short deadlines while bearing actual mediation costs and preserving each country through the aftermath.
The completed icon shows three sealed agreements arranged around three surviving capital markers.
Use the three-way composition to distinguish it clearly from the protective shields and aggressive division icons.

## A6 Keep the division together

**Exact ID:** `chaosx_113_division_held`.
**Working label:** Keep the division together, not final localisation.
**Eligible player country:** An independent claimant, minor or major, participating in two target crises from the same Grand opening wave.
**Visibility:** Hidden until the two qualifying wars begin.
**Difficulty:** Extreme.

The title direction is cold and political, emphasizing the durability of an aggressive coalition's division.
The description direction must plainly identify two actual complete partitions, target resistance, a major defender, the player's gains, fulfilled partner shares, united coalitions, and the long hold.
The presentation should acknowledge coercion and consequence without describing every territorial loss as the target's willing agreement.

### Required unlock conjunction

1. The player is an independent claimant in two different target crises from the same wave that opened as Grand Partitions.
2. Both targets reject the division and enter actual native wars against the player and at least one other recorded claimant.
3. At least one major power actually enters on a target's defensive side across those two wars.
4. Each target reaches the verified complete-partition outcome with at least two independent claimant beneficiaries.
5. The player receives at least one state from each target and at least five of those target states in total.
6. Every claimant that remained committed when enforcement began receives every state assigned to it in the last unanimously ratified claimant division before that enforcement.
7. The actual native war and peace result matches those promised shares.
8. Coalition Cohesion is at least 75, the united band, when each final partition outcome is recorded.
9. No pair of recorded claimant partners enters war against one another from the first enforcement through the final hold.
10. Every beneficiary remains independent and retains its awarded states for 180 consecutive days after the second complete partition.
11. The player's own independence and country identity continue throughout the attempt and hold.

Claimant signatures record their proposed division and never replace target consent to a peaceful transfer.
The achievement requires actual wars and native outcomes because both targets rejected the division.
Preserve each enforcement allocation version and all committed signatories so a later smaller promise cannot erase an unmet share.
Voluntary extinction and unrelated outside conquest cannot qualify.
The rare super-event may occur during this route, but it is a separate presentation trigger with its own conditions.
Its display, ten-state threshold, and 180-day interval between partitions are not additional achievement conditions.

### Disqualifiers and tracking

A single-power annexation, missed partner share, opportunistic seizure from a partner, subject beneficiary, claimant betrayal, or loss of an awarded state during the hold disqualifies the attempt.
Taking five states without both complete-partition outcomes cannot qualify.
Ratifying a division that the native peace does not honor cannot qualify.
One country's artificial appearance in two records cannot replace two target identities.

Track both crisis IDs, the common Grand opening wave, player and target identities, target refusals, actual attacker and defender rosters, major defensive entry, final pre-enforcement claimant allocation versions, all enforcement signatories, actual state owners and awards, Cohesion at each completion, claimant war relationships, beneficiary independence, and the 180-day common hold.
The surviving observer must retain this record when the targets cease to own territory.

The challenge is to win two wider wars and keep a fragile division intact among competing powers.
The completed icon shows two divided maps beneath a single iron compass with distinct beneficiary colors and an austere tone.
The same palette family may connect it to the event, while its subject remains independently generated achievement art.

## Shared tracking and evaluation contract

Create a bounded attempt record only when an achievement's first qualifying real condition occurs.
Bind it to the current player country identity, its identity generation, the exact achievement ID, immutable wave and crisis IDs, and required opening snapshots.
Do not backfill a qualifying history from a current final map when records of its causes are missing.
Player switching cannot transfer one country's attempt to another identity.
Country extinction, recreation, subject change, or ambiguous identity transformation follows the achievement's stated disqualifiers and the current owner's identity rules.

Keep the distinction between a failed attempt and permanent achievement ineligibility.
A failed attempt must not erase the possibility of a later separate qualifying Event 113 crisis when the same country and owner rules allow it.
Completed achievements remain completed through the owner rather than being relocked when a later campaign changes conditions.
Hidden reveal and not-eligible presentation use actual eligibility facts and must not expose false progress or a stale raw tracking key.

Each hold starts only when all of that achievement's required conditions are simultaneously true.
Store its absolute start date, the first qualifying actual outcome date, and any interruption or disqualifier with its reason.
Do not accumulate nonconsecutive periods into a 180-day hold.
Record a route's stated permanent failure without restarting that same attempt, and keep a later independently qualifying attempt separate.
Process outcomes and their actual timestamps before deadline failure when both occur on the same date.
A valid restoration or outcome recorded by its deadline can be consumed after an interface refresh, while one that occurred afterward cannot earn retroactive credit.

Reuse the event's actual award, delivery, consent, war, outcome, and durability evidence.
Avoid a second invented participant list or aggregate success flag that could conflate different targets.
The crisis observer must survive target extinction where a claimant achievement still requires the outcome.
Keep the immutable first public demand separate from current proposal versions and later amendments.
For A5, additionally retain the offer present when the player became mediator and the change attributable to its later proposal.
For A6, retain the last unanimously ratified claimant allocation before enforcement even after the coalition or target's active scopes retire.

Use event-driven facts, existing bounded participant observation, and absolute scheduled due dates under the verified current owner.
Do not add an unlimited whole-world daily scan to support these achievements.
Retain detailed history only while a Task, achievement attempt, hold, event log requirement, or restoration window still needs it.
After every dependent observer closes, reduce the crisis data to its approved terminal summary and clean up owned transient state once.
Save and load preserve identity, dates, receipts, and consumed-unlock state without granting elapsed time, replaying deliveries, or awarding twice.

Implement the conditions with supported engine effects, triggers, scope rules, and current helper contracts established from installed documentation and the offline wiki.
An unverified war relationship, ownership transition, native achievement field, or save behavior remains a concrete implementation blocker until inspected.
The planning package provides acceptance conditions rather than executable parser snippets or a claim that these bindings already exist.

## Icon production contract

Use `chaosx_icon_artist` with the current `chaos-redux-event-assets` skill and the exact six IDs and motifs above.
Inspect the canonical reference root at `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/gfx_references`.
Read `README.md`, `CATALOG.md`, `icons/achievements/contact_sheet.png`, and the matching individual achievement examples before generation.
The reference art supplies style and composition guidance and must never become the shipped subject.

Generate one original subject per achievement with a genuinely transparent background, no achievement frame, square backdrop, red cross, text, or fake checkerboard.
Keep the full generated source, exact prompt and arguments, references with declared roles, candidate lineage, SHA-256, source/native-size reviews, and explicit final selection.
Process the subject into one centered transparent 64×64 color layer with intact edges and suitable native readability.
Grey and not-eligible variants are deterministic derivatives of that exact subject, not separately generated scenes or resized icons from another family.

Use the following exact supplied 64×64 workflow inputs without moving, resizing, cropping, recoloring, redrawing, filtering, or replacing them.

| Input relative to canonical root | Required SHA-256 | Required use |
| --- | --- | --- |
| `icons/achievements/template/achievement_template.png` | `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA` | Background under the completed color subject |
| `icons/achievements/template/achievement_template_grey.png` | `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022` | Background under both grey and not-eligible sources |
| `icons/achievements/template/overlay.png` | `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD` | Unchanged red-cross overlay on the grey subject for the not-eligible source |

The completed source is the processed transparent color subject unchanged.
Create the grey source by deterministic grayscale conversion with its canvas, position, and alpha unchanged.
Create the not-eligible source by compositing the unchanged overlay above the grey source at exact native alignment.
Provide all three complete source layers to `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py` through its verified current CLI.
Use a separate output directory and retain all three composited review PNGs, the complete source triplet, and the original generated master.
The processor applies the supplied backgrounds and creates the final DDS states.
Do not run the generic single-image converter independently on the three final achievement states.
Do not feed processed outputs back as source layers or use a reprocessing exception without an explicit intentional replacement decision.

For an existing ID that is deliberately migrated, follow the existing-triplet migration contract with the exact supplied completed, grey, and not-eligible source layers.
A missing inherited state remains a migration blocker and must not be silently recreated from an unrelated final output.

### Exact runtime output map

| Achievement ID | Completed | Grey | Not eligible |
| --- | --- | --- | --- |
| `chaosx_113_unbroken_frontier` | `gfx/achievements/chaosx_113_unbroken_frontier.dds` | `gfx/achievements/chaosx_113_unbroken_frontier_grey.dds` | `gfx/achievements/chaosx_113_unbroken_frontier_not_eligible.dds` |
| `chaosx_113_three_shields` | `gfx/achievements/chaosx_113_three_shields.dds` | `gfx/achievements/chaosx_113_three_shields_grey.dds` | `gfx/achievements/chaosx_113_three_shields_not_eligible.dds` |
| `chaosx_113_renounced_share` | `gfx/achievements/chaosx_113_renounced_share.dds` | `gfx/achievements/chaosx_113_renounced_share_grey.dds` | `gfx/achievements/chaosx_113_renounced_share_not_eligible.dds` |
| `chaosx_113_map_restored` | `gfx/achievements/chaosx_113_map_restored.dds` | `gfx/achievements/chaosx_113_map_restored_grey.dds` | `gfx/achievements/chaosx_113_map_restored_not_eligible.dds` |
| `chaosx_113_three_settlements` | `gfx/achievements/chaosx_113_three_settlements.dds` | `gfx/achievements/chaosx_113_three_settlements_grey.dds` | `gfx/achievements/chaosx_113_three_settlements_not_eligible.dds` |
| `chaosx_113_division_held` | `gfx/achievements/chaosx_113_division_held.dds` | `gfx/achievements/chaosx_113_division_held_grey.dds` | `gfx/achievements/chaosx_113_division_held_not_eligible.dds` |

These are eighteen exact root-level files under `gfx/achievements/`.
The achievement ID supplies the final basename without an additional prefix or Event 113 subfolder.
Register or retain every actual completed, grey, and not-eligible sprite alias through `interface/chaosx_achievements.gfx` using the current owner's exact pattern.
Record the registry entry, English localisation keys, all aliases, final paths, and live state consumers in one row-level crosswalk.

Every output must decode as strict one-level 64×64 legacy BGRA DDS and have pixels exactly equal to the required untouched background beneath its exact source layer.
Check the converter's header and masks, exact length, canvas, alpha, and absence of unrequested mipmaps.
The ordinary 64×64 one-level BGRA file length is 16,512 bytes under that verified contract.
A tolerant source decoder never relaxes final output validation.
Inspect a native-size six-achievement triplet contact sheet and enlarged comparisons for alignment, silhouette, template integrity, color and grey distinction, unchanged red crosses, and clean edges.
The main agent must visually review those sheets before final integration.

## Localisation and presentation

Write final title and description text from the route directions after implementation proves the exact conditions.
Keep the wording focused on what the player must accomplish and what invalidates progress.
Show meaningful progress such as qualifying targets, actual outcomes, remaining hold time, recovery deadline, and missing participation in the owner's supported tooltip or achievement detail surface.
Do not expose internal flags, raw IDs, source revisions, or implementation history to the player.
Dynamic country and state names come from the actual bound identities rather than a fixed historical list.

Use the owner's existing visible, hidden, grey, completed, and not-eligible behavior.
For A3, reveal only after its qualifying full renunciation rather than an arbitrary withdrawal.
For A4, reveal after the substantial actual loss and two-recipient condition.
For A6, reveal when its two qualifying target wars begin.
Keep reveal flags separate from unlock flags and preserve completed state once the owner grants it.
The ordinary visible achievements remain assessable before their special campaign situation appears, subject to current global achievement rules.

A failed attempt can explain its concrete reason without declaring the entire achievement permanently impossible when a later independent attempt is legal.
A hidden condition must not cause an invisible reward or a mistaken completed icon before every unlock condition is met.
The native three-state icon selection and final text need a reviewed live consumer, not only a file inventory.

## Required acceptance cases

Run the relevant source, supported engine, save-observation, and native UI checks through the current owners and record the limits of each kind of evidence.
Use the package's full acceptance matrix together with these achievement-specific cases.
These are expected results for future implementation verification, not tests already run by the planning agent.

| Case | Scenario | Required result |
| --- | --- | --- |
| A1 success | Baseline minor fights two original claimants including one actual major, accepts no event protection or defensive ally, then holds every opening state for 180 days | One unlock after the complete hold |
| A1 disqualification | The same defense accepts foreign protection, joins a faction, capitulates, or gains a foreign defensive belligerent | Attempt disqualified even if the final map is intact |
| A1 hold loss | Any opening state loses ownership or full control during the postwar hold and later returns | This crisis's attempt permanently fails with no timer restart |
| A1 opening memory | A baseline opening later evolves during the actual war | Baseline achievement route remains valid if all other conditions hold |
| A2 distinct targets | Three legal commitments and actual defenses belong to three targets in one Grand opening wave | Three independent outcome and participation records |
| A2 merged war | The actual merged roster contains only two protected targets or omits one target's relevant attackers | Missing third contribution, no unlock |
| A2 short war | One relevant war lasts under 30 days | Credit only with entry within five days of its first attack and continued participation through resolution |
| A2 nominal support | Three pledges exist but one target receives no real military entry | No unlock regardless of surviving final borders |
| A3 genuine reversal | Valid complete demand includes a preopening core, full withdrawal precedes all awards, target accepts after 15 days, both aid packages arrive, and the durable result qualifies | Attempt can complete after its full hold |
| A3 invalid baseline | The player's core is created after opening or it only reduces part of its demand | No qualifying renunciation |
| A3 territorial profit | The player receives an opening state later during protection or the hold | Attempt disqualified |
| A3 hold breach | A settlement breaks, retained capital control is lost, or required independence or retained ratios fail during the hold | Attempt permanently fails even if the condition is later repaired |
| A4 actual recovery | Substantial two-recipient loss is restored within 1,080 days with actual military recovery provenance, then held for 180 days | One unlock even when the hold ends after the restoration deadline |
| A4 timing | Full restoration happens after the deadline or ownership returns without full control | No qualifying restoration |
| A4 recreated country | The original target becomes extinct and a later country uses the same tag | No inheritance of the original attempt |
| A5 new contribution | All three mediations improve the immutable first demand and the then-current offer after the player joins | Material contribution recorded individually |
| A5 inherited concession | The mediator repeats an improvement already completed before its participation | No contribution credit for that target |
| A5 war breach | A relevant partition attack begins between mediation acceptance and that target's final ratification | Attempt disqualified despite a later peaceful map |
| A5 durable outcome | All three agreements execute, preserve the stricter remnant, and hold for 180 days with every promise fulfilled | One unlock after the common hold |
| A6 partner shares | Two resisted complete partitions occur but one enforcement signatory receives less than its saved promised allocation | Attempt disqualified |
| A6 major defender | The player defeats two targets without a major actually joining either defensive side | No unlock |
| A6 durable division | Both complete partitions meet every personal and coalition condition and all beneficiaries hold their awards independently for 180 days | One unlock without requiring the super-event to display |
| Persistence | Save and load occurs during a hold, restoration window, or consumed unlock | Exact dates and receipts retained with no extra days or duplicate unlock |
| Cleanup | A target scope disappears while an A6 record or A4 window is still required | Surviving observer retains required history until the dependent attempt ends |
| Identity | The player switches country or a tag is recycled | Attempt remains bound to the original identity and cannot transfer |
| Same-date boundary | A restoration or hold completion is recorded on its deadline date | Use the actual timestamp before timeout and never credit a later event retroactively |
| Icon coverage | Registry, aliases, and consumers are audited after all art is delivered | Six IDs and all eighteen exact state files resolve with correct pixels and visibility |

Provide a final achievement completion report listing the owning registry, exact IDs, condition and tracking coverage, real verification scenarios, localisation, all icon states, current consumer evidence, and remaining blockers.
Source-only review, a static planning check, or the absence of parser errors cannot prove campaign history or native state presentation.
The implementation owner must resolve every missing condition, asset, source, or required validation route before claiming the achievement package complete.
