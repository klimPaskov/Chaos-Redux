# Event 021 takeover status, 2026-10-06

Disposition: implemented in source and assets, with live acceptance and incomplete MCP certification still open.
Event 021 and SCN-018 retain `Needs Testing`.
No Hearts of Iron IV session, desktop window, Blender worker, spreadsheet or CSV was operated by this pass.

## Commits and ownership

- `0ff1cdfb9cf8e148433813d2bde30b46261d0ebc`: regional exposure, campaign adaptation, mobilization, sponsor counterplay and cleanup, forced-entry explanations, crisis-based popup guards, historical detail selection and production-helper regressions.
- `22d2029d09330cfe54d9d418a5ae3a9ea1e38965`: relief and reconstruction icon repairs, transparent source crops, previews and measurement evidence.
- The documentation commit containing this report is identified by `git log -1 -- docs/plans/021_random_civil_war_plans/takeover_status_2026-10-06.md`.

The implementation commit contains only Event 021 paths and three shared Event Log hook lines.
The unrelated 33-line equipment-from-heavens changes in the shared effects file and the separate history-empty predicate change in the shared GUI file remain outside this pass.
Both commits use an isolated index, `commit-tree`, compare-and-swap publication and path-scoped real-index reconciliation.
Every inherited 021 change present when this pass began was reviewed, and none was dropped.
The restart preserved the uncommitted pass, which was resumed and committed.

## What was verified and completed

The latest takeover history ended at audit round 3.
Four later commits already implement D33 to D36: `f47e57c54`, `9eb1ce3d4`, `701419d6f` and `c03bcf4cc`.
Their source was reviewed rather than replaced.

| Remaining audit item | Current disposition and evidence |
| --- | --- |
| Authority deltas repeated and leaked between crises | D33 applies only the pending delta, uses transition helpers and clears condition flags at cleanup and new-role initialization. |
| Authority did not follow the war | D34 applies severity, capital and supply transitions, held-territory changes and settlement outcomes through the existing state-control hook and bounded review. |
| Permanent pressure relief accumulated without limit | D35 bounds the modifier at -30 to 30 and moves it six points toward zero per due review. |
| Unaffordable postwar reform and incorrect incident wording | D36 gives reform a political-power gate and valid AI fallback, with role-aware tolerance text. |
| Exposure had no lasting risk or readable stage | D37 establishes the existing nearby-conflict input, advances unanswered exposure on due reviews, lowers it through containment, shows its stage and leaves a 180-day risk tail. |
| Active sides had no chosen adaptation or high-chaos tool | D38 provides a paid 90-day specialization and one 60-day regional mobilization with civilian strain and recurrence memory. |
| Sponsor counterplay and neighbour families were missing | D39 adds the exact-sponsor response and maps related containment, relief and aid families to the existing compact actions. |
| Event Log historical detail pointer was never published | D41 joins each immutable detail row to its shared history sequence and resolves the selected row before opening the details view. |
| Small decision icons were undersized | Both reviewed sprites retain 32x32 consumers, with relief at 28x27 visible pixels and reconstruction at 28x25. |
| Forced entry could remain silent | D43 reports active crises, pending foreign claims, exhausted capacity or missing viable regions through the owning entry and localisation. |
| Aid cleanup could clear an uninvolved sponsor | D44 follows only the reciprocal relationship and releases the matching sponsor when its recipient leaves. |
| Succession and later fronts could repeat presentations | D45 keeps durable crisis identities for war news and neighbour reports, with aggregate scenario presentation. |
| A regular source target could leak across exposure reviews | D46 rebinds the current source and prevents the child from overwriting the caller's global source target. |

The earlier routed country-only `exists` checks in state scopes remain removed in `00fe90801` and `488e37e11`.
Mission binding, the 90-day terms gate, the variable settlement hold, distinct postwar directions, visible strange incidents, independent disabled evolution scheduling, priority-front targeting, dynamic-tag admission and the shared date wrapper remain in place.
The CXT daily hook only registers content and marks synchronization pending through the existing shared helper.
It does not grant content periodically.

