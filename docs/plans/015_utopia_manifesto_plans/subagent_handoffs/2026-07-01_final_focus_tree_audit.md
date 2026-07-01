# Event 015 `utopia_manifesto` Final Focus-Tree Audit

Subagent: Chaos Redux focus tree subagent
Date: 2026-07-01
Scope: final audit of `common/national_focus/015_utopia_manifesto_focus_tree.txt` and directly related Event 015 focus helpers, GFX, and localisation.

## Verdict

Pass with one narrow patch.

The Event 015 focus tree is clean for completion from the focus-tree side. It implements the requested branch families, has 105 focus blocks, no duplicate focus IDs, no dangling focus prerequisite or mutual-exclusion references, AI blocks on every focus, matching focus title/description localisation, and base plus `_shine` sprite coverage for every referenced focus icon.

I patched one local prerequisite defect: `utopia_new_utopia` now requires `utopia_adapt_the_commonwealth`, matching the spec and the existing achievement gate that treat geography adaptation as part of the clean New Utopia closure.

No improvement-loop plan was written. The tree is not shallow enough to require a new design handoff.

## High-Priority Fixes First

| Priority | Status | File / identifier | Finding |
| --- | --- | --- | --- |
| 1 | Fixed | `common/national_focus/015_utopia_manifesto_focus_tree.txt`, `utopia_new_utopia` | New Utopia could be taken without completing `utopia_adapt_the_commonwealth`, even though the spec requires geography adaptation for the clean proclamation and `utopia_manifesto_new_utopia_achievement_ready` already requires it. |
| 2 | Pass | `common/scripted_effects/015_utopia_manifesto_effects.txt`, `utopia_manifesto_refresh_marked_bounds_branch` | The earlier Marked Bounds `allow_branch` reveal issue is patched: ledger refresh dirties the focus-tree layout once Marked Bounds can open after tree load. |
| 3 | Pass | `interface/015_utopia_manifesto.gfx`, `GFX_goal_utopia_*` | The earlier missing shine issue is resolved. Every referenced focus icon has base and `_shine` sprite definitions. |
| 4 | Non-blocking | `common/national_focus/015_utopia_manifesto_focus_tree.txt`, support leaves and late hardline outcomes | Several support/leaf focuses use flat `ai_will_do` bases. This is acceptable for completion because all route anchors, Marked Bounds entry, New Utopia, and key gated focuses have route/ledger-aware AI. |

## Patch Details

| Changed file | Changed focus ID | Change |
| --- | --- | --- |
| `common/national_focus/015_utopia_manifesto_focus_tree.txt` | `utopia_new_utopia` | Added `prerequisite = { focus = utopia_adapt_the_commonwealth }`. |

Route behavior before and after:

| Route surface | Before | After |
| --- | --- | --- |
| New Utopia late proclamation | Required one normal route finisher, `utopia_common_store_network`, `utopia_no_secret_empire`, and clean ledger gates. It did not require geography adaptation. | Also requires `utopia_adapt_the_commonwealth`, so the clean late identity cannot skip the geography adaptation branch. |

Localisation keys changed: none.
Icon IDs changed: none.
Scripted helper IDs changed: none.

## Route Coverage Table

