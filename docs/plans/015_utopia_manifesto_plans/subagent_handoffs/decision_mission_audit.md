# Event 15 Decision and Mission Audit

## Verdict

**FAIL — the Event 15 decision/mission surface is not completion-ready.**

The required inventory exists and the patched phase, icon, cost, and doctrine work is present. The failure is caused by player-visible missing localisation and several functional lifecycle gaps in Necessary Ground, stewardship, league membership, and disable-safe cleanup. These are accepted-spec blockers, not optional polish.

Audit snapshot: 2026-07-14 after the phase-family, tier-affordability, doctrine-gating, and explicit-icon patches. The primary decision source audited at SHA-256 `A1525068790D31225C5A3D86906D156A60A4565E6D1FCF5F0F49D82FB9DA2647`.

## Inventory and structural result

| Category | Decisions | Missions |
|---|---:|---:|
| Commonwealth Ledger | 26 | 10 |
| Districts | 6 | 3 |
| Island | 11 | 2 |
| Necessary Ground | 16 | 3 |
| Stewardship | 11 | 4 |
| League | 10 | 4 |
| Defense | 5 | 4 |
| Governance | 8 | 1 |
| Formation | 5 | 1 |
| **Total** | **98** | **32** |

The required exact counts therefore pass.

Structural coverage also passes:

- 98/98 decisions have `complete_effect` and `ai_will_do`.
- 32/32 missions have `activation`, variable-backed `days_mission_timeout`, `timeout_effect`, and `cancel_effect`.
- 77 decisions have material/custom affordability checks, and all 77 call the prepared payment helper. Ninety-one decisions charge political power; the seven unpriced actions are six calling selectors and the clear-target action.
- 130/130 decisions and missions have explicit icons. All nine categories have explicit icons. The 54 unique referenced sprite handles resolve in `interface/015_utopia_manifesto.gfx`, and every referenced texture exists.

## Verified patched items

These requested fixes are present, but they do not overturn the blockers below.

1. **Phase-family gating is implemented.** The monotonic phase helper is at `common/scripted_effects/015_utopia_manifesto_effects.txt:713`; category gates are in `common/decisions/categories/015_utopia_manifesto_categories.txt:17-117`; focus rewards advance the phase from foundations through mature play.
2. **Tier-specific growth affordability is implemented.** Foundation, network, and capstone military/institutional triggers are defined at `common/scripted_triggers/015_utopia_manifesto_triggers.txt:967-1091`, and every paid-growth focus now uses its matching tier trigger before applying its matching tier input.
3. **Ultimatum and enforcement are doctrine-gated.** Both require `utopia_manifesto_necessary_victory_doctrine` at `common/decisions/015_utopia_manifesto_decisions.txt:2286` and `:2329`. The ultimatum additionally respects strict authorization and the coercive-tools block; enforcement respects strict authorization.
4. **The premature league-initialization call was removed from focuses.** `utopia_manifesto_initialize_league` is now called only by `decision_utopia_initialize_league` at `common/decisions/015_utopia_manifesto_decisions.txt:2957-2984`.

## Ordered blockers

### 1. Player-facing decision localisation is absent

This is an immediate completion blocker.

- 0/130 decision and mission title keys are defined in English localisation.
- 0/130 decision and mission description keys are defined.
- Only the Ledger category is localised; the other 8/9 category titles and descriptions are absent.
- All 76 unique `custom_cost_text` bases are absent, including their blocked and tooltip forms.
- All 124 unique decision/mission `custom_effect_tooltip` keys are absent.

The definitions are not present in any file under `localisation/english/`; the current `localisation/english/015_utopia_manifesto_l_english.yml` contains the Ledger GUI and event-system text, not this decision surface. The result would expose raw keys or blank cost/effect text for essentially the entire system.

### 2. Necessary Ground does not implement the accepted case model safely

The route names exist, but the case data and target selection do not represent the six accepted case families or a target that actually solves the declared need.

