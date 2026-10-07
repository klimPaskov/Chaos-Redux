# Event 097 achievement implementation and art prompt

Implement the six achievement designs reproduced below and their exact asset states. The accepted source of truth is Part 9 of the Collaboration specification. Read the full ten-part specification, current AGENTS.md, `chaos-redux-events`, `chaos-redux-event-assets`, the achievement registry's current patterns, and the native/source capability gates before changing files.

The detailed brief below preserves every eligibility, objective, disqualifier, visibility, difficulty, tracking, and icon requirement. Working labels are not final localization. Write final titles and descriptions only after the actual conditions are implemented and checked. Do not make the challenges easier because a tracking input or connected event is missing.

Use observed native events and minimal persistent facts. Do not infer prewar collaboration, old factory counts, government creation, or a national uprising from the present map. Continuous intervals need real continuity checks, stable cohorts, reset behavior, and save/load proof. A1 needs original war-entry snapshots. A3 needs an actual positive Fifth Column grant. A4 needs actual native governments, including the democratic route where supported. A5 and A6 need the accepted companion contracts.

Inspect the current shared registry and keep `common/achievements/chaos_redux_achievements.txt` as the authoritative root where the current pattern requires it. Wire exact IDs, localization, and `interface/chaosx_achievements.gfx`. Produce completed, grey, and not-eligible DDS files for each ID directly in `gfx/achievements/` using the asset prompt's mandatory template workflow.

Use the named icon artist for art after reference review. Use the appropriate independent completion, localization, country, and decision audits on actual implemented results. No such agent execution or gameplay verification occurred in planning. Report every actual action and unresolved dependency.

For every achievement, provide at least one valid unlock fixture, one near miss, one anti-farming fixture, and a save/load fixture. For timed conditions, demonstrate an actual reset on a broken condition, not only a successful end-of-period sample. Withhold or visibly gate connected challenges whose native or companion capability is not implemented. Never ship an apparently available impossible challenge.

## Full achievement design

# 097 Collaboration
## Part 9: Achievement design

## Shared rules

These are difficult campaign challenges built around decisions and consequences. Receiving the global grant, opening a report, reaching a Chaos threshold, or inheriting a collaboration government does not qualify by itself.

Use the project's normal achievement eligibility and completion rules. These challenges require at least one actual material Event 097 manifestation in the campaign. Event-specific tracking begins only from observed, valid gameplay. Never invent historical observations when a save is loaded or an achievement is introduced into an existing campaign.

All achievement names below are working directions. Final titles and descriptions must be written from the actual implemented conditions. An achievement should remain unobtainable in a configuration that lacks a required capability rather than silently substituting an easier goal, but it must also be visibly gated or withheld so players are not offered a broken challenge.

Completed achievements remain completed under the shared framework. Before completion, a broken continuous condition resets that challenge's continuous interval. Timers use actual calendar days and persist correctly across save and load.

For a fixed-cohort challenge, choose the cohort automatically from the earliest qualifying observed members that jointly satisfy its composition rules, with a stable political-identity tie-break. Expose the tracked members through ordinary achievement progress, not a new management screen. A member cannot be exchanged during a running interval. After a reset, a new qualifying cohort can form.

## A1: Reciprocal conquest

**Identifier:** `chaosx_097_reciprocal_conquest`

**Title direction:** Conquering opponents who were equally prepared to receive the player's own surrender. The tone should acknowledge mutual vulnerability rather than celebrate a free intelligence bonus.

**Description direction:** Defeat five substantial independent opponents while both sides possess deep collaboration against each other, without the player country capitulating during the challenge.

**Eligible country:** Any living player country allowed by the shared achievement framework.

For each of five distinct target political identities, record that the target was independent and had at least 25 total civilian and military factories when its qualifying war against the player began. At that war entry, the player's collaboration inside the target and the target's collaboration inside the player must both be at least 60. The player must then contribute to the target's actual capitulation and control at least five eligible target homeland states at that outcome.

The five targets must be defeated within 365 days of the first qualifying target capitulation. The player must not capitulate between the first qualifying war entry and the final credited defeat. A failed interval can start a new attempt using new observed qualifying wars, but old defeats cannot be credited twice within the same attempt.

**Disqualifiers:** Subject farming, repeated defeats of the same identity, a target released by the player for this attempt, native debug or ineligible campaign conditions, and a defeat without the player's required occupation contribution.

