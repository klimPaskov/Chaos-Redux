# Event 027 Doctrine Research postfix completion audit — 2026-08-30

> **Superseded status notice (2026-09-01):** This dated completion audit is preserved as historical evidence and is superseded as a current status authority by ../documentation_state.md. Its broad findings and dated MCP artifact references do not replace the current ledger.

## Audit result

**Overall status: BLOCKED — source-playable, but not acceptance-complete.**

The current Event 027 implementation has a playable source path for global firing, per-country batches, human choices, silent AI resolution, doctrine adoption, native mastery adapters, evolutions, Event History, Event Details, achievements, assets, and catalog registration. The postfix presentation and History fixes are present. The requested 107-item mappings and native calls are present exactly.

Acceptance completion is not granted because required native doctrine, persistence, lifecycle, probability, comparison, visual-consumer, evolution-timing, and achievement scenario evidence remains unavailable. One achievement requirement is also not implemented exactly in source: First Lesson records batch-start empty-domain snapshots but does not consult them when awarding the achievement.

This was a read-only audit. No gameplay, localization, asset, spreadsheet, specification, or existing handoff was edited. The only file written is this handoff.

## Final audited source identity

The live source was re-read after all concurrent parent updates, including the final Special Forces dual-track guard.

| Surface | SHA-256 |
| --- | --- |
| `events/027_doctrine_research.txt` | `08946d48e168ff2e4b90a7e12642bba5c1712bf527f04c70399bbb79c48ff703` |
| `common/scripted_effects/027_doctrine_research_effects.txt` | `5bcfdee0d17e503ffcd46e0d6fb3cb722d867146d7e5088b22541e5a7c2e0734` |
| `common/scripted_effects/027_doctrine_research_ai_effects.txt` | `64fcc4f2a0b18fe8e337a1f928b1819ff08f3d0cd7a043c5f6c20cecfb248616` |
| `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt` | `4d99cfb34b38124961bfd153acebac21c6ca2106369a2445bad88ec605495e46` |
| `common/scripted_triggers/027_doctrine_research_triggers.txt` | `11fbe721afeddbcf1df9f9f3ff7656aed22e8d1e12b11d2fd3660cd041330fc2` |
| `localisation/english/027_doctrine_research_l_english.yml` | `c709a8a1d0a5c279bb1d459f3cad8f426f3368676571c2d1da407ab09494344a` |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | `ebf20975c1fba51dc68cccbc0dfbae62c7805683464a24f2422cfdc9825b972e` |

The final Event MCP revision is `02410b498829a4d0ecf4f00b3bed6568cc73bd9f994fc2ec3f4fa23bf4e75706`, graph hash `149cd6a3748d8b891a746c11add205380c8e69e16acf5bfc5b2525a7ae7bafed`.

The final weighted-source MCP revision is `58e1d29224321ff432d9ace0767594619db0e7b3d56eecf8798690af0aaaae1`, source hash `1cfd3c27a7bf4b57d6d28cc53f72e8e14145d47f1b01556581aae9e80cdebf27`.

## Completion status by surface

