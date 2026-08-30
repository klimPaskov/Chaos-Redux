# Event 006 super-event text and rights handoff

Research date: 2026-08-30.

Scope: bounded research for Event 006 super-event slots `23` and `24`, covering exact quote wording, attribution, role fit, button or cultural-remark options, and text-rights status. No localisation, gameplay, scripted localisation, sound, asset, spreadsheet, or source-specification file was changed.

## Status summary

- Slot `23`, **The League of New States**, remains text-approved: the Wilson Point XIV excerpt, original button, attribution, and role fit are verified, with low text-copyright risk.
- Slot `24`, **Every Border a Casus Belli**, remains wording-approved under the existing KJV selection, but its rights status is jurisdiction-sensitive: BibleGateway labels the KJV text public domain while its version information also records Crown rights in the United Kingdom.
- A rights-clean WEB wording is documented below as a backup only; the parent must explicitly approve any replacement because the Event 006 prompt says not to silently substitute the approved KJV package.
- The separate slot-`23` London Brass Players recording-rights hold remains in force and is not a text blocker. The accepted slot-`24` audio rights are documented separately and were not changed here.

## Authority and source-register crosswalk

The controlling local text authority is `docs/specs/006_independence_wave_specs/research/006_super_event_text_research.md`, with ordinary runtime identifiers confirmed by the dated text-verification notes as `23` for **The League of New States** and `24` for **Every Border a Casus Belli**.

The source register rows are `SRC-WILSON-XIV` and `SRC-HOSEA-KJV` in `docs/specs/006_independence_wave_specs/research/006_source_register.csv`.

The Event 006 super-event prompt keeps the approved title, button, quote, and audio selections authoritative and requires a documented blocker before any replacement.

## Fresh source-page checks

