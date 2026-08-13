# Event 015 Utopia Manifesto Decision and Mission Completion Audit

Date: 2026-07-15  
Auditor: `chaosx_decision_mission_auditor`  
Mode: read-only audit; no gameplay, localisation, asset, or spreadsheet files were changed

## Acceptance verdict

**FAIL — Event 015 is not ready for a completion claim.**

The implemented decision and mission architecture is broad and most core lifecycles are mechanically present, but the live source still contains one P0 player-facing blocker, three P1 gameplay/integration blockers, and one P2 affordability defect. The earlier ordinary-war entry into the total-repeal aftermath has been corrected and is not a remaining finding.

| Priority | Open findings | Completion effect |
| --- | ---: | --- |
| P0 | 1 | The majority of the decision surface exposes missing names, descriptions, cost text, and outcome tooltips. |
| P1 | 3 | Prefire evolution state is not producible, foreign reactions/news are unreachable, and the calling mission cap can be bypassed. |
| P2 | 1 | Exact custom-cost stockpiles are rejected by 181 strict-greater-than checks. |
| P3 | 0 | None. |

## Findings

### P0 — Most decision and mission localisation is absent

Representative live use sites include:

- `common/decisions/015_utopia_manifesto_decisions.txt:20`, `:36`, and `:38` for the opening survey name, cost text, and outcome tooltip;
- `common/decisions/015_utopia_manifesto_decisions.txt:2310`, `:2341`, and `:2343` for drafting a Necessary Ground case;
- `common/decisions/015_utopia_manifesto_decisions.txt:4310`, `:4342`, and `:4344` for auxiliary contracts;
- `common/decisions/015_utopia_manifesto_decisions.txt:4946`, `:4962`, and `:4964` for Commonwealth proclamation; and
- `common/decisions/categories/015_utopia_manifesto_categories.txt:50`, `:60`, `:70`, `:80`, `:95`, and `:108` for six unlocalised categories.

An exact cross-check of both Event 015 decision files against all 164 localisation `.yml` files in the live repository found:

| Key surface | Distinct referenced/defined | Missing exact localisation key | Coverage missing |
| --- | ---: | ---: | ---: |
| `custom_cost_text` | 91 | **61** | 67.0% |
| `custom_effect_tooltip` | 159 | **109** | 68.6% |
| decision/mission identifiers | 160 | **112 names and 112 descriptions** | 70.0% lack both |
| decision categories | 9 | **6 names and 6 descriptions** | 66.7% lack both |

The six missing category pairs are `utopia_manifesto_necessary_ground_category`, `utopia_manifesto_stewardship_category`, `utopia_manifesto_league_category`, `utopia_manifesto_defense_category`, `utopia_manifesto_governance_category`, and `utopia_manifesto_formation_category`.

The missing cost-key set spans the opening survey and stores, callings, property, Necessary Ground, stewardship, League, defense and paid growth, constitutional correction, formation, and post-formation play. Examples include `utopia_manifesto_cost_survey_transport`, `utopia_manifesto_cost_need_case_draft`, `utopia_manifesto_cost_auxiliary_contract`, and `utopia_manifesto_cost_commonwealth_proclamation`. Evolution-consumption localisation is present; it does not cover the main decision file.

Impact: raw identifiers appear in the decision UI, the player cannot reliably see the material obligation or terminal outcome of most operations, and the accepted requirement that costs, trigger tooltips, effects, and gameplay wording remain aligned is not met.

Closure condition: define every missing identifier, `_desc`, cost-text, effect-tooltip, success/failure/partial tooltip, and category pair in UTF-8 BOM English localisation, with the displayed amounts and consequences matching the live constants and effects.

### P1 — The accepted prefire evolution path has no producer for a choice

The formal addendum requires the prefire path to set the same interpretation state and call the same setup helper as active delivery (`docs/plans/015_utopia_manifesto_plans/015_utopia_manifesto_formal_improvement_loop_addendum_2026-07-15.md:309` and `:341`).

