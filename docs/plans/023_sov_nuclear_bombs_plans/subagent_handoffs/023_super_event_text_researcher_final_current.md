# Event 23 super-event text research handoff

## Scope and result

This handoff covers only the text research for Event 23 `sov_nuclear_bombs`, nonterminal super-event slot/audio ID 108, whose role is the first confirmed multi-major nuclear exchange.

The strongest main quote is already present in the current localisation and is a verified public-domain archival quotation, so no replacement wording is required.

The current button text is acceptable original writing and is safe to retain, although it repeats the title; a sourced historical alternative is documented below if the parent wants a distinct button reaction.

The event script, `AGENTS.md`, and the `chaos-redux-events` skill were not opened in this bounded text-research pass because this worker is restricted from reading gameplay implementation and repo-wide implementation guidance. Role and threshold conclusions below come from the named super-event skill, the Event 23 super-event prompt, and Parts 5, 7, and 8 of the Event 23 specification.

## Selected main quote

**Exact wording:** “The first blow or series of first blows may be the last.”

**Recommended localisation value for `chaosx_super_event.108.q`:** `The first blow or series of first blows may be the last.`

**Author and speaker:** Major General Leslie R. Groves, in a written memorandum; this is not a speech quotation.

**Source work:** “Our Army of the Future—As Influenced by Atomic Weapons,” the “Memorandum by the Commanding General, Manhattan Engineer District (Groves)” in *Foreign Relations of the United States, 1946, General; The United Nations, Volume I*, item 10.

**Date:** Washington, 2 January 1946; the source footnote records that Groves transmitted the memorandum to John M. Hancock on 10 June 1946.

