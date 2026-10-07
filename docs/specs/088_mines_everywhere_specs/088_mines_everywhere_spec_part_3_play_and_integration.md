# Event 088: Mines everywhere
## Part 3. Naval play, campaign connections, and Chaos

### Strategic pressure

The global coverage changes the value of preparation and clearance without replacing the existing naval game. A fleet can be powerful in ordinary combat and still face hostile minefields on its intended route. A country with few ships has to decide where its available naval effort matters most. A defender can benefit from its own field while facing the same problem in nearby enemy-owned fields.

The map should not become a uniform damage zone with a scripted outcome. The distribution of ownership, current wars, native mine effects, access restrictions, available ships, and ordinary sweeping creates the differences between campaigns. The event deliberately gives the same placement opportunity while allowing the consequences to differ.

### Operational response profiles

**Supply-dependent country.** The most valuable early clearance is a route that sustains an existing commitment. Its strategic cost is the naval attention and material committed to clearance rather than combat elsewhere. The event does not impose a second artificial supply penalty on top of the native effect.

**Naval offensive.** An attacking country must judge whether a landing can proceed under the current hostile mine situation or should wait for clearance. The event does not add a scripted invasion lock. A costly operation remains possible where native rules allow it, and the consequences come from those rules.

**Coastal defense.** A defender has fields of its own but cannot treat the entire region as safe. The useful distinction is between the danger it presents to an enemy and the danger it faces from hostile owners. Defensive presentation must not imply immunity.

**Limited naval capacity.** A country unable to clear every threatened route can concentrate, postpone an operation, or accept exposure. It does not receive a free minesweeping fleet, technology, or blanket protection merely because the incident is severe. Difficulty should come from the campaign's available responses rather than an extra event currency.

**Peacetime planning.** A neutral country sees a materially changed sea without being forced into conflict. Normal peacetime behavior determines how long fields remain and whether any immediate risk applies. A future war can change the relevance of surviving fields, but Event 088 does not preserve them unnaturally until that war arrives.

### AI behavior

Every eligible AI country receives exactly the same placement treatment as a human country. The AI does not make a random acceptance choice. It does not receive hidden protection, secretly reduced hostile fields, or a free clearance pulse.

Ordinary naval AI remains responsible for fleets and missions. Acceptance requires checking whether it can respond meaningfully to the new mine situation. The implementation should retain supported native behavior wherever it already works. A discovered failure is a concrete integration issue, not permission to simulate AI mine removal through periodic deletion.

Any event-specific AI adjustment must be narrow, use a verified supported strategy, and be justified by measured behavior. It must preserve the tradeoff between clearance and other tasks. It must not permanently rewrite the country's overall naval strategy or impose an unconditional global mission override. There is no new random response pool inside Event 088. The existing event and cluster selection probabilities still need their normal audit.

### Connections to other accepted event concepts

**Event 056, The Navy.** A sudden fleet grant can change how much naval force a country can commit after the mines appear. New ships still face the existing fields. Event 088 does not grant an immunity tag to those ships or refill fields simply because another event creates a fleet. Their practical usefulness depends on their actual equipment and native mission capability.

**Event 059, The Offensive.** Aggressive war behavior can make a mine-covered route strategically urgent. The combination should emerge through ordinary operations. Event 088 does not start another war, duplicate an aggression modifier, or award extra Chaos for a war that another system already counts.

**Event 061, Return to Peacetime, and peace-making effects.** Changes in war status can change which fields are hostile or how the engine treats them. Peace must not be credited as player minesweeping. Event 088 never restores fields to preserve the danger after a legitimate peace effect.

**Events 082 and 087, Law Upgrade and Military Madness.** Mobilization and military modifiers can change the resources and capabilities with which a country faces the aftermath. They do not alter Event 088's fixed addition, owner separation, or once-only nature. Do not infer that an arbitrary military modifier also modifies mines unless the actual statistic supports that relationship.

**Trade disruption and famine-related systems.** Actual disruption caused by native naval outcomes can feed the systems that already observe those outcomes. Event 088 does not award a second synthetic convoy-loss counter or infer famine from mine placement alone. A field that exists is evidence of a field, not evidence that a convoy has sunk or a population has starved.

These connections are behavioral contracts. They do not introduce hidden cross-event triggers or new dependencies merely because the events can coexist.

### Sudden Abundance membership