| Surface | Source status | Acceptance status | Audit disposition |
| --- | --- | --- | --- |
| Root firing and 1/2/3/4/5-choice batches | Finished | Partial | Root and evolution-sized firing profiles are wired; runtime fanout and timing traces remain missing. |
| Human event chain and pagination | Finished | Partial | `.1`–`.12` and `.60`–`.77` are present; standard-popup clipping and complete pagination consumer proof remain missing. |
| Native doctrine adoption/mastery adapters | Finished in source | Blocked | Exact call inventory exists, but native one-step, banked mastery, completion, and save/reload behavior lack accepted doctrine/runtime evidence. |
| Special Forces | Pass with limitation in source | Blocked for final acceptance | The final dual-track rule fails closed safely; technology/runtime proof remains unavailable. |
| AI resolution | Finished in source | Blocked | Scoring and exhausted closure are wired; no resolved probabilities or accepted named-scenario outcomes exist. |
| Queues and receipts | Finished in source | Blocked | Alignment and parent-link validation exist; interrupted native transactions deliberately quarantine because durable recovery proof is absent. |
| Controller lifecycle | Partial | Blocked | Prompt latching and documented lifecycle callbacks exist; pure tag switch and arbitrary human/AI controller transitions remain unproven and have no dedicated callback. |
| Localization and dynamic status | Finished | Partial | Mechanical coverage and postfix prose pass source review; final rendered consumer presentation remains unproven. |
| Event History and Event Details | Finished in source | Partial | Actorless payload and exact 1–5 History variants are wired; final shared-UI consumer evidence remains missing. |
| Evolutions | Finished in source | Partial | Four stages, actorless records, and 90-day source pacing exist; accepted timing and presentation traces are missing. |
| Achievements | Partial | Blocked | Definitions, flags, tracking, localization, and icons exist; First Lesson omits its batch-start-empty check and no positive/negative runtime matrix is accepted. |
| Assets | Finished | Partial acceptance | Final DDS files and wiring are complete; consumer screenshots are still absent. |
| Cluster 9 | Event 027 member finished | Intentionally partial | Event 027 is registered as an optional Medium member; IDs 54, 65, 67, 83, 85, and 89 remain unreworked. |
| Documentation and catalog | Mostly finished | Partial | Overview and XLSX/export rows are current; `mcp_evidence.md` and older audits contain superseded revision/prose findings. |

## Exact requested invariants

### 107 dynamic option-status mappings — pass

`localisation/english/027_doctrine_research_l_english.yml` contains exactly 107 unique `GetDoctrineResearchOptionStatus*` references. `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt` contains exactly 107 unique matching `defined_text` names. The set difference is empty in both directions.

These are track-qualified mappings, including separate First and Second Special Forces page mappings even where vanilla reuses the same underlying token.

### 107 native mastery and installation calls — pass in source

`common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt` contains exactly:

- 107 `add_mastery = { ... }` calls;
- 107 `set_sub_doctrine = { ... }` calls.

The call inventories cover the same 107 track-qualified adapter rows. There are 99 unique native subdoctrine tokens because vanilla's eight Special Forces tokens are deliberately represented once for each of the two track consumers.

This count proves source coverage, not native engine behavior. It does not close the technology/doctrine MCP or banked-mastery blockers.

### Special Forces duplicate-token and dual-track gate — pass with disclosed limitation

Source evidence:

- `common/scripted_triggers/027_doctrine_research_triggers.txt:533-627` permits active Special Forces mastery only while at least one of `special_forces_first` and `special_forces_second` is empty.
- With exactly one occupied track, any installed shared token can be attributed to that occupied track; the empty track remains selectable by exact folder index.
- With both tracks occupied, both Special Forces track-availability predicates fail before a mastery option can enter the pool.
- Empty candidates at `common/scripted_triggers/027_doctrine_research_triggers.txt:2350-2388` require `NOT = { has_doctrine = <token> }`, preventing the same reused token from being installed in both tracks.
- Visible `.72` and `.73` active options additionally require the corresponding `has_subdoctrine_in_track` predicate, while their empty branches use the exact selected track and folder index.
- `doctrine_research_country_has_valid_action` remains an OR across Army, Navy, Air, Special Forces, and Chaos Warfare at `common/scripted_triggers/027_doctrine_research_triggers.txt:966`, so an ambiguous Special Forces state cannot remove valid non-Special-Forces actions.

Classification against the accepted conditional language:

- **Pass:** the installed graph does not expose a token-to-occupied-track trigger for reused tokens, so the implementation admits Special Forces mastery only where branch identity is provable and fails closed otherwise. This matches the specification's conditional-adapter, invalid-identity, and ordinary-domain-preservation requirements.
- **Limitation:** when both Special Forces tracks are occupied, Event 027 offers no active Special Forces mastery action even if one of those branches is incomplete. This is a deliberate capability reduction caused by missing native identity evidence.
- **Not a gameplay deviation:** the event does not guess a track, copy mastery to both tracks, substitute Army mastery or experience, or suppress Army/Navy/Air/Chaos actions.
- **Still acceptance-blocked:** `hoi4.tech_inspect` and runtime evidence cannot prove the installed Special Forces graph and native readback. The source guard is correct, but source review is not equivalent engine evidence.

