# Event 012 Africa Super-Event Text Research

Updated: 2026-06-16

## Scope

- Event ID: `012`
- Event slug: `africa`
- This note covers super-event text research only: title direction, main-quote candidates, button/cultural-remark candidates, provenance, confidence, and blockers.
- Audio, image, localisation implementation, slot wiring, and gameplay files remain out of scope for this pass.
- Role labels from the spec are treated as working labels, not final localisation.

## Method and guardrails

- Read surfaces: `docs/specs/012_africa_specs/prompts/012_africa_super_event_prompt.md`, `CURRENT_SOURCE_OF_TRUTH.md`, `specs/012_africa_evolutions_world_end_and_scenarios.md`, `specs/012_africa_high_chaos_absurd_paths.md`, `specs/012_africa_niche_authorities_high_chaos_expansion.md`, `matrices/012_africa_acceptance_criteria.md`, `matrices/012_africa_absurd_high_chaos_routes_matrix.md`, and `matrices/012_africa_expanded_subject_matrix.md`.
- Historical and literary wording was checked against traceable sources, preferring official documents, scripture, Project Gutenberg texts, and stable archives.
- Modern or still-copyrighted political lines are kept short and flagged.
- I did not treat quote-book copy, proverb aggregators, or unsourced social-media repetition as acceptable evidence.

## Top-level recommendations

These are the strongest current text packages by role. They are recommendations, not yet final localisation keys.

| Role | Recommended title direction | Recommended quote | Recommended button / remark | Confidence |
| --- | --- | --- | --- | --- |
| Africa unification / Charter League | Congress / unity / charter register; avoid empire-first wording | `Divided we are weak; united, Africa could become one of the greatest forces for good in the world.` | `Unite now or perish.` | High on quote, medium on final title |
| Scramble reversal / escalation | historical “Scramble” language is still the right frame | `They make a desert and call it peace.` | `All its manifestations.` | High |
| RSA continental victory peace with Allies | peace-after-civil-rupture, not triumphal annexation | `Peace hath her victories / No less renowned than war.` | `Much remains to conquer still.` | High |
| Continent-sponsor path | export, liberation, congress abroad, not colonial mimicry | `Our independence is meaningless unless it is linked up with the total liberation of Africa.` | `The lesson travels.` | Medium-high |
| Cross-continent union path | federation / congress / union register | `In the Parliament of man, the Federation of the world.` | `The federation of the world.` | High |
| Terminal World Is One gate | final world-order proclamation, cold and terminal | `the only way in which it can be permanently ended is by a world-federation.` | `Universal law.` | High |
| Forest Parliament | parliament / congress register, never beast-joke wording | `But ask now the beasts, and they shall teach thee` | `Ask now the beasts.` | High |
| World Root Mandate | root / breath / life register, solemn and uncanny | `In whose hand is the soul of every living thing, and the breath of all mankind.` | `The breath of all mankind.` | High |
| Archive of Old Seats reveal | archive / old seats / registry register | `To be unacquainted with what has passed in the world, before we came into it ourselves, is to be always children.` | `What’s past is prologue.` | High |
| Counterfeit crowns exposure | exposure / false regalia / usurped title register | `Now does he feel his title / Hang loose about him, like a giant's robe / Upon a dwarfish thief.` | `Borrowed robes.` | High |
| Bestiary Clause reveal | legal admission of nonhuman seats, not comedy | `But ask now the beasts, and they shall teach thee` | `The animals have papers.` | Medium |
| Parliament of Root and Fang escalation | solemn impossible parliament, not gag wording | `In whose hand is the soul of every living thing, and the breath of all mankind.` | `Root and fang.` | High on quote, medium on button |
| Archive-world union terminal | archive becomes global sovereignty | `Humanity is made up more of the dead than of the living.` | `The record remains.` | Medium |

## Core roles

### 1. Africa unification / Charter League

**Role fit**

This is anti-colonial continental recognition. The text should sound like a public congress becoming irreversible state fact, not like a dynastic conquest banner.

**Recommended title direction**