The live prefire evaluator only records five enabled-setting flags (`common/scripted_effects/015_utopia_manifesto_effects.txt:4189-4225`). Consumption converts those flags into five `*_setting_enabled` flags and then calls the prepared-choice wrapper (`common/scripted_effects/015_utopia_manifesto_effects.txt:4228-4281`). The wrapper explicitly requires a prepared option token (`common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt:297-316` and `:431-523`).

An exact producer scan across `common/`, `events/`, and `history/` found zero setters for all five stage tokens:

- `utopia_manifesto_prefire_glosses_choice`
- `utopia_manifesto_prefire_shores_choice`
- `utopia_manifesto_prefire_cities_choice`
- `utopia_manifesto_prefire_nowhere_choice`
- `utopia_manifesto_prefire_perfect_choice`

The only five setters for generic `utopia_manifesto_prefire_evolution_choice` are inside the same wrapper at `common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt:438`, `:457`, `:476`, `:495`, and `:514`; each copies one of the five never-produced stage tokens. The file header also states that ordinary setting-enabled prefire remains staged for later delivery (`common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt:4-7`).

Impact: active choices correctly use the shared interpretation dispatcher, but an enabled prefire evolution cannot enter that dispatcher with any of its three accepted interpretations. Prefire therefore does not produce the same downstream unlock state as active delivery, and the explicit prefire API is dead code.

Closure condition: provide a real scenario/prefire producer for each accepted stage choice and consume it through `utopia_manifesto_apply_prepared_evolution_choice`; then prove all fifteen option states are idempotent and equivalent between active and prefire delivery.

### P1 — Foreign-reaction and international-news event families are unreachable

The six reacting-country events are defined at:

- `events/015_utopia_manifesto.txt:3771` — `chaosx.nr15.110`
- `events/015_utopia_manifesto.txt:3800` — `chaosx.nr15.111`
- `events/015_utopia_manifesto.txt:3829` — `chaosx.nr15.112`
- `events/015_utopia_manifesto.txt:3858` — `chaosx.nr15.113`
- `events/015_utopia_manifesto.txt:3887` — `chaosx.nr15.114`
- `events/015_utopia_manifesto.txt:3925` — `chaosx.nr15.115`

Their cooperative options are the only entries into founder-side partnership bridge `chaosx.nr15.116` (`events/015_utopia_manifesto.txt:3784`, `:3813`, `:3842`, `:3871`, `:3900`, `:3909`, `:3938`, and `:3947`). However, a repository-wide gameplay-source reference scan found no caller for `.110` through `.115`; every literal reference is inside its own definition/localisation identifiers.

The three internationally visible milestone events are likewise definition-only:

- `events/015_utopia_manifesto.txt:4444` — League/Commonwealth milestone `.160`
- `events/015_utopia_manifesto.txt:4455` — Necessary Ground war milestone `.161`
- `events/015_utopia_manifesto.txt:4466` — colony-revolt milestone `.162`

The actor-scoped incident dispatcher at `events/015_utopia_manifesto.txt:4242-4435` schedules evolutions and domestic incidents but never dispatches a foreign reaction or any of the three news events.

Impact: the accepted foreign-reaction matrix never runs, reaction opinion/partnership flags cannot be produced through this family, the founder bridge cannot receive those responses, and the three authored news moments never appear.

Closure condition: wire route-, geography-, conduct-, case-, League-, war-, and revolt-aware callers with correct reacting-country/FROM scope, one-shot guards, AI weights, and cleanup; prove `.110-.115` and `.160-.162` each have at least one reachable, non-spam path.

### P1 — The one-active-calling-mission cap is bypassable

The accepted structure calls for one active calling mission (`docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_4_decisions_and_missions.md:1277-1288`). Normal calling methods enforce this by checking `utopia_manifesto_calling_mission_active` and setting it before activating their shared mission; see `common/decisions/015_utopia_manifesto_decisions.txt:438-464`.

Two other calling missions only check the shared lock before starting and never claim it:

- calling sustainment checks the shared flag at `common/decisions/015_utopia_manifesto_decisions.txt:675-679`, then sets only `utopia_manifesto_calling_sustainment_active` at `:692-695`;
- second-trade training checks the shared flag at `common/decisions/015_utopia_manifesto_decisions.txt:722-725`, then sets only `utopia_manifesto_second_trade_active` at `:738-740`.

After either mission starts, `utopia_manifesto_calling_mission_active` remains clear, so `decision_utopia_issue_open_call` and the other normal calling methods remain available. The reverse order is blocked, making the lock dependent on click order. Second-trade training and normal calling work also share `utopia_manifesto_calling_days` (`common/decisions/015_utopia_manifesto_decisions.txt:738-749` and the normal preparation at `:456-464`), increasing the risk of cross-operation state interference.

Impact: the mission-cap acceptance rule and intended administrative scarcity can be bypassed, and multiple calling missions can overlap despite the UI/design promise of one active calling operation.

Closure condition: make all calling mission families claim and release one authoritative lock (or gate every start through one authoritative active-calling trigger), including success, failure, cancellation, total repeal, and system cleanup.

### P2 — Exact custom-cost affordability is rejected throughout the main decision file

The main decision file contains **181** custom affordability comparisons of the form `resource > constant:utopia_manifesto_decision_cost.*`. The breakdown is 156 equipment comparisons and 25 manpower/experience/command-power/stability comparisons. Representative sites include the opening survey (`common/decisions/015_utopia_manifesto_decisions.txt:33-34`), Necessary Ground purchase (`:2443-2444`), stewardship (`:3070` and `:3133-3134`), proclamation (`:4959-4960`), and post-formation charters (`:5034-5036`).

The common payment helper then subtracts exactly the prepared amount (`common/scripted_effects/015_utopia_manifesto_decision_effects.txt:14-89`). Consequently, a stockpile equal to the displayed cost is unaffordable; the player must possess at least one unit more than the amount actually consumed. The evolution-consumption affordability triggers use equality-safe `NOT = { resource < cost }` logic, so the two decision surfaces are inconsistent.

Impact: displayed cost and executable threshold differ across nearly every main operation, including the opening survey, stores, districts, island construction, Necessary Ground, stewardship, League, defense, and formation.

Closure condition: replace the strict custom-cost checks with equality-safe trigger forms while retaining the exact existing payment amounts, then re-audit every custom cost against its tooltip and payment inputs.

## Surface-by-surface acceptance review