The behavior is not fully documented. `docs/events/027_doctrine_research/overview.md:72` and `docs/plans/027_doctrine_research_plans/mcp_evidence.md:100-104` describe duplicate-token prevention for empty tracks but do not yet disclose the both-occupied active-mastery suppression. This is a documentation gap.

### Exhausted AI batch closure — pass in source, blocked in probability evidence

`doctrine_research_ai_resolve_active_batch` at `common/scripted_effects/027_doctrine_research_effects.txt:3401-3414` recalculates while the active batch, original batch ID, remaining-choice count, guard, and valid-action predicate remain valid.

If choices remain but no valid action survives, line 3412 calls `doctrine_research_complete_active_batch = yes`. That is normal exhausted closure, not quarantine. A still-valid but unresolved selection uses the quarantine path.

The probability auditor could not materialize the all-zero/exhausted fixture, so this remains a source pass rather than accepted AI scenario proof.

### Controller prompt flag — pass in source, lifecycle acceptance blocked

`doctrine_research_active_batch_prompted_human` is:

- set when a human active batch is opened at `common/scripted_effects/027_doctrine_research_effects.txt:1821`;
- cleared before AI resolution at line 1817;
- checked and set once during lifecycle reconciliation at lines 3292-3295;
- cleared on batch close and annex-state cleanup at lines 3056 and 3443.

The callbacks in `common/on_actions/027_doctrine_research_on_actions.txt` cover state control, puppet/release, subject autonomy/freeing, civil-war end, and annexation. They do not provide a dedicated pure player tag-switch or arbitrary human/AI controller-change callback. Those transitions remain acceptance blockers until traced through an actual supported callback or given another explicit lifecycle mechanism.

### Postfix confirmation and remaining-choice presentation — pass in source

`chaosx.nr27.7` calls `doctrine_research_prepare_confirmation_display`; `GetDoctrineResearchConfirmationDescription` selects distinct adoption and mastery descriptions. Adoption omits irrelevant mastery fields, while mastery retains domain, Grand Doctrine, track, branch, level, completion, and Milestone context.

All 23 required active-page descriptions expose remaining choices:

- `.2`, `.3`, `.4`, `.5`, and `.7`;
- every track page `.60` through `.77`.

The `.7` value is supplied by both action-specific confirmation strings. No active-page mapping is missing.

The Event 027 English localization contains zero player-facing occurrences of `receipt`, `receipts`, `queue`, `queued`, or `duplicate`. Internal source and documentation may still use those implementation terms.

### Event History and Event Details postfix — pass in source

`doctrine_research_prepare_firing_profile` stores `global.doctrine_research_last_firing_size` at `common/scripted_effects/027_doctrine_research_effects.txt:1691-1700`.

The repeatable-event handler maps that value to `events_log_history_payload_override` before recording the single History row at `common/scripted_effects/chaosx_logic_effects.txt:1280-1288`.

Actor mapping remains explicitly empty for Event 027 at `common/scripted_effects/chaosx_events_log_effects.txt:220-228`.