- Use congress / charter / union language.
- Strong title-direction anchors:
  - `Africa Must Unite` direction from Kwame Nkrumah's 1963 book and speech tradition.
  - OAU / AU `unity and solidarity` language if the route is more institutional than militant.
  - `Africa Is One` remains an acceptable internal role frame, but I would not lock it as final loc before the main agent decides whether the winning route is congress, command, crown, or covenant.

**Main quote candidates**

1. **Recommended**
   - Quote: `Divided we are weak; united, Africa could become one of the greatest forces for good in the world.`
   - Author: Kwame Nkrumah
   - Source: *I Speak of Freedom*
   - Year: 1961
   - URL: https://www.marxists.org/subject/africa/nkrumah/1961/speak-freedom.htm
   - Confidence: High on wording and attribution
   - Copyright note: modern political writing; short direct quotation only
   - Fit: strongest concise articulation of continental unity as power, not merely sentiment

2. Backup
   - Quote: `The forces that unite us are intrinsic and greater than the superimposed influences that keep us apart.`
   - Author: Kwame Nkrumah
   - Source: *Africa Must Unite*
   - Year: 1963
   - URL: https://www.marxists.org/subject/africa/nkrumah/1963/africa-must-unite.pdf
   - Confidence: High
   - Copyright note: modern political writing; short direct quotation only
   - Fit: slightly calmer and more constitutional than the recommended line

3. Backup
   - Quote: `To promote the unity and solidarity of the African States`
   - Author / issuer: Charter of the Organization of African Unity, Article II
   - Source: official OAU Charter
   - Year: 1963
   - URL: https://au.int/sites/default/files/treaties/7759-file-oau_charter_1963.pdf
   - Confidence: High
   - Copyright note: official intergovernmental document
   - Fit: usable only if the route needs austere institutional tone; weaker as drama

**Button / cultural remark candidates**

1. **Recommended**
   - Text: `Unite now or perish.`
   - Source: Kwame Nkrumah, Addis Ababa union speech / `Towards African Unity`
   - Year: 1963
   - URL: https://www.marxists.org/subject/africa/nkrumah/1963/nkrumah-towards-african-unity.pdf
   - Confidence: High
   - Copyright note: short modern political quotation
   - Fit: terse, memorable, and already in the register of continental emergency

2. Backup
   - Text: `For the sake of the trusting millions.`
   - Source: same Nkrumah passage in *Africa Must Unite*
   - URL: https://www.marxists.org/subject/africa/nkrumah/1963/africa-must-unite.pdf
   - Confidence: Medium-high
   - Fit: good for federal or welfare-heavy routes; less sharp

**Implementation note**

- If the winning route is federal or Charter League-heavy, use the Nkrumah unity quote.
- If the winning route is harder-edged military command, keep the quote and shift the title toward `The Charter Holds` or `The Continental Congress`.

### 2. Scramble for Africa reversal / escalation

**Role fit**

This is the moment old empires discover that their maps no longer behave. The best package should sound accusatory and hypocritical rather than purely triumphant.

**Recommended title direction**

- Keep explicit `Scramble` language.
- Strong directions: `The Second Scramble`, `The Scramble Returns`, or `The Maps Rebel`.
- I would not use purely generic panic titles here.

**Main quote candidates**

1. **Recommended**
   - Quote: `They make a desert and call it peace.`
   - Author: Tacitus
   - Source: *Agricola*, speech of Calgacus, in translation
   - Approx. period: c. AD 98
   - URL: https://www.gutenberg.org/files/7524/7524-h/7524-h.htm
   - Confidence: High on attribution, medium-high on exact English wording because translation varies slightly
   - Copyright note: public domain
   - Fit: best compact line for imperial hypocrisy and coercive “order”

2. Backup
   - Quote: `colonialism in all its manifestations is an evil which should speedily be brought to an end`
   - Author / issuer: Asian-African Conference Final Communique, Bandung
   - Year: 1955
   - URL: https://www.aalco.int/Basicdocuments/FINAL%20COMMUNIQU%C3%89%20OF%20THE%20ASIAN-AFRICAN%20CONFERENCE.pdf
   - Confidence: High
   - Copyright note: official conference document
   - Fit: excellent anti-colonial wording, but more declarative than dramatic

