# Event 006 Patron Ledger Decision/Mission Audit Handoff

Scope: Event 006 Independence Wave, Patron Ledger tranche only.

## Files changed

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `localisation/english/006_independence_wave_l_english.yml`

No Event 005 files were edited.

## Changed ids and keys

Decisions with patched availability tooltips:

- `independence_wave_accept_patron_advisers`
- `independence_wave_balance_rival_patrons`
- `independence_wave_expose_foreign_broker`
- `independence_wave_reject_dependency_clauses`
- `independence_wave_request_arms_corridor`
- `independence_wave_convert_loans_to_treaty_debt`

Scripted effects with added patron-leverage clamp calls:

- `independence_wave_select_revolutionary_committee`
- `independence_wave_focus_revolutionary_volunteer_office`
- `independence_wave_focus_congress_support`
- `independence_wave_draft_compact_anti_puppet_clause`

Existing helper reused:

- `independence_wave_clamp_patron_leverage`

Localisation keys added:

- `independence_wave_accept_patron_advisers_requirements_tt`
- `independence_wave_balance_rival_patrons_requirements_tt`
- `independence_wave_expose_foreign_broker_requirements_tt`
- `independence_wave_reject_dependency_clauses_requirements_tt`
- `independence_wave_request_arms_corridor_requirements_tt`
- `independence_wave_convert_loans_to_treaty_debt_requirements_tt`

## Issues by severity

High:

- No high-severity Patron Ledger blocker remains after this patch. The ledger decisions are one-shot flagged, share a timed cooldown, and do not duplicate equipment rewards.

Medium:

- Before patch, Patron Ledger decision availability exposed long scripted-trigger gates directly. This was likely to show raw helper names or overly verbose trigger blocks instead of player-facing requirements.
- Before patch, several route/congress effects that feed the Patron Ledger variable could reduce `independence_wave_patron_leverage` below `constant:independence_wave_decision.patron_leverage_floor` before ledger relief decisions became available.

Low:

- Patron Ledger costs are still political-power-only. The effects are not flat PP exchanges because they move leverage, militia, foreign attention, legitimacy, pressure, and equipment, but a later tranche should consider route-access, convoy, support-equipment, army XP, or obligation costs.
- The ledger is a first decision-category layer, not a full dossier or scripted GUI. This is acceptable for a first tranche, but the docs correctly keep GUI work as future scope.

## Decision category lifecycle notes

- `independence_wave_patron_ledger_category` is visible only through `can_independence_wave_open_patron_ledger`.
- Category visibility is tied to Event 006 release origin and patron route, port ledger, balanced sponsors, anti-puppet proof, or high patron leverage.
- `visible_when_empty = yes` is acceptable because the category description functions as a status surface even when decisions are on cooldown or exhausted.
- Each Patron Ledger decision has a one-shot completion flag and all six actions block on `independence_wave_patron_ledger_cooldown`.
- Duplicate reward loops are blocked by per-decision flags plus shared cooldown.

## Mission quality notes

No Patron Ledger missions are currently implemented.

- Owner: Event 006 released country.
- Category: `independence_wave_patron_ledger_category`.
- Region: not map-targeted; no state or region objective.
- Requirement: scripted trigger per action, now wrapped in player-facing custom trigger tooltips.
- Duration: clickable decisions use `days_remove = @independence_wave_breakaway_decision_days`; no active mission duration.
- Success: immediate complete effects set one-shot flags, move ledger variables, and apply rewards or relief.
- Failure: no Patron Ledger failure branch yet.
- Duplicate risk: low for current rewards due one-shot flags; future repeatable patron actions would need stronger cost and cooldown design.

## Cost and requirement clarity notes

- Patched all six Patron Ledger availability blocks to use custom trigger tooltips instead of exposing raw scripted triggers.
- Requirement text now calls out ledger access, cooldown, pressure/danger gates, route gates, war state, militia weakness, legitimacy, anti-puppet proof, and port-ledger route where relevant.
- Constants centralize decision costs, leverage gates, relief, gains, cooldown days, and equipment rewards.
- Remaining design gap: all six ledger actions cost political power. This is readable and stable for this tranche, but not yet as rich as convoy/equipment/route-access/XP/factory-burden costs.