| Source | Verified evidence | Rights or caution |
| --- | --- | --- |
| [Yale Avalon Project, President Woodrow Wilson's Fourteen Points](https://avalon.law.yale.edu/20th_century/wilson14.asp) | The page is headed `8 January, 1918`, identifies President Woodrow Wilson's Fourteen Points, and reproduces Point XIV, including the selected association-and-covenants wording. | Use the short underlying historical excerpt, not Yale's page design or full page copy. |
| [U.S. National Archives, President Woodrow Wilson's 14 Points](https://www.archives.gov/milestone-documents/president-woodrow-wilsons-14-points) | The National Archives identifies the January 8, 1918 address to Congress and reproduces the same Point XIV sentence, independently corroborating wording and attribution. | Federal archival presentation is a stronger corroborating access point; no modern copyrighted work is being quoted. |
| [United Nations Office at Geneva, Covenant of the League of Nations](https://www.ungeneva.org/en/about/league-of-nations/covenant) | Article 10 provides a traceable 1919 treaty alternative about preserving members' territorial integrity and political independence. | Historical treaty text; it supports a defensive guarantee but not the first-act formation beat as directly as Point XIV. |
| [BibleGateway, Hosea 8:7 KJV](https://www.biblegateway.com/passage/?search=Hosea%208%3A7&version=KJV) | The page displays the exact KJV verse wording and labels the King James Version `Public Domain`. | The page's public-domain label must be read with the version-specific United Kingdom caveat below. |
| [BibleGateway, Authorized (King James) Version information](https://www.biblegateway.com/versions/Authorized-King-James-Version-AKJV-Bible/) | The version page states that rights in the KJV are vested in the Crown in the United Kingdom and that the Cambridge KJV text is reproduced by permission of Cambridge University Press. | Do not describe the KJV as unconditionally public domain worldwide. |
| [eBible, World English Bible Hosea 8](https://ebible.org/engwebp/HOS08.htm) | The WEB page gives the alternative exact sentence `For they sow the wind, and they will reap the whirlwind.` and identifies the translation as public domain. | The page is a project-host rights statement rather than a legal opinion, but it supplies a clearer worldwide-distribution basis than the KJV page. |
| [eBible, World English Bible FAQ](https://eBible.org/eng-web/webfaq.htm) | The project FAQ says the WEB may be freely used for personal or commercial purposes and has no legal monopoly controlling quotation or Bible software use. | Preserve the exact translation name and source URL if the parent later approves the WEB variant. |
| [Suetonius, Life of Julius Caesar, 1913 Loeb text at the University of Chicago](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Suetonius/12Caesars/Julius*.html) | The page identifies the 1913 Loeb Classical Library reproduction as public domain and records Caesar's reported phrase translated as `The die is cast.` | The historical report and the translated wording are high-confidence as a short allusion, but it is less specific to the sowing-and-reaping escalation than Hosea. |

## Slot 23: The League of New States

### Role and fit

Slot `23` is the first durable Event 006 league becoming an active institution after founding membership, a successful congress, charter adoption, leadership selection, and visible diplomatic or military capacity. The broad institutional wording remains suitable for defensive, legalist, developmental, sovereign-equality, armed-liberation, and revisionist charter families.

### Considered main-quote candidates

| Candidate | Source, fit, and rights | Decision |
| --- | --- | --- |
| `A general association of nations must be formed under specific covenants...` | Exact opening of Point XIV in the Yale transcript and National Archives transcript. It names the institutional act and covenant structure, directly matching the first durable league reveal. The 1918 historical speech is age-cleared historical material for the intended use; the short excerpt has low text-copyright risk. | **Selected.** Woodrow Wilson, *Fourteen Points*, Point XIV, address to Congress, 8 January 1918. Attribution confidence: high. |
| `mutual guarantees of political independence and territorial integrity to great and small states alike` | Exact continuation of Point XIV in both corroborating transcripts. It strongly supports sovereign equality, but without the opening institutional act it is weaker as the sole quote for league formation. | Backup fragment only. Attribution confidence: high. |
| `The Members of the League undertake to respect and preserve as against external aggression the territorial integrity and existing political independence of all Members of the League.` | Exact Article 10 sentence in the 1919 League Covenant at the UN Geneva source. It is a strong defensive-guarantee reference, but presupposes an already existing League and therefore reads as a later security obligation rather than the first formation moment. | Rejected for this slot; retain as a documented historical alternative. Attribution confidence: high. |

The selected excerpt's ASCII `...` is an editorial omission marker for the source continuation, not a claim that the source sentence ends there. ASCII periods are retained because the prior static UI evidence records that the current quote font lacks a Unicode ellipsis glyph.

### Selected button and remark candidates

| Candidate | Type, fit, and rights | Decision |
| --- | --- | --- |
| `Small states, one covenant.` | Original Event 006 wording. It reacts to the ratified institution, echoes Point XIV's covenant and equality theme, and has no external quotation or licensing dependency. | **Selected.** |
| `Great and small states alike.` | Exact short Point XIV fragment. It is historical and low-risk, but reads like a citation fragment rather than a reaction to the newly constituted league. | Backup only. |
| `A covenant of equals.` | Original title-like reaction that foregrounds sovereign equality, but it is less concrete and less distinctive than the selected button. | Backup only. |

### Implementation-ready current package

```yaml
chaosx_super_event.23.t: "The League of New States"
chaosx_super_event.23.a: "Small states, one covenant."
chaosx_super_event.23.q: "\"A general association of nations must be formed under specific covenants...\"\n §Y-Woodrow Wilson, Fourteen Points, Point XIV, 8 January 1918-§!"
```

The existing broad description recommendation remains the accepted text direction; this handoff does not authorize a description or localisation change.

### Slot-23 text rights verdict

Text status: **approved-ready; no text-rights blocker identified.** The underlying Wilson speech is a 1918 historical address, and the selected excerpt is short and independently corroborated by the National Archives. Yale's page footer and presentation remain separate from the public historical source text and should not be treated as a blanket licence for copying the page.

Package status: **still blocked on the separate accepted London Brass Players recording for audio ID `23`**, as recorded in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_super_event_23_audio_rights_reverification_2026-08-27.md`. This audio hold does not justify changing the Wilson quote or original button.

## Slot 24: Every Border a Casus Belli

### Role and fit

Slot `24` is reserved for a global threat escalation in which radical or militarized Event 006 governments coordinate territorial claims, ultimatums, arms shipments, sponsorship of breakaways, and synchronized wars. The wording does not fit a normal wave, ordinary election, weak consultative congress, isolated formable, or routine border war.

### Considered main-quote candidates

| Candidate | Source, fit, and rights | Decision |
| --- | --- | --- |
| `For they have sown the wind, and they shall reap the whirlwind...` | Exact beginning of Hosea 8:7 in the KJV source page. It gives a compact cause-to-amplified-consequence image for governments whose coordinated claims create a larger war system. BibleGateway labels the KJV public domain, but its version page records Crown rights in the United Kingdom, so this is U.S.-clear on the cited evidence and not unconditionally worldwide-rights-clear. | **Selected by the approved Event 006 package, subject to the jurisdiction caveat.** Attribution confidence: high for Hosea 8:7 and KJV wording. |
| `For they sow the wind, and they will reap the whirlwind.` | Exact first sentence of Hosea 8:7 in the World English Bible Protestant page. It preserves the same metaphor with a complete sentence and the eBible project states that the WEB is public domain and freely copyable. | Rights-clean backup requiring explicit parent approval because it changes the approved translation and wording. Attribution confidence: high for verse, translation, and displayed wording. |
| `The die is cast.` | Exact short translation of Caesar's reported phrase in Suetonius, *Life of Julius Caesar*, 32, in the 1913 Loeb text. It is public-domain source material and communicates an irreversible threshold, but it loses the selected quote's deliberate-action-to-consequence structure. | Rejected as the main quote; retain as a strong button backup. Attribution confidence: high for the cited page's wording, medium-high for the ancient reported saying as historical speech. |

The selected KJV excerpt's ASCII `...` marks the verse continuation after `whirlwind`; the source continues with a colon and additional clauses. It is not a source punctuation mark and should remain documented as an editorial omission marker.

### Selected button and cultural-remark candidates

| Candidate | Type, fit, and rights | Decision |
| --- | --- | --- |
| `They have sown the wind.` | Short KJV allusion to the selected verse. It gives an immediate reaction to the bloc's self-created escalation without repeating the consequence clause. The same United Kingdom Crown-rights caveat applies to the translation. | **Selected by the approved Event 006 package, subject to the jurisdiction caveat.** |
| `They shall reap the whirlwind.` | Exact short KJV fragment. It emphasizes consequence but duplicates the main quote's second half and has the same jurisdiction-sensitive rights status. | Backup only. |
| `The die is cast.` | Short public-domain-literature allusion to Suetonius's report of Caesar crossing into civil war. It is concise, rights-clean on the cited 1913 translation page, and makes the irreversible threshold legible, but it is less specific to coordinated claims than the selected Hosea allusion. | Rights-clean button backup requiring parent approval if adopted. |
| `They sow the wind.` | Short WEB allusion matching the rights-clean WEB quote variant. It is a translation change from the approved KJV button and therefore requires explicit parent approval. | Rights-clean translation backup only. |

### Implementation-ready current package

```yaml
chaosx_super_event.24.t: "Every Border a Casus Belli"
chaosx_super_event.24.a: "They have sown the wind."
chaosx_super_event.24.q: "\"For they have sown the wind, and they shall reap the whirlwind...\"\n §Y-Hosea 8:7, King James Version-§!"
```

### Rights-clean WEB alternative, not selected

If the parent requires a package with a clearer worldwide text-rights basis, the exact alternative is:

```yaml
chaosx_super_event.24.a: "They sow the wind."
chaosx_super_event.24.q: "\"For they sow the wind, and they will reap the whirlwind.\"\n §Y-Hosea 8:7, World English Bible-§!"
```

The eBible verse page states that the World English Bible is public domain, and the project FAQ states that it may be freely used for personal or commercial purposes. This is a rights recommendation only; it does not replace the approved KJV package without parent approval.

### Slot-24 text rights verdict

Text wording and attribution status: **verified.** KJV source wording is exact, the book/chapter/verse attribution is complete, and the role fit is strong.

Rights status: **U.S.-clear on the cited BibleGateway public-domain label; worldwide status requires a caveat.** The BibleGateway version-information page expressly says that KJV rights are vested in the Crown in the United Kingdom and that the Cambridge KJV text is reproduced by permission. Do not write the research record as though the KJV were unconditionally public domain in every jurisdiction, and do not rely on an unverified fair-use or fair-dealing assumption for a distributed mod.

If the intended distribution policy requires worldwide rights clearance, the WEB sentence and button are the strongest text-only alternative found in this pass. The translation switch changes approved player-facing wording, so the parent must choose it explicitly and preserve the WEB source and rights note.

## Parent implementation recommendation

1. Keep slot `23` title, original button, Wilson quote, and compact attribution exactly as approved; no text replacement is warranted.
2. Keep slot `24` title and current KJV package only if the parent accepts the documented U.S.-clear and United Kingdom Crown-rights caveat; otherwise explicitly approve the WEB variant before changing any localisation.
3. Preserve the full source URLs, source-register IDs, translation labels, and omission-marker explanation in permanent super-event documentation.
4. Keep slot-`23` audio fail-closed until a written permission or waiver covers United States and worldwide redistribution of the exact London Brass Players recording, or the parent/user explicitly reopens recording selection.
5. Do not alter audio ID `24` or its verified recording on the basis of this text-only review.

## Simplifications, omissions, and blockers

- No quote, button, title, or source was silently replaced.
- No runtime, localisation, audio, image, event, or spreadsheet change was made.
- Slot `23` remains package-blocked by the separate recording-rights hold, although its text is clear.
- Slot `24` has a translation-rights jurisdiction caveat under the approved KJV choice; the public-domain WEB variant is documented but remains unselected pending parent approval.
- No legal opinion is offered; the rights statements above are source-based distribution-risk notes.
