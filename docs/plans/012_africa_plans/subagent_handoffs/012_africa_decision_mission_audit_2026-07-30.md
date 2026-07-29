# Event 012 Africa decision and mission audit handoff

## Scope and outcome

This read-first audit covered the Event 12 decision categories, all 213 direct decision and mission identifiers, the 102-action registry, shared action runtime, target validation, AI dispatcher, priority-member and RSA decision packages, localisation, the Charter scripted GUI, and the Event 13 natural-disaster caller contract.

The audit began read-only and then applied the parent-authorised narrow correction for the visible pathogen no-op and the shared-launch silent failure.

No models, country tags, scripted GUI rewrites, new decision systems, or fallback paths were added.

No commit was created.

## Matrix and static coverage

| Surface | Result |
| --- | --- |
| Action matrix rows | 102 of 102 parsed from `docs\specs\012_africa_specs\matrices\012_africa_decision_mission_matrix.csv`. |
| Player selectors | 102 of 102 `africa_select_<decision_key>` identifiers exist in `common\decisions\012_africa_decisions.txt`. |
| Action constants, profiles, and disposition records | 102 of 102 action keys resolve through `africa_action` constants, profile branches, and full, partial, and failure records. |
| Decision and mission identifiers | 213 direct identifiers across the three decision files, with 213 unique and zero duplicate identifiers. |
| Direct localisation | Zero missing name or description keys for the 213 identifiers. |
| Tooltip localisation | Zero missing keys across 69 custom-trigger, 6 custom-cost, and 65 custom-effect tooltip references. |
| Outcome localisation | Zero missing keys across all 306 `africa_action_result_<key>_<outcome>` keys. |
| Active timed matrix profiles | 95 non-instant profiles: 4 short, 21 medium, 56 long, and 14 epic. |
| Non-action decision packages | Priority-member has 55 direct decisions or missions, and RSA has 7. |

## Parent-authorised patch

| File | Identifier | Before | After |
| --- | --- | --- | --- |
| `common\decisions\012_africa_decisions.txt` | `africa_select_weaponise_fictional_pathogen` | The selector appeared once the high-chaos phase opened even though its required review-authorisation flag has no runtime setter. | Visibility also requires `africa_fictional_pathogen_review_authorized`, so the unavailable action is no longer offered as a usable player choice. |
| `common\scripted_effects\012_africa_action_effects.txt` | `africa_begin_quoted_action_against_target` | A changed target, route, or profile requirement could make an enabled shared launch click finish silently. | A failed final validation sends human players to `chaosx.nr12.221`; AI behaviour and the quote state stay unchanged. |
| `events\012_african_union.txt` | `chaosx.nr12.221` | No player-facing response existed for the final preflight failure. | A host-scoped notification explains that no commitment was spent and that the quotation remains available. |
| `localisation\english\012_african_union_l_english.yml` | `chaosx.nr12.221.t`, `.d`, `.a` | No text existed. | Added the title, explanation, and acknowledgement. |

The correction deliberately does not create an authorisation setter, pathogen delivery system, outbreak result, model package, or duplicate preflight trigger.

The success branch still clears the selected action and quote only after record creation.

The new failure branch leaves both intact, so the player can inspect or revise the current quotation after the notification.

## Issue list, sorted by severity

### Critical remaining matrix blocker — Action 73 is intentionally hidden but not implemented end-to-end

`weaponise_fictional_pathogen` has no setter for `africa_fictional_pathogen_review_authorized` anywhere in the repository.

Before the patch, the visible selector could reach a final validation failure because the authorisation flag was absent.

The patch removes that visible dead-end, but it does not make the action complete.

If a future feature writes the authorisation flag, the current validator in `common\scripted_effects\012_africa_action_effects.txt` only checks a disease flag and the review flag.

It does not require a selected enemy, war, delivery means, target access, or stockpile consumption.

Its full semantic branch only writes `africa_fictional_pathogen_stockpile_bounded` and `africa_fictional_pathogen_consequence_review_due`.

It does not begin the matrix-promised target outbreak, limited contamination, backfire, source registration, delivery-team cleanup, or diplomatic consequence.

The AI candidate gate has the same missing enemy and delivery checks, but cannot currently launch the action because it also requires the unset authorisation flag.

Recommended owner action: write a separate accepted design plan before adding any setter, then implement the authoritative target, delivery, full, partial, failure, and cleanup contract in the same tranche.

### High remaining constraint gap — hostile natural-disaster calls have an exact enemy but no quantitative strength scale

Actions 69 and 70 require an eligible host, a selected existing non-host enemy at war with that host, the additional reservation payment, and an uncooldowned caller.

