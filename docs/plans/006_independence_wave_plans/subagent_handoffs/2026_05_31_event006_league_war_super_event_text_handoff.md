# Event 006 League War Super-Event Text Handoff

Date: 2026-05-31
Task scope: quote/title/description/button recommendation package only
Requested slot assumption: `54` unless parent changes it
Role: the League of New States exists and enters a serious defensive or recognition war against a major, patron, or hostile coalition; at least four Event006 members are involved; tone should be tense, defensive, and focused on a small-state charter hardening into armed cooperation

## Recommendation summary

Recommended title: `The Charter Is Armed`

Recommended main quote:

> "A republic of this kind able to withstand an external force, may support itself without any internal corruption."

Recommended attribution:
- Author: Charles-Louis de Secondat, Baron de Montesquieu
- Work: *The Spirit of Laws*, Book IX, Chapter I
- Year: 1748 original work; verified in 1758 English translation
- Source URL: https://en.wikisource.org/wiki/The_Spirit_of_Laws_%281758%29/Book_IX
- Attribution confidence: High
- Copyright note: Public domain

Recommended button text: `For Peace and Common Defence.`

Recommended button source note:
- Short public-domain fragment from Thomas Hobbes, *Leviathan* (1651), Chapter XVII
- Source URL: https://en.wikisource.org/wiki/Leviathan_%281651%29/Chapter_17
- Copyright note: Public domain

## Why this package fits the role

`The Charter Is Armed` is the strongest of the candidate titles because it captures the exact super-event transition: the League stops being only a congress, pact, or recognition forum and becomes a war-making defensive bloc. It is more distinctive than `The League Goes to War`, and unlike `Five Flags Call the Army`, it does not hard-code a member count that the current role does not guarantee.

The Montesquieu line is the cleanest main quote for this role because it is directly about small republics joining together to resist external force. It sounds political rather than melodramatic, which suits a defensive recognition war. The Hobbes fragment works better as the button than as the main quote because it reinforces the title's meaning without making the quote package too heavy or too cynical.

## Title comparison

### 1. `The Charter Is Armed` — recommended
- Best fit for the role.
- Distinctive, memorable, and tied to the League's political identity.
- Communicates defensive militarisation without sounding generic.
- Still works whether four, five, or more League members are in the war.

### 2. `The League Goes to War` — backup
- Clear and immediately legible.
- Slightly plain and more generic than the recommended option.
- Good fallback if the parent wants a more direct, less literary title.

### 3. `Five Flags Call the Army` — not recommended as default
- Strong image, but brittle.
- The role says at least four Event006 members, not exactly five.
- Use only if parent later hard-locks the super-event to a five-member military call-up state.

## Quote research

### Candidate A — recommended

Quote:

> "A republic of this kind able to withstand an external force, may support itself without any internal corruption."

Attribution:
- Charles-Louis de Secondat, Baron de Montesquieu

Source:
- *The Spirit of Laws*, Book IX, Chapter I
- Verified at: https://en.wikisource.org/wiki/The_Spirit_of_Laws_%281758%29/Book_IX

Period:
- 1748 original publication
- 1758 English translation page verified

Fit:
- Directly describes a confederation of small republics surviving by armed association.
- Strong fit for a League of New States fighting for sovereignty, recognition, and survival.
- Sounds constitutional and martial at once, which matches the role better than a purely heroic war quote.

Confidence:
- High

Copyright note:
- Public domain

### Candidate B — backup quote

Quote:

> "Covenants, without the Sword, are but Words, and of no strength to secure a man at all."

Attribution:
- Thomas Hobbes

Source:
- *Leviathan* (1651), Chapter XVII
- Verified at: https://en.wikisource.org/wiki/Leviathan_%281651%29/Chapter_17

Period:
- 1651

Fit:
- Extremely strong thematic fit for a charter becoming an armed compact.
- Sharper and harsher than the Montesquieu line.
- Best used if parent wants the super-event to feel colder, more coercive, and more iron-law political.

Confidence:
- High

Copyright note:
- Public domain

### Candidate C — backup quote

Quote:

> "The principal purposes to be answered by Union are these - The common defence of the members..."

Attribution:
- Alexander Hamilton

Source:
- *The Federalist* No. 23, 18 December 1787
- Verified at: https://founders.archives.gov/documents/Hamilton/01-04-02-0180

Period:
- 1787

Fit:
- Very direct constitutional-war language.
- Good for a more formal, institutional tone.
- Less elegant as a super-event quote because it reads more like argument than pronouncement.

Confidence:
- High

Copyright note:
- Public domain

## Button text and cultural remark research

### Candidate 1 — recommended

Text:
- `For Peace and Common Defence.`

Type:
- Short public-domain fragment

Source:
- Thomas Hobbes, *Leviathan* (1651), Chapter XVII
- Verified at: https://en.wikisource.org/wiki/Leviathan_%281651%29/Chapter_17

Fit:
- Reads like a compact league motto.
- Matches the defensive tone and the political register of the event.
- Short enough to sit cleanly in the UI.

Copyright note:
- Public domain

### Candidate 2 — backup

Text:
- `For the common defence.`

Type:
- Short public-domain political fragment

Source:
- Alexander Hamilton, *The Federalist* No. 23
- Verified at: https://founders.archives.gov/documents/Hamilton/01-04-02-0180

Fit:
- Clear and serviceable.
- Slightly plainer and less distinctive than the recommended button.

Copyright note:
- Public domain

### Candidate 3 — backup

Text:
- `Then let the Charter be defended.`

Type:
- Original in-house line, not a sourced quote

Fit:
- Strongly aligned with the event role.
- Safe to use if parent wants to avoid a second literary attribution in the package.

Copyright note:
- Original line, no external copyright issue

## Draft localisation package

Draft keys in existing Chaos Redux super-event style, assuming slot `54`:

```yaml
super_event.54.t: "The Charter Is Armed"
super_event.54.d: "The League of New States has entered the war it was formed to escape. What began as a congress of fragile republics and improvised ministries is becoming a military compact, with four or more member states now bound to a common front.\n\nForeign chancelleries that dismissed the League as a paper arrangement must now reckon with mobilized borders, pooled commands, and governments resolved to survive. Recognition, sovereignty, and the right of the new states to endure will be argued under arms."
super_event.54.a: "For Peace and Common Defence."
super_event.54.q: "\"A republic of this kind able to withstand an external force, may support itself without any internal corruption.\"\n§Y-Montesquieu, The Spirit of Laws, Book IX, Chapter I§!"
```

## Backup package options

### Backup package A
- Title: `The League Goes to War`
- Button: `For the common defence.`
- Quote: Hobbes, `Covenants, without the Sword, are but Words, and of no strength to secure a man at all.`

Use this if parent wants a blunter, more openly martial version.

### Backup package B
- Title: `The Charter Is Armed`
- Button: `Then let the Charter be defended.`
- Quote: Hamilton, `The principal purposes to be answered by Union are these - The common defence of the members...`

Use this if parent wants a more institutional and less philosophical package.

## Copyright risk note

All recommended direct references in this handoff are from public-domain works. No modern copyrighted songs, films, books, or game lines were used. Risk is low.

## Implementation recommendation for the parent agent

Use `The Charter Is Armed` unless event logic later makes the member count exact and central enough to justify a number-based title.

If the parent wants the most role-accurate main quote, keep Montesquieu as the `.q` line and Hobbes only as the `.a` fragment. That pairing gives:
- a quote about small-state confederation surviving external attack
- a button that signals the League's charter has become an armed obligation

If the slot changes from `54`, only the numeric localisation key stem should change; the text package itself should still fit the role well.
