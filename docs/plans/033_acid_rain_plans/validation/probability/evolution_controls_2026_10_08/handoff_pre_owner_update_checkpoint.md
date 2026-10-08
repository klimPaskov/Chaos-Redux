# Event 033 evolution controls: pre-F5 probability checkpoint — 2026-10-08

Status: pre-edit immutable source and explicit scenario contracts established; live MCP probability coverage still pending; F5 owner patch and mandatory matching comparison remain outstanding.
This is a bounded checkpoint, not a probability pass, native disable-control proof, or final F5 completion claim.

## Ownership and source identity

Auditor mode is read-only/report-only.
The parent owns all gameplay edits, source validators and final integration; the user owns live-game validation.
No gameplay, constants, weights, costs, timers, CSV, workbook, assets, tools/packages or commits were changed by this audit.
The completed region-policy audit remains historical and was not rerun.

All paths below are relative to `docs/plans/033_acid_rain_plans/validation/probability/evolution_controls_2026_10_08/`.

| Snapshot | Raw SHA256 | Bytes |
| --- | --- | --- |
| before-source/common/scripted_effects/033_acid_rain_effects.txt | e455292b55d0443abb234a00506b9501b02f8c2a8df5afe298ff855f56cb406f | 356142 |
| before-source/common/script_constants/033_acid_rain_constants.txt | 58deff691f6e43f7de79cf60a5757dfdcb9e003b77d7104bd064ec7a5a83137c | 35084 |
| before-source/common/scripted_triggers/chaosx_settings_triggers.txt | e36b9e785fc109032514501af464d4331eeec8fce2fd88a620fb0739f22a2b70 | 18894 |
| logging-bridge_94c0c9d3/common/scripted_effects/033_acid_rain_effects.txt | 94c0c9d3c8b8b63f57878033648bb71b1f34ac89739d279a299ec3f163c1a510 | 356300 |

E455 was recovered directly as raw Git blob bytes from commit `03447df6c5e4226525d2c26dc450f103d2297e78`, not from the live 94C0 file.
The initial Git archive export converted LF to CRLF, producing CE7EC4BF…93AD47; its tar and extracted bytes remain preserved in the audit area as rejected export evidence, never relabelled E455.
The exact raw E455 Buffer was checked against the required SHA before writing a fresh, non-overwriting snapshot.
The three requested sources plus six bounded supporting files are recorded in `source_manifest.json`.
Supporting files are current captured dependencies, not a full historical workspace reconstruction.
`logging_bridge_scope_receipt.json` proves byte-for-byte equality with E455 after removing exactly the two added logging-context assignments; it proves no other source change between these two snapshots, not native logging UI behavior.
The live runtime was rechecked at this checkpoint and still hashes 94C0…A510.

## Named saved fixtures

| Fixture | SHA256 | Contract |
| --- | --- | --- |
| scenario_contracts_E455_v2.json | cbe062db33aa23dd53d12f8b2bf8b9fb028b066c9b6118a408d0cb424e341ffa | 24 formation masks and 21 named live/lifecycle cases |
| conditional_chance_scenarios_E455.json | 8cbe4cbe881395a553a1d84d438a0fa4cac15b65fcda2cc8f34cce0dda6d74a4 | 32 paired enabled/disabled arithmetic-conditioned roll cases |
| conditional_roll_manifest_E455.json | 3a07a5959da20e1f7c940d8c79a0a94607c7fbf39f812dc7acea4716d995ae8d | Two independent scalar roll families; not native gate eligibility |
| chance_arithmetic_E455.json | 1df44cddc08d1d8017ff454a6f6beee47dfc2e5f0c977d88d63ac5057e31edd9 | Authored terms, source mapping, inputs and clamp derivation |

The formation IDs are `F400_M000` through `F400_M111`, `F600_M000` through `F600_M111`, and `F800_M000` through `F800_M111`.
Mask order is I/II/III; 1 means enabled and 0 means the actual native disable flag is present.
Lifecycle IDs cover `L1..3_enabled/disabled_notice`, `P1..3_disable_on_due`, `R1..3_reenable_after_cancel`, queued cell forecast, committed cell/front/global histories and endpoints, lower-Chaos retention, global-disabled ordinary coverage and direct disabled global commit.
The probability cases are `W01..W16`, each suffixed `_enabled` and `_disabled`; each provides both numeric authored chance inputs explicitly.
Version1 of the source-contract fixture remains preserved but is superseded by version2: the stage-III due field was corrected to the actual `global.acid_rain_global_warning_day`.
Do not use version1 as an executable fixture.

The flags are sourced from the frozen shared settings trigger and toggle effect, not arbitrary model controls:

- events_log_disabled_evolution_33_33_1
- events_log_disabled_evolution_33_33_2
- events_log_disabled_evolution_33_33_3

