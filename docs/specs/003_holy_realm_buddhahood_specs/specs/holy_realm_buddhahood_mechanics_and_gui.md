# Holy Realm Mechanics and Mandala GUI

## The mandala panel

The mandala panel is the central presentation surface. It should be a scripted GUI window opened from the Holy Realm decision category. It may also be opened from event details after the event is active.

The panel is not decoration. It shows values, route status, power readiness, and Final Silence eligibility. Every player-clickable action in the panel must have the same validation as a decision. Buttons must show missing requirements, costs, cooldowns, and visible effects. AI countries need equivalent decision or scripted-effect paths.

## Visual layout

The panel should feel like a large sacred interface inside HOI4, not a modern mobile minigame.

Suggested layout:

| Area | Content | Visual state |
| --- | --- | --- |
| Center | Animated mandala sprite | Changes from closed lotus to radiant wheel to quiet empty ring |
| Outer ring | World Suffering and active chaos threats | Flame or smoke intensity grows with chaos |
| Left pillar | Bodhi Progress and teaching successes | Scroll or prayer-wheel markers |
| Right pillar | Dhyana Depth and Meditation Charge | Lotus tiers and concentration bar |
| Lower left | Compassion and Sangha Cohesion | Refugee lamps and compact seal |
| Lower right | Detachment and Defilements | Mirror cracks when corrupted |
| Bottom row | Buttons for Teaching, Meditation, Powers, Final Silence | Locked, available, active, warning, complete states |
| Top corner | Current leader portrait stage | Static or animated portrait depending on stage |

The central mandala should have major state variants:

1. Dormant Mandala: before the panel is fully unlocked.
2. Teaching Mandala: teaching missions active.
3. Dhyana Mandala: meditation ritual active.
4. Awakened Mandala: Buddhahood complete, powers available.
5. Wrathful Protection Mandala: active chaos emergency.
6. Final Silence Mandala: ritual underway.
7. Empty Mandala: Final Silence complete.

## Meditation charge and the three-minute ritual

User experience target: the player performs a meditation channel that feels like holding focus on a sacred icon for about three minutes. The icon pulses while the player concentrates. When the ritual completes, Meditation Charge rises enough to use one or more Buddha powers.

Engine validation is required. If the HOI4 scripted GUI layer can detect a held mouse button or continuous hover state, implement the primary version:

- Button name: `Dhyana Seal`.
- Duration: 180 real seconds.
- The progress ring advances only while the player holds the icon or maintains the required interaction state.
- Moving away, closing the panel, or switching tabs pauses or resets progress depending on selected difficulty.
- Pulse animation speeds up at 33, 66, and 90 percent.
- At completion, fire a short event or tooltip and add Meditation Charge.

If the engine cannot support literal mouse holding, implement the accepted fallback as a concentration sequence rather than a store button:

- The player starts `Three-Minute Vow` from the panel.
- A visible ritual state appears on the mandala.
- The player must complete four concentration beats named Intention, Energy, Mind, and Investigation.
- Each beat is a small timed decision or GUI action with a cost, a tooltip, and a cooldown short enough to feel interactive if the engine supports short UI timing.
- If real-time beats are not supportable, convert the sequence into an in-game meditation mission with a clear duration, such as 21, 49, or 108 days depending on balance.
- During the vow, the Holy Realm suffers opportunity costs, such as lower political gain, lower offensive war justification, fewer teaching slots, or tied-down sanctuary guards.
- The central animation still pulses while the vow is active.

The fallback must preserve the design logic. The player is making a visible commitment to meditation before powers can be used. It must not become a normal click that instantly buys a buff.

## Dhyana Depth unlocks

| Depth | Name | Unlocks | Risk |
| --- | --- | --- | --- |
| 0 | Restless Seat | No powers | Teaching missions only |
| 1 | First Dhyana | Meditation Charge cap 25, basic calm decisions | Failure can add doubt |
| 2 | Second Dhyana | Teaching mission success improves, panel pulse becomes stable | More opportunity cost during war |
| 3 | Third Dhyana | Lesser anti-chaos blessings, stronger sanctuary defense | Failed vow can start rumours |
| 4 | Fourth Dhyana | Buddhahood eligibility and power charging | High Defilements block transformation |

Dhyana Depth should be tied to focus tree progression, missions, and decisions. It should not be a pure focus reward. The player needs to act through the meditation system.

## Teaching missions

Teaching missions increase Bodhi Progress and improve virtue values. They are the main route to Buddhahood. They should be varied and dynamic.

Mission families:

| Mission family | Story action | Main requirements | Success rewards | Failure outcome |
| --- | --- | --- | --- | --- |
| Send Dhamma Envoys | Dispatch teachers and translators | Relations, safe route, support equipment or convoys | Bodhi, Compassion, target stability | Envoys detained, Defilements rise |
| Guard the Pilgrimage Route | Protect monks and refugees | Supplied divisions in named states or borders | Bodhi, Sangha Cohesion, route access | Refugee panic, mission cooldown |
| Rebuild the Stupa Network | Repair sacred and public sites | Civilian factories, building slots, local control | Bodhi, Detachment, local support | Construction strain, lower stability |
| Debate the Worldly Ministers | Resist turning the realm into a war state | Political faction conditions, high Detachment | Defilements down, unlock focus | Schism pressure rises |
| Teach Under Bombardment | Complete teaching during a chaos war | Target at war with chaos, support convoy or air route | Large Bodhi and World Suffering insight | High casualty report |
| Shelter the Dispossessed | Accept refugees from chaos zones | Manpower capacity, supply, stability cost | Compassion, Sangha Cohesion, recruitable support | Supply strain and unrest |
| Translate the Wheel | Radio and print doctrine | Civilian factories, command staff, maybe radio tech | Teaching success factor, target reach | Propaganda backlash |
| Heal the Terrified | Field hospitals and relief | Support equipment, manpower, safe corridor | Lowers chaos pressure effects in target | Disease or panic event |

Teaching success should scale with:

- Target stability and war support.
- Whether a chaos country threatens the target.
- Whether the Holy Realm has route access.
- Whether the target is hostile, neutral, friendly, or a compact member.
- Dhyana Depth.
- Compassion and Detachment.
- Defilements.
- Previous success in the region.
- Active evolutions.

The mission system should avoid showing too many missions at once. Use three visible slots by default, four after a focus, and five after Buddhahood or the One Becomes Many power.

## Buddhahood transformation

When requirements are met, the event `The Unshaken Seat` starts the transformation. The player should see:

- The Bodhisattva portrait replaced by the Buddha portrait.
- The country name or cosmetic name change to a more final Holy Realm identity.
- The mandala becomes the Awakened Mandala.
- The super-event `The Awakened One` appears.
- The permanent spirit `The Awakened Seat` is added.
- Powers appear in the panel, but all are locked behind Meditation Charge.
- Teaching missions change from earning Bodhi Progress to lowering World Suffering, supporting allies, and restoring Defilements.

Buddhahood should be irreversible. The leader cannot become the Bodhisattva again. If the country later suffers failure, it should lose access to clean Final Silence or gain corrupted states, not undo the transformation.

## Buddha powers

The powers are named after traditional supranormal motifs, then translated into HOI4 mechanics. They should be dramatic, temporary, and anti-chaos focused.

All powers require:

- `holy_realm_leader_is_buddha = yes`.
- Meditation Charge above the power cost.
- Not already in the same power cooldown.
- Not targeting a normal country unless the power is non-combat or defensive.
- If offensive, target must satisfy the chaos enemy trigger.

### One Becomes Many

Story: the Buddha appears to be many and sends teaching presence across multiple fronts.

Mechanics:

- Temporarily increases active teaching mission slots.
- Creates `Dharma Envoy Manifestations` as timed country modifiers or target flags.
- In wars against chaos, grants planning speed and coordination to Holy Realm and Sangha Compact armies.
- Unlocks simultaneous relief missions.

Risks:

- If Defilements are high, creates a False Buddha echo event.
- Cannot be used twice while envoys are active.

### Passing Through Walls

Story: fortifications, mountains, and ramparts no longer stop the Awakened path.

Mechanics:

- Strong attack and breakthrough against chaos countries in mountains, hills, forts, and urban strongpoints.
- Can trigger a targeted decision against a chaos-held fortress state.
- Temporarily reduces enemy fort effects only for Holy Realm or compact units.

Risks:

- If used against a normal country, add major Defilements and disqualify clean achievements.

### Walking on Water

Story: water becomes like dry land to the focused mind.

Mechanics:

- River crossing penalty reduction against chaos countries.
- Temporary amphibious and naval invasion support if the Holy Realm has access or compact allies with ports.
- Can open a `Lotus Bridge` relief route to a coastal compact member.

Risks:

- Requires convoys or compact naval access unless the implementation treats it as a purely spiritual route.
- High world suffering raises effect strength but also cooldown.

### Vanishing from Sight

Story: armies and envoys move unseen by chaos forces.

Mechanics:

- Temporary enemy intel penalty for chaos countries at war with the Holy Realm.
- Boosts resistance and evacuation missions in chaos-occupied states.
- Reduces Holy Realm operative capture risk if operatives exist.

Risks:

- If used during ordinary espionage against normal countries, Defilements rise.

### Seated in the Sky

Story: the Buddha travels in space like a bird while seated in meditation.

Mechanics:

- Emergency redeployment of a limited number of elite guard divisions to a threatened core, compact member capital, or named sanctuary state.
- Air supply and supply grace bonuses in mountain and isolated states.
- Special one-time relief event when a capital is about to fall to chaos.

