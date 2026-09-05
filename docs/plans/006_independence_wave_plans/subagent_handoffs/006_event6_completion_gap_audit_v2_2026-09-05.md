# Event 006 completion-gap audit v2

Date: 2026-09-05.

Scope: read-only completion audit of the current Event 006 Independence Wave implementation, with priority on narrow source-provable gameplay or wiring defects that do not widen package admission, invent identity or rights evidence, introduce fallback assets, or weaken the absolute no-pre-event contract. No gameplay, AI, event, decision, focus, asset, localisation, spreadsheet, or runtime file was changed by this audit.

## Completion status by surface

| Surface | Status | Current evidence |
| --- | --- | --- |
| Root event, allocation, release, reports, cleanup | Partial | Static allocator, flag, country API, FORM-16, and scenario-matrix audits pass. The current focused Event MCP routes remain partial and do not prove helper-expanded release, transfer, rollback, report delivery, save/load, or live behavior. |
| Package registry and country content | Blocked | Current authority remains 32 content-attested selectable packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows. IW-095 remains package-local and centrally unadmitted. |
| IW-095 AI strategy wiring | Incorrect and blocked | Three AI strategy activation predicates read flags that no package effect writes. The exact source correction is deterministic, but the mandatory probability analyzer exposes no comparable `ai_strategy_factor` surface. |
| Decisions, missions, focuses, ideas, League, formables, achievements | Partial | Existing source and dated handoffs establish substantial bounded implementation. This audit found no second narrow non-weighted defect that could be patched without reopening accepted design or admission boundaries. |
| Assets and documentation | Partial | IW-095 identity, portrait roster, flag, FORM-24, and super-event rights evidence remain blocked. The current source-of-truth and resume references are reconciled below to the three-flag finding; no asset fallback is authorized. |

## Concrete source defect

The IW-095 Dahomey package uses unprefixed `independence_wave_dah_*` lifecycle receipts, but three AI blocks use nonexistent `independence_wave_iw095_dah_*` variants:

1. `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:3648`, inside `independence_wave_iw095_dahomey_host_restraint`, checks `independence_wave_iw095_dah_host_ledgers_settled`. The package writes and clears `independence_wave_dah_host_ledgers_settled` in `common/scripted_effects/006_independence_wave_first_footprint_package_effects.txt:308,346,459`, and `iw095_settle_former_host_ledgers` reads that same canonical flag in `common/decisions/006_independence_wave_decisions.txt:4117`.
2. `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:3661`, inside `independence_wave_iw095_dahomey_settled_compact`, checks `independence_wave_iw095_dah_compact_stabilized`. The compact lifecycle writes and clears `independence_wave_dah_compact_stabilized` in `common/scripted_effects/006_independence_wave_first_footprint_package_effects.txt:44,48,451`.
3. `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:3676`, inside `independence_wave_iw095_dahomey_emergency_directorate`, checks `independence_wave_iw095_dah_emergency_government`. The emergency-government installer and cleanup write and clear `independence_wave_dah_emergency_government` in `common/scripted_effects/006_independence_wave_first_footprint_package_effects.txt:223,349,462`.

Repository-wide source search found no writer for any of the three `independence_wave_iw095_dah_*` variants. Therefore the host-restraint strategy does not stop when the canonical settlement receipt is written, while the settled-compact and emergency-directorate strategy layers cannot activate from their actual package receipts.

The package-local implementation handoff states that the four IW-095 AI layers are intended to operate after the identity and setup gates, and the accepted first-footprint addendum includes the matching former-host and government-settlement mechanics. Correcting these three identifiers does not add a carrier, package adapter, content attestation, preflight, Join row, SCN-008 row, identity receipt, flag, portrait, formable member, or pre-event visibility path. The existing `allowed`, package, setup, identity, and route gates remain intact.

## Proposed owner patch

In `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`, change only the three activation flag tokens:

```text
NOT = { has_country_flag = independence_wave_dah_host_ledgers_settled }
has_country_flag = independence_wave_dah_compact_stabilized
has_country_flag = independence_wave_dah_emergency_government
```

Do not change the AI strategy values, route conditions, package gates, identity gate, setup gate, central admission, or any asset surface.

## Mandatory probability blocker