3. Backup
   - Quote: `To eradicate all forms of colonialism from Africa`
   - Author / issuer: OAU Charter, Article II
   - Year: 1963
   - URL: https://au.int/sites/default/files/treaties/7759-file-oau_charter_1963.pdf
   - Confidence: High
   - Fit: strong if the event text leans institutional and legal

**Button / cultural remark candidates**

1. **Recommended**
   - Text: `All its manifestations.`
   - Source: Bandung Final Communique fragment
   - Year: 1955
   - URL: https://www.aalco.int/Basicdocuments/FINAL%20COMMUNIQU%C3%89%20OF%20THE%20ASIAN-AFRICAN%20CONFERENCE.pdf
   - Confidence: High
   - Copyright note: official document
   - Fit: dry, bitter, and short; it makes the reversal sound like an indictment

2. Backup
   - Text: `They call it peace.`
   - Source: Tacitus, *Agricola*
   - URL: https://www.gutenberg.org/files/7524/7524-h/7524-h.htm
   - Confidence: High
   - Fit: sharper and grimmer if the event is already at war

**Implementation note**

- This is one of the safest roles for direct historical wording.
- Do not use joke buttons about maps or crayons here; the spec wants dread and hypocrisy, not meme tone.

### 3. RSA civil-war continental victory peace with Allies

**Role fit**

The event is a civil rupture inside South Africa that forces an external peace. The text should sound exhausted, administratively final, and costly.

**Recommended title direction**

- Use congress / settlement / proclamation language rather than liberation-theatre or revenge-theatre.
- Strong directions: `The Continental Settlement`, `The Congress in Pretoria`, `The Peace of the Union`.

**Main quote candidates**

1. **Recommended**
   - Quote: `Peace hath her victories / No less renowned than war.`
   - Author: John Milton
   - Source: `To the Lord General Cromwell`
   - Year: 1652
   - URL: https://www.gutenberg.org/ebooks/31706.txt.utf-8
   - Confidence: High
   - Copyright note: public domain
   - Fit: strongest concise line for victory that still lands as burdensome postwar settlement

2. Backup
   - Quote: `From ancient grudge break to new mutiny, / Where civil blood makes civil hands unclean.`
   - Author: William Shakespeare
   - Source: *Romeo and Juliet*, Prologue
   - Approx. date: c. 1595
   - URL: https://www.gutenberg.org/files/1513/1513-h/1513-h.htm
   - Confidence: High
   - Copyright note: public domain
   - Fit: very strong civil-war line, but more tragic than settlement-oriented

3. Backup
   - Quote: `there runs a certain unity`
   - Author: Olive Schreiner
   - Source: *Thoughts on South Africa*
   - Year: 1923
   - URL: https://www.gutenberg.org/cache/epub/64520/pg64520-images.html
   - Confidence: Medium because excerpting needs care
   - Copyright note: public domain in the US; check target jurisdiction if needed
   - Fit: good title-direction source, weaker as the main quote

**Button / cultural remark candidates**

1. **Recommended**
   - Text: `Much remains to conquer still.`
   - Source: Milton, same sonnet
   - URL: https://www.gutenberg.org/ebooks/31706.txt.utf-8
   - Confidence: High
   - Fit: it keeps the aftermath sober and unfinished

2. Backup
   - Text: `Civil hands unclean.`
   - Source: *Romeo and Juliet* fragment
   - URL: https://www.gutenberg.org/files/1513/1513-h/1513-h.htm
   - Confidence: High
   - Fit: harsher and darker if the event art leans urban destruction

**Implementation note**

- The Milton package is the cleanest final candidate.
- If the main event art or description focuses more on Johannesburg / Cape civil devastation than on treaty aftermath, the Shakespeare backup becomes stronger.

### 4. Continent-sponsor path

