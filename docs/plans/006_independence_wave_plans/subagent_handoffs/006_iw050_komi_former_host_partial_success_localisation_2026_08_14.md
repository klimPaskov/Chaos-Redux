# IW-050 Komi former-host partial-success localisation clarification

Date: 2026-08-14

## Scope

This handoff records a localisation-only clarification for the package-local `independence_wave_komi_settle_former_host_ledgers` project. No central dispatcher, content attestation, preflight, deterministic Join, portrait, flag, workbook, decision availability, timer, cost, or AI surface was changed.

## Source/effect alignment

The decision remains available only while the former host is living and not at war, but the host can become invalid during the 75-day timer. The existing effect `independence_wave_komi_focus_settle_former_host_ledgers` still raises Congress Cohesion and Taiga Readiness, while it calls `independence_wave_komi_apply_former_host_settlement` only when `has_independence_wave_komi_unsettled_host` is false. Therefore the local Komi ledger outcome can succeed while the bilateral external settlement remains unresolved.

The updated strings are:

- `localisation/english/006_independence_wave_komi_l_english.yml:40` — the project description now states that bilateral settlement is recorded only when the former host remains available and at peace, and that the Komi ledgers still advance without resolving external claims when the host is lost or returns to war.
- `localisation/english/006_independence_wave_komi_l_english.yml:64` — the effect tooltip states the same conditional bilateral outcome alongside the two ledger increases.

The localization file retains its UTF-8 BOM. The wording describes existing behavior; it does not introduce a new recovery or settlement rule.

## Current weighted-surface receipt

A fresh mandatory `hoi4.probability_inspect` on `common/decisions/006_independence_wave_komi_decisions.txt` with adapter `mission_ai_will_do` returned `PROBABILITY_SOURCE_INSPECTED`, source revision `305a3948864ace3a0facb3190b6d7d10198123cc882bdbdfffb8f8bd5e080362`, source hash `4df0d448dadba7dbfbf8d0f33c07fe08fce8cf941788548dc21cdcda8d6623ad`, eleven candidates, zero available candidates, fifteen required inputs, and zero unresolved inspect diagnostics.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/54eef1084a20844ca59fae8a58986d746d29c93061f8ee0537c737fca1f580ce/fdba42ec8442bb54082fc6ded1c5ddb5ac0a3b5b1c8d90222e47d1657608894c/probability-inspect-4df0d448dadb.json`.

Because only localization changed, this receipt does not support a before/after probability or balance claim.

## Remaining boundary

IW-050 Komi remains package-local and fail-closed outside the current central admission/Join authority. Its broader identity, flag, portrait, map/formable, and central attestation gates remain documented in the current package admission handoffs.