## Design, balance and presentation

The accepted decisions and their reasons are recorded in `agent_decisions_2026-10-05.md`, D37 to D47.

- Adaptation spends 15 army experience and 200 rifles, then chooses supply escorts, defensive positions or mobile columns for 90 days.
- Each specialization has a distinct useful benefit and a military disadvantage.
- Mobilization spends 1,500 rifles and 100 support equipment and applies 60 days of military strength, temporary stability loss and consumer goods burden.
- Counting both civilian sacrifices gives four cost types, so the draft command-power payment was removed.
- Mobilization adds 12 to the government's later recurrence calculation, including a successor government.
- Exposing intervention spends 25 political power and 50 support equipment, ends the matching commitment and costs 30 sponsor opinion, retaining delivered arms.
- A response slot opens only after a current-phase order closes, keeping at most six selectable actions including the capital commitment card.
- Unaffordable optional responses do not occupy that slot or consume their use.
- The regular government chain has at most six presentations: opening, multifront news, optional strange incident, chosen adaptation, settlement and final verdict.
- A neighbour receives one border report per ordinary source crisis, including through succession or later fronts.
- Scenario wars use the aggregate launch presentation, with no per-target multifront news or border popup cascade.

The campaign modifier text reads shared tuning values.
Native idea modifier macros mirror that table because their consumer does not accept `constant:` values.
The macro values and displayed values were checked for agreement.
The existing opening report picture, Fractured Command and War-Torn Administration pictures, and registered priority-front and loyalty-review decision sprites are reused.
No new portrait, custom GUI, focus tree, model or super-event is introduced.

The relief icon's initial mean alpha of 192.175 was corrected to 201.092, with unchanged visible bounds and transparent corners.
The reconstruction mean alpha is 216.106.
Both final DDS files were visually reviewed on light and dark backgrounds and decode correctly.
Their source crops and review evidence are committed, while intermediate converter output remains in the active asset workspace.

## Meaningful validation and limits

- Calendar regressions: 6 checks, including actual shared conversion and caller-owned deadlines.
- Evolution logging regressions: 12 checks.
- Front-plan regressions: 3 checks.
- Sponsor and news regressions: 8 checks executing the production helpers against bounded country fixtures, including stale pair protection, reciprocal cleanup and succession news suppression.
- Report colour audit: no coloured title or description key reached by the Event 021 report/news chains.
- Localisation and completion auditors reviewed the new surfaces, and the parent resolved their phase-count and documentation findings.
- Whole-file MCP validation was requested for every changed event, decision, scripted effect, scripted trigger and shared hook surface.

The new event and decision file checks returned no reported errors.
Helper checks remain partial because root scopes or native argument blocks are not fully certified by the file route.
An explicit country-scope news-helper check confirmed native command kinds and declared scopes, while listing six argument blocks as unchecked.
The pertinent cited array, variable and news syntax was then read directly.
The fixture regressions do not execute the game, prove timer expiry or certify native civil-war allocation.

The probability specialist discovered the three new decision weights but could not produce reliable final scenario scores.
Option inspection and four-scenario evaluation each returned `timed out awaiting tools/call after 600s`.
The emergency-terms comparison had zero eligible rows and 13 unresolved inputs, so its zero-change output is not numerical certification.
Its exact source hashes, scenario matrix and artifact links are in `subagent_handoffs/2026-10-06_probability_audit.md` and its evidence folder.

The event render timed out after 600 seconds.
The graph comparison returned `EVENT_GRAPH_ARTIFACT_INVALID` for an unsupported graph schema version.
The shared GUI inspection returned generated-state diagnostics, which are not accepted phase fixtures.
The intended detail render returned `RENDER_DIMENSIONS_BLOCKED`, with hierarchy dimensions 900x50276 exceeding the 16384-pixel limit and no PNG.
Matching before-and-after visual acceptance therefore remains open, and source review is not substituted for it.

## Exact orchestrator live checks