- Every drafted case is hard-set to the provisioning calling family at `common/decisions/015_utopia_manifesto_decisions.txt:1896`. No other code assigns a Necessary Ground case family. Port access, corridor, resource, settlement, island/refuge, and reconstruction cases are therefore not implemented as distinct cases.
- Country selection is restricted to `target_array = neighbors` (`:1778` and throughout the family). Target validity at `common/scripted_triggers/015_utopia_manifesto_triggers.txt:625-634` checks only existence/normal-country safety. It does not check the declared deficit, reachability, port/resource/corridor relevance, strength, league conflict, or route compatibility.
- State selection accepts any non-ROOT-controlled, non-ROOT-core state controlled by the selected country (`common/scripted_triggers/015_utopia_manifesto_triggers.txt:643-649`). It does not require target ownership and does not test coast, resources, adjacency, supply connection, settlement suitability, reconstruction damage, or proportionality. An occupied third-party state can qualify.
- The peaceful decisions exist—purchase, long supply, lease, joint administration, and association—but acceptance only sets founder-side case/stewardship flags. No treaty, access, lease, state status, autonomy relationship, target modifier, or other target-specific gameplay relationship is created.
- Enforcement creates the one state wargoal at `common/decisions/015_utopia_manifesto_decisions.txt:2351-2359`, but there is no matching removal/expiry cleanup when the case is renounced, the need disappears, the target disappears, or stewardship ends.
- `utopia_manifesto_clear_active_need_case` (`common/scripted_effects/015_utopia_manifesto_effects.txt:804-826`) clears the arrays and numeric case record but not `utopia_manifesto_case_response_active`, offer flags, settlement accepted/refused, counteroffer, ultimatum, enforcement, or target-response flags. Those flags can contaminate the next case. In particular, a stale accepted/refused flag can immediately resolve a later response mission, while a stale ultimatum flag can permanently hide later ultimata.
- Case validity (`common/scripted_triggers/015_utopia_manifesto_triggers.txt:651-664`) does not revalidate the saved state, its controller/owner, the selected-country id, or continuing Need. `on_annex` and `on_state_control_changed` contain no case cleanup. The accepted target-disappearance scenario therefore fails.
- Need resolution provides a manual renunciation option, but there is no complete renounce/convert/continue choice, no continued-case political cost, and no automatic invalid-case notification. AI case closure is only a weight on the manual decision.

Required correction: implement distinct case-family selection and family-specific target/state relevance; revalidate the exact saved country and state; clear all case-local flags at case start and closure; close or convert cases on annex/control/Need invalidation; and remove case-generated claims or wargoals when their legal basis ends.

### 3. Disable-safe and target-disappearance cleanup is incomplete

The full cleanup helper does not safely terminate the decision system.

- The 32 missions use 32 country-flag activation conditions. Of those activation flags, the `utopia_manifesto_clear_all_runtime_state` call chain explicitly clears only `utopia_manifesto_need_case_active` and `utopia_manifesto_calling_sustainment_active`; 30 mission activation flags are left set.
- There is no shared removal pass for active missions or targeted missions. The only `remove_mission` in the decision helpers is the normal constitutional-correction resolution at `common/scripted_effects/015_utopia_manifesto_decision_effects.txt:1076`.
- Missions that later cancel because the Ledger disappeared can run failure effects after the Ledger variables were cleared, recreating flags and deltas after cleanup. Missions without a Ledger-based cancel trigger can remain stranded.
- `utopia_manifesto_enter_disable_safe_state` exists at `common/scripted_effects/015_utopia_manifesto_effects.txt:2131`, but no gameplay file calls it. The terminal event path calls the weaker `utopia_manifesto_clear_all_runtime_state` directly at `events/015_utopia_manifesto.txt:3456`.
- `utopia_manifesto_clear_league_runtime` does not clear root pending/mission flags such as technical mission, reserve compact, invitation, or legitimacy; it also cannot clear target-side technical-host and reserve-invite flags because those targets are not all retained in cleanup arrays.
- Resolved stewardship normally clears the active case but does not itself clear the selected country target. Some individual decisions do so afterward, but the core helper is not lifecycle-safe if invoked by an event or external cleanup.

