# Event 027 final completion audit — 2026-08-30

> **Superseded status notice (2026-09-01):** This dated completion audit is preserved as historical evidence and is superseded as a current status authority by ../documentation_state.md. Its acceptance findings remain historical and do not constitute current acceptance.

## Status

**BLOCKED**

Event 027 is **source-playable** in the limited sense that its root, global fanout, country queues, human choice chain, AI continuation, doctrine adapters, logs, details, evolutions, achievements, catalogue records, and assets are present and connected in source.

Event 027 is **not acceptance-verified**. Required source behavior and engine/MCP evidence remain incomplete, so this audit does not promote the package to complete.

## Criteria met in current source

- Registration and dispatch are present: `chaosx.nr27.1` is the hidden root; Event 027 is default-enabled, repeatable, Tier 0/Calm-eligible, registered in the National Breakthroughs cluster, and dispatched through the shared event system. The firing profile snapshots one global stage and one global batch size before country fanout.
- Country-owned batch and receipt ledgers exist. The current alignment checks treat batch arrays and receipt arrays as separate families, and receipt-to-batch parent indices are validated in `common/scripted_triggers/027_doctrine_research_triggers.txt:925` and `common/scripted_effects/027_doctrine_research_effects.txt:312`.
- The active native doctrine boundary is implemented for Army, Navy, Air, Special Forces, and Chaos Warfare. The current package contains five domain candidates, 13 Grand Doctrine candidates, 18 track slots, 99 distinct native/custom subdoctrine identities, and 107 track-qualified mastery adapters. Active tracks use `add_mastery`; empty ordinary tracks use the renamed `doctrine_research_apply_ordinary_empty_track_mastery` and `set_sub_doctrine` at `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt:20150`, while Special Forces has its two-track-specific adapter at line 22058. No caller of the old ordinary empty-track adapter name remains.
- The source attempts exactly one observable level per Event 027 mastery receipt by snapshotting the native level, applying one-point `add_mastery` steps, rereading `has_mastery_level`, and accepting only the expected post-level. It also refuses to consume a choice when empty-track adoption is observed to have completed the branch natively.
- The human chain is bounded and paginated. It contains 30 Event 027 IDs (`.1`–`.12`, `.60`–`.77`), 28 next/previous navigation options, 196 referenced option-localisation keys, and no missing Event 027 option key found by the source audit.
- AI source parity is structurally present: AI uses the same validity gates and resolves domain, Grand Doctrine, track, and subdoctrine choices through scored scripted effects rather than an ordinal first-valid fallback.
- Batch sizes 1/2/3/4/5, firing-stage snapshots, four evolution-history entries, event-log actor mapping, Event Details content, cluster details, achievement definitions, and catalogue rows are wired. The authoritative workbook still honestly marks Event 027 `Needs Testing` and National Breakthroughs `Partially Available`.
- The report image and all nine achievement DDS variants exist and are wired. The report DDS is 210×176 with SHA-256 `D7299954367B8374142A8A8242CEB8DE9117E80D3809D92CAED1339F188281A5`; the nine achievement files match the hashes recorded by the icon handoff and their GFX aliases are present at `interface/chaosx_achievements.gfx:1564`. No portrait, dedicated event-owned scripted GUI, animation, super-event, or custom 3D unit is in scope, so no portrait creator, event UI worker, frame-animation, super-event, or 3D/audio/counter handoff is required.

## Exact remaining blockers

1. **Required mastery presentation is not implemented.** The accepted choice-flow specification requires each mastery option to name the track, subdoctrine, current level, and next level, with completion state visible. Current option localisation remains static text such as `Advance Mobile Infantry` in `localisation/english/027_doctrine_research_l_english.yml:63`. No dynamic current-level/next-level surface or result-level wording was found. This gap is also admitted in `docs/plans/027_doctrine_research_plans/mcp_evidence.md:109`.

2. **Exact native mastery and banked mastery are not proven.** Source adapters exist, but no accepted engine evidence proves low-, middle-, final-, fractional-, or banked-mastery behavior; empty-track adoption plus the first Event 027 step; Special Forces track identity; Chaos Warfare identity; branch completion caused by native banked progress; or separate native/Event 027 attribution. `hoi4.tech_inspect`, `hoi4.tech_render`, and the final revision-object `hoi4.tech_compare` attempt all returned `SCAN_BYTE_LIMIT` with zero artifacts. Source inspection is not equivalent doctrine-graph or runtime evidence.

3. **Receipt idempotency and queue persistence are not acceptance-proven.** Consumed and effect-applied receipts have source handling, but prepared, ambiguous, or abandoned receipts are deliberately converted to ambiguous and the active batch is quarantined because the source has no durable proof that the native effect did not already occur (`common/scripted_effects/027_doctrine_research_effects.txt:3310`). Save/reload between native mutation and choice decrement, repeated confirmation/double acceptance, queued batches of sizes 1–5, and overlapping firings still lack accepted scenario evidence.

4. **Human/AI control and tag-switch lifecycle coverage is incomplete.** Country-owned ledgers and subject/release/autonomy/civil-war callbacks preserve ownership, but `common/on_actions/027_doctrine_research_on_actions.txt` contains no pure player tag-switch or human/AI controller-change callback. The accepted behaviors “AI country becomes human-controlled: open the next choice” and “human country becomes AI-controlled: continue through AI” therefore remain source-unproven, in addition to lacking runtime evidence. Government-in-exile eligibility is present in the validity trigger but is not acceptance-tested.

