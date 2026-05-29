# Super-Event Prompt: Event 6 Independence Wave

Use `chaos-redux-super-events` only for evolved Independence Wave moments that deserve super-event treatment. The base minor repeatable event should not receive a super-event.

Event 006 is independent from Event 005. Do not use Soviet Collapse presentation, quotes, audio, imagery, event-log framing, or republic-collapse tone for an Event 006 release. Shared tags and Soviet republic style tags released by Independence Wave need Event 006 presentation. Reuse only generic historical symbols or sourced material that does not imply Event 005 mechanics.

## Required super-event candidates

### First League of New States

Role: faction formation and world-order signal.

Trigger direction:

- at least three Independence Wave countries exist
- coalition cohesion is high
- League Charter focus or equivalent decision completed
- formal faction creation happens
- the league is independent from major-power puppet control

Tone:

- diplomatic, tense, small states acting with unexpected seriousness
- not apocalyptic
- the world notices that weak states have created a bloc of their own

Image direction:

- period diplomatic congress room
- many small flags
- delegates around table
- stark composition

Quote direction:

- real quote about self-determination, small nations, sovereignty, or balance of power
- public domain or historical source preferred

Audio direction:

- restrained, tense, state ceremony mood
- no action music

### The Great Partition Week

Role: high-chaos release scale reveal.

Trigger direction:

- Evo IV or Evo V wave releases at least eight countries
- at least one historical-return or local-polity package appears
- no previous mass-wave super-event has fired

Tone:

- bureaucratic shock and map-room panic
- not one empire collapsing, but the whole language of borders failing
- emphasize many committees acting at once

Image direction:

- map room, telegraph office, newspapers, or officials pinning many small flags
- period-compatible where possible

Quote direction:

- real quote about nations, borders, self-determination, state power, or political order

Audio direction:

- tense and procedural, not heroic

### The First Old Name Returns

Role: first high-chaos historical-return state that changes the tone of the event.

Trigger direction:

- first implemented historical-return package becomes independent through Event 006
- examples include Assyria, Mesopotamia, Volga Bulgaria, Sokoto, Kanem-Bornu, Buganda, Asante, Mapuche Araucania, Palmares, or similar package
- the package was released by Independence Wave origin, not another event

Tone:

- diplomats expected a small new state and instead see an old name on the wire
- serious, uncanny, political
- not automatically supernatural

Image direction:

- archive, old map, seal, treaty table, palace room, local council, or map office

Quote direction:

- real quote about history, memory, peoples, statehood, or old names returning

Audio direction:

- restrained historical gravity

### The First Impossible State

Role: reveal of high-chaos transformation.

Trigger direction:

- first Anti-Mankind Directorate, Necromantic Custodianship, Archive-State, or equivalent strange country becomes independent through Event 006
- no previous strange Independence Wave super-event has fired

Tone:

- observers cannot agree what kind of state has appeared
- reports describe bureaucrats, seals, census offices, or border guards before naming the horror
- do not reveal every mechanic in the text

Image direction:

- symbolic or generated if fully invented
- if using a photo base, it should be period-compatible and transformed through asset workflow

Quote direction:

- real quote about state power, death, mankind, law, or the loss of human categories
- avoid invented quotes

Audio direction:

- cold, restrained, ceremonial dread
- no horror jump-scare tone

## Required documentation

For each super-event:

- role
- trigger
- localisation title and description
- quote and attribution
- cultural remark or button line
- image source or generation plan
- audio source, license, converted file, sound definition, and wiring
- event-origin check if using a tag that can also appear in another event

## Expanded super-event package design

Super-events are rare escalation signals for Event 006. The ordinary wave does not get one. The super-event should fire only when the event changes the world order, reveals a high-chaos identity, or pushes small-state politics into factional or impossible territory.

### Super-event gating rules

| Rule | Requirement |
| --- | --- |
| Origin lock | The actor must have `chaosx_release_origin_independence_wave` or the event context must be Event 006 |
| No Event 005 dependency | Shared tags and Soviet republic style tags never inherit Event 005 super-events because they share geography or tag identity |
| One reveal per role | The first old-name reveal, first impossible state, and first formal league each get one global reveal |
| No spam | Repeat waves use normal news or event log entries unless they exceed a higher threshold |
| Settings-aware playback | Follow existing super-event settings and skip safely when disabled |
| Documentation alignment | Add super-event docs, catalog note, asset manifest row, localisation, audio note, and event log entry together |