Use a copy derived from `qa_001_fresh_head` where available, with the current pass's commits loaded.
Use Germany as the multi-state government fixture, or another normal multi-state country with real starting forces if Germany is unavailable in that setup.
The commands below assume Germany and a claimant shown as D01, with the claimant tag substituted when the engine uses another dynamic tag.
Console and forced setups deliberately disqualify achievement unlocks, while still allowing their tracking conditions to be inspected.

### 1. Opening and refusal

Set the player to Germany and prepare a bounded fixture:

```text
tag GER
pp 500
cp 100
xp 100
ae 10000 infantry_equipment_1
ae 500 support_equipment_1
ae 200 motorized_equipment_1
ae 50 convoy_1
manpower 50000
eval_effect GER = { add_stability = -0.5 }
event chaosx.nr21.1 GER
```

Expect one government opening report with three postures, a real claimant or a precise refusal, and a readable State Authority band.
Use Settings to force Event 21 again while that crisis is active.
Expect one refusal explaining the active crisis, with no extra claimant, army split or repeated report loop.
In a separate capacity-saturated setup, expect the corresponding capacity explanation rather than silence or a same-tag substitution.

### 2. Evolution I and phase budget

Start from the baseline-war fixture, enable Evolution I in Settings, and set the matching Chaos tier through the existing UI.
For a bounded transition check:

```text
eval_effect GER = { set_global_flag = random_civil_war_evolution_i_unlocked }
event chaosx.nr21.11 GER
```

Expect a viable added side or the management phase without an invented side.
Check priority-front targeting, capital defense and integration, including the no-side management result.
An opening arsenal order alone must not open an extra response row after the phase changes.
Taking a current-phase order must open one response slot, with at most six selectable actions.

### 3. Authority and uninterrupted missions

Select Defend the Capital, then the capital hold.
Use the actual claimant tag in this state-scope effect:

```text
eval_effect GER = { var:event021_hold_capital_mission_target_state = { set_state_controller_to = D01 } }
```

Expect immediate hold failure, capital-loss authority reduction and a reachable weaker band.
Restore control with `set_state_controller_to = GER` in the same bound state.
Expect recovery to apply once, without turning later action costs into gains.
Repeat the control interruption using `var:random_civil_war_rail_mission_state` during its 30-day hold.
A fresh uninterrupted capital hold must resolve only after its configured 150 days.
Observe lost and recovered core territory changing authority and the pressure summary.

### 4. Terms and postwar hold

Without mediation, emergency terms must remain unavailable before crisis day 90.
With a valid neighbour mediation, they must become available earlier and count as negotiated.
Signing must stop the relevant war and begin the correct obligation and aftermath.
Select Hold the Settlement Terms on settlement day 30.
Expect roughly 150 days remaining, ending at settlement day 180, with the parent review not judging ahead of the active hold.
A held obligation gives its stated reward and one accurate final verdict.
A breach gives its distinct consequence and one accurate final verdict.
For a government military victory, compare the four directions and verify reform is unavailable below 30 political power.

### 5. Evolution II exposure and source identity

Enable Evolution II and use:

```text
eval_effect GER = { set_global_flag = random_civil_war_evolution_ii_unlocked }
event chaosx.nr21.12 GER
```

Switch to a neighbouring normal country outside the war and open the crisis category.
Expect a named live source and Observed, Pressured, Penetrated or Mobilizing exposure.
Monitoring and mediation lower one stage and hold advancement during their existing response periods.
Unanswered exposure advances only on due reviews and Mobilizing raises risk without automatically starting a war.
Close the source war and observe category cleanup plus a finite 180-day nearby-conflict tail.
Use two distinct source wars in one review pass to verify each neighbour points to the current source, rather than the first source in the effect chain.
Re-exposure by a later front in the same ordinary crisis must not repeat its border report.

### 6. Adaptation and high-chaos mobilization

