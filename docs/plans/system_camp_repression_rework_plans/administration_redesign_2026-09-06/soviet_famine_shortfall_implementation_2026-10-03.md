# Soviet famine shortfall implementation

Disposition: implemented in source, with scoped audits and consumer evidence still incomplete.
Acceptance basis: the user's direct 2026-10-03 choice of an explicit no-resource response with famine and corruption penalties.
The request rejects requisition debt and does not authorize population creation, invented casualty attribution or repeated mission penalties.

## Current implementation

The existing material trigger is shared by the native relief decision's custom-cost and availability gates and by funded event options.
The funded helper now repeats a full final order preflight before its equipment debit.
It rejects an invalid original authority, resolved famine, missing stock and an already active relief flag or mission.
An accepted request spends each equipment type once and activates one mission.
The decision dispatcher returns its declared 30-PP quote when the helper rejects.
The package router applies the scripted cooldown only after an accepted request and clears the result flag.
The production action mapper routes accepted famine relief to `camp_gui_country_action_2_cooldown` with the centralized 150-day duration.
The existing relief mission lasts 180 days, so the timed flag may have expired before a timeout permits the next paid attempt under the September 26 retry contract.
Every retry still requires the full resource quote, and this timing grants no free relief.
Event callers pay no additional PP and cannot call the decision refund path.

Warning shortfall uses the centralized +5 famine and +3 corruption consequences.
Critical shortfall uses the existing +12 famine, +8 corruption and evidence consequence.
Neither choice activates a mission, spends nonexistent equipment, changes population directly or grants research.
An independently funded relief mission remains active if an older shortage popup is answered later.
Each local warning and crisis pool includes ongoing-relief and eased-famine acknowledgements, represented as options 5 and 6 in the six-option local pools and gated to original SOV authority.
Those acknowledgements grant no PP, equipment, people or research and do not start another mission.
The delayed crisis skips false catastrophe presentation when famine pressure has already reached zero.
Funded event choices repeat the material check at selection, so a stale quoted option can reach the explicit shortage consequence without a phantom relief award.

The crisis option key is `soviet_gulag.2.shortfall`.
The description retains `soviet_gulag.2.d`.
Both keys have exactly one English definition after the collision repair.

The parent bound `soviet_gulag_relief_funded_tt` inside each accepted event-funded branch in `events/soviet_gulag.txt`.
Its source text expands the three equipment amounts with their actual texticons and the dynamic -2% stability consequence, while the real transaction runs inside hidden presentation to avoid duplicate generated lines.
The ordinary decision consequence tooltip displays the same stability change, and its full cost hover shows the native 30 PP plus the three equipment resources.
The resource quote is unchanged, and event-funded responses charge no additional PP.
The parent repaired source `?R` formatting corruption with a Unicode-escaped atomic write.
These source bindings do not establish final native pixels or debit order.

## Source scenarios

[`soviet_famine_shortfall_source_results.json`](soviet_famine_shortfall_source_results.json) records seventeen passing cases interpreted from the production helper, dispatcher, router, decisions and events.
They cover exact stock, each one-unit equipment shortage, stale paid refunds, site-free funded choices, empty stock without a valid site, distinct warning/crisis penalties, stale event selection, independently active relief, duplicate orders, resolved famine and invalid original authority.
The cooldown case parses the real production action-to-slot-2 mapper and asserts the exact 150-day timed flag request.
Only the native timed-flag primitive is mocked for that mapping proof, rather than a synthetic mapper call count.
Equipment mutation, native PP ordering and mission activation remain explicit mocks.
The two conceal/admission terminal fixtures and five Soviet survivor-release fixtures retain their bounded source evidence, while the latest origin-owner integration reports 35 foundation fixtures.
These results do not establish live click behavior, refund timing, native cooldown or historical calibration.

## MCP and reference evidence

