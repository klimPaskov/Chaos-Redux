# Event 010 — Death: Country Package, Focus Tree, Units, and Identity

## Country package matrix

| Surface | Design requirement |
| --- | --- |
| Proposed tag | `DTH`, final implementation must conflict-check against vanilla, Chaos Redux, and common mod tags. |
| Country name | `Death` |
| Adjective | `Death` or `Deathly`; use the shorter player-facing form unless localisation requires adjective distinction. |
| Leader | `Zol` |
| Leader type | Fictional supernatural/nonhuman singular ruler. |
| Map color | Complete black. |
| Flag | Near-black or pure-black fictional flag; no text; may use subtle cloth/void texture for readability but the map color remains pure black. |
| Starting state | Random eligible remote island state. |
| Capital | Origin state at creation; can move to latest mainland foothold if the origin is occupied and engine needs a controlled capital. |
| Ideology | Use the least disruptive existing ideology if no custom chaos ideology exists, likely neutrality with special scripted classification. |
| Ruling party | `Zol` or `The Last Office`; short and uncanny. |
| Elections | None. |
| Diplomacy | No normal diplomacy before reveal. After reveal, automatic war with neighbors and world-threat behavior. |
| Faction | None for Death. Herald countries may enter a separate `Black Oath` relation, but Death itself does not form a normal alliance. |
| Industry | None. Death deletes industry in every state it consumes and should not produce equipment normally. |
| Manpower | Do not use state manpower. Consumed population is stored in event variables and drives spread/ghost scaling. |
| Starting divisions | None. |
| Navy/Air | None. Spread across sea happens through the coastal-jump mechanic, not a navy. |
| Cores | Every consumed/controlled state is cored by Death for safety. |
| State resistance | None inside Death-controlled states because they are Death cores and have zero population. |
| Classification | Register as `is_special_chaos_country`; also register as `is_actual_nonhuman_country`. |
| Playability | AI-controlled by default. If debug/manual play exposes it, use the fixed-purpose focus tree below. |

## Leader: Zol

Zol should not feel like a conventional portrait leader. The player sees a name and a face-like absence.

Asset direction:

- generated fictional/nonhuman portrait;
- 156x210 HOI4-style leader portrait;
- black figure or void-lit bust, not a real person;
- period-compatible painterly finish, not modern fantasy splash art;
- no readable text;
- no gore;
- static fallback required;
- world-end portrait package with a static leader fallback and a registered eight-frame animated sprite built from real generated frames, not a filter pulse.

Zol should have a unique leader trait direction such as `God of Death`. The trait should not grant ordinary political bonuses. It should clarify that Death does not use industry, elections, or normal manpower.

## Country names and cosmetic states

Death should not have normal ideology variants such as democratic Death or communist Death. If the engine requires ideology-specific localisation keys, they should all resolve to `Death` with appropriate `_DEF` and `_ADJ` forms.

Potential localisation set:

- `DTH: "Death"`
- `DTH_DEF: "Death"`
- `DTH_ADJ: "Death"`
- `DTH_neutrality: "Death"`
- `DTH_neutrality_DEF: "Death"`
- `DTH_neutrality_ADJ: "Death"`

Do not add playful ideology labels. The simplicity of the name is the point.

## Starting setup

Death starts with:

- no units;
- no factories;
- no production lines;
- no research slots that matter;
- no advisers;
- no recruitable manpower;
- no starting navy, air force, or equipment;
- one controlled consumed island state;
- hidden spread variables initialized;
- no public war unless the origin state transfer requires a temporary hidden conflict, in which case it must be cleaned immediately.

The country should not need a normal economy because its power comes from scripted consumption, withering, and ghost hosts. Any normal industry gained through edge cases must be deleted by maintenance cleanup.

## Death-specific ideas

Death should have very few ideas. They are not a reward ladder. They represent rules.

| Idea | Start/unlock | Role | Lifecycle |
| --- | --- | --- | --- |
| `Country Without Breath` | Start | Blocks normal economy, manpower, diplomacy, and politics. | Permanent while Death exists. |
| `The First Silence` | Start | Keeps early behavior passive and hidden. | Replaced by `Public Death` after reveal. |
| `Public Death` | Mainland reveal | Enables world-threat, withering, and neighbor wars. | Replaced by the world-end Death idea at world-end. |
| `World-End Death` | World-end | Enables aggressive ghosts and continental foothold behavior. | Permanent until Death or the world ends. |
| `The Black Census` | 600-tier or later | Converts consumed population into ghost scaling. | Upgrades at 800 and world-end tiers. |