**Role fit**

Africa is no longer merely unified. It starts exporting cadres, arms, and continental method. The tone should be escalating, ambitious, and slightly alarming.

**Recommended title direction**

- Use `office`, `congress abroad`, `continental export`, or `lesson` language.
- Strong directions: `The Lesson Travels`, `The Continental Export Office`, `A Congress Abroad`.

**Main quote candidates**

1. **Recommended**
   - Quote: `Our independence is meaningless unless it is linked up with the total liberation of Africa.`
   - Author: Kwame Nkrumah
   - Source: Ghana independence speech
   - Year: 1957
   - URL: https://speakola.com/political/kwame-nkrumah-independence-day-ghana-1957
   - Confidence: Medium-high; wording is widely repeated and stable, but the accessible transcript is secondary rather than an official Ghana state archive
   - Copyright note: modern political speech; keep quotation short
   - Fit: best short line for Africa treating its own freedom as incomplete while others remain unfree

2. Backup
   - Quote: `colonialism in all its manifestations is an evil which should speedily be brought to an end`
   - Author / issuer: Bandung Final Communique
   - Year: 1955
   - URL: https://www.aalco.int/Basicdocuments/FINAL%20COMMUNIQU%C3%89%20OF%20THE%20ASIAN-AFRICAN%20CONFERENCE.pdf
   - Confidence: High
   - Fit: stronger if the sponsor path is explicitly anti-colonial rather than hegemonic

3. Backup
   - Quote: `The forces that unite us are intrinsic and greater than the superimposed influences that keep us apart.`
   - Author: Kwame Nkrumah
   - Source: *Africa Must Unite*
   - Year: 1963
   - URL: https://www.marxists.org/subject/africa/nkrumah/1963/africa-must-unite.pdf
   - Confidence: High
   - Fit: better for idealist sponsor routes than for hard covert-action routes

**Button / cultural remark candidates**

1. **Recommended**
   - Text: `The lesson travels.`
   - Source type: original wording
   - Confidence: n/a
   - Fit: safest concise button if the main quote is already modern and political

2. Sourced backup
   - Text: `All its manifestations.`
   - Source: Bandung fragment
   - URL: https://www.aalco.int/Basicdocuments/FINAL%20COMMUNIQU%C3%89%20OF%20THE%20ASIAN-AFRICAN%20CONFERENCE.pdf
   - Confidence: High
   - Fit: good if the sponsor path is militant anti-colonial rather than solidarist

**Blocked item**

- I did not find a better short public-domain line for transcontinental anti-colonial export than the Nkrumah / Bandung pair. This role is still somewhat dependent on mid-20th-century copyrighted political speech unless the main agent prefers a less specific original title-button package.

### 5. Dynamic cross-continent union formation

**Role fit**

This is bureaucratically impossible federation made real. The line should acknowledge scale without collapsing into generic apocalypse.

**Recommended title direction**

- Dynamic union names from the spec are already strong:
  - `Afro-Asian Union`
  - `African-Middle Eastern Union`
  - `Afro-Eurasian Union`
- Final title should match the actual political form: federation, congress, command, protectorate, covenant, or empire.

**Main quote candidates**

1. **Recommended**
   - Quote: `In the Parliament of man, the Federation of the world.`
   - Author: Alfred, Lord Tennyson
   - Source: `Locksley Hall`
   - Year: 1842
   - URL: https://www.gutenberg.org/files/8601/8601-h/8601-h.htm
   - Confidence: High
   - Copyright note: public domain
   - Fit: strongest concise transcontinental-federation line; grand without being tied to a single region

2. Backup
   - Quote: `The federation of the world`
   - Author: same
   - Source: same
   - URL: https://www.gutenberg.org/files/8601/8601-h/8601-h.htm
   - Confidence: High
   - Fit: useful if the full Tennyson line is reserved for the button or title direction

