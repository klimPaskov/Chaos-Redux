# Event 20 super-event 087 text research handoff

Date: 2026-08-01.

Scope: text research only for the optional Rat King global-defeat aftermath super-event, slot 87 (`global_defeat_super_event_id = 87`). No gameplay, event, localisation, GFX, audio, or registry files were edited.

## Role and integration boundary

Slot 87 should be rare aftermath coverage for a qualifying, continent-spanning Rat King catastrophe. It should fire after news event `chaosx.nr020.71` and before the ordinary reconstruction/aftermath chain (`.72`/`.73`), and it must remain mutually exclusive with world-end super-event 086. A short regional war, a crisis under 365 days, or an ordinary RTX defeat should not produce this super-event.

The text should acknowledge that the crown has fallen while hospitals, railways, archives, empty towns, and sealed warrens still carry the cost. It should not expose eligibility thresholds or imply that disease disappeared immediately. The existing 085 and 086 buttons are already `Sic transit gloria mundi.` and `A plague o' both houses!`; slot 87 should use a different register and should not reuse either quotation family.

## Main-quote candidates

| Candidate | Exact short fragment | Source and date | Fit | Confidence and rights |
| --- | --- | --- | --- | --- |
| **Aeschylus, selected** | “In visions of the night, like dropping rain, / Descend the many memories of pain” | *Agamemnon*, chorus; ancient play first performed ca. 458 BCE. Wording is E. D. A. Morshead's 1881 English translation. [Project Gutenberg text](https://www.gutenberg.org/cache/epub/8604/pg8604-images.html); [MIT Internet Classics metadata/text](https://classics.mit.edu/Aeschylus/agamemnon.html). | The surviving world is not triumphant: plague memories return at night, and the cost of victory remains inside the people who rebuild. The chorus's movement from suffering toward hard-won knowledge matches a defeat aftermath without making the Rat King noble. | High attribution confidence: the wording and Morshead attribution are confirmed in both texts. Aeschylus is ancient and the 1881 translation is public domain by age; Project Gutenberg permits reuse under its licence. The source line ends at `pain` without terminal punctuation, so the implementation should preserve that or mark an editorial omission rather than silently invent punctuation. |
| George Santayana | “Those who cannot remember the past are condemned to repeat it.” | *The Life of Reason*, “Reason in Common Sense,” ch. XII (1905). [Project Gutenberg text](https://www.gutenberg.org/files/15000/15000-h/15000-h.htm). | Directly supports memorial, archive-preservation, and vigilance themes. It is concise and legible, but it is now a heavily reused aphorism and says less about grief than the Aeschylus fragment. | High wording/attribution confidence. 1905 publication is public domain in the United States; Project Gutenberg provides a reusable edition. Use as a backup, not the lead, because its familiarity can feel generic. |
| Rudyard Kipling | “Or watch the things you gave your life to, broken, / And stoop and build 'em up with worn-out tools.” | “If—,” written 1895 and published in *Rewards and Fairies* (1910). [Poetry Foundation text](https://www.poetryfoundation.org/poems/46473/if---); [Project Gutenberg catalogue/eBook](https://www.gutenberg.org/ebooks/23967). | Precisely names reconstruction after catastrophic loss and the exhaustion of survivors. It is more exhortatory and paternal than the reflective slot-87 brief, and the poem is very recognizable. | High wording/attribution confidence. The poem is public domain by age; keep the excerpt short. Use only as a backup if the design wants a rebuilding-forward rather than memorial tone. |
| Abraham Lincoln | “Let us strive on to finish the work we are in; to bind up the nation's wounds” | Second Inaugural Address, 4 March 1865. [Library of Congress primary text](https://www.loc.gov/resource/mal.4361300/?st=text). | Offers an unusually clear reconstruction and reconciliation image for hospitals, infrastructure, and former coalition members. It is tied to the American Civil War and can sound too civic or optimistic for a plague-world aftermath. | High wording/attribution confidence; a U.S. government speech is public domain. Use as a backup when the event's visual and audio treatment is explicitly reconstruction/reconciliation. |
| John Donne | “Any man's death diminishes me, because I am involved in mankind” | *Devotions upon Emergent Occasions*, Meditation XVII (1624). [Project Gutenberg text](https://www.gutenberg.org/files/23772/23772-h/23772-h.htm). | Gives the event a communal death-and-survivor perspective and works especially well with a memorial image. It is religious prose and its bell passage is strongly associated with a later modern novel, so it is better as a backup or button source. | High wording/attribution confidence. Donne's 1624 work is public domain; use this short fragment only. |
| Thucydides / Pericles (backup only) | “For heroes have the whole earth for their tomb.” | Funeral Oration as recorded by Thucydides, *History of the Peloponnesian War*, Book II; wording commonly from Richard Crawley's public-domain translation. [MIT Internet Classics source](https://classics.mit.edu/Thucydides/pelopwar.2.second.html). | Strong memorial language for the dead of a global catastrophe, but it makes the event sound like a conventional heroic war and the speech is a reconstruction by Thucydides rather than a verbatim transcript. | Medium attribution confidence for the exact speech wording; public-domain ancient source/old translation. Keep as a reserve only. |

## Selected main quote

**Recommendation:**

> “In visions of the night, like dropping rain,  
> Descend the many memories of pain”
>
> — Aeschylus, *Agamemnon* (trans. E. D. A. Morshead, 1881)

Use this as the value of `chaosx_super_event.87.q`, with the attribution on its own line in the same style as 085 and 086. The two-line fragment is fourteen words, is traceable to the chorus, and does not repeat the Biblical or Shakespearean atmosphere already used by 086. It gives the defeat event a cost-of-victory perspective while leaving room for the description to name practical rebuilding.

If the quote area cannot comfortably hold a two-line fragment, the exact short fallback from the same source is “Men shall learn wisdom, by affliction schooled.” It is only seven words, but it sounds more moralizing and less like survivor testimony.

## Cultural remark and button candidates

| Candidate | Source and date | Fit and risk |
| --- | --- | --- |
| **`Lest we forget.` (selected)** | Refrain from Rudyard Kipling, “Recessional” (1897). [Wikisource primary text](https://en.wikisource.org/wiki/Rudyard_Kipling%27s_Verse%2C_Inclusive_Edition%2C_1885-1918/Recessional); [Project Gutenberg anthology text](https://www.gutenberg.org/files/16436/16436-h/16436-h.htm). | Four-word memorial/vigilance fragment for a world that has survived but is not safe. The source repeats “Lest we forget—lest we forget!”; shortening it for a button is a transparent fragment, not an invented quotation. The poem is public domain (1897), so copyright risk is low. The phrase has Biblical roots, but the recommendation is specifically the Kipling refrain and should be attributed in the research note rather than expanded into the stanza. |
| `For whom the bell tolls.` | John Donne, Meditation XVII (1624), [Project Gutenberg text](https://www.gutenberg.org/files/23772/23772-h/23772-h.htm). | A compact death/memorial allusion, but the phrase is strongly associated with Hemingway's 1940 novel. The title-like fragment itself is old/public domain; modern association risk makes it a backup only. |
| `No man is an island.` | John Donne, Meditation XVII (1624), same [Project Gutenberg text](https://www.gutenberg.org/files/23772/23772-h/23772-h.htm). | Clear solidarity and reconstruction message, public domain, and low text risk. It is less distinctive than `Lest we forget.` and duplicates the Donne source if Donne is also used for the quote. |
| `The tumult and the shouting dies.` | Kipling, “Recessional” (1897), same [Wikisource text](https://en.wikisource.org/wiki/Rudyard_Kipling%27s_Verse%2C_Inclusive_Edition%2C_1885-1918/Recessional). | A colder immediate-aftermath button that pairs well with a silent Royal Basin. It is a seven-word public-domain fragment, but the grammar and its imperial poem context are less welcoming than the selected refrain. |
| `The work begins.` | Original wording, no external source. | Safest rights position and easy to read, but generic and not sufficiently memorial for the rare global-defeat role. Keep only as an unquoted fallback if the project avoids all cultural references in this slot. |

**Selected button/cultural remark:** `Lest we forget.` — Kipling, “Recessional” (1897), public-domain short fragment. It turns the one-button interaction into a memorial vow and preserves the slot's reflective, vigilant tone instead of celebrating the military defeat.

## Recommended text package for slot 87

The following is original implementation-facing wording, not a quotation:

- Title: `THE WOUNDS REMAIN`
- Description: `The Rat King's dominion has ended after a catastrophe that crossed continents. The Royal Basin is silent, but hospitals, railways, archives, and emptied towns still bear the plague's mark. Survivors begin the long work of sealing warrens, rebuilding what can be rebuilt, and preserving the memory that victory did not make the world safe.`
- Button: `Lest we forget.`
- Main quote: `In visions of the night, like dropping rain,` followed by `Descend the many memories of pain`, attributed to Aeschylus, *Agamemnon* (trans. E. D. A. Morshead).

The description is deliberately aftermath-focused: it names the empty surface and the work left behind, does not reveal the gate's numerical thresholds, and does not promise immediate disease clearance. The proposed title is original and distinguishes slot 87 from the existing report title “After the Crown Falls.”

## Short implementation recommendation

The main agent should wire the selected text to the existing slot-87 ID and keep its gate after `chaosx.nr020.71`, before ordinary aftermath event `.73`, with the world-end branch 086 excluded. Preserve the quote's source line break and avoid adding a terminal period to `pain` unless it is marked as editorial punctuation. Keep `Lest we forget.` distinct from the 085 and 086 button strings. A unique memorial/lamament track and settings-aware audio ID remain separate research/asset work; neither 101 coronation audio nor 102 world-end audio should be reused.

## Remaining uncertainty and rights notes

- The quote attribution is high confidence, but the Morshead source line ends `pain` without terminal punctuation. The localisation owner should decide whether the UI's closing quotation mark is sufficient or whether an editorial ellipsis is preferable.
- The event's global-defeat gate and exact timing remain implementation-owned; this note assumes the addendum's once-only 365-day, multi-continent, multi-major-opponent gate.
- `Lest we forget.` is a four-word fragment of a public-domain 1897 refrain. Do not copy the full stanza into localisation; the short fragment is enough for the button.
- `For whom the bell tolls.` is safe as an old fragment but carries a strong Hemingway association; it is not the recommendation.
- Audio, image provenance, and registry wiring were not researched or changed in this text-only handoff.

Changed file: this handoff note only.