Do not add new ideas for every focus or every spread stage. Use idea replacement or modifiers to the same small idea set.

## Unit package

### No starting army

The absence of units is required. Early Death should be possible to stop by a country that discovers it and occupies the island.

### Ghost unit type

The custom unit exists only after evolution unlock.

Suggested unit type: `death_ghost_host`

Design goals:

- cheap to script-spawn but not recruit normally;
- zero or scripted manpower source;
- poor supply use if possible, because they are not living formations;
- poor stats at first;
- severe organization cap early;
- no ordinary equipment dependence unless implementation needs a dummy equipment type;
- compatible with AI passive/aggressive behavior changes by tier.

### Template scaling

| Tier | Spawn ratio direction | Stats direction | AI behavior |
| --- | --- | --- | --- |
| Tier 0 | No divisions. | None. | Passive country. |
| 600 tier | Very low ratio: one weak host per several consumed states or a large consumed-population band. | Much weaker than infantry, very low org. | Hold borders, do not attack. |
| 800 tier | More divisions per state/population band. | Still weaker than infantry, slightly better org and defense. | Hold, local counterattacks only when enemy is exhausted. |
| World-end | Many divisions, especially in footholds. | Comparable to ordinary infantry. | Aggressive attacks and exploitation. |

The implementation should use script constants for ratios, caps, minimums, and maximums. Death should not spawn 100 divisions from eating a few islands, but it should become terrifying after consuming millions.

### Ghost names

Division name pool directions:

- `Pale Host`
- `Thin Column`
- `Mourning Line`
- `Ruin Host`
- `Black Infantry`
- `The Uncounted`
- `No. [n] Silence`

Avoid joke names. The tone should be quiet and official, like a broken registry.

## Death focus tree role

Death is a fixed-purpose chaos country. It does not need normal democratic, communist, fascist, monarchist, industry, diplomacy, or expansion politics. It does need a structured progression surface if the tag becomes playable through debug or a triggerable scenario, and the AI needs route-aware behavior.

The Death focus tree should be narrow, nonstandard, and stage-gated. It exists to express method, shroud, ghosts, coastal recovery, and endgame hunger, not normal country-building.

If the implementation chooses to represent these paths through scripted progression rather than a visible focus tree, the same branch logic must still exist in mechanics, AI, docs, and event-log detail. Do not replace it with a single linear scripted ladder.

## Focus tree architecture map

```text
                          [The First Silence]
                                  |
                         [A Country on the Island]
                                  |
             ------------------------------------------------
             |                    |                         |
       SHROUD LANE           HUNGER LANE              CENSUS LANE
   concealment/reports   target selection/spread     deaths -> ghosts
             |                    |                         |
 [No Mail Before Spring]  [Lowest Names First]      [The Black Census]
 [Weather on Paper]       [Ports Without Voices]    [No Graves Needed]
 [The Island Pattern]     [The Mainland Smell]      [First Ghost Muster]
             |                    |                         |
             -----------------[Public Death]-----------------
                                  |
             ------------------------------------------------
             |                    |                         |
       COASTAL LANE         WASTELAND LANE            HOST LANE
   jumps and footholds    wither and occupation    ghost strength/AI
             |                    |                         |
 [The Tide Learns Roads]   [Every Road Slows]       [Mourning Host]
 [Another Shoreline]       [The Empty Supply]       [Ruin Host]
 [No Ferry Returns]        [State Without State]    [Orders Without Breath]
             |                    |                         |
             ----------------[World-End Footholds]----------------
                                  |
                           [World Consumed]
```

The tree should not be a vertical checklist. The opening trunk establishes the silent country. Three pre-reveal lanes govern concealment, hunger, and population-to-ghost preparation. The reveal node `Public Death` unlocks the post-reveal lanes. The world-end node gates the final focus. Exact focus names can be adjusted by implementation and must not be treated as researched super-event text.

## Focus path details

### Opening trunk

