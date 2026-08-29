# Event 006 super-event text re-check

Research date: 2026-08-24.

Mode: bounded source, attribution, role-fit, and wording audit only. No localisation, event, super-event wiring, audio, asset, spreadsheet, or source-specification file was changed.

## Current verdict

Preserve the accepted ordinary slots and text packages:

- `23` — **The League of New States**: Woodrow Wilson, *Fourteen Points*, Point XIV, 8 January 1918.
- `24` — **Every Border a Casus Belli**: Hosea 8:7, King James Version.

No factual, attribution, copyright, or role-fit blocker was found in either text package. The 2026-08-06 authority reconciliation still identifies `23` and `24` as the current ordinary runtime identifiers. The 2026-08-22 slot-23 audio re-verification changes no text verdict: its separate recording-rights hold remains active, and no replacement audio or text is authorized without parent approval.

## Selected implementation package

```yaml
chaosx_super_event.23.a: "Small states, one covenant."
chaosx_super_event.23.q: "\"A general association of nations must be formed under specific covenants...\"\n §Y-Woodrow Wilson, Fourteen Points, Point XIV, 8 January 1918-§!"
chaosx_super_event.24.a: "They have sown the wind."
chaosx_super_event.24.q: "\"For they have sown the wind, and they shall reap the whirlwind...\"\n §Y-Hosea 8:7, King James Version-§!"
```

The three ASCII periods are intentional. The earlier text verification recorded that the current quote font lacks a Unicode ellipsis glyph; the omission marks also make clear that both displayed excerpts continue in their sources.

## Main quote candidates and evidence

### Slot 23 — The League of New States

| Candidate | Evidence and fit | Verdict |
| --- | --- | --- |
| `A general association of nations must be formed under specific covenants...` | Exact opening of Point XIV in the Yale Avalon transcript and the National Archives transcript. Wilson delivered the address to Congress on 8 January 1918. It directly names an association formed by covenants and therefore fits the first durable league/institutional reveal without forcing a charter ideology. | **Selected. High attribution confidence.** |
| `mutual guarantees of political independence and territorial integrity to great and small states alike` | Exact Point XIV continuation. It gives the strongest sovereign-equality emphasis, but loses the institutional action and is less natural as the main quote without the preceding clause. | Backup fragment only. |
| Full Point XIV sentence | The full sentence is source-accurate and public historical text, but is materially longer than the accepted excerpt and risks the fixed quote box once attribution is added. | Not selected; retain only as source context. |

Source and provenance:

- Primary text: [Yale Avalon Project, President Woodrow Wilson's Fourteen Points](https://avalon.law.yale.edu/20th_century/wilson14.asp). The page labels the document `8 January, 1918` and reproduces Point XIV verbatim.
- Primary corroboration: [U.S. National Archives, President Woodrow Wilson's 14 Points](https://www.archives.gov/milestone-documents/president-woodrow-wilsons-14-points). The page identifies Wilson's 8 January 1918 address to Congress and reproduces Point XIV.
- Catalog corroboration retained by the earlier note: [Library of Congress, Address of President Wilson to Congress](https://www.loc.gov/item/18026102/). A direct request was Cloudflare-blocked in this pass, so the Yale and National Archives pages carry the wording/date verdict.
- Speaker: Woodrow Wilson. Work/document: *Fourteen Points*, Point XIV. Date: 8 January 1918; delivered as an address to Congress in Washington, D.C.
- Attribution confidence: **High**. The wording, speaker, document, point number, and date are independently traceable.
- Rights: 1918 historical address and short excerpt are public-domain material in the United States; no modern copyrighted text is involved.

### Slot 24 — Every Border a Casus Belli

| Candidate | Evidence and fit | Verdict |
| --- | --- | --- |
| `For they have sown the wind, and they shall reap the whirlwind...` | Exact opening of Hosea 8:7 KJV. The verse links deliberate conduct to amplified consequences, matching coordinated claims, sponsorship, ultimatums, and synchronized war. | **Selected. High confidence for book/chapter/translation and wording.** |
| `they shall reap the whirlwind...` | Exact shorter fragment from the same verse. It preserves the consequence image but drops the causal subject and is therefore weaker for a bloc that actively creates the crisis. | Backup quote only. |
| Full Hosea 8:7 | Exact source context, but the remaining clauses exceed the intended quote-box economy and would dilute the escalation beat. | Not selected; retain only as source context. |

Source and provenance:

- Text and translation: [Bible Gateway, Hosea 8:7, King James Version](https://www.biblegateway.com/passage/?search=Hosea%208%3A7&version=KJV). The page displays the exact verse and labels the KJV text `Public Domain`.
- Attribution: Hosea 8:7, King James Version. Attribution confidence: **High** for the cited canonical reference, translation, and wording.
- Date: no secure composition or redaction year is supplied by the source; no date should be added to the in-game attribution.
- Rights: the KJV is identified as public domain on the source page; the selected excerpt is short and presents no modern copyright risk.

## Cultural remark/button candidates

### Slot 23

| Candidate | Provenance and fit | Verdict |
| --- | --- | --- |
| `Small states, one covenant.` | Original Event 006 wording, not presented as an external quotation. It reacts to the institutional reveal, keeps the charter/covenant motif, and fits the defensive, legalist, sovereign-equality, and developmental variants. | **Selected.** |
| `Great and small states alike.` | Short exact fragment from Wilson Point XIV, with the same public-domain source as the quote. It foregrounds equality but is less specific to the newly ratified league and reads more like a citation fragment than a reaction. | Source-backed backup only; do not replace without parent approval. |

### Slot 24

| Candidate | Provenance and fit | Verdict |
| --- | --- | --- |
| `They have sown the wind.` | Short allusion to Hosea 8:7 KJV. It is not claimed as an independent original line, and it gives the button a concise warning/reaction to the bloc's self-created escalation. | **Selected.** |
| `They shall reap the whirlwind.` | Exact KJV fragment from Hosea 8:7. It emphasizes consequence, but is less immediate as a reaction than the accepted cause-to-consequence setup and repeats the main quote's second half. | Source-backed backup only; do not replace without parent approval. |

No modern song, film, book, game, or other copyrighted work is used. The slot-23 button is original; the slot-24 button is a short, clearly documented public-domain scriptural allusion.

## Current handoff and blocker reconciliation

- `super_event_research/006_super_event_text_verification.md` remains the strongest text authority: it records the corrected broad-role descriptions, high-confidence source checks, and estimated fixed-box fit. Its description corrections remain parent-adoption work and are not silently changed here.
- `subagent_handoffs/006_super_event_text_research_handoff.md` remains aligned: no quote or button replacement was required, and parent ownership of final localisation and wiring is unchanged.
- `subagent_handoffs/006_super_event_research_authority_reconciliation_2026_08_06.md` confirms the ordinary runtime IDs `23` and `24` and records that accepted text selections were unchanged.
- `subagent_handoffs/006_super_event_23_audio_reverification_v117_2026_08_22.md` confirms that slot `23` still has a separate accepted-recording redistribution blocker. It does not weaken the slot-23 text provenance and does not authorize replacing the quote/button package.
- Earlier static-fit evidence remains usable but is not a fresh integrated render: the Wilson quote was estimated at about 4 lines/72 px and the Hosea quote at about 3 lines/54 px in the fixed quote box; both buttons were recorded as fitting.

## Parent implementation recommendation

Keep the accepted `.a` and `.q` values, preserve the exact source attributions in permanent research documentation, and use ASCII `...` in the runtime quote strings. Do not reopen candidate selection or add a replacement for slot `23` unless the parent explicitly approves a new text/audio package. The text package is unblocked; overall slot-23 super-event completion remains blocked only by the separately documented audio-rights and wiring hold.
