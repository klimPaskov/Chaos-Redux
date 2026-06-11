# Holy Realm: Buddhahood and the Final Silence

Event slug: `holy_realm_buddhahood`

Event id: `003`. Use the existing Chaos Redux event namespace `chaosx.nr3.*` for implementation.

Primary actor: the Holy Realm. Target selection should use Tibet first. If Tibet is gone, use Bhutan or Nepal only if one exists and is valid. If no valid country exists, the event should appear as unavailable in manual event views and must not queue a delayed event against a missing tag.

Core promise: the Holy Realm begins as a fragile mountain sanctuary led by a Bodhisattva. Through teaching missions, disciplined meditation, and sacrifices made under chaos pressure, the Bodhisattva draws closer to Buddhahood. When the leader becomes the Buddha, the portrait, country identity, focus tree, decision category, mandala panel, and super-event presentation all change. The Buddha can show supranormal powers, but only after a meditation ritual charges them. The Final Silence is the ultimate route. It can only begin after Buddhahood and represents the in-game approach to Ultimate Nirvana.

This is not a generic holy war event. The Holy Realm is strongest against countries marked by Chaos Redux as inhuman, world-threatening, or event-created chaos actors, such as zombies, aliens, and equivalent high-chaos states. Against ordinary countries, the Holy Realm should rely on diplomacy, sanctuary, defensive terrain, and teaching missions. The strongest powers must be gated by meditation, high campaign stakes, and visible sacrifice.

## Tone and handling

The event uses Buddhist vocabulary as an alternate-history and supernatural Chaos Redux mechanic. Player-facing text should stay reverent, austere, and direct. It should avoid parody, crude jokes, and cheap irony around Nirvana, Buddhahood, monks, relics, or living religious symbols.

The Holy Realm's power should feel frightening because it is calm. The best atmosphere is a world at war hearing bells from a mountain country that should be too weak to matter, then watching chaos countries fail to cross a river, breach a pass, or keep their armies coherent after the Buddha enters meditation.

## Campaign role

The Holy Realm is a late-developing anti-chaos anchor. Early gameplay is survival and moral preparation. Mid-game is teaching, sanctuary building, and meditation. Late game is the transition to Buddhahood, revealed powers, and the Final Silence route.

The Holy Realm should not become a universal conquest tag. It may intervene against chaos countries and may liberate occupied holy or sanctuary regions, but it should receive penalties or disqualifiers for predatory conquest against normal countries. It can create a defensive and humanitarian faction, the Sangha Compact, but the faction needs membership rules, shared goals, and failure states.

## Main values

| Value | Range | Meaning | Visible surface | Changes through |
| --- | --- | --- | --- | --- |
| Bodhi Progress | 0 to 108 | How close the Bodhisattva is to Buddhahood | Mandala ring, leader tooltip, event details | Teaching missions, compassion choices, focus rewards, major sacrifices |
| Dhyana Depth | 0 to 4 | Depth of meditative absorption | Mandala lotus, meditation decision tooltip | Meditation vows, focus path, no-war retreats, completed sanctuary work |
| Compassion | 0 to 100 | Public and spiritual legitimacy of the path | Mandala lower left value, spirit tooltip | Refuge missions, mercy choices, avoiding normal conquest, healing chaos damage |
| Detachment | 0 to 100 | Ability to use power without worldly corruption | Mandala upper right value | Renunciation focuses, refusing territorial rewards, accepting political costs |
| Defilements | 0 to 100 | Remaining worldly corruption and spiritual risk | Mandala cracked mirror, warning pulse | Failures, using powers for ordinary war, conquest of normal countries, schism events |
| Meditation Charge | 0 to 100 | Stored concentration for Buddha powers | Central mandala glow and power buttons | Channeling ritual, jhana focus completions, retreat missions |
| World Suffering | dynamic | How much chaos pressure the Holy Realm can perceive | Mandala outer flame and event details | Active world threats, deaths, chaos value, chaos countries at war, fallen capitals |
| Sangha Cohesion | 0 to 100 | Strength of the humanitarian compact | Faction panel, decisions, event details | Members aided, members ignored, war state, foreign pressure, failed votes |

Bodhi Progress by itself is not enough. Buddhahood requires:

- Bodhi Progress at 108.
- Dhyana Depth at 4.
- Defilements below 20.
- At least 12 successful teaching missions, with at least one mission completed during a major chaos crisis.
- Completion of the focus `The Unshaken Seat`.
- The transformation event and super-event have not already fired.

If the player reaches 108 Bodhi Progress with high Defilements, the route stalls into the False Buddha Schism evolution instead of becoming the Buddha.

