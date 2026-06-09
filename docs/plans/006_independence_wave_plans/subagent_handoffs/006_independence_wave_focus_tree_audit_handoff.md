# Event 006 Focus Tree Audit Handoff

## Scope

Audited the Event 006 provisional focus tree and directly related loading, helper, decision, idea, localisation, and documentation surfaces.

Files audited:

- `common/national_focus/006_independence_wave_focus.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/decisions/categories/006_independence_wave_categories.txt`
- `events/006_independence_wave.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`

Primary specs and plans used:

- `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_decisions_ai.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_coding_prompt.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_foundation_tranche_handoff.md`

## Files Changed

- `common/national_focus/006_independence_wave_focus.txt`
- `docs/events/006_independence_wave.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_independence_wave_focus_tree_audit_handoff.md`

## Patch Summary

Changed focus id:

- `independence_wave_reveal_the_formation_ledger`

Before:

- The formation ledger focus required either `independence_wave_archive_identity_clue` or `independence_wave_land_congress_clue`.
- Both clue focuses are high-chaos, old-state-memory, or local-polity gated.
- Ordinary Event 006 releases could finish `independence_wave_league_charter_draft` and still be unable to reach the existing regional compact formation route.

After:

- `independence_wave_reveal_the_formation_ledger` can now be reached through `independence_wave_league_charter_draft`, `independence_wave_archive_identity_clue`, or `independence_wave_land_congress_clue`.
- The focus was moved from `y = 13` to `y = 14` so the new league-charter prerequisite is above the reveal focus.
- `docs/events/006_independence_wave.md` now states that the formation ledger opens after the league charter, archive clue, or land-congress clue.

Localisation keys changed:

- None.

Icon ids changed:

- None.

## Route Coverage Table

| Required route or lane | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Provisional opening | `independence_wave_count_the_dossiers`, `independence_wave_provisional_council`, `independence_wave_barracks_count`, `independence_wave_emergency_budget`, `independence_wave_recognition_desk` | Partial | Functional compact trunk with legitimacy, budget, militia, and recognition helpers. Still not a full host anger or loyalist-risk ledger. |
| Civic legitimacy | `independence_wave_observer_charter`, `independence_wave_observer_protected_elections`, `independence_wave_file_for_arbitration`, `independence_wave_civic_republic` | Partial | Real route lock and civic payoff exist. Missing observer variants, richer recognition, minority/municipality content, and advisor identity. |
| Military survival | `independence_wave_officer_mandate`, `independence_wave_secure_the_capital_guard`, `independence_wave_military_supply_board`, `independence_wave_emergency_state` | Partial | Real route lock and military payoff exist. Missing defensive belt, officer staff depth, loyalist conflict variant, and crisis recovery. |
| Revolutionary committee | None | Missing | Spec requires a radical route with workshop militias, police purges, volunteers, and commune supply. |
| National directorate | `independence_wave_national_directory`, `independence_wave_border_office`, `independence_wave_dossier_war_plans`, `independence_wave_claimant_state` | Partial | Route lock and claim ambition exist. Missing actual border commission decisions, claims, ultimatums, war goals, and postwar handling. |
| Patron cabinet | `independence_wave_sponsored_cabinet`, `independence_wave_invite_military_mission`, `independence_wave_balance_the_sponsors`, `independence_wave_write_the_cabinet_contract` | Partial | Patron leverage is tracked. Missing dependency/autonomy danger resolution, rival patron variant, and major-power hooks. |
| Anti-patron struggle | `independence_wave_balance_the_sponsors` only | Simplified | Balancing sponsors reduces leverage, but there is no dedicated expose-brokers, debt-audit, counterintelligence, league-protection path. |
| Historical-return overlay | `independence_wave_archive_identity_clue` | Simplified | Only a clue gate exists. No Assyria, Mesopotamia, Volga Bulgaria, African, South American, Steppe, or Caucasus overlay content. |
| Local-polity overlay | `independence_wave_land_congress_clue` | Simplified | Only a clue gate exists. No land congress route, authority dispute, protectorate term, or local defense package. |
| Coalition congress | `independence_wave_send_permanent_delegation`, `independence_wave_mutual_aid_tables`, `independence_wave_league_charter_draft` | Partial | Functional congress lane exists. Missing failure through rival claims, patron domination, ideology conflict, and real league formation. |
| Border commission | National directorate branch only | Simplified | Claim ambition exists, but no survey, arbitration, protected transfer, ultimatum, demand, claim, or war-goal helper is wired. |
| Crisis branch | None | Missing | No failed stability, capital loss, loyalist, patron betrayal, or emergency recovery focus branch. |
| Free port/free city overlay | None | Missing | Spec route family not implemented. |
| Railway sovereignty overlay | None | Missing | Spec route family not implemented. |
| Strange modules | None | Missing | No anti-mankind, necromancy, archive-state, or impossible diplomacy focus modules. |
| Formation ledger/regional compact | `independence_wave_reveal_the_formation_ledger` plus `independence_wave_formation_ledger_category` decisions | Partial, locally fixed | Existing route is now reachable from the league charter as well as high-chaos clue focuses. Package-specific formables remain missing. |

