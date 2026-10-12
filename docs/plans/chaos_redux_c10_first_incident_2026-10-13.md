# C10: Secret Alliance first incident

The requested varying first incident is implemented in `04bd73d68238718675d2a5db1ad77400674349a2`.
The acceptance basis is the owner's explicit C10 instruction to confirm variation and fix the entry if it always opens with Orders from Unknown Hands.

## History and change

`git log -S 'id = chaosx.nr11.3' -- events/011_secret_alliance.txt` and the event diff for `d1d641122f2ed7b86654e035965bd33cba827290` show that the current implementation introduced the unconditional `.3` opening.
Its parent has no version of this event file, and the earlier incarnation at `13795a26e` uses a single visible `.1` entry with different mechanics.
There is no correct earlier varying opener to restore into the current implementation, so this is the minimal authorized C10 fix rather than a claimed historical restoration.

The accepted `.1` entry initializes its existing context, then draws between the original `.3` report and `secret_alliance_launch_weighted_operation`.
Both opening weights are 1 and live in the existing `secret_alliance_operation` constant category.
Orders therefore has a 50% opening share, and existing operations share the other 50% according to their existing family weights and eligibility.
The dispatcher prepares actor, surface, risk, evidence class, and recovery before firing a report, which preserves the stored-operation resolution contract.
Baseline eligibility excludes political and military operation families until Evolution I, and disables sabotage or military operations when their required surfaces are unavailable.

Changed files are `events/011_secret_alliance.txt`, `common/script_constants/011_secret_alliance_constants.txt`, and `docs/events/011_secret_alliance/overview.md`.
The existing two-option reports and their text, art, costs, and operation-family weights remain their original consumers.
No simplification was made in C10.

## Reference and verification evidence

The connected reference tools were exposed and their live schemas were inspected.
Installed `documentation/effects_documentation.md`, lines 5413-5432, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, was read through `hoi4.reference_read` for proportional `random_list` selection and variable weights.
The same revision's lines 2943-2967 were read for country-scope `country_event` dispatch.
Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, lines 4504-4571, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, was read for weighted selection and unfixed event seeds.
Installed `documentation/script_concept_documentation.md`, lines 216-222, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`, and `common/script_constants/documentation.md`, lines 1-34, revision `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`, were located by reference search and read locally after their reference-read request stalled.
Vanilla `events/Germany.txt`, lines 6752-6765, supplies the inspected precedent for a `random_list` selecting one country event.
The existing Event 011 operation dispatcher already uses script-constant list weights for its political-pressure variants.

The focused `hoi4.event_inspect` trace for `.1` returned `EVENT_INSPECTED_PARTIAL`, revision `0659c0b191810740668b081f9274bd73073ffe31a716ff0e1756b9604bbf687e`, graph hash `faba610935166f4612f01a82ddae92e14e94256c77dd42449655e72dc17cf1d8`.
It covers event and on-action source and explicitly defers helper projections and lifecycle passes, so dispatcher preparation was checked directly in `common/scripted_effects/011_secret_alliance_effects.txt`, lines 2475-2797.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8668602fef67fb5a2f8eafaebd7f4e6b385f2cb4ad540fda9fb6458cc195fd5d/90d37a1bf6907ad74c42a3ea343222e37376ea0c57f3dc519f71a68b3d707189/event-trace-0659c0b19181.json`.
One `hoi4.source_lookup` request for `random_list` and one file-mode `hoi4.script_validate` request for this event file were stopped after returning no result within the work window.
They are not passed checks, and no unchanged retry was made.
Useful future retry requires a narrower source request or a responsive validation route, rather than another workspace-wide scan.
No game was launched.

Independent `chaosx_ai_probability_auditor` review compared the exact before/current root and read the existing dispatcher and constants.
It confirmed the complete outer pool changes from 100% Orders to 50% Orders and 50% operation launch under identical valid-entry conditions.
The inner calculations use three explicit valid founders, liaison/fear, intelligence/ideology, and logistics/opportunism, with tied motive counts selecting containment doctrine, no prior operation, no covered members, and no exposed/protected surfaces.
Evolution I/II cases additionally have a valid neighboring founder and military surface.
Family order below is diplomatic, intelligence, sabotage, political, military, recruitment.

| Named scenario | Final family weights after the existing 80 ceiling | Conditional shares given operation launch |
| --- | --- | --- |
| Baseline, industrial surface present | 80 / 80 / 64 / 0 / 0 / 40 | 30.30% / 30.30% / 24.24% / 0% / 0% / 15.15% |
| Baseline, industrial surface absent | 80 / 80 / 0 / 0 / 0 / 40 | 40% / 40% / 0% / 0% / 0% / 20% |
| Evolution I, industrial and military surfaces present | 80 / 80 / 64 / 36 / 36 / 40 | 23.81% / 23.81% / 19.05% / 10.71% / 10.71% / 11.90% |
| Evolution II, industrial and military surfaces present | 80 / 80 / 72 / 36 / 44 / 40 | 22.73% / 22.73% / 20.45% / 10.23% / 12.50% / 11.36% |

Parent review caught the auditor's first table using pre-clamp weights, and the auditor rechecked `secret_alliance_operation_weight.maximum = 80` and all six clamps before returning the corrected table above.
These source-derived shares are conditional on the declared fixed inputs, and each occupies half the overall opening probability.
Evolution II's political-family share has the existing 85:15 nested pressure/violence split, giving approximately 4.35% and 0.77% overall opening shares.
Actor, evidence class, readiness layer and low initial risk are prepared before exactly one family report is dispatched, with recovery set for the immediate operation branch.
The initial pattern and operation are mutually exclusive, and all four scenarios retain positive alternatives.
The auditor's single Event 011 probability-inspect attempt was stopped while pending, so these calculations are source evidence and not an MCP or live-game result.
Later pulse timing and actor-selection probabilities were not recalculated because neither changed in C10.
No source defect remained in the requested opener after this review.

Skills used: `chaos-redux-events`, `chaos-redux-ai-strategies`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`.
No skills were created or updated.