## Baseline stages

Baseline stages are the normal flow of the event. They must not be logged as evolutions.

### Stage 0: A Rumour in the Mountains

The Holy Realm is identified. The Bodhisattva appears as a leader or national figure. The country receives early spirits that make it fragile but spiritually unusual.

Opening spirits:

| Spirit | Role | Starting effect direction | Lifecycle |
| --- | --- | --- | --- |
| Fragile Sangha | The realm is not ready for a world role | Lower recruitable population, weaker political gain, better resistance to panic | Mitigated by teaching and governance focuses |
| Remote Sanctuaries | Mountain isolation protects and limits the country | Strong defense on core mountains, weaker trade and industry | Can become Pilgrimage Roads or Sealed Valleys |
| Worldly Burden | The Bodhisattva must lead a state while seeking liberation | Small Defilements gain from ordinary wars and conquest | Removed at Buddhahood or worsened by schism |

Player experience: the country is not yet powerful. The first choices decide whether the Holy Realm opens itself to refugees and teaching, stays defensive, or rushes worldly security.

### Stage 1: Teaching Missions

The player unlocks a rotating mission system. Teaching missions send monks, doctors, translators, envoys, and protectors into target countries or regions. They are not passive clicks. Most require resources, route access, a safe corridor, a target state, or a temporary objective.

Success gives Bodhi Progress and one virtue value. Failures raise Defilements, spawn schism rumours, or reduce Sangha Cohesion. Repeated success against chaos pressure makes the world start treating the Bodhisattva as more than a local monk.

### Stage 2: The Four Dhyana Path

The Holy Realm begins formal meditation training. This is where the mandala panel becomes central. The player can start vows, retreats, and concentration rituals. Dhyana Depth unlocks at 1, 2, 3, and 4. Each depth changes the mandala, the leader portrait, and available decisions.

Dhyana progression should be slow enough that the player plans around it. A country at war may still advance, but it must protect sanctuaries and accept opportunity costs.

### Stage 3: The Unshaken Seat

At high Bodhi Progress, the Bodhisattva enters a final preparation state. The portrait changes to the Great Bodhisattva stage. The country receives stronger defensive and diplomatic tools. The player must complete a final set of missions:

- Protect the capital sanctuary.
- Complete one teaching mission in a country threatened by chaos.
- Bring Defilements below 20.
- Reach Dhyana Depth 4.
- Complete the focus `The Unshaken Seat`.

### Stage 4: Buddhahood

When all requirements are met, the transformation event fires. The super-event `The Awakened One` appears. The leader becomes the Buddha through a character swap or portrait stage change. The mandala becomes fully active. The power decisions unlock, but they still require Meditation Charge.

The country spirit `Revealed Powers of the Buddha` is not permanent by default. It appears after the first power display and then can be renewed through meditation. A weaker permanent spirit, `The Awakened Seat`, represents the new leader identity.

### Stage 5: The Final Silence

The Final Silence route becomes visible only after Buddhahood. It has two forms.

If global chaos is below the world-end threshold, the route is an endgame spiritual victory path. It produces enormous anti-chaos suppression, a unique aftermath, and a leader succession through the Empty Seat, but it does not set `world_end`.

If global chaos is above the world-end threshold, the route can become a terminal world-end scenario. It sets `world_end`, sets `world_end_final_silence`, shows the Final Silence super-event, stops incompatible event branches, and records the terminal state in the event log and spreadsheet.

The Final Silence should never be available before Buddhahood. It should also require the player to have shown at least one Buddha power against a real chaos country. The route represents the Buddha using the supramundane end of defilements, not simply pressing a victory button.

## True evolution tracks

Evolutions are not normal stages. They are mutation tracks that alter how the event behaves.

### Evolution A: The Pattern of Suffering

Condition: at least four teaching missions completed across different regions, and at least one world threat active.

Effect: the Holy Realm learns to identify chaos countries earlier. The event log records the Holy Realm as a world-threat observer. Teaching missions against threatened countries gain higher reward, but the Holy Realm draws attention from chaos actors.

Content unlocks:

- Decision `Read the Pattern in the Wheel`.
- Mandala outer flame state.
- Event-log evolution entry `Pattern of Suffering`.
- AI behavior that directs the Holy Realm toward the most dangerous chaos source.

### Evolution B: False Buddha Schism

Condition: Bodhi Progress reaches 90 or more while Defilements are 50 or more, or the player uses Buddha-like powers before the actual Buddhahood flag through a rare failed relic event.

Effect: a pretender movement appears. This may create internal unrest, a rival character, or a small hostile cult tag only if the map and campaign state support it. The schism tries to turn the mandala into a worldly weapon.