## Missing Or Simplified Content

- `common/national_focus/006_independence_wave_focus.txt`: missing revolutionary committee route family.
- `common/national_focus/006_independence_wave_focus.txt`: missing dedicated anti-patron struggle branch; `independence_wave_balance_the_sponsors` is only a simplified patron-leverage relief focus.
- `common/national_focus/006_independence_wave_focus.txt`: historical-return and local-polity overlays are clue focuses only.
- `common/national_focus/006_independence_wave_focus.txt`: no crisis branch for failed stability, loyalists, capital exile, or patron betrayal.
- `common/national_focus/006_independence_wave_focus.txt`: no free city, free port, railway sovereignty, or strange-module branches.
- `common/national_focus/006_independence_wave_focus.txt` and `common/decisions/006_independence_wave_decisions.txt`: border commission route has claim-ambition variables but no actual claims, demands, war goals, protected transfers, or arbitration targets.
- `common/script_constants/006_independence_wave_constants.txt`: package constants cover ordinary, dormant, historical-return, and strange packages, but do not yet cover the full spec set such as game-rule, protectorate, city, railway, and local-polity package types.

## Icon Coverage Table

| Surface | Icon coverage | Status | Notes |
| --- | --- | --- | --- |
| Focus tree | 24 unique focus icon ids used | Pass | All focus icons resolve in repo interface files or vanilla `interface/goals.gfx` / `goals_shine.gfx`. |
| Idea icons | 4 reused generic idea pictures | Pass | Reuses `generic_political_discourse`, `generic_political_address`, `generic_army`, `generic_prepare_civil_war`. Bespoke Event 006 idea icons remain future asset work. |
| Decision icons | 4 reused generic decision icons | Pass | Reuses generic political/army/civil-war icons. Bespoke dossier, congress, patron, and formation icons remain future asset work. |
| Focus filters | Vanilla focus filters only | Pass | No custom filter sprites needed in this tranche. |

## Localisation And Reward Mismatches

- Localisation coverage check found no missing focus, decision, category, or idea keys in `localisation/english/006_independence_wave_l_english.yml`.
- File encoding check confirmed UTF-8 BOM.
- Forbidden `:0` localisation key scan found no matches.
- `independence_wave_file_for_arbitration` uses `constant:independence_wave_focus.pressure_relief_small` to reduce `independence_wave_claim_ambition`. The gameplay effect matches arbitration restraint, but the constant name is semantically mismatched. This was not patched because the effect value is intentional and a constants rename would touch broader tuning references.
- `independence_wave_dossier_war_plans` and `independence_wave_claimant_state` build claim ambition but do not yet grant claims, decisions, or war goals. This is a design-content gap, not a syntax issue.

## AI Behavior Gaps