The direct stdio server initialized as `hoi4-agent-tools` 3.6.0 and exposed its tool and task schemas in [`mcp/soviet_famine_2026-10-03/server.json`](mcp/soviet_famine_2026-10-03/server.json).
No native MCP task was requested by the client.
Connected reference calls did not return during this turn and their orchestration cell was terminated before any result was obtained.
Direct `reference_context`, `reference_search` and `reference_read` returned revision-bound evidence for installed `has_equipment` at 3835–3843, offline trigger Equipment at 1509–1583, offline event Options at 153–179, and offline decision cost at 284–336.
The complete context request uses limit 12, rather than treating the earlier omitted sections as read coverage.
The parent also read installed equipment-debit effects at 1252–1265, PP effects at 1854–1862, Script Constants at 216–243, and the manual custom-cost/debit precedent `AFG_recruit_turkestan_legion` around 1685–1750.
The exact underlying paths and source revisions remain in the reference archive.
The exact vanilla source lookup request did not return within its 180-second MCP request limit.
Source review is not substituted for the missing lookup result.
The decision auditor subsequently read installed `common/decisions/RAJ_GOE.txt`, `RAJ_arm_communist_militants` at lines 5095–5169, which combines native `cost = 25`, a custom equipment gate/text and a manual 500-equipment debit.
That installed precedent corrects the older offline-wiki blanket incompatibility sentence as a design blocker.
It does not prove Chaos Redux's native combined-price rendering or engine debit order.

Before copies of the event, decision, trigger, major-country effect and dispatcher files are immutable evidence inputs under the same MCP archive.
The first probability auditor lost its app workspace routing before producing a recoverable baseline result.
Its process/handle was revalidated as absent, and the continuing auditor uses task-enabled 3.6.0 inspect, evaluate, sweep and compare routes.
No AI weight was changed by this transaction patch.
The parent reports complete local event pools, with equipment, variable-backed target and mission inputs still partly unresolved.
The isolated native decision's raw willingness score 40 is score-only, with no exact click probability.
The current [decision audit](soviet_famine_shortfall_decision_audit_2026-10-03.md) retains its named scenarios and analysis identities, and the probability auditor's final scenario-specific handoff remains pending.
Archive requests/results under `mcp/soviet_famine_2026-10-03/` are evidence inputs, not completion proof from a task status alone.
The curator has no exposed `mcp__hoi4_agent_tools__hoi4_*` tools or tool-search route in its current connection, so it cannot perform fresh event inspect/render/compare, GUI or probability checks.
This exact route gap leaves fresh MCP reconciliation blocked here and does not contradict the auditor's independently verified service session.

## Supplied live startup defect

The user supplied the cycle-one startup error for raw line breaks inside `camp_admin_records_unknown_origin_note`.
The parent changed that string to one physical line containing escaped `\n\n` and preserved its current prose pending the approved origin-pause implementation.
The copied cycle-one `text.log` still contains the old duplicate famine-key reports at 08:40:47 and 08:42:01.
It is a launch snapshot rather than a fresh result for the repaired source.
The current key scan is clean for the description and shortfall keys.
The agent did not launch Hearts of Iron IV and makes no clean-startup claim.

## Remaining requirements

- The [decision audit](soviet_famine_shortfall_decision_audit_2026-10-03.md) and [localisation handoff](soviet_famine_shortfall_localisation_2026-10-03.md) preserve their earlier snapshot findings. Their unbound funded-tooltip and synthetic cooldown claims are superseded for current source status by this report, without replacing their unresolved consumer evidence.
- Final scenario-specific matched probability findings and source-linked event inspection/render/compare remain required. The auditor's partly unresolved inputs must stay visible.
- Native combined PP/custom-equipment cost presentation and debit ordering remain unproved.
- A refunded stale click's native re-enable behavior remains unproved.
- Dynamic quote presentation and option tooltip pixels need accepted consumer evidence. The native `countrydecisionview` GUI request timed out, leaving no final decision pixels.
- The current origin owner integration has retired proportional/unknown-pool outside allocation. Parent-owned Records warning, country/programme/lifecycle/UI/localisation integration and matched new visual evidence remain in progress.
- The full camps package remains incomplete and has no scoped completion commit.
