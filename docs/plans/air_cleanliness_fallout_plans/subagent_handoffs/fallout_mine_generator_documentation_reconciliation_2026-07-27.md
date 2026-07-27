# Mine Generator documentation reconciliation handoff

Status: current-reconciliation patch complete for the dormant Mine Generator tranche. Gameplay completion and runtime acceptance are not claimed by this handoff.

## Scope

The reconciliation covers candidate `642`, events `642` through `648`, transaction `710063`, route `7163`, Event Log history `9169`, `63` ordinary rows, and `523` defined event blocks.

The reconciliation preserves historical snapshots, the unset scheduler activation flags, and the explicit host-authority, save-recovery, delayed-delivery, multiplayer, Event Log, and player-visible runtime blockers.

## Source-of-truth map

| Surface | Path | Disposition | Evidence or boundary |
| --- | --- | --- | --- |
| Accepted design | `docs/specs/air_cleanliness_fallout_specs/specs/64_reviewed_regional_mine_generator.md` | Accepted source design, unchanged | Defines the identity ledger, branches, ledgers, cleanup, asset contract, and dormant runtime boundary. |
| Tranche handoff | `docs/plans/air_cleanliness_fallout_plans/2026-07-27_mine_generator_tranche_addendum.md` | Accepted design handoff, unchanged | It records the same identities and requires gameplay, localisation, assets, Event Log, spreadsheet alignment, and focused proof before an implemented disposition. |
| Static implementation proof | `docs/plans/air_cleanliness_fallout_plans/FALLOUT_MINE_GENERATOR_PROOF.md` | Static implementation complete, live validation pending, unchanged | Proves event identities, direct native-resource trigger, numerical contract, localisation, Event Log routing, asset package, and cleanup evidence. |
| Current event id ledger | `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md` | Current summary and Mine Generator tranche reconciled | The current header now reports `63` rows and `523` blocks through `648`. Historical sections remain unchanged. |
| Current scheduler proof | `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_SCHEDULER_PROOF.md` | Current summary and Mine Generator tranche reconciled | The current header, status, range, and latest tranche now include Mine Generator. Activation and runtime blockers remain explicit. |
| Implementation status README | `docs/plans/air_cleanliness_fallout_plans/README_IMPLEMENTATION_STATUS.md` | Current summary and Mine Generator tranche reconciled | The latest tranche, scheduler foundation, current count, proof link, and blocker wording now include Mine Generator. |
| Candidate pilot proof | `docs/plans/air_cleanliness_fallout_plans/FALLOUT_REVIEWED_CANDIDATE_PILOT_PROOF.md` | Current header, upper bound, constants count, and Mine Generator tranche reconciled | The current header now reports candidate `642`, route upper bound `7164`, `63` rows, and `523` blocks. Historical correction sections remain unchanged. |
| Source spec index | `docs/specs/air_cleanliness_fallout_specs/SOURCE_SPEC_INDEX.md` | Unchanged | Spec 64 was already listed at line 128 and no stale current count was present. |

## Plan and handoff disposition

| Document | Disposition | Reason |
| --- | --- | --- |
| `2026-07-27_mine_generator_tranche_addendum.md` | Accepted design handoff remains open | The static proof exists, but the addendum explicitly conditions an implemented disposition on final spreadsheet alignment and main-agent confirmation. |
| `FALLOUT_MINE_GENERATOR_PROOF.md` | Evidence promoted into current ledgers | The proof is the static implementation evidence and continues to state that live validation is pending. |
| `FALLOUT_EVENT_ID_LEDGER.md` | Current reconciliation implemented | The header and latest tranche now carry the Mine Generator identity and count. |
| `FALLOUT_EVENT_SCHEDULER_PROOF.md` | Current reconciliation implemented | The current scheduler summary and latest tranche now carry the Mine Generator identity and count. |
| `README_IMPLEMENTATION_STATUS.md` | Current reconciliation implemented | The status summary and scheduler foundation now carry the Mine Generator identity and count. |
| `FALLOUT_REVIEWED_CANDIDATE_PILOT_PROOF.md` | Current reconciliation implemented | The current candidate proof now carries candidate `642`, route upper bound `7164`, and the 63-row count. |