3. Backup
   - Quote: `The forces that unite us are intrinsic and greater than the superimposed influences that keep us apart.`
   - Author: Kwame Nkrumah
   - Source: *Africa Must Unite*
   - URL: https://www.marxists.org/subject/africa/nkrumah/1963/africa-must-unite.pdf
   - Confidence: High
   - Fit: good if the union is explicitly Afrocentric rather than universalist

**Button / cultural remark candidates**

1. **Recommended**
   - Text: `The federation of the world.`
   - Source: Tennyson fragment
   - URL: https://www.gutenberg.org/files/8601/8601-h/8601-h.htm
   - Confidence: High
   - Fit: short, ceremonial, and legible in UI

2. Backup
   - Text: `Standards of the peoples.`
   - Source: nearby Tennyson imagery in `Locksley Hall`
   - URL: https://www.gutenberg.org/files/8601/8601-h/8601-h.htm
   - Confidence: Medium
   - Fit: more visual, less explicit

### 6. Terminal World Is One gate

**Role fit**

This is a world-end proclamation, not a normal victory. The line should feel terminal and ideological rather than merely optimistic.

**Recommended title direction**

- Keep the current `The World Is One` direction as a valid working front-runner.
- Backup directions: `Universal Law`, `The Final Congress`, `One World Order` only if the route is openly tyrannical.

**Main quote candidates**

1. **Recommended**
   - Quote: `the only way in which it can be permanently ended is by a world-federation.`
   - Author: Bertrand Russell
   - Source: *Why Men Fight*
   - Year: 1917
   - URL: https://www.gutenberg.org/files/55610/55610-h/55610-h.htm
   - Confidence: High
   - Copyright note: public domain text at Project Gutenberg
   - Fit: best cold-political line for a terminal world-order route; can read as warning or justification

2. Backup
   - Quote: `One God, one law, one element, / And one far-off divine event, / To which the whole creation moves.`
   - Author: Alfred, Lord Tennyson
   - Source: *In Memoriam A.H.H.*, Conclusion
   - Year: 1850
   - URL: https://www.gutenberg.org/cache/epub/70950/pg70950-images.html
   - Confidence: High
   - Copyright note: public domain
   - Fit: grand and final, but more hopeful and metaphysical

3. Backup
   - Quote: `And the Lord shall be king over all the earth: in that day shall there be one Lord, and his name one.`
   - Source: Zechariah 14:9, KJV
   - URL: https://www.biblegateway.com/passage/?search=Zechariah+14%3A9&version=KJV
   - Confidence: High for KJV wording
   - Copyright note: public domain
   - Fit: very final, but too route-specific unless the branch is openly covenantal or theocratic

**Button / cultural remark candidates**

1. **Recommended**
   - Text: `Universal law.`
   - Source: Tennyson nearby phrase `lapt in universal law`
   - URL: https://www.gutenberg.org/files/8601/8601-h/8601-h.htm
   - Confidence: High
   - Fit: short and terminal

2. Backup
   - Text: `One far-off divine event.`
   - Source: Tennyson
   - URL: https://www.gutenberg.org/cache/epub/70950/pg70950-images.html
   - Confidence: High
   - Fit: excellent if the route is majestic rather than coldly administrative

## High-chaos roles

### 7. Forest Parliament reveal

**Role fit**

The event must be solemn and impossible, not comic. The text should sound like nonhuman testimony entering politics.

**Recommended title direction**

- Keep parliament / congress language.
- Strong directions: `The Forest Parliament`, `The Forest Signs Separately`, `The Parliament of the Green`.

**Main quote candidates**

1. **Recommended**
   - Quote: `But ask now the beasts, and they shall teach thee`
   - Source: Job 12:7, KJV
   - URL: https://www.biblegateway.com/passage/?search=Job+12%3A7-10&version=KJV
   - Confidence: High
   - Copyright note: public domain
   - Fit: strongest concise line for nonhuman political testimony

2. Backup
   - Quote: `or speak to the earth, and it shall teach thee`
   - Source: Job 12:8, KJV
   - URL: https://www.biblegateway.com/passage/?search=Job+12%3A7-10&version=KJV
   - Confidence: High
   - Fit: better if the image leans root / earth rather than primate delegates