**Difficulty:** Very hard. Deep collaboration exists on both sides and the player must conduct five genuine, substantial campaigns within a limited period.

**Visibility:** Visible when Event 097 is enabled and the underlying native collaboration capability is supported.

**Tracking:** Snapshot independence, factory count, both native collaboration values, target identity, and war entry. Track actual capitulation beneficiary or contribution and the player's controlled qualifying state count. Do not infer prewar values from the postwar map.

**Icon direction:** Two opposing military caps above a single broken defensive line, with neither side visually safe from betrayal. No words or national emblems.

## A2: An administration that lasts

**Identifier:** `chaosx_097_administration_that_lasts`

**Title direction:** A prepared administration that remains functional beyond the first parade.

**Description direction:** Maintain a durable occupation across five states from at least two different defeated countries after receiving genuine early administrative handovers.

**Eligible country:** Any eligible player country with Evolution II active.

Select a tracked cohort of five states, including homeland states from at least two distinct defeated political countries. Each state must have received an actual positive Event 097 early handover for this player sponsor, rather than only native post-capitulation compliance. Keep all five under the player's continuous direct control for 180 days. Throughout that interval, their compliance must remain at least 70 and resistance below 25.

The interval may begin after all five states satisfy the conditions. The cohort is fixed for that interval so a failed state cannot be silently exchanged for another. A broken condition resets the interval. A new qualifying cohort can begin another attempt.

**Disqualifiers:** Peaceful control transfer counted as a handover, own-core administration, client-government control instead of direct control, repeated payment of a spent offer, or substitution of a state during the interval.

**Difficulty:** Hard. The player must retain a broad, genuinely collaborative occupation through sustained play and avoid abusing recapture.

**Visibility:** Visible with Evolution II available in the supported configuration.

**Tracking:** Actual positive handover receipt, sponsor and target identities, cohort, compliance and resistance threshold transitions, control changes, and calendar interval. Checks are bounded to the cohort, not every occupied state in the world.

**Icon direction:** An intact civic building surrounded by five small keys, suggesting a durable administration rather than a new currency.

## A3: Return from the brink

**Identifier:** `chaosx_097_return_from_the_brink`

**Title direction:** Recovering after the enemy's collaborators have already begun to act.

**Description direction:** Survive a real Fifth Column breakdown, prevent that sponsor's final realignment, and later defeat the responsible power.

**Eligible country:** An eligible player country that suffers an actual positive first-stage Fifth Column award to an enemy sponsor. The sponsor must have at least 25 total civilian and military factories at that incident.

Within 30 days of the first breakdown, bring the player's surrender progress below 25%. The responsible sponsor must not receive an actual positive final-stage breakthrough during that recovery window. The player must not capitulate. Within 365 days of the first breakdown, contribute to that sponsor's actual capitulation while controlling at least five of its qualifying homeland states. Remain independent and uncapitulated for 90 days after that victory.

**Disqualifiers:** A capped no-op breakthrough, an invented warning without a native increase, the sponsor being a deliberately released client, country switching that violates shared achievement eligibility, or a recovery inferred from missing historical data.

**Difficulty:** Very hard. The player must reverse a real near-defeat situation and then defeat the actual source of the danger.

**Visibility:** Visible with Evolution III supported. Progress remains private to the player.

**Tracking:** Sponsor-target incident identity, positive native grant, current surrender progress, 30-day recovery deadline, second-stage actual result, qualifying later victory, and 90-day independence interval.

**Icon direction:** A damaged defensive shield pushed upright against a toppled foreign standard, without readable insignia.

## A4: A world of local governments

**Identifier:** `chaosx_097_local_government_network`

**Title direction:** An empire governed through several genuinely local regimes.

**Description direction:** Maintain five qualifying native collaboration governments created through Evolution IV for a sustained period.

**Eligible country:** Any eligible player sponsor, including democracies once the required native exception is verified.

Create five distinct native collaboration governments through qualifying Evolution IV readiness opportunities. Each must administer at least five homeland states belonging to its own defeated political identity when created. Keep a fixed cohort of five governments continuously alive, uncapitulated, administering at least five of their applicable homeland states each, and tied to the player as their actual installing power and current overlord for 180 days.

The interval resets if any cohort member ceases to meet the relationship or survival condition. A new cohort can begin later. A regime inherited from another sponsor does not count as personally installed.