## AI validity and route-lock notes

- AI weights are present for all six Patron Ledger decisions.
- Patron cabinet and war state favor accepting advisers and arms corridors.
- Civic, balanced-sponsor, revolutionary, national, and anti-puppet routes favor pressure-reducing actions.
- Anti-puppet proof lowers AI desire for additional patron dependency and raises desire for broker exposure/rejection.
- Shared cooldown prevents rapid AI chaining. The AI can still eventually take multiple one-shot ledger actions over time, which is acceptable for the current first layer.
- No targeted patron-country selection is present, so there are no dead target-country or invalid route-target risks in the Patron Ledger itself.

## Localisation and tooltip gaps

- Localisation file remains UTF-8 with BOM.
- No forbidden `:0` keys found.
- Category and all six decision name/description keys exist.
- Patched six missing requirement tooltip keys.
- Text remains player-facing and does not describe implementation history.

## Cleanup and exploit-risk notes

- Patron Ledger cooldown uses a timed country flag set through a temp-variable duration, matching the repo instruction for constant-backed duration fields.
- Completion flags are never cleared, so rewards cannot be farmed.
- Equipment rewards are limited to one `independence_wave_request_arms_corridor` completion.
- Patron leverage relief is clamped after all Patron Ledger relief decisions and after the related route/congress effects patched here.
- Remaining out-of-scope risk: `independence_wave_offer_protected_transfer` spends patron leverage without a patron-leverage floor check or clamp. That belongs to the Border Commission surface, not this Patron Ledger patch.

## Before and after behavior

Before:

- Patron Ledger decision requirements were driven by scripted triggers directly in `available`.
- Related revolutionary/congress anti-patron relief could push `independence_wave_patron_leverage` below the configured floor before or around Patron Ledger use.

After:

- Patron Ledger decisions show concise custom requirement tooltips.
- Related anti-patron relief calls the existing leverage clamp helper and cannot leave `independence_wave_patron_leverage` below the configured floor.
- No decision reward amount, AI weight, cost, visibility gate, or route design was changed.

## Validation run

- `git diff --check -- common/decisions/006_independence_wave_decisions.txt common/scripted_effects/006_independence_wave_effects.txt localisation/english/006_independence_wave_l_english.yml`
- `rg -n "<=|>=" common/decisions/006_independence_wave_decisions.txt common/scripted_triggers/006_independence_wave_triggers.txt common/scripted_effects/006_independence_wave_effects.txt common/script_constants/006_independence_wave_constants.txt localisation/english/006_independence_wave_l_english.yml`
- `rg -n ":0\\s*\\\"" localisation/english/006_independence_wave_l_english.yml`
- `xxd -g 1 -l 3 localisation/english/006_independence_wave_l_english.yml`
- Brace-depth check over Event 006 decision, category, trigger, effect, and constant files.
- Localisation coverage check for all patched Patron Ledger tooltip keys and all Patron Ledger decision/category name and description keys.

## Skipped validation

- No live-game scenario validation was run.
- No full repo `git diff --check` was used because the worktree contains unrelated Event 005 and other parent changes outside this subagent scope.

## Remaining issues and recommended fixes

- Consider richer costs for future Patron Ledger expansion: convoys for arms corridors, support equipment or army XP for advisers, legitimacy/coalition costs for treaty debt, and foreign-attention or route-access constraints for broker exposure.
- Consider a future status or scripted GUI surface only if the parent wants the ledger to show current leverage, cooldown, and route pressure more explicitly.
- Border Commission should separately audit `independence_wave_offer_protected_transfer` for patron-leverage floor safety.
- The Patron Ledger first layer is sufficient for the parent to proceed as a bounded decision-category tranche; it is not a complete patron gameplay system.
