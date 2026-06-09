# Event 006 Super-Event Text Handoff

## Status

Ready for implementation. No quote-source blocker found.

## Target

- Event: `006 Independence Wave`
- Super-event slot: `58`
- Working title: `The Rump That Endures`
- Role: host survival rule made visible after a high-chaos wave reduces a host to a one-state or near-rump government without deleting it

## Recommended Text Package

### Title

`The Rump That Endures`

Reason:
This is the strongest title among the current options and the user-provided working title. It makes the legal-political point immediately: the state has been reduced, but it has not ceased to exist.

### Main Quote

`"At both those periods the nation had lost the bond of union in their ancient edifice; they did not, however, dissolve the whole fabric."`

- Speaker/author: Edmund Burke
- Source work: *Reflections on the Revolution in France*
- Year: 1790
- Source URL: https://www.gutenberg.org/files/3286/3286-h/3286-h.htm
- Verification note: the wording appears in the Project Gutenberg text of Burke's work and is also visible in the searched excerpt for the same passage
- Attribution confidence: High
- Copyright/public-domain note: Public domain

Why this fits:
This quote says exactly what the super-event needs to say. A political order can lose major parts, even its old bond of union, without dissolving altogether. That matches the Event 006 host-survival rule: humiliation and reduction, not extinction.

### Recommended Button Text

`The seal is not dead.`

Reason:
This is the strongest of the current spec options. It is short, dignified, institutional, and legible at a glance. It frames the survivor as a state that still has legal personality, archives, signatures, and ministries rather than as a joke or a map oddity.

Source note:
Original line from the spec set, not an external quotation or cultural reference.

### Recommended Description

The wave has stripped the host of provinces, revenues, roads, and proud distances, but it has not stripped it of statehood. Somewhere behind guarded doors, in a capital quarter or the last defensible seat of power, the seal still descends onto paper, decrees still leave the ministry, and the government continues to speak in its own name.

What survives is no longer a realm in the old sense. It is a remnant administration, a shrunken court, a cabinet with too few rooms and too many maps of loss. Foreign offices may mock it, rebels may crowd its borders, and its own citizens may measure its fall in stations, depots, and vanished districts, yet the law has not pronounced it dead.

So long as one protected seat still answers, the host endures. Reduced, humiliated, and forced inward, it remains a claimant, a signature, and a government. The state has been cornered into its last chamber, but that chamber is still a state.

## Considered Main Quote Candidates

### 1. Selected

`"At both those periods the nation had lost the bond of union in their ancient edifice; they did not, however, dissolve the whole fabric."`

- Author: Edmund Burke
- Work: *Reflections on the Revolution in France*
- Year: 1790
- URL: https://www.gutenberg.org/files/3286/3286-h/3286-h.htm
- Confidence: High
- Public domain: Yes
- Fit note: Best direct expression of partial constitutional survival after catastrophic loss

### 2. Strong backup

`"The king never dies. Henry, Edward, or George may die; but the king survives them all."`

- Author: William Blackstone
- Work: *Commentaries on the Laws of England*, Book 1, Chapter 7
- Year: 1765-1769 period; wording verified in Book 1 online edition
- URL: https://www.gutenberg.org/cache/epub/30802/pg30802-images.html
- Verification note: the relevant passage is visible in the opened Project Gutenberg text
- Confidence: High
- Public domain: Yes
- Fit note: Very strong legal-continuity language. Best if the main agent wants the event to feel more jurisprudential and explicitly about the immortality of state office.
- Caution: Monarchical wording may feel slightly narrower than Event 006's general host-survival rule.

### 3. Backup

`"A Multitude of men, are made One Person, when they are by one man, or one Person, Represented..."`

- Author: Thomas Hobbes
- Work: *Leviathan*, Chapter XVI
- Year: 1651
- URL: https://englishphilosophy.org/hobbes/l/1/16
- Secondary corroboration URL: https://www.gutenberg.org/files/3207/3207-h/3207-h
- Confidence: Medium-High
- Public domain: Yes
- Fit note: Strong philosophical framing for why a state can persist in representation even when materially reduced.
- Caution: Slightly more abstract than Burke or Blackstone, and less immediately legible in the super-event UI.

## Considered Button / Remark Candidates

### 1. Selected

`The seal is not dead.`

- Type: original button line
- Source: spec option
- Fit note: best match for legal continuity, documentation, and institutional survival

### 2. Backup

`The last ministry opens.`

- Type: original button line
- Source: spec option
- Fit note: strong for the cabinet/ministry corridor presentation, especially if the art emphasizes emergency offices
- Caution: slightly more scene-specific and less universal than the selected line

### 3. Backup

`A country can fit in one room.`

- Type: original button line
- Source: spec option
- Fit note: vivid and memorable
- Caution: edges toward irony and can undercut the legal seriousness of the moment if the rest of the package stays solemn

## Backup Title Options

- `One State Still Answers`
- `The Capital Remains`

Recommendation:
Keep `The Rump That Endures`. It is clearer and more distinctive than the alternates. `The Capital Remains` is weaker because the event is not only about geography. `One State Still Answers` is good, but less evocative.

## Source and Verification Notes

### Burke

- Search result excerpt showed the exact sentence: "they did not, however, dissolve the whole fabric"
- Opened Project Gutenberg selection confirms the passage in a public-domain Burke text
- Work attribution is stable and well-known

### Blackstone

- Opened Project Gutenberg text confirms the line:
  `The king never dies. Henry, Edward, or George may die; but the king survives them all.`
- This is a direct legal doctrine of continuity and a reliable backup

### Hobbes

- Exact wording verified via English Philosophical Texts Online for *Leviathan* chapter XVI
- Project Gutenberg text of *Leviathan* used as corroborating public-domain edition

## Copyright Risk Note

Low.

All recommended direct-quote candidates are from public-domain works:

- Edmund Burke, 1790
- William Blackstone, eighteenth century
- Thomas Hobbes, 1651

No modern copyrighted lyrics, film dialogue, game dialogue, or prose are used.

## Fit Summary

This package keeps the event distinct from total collapse, extinction, or an Event 005-style terminal disintegration. The tone is damaged legality: the host has lost land and stature, but still possesses office, seal, claim, and name. Burke is the best anchor because he describes a political order losing core structural unity without ceasing to exist.

The selected button text supports the same reading in miniature. It tells the player that the surviving host is not a leftover bug-shaped fragment on the map; it is a diminished but still recognized state form.

## Implementation Recommendation

Use this package unless the main agent specifically wants a more legalistic line:

- `super_event.58.t`: `The Rump That Endures`
- `super_event.58.a`: `The seal is not dead.`
- `super_event.58.q`: Burke quote above with attribution to Edmund Burke, *Reflections on the Revolution in France* (1790)
- `super_event.58.d`: use the three-paragraph description above, or trim lightly while preserving the legal-survival emphasis

If the presentation art ends up strongly monarchical or court-centered, Blackstone becomes the best backup quote. If the presentation is more abstract and constitutional, Burke remains the best choice.