| Surface | Status | Live evidence and disposition |
| --- | --- | --- |
| Living Ledger | Pass mechanically; P0 localisation still affects entry actions | The GUI is attached at `common/decisions/categories/015_utopia_manifesto_categories.txt:18-26`; live contribution recomputation, durable policy deltas, total rebuild, clamping, bands, and refresh are separated at `common/scripted_effects/015_utopia_manifesto_effects.txt:427`, `:516`, `:546`, `:554`, `:589`, and `:600`. Need, Plenty, Concord, and Choice/Assignment are the only meter family; no contradiction meter was found. |
| Calls, callings, and stores | **Fail due to P0/P1/P2** | Capital store, seasonal reserve, two-year reserve, six calling families/methods, emergency levy, sustainment, second trade, and short-day suspension exist. Their paid/dynamic lifecycles are present, but most text is missing, exact stockpiles fail, and sustainment/second trade bypass the calling lock. |
| Districts and Penal Works | Pass mechanically; P0/P2 remain | State survey, four suitability-bound roles, one global district project, charter follow-up, and route outcomes are present at `common/decisions/015_utopia_manifesto_decisions.txt:1073-1538`. Penal Works is a paid Closed Island project at `:1394-1461`; verified state civilian deaths use the shared death transaction at `common/scripted_effects/015_utopia_manifesto_decision_effects.txt:882-948`, and terminal/failure cleanup is present at `:950-981` and `:1217-1299`. |
| Island variants | Pass mechanically; P0/P2 remain | Existing island capital, coastal refuge, inland island, leased island, archipelago, staged site/harbor/terminal/provision/fortification construction, lease renewal/return, and scope cleanup are implemented at `common/decisions/015_utopia_manifesto_decisions.txt:1541-2205` and `common/scripted_effects/015_utopia_manifesto_decision_effects.txt:1582-1921`. |
| Defense and paid growth | Pass mechanically; P0/P2 remain | Store guard, citizen watch, engineer companies, auxiliary contracts/demobilisation, and route formations are implemented at `common/decisions/015_utopia_manifesto_decisions.txt:4145-4467`. Unit creation is confined to the paid growth executor (`common/scripted_effects/015_utopia_manifesto_effects.txt:4773-4862`), which charges dynamic manpower, infantry equipment, support equipment, and army experience before creation. |
| League and Commonwealth | **Fail due to P0/P1/P2** | League founding, aid, technical mission, compact, invitations, legitimacy, reconstruction, defense council, sponsorship, and expulsion exist at `common/decisions/015_utopia_manifesto_decisions.txt:3607-4144`; one League-objective lock is used for its missions. The authored foreign reaction/news layer is unreachable. |
| Necessary Ground | Pass mechanically; P0/P2 remain | Domestic review, target and state selection, one active case, integrity, six peaceful offers, response waiting, counteroffer/revision, ultimatum, enforcement, war tracking, lease/joint-administration conversion, renunciation, expiry, invalidation, and wargoal cleanup exist at `common/decisions/015_utopia_manifesto_decisions.txt:2207-3095` and `common/scripted_effects/015_utopia_manifesto_effects.txt:1205-3056`. No core or permanent claim effect was found. |
| Stewardship, integration, revolt, Assigned Colony | Pass mechanically; P0/P2 remain | Provision, route restoration, local charter, Assigned Administration, charter period, status vote, autonomy, return, long integration, and revolt cleanup exist at `common/decisions/015_utopia_manifesto_decisions.txt:3096-3606`. Assigned Colony state application, return, integration, revolt scope capture, revolt cleanup, mission removal, and runtime teardown are present at `common/scripted_effects/015_utopia_manifesto_effects.txt:3273-3497`. Long integration transfers the selected state but does not create a core. |
| Constitutional crisis, correction, formation, post-formation | Pass mechanically; P0/P2 remain | Constitutional correction, five governance corrections, corrected tables, appeals, formation proof, paid proclamation, and three post-formation renewals exist at `common/decisions/015_utopia_manifesto_decisions.txt:4468-5053`. Correction/repeal/formation-proof exclusions prevent those terminal objectives from overlapping. |
| Fifteen evolution consumers | **Fail due to prefire P1** | Active delivery has fifteen route/state-aware, paid decisions and one shared bounded mission at `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt:14-465`. Cost dispatch is at `common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt:541-604`, immediate system effects at `:665-768`, timeout consequences at `:791-945`, and cleanup at `:947-1005`. Active options therefore have visible paid consequences in existing systems, but the accepted equivalent prefire state is not producible. |
| Total repeal and aftermath | Pass after live correction | The repeal mission begins the aftermath only through `common/decisions/015_utopia_manifesto_decisions.txt:4584-4603` into `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt:10-14`. `common/on_actions/015_utopia_manifesto_on_actions.txt:19-29` now treats ordinary war only as a Ledger refresh; no ordinary-war path to `chaosx.nr15.120` remains. Snapshot, League succession, colony/assigned-stewardship disposition, route choices, and final teardown are present in `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt:40-251`. |
| Prohibited shortcuts and hidden rewards | Pass except exact-affordability P2 | No Event 015 `add_core_of`, `remove_core_of`, `add_claim_by`, or `remove_claim_by` was found. All unit creation is in the paid growth helper. Of 120 decisions, only seven lack both a political-power cost and a custom-cost trigger: six calling-family selectors and `decision_utopia_clear_necessary_ground_target`; none grants material, territory, units, equipment, or a generic reward. Equipment additions outside payment helpers are explicit cross-country aid/contract transfers after source payment, not generic dumps. |

