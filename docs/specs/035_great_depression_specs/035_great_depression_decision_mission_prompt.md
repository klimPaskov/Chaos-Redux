# Event 35 Great Depression 2.0 decision and mission implementation prompt

## Goal

Implement the complete Event 35 decision and mission system from specification parts 1 through 9 and the decision and state lifecycle maps. Use one ordinary decision category with one public Depression Severity value, phased action visibility, a selected Depression Center flow, dynamic material costs, AI equivalents, persistent missions, and complete cleanup.

Follow `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-events`, the current Event 35 source, current decision precedents, offline wiki, installed vanilla documentation, and vanilla examples before editing.

## Presentation boundary

Use the ordinary decision interface with:

- Static category picture or accepted phase variants.
- Severity meter or compact progress display.
- Current band.
- Trend.
- Next threshold.
- Up to three causes.
- Current phase.
- Selected Depression Center summary.
- Current recovery-program status.

Do not create a dedicated scripted GUI unless the normal category fails after direct inspection. A later exception requires an accepted layout brief, `chaosx_event_ui_worker`, and mandatory GUI MCP evidence.

## Visible action budget

- Three to five normal primary actions per phase.
- Six is the hard maximum.
- One to three active missions, with two as the normal maximum.
- Hide invalid, obsolete, completed, and contradictory actions.
- Selected-center actions appear only for one current state.
- AI evaluates all centers without using the human selector.

## Core actions

Implement:

1. Emergency Public Works.
2. Rescue Strategic Industry.
3. Stabilize Finance and Trade.
4. Austerity and Retrenchment.
5. Direct State Planning.
6. Let the Market Clear.

Working labels are structural. Write final in-world localisation.

Every action requires:

- Availability and visibility.
- Exact dynamic cost.
- No more than four spendable cost types.
- Non-cost requirements.
- Immediate effect.
- Mission or commitment where applicable.
- Long-term result.
- Failure and cancellation consequence.
- Cooldown and active cap.
- AI score.
- Tooltip and icon.
- Invalid-target and crisis-end cleanup.

## Cost rules

Prefer:

- Civilian factory commitments.
- Trains.
- Convoys.
- Fuel.
- Support equipment.
- Motorized equipment.
- Manpower.
- Stability.
- Temporary output or construction sacrifice.
- Political power only for genuine authority or legislation.

Do not use political power as the universal price. Do not hide a fifth spendable cost in effects or confirmation text.

Use correct texticons and dynamic amounts. Requirements such as state control, supply, route access, or active status are not costs.

## Emergency Public Works

Implement state-targeted employment and infrastructure projects.

Requirements:

- Valid controlled center or approved alternate state.
- Project capacity.
- Required civilian and material resources.

Effects:

- Starts project mission.
- Lowers unemployment pressure while supplied.
- Protects one deterioration step.
- Uses civilian and construction capacity.

Success:

- Meaningful Severity relief.
- Center improvement.
- Infrastructure, railway, maintenance, or recovery legacy according to project.

Failure:

- Abandoned Works.
- Partial material loss.
- Local and national pressure.

Public works cannot grant a free permanent factory.

## Rescue Strategic Industry

Implement state-targeted protection for important factories, resources, supply hubs, or military production.

Effects:

- Protect one closure check.
- Preserve strategic output.
- Shift burden to the wider civilian economy.

Success:

- Better center status and preserved industrial ledger.

Failure:

- Resource loss and stronger shutdown pressure.

AI ranks real strategic value.

## Stabilize Finance and Trade

Implement one national program with emergency and later forms.

Effects:

- Reduce volatility and next-shock size.
- Protect payments, trade, and imports.
- Reduce Financial Contagion risk.
- Support center reopening.

Use current-country institutional language. Do not hardcode American agencies.

## Austerity and Retrenchment

Implement an actual tradeoff.

Immediate results:

- Release or reduce commitments.
- Raise unemployment and possibly Severity.
- Cancel or weaken selected projects.
- Increase political and relapse risk.

Later results:

- Lower program burden if social order holds.

Do not allow one click to give immediate Severity relief and full capacity return without cost.

## Direct State Planning

Implement a national commitment that coordinates orders, finance, allocation, and strategic production.

Effects:

- Preserve output and employment.
- Improve rescue and project reliability.
- Create authority, administrative, and flexibility costs.
- Interact with Social Collapse actor pressure.

Adapt final text and availability to country context.

## Let the Market Clear

Implement a timed liquidation route.

Requirements:

- Valid selected center or sector.
- Protected industrial floor remains.
- No duplicate liquidation.

Immediate results:

- Severity and unemployment increase.
- Support ends.
- Center begins closure or consolidation mission.

Long result:

- Lower future burden after actual loss.
- Consolidation or hollowing legacy.

The route must record exact Event 35 industrial loss for achievements and cannot substitute unrelated war damage.

## Selected Depression Center flow

Use a target selector or current target pattern that shows one center to the human player.

Required center actions:

- Protect Center.
- Reopen Idled Plants.
- Rebuild Shuttered Center.
- Restructure or Consolidate.
- Abandon Center.