The event belongs to Sudden Abundance at Medium severity because countries abruptly receive large quantities of a naval asset without normal buildup. That asset creates a hostile, dangerous form of abundance. Medium is the user-assigned cluster severity. It must not be reinterpreted as a permission to affect only a medium-sized fraction of the map.

The cluster remains a single selection outcome for the shared event engine. Its history contains the member outcome rather than a second top-level ordinary-event record for the same incident. Event 088's once-only state must be respected whenever that cluster is selected again. Having a repeatable parent cluster does not make this member repeatable. A member's presentation does not reset the shared countdown or award major-event weight independently of the cluster's one logical outcome.

Required or optional participation within the implementation's cluster registry is a separate property from severity. The parent implementation must inspect and preserve the actual cluster model. It must not invent a probability from the word Medium, duplicate the event in two picker pools, or add a second timer slot to compensate for incomplete membership wiring.

### Shared and independent campaign timing

The incident is global even when the campaign uses independent country event timers. The country whose selection reaches Event 088 initiates the one world change. Other countries do not receive additional timer resets, major-weight increments, or separate ordinary event selections merely because their minefields were included. Their availability must nevertheless recognize that the fire-once member has been consumed globally.

A later selection of Sudden Abundance may still use its other eligible members. Event 088 remains unavailable and must not be replaced with another mine pass for a different country. Multiplayer viewers share the committed world state rather than executing their own deposition on opening the report.

Existing saves require honest historical handling. If the legacy single-region Event 088 already fired, an update must not quietly treat the new implementation as a fresh incident or refill the world. Preserve that consumed state and the existing mines. A legacy firing is not evidence that worldwide coverage occurred, and it must not seed the new clearance achievements with invented global provenance.

### Chaos impact map

The starting magnitude below is an authored balance proposal, not a value supplied by the user or a measured engine result. Chaos level 1 remains the event's selection tier and is distinct from the amount added to the global Chaos Meter.

| Milestone or outcome | Why Chaos changes | Direction and starting magnitude | Dynamic factors | Repeat guard | Shared-source overlap | Reversal or containment counterpart |
| --- | --- | --- | --- | --- | --- | --- |
| The first complete worldwide pass materially adds mines | An unexplained, simultaneous global naval obstruction changes the world | +20 once | At least one field must actually increase. The amount does not multiply by countries or regions | One global manifestation award for Event 088 | Do not repeat the cluster's selection accounting or other incident awards | Native clearance removes the concrete threat locally. No automatic global refund is attached |
| Every eligible field was already full and none increases | The selection creates no new material manifestation | 0 | Actual preexisting saturation must be distinguished from an addition | Event may still be consumed once as a completed no-change application | No award merely because the picker selected it | Existing fields remain normal game state |
| A ship is damaged, shipping is interrupted, or another war begins later | These are later native or shared-system outcomes | 0 additional from Event 088 | Relevant shared systems may count independently under their own rules | No Event 088 per-loss or per-war counter | Prevent duplicate deaths, war, trade, and famine accounting | Use the existing owning system's containment rules |
| One country clears a route | A local operational threat has been reduced, but other countries and routes can remain exposed | 0 additional from Event 088 | Country-relative clearance is not global demilitarization | Achievements can record qualifying clearance without meter farming | No repeated negative award for alternating laying and sweeping | The reward is the reopened route and any earned achievement |
| Peace, decay, annexation, or a later ownership transition removes or changes fields | Normal campaign lifecycle | 0 additional from Event 088 | Verified native behavior determines the result | The manifestation guard survives every transition | Do not duplicate peace or annexation accounting | No refill or compensating placement |

A +20 award places the proposal at the low end of the supplied planning skill's global-disruption band. It is deliberately once-only. The exact magnitude still needs balancing against the active campaign's other Chaos sources. If runtime inspection cannot establish whether placement materially increased a field, that observability issue must be resolved rather than awarding Chaos on selection alone.

### Recovery and long-term meaning

Recovery is local and earned through the naval game. A successfully reopened route is useful immediately, even if danger remains elsewhere. Event details preserve the fact that the incident occurred without treating the original saturation level as a live mine count forever.

The historical record and the current naval map answer different questions. The history records what the event attempted and committed at its firing. The naval map describes the surviving fields and current danger. No presentation should turn an old 1,000-mine snapshot into a claim that the same field is still full after it has been swept.