The required `chaosx_ai_probability_auditor` pass used `hoi4.probability_inspect` with `adapter = ai_strategy_factor`. It returned `status = ok`, `code = PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason = no_weighted_surfaces`, zero candidates, zero available candidates, zero required inputs, zero unresolved inputs, source revision `4ac308c8efe9b10bbb6b5836a9d392bd36de637d0185311de404dea9b43d658f`, and source hash `b1ffe02504cebe5c75fba1b7d2ecec44a28e4540ee33ed9b7fbab9aaf6a7c751`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79a511afe6f5d734ad046cc0166f8ee9106f34cfe7ca68adec8c28923af1bdc7/e8bceeacc1f732a5b3ac1ed3234ae7d0ecd3f67af16937f596e289f39f159f50/probability-inspect-b1ffe02504ce.json`.

`hoi4.probability_evaluate`, `hoi4.probability_sweep`, a path-only `hoi4.probability_compare`, and a direct in-memory before/after comparison all returned `PROBABILITY_SURFACE_EMPTY` with `No weighted blocks matched this request` and no available adapters. No comparison id, artifact, scenario hash, factor result, ranking, or probability result exists. The named scenario declarations were `IW095_DAH_HOST_LEDGER_FLAG_BASELINE_2026_09_05` and `IW095_DAH_HOST_LEDGER_FLAG_COMPARE_2026_09_05`.

Disposition: the three-token correction is source-provable and mechanically bounded, but it remains `blocked` under the repository's mandatory weighted-logic contract until the installed analyzer can expose and compare this `ai_strategy_factor` surface. This audit does not authorize bypassing the comparison requirement.

## Event MCP evidence and limits

A fresh `hoi4.event_inspect` lint and `hoi4.event_render` overview used selector `{ kind: event, eventId: chaosx.nr6.1 }`, helper expansion, and the current working source. Both returned partial evidence at revision `2e8079f82e18675c419eb9da801ecfaf12495e0e77986c6be7b615dc1950b893` and graph hash `3ed2cf337d5d05c8ffdc9e66f538f05f68d93bb266154dbf8847f37e846e1b5a`. The render layout hash is `340071ffd5797720635ee88ef724d794ec40a8b419d505221944ec59b8ab1bb8`.

- Inspect: `EVENT_INSPECTED_PARTIAL`, focused mode, 2,199 diagnostics, one blocking diagnostic counted by the report, and failed validation because large-workspace helper projections and lifecycle passes were deferred. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/26afc7587979f11f7fca63c232ec014b863952c6146422734af9c82caacedc03/03246ac61ec7c30493ffc090dc79ef996fe085ffc93fc860608f07d1c9a0dc54/event-lint-2e8079f82e18.json`.
- Render: `EVENT_RENDERED_PARTIAL`, focused mode, five selected nodes and 42,532 omitted nodes, with the same deferred-analysis validation limit. Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1dbc848b11c5b8494480498d222bd03ef40c481db99fbc1610d105e1f42b7d3e/cc736161e0f978135b65284a327aecce86712a749e7789c5cc1589dce6f66c5a/event-overview-2e8079f82e18-manifest.json`.

No event-source revision was proposed or written, so an Event Chain Viewer `hoi4.event_compare` is not applicable to this read-only audit. The probability before/after comparison was attempted separately and is blocked as recorded above. Source review is not treated as equivalent engine evidence.

## Accepted-plan disposition

- `docs/plans/006_independence_wave_plans/006_event6_first_footprint_admission_improvement_addendum_2026_08_26.md`: `accepted and queued` for the broader cohort; IW-095 package-local mechanics exist, but central admission remains blocked by identity, portrait-roster, flag, FORM-24, package, probability, and engine evidence.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw095_dahomey_package_local_implementation_2026-08-27.md`: `implemented` only at package-local source scope; its claim that four AI layers exist is narrowed by the three broken receipt predicates found here.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_dahomey_ai_flag_audit_2026-09-05.md`: remains valid for the first host-ledger mismatch and its earlier empty probability surface, but is incomplete for current completion tracking because it did not record the settled-compact and emergency-government mismatches. This v2 handoff supplements it; it does not supersede its original artifact.

## Meaningful validation

The following current static audits passed without changing source:

```powershell
python .tools/audit_event6_flags.py
python .tools/audit_event6_allocator.py
python .tools/audit_event6_country_api.py
python .tools/audit_event6_form16.py
python .tools/audit_event6_scenario_matrix.py
```

The allocator remains at 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 adapters, 32 content attestations, 29 compatible groups, and the exact 3/4/5/7/10 wave ladder. The scenario matrix passed 32 cells and eight edge cases. These static checks do not detect the three AI flag mismatches and do not replace probability or live behavior evidence.

After a future owner is able to obtain a valid same-scenario AI comparison, validate the exact identifier closure with:

```powershell
rg -n "independence_wave_(iw095_)?dah_(host_ledgers_settled|compact_stabilized|emergency_government)" common/ai_strategy common/scripted_effects common/decisions
```

The expected post-patch result is zero `independence_wave_iw095_dah_*` reads and preserved canonical package writers/readers.

## Remaining blockers and next actions

1. Extend or repair the installed HOI4 probability analyzer so `ai_strategy_factor` exposes the three named IW-095 strategy blocks, then rerun the same named baseline and direct before/after comparison before applying or promoting the three-token patch.
2. Keep IW-095 centrally unadmitted. Its 1936 identity, complete sourced portrait roster, defensible rights-cleared flag, FORM-24 membership contract, and complete engine evidence require user/parent evidence and cannot be synthesized by this source repair.
3. Preserve the 32/29/40/161 `HOLD / PARTIAL` boundary and absolute no-pre-event contract.
4. If the AI patch is later applied, write a new owner handoff with the exact diff, probability comparison artifact, repeated static audits, and current source revision. Do not claim live-game proof.

No simplification or fallback was introduced by this audit.
