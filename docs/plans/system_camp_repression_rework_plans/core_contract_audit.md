# Camp Repression Rework Core Contract Audit

> **Superseded audit snapshot.** This report preserves the original core findings and the corrected re-audit that closed `CR-CORE-01` through `CR-CORE-07`. Its hashes and line references describe frozen intermediate files, not the final package. Use `source_of_truth_and_completion_tracker.md`, `completion_report.md`, and `scenario_contract_validation_report.md` for current status. The final decision-and-mission audit passed, and all 15 scenario contracts passed static trace; no engine-runtime scenario execution occurred in this environment, and that validation gap remains explicit in the final record.

## Final corrected re-audit verdict

The corrected shared-core snapshot passes `CR-CORE-01` through `CR-CORE-07`.

- Remaining P0: 0
- Remaining P1: 0
- Remaining P2: 0
- New regressions: none

The final re-audit confirmed recurring restricted-method validation/consumption and fail-closed shortage cleanup; non-overwriting responsibility guards at effects and decision targets; a single exact Deaths adapter for Mengele; annex/dead-perpetrator cleanup and discovery; dynamic evidence severity based on camp-specific Deaths; exact biological availability/execution parity; and bare temporary-variable use for vaccination progress. The temporary Ledger performance regression found during the re-audit was corrected by restoring the `camp_repression_ledger_open` gate around monthly display-array rebuilding.

Final frozen SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `common/script_constants/camp_repression_rework_constants.txt` | `566501372C2A54E2A4EB5FAE212B5A946C18F8CAF2692FDBD1DD2D5ECD880500` |
| `common/scripted_triggers/camp_repression_rework_triggers.txt` | `462583049ECA6342EA3739806BFD8B97498FD612C2EB3AF0B0B2BF8537812D1B` |
| `common/scripted_effects/camp_repression_rework_effects.txt` | `DD16FB289A91B705A1E20A43EA1CBFE2A29582409374267AA8B29F09FD125A09` |
| `common/scripted_effects/genocide_crisis_effects.txt` | `2A9CB6747EC8E8FCBF9E274618CE35D4C3C100CA48BD7B65B861501823F0B9DD` |
| `common/scripted_effects/germany_mengele_effects.txt` | `2ED313C2BF9C9F147443E8340D450AFD6920D476675A8F1DE16691D1CA7A865D` |
| `common/scripted_effects/biowarfare_effects.txt` | `1B455411EC0A1469857054CB1B4FBCC0054EC0FB3FECA8057BEA850007710F30` |
| `common/on_actions/genocide_crisis_on_actions.txt` | `53B1D0107809E3C17C9852D9B058BD87F02DF77401D0C16919D65BE8B9CE9036` |
| `common/scripted_effects/005_soviet_collapse_effects.txt` | `9C2DA277879BFDD5FB9BF577A215003A4F74E22743958628BCBE60E3016DDCEC` |

The detailed sections below are the initial audit record and are superseded by this corrected re-audit verdict. They are retained to document why each remediation was required.

## Initial verdict (superseded)

The core runtime is **not completion-ready**. The audited snapshot has no confirmed P0 defect, but it still has four P1 contract breaks and three P2 defects:

- **P0:** 0
- **P1:** 4
- **P2:** 3
- **P3:** 0

The highest risks are continuing chemical/biological use without recurring consumption or shortage shutdown, responsibility corruption when an unresolved evidence site is reused, the unconverted Mengele exact-Deaths path, and missing annex/dead-perpetrator cleanup.

This was a read-only gameplay audit. No Event 17 file or surface was inspected. The only repository write made by the auditor is this report.

## Audit basis and snapshot

The audit used the repository `AGENTS.md`, the required offline Paradox wiki core pages, official vanilla documentation for variables, collections/arrays, effects, triggers, scopes, on-actions, and script constants, and vanilla array/on-annex precedents. The accepted contract was read from the package index, Parts 1/4/6/7, `source_of_truth_and_completion_tracker.md`, and especially `core_script_architecture_handoff.md`.

Exact line references below are against the following shared-file snapshot, frozen after the major-country dispatcher insertion on 2026-07-11:

| File | SHA-256 |
| --- | --- |
| `common/scripted_effects/camp_repression_rework_effects.txt` | `C33D259AA7C3E7E0D54D84BE152F7F40751B111EDCF321E598008714FA4F241A` |
| `common/scripted_triggers/camp_repression_rework_triggers.txt` | `620E44EE526C63F8F1E3C5A18B2A890EC199FCF880B61FA3DF6AC48690B900EB` |
| `common/scripted_effects/genocide_crisis_effects.txt` | `EEEDC187C364263E6CE593120AB65CF2FEA107FFF85AF59A699340ED4CAA72B0` |
| `common/scripted_effects/germany_mengele_effects.txt` | `0CE502C4D99D36F30565D1F5A5F586F80AA84FC9F242B58E1327106F3FA3B4F7` |
| `common/scripted_effects/biowarfare_effects.txt` | `529EA919D797AEAAF2D5AD73E29AA3A9153B6CC16E5803A95F65F6A8085EA9B3` |
| `common/decisions/camp_repression_generic_decisions.txt` | `D1455EAFC90114B25656726C738DDA9587FE74AC455F739D77ADF9D2CB6017BE` |

## Findings summary

| ID | Severity | Remaining defect | Primary evidence |
| --- | --- | --- | --- |
| CR-CORE-01 | P1 | Continuing chemical/biological use is free, is not revalidated, and never shuts down on shortage; the required short-term resistance suppression is also absent. | `camp_rework_apply_monthly_state_effects`, lines 906-920 |
| CR-CORE-02 | P1 | An inactive site with unresolved evidence can be reactivated by a different country, overwriting the primary pointer while leaving the state in the old perpetrator's evidence array. | Generic activation lines 87-126; activation effect lines 2376-2402 |
| CR-CORE-03 | P1 | `germany_mengele_register_experiment_deaths` still bypasses the required exact state-Deaths adapter and perpetrator post-processing. | `germany_mengele_effects.txt`, lines 152-193 |
| CR-CORE-04 | P1 | Annexed/dead perpetrators have no camp cleanup hook, remain in the global active-country registry, and can make unresolved evidence undiscoverable. | Camp on-actions lines 9-30; cleanup lines 1025-1048; discovery lines 791-818 |
| CR-CORE-05 | P2 | Discovery severity still ignores dynamic evidence depth, actual deaths, reach, observer exposure, and foreign visibility. | `genocide_calculate_discovery_condemnation_from_prev_state`, lines 567-671 |
| CR-CORE-06 | P2 | Biological decision availability is weaker than execution: facility plus tech is enough to pay for a decision that can resolve to tier zero without bomb stockpile. | Trigger lines 809-817 versus resolver lines 1998-2030 |
| CR-CORE-07 | P2 | Smallpox weekly progress scopes a temporary variable as `ROOT.weekly_progress`; temporary variables have no scope. | `biowarfare_effects.txt`, lines 2784-2819 |

## Detailed findings

### CR-CORE-01 — P1 — Continuing restricted methods do not consume or fail closed

**Accepted contract**

- `core_script_architecture_handoff.md:347,355-356` requires the monthly state dispatcher to resolve live tiers, consume continuing stockpile, and use a consumer that reports failure.
- `core_script_architecture_handoff.md:378-385` requires monthly consumption before the one consolidated Deaths call; a failure clears the active-use flag but retains contamination/evidence.
- `core_script_architecture_handoff.md:473` says activation and **each continuing monthly use** consume separate constant-defined amounts.
- `source_of_truth_and_completion_tracker.md:104,414` also requires stockpile/logistics consumption and short-term resistance reduction for every use.

**Implementation evidence**

- `camp_rework_apply_monthly_state_effects` at `common/scripted_effects/camp_repression_rework_effects.txt:906-920` refreshes the state, prepares the death profile, makes the Deaths call, and adds evidence/resistance. It performs no live tier resolution, stockpile validation, consumption, logistics charge, or failure cleanup.
- Active method flags continue to multiply monthly Deaths at `common/scripted_effects/camp_repression_rework_effects.txt:780-829`, independent of current capability or stockpile.
- Chemical stockpile consumption occurs only on activation in `camp_rework_apply_chemical_escalation_in_from` at lines `2139-2179`, calling `camp_rework_consume_chemical_stockpile` at line `2147`.
- Biological stockpile consumption likewise occurs only on activation in `camp_rework_apply_biological_escalation_in_from` at lines `2239-2295`, calling `camp_rework_consume_biological_stockpile` at line `2247`.
- Only one cost ladder exists for each method (`common/script_constants/camp_repression_rework_constants.txt:414-429,539-552`); there are no distinct continuing-monthly costs.
- Both activations add accident pressure to country and state resistance (`camp_repression_rework_effects.txt:2148-2169,2248-2265`). No effect supplies the required short-term resistance suppression.

**Impact**

One paid activation grants the full multiplier for the timed flag's duration even after equipment is exhausted or facilities/capability are lost. This breaks resource balance, UI truth, AI equivalence, and the accepted fail-closed safety contract.