5. **Evolution timing is not acceptance-verified and retains a first-run edge.** The shared global-host daily coordinator calls `doctrine_research_process_evolution`, and the main path schedules one enabled stage after the 90-day constant. However, `doctrine_research_prepare_evolution_stage` can still set the first firing directly to the highest enabled stage when neither the clock nor fired-once flag exists (`common/scripted_effects/027_doctrine_research_effects.txt:202`). The no-same-day threshold rule and one-stage-per-delay behavior need complete timing evidence, including this pre-coordinator/manual-dispatch edge.

6. **All AI/probability acceptance scenarios are unresolved.** The required `chaosx_ai_probability_auditor` pass covered the repeatable pool, optional cluster participation, domain, Grand Doctrine, track, subdoctrine, and 2–5-choice allocation surfaces. `hoi4.probability_inspect` returned `PROBABILITY_SOURCE_INSPECTED` but `poolComplete:false`, `candidates:0`; the exact 37-scenario `hoi4.probability_compare` returned `PROBABILITY_ANALYZED` with `candidates:0` and `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`. None of `DR-A01–DR-A06`, `DR-B01–DR-B04`, `DR-C01–DR-C07`, `DR-D01–DR-D06`, `DR-E01–DR-E06`, `DR-F01–DR-F05`, or `DR-G01–DR-G03` is acceptance-proven. There are no accepted normalized rankings, dominance/starvation checks, rank reversals, or human/AI parity outcomes.

7. **Mandatory event-chain MCP evidence remains partial.** This audit reran `hoi4.event_inspect` for `chaosx.nr27.1` and `hoi4.event_render` for overview, options, reachability, state, timing, terminals, and unresolved views. All returned `EVENT_INSPECTED_PARTIAL` or `EVENT_RENDERED_PARTIAL` at revision `ac2516cf55a82d5ce3152e98d00c31e148f74b85a13a09c3ad7791c0453bef18`; the bounded graph omits the large helper-expanded surface and does not prove pagination, receipts, lifecycle, or terminal coverage. `hoi4.event_compare` against the earlier revision returned `EVENT_REVISION_NOT_CACHED`. The exact artifacts and earlier comparison errors are recorded in `docs/plans/027_doctrine_research_plans/mcp_evidence.md:15`–`31`.

8. **Player-facing visual and achievement acceptance is incomplete.** Source pagination exists, but no accepted render proves the largest Army/Navy/Air pages are unclipped and navigable or that Event Details and Event Log text present the full result correctly. Achievement wiring and icons are complete in source/assets, but the required positive and negative receipt, banked-mastery, save/reload, cross-branch, and tag-switch cases have not been validated.

## Accepted-plan disposition

- The repository-explorer and scripted-system-architect plans have been implemented at source level where noted above. Their native mastery, persistence, and engine-proof requirements remain blocked rather than promoted.
- The parent implementation and pagination handoffs are implemented source tranches, not completion handoffs. Pagination closed the earlier missing-navigation defect; it did not close rendered overflow or dynamic-level text.
- Generated report art and achievement icon handoffs are complete and parent wiring is present. The localisation handoff is only partially promoted because the accepted dynamic mastery-level wording is still absent.
- The probability-baseline handoff is not accepted as balance proof. The final probability auditor confirms that all 37 named scenarios remain unresolved.
- The earlier completion audit is superseded for defects that the current source demonstrably closed: separate ledger-family alignment, receipt parent validation, default/Tier-0 registration, ordinary empty-track adapter routing, 1–5 batch constants, pagination, and removal of the active ordinal AI fallback. Its native/runtime/MCP concerns remain open where repeated above.
- `mcp_evidence.md` and `overview.md` explicitly disclaim completion. The workbook's `Needs Testing` and cluster `Partially Available` values are current and not stale completion claims. No unresolved improvement-loop addendum was found, and every Event 027 patch-producing subagent has a handoff note.

## Meaningful validation performed

- Read every Event 027 specification, overview, MCP evidence file, source surface, current Event 027 handoff, and the relevant settings, dispatch, cluster, event-log, details, evolution, achievement, CXT, localisation, GFX, asset-manifest, and authoritative workbook records.
- Recounted event IDs, navigation options, localisation references, doctrine candidates, and native adapter identities; confirmed the renamed ordinary empty-track adapter has one definition and one active dispatch with no stale caller.
- Rechecked the authoritative XLSX read-only: Event 027 is row 28 with status `Needs Testing`; National Breakthroughs is row 10 with status `Partially Available`.
- Used the mandatory read-only event inspect/render/compare routes, doctrine inspect/render/compare routes, and the dedicated probability auditor. The exact MCP limits are reported above rather than replaced with source-only claims.
- Verified report/achievement asset presence, recorded dimensions/hashes, GFX aliases, achievement registry entries, and localisation wiring against the existing asset handoffs.

## Recommended next actions

1. The implementation owner must add the accepted dynamic current/next/completion mastery presentation and resolve or explicitly redesign the first-run evolution edge.
2. Produce engine evidence for every ordinary/Special Forces/Chaos Warfare low-, middle-, final-, empty-track-, and banked-mastery sequence, plus receipt interruption, save/reload, queued-batch, tag/control transition, and achievement cases.
3. Restore complete MCP doctrine scanning and event revision caching, then rerun event and technology inspect/render/compare evidence on the same final source revision.
4. Supply concrete country-state fixtures and a complete custom-pool manifest for all 37 named scenarios; rerun inspect/evaluate/sweep/render and same-scenario probability comparison through `chaosx_ai_probability_auditor`.
5. Capture accepted pagination, Event Log, and Event Details visual evidence before changing the catalogue status or making a completion claim.

## Changed files

- Gameplay, localisation, assets, and spreadsheets changed by this auditor: **none**.
- Audit artifact created: `docs/plans/027_doctrine_research_plans/subagent_handoffs/completion_auditor_final_2026-08-30.md`.
