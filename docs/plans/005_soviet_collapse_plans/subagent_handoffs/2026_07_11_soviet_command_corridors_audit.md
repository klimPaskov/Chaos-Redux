# Event 005 Command and Corridors Read-Only Audit

**Date:** 2026-07-11
**Mode:** read-only `chaosx_decision_mission_auditor`
**Audited surface:** current Command and Corridors backend/main wiring in the Event 005 constants, scripted triggers, scripted effects, decisions/missions, scripted localisation, English localisation, event entry/refill flow, and AI strategies.
**Verdict:** **not completion-ready**. The 118-mission classification, capped refill integration, and exactly-one compromise resolution are structurally sound. Live corridor binding, posture/crisis prioritisation, release-cause consumers/scopes, and the UWR/KMB hooks still contain acceptance-breaking omissions.

This audit did not edit gameplay files and did not create a commit.

## Required references consulted

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- the required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on-actions, events, decisions, ideas, and AI
- vanilla `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, script-constant documentation, AI-strategy documentation, and vanilla mission/decision precedents
- `2026_07_11_soviet_collapse_improvement_loop_addendum.md`
- `2026_07_11_soviet_command_corridors_backend_handoff.md`

## Acceptance blockers

### [P1] The 21 corridor missions are admission-gated, not bound to a live state for their full lifetime

The state-selection primitives themselves are valid and use no fallback:

- `is_soviet_collapse_corridor_state_candidate` and `has_soviet_collapse_selected_corridor_state` are at `common/scripted_triggers/005_soviet_collapse_triggers.txt:8883-8914`.
- They require original Union territory, current ownership and control by Moscow, passability, and at least one supported supply-node, naval-base, railway-connection, or border condition.
- `soviet_collapse_select_corridor_state_candidate` at `common/scripted_effects/005_soviet_collapse_effects.txt:25929-25939` clears the old pointer before selecting a random live candidate. No named state or hardcoded substitute exists.
- The priority prefill has one outer live-target guard at `:26202-26239`; the ordinary remainder has a live-target guard on all 21 corridor activations in `soviet_collapse_activate_opening_objectives` at `:27784-27901`.

The invariant stops there. A brace-aware scan of all 21 mission definitions found:

- 21/21 have an `available` block;
- 0/21 `available` blocks reference `has_soviet_collapse_selected_corridor_state`;
- 0/21 mission blocks reference `soviet_collapse_corridor_state_target` at all.

The affected definitions begin at these lines in `common/decisions/005_soviet_collapse_decisions.txt`:

`005:604`, `006:638`, `017:1017`, `034:1605`, `038:1742`, `043:1915`, `046:2017`, `047:2051`, `053:2260`, `056:2362`, `061:2533`, `062:2567`, `063:2604`, `068:2783`, `069:2821`, `091:3640`, `094:3759`, `098:3908`, `099:3969`, `106:4267`, and `127:4740`.

For example, mission 005 at `:604-637` can complete from `can_count_soviet_collapse_missing_trains` and mission 127 at `:4740-4772` can complete from `can_inventory_soviet_collapse_recovered_depots`; neither proves that the selected state is still live or that the work occurred there. If ownership/control/geography changes after activation but before the next refill, a mission can still complete. If it reaches its deadline first, its `timeout_effect` still records a corridor-family failure even though the geographic project ceased to exist.

The existing shared trigger **can and should be reused in all 21 `available` blocks**; a new wrapper is not required merely for the live-state test. However, `available` alone is insufficient because a non-selectable mission whose `available` becomes false will still time out. The bounded safe correction is:

1. add `has_soviet_collapse_selected_corridor_state = yes` to every corridor mission's `available`/hidden trigger;
2. add the shared cancellation invariant to every corridor mission:

   ```text
   cancel_trigger = {
	   NOT = { has_soviet_collapse_selected_corridor_state = yes }
   }
   cancel_effect = {
	   soviet_collapse_queue_objective_refill = yes
   }
   ```

   This removes an invalid project without running success or timeout effects and refills the freed slot through the existing scheduler.
3. make each completion predicate derive its rail/depot/port/border/supply work from `var:soviet_collapse_corridor_state_target`. The shared live guard proves only existence; it does not satisfy the accepted requirement that the project itself be tied to the selected state. Similar projects can share a small number of state-scope scripted triggers, but the 21 results still require manual semantic review.
4. add the live target to `can_pay_soviet_collapse_corridors_and_depots_compromise_cost` or the corridor compromise decision. At present, an invalid-but-not-yet-pruned corridor mission can be compromised for political power.

Until item 3 is implemented, the backend handoff's admitted non-targeted-mission simplification remains a direct divergence from “Bind geography to real state conditions.” The accepted addendum explicitly approved no fallback or simplification.

### [P1] An invalid corridor pointer is not cleared when no replacement candidate exists

`soviet_collapse_activate_opening_objectives` only calls the selector when the stored target is invalid **and** another candidate exists (`common/scripted_effects/005_soviet_collapse_effects.txt:27738-27745`). The selector itself is already safe without a candidate because it clears first and selects only inside an `if` (`:25929-25939`). Consequently, the outer `has_soviet_collapse_corridor_state_candidate` condition leaves the old country variable and old state flag behind when the final candidate becomes invalid.

Missions are pruned and scripted localisation displays the absent branch, but the stale state can silently become selected again if it later happens to satisfy the candidate trigger. This contradicts the handoff's claim that the target is refreshed or cleared.

Bounded correction: when `NOT = { has_soviet_collapse_selected_corridor_state = yes }`, call `soviet_collapse_select_corridor_state_candidate` unconditionally. Its existing clear-first implementation handles both replacement and no-candidate cases. Terminal and reconquest cleanup already reach `soviet_collapse_clear_corridor_state_candidate` through `soviet_collapse_cleanup_terminal_collapse_missions` (`:25364-25417`).

### [P1] Crisis thresholds suppress the family that made the crisis worse

The priority formula at `common/scripted_effects/005_soviet_collapse_effects.txt:26033-26153` measures:

- Chain: Authority deficit plus Obedience deficit;
- Corridors: Depot Vulnerability above its ceiling;
- Settlement: Armed Breakaway Momentum above its ceiling;
- then adds bounded Foreign, League, and Old Movement modifiers.

The constants at `common/script_constants/005_soviet_collapse_constants.txt:2596-2612` switch from contested `50 / 45 / 42 / 30` to crisis `45 / 48 / 58 / 56` for Authority / Obedience / Republic / Depot. Only Obedience becomes more demanding. Authority becomes easier, while the two dangerous-value ceilings become dramatically more permissive.

With secondary pressures set to zero, the discontinuity is concrete:

| Forced crisis components | Current crisis primary scores | Contested-band scores | Result |
|---|---:|---:|---|
| A 55, O 50, R 42, D 55 | Chain 0, Corridor 0, Settlement 0 | Chain 0, Corridor 25, Settlement 0 | Current tie-break selects Chain and ignores severe depot pressure. |
| A 55, O 50, R 55, D 30 | Chain 0, Corridor 0, Settlement 0 | Chain 0, Corridor 0, Settlement 13 | Current tie-break selects Chain and ignores high breakaway momentum. |
| A 47, O 47, R 42, D 30 | Chain 1 | Chain 3 | Crisis relaxes the Authority deficit even while the center is weaker. |
| A 55, O 50, R 60, D 60 | Corridor 4, Settlement 2 | Corridor 30, Settlement 18 | The correct families remain ordered, but their primary urgency is almost erased and can be overtaken by secondary noise. |

This is not defensible as “triage tuning” for the accepted design. The board already reserves one mission per family before filling remaining slots, so it does not need relaxed crisis ceilings to preserve variety. The current values also affect release-cause attribution because `soviet_collapse_record_dominant_release_cause` calls the same priority computation.

Recommended bounded tuning: enforce a monotonic recovery invariant—crisis Authority/Obedience floors must not be below contested floors, and crisis Republic/Depot ceilings must not be above contested ceilings. A conservative concrete first pass is **50 / 48 / 42 / 30**: preserve the intentional crisis Obedience emphasis while stopping Authority, Republic, and Depot pressure from disappearing. Re-run the four scenarios above plus mixed Foreign/League/Old Movement cases before accepting balance.

### [P1] Priority is not posture-aware, and the first board is filled before the player chooses a posture

The accepted design says to calculate distance from the **posture's** safe band. The priority effect contains no reference to any opening posture flag; it chooses only calm, contested, or crisis windows (`common/scripted_effects/005_soviet_collapse_effects.txt:26033-26065`). The posture flags are set in `events/005_soviet_collapse.txt:62`, `:77`, `:92`, and `:113`, but the first `soviet_collapse_activate_opening_objectives` call occurs in event `chaosx.nr5.2` immediate at `:50-56`, before any option runs.

Therefore the initial family priority cannot reflect the player's posture, either through the flags or through the option deltas. This is more than a display lag: it decides which family receives the first reserved slot.

Bounded correction:

1. move the initial activation from `immediate` to the event's `after` block (or one shared helper called by every option) so posture flags and deltas exist first;
2. add posture-specific safe-band offsets/constants to `soviet_collapse_compute_operational_family_priorities`, or explicitly change the accepted design/documentation if the intended model is crisis-window bands rather than posture bands.

### [P1] Neighbor reactions read the wrong country through `ROOT`

Release cause flags and the numeric cause are recorded on the newly set-up breakaway. `soviet_collapse_apply_release_cause_neighbor_reactions` then iterates its neighbors at `common/scripted_effects/005_soviet_collapse_effects.txt:4642-4674`, but inside the iterator it reads:

- `ROOT.soviet_collapse_release_cause` at `:4647`; and
- `ROOT = { has_soviet_collapse_release_cause_* = yes }` at `:4653-4668`.

`ROOT` is not reliably the released country. Many setup calls occur inside SOV-rooted `for_each_scope_loop`/country iterators (examples at `:2900-2923`, `:2985-3008`, and `:3159-3198`), so the current country is the released country while `ROOT` remains Moscow or another outer actor. In those paths the neighbor gets a zero/missing last cause and none of the cause-specific component changes.

Safest bounded scope pattern: at the start of the released-country helper, use a regular event target and reference it explicitly inside the neighbor iterator:

```text
save_event_target_as = soviet_collapse_release_actor
every_neighbor_country = {
	limit = { has_country_flag = soviet_collapse_breakaway }
	set_variable = {
		soviet_collapse_last_neighbor_release_cause = event_target:soviet_collapse_release_actor.soviet_collapse_release_cause
	}
	if = {
		limit = { event_target:soviet_collapse_release_actor = { has_soviet_collapse_release_cause_command_fracture = yes } }
		# bounded reaction
	}
}
```

A regular event target is preferable to a global target: it survives the nested iterator, carries through the current effect chain, automatically clears, and cannot leak across releases. Direct `PREV` could work at the first iterator depth, but the named event target is safer against later nested scopes.

### [P1] “Sponsor interest” is recorded but never applied

`soviet_collapse_record_dominant_release_cause` writes `soviet_collapse_release_sponsor_interest` at `common/scripted_effects/005_soviet_collapse_effects.txt:4718`, `:4730`, `:4741`, and `:4747`, then sets `soviet_collapse_release_sponsor_interest_active` at `:4750-4752`. A repository-wide gameplay search found no reader of either identifier. The values are dead state and cannot affect a sponsor, target selection, foreign-decision AI, or influence.

Bounded correction: consume `FROM.soviet_collapse_release_sponsor_interest` in the existing dynamic foreign-patron target/decision path, preferably as a centralized AI-weight or initial influence modifier when a patron evaluates/selects that released country. Do not create another patron scheduler. Keep command fracture at its intentional zero, and let corridor/negotiated/foreign causes contribute their configured `1 / 1 / 4` weights. If immediate component pressure is used as well, route it through the existing influence/patronage clamp helpers rather than inventing a parallel variable.

The neighbor metadata `soviet_collapse_neighbor_release_reaction_pending` and `soviet_collapse_last_neighbor_release_cause` is likewise only written. Once the scope bug is fixed, the immediate component adjustment can satisfy the neighbor-reaction requirement; either remove the unused pending metadata or add a one-time consumer and clear it. Do not leave permanent “pending” flags with no consumer.

### [P2] Release cause is calculated after the release has already altered Moscow's pressures

In `soviet_collapse_apply_breakaway_setup_package`, the opening/follow-on breakaway pressure and evolution bookkeeping run before `soviet_collapse_record_dominant_release_cause` (`common/scripted_effects/005_soviet_collapse_effects.txt:4801-4843`). The recorded “cause” can therefore include the consequences of the current release, and sequential opening-wave releases can contaminate the attribution of later releases.

The later application order is otherwise correct:

- record cause at `:4843`;
- add cause-specific force package at `:5076`;
- initialize republic components, then add cause-specific setup at `:5096-5100`;
- set Moscow's next-priority flag during recording.

Recommended bounded correction: compute and store the cause before applying the current breakaway's source/follow-on pressure, while retaining the explicit recent-failure boosts. Then apply the stored cause to the force/setup packages after ordinary setup as now. This makes “cause” describe the crisis that produced the release, not the release's own aftermath.

### [P1] UWR and KMB crisis hooks are definitions without call sites

The backend defines:

- `soviet_collapse_apply_kmb_treaty_corridor_crisis_hook` at `common/scripted_effects/005_soviet_collapse_effects.txt:27584-27598`;
- `soviet_collapse_apply_kmb_concession_crisis_hook` at `:27600-27613`;
- `soviet_collapse_mark_uwr_contaminated_state_for_aftermath` at `:27617-27633`.

There are no gameplay call sites for any of them.

Exact missing integrations:

- `kmb_sign_resource_treaty` (`common/decisions/005_soviet_collapse_decisions.txt:13165-13203`) never calls the treaty hook.
- `kmb_force_mining_concession` (`:13233-13323`) never calls the concession hook.
- The actual contamination effect `soviet_collapse_uwr_contaminate_neighbor_front` (`common/scripted_effects/005_soviet_collapse_effects.txt:20367-20397`) applies anthrax/plague inside the victim state but never calls the aftermath marker. Both UWR focus rewards at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1515` and `:1542` already funnel through this one effect, so one correctly scoped call there covers both.

