# Event 006 Border Commission Focus Tooltip Audit

Date/time: 2026-05-30 08:59:31 UTC

Scope:
- Audited the bounded parent patch in `common/national_focus/006_independence_wave_focus.txt`.
- No flag assets, flag definitions, or visual assets were opened or edited.
- No gameplay files were changed by this audit.

## Changed Files

| File | Change |
| --- | --- |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_085931_border_commission_focus_tooltip_audit.md` | Added this audit handoff. |

## Audited Focus Tooltip Patch

| Focus id | Parent tooltip addition | Decision exists | Localisation exists | Route viability |
| --- | --- | --- | --- | --- |
| `independence_wave_file_for_arbitration` (`common/national_focus/006_independence_wave_focus.txt:485`) | `unlock_decision_tooltip = independence_wave_freeze_claim_under_observers` (`:498`) | Yes, decision block at `common/decisions/006_independence_wave_decisions.txt:1263`. | Yes, name/desc at `localisation/english/006_independence_wave_l_english.yml:206` and `:207`. | Viable on the civic arbitration route after the border survey is filed and a valid border target exists. |
| `independence_wave_claimant_state` (`common/national_focus/006_independence_wave_focus.txt:639`) | `unlock_decision_tooltip = independence_wave_petition_border_parish` (`:651`) | Yes, decision block at `common/decisions/006_independence_wave_decisions.txt:1175`. | Yes, name/desc at `localisation/english/006_independence_wave_l_english.yml:198` and `:199`. | Viable on the national directory border route after the border survey is filed and a valid border target exists. |

## Route Coverage

| Route / branch | Relevant focuses | Surfaced decisions | Gate check |
| --- | --- | --- | --- |
| Civic arbitration route | `independence_wave_observer_charter` -> `independence_wave_observer_protected_elections` -> `independence_wave_file_for_arbitration` | `independence_wave_request_league_arbitration`, `independence_wave_freeze_claim_under_observers` | `can_independence_wave_open_border_commission` accepts `independence_wave_route_civic_mandate` and `independence_wave_focus_arbitration_files`; the decision still needs `independence_wave_border_survey_filed` and a valid target state. |
| National directory border route | `independence_wave_national_directory` -> `independence_wave_border_office` -> `independence_wave_dossier_war_plans` -> `independence_wave_claimant_state` | `independence_wave_file_border_survey`, `independence_wave_issue_dossier_ultimatum`, `independence_wave_petition_border_parish` | `can_independence_wave_open_border_commission` accepts `independence_wave_route_national_directorate`; `independence_wave_petition_border_parish` still needs `independence_wave_border_survey_filed`, no cooldown, dispute room, and a valid target state. |

## Missing Or Simplified Content

| Item | Status |
| --- | --- |
| Missing referenced decision ids | None found for the two added tooltips. |
| Missing localisation keys | None found for the two added decision names/descriptions. |
| Impossible advertised decisions | None found. Both decisions have possible route states, but they are state-targeted and remain gated by the survey flag plus target availability. |
| Simplification / residual risk | `unlock_decision_tooltip` reads as an unlock even though the state-targeted decisions are also controlled by scripted triggers. This matches the existing Border Commission surfacing style but may be interpreted by players as an immediate button if no target or survey exists. |

## Icon Coverage

| Surface | Icon id | Status |
| --- | --- | --- |
| `independence_wave_file_for_arbitration` focus | `GFX_goal_generic_forceful_treaty` | Existing vanilla-style focus icon reference; unchanged. |
| `independence_wave_claimant_state` focus | `GFX_goal_generic_more_territorial_claims` | Existing vanilla-style focus icon reference; unchanged. |
| `independence_wave_freeze_claim_under_observers` decision | `generic_political_discourse` | Existing decision icon reference; unchanged. |
| `independence_wave_petition_border_parish` decision | `generic_political_address` | Existing decision icon reference; unchanged. |

## Localisation And Reward Mismatch Audit

| Identifier | Finding |
| --- | --- |
| `independence_wave_file_for_arbitration` | Focus title/description match peaceful arbitration; freeze-under-observers tooltip is thematically aligned with the route. |
| `independence_wave_freeze_claim_under_observers` | Localisation uses `[FROM.GetName]`, appropriate for `state_target = any` decision scope. |
| `independence_wave_claimant_state` | Focus title/description match a state asserting border claims; parish petition tooltip is thematically aligned. |
| `independence_wave_petition_border_parish` | Localisation uses `[FROM.GetName]`, appropriate for `state_target = any` decision scope. |

## AI Behavior Gaps

| Identifier | Finding |
| --- | --- |
| `independence_wave_freeze_claim_under_observers` | Has route-aware AI weights favoring civic mandate and discouraging national directorate. No patch needed. |
| `independence_wave_petition_border_parish` | Has route-aware AI weights favoring national directorate and discouraging civic mandate. No patch needed. |

## High-Priority Fixes

None. The parent additions are syntactically valid and reference existing decisions/localisation. No gameplay patch was applied.

## Validation Commands And Results

| Command | Result |
| --- | --- |
| `rg -n "<=|>=" common/national_focus/006_independence_wave_focus.txt common/decisions/006_independence_wave_decisions.txt common/scripted_triggers/006_independence_wave_triggers.txt common/scripted_effects/006_independence_wave_effects.txt` | No unsupported `<=` or `>=` operators found. |
| `awk` brace counts on focus, decision, trigger, and effect files | All checked files had matching `{` and `}` counts. |
| Duplicate focus id check with `rg -o "id = ..."` / `sort` / `uniq -d` | No duplicate focus ids found in `006_independence_wave_focus.txt`. |
| Duplicate decision id check with `rg` / `sort` / `uniq -d` | No duplicate decision ids found in `006_independence_wave_decisions.txt`. |
| `comm` check of focus `unlock_decision_tooltip` ids against decision ids | No missing focus tooltip decision ids found. |
| `comm` check for the two added decision localisation name/desc keys | No missing localisation keys found. |
| `file -b --mime-encoding localisation/english/006_independence_wave_l_english.yml && xxd -p -l 3 ...` | Encoding reports `utf-8`; BOM bytes are `efbbbf`. |

## Skipped Validation

| Check | Reason |
| --- | --- |
| In-game runtime validation | Not available from this subagent environment. |
| Full mod load validation | Not run because the task is a bounded focus-tooltip audit and the worktree contains intentional unrelated dirty Event 005/Event 006 changes. |

## Remaining Risks

- The two advertised decisions depend on prior `independence_wave_border_survey_filed` state and valid target states. The focus tooltip is therefore an advertised decision surface, not a guarantee that a usable state target appears immediately after focus completion.
- Existing broader Border Commission trigger design was not redesigned, per task scope.