### Required super-event package table

| Key | Role | Minimum trigger | Why it deserves treatment |
| --- | --- | --- | --- |
| `independence_wave_first_league` | first small-state faction | League of New States forms with at least three independent Event 006 members | first world-order shift from repeated small breakaways |
| `independence_wave_great_partition_week` | high-chaos mass wave | Evo IV or Evo V releases eight or more countries and includes old or local package | map shock, not a normal release |
| `independence_wave_first_old_name` | first historical-return state | first researched historical-return package releases through Event 006 | changes tone from modern separatism to old-state restoration |
| `independence_wave_first_impossible_state` | first strange package | first necromantic, anti-mankind, archive-state, or impossible package releases | reveals the event can create non-normal states |
| `independence_wave_league_war` | small-state league enters major conflict | League of New States fights a major or a patron coalition | proves the wave is now a military bloc |
| `independence_wave_human_renunciation` | anti-mankind doctrine public reveal | Event 006 state adopts anti-mankind route and controls enough territory to matter | rare World Collapse escalation |
| `independence_wave_the_rump_that_endures` | host survival signal | huge high-chaos wave reduces a major host to one state but does not erase it | reinforces the absolute design rule through story |

### Super-event 1: First League of New States

**Role:** faction formation and world-order signal.

**Trigger detail:**

- at least three living Event 006 countries
- none of the founders is a puppet below the autonomy threshold
- at least two founders are not in a major-led faction
- coalition cohesion is high
- League Charter focus, league decision, or congress resolution completed
- no previous Event 006 league super-event fired

**Title options:**

- `The League of New States`
- `Small Flags at One Table`
- `The Charter Opens`

**Description direction:**

The description should show that several fragile countries have stopped acting like isolated accidents. They have built a formal congress, recognized each other, promised aid, and forced major powers to treat them as a bloc. The language should be diplomatic and sober. Avoid comedy, apocalypse, or triumphalism.

**Button text options:**

- `A table can be a frontier.`
- `They sign because they must.`
- `Small states learn fast.`

**Quote direction:**

Use a verified real quote about sovereignty, statehood, balance of power, or small nations. Acceptable source families include Woodrow Wilson speeches, League of Nations era public texts, interwar diplomatic speeches, or older public domain political writing. Verify exact wording before implementation.

**Image direction:**

Archival diplomatic room, map table, meeting hall, or period congress image. Generated image is acceptable only if a source image cannot fit and the asset prompt marks it as symbolic.

**Audio direction:**

Low brass, quiet strings, restrained ceremony, no battle music.

### Super-event 2: The Great Partition Week

**Role:** high-chaos mass-release scale reveal.

**Trigger detail:**

- Evo IV or Evo V active
- actual release count in one wave is at least eight
- at least one historical-return, local-polity, city, railway, or strange package appears
- at least three different hosts are affected, or one major host loses several regions while surviving
- no previous mass-wave super-event fired

**Title options:**

- `The Great Partition Week`
- `A Week of New Borders`
- `The Map Room Does Not Sleep`

**Description direction:**

This should feel administrative and unsettling. Telegraphs, ministries, consulates, border posts, and newspaper offices all fail to agree which flags exist. The point is not one empire collapsing. The point is that the political language of release has become repeatable and contagious.

**Button text options:**

- `Count them again.`
- `The pins keep moving.`
- `A map is now a warning.`

**Quote direction:**

Use a real quote about nations, borders, self-determination, state power, or political order. Avoid invented quotes.

**Image direction:**

Map room, telegraph office, newspapers, clerks, pinned borders, diplomatic panic.

**Audio direction:**

Tense procedural music. Avoid heroic anthems.

### Super-event 3: The First Old Name Returns

**Role:** first historical-return state reveal.

**Trigger detail:**

- first Event 006 historical-return package becomes independent
- package is not a normal releasable under baseline logic
- origin flag is Independence Wave
- no previous old-name Event 006 super-event fired

**Candidate package examples:**

Assyria, Mesopotamia, Volga Bulgaria, Sokoto, Kanem-Bornu, Buganda, Asante, Mapuche Araucania, Palmares, Barotseland, Bukhara, Khiva, Kokand, Circassia, or Mountain Republic.