The UWR marker also stores `OWNER` as `soviet_collapse_uwr_contamination_source` (`common/scripted_effects/005_soviet_collapse_effects.txt:27621`). At the affected state, `OWNER` is the victim country, not the UWR actor. Save the UWR country as a regular event target before `every_neighbor_country`, call the marker immediately after the contamination application in state scope, and store that event target as the source.

Until these call sites exist, UWR and KMB do not participate in the shared crisis through the advertised hooks.

### [P1] KMB AI uses an undefined scripted trigger

`common/ai_strategy/005_soviet_collapse.txt:930` and `:945` reference `has_soviet_collapse_kmb_superior_concession_target`. No definition exists in `common/scripted_triggers/005_soviet_collapse_triggers.txt` or elsewhere in gameplay script. The treaty/concession postures therefore cannot be considered valid.

`kmb_force_mining_concession` already repeats the intended country-scope neighbor test in its `available`, completion selection, and `ai_will_do` blocks (`common/decisions/005_soviet_collapse_decisions.txt:13236-13311`): an existing neighbor, no current war, legal declaration, and KMB strength ratio above `constant:soviet_collapse_kmb_ai.superiority_ratio`.

Bounded correction: define one reusable country-scope `has_soviet_collapse_kmb_superior_concession_target` with that exact test and use it in the decision and both AI strategies. This eliminates three repeated scope chains and prevents decision/strategy semantics from drifting. A separate “valid target” trigger is only needed if legality and superiority are intentionally distinct concepts.

