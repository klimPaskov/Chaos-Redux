# Chaos Warfare documentation cleanup handoff

This handoff lists documentation contradictions and stale statements found while closing the CBRN implementation surface.

This reconciliation is bounded to the five user-authorized Markdown surfaces named in the task. Gameplay, localisation, assets, GUI, and spreadsheets are outside the patch scope, and broader system-document cleanup remains queued rather than silently treated as complete.

## Superseding core-first disposition

The user subsequently authorized unsupported content to be skipped so the supported core mechanics can close without proxies or fallbacks.

- Ground Chemical operations and continuous Chemical air missions remain inactive behind verified-current-version hooks. The separate legacy selected-state occupation operation is also inactive, but nerve-agent camp suppression is supported through Gas-Chamber Saturation Drills and the existing camp transaction.
- `Air Is Still Breathable`, `No Wind Is Friendly`, `The Antidote Arrived`, and `Unbroken Supply Corridor` were removed from the active achievement registry because their exact required receipts are unavailable.
- Hardened Mobile Plant was removed rather than replaced with a reliability, cost, bombing-loss, or capture-loss approximation.
- Historically sourced unique national MIO names and exact live production-share claims are skipped as non-core work. Generic functional MIO families and route-aware AI remain active.
- These items are explicit omissions, not open core blockers. Earlier blocker language below records the pre-disposition audit and is superseded where it conflicts with this section.

## Bounded reconciliation result

| Surface | Disposition | Current result |
| --- | --- | --- |
| `2026-07-13_requirement_traceability_and_migration_ledger.md` | reconciled | Current source/audit statuses, plan dispositions, and achievement blockers are recorded. |
| `documentation_state.md` | reconciled | Current CBRN implementation state, achievement receipts, engine boundaries, and unresolved risks are recorded. |
| `documentation_cleanup_handoff.md` | reconciled | Source-of-truth map, contradiction list, stale-instruction list, dispositions, and parent decisions are recorded here. |
| `completion_audit_checklist.md` | reconciled | Exact source-audited items, fail-closed achievements, queued work, and user-owned validation are distinguished without false completion boxes. |
| `2026-07-29_stage_14_package_scenario_evidence.md` | reconciled | Scenario status is precise and the achievement reachability audit is added without claiming runtime validation. |

## Current source-of-truth map

1. The twelve numbered specifications under `docs/specs/chaos_warfare_system_specs/specs/` remain authoritative.
2. The ten accepted matrices under `docs/specs/chaos_warfare_system_specs/matrices/` provide implementation mappings and tuning constraints after the numbered specifications.
3. The specialist prompts under `docs/specs/chaos_warfare_system_specs/prompts/` provide bounded implementation guidance after the specifications and matrices; unsupported prompt items are omitted under the later core-first user disposition rather than approximated.
4. Current gameplay source is evidence of existing contracts, not permission to invent missing hooks, proxies, estimators, neutral receipts, or fallbacks.
5. The named Stage 5, Stage 6-10, decision/mission, country-profile, improvement-loop, and Stage 14 reports are audit evidence with the dispositions below; they do not override the numbered specifications or make live validation claims.

## Unresolved plan and handoff disposition