Required effect-time context is event ID33, evolution type33, stage1/2/3 and its corresponding tier1/2/3.
The shared enabled trigger additionally tests current display-tier minima 200/400/600.
These are not Event033's authored formation/admission thresholds 400/600/800.
Dates are explicit synthetic date units, one day = 24/100000; days were not placed directly into global.date.

## Baseline source findings

E455 formation ignores all three native evolution-disable flags.
Seventeen of the 24 named masks conflict with the accepted enabled-stage branch contract: four at400, six at600 and seven at800.
This count concerns authored branch admission only; actual stage-II region assignment is not claimed.
The baseline also lacks a current shared enabled check at stage-I notice admission/due unlock/severe-roll admission, stage-II split notice/due commit/third-front roll admission, and stage-III notice/due commit.
The global commit effect itself only checks that the global layer is not already active before mutations and impact receipt.

Disabling a pending global warning needs both cancellation and a return to regional processing; merely wrapping the pending commit while leaving global_warning phase would freeze ordinary coverage.
Already active cells, committed fronts, histories, impact receipts and natural endpoints must remain processed after disable or lower Chaos.
The full host worker and cell-maintenance helper must not be blanket-gated.

The queued severe-cell forecast is a distinct commitment boundary: targets are reserved while active_entries=0.
Its cancellation/retention policy must be explicit in the owner patch and reviewed against the accepted scope.
These fixtures do not infer that native behavior from scalar weights.
Exact native state/front/coverage/receipt ledgers are omitted per case rather than defaulted.
Existing A11/A15 missing30facts remain unresolved.

The unchanged authored conditional severe chances in the W fixtures span0–25 percent and third-front chances20–50 percent.
The source draw is integer min1/max101 exclusive with acceptance <= chance.
Severe extreme intensity also receives the strong bonus; the prior-cell penalty is keyed to global cell count.
The third-front source intensity bonus is OR over slots1/2, applied once even when both are strong.
These are arithmetic derivations from authored source, not balance choices or observed native results.
Gate denial means no draw; it must not be conflated with changing or renormalizing the conditional chance.
Successful severe target creation and actual third-front assignment require downstream pool/state facts beyond a successful roll.

## Live route receipts and active handles

The first required `hoi4.probability_inspect` was dispatched against logical runtime path plus snapshotPath and expected E455 hash.
Its terminal receipt `r01_probability_inspect_result.json` is a 600-second client tools/call timeout, SHA256 `29d2a686444492667ccba083e3cc59bc9341228b11536e4baddc8488650bd7f0`.
Backend completion is unknown; this is not a failed probability result, analyzed result or pass.
After that terminal client result, r05 genuinely narrowed the request to the single saved severe draw at E455 line4501.

As of 2026-10-08 07:45:21 UTC, the following client exec cells were just re-observed as active:

| Receipt | Tool | Confirmed active cell | Scope |
| --- | --- | --- | --- |
| r05 | hoi4.probability_inspect | 31 | Saved severe draw line4501, E455 frozen source |
| r06 | hoi4.probability_inspect | 35 | Distinct two-family arithmetic-conditioned declared pool |
| r04 | hoi4.reference_search | 28 | Exact random-draw documentation query |
| r07 | hoi4.event_inspect | 38 | Only chaosx.nr33.111, depth1, six-node/eight-edge bound |

No backend job handle was returned and no job capability has been assumed.
No requests were duplicated on observer timeout.
The scripts preserve terminal result receipts when they return.
r02 was a terminal schema rejection for question length above160 characters; r03 was the bounded corrected request and returned OK.
r03 retained omittedSources and is not full documentation coverage.
The relevant installed random/flag/comparator/meta-trigger sections and offline wiki random/temp-variable/date/flag sections were read directly as well.
Installed direct_random extraction code recognizes `random={chance=...}`, not Event033's saved `set_variable_to_random` plus subsequent comparator.
This is an identified adapter scope limit, pending actual narrower live response.
There is currently no successful completed probability inspection, evaluate, render or comparison certificate for F5.
Evaluation/render remain queued behind their matching successful inspection.
The event inspection is live current-source structure, not an E455 historical workspace execution.

## Required owner-after comparison

Send the exact owner F5 after hash/source before comparison.
The auditor will freeze separate raw after bytes without modifying any before file.
Retain the same named fixture IDs/facts and verify constants plus authored chance equations, draw bounds, weights, costs, durations and impact receipts against actual after source.
Run mandatory matching probability_compare through the supported live schema; never self-compare or substitute the 94C0 logging bridge for an F5 after patch.
If only declared conditional pools are supported, classify that compare as local conditional probabilities only, with native control binding, helper lifetime, downstream pools and lifecycle closure explicitly unresolved.
The source/lifecycle contract baseline is available for owner implementation now; the full assigned probability audit remains open.

Skills used: chaos-redux-subagents and chaos-redux-events.
They enforced the read-only auditor/owner boundary, frozen snapshot logical source mapping, retained evidence/active-handle discipline and mandatory owner-applied matching comparison.
No skills were changed.