The remaining KMB/UWR strategy scopes are coherent: UWR and KMB are gated by original tag, successor identity, and live successor surface; KMB basin control checks state 569 from KMB scope; coal-golem production uses the existing archetype; release-cause AI is gated to breakaways during active/terminal aftermath. UWR AI still only translates route flags into generic army/production/concentration weights; without a contamination decision or wired aftermath hook, it does not yet satisfy the accepted facilities, payload-readiness, controlled-contamination, and expansion-target behavior.

### [P2] KMB cost constants are unused magic-number duplicates

`soviet_collapse_kmb_balance` defines all six decision costs at `common/script_constants/005_soviet_collapse_constants.txt:1542-1547`, but the six KMB decisions still use literal `20 / 25 / 25 / 35 / 30 / 45` costs at `common/decisions/005_soviet_collapse_decisions.txt:13061`, `:13088`, `:13115`, `:13167`, `:13207`, and `:13235`.

Bounded correction: use the constants directly if the decision `cost` parser accepts `constant:` tokens in the current engine. If it does not, replace the literals with file-scoped `@` cost constants and remove the dead script-constant entries. The source of truth must be singular; do not retain a duplicated “keep in sync” table.

### [P2] Compromise AI does not meet the accepted cost/time/war contract

The three compromise decisions are at `common/decisions/005_soviet_collapse_decisions.txt:218-334`. Their availability correctly requires an active family and enough resources, and their `ai_will_do` reacts to family priority and one pressure component. However:

- the two custom political-power decisions have no `ai_hint_pp_cost`, so AI budgeting does not reserve their 35/50 PP costs;
- no compromise AI block accounts for war state;
- no block accounts for mission time remaining;
- the corridor decision does not independently require a live corridor target.

Vanilla decision documentation specifically requires `ai_hint_pp_cost` for custom PP costs. Add hints from the same single tuning source used by the payment helpers. Add a war-state modifier appropriate to the family and a live-target gate to the corridor path. If the engine exposes no remaining-mission-time trigger, the accepted requirement needs an explicit supported approximation or a design amendment; it cannot be silently claimed as implemented.

## Structural invariants that pass

### 118 missions are classified exactly once

A brace-aware scan of current mission definitions and family membership returned:

| Family | Outcome types | Count |
|---|---|---:|
| Chain of Command | `command` 21, `authority` 9, `cleanup` 7 | 37 |
| Corridors and Depots | `rail` 11, `depot` 10 | 21 |
| Republic Settlement | `settlement` 10, `foreign` 22, `league` 8, `legal` 3, `old_movement` 17 | 60 |
| **Total** | | **118** |

There are 118 unique definitions, 118 unique family members, zero duplicates, zero missing members, and zero extra members. The existing IDs remain unchanged across 001-128 with the pre-existing gaps `090`, `109`, `110`, and `112-118`; no mission was renumbered.

