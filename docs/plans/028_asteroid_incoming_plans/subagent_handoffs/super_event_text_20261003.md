# Event 028 Super-Event Text Research Handoff

Date: 2026-10-03.

Disposition: implemented for the accepted text choice only. Acceptance basis: the parent explicitly accepted the Bacon excerpt and FitzGerald button text within the user's source-verified text contract. The [research note](../../../super_events/028_asteroid_incoming_text_research.md) contains eight main-quote candidates and six cultural-remark candidates with verified wording and direct source links.

Implementation evidence: the parent reports that English slot 116 now stores the exact quote fragment, a newline, `Francis Bacon`, and button text `The Moving Finger writes`. This is parent-provided evidence and was not independently checked against localisation source in this documentation-only update.

## Recommendations

- Keep title `The Stone's Verdict`.
- Main quote: `Nature to be commanded must be obeyed`.
- Main quote attribution: Francis Bacon, *Novum Organum*, Book I, Aphorism III, English wording checked against the 1858 edition in *The Works of Francis Bacon*, volume IV.
- Button text: `The Moving Finger writes`.
- Button source: Edward FitzGerald, *Rubáiyát of Omar Khayyám*, first edition, 1859, quatrain LI. The exact English words belong to FitzGerald's rendering; do not credit the phrase directly to historical Omar Khayyám.
- Backup quote: Ovid's Phaethon passage in Arthur Golding's 1567 *Metamorphoses*, `Like to a starre in Winter nights`.
- Backup remark: Shakespeare's `the rest is silence` from *Hamlet*, or Shelley's `Nothing beside remains` from “Ozymandias.” Both are public-domain source texts, with role-fit caveats documented in the research note.

## Evidence and implementation boundary

The Bacon wording is present on page 47 of the scanned 1858 source edition. The parent reports that opening the Berkeley PDF returned HTTP 403, then reverified the English wording against the Wikisource Spedding Book I transcription at Aphorism III and checked the FitzGerald first-edition transcription at quatrain LI, lines 512–516. The direct scan URL remains in the research note as the primary-scan handoff. The accepted quote string is the exact excerpt with no ending punctuation, followed by a newline and `Francis Bacon`.

The super-event button text is now reported as `The Moving Finger writes`. The separate news acknowledgement `The Earth remembers the blow.` remains in `chaosx.news.32.a` as authored news text, not as a cultural quotation. The parent will review later whether to replace it or leave it as plain authored text; this handoff makes no change to it.

The supplied period-impact image direction is compatible with both selected texts. Biblical end-times candidates and whole-world-collapse poetry were considered and rejected where they overstate the event's confirmed consequences. The text source search found no duplicate of the selected button phrase in the scoped super-event text files.

The parent-provided Event 028 audio research note and its selected Brahms track remain unchanged. A narrow catalogue lookup confirmed the Event 028 music row. This handoff makes no audio recommendation or rights change.

## Files and remaining ownership

Updated only:

- `docs/super_events/028_asteroid_incoming_text_research.md`
- `docs/plans/028_asteroid_incoming_plans/subagent_handoffs/super_event_text_20261003.md`

This agent changed only the two listed documentation files. The parent reports that English slot 116 has been implemented, but this agent did not modify or inspect localisation source. No event, image, GUI, audio, sound-definition, spreadsheet, or shared-selector files were changed in this update. The parent owns the commit and native visual or GUI evidence, which remain unresolved. No in-game testing is claimed.

No requested research-count simplification was made.
