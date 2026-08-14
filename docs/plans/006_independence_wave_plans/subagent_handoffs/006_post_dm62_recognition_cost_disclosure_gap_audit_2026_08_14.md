# Event 006 post-DM-62 recognition cost-disclosure audit

Date: 2026-08-14

Audit base: `062cfc4852b742289c87d303bc8c8a3f75bd3847` and `66bd02c20`

Mode: read-only completion audit. The source corrections described below were applied by the parent in the shared worktree while this audit was running. This auditor did not edit gameplay, localisation, assets, the event catalog workbook, or central admission.

## Disposition

One concrete accepted-matrix gap was found in DM-16 and the parent has applied the bounded source correction in the current worktree.

The parent also applied the same already-supported selector repair to the adjacent IW-184/HBX and DM-42 surfaces while this audit was running. HBX, DM-16, and DM-42 now select the existing factory-aware diplomatic cost triplet for the light civilian-factory commitments already present in their source. These are owner-applied repairs; this auditor claims no gameplay edit.

DM-16 `independence_wave_coordinate_recognition_campaign` reserved one civilian factory through `@CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT`, but its card selected `independence_wave_cost_diplomatic_standard`, whose base, tooltip, and blocked text disclose only Command Power and convoy-or-train capacity.

Commit `062cfc485` introduced the exact matching reusable triplet `independence_wave_cost_diplomatic_standard_factory` for DM-62. The safe DM-16 correction is therefore one selector replacement with no new localisation or tuning.

## Accepted requirement and exact evidence