**Suggested patch**

1. Add separate activation and monthly-use constants for each chemical and biological tier, plus a bounded logistics/administrative cost.
2. Add a state-scope maintenance adapter called before `camp_rework_prepare_monthly_state_death_profile`. It should copy the state's stored tier, enter `var:genocide_responsible_country`, revalidate the exact tier's facility/tech/equipment, consume the monthly amount, and return a bare temporary success flag.
3. On failure, clear `camp_rework_chemical_method_active` or `camp_rework_biological_method_active` and its legacy active flag, reset the active tier, but preserve contamination, evidence flags, evidence depth, and responsibility.
4. Do not call contamination or Deaths from the maintenance consumer. The existing single monthly Deaths call at line 912 must remain the only normal monthly state call.
5. Apply a bounded, temporary resistance-suppression value on successful use while retaining the positive accident/evidence/tribunal liabilities.

### CR-CORE-02 — P1 — Reactivation can corrupt historical responsibility

**Accepted contract**

- `core_script_architecture_handoff.md:17,170,275` makes `genocide_responsible_country` persistent until explicit final evidence resolution and defines `camp_site_evidence_resolved` as the cleanup gate.
- `core_script_architecture_handoff.md:757-759` requires reuse/reactivation to resolve or preserve old evidence before assigning a new primary pointer.
- `core_script_architecture_handoff.md:752` defines optional secondary responsibility without overwriting the primary pointer.

**Implementation evidence**

- Generic activation accepts an inactive pool state at `common/decisions/camp_repression_generic_decisions.txt:87-102,104-126`. It does not reject `camp_rework_site_dismantled`, unresolved evidence, or an existing responsibility pointer belonging to another country.
- `camp_rework_activate_detention_in_from` unconditionally writes `genocide_responsible_country = ROOT` at `common/scripted_effects/camp_repression_rework_effects.txt:2376-2385`.
- `camp_rework_register_active_site` then registers the state to the newly stored perpetrator at `common/scripted_effects/camp_repression_rework_effects.txt:343-432`.
- `camp_rework_register_evidence_state` adds the state to the currently stored country's `camp_evidence_states` array at `common/scripted_effects/camp_repression_rework_effects.txt:1256-1277`; it cannot remove the stale membership from the former country after the pointer is overwritten.
- Dismantlement intentionally preserves evidence and registers it at `common/scripted_effects/camp_repression_rework_effects.txt:1624-1672`, making the reuse path reachable by design.
- `camp_site_evidence_resolved` and `camp_site_secondary_responsible_country` have no gameplay implementation; their only matches are in planning documents.

**Impact**

The same state can remain in the former perpetrator's evidence array while its only primary pointer names the new operator. Discovery then condemns only the new pointer, losing or misassigning the historical crime and leaving the two countries' ledgers structurally inconsistent.

**Suggested patch**

1. Immediately block generic activation when unresolved evidence has a primary responsible country other than ROOT.
2. Implement an explicit evidence-resolution effect. Only after tribunal/redress/records disposition sets `camp_site_evidence_resolved` may it remove old evidence-array membership and clear or replace the primary pointer.
3. If unresolved reuse is a required design, implement the accepted preserved/secondary responsibility model and collaborator shares before allowing it. Do not solve reuse with an unconditional pointer overwrite.

### CR-CORE-03 — P1 — Mengele exact deaths bypass the camp adapter

**Accepted contract**

- `core_script_architecture_handoff.md:40-41,345-346,411-438` requires event-authored exact deaths to pass through `camp_rework_register_exact_state_deaths`, write both state output fields, and credit the stored perpetrator.
- `core_script_architecture_handoff.md:51,550,833` explicitly names `germany_mengele_register_experiment_deaths` and state 88 as the required conversion.

**Implementation evidence**

- `germany_mengele_register_experiment_deaths` computes the amount and directly calls `chaos_meter_register_deaths` in state 88 at `common/scripted_effects/germany_mengele_effects.txt:152-193`, especially lines `184-191`.
- It does not write `genocide_last_state_deaths` or `camp_site_last_month_deaths` and does not call `genocide_credit_state_deaths_to_responsible`.
- No implementation of `camp_rework_register_exact_state_deaths`, `camp_exact_deaths`, or `camp_site_last_month_deaths` exists in gameplay script.
- The bypass remains live from `events/germany_mengele.txt:84,246,300,357`.

**Impact**

The victim state and Deaths history are affected, but the camp state result and stored perpetrator ledger are not. Germany/Mengele reports therefore disagree with the canonical camp accounting and discovery/tribunal data.

