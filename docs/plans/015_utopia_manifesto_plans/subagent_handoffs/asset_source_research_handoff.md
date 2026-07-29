# Event 015 asset source and attribution audit handoff

> Current disposition, 2026-07-15: the quotation and audio conclusions remain current. The route-image blocker recorded later in this dated handoff is closed by the five generated 457x328 route images, their source records, runtime DDS files, and `interface/015_utopia_manifesto_super_event.gfx` registrations. The two older images remain historical assets and are not fallbacks.

Audit date: `2026-07-14`  
Role: `chaosx_asset_source_researcher`  
Scope: report/news/super-event image provenance, Thomas More quotation attribution/public-domain compatibility, and Event 015 super-event audio source/licence/uniqueness only

## Outcome

The Event 015 report image, news image, and two installed legacy super-event images have traceable OpenAI `image_gen` records. Their generated masters, exact prompts, processed previews, final DDS paths, dimensions, and source/final SHA-256 values are now tied together in `docs/assets/015_utopia_manifesto/manifest.md`.

The Thomas More quotation is accurately reproduced and attributed to Thomas More, *Utopia*, translated by Gilbert Burnet. The wording matches the closing sentence in Project Gutenberg ebook 2130, and that edition's introduction explicitly identifies Burnet's 1684 translation. More died in 1535, Burnet in 1715, and editor Henry Morley in 1894, so the quoted text and edition chain are public-domain compatible. The five current localisation entries for slots `96`-`100` all reproduce the same exact sentence and attribution.

Playback audio ID `57` is a unique, documented, compatible cue. It uses Johannes Brahms's *Symphony No. 3 in F major, Op. 90*, III. *Poco allegretto*, performed by the Musopen Symphony Orchestra. The specific Commons recording is dedicated under CC0 1.0 Universal. The source master, frozen Commons page, structured metadata, CC0 deed, CC0 legal code, final WAV, and Event 015 WAV mirror are all present and checksum-backed. The HTML music catalogue now contains the missing active row.

The overall super-event visual package is incomplete. Five route-specific sprites are registered and selected for display slots `96`-`100`, but none of their generated source PNGs or runtime DDS files exists. The two installed legacy super-event images are not accepted as fallbacks.

## Image provenance evidence

Source mode for all four installed images below: fictional OpenAI `image_gen` output with no internet image, archival photograph, real-person likeness, or third-party character reference.

Canonical records:

- prompts: `docs/assets/015_utopia_manifesto/prompts/generated_event_art_prompts.md`
- processing handoff: `docs/assets/015_utopia_manifesto/generated_event_art_handoff.md`
- source and checksum ledger: `docs/assets/015_utopia_manifesto/manifest.md`

| Asset | Source SHA-256 | Final DDS SHA-256 | Disposition |
| --- | --- | --- | --- |
| `report_event_utopia_manifesto_found` | `18aceefe049b6f842d695cdf95d7588b319ced45699801f0115dbdb1018fead3` | `36783e46587bd593716140ebeb15b0eecfcc86b0f5e1dfed5d610b132592a86a` | installed and currently used |
| `news_event_utopia_boundary_crisis` | `734958fe691ccc4ac116e003635f6147dd19c6ae1c2b480d7f4c026075ba526e` | `7c4a7fa5ee44eb2ddd1f2d08fac3ce59958b09c701a51ff44669a54ddc79d7be` | installed and registered; no current event call found in this audit |
| `super_event_utopia_new_utopia` | `5fddc71b2a5a8aaf4b5f5f2a406f199b614fc7d99b4a403037d3644801ff5f81` | `06606c3b38feaac7823bebdcaaa94a678efabdf0d7ac2c38463f1ddbebb954d4` | installed legacy image; not selected by current slots |
| `super_event_utopia_marked_bounds` | `5d57fd6b9d3d39618a1a0e1cafacdd7f406ab4137fbafbc33b7bea9023f16802` | `b58b7157af42943d38f1a7327bbf24ae5a365d4bfb63c182c5a5baea3df44ed9` | installed legacy image; not selected by current slots |

The source and final hashes above were recalculated from the current files and match the new manifest rows. Source and processed dimensions also match the handoff: report `1369x1149 -> 210x176`, news `2020x778 -> 397x153`, New Utopia `1479x1063 -> 457x328`, and Marked Bounds `1479x1064 -> 457x328`.