**Button / cultural remark candidates**

1. **Recommended**
   - Text: `Ask now the beasts.`
   - Source: Job 12:7 fragment
   - URL: https://www.biblegateway.com/passage/?search=Job+12%3A7-10&version=KJV
   - Confidence: High
   - Fit: short and immediately legible

2. Backup
   - Text: `The forest signs separately.`
   - Source type: original wording, drawn from spec tone
   - Fit: excellent original button if the main agent wants to avoid double-using Job for both quote and button

### 8. World Root Mandate

**Role fit**

This is not merely an animal parliament. It is an order binding human and nonhuman life under one mandate.

**Recommended title direction**

- Keep `World Root` / `Root Mandate` register.
- Strong directions: `The World Root Mandate`, `The Root Takes the World`, `The Root and the Breath`.

**Main quote candidates**

1. **Recommended**
   - Quote: `In whose hand is the soul of every living thing, and the breath of all mankind.`
   - Source: Job 12:10, KJV
   - URL: https://www.biblegateway.com/passage/?search=Job+12%3A10&version=KJV
   - Confidence: High
   - Copyright note: public domain
   - Fit: best single line for the covenantal fusion of all life and humanity

2. Backup
   - Quote: `I believe a leaf of grass is no less than the journey work of the stars,`
   - Author: Walt Whitman
   - Source: *Leaves of Grass*
   - Year: 1855
   - URL: https://www.gutenberg.org/files/1322/1322-h/1322-h.htm
   - Confidence: High
   - Copyright note: public domain
   - Fit: beautiful and strange, but less authoritative than Job

**Button / cultural remark candidates**

1. **Recommended**
   - Text: `The breath of all mankind.`
   - Source: Job 12:10 fragment
   - URL: https://www.biblegateway.com/passage/?search=Job+12%3A10&version=KJV
   - Confidence: High
   - Fit: solemn and compact

2. Backup
   - Text: `A leaf of grass.`
   - Source: Whitman fragment
   - URL: https://www.gutenberg.org/files/1322/1322-h/1322-h.htm
   - Confidence: High
   - Fit: quieter, more poetic, less commanding

## Archive / Bestiary package

### 9. Archive of Old Seats continental reveal

**Role fit**

This is the dossier / archive layer becoming a continental constitutional force. The line should privilege memory, precedent, and restored record.

**Recommended title direction**

- Strong directions: `The Archive of Old Seats`, `Open the Archive`, `The Old Seats Return`.

**Main quote candidates**

1. **Recommended**
   - Quote: `To be unacquainted with what has passed in the world, before we came into it ourselves, is to be always children.`
   - Author: Cicero
   - Source: *Brutus or History of Famous Orators*
   - Approx. period: 46 BC
   - URL: https://www.gutenberg.org/cache/epub/9776/pg9776.html
   - Confidence: High on the cited translation
   - Copyright note: public domain
   - Fit: best archive-state line in the package

2. Backup
   - Quote: `What’s past is prologue`
   - Author: William Shakespeare
   - Source: *The Tempest*, Act II, Scene I
   - Approx. date: c. 1611
   - URL: https://www.gutenberg.org/files/23042/23042-h/23042-h.htm
   - Confidence: High
   - Copyright note: public domain
   - Fit: excellent shorter alternative, especially as button text

**Button / cultural remark candidates**

1. **Recommended**
   - Text: `What’s past is prologue.`
   - Source: *The Tempest*
   - URL: https://www.gutenberg.org/files/23042/23042-h/23042-h.htm
   - Confidence: High
   - Fit: ideal archive button

2. Backup
   - Text: `Open the archive.`
   - Source type: original wording
   - Fit: safer if the quote already carries the literary weight

### 10. Counterfeit crowns exposure

**Role fit**

This role is about fraudulent restoration masks and stolen legitimacy. It needs exposure, not grandeur.

**Recommended title direction**

- Strong directions: `Counterfeit Crowns`, `Borrowed Robes`, `False Restoration`.

