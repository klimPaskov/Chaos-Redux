# Event 12 Africa language, ruler-name, and sensitivity protocol

## Purpose

The user requires absurd, funny, and obscene source-language ruler or court flavour while keeping the broader package historically serious.

This note defines how that flavour can be used without turning African languages, ethnic identities, or real people into caricatures.

## Required strings

The following user-mandated Afaan Oromoo strings must be available as fictional ruler, regnal, court, council, or title flavour:

- `qaama saalaa koo xuuxaa`
- `haadha kee waliin wal qunnamtii saalaa raawwadhe`

They remain untranslated in English-facing text.

They must never be used in:

- file names
- script identifiers
- localisation keys
- country tags
- cosmetic tags
- sprite names
- asset names
- character keys
- technology keys
- unit template keys
- achievement keys
- debug names

Use neutral internal identifiers such as:

- `africa_absurd_regnal_name_01`
- `africa_absurd_regnal_name_02`

The final visible string should be supplied only through localisation.

## Verification status

### First required string

Partial lexical evidence supports:

- `qaama saalaa` as a term for genital or sexual organs
- `koo` as a first-person possessive meaning my or mine
- `xuuxaa` as a form associated with sucking or smoking in available online examples

The complete phrase has not been verified by a native speaker in a reliable published source.

Status:

- user-mandated
- partial lexical support
- full idiomatic meaning and register require native-speaker review

### Second required string

Partial lexical evidence supports:

- `haadha kee` as your mother
- `wal qunnamtii saalaa` as sexual relations or intercourse
- `raawwadhe` as a first-person completed form associated with having performed or done an action

The complete phrase has not been verified by a native speaker in a reliable published source.

Status:

- user-mandated
- strong component-level support
- full idiomatic meaning, offensiveness, and dialect require native-speaker review

## Source notes for component review

The available online material is uneven. It is sufficient to support a cautionary component review, not a final linguistic certification.

Sources consulted:

- [Afaan Oromo-English Dictionary](https://www.scribd.com/document/870398584/Afaan-oromo-dictionary), online dictionary copy containing `qaama saalaa` for genital
- [Afaan Oromo Online language material](https://afaan-oromoo.com/brief-history-of-afaan-oromoo-and-qubee-afaan-oromoo-afaan-oromoo/), containing examples of `wal-qunnamtii saalaa`
- [Oromo translation example containing `qaama saalaa`](https://quranenc.com/en/browse/oromo_ababor/7/20), QuranEnc
- [Oromo grammar walkthrough](https://mossyrune.com/grammar/walkthrough/oromo), containing `koo` and `kee` possessive examples
- [Afaan Oromoo religious text with `wal-qunnamtii saalaa raawwadhe`](https://t.me/s/oromoQuen?before=1789), used only as an occurrence check and not as an authority for profanity or register

## Native-speaker review requirement

Before final localisation, every obscene or vulgar name should be reviewed by at least one fluent speaker of the relevant language.

The review record should contain:

- exact string
- language
- dialect or regional variety
- literal gloss
- idiomatic meaning
- grammatical person and number
- whether it sounds like a name, sentence, insult, command, boast, or nonsense phrase
- offensiveness level
- whether it targets a protected group or real community
- whether it includes a slur
- whether it is safe for the intended humour tier
- reviewer confidence
- approved spelling

## Additional obscene name policy

No additional raw obscene phrases are added to this planning package because the available research did not provide reliable native-speaker verification.

This is an intentional accuracy safeguard, not a rejection of the requested humour.

The implementation should commission a bounded multilingual review for additional names in languages connected to implemented country packages.

Priority language groups can include:

- Afaan Oromoo
- Swahili
- Yoruba
- Hausa
- Akan or Twi
- Lingala
- Kikongo varieties
- Zulu
- Xhosa
- Shona
- Amharic
- Somali
- Malagasy
- Arabic varieties used in North and North-East Africa

The review should produce a small pool rather than hundreds of phrases.

Recommended target:

- 3 to 6 approved vulgar or absurd names for each major language pool that actually appears in the implementation
- 1 to 3 approved names for smaller regional pools
- no pool for a language that does not have a relevant leader, court, or high-chaos package

## Humour placement rules

Approved obscene names can appear as:

- fictional monarch names
- regnal names
- epithets
- court nicknames
- high-chaos prophet names
- nonhuman sovereign names
- satirical council members
- rare advisor names
- hidden character-pool outcomes

They should not appear as:

- the public country name
- the main event title
- the Charter League name
- a real historical person
- a real ethnic group label
- a real religious title used only for mockery
- a technical or debug identifier
- every leader in a region

## Frequency and weighting

The joke should remain rare enough to surprise the player.

Suggested distribution:

- grounded routes: very low chance
- absurd political routes: low to medium chance
- high-chaos courts: medium chance
- nonhuman and supernatural routes: medium to high chance
- serious historical restoration with a real ruler: disabled

A country should not reroll its ruler repeatedly to farm joke names.

## Protected boundaries

Reject any candidate that:

- contains an ethnic slur
- contains a racial slur
- mocks a disability
- targets a real living person
- uses a sacred formula only as crude abuse without route justification
- reproduces colonial stereotypes
- presents a human African ethnic group as an animal
- uses sexual violence as a light joke
- is translated incorrectly
- is only machine-translated

## Technical handoff

The implementation should use:

- neutral indexed localisation keys
- route and region specific name pools
- one-time assignment at leader creation
- fixed assigned names after creation
- matching portrait gender pools where the leader is a person
- institutional names, emblems, and text for councils and symbolic bodies, with no council or group portraits
- a debug tool that displays neutral keys rather than raw vulgar strings where possible

## Localisation note

English-facing localisation should show the approved source-language string without an English profanity translation.

Optional tooltip direction can state the language or court origin without giving the vulgar gloss.

The joke depends on apparent foreign-language dignity. A direct English translation would make the package cruder and less effective.

## Review ledger template

| Neutral key | Language | Dialect | Visible string | Literal gloss | Idiomatic meaning | Offensiveness | Approved | Reviewer note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| africa_absurd_regnal_name_01 | Afaan Oromoo | needs review | user-required string 1 | needs review | needs review | needs review | pending | preserve exact spelling until reviewed |
| africa_absurd_regnal_name_02 | Afaan Oromoo | needs review | user-required string 2 | needs review | needs review | needs review | pending | preserve exact spelling until reviewed |

The final ledger should remain in documentation, not in player-facing text.