| Required branch / route | Status | Primary file / focus IDs | Notes |
| --- | --- | --- | --- |
| Opening trunk | Pass | `utopia_open_the_manifesto` through `utopia_four_readings` in `common/national_focus/015_utopia_manifesto_focus_tree.txt` | Introduces ledger, stores, useful arts, Need, boundaries, and route fork. |
| Living Humanism | Pass | `utopia_living_humanism`, `utopia_councils_before_ministers`, `utopia_six_hour_country`, `utopia_free_sick_tables`, `utopia_consent_assemblies`, `utopia_mercy_in_the_registers`, `utopia_renounce_the_idle_clause`, `utopia_living_commonwealth` | Mutually exclusive route anchor; Consent and peaceful/reform rewards match route role. |
| Common Store State | Pass | `utopia_common_store_state`, `utopia_grain_without_owners`, `utopia_standard_measures`, `utopia_train_of_stores`, `utopia_surplus_without_gold`, `utopia_central_auditors`, `utopia_crisis_rations`, `utopia_store_state` | Surplus, stores, audits, trains, and crisis-ration rewards avoid a generic factory-only route. |
| Guild Commonwealth | Pass | `utopia_guild_commonwealth`, `utopia_congress_of_masters`, `utopia_apprentice_lots`, `utopia_second_trade_law`, `utopia_workshop_councils`, `utopia_engineer_guilds`, `utopia_common_patents`, `utopia_guild_charter` | Vocation, apprenticeship, workshop, research, and craft militia hooks are present. |
| Island Discipline | Pass with note | `utopia_island_discipline` through `utopia_island_compact` | Implemented as coastal/island-gated civic defense with harbors, convoys, shore engineers, harbor watch, and Foreign Suspicion tradeoffs. Landlocked countries instead use `utopia_landlocked_caravan_stores`; they do not get the full Island Discipline interpretation. |
| Economy / storehouse | Pass | `utopia_storehouse_spine` through `utopia_common_store_network` | Uses infrastructure, state projects, storehouse decisions, Surplus, and foreign aid hooks. |
| Vocation / learning | Pass | `utopia_vocation_balance` through `utopia_all_useful_arts` | Uses vocation flags, education/research, labor, healers/engineers, and useful-arts rewards. |
| Military / just war | Pass | `utopia_just_war_review` through `utopia_guard_the_ledger` | Household Guard, Storehouse Engineers, defensive drill, no-glory candidate, reinforcement paths, and Needful Land interaction are present. |
| Diplomacy / League | Pass | `utopia_neighbors_read_the_book` through `utopia_no_secret_empire`; League confidence helpers in `common/scripted_effects/015_utopia_manifesto_effects.txt` and triggers in `common/scripted_triggers/015_utopia_manifesto_triggers.txt` | League is confidence/member driven, not an automatic faction. Aid corridor missions and League identity threshold are wired. |
| Needful Land / integration | Pass | `utopia_needful_land_question` through `utopia_needful_land_commission`; target and integration triggers in `common/scripted_triggers/015_utopia_manifesto_triggers.txt` | Claims and integration remain decision/mission gated; the focus tree does not grant large instant cores. |
| Geography adaptation | Pass | `utopia_coastal_store_routes`, `utopia_landlocked_caravan_stores`, `utopia_subject_ledger`, `utopia_tiny_country_deep_ledger`, `utopia_adapt_the_commonwealth` | Conditional coastal, landlocked, subject, and tiny-country entries converge through OR prerequisite semantics. New Utopia now requires the convergence focus. |
| Hidden Marked Bounds | Pass | `utopia_marked_bounds_clause` through `utopia_no_idle_acre`; `utopia_manifesto_can_open_marked_bounds`; `utopia_manifesto_refresh_marked_bounds_branch` | Hidden branch uses `allow_branch`, has matching `available`, route setting, surveyor/war/settlement sequence, and a one-time layout dirty refresh after ledger changes. |
| Late proclamation outcomes | Pass | `utopia_paper_utopia`, `utopia_new_utopia`, `utopia_necessary_commonwealth`, `utopia_marked_bounds_state`, `utopia_proclaim_the_common_store`, `utopia_the_manifesto_survives` | Outcome focuses are mutually exclusive and then converge. New Utopia now correctly includes geography adaptation. |

## Missing Or Simplified Content

| Status | File / identifier | Note |
| --- | --- | --- |
| None blocking | N/A | No required route family is missing. |
| Simplified but acceptable | `utopia_island_discipline` | The route is coastal/island-gated. This is consistent with its current reward implementation, but narrower than the broadest reading of the spec phrase "island in the mind." A full landlocked Warden interpretation would require broader route design, so I did not patch it. |
| Simplified but acceptable | Leaf `ai_will_do` blocks across support branches | Several leaf nodes use flat base weights. Route anchors and major gated outcomes carry the meaningful route/ledger AI behavior. |
| Intentional | `utopia_league_of_need` / `utopia_manifesto_maybe_apply_league_identity` | The League outcome is threshold-driven through member count and League Confidence rather than a separate late proclamation focus. This matches the accepted final depth addendum. |

## Icon Coverage Table

| Check | Result | Evidence |
| --- | --- | --- |
| Focus blocks | 105 | `common/national_focus/015_utopia_manifesto_focus_tree.txt` |
| Unique focus IDs | 105 | Mechanical extraction from focus IDs, excluding the tree ID. |
| Unique focus icons referenced | 99 | Six icon IDs are intentionally reused for related paired focuses. |
| Missing base icon sprites | 0 | Every referenced `GFX_goal_utopia_*` icon exists in `interface/015_utopia_manifesto.gfx`. |
| Missing `_shine` sprites | 0 | Every referenced focus icon has a matching `${icon}_shine` sprite. |
| Utopia goal shine sprites in GFX | 109 | `interface/015_utopia_manifesto.gfx` contains 109 `GFX_goal_utopia_*_shine` sprite definitions. |
| Reused focus icon IDs | 6 | `GFX_goal_utopia_councils`, `GFX_goal_utopia_store_state`, `GFX_goal_utopia_surplus`, `GFX_goal_utopia_auditors`, `GFX_goal_utopia_engineers`, `GFX_goal_utopia_arbitration_tables`. |

