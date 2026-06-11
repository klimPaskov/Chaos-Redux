# Holy Realm Buddhahood Super-Event Text Handoff

Scope: quote/title/subtitle research only. No gameplay or localisation edits.

## Recommendation summary

### 1. The Awakened One

- Recommended title: `The Awakened One`
- Title backups: `Beneath the Unshaken Seat`, `The Wheel Stands Still`
- Subtitle/description lead note: the world stops treating the former Bodhisattva as a normal sovereign; capitals, soldiers, and pilgrims all report the same impossible calm.
- Recommended quote: `he stands, dispelling the hosts of Mara, like the sun that illuminates the sky.`
- Source: *Vinaya Texts, Part I* (Mahavagga I.1.7), translated by T. W. Rhys Davids and Hermann Oldenberg, 1881
- Source URL: https://sacred-texts.com/bud/sbe13/sbe1312.htm
- License status: public domain translation by publication date; hosted in the Sacred Books of the East archive
- Why this fits: this is the cleanest transformation quote in the package. It marks awakening, victory over Mara, and visible radiance without forcing the event to claim literal identity with the historical Gautama Buddha.

Backup quote options:

- `maker of the tabernacle, thou hast been seen`
- Source: *Dhammapada* 153-154, trans. F. Max Muller, 1881
- URL: https://sacred-texts.com/bud/sbe10/sbe1013.htm
- License: public domain

- `the mind ... has attained to the extinction of all desires`
- Source: *Dhammapada* 154, trans. F. Max Muller, 1881
- URL: https://sacred-texts.com/bud/sbe10/sbe1013.htm
- License: public domain

### 2. Powers of the Awakened

- Recommended title: `Powers of the Awakened`
- Title backups: `The River Became Earth`, `The Wall Was Only Air`
- Subtitle/description lead note: the first miracle should read like a military impossibility observed by frightened witnesses, not a triumphant spell cast.
- Recommended quote: `Get rid of this disposition, train yourself, and remain in that.`
- Source: *Dialogues of the Buddha*, DN 11 `Kevaddha Sutta`, translated by T. W. Rhys Davids, 1899
- Source URL: https://sacred-texts.com/bud/dob/dob-11tx.htm
- License status: public domain translation by publication date
- Why this fits: the event is about powers becoming undeniable, but the spec explicitly wants a line that keeps powers subordinate to liberation. The `wonder of education` passage does that better than a raw miracle list.

Backup quote options:

- `not by entering into a trance ... be not confident ...`
- Source: *Dhammapada* 271-272, trans. F. Max Muller, 1881
- URL: https://sacred-texts.com/bud/sbe10/sbe1021.htm
- License: public domain
- Fit note: strong warning that altered states are not the goal; good if the main team wants a more ascetic tone.

- `from being one he becomes multiform`
- Source: DN 11 `Kevaddha Sutta`, trans. T. W. Rhys Davids, 1899
- URL: https://sacred-texts.com/bud/dob/dob-11tx.htm
- License: public domain
- Fit note: direct tie to the actual power list, but weaker spiritually than the selected line.

### 3. The Final Silence

Use one title for both branches. Differentiate with subtitle/description and quote.

- Recommended title: `The Final Silence`
- Title backups: `The Last Bell`, `When the Wheel Stopped`

#### Non-terminal variant

- Subtitle/description lead note: the seat is empty, fronts go quiet, but the world remains to reckon with what has been left behind.
- Recommended quote: `Where is it that both name and form die out, leaving no trace behind?`
- Source: *Dialogues of the Buddha*, DN 11 `Kevaddha Sutta`, translated by T. W. Rhys Davids, 1899
- Source URL: https://sacred-texts.com/bud/dob/dob-11tx.htm
- License status: public domain translation by publication date
- Why this fits: this is the best non-terminal line for the Empty Seat aftermath. It is spare, metaphysical, and non-martial, which matches the spec.

#### Terminal variant

- Subtitle/description lead note: radio traffic, commands, and battle rhythm all fall silent at once; the event should feel final, not explosive.
- Recommended quote: `As the extinction of a flame, even so was his mind's release.`
- Source: *Buddhist Scriptures*, `The Death of Buddha` quoting the Mahaparinibbana tradition, translated/compiled by E. J. Thomas, 1913; excerpt citing `Mahaparinibbana S. VI`
- Source URL: https://sacred-texts.com/bud/busc/busc24.htm
- License status: public domain in the US by publication date; old printed translation
- Why this fits: it gives the terminal branch a stronger final image than the non-terminal line, while staying quiet and non-spectacular.

Backup quote options:

- `Impermanent are compound things; strive with earnestness.`
- Source: `The Death of Buddha`, citing the Tathagata's last words
- URL: https://sacred-texts.com/bud/busc/busc24.htm
- License: public domain
- Fit note: excellent for severity and finality, but it sounds more like a charge to the living than the end-state itself.

- `This truly is the highest happiness!`
- Source: *Vinaya Texts, Part I* (Mahavagga I.3.4), trans. T. W. Rhys Davids and Hermann Oldenberg, 1881
- URL: https://sacred-texts.com/bud/sbe13/sbe1312.htm
- License: public domain
- Fit note: stronger for the non-terminal spiritual-victory branch than for the terminal world-end branch.

## Button and subtitle notes

No joke button text is suitable here. The existing spec direction is already better than most sourced cultural references.

Recommended localisation-safe button direction:

- `The wheel turns.` for `The Awakened One`
- `The armies stopped speaking.` for `Powers of the Awakened`
- `The seat is empty.` for non-terminal `The Final Silence`
- `Nothing answered.` for terminal `The Final Silence`

These are not direct quotations and do not need source attribution.

## License and translation risk notes

- The strongest recommendations above are all from public-domain English translations published between 1881 and 1913.
- The tradeoff is tone: several lines use older diction such as `Mara`, `name and form`, `mystic wonder`, and Victorian cadence.
- Modern alternatives exist on Access to Insight and SuttaCentral, but they are not public domain. Access to Insight republishes under a free redistribution license with conditions; SuttaCentral translations vary by translator and license.
- If the implementation pass wants more contemporary English, switch only after checking the exact translation license for the chosen line.

## Main-agent implementation note

- Keep the quoted text short in UI.
- Preserve source wording if using the recommended public-domain lines.
- If the team wants a more contemporary style, prefer changing the description text first and keep the quote archival.
- The cleanest package from a source-risk standpoint is:
  - `The Awakened One` -> Mahavagga sunrise-over-Mara line
  - `Powers of the Awakened` -> Kevaddha `wonder of education` line
  - `The Final Silence` non-terminal -> Kevaddha `name and form die out` line
  - `The Final Silence` terminal -> `extinction of a flame` line