**Disqualifiers:** Generic puppets, repeated creations from the same defeated identity, annex-and-release loops, governments made by another sponsor, and native creation calls that failed or transferred no legitimate area.

**Difficulty:** Very hard. Five substantial conquests must be consolidated and their regimes maintained.

**Visibility:** Visible with the verified Evolution IV route. Do not expose an apparently achievable democratic version before its native creation capability is supported.

**Tracking:** Qualified readiness opportunity, successful native government identity, installing sponsor, creation-state bundle, current overlord, capitulation or dissolution, and fixed-cohort interval.

**Icon direction:** Five small government buildings linked to one distant capital, using a compact composition rather than a literal map.

## A5: The homeland returns

**Identifier:** `chaosx_097_homeland_returns`

**Title direction:** National restoration after a foreign-backed local regime has taken root.

**Description direction:** As the surviving national claimant, return through Event 095, recover a substantial homeland from a qualifying collaborator regime, and remain independent.

**Eligible country:** A living player-controlled national claimant, including a supported government in exile, whose homeland is administered by an observed Event 097-created collaboration government. The player retains the claimant's political identity throughout the eligible interval.

At the qualifying Event 095 uprising, snapshot at least five homeland core states administered by that collaborator regime. The uprising must actually restore the claimant through Event 095. The claimant must subsequently control every state in that snapshot, remove the collaborator regime's control from its homeland, and remain independent and uncapitulated for 180 days.

**Disqualifiers:** Peaceful release by the sponsor masquerading as an uprising, unsupported identity switching, fewer than five snapshot states, an ordinary puppet without qualifying Event 097 creation history, or fabricated preexisting history.

**Difficulty:** Very hard. It requires surviving as the rightful political claimant, an actual connected uprising, military or political recovery, and durable independence.

**Visibility:** Available only when both Event 095's accepted restoration route and the required Event 097 native government history are implemented. Otherwise withhold the challenge with an explicit dependency record.

**Tracking:** Original claimant identity, client regime identity, installing sponsor, uprising receipt from Event 095, immutable homeland cohort, later control and independence. The restoration event remains the authoritative source of uprising success.

**Icon direction:** A national civic building emerging from beneath a broken foreign control chain. Keep it country-neutral.

## A6: Two spheres of collaborators

**Identifier:** `chaosx_097_two_collaborator_spheres`

**Title direction:** The restored Iberian partition operated through two separate networks of local governments.

**Description direction:** As one of the accepted treaty partners, sustain both partners' distinct collaborator spheres after the partition route has actually advanced beyond its opening Iberian dispute.

**Eligible country:** The player occupying one of the actual Spanish or Portuguese partner roles in the accepted Event 093 treaty route. Resolve the route's real roles, including supported successor identities, rather than hard-coding a cosmetic country name.

Both partners must have activated the accepted world-partition stage. Each must personally install and retain at least five distinct qualifying Event 097 native collaboration governments, each with at least five homeland states at creation. The two government cohorts must not overlap. Both partners must retain their agreed cooperative treaty relationship and their respective regimes for 180 days.

**Disqualifiers:** A Galicia-only settlement, borrowing the other partner's installation credit, generic puppets, a broken treaty relationship, duplicate target identities, or an unsupported treaty hook assumed to exist.

**Difficulty:** Exceptional. This is a coordinated late-campaign objective across two separate powers and ten substantial regimes.

**Visibility:** Hidden until the accepted world-partition stage and Evolution IV are both actually available. Do not register an unachievable live challenge before the companion route exists.

**Tracking:** Authoritative treaty partners and stage, each sponsor's government-creation history, disjoint fixed cohorts, cooperation changes, and shared calendar interval. Event 097 must not create its own version of the treaty state.

**Icon direction:** Two contrasting celestial halves above separate groups of civic buildings, suggesting division of the world without text or a historically inaccurate treaty map.

## Art states and truthful completion

Each achievement needs completed, grey, and not-eligible assets. The subject illustration is one layer in the established template workflow. Final 64 by 64 output, grey treatment, and the not-eligible overlay must follow the project pipeline.

An achievement is complete only when its real gameplay conditions, eligibility, reset rules, native identities, localization, three visual states, and registry wiring are all implemented and checked. An attractive icon or a list of conditions alone is not a finished achievement.