- All 31 focus blocks have `ai_will_do`.
- Route-opening AI reacts to ideology, war state, stability, claim ambition, legitimacy, and patron leverage.
- No separate AI strategy plan exists for Event 006 releases.
- AI has no dedicated revolutionary route behavior because the route is missing.
- AI has no explicit anti-patron path beyond lower weighting for patron route and a leverage-sensitive sponsor-balancing focus.
- AI cannot reason about package overlays, border commissions, strange modules, or crisis recovery because those routes are not implemented.
- Formation AI can use the regional compact decisions after the ledger opens, but package-specific formable AI is missing.

## High-Priority Fixes And Findings

1. Fixed `common/national_focus/006_independence_wave_focus.txt` `independence_wave_reveal_the_formation_ledger`: added `independence_wave_league_charter_draft` as a valid OR prerequisite and moved the focus down one row.
2. Remaining high priority: implement or plan the missing revolutionary committee branch before claiming the route family complete.
3. Remaining high priority: add a real anti-patron branch or explicitly downgrade it in the spec; current content is a sponsor-balancing focus, not a route.
4. Remaining high priority: wire border commission gameplay from `independence_wave_border_office`, `independence_wave_dossier_war_plans`, and `independence_wave_claimant_state` into decisions, claims, or war-goal helpers.
5. Remaining high priority: package overlays are currently only clue gates. Do not claim historical-return or local-polity route completion from this tree.

## Event 005 Separation Check

- `independence_wave_setup_released_country` sets `chaosx_release_origin_independence_wave` before calling `independence_wave_load_provisional_focus_tree`.
- `independence_wave_load_provisional_focus_tree` loads only `independence_wave_liberation_provisional_tree`.
- The provisional tree `country` scorer checks `is_independence_wave_release = yes`.
- No Event 005 focus tree id, formable helper, or Soviet Collapse focus loader is called from the audited Event 006 files.
- `is_independence_wave_release` excludes Soviet Collapse origin/breakaway flags to prevent shared-tag contamination.

## Validation Run

- Read offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, national focus modding, and AI focuses.
- Read vanilla docs from `~/projects/Hearts of Iron IV/documentation/` and `~/projects/Hearts of Iron IV/common/script_constants/documentation.md`, including `load_focus_tree` effect documentation.
- Inspected vanilla focus/loading precedents in `common/national_focus/generic.txt`, `common/national_focus/philippines.txt`, and vanilla `load_focus_tree` call sites.
- Trailing-whitespace scan over Event 006 touched files and this handoff.
- Brace balance check over Event 006 focus/effects/triggers/constants/ideas/decisions/categories and `events/006_independence_wave.txt`.
- Unsupported comparison-operator scan over Event 006 touched files.
- Focus localisation coverage check for all 31 focus ids.
- Decision/category/idea localisation coverage check.
- Focus icon coverage check against repo `interface/` and vanilla `interface/`.
- Duplicate Event 006 focus id scan across `common/national_focus/`.
- UTF-8 BOM check for `localisation/english/006_independence_wave_l_english.yml`.
- Forbidden localisation `:0` key scan.

## Skipped Validation

- No live HOI4 load test was run.
- No full Clausewitz parser validation tool was available in the repository.
- No in-game route scenario validation was run.
- No web research was used, per task instruction.

## Remaining Risks And Gaps

- The current tree is a provisional first-pass trunk and does not satisfy the full focus-tree spec route coverage.
- The tree can load for Event 006 releases, but future package overlays still need origin-gated package checks before they are considered safe.
- The focus tree remains generic and reuses vanilla icons. Asset work for bespoke focus, idea, decision, formation, and package icons is still pending.
- `events/006_independence_wave.txt` still implements an ordinary-candidate-only first tranche. Broader package route gaps should not be patched inside this audit without a larger implementation tranche.
- No improvement-loop plan was written in this audit because the broad gaps are already explicit in the specs and foundation handoff; implementation was limited to one narrow route unlock fix.