## Quotation evidence

Current localisation wording:

> However, there are many things in the commonwealth of Utopia that I rather wish, than hope, to see followed in our governments.

Attribution: Thomas More, *Utopia*, translated by Gilbert Burnet.

Evidence:

- primary text and translation statement: <https://www.gutenberg.org/files/2130/2130-h/2130-h.htm>
- Project Gutenberg catalogue record: <https://www.gutenberg.org/ebooks/2130>
- independent bibliographic cross-check identifying Burnet as translator and Morley as editor: <https://onlinebooks.library.upenn.edu/webbin/gutbook/lookup?num=2130>
- canonical repo research note: `docs/super_events/015_utopia_manifesto/text_research.md`

The quote is exact, not paraphrased or modernized. The source page identifies Burnet's translation and Project Gutenberg marks ebook 2130 public domain in the United States. The author, translator, and editor death dates also place this text beyond ordinary life-plus-70 terms. No quote-source or attribution blocker remains.

## Audio rights, identity, and uniqueness evidence

Selected recording:

- work: Johannes Brahms, *Symphony No. 3 in F major, Op. 90*, III. *Poco allegretto*
- performer/source author: Musopen Symphony Orchestra
- live source page: <https://commons.wikimedia.org/wiki/File:Brahms,_Symphony_No._3_in_F_Major,_Op._90_-_III._Poco_allegretto.ogg>
- frozen source revision: <https://commons.wikimedia.org/w/index.php?title=File:Brahms,_Symphony_No._3_in_F_Major,_Op._90_-_III._Poco_allegretto.ogg&oldid=956414568>
- recording licence: <https://creativecommons.org/publicdomain/zero/1.0/>
- licence legal code: <https://creativecommons.org/publicdomain/zero/1.0/legalcode.en>
- composition: public domain; Brahms died in 1897
- recording: file-specific CC0 1.0 Universal, including related and neighbouring rights to the extent allowed by law
- attribution condition: none; courtesy credit retained

Identity chain:

- preserved source: `docs/super_events/source_audio/015_utopia_manifesto/brahms_symphony_3_iii_poco_allegretto_musopen_cc0_original.ogg`
- Commons size and SHA-1: `8,770,243` bytes; `38f129111cb55461c7749a52b7ac608a13709b11`
- preserved source SHA-256: `ba1db2035d78954d5f15711594817ccceaa730bd83df68734cb724a2e3ba32df`
- final WAV: `sound/015_utopia_manifesto/super_event_57_utopia_has_neighbors.wav`, `116.000000 s`, stereo, `44,100 Hz`, SHA-256 `68ebdcb9a4d81ca9863e85344fc19ab1ad99ffb7e83c836691d7a92181bfd1b9`
- final WAV mirror: `sound/015_utopia_manifesto/super_event_57_utopia_has_neighbors.wav`, `116.000000 s`, stereo PCM s16le, `44,100 Hz`, SHA-256 `05da5a30ba49c6592e5295dd499e9ad3e97279586bb7e7d51228ad236ce58655`
- embedded OGG tags name the title, performer, composer, Event 015, CC0 licence, Commons source, and edit interval

Runtime/catalog identity:

- playback audio ID: `57`
- display slots using it: `96`-`100`
- six Event 015 sound wrappers point only to the Event 015 OGG
- six Event 015 sound wrappers point only to the Event 015 WAV base sound
- `utopia_manifesto_emit_regional_proclamation` assigns audio ID `57` before settings-aware playback
- `music/chaosx_music_track_list.html` has one Event 015 row for playback audio ID `57`, with source, performer, CC0 link, duration, edit notice, and display-slot use

Uniqueness checks:

- all `54` OGG files under `music/` were container-hash checked; only the Event 015 OGG has its SHA-256
- exact first-20-second Chromaprint scan of all `54` OGGs returned one match: the Event 015 OGG
- exact first-20-second Chromaprint scan of all `52` WAVs under `sound/` returned one match: the expected Event 015 WAV mirror
- repository-wide title, source, filename, helper, wrapper, and audio-ID searches found no mapping to another event
- Event 018 uses a different Brahms work, Symphony No. 1, movement I, with a different source and derivative; it is not a reuse of the Event 015 track

