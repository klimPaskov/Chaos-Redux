# 106 Resistance, Part 4: Recovery, Chaos, and achievements

## The occupation after the wave

The immediate increase creates a new demand on the occupier's existing resources and policies. The player decides how much of the war effort to commit to holding foreign territory. A well supplied garrison and favourable native recovery conditions can bring resistance down again. An overstretched country may face losses and disruption in several occupied homelands at once.

Use the installed occupation system's manpower, equipment, garrison template, law, compliance, and intelligence rules. The specification does not invent a fixed recovery rate or promise that a particular law always solves the problem. Their exact effects depend on the supported game version and the campaign's active modifiers.

The important tradeoff is practical. Resources used by occupation forces compete with other needs. Recovering recently pacified territory can delay the occupier's next offensive. A country whose homeland is occupied may exploit the same pressure through its existing army, diplomacy, and supported liberation routes.

### Campaign response matrix

| Situation | Meaningful response | What remains uncertain |
| --- | --- | --- |
| A small occupier with one foreign state | Review that occupation's garrison supply and policy before expanding further | Whether native recovery will outpace losses after the shock |
| An empire with several occupied homelands | Prioritize equipment and manpower across exposed occupations, taking account of local resistance and compliance | Which local movements a later 095 firing will find ready |
| A well established annexed occupation | Use its stronger compliance and supply position to recover the immediate rise | High compliance helps the aftermath but never cancels the wave |
| A subject holding foreign territory | Manage the subject's actual occupation under its own controller identity | Whether existing support from its overlord is enough under the native rules |
| A dispossessed human country that remains playable | Use the occupier's strain as an opportunity to recover its actual cores | Resistance does not promise a friendly uprising or a successful war |
| Several rival occupations of one homeland | Pursue each remaining occupying side and the current state of the homeland | A revolt against one occupier does not automatically settle the others |

## AI behavior

The world wave treats AI and human controllers equally. AI countries receive no automatic resistance reduction, free garrison equipment, cheaper occupation law, or immunity as compensation.

Their response uses the existing occupation AI. Validation must establish that the new resistance levels become visible to its ordinary garrison and equipment decisions. The native system already has a relationship between resistance, garrison losses, and equipment management, as the developer's public account describes in evidence item E06. The exact installed behavior still needs an observed scenario.

| AI role | Required behavior and evidence |
| --- | --- |
| Minor or major occupier | Receives every valid state addition and continues to manage garrison requirements through native occupation behavior |
| Subject occupier | Uses its own controlled states, with no duplicate processing through its overlord |
| Strongly supplied occupier | Can recover under its genuine native modifiers, without a 106-only hidden exemption |
| Occupier with weak supply or low compliance | Bears the resulting local risk and can face a stronger 095 response through the same public contract as a human occupier |
| Existing homeland country | Uses its normal military and political behavior, while 095 owns any uprising decisions and forces |
| Newly restored country or active revolt | Uses the country and military AI established by its actual owner event |

There is no random choice inside the 106 addition. The relevant weighted surfaces are the shared repeatable picker and the 095 candidate response defined in Part 3. Their probability handoffs must distinguish an event-selection probability, an independent uprising roll, an AI willingness score, and native behavior that the available tools cannot quantify.

## Chaos from actual new pressure

Let `D` be the sum of the actual positive resistance additions in this wave, measured in percentage points across all valid states. This is an internal calculation. A state moving from 90 to 100 contributes 10, regardless of the nominal wave strength. A state already at 100 contributes zero.

Use the following initial calibration. These values are parent-selected design additions under the user's request for a full expansion. They are tunable balance anchors, separate from the user's fixed wave amounts and evolution thresholds.

| This wave's actual sum `D` | Direct Chaos award before guards |
| --- | ---: |
| 0 | 0 |
| More than 0 and less than 25 | 0 |
| At least 25 and less than 250 | +2 |
| At least 250 and less than 1000 | +3 |
| At least 1000 | +5 |

Ten uncapped baseline additions produce `D = 250`. Forty produce `D = 1000`. Evolved waves reach a band through the resistance they actually add. Current Chaos does not multiply that award again.

### Repetition limits