**Primary source:** [U.S. Department of State, FRUS 1946, Document 600](https://history.state.gov/historicaldocuments/frus1946v01/d600).

**Attribution confidence:** High for wording, document, date, and Groves attribution: the official page supplies the document heading, date, and exact sentence under item 10. The page labels the memorandum “(Groves)” rather than displaying a separate signature, so the safest documentation label is “Major General Leslie R. Groves, memorandum.”

**Rights and copyright note:** The underlying memorandum is a United States Government work. U.S. Copyright Office guidance states that copyright protection is not available under 17 U.S.C. §105 for a work of the United States Government; see [17 U.S.C. §105](https://www.copyright.gov/title17/92chap1.html#105). This is therefore a low-risk public-domain source in the United States, with the normal caveat that the State Department’s edited web presentation and local law outside the United States may have separate considerations. The proposed excerpt is only twelve words.

**Fit for slot 108:** This is unusually well matched to the exact Event 23 threshold. “First blow or series of first blows” describes the first confirmed major-to-major detonation and the immediate possibility of retaliation, while “may be the last” conveys the shortened decision window and irreversible danger without declaring Fallout, world termination, or Final Silence. The sentence reads as an archival warning about failed control rather than as a claim that the nonterminal super-event has already ended the world.

**Implementation recommendation:** Retain the existing quote text exactly and document the attribution in the research/spec handoff. Do not silently replace it with a paraphrase or attach a different speaker. If the parent adds an attribution outside the player-facing quote key, use “—Leslie R. Groves, memorandum, 1946” rather than calling it a speech.

## Considered main-quote candidates

| Candidate | Source, period, and exact wording | Attribution confidence and rights | Fit and disposition |
|---|---|---|---|
| **Leslie R. Groves — selected** | “The first blow or series of first blows may be the last.” *Our Army of the Future—As Influenced by Atomic Weapons*, 1946. [Official FRUS source](https://history.state.gov/historicaldocuments/frus1946v01/d600) | High attribution and wording confidence. Underlying U.S. Government memorandum is public domain in the United States under 17 U.S.C. §105. | Directly atomic, directly about first strikes and exchange timing, and severe without making the route terminal. **Selected.** |
| W. B. Yeats | “Things fall apart; the centre cannot hold;” from “The Second Coming,” written 1919 and published in *Michael Robartes and the Dancer* in 1920. [Project Gutenberg text](https://www.gutenberg.org/cache/epub/72987/pg72987-images.html) | High wording and attribution confidence. The 1920 poem is public domain in the United States. | Strong image for failing command, communications, and political order, but the surrounding poem’s apocalyptic register risks making this nonterminal exchange event sound like Fallout. **Backup only; better as a short allusion if used at all.** |
| William Shakespeare, spoken by Cassius | “The fault, dear Brutus, is not in our stars, / But in ourselves, that we are underlings.” *Julius Caesar*, Act 1, Scene 2, written/performed around 1599. [Folger text](https://www.folger.edu/explore/shakespeares-works/julius-caesar/read/1/2/) and [Folger dating note](https://www.folger.edu/explore/shakespeares-works/julius-caesar/about-shakespeares-julius-caesar/) | High wording and attribution confidence. Shakespeare’s text is public domain. | Useful for responsibility rather than fate, but “underlings” and the Roman political context are less precise for the atomic-exchange threshold than Groves. **Backup if the intended emphasis shifts to human responsibility.** |
| Hosea, KJV translation | “For they have sown the wind, and they shall reap the whirlwind.” Hosea 8:7; the King James Version dates to 1611, with the familiar 1769 revision. [Bible Gateway KJV text](https://www.biblegateway.com/passage/?search=Hosea+8%3A7&version=KJV) | High confidence for the verse and KJV wording. The KJV is marked public domain by the cited source; use the KJV wording, not a modern copyrighted translation. Traditional biblical-period authorship is less specific than the translation attribution. | Clear consequence and judgment imagery, but “they” assigns moral culpability and “whirlwind” is less specifically an exchange than Groves’s wording. **Backup for an explicitly prophetic or judgmental tone.** |
| Carl von Clausewitz | “War is a mere continuation of policy by other means.” Section heading in J. J. Graham’s English translation of *On War*, Book I, Chapter 1, §24; original work 1832, translation first published 1874. [Project Gutenberg translation](https://dev.gutenberg.org/cache/epub/1946/pg1946-images.html) | High confidence for the Graham translation and source location. The original work and 1874 translation are public domain. It is important to identify this as the translation’s section heading rather than imply this exact English sentence is Clausewitz’s original wording. | Makes the exchange a consequence of state policy and responsibility, but is analytical and not specifically nuclear. **Backup only.** |
| Publius Cornelius Tacitus, speech attributed to Calgacus | “Where they make a desert, they call it peace.” *Agricola* 30.4, written approximately 98 CE. [Project Gutenberg translation](https://www.gutenberg.org/cache/epub/7524/pg7524-images.html) and [Library of Congress scan with citation](https://tile.loc.gov/storage-services/master/gdc/gdcebookspublic/20/20/71/64/65/2020716465/2020716465.pdf) | High confidence that the wording occurs in an old translation; medium confidence for Calgacus as the historical speaker because Tacitus is constructing a reported speech rather than preserving a recording. Ancient source and old translation are public domain. | Excellent devastation-and-euphemism imagery, but it points toward aftermath and “peace,” and the speaker attribution is less secure. **Prefer as a button/allusion backup, not the main quote.** |

## Button assessment and recommendation

### Current button

**Current text:** “The exchange has begun.”

This is acceptable original writing under the Event 23 brief. It is short, severe, directly describes the confirmed threshold, carries no copyright or attribution risk, and does not introduce a modern cultural reference that needs clearance.

The only weakness is repetition: it closely restates the current title “The Exchange Has Begun,” so it reads more like a state label than a distinct player reaction.

**Selected low-risk recommendation:** Retain “The exchange has begun.” if the parent values directness and minimal attribution overhead. A sourced cultural remark is not required for correctness or fit.

### Optional sourced replacement

**Recommended distinct button alternative:** “The die is cast.”

**Source and wording:** Suetonius reports Caesar’s remark at the Rubicon as “The die is cast” in *The Life of Julius Caesar* 32.1/XXXII. [Fordham Ancient History Sourcebook text](https://sourcebooks.web.fordham.edu/ancient/suetonius-julius.asp).

**Attribution confidence:** High that the phrase is present in the cited Suetonius account; medium that these are the exact historical words spoken, because Suetonius reports the episode and other ancient accounts use a differing formulation. Attribute it as “reported by Suetonius” if attribution is shown anywhere outside the button.

**Period and rights:** The event narrated is approximately 49 BCE; Suetonius wrote approximately 121 CE. The ancient source and the cited old translation are public-domain material, although the electronic edition can have separate site terms. The proposed fragment is four words and has low copyright risk.

**Fit:** It marks the first confirmed exchange as a point of no return without claiming that Fallout or Final Silence has occurred. It is more reaction-like and less repetitive than the current button, but it is also a familiar cliché and carries a stronger implication of irreversible commitment.

**Replacement recommendation:** Use “The die is cast.” only if the parent accepts the historical-report attribution caveat and wants a distinct cultural button. Otherwise keep the current original button.

## Considered button and cultural-remark backups

| Candidate | Source and rights | Fit and disposition |
|---|---|---|
| “The die is cast.” | Suetonius, *Life of Julius Caesar* 32.1/XXXII, ancient source and old translation; [Fordham source](https://sourcebooks.web.fordham.edu/ancient/suetonius-julius.asp). Low rights risk; medium confidence for exact historical utterance, high confidence for the reported wording. | Best sourced alternative for an irreversible threshold. **Primary cultural replacement option.** |
| “The centre cannot hold.” | W. B. Yeats, “The Second Coming,” 1919/1920; [Project Gutenberg text](https://www.gutenberg.org/cache/epub/72987/pg72987-images.html). Public-domain poem. | Concise image of failed command and communications, but its apocalyptic associations can overstate a nonterminal event. **Backup only.** |
| “Where they make a desert, they call it peace.” | Tacitus, *Agricola* 30.4, approximately 98 CE; [Project Gutenberg translation](https://www.gutenberg.org/cache/epub/7524/pg7524-images.html). Ancient source and old translation are public domain. | Strong devastation allusion, but it implies an aftermath/peace framing and has the Calgacus attribution caveat. **Backup only.** |
| “Their's not to reason why.” | Alfred, Lord Tennyson, “The Charge of the Light Brigade,” 1854/1855; [Project Gutenberg edition of *Maud, and Other Poems*](https://www.gutenberg.org/files/56913/old/56913-h/56913-h.htm). Public-domain poem. | The source edition uses the archaic spelling “Their's”; the familiar “Theirs” should not be silently presented as the exact cited text. The line can suggest failed command, but its blind-obedience and Crimean-war associations make it weaker for this event. **Backup only.** |

## Final package recommendation

1. Keep `chaosx_super_event.108.q` as `The first blow or series of first blows may be the last.` and document it as a quotation from Major General Leslie R. Groves’s 1946 Manhattan Engineer District memorandum.
2. Keep `chaosx_super_event.108.a` as `The exchange has begun.` if direct, attribution-free reaction text is preferred; it is acceptable original writing and needs no sourced cultural remark.
3. If the parent wants to remove the title/button repetition, replace only the button with `The die is cast.` and preserve the Suetonius “reported wording” caveat in the handoff or documentation.
4. Do not use Yeats’s apocalyptic line, the Hosea verse, or the Tacitus line as the main quote for this slot because each risks shifting the nonterminal first-exchange event toward terminal apocalypse or aftermath.
5. No modern copyrighted song, film, book, game, or television quotation is needed.

## Files and change boundary

Only this handoff is intended to be written by the text-research worker: `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_super_event_text_researcher_final_current.md`.

No gameplay, localisation, GFX, sound, workbook, or specification file was edited.
