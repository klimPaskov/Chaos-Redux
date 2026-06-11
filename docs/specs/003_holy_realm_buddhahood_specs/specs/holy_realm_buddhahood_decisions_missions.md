# Holy Realm Decisions and Missions

The Holy Realm decision layer must feel like action, not a shop. Political power and command power may appear, but major actions should also use equipment, convoys, trains, civilian factories, manpower, stability, war support, supply, local support, route access, and actual objectives.

## Decision categories

| Category | Visibility | Purpose |
| --- | --- | --- |
| Holy Realm Mandala | After `Open the Mandala Chamber` | Opens GUI and shows core values |
| Teaching Missions | After `The Bodhisattva's Vow` | Earns Bodhi and virtues through target actions |
| Sanctuary Works | After industry branch opener | Builds logistics and refugee capacity |
| Sangha Compact | After diplomacy branch | Manages aid, members, cohesion, and shared defense |
| Buddha Powers | After Buddhahood | Uses Meditation Charge for powers |
| Final Silence | After `The Last Wheel` and Buddhahood | Runs the final ritual |
| False Buddha Schism | Only if evolution active | Resolves or exploits schism |

## Active mission caps

Default visible teaching missions: 3.

After `The Four Directions`: 4.

After `One Becomes Many`: 5 for the duration of the power.

Do not show every possible target. The category should prioritize countries by chaos threat, relations, nearby danger, prior teaching history, and compact membership.

## Teaching mission examples

### Send Dhamma Envoys

Who sees it: Holy Realm.

Targets: non-chaos countries that are reachable, or countries threatened by chaos.

Costs and requirements:

- Support equipment.
- Convoys or land route access for distant targets.
- Relations or prior contact.
- Stability above a minimum, unless the target is under chaos attack.

Success:

- Bodhi Progress up.
- Compassion up.
- Target gets a small stability or panic-reduction effect.
- Teaching history flag on target.

Failure:

- Envoys detained or lost.
- Defilements up if the player sent them through an unsafe route.
- Cooldown for that region.

AI:

- Prefer targets threatened by chaos.
- Avoid targets with no route unless using a specific focus or power.

### Guard the Pilgrimage Route

Type: timed mission.

Objective: place supplied divisions in a named route state group or hold key states for the duration.

Costs:

- Tied-down divisions.
- Infantry equipment and support equipment if escorts are formed.
- Supply strain if state infrastructure is poor.

Success:

- Opens a route for teaching missions.
- Bodhi and Sangha Cohesion up.
- May reduce World Suffering in the target area.

Failure:

- Refugee panic event.
- Route closes.
- Compact member confidence down.

### Rebuild the Stupa Network

Type: construction mission.

Objective: use civilian factories or complete infrastructure, railway, or supply hub work in named sanctuary states.

Costs:

- Civilian factory use.
- Time.
- Stability strain if refugees are high.

Success:

- Detachment up.
- Dhyana support and teaching reach up.
- Local defense and supply improve.

Failure:

- Construction delays.
- Refugee burden or local unrest.

### Teach Under Bombardment

Type: high-risk mission.

Targets: a country or state threatened by a chaos country.

Requirements:

- Active chaos war or chaos occupation nearby.
- Support equipment and manpower.
- Safe corridor, air route, or a Buddha power after Buddhahood.

Success:

- Large Bodhi reward.
- World Suffering insight.
- Target gets morale or panic relief.

Failure:

- Casualty report.
- Defilements up if unprepared.
- Wrathful Protection evolution can become more likely.

### Shelter the Dispossessed

Type: repeatable with escalating costs.

Costs:

- Manpower capacity.
- Stability.
- Consumer goods or civilian factory burden.
- Food and supply abstraction through infrastructure and trains.

Success:

- Compassion up.
- Possible manpower or recruitable support after integration.
- Compact Cohesion up if refugees come from a compact member.

Failure or overuse:

- Supply strain.
- Disease or unrest report.
- Local opposition focus or decision becomes visible.

## Meditation decisions

### Begin the Three-Minute Vow

This starts the meditation channel or fallback sequence.

Requirements:

- Not in ordinary offensive war unless a chaos country threatens the realm.
- Capital sanctuary controlled.
- Dhyana path unlocked.
- Defilements below a high threshold.

Costs:

- Political attention and court business are suspended.
- Reduced offensive planning while active.
- Some teaching slots pause unless the One Becomes Many power is active.

Success:

- Meditation Charge up.
- Dhyana mastery progress up.

Failure:

- Small Defilements up.
- Doubt event if repeated failures happen.

### Renew the Vow Under Fire

Emergency version when chaos threatens capital or compact member.

Costs:

- Command power.
- Support equipment.
- War support or stability risk.
- Tied-down guardian divisions.

Success:

- Meditation Charge up faster.
- Wrathful Protection or anti-chaos powers become available.

Failure:

- Panic and Defilements rise.

## Buddha power decisions