## Localisation And Reward Mismatch List

| Identifier | Status | Note |
| --- | --- | --- |
| All 105 focus IDs | Pass | Each focus has both `focus_id` and `focus_id_desc` keys in `localisation/english/015_utopia_manifesto_l_english.yml`. |
| `utopia_open_the_manifesto_tt` | Pass | Tooltip now correctly says the ledger opened on Manifesto acceptance, not on this focus. |
| `utopia_mark_needed_districts_tt` | Pass | Tooltip now says marked districts open survey work and that claims still come from the decision/mission path. |
| `utopia_new_utopia_desc` | Pass after patch | Description says Consent, Surplus, and useful work are aligned; route now also requires the adaptation focus as intended by the spec. |
| `utopia_necessary_commonwealth_desc` / `utopia_marked_bounds_state_desc` | Pass | The descriptions are distinct and match their strict survival versus hardline surveyor outcomes. |

## AI Behavior Gaps

| Area | Status | File / identifier | Note |
| --- | --- | --- | --- |
| Route anchors | Pass | `utopia_living_humanism`, `utopia_common_store_state`, `utopia_guild_commonwealth`, `utopia_island_discipline` | Each uses route-weight variables and ideology/ledger/context modifiers. |
| Route-weight preparation | Pass | `common/scripted_effects/015_utopia_manifesto_effects.txt`, `utopia_manifesto_prepare_ai_route_weights` | Weights respond to government type, subject status, Need, high chaos, and Consent. |
| Hidden Marked Bounds | Pass | `utopia_marked_bounds_clause`, `utopia_manifesto_can_open_marked_bounds` | AI starts at low base, increases under high Need, authoritarian government, and Marked Bounds route weight. |
| New Utopia | Pass | `utopia_new_utopia` | AI avoids it under high Overreach and now cannot skip geography adaptation. |
| Necessary Commonwealth / Marked Bounds State | Partial but acceptable | `utopia_necessary_commonwealth`, `utopia_marked_bounds_state` | Gated by route/ledger state but use flat base AI weights. This is a tuning risk, not a completion blocker. |
| Support leaves | Partial but acceptable | Several support branch focuses | Every focus has AI, but many lower-risk support focuses are flat weighted. |

## Validation

Task-specific checks run after the patch:

| Check | Result |
| --- | --- |
| Focus block count | 105 |
| Unique focus IDs | 105 |
| `ai_will_do` blocks | 105 |
| Dangling `focus = ...` prerequisite / mutual-exclusion refs | 0 |
| Missing focus title localisation | 0 |
| Missing focus description localisation | 0 |
| Missing base sprite definitions for referenced focus icons | 0 |
| Missing `_shine` sprite definitions for referenced focus icons | 0 |
| `utopia_new_utopia` has `utopia_adapt_the_commonwealth` prerequisite | Yes |
| Unsupported `<=` / `>=` in audited focus/effect/trigger files | None found |
| Brace balance in audited focus/effect/trigger files | Balanced |

Skipped live game validation. This subagent only has repo access; no HOI4 runtime check was available in this context.

## Remaining Route Risks

1. `utopia_island_discipline` is intentionally coastal/island-gated by current rewards. If the parent wants the route to be selectable by all landlocked threatened minors, that needs a broader Warden/inland alternate route design rather than a one-line availability patch.
2. League identity is applied through confidence/member thresholds instead of a separate late League outcome focus. This matches the accepted implementation addendum, but reviewers should know it will not appear as one of the mutually exclusive bottom-row proclamation focuses.
3. Some support focus AI is flat. This should not block completion, but a future balance pass could make shared support branches more route-aware.
4. The Event 015 gameplay files are currently untracked in this dirty worktree, so this handoff cannot provide a tracked baseline diff for the full implementation.

## Skills And References Used

Skills used:

- `hoi4-focus-trees`
- `chaos-redux-events`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`

Required references consulted before auditing:

- `AGENTS.md`
- Offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, and national focus modding.
- Vanilla HOI4 documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`, including effects, triggers, modifiers, script concepts, and script constants documentation.
- Vanilla focus precedent in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/denmark.txt`.
