# Super-event specification

## Super-event policy

Event 38 is Minor Fire-Once and does not need a super-event merely for its opening. The opening should use a strong report or news event.

Super-events are reserved for campaign thresholds that change regional or global order.

## Required super-events

### SE-038-A: Operation The Final Crusade

**Visibility:** hidden until the Teutonic Order faction forms.

**Role:** major faction formation and proclamation of a multinational global campaign.

**Trigger meaning:** Malta or Holy See, Nazi Germany, and the Holy Realm have formed the Teutonic Order and formally begun Operation The Final Crusade.

**Title direction:** concise and specific to the operation or three-state faction. Avoid generic “final war” language.

**Description direction:** describe the alliance, its military roles, religious mythology, and first regional campaigns. Make the ideological contradiction and coercive danger visible without an explanatory essay.

**Button direction:** short researched cultural or military remark with irony or fatalism. It must fit the alliance and stay within copyright limits.

**Quote direction:** verified historical, religious, political, or literary source about crusade, fanaticism, alliance, power, or false certainty. Do not invent a quote.

**Image direction:** generated fictional period-authentic scene showing Malta crusaders, German industry or armour, and Holy Realm symbolism in one coherent alliance presentation. Avoid a map-table composition, celebratory Nazi spectacle, readable generated text, and modern cinematic UI.

**Audio direction:** unique licensed or public-domain structured musical cue, likely martial, religious, or processional, between about one and two minutes after editing.

**Slot:** assign after auditing current slots. No accidental reuse.

### SE-038-B: Atlantis

**Visibility:** hidden until Germany accepts the betrayal.

**Role:** hidden route reveal and alliance rupture.

**Trigger meaning:** Germany adopts Atlantis identity, leaves the Teutonic Order, attacks Malta or Holy See and Holy Realm, and deploys the initial Supreme formations.

**Title direction:** short, strange, and tied to the Atlantean proclamation or Atlantus. Avoid a generic empire title.

**Description direction:** describe the regime's ancestry claim as propaganda, the return of Hitler to German command where applicable, Berlin's renaming, the betrayal, and the first attacks.

**Button direction:** bitter or incredulous researched cultural remark. Avoid admiration.

**Quote direction:** verified source about mythic ancestry, hubris, race ideology, betrayal, or imperial delusion. Primary or scholarly historical context is preferred.

**Image direction:** generated fictional scene of a transformed German regime, elite tanks, monumental Atlantus imagery, and broken alliance symbols. The image should communicate menace and ideological delusion.

**Audio direction:** unique licensed structured musical cue, severe and militarized, with no reused Teutonic track.

### SE-038-C: The Holy World

**Visibility:** public terminal route.

**Role:** world-end proclamation.

**Trigger meaning:** the Papal actor has proven full control of one continent, Chaos has reached at least 1000, the branch is enabled, and final activation has set the shared world-end state.

**Title direction:** use the accepted public route name or a concise Papal proclamation title.

**Description direction:** explain that the Pope has called the final world crusade, believer governments submit to Papal war leadership, and nonbelievers organize resistance. State the terminal order clearly without listing bonuses.

**Button direction:** short sourced religious, literary, or cultural reaction with finality.

**Quote direction:** verified scripture, public-domain religious text, historical Papal document, or public-domain literature about judgment, universal authority, war, or the limits of earthly rule. Context and attribution must be correct.

**Image direction:** generated fictional global Papal war scene centered on Rome, Jerusalem, believer armies, and a world divided by submission and resistance. Avoid a plain map or title card.

**Audio direction:** unique licensed or public-domain religious or orchestral musical recording with finality. Composition and recording rights need separate verification.

## Conditional super-events

### Holy See formation

A Holy See formation super-event is justified only if the route changes regional order, installs the Pope as political ruler, and moves the capital to Rome. If implementation treats it as a smaller internal transformation, use a news event instead.

### Kingdom of God formation

A formation super-event is justified when the actor controls a major territorial network and the proclamation changes international politics. A small Malta-only cosmetic change does not qualify.

### Eleventh Crusade victory

Use a normal news event unless the comeback restores a major regional order after a long, costly campaign.

### Atlantis defeat

A defeat aftermath super-event is justified only when Atlantis fought a global or near-global war long enough to reshape the campaign.

### Holy World defeat

A terminal defeat super-event is appropriate when the final world war ends and a new postwar settlement begins.

## Research workflow

For each approved super-event:

1. define exact role and trigger
2. use the super-event text researcher for quote and button candidates
3. verify wording, attribution, work, date, source, confidence, and copyright status
4. use the audio researcher for repository and web candidates
5. verify composition and recording rights separately
6. download from a legitimate source
7. preserve original source
8. edit and convert to final WAV
9. use generated-event-art or source researcher for the image according to source mode
10. process to final DDS
11. assign unique slot, sprite, audio ID, base sound, and volume wrappers
12. call `play_current_super_event_sound = yes`
13. update permanent research note and `music/chaosx_music_track_list.html`

## Audio file plan

Recommended runtime paths:

```text
sound/038_malta_crusaders/super_event_<slot>_operation_final_crusade.wav
sound/038_malta_crusaders/super_event_<slot>_atlantis.wav
sound/038_malta_crusaders/super_event_<slot>_holy_world.wav
```

The final filenames use actual assigned slot or stable super-event ID according to current project convention.

## Localisation keys

Use the current super-event key pattern:

```text
chaosx_super_event.<slot>.t
chaosx_super_event.<slot>.d
chaosx_super_event.<slot>.a
chaosx_super_event.<slot>.q
```

The implementation must update the scripted localisation image selector, title, description, quote, remark, and audio selection for each slot.

## World-end alignment

The Holy World super-event fires only after:

- branch toggle checked
- 1000 or more Chaos
- exact terminal readiness
- shared world-end state set
- scenario-specific flag set
- Papal actor frozen and valid

The manual scenario uses the same Holy World super-event after it raises Chaos and activates the shared terminal runtime.

## Asset and text restrictions

- no invented quotes
- no misattributed quotes
- no long copyrighted lyrics or dialogue
- no default audio
- no generated test tones, drones, or primitive waveforms
- no reused track without explicit approval
- no unrelated image slot
- no map-only final art unless explicitly approved
- no hidden-route spoilers before reveal
- no developer-facing implementation history in player text

## Completion evidence

For each final super-event, the completion report lists:

- role and trigger
- slot
- localisation keys
- selected quote and source
- button reference and source where applicable
- image path, sprite, source mode, and manifest
- audio title, creator, performer, source, license, duration, and final path
- base sound and volume wrappers
- audio ID and helper call
- permanent research note
- audio catalog row
- settings-aware playback proof
- screenshot and live user validation status
