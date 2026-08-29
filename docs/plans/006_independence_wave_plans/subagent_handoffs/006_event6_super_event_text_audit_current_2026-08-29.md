# Event 006 super-event text audit and handoff

Audit date: 2026-08-29.

Scope: bounded Event 006 super-event text, source, attribution, role-fit, UI-fit, and documentation audit. This pass did not edit gameplay, event effects, scripted localisation, super-event wiring, audio, assets, portraits, spreadsheets, or source specifications. It did not perform live-game validation.

## Current verdict

Preserve the approved ordinary slots and text packages exactly:

- `23` — **The League of New States**: Woodrow Wilson, *Fourteen Points*, Point XIV, 8 January 1918.
- `24` — **Every Border a Casus Belli**: Hosea 8:7, King James Version.

No factual, wording, attribution, copyright, or role-fit blocker was found in either text package. The current Event 006 localisation audit reports that the runtime quote strings match the implementation-ready values at `localisation/english/006_independence_wave_l_english.yml:115` and `:119`; no localisation patch is required in this tranche.

The only remaining blocker relevant to the super-event package is slot `23` audio. The accepted London Brass Players recording remains uncleared for United States/worldwide redistribution, so audio ID `23`, its wrappers, and its firing assignment must remain absent. This does not authorize a replacement quote, button, title, description, or recording.

## Source verification

The [Yale Avalon Project transcript of Woodrow Wilson's Fourteen Points](https://avalon.law.yale.edu/20th_century/wilson14.asp) identifies the 8 January 1918 document and reproduces Point XIV, including `A general association of nations must be formed under specific covenants for the purpose of affording mutual guarantees of political independence and territorial integrity to great and small states alike.`

The [U.S. National Archives record for Wilson's 14 Points](https://www.archives.gov/milestone-documents/president-woodrow-wilsons-14-points) identifies the January 8, 1918 address to Congress and independently reproduces the same Point XIV wording.

The [BibleGateway Hosea 8:7 KJV page](https://www.biblegateway.com/passage/?search=Hosea%208%3A7&version=KJV) displays `For they have sown the wind, and they shall reap the whirlwind: it hath no stalk; the bud shall yield no meal: if so be it yield, the strangers shall swallow it up.` and labels the King James Version text public domain.

Attribution confidence is **high** for both selected packages. The Wilson speaker, work, point number, date, and wording are corroborated by two archival sources. The Hosea book/chapter/verse, translation, and wording are precise; no uncertain human speaker or composition date is added.

## Approved implementation package

```yaml
chaosx_super_event.23.t: "The League of New States"
chaosx_super_event.23.d: "Delegates from the newest states have ratified a common charter and chosen the league's leadership. The signatories promise arbitration, mutual aid, and collective resistance to any former host or foreign patron that attempts to extinguish a member.\n\nThe league can speak for its members, bargain in their name, and coordinate shared aid or mobilization."
chaosx_super_event.23.a: "Small states, one covenant."
chaosx_super_event.23.q: "\"A general association of nations must be formed under specific covenants...\"\n §Y-Woodrow Wilson, Fourteen Points, Point XIV, 8 January 1918-§!"
chaosx_super_event.24.t: "Every Border a Casus Belli"
chaosx_super_event.24.d: "New-state governments coordinate claims, ultimatums, arms shipments, and mobilization schedules across several regions. Their border commands follow shared timetables, and governments pledge arms or troops to support one another's territorial demands.\n\nFormer hosts reinforce several fronts as they prepare for wars that may begin on the same day."
chaosx_super_event.24.a: "They have sown the wind."
chaosx_super_event.24.q: "\"For they have sown the wind, and they shall reap the whirlwind...\"\n §Y-Hosea 8:7, King James Version-§!"
```

The three ASCII periods are intentional omission marks. The current quote font lacks a Unicode ellipsis glyph, and the marks show that the source continues after the displayed excerpt.

## Candidate comparison

### Slot 23 quote and button

The selected Wilson opening names an association formed under covenants and therefore fits the first durable league reveal without forcing a defensive, developmental, sovereign-equality, armed-liberation, or revisionist charter variant.

The exact continuation `mutual guarantees of political independence and territorial integrity to great and small states alike` is a source-backed backup fragment, but it loses the institutional action. The full Point XIV sentence is source-accurate and public historical text, but is too long for the fixed quote box after attribution.

The selected button `Small states, one covenant.` is original Event 006 wording. The source-backed backup `Great and small states alike.` is less specific to the new institution and reads more like a citation fragment.

### Slot 24 quote and button

The selected Hosea opening preserves both deliberate action and amplified consequence, matching coordinated claims, sponsorship, ultimatums, and synchronized war.

The exact backup `they shall reap the whirlwind...` preserves the consequence image but drops the active subject and causal setup. The full verse is source-accurate but too long for the intended quote-box economy.

The selected button `They have sown the wind.` is a short public-domain scriptural allusion. The backup `They shall reap the whirlwind.` repeats the quote's consequence clause and is less immediate as a reaction.

No modern copyrighted song lyric, film line, book line, or game dialogue is used. The slot-23 button and both descriptions are original package text, while the slot-24 button is documented as a short KJV allusion.

## Runtime and documentation handoff

The permanent research authority is [docs/super_events/006_independence_wave/research.md](../../../super_events/006_independence_wave/research.md). It now records the exact text package, candidate comparison, source URLs, confidence, rights notes, UI-fit evidence, and the no-substitute slot-23 audio blocker.

The current runtime state remains:

- Slot `23`: image/text dispatch registered; audio ID `23`, wrappers, and firing absent while the accepted London Brass Players recording is rights-blocked.
- Slot `24`: image, text, audio, wrapper, and factual predicate source-wired; end-to-end reachability remains partial under Event 006 package and league gates.

The main agent should retain the current localisation values, preserve the exact Wilson and Hosea quotations including ASCII `...`, and carry the slot-23 audio-rights blocker into the overall completion report. No runtime text or wiring change is recommended by this audit.

## Simplifications, omissions, and blockers

No simplification was made within the assigned text scope. No quote, button, title, description, or audio replacement was invented or substituted.

The accepted slot-23 recording remains blocked for United States/worldwide redistribution. Candidate recordings remain research-only and require explicit parent/user approval, human audition, and rights/attribution review before any production use.

Integrated live rendering was not performed or claimed. Existing static UI-fit evidence remains the basis for the quote-box recommendation, and the current localisation audit supplies the runtime string-match evidence.