`GetEventsLogEventDetailDescription` contains five exact Event 027 payload branches at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:5938-5973`, selecting one-, two-, three-, four-, and five-choice History descriptions. Four Event Details evolution previews remain registered at `common/scripted_effects/chaosx_events_log_effects.txt:3037-3059`.

This closes the older localization handoff's source defects concerning a static History description and an Event Details premise that omitted the one-to-five range. It does not provide a final shared Event Log/Event Details consumer render.

### People's War maximum — pass in source

`constant:doctrine_research_event.peoples_war_max_mastery_level` is 4. `doctrine_research_prepare_display_levels` uses it for the visible maximum at `common/scripted_effects/027_doctrine_research_effects.txt:375-381`, and transaction summary milestone evaluation uses the same four-level threshold at lines 3031-3044. Other supported branches retain the ordinary five-level maximum.

## Queues, receipts, and persistence

`doctrine_research_country_state_is_aligned` at `common/scripted_triggers/027_doctrine_research_triggers.txt:1027-1051` checks every batch parallel array, all five batch-start empty-domain snapshots, and every receipt parallel array. The implementation also validates receipt-to-batch parent identity before processing.

Each firing appends a distinct batch with fixed stage, size, remaining choices, status, creation date, human-start marker, and start-state snapshots. The oldest queued row is promoted after the active row closes.

The transaction records prepared state before native mutation, records `effect_applied` after a verified effect, and consumes a choice only after success. Existing `choice_consumed` and `effect_applied` rows can be resumed or finalized.

However, prepared, ambiguous, or abandoned rows lack durable proof that the native mutation did not already occur. `doctrine_research_confirm_selection` converts them to ambiguous and quarantines the active batch at `common/scripted_effects/027_doctrine_research_effects.txt:3120-3126`. This is safe failure behavior, but it is not the specification's accepted save/reload idempotency proof.

No accepted traces exist for interruption between native mutation and decrement, duplicate confirmation, overlapping 1–5-choice firings, reload during a queue, or persistence through the complete lifecycle matrix.

## Achievements

The three definitions exist at `common/achievements/chaos_redux_achievements.txt:4203-4216`, with source tracking in `common/scripted_effects/027_doctrine_research_achievement_effects.txt` and nine wired DDS variants at `interface/chaosx_achievements.gfx:1564-1572`.

Source tracking passes these structural checks:

- First Lesson requires a human-started batch larger than one, a consumed adoption, and a later consumed mastery action in the same domain and batch.
- Single School requires a human Evolution IV five-choice batch, five exact `post = pre + 1` mastery receipts for the same domain/Grand Doctrine/track/subdoctrine, and a five-level result.
- Joint Curriculum counts deduplicated domain-plus-track identities and unlocks at four distinct mastery tracks.

### First Lesson exact requirement — source defect and blocker

The specification at `027_doctrine_research_spec_part_4_presentation_assets_achievements.md:228` requires adoption in a domain that had no active Grand Doctrine **at batch start**.

The batch-start empty-domain arrays are created and alignment-checked, but `doctrine_research_achievement_first_lesson_check` at `common/scripted_effects/027_doctrine_research_achievement_effects.txt:10-65` never reads the applicable `doctrine_research_batch_start_empty_*` value. It proves only that adoption was legal when the choice occurred.

Therefore an external state change that removes a Grand Doctrine after batch creation could permit adoption and falsely satisfy First Lesson. This is a real unimplemented requirement, not merely missing runtime evidence.

All three achievements also lack accepted positive and negative scenario traces covering native/banked progress, cross-branch actions, annexation, cancellation, save/reload, and tag/controller transitions.

## Localization

The Event 027 English file is UTF-8 with BOM and contains 333 unique keys. All 261 direct Event 027 references resolve. The 107 dynamic status calls and definitions match exactly.

Postfix source checks pass:

- action-specific confirmation;
- remaining choices on every active page;
- institutional stage names `Foundational`, `Expanded`, `Advanced`, `Joint-Service`, and `Comprehensive`;
- exact one-to-five History descriptions;
- revised evolution prose;
- People's War four-level display;
- removal of internal queue/receipt/duplicate-prevention jargon from player text.

The earlier `localisation_auditor_final_2026-08-30.md` findings about static History detail, missing one-to-five Event Details wording, action-agnostic confirmation, and player-facing implementation jargon are superseded by current source. Its render/overflow blocker remains valid.

## Assets

The report image exists at `gfx/event_pictures/027_doctrine_research/027_doctrine_research_report.dds`, is wired by `interface/027_doctrine_research.gfx`, measures 210×176, and has SHA-256 `d7299954367b8374142a8a8242ceb8de9117e80d3809d92caed1339f188281a5`.

All nine achievement DDS files exist at 64×64 and match the icon-artist handoff hashes:

- First Lesson: `e2ab92e0066439bc85df6d2b3e6a913e0e5a8ebcaa629f3c0e9c46215fc084ce`, grey `7105734156bde4c93f685a50a79df817cb1134c99a2323e2f30dd2848eabb79b`, not eligible `1701448bdf01d64df3123c7abfe9d3f42bc84f798f0c49a935377e45116b721e`.
- Single School: `cd88a460f6bf4d4a461d4fb885e2ae08043a63bcab0f4098008b2e6b49d766c1`, grey `30d4637c8bec116107c066bfd02c52fc764cd8d0f2ffcef0be08b725df953c6f`, not eligible `33f9ebde47d8394c2377815335d4e5575be094a268b3866caa0692285fefb492`.
- Joint Curriculum: `4ee3f0f20d0c716418450539d400412475977f41bed1a8c0d8f913e59dc4240f`, grey `d80f96be8d87290436b5b71cc7a811dacbfef020c77a956418203009d7ff46ab`, not eligible `e4628a234f03d49c8d96a9c0de6231feebe6b774625514fa7b06f8e14e15a2c9`.

The processed report and achievement contact sheet were visually inspected during this audit. The report is an appropriate period military-institution scene; the three achievement families and their grey/not-eligible variants are distinguishable.

No character portrait, dedicated event-owned scripted GUI, animation, super-event, custom 3D unit, unit audio, or custom counter is in scope. Therefore no portrait creator, event UI worker, frame-animation, super-event, or 3D/audio/counter handoff is required. Event Log and Event Details are shared existing systems, not a named Event 027 scripted GUI.

## Evolutions, registration, and cluster

Event 027 is registered as a Tier 0 Minor Repeatable event in `common/scripted_effects/chaosx_logic_effects.txt:188-190` and `:323`, and is enabled by default.

The source implements baseline size 1 and evolution sizes 2, 3, 4, and 5. Evolution processing advances one enabled stage after the configured 90-day date, records each enabled stage once, and records actorless evolution rows. A pre-first-fire unlocked stage supplies the first firing's highest enabled size as required by the specification.

Cluster 9, National Breakthroughs, maps Event 027 to an optional Medium row at Calm World in `common/scripted_effects/chaosx_event_cluster_effects.txt:606-615` and `:1524-1540`. Event 027 remains the only implemented member row from the listed catalog family. The cluster's `Partially Available` status is honest; it cannot be promoted while IDs 54, 65, 67, 83, 85, and 89 remain `To Be Reworked`.

Cluster selection probabilities remain unresolved because MCP did not materialize the complete shared member pool and runtime factors.

## Authoritative XLSX and exports

The workbook was opened read-only and reconciled directly, not through a CSV source.

`Events!A28:N28` contains Event 027 with:

- name `Doctrine Research`;
- exact current Event Details text;
- exact current Evolution I–IV text;
- blank Evolution V and World-End fields;
- type `Minor Repeatable`;
- Chaos level `1`;
- Cluster ID `9`;
- severity `Medium`;
- status `Needs Testing`.

`Clusters!A10:G10` contains National Breakthroughs with exact current cluster-detail wording, members `27, 54, 65, 67, 83, 85, 89`, type `Minor Repeatable`, Chaos level `1`, and status `Partially Available`.

The workbook Event Details and four evolution fields match live localization character-for-character. The normalized Event 027 and Cluster 9 CSV rows match the workbook rows.

Current export evidence:

| Export | Data rows | SHA-256 |
| --- | ---: | --- |
| `chaos_redux_events_catalog.csv` | 165 | `48e639a8d8632bea3838c9c3ec8e4e473517722d3945a844666131cc4bdd75bb` |
| `chaos_redux_clusters_catalog.csv` | 15 | `77b2509d31b0e86cc20a1cfb226fa9412b31eed59ec713e9c1afe2e352a8597e` |
| `chaos_redux_scenarios_catalog.csv` | 14 | `05a5e47238cf23e12a3ac6ba09720106460b42a212b553563f1069e70f139eee` |

The spreadsheet handoff reports total physical rows including headers as 166, 16, and 15; the counts above are data rows. There is no Event 027 manual scenario row, matching the workbook handoff.

## Fresh mandatory MCP evidence

### Event inspection and rendering

Final `hoi4.event_inspect` lint for `chaosx.nr27.1` returned `EVENT_INSPECTED_PARTIAL`, no direct target blocker, revision `02410b498829a4d0ecf4f00b3bed6568cc73bd9f994fc2ec3f4fa23bf4e75706`, and graph hash `149cd6a3748d8b891a746c11add205380c8e69e16acf5bfc5b2525a7ae7bafed`.

Lint artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/32e92b65f2f8ce73a93835662fedc5e755d5a6df3d6aff459c5b1f63262280d9/f53a74d613281d3edd87c8e157329baf845e66258ebbce9938bc45bf2305cdb2/event-lint-02410b498829.json`