| Evidence or plan | Disposition | Reason or remaining work |
| --- | --- | --- |
| `2026-07-14_stage_5_completion_audit.md` | promoted as local evidence | Stage 5 doctrine and balance tranche passed its bounded audit; it does not close package completion. |
| Stage 6 chemical migration and doctrine addenda | core implemented; unsupported routes omitted | Doctrine potency and Condemnation boundary is implemented; ground Chemical exact HQ/weather/terrain operations and continuous air remain inactive without verified hooks. |
| Stage 7 biological lifecycle and route validations | promoted as bounded evidence | Native raids, operative release, battlefield dissemination, sabotage, bounded historical decisions, doomsday, countermeasures, potency hierarchy, and agent-neutral native raid odds are recorded; final package scenarios remain open. |
| Stage 9 decision/mission audit | historical bounded evidence, superseded for nerve suppression | Supported decision/mission surfaces passed the scoped audit. The later camp integration supplies the accepted playable nerve-agent route; only the separate legacy occupation operation remains inactive. |
| Stage 10 AI/country handoffs | core implemented; non-core identities skipped | Country profiles, route-aware AI, generic MIO families, and MIO visibility are source-audited; exact live production shares and historically sourced unique national MIO identities are not claimed. |
| `2026-07-29_near_completion_improvement_loop_closure.md` | accepted closure; no new addendum | Broad expansion is closed, and no estimator, proxy, neutral receipt, fallback, or scope reduction is authorized. |
| `2026-07-29_stage_14_package_scenario_evidence.md` | promoted as source evidence | Deterministic supported-core scenarios and AI score evidence are recorded; unsupported scenarios and achievements are explicit omissions. |
| `subagent_handoffs/2026-07-29_package_decision_mission_audit.md` | promoted as bounded evidence | The bounded decision/mission surface passed its audit without closing the package. |
| `subagent_handoffs/2026-07-29_package_country_profile_audit.md` | promoted as bounded evidence | The actionable AI migration finding was fixed; exact live shares and unique national MIO identities remain unresolved. |
| Older Stage 7 reports that retain superseded legacy-caller wording | left unchanged; later migration evidence supersedes the stale paragraph for current status | No out-of-scope report was rewritten or deleted in this pass; the parent should use the later legacy-migration validation when resolving that contradiction. |

## Achievement reachability findings

- `Quarantine Without Collapse` is promoted to implemented and source-audited. `cbrn_achievement_refresh_bio_containment_receipt` reads current and needed trucks and trains through exact `get_supply_vehicles_temp` receipts, applies the 0.80 `minimum_supply` threshold to each class, and writes `cbrn_achievement_outbreak_supply_ready_history` only at exact catastrophic-outbreak recovery. The completion trigger requires that receipt, with no periodic estimator or building proxy.
- `No Wind Is Friendly`, `The Antidote Arrived`, `Unbroken Supply Corridor`, and `Air Is Still Breathable` are explicit unsupported omissions. Their exact receipts are unavailable, so they have no active registry, trigger, localisation, or GFX entry and do not block supported-core playability.
- The starting-eligibility finding is resolved in source. The one-time startup transaction writes `cbrn_achievement_start_country_eligible`, `cbrn_achievement_starting_major_power`, and `cbrn_achievement_starting_civil_defence_profile` after accepted profiles; the common eligibility trigger requires the first receipt, `A Mask for Every Door` requires the civil-defence receipt, and registry `possible = always yes` remains presentation-only.
- `A Poisoned Victory` now requires current Condemnation at or above `constant:cbrn_achievement_threshold.minimum_active_condemnation` rather than only a historical peak; it is source-audited but remains subject to the package reachability audit.

## Contradictions resolved

- Doctrine wording now consistently says that doctrine increases CBRN potency and only mitigates Condemnation; it does not create, authorize, or conceal camp/genocide infrastructure or erase evidence, attribution, deaths, contamination, medical load, resistance trauma, history, or responsibility.
- Continuous air remains fail-closed without an estimator, and selected-state native raid results are not described as fabricated weather or terrain measurements.
- Biological potency is documented as Tularemia < Anthrax < Plague < Smallpox, with only Smallpox severe; native raid success factors remain agent-neutral.
- Biological delivery routes retain native raids, exact-state operative release, bounded sabotage, bounded historical decisions, and the doomsday decision, with existing military raid assets preserved.
- CBRN-private helper ownership remains in CBRN-specific subsystem files and is not moved into shared dynamic registries merely for documentation convenience.
- Native decision-category presentation is accepted; window-only animation concepts are not described as missing implementation because no accepted consumer exists.

## Contradictions still open

- Ground Chemical exact-state HQ/weather/terrain receipt remains unavailable.
- The legacy selected-state occupation operation lacks exact weather, terrain, and target-loss receipts. The accepted camp nerve-suppression route is implemented independently and does not infer those inputs.
- Hardened Mobile Plant lacks an exact bombing/capture equipment-loss transaction.
- Historically sourced unique national MIO identities remain unresolved.
- Precise live production shares, long-run AI pacing, and user-owned runtime validation remain unresolved.
- The four unsupported achievement proposals remain omitted; no proxy receipts or narrowed eligibility definitions are permitted.

## Duplicate, superseded, and stale instruction list