Award positive 106 Chaos at most once every 90 elapsed days worldwide. The first eligible credited wave starts that clock. Day 90 is eligible again. Keep a gross lifetime positive ceiling of +30 for this event family across all countries, stages, and firing routes.

When a wave qualifies, its proposed gain is the smaller of the table amount and the remaining lifetime allowance. A final allowance of 1 permits a final +1. Only a positive gain actually accepted by the shared Chaos system consumes the time gate and lifetime allowance. A suppressed or zero gain creates no later reduction credit.

There is no carried balance. A wave with `D = 24` gives zero. Two such waves still give zero. A qualifying wave during the 90-day gate still changes resistance and local history, but its blocked Chaos amount is discarded. A later wave must qualify through its own actual additions.

Save and reload, stage changes, controller changes, settings changes, duplicate delivery, and completed containment do not reset the gross lifetime total. Reductions never reopen the positive allowance.

## Chaos impact map

| Milestone or outcome | Why Chaos changes | Direction and starting amount | Dynamic factors | Repeat guard | Shared-source overlap | Containment counterpart |
| --- | --- | --- | --- | --- | --- | --- |
| A qualifying wave adds resistance to occupied territory | A real new burden of instability has appeared | +2, +3, or +5 | Actual sum `D`, remaining lifetime allowance, elapsed time since credited gain | One gain per 90 days, +30 gross lifetime, one credit per wave | Counts the added occupation pressure only | Its frozen affected footprint can earn a limited reduction |
| An empty wave, a fully capped wave, or `D < 25` | This firing creates no qualifying new burden under the chosen bands | 0 | This wave's actual result only | No carryover or deferred award | Nothing duplicated | Creates no refundable credit |
| An evolution activates or is logged | Future capability changes without a new wave | 0 | Highest active stage changes future `A` | One stage history record, no Chaos award | Nothing duplicated | No reduction owed |
| 095 turns local conditions into an armed outcome | Country creation, troops, and wars belong to that outcome's owner | 0 additional from 106 for the armed outcome | 095 consumes the valid local support from Part 3 | 095 owns committed outcome receipts | Its wars and losses remain with their existing shared sources | 106 cannot refund those separate outcomes |
| A credited footprint recovers at both required checks | Most of the credited pressure has been brought back under control | Up to -1 for a +2 or +3 credit, or -2 for a +5 credit | Original affected weights, observed recovery, remaining reduction allowance | One settlement per credited wave, -10 gross lifetime ceiling | Counts recovery of resistance, not peace, deaths, or territorial transfer | Consumes the original credit once |

## A finite containment return

Only a wave with actual credited Chaos opens a containment record. Freeze every state that gained resistance in that wave, its original occupier, its occupation episode, its pre-wave resistance, and the actual addition. The actual addition is that state's fixed weight. The sum of those original weights remains the denominator for the entire record.

Check that fixed footprint at 180 and 270 elapsed days after the wave. A state contributes its weight to the final qualifying intersection only if it satisfies all the following at both observations and remains valid at settlement:

- The original occupier still directly controls it, and the original occupation episode remains valid.
- It has had no intervening control loss, transfer, release, or conversion into the occupier's core.
- Current resistance is at most its pre-wave resistance and at most 25.
- No later positive 106 addition has superseded this state's contribution to that containment record.

The same states must pass both observations. It is insufficient for one group to supply 75% at day 180 and a different group to supply 75% at day 270.

Lost, released, transferred, cored, or otherwise invalid states contribute zero while retaining their original denominator weight. A vanished controller contributes no qualifying weight. An original high-weight state cannot be removed to make the remaining footprint easier.

A later positive 106 write permanently disqualifies that state's contribution to the older pending containment record. This also applies when the later wave received no Chaos award. A capped write of zero does not supersede it. Later recovery can therefore settle at most the newest eligible credited pressure for that state, rather than refunding several overlapping shocks through one fall in resistance.

If the qualifying intersection reaches at least 75% of the original weighted footprint, propose a reduction equal to half the wave's actual credited Chaos, rounded down. Apply the remaining lifetime reduction allowance, whose gross ceiling is 10. Thus +2 permits -1, +3 permits -1, +5 permits -2, and a final +1 permits no reduction.