`africa_call_hostile_natural_disaster_from_action` passes the exact selected country to Event 13 and correctly never substitutes a target.

It varies Event 13 severity categorically from severe to regional or catastrophic according to the action and covenant flags.

It never supplies `natural_disaster_call_death_scale`, `building_scale`, `warning_scale`, `recovery_scale`, or `supply_scale`.

Event 13 defaults every absent scale to `1.00`, so target size, war pressure, ecological readiness, and the additional cost tier do not quantitatively scale the impact.

Recommended owner action: extend only the existing Event 12 to Event 13 caller contract with central constants and a bounded strength formula after design approval.

### Major remaining depth gap — all 95 timed matrix actions collapse into four fixed timers

The matrix describes ranges or dynamic timing for all 95 non-instant actions.

The runtime initializes only four shared variables once: short 60, medium 120, long 240, and epic 540 days.

No action runtime effect subsequently changes those variables.

The four shared missions retain `available = { hidden_trigger = { always = no } }` and resolve at timeout through the risk-weighted outcome roll.

Eight offer-response actions can resolve early through `chaosx.nr12.210`.

The other 87 timed actions are passive timers rather than action-specific mission objectives with success and failure conditions.

Recommended owner action: plan a duration and objective layer that derives a per-record duration from existing target, pressure, readiness, access, and risk data, then gives only appropriate action kernels an active mission condition.

### Medium remaining clarity gap — final action requirements are post-click rather than preflight-visible

The two shared launch decisions expose quote, phase, cost, and state-target checks, while the complete 102-branch `africa_validate_action_specific_requirements` remains inside `africa_begin_quoted_action_against_target`.

The new event closes the silent-no-op defect without duplicating all 102 requirements into a stale proxy trigger.

Players still receive generic feedback after a failed final revalidation rather than an action-specific disabled tooltip before clicking.

Recommended owner action: add a future dynamic preflight explanation generated from the authoritative profile and validator contract rather than duplicating the condition tree.

### Medium GUI discoverability gap — the Charter window exposes 8 of 14 action-family page controls

`interface\012_africa_charter.gui` and `common\scripted_guis\012_africa_charter_scripted_gui.txt` expose tabs for protection, accession, regional congress, integration, economy, diaspora, rival bloc, and high chaos.

The normal decision list retains page selectors for the other six families, so this is not an unwired execution path.

Scramble, world order, constitutional crisis, post-unification, host opening, and regional restorations have no matching Charter-window tab.

Recommended owner action: review whether late-family decisions should remain list-only or receive a deliberately designed second UI page.

### Deferred and safe under the current task constraints — Actions 74 through 76

`awaken_stone_cohort`, `train_gorilla_heavy_infantry`, and `organise_pan_sappers` each require `africa_strange_formation_package_ready`.

That gate has no setter, and every selector is hidden by the same condition.

The three actions therefore cannot be quoted or launched by player or AI and do not create a free-unit or model fallback path.

This is compatible with the explicit no-model constraint, but it means four matrix actions are presently non-playable when Action 73 is included.

## Decision category lifecycle notes

The Charter Council is host-only and owns the quotation, selected target, selected state cursor, capacity reservation, action generation, and action-family paging state.

The fourteen action-family categories are host-gated and add their own phase, evolution, unification, constitutional, first-proof, or Congress gate where required.

The transition path is protection-first for ordinary integration work.

Actions 31 through 37 require chartered, autonomous-federal, or occupied-settlement relationship states, and Action 38 uses the stricter living-core recognition trigger with security, review, and integration gates.

The action record prevents a second action on the target, reserves capacity, tags state projects, and cleanup removes the mission, arrays, reservations, project flags, and stale action variables before applying the target cooldown.

Priority-member lifecycle is package registration, political settlement, League bargaining, overlap disposition, departure or recall, package mechanic, force reinforcement, and capped post-settlement progression.

RSA lifecycle is restricted to the civil-war coalition, post-war settlement, temporary lease, or one-time exile recovery state, with target-root guards on the two targeted decisions.

## Mission quality notes