**Title options:**

- `An Old Name Returns`
- `The Archive Raises a Flag`
- `Yesterday Signs the Border`

**Description direction:**

The description should not claim the old state has literally returned unchanged. It should show modern officials using old archives, old names, treaty fragments, dynastic memory, community congresses, and chaos pressure to justify statehood.

**Button text options:**

- `The seal still opens doors.`
- `Old paper, new guards.`
- `History has filed a claim.`

**Quote direction:**

Use a verified real quote about history, nations, memory, or political legitimacy. Do not use unsourced ancient-style quotations.

**Image direction:**

Archive room, treaty desk, old map, antiquities under bureaucratic lighting, seal and passport desk. Package-specific images can be used if sourced.

**Audio direction:**

Slow, ceremonial, uncertain.

### Super-event 4: The First Impossible State

**Role:** reveal of high-chaos transformation.

**Trigger detail:**

- first Event 006 strange package becomes independent
- package type is necromantic, anti-mankind, archive-state, railway sovereignty gone impossible, or equivalent
- no previous strange Independence Wave super-event fired

**Title options:**

- `The First Impossible State`
- `A Country Without Citizens`
- `The Unmarked Congress`

**Description direction:**

Describe reports of offices, border guards, stamps, census files, and law before naming the horror. The state should feel frightening because it behaves like a government. Do not reveal every mechanic. Do not use monster language unless the route explicitly does.

**Button text options:**

- `The paperwork is alive.`
- `No one knows who signed.`
- `A border answers back.`

**Quote direction:**

Use a verified real quote about state power, death, law, or loss of human categories. If no safe quote fits, use a short public domain legal or philosophical line after verification.

**Image direction:**

Generated symbolic art is preferred. An office, border marker, sealed archive, empty parliament, or graveyard registry can work. Avoid modern horror tropes.

**Audio direction:**

Sparse, low, bureaucratic dread.

### Super-event 5: League War

**Role:** small-state bloc enters a serious war.

**Trigger detail:**

- League of New States exists
- at least four Event 006 countries are in the league or guarantee network
- league enters war against a major, a patron coalition, or a host coalition
- war goal is tied to recognition, border enforcement, anti-patron defense, or defense of a member
- no previous league-war super-event fired

**Title options:**

- `The League Goes to War`
- `Five Flags Call the Army`
- `The Charter Is Armed`

**Description direction:**

The league should not feel like a joke faction. It should be under-equipped, politically fragile, but serious enough to pull members into a regional war. Describe telegraphs, emergency rail schedules, votes, and volunteers.

**Button text options:**

- `The charter has teeth.`
- `Small states do not stay small forever.`
- `The vote passes.`

**Quote direction:**

Use verified quotation about collective defense, sovereignty, small nations, or the cost of peace.

**Image direction:**

Mobilization offices, rail station, volunteer columns, flags around a war table.

**Audio direction:**

Tense march, not triumphal.

### Super-event 6: Human Renunciation

**Role:** anti-mankind doctrine reveal.

**Trigger detail:**

- Event 006 country completes anti-mankind route lock
- country controls enough states, manpower, or strategic value to matter
- strange-state cooperation exists or a world-threat hook is active
- no previous anti-mankind Event 006 super-event fired

**Title options:**

- `The Human Name Is Struck`
- `Citizenship Ends`
- `The Directorate Against Man`

**Description direction:**

This is a rare World Collapse signal. It should read like a state ideology has crossed a line that diplomats cannot translate. Keep it legalistic, cold, and clear.

**Button text options:**

- `The forms reject us.`
- `There is no appeal.`
- `The state speaks against its makers.`

**Quote direction:**

A real quote about mankind, law, state power, death, or political violence. Verify exact wording.

**Image direction:**

Generated symbolic art. Empty ministry, shredded census, seal over erased human figure, border gate without people.

**Audio direction:**

Low, sparse, hostile, without action-movie rhythm.

### Super-event 7: The Rump That Endures

**Role:** host survival rule made visible.

**Trigger detail:**

- high-chaos wave removes many states from a host
- host survives with exactly one state or near-rump status
- protected state is capital or highest-value remaining state
- no host-destruction event fired because Event 006 never deletes hosts
- host is not already a one-state country before the wave

**Title options:**

