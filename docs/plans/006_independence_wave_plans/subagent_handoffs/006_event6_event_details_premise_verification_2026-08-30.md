# Event 006 Event Details premise verification

Date: 2026-08-30 (Europe/Kyiv).

## Scope and result

This localisation-only verification reviewed the Event 006 Event Details premise after a stale audit reported exact Join thresholds and rival-compact ledger text near the shared GUI localisation key.

No localisation edit was required. Commit `7ac9c82c4` (`docs(event006): keep details premise-only`) already applied the accepted correction, and the current checkout retains it at `localisation/english/chaosx_gui_l_english.yml:1090`.

The key `chaosx.events_log.window.event_details.independence_wave` currently reads:

> New governments have taken control of capitals, ministries, and borders across several regions. Their leaders must turn sudden sovereignty into functioning states while former hosts, neighboring powers, and rival movements decide whether to recognize or challenge them.
>
> Every new government faces the same unsettled question: can it secure a place in the world before old borders, unfinished claims, and competing visions of independence pull the wave apart?

This is the accepted two-paragraph, premise-only text. It contains no exact Join thresholds, automatic-wave counts, rival-compact ledger values, package or formable IDs, raw constants, implementation labels, or hidden route mechanics.

## Old-to-current intent

The superseded wording exposed the Join eligibility threshold through `constant:independence_wave_join.*` tokens and appended `[GetIndependenceWaveRivalBlocEventDetails]` plus `[GetIndependenceWaveRivalBlocEventDetailsMember]`, which displayed the rival compact's numeric ledger. The accepted current wording replaces those mechanics with the public situation: new governments hold capitals and borders, struggle to establish functioning states, and face recognition, former-host, border, and rival pressures.

No further rewrite was made because it would replace already accepted wording and create a new mismatch with the workbook source pending a separate spreadsheet-owner update.

## Selector and related-surface review

- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:6561` maps Event 006 directly to `chaosx.events_log.window.event_details.independence_wave`.
- The Event 006 detail key no longer invokes either rival-compact getter.
- `GetIndependenceWaveRivalBlocEventDetails` and `GetIndependenceWaveRivalBlocEventDetailsMember` remain defined in `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`, and their ledger strings remain in `localisation/english/006_independence_wave_rival_bloc_l_english.yml`. They are not consumed by the current Event 006 premise and were left unchanged because dedicated status and mechanical surfaces are outside this task.
- The generic Event Details metadata keys remain shared framework text and were not changed.
- The read-only workbook alignment handoff `006_event6_catalog_alignment_probe_2026-08-30.md` confirms that `Events!C7` exactly matches the current localisation key. The workbook and generated CSVs were not edited.

## Localisation audit lists

- Missing keys: none in the inspected Event 006 Event Details selector path.
- Duplicate keys: none for `chaosx.events_log.window.event_details.independence_wave`.
- Scripted localisation issues: none in the current Event 006 detail selector. The rival-compact getters remain defined but are no longer appended to this premise.
- Dynamic text opportunities: none appropriate for the premise-only field. Exact thresholds and ledgers belong on their existing mechanical or status surfaces.
- Cross-surface mismatches: none between the current Event 006 key and `Events!C7`. The 2026-08-29 localisation audit statement that the aligned text still includes both rival-compact selectors is stale and is superseded by commit `7ac9c82c4`, the 2026-08-29 premise repair handoff, and the 2026-08-30 catalog alignment probe.
- File encoding concerns: none. `chaosx_gui_l_english.yml` begins with the UTF-8 BOM bytes `EF BB BF`.
- Sourced quotations: none appear on the inspected Event 006 Event Details surface, so no quotation wording or attribution was altered.

## Prose-quality review

- Vagueness: the current text identifies governments, capitals, ministries, borders, former hosts, neighboring powers, and rival movements. No vague institutional placeholder requires repair.
- Bloat: the current premise is two short paragraphs and does not enumerate mechanics or repeat its setup.
- Obvious explanation: the text does not explain the Event Details UI, its button, or visible metadata.
- Repetition: no sentence restates the title or repeats the same consequence.
- Overcomplication: the text uses familiar language and keeps each sentence focused on one public situation.
- Style-rule repair: the current text contains no em dash, sentence semicolon, staccato chain, staged contrast, AI-style process wording, or implementation history.

## Meaningful validation

- `git show HEAD:localisation/english/chaosx_gui_l_english.yml` confirms that the accepted premise is already committed at HEAD rather than existing only as an uncommitted shared-worktree edit.
- `git log -S "Every new government faces the same unsettled question" -- localisation/english/chaosx_gui_l_english.yml` identifies `7ac9c82c4` as the correction commit.
- Targeted source searches found no Join constants, rival-compact getters, implementation IDs, or numeric ledger tokens inside the current Event 006 detail value.
- A read-only `hoi4.event_inspect` trace for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51f1ee5a58812b17011e0d7a0ab8c0d0ed5003c99d6261e3148aa954b581ffdf/aef4b0a1e8bd78dd60c7c78bc751641e4ccc39e6bff3dc02652e735a8a65dd72/event-trace-d4de198c1706.json`. This is source-linked chain evidence and not a live-runtime claim.

## Skipped or blocked validation

The first event-inspection request was rejected because the selector required `{ kind = event, eventId = ... }`; the corrected request completed as recorded above.

The required production GUI route did not produce a current artifact. `hoi4.gui_inspect` for `events_log_popup_window` with the Event 006 review scenario timed out after 180 seconds. A narrower retry for `events_log_event_details_window` also failed to return within the bounded wait and was terminated without an artifact. Therefore this handoff does not claim current production-render proof for wrapping, clipping, overflow, or in-game selection of the Event 006 text. The source-only checks are not treated as equivalent visual evidence.

## Changed files and keys

- Changed file: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_event_details_premise_verification_2026-08-30.md`.
- Changed localisation keys: none. The required correction already exists in commit `7ac9c82c4`.
- Dynamic localisation added or fixed: none.
- Gameplay or display behavior changed: none.

The shared localisation file has unrelated concurrent edits elsewhere in the working tree. It was not staged or modified by this verification.

## Unresolved decisions, blockers, and simplifications

No wording decision remains for the Event 006 premise, and no fallback or simplification was introduced. Current GUI render evidence remains blocked by the timeouts above. Whole-event completion and unrelated Event 006 mechanics remain outside this bounded task.
