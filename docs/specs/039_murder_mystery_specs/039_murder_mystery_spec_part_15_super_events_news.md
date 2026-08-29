# Murder Mystery Specification Part 15: Super-Events, News, Reports, and Localisation Direction

## Presentation hierarchy

Event 39 contains many serious incidents. Only campaign thresholds receive super-event treatment. The opening murder, national cult, foreign cells, major assassinations, capture, and ordinary derivative creation use normal event, news, or report presentation.

The accepted super-event set contains three roles:

1. Assassin State public reveal
2. World of Anarchy activation
3. Brotherhood defeat aftermath when the movement reached a qualifying global scale

A separate final-victory super-event is optional only if the shared world-end framework has a distinct terminal resolution slot and the implementation can provide a complete unique package. It is not required by this source spec.

## Super-event A: Assassin State public reveal

### Trigger

Fire after the Evolution III split transaction succeeds, both countries have valid capitals and forces, war is active, and the Assassin State is visible on the map.

### Role

First public reveal and irreversible political shift.

### Title direction

Short and specific. It should identify the movement becoming territorial or public without using a generic end-of-order title. Working direction can refer to the hidden hand becoming a state, the empty chair gaining territory, or the murderer declaring a government.

### Description direction

Explain that the suspected murderer has appeared as the leader of an organized territorial movement inside the original country. Mention the open war, disciplined cadres, and international cells. Preserve uncertainty about earlier crimes and personal origin.

### Button direction

A restrained reaction to the contradiction of an anti-leadership movement creating a state. Research a brief cultural reference or write an original reaction after the reference gate. Do not use a long modern quote.

### Quote research

Primary researched candidate:

- William Shakespeare, *Henry IV, Part 2*, Act 3, Scene 1
- candidate excerpt: `Uneasy lies the head that wears a crown.`
- fit: links the opening assassination and the movement's attack on state leadership to the revealed leader's own new vulnerability
- attribution confidence: high through the Folger Shakespeare Library
- rights direction: public-domain work, verify the chosen edition and punctuation in final notes

The final researcher should compare this candidate with at least two other verified public-domain or historical candidates before selection.

### Image direction

A full generated scene showing a transferred administrative or urban district under organized Assassin control, the new flag, disciplined cadres, and the original government's front beyond it. The leader can be present as a distant or obscured figure. Avoid generic ninja imagery, religious symbols, and identifiable real politicians.

### Audio direction

Research a unique licensed musical track that supports a political reveal and organized revolt. The track should have structure, not a drone or sound effect. Final runtime format follows the current super-event skill, which requires WAV. Use the settings-aware sound helper and a unique audio ID.

## Super-event B: World of Anarchy

### Trigger

Fire only after the terminal activation transaction sets shared world-end state, initializes the target registry and first campaign sector, reveals the category, and confirms the movement can continue.

### Role

World-end activation.

### Title direction

Use the accepted public terminal name or a specific route-aware variant. Avoid generic phrases about darkness, final crisis, or humanity falling.

### Description direction

Explain that the Assassin movement has declared organized leadership itself to be the target and has begun a coordinated global campaign. Mention ordinary governments, cells, subjects, and the movement's hidden command contradiction. Do not claim every government has already fallen.

### Button direction

The reaction should be cold, skeptical, or resigned. It can point to the fact that someone still had to give the order. Research a short cultural reference only if it fits and remains within copyright limits.

### Quote research

Primary researched candidate:

- Joseph Conrad, *The Secret Agent*
- candidate excerpt: `The terrorist and the policeman both come from the same basket.`
- fit: captures the movement's claim to abolish authority while building its own coercive state and intelligence system
- attribution confidence: high through Project Gutenberg text
- rights direction: public-domain novel in the United States, verify regional use and final edition wording

The final researcher should compare this candidate with other public-domain sources about power, law, command, and revolution. Do not select it merely because it mentions terrorism.

### Image direction

A full generated documentary-style scene showing several government centers losing command, broken communications, empty official spaces, active cells, and one concealed coordinating network. The scene should communicate worldwide scale without a flat world map, title card, or graphic bodies.

### Audio direction

Research a unique licensed musical recording with finality and structured momentum. Prefer public domain composition and a clearly usable recording, Creative Commons, or institutional archive material. Final WAV should normally be one to two minutes after editing unless a documented exception is better.

## Super-event C: Brotherhood defeat aftermath

### Trigger gate

Fire only when the movement:

- reached Evolution IV or V
- existed for a meaningful duration
- created multiple derivatives or held a substantial territory network
- caused a broad war or terminal activation
- was defeated with no valid movement heir
- left a postwar settlement that changes several countries

A small local Assassin State defeated soon after formation receives a news event and aftermath report, not this super-event.

### Role

Defeat aftermath and costly restoration.

