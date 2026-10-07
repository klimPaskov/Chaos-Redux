# Event 088: Mines everywhere
## Part 5. Naval achievement routes

### Achievement purpose

The achievement set rewards overcoming the mine situation. Receiving a field, acknowledging the report, remaining alive for a short period, or waiting for ordinary decay is not mastery. Both achievements require difficult campaign actions and evidence that distinguishes those actions from diplomatic or ownership changes.

The identifiers below are proposed registration keys, not finished player-facing titles. Both entries are visible once the event's achievement group is available under the existing achievement framework. Their exact final title and description wording belongs to implementation. They carry cosmetic achievement recognition rather than additional combat bonuses or another Chaos award.

The tracking requirements are normative. Several native observations have not been verified in the available environment. That is a technical blocker to implementing the affected achievement, not permission to replace it with an easy unlock. The implementation handoff separates event placement support from achievement observation support.

### Common qualifying clearance

A qualifying region must have belonged to the firing-time sea set and must have contained at least two distinct hostile owners whose fields were materially increased by Event 088. The player must have been at war with those owners when the qualifying clearance begins. The player then contributes actual native minesweeping removal in that region and the region reaches zero currently relevant hostile mines while the required hostility remains in force.

A lower mine count by itself is insufficient. Progress needs a reliable positive attribution to the player's sweeping and a way to exclude peace, owner disappearance, passive decay, and administrative field removal as the cause of the qualifying transition. Allied assistance is allowed, but the player must have removed mines rather than merely having a task force in the area.

The original qualifying hostile ownership must remain resolvable throughout the attempt. Peace with a qualifying owner, the removal of that owner, or a state change that makes a field harmless invalidates that attempt rather than proving clearance. The region can start a fresh attempt later if it still meets the real requirements. Losing an attempt does not withdraw an achievement already legitimately earned.

Each region can contribute once to an achievement. Repeated minelaying and sweeping in the same region cannot farm distinct-region progress. Debug-triggered test firings, artificial achievement progress writes, and forced test clearance are ineligible under the framework's established test rules.

### Achievement A: `chaosx_088_clearance_campaign`

**Title direction.** A concise maritime expression connecting sustained clearance to reopening a working sea route. Avoid a generic congratulation, a real naval commander's quote, and a title suggesting the player has cleared the entire world.

**Description direction.** State the requirement to complete qualifying player-attributed clearance in five distinct Event 088 regions that each began with at least two qualifying hostile owners. Make the ongoing-hostility and passive-removal exclusions understandable without promising hidden statistical precision.

**Eligible countries.** A human-controlled existing country that participated in the campaign at the event firing and subsequently has native minesweeping capability. Eligibility is not restricted by a historical tag, ideology, major status, original coastline, or starting fleet size. A late-created country cannot acquire a fictitious firing-time identity for this achievement.

**Unlock conditions.** Event 088 completed legitimately. The country records qualifying clearance in five distinct valid regions. Each region meets the common hostile-owner and player-attribution conditions. The achievement framework's ordinary campaign eligibility remains valid. Progress can span several separate naval operations within the same campaign.

**Failure and disqualifiers.** Peace, decay, annexation, disappearing ownership, allied-only sweeping, and generic mine deletion do not qualify as player clearance. Five confirmations of one region count as one. Completing a no-change firing in a world where Event 088 added no mines cannot create qualifying fields.

**Difficulty.** High. The player needs several genuinely contested areas, a usable clearance force, sustained warfare with the qualifying owners, and successful clearance across a substantial part of the naval campaign. It cannot be earned by the opening grant.

**Progress presentation.** Show qualifying distinct regions out of five only when the framework can display a trustworthy count. Retain enough history to explain why a completed-looking region failed the conditions. Do not show exact per-source Event 088 mine counts if the engine only stores aggregated owner fields.

**Icon direction.** A recognizable mine beside a narrow, visibly clear passage through dark water. The opening should read as a navigable channel rather than a magical shield. Use one strong silhouette and avoid small numeric counters, text, and decorative flags.

### Achievement B: `chaosx_088_open_water_offensive`

**Title direction.** A concise expression linking clearance to an audacious overseas operation. It should sound like an accomplishment in hostile waters without implying that the event granted the invading fleet immunity.

**Description direction.** Explain the combined route: qualify three regions through active clearance, complete a player-led naval invasion using the cleared operational route, and defeat the selected coastal enemy before the relevant war relationship ends. The text must distinguish a native landing from a state acquired through a peace deal or unrelated annexation.

**Eligible countries.** A human-controlled existing country eligible for the event's naval achievement tracking. No historical country is required. The target is an actual current coastal enemy chosen by the player's qualifying operation, not a named country forced into existence.

**Unlock conditions.** The country completes qualifying clearance in three distinct regions. At least one of those regions is demonstrably used by a later player-led native naval invasion. The invasion successfully establishes the player's control in an enemy coastal state. The invaded country is a qualifying hostile mine owner for that cleared route. The invaded country then capitulates to the player's side while the relevant war relationship continues, and the player still controls the landing state or has retained it within an explicitly supported allied control transfer.

The invasion must follow the qualifying clearance. A landing completed before the event cannot be retroactively counted. The path, attacker, target, landing transition, and final enemy defeat need reliable attribution. A declaration of war, a planned arrow on the map, naval supremacy, or a generic coastal-state conquest is not a substitute for an executed naval invasion.

**Failure and disqualifiers.** Peace with the selected enemy before the required outcome closes the operation attempt. A target erased by an unrelated event does not count as the required defeat. A land attack that happens to capture a coastal state does not count as a landing. An allied-only landing does not count as player leadership. Losing the landing state before the qualifying defeat invalidates that attempt unless the verified framework can distinguish an intended allied control transfer from an enemy recapture.

**Difficulty.** Very high. The player must convert clearance into a successful operation and a strategic result while maintaining the relevant hostile relationship. This route rewards offensive use of a cleared sea rather than duplicating the five-region clearance achievement.

**Progress presentation.** Separate the three-region clearance condition, verified landing, selected enemy, retained landing state, and qualifying defeat. Never display a completed landing merely because a trigger observes a coastal state under player control.

**Icon direction.** A period landing craft moving through a clear gap between mine silhouettes toward a distant shore. Keep the craft and forward direction dominant so the icon remains distinguishable from the first achievement at 64 × 64. Do not depict a famous real landing or add a national emblem without a source-based reason.

### Tracking integrity and retained progress

The framework must retain the event's legitimate firing identity, distinct qualifying regions, qualifying hostile owners, and the player identity associated with the attempt. Country switching and multiplayer handovers follow the existing achievement framework, with no duplicated unlocks across successor identities.

Tracking must be bounded to eligible human achievement participants and event-relevant records. It must not add a second worldwide daily sea-region scan just to approximate clearance. Suitable native event hooks or the existing achievement evaluation cadence may be used only when they can observe the required facts accurately.

Minefields may aggregate old mines, Event 088 additions, and later native minelaying under the same owner. The achievements therefore require that Event 088 materially increased the field and that the later field was cleared. They do not claim that a particular individual mine removed by sweeping can be assigned to the event. If source-level removal attribution is unavailable, the implementation must not invent it.

### Unlock and reward boundaries

Achievements do not cause a second placement, remove remaining mines, grant fleet statistics, change diplomacy, or reduce the global Chaos Meter. The reopened sea and successful campaign outcome are the substantive gameplay rewards. Recognition belongs to the achievement framework once the actual conditions are proved.