Power decisions should be hidden until Buddhahood. Each power spends Meditation Charge and has a cooldown. Effects should use a reusable helper so focuses, events, and GUI buttons can call the same logic.

| Decision | Charge | Target | Main effect | Abuse check |
| --- | --- | --- | --- | --- |
| Show One Becomes Many | 35 | Self and teaching targets | More mission slots, coordination | Cannot stack |
| Walk Through Walls | 45 | Chaos enemy or fortress state | Mountain, fort, urban breakthrough | Normal target disqualifies clean route |
| Walk on Water | 40 | Chaos front with river, strait, or coastal route | Crossing and relief | Requires route or compact naval access |
| Vanish from Sight | 35 | Chaos occupation or enemy | Intel and rescue | Ordinary espionage abuse adds Defilements |
| Sit in the Sky | 60 | Threatened sanctuary or compact capital | Emergency redeploy and supply | Limited divisions only |
| Touch Sun and Moon | 80 | Global chaos crisis | Huge anti-chaos morale and enemy penalty | Fails if no real chaos threat |
| Extinguish Defilements | 100 | Self | Starts Final Silence | Requires low Defilements |

## Sangha Compact decisions

The compact should behave like a living faction system.

Values:

- Sangha Cohesion.
- Member Confidence.
- Aid Burden.
- Patron Pressure if major powers try to use the compact.

Decision families:

| Decision family | Action | Costs | Result |
| --- | --- | --- | --- |
| Recognize a Suffering Government | Bring threatened country closer | Relations, stability, diplomatic capacity | Compact eligibility and influence |
| Open a Refuge Corridor | Move refugees or aid | Convoys, trains, support equipment | Compassion and cohesion |
| Send Relief Columns | Support a member at war | Equipment and tied-down divisions | Member defense and trust |
| Convene the Compact Vote | Admit a member or set shared goal | Cohesion threshold | Membership or refusal event |
| Demand Anti-Puppet Clauses | Keep major powers from dominating members | Diplomatic risk | Independence resilience |
| Joint Defense of the Passes | Shared defensive plan | Command power, equipment, member support | Anti-chaos defense bonus |
| Rebuild the Silent Cities | Post-crisis reconstruction | Civilian factories and time | Aftermath recovery |

Membership failure:

- If the Holy Realm ignores a member under chaos attack, cohesion falls.
- If the Holy Realm conquers normal neighbors, members may leave.
- If a major power dominates aid, patron pressure rises.

## Final Silence decisions

Final Silence decisions are visible only after Buddhahood and `The Last Wheel`.

### Renounce the Last Crown

Effect:

- Removes ordinary conquest tools or locks new ordinary war goals.
- Reduces Defilements.
- Signals route commitment.

Disqualifier:

- If the player declares an ordinary offensive war after this, Final Silence cancels.

### Seal the Mandala

Effect:

- Starts the final ritual mission.
- Consumes a large amount of Meditation Charge.
- Mandala enters Final Silence animation.

Requirements:

- Dhyana Depth 4.
- Defilements below 10.
- Capital controlled.

### Gather the Witnesses

Effect:

- Compact members and taught countries receive reaction events.
- Global observers may approve, fear, or misunderstand the ritual.
- Requires enough teaching history or compact recognition for clean completion.

### Extinguish the Defilements

Effect:

- Consumes Meditation Charge 100.
- Sets final check variables.
- If chaos value is above 1000 and no world-end exists, opens terminal path.

### Enter the Final Silence

Effect:

- If terminal path valid, set world-end flags and fire super-event.
- If terminal path invalid, fire non-terminal aftermath and transform leader to Empty Seat.

Failure:

- If capital falls, schism active, or Defilements rise, trigger `Echo Without Seat`.

## Cleanup rules

Decision categories must close or update when:

- Holy Realm is annexed.
- The leader is no longer the Bodhisattva or Buddha due to an invalid state.
- Final Silence completes.
- World-end flag exists for another scenario.
- Target country no longer exists.
- Target is no longer a valid teaching or compact target.
- Mission target state is no longer controlled by the expected actor.

Temporary flags and variables should be cleared after events consume them. Power cooldowns should be timed flags, with file-scoped constants if timed flag fields reject script constants or variables.

## Exploit checks

The implementation must prevent:

- Using anti-chaos buffs against normal countries.
- Stacking One Becomes Many mission slots permanently.
- Farming Bodhi from the same safe target forever.
- Gaining infinite manpower from refugees.
- Creating free elite divisions without equipment or caps.
- Starting Final Silence without Buddhahood.
- Starting terminal Final Silence below the world-end chaos threshold.
- Resetting Defilements by tag switching or cosmetic changes.
- Abusing ordinary conquest while preserving clean-route achievements.

## Localisation direction

Cost text should be icon-first and short. Examples:

- `200 <support_equipment_texticon>`.
- `2 <convoy_texticon>`.
- `Guard the Pilgrimage Route`.
- `Capital sanctuary controlled`.
- `§RDefilements too high§!`.

Long requirements should use custom tooltips. Place names should be readable and named regions should be documented.