Required correction: create one idempotent mission/target cleanup effect that removes every active normal and targeted mission before clearing its flags/arrays; invoke it from rejection, terminal disable, annex/target invalidation, route supersession, and stewardship/league closure; then make the terminal path call the actual disable-safe wrapper.

### 4. Stewardship and Assigned Colony are not target-specific territorial systems

The named decision sequence exists—provision, transport restoration, charter, charter period, vote, autonomy/return, long integration, revolt, and Assigned Colony—but its outcomes are founder flags and national idea stages rather than state/country status.

- A peaceful settlement starts stewardship while the target still owns and controls the selected state. No possession, administration, lease, access, autonomy, associate, or stewardship relation is created.
- `utopia_manifesto_integrate_stewardship` at `common/scripted_effects/015_utopia_manifesto_effects.txt:1125-1137` sets an authorization flag, records a completion, and clears the case. It does not integrate a state or country. The status-vote “integration” option can call this immediately, bypassing the advertised long integration mission.
- No Event 15 decision/event/focus effect grants or manages state ownership, autonomy, associate status, claims, or cores. The only territorial effect in the audited surface is the enforcement wargoal. Instant core spam is absent because real integration is absent, not because the integration ladder is complete.
- `utopia_manifesto_assigned_colony_active` is set at `common/decisions/015_utopia_manifesto_decisions.txt:2681` and is never cleared anywhere. It permanently blocks subsequent colony administration after the first use.
- `utopia_manifesto_assign_colonial_administration` at `common/scripted_effects/015_utopia_manifesto_country_effects.txt:343-346` only swaps the founder's national stewardship idea to a failure stage. It does not identify the colony, impose target/state obligations, create supply/garrison burden, or define exit/status review.
- Revolt handling places a flag on the former target, clears the case pointer, and exposes a cleanup decision only through `target_array = neighbors` at `common/decisions/015_utopia_manifesto_decisions.txt:2921-2954`. If that country ceases to be a neighbor or disappears, the revolt flag is stranded and no cleanup array can reach it.

Required correction: retain a target/state pointer for the entire stewardship lifecycle; implement explicit temporary administration/associate/autonomy/return/integration outcomes; make long integration the gate for permanent status; tie Assigned Colony benefits and burdens to the exact target; and clear active colony/revolt state on every terminal outcome.

### 5. League rules and response resolution are incomplete

- Candidate validity at `common/scripted_triggers/015_utopia_manifesto_triggers.txt:708-718` does not exclude majors, subjects, existing faction members, active hostile Need targets, poor relations, distant/unreachable countries, or candidates unwilling to accept autonomy rules. A player can invite a major as an ordinary member despite the accepted rule.
- The focus eligibility helper scans `any_country` (`common/scripted_triggers/015_utopia_manifesto_triggers.txt:527-530`), while every actionable league target uses `target_array = neighbors` (for example `common/decisions/015_utopia_manifesto_decisions.txt:3200`). A remote qualifying country can unlock the focus while leaving no actionable candidate.
- Observer and reserve responses do not resolve correctly. Event 212 handles observer/reserve at `events/015_utopia_manifesto.txt:2896-2908`, but the invitation mission completes only for member/refused targets (`common/decisions/015_utopia_manifesto_decisions.txt:3249-3254`). Observer status therefore times out as a refusal. Reserve contribution is recorded only if the target is already a league member (`common/scripted_effects/015_utopia_manifesto_effects.txt:1345-1356`), so a nonmember who accepts a reserve compact is not marked as a contributor and that mission also times out as refusal.
- Initialization is no longer premature, but it remains destructive. `utopia_manifesto_initialize_league` first calls `utopia_manifesto_clear_league_runtime` (`common/scripted_effects/015_utopia_manifesto_effects.txt:1178-1190`), and that cleanup clears `utopia_manifesto_recognized_external_partners` at `:1426`. Founding the league can erase the pre-existing associate network it is supposed to formalize.
- No Event 15 file creates a faction or adds members to one. There is no implementation of the accepted formal-defense transition, minimum-member/shared-mission/threat vote, or route-specific league leadership model.
- The “one league objective” cap is not shared. A technical mission, reserve answer, invitation answer, and legitimacy mission can overlap because each uses only its own active/pending flag.