Return to a live side in the Evolution II war, with one current-phase order taken and adequate resources.
Expect Adapt the Campaign in the response slot.
Take it and verify exactly 15 army experience and 200 rifles are spent, with one report.
Test supply, defense and columns in separate fixture copies.
Defense must appear only for a country with mountain or urban terrain.
Expect one matching 90-day idea and its stated military disadvantage, with no second specialization from the same report or decision.
Set Totalen Chaos or World Collapse through Settings, then take Mobilize the Region after adaptation.
Expect 1,500 rifles and 100 support equipment spent, no command-power debit, the 60-day idea and visible civilian sacrifices.
Verify cleanup removes the military ideas and recurrence memory follows the surviving government.

### 7. Sponsors, counterplay and cleanup isolation

From a valid exposed neighbour, fund the opposition with the existing support decision.
Expect the actual recipient to receive its stated rifles and the government's intervention loss to occur once.
Return to the government, free the response slot and take Expose Foreign Intervention.
Expect 25 political power and 50 support equipment spent, the exact commitment ended, sponsor opinion reduced by 30 and delivered arms retained.
Use a second neighbour supporting the government and a third neighbour merely monitoring the border.
Cleaning up the monitoring neighbour must not erase the second neighbour's aid.
Ending the actual recipient's crisis must release its matching sponsor on both sides.

### 8. Strange incident, succession and popup budget

Exercise the existing rare incident through its normal eligible Evolution II path.
Expect one uncertain report per affected side, a benefit with strain, and the three material responses.
Let a claimant replace the government in an ordinary multifront war.
Expect no repeated multifront news, preserved fronts and mobilization memory, and the existing external-war prompt only for a valid missing relation.
An AI successor must not receive a human prompt.
Count presentations against the six-item ordinary government budget above.

### 9. Event Log and icon consumers

Open the earliest Event 21 history entry, a later settlement entry and an unrelated event entry in turn.
Expect each historical entry's own country, cause, severity, capital, fronts, sponsor and settlement values, including the first zero-based row.
The unrelated entry and ordinary Event 21 catalog view must show no stale historical crisis summary.
Inspect long country names, scrolling and the compact summary for clipping or overlap.
Inspect Relief Corridor and Reconstruction at native decision-panel size, with similar framing to their siblings and no alpha fringe.

### 10. Maximum, disabled stages and persistence

From the fresh fixture, launch SCN-018 through Settings at Maximum and inspect its aggregate outcome.
Expect guarded dynamic-tag admission, explicit capacity shortfalls, no fabricated same-tag replacement for a safe multi-state target, and no per-country news or border-report cascade.
Disable each evolution individually, advance the bounded scheduler and confirm no repeated disabled-stage callbacks or blocked enabled successor stages.
Re-enable a stage and verify its normal scheduling resumes.
Save and reload during an active mission, exposure and settlement obligation, confirming targets, fronts, phase, timers and report identities persist.
Check native civil-war rounding and restoration of forces, stockpile and manpower after a deliberately rejected opening.

## Simplifications, omissions and blockers

No gameplay route was replaced by an unapproved fallback.
Related arms-route and recruitment actions intentionally share Monitor the Border, while displaced-civilian aid and military corridors use the existing relief and support actions.
The history panel intentionally omits the dense force ratios, equipment band, priority-front and package bookkeeping from its visible summary, while retaining those values in its immutable arrays.
This presentation reduction is recorded under D41.
Native modifier macros remain mirrored rather than replaced with unsupported `constant:` tokens.
Numeric probability, complete helper semantics, matched GUI renders and live acceptance remain incomplete for the reasons above.
The grounded KUB portrait remains a wired source placeholder pending the user's HOI4-style final.
Inherited Event 006 package acceptance belongs to its owner and is not certified by this pass.
Catalog wording is queued in `catalog_changes_pending.md`, with no workbook or CSV changes.

## Skills and future work

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-scripted-gui`, `chaos-redux-event-assets`, `chaos-redux-subagents` and `chaos-redux-shared-git-commit`.
No new skill was created or updated, as the relevant source, array, cleanup, cost and asset rules are already covered.
A later accepted expansion could distinguish verified rail operations from the current general supply plan, using the existing front targets rather than another meter or decision category.
No such expansion is implemented or queued by this pass.
