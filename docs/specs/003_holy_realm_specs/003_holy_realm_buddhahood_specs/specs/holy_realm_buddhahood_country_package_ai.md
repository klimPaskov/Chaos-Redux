# Holy Realm Country Package and AI Matrix

## Target country handling

Primary target: Tibet.

Fallbacks: Bhutan or Nepal only if Tibet is gone and the fallback country exists, is not already a chaos country, and can plausibly host the Holy Realm. Do not create a delayed event for a missing country.

The implementation should track origin:

- `holy_realm_origin_tibet`.
- `holy_realm_origin_bhutan`.
- `holy_realm_origin_nepal`.
- `holy_realm_event_created_country` only if a release path actually creates a tag.

If the event transforms an existing country, use cosmetic tags, leaders, advisors, ideas, and additive focus branches where possible. If the event releases a new Holy Realm tag, create full history, localisation, flags, leader, units, and focus loading.

## Country identity states

| State | Trigger | Name direction | Leader direction |
| --- | --- | --- | --- |
| Ordinary target | Before event | Existing country name | Existing leader |
| Holy Realm | Event reveal | The Holy Realm, regardless of Tibet, Bhutan, or Nepal origin | Bodhisattva leader |
| Great Bodhisattva Realm | Bodhi high and Dhyana 3 | More sacred but not final | Great Bodhisattva portrait |
| Awakened Realm | Buddhahood | The Awakened Realm or The Holy Mandala | Buddha portrait |
| Empty Seat | Final Silence aftermath | Realm of the Empty Seat or Silent Mandala | Empty Seat council or successor |
| False Mandala | Schism route | False Mandala or Worldly Mandala | False Buddha or Protector Regent |

The base event-reveal identity must not branch into Tibet-, Bhutan-, or Nepal-specific Holy Realm names. Ideology-specific names should exist for democratic, neutrality, fascism, and communism if the country can switch ideology. If the event locks ideology, cosmetic names and party names should still reflect route identity.

## Leader and portrait plan

The leader begins as the Bodhisattva. The leader may be fictional, symbolic, or an invented religious figure. Do not use a generated portrait for a real historical religious leader. If a real historical person is used, the portrait must be sourced and documented.

Portrait stages:

| Stage | Condition | Portrait | Animation |
| --- | --- | --- | --- |
| Bodhisattva | Start | Plain monk or teacher, humble | Static |
| Teacher of the Four Directions | Bodhi 25 | Warmer light, more pilgrims | Static or subtle optional |
| Great Bodhisattva | Bodhi 75 and Dhyana 3 | Stronger aura, mandala in background | Optional animated route portrait |
| Buddha | Transformation complete | Calm luminous figure, no text, no caricature | Animated portrait required with static fallback |
| Empty Seat | Final Silence aftermath | Empty throne, lotus, bell, or council silhouette | Animated optional, static required |
| False Buddha | Schism | Too-bright or cracked sacred image | Static or animated if route major |

Portrait implementation can use character swaps if direct portrait switching is unreliable. The visible leader name and trait should change at Buddhahood.

Leader traits:

| Trait | Stage | Effect direction |
| --- | --- | --- |
| Bodhisattva Vow | Start | Teaching and stability, weak war aggression |
| Great Compassion | Mid | Refuge and mission success |
| Unshaken Seat | Pre-Buddha | Lower Defilements, stronger meditation |
| The Buddha | Final leader | Anti-chaos powers and high Detachment |
| Empty Seat | After Final Silence | Reconstruction and compact stability, no power activation |

## Starting ideas

Use a small number of deep ideas, not a pile of generic modifiers.

| Idea | Role | Starting effect direction | Upgrade path |
| --- | --- | --- | --- |
| Fragile Sangha | Weak state capacity | Lower political gain, lower recruitable population | Council, Assembly, or Regent reforms |
| Remote Sanctuaries | Geography and isolation | Mountain defense, industry and trade weakness | Pilgrimage Roads or Sealed Valleys |
| Worldly Burden | Spiritual risk | Defilements from ordinary war and conquest | Removed at Buddhahood or worsened by schism |
| Open Refuge | Optional early | More manpower potential, supply strain | Upgraded by refugee missions |

## Starting forces

The Holy Realm should not start as an empty tag if it is expected to fight. It should also not receive a generic army dump.

Dynamic setup factors:

- Origin country size and state control.
- Chaos tier at event firing.
- Whether a chaos country is nearby.
- Number of core mountain states controlled.
- Stability and war support.
- Whether the country is already at war.

Suggested force families:

| Force | Template concept | Source | Scaling |
| --- | --- | --- | --- |
| Temple Guards | Small mountain infantry with support if available | Monasteries and capital guards | More if capital safe and stability high |
| Pilgrimage Escorts | Light infantry or cavalry-like escorts | Route protection missions | Unlocked through teaching path |
| Mountain Pass Detachments | Defensive mountain infantry | State defense networks | More if border threatened |
| Relief Columns | Support-heavy low attack units | Refuge and medical networks | Unlocked by Sanctuary Works |
| Wrathful Protectors | Rare anti-chaos elite units | Emergency chaos threat | Limited and can raise Defilements |