**Suggested patch**

Implement the accepted state-scoped exact adapter: reset the output, set civilian/state-pop/OWNER/reason inputs, call `chaos_meter_register_deaths` exactly once, immediately copy its actual result to `camp_site_last_month_deaths` and `genocide_last_state_deaths`, and call `genocide_credit_state_deaths_to_responsible`. Route the state 88 block through that adapter.

### CR-CORE-04 — P1 — Annexed/dead perpetrator lifecycle is incomplete

**Accepted contract**

- `core_script_architecture_handoff.md:759,801,836` requires annexation to stop active use, remove active-array membership, preserve the historical pointer/evidence, and allow normal discovery without blaming the current owner.
- `source_of_truth_and_completion_tracker.md:251` also requires ledger cleanup on annexation.

**Implementation evidence**

- `common/on_actions/genocide_crisis_on_actions.txt:9-30` has startup, state-control, and capitulation hooks, but no camp `on_annex` hook.
- The only relevant existing annex hook, `common/on_actions/chaosx_on_actions_chaos_meter.txt:93-99`, calls only `chaos_meter_on_annex`.
- `camp_rework_clean_inactive_countries` at `common/scripted_effects/camp_repression_rework_effects.txt:1025-1048` only stages entries whose country scope passes `exists = yes` at line 1031. A dead country therefore remains in `global.camp_repression_active_countries` indefinitely.
- State-control cleanup exists at `common/scripted_effects/genocide_crisis_effects.txt:821-833`, but it cannot perform the missing country-registry/ledger cleanup.
- `genocide_try_discover_state_atrocity` at `common/scripted_effects/genocide_crisis_effects.txt:791-818` requires either war between perpetrator and discoverer or `genocide_destroyed_atrocity_site` at lines `806-809`. A dead perpetrator cannot be at war, and a captured/unregistered site need not be marked destroyed.

**Impact**

Annexed actors leak from the canonical monthly registry and can retain stale ledger-open/UI state. More importantly, unresolved evidence tied to a dead perpetrator can fail the discovery gate forever, contrary to the required preserved-blame lifecycle.

**Suggested patch**

1. Add a camp annex adapter using vanilla `on_annex` scopes (ROOT annexer, FROM annexed). In a two-pass cleanup, unregister FROM's active sites, remove FROM from the global active-country registry, and clear ledger UI/cache state while preserving evidence arrays and the original state pointer.
2. Make dead scopes removable from `camp_rework_clean_inactive_countries`; do not require `exists = yes` in the only removal branch.
3. Add a discovery branch for unresolved evidence whose responsible country no longer exists. Mark and report discovery normally, retain the original pointer/evidence, skip country condemnation if no live scope can receive it, and never substitute OWNER/controller. Successor liability must remain an explicit rule.

### CR-CORE-05 — P2 — Discovery severity omits required dynamic inputs

**Accepted contract**

- `core_script_architecture_handoff.md:45,744-754` requires site type, evidence depth, cover-up, experiment/contamination, actual deaths, network reach, repeat discovery, and foreign visibility.
- `source_of_truth_and_completion_tracker.md:111` records the same requirement.

**Implementation evidence**

- `genocide_calculate_discovery_condemnation_from_prev_state` at `common/scripted_effects/genocide_crisis_effects.txt:567-671` uses site class, repeat count, destroyed/failed cover-up, experiment traits, Mengele values, and a chemical flag.
- It never reads `camp_state_evidence_depth`, `genocide_last_state_deaths`/`camp_site_last_month_deaths`, `camp_state_observer_exposure`, `camp_network_reach`, or `camp_foreign_visibility`.
- The application block at `common/scripted_effects/genocide_crisis_effects.txt:673-705` adds fixed visibility/pressure and a fixed biological source, but does not recover those missing severity inputs.

**Impact**

A shallow site and a deep, high-death, internationally exposed network can produce the same condemnation once site class and repeat status match. Player-facing evidence, reach, and visibility values therefore do not drive the outcome they describe.

**Suggested patch**

Add constant-scaled and clamped contributions from state evidence depth, the latest recorded actual state deaths (or a new canonical cumulative state-deaths field), state observer exposure, responsible-country network reach, and responsible-country foreign visibility before the existing repeat/cover-up branches. Preserve the current stored-responsible-country routing and source-aware condemnation adapters.

### CR-CORE-06 — P2 — Biological availability can charge for a no-op

**Accepted contract**

The restricted-method contract requires live capability **and stockpile** to select a tier; a visible/available paid action must have an executable effect.

**Implementation evidence**

