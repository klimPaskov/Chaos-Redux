# Event 032 ordinary preparation repair

Disposition: implemented source tranche under final independent review, not whole-event completion.
Acceptance basis: the user's full Event 32 contract, Parts 3 and 5, and `subagent_handoffs/032_operation_preparation_decision_audit_2026-10-03.md`.
The explicit one-category instruction supersedes the older second-category layout while retaining country, objective, exact-state, and clear-target functionality.
Part 5 records that basis.

## Implementation and review

The durable source/API contract is [ordinary preparation](../../events/032_missiles/systems/ordinary_preparation.md).
The parent repaired self-cancelling missions, missing readiness transitions, fees on rejected preflight, overwritten best-state scores, wrong counterforce profiles, country/state FROM misuse, and excessive selector rows.
Additional repairs cover fresh inclusive affordability, accepted-only cooldowns, positive unchanged site receipts, projected shares before escrow, persisted failure causes, non-operation cleanup isolation, typed site requests, and compact category context.
Disabled Special Warheads retains selection/history but new ordinary orders use conventional payload and base cost; already-frozen special receipts invalidate rather than silently downgrade.

The independent re-audit found an unverified argument-block scripted-helper dependency and insufficient allocation validation.
Every introduced argument-block/$PARAM$ helper call was replaced by zero-argument literal wrappers, documented temporary trigger quotes, and four literal mission IDs with locally declared meta DAYS.
No accepted gameplay route, cost, cooldown, or willingness coefficient changes through that API repair.
Projected shares fit before escrow; retained shares must be positive, unchanged, and within capacity.
The rejected-resource branch aborts any uncommitted escrow before cleanup.

The localization handoff was reviewed, temporary math triggers were verified against installed documentation and vanilla SEA_PRC localization, and its editable/general requirement tooltips were wired.
Fresh reserve display no longer reads normal preview caches.
Unread failure context exposes a persistent cause after native mission removal without erasing failure history.
No new event, scan, GUI, artwork, equipment, country, focus tree, world-end branch, or native raid scaffold is introduced.
Existing same-family sprites are reused.

## Baselines and tests

The initial eight byte-exact before hashes are in the probability handoff and `baselines/2026-10-03_ordinary_preparation/`.
The additional core-effects before hash is `47cc92f71f3f927ed5b0e88277c039734c77fd21da7f2564828a6bbb581859b5`.
The new preparation-cost trigger file has no before counterpart.
TXT/YML snapshots disable text normalization; raw committed hashes must be verified before publishing.

Commands: `python .tools/test_event32_ordinary_preparation.py`, `python .tools/test_event32_evolution_gates.py`, and `python .tools/test_event32_recipient_scope.py`.
The post-review source point passed 17, 6, and 11 test methods respectively.
Those tests cover fee boundaries, accepted payment/cooldowns, due-date readiness, timer arithmetic, receipt guards, exact state, typed site input, disabled-track fallback, literal helper contracts, and cleanup ownership.
Specialist color/context cases are source models, not native UI or engine execution.

The probability specialist was spawned without inherited context before weighted changes.
Decision/mission willingness coefficients remain unchanged; country eligibility and target-state ranking are probability-bearing changes.
Matching comparisons use STRIKE-05, TGT-S-01/02/04, and TGT-C-04 with declared GER/POL/FRA model facts and existing state IDs 85–87.
These are not live-game observations.

## Required reference evidence

| Source | Read lines | Revision |
| --- | --- | --- |
| Installed common/decisions/_documentation.md | 13–45, live reference_read | 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019 |
| Offline Decision modding wiki | 465–478, 577–611 | 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162 |
| Installed effects_documentation.md | 661–669, 1051–1063, 6083–6090 | 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af |
| Offline Effects wiki | 1917–1925 | 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c |
| Installed triggers_documentation.md | 5185–5209, 6455–6468, 7482–7502 | 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29 |
| Offline Data structures wiki | 1516–1518, 1602, 1615, 1667–1677 | 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4 |
| Vanilla PHI_scripted_effects.txt | 243–248 | b3cae2c958e7372b56fbfcbd48ded242fd681f08d7259a73c17669c4080b7959 |
| Vanilla GER_scripted_effects.txt | 1288–1291 | 1d6b5cc8e00d685aa3c95cecab41cfeb2da590e90490de5dcce05e8e8e2beeb3 |

