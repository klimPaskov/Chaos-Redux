# Event 015 Necessary Ground Completion Final Re-audit

Date: 2026-07-15  
Agent role: `chaosx_decision_mission_auditor`  
Mode: focused read-only source audit; this report is the only auditor-authored change  
Verdict: **PASS**

## Result

The Necessary Ground target-disappearance repair passes the focused final re-audit. There are no open P0, P1, P2, or P3 findings in the audited repair surface.

This report supersedes the **FAIL** verdict in `decision_mission_completion_reaudit_2026_07_15.md`. The former target-disappearance blocker and the adjacent multiplayer state-link blocker are closed in the current source snapshot.

The accepted invariant is now maintained: a Necessary Ground country or state target cannot disappear, change controller, be replaced, or be cleaned by one founder while leaving another exact founder with a stale case, a cross-selected enforcement state, or an acquired state outside stewardship or an explicit terminal disposition.

## Repair proof

### Last-state transfer and defensive validation

- `utopia_manifesto_case_target_can_survive_state_transfer` and its exact active-target wrapper require the target to own more than one state before purchase, ultimatum, or unilateral enforcement (`common/scripted_triggers/015_utopia_manifesto_triggers.txt:1767-1777`).
- The full case-validity contract repeats that gate for transfer methods until the selected state is already in resolved founder possession, while stewardship is stage-exempt (`common/scripted_triggers/015_utopia_manifesto_triggers.txt:1898-1921`).
- Purchase, ultimatum, and enforcement expose the same visible explanation at `common/decisions/015_utopia_manifesto_decisions.txt:2461-2467`, `:2923-2928`, and `:2973-2978`. The localisation states: “The selected country must retain at least one owned state after the proposed transfer.” (`localisation/english/015_utopia_manifesto_decision_completion_l_english.yml:573`).
- Bilateral acceptance re-enters the full case-validity contract. If a purchase or accepted ultimatum has become a last-state transfer after the offer was sent, it records `utopia_manifesto_case_transfer_cancelled_to_preserve_target` and invalidates without transferring the state (`common/scripted_effects/015_utopia_manifesto_effects.txt:2903-2957`).
- Enforcement repeats the exact active-target survival gate in the execution helper before creating its wargoal (`common/scripted_effects/015_utopia_manifesto_effects.txt:2987-3033`). The post-peace resolver has an invalid-target terminal before its normal stewardship/failure branches (`:3065-3105`).

### Exact country and state ownership

- Active countries retain a target-side reverse founder array. Register, unregister, last-founder marker clearing, and founder-side link clearing are centralized at `common/scripted_effects/015_utopia_manifesto_effects.txt:1461-1504`.
- Active states now have the analogous state-side `utopia_manifesto_case_state_founders` array. Registration is duplicate-safe; unregistration clears `utopia_manifesto_active_case_state` only when the final founder leaves; state replacement and terminal case cleanup use the centralized link helper (`common/scripted_effects/015_utopia_manifesto_effects.txt:1507-1561` and `:1809-1822`).
- `utopia_manifesto_is_exact_active_case_target_for_root` requires the shared marker, reverse founder membership, and exact stored target ID. State selection, target validity, state owner/controller bounds, enforcement-war recognition, and restitution use this founder-specific contract (`common/scripted_triggers/015_utopia_manifesto_triggers.txt:1735-1764`, `:1817-1859`; `common/on_actions/015_utopia_manifesto_on_actions.txt:42-55`; `common/scripted_effects/015_utopia_manifesto_effects.txt:3052-3062`, `:3393-3447`).
- Active-state and resolved-possession triggers likewise require the shared marker, exact founder membership, and stored state ID (`common/scripted_triggers/015_utopia_manifesto_triggers.txt:1788-1815`, `:1817-1859`).
- The wargoal effect meta-injects the exact stored state ID as its generator (`common/scripted_effects/015_utopia_manifesto_effects.txt:3005-3027`). The wargoal type additionally requires the state marker, the goal-owning `ROOT` in the state reverse array, and ownership by original target `PREV` (`common/wargoals/015_utopia_manifesto_wargoals.txt:21-28`). This isolates same-target multiplayer wargoals even when founders selected different states.

### One-shot country and state callbacks

- `on_annex` saves annexer and annexed-target regular event targets, snapshots the annexed target's reverse founder array before any mutation, and sends hidden `.163` to each exact founder (`common/on_actions/015_utopia_manifesto_on_actions.txt:114-135`; `events/015_utopia_manifesto.txt:5002-5013`).
- `.163` runs with that founder as event `ROOT`. Its method-aware handler adopts the annexer during stewardship, records the explicit founder-extinction disposition when the founder is the annexer, or invalidates a pre-stewardship case (`common/scripted_effects/015_utopia_manifesto_effects.txt:3146-3223`).
- An annexed Event 015 founder receives immediate hidden `.164`, so cleanup runs with the exact founder as `ROOT` and unregisters its country and state links through the normal disable-safe chain (`common/on_actions/015_utopia_manifesto_on_actions.txt:185-188`; `events/015_utopia_manifesto.txt:5015-5026`; `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt:53-75`).
- `on_state_control_changed` snapshots only the changed state's reverse founders, saves that exact state as a regular event target, and schedules hidden `.165` for each exact founder one hour later (`common/on_actions/015_utopia_manifesto_on_actions.txt:219-238`; `events/015_utopia_manifesto.txt:5028-5060`). The delay is an ordering barrier: full annexation reaches `.163` adoption/closure before state validation, while ordinary third-party control changes are still handled by a bounded one-shot callback. Founder membership, exact state ID, live target, and active-case checks make stale delayed deliveries no-ops.