- `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv:17` identifies DM-16 as the shared Coordinate Recognition Campaign for a network or League member, with concrete shared diplomatic costs and a target-recognition outcome.
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md:520-533` defines the recognition decision family and explicitly allows civilian-factory burden alongside convoys and diplomatic capacity.
- `common/decisions/006_independence_wave_decisions.txt:858-917` owns DM-16. Before the parent patch, lines 882-883 paired generic diplomatic-standard text with the light civilian-factory reservation.
- `localisation/english/006_independence_wave_decisions_l_english.yml:29`, `:58`, and `:59` define the existing factory-aware base, tooltip, and blocked keys from `062cfc485`. They read the same diplomatic-standard constants and `independence_wave_decision_cost.civilian_factory_light` used by DM-16.
- The offline Decision Modding wiki documents that `custom_cost_text` selects the base key, `<key>_tooltip`, and `<key>_blocked`. The installed vanilla `common/decisions/EST.txt:358-363` uses a distinct factory-count cost key for a civilian-factory requirement, confirming that the selected key is the player-facing cost contract.

## Owner-applied current worktree correction

Current worktree source now contains:

```text
custom_cost_text = independence_wave_cost_diplomatic_standard_factory
modifier = { civilian_factory_use = @CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT }
```

This changes only the displayed cost selector. DM-16 retains its existing target-root gate, weaker-recognition target test, network membership, diplomatic-standard affordability helper and payment effect, long duration, standard cooldown, recognition and League deltas, cancellation rules, and high AI willingness score.

The parent also applied the same selector correction to:

- admitted IW-184/HBX `independence_wave_hbx_settle_federal_asset_ledger` at `common/decisions/006_independence_wave_pacific_decisions.txt:119`;
- DM-42 `independence_wave_request_collective_recognition` at `common/decisions/006_independence_wave_decisions.txt:2199`.

Both decisions retain the same factory-light modifier, affordability trigger, payment helper, timing, effects, cleanup, and AI score that existed before the selector repair. Their dedicated owner handoffs are `006_hbx_federal_asset_ledger_cost_localisation_alignment_2026_08_14.md` and `006_dm42_collective_recognition_cost_localisation_patch_2026_08_14.md` in this directory.

These concurrent corrections are source-aligned and are not claimed as this auditor's edits.

Before committing DM-16, the owner should ensure the diff contains only the semantic selector change. During the audit, the unchanged `independence_wave_coordinate_recognition_campaign = {` line briefly appeared in the diff from line-ending normalization and did not belong to the gameplay correction.

## Current authority boundary

The allocator audit still passes with 149 publishers, 40 runtime adapters, 32 content attestations, 29 compatible reservation groups, and the `3/4/5/7/10` automatic ladder with World Collapse at 10. The eight adapter-only rows remain IW-013, IW-015, IW-043, IW-058, IW-093, IW-098, IW-177, and IW-179. IW-047 MEL and IW-050 KOM remain package-local and unadmitted. This correction does not add an adapter, attestation, Join branch, tag, identity, flag, portrait, anchor, or reservation group.

## Surface and accepted-plan disposition

- Decision cost disclosure: implemented in the current owner worktree for HBX, DM-16, and DM-42. Each repair reuses the triplet accepted and introduced for DM-62; no cost or behavior was redesigned.
- Weighted logic: unchanged and only partially evidenced under the empty fixture. The MCP receipts below are structural/score-only, not balance proof.
- Event chain: unchanged and still `EVENT_INSPECTED_PARTIAL` across all twelve Event 006 event files at the last event-source revision. No event-source patch or comparison is claimed.
- Central admission and package authority: unchanged and HOLD/PARTIAL at 40 adapters, 32 attestations, 29 compatible groups, and 161 unattested selectable rows. MEL and KOM remain fail-closed.
- GUI and assets: not touched. These are ordinary decisions rather than an Event 006-owned dedicated scripted GUI, and the selector repairs require no new visual asset.
- Localisation and catalog: the already-present factory-aware base/tooltip/blocked triplet is reused. No wording, workbook, or catalog semantic changed, so no workbook mutation is claimed.
- Documentation: the HBX, DM-16, and DM-42 owner handoffs record the implemented selectors. This audit promotes those three findings to owner-applied and supersedes its earlier DM-42-pending wording; it accepts no broader admission or package plan.

## Weighted-logic and MCP disposition

DM-16 contains an unchanged `ai_will_do` block. A current read-only `chaosx_ai_probability_auditor` pass over `common/decisions/006_independence_wave_decisions.txt` covered DM-16 as the named surface. The source corrections change no weight, trigger, target, cooldown, or effect, so they do not produce a probability delta or require a balance-target decision.

The Event 006 event graph is unchanged by `062cfc485`, `66bd02c20`, or the current decision selectors. The current all-file event evidence therefore remains revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, with all twelve file-scoped inspections returning `EVENT_INSPECTED_PARTIAL`. No event-source comparison is claimed because no event file changed.

DM-16 uses the ordinary decision framework rather than an Event 006-owned dedicated scripted GUI. No GUI rewrite or event UI worker is required for this text-selector repair.

### Current probability receipt

Fresh `hoi4.probability_inspect` on `common/decisions/006_independence_wave_decisions.txt` with adapter `decision_ai_will_do` returned `PROBABILITY_SOURCE_INSPECTED` for workspace `mod_chaos_redux_ea3b2d67c2c0`:

- source revision: `de4ea8794eabc91b142274a08be8da11d772fbc94a6141328f2cbe31fce549ba`
- source hash: `c7b8349df5ccbc3ef6c2511abdb7f1fe34e6d7dd45bff82970e2c726d43a635a`
- 10 decision candidates, 0 available under the empty fixture, 79 required inputs, 0 inspect-unresolved rows, `poolComplete=false`
- artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1dd48e1e483868a201bb2fc3decaa6101fe13817edcdc80aa6a82ca715c57b3/eac4004b3954ce95c809ce6ead2c218d9caf0b3d976c5d14129e38c2db66e95d/probability-inspect-c7b8349df5cc.json`

This is a structural/current-source receipt only. It does not prove normalized click probability or campaign balance because the adapter reports no available candidates and an incomplete pool.

The DM-16 target probe through `decision_ai_will_do` returned `candidate_pool_not_found`; the MCP exposes this targeted timed surface through `mission_ai_will_do`. The mission-target inspect returned one candidate and two required inputs at revision `de4ea8794eabc91b142274a08be8da11d772fbc94a6141328f2cbe31fce549ba`, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fbc4c2666df60f1af3d54dc4a762377ce7d68928a7147157ce88ae2e90b04f14/7cc2cc92d166137fc72287084e296ec8e77e18c79c7caae5c742fca48c4b4c60/probability-inspect-c7b8349df5cc.json`.

Named empty-fixture evaluation `E6_DM16_TARGET_EMPTY_CURRENT_2026_08_14` returned `PROBABILITY_ANALYZED_PARTIAL`, two unresolved items, and zero diagnostics: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b652e7ad8cdb4ad0d34004f438b63cb4018d34dacbc31c333a075318a36dec7b/ef553af94a78c0b7e285f82e22a1f0c8e6e546c3c2a0c27986c9cb70e2884857/probability-8091a07348c36689c1cbf5af.json`. This is score-only/partial evidence; no campaign fixture was invented and no quantitative probability claim is made.

No `hoi4.probability_compare` was required because HBX, DM-16, and DM-42 changed only `custom_cost_text`; all weighted logic is byte-for-byte outside the intended semantic patch.

## Validation and remaining risk

- Confirmed that HBX, DM-16, and DM-42 each have an active resource shape of diplomatic standard plus `civilian_factory_light` and that the existing factory-aware triplet describes exactly that shape.
- Confirmed that the three selector patches do not change `ai_will_do`, target selection, effects, duration, cooldown, or cleanup.
- Confirmed that the current allocator remains at 40 / 32 / 29 / 161 and preserves MEL/KOM fail-closed.
- `git diff --check` passed for the relevant shared decision, Pacific decision, and decision-localisation files.

At the final audit observation, DM-42's semantic selector line and the unchanged following modifier line appeared as changed because their line endings differed from the surrounding CRLF source. A separate owner is reconciling that incidental formatting. It is not a gameplay requirement, must not be presented as an additional source change, and does not alter this audit disposition.

After the owner-applied HBX, DM-16, and DM-42 repairs, this pass proves no additional bounded source patch that satisfies the task constraints. The 161 unattested selectable rows remain a broad admission boundary rather than authority for isolated source edits. The next package tranche still requires package-specific identity, flag, portrait, anchor, compatibility, and typed-fixture evidence before central attestation can safely widen; this auditor does not invent those inputs or recommend widening admission.

Event 006 remains HOLD / PARTIAL. This handoff makes no broad completion or quantitative AI claim.
