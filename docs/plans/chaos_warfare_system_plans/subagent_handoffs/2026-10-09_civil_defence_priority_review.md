# Civil Defence Priority Review

Disposition: the final source review supports the accepted repair plan and found no blocking gameplay defect in the priority, lifecycle, or caller boundaries.
The queued permanent-history/category issue and the no-reserve AI first-production deadlock are addressed by the current-specific triggers and shared structural gap predicate.

## Scope and reviewed identifiers

This review covers only the parent’s three-file patch in `common/scripted_triggers/cbrn_protection_triggers.txt`, `common/scripted_effects/cbrn_protection_effects.txt`, and `common/scripted_effects/cbrn_protection_decision_effects.txt`.
The new helpers are `cbrn_state_has_active_chemical_response`, `cbrn_state_has_current_chemical_need`, `cbrn_country_has_current_chemical_need`, `cbrn_state_has_automatic_priority_mask_gap`, `cbrn_complete_threatened_filter_replacement_program`, and `cbrn_complete_threatened_priority_distribution_program`.
The review did not reopen the committed hospital audit or the broader history/priority audit.

## Entry, issue, and AI-gap behavior

`cbrn_country_has_current_chemical_need` is limited to controlled states with an exact chemical alert, live chemical contamination, or one of the four active 14-day civilian response flags, plus an active enemy with chemical capability or confirmed current-enemy use history.
It excludes permanent victim history and the isolated retaliation-authorization permission.
Civil Defence visibility keeps its separate biological-outbreak and active occupied-program reveals.
`cbrn_country_needs_civilian_mask_issue` uses current need plus the pending British 1939 receipt, so a victim-history-only country no longer triggers routine civilian issue.
The UK receipt remains separate and its existing successful-issue cleanup is unchanged.

`cbrn_state_has_automatic_priority_mask_gap` is the shared, reserve-independent contract for both the AI gap and automatic receiver: controlled ROOT core, populated, not occupied by a state project, below the existing priority-coverage target, and either locally threatened or strategically valuable.
The receiver adds the existing national-reserve flag and the execution effects still require live stock.
This lets production AI plan before a reserve receipt exists while keeping execution stock-bound.
The mask-production signal adds current need without removing any existing signals, and the orphan 95%-coverage branch was removed from `cbrn_country_below_mask_ai_target`; no full-distribution execution caller or new mass-distribution route was added.

## Maintenance order and contract preservation

The current maintenance cycle runs military filter service and issue first, then completes the full threatened civilian filter-service pass, then the threatened priority issue pass, then non-threat civilian filter service, and finally non-threat priority issue.
The loops complete a whole service tier before moving to its issue tier, so a state does not receive new masks ahead of filter service for another threatened state.
Threatened priority issue accepts low-value populated ROOT cores when they have local need; the existing 50% priority gap still limits quantity.
The strategic fallback retains the existing capital/value target behavior, but now runs only after the local-threat tier.

`cbrn_state_is_valid_distribution_target` remains unchanged and still serves occupied, full-distribution, and existing filter-service consumers.
The new automatic issue helper is core-only; occupied noncore distribution continues to use the existing paid reservation, escrow, cooldown, cancellation, and refund path.
The threatened filter-service pass can maintain previously issued noncore stocks through the existing filter receiver, but it does not grant new noncore mask stock.
Export/import and other foreign-aid decisions were not altered.

The active `cbrn_protection_project_active` exclusion remains in both the generic validity trigger and the shared automatic-priority gap trigger.
Although the automatic completion wrapper clears that project flag, the receiver cannot enter on a busy state, so it does not take ownership of an active state project.
Military-first sequencing, state transactions, model allocations, filter costs, population ratios, rounding, and the existing coverage constants remain in place.
No world pulse, new on-action, global state sweep, persistent flag, or new timer was added.

## Remaining issues and limits

1. **Documentation is stale for the new helper contracts.** `common/scripted_triggers/cbrn_scripted_triggers.md` still describes the priority gap as any undercovered core and does not mention the threat/strategic-value split, reserve-independent AI planning, the current-need helpers, or the updated maintenance order.
`common/scripted_effects/cbrn_scripted_effects.md` still describes the single capital-first priority program without the threatened-first service/issue phases.
This audit made no shared-document edits.

2. **Allocation within one tier remains source-order dependent.** The threatened and fallback passes still test the capital first and then use `every_controlled_state`; source review cannot establish the engine’s order for the rest of that tier.
The patch guarantees local threat before strategic fallback, not equal allocation among states in the same tier.

3. **Legacy full-distribution definitions remain but have no gameplay callers.** `cbrn_complete_full_distribution_program`, `cbrn_country_has_full_distribution_work`, and the full-civilian gap helper remain declared; the 95% AI demand branch is gone and no completion call was added.
This is dormant source surface, not a second automatic distribution route.

4. **AI/probability evidence is delegated.** Trigger eligibility and `cbrn_country_has_mask_production_signal` change AI strategy inputs, but this patch changes no numeric weights or constants.
The designated probability/consumer reviewer owns scenario-specific comparison; this report makes no normalized probability claim.

The existing 125-case continuing-protection source result plus its four ROOT-binding probes predate this priority patch.
Parent-owned source tests and the probability reviewer’s after-source evidence remain outside this read-only review.
No game, native decision UI, log, MCP, or source test was run here, so native target refresh and engine iteration order remain unobserved.

No gameplay, tests, shared documentation, or index files were changed by this audit; its only output is this handoff.