**Main quote candidates**

1. **Recommended**
   - Quote: `Now does he feel his title / Hang loose about him, like a giant's robe / Upon a dwarfish thief.`
   - Author: William Shakespeare
   - Source: *Macbeth*, Act V, Scene II
   - Approx. date: c. 1606
   - URL: https://shakespeare.mit.edu/macbeth/full.html
   - Confidence: High
   - Copyright note: public domain
   - Fit: nearly perfect for false crowns and theatrical usurpation

2. Backup
   - Quote: `What’s past is prologue`
   - Author: Shakespeare
   - Source: *The Tempest*
   - URL: https://www.gutenberg.org/files/23042/23042-h/23042-h.htm
   - Confidence: High
   - Fit: useful if the event focuses more on archival proof than exposed fraud

**Button / cultural remark candidates**

1. **Recommended**
   - Text: `Borrowed robes.`
   - Source: *Macbeth* fragment
   - URL: https://shakespeare.mit.edu/macbeth/full.html
   - Confidence: High
   - Fit: strongest concise button in the whole Archive package

### 11. Bestiary Clause reveal

**Role fit**

This is legal and uncanny. The text must make clear that nonhuman actors are being admitted as explicit nonhuman seats, not treated as jokes or mascots.

**Recommended title direction**

- Strong directions: `The Bestiary Clause`, `The Clause Is Signed`, `The Animals Have Standing`.
- Do not use a comic title as final loc unless the whole route intentionally leans theatrical and the main agent approves it.

**Main quote candidates**

1. **Recommended**
   - Quote: `But ask now the beasts, and they shall teach thee`
   - Source: Job 12:7, KJV
   - URL: https://www.biblegateway.com/passage/?search=Job+12%3A7-10&version=KJV
   - Confidence: High
   - Fit: strongest explicit nonhuman-witness line

2. Backup
   - Quote: `In whose hand is the soul of every living thing, and the breath of all mankind.`
   - Source: Job 12:10, KJV
   - URL: https://www.biblegateway.com/passage/?search=Job+12%3A10&version=KJV
   - Confidence: High
   - Fit: better if the clause is framed as broad life-law rather than animal testimony

**Button / cultural remark candidates**

1. **Recommended but blocked for tone check**
   - Text: `The animals have papers.`
   - Source type: spec-grounded allusive wording, not a real quotation
   - Confidence: n/a
   - Fit: memorable and specific
   - Blocker: good conceptually, but still needs main-agent tone judgment because it can read too comic if paired with solemn art

2. Sourced backup
   - Text: `Ask now the beasts.`
   - Source: Job 12:7 fragment
   - URL: https://www.biblegateway.com/passage/?search=Job+12%3A7-10&version=KJV
   - Confidence: High
   - Fit: safer final candidate if solemnity is the priority

### 12. Parliament of Root and Fang escalation

**Role fit**

This is the absurd package going fully constitutional. It must sound solemn, crowded, and politically impossible.

**Recommended title direction**

- Strong directions: `Parliament of Root and Fang`, `The Root and the Fang`, `The Impossible Parliament`.

**Main quote candidates**

1. **Recommended**
   - Quote: `In whose hand is the soul of every living thing, and the breath of all mankind.`
   - Source: Job 12:10, KJV
   - URL: https://www.biblegateway.com/passage/?search=Job+12%3A10&version=KJV
   - Confidence: High
   - Fit: best line for mixed human / nonhuman constitutional order

2. Backup
   - Quote: `I believe a leaf of grass is no less than the journey work of the stars,`
   - Author: Walt Whitman
   - Source: *Leaves of Grass*
   - URL: https://www.gutenberg.org/files/1322/1322-h/1322-h.htm
   - Confidence: High
   - Fit: excellent if the route turns more visionary than juridical

**Button / cultural remark candidates**

1. **Recommended**
   - Text: `Root and fang.`
   - Source type: original wording
   - Fit: clean, ritual, not jokey