Close the record after its one settlement attempt. Any amount suppressed by the shared meter or lost to its zero floor is not banked for later. The reduction does not return capacity to the +30 gross positive ceiling. This keeps repeated recovery from becoming a source of unlimited negative Chaos.

### Bounded lifetime and evidence

Use two finite scheduled observations of stored cohort members. They are addressed through the verified country or shared lifecycle routes and inspect only the named footprint. The final settlement revalidates those stored members. It does not search the world for countries that happen to look recovered.

Every unsettled record expires at day 300. Retire expired records before opening a new one. The 90-day positive-award gate and the 300-day lifetime allow at most four pending containment records. Size compact lifetime credit identities for up to 30 positive integer credits under the +30 gross ceiling, so storage does not assume that the shared meter always accepts the full request. Release detailed state rows after settlement or expiry, keeping only small spent identifiers needed to reject duplicate work.

Resistance is observed at two checkpoints. The design does not claim continuous low resistance between them. Continuous control and occupation continuity are separate facts that require verified lifecycle evidence. If an actor disappears or a required observation is missed, do not invent the missing proof or reduce the denominator. The implementation must preserve the finite scheduling and overdue-expiry contract through save and reload.

This proof is separate from the 365-day local memory used by 095. An expired uprising-support receipt cannot be revived by a still-open achievement or containment record.

### Due observations and a new wave on the same date

An unobserved day-180 or day-270 containment or achievement checkpoint takes precedence over a new 106 write at that exact elapsed-day boundary. Before stage resolution and state mutation, drain only registered proof records due at that boundary through their stored cohorts. The ordinary callback and this pre-write route share the same once-only observation and settlement identity. No recurring world scan is needed.

Record the observation and any resulting settlement or achievement completion first. Then apply the new wave. Its positive additions supersede contributions in older containment records that are still pending, including a record that has just passed its first observation. A completed settlement or earned achievement is not clawed back. A zero addition does not supersede pending containment weight.

Save and reload preserve the due boundary, observation result, and completion state. A callback delivered after the checkpoint date cannot replace a missing observation with a later favorable snapshot. This precedence controls the 106 write and the named proof checks. It does not reconstruct earlier native resistance changes elsewhere in that date.

## Achievement 1: Containment mastery

Working label, not final localisation. Proposed stable achievement ID: `chaosx_106_containment_mastery`.

This challenge rewards an existing human occupier for recovering from a severe actual shock while keeping every affected occupation. It adds no gameplay reward or enrollment action.

| Field | Required design |
| --- | --- |
| Eligible country | An existing human-controlled country with valid occupied territory |
| Qualifying wave | An active Stage II or Stage III wave, nominally +75 or +100, that actually adds at least 50 points in at least five of its occupied states |
| Immutable cohort | Every occupied state under that country that receives any positive addition in the first qualifying wave |
| Observation dates | Days 180 and 270 after the qualifying attempt starts |
| Required state result | Every cohort state is still a valid occupation under that country, with resistance at most 25 and compliance at least 40 at both observations |
| Control condition | Direct control of every cohort state remains uninterrupted for the attempt |
| Attempt failures | Control loss, transfer, release, conversion into an occupier core, removal from occupation, an omitted original member, or loss of the eligible human-control route |
| Retry | A later qualifying wave may restart an attempt only with the same original cohort. At least five original cohort members must again gain at least 50 actual points, and all original members must be valid occupations under the player at the restart |
| Visibility | Visible after the applicable occupation challenge is first discovered |
| Difficulty | Very hard |
| Icon | A repaired rail junction or guarded lamp holding against extinguished sparks, with a strong 64×64 silhouette |

The original cohort never shrinks. Newly conquered states cannot replace difficult old members or supply the five-state restart condition. A later wave can make recovery harder, but it does not erase the first attempt's evidence or silently move its checkpoints. A failed attempt requires an explicit later qualifying restart.

The challenge concerns low resistance and substantial compliance at two observed dates, plus continuous territorial control. Its text must not claim uninterrupted low resistance merely from two samples. Native garrison and occupation choices, including legitimate 097 recovery, can contribute to success through their actual results.

## Achievement 2: Homeland recovery

Working label, not final localisation. Proposed stable achievement ID: `chaosx_106_home_recovery`.