No audio-source, licence, attribution, format, identity, or reuse blocker remains.

## Exact unresolved blocker

The five current route-specific images have prompt briefs but no source, processed, package, or runtime files:

| Slot | Required sprite | Missing runtime DDS |
| --- | --- | --- |
| `96` | `GFX_super_event_015_consent_of_households` | `gfx/super_events/015_utopia_manifesto/super_event_015_consent_of_households.dds` |
| `97` | `GFX_super_event_015_common_table` | `gfx/super_events/015_utopia_manifesto/super_event_015_common_table.dds` |
| `98` | `GFX_super_event_015_guardians_of_measure` | `gfx/super_events/015_utopia_manifesto/super_event_015_guardians_of_measure.dds` |
| `99` | `GFX_super_event_015_closed_island` | `gfx/super_events/015_utopia_manifesto/super_event_015_closed_island.dds` |
| `100` | `GFX_super_event_015_joke_understood` | `gfx/super_events/015_utopia_manifesto/super_event_015_joke_understood.dds` |

Required resolution for each image:

1. Generate one distinct master from the recorded prompt in `docs/assets/015_utopia_manifesto/prompts/generated_event_art_final_prompts.md`.
2. Preserve the generated master in `docs/assets/015_utopia_manifesto/source_png/`.
3. Process a `457x328` preview, export the matching runtime DDS, and keep sprite/path names exactly as registered.
4. Add a prompt-linked manifest row with source and final checksums.

No fallback, placeholder, legacy-image substitution, or unverified source is approved.

## Files changed

- `docs/assets/015_utopia_manifesto/manifest.md`
  - added the non-icon generated-source/checksum ledger
  - distinguished installed legacy super images from current route sprites
  - recorded the five prompt-only route image blockers
- `docs/assets/015_utopia_manifesto/generated_event_art_handoff.md`
  - added generated-source provenance and current route-image status
- `docs/assets/015_utopia_manifesto/prompts/generated_event_art_final_prompts.md`
  - clarified that prompt text is not generation evidence
- `docs/super_events/015_utopia_manifesto/audio_research.md`
  - reconciled current WAV integration, hashes, runtime keys, catalogue row, and uniqueness scan
- `docs/super_events/super_event_audio_packages.md`
  - added the active Event 015 audio package with source, CC0 rights, paths, checksums, edit record, slots, audio ID, and uniqueness status
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/super_event_audio_researcher_handoff.md`
  - added a current integration/source re-audit that supersedes proposal-era pending language
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/super_event_text_researcher_handoff.md`
  - recorded current localisation integration and primary-text recheck
- `docs/events/015_utopia_manifesto/overview.md`
  - replaced the stale two-super-event account with display slots `96`-`100`, audio ID `57`, source records, and the exact image blocker
- `docs/specs/015_utopia_manifesto_specs/handoffs/unresolved_verification_blockers.md`
  - replaced stale claims that no art/text/audio existed with the current resolved and unresolved state
- `music/chaosx_music_track_list.html`
  - added the missing playback audio ID `57` source/licence row
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/asset_source_research_handoff.md`
  - created this handoff

## Scope boundaries and validation

No gameplay, localisation, scripted localisation, interface/GFX, audio binary, image binary, spreadsheet, or icon-owned manifest row was changed.

Meaningful validation performed:

- recalculated and matched every documented source-image and final-DDS checksum
- verified all documented image dimensions from the current files
- checked all five current route DDS paths and confirmed they are absent
- rechecked the More sentence and Burnet attribution against the primary text
- recalculated the source-audio, OGG, WAV, and frozen-evidence hashes
- decoded and profiled the source, OGG, and WAV with FFprobe
- verified six music definitions, six sound wrappers, one station entry, one catalogue row, and the Event 015 audio constant
- ran repository-wide WAV hash and Chromaprint uniqueness scans

No commit was created. The five-file route-image blocker prevents a clean overall super-event completion claim, and most Event 015 documentation surfaces in this handoff were already untracked shared-plan outputs. The parent should review and commit the integrated Event 015 plan without folding unrelated concurrent changes into this bounded audit.

## Simplifications, omissions, and blockers

- Simplifications: none.
- Fallbacks: none.
- Omitted requested audit surfaces: none.
- Remaining blocker: the five route-specific super-event source/processed/DDS/checksum packages listed above.