- `camp_rework_country_has_biological_escalation_capacity` at `common/scripted_triggers/camp_repression_rework_triggers.txt:809-817` checks a biowarfare facility and any delivery technology, but no bomb stockpile.
- `camp_rework_resolve_restricted_method_tiers` at `common/scripted_effects/camp_repression_rework_effects.txt:1998-2030` requires facility, matching technology, and matching bomb stockpile for every biological tier.
- The paid generic decision uses the weaker trigger for visibility, root targeting, and availability at `common/decisions/camp_repression_generic_decisions.txt:396-439`, then dispatches at lines `440-449`.

**Impact**

A country with a facility and delivery technology but no matching bomb can see and take the decision, pay its political-power cost, enter the biological branch, resolve to tier zero, and receive no effect.

**Suggested patch**

Create shared per-tier biological capacity triggers containing facility, exact technology, and exact equipment checks. Use the same triggers in the decision availability and tier resolver, or mirror the resolver's complete OR exactly. Availability and execution must not drift.

### CR-CORE-07 — P2 — Scoped temporary variable breaks weekly vaccination progress

**Engine contract**

`AGENTS.md:112` and the offline wiki's variable documentation state that temporary variables have no scope. `ROOT.temp_name`, `PREV.temp_name`, and `THIS.temp_name` do not access the temporary value.

**Implementation evidence**

- `progress_smallpox_vaccination` creates and modifies temporary `weekly_progress` at `common/scripted_effects/biowarfare_effects.txt:2784-2805`.
- Inside `every_controlled_state`, line `2819` reads `ROOT.weekly_progress`.
- `weekly_progress` has no normal-variable assignment anywhere in the repository.

**Impact**

Controlled states read zero or an unrelated regular country variable instead of the computed weekly progress, so vaccination progression can stall or become stale.

**Suggested patch**

Use the bare temporary token inside the state loop:

```txt
add_to_variable = { smallpox_vaccination_progress = weekly_progress }
```

Alternatively, deliberately copy the value to a distinct normal country variable before entering the state scope and clear it afterward. The bare temporary is simpler and matches the current single-chain use.

## Contracts that currently pass

The following audited contracts were confirmed and should be preserved while patching the findings:

- Direct construction is disabled for all three camp buildings at `common/buildings/chaosx_buildings.txt:107-150,182-188`; activation remains decision-routed.
- `camp_rework_register_active_site` is duplicate-safe for the global active-state array and the responsible country's active array at `common/scripted_effects/camp_repression_rework_effects.txt:343-432`. Its `var:genocide_responsible_country` / `PREV` use correctly carries the state into the country-owned arrays.
- Evidence registration is separately country-owned at `common/scripted_effects/camp_repression_rework_effects.txt:1256-1277`, and dismantlement preserves evidence/site type before unregistering at lines `1624-1672`.
- Migration is version-gated and bounded to its rebuild at `common/scripted_effects/camp_repression_rework_effects.txt:1732-1845`; the recurring pulse does not perform a world scan.
- The recurring monthly hook is the existing host-only pulse at `common/on_actions/chaosx_on_actions_chaos_meter.txt:53-64`; the canonical runtime loops registered arrays in `camp_rework_monthly_global_pulse` at `common/scripted_effects/camp_repression_rework_effects.txt:1051-1068`.
- Normal monthly state processing makes one Deaths call and copies/credits the actual result at `common/scripted_effects/camp_repression_rework_effects.txt:906-920`.
- Chemical and biological target triggers are mutually exclusive at `common/scripted_triggers/camp_repression_rework_triggers.txt:819-840`, and their monthly multipliers use one `if`/`else_if` chain at `common/scripted_effects/camp_repression_rework_effects.txt:780-829`.
- Chemical and biological activation each call one contamination path and then credit that output; no activation double-count was confirmed in `camp_repression_rework_effects.txt:2139-2179,2239-2295`.
- Discovery blame is routed through the stored state responsibility pointer rather than the discoverer/current owner at `common/scripted_effects/genocide_crisis_effects.txt:791-818` when the responsible scope exists.
- A mechanical scoped-temp scan of the requested effect/trigger files found no other confirmed `ROOT`/`PREV`/`THIS` temporary-variable misuse beyond CR-CORE-07.

## Completion assessment

The core contract cannot be marked complete until CR-CORE-01 through CR-CORE-04 are fixed and re-audited. CR-CORE-05 through CR-CORE-07 should be fixed in the same core tranche because they affect accepted outcome semantics and paid-action correctness.

No fallback or gameplay simplification was introduced by this audit. The explicitly excluded Event 17 surface was not inspected.