- `The Capital Remains`
- `One State Still Answers`
- `The Rump Government Holds`

**Description direction:**

This should frame the remaining host as damaged but still legally alive. The wave has humiliated it, not deleted it. This supports user-facing clarity and prevents players from thinking the system bugged out by leaving a tiny survivor.

**Button text options:**

- `A country can fit in one room.`
- `The seal is not dead.`
- `The last ministry opens.`

**Quote direction:**

Use a real quote about state endurance, law, sovereignty, or government survival.

**Image direction:**

Guarded capital building, emergency cabinet, map with many missing regions, ministry corridor.

**Audio direction:**

Quiet, defeated, stubborn.

### Localisation package pattern

Every super-event needs:

```yaml
super_event.<slot>.t: "<title>"
super_event.<slot>.d: "<two or three paragraph description>"
super_event.<slot>.a: "<button text>"
super_event.<slot>.q: "<verified quote and attribution>"
```

Do not leave quote placeholders in final implementation. If quote verification fails, mark the super-event blocked rather than inventing a quote.

### Quote research checklist

For each quote candidate, record:

| Field | Required |
| --- | --- |
| exact wording | yes |
| speaker or source | yes |
| original work or speech | yes |
| date or approximate period | yes |
| public domain or usage note | preferred |
| source link or archive | yes |
| confidence | high, medium, low |
| reason it fits the super-event role | yes |
| rejected alternatives | useful when a famous quote is misattributed |

### Audio research checklist

For each audio candidate, record:

| Field | Required |
| --- | --- |
| track title | yes |
| composer or source | yes |
| license status | yes |
| source link | yes |
| target mood | yes |
| start and end timestamp if excerpted | yes |
| loop or one-shot behavior | yes |
| `.ogg` output path | implementation stage |
| volume note | yes |
| reason for rejection if not used | yes |

### Super-event validation

Before claiming the super-event package complete, verify:

1. trigger condition reads Event 006 origin
2. settings-aware playback is used
3. title, description, button, quote, image, audio, event log, and docs describe the same moment
4. no Event 005 localisation, art, audio, or route text is used by accident
5. no super-event fires for ordinary low-chaos waves
6. repeat prevention flags exist
7. source notes exist for quote, image, and audio
8. catalog update lists only super-events that were actually implemented or planned as candidates

## Formable and scripted-GUI super-event additions

Super-events should not fire for every formation. Use them only when the formation changes regional order, reveals a hidden identity, creates a bloc, completes a strange route, or turns a repeated wave mechanic into a campaign milestone.

Additional super-event candidate:

### The Charter Becomes a State

Role: final formable or federation reveal.

Trigger direction:

- an Event 006 country forms a major regional federation, historical-return state, local-polity confederation, or League-derived compact
- the formation uses `chaosx_formation_origin_independence_wave`
- the formed identity is independent from major-power puppet control unless the super-event is specifically about a patron-backed mandate
- no earlier formation super-event has fired for the same family

Tone:

- political proclamation
- map-room surprise
- not apocalyptic unless the route is strange
- show that independence has become statecraft

Title direction:

- direct and institutional
- examples: "The Charter Becomes a State", "The Old Name Signs Again", "A Congress With Borders"

Image direction:

- proclamation table, formation seal, map with several small flags, congress hall, or old archive opened beside a modern charter
- generated if the formation is alternate-history or symbolic
- sourced only if it must depict real historical material

Quote direction:

- sovereignty, union, federation, recognition, self-rule, or statecraft
- use a sourced quote, not invented text

Audio direction:

- restrained ceremonial music
- avoid triumphal music unless the route is deliberately triumphal

### The Window Opens

Role: first major scripted GUI milestone.

Trigger direction:

- first time the New States Congress, Patron Ledger, or Formation Ledger reaches a campaign-shaping threshold
- a GUI-driven vote or decision creates a faction, blocks puppeting, forms a state, or triggers a regional war

Tone:

- the player sees a mechanism become history
- bureaucratic, diplomatic, tense, and public

Image direction:

- voting board, congress table, switchboard, ledger, telegraph room, or formation seal
- generated unless a real archival source is appropriate

Animated support note:

The surrounding route may use animated portraits, category seals, or GUI sprites, but those do not replace the super-event package. The super-event still needs text, quote, button text, image, audio, trigger, docs, and catalog alignment.
