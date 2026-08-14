# IW-050 Komi Administration-Standard Cost Localisation Re-Audit

Date: 2026-08-14

Mode: read-only source audit of HEAD `8b1aaeaae` after the owner-applied Komi cost/localisation patch.

## Disposition

The patch is source-backed and complete for the requested six Komi administration-standard projects. No gameplay source, central admission, deterministic Join, or unrelated file was edited by this audit. The audit handoff itself is committed separately as `d84816ecc`.

The six projects now use `independence_wave_komi_cost_administration_standard` for their player-facing cost text and retain the one-factory reservation. The canonical package value is `independence_wave_komi_cost.civilian_factory_use = 1` in `common/script_constants/006_independence_wave_komi_constants.txt:31-34`; the decision file's `@CR_SC_INDEPENDENCE_WAVE_KOM_CIVILIAN_FACTORY_USE = 1` mirror is intentional because the `modifier` field rejects the shared `constant:` token form. The mirror and canonical value agree.

## Six verified projects

| Project | Current source span | Trigger/payment | Cost display and reservation |
| --- | --- | --- | --- |
| `independence_wave_komi_integrate_rail_guards` | `common/decisions/006_independence_wave_komi_decisions.txt:85-101` | Komi administration-standard affordability and `independence_wave_decision_pay_administration_standard` | Komi administration-standard base key plus `@CR_SC_INDEPENDENCE_WAVE_KOM_CIVILIAN_FACTORY_USE` |
| `independence_wave_komi_register_komi_communities` | `:102-118` | Komi administration-standard affordability and shared administration-standard payment | Komi administration-standard base key plus the one-factory mirror |
| `independence_wave_komi_ratify_constitutional_autonomy` | `:136-152` | Komi administration-standard affordability and shared administration-standard payment | Komi administration-standard base key plus the one-factory mirror |
| `independence_wave_komi_adopt_taiga_land_compact` | `:153-169` | Komi administration-standard affordability and shared administration-standard payment | Komi administration-standard base key plus the one-factory mirror |
| `independence_wave_komi_convene_rail_councils` | `:170-186` | Komi administration-standard affordability and shared administration-standard payment | Komi administration-standard base key plus the one-factory mirror |
| `independence_wave_komi_codify_durable_sovereignty` | `:203-242` | Komi administration-standard affordability and shared administration-standard payment | Komi administration-standard base key plus the one-factory mirror |

The current working-tree diff changes exactly the six `custom_cost_text` assignments at source lines 92, 109, 143, 160, 177, and 222 from the generic `independence_wave_cost_administration_standard` key to the Komi-specific key. The existing `custom_cost_trigger`, payment effect, project duration, route requirements, active-project serialization, and cancellation behavior remain unchanged.

## Stale findings versus live issues

The historical finding that Komi administration-standard projects displayed the shared two-factory cost is resolved by `8b1aaeaae`; no generic administration-standard key remains in this Komi decision file. The earlier strategic-project display/reservation mismatch is stale after `85f5c9778`, `9e52e1eaf`, and `ffc303781`: strategic projects now use the Komi strategic triplet, reserve the same one-factory mirror, and display the canonical Komi factory constant. The earlier origin-ended readiness/cancellation concern is stale after `85f5c9778`. The durable-sovereignty, emergency resource-gate, and codify wording/tooltip findings are stale after `b8aa313a8`.

No live cost or cost-localisation defect remains in the current Komi source. The former-host partial-success wording and the package's central admission/Join boundary remain separate owner/design or authority issues; they are outside this cost/localisation patch and do not justify a narrow source edit here.

## Localisation verification

`localisation/english/006_independence_wave_komi_l_english.yml` contains the complete triplet at lines 58-60:

- `independence_wave_komi_cost_administration_standard`
- `independence_wave_komi_cost_administration_standard_blocked`
- `independence_wave_komi_cost_administration_standard_tooltip`

Each triplet value displays command power, manpower, and `£civ_factory`, and each references `[?constant:independence_wave_komi_cost.civilian_factory_use|0]`, so the displayed factory burden is the canonical one-factory value. The normal and tooltip forms use the yellow presentation; the blocked form uses the red presentation.

The Komi source has ten `custom_cost_text` lines across its ten timed projects. Its four unique cost references are the shared administration-light and security-standard keys plus the Komi administration-standard and strategic keys. Cross-checking the Komi and shared English localisation files found zero unresolved references. The Komi source has zero remaining `custom_cost_text = independence_wave_cost_administration_standard` references. The Komi localisation file has a UTF-8 BOM and no duplicate localisation keys.

The strategic triplet is also present and canonical at lines 55-57, while the light and security projects intentionally retain their existing shared cost keys. Those are outside the requested six-project administration-standard patch and were not changed.

## Lifecycle, AI, and route notes

All six projects remain serialized by `NOT = { has_independence_wave_komi_active_package_project = yes }`, retain their package and capital-control requirements, and pay through the existing shared administration-standard effect. The patch changes only the displayed cost key; it does not alter payment timing, cancellation failure, route gates, duration, or cleanup.

The mandatory `mission_ai_will_do` probability inspection of the unchanged Komi decision AI surface returned `PROBABILITY_SOURCE_INSPECTED` with 11 candidates, 15 required inputs, zero inspect-unresolved items, and `poolComplete = false`. The cost/localisation commit changes no AI factor, so no balance or normalized selection claim is made. The ordinary Komi decision category has no decision-owned scripted GUI; GUI inspect/render/rewrite is not applicable to this cost-localisation-only audit.

KOM remains package-local and fail-closed for central attestation, dispatcher, scenario preflight, and deterministic Join admission. This audit does not widen any of those boundaries.

## Evidence and validation

Static current-source audit results:

- Six administration-standard project blocks each contain the Komi administration-standard affordability trigger, Komi base cost key, one-factory reservation mirror, and administration-standard payment effect.
- Canonical script constant: `independence_wave_komi_cost.civilian_factory_use = 1`.
- Decision-file mirror: `@CR_SC_INDEPENDENCE_WAVE_KOM_CIVILIAN_FACTORY_USE = 1`.
- Standard cost localisation triplet: 3/3 keys present and all 3 reference the canonical Komi factory constant.
- Unresolved custom-cost references against Komi plus shared English localisation: 0.
- Stale generic administration-standard references in the Komi decision source: 0.
- Duplicate Komi localisation keys: 0; UTF-8 BOM: present.

Current probability artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d74a98d1c9657221289f5051d855a5f0d38dd0896fd522916d7b0c3cb6c8c1e/9cde575c8b7f4b6adf381aac803a17cb72a2d036d94b5bb2840dab440defbb6d/probability-inspect-4df0d448dadb.json`.

Live HOI4 execution, save/load, and in-game visual inspection were not claimed. No source edits were made by this auditor; the owner-applied decision/localisation diff in `8b1aaeaae` remains the only gameplay change under review.
