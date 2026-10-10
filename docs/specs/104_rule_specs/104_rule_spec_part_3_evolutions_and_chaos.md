# Event 104 Rule: evolutions, counts, and Chaos

## Evolution lifecycle

Rule has exactly the four evolutions in the user brief.
Each has a persistent unlocked state and an independently respected player enable setting.
An unlocked stage contributes its capability only while that stage is enabled.
Disabling a stage does not erase its unlock history or undo any already committed native rule setting.
Reenabling an already unlocked stage restores its capability without another evolution record or Chaos award.

Unlocks persist through later falls in Chaos.
Current Chaos still affects batch size through the formulas below.
Every formula clamps its inputs, so an unlocked high-tier stage continues to have defined behaviour after Chaos falls below its original threshold.

Separate activation eligibility from use of an already unlocked capability.
The inspected shared `is_current_evolution_enabled` helper includes the current Chaos threshold, so its full gate belongs at activation and first-time recording.
An already unlocked capability instead requires its durable unlocked state and an enabled stage setting.
Do not reapply the current threshold through that helper on every firing and accidentally remove a sticky unlock.

### Before the first successful Rule firing

The first occurrence may open in an evolved form.
During preparation, derive the enabled stages whose Chaos requirements are met.
Those stages provisionally contribute to that first batch's count and selection behaviour.
After at least one native rule transition is verified, commit their unlocks and record each newly unlocked enabled stage once.
Record their activation before or consistently alongside the occurrence that used them, according to the shared history ordering contract.
The records must retain their own stage and threshold identities.

A zero-success request commits neither provisional pre-fire unlocks nor a successful occurrence.
It cannot consume an evolution record merely because the world was at high Chaos when an unusable event was selected.
An already unlocked stage remains unlocked if a later request fails.

### After the first successful Rule firing

The persistent Rule system can evolve between firings while the master Rule event setting is enabled.
An enabled locked stage becomes eligible while the master event is enabled, current Chaos is at or above its threshold, and at least one genuine Event 104 change exists in campaign history.
Eligibility enters the stage's dynamic MTTH process.
It does not guarantee activation on the day the threshold is crossed.

The proposed base MTTH parameter is 90 days.
The parameter is multiplied by 0.8 when at least four native rules have been successfully changed by Event 104.
It is multiplied by 0.8 when current Chaos is at least 200 above that stage's requirement.
Both factors can apply, giving a minimum parameter of 57.6 days under this initial tuning.
Use the installed game's verified MTTH handling for fractional values and probability semantics.
The package does not claim that this parameter is a measured mean, median, guaranteed deadline, or exact cumulative probability.
The required probability audit must establish the installed adapter's interpretation.

When Chaos falls below the threshold before activation, the stage is ineligible until the condition returns.
There is no hidden bank of guaranteed progress or catch-up activation.
Disabling a locked stage stops its eligibility without marking it unlocked or recorded.
If it is later enabled before the first successful Rule occurrence, the pre-fire opening rule applies.
If it is enabled after an occurrence, the ordinary active-system MTTH process applies.

Disabling the master Rule event pauses these background MTTH checks and new automatic unlock notifications.
It preserves unlocked stages and all committed native changes.
Reenabling it resumes evaluation under current conditions, with no catch-up draws or backdated guaranteed progress.
A legitimate forced request uses the accepted forced dispatch route and the applicable enabled capabilities, including the pre-first-success evolved opening where relevant.
That explicit request does not resume background evolution checks while the master setting remains disabled.

The implementation should evaluate the four small stage gates through an existing verified global scheduling route or an equivalent event-owned bounded lifecycle.
It must not add a daily, weekly, or monthly scan over every country.
The same global activation cannot receive one independent chance per human player.
If the chosen executor disappears, scheduling must transfer through the shared lifecycle contract without duplicating elapsed evaluations or dropping the system.

### What activation changes immediately

Activation immediately changes Rule's available selection capability, its existing evolution preview and history state, and the parameters used by the next attempted firing.
There is no actor, army, or timed crisis package that needs a second event to receive an upgrade.
Activation itself does not change a native rule.
Actual rule mutations remain tied to Rule firings, preserving the repeatable-event identity.
Each activation has zero direct Chaos impact.

## Capabilities and independent toggles