Vanilla Argentina focus lines 486–489 supplies the signed mission-timeout precedent, revision `e7b06a02bfe938ae96c455fb13923c23a160178e74a1733cf92a7c1a38ed2a7e`.
Vanilla SEA_PRC_scripted_loc lines 38–54 confirms temporary math in a localization trigger.
Offline Triggers lines 1593 and 1644–1654 gives parallel intelligence syntax.
Existing chaosx_buildings lines 38–109 defines the actual chemical/biological facilities.
The installed guide's prose says state_trigger; exact vanilla/offline definitions use state_target, which is preserved.

## Mandatory evidence limits

Reference context reported omitted Effects, Triggers, Scopes, Localisation, and installed-effects sections at its limit; pertinent detailed rules were read locally, not inferred from the compact bundle.
Offline reference_read line577/max35 timed out after 600 seconds.
The line584/max5 retry returned REFERENCE_POSITION_OUTSIDE_SECTION because the ID represented the heading only.
Targeted reference_search returned the correct State targeted decisions section, and live reference_read returned lines 584–595 with revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`.
Exact vanilla source_lookup max18 timed out after 600 seconds; the max8 retry returned PHI_set_pre_investment_variables at game:common/scripted_effects/PHI_scripted_effects.txt:243–250, indexed revision `b1363227b54b209ff11250aa570532cf480916ff13ce02cd5a5b9f2fc05a4f68`, with complete bounded definition coverage and references intentionally excluded.
The live schema has no view/keyPath fields, no script_validate, and no confirmed connected version/health/task negotiation; helper_expansion/jobs/native tasks are not assumed.
No standalone Technology Tree Viewer was confirmed.

The localization handoff records exact MCP -32603 request-capacity scandir failures and its corrected decision_inspect scenario-schema rejection.
Its subsequent inspector observation was terminated without an artifact; this does not establish server cancellation.
The re-auditor also returned no domain artifacts during its observation window.
These are coverage/service gaps, not numeric or engine passes.
The parent subsequently read the installed v3.6 probability schema and corrected the specialist's nested-state placement: actor, flags, scopes, and scopePools are top-level scenario fields; state is a flat scalar/array map.
Frozen comparison sources use logical path plus snapshotPath and expectedSourceHash, not the documentation snapshot as an ordinary runtime path.
The correctly bound five-scenario decision compare timed out after 600 seconds without an artifact.
Its narrower STRIKE-05/counterforce retry retains the full scenario context and same frozen/current source pair and is pending in specialist cell 427.
Matching mission inspection/comparison remains separately tracked by that specialist.
Malformed or empty-state attempts do not close the named scenarios.
The available custom-pool modes are categorical or independent chances, not deterministic argmax; no weighted surrogate is substituted for the target selector's maximum-score behavior.
Event/technology/probability evidence and native gameplay observations remain separate mandatory routes.
The supplied menu QA log is not Event 32 execution proof or a clean project-wide log.
No game or autonomous desktop testing was launched.

## Remaining accepted work

The independent source findings are resolved; the source-only repair can be committed without presenting the pending domain checks as passes.
Retain the pending comparison's final result or exact failure in a reviewed follow-up; the whole event and balance acceptance stay open.
Catalog status remains To Be Reworked; the reviewed workbook/export commit is authoritative and no CSV is directly edited.
Continue physical integer allocation/custody, special payload reservation/selection, maintenance-phase access/refresh, other project-mission success/timing, dynamic evolution pacing, retaliation bounds, every probability case, improvement-planner closure, completion audit, and user-owned live acceptance.
These are outstanding requirements, not rejected design or claimed completion.