Content unlocks:

- Decisions to reconcile, exile, debate, or suppress the pretender.
- A possible leader portrait variant for the False Buddha.
- A hidden achievement for resolving the schism without executions or ordinary conquest.
- A high-risk shortcut to power that disqualifies the clean Final Silence route.

### Evolution C: The Relic Mandala

Condition: the Holy Realm controls or protects enough holy sites or receives relics through foreign missions.

Effect: the mandala panel gains a relic ring. Meditation Charge cap increases. Powers become stronger, but failures can raise Defilements faster.

This evolution should require real map or diplomatic work, not only a focus. The player must hold named sanctuary states, secure pilgrimage corridors, or receive relics from aligned countries.

### Evolution D: Wrathful Protection

Condition: a chaos country kills enough civilians, conquers a Sangha Compact member, or threatens the Holy Realm capital.

Effect: the Holy Realm unlocks emergency powers that are stronger against chaos armies but risk Defilements. The route does not make the Buddha cruel. It represents terrifying compassionate protection under extreme conditions.

Content unlocks:

- Stronger anti-chaos combat decisions.
- Warning pulse on the mandala panel.
- AI permission for more aggressive anti-chaos action.
- Failure chance that increases if the player also wars against normal countries.

## Connections to Chaos Redux systems

The event must connect with the shared world-threat framework. The Holy Realm should not invent parallel chaos-threat flags when existing world-threat state exists. It should read active chaos sources and special country classifications.

The event should respect global random-event registration, event log naming, debug naming, event details, evolution details, super-event slots, and event catalog alignment.

The strongest anti-chaos effects must only apply against countries that are tagged or classified as chaos threats. The implementation should define a reusable trigger such as `is_holy_realm_chaos_enemy = yes` if an equivalent does not already exist. This trigger should include zombies, aliens, Great Revolution style chaos countries, and future chaos-country sources. It should exclude ordinary countries unless they have a specific chaos-source flag.

## High-level event map

Implementation uses the assigned namespace `chaosx.nr3.*`.

| Event | Role | Visible to player |
| --- | --- | --- |
| `chaosx.nr3.1` | Bootstrap and target selection | No |
| `chaosx.nr3.2` | First reveal of the Holy Realm | Yes |
| `chaosx.nr3.3` | Mandala panel unlocked | Yes |
| `chaosx.nr3.10` to `.29` | Teaching mission reports | Yes |
| `chaosx.nr3.30` to `.39` | Meditation vow reports | Yes |
| `chaosx.nr3.40` | The Unshaken Seat | Yes |
| `chaosx.nr3.50` | Buddhahood transformation | Yes |
| `chaosx.nr3.51` | Buddhahood super-event driver | Hidden or system event |
| `chaosx.nr3.60` to `.69` | Buddha power displays | Yes |
| `chaosx.nr3.70` | Final Silence ritual begins | Yes |
| `chaosx.nr3.71` | Final Silence completion, non-terminal | Yes |
| `chaosx.nr3.72` | Final Silence world-end | Yes |
| `chaosx.nr3.80` to `.99` | Evolution events | Mixed |
| `chaosx.nr3.100` to `.119` | Sangha Compact and foreign reactions | Mixed |

## Event log and details direction

The event log should show the Holy Realm as a major spiritual actor after the first reveal. Before the event fires, manual event views should show the valid target or `N/A` if no target exists.

Event detail text should have three states:

1. Before Buddhahood: the world sees a teaching realm with growing rumours.
2. After Buddhahood: the world sees a Buddha capable of visible powers.
3. During Final Silence: the event details should become sparse, with almost no dramatic language. The silence should feel like the point.

Evolution detail text should separate real evolutions from normal stages. The False Buddha Schism, Pattern of Suffering, Relic Mandala, and Wrathful Protection are evolution tracks. Ordinary teaching and meditation progress are not.

## Balance target

The Holy Realm should be weak early, difficult to snowball, and extremely valuable against high-chaos enemies after Buddhahood. It should not be able to use Buddha powers for ordinary annexation without spiritual penalties. A player who tries to become a normal conqueror should still be strong defensively, but they should lose access to the clean Final Silence route and risk schism.

The clean route should be difficult:

- Many missions.
- Real map and supply objectives.
- Low Defilements.
- Dhyana Depth 4.
- No abuse of powers against normal countries.
- At least one meaningful anti-chaos act before Final Silence.

The high-chaos route should be tempting:

- Faster power activation.
- Stronger anti-chaos combat.
- Higher risk of Defilements and schism.
- More dangerous visuals and super-event tone.