| Focus group | Purpose | Unlocks/changes |
| --- | --- | --- |
| `The First Silence` | Establishes the origin state and passive early behavior. | Sets early hidden state if not already set by event. |
| `A Country on the Island` | Makes Death visible as a country but not yet public as a threat. | Keeps no-army status; reinforces deletion of normal economy. |

These focuses should be very short or auto-completed for AI because the event script already creates the state. They are a presentation and debug-play surface, not a normal 70-day opening.

### Shroud lane

Narrative role: the world fails to notice.

Mechanical role:

- extends or manipulates report delays;
- reduces early investigation chance;
- makes low-chaos island spread quieter;
- adds pre-reveal report variants.

Anchor focuses:

| Focus | Role |
| --- | --- |
| `No Mail Before Spring` | The first report delay becomes longer unless a player owns nearby assets. |
| `Weather on Paper` | Report text points to storms, broken radios, and missing cargo manifests. |
| `The Island Pattern` | Repeated island reports begin, but Death remains unnamed. |

Tradeoff: the Shroud lane delays global response but does not strengthen Death militarily. If the player finds Death anyway, it remains easy to kill.

### Hunger lane

Narrative role: Death chooses the least defended names first.

Mechanical role:

- strengthens low-pop island target preference;
- increases spread pressure from consumed states;
- moves toward mainland eligibility;
- makes consumed population more important.

Anchor focuses:

| Focus | Role |
| --- | --- |
| `Lowest Names First` | Early targeting strongly prefers the smallest populations. |
| `Ports Without Voices` | Island ports and piers vanish as possible report hooks. |
| `The Mainland Smell` | Mainland target weighting opens once enough island pressure exists. |

Tradeoff: faster spread makes discovery more likely. More missing reports mean more countries can investigate.

### Census lane

Narrative role: every consumed person becomes a number in Zol's book.

Mechanical role:

- stores consumed population cleanly;
- prepares later ghost scaling;
- unlocks ghost evolutions once chaos permits.

Anchor focuses:

| Focus | Role |
| --- | --- |
| `The Black Census` | Consumed population becomes the main scaling value. |
| `No Graves Needed` | Population loss reports become stranger and harder to classify. |
| `First Ghost Muster` | Enables 600-tier weak ghosts when evolution permits. |

Tradeoff: this lane does nothing if Death has not consumed enough population. It rewards a long-hidden Death, not a tiny island start.

### Public Death convergence

`Public Death` unlocks after the mainland reveal trigger. It should not be completed before reveal. It updates ideas, event logs, world-threat state, and war behavior.

### Coastal lane

Narrative role: the sea carries Death back after local victory.

Mechanical role:

- unlocks coastal-jump recovery;
- reduces jump cooldown at higher tiers;
- opens world-end foothold logic;
- interacts with enemy coastal watch decisions.

Anchor focuses:

| Focus | Role |
| --- | --- |
| `The Tide Learns Roads` | Death can return to nearby coasts after being pushed back. |
| `Another Shoreline` | Coastal jump target pool expands. |
| `No Ferry Returns` | Enemy evacuation and patrol decisions become less effective at high chaos. |

Tradeoff: coastal recovery spends spread pressure and exposes Death to more countries at once.

### Wasteland lane

Narrative role: territory stops being territory.

Mechanical role:

- strengthens state modifier penalties;
- improves withering of unguarded neighboring states;
- makes recaptured Death states hard to use;
- creates stronger occupation hazards.

Anchor focuses:

| Focus | Role |
| --- | --- |
| `Every Road Slows` | Movement penalties become harsher. |
| `The Empty Supply` | Supply hubs, ports, and rail in Death states become useless. |
| `State Without State` | Recaptured wastelands remain permanently empty unless outpost projects succeed. |

Tradeoff: stronger wasteland penalties also slow Death's ghost movement until the Host lane catches up.

### Host lane

Narrative role: the dead country learns to hold borders.

Mechanical role:

- improves ghost templates;
- changes AI from passive to local counterattack to aggressive at world-end;
- spawns ghost divisions according to consumed population and stage.

Anchor focuses:

| Focus | Role |
| --- | --- |
| `Mourning Host` | 800-tier ghost strengthening. |
| `Ruin Host` | World-end ghost template. |
| `Orders Without Breath` | AI aggression toggles for world-end. |