Final root overview render returned `EVENT_RENDERED_PARTIAL` on the same revision and graph hash. It selected two nodes and omitted 42,344. Helper count remained zero, and validation remained false because the large-workspace analysis deferred helper projection and lifecycle passes.

Overview artifacts:

- Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16641e5c469726fe58d84b6252bfbbaa4bfcf58d2481c220f565d78672d41472/2c68db95daaa4f0ca3619b108e73718c2a17821dd4bebe48b539ec99f404da3e/event-overview-02410b498829-manifest.json`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0e2926009d294d0c2f6f9399e12852ba7517feaca5eb59f2afbdcfb4d96a6870/a6fff55a59ecbcef65572f2729ca82e1f1817f01e49a152f16862c61ef3af108/event-overview-02410b498829.json`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/73d7109095265c5b099020cbe2826ff80d5e97dfbf642765c5d20688894ab2a9/7ec090ec200334061e7604754ab9e4e77adfd453dc18166a4aeee16bd1870f0f/event-overview-02410b498829.svg`
- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/230de6dd0783856c3cf6a2dca766239dd2d8d2eda73898dbc284de1537870d6e/70e5b44904aca2ee0b22733df9d810bb637ccb93186db2922f641e72d9d1e820/event-overview-02410b498829.png`

Earlier focused `.2`, `.7`, and `.60` renders succeeded on the immediately preceding source revision, but they are not treated as final-revision evidence after the trigger update.

