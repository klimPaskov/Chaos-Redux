# Event 016 Mengele Singularity decision audit

**Status:** bounded source audit, read-only. Audited decision IDs: `mengele_event016_construct_singularity_command_node`, `mengele_event016_construct_singularity_power_link`, and `mengele_event016_authorize_singularity_detonation`. No gameplay files were changed, staged, committed, or tested in a live game.

## Findings

### P1 — Construction actions exceed the cost-type limit and use literal resource names

Both construction decisions expose five directly deducted resources: political power, support equipment, trucks, fuel, and manpower. Their cost strings add a civilian-factory reservation. This already exceeds the decisions skill’s four-spendable-cost limit before counting that reservation. The shared strings spell out resource names and omit texticons; the expected `_blocked` and `_tooltip` cost variants were not found.

Evidence: `common/decisions/016_mengele_singularity_construction_decisions.txt:23-30,77-84`; shared cost strings in `localisation/english/016_brilliant_scientist_projects_l_english.yml:569-570`; cost constants in `common/script_constants/016_brilliant_scientist_project_constants.txt:60-70`.

**Recommended fix:** parent to revise each action to at most four spendable types, then align the affordability/debit effects and provide icon-first normal, blocked, and tooltip strings. Preserve the civilian-factory reservation as a clearly explained requirement if the accepted design allows it.

### P2 — Affordability tooltip trigger includes non-cost requirements

Each `custom_cost_trigger` calls the full `construction_can_begin_*` trigger. That trigger includes unlock, site, active-receipt, and pending-site checks; the shared `brilliant_scientist_can_pay_singularity_*` predicate also checks facility eligibility and available civilian factories alongside actual affordability. Consequently a blocked site or occupied construction slot can be reported through the cost row as though it were an unaffordable payment. The same cost localization key is also invoked by an ordinary `custom_trigger_tooltip`; whether this visibly duplicates text needs a render.