Tradeoff: more divisions make Death more visible and easier for AI majors to prioritize as a war threat.

### World-end footholds and world consumed branch

The world-end foothold branch requires the terminal conditions: continent consumed and Chaos above 1000. It creates one coastal foothold on every continent that does not already contain a Death-consumed state, immediately spawns local Last Shore hosts for real world-end starts, and then unlocks the aggressive host behavior. Triggerable scenario starts preserve their separate intensity-scaling host pass instead of double-spawning local foothold hosts.

The final branch unlocks only when all eligible states are consumed. It should fire the final super-event and achievement. It is not a normal focus reward; it is a campaign ending. Exact final focus names should not be treated as super-event titles.

## Focus filters and categories

Death's focus tree should use custom filter categories if the existing system supports them:

| Filter | Applies to |
| --- | --- |
| Death: Shroud | Concealment and report-delay focuses. |
| Death: Hunger | Spread and target-selection focuses. |
| Death: Census | Consumed-population and ghost-scaling focuses. |
| Death: Wasteland | State effects and wither focuses. |
| Death: Host | Ghost division focuses. |
| Death: Last Shores | World-end and final-state focuses. |

## AI focus behavior

Death AI should not choose focuses randomly. Its progression should be mostly scripted by stage and available content.

AI priority:

1. Opening trunk at creation.
2. Shroud if hidden and few reports have fired.
3. Hunger if island spread is too slow.
4. Census if consumed population is high enough to make future ghosts useful.
5. Public Death once reveal has fired.
6. Wasteland if it has mainland borders and withering opportunities.
7. Coastal if it has been pushed back or lacks mainland footholds.
8. Host if ghost tier is available.
9. Last Shores when terminal conditions exist.

AI should not pursue world-end focus content before the required conditions are true.

## Herald and necromancy identity packages

Some countries may interact with Death through dark methods or joining Death. These are not Death itself.

### Necromantic defender

A country at war with Death can unlock dark anti-Death methods after:

- recapturing a Death wasteland;
- suffering high casualties against Death;
- reaching high chaos;
- completing an investigation or black-book decision.

Identity changes:

- no country rename by default;
- national spirits such as `death_black_book_offices`, `death_black_book_scandal`, or the active Black Oath/Black Apostolate spirits;
- potential advisor/council unlocks;
- high stability/war support/condemnation risks;
- special bound-shade units that are weak, capped, and politically dangerous.

### Herald of Zol

A country can pledge to Zol through a high-risk alternate path. This is the join-Death route.

Eligibility should be narrow:

- Death publicly revealed;
- country is at war with Death or borders a Death wasteland;
- high chaos or severe desperation;
- not already a special nonhuman country;
- player choice, or AI only under extreme conditions;
- not a required democratic containment leader unless overrun and unstable.

Effects:

- country gains `death_herald_of_zol`;
- leaves or breaks from containment compact;
- gains temporary protection from Death target selection;
- receives `Black Oath` and Herald decisions;
- can feed states, prisoners, equipment, or names to Death for power;
- suffers stability, legitimacy, and diplomatic collapse;
- becomes hostile to containment countries;
- risks eventual consumption if it fails to keep paying the oath.

Possible cosmetic identity:

- `Herald of Zol` as a temporary cosmetic name, not a full formable tag by default;
- blackened route flag and localisation through the Herald cosmetic tag;
- leader keeps identity while the country carries the Black Oath national idea.

This route must not turn Death into a friendly normal faction member. It is an evil bargain with a country that may still be eaten.

## Formable assessment

Death itself should not form a larger country. Its final form is the whole map, not a formable title.

The Herald route includes a formable-like cosmetic transformation, `The Black Apostolate`. It is hidden and difficult:

- player is a Herald of Zol;
- controls a large number of wasteland states without being consumed;
- keeps Death alive into world-end stage;
- accumulates enough name debt, black favor, and deliberately sacrificed wasteland states;
- accepts permanent diplomatic isolation;
- cannot restore normal population.

It uses:

- cosmetic name and adjective;
- flag variants;
- a national idea;
- decisions and achievement hook;
- AI block;
- no free cores over living states unless those states have been consumed or deliberately sacrificed.