The family triggers are at `common/scripted_triggers/005_soviet_collapse_triggers.txt:8648-8866`. Each priority helper enumerates its family once (`common/scripted_effects/005_soviet_collapse_effects.txt:26155-26309`), and the ordinary remainder still contains all 118 unique IDs (`:27784-27901`).

### Existing cap/refill scheduler is preserved

- `soviet_collapse_activate_priority_operational_objectives` (`common/scripted_effects/005_soviet_collapse_effects.txt:26311-26354`) computes one top family, orders the other two by score, and calls each family helper once.
- Each family helper checks that no same-family mission is already active and uses a short-lived selection flag, so it adds at most one family mission before the ordinary remainder fills spare slots.
- `soviet_collapse_activate_opening_objectives` still owns counting, cap calculation, surplus pruning, priority prefill, and the 118-mission remainder (`:27707-27902`).
- `soviet_collapse_queue_objective_refill` and `soviet_collapse_process_objective_refill` reuse hidden event `chaosx.nr5.128` and the existing monthly cap (`:27635-27704`; `events/005_soviet_collapse.txt:141-160`).
- No second release scheduler, second mission board, or new recurring all-country on-action was introduced.

### Compromise resolves exactly one active mission and does not double-count

The three resolvers are at:

- Chain: `common/scripted_effects/005_soviet_collapse_effects.txt:26377-26755`;
- Corridors: `:26756-26974`;
- Settlement: `:26975-27582`.

The scan proved 37/37, 21/21, and 60/60 family members respectively. Each candidate branch checks a family guard flag, marks the existing mission done, calls `remove_mission`, applies one compromise helper, and sets the guard. Only a successful branch queues the existing refill; the guard is cleared at the end. Vanilla documents that `remove_mission` runs neither complete nor timeout effects, so the removed mission cannot add its ordinary success/failure effect.

None of the three compromise outcome helpers calls `soviet_collapse_register_monthly_threat_success` or `soviet_collapse_register_monthly_threat_failure`. Ordinary complete/timeout wrappers continue to register exactly one result. The decision has no ordinary `cost`, and the hidden payment helper runs once, so there is no double charge.

