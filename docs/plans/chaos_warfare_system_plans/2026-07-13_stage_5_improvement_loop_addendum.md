# Stage 5 improvement-loop addendum

Status: closed for Stage 5; the overall Chaos Warfare goal remains in progress

## Scope and method

This pass reviews the implemented Stage 5 Chaos Warfare doctrine, institutional progression, use policy, doctrine-only technologies, officer corps, high command, leader trait, migration, localisation, assets, AI, and shared-consequence integration. It applies the accepted numbered specifications and matrices without expanding into the later delivery-route, biological-agent, nerve-suppression, full consequence, achievement, or country-profile stages.

Two attempts to route this review through `chaosx_improvement_loop_planner` were rejected by the service safety filter before either agent produced files, findings, or patches. The parent therefore completed the required improvement-loop review locally from the already-read `chaos-redux-improvement-loop` workflow. No blocked planner output was treated as evidence.

## Findings implemented in this pass

### Existing-save institutional migration

The offline on-action reference states that `on_startup` does not execute when a save is loaded. The initial migration path could therefore reconcile new games but could leave a country that already held `chaos_warfare` without the Stage 5 adoption flag or institutional program surface.

The implementation adds `cbrn_convene_institutional_review`, a zero-cost one-time country decision that:

- is visible only to a country with `chaos_warfare` and without `cbrn_chaos_warfare_adopted`;
- calls the same idempotent `cbrn_migrate_legacy_chaos_warfare` helper used by new-game migration;
- reconstructs native mastery history and removes the obsolete Concentration-law capability without fabricating reserves, fielded formations, protected-order history, policy authorization, or institutional milestones;
- exposes the bounded establishment mission after reconciliation;
- has high route-neutral AI priority and disappears as soon as migration records adoption; and
- uses a distinct final 32x32 decision asset rather than a placeholder or cross-type substitute.

This closes the save-load gap without a daily, weekly, monthly, or other broad all-country pulse.

### One Condemnation ladder

The review found parallel doctrine Condemnation tables that could drift during later route migration. Stage 5 now has one canonical 0.90/0.80/0.70 ladder in `chem_integrated_operations.condemnation_mult`. The shared chemical exposure record and the bounded legacy chemical and biological adapters read that same table.

Doctrine mitigation applies only to Condemnation. It does not reduce payload consumption, evidence, attribution, deaths, contamination, medical saturation, confirmed-use history, resistance trauma, biological use counters, or domestic war-support consequences. Strategic and mass-casualty Condemnation floors are applied after doctrine multiplication. Terminal Hazard Doctrine can increase Condemnation, deaths, and supply burden but cannot suppress evidence or attribution.

### Explicit AI ownership

The review completed explicit nonhuman refusal paths for doctrine policy, commission, spirit, high-command, and commander-trait selection. Ordinary defensive and democratic profiles remain defensive or retaliatory; aggressive profiles receive consideration weights only and never receive free stock, readiness, institutions, operation proof, or policy authorization.

### Localisation and helper depth

Tuning-sensitive Stage 5 localisation uses direct constant-backed values, including derived multiplier/baseline displays. The review removed two unused doctrine helpers and one unused readiness constant, then confirmed that every remaining Stage 5 doctrine helper has a caller and reference documentation. Static doctrine parser values remain file-local mirrors because installed doctrine documentation does not prove global script-constant support in those fields.

## Deliberate boundaries, not simplifications

- Chemical Barrage remains fail-closed because no verified tactic activation effect can debit payload before entering the shared exposure pipeline.
- Chemical Air Interdiction is an eligibility marker only. There is no continuous ordinary-air contamination estimator, and idle chemical-capable aircraft cannot contaminate a region.
- Exact-state cleanup is a dedicated selected-state decision because the commander ability surface has no verified exact selected-state target.
- The Army Headquarters surface remains the theater layer and does not receive an ordinary-division substitute.
- Hazard Assault Training is the explicit equipment-backed mastery source because native mastery has no verified exact per-formation equipment-fill trigger.
- Protective Foundation proves post-adoption gas-mask production plus a live reserve because the installed engine exposes exact cumulative production but no verified current production-line trigger.
- CBRN Coercive Security, not the doctrine use-policy ladder, owns nerve-suppression authorization. The Stage 5 commission therefore remains fail-closed until that later occupation-policy surface exists.
- Numbered specification 08 controls the conflict with broad package language: doctrine does not unlock camps, extermination infrastructure, experiment sites, or a generic Concentration occupation law.

These boundaries disclose unsupported engine behavior and avoid estimators, fabricated proofs, passive contamination, and unapproved fallbacks.

## Deferred work owned by later stages

The following are required by the overall Chaos Warfare goal but are not Stage 5 defects: migration of every chemical delivery route into the shared exposure pipeline; complete biological agent, incubation, spread, accident, treatment, and containment behavior; equipment-consuming nerve-agent suppression and resistance trauma; full Condemnation, sanctions, attribution, outbreak, achievement, scripted-GUI, route-profile, country-profile, and documentation integration. They remain queued under the staged implementation plan and cannot be used to claim the overall goal complete.

## Closure evidence

- [x] Register and visually inspect the unique institutional-review decision asset.
- [x] Re-run the decision/mission specialist audit against the migration decision and its AI/cleanup behavior. The audit passed after fixing nonhuman modifier ordering, parser-sensitive timed flags, and remediation cost disclosure.
- [x] Invoke the read-only Stage 5 completion auditor against the numbered specifications, matrices, specialist prompts, balance scenarios, asset manifest, localisation coverage, and documented engine boundaries. The service safety filter stopped the auditor before it produced findings; this is disclosed as an audit limitation and not represented as a specialist pass. The parent completed the same closure comparison locally and found no unresolved Stage 5 requirement.
- [x] Re-run Stage 5 helper, constant, localisation, GFX-path, DDS-header, parser-mirror, AI, scenario, and changed-file ownership checks. The refresh covered 30 scoped script/GFX files, five doctrine files, 530 localisation keys, 88 localisation constant references, 50 effects, 48 triggers, and 45 runtime assets.
- [x] Promote this addendum and the Stage 5 implementation plan to closed after resolving every local and specialist finding and carrying the explicitly later-stage requirements forward without using them as a Stage 5 simplification.