Required correction: implement the full candidate gate and consistent target pool; resolve all five response types explicitly; preserve recognized partners during initialization; add one shared league-objective cap; implement member exit/betrayal cleanup; and implement the conditional formal faction transition with route-specific governance and shared actions.

### 6. Dynamic timing and AI exist but do not meet the accepted depth

- All mission timers are variable-backed, but the shared duration helper at `common/scripted_effects/015_utopia_manifesto_decision_effects.txt:96-133` only uses war, owned-state count, stable Plenty, and trusted Concord. It does not use infrastructure despite a defined low-infrastructure threshold, nor route, calling capacity, local transport/weather, foreign cooperation, target distance, local support, or prior failures as required by the specification.
- Emergency provision and transport restoration can run simultaneously because each blocks only its own flag (`common/decisions/015_utopia_manifesto_decisions.txt:2508-2616`). There is no low global stewardship cap.
- All 98 decisions have AI blocks, but Necessary Ground AI does not calculate target relevance or comparative military safety, and league AI does not enforce the candidate rules above. Presence of `ai_will_do` is not equivalent to the accepted target and closure behavior.

Required correction: introduce family-relevant duration modifiers, shared mission slots for stewardship and league objectives, target relevance scoring, comparative-strength safety, and invalid-case closure logic.

## Required route coverage result

| Required route/system | Result |
|---|---|
| Purchase | Named decision and bilateral response exist; no purchase/treaty/state outcome. |
| Lease | Named decision and response exist; no lease/access/status outcome. |
| Settlement agreement / long supply | Named long-supply decision exists; it reuses the purchase response and creates no distinct agreement. |
| Joint administration | Named decision and response exist; no joint-administration status. |
| Association | Named decision and response exist; no target-specific associate status. |
| Ultimatum | Exists and is doctrine-gated; case-local cleanup is unsafe. |
| War | One-state wargoal exists; there is no invalidation cleanup or post-acquisition linkage. |
| Provision / transport / charter | Named projects exist; not bound to real target administration and can overlap. |
| Vote / autonomy / return | Named outcomes exist; they do not enact target/state status. |
| Long integration | Timed mission exists; status-vote integration can bypass it and completion creates no territorial status. |
| Revolt | Narrative/flag path exists; target pointer and disappearance cleanup are unsafe. |
| Assigned Colony | Named decision exists; active state never clears and no target-specific colony lifecycle exists. |
| League | Named actions and cohesion counters exist; candidate rules, two response paths, partner preservation, objective cap, and faction transition fail. |

## Correction order for the main agent

1. Repair case, stewardship, league, and cleanup lifecycles first so identifiers and outcomes are stable.
2. Implement the missing target/state relationships and conditional faction transition.
3. Add shared mission caps plus duration/AI relevance logic.
4. Write complete English decision/category/cost/effect localisation against the final behavior.
5. Re-run this audit against the complete surface; the current verdict must not be promoted to PASS before all six blocker groups are resolved.

## Simplifications, omissions, and audit risk

No fallback or gameplay simplification was introduced by this read-only audit. The implementation omissions are disclosed in the blocker list above.

The audit is static. The exact runtime scope behavior of the state-wargoal generator and same-tick bilateral response/targeted-mission ordering remains an engine-runtime risk, but the FAIL verdict does not depend on either uncertainty.

## Files changed by this audit

- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/decision_mission_audit.md`

No gameplay, localisation, asset, interface, or spreadsheet file was edited.

## Skills

- Used: `hoi4-decisions-missions`, `chaos-redux-subagents`.
- Created or updated: none.