| Active capability | Effect |
| --- | --- |
| Evolution I | Enables the small one-or-two-rule count profile. |
| Evolution II | Admits historically touched rules into ordinary selection when they have another valid non-default destination. |
| Evolution III | Enables its broader dynamic count profile. It uses fresh rules only when neither II nor IV supplies revision permission. |
| Evolution IV | Enables its larger count profile and its own mixed fresh/revision selection. Revision is intrinsic to this stage's accepted design. |

Count precedence is IV, then III, then I, then the baseline.
Evolution II changes eligibility rather than count.
Revision permission is active when either II or IV is active.
The implementation must not secretly mark a disabled lower stage unlocked to make an enabled higher stage work.

Examples make the toggle semantics concrete.
With I disabled and II enabled, a firing changes one rule and may revise a touched rule.
With II disabled and III enabled, a firing can change several fresh rules but cannot revise touched ones.
With II disabled and IV enabled, IV can still reshuffle touched rules because that behaviour belongs to IV itself.
The evolution preview must explain those independent capabilities clearly enough that disabling II is not presented as a master prohibition on the separate IV feature.

## Shared inputs

`C` is current Chaos, sampled once when the request begins and clamped to the supported 0 to 1000 range for these count formulas.
`F` and `R` are the eligible fresh and revisable sets from Part 2 at preparation time.
Their provenance, the IV footprint count, and each row's fresh or revision classification are frozen by stable native identity before the current request writes anything.
A fresh row changed earlier in this same batch does not count as a revision for this batch's quota, footprint, report, or achievement totals.
`N` is the size of the permitted initial union for the active capabilities.
`B(p)` is a single Bernoulli draw that is one with probability `p` and zero otherwise.
Each count profile uses exactly the indicated count draw.
It does not reroll to reach a preferred outcome.

The requested count is `K = min(N, raw_count)`.
Subsequent compatibility changes, failed candidates, or empty destination sets can lower the actual committed count.
The same count draw is retained for the whole request.
The event's own Chaos award is applied after the batch, so it cannot enlarge its own current count or trigger another free cascade.

## Evolution I: Another Rule

At 200 or more Chaos, Another Rule can unlock.
Its count profile is:

`raw_count = 1 + B(p)`

`p = min(0.65, 0.35 + 0.00075 × max(C - 200, 0))`

This begins with a 35 percent chance of a second requested rule at Chaos 200.
At Chaos 400 the chance is 50 percent.
At Chaos 600 and above it reaches its initial tuning ceiling of 65 percent.
The profile remains small even if later evolution stages are disabled.

Another Rule preserves fresh-only selection unless revision permission is active separately.
Two slots always refer to two distinct native rules.
There is no chance for the second slot to change the first rule a second time.

## Evolution II: Rule Revisions

At 400 or more Chaos, Rule Revisions can unlock.
The fresh and revision pools become eligible together under ordinary selection.
Rules outside the immediately previous batch receive the soft respite described in Part 2.
The picker still selects rules first and valid destinations second.

Every revised destination must be non-default, different from the actual current option, meaningful now, compatible with the batch, and supported by the native writer.
Historical ownership stops being an exclusion but remains available for reporting, Chaos novelty, achievements, and Evolution IV's mix.
No rule's initial player-selected option is treated as a protected destination or mandatory restoration target.

A two-option rule can remain exhausted forever after its first change.
A three-option rule with one default and two non-default options can alternate between those two alternatives if both transitions remain meaningful.
The first visit to a new alternative can earn the limited novelty award below.
Repeated oscillation between already visited settings remains a real gameplay revision but cannot generate unlimited Chaos.

## Evolution III: Rule Cascade

At 600 or more Chaos, Rule Cascade can unlock.
Its count profile is:

`raw_count = 2 + floor(clamp(C - 600, 0, 400) / 200) + B(0.5)`

This produces a requested two or three changes at Chaos 600, three or four at 800, and four or five at 1000.
Compatibility and availability can shorten the batch.
The rule and option draws remain random within their current strata.

The broader wave should change several campaign assumptions in one readable occurrence.
The event does not add a guaranteed war, ideological conversion, faction collapse, or country modifier to amplify a small pool.
If only two compatible rules remain, two actual changes are the complete result.