2. Sourced backup
   - Text: `the breath of all mankind.`
   - Source: Job 12:10 fragment
   - URL: https://www.biblegateway.com/passage/?search=Job+12%3A10&version=KJV
   - Confidence: High

### 13. Archive-world union terminal

**Role fit**

The archive has stopped being a registry and become a planetary sovereign principle. This should feel colder and more uncanny than the ordinary World Is One path.

**Recommended title direction**

- Strong directions: `The Archive of the World`, `The World Under Record`, `The Last Ledger`.

**Main quote candidates**

1. **Recommended**
   - Quote: `Humanity is made up more of the dead than of the living.`
   - Attributed by: Auguste Comte, cited in a public-domain philosophical exposition
   - Source witness: *The Philosophy of Auguste Comte*
   - Year of witness text: 1903
   - URL: https://www.gutenberg.org/cache/epub/56517/pg56517-images.html
   - Confidence: Medium; the wording is stable and explicitly attributed to Comte in public-domain secondary exposition, but I did not verify it against a French primary edition in this pass
   - Copyright note: public-domain witness text; attribution should be marked as medium-confidence
   - Fit: strongest archive-terminal line because it turns historical record into sovereign burden

2. Backup
   - Quote: `the living are more and more governed by the dead`
   - Attributed by: Auguste Comte, reported in John Stuart Mill's *Auguste Comte and Positivism*
   - Year of witness text: 1865
   - URL: https://www.gutenberg.org/files/16833/16833-h/16833-h.htm
   - Confidence: Medium
   - Fit: harsher and more openly domineering

3. Backup
   - Quote: `What’s past is prologue`
   - Author: Shakespeare
   - Source: *The Tempest*
   - URL: https://www.gutenberg.org/files/23042/23042-h/23042-h.htm
   - Confidence: High
   - Fit: safer if the Comte attribution is considered too indirect

**Button / cultural remark candidates**

1. **Recommended**
   - Text: `The record remains.`
   - Source type: original wording
   - Fit: strongest concise button without overcommitting to uncertain quotation provenance

2. Sourced backup
   - Text: `What’s past is prologue.`
   - Source: Shakespeare
   - URL: https://www.gutenberg.org/files/23042/23042-h/23042-h.htm
   - Confidence: High

## Blockers and caution notes

- **No final localisation keys yet.** The research is strong enough to support final loc drafting for several roles, but the title layer still depends on route tone and presentation art.
- **Nkrumah transcript caution.** The 1957 independence line is extremely famous and stable, but the accessible transcript I verified is a secondary transcript page rather than an official Ghana state archive. I rate it medium-high, not absolute.
- **Comte attribution caution.** The archive-terminal Comte line is strong but presently rests on public-domain secondary witnesses. If the main agent wants maximum-proof sourcing, use the Shakespeare backup instead.
- **Bestiary button caution.** `The animals have papers.` is effective but not a real quotation and can tip too comic if paired with solemn art. Keep it blocked until the main agent chooses final presentation tone.
- **Do not use unsourced “African proverb” material.** I did not find a proverb candidate with primary-text reliability strong enough for finals in this pass.
- **Keep human material human.** Historical African polities should keep political, archival, and anti-colonial language; nonhuman / covenant roles should be explicitly labeled as impossible, nonhuman, or supernatural routes.

## Short implementation recommendation for the main agent

- Safest near-final packages:
  - Africa unification: Nkrumah `Divided we are weak...` + `Unite now or perish.`
  - Scramble reaction: Tacitus `They make a desert...` + Bandung `All its manifestations.`
  - RSA peace: Milton `Peace hath her victories...` + `Much remains to conquer still.`
  - Cross-continent union: Tennyson `Parliament of man...`
  - Terminal World Is One: Russell `world-federation` line if the route should read cold and terminal
  - Forest / Bestiary / Root: Job 12 is the strongest shared source family
  - Archive package: Cicero / Shakespeare / Macbeth are the strongest proven cluster
- If the main agent wants maximum-proof-only sourcing, avoid the Comte and 1957 Nkrumah lines and use the public-domain backups already listed here.