- Older system documents named in the required cleanup order remain queued because they are outside this bounded patch; they must not be treated as current merely because this handoff references them.
- The older Stage 7 countermeasure report's legacy-caller limitation is superseded for current source status by the later legacy-biological-migration validation, but the older report remains unchanged.
- The achievement prompt's four unsupported entries are superseded by the later user-authorized supported-core omission. The eleven retained achievements still use their exact starting and campaign receipts.
- The asset prompt's optional window-animation concepts have no accepted consumer under the native category decision; no stale prompt is authorized to expand the GUI surface during this pass.

## Recommended parent decisions

1. Supply an exact current-version ground Chemical, legacy occupation-operation, or bombing/capture transaction receipt before reopening those omitted surfaces.
2. Reopen any of the four omitted achievements only if its exact required receipt becomes available; no proxy or narrowed replacement is authorized.
3. Decide whether historically sourced unique national MIO identities and precise live production shares are required for a later non-core tranche; no generic substitute is being promoted as equivalent.

## Proposed cleanup if patching is not allowed

Patching is allowed for the five named surfaces and was applied there. No deletion, archival, gameplay edit, localisation edit, asset edit, GUI edit, or spreadsheet edit is proposed in this pass. Future cleanup of the broader system documents should use the source map and dispositions above.

## Queued broader cleanup order outside this pass

1. Reconcile `docs/systems/cbrn_chemical_delivery.md` with the canonical chemical-state ledger, targeted continuing-death events, the doomsday batch adapter, and the current route list.
2. Reconcile `docs/chemical_warfare/chemical_warfare_documentation.md` with the current doomsday Condemnation tuning and the inactive legacy support/cylinder paths.
3. Reconcile `docs/systems/cbrn_designers.md` with the current selected-state raid gate, the grant-only aircraft module boundary, and the explicit Hardened Mobile Plant engine limitation.
4. Check the biological lifecycle, countermeasure, Japan campaign, and biological sabotage documentation against the four-agent potency hierarchy and the agent-neutral native raid success factors.
5. Check every specialist prompt and implementation-stage report for wording that implies an estimator, a broad periodic pulse, an unapproved fallback, or doctrine control over camp creation or responsibility.
6. Update the completion audit checklist and requirement traceability ledger only after each item has evidence in source files or an explicitly recorded engine limitation.

## Broader contradictions queued for a later pass

- The chemical delivery system documentation still lists biological actions and nerve suppression as pending even though their route adapters now exist; it should describe them as separate exact delivery adapters and retain only their genuine engine-boundary limitations.
- The chemical warfare documentation still describes doomsday Condemnation as a 40-point base with an 80-point stock-scaled cap, while the active doomsday adapter uses the centralized accepted 150-to-500 batch range.
- Some older chemical documentation describes support-company contamination as an active combat route even though the current on-action file does not call those legacy release helpers.
- Designer documentation should distinguish implemented MIO visibility and AI differentiation from the unsupported static country-assignment behavior.
- Biological documentation must say that native raid success is agent-neutral and that severity is a lifecycle result, with Smallpox the only severe agent under the accepted hierarchy.
- Any dynamic-effects or dynamic-triggers documentation that lists CBRN-private helpers should point to their CBRN-specific files instead.

## Required factual wording

Use “fail-closed pending a verified current-version hook” for unsupported continuous-air, live weather/terrain, bombing-loss, and static designer-assignment surfaces.

Do not call a native raid outcome a weather or terrain measurement.

Do not call an equipment block's native operation cost a runtime payload receipt when the engine does not expose that amount.

Do not describe doctrine Condemnation mitigation as evidence suppression, attribution suppression, death reduction, contamination reduction, or responsibility removal.

Do not describe retained legacy definitions as active delivery routes without a current caller and exact shared-pipeline receipt.

## Audit provenance

The helper-index update was made during the current implementation pass.

Fresh bounded specialist audit reports were requested but were rejected by the platform before execution, so they remain an explicit audit gap rather than an implied approval.

The next owner must run the repository-mapped decision, focus, country-package, localisation, event, improvement-loop, and completion audits after the documentation reconciliation.

## Completion gate

This handoff is not a waiver for the remaining audit stages and does not authorize fallbacks or undocumented approximations.