## Evolution IV: No Stable Rulebook

At 800 or more Chaos, No Stable Rulebook can unlock.
Its count profile is:

`raw_count = min(8, 4 + floor(clamp(C - 800, 0, 200) / 100) + I(|R| >= 4) + B(0.5))`

`I(condition)` is one when the condition is true and zero otherwise.
The extra footprint slot applies when at least four previously changed rules are currently revisable.
It rewards the intended accumulated rulebook with a larger potential reshuffle rather than counting dead, cosmetic, or exhausted history.

The profile requests four or five changes at Chaos 800 in a small revision pool.
With at least four revisable altered rules, it requests five or six.
At Chaos 1000 with that revision footprint, it requests seven or eight.
Eight successful rule changes is the absolute per-firing maximum in this design.

### Mixed selection

IV aims to change a substantial share of the altered rules while continuing to introduce fresh changes.
At request preparation, set a revision target:

`Q = min(ceil(|R| / 2), max(0, K - I(|F| > 0)))`

If a fresh candidate exists, first attempt to secure one fresh successful change.
Then draw revisable rules toward `Q` successful revisions.
Fill any remaining slots from the current permitted union.
Within each category, rules outside the previous successful batch are preferred until exhausted, then recent rules become eligible.
Rule draws and destination draws remain uniform within their current category and recency stratum.

`Q` is an intent for the initial state, not permission to force invalid transitions.
If compatibility removes all candidates of one category, the remaining valid category may fill the batch.
Failed attempts do not count toward the target.
Actual fresh and revised totals appear in the immutable result.
The event never relabels a fresh change as a revision to claim that the mix was achieved.

With six currently revisable rules, three fresh rules, and `K = 6`, the initial revision target is three.
The algorithm first seeks one fresh change, then three revisions, then fills the last two slots from whatever remains valid.
It can produce additional revisions or fresh changes in those final slots.
The example assumes its candidate transitions remain compatible.

## Count examples

The table gives the proposed requested counts before pool and compatibility shortening.
The probabilities and expectations are mathematical consequences of the specified count draws.
They are not live-game timing measurements.

| Active count profile | Chaos | Eligible revisable rules | Requested counts | Expected requested count |
| --- | ---: | ---: | --- | ---: |
| Baseline | 150 | Any | 1 | 1.00 |
| I | 200 | Any | 1 at 65 percent, 2 at 35 percent | 1.35 |
| I | 400 | Any | 1 or 2, equally likely | 1.50 |
| I | 700 | Any | 1 at 35 percent, 2 at 65 percent | 1.65 |
| III | 600 | Any | 2 or 3, equally likely | 2.50 |
| III | 800 | Any | 3 or 4, equally likely | 3.50 |
| III | 1000 | Any | 4 or 5, equally likely | 4.50 |
| IV | 800 | 0 to 3 | 4 or 5, equally likely | 4.50 |
| IV | 800 | At least 4 | 5 or 6, equally likely | 5.50 |
| IV | 900 | At least 4 | 6 or 7, equally likely | 6.50 |
| IV | 1000 | At least 4 | 7 or 8, equally likely | 7.50 |

## Chaos impact philosophy

Chaos comes from verified changes to the campaign's actual operating conditions.
The event picker selecting Rule, the count draw, an evolution unlock, a failed candidate, and the acknowledgement have zero Chaos impact.
An unusual permissive result can be destabilising even when it benefits the player.
A restrictive result is not automatically worth more merely because it is inconvenient.

Chaos credit is based on new native rule states caused by Event 104.
The event keeps hidden provenance and destination-visit records for this purpose.
These are ordinary accounting records and do not create a player currency or management mechanic.

## Chaos impact map