Risks:

- Cannot move divisions into normal offensive wars.
- Requires Dhyana Depth 4 and high Meditation Charge.

### Touching the Sun and Moon

Story: the Buddha touches the heavenly bodies, showing mastery beyond ordinary reach.

Mechanics:

- Global Holy Realm and compact morale burst against chaos countries.
- Chaos enemies suffer temporary organization recovery and planning penalties.
- Reveals hidden chaos sources or event targets if the world-threat system supports it.

Risks:

- This should be one of the most expensive powers.
- If activated while no real chaos threat exists, it becomes a failed omen and raises Defilements.

### Extinction of Defilements

Story: the only supramundane power is the ending of defilements.

Mechanics:

- Prerequisite for Final Silence completion.
- Requires Meditation Charge 100, Defilements below 10, Dhyana Depth 4, Buddhahood, and one successful anti-chaos power display.
- Begins the Final Silence ritual rather than giving a normal combat buff.

Risks:

- If interrupted by capital loss, leader death event, schism, or Defilements spike, the Final Silence fails and creates a unique aftermath.

## Anti-chaos buff package

The first time a Buddha power is shown against a chaos country, fire a major event and apply `Revealed Powers of the Buddha`.

Effect direction:

- Strong attack and defense against chaos countries.
- Organization recovery and supply grace when defending sanctuaries against chaos.
- Faster teaching mission success in countries currently invaded by chaos.
- Reduced chaos-country infiltration or panic effects on compact members.
- No bonus against ordinary countries.

This buff should be strong enough to matter. It is the user's requested major power moment. It should not be a tiny 2 percent modifier. Suggested magnitude for tuning is large, such as 20 to 40 percent in the relevant anti-chaos domains, balanced by cooldowns, Meditation Charge costs, and ordinary-war disqualifiers.

## Final Silence ritual

The Final Silence is a multi-step late route. It must feel like entering Ultimate Nirvana, not like launching a weapon.

Prerequisites:

- Buddhahood complete.
- `The Awakened One` super-event has fired.
- Dhyana Depth 4.
- Meditation Charge 100.
- Defilements below 10.
- At least one Buddha power used against a chaos country.
- Focus `The Last Wheel` complete.
- No active False Buddha Schism.
- Capital sanctuary has not fallen in the last 180 days.

Ritual steps:

1. `Renounce the Last Crown`: removes or weakens ordinary conquest tools.
2. `Seal the Mandala`: locks the player into the route and starts a mission timer.
3. `Gather the Witnesses`: compact members, nearby countries, and enemies react.
4. `Extinguish the Defilements`: consumes Meditation Charge and checks corruption.
5. `Enter the Final Silence`: fires non-terminal or world-end completion.

Non-terminal completion:

- Massive anti-chaos suppression.
- Strong global stability or panic recovery for non-chaos countries.
- Holy Realm leader becomes `The Empty Seat` or a council successor.
- Powers stop being usable because the Buddha has passed beyond worldly action.
- The Sangha Compact becomes a guardianship and reconstruction bloc.

World-end completion:

- Allowed only when global chaos is above 1000 and no other world-end flag is set.
- Set `world_end` and `world_end_final_silence`.
- Set matching super-event visible flag.
- Stop incompatible future systems and branches.
- Event log, event details, docs, and spreadsheet describe the terminal state.

Failure cases:

- Capital falls during ritual: Final Silence breaks into `Echo Without Seat`, a severe but non-terminal crisis.
- Defilements rise above threshold: False Buddha Schism or corrupted mandala state.
- A compact member betrays the ritual: Sangha Cohesion collapse and a diplomatic event.
- Player starts an ordinary offensive war: ritual cancels and clean route disqualifies.

## Mandala GUI animation rules

Every animated asset must follow the frame animation workflow. Final assets are frame sheets, not GIFs. Every loop needs source frames. Local scripts may assemble and resize frames, but they must not create the main animation by only pulsing, scaling, blurring, recoloring, or moving one still.

Minimum animated assets:

| Asset | Size | Frames | Use |
| --- | --- | --- | --- |
| Central mandala dormant | 420x420 | 8 | Idle panel state |
| Central mandala meditation | 420x420 | 12 | Three-minute ritual or vow active |
| Central mandala awakened | 420x420 | 12 | Buddhahood state |
| Central mandala final silence | 420x420 | 12 | Final Silence ritual |
| Dhyana Seal button | 96x96 | 8 | Meditation hold or concentration sequence |
| Warning flame ring | 420x420 | 8 | Wrathful Protection and danger states |
| Buddha portrait animated | 156x210 | 8 | Leader portrait after Buddhahood |
| Empty Seat portrait animated | 156x210 | 8 | Final Silence aftermath |

Every animated asset needs a static fallback. If any target surface cannot support animation, use the fallback and keep the mandala state readable through static variants.