The event bridge semantics match the offline wiki and vanilla references. `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:26-32` documents that effect-fired events reset `ROOT` to the recipient, carry regular event targets, and may be fired immediately for a country that no longer exists. Lines 168-192 document immediate and delayed effect firing. `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:1282-1287` documents regular arrays as persistent and scope-local. Vanilla `common/wargoals/00_invasion.txt:79-88` documents `ROOT` as the goal owner and `PREV` as the original target inside `take_states`; vanilla event files use numeric state IDs in `generator = { ... }`.

## Scenario matrix

| Scenario | Result | Disposition and evidence |
|---|---|---|
| One-state purchase | PASS | The visible decision gate blocks the offer. If the target becomes one-state after the offer, defensive acceptance invalidates without transfer. |
| One-state ultimatum | PASS | The visible ultimatum gate blocks issue; later acceptance rechecks the same survival contract. |
| One-state enforcement | PASS | Both the decision and execution helper require target survival before the exact-state wargoal is created. |
| Two-state transfer into stewardship | PASS | The target retains one state; settlement acceptance precedes transfer; resolved possession and stage-aware validity keep the acquired state live; stewardship starts. |
| Third-party annexation before stewardship | PASS | `.163` reaches the exact founder and invalidates/cleans the case without voluntary-renunciation evidence. Queued `.165` deliveries no-op. |
| Third-party annexation during enforcement | PASS | `.163` removes the founder's exact case and wargoal; the invalid-target peace branch remains a terminal guard. |
| Third-party annexation during stewardship | PASS | `.163` replaces the target ID and both one-entry target arrays with the annexer, registers the founder on the successor, applies the configured integrity/support losses, and validates the settled successor. |
| Annexation by the case founder | PASS | The founder-extinction branch records coercive conduct and unresolved stewardship failure, then closes the case explicitly. It does not masquerade as renunciation. |
| Annexation of the founder | PASS | Immediate `.164` runs in the annexed founder scope and centrally unregisters all country/state links. A later delayed `.165` is inert. |
| Multiple founders, same target and same state | PASS | Both reverse arrays are mutation-safe. One founder's cleanup removes only that founder; shared markers clear only after the final founder. |
| Multiple founders, same target and different states | PASS | Each state records its exact founder. Meta-generated state IDs plus `ROOT` membership prevent one founder's wargoal from selecting the other's state. |
| Third-party state control without annexation | PASS | The changed state notifies every recorded founder through `.165`; exact founder validation closes an invalid case even when neither new nor old controller is an Event 015 actor. |
| Successor target reachability | PASS | Adoption rewrites `utopia_manifesto_case_target_id`, `utopia_manifesto_selected_country_id`, `utopia_manifesto_active_case_targets`, and `utopia_manifesto_selected_country_targets` together (`common/scripted_effects/015_utopia_manifesto_effects.txt:3146-3158`). |
| Cleanup and AI/player parity | PASS | Player and AI decisions use the same gates/effects. All exceptional cleanup is event-driven and founder-specific; no player-only or AI-only lifecycle path was found. |
| Localisation and recurring-scan constraint | PASS | The survival tooltip is defined and used on all three transfer routes. No daily, weekly, monthly, or equivalent recurring repair scan was introduced. |

## Focused source checks

- The current Event 015 file contains **99** top-level event definitions and **99** Event 015 IDs, with no duplicate ID. `.163`, `.164`, and `.165` are present and triggered only.
- Direct writes to `utopia_manifesto_active_case_state` are confined to its register/unregister helpers. Direct writes to `utopia_manifesto_active_case_target` are confined to its register/unregister helpers plus the post-snapshot annexed-target terminal clear.
- The state callback uses only the changed state's reverse array. The country callback uses only the annexed target's reverse array. Neither callback iterates all countries.

## Final audited SHA-256 snapshot

| File | SHA-256 |
|---|---|
| `common/decisions/015_utopia_manifesto_decisions.txt` | `4678a6afe7208c16951305c711d41f6d74b2eec05c23f4c5fa28b5aa2e4a8b6f` |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | `4ef6c2adce52e46ef3adabf2bdf8a604b20f3cfc05452d69432358267c75ad30` |
| `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt` | `0e027f7512bdf07dd04123ef97802235cd18db5d6f46e6de909d8376df7cce4d` |
| `common/scripted_triggers/015_utopia_manifesto_triggers.txt` | `b59a2fe103eb3d928014b59ecc9d4d11708266badf0fcb0a1ec050160df0573a` |
| `common/on_actions/015_utopia_manifesto_on_actions.txt` | `870e11a9025c3a4f0010fb9755fa804e3df995b61de374532587203c24391be5` |
| `common/wargoals/015_utopia_manifesto_wargoals.txt` | `d81e435349f9bcc1386b98e492d67eaa87f2d029886cb07b91588401a3314543` |
| `events/015_utopia_manifesto.txt` | `b1e554aa69a4d35906f6fe24215680cad34fb21971ee621dd71ea1befeae7f7f` |
| `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml` | `dcb6d839a88b0f163d01accdc51a7e88613c3a759220fe9bbfff5c7d8a0c9dd3` |
| `common/script_constants/015_utopia_manifesto_constants.txt` | `a426f72ee144e8bbf940ffb46460777b8b69f6f2fbf8b1989c020a663cf901e1` |

## Simplifications, omissions, and blockers

- No fallback, simplification, or omitted scenario was used in this focused re-audit.
- No gameplay, localisation, asset, spreadsheet, or canonical specification file was edited by this auditor.
- No blocker remains in the audited Necessary Ground target/state disappearance repair.

## Skills used

- `chaos-redux-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-subagents`