| Material outcome | Starting award | Dynamic basis | Repeat guard | Overlap and counterpart |
| --- | ---: | --- | --- | --- |
| First Event 104 change of a rule | +1, +2, or +3 | +1 when the final batch changes meaningful options for one or two distinct countries, +2 for three to nine, +3 for ten or more. Count countries, not actor-target pairs. | One first-change award per rule for the campaign. | The award represents abnormal rule conditions. Later wars, casualties, annexations, and tension remain owned by their shared sources. Rule produces no restoration-to-default counterpart. |
| First Event 104 use of a different non-default destination on a touched rule | +1 | The transition must still be meaningful at final batch state. | Once per native rule and destination option. A successful destination is marked visited even if the batch cap reduces the final total. | This pays for a novel revision, not the later diplomatic action it enables. |
| Revision to an option previously used by Event 104 | 0 | The gameplay change still occurs and is reported. | The destination-visit record prevents cycling for points. | No artificial award is added to make a repeat feel stronger. |
| Evolution eligibility, activation, or logging | 0 | Capability only. | Unlock and record each enabled stage once. | Any later rule mutations use their own verified result rows. |
| Rejected or zero-success attempt | 0 | No verified material change. | No visited destination or touched flag is added. | No successful firing record or pacing debit. |
| Rule change by another system | 0 from Event 104 | Native current state is accepted as external. | Provenance must identify an Event 104 commit to earn credit. | The other system owns its actual destabilisation or containment accounting. |

Sum the eligible first-change and novel-revision awards after the batch's final compatibility check.
The proposed cap is **+12 Chaos per successful Rule occurrence**.
The cap keeps a large repeatable cascade proportionate while allowing the actual native effects to remain substantial.
It applies to the batch as a whole and does not turn additional committed changes into fake failures.
Store the raw eligible total and the capped applied total in the occurrence's accounting evidence.

The set of visited destinations is finite for a fixed admitted registry.
Revisiting previously used options cannot create an endless Rule-specific Chaos loop.
A newly installed content package or changed rule definition requires an explicit registry migration and evidence update before new identities or destinations become eligible.
Renaming a registry row must not reset novelty credit for the same native rule.

If the actual consumer cannot establish the number of affected countries reliably, use the conservative +1 first-change award for that row and record the evidence limitation.
Do not infer ten affected countries merely because the rule is stored globally.
The membership and meaningfulness proof required for eligibility still applies.

## Shared accounting and forced requests

All entry routes use the same verified change records.
Normal random selection, cluster dispatch, and an authorised manual request cannot each charge the same commit separately.
A cluster burst treats Rule as one development for the shared pacing system.
The Rule-specific Chaos award represents its own native transitions and is applied once through the shared Chaos history path.

Manual force can bypass the shared restrictions that the project's current force mode explicitly allows.
It cannot bypass missing native support, protected settings, invalid destinations, save safety, or impossible current context.
A failed manual request gives the originating human a bounded failure receipt through the available shared feedback contract.
The supplied current documentation names a helper that was not found in the inspected repository revision, so its implementation availability must be resolved before wiring.
The event must not invent success to avoid that integration gap.

## Central tuning anchors

| Anchor | Proposed initial value | Purpose |
| --- | ---: | --- |
| Baseline count | 1 | Preserve the simple opening identity. |
| I second-rule chance at 200 | 0.35 | Make the first evolution occasional rather than automatic. |
| I maximum second-rule chance | 0.65 | Keep the small profile recognisable when later stages are disabled. |
| III base count at 600 | 2 | Start a broader wave without exhausting a modest pool immediately. |
| III Chaos step | 200 | Add one requested slot at 800 and 1000. |
| IV base count at 800 | 4 | Establish a distinct larger reshuffle. |
| IV Chaos step | 100 | Add one requested slot at 900 and 1000. |
| IV revisable-footprint threshold | 4 | Add a slot when the altered set can support a substantial revision. |
| Maximum successful batch | 8 | Bound presentation, selection, and event impact. |
| Active evolution MTTH parameter | 90 days | Allow evolution between successful firings. |
| Evolution parameter factor for four touched rules | 0.8 | Make an established altered world evolve sooner. |
| Evolution parameter factor for 200 extra Chaos | 0.8 | Respond to the current Chaos situation. |
| First-change Chaos bands | +1, +2, +3 | Scale to demonstrated affected-country breadth. |
| Novel revision Chaos | +1 | Credit new options without rewarding endless repetition. |
| Per-occurrence Chaos cap | +12 | Keep the event proportionate within Minor Repeatable pacing. |

Store cross-file values in the project's shared script-constant mechanism where the exact field supports it.
Use verified field-specific alternatives where the parser does not support a runtime value or shared constant.
These anchors can be tuned after scenario evidence, but every change must preserve the user-facing distinction between the four evolutions.