## Meaningful validation performed

1. Parsed both Event 015 decision files into **120 decisions and 40 missions**.
2. Verified all **40/40 missions** have a variable-backed `days_mission_timeout`, `activation`, `available`, `cancel_trigger`, `cancel_effect`, and `timeout_effect`.
3. Verified all **40/40 missions** have at least one explicit `activate_mission` or `activate_targeted_decision` caller.
4. Traced the explicit one-at-a-time locks for calling, district, Necessary Ground, stewardship/integration, League, evolution-policy, constitutional, repeal, and formation-proof operations; this exposed the asymmetric calling lock above.
5. Cross-checked **91** cost keys, **159** effect-tooltip keys, **160** decision/mission identifiers, and **9** categories against all live localisation files; exact missing counts are reported in P0.
6. Counted and classified all **181** strict custom-cost comparisons, then traced them to the exact-subtraction helper.
7. Scanned all gameplay source for producers of the six prepared prefire tokens and callers of events `.110-.115` and `.160-.162`; the missing producers/callers are reported above.
8. Traced state ownership, wargoal, core/claim, equipment, manpower, and unit-creation effects to distinguish paid transfers and terminal settlement from prohibited free grants.
9. Re-audited the patched `on_war` path and confirmed `chaosx.nr15.120` is now reached only by the deliberate total-repeal helper.

## Files and references inspected

### Required repository guidance and skills

- `AGENTS.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`

### Accepted Event 015 design sources

- `docs/specs/015_utopia_manifesto_specs/README.md`
- `docs/specs/015_utopia_manifesto_specs/PACKAGE_MANIFEST.md`
- all eight files under `docs/specs/015_utopia_manifesto_specs/specs/`
- `docs/specs/015_utopia_manifesto_specs/matrices/decision_mission_matrix.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/target_eligibility_matrix.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/ai_strategy_matrix.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/idea_lifecycle_matrix.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/completion_coverage_matrix.md`
- `docs/specs/015_utopia_manifesto_specs/focus_graphs/mechanic_state_flow.md`
- `docs/plans/015_utopia_manifesto_plans/015_utopia_manifesto_formal_improvement_loop_addendum_2026-07-15.md`

### Live Event 015 source

- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt`
- `common/decisions/categories/015_utopia_manifesto_categories.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_decision_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_country_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_identity_effects.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `common/scripted_triggers/015_utopia_manifesto_evolution_consumption_triggers.txt`
- `common/scripted_triggers/015_utopia_manifesto_evolution_delivery_triggers.txt`
- `common/script_constants/015_utopia_manifesto_constants.txt`
- `common/script_constants/015_utopia_manifesto_decision_constants.txt`
- `common/script_constants/015_utopia_manifesto_evolution_consumption_constants.txt`
- `common/national_focus/015_utopia_manifesto_focus_tree.txt`
- `common/on_actions/015_utopia_manifesto_on_actions.txt`
- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`
- `interface/015_utopia_manifesto_ledger.gui`
- `events/015_utopia_manifesto.txt`
- all Event 015 English localisation files and a repository-wide localisation-key scan

### Required offline wiki and vanilla references

- Offline wiki: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface Modding, and Scripted GUI Modding.
- Vanilla documentation: `common/decisions/_documentation.md`, `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, `documentation/effects_documentation.md`, and `documentation/triggers_documentation.md`.
- Vanilla precedents: `common/decisions/CHI_decisions.txt`, `common/decisions/AST.txt`, and `common/decisions/WTT_border_conflicts.txt`.

## Simplifications, omissions, fallbacks, blockers, and risks

- No fallback was assumed or approved in this audit.
- No gameplay patch was made because the delegated task was audit-only.
- The five findings above are unresolved live-source omissions/defects, not optional polish.
- The accepted completion claim remains blocked until the P0 and P1 findings are closed and the P2 affordability mismatch is corrected or explicitly rejected through a source-of-truth spec change.
- No skill was created or updated. Skills used: `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`.