This challenge follows an existing human country as it recovers occupied cores after a real locally supported 095 uprising. It requires the player to win territory through its own war effort and to keep the complete restored footprint after peace.

| Field | Required design |
| --- | --- |
| Eligible country | An existing independent human-controlled country whose cores are under hostile occupation, using an already supported control route |
| Qualifying wave | Nominal addition at least 50, with at least three occupied core states each gaining at least 25 actual points and at least 100 actual points added across its affected occupied cores |
| Immutable cohort | Every core of that country under hostile occupation that receives a positive addition in the first qualifying wave |
| Local 095 link | A later 095 firing commits a real armed outcome using a still-valid positive 106 receipt from at least one cohort state |
| Earned recovery | At least two original cohort states pass directly into the player's control through its own hostile control changes during a war against their occupying side |
| Complete recovery | The player directly owns and controls every original cohort state |
| Lasting result | Keep the complete set for 180 elapsed days after complete recovery and peace with the surviving recorded occupiers and hostile 095 actors, whichever condition becomes true last |
| Independence | Remain independent throughout the tracked recovery and the final hold |
| Control route | Remain the eligible existing human country. The challenge grants no switch into a new rebel country |
| Reset | Losing any cohort state or resuming a relevant war restarts the final hold after full recovery and the required peace are restored |
| Terminal failure | Losing independence or the eligible human-control route closes this achievement attempt as failed for the rest of the campaign, with no restart |
| Invalid shortcuts | Gifts, peaceful transfers, release effects, and ally-held territory do not supply the two own hostile recaptures. Becoming a subject invalidates the attempt |
| Visibility | Hidden until the qualifying occupation and local 095 relationship have been established |
| Difficulty | Very hard |
| Icon | Broken restraints opening around a restored home, without a country-specific flag |

The two own recaptures leave room for 095 to restore another state from the minimum three-state cohort. This avoids requiring the player to deliberately lose a newly restored state just to recapture it for credit.

Ceded states and changes in core status never remove an original cohort member. The challenge still requires direct ownership and control of the full frozen set. A destroyed occupying tag can be treated as no longer at war only after its lifecycle is verified. Renaming, tag changes, and a missing pointer cannot silently erase a still-active hostile side.

A candidate selection or attempted rebel spawn cannot satisfy the 095 link. The consumer must return committed evidence identifying the uprising, the actual state, the valid positive receipt, and the resulting armed outcome. An ordinary native uprising by itself does not satisfy this specific 095 achievement condition.

The inspected legacy 095 script has no 106 history reader. This achievement therefore remains dependent on the 095 integration specified in Part 3. It cannot be substituted with an event-fired flag. The own-hostile-recapture detector and the continuous independence and post-peace hold also require verified existing achievement or lifecycle contracts.

## Achievement tracking and presentation

Keep at most one immutable cohort per achievement for each eligible human country. Repeated waves do not create an unlimited list of attempts. A containment attempt can restart against its original cohort under the stated entry test. Homeland recovery continues against its original cohort and its genuine armed-outcome proof only while the attempt remains eligible. Loss of independence or the supported human-control route is a terminal campaign failure for that achievement. Retain the immutable cohort and closed identity so later independence, a returning player, a new wave, or a stale callback cannot restart it or reuse its old recapture and 095 evidence. Ordinary territorial loss or renewed relevant war resets only the final hold.

Use the project's established achievement eligibility, debug, and multiplayer rules. Forced test firings and synthetic fixtures do not count as earned campaign progress. If the current framework cannot distinguish the relevant test route, wire that distinction before enabling these achievements.

The achievement subjects and all three texture states are specified in Part 5. Final names and descriptions are written after the mechanics are implemented and checked. They should explain the difficult campaign objective and the few conditions the player needs to understand, leaving receipt and callback details internal.

## Why these additions belong here

The wave already supplies the event's large immediate effect. The added depth follows its consequences: native recovery, local support for a later uprising, limited Chaos feedback for real new pressure, a small return for demonstrable containment, and two demanding ways to master or exploit the resulting campaign state.

The balancing values above are explicit so implementation does not have to invent them. Runtime tuning may adjust these parent-selected secondary anchors with evidence. The fixed 25, 50, 75, and 100-point additions and the 200, 400, and 600 Chaos requirements remain the user's design.