Configured compromise costs and gates are coherent:

- Chain: 15 command power, gate 14.99;
- Corridor: 35 political power, gate 34.99;
- Settlement: 50 political power, gate 49.99.

At the raw total-threat formula (`(R + D + F + L + M + 75 - A - O) * 0.25`), the compromise deltas are distinguishable and directionally coherent:

| Compromise | Component-sum change before multiplier | Approximate raw threat change | Assessment |
|---|---:|---:|---|
| Chain: A +1, O +1, R +2 | 0 | 0 | Stabilises command while conceding equal breakaway momentum. |
| Corridor: A -2, D -2, F +1, L +2 | +3 | +0.75 | Repairs the depot problem but yields political/foreign/League pressure. |
| Settlement: A -2, R -2, F +1, L +2 | +3 | +0.75 | Relieves breakaway momentum but yields central and external leverage. |

These are materially weaker than the corresponding failures and do not masquerade as decisive successes. Player-facing compromise tooltips and costs match the constants.

### Release cause does not bypass release gates

The cause identifiers are confined to recording, setup, localisation, and cause-responsive AI. No cause flag or value appears in progressive release eligibility, release timing, release candidate selection, MTTH, or a new scheduler. The existing staged/pressure gates therefore remain authoritative.

Cause-specific setup/force behavior is present:

- command: local authority pressure, one field unit, next Chain priority;
- corridor: depot control, one field unit, next Corridor priority;
- negotiated: institution strength/resilience, next Settlement priority;
- foreign/League: liaison, patronage risk, League support, next Settlement priority.

The four release-cause AI strategy blocks at `common/ai_strategy/005_soviet_collapse.txt:734-817` use country-scope breakaway flags and the active/terminal aftermath gate. Those scopes are correct. The sponsor and neighbor defects above prevent the complete acceptance claim, not the release-gate integration.

### Scripted localisation does not dereference a dead corridor pointer

`GetSovietCollapseCorridorTargetStatus` checks `has_soviet_collapse_selected_corridor_state` before choosing `soviet_collapse_corridor_target_selected` (`common/scripted_localisation/005_soviet_collapse_scripted_localisation.txt:481-488`). Only that selected key dereferences `[?soviet_collapse_corridor_state_target.GetName]`; the absent branch does not. The display is therefore safe even while the stale pointer defect exists.

## Localisation findings

- The priority, target, release-cause, compromise-name, cost, and tooltip keys exist and are wired.
- The compromise descriptions accurately state their component changes and correctly say they record neither a success nor a failure.
- `soviet_collapse_soviet_category_desc` at `localisation/english/005_soviet_collapse_l_english.yml:92` exposes implementation mechanics: “refill office,” “reserves at most one place,” “remaining objective slots,” and recorded counter semantics. Replace this with in-world command-board language; player-facing text should describe the current crisis and available bargain, not scheduler internals.
- `soviet_collapse_breakaway_category_desc` currently says the cause changes sponsor interest and neighboring reactions. That sentence overclaims behavior until the dead sponsor state and wrong neighbor scope are corrected.

## Completion assessment

The implementation has a solid shared backbone, but it cannot be signed off under the accepted addendum. Required corrections remain in gameplay, AI, and player-facing behavior:

1. enforce live selected-state invariants and true state-bound project conditions for all 21 corridor missions;
2. clear invalid corridor pointers even when no replacement exists;
3. replace crisis thresholds that suppress the worsened family and make priorities genuinely posture-aware after option selection;
4. fix released-country scope for neighbor reactions and consume sponsor-interest state;
5. wire all three UWR/KMB hooks with the correct actor scope;
6. define and reuse the KMB superior-target trigger;
7. centralize KMB costs and complete compromise AI budgeting/war/time/target handling;
8. revise implementation-facing and currently overclaiming localisation.

**Simplifications, omissions, and blockers:** the current non-targeted corridor missions are a documented simplification but were not approved by the source addendum; sponsor and neighbor consequences are incomplete; UWR/KMB hooks are unwired; KMB treaty/concession AI contains an undefined trigger; posture-specific prioritisation and the accepted AI considerations are incomplete. Event 005 Command and Corridors therefore remains incomplete.