| Mission family | Owner and category | Region and requirement | Duration | Success | Failure or cleanup | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| Shared Charter action bands | Current host, Charter Council | Active selected country or host record with matching generation and band flag | 60, 120, 240, or 540 days | Eight offer-response actions can resolve from the target response; otherwise the timeout rolls full, partial, or failure by risk | Event end or stale generation calls shared cancellation cleanup; timeout resolves then cleans | One record, active target flag, capped capacity, and target cooldown prevent a duplicate |
| Continental-peace exemption | Current host, Charter Council | Peace-exemption target with current host generation and active completion mission | 180 days | The conditions becoming ready close the exemption cleanly | Breach, event end, stale generation, or timeout closes the exemption | Target array and active mission flag bound the exemption |
| World sponsorship obligation | Current host, World Order | Installed package target with unpaid sponsorship obligation | 180 days | Fulfilment consumes PP, infantry equipment, support equipment, and convoys, then clears the obligation | Timeout defaults the obligation; cancellation clears an invalid or removed package relationship | Host-scoped target array and due flag prevent overlap |
| Priority-member withdrawal | Priority package country, Priority Member | Leaving or rival relationship with withdrawal in progress | 90 days | Timeout completes peaceful withdrawal | Cancellation restores the appropriate relationship when departure no longer applies | Withdrawal-in-progress and package flags prevent a second notice |
| RSA first proof | RSA coalition, RSA crisis | Civilian corridor security custom-tooltip condition | 360 days | The available condition completes the first-proof helper | Civil-war or coalition invalidation, or timeout, invokes the failure helper | Route completion flags make the proof one-shot |

The shared action bands are the principal mission-quality concern because they represent 95 matrix actions with only four static durations and no general action-specific objective surface.

## Cost and requirement clarity notes

The 102 selectors cost zero because they only choose a profile and refresh a quote.

The shared execution effect recomputes concrete resource costs against the exact target before it can pay or create a record.

The quote uses target factory and controlled-state scale, confidence, selected project-state count, integration burden, colonial pressure, active action load, access, war, route, and overlay factors before rounding the resource components.

The visible custom-cost string lists PP, command power, manpower, infantry equipment, support equipment, trucks, trains, convoys, fuel, civilian capacity, intelligence capacity, stability, and war support.

This is not a passive political-power store.

Priority-member actions use explicit package progress, cooldown, and maturity controls, while RSA custom costs couple PP with command power, equipment, train, support, or stability gates as appropriate.

## AI validity and route-lock notes

The 102 player selectors use zero AI weight by design.

The host-only AI controller selects from bounded rosters, evaluates the same profile and final validator, applies a policy-derived risk ceiling, and calls the same shared launch effect.

The natural-disaster candidate gate repeats the actor eligibility, war, payment, cooldown, and exact enemy target validation for AI.

The currently hidden pathogen action cannot be launched by AI because its review-authorisation requirement has no setter.

No active AI path was found that targets a dead country, bypasses the selected-enemy requirement for hostile natural disasters, crosses a closed route, bypasses the existing formable gates, or creates a free unit loop.

## Localisation and tooltip notes

All Event 12 English localisation files scanned in this audit retain UTF-8 BOM encoding.

The 213 decision or mission names and descriptions, 140 direct custom tooltip references, and 306 action result strings resolve statically.

The new `chaosx.nr12.221` strings are player-facing and describe the current action state without exposing implementation history or numeric tuning.

The post-click notification is a correction, not a replacement for a future dynamic action-specific preflight tooltip.

## Scripted GUI evidence

Read-only GUI inspection was run for `africa_charter_window` under the default scenario.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b67d4fc480ab6e663b115d046107e3768aa9dc9f7b74b8bc03d83d8792d40fdc/55becbd604120e21d101cda9236a5603b3aadebd900884b03252ec6c45df05bd/gui-inspect.3187bdef52b5bed5.json`.

The inspect result modelled 706 elements, approximated 91, ignored 135, and reported 6 missing, 54 unsupported, and 13 unresolved elements for the full workspace graph.

Its diagnostics are workspace-global, include unrelated GUI context and vanilla texture errors, and are truncated, so they are not reliable evidence of an Event 12 layout defect.

No GUI source was rewritten.

## Meaningful validation

Static matrix reconciliation confirmed all 102 selector, constant, profile, and full, partial, and failure outcome contracts.

The patch-specific review confirmed that `chaosx.nr12.221` is unique, is emitted only on a human final-validation failure, and has all three localisation keys.

The shared success branch remains the only path that clears the selected action, quote, and state cursor, which confirms the failure notification preserves the refreshed quote.

The four patch files passed `git diff --check`, touched Clausewitz files have equal opening and closing brace counts, and the modified localisation file retains UTF-8 BOM.

No HOI4 launch, campaign simulation, or GUI fidelity acceptance was performed because this audit cannot provide live consumer validation and the GUI diagnostics are global rather than Event 12-specific.

## Simplifications, omissions, and blockers

No simplification was introduced by this patch.

The accepted matrix is not fully playable because Action 73 remains authorisation-gated with no implementation path and Actions 74 through 76 remain deliberately model-gated.

The dynamic-duration and natural-disaster-strength gaps remain unimplemented by explicit parent direction for this narrow corrective tranche.

## Guidance used

Applied `hoi4-decisions-missions`, `chaos-redux-events`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents`.