Selector requirements:

- Valid center list.
- State name and status.
- Current project and risk.
- No stale selected state after transfer, recapture, annexation, recovery, or deletion.
- AI bypass that evaluates all valid centers.

## Missions

Implement:

- Halt the Panic.
- Keep Essential Industry Running.
- Put the Depression Centers Back to Work.
- Hold the Social Peace.
- Prove the Stabilization.
- Prove the Recovery.
- Emergency National Stabilization.

Mission rules:

- Auto-complete when the objective is met.
- Use dynamic duration from centralized constants.
- Name exact states, thresholds, and actions.
- Distinct success and failure effects.
- No second payment click after the objective is complete.
- Cancellation on invalid country without failure effect.
- Save-safe mission progress.

## Phase visibility

### Panic and Contraction

Show:

- Public Works.
- Strategic Rescue.
- Finance and Trade.
- One policy commitment.
- Halt the Panic.

### Depression

Show:

- Three most relevant intervention actions.
- One compatible route action.
- Selected-center actions.
- One or two missions.

### Stabilization

Show:

- Maintain or unwind program.
- Reopen remaining centers.
- Relapse protection.
- Prove Stabilization or Recovery.

### Recovery

Show:

- Final center work.
- Program consolidation.
- Prove Recovery.

Emergency actions appear only in valid emergencies.

## Policy consistency

Track qualitative program history. Contradictory rapid switches create an efficiency or relapse penalty. A deliberate transition action can change program safely.

Required compatibility behavior:

- Public works and immediate austerity conflict.
- Rescue and liquidation of the same center conflict.
- State planning and abrupt market clearing conflict.
- Finance stabilization supports several programs.
- Mixed coherent policy is valid when transitions are deliberate.

Do not expose a raw hidden policy score.

## Evolution I decision additions

Implement compact source and exposed-country actions:

- Request aid.
- Clearing arrangement.
- Restrict outflows.
- Prioritize domestic recovery.
- Offer boom supply contract.
- Shield domestic finance.
- Diversify trade.
- Support source.
- Withdraw from market.
- Exploit supply gap.

Expose only actions relevant to the current role and link. Aid requires donor debit, recipient receipt, dependence, exposure, cooldown, and rollback proof.

## Evolution II decision additions

For each major incident, implement valid response families:

- Relief and bargaining.
- Nationalization or direct planning.
- Reform and settlement.
- Emergency rule or suppression.
- Corporate rescue.
- Liquidation.

Do not display every response when the country cannot plausibly use it. Civil-conflict actions remain hidden until the hard gate.

## Evolution III decision additions

Implement compact global-stage actions:

- Emergency Trade Clearing.
- Reconstruction and Employment Fund.
- Protect Domestic Market.
- Coordinate Industrial Demand.
- Recovery Conference.
- Withdraw from International Commitments.

Most countries should not receive all actions at once. Filter by role, global stage, material capacity, faction or regional relationship, and national vulnerability.

## AI

AI uses the same effects and costs.

Implement profiles from part 9 and named scenarios from the AI matrix. AI must:

- Reserve resources for active missions.
- Rank centers by actual value.
- Avoid policy spam.
- Avoid liquidation of last viable center.
- Contain near-conversion exposure.
- Support allies and subjects only when affordable.
- Reject dangerous boom supplier contracts.
- Avoid coup or civil-war options before their full gate.

Every weighted decision and target requires the audit, patch, compare cycle.

## Dynamic localisation

Show:

- Severity and band.
- Trend and causes.
- Next threshold.
- State name and status.
- Exact dynamic cost.
- Mission duration.
- Required threshold.
- Source or donor country.
- Current global stage.

Use concise tooltips. Do not expose raw scripted triggers, internal variables, hidden actor pressure, or future outcomes.

## Assets

Use final assets from the Event 35 asset handoff:

- Category icon and pictures.
- Core action icons.
- Center action icons.
- Mission icons.
- State status icons.
- Evolution and worldwide action icons.

Do not use missing, unrelated, resized, or primitive placeholder icons.

## Cleanup and exploit checks

Verify:

- Commitments release once.
- Resource debits cannot duplicate.
- Failed transaction refunds only proven debit.
- Projects cannot be started beyond caps.
- Threshold rewards cannot repeat.
- State transfer removes old actions.
- Recovery hides every crisis action.
- Annexation clears national action state.
- Aid cannot farm influence or resources.
- Liquidation records exact source and respects floors.
- Save and reload cannot reroll or duplicate missions.

## Required audit handoff

Run `chaosx_decision_mission_auditor` after implementation. The handoff must list:

- Categories.
- Decision IDs.
- Mission IDs.
- Cost types and ranges.
- Active caps.
- State selector identifiers.
- AI weights and scenario evidence.
- Localisation keys.
- Icons.
- Cleanup effects.
- Exploit findings.
- Missing or simplified content.

Do not claim the decision system complete while any core action, mission, phase, AI path, state action, evolution action, cost text, icon, cleanup path, or audit scenario is missing.