Unit growth must come through focuses, missions, and equipment costs. Avoid repeated free units.

## Advisors and high command

Advisor categories should match route identity:

- Abbot administrator for Council route.
- Protector Regent or secular minister for Regent route.
- Refuge organizer for Pilgrim Assembly route.
- Mountain logistics expert for industry branch.
- Guardian commander for military branch.
- Compact envoy for diplomacy branch.
- Meditation master for Dhyana path.
- Schism figure only if evolution active.

Real historical advisors require sourced portrait handling if visible. Fictional advisors can use generated portraits only if the asset scope includes them.

## Flags and cosmetic tags

Flag coverage:

- Base Holy Realm flag for each origin if needed.
- Awakened Realm flag or cosmetic tag after Buddhahood.
- Empty Seat flag after Final Silence if non-terminal path continues.
- False Mandala flag if schism route becomes a country or cosmetic state.
- Puppet variants only if the country can become a subject.

Flag design direction:

- Clean, readable at HOI4 sizes.
- Use lotus, wheel, mountain, bell, or empty seat motifs.
- Avoid generated text.
- Sourced historical symbols if using real religious or national symbols.
- Fictional variants may use generated art with manifest notes.

## Formable and identity expansion

The Holy Realm can form a larger non-conquest identity only if the route earns it.

Working formable: `The Great Mandala`.

Formation type: cosmetic tag or new tag only if the implementation has a strong reason. A cosmetic tag is preferred if the country remains the same political entity.

Requirements:

- Buddhahood complete.
- Sangha Compact exists with at least three stable members, or Holy Realm controls and protects the required sanctuary corridor states.
- No ordinary conquest disqualifier.
- Defilements below 20.
- Completion of the focus `No Empire of the Wheel` or equivalent.
- Post-formation integration missions for any newly controlled territory.

Effects:

- Rename country and adjective.
- New flag.
- Unlock post-formation stabilization decisions.
- No instant broad cores. Grant claims, compliance support, or staged cores through missions.
- Super-event only if formation changes regional order or occurs after Buddhahood.

Hidden formable: `The Silent Mandala`.

Requirements:

- Final Silence non-terminal completion.
- Empty Seat aftermath.
- Compact still exists.
- No active schism.

This is a rare identity state, not a conquest reward.

## AI actors

### Holy Realm AI

Early priorities:

- Survive.
- Build sanctuary infrastructure.
- Complete safe teaching missions.
- Avoid ordinary offensive wars.

Mid priorities:

- Reach Dhyana Depth 3 or 4.
- Help nearby countries threatened by chaos.
- Form compact if world-threat conditions support it.

Late priorities:

- Use Buddha powers against active chaos countries.
- Avoid Final Silence unless requirements are met and chaos is high.
- If capital is threatened, use Seated in the Sky or Wrathful Protection.

AI should not choose high-risk schism shortcuts unless chaos is very high or the country is near collapse.

### Compact member AI

Should join if:

- Threatened by chaos.
- Has teaching history with the Holy Realm.
- The Holy Realm has not conquered normal neighbors.
- The member lacks better protection.

Should refuse if:

- It is a chaos country.
- It is a puppet of a hostile major power.
- It distrusts the Holy Realm due to conquest or schism.

### Major power AI

Should react with skepticism and interest:

- Democratic or neutral powers may support refugee corridors.
- Fascist or militarist powers may fear the compact or try to influence it.
- Communist powers may support anti-chaos work but resist religious diplomacy, depending on ideology and relations.
- Major powers fighting chaos should value Buddha powers and teaching relief.
- Major powers should not join the compact casually if it conflicts with their faction obligations.

### Chaos country AI

Should treat the Holy Realm as a strategic threat after Buddhahood:

- Prioritize disrupting teaching routes.
- Target compact members to lower cohesion.
- Attack sanctuary corridors if feasible.
- If zombies or aliens have special logic, add Holy Realm as a priority after first power display.

Do not let chaos AI chase the Holy Realm across impossible terrain if no route exists.

## AI decision matrix

| Situation | Holy Realm AI action | Avoid |
| --- | --- | --- |
| Peace, low chaos | Teaching, infrastructure, meditation | Final Silence rush |
| Nearby chaos war | Teach Under Bombardment, relief corridors, guard routes | Ordinary conquest |
| Capital threatened | Guardian focuses, Wrathful Protection, emergency meditation | Long foreign missions |
| Bodhi high, Defilements low | Push Fourth Dhyana and Buddhahood | Schism shortcuts |
| Bodhi high, Defilements high | Reduce Defilements, resolve schism risk | Transformation attempt |
| Buddha exists, chaos enemy active | Use powers based on front need | Powers against normal countries |
| Chaos above 1000, all requirements met | Consider Final Silence | Ritual if capital unsafe |
| Compact member falling | Send relief or Seated in the Sky | Ignore and lose cohesion |

## Documentation needs

The event doc must include:

- Target selection logic.
- Country identity states.
- Leader and portrait stages.
- Starting ideas and lifecycles.
- Starting force scaling.
- Focus tree routes.
- Decision categories.
- Mandala GUI and animation state requirements.
- Super-events.
- Final Silence world-end and non-terminal variants.
- Achievement and formable notes.