`hoi4.event_compare` from the immediately preceding revision `2455d0b62f8b...` to final revision `02410b498829...` returned `EVENT_REVISION_NOT_CACHED` with zero artifacts. Source comparison is not substituted for the required MCP comparison.

### Technology and doctrine tools

A fresh focused `hoi4.tech_inspect` for `peoples_war` returned `SCAN_BYTE_LIMIT`, no files, and no artifact. A focused `hoi4.tech_render` for `mobile_infantry` also returned `SCAN_BYTE_LIMIT`. An earlier focused inspect timed out after 180 seconds. No accepted `hoi4.tech_compare` artifact exists.

This blocks engine-backed proof for Army, Navy, Air, Special Forces, Chaos Warfare, branch maxima, native track membership, and mastery semantics. It does not negate the source adapters, but source inspection is not equivalent evidence.

### Weighted AI and probability tools

The required current-source pass was routed through `chaosx_ai_probability_auditor`.

The auditor discovered four separate pools:

| Pool | Rows |
| --- | ---: |
| Domain | 5 |
| Grand Doctrine | 13 |
| Track | 18 |
| Subdoctrine | 107 |
| Total source-discoverable rows | 143 |

Fresh cached `hoi4.probability_inspect` returned `PROBABILITY_SOURCE_DISCOVERED` with 143 available candidates but zero resolved candidates. Artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/91d9ed7a2f898d3cc7471499d01d1b700b90bb7c25386dbaa7301473430bd9b6/b8da92e4eb3012b4a1b22f26929d11d0de6e068fd57d0921969d0a42f2942f23/probability-inspect-1cfd3c27a7bf.json`

Refresh inspection, a five-row domain pool, the first DR-A01 evaluation, and the full `DR_027_FINAL_2026_08_30` 37-scenario set each timed out after 180 seconds. One source-plus-adapter retry returned `INTERNAL_ERROR`. No current scenario hash or resolved score/probability was produced.

The submitted set covered all 37 required IDs: A=6, B=4, C=7, D=6, E=6, F=5, G=3.

No current `probability_compare` succeeded and no comparison artifact exists. Sweeps, seeded simulation, sequence analysis, and probability renders could not proceed from an unresolved analysis. The shared event picker and National Breakthroughs optional-member pool also remain unresolved.

Consequently, no accepted evidence proves normalized rankings, invalid-candidate exclusion, dominance/starvation limits, rank reversals, multi-choice recalculation, human/AI parity, optional cluster participation, or exhausted/all-zero closure. The source closure path passes review, but weighted acceptance remains blocked.

## Accepted-plan and handoff disposition

- `repo_explorer_2026-08-29.md`: implemented discovery input; no open plan item by itself.
- `scripted_system_architect_2026-08-29.md`: implemented source architecture; native/runtime proof remains open.
- `parent_implementation_2026-08-30.md`: implemented source tranche, not a completion handoff.
- `parent_pagination_followup_2026-08-30.md`: implemented; deterministic `.60`–`.77` pagination exists. Rendered overflow remains open.
- `generated_event_art_2026-08-29.md` and `icon_artist_2026-08-29.md`: accepted asset packages; checksums and wiring reconcile.
- `localisation_auditor_2026-08-30.md`: historical working audit, superseded by the final localization audit and postfix parent fixes.
- `localisation_auditor_final_2026-08-30.md`: source defects concerning confirmation, History payload, Event Details range, and jargon are now closed; its rendering blocker remains valid.
- `spreadsheet_final_2026-08-30.md`: accepted and reconciled exactly with the current workbook and exports.
- `probability_baseline_2026-08-29.md` and `probability_final_2026-08-30.md`: not balance acceptance; the fresh current-source auditor still resolves zero candidates.
- `completion_auditor_2026-08-30.md` and `completion_auditor_final_2026-08-30.md`: historical snapshots superseded by current source and this postfix audit. Their native, persistence, lifecycle, probability, and presentation blockers remain materially valid; their closed localization/history findings must not be carried forward.
- `mcp_evidence.md`: directionally honest about source-playability versus acceptance, but stale as final evidence. Its event revision, export hashes, localization/history description, and Special Forces behavior predate the postfix source. It must not be used as the current final artifact index.
- Improvement-loop disposition remains closure. No unresolved improvement addendum was found that is waiting for implementation or promotion.

No subagent patch in the Event 027 package lacks a corresponding handoff. The latest concurrent fixes are parent-owned and are reflected in source, overview, and the spreadsheet handoff, but the Special Forces both-occupied limitation and final MCP revision are not yet promoted into the existing evidence document.

## Remaining blockers and recommended next actions

1. Correct First Lesson to require the applicable batch-start empty-domain snapshot, then rerun its positive and negative cases.
2. Restore a technology/doctrine MCP scan under the configured byte ceiling and produce inspect, render, and compare artifacts for Army, Navy, Air, Special Forces, and Chaos Warfare.
3. Produce accepted native traces for empty-track installation plus one mastery step, low/middle/final levels, People's War's four-level maximum, fractional and banked mastery, native completion, and separate Event 027 attribution.
4. Prove receipt idempotency and queue persistence across interruption, reload, duplicate confirmation, overlapping batches, annexation, subject changes, government in exile, controller changes, and pure tag switch.
5. Supply resolvable country/doctrine fixtures and complete picker/cluster manifests for all 37 named scenarios, then rerun inspect, evaluate, sweep, simulation, sequence, render, and same-scenario compare through `chaosx_ai_probability_auditor`.
6. Capture final-revision standard event popup, largest paginated pages, Event History, Event Details, evolution, report-art, and achievement consumer evidence. The shared Event Log/Details framework does not require `chaosx_event_ui_worker`.
7. Capture evolution eligibility and 90-day pacing traces, including pre-first-fire evolution and disabled-stage combinations.
8. Document the Special Forces both-occupied suppression in the overview and refresh `mcp_evidence.md` with final source hashes, revision `02410b498829...`, current export hashes, current History behavior, and current MCP limitations.
9. Keep Event 027 `Needs Testing` and National Breakthroughs `Partially Available` until the blockers above are closed; do not promote either status from source playability alone.

## Final completion boundary

Event 027 is **source-playable**: the current source provides a coherent player and AI path, exact static adapter coverage, safe exhausted closure, a fail-closed conditional Special Forces boundary, complete postfix localization/history wiring, final assets, and synchronized catalog rows.

Event 027 is **not acceptance-complete**: required engine and consumer evidence is missing, probability analysis resolves no candidates, comparison routes are unavailable, persistence and lifecycle scenarios are unproven, and First Lesson does not enforce its exact batch-start condition.

No hidden fallback or substitute reward was found. The Special Forces both-occupied omission is an explicit fail-closed limitation, not a substitute. The cluster's unreworked members and all evidence gaps remain blockers rather than future-work footnotes.
