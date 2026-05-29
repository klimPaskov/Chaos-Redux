# Focus Compact Reward Cleanup Handoff

Date: 2026-05-29 11:12 UTC

## Scope

Patched only:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

No scripted effects, scripted triggers, decisions, localisation, flags, scenario, or asset files were edited.

## Route Coverage Table

| Required route or area | Implemented branch checked | Status | Notes |
| --- | --- | --- | --- |
| Ukraine compact political/foreign/expansion lanes | `soviet_collapse_ukraine_focus_tree` | Patched | Continuous panel moved from far-right margin to `x = 4032`; right-side route and expansion outliers remain compact at max `x = 38`. |
| Belarus compact rail/forest/corridor lanes | `soviet_collapse_belarus_focus_tree` | Patched | Continuous panel moved to `x = 3072`; max focus `x` is now `28`, and no duplicate focus coordinates remain. |
| Belarus forest mutual-exclusion branch | `blr_soviet_collapse_partisans_or_army` family | Patched | `decentralized_detachments` moved inward, shared ammunition/staff follow-up moved left of the exclusive diamond so it no longer sits in the middle lane. |
| Reward spam cleanup | Ukraine, Belarus, NLC, CFR representative focuses | Patched | Replaced small stockpile/building-only pieces with existing route variables, flags, helper effects, or decision/mechanic unlock flags already available to the trees. |

## Changed Focus IDs

- `ukr_soviet_collapse_black_banner_compact`
- `ukr_soviet_collapse_free_soil_compromise`
- `ukr_soviet_collapse_anatolian_grain_mission`
- `ukr_soviet_collapse_the_western_question_cannot_wait`
- `ukr_soviet_collapse_romanian_port_route`
- `ukr_soviet_collapse_equipment_corridor_authority`
- `ukr_soviet_collapse_ports_need_soldiers`
- `blr_soviet_collapse_foreign_aid_through_brest`
- `blr_soviet_collapse_guide_companies`
- `blr_soviet_collapse_village_warning_bells`
- `blr_soviet_collapse_partisans_or_army`
- `blr_soviet_collapse_decentralized_detachments`
- `blr_soviet_collapse_forest_ammunition_hides`
- `blr_soviet_collapse_the_forest_general_staff`
- `blr_soviet_collapse_minsk_does_not_own_every_tree`
- `NLC_station_court_registers`
- `NLC_ice_watch_training_yards`
- `NLC_ration_and_signal_escorts`
- `CFR_emergency_cement_accounts`

## Route Behavior Before And After

| Focus or area | Before | After |
| --- | --- | --- |
| Ukraine panel and right lane | Ukraine still had excess right-side width after the previous compacting pass. | `continuous_focus_position` is closer, and no Ukraine duplicate coordinates remain after the right-lane cleanup. |
| Belarus panel and forest branch | Belarus had a larger right margin and a forest common follow-up centered under mutually exclusive alternatives. | The panel is closer, the exclusive branch is narrower, and the shared forest ammunition/staff path is offset left of the diamond. |
| `ukr_soviet_collapse_romanian_port_route` | Gave foreign channel plus a small convoy stockpile. | Opens the Black Sea security mission flag, increases liaison/depot variables, and refreshes consolidated republic ideas. |
| `ukr_soviet_collapse_equipment_corridor_authority` | Gave foreign channel plus support equipment. | Opens the League arms board flag, unlocks League unit deployment decisions, adds depot/liaison progress, and refreshes ideas. |
| `ukr_soviet_collapse_ports_need_soldiers` | Mixed two small equipment grants with a coastal bunker. | Keeps the coastal defense identity but shifts reward toward manpower, war support, foreign/military helpers, and idea refresh. |
| Belarus/NLC representative stockpile rewards | Several focuses used small equipment grants as the main payoff. | Rewards now use local authority, resilience, depot, liaison, recovery progress, and existing helper effects. |
| `CFR_emergency_cement_accounts` | Added one random infrastructure level after mandate gain. | Uses the existing CFR public works helper instead of a one-off construction reward. |

## Icon Coverage Table

| Focus group | Icons changed | Status |
| --- | --- | --- |
| Ukraine touched focuses | None | Existing icon ids preserved. |
| Belarus touched focuses | None | Existing icon ids preserved. |
| NLC touched focuses | None | Existing icon ids preserved. |
| CFR touched focuses | None | Existing icon id preserved. |

## Localisation And Reward Mismatch List

- No localisation files were edited by scope.
- Checked touched focus localisation strings where present; they describe corridors, port guards, village warning, legal registers, training yards, escorts, and cement accounts broadly enough for the new variable/helper rewards.
- No new localisation keys or icon ids were added.

## AI Behavior Gaps

- No AI weights were changed.
- Existing route-aware modifiers remain in place for the touched focuses.
- Broader AI route planning remains outside this bounded focus-file cleanup.

## Missing Or Simplified Content

- This was not a full focus-tree redesign.
- Ukraine still has dense late political/expansion cross-links that would benefit from a separate visual pass if the parent wants every route lane redrawn.
- The patch intentionally cleaned a representative reward set rather than replacing every small stockpile/building reward across all Soviet Collapse trees.

## Validation

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt`: passed.
- Unsupported operator scan for `<=` and `>=` in touched focus files: no matches.
- Simple brace balance for touched focus files: final depth `0`, no early closes.
- Coordinate audit for Ukraine/Belarus: no duplicate focus coordinates after patch.

## Skipped Validation

- No in-game load or visual screenshot validation was run from this subagent environment.
- No localisation validation was run because localisation edits were explicitly out of scope.

## Remaining Route Risks

- The three touched focus files already contain broad concurrent edits from earlier/parallel work; this handoff covers only the bounded cleanup above.
- If the parent wants a full reward-spam removal pass, queue a separate improvement plan rather than expanding this patch further.

## Plan Handoff

No separate improvement plan was written.