### Title direction

Focus on the movement's network breaking, the return of government under suspicion, or the surviving records. Avoid a simple victorious slogan.

### Description direction

Explain what was defeated, what institutions and people were lost, what cells or documents remain, and why ordinary politics does not return immediately. Tone should be reflective and guarded.

### Button direction

Use a restrained reaction about law, memory, or unfinished investigation. Research any cultural reference before use.

### Quote research

Primary researched candidate:

- Francis Bacon, `Of Revenge`
- candidate excerpt: `Revenge is a kind of wild justice.`
- fit: frames the movement's violence and the danger that victors repeat it during suppression
- attribution confidence: high through Project Gutenberg editions of Bacon's essays
- rights direction: public-domain text, verify final punctuation and source edition

The final researcher should compare at least two alternatives about law, revenge, memory, or rebuilding.

### Image direction

A full generated scene of captured archives, dismantled symbols, returning civil institutions, guarded survivors, and uncertain reconstruction. Avoid a triumphant parade or clean return to normal.

### Audio direction

Research a unique reflective musical track. It should convey cost and unstable recovery. It must not reuse either earlier Event 39 track.

## Audio implementation contract

For every accepted super-event:

- select and verify a unique musical track
- document title, composer or creator, performer or recording source, source URL, license, usage terms, duration, and attribution
- check composition and recording rights separately
- preserve the legitimate downloaded source while work is active
- convert the final cue to game-ready WAV
- place it in the event-scoped sound folder
- register the base sound and settings-volume wrappers
- set the unique current audio ID
- call the settings-aware playback helper
- add the track and super-event ID to the canonical HTML music catalogue
- promote durable provenance before deleting the temporary workspace

The supplied audio-researcher TOML still says OGG. The current super-event skill requires WAV and is authoritative for this package. The stale subagent definition should be corrected through the skill-maintenance workflow before or during implementation.

Generated tones, oscillators, beeps, noise beds, generic ambience, unclear-license tracks, modern commercial recordings without permission, and placeholder audio are forbidden.

## News event set

### Opening leader murder

Global news after the safe succession transaction. Show the host flag and leader office. Communicate uncertainty and national crisis. Do not reveal the cult or future state.

### Mysterious killer captured

Global news only after full capture before a surviving international movement remains. Confirm the operation and public relief. Preserve unresolved motive and origin.

### Major foreign assassination

Global news when a safe named national leader or internationally significant commander is murdered abroad. Minor office casualties use reports.

### Foreign Assassin revolt

Global news for the first successful foreign derivative and later derivatives only when country importance or strategic effect justifies it. Avoid one global popup for every small revolt.

### Assassin State defeated

Global news when the original state is defeated before the super-event aftermath gate. Mention surviving cells when they remain.

## Report event set

Report events should cover:

- evidence secured or destroyed
- witness protected, missing, or killed
- attempted attack stopped
- generic office casualty
- named military or advisor death that lacks global significance
- cell route discovered
- local cell dismantled
- operative compromised
- revolt preparation detected
- foreign support intercepted
- subject disobedience
- movement inheritance
- remnant cleanup
- postwar institutional recovery

Reports should use the project report picture and localisation pattern. They should not use generic newspaper prose for every update.

## Localisation direction

The planning package defines direction, not final pasteable prose.

### Tone by actor

- original host: procedural, uncertain, increasingly strained
- strong intelligence government: precise and evidence-centered
- repressive government: public-order language and institutional defensiveness
- foreign affected government: informed but locally uncertain
- central Assassin State: disciplined, doctrinal, internally contradictory
- decentralized route: plural voices and local mandates
- pragmatic route: temporary-state language and instrumental policy
- terminal movement: public abolition of authority with concealed command language
- postwar victors: cautious restoration and continuing suspicion

### Dynamic placeholders

Use dynamic country, original host, current movement, leader office, selected role, selected state or route, case stage, network stage, Cohesion stage, selected foreign country, subject, and campaign sector where the live event needs them.

Do not print raw variable values when a stage, threshold, or concise number with context is clearer.

### Hidden information

Player-facing text must not reveal:

- protected character registry
- exact named target weights
- future evolution roll
- unselected Assassin State territory
- hidden movement heir
- secret false-lead result
- exact revolt score components
- terminal administration callback details

### Cultural references

Every quote, slogan, film line, book line, lyric fragment, historical remark, scripture, proverb, or cultural allusion requires web verification and documentation. Modern copyrighted references should remain very short or use paraphrased allusion.

## Completion standard

Presentation is complete only when every event role uses the correct level, all three accepted super-event packages have aligned text, image, quote, audio, slot, and wiring, normal news and reports avoid spam, localisation preserves ambiguity and dynamic context, and no final quote, cultural remark, image, or audio remains unresearched or placeholder.