## Contradictions resolved

- The current event id ledger header reported `61` rows, `509` blocks, and range `634`. It now reports `63` rows, `523` blocks, and range `648`.
- The current scheduler proof header and status reported `62` rows, `516` blocks, and range `641`. They now report `63` rows, `523` blocks, and range `648`.
- The README latest-tranche summary and scheduler foundation reported Mountain Pass Census as current. They now report Mine Generator and link its proof.
- The candidate pilot proof reported candidate `635`, route upper bound `7163`, and `516` blocks. It now reports candidate `642`, route upper bound `7164`, and `523` blocks.

## Contradictions still open

- The addendum still says it should be marked implemented only after workbook alignment and main-agent confirmation. This remains a deliberate open disposition because the spreadsheet is outside this task scope and was not edited or audited here.
- Spec 64 still says that the source specification does not claim gameplay or runtime acceptance. The static proof says implementation is complete and live validation is pending. These statements are compatible source-design and implementation-boundary statements, so neither was rewritten.
- Historical count paragraphs still contain older row and block totals. They are retained as labeled or superseded snapshots and were not rewritten.

## Duplicate, superseded, and stale-document audit

- No duplicate Mine Generator spec, proof, or tranche document was found in the named scope.
- `FALLOUT_MINE_GENERATOR_PROOF.md` is evidence for the tranche and does not supersede Spec 64.
- Historical sections in the four current ledgers remain intentionally preserved instead of being deleted or rewritten.
- No Mine Generator-specific prompt file was found in the targeted docs paths. The generic source-index prompts remain unchanged.
- The addendum condition about implemented disposition remains the only stale or conditional instruction requiring a parent decision.

## Recommended parent decisions

1. Confirm whether spreadsheet alignment is complete before changing the addendum disposition from accepted design handoff to implemented.
2. Keep both scheduler activation flags unset until user-owned runtime checks cover scheduler dispatch, delayed queue delivery, host authority, save recovery, multiplayer behavior, Event Log rendering, and player-visible art.
3. Retain Spec 64 as the accepted source design unless the parent wants a separate implementation-status notice added without weakening its runtime boundary.

## Files changed

- `docs/plans/air_cleanliness_fallout_plans/README_IMPLEMENTATION_STATUS.md` lines 3, 5, 92, 108, 110, 114, and 820 through 828.
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md` lines 3, 5, 17, and 736 through 748.
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_SCHEDULER_PROOF.md` lines 3, 5, 11, 13, and 678 through 688.
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_REVIEWED_CANDIDATE_PILOT_PROOF.md` lines 3, 5, 15, 19, 74, and 539 through 549.
- `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/fallout_mine_generator_documentation_reconciliation_2026-07-27.md` created as this handoff.

No spec, addendum, source index, gameplay, localisation, spreadsheet, asset, or runtime file was edited.

## Validation

- The constants block contains `63` candidate ids, `63` transaction keys, and `63` route ids, including Mine Generator `642`, `710063`, and `7163`.
- The event source contains `chaosx.fallout.642` through `chaosx.fallout.648`, and the proof files contain Event Log history `9169`.
- Targeted `rg` checks confirm the four current summaries carry `63`, `523`, `642`, `710063`, `7163`, and `9169`.
- `SOURCE_SPEC_INDEX.md` already contains Spec 64 at line 128.
- `git diff --check` was run on all four edited current-summary files.

HOI4 was not launched. Spreadsheet inspection and workbook export were skipped because this task forbids spreadsheet edits and assigns the workbook to the spreadsheet worker.

## Remaining risks

The Mine Generator remains dormant. Scheduler activation, host authority, save recovery, delayed delivery, multiplayer behavior, Event Log rendering, and player-visible runtime art remain unobserved. The parent must resolve the addendum disposition after confirming spreadsheet alignment and final integration status.
