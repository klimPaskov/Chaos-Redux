# Event 006 super-event text research handoff

Research date: 2026-08-26.

Scope: bounded source, wording, attribution, rights, role-fit, and UI-fit verification for the two Event 006 super-events. No localisation, gameplay, super-event wiring, audio, asset, spreadsheet, or source-specification file was changed. No live-game validation was performed or claimed.

## Source material reviewed

- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`
- `docs/specs/006_independence_wave_specs/prompts/independence_wave_super_event_prompt.md`
- `docs/specs/006_independence_wave_specs/research/006_super_event_text_research.md`
- `docs/specs/006_independence_wave_specs/research/006_research_bibliography.md`
- `docs/specs/006_independence_wave_specs/research/006_source_register.csv`
- `docs/plans/006_independence_wave_plans/super_event_research/006_super_event_text_verification.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_super_event_text_round_2026_08_24.md`
- Current definitions in `localisation/english/006_independence_wave_l_english.yml` for slots `23` and `24`.

Fresh HTTPS source-page checks on 2026-08-26:

- [Yale Avalon Project, President Woodrow Wilson's Fourteen Points](https://avalon.law.yale.edu/20th_century/wilson14.asp) displays Point XIV and the `8 January, 1918` document heading.
- [U.S. National Archives, President Woodrow Wilson's 14 Points](https://www.archives.gov/milestone-documents/president-woodrow-wilsons-14-points) identifies Wilson's 8 January 1918 address to Congress and reproduces the same Point XIV wording.
- [BibleGateway, Hosea 8:7, King James Version](https://www.biblegateway.com/passage/?search=Hosea%208%3A7&version=KJV) displays the selected verse wording and labels the KJV text `Public Domain`.

## Current verdict

Keep the approved ordinary slots and text packages:

- `23` — `The League of New States`: Woodrow Wilson, *Fourteen Points*, Point XIV, 8 January 1918.
- `24` — `Every Border a Casus Belli`: Hosea 8:7, King James Version.

No factual, wording, attribution, copyright, or role-fit blocker was found in either text package. No approved-ready replacement is needed. The separate slot-23 audio recording rights hold remains a blocker for the complete League super-event package, but it does not block the quote or button text.

## Super-event 1: The League of New States, slot 23

### Exact role and fit

This is the first durable Event 006 league becoming an active diplomatic or military institution after minimum founding membership, a successful congress, charter adoption, and leadership selection. The accepted wording is broad enough for defensive, legalist, developmental, sovereign-equality, armed-liberation, and revisionist charter variants. Charter-specific tone belongs in follow-up events and dynamic league presentation, not in the single broad formation quote.

### Selected main quote

> “A general association of nations must be formed under specific covenants...”

Speaker: Woodrow Wilson.

Source work/document: *Fourteen Points*, Point XIV, in Wilson's address to Congress on war aims and peace terms.

Date: 8 January 1918.

Primary source: [Yale Avalon Project transcript](https://avalon.law.yale.edu/20th_century/wilson14.asp).

Independent corroboration: [U.S. National Archives transcript and record citation](https://www.archives.gov/milestone-documents/president-woodrow-wilsons-14-points).

Attribution confidence: High. Both pages identify the 8 January 1918 address and reproduce the Point XIV sentence beginning `A general association of nations must be formed under specific covenants`.

Rights note: The underlying 1918 historical address is public-domain material in the United States by age, and the selected excerpt is short. The source-page transcripts should not be treated as a blanket worldwide licence for unrelated page content, but no modern copyrighted work or rights-sensitive recording is used by this text package.

### Considered quote candidates

| Candidate | Verification and contextual fit | Decision |
| --- | --- | --- |
| `A general association of nations must be formed under specific covenants...` | Exact opening of Point XIV in the Yale transcript and National Archives transcript. It names the institutional act and covenant structure, directly matching a first durable league reveal without forcing one charter ideology. | **Selected.** High attribution confidence. |
| `mutual guarantees of political independence and territorial integrity to great and small states alike` | Exact continuation of Point XIV in both corroborating transcripts. It strongly supports sovereign equality, but loses the institutional action and is weaker as the sole main quote without the opening clause. | Backup fragment only. |
| Full Point XIV sentence, including `for the purpose of affording...` and `to great and small states alike` | Source-accurate and public historical text, but materially longer once the in-game attribution is added and less economical for the fixed quote box. | Not selected; retain as source context. |

The three ASCII periods are intentional. Existing static-fit evidence records that the quote box does not provide a Unicode ellipsis glyph; `...` marks the omitted source continuation without a missing-glyph risk.

### Button and cultural-remark candidates

Selected button: `Small states, one covenant.`

This is original Event 006 wording, not an external quotation. It reacts to the institutional reveal, fits all accepted league-charter variants, and echoes Point XIV's covenant/equality language without pretending to quote Wilson.

Backup button: `Great and small states alike.`

This is an exact short fragment from Point XIV and is public historical text, but it reads more like a citation fragment than a reaction and is less specific to the newly ratified league. Do not replace the selected original button without parent approval.

Modern-copyright risk: None identified. The selected button is original and the backup is a short public historical fragment.

### Implementation-ready text values

```yaml
chaosx_super_event.23.a: "Small states, one covenant."
chaosx_super_event.23.q: "\"A general association of nations must be formed under specific covenants...\"\n §Y-Woodrow Wilson, Fourteen Points, Point XIV, 8 January 1918-§!"
```

The current slot-23 title and description remain aligned with the approved broad formation role. The parent may adopt the existing current definitions directly; this handoff does not authorize a title, description, or wiring change.

UI-fit evidence retained from the current verification note: title and button fit their fixed boxes, and the quote with full attribution was estimated at four lines, about 72 px, within the approximately 79 px quote box. This is static evidence, not an integrated live-game render.

## Super-event 2: Every Border a Casus Belli, slot 24

### Exact role and fit

This is a global threat escalation in which radical or militarized Event 006 governments turn sudden sovereignty into coordinated claims, ultimatums, arms shipments, sponsorship of breakaways, and synchronized war. The wording covers the accepted offensive-league, high-chaos wave, synchronized-war, hidden-aggressive-formable, and league-sponsored-cascade trigger families. It does not fit a normal wave, ordinary election, weak consultative congress, isolated small formable, or routine border war.

### Selected main quote

> “For they have sown the wind, and they shall reap the whirlwind...”

Attribution: Hosea 8:7, King James Version.

Source: [BibleGateway, Hosea 8:7 KJV](https://www.biblegateway.com/passage/?search=Hosea%208%3A7&version=KJV).

Date or period: The canonical verse has no secure composition date needed for this attribution. The cited English translation is the King James Version, first published in 1611.

Attribution confidence: High for the cited book/chapter/verse, translation, and wording. No historical human speaker or composition date should be invented or added to the in-game attribution.

Rights note: The source page labels the KJV text `Public Domain`. The selected excerpt is short, precisely cited, and presents no modern song, film, book, or game copyright risk.

### Considered quote candidates

| Candidate | Verification and contextual fit | Decision |
| --- | --- | --- |
| `For they have sown the wind, and they shall reap the whirlwind...` | Exact beginning of Hosea 8:7 KJV. The verse's cause-to-amplified-consequence image matches governments that deliberately coordinate claims and support arrangements into a larger war system. | **Selected.** High confidence for wording and canonical attribution. |
| `they shall reap the whirlwind...` | Exact shorter fragment from the same verse. It preserves the consequence image but drops the active subject and causal setup, making it weaker for a bloc that creates the crisis. | Backup quote only. |
| Full Hosea 8:7 | Source-accurate context, but the later clauses exceed the intended quote-box economy and dilute the escalation beat. | Not selected; retain as source context. |

The source continues after `whirlwind` with a colon and further clauses. The three ASCII periods accurately mark that continuation and avoid the missing Unicode ellipsis glyph documented in the current UI-fit note.

### Button and cultural-remark candidates

Selected button: `They have sown the wind.`

This is a short allusion to Hosea 8:7 KJV, documented as an allusion rather than an independent original line. It gives the player a concise reaction to the bloc's self-created escalation and does not duplicate the quote's consequence clause.

Backup button: `They shall reap the whirlwind.`

This is an exact short KJV fragment. It emphasizes consequence but repeats the main quote's second half and is less immediate as a button reaction. Do not replace the selected button without parent approval.

Title note: `Every Border a Casus Belli` is original Event 006 wording built around the common legal phrase `casus belli`; it is not presented as a quotation.

Modern-copyright risk: None identified. The selected and backup remarks are short public-domain scriptural fragments; the title is original package wording.

### Implementation-ready text values

```yaml
chaosx_super_event.24.a: "They have sown the wind."
chaosx_super_event.24.q: "\"For they have sown the wind, and they shall reap the whirlwind...\"\n §Y-Hosea 8:7, King James Version-§!"
```

The current slot-24 title and route-neutral description remain aligned with the dangerous coordinated revisionism role. The parent may adopt the existing current definitions directly; this handoff does not authorize a title, description, or wiring change.

UI-fit evidence retained from the current verification note: title and button fit their fixed boxes, and the quote with attribution was estimated at three lines, about 54 px, within the approximately 79 px quote box. This is static evidence, not an integrated live-game render.

## Parent implementation recommendation

Keep the approved slot-23 and slot-24 `.a` and `.q` values exactly as recorded above, including ASCII `...` omission marks and compact attributions. Preserve the full source URLs and candidate rationale in the permanent super-event documentation. Keep charter-specific league tone in follow-up events unless a clean dynamic localisation branch is intentionally adopted.

Text status: **approved-ready; no replacement required; no text blocker.**

Package status: **slot 23 remains separately blocked by the accepted London Brass Players recording's United States redistribution-rights hold; that audio blocker does not authorize changing the slot-23 quote or button.**

No simplification was made within this text-research scope.