Evidence: the decision lines above; `common/scripted_triggers/016_mengele_singularity_construction_triggers.txt:28-40`; shared payment predicates in `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt:2358-2375).

**Recommended fix:** keep the cost trigger limited to actual affordability and give site, unlock, and active-build blocks their own concise requirement tooltip. Remove the repeated cost-key tooltip if the production render confirms duplicate presentation.

### P2 — Post-lock fallback dispatches to Kruger when Mengele’s guard fails

The shared Fallout lock adapter calls the Mengele finalizer when its provider guard passes, but its `else` calls the Kruger finalizer unconditionally. A Mengele request that passed request validation but fails the Mengele post-lock guard would therefore miss Mengele’s fired-state/event/cleanup finalization and enter a Kruger-only path.

Evidence: `common/scripted_effects/fallout_consolidated_effects.txt:39492-39504`; Mengele post-lock guard in `common/scripted_triggers/016_mengele_singularity_terminal_triggers.txt:41-69`. The normal request path rechecks actor and physical readiness before lock, so this is a conditional dispatch/failure-recovery defect; source review does not establish that the mismatch is reachable in normal synchronous execution.

**Recommended fix:** dispatch by the accepted request’s provider/source and give a failed Mengele finalizer guard an explicit failure/recovery path instead of falling through to Kruger.

### P2 — Terminal requirement tooltip omits several lockout causes

The displayed terminal requirement text covers program/network readiness, the Fallout channel, and the six Gotterdammerung components. The readiness trigger additionally blocks for an active incident, disabled scenario/Chaos, sibling terminal completion, and `world_end_disabled`. Those causes are not explained by the current requirement string.

Evidence: `common/decisions/016_mengele_singularity_terminal_decisions.txt:17-21`; `common/scripted_triggers/016_mengele_singularity_terminal_triggers.txt:14-27`; terminal strings in `localisation/english/016_mengele_singularity_terminal_l_english.yml:4-5`.

## Parent disposition after audit

The source commit `6abe7b9cf` retained the accepted Kruger-equivalent construction prices. The accepted Event 016 closure plan explicitly requires the same construction cost behavior, so the general four-type decision guideline does not authorize deleting a paid resource here; the icon and cost presentation part of the P1 finding remains a presentation task.
The conditional post-lock fallthrough was fixed by dispatching only to a finalizer whose actor has its own submitted receipt. The private post-lock guard now uses accepted request identity and shared lock state rather than prelock provider membership.
The terminal requirement text now names scenario, Chaos Meter, incident, and competing world-end locks. Construction now separates affordability in `custom_cost_trigger` from route/site/slot requirements in an ordinary tooltip and removes the duplicated cost tooltip. Icon-first cost styling and native GUI presentation remain open because the audit's render did not complete.
The begin callback now checks direct costs and physical eligibility after native factory reservation without asking for a second set of free factories, covering the exact-threshold source path. Native callback ordering and the decision-list render remain unverified.

## Lifecycle, costs, and player-facing surface

The category exposes at most two timed construction actions plus the terminal action; they are state-targeted decisions, not missions. A construction target must be a state the player owns and controls with a qualifying facility. The two builds reserve 5 or 6 civilian factories and use the shared construction-duration constants. A valid timer removal completes the linked site-ledger row; cancellation or invalid completion snapshots and clears the direct-payment receipt, cancels the pending row, and refunds the recorded PP, support equipment, trucks, fuel, and manpower once. Provider cleanup is wired through the existing closure and annexation paths. The decision-owned construction wrappers follow the established Kruger board pattern in `common/decisions/016_brilliant_scientist_directorate_project_board.txt:3923-4049`.

No confirmed arithmetic or missing-refund defect was found in the inspected payment/settlement effects. Cancellation depends on native timed-decision callback ordering and state-target `FROM` behavior, which source comparison cannot prove. The category has no `scripted_gui` attachment. There are no active missions in this surface. Player-facing costs are long, raw resource-name lists; durations and site requirements are present in code, but the cost/requirement presentation needs the separation described above. The terminal requirements identify the main physical thresholds but not every current lockout.

## Unverified engine limits and validation gaps

- The native decision-list GUI inspection was started, but the call was still running when this bounded audit was interrupted (exec cell 35). No `hoi4.gui_inspect` result or `hoi4.gui_render` artifact was captured; visible duplication, clipping, and tooltip behavior remain unverified.
- The parent removed the begin effect’s second civilian-factory availability check, covering the exact 5/6-free-factory source path after native reservation. Native ordering at the threshold still requires engine acceptance.
- Static provider receipts have no timer-generation token. Same-family restart after cancellation and a late old native callback remain an engine-ordering acceptance case; the accepted closure plan records this as unresolved. Test cancel, restore eligibility, restart, then deliver/observe any old callback before considering the lifecycle proven.
- No live game was launched, as instructed. The source handoff cannot establish native timer, cancel, remove, or UI behavior.

## AI and route-lock evidence

Construction weights use the shared high-priority base and a wartime preferred multiplier. The existing construction AI handoff reports matching Kruger scores in its named peace/war fixtures (10/20), while target eligibility and the wider decision pool remain unresolved: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_mengele_singularity_construction_ai_audit_2026-09-25.md`. Terminal AI is deliberately zero like Kruger; the terminal AI handoff reports zero in two named fixtures, with eligibility/pool coverage unresolved: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_mengele_singularity_physical_terminal_integration_2026-09-25.md`. I made no probability MCP calls, to avoid duplicating the separate auditor’s work.

The provider request actor is validated before the shared Fallout lock and the Mengele finalizer has a durable post-lock guard. The parent corrected conditional dispatch by submitted receipt after this audit; no live acceptance evidence is available.

## Scope and validation

Reviewed the requested construction/terminal decisions, named triggers/effects, linked site ledger, localization, provider cleanup, shared Fallout adapter, accepted completion contract and closure plan, and compared the construction lifecycle to Kruger. Consulted the required offline wiki pages and relevant vanilla decision documentation/examples. No gameplay source was changed. The only file written for this audit is this handoff. The probability auditor’s handoffs are referenced above and were not duplicated.
