# Event 010 Death Focus Tree Depth Follow-Up Plan

Status: implemented by the parent agent after the focus-tree audit and improvement-loop addendum.

This file records the implementation-ready minimum expansion that replaced the earlier loose follow-up. The parent implementation went beyond the 17-focus minimum and expanded `common/national_focus/010_death_focus_tree.txt` into a fixed-purpose 26-node Death lane tree with opening, Shroud, Hunger, Census, Public Death, Coastal, Wasteland, Host, Last Shores, and World Consumed branches. The later remaining-route addendum has also been implemented: Dark Methods, Black Oath, Herald, Black Apostolate, Black Atlas, and the world-end Zol animated package are active behind their real prerequisites rather than hidden placeholders.

Implemented follow-up evidence:

- `common/national_focus/010_death_focus_tree.txt` contains all required lanes plus the fuller source-spec intermediate nodes.
- `common/scripted_effects/010_death_effects.txt` reads focus flags for stricter low-pop island spread, wither progress, and revealed coastal-jump cooldown.
- `common/scripted_triggers/010_death_triggers.txt` adds the stricter low-pop island target helper and makes coastal watch no longer an absolute block after the `No Ferry Returns` focus.
- `interface/010_death.gfx` registers base and `_shine` sprites for every Death focus.
- `localisation/english/010_death_l_english.yml` contains title and description keys for every implemented focus.
- `docs/events/010_death.md`, `docs/assets/010_death/generated_art_manifest.md`, and `docs/assets/010_death/generated_art_gfx_handoff.md` document the expanded focus tree and completed route/asset packages.

## Original Audit Verdict

Superseded by the parent implementation. The text below records the audit finding that existed before the 26-node lane tree and remaining-route implementation.

The earlier seven-focus DTH ladder was acceptable only as a fixed-purpose debug package if the parent explicitly queued or superseded the source focus-tree architecture in `docs/specs/010_death_specs/specs/010_death_country_package_and_focus_tree.md`.

Against the accepted spec at audit time, that ladder was materially incomplete. The spec says Death may be fixed-purpose, but still needs branch logic around shroud, hunger, census, coastal recovery, wasteland pressure, host behavior, and terminal hunger. It also says the implementation must not replace that branch logic with a single linear ladder unless the same logic exists in mechanics, AI, docs, and event-log detail. The implemented tree now expresses those lanes and the related mechanics.

Classification:

| Finding | Classification if current spec remains accepted | Can be queued instead? |
| --- | --- | --- |
| Seven-focus ladder lacks real Shroud/Hunger/Census/Public Death/Coastal/Wasteland/Host lanes | Completion blocker for final spec-fidelity review | Yes, only if the source spec and event doc explicitly say the compact tree is accepted and the lane tree is future depth |
| `death_black_census_focus` does not add or upgrade `death_black_census` | Completion blocker | No, because the implemented focus title/description already promise this surface |
| `death_wasteland_roads` does not change wither/wasteland behavior | Completion blocker | No, because the implemented focus title/description already promise this surface |
| Focus AI is mostly flat and not stage-aware | Completion blocker for DTH as an AI-usable focus tree | No, because DTH can load and use the tree |
| Dark Methods and Black Oath were outside this focus-only pass | Resolved by the remaining-route addendum implementation | No outstanding queue remains for these routes |
| Black Atlas GUI and animated Zol/world-end presentation were outside this focus-only pass | Resolved by the remaining-route addendum and final asset pass | No outstanding queue remains for these surfaces |

## Smallest Real Expansion

Do not build a normal country tree. Add a compact 17-focus Death tree: 7 existing focuses retained, 10 new focuses added. Each lane has two focuses, enough to be felt without ordinary politics, industry, or diplomacy filler.

Recommended costs:

| Cost constant | Value | Use |
| --- | ---: | --- |
| `death_focus_cost.very_short` | 2 | Opening trunk |
| `death_focus_cost.short` | 3 | First lane focus |
| `death_focus_cost.medium` | 5 | Second lane focus and Public Death |
| `death_focus_cost.long` | 7 | Terminal focuses |

If `cost = constant:...` is not accepted in focus files, keep file-scoped `@death_focus_*` aliases in `common/national_focus/010_death_focus_tree.txt`, but keep the authoritative values mirrored in `common/script_constants/010_death_constants.txt` for effects, triggers, and docs.

### Focus topology

| Focus id | Status | Lane | Position | Prerequisite / availability | Reward summary |
| --- | --- | --- | --- | --- | --- |
| `death_first_silence_focus` | New | Opening | `x = 10 y = 0` | none | Calls `death_focus_apply_first_silence`; reinforces no-army/no-economy state, records origin evolution if not already recorded |
| `death_country_on_the_island` | New | Opening | `x = 10 y = 1` | `death_first_silence_focus` | Calls `death_focus_apply_country_on_the_island`; reload-safe DTH setup, clamps spread pressure, confirms DTH remains hidden unless revealed |
| `death_shroud_whispers` | Existing | Shroud | `x = 6 y = 2` | `death_country_on_the_island` | Rework reward into `death_focus_apply_shroud_whispers`; lowers report visibility and delays broad recognition without strengthening hosts |
| `death_no_mail_before_spring` | New | Shroud | `x = 6 y = 3` | `death_shroud_whispers` | Calls `death_focus_apply_no_mail_before_spring`; extends report delay bands and reduces early investigation pressure |
| `death_hunger_shore` | Existing | Hunger | `x = 10 y = 2` | `death_country_on_the_island` | Rework reward into `death_focus_apply_hunger_shore`; raises island pressure and unlocks stricter low-pop island target preference |
| `death_lowest_names_first` | New | Hunger | `x = 10 y = 3` | `death_hunger_shore` | Calls `death_focus_apply_lowest_names_first`; makes `death_try_island_spread` try a stricter low-pop target pool before normal island spread |
| `death_black_census_focus` | Existing | Census | `x = 14 y = 2` | `death_country_on_the_island`; available once `global.death_consumed_population` is at or above `constant:death_focus_gate.black_census_population_k` or Death is revealed | Calls `death_focus_apply_black_census`; adds `death_black_census`, sets census-scaling flag, improves ghost readiness but does not spawn free armies by itself |
| `death_first_ghost_muster_focus` | New | Census / host bridge | `x = 16 y = 4` | `death_black_census_focus`; available at `constant:death_ghosts.passive_threshold` or higher | Calls `death_focus_apply_first_ghost_muster`; spawns one tier-appropriate host if a valid active wasteland exists and records the military stage. This is not required for Public Death below the 600 tier |
| `death_public_death_focus` | New | Convergence | `x = 10 y = 5` | Requires the pre-reveal foundation: `death_no_mail_before_spring`, `death_lowest_names_first`, and `death_black_census_focus`; available only after `death_publicly_revealed` | Calls `death_focus_apply_public_death`; ensures `death_public_death` idea, world-threat refresh, neighbor-war refresh, and mainland reveal evolution are aligned |
| `death_another_shoreline` | New | Coastal | `x = 6 y = 6` | `death_public_death_focus` | Calls `death_focus_apply_another_shoreline`; improves coastal-jump recovery and reduces revealed cooldown through a focus-specific cooldown constant |
| `death_no_ferry_returns` | New | Coastal | `x = 6 y = 7` | `death_another_shoreline` | Calls `death_focus_apply_no_ferry_returns`; makes coastal watch reduce jump chance/pressure rather than hard-block all high-chaos or world-end returns |
| `death_wasteland_roads` | Existing | Wasteland | `x = 10 y = 6` | `death_public_death_focus` | Rework reward into `death_focus_apply_wasteland_roads`; increases wither progress only through the existing pulse and marks wasteland lane active |
| `death_every_road_slows` | New | Wasteland | `x = 10 y = 7` | `death_wasteland_roads` | Calls `death_focus_apply_every_road_slows`; strengthens active/recaptured wasteland penalties through existing modifiers or a documented focus flag read by modifier/update helpers |
| `death_mourning_host` | Existing | Host | `x = 14 y = 6` | `death_public_death_focus`; available at `constant:death_ghosts.passive_threshold` or higher | Rework reward into `death_focus_apply_mourning_host`; spawns weak hosts, keeps AI passive/holding |
| `death_orders_without_breath` | New | Host | `x = 14 y = 7` | `death_mourning_host`; available at `constant:death_ghosts.stronger_threshold` or world-end | Calls `death_focus_apply_orders_without_breath`; upgrades host AI from hold to local counterattack, never full aggression before world-end |
| `death_last_shores_focus` | Existing | Terminal | `x = 10 y = 9` | Separate AND prerequisites: `death_no_ferry_returns`, `death_every_road_slows`, `death_orders_without_breath`; available if `death_can_start_world_end = yes` or `death_world_end_started` | Keeps current world-end start/foothold behavior, but prerequisite chain now proves post-reveal lanes |
| `death_world_consumed_focus` | Existing | Terminal | `x = 10 y = 10` | `death_last_shores_focus`; available if `death_whole_world_consumed = yes` | Keeps current final helper |

### Accepted omissions inside this minimum

- Do not add the full 23-node source tree yet. This 17-focus version is the smallest real lane tree and avoids filler.
- Do not add normal political, industrial, diplomatic, reform, adviser, research, or economy branches.
- Do not expose Dark Methods, Black Oath, Herald of Zol, Black Apostolate, or Black Atlas from this focus pass.
- Do not add custom focus filter categories unless the parent wants a wider focus UI infrastructure pass. Use existing filters for this minimum.

## Required Script Surface

Use existing Death helpers wherever possible. Add narrow focus helpers instead of packing complex logic directly into focus rewards.

### New or revised constants

Add these to `common/script_constants/010_death_constants.txt`:

| Category/key | Proposed value | Use |
| --- | ---: | --- |
| `death_focus_cost.very_short` | 2 | Opening focuses |
| `death_focus_cost.short` | 3 | Lane starters |
| `death_focus_cost.medium` | 5 | Lane capstones and Public Death |
| `death_focus_cost.long` | 7 | Last Shores / World Consumed |
| `death_focus_gate.black_census_population_k` | 250 | Minimum consumed-population gate for Black Census before reveal |
| `death_focus_reward.report_delay_bonus_days` | 21 | Shroud report-delay modifier |
| `death_focus_reward.report_visibility_reduction` | -1 | Missing-report pressure offset |
| `death_focus_reward.lowest_names_cap_k` | 50 | Stricter island target cap for Hunger capstone |
| `death_focus_reward.hunger_pressure` | 2 | Hunger lane spread pressure |
| `death_focus_reward.public_death_pressure` | 1 | Public Death convergence pressure |
| `death_focus_reward.coastal_cooldown_days` | 42 | Revealed cooldown after coastal lane capstone |
| `death_focus_reward.coastal_pressure_cost` | -1 | Pressure cost paid when an improved coastal jump succeeds |
| `death_focus_reward.wither_bonus` | 1 | Extra wither progress after Wasteland lane capstone |
| `death_focus_reward.host_extra_passive_spawns` | 1 | Extra passive host cap for Host lane |
| `death_focus_reward.host_extra_stronger_spawns` | 1 | Extra stronger host cap for Host lane |
| `death_focus_ai.opening` | 100 | AI opening trunk |
| `death_focus_ai.hidden_shroud` | 55 | AI hidden Shroud priority |
| `death_focus_ai.hidden_hunger` | 50 | AI hidden Hunger priority |
| `death_focus_ai.hidden_census` | 35 | AI hidden Census priority |
| `death_focus_ai.public_convergence` | 100 | AI Public Death priority after reveal |
| `death_focus_ai.post_wasteland` | 45 | AI Wasteland lane |
| `death_focus_ai.post_coastal` | 50 | AI Coastal lane |
| `death_focus_ai.post_host` | 45 | AI Host lane |
| `death_focus_ai.terminal` | 100 | AI Last Shores / terminal focus |

Existing `death_focus_reward.pressure_small`, `pressure_medium`, `ghost_equipment_small`, `ghost_manpower_small`, and `world_end_pressure` can remain, but the new helper names should make each lane's role explicit.

### New helper effects

Add focus-owned wrappers in `common/scripted_effects/010_death_effects.txt`:

| Helper | Scope | Required behavior |
| --- | --- | --- |
| `death_focus_apply_first_silence` | DTH country | Set `death_focus_first_silence`, ensure `death_country_without_breath` and `death_first_silence`, record origin evolution if needed |
| `death_focus_apply_country_on_the_island` | DTH country | Set `death_focus_country_on_the_island`, call `death_setup_country`, clamp spread pressure, keep no public reveal side effects |
| `death_focus_apply_shroud_whispers` | DTH country | Set `death_focus_shroud_whispers`, add report-delay/visibility variables, record island-report evolution only if a report stage exists |
| `death_focus_apply_no_mail_before_spring` | DTH country | Set `death_focus_no_mail_before_spring`; report scheduling should read this flag for the next report delay |
| `death_focus_apply_hunger_shore` | DTH country | Set `death_focus_hunger_shore`, add `constant:death_focus_reward.hunger_pressure`, no host spawning |
| `death_focus_apply_lowest_names_first` | DTH country | Set `death_focus_lowest_names_first`; island spread should try `death_is_valid_island_spread_target_lowest_names` first |
| `death_focus_apply_black_census` | DTH country | Set `death_focus_black_census`, add `death_black_census` if missing, set `death_black_census_active` |
| `death_focus_apply_first_ghost_muster` | DTH country | Set `death_focus_first_ghost_muster`, call `death_spawn_ghost_hosts_for_current_tier` once if threshold allows |
| `death_focus_apply_public_death` | DTH country | Set `death_focus_public_death`, ensure `death_public_death` idea, call `death_refresh_world_threat_source`, and call the existing neighbor-war refresh if present or add a narrow one |
| `death_focus_apply_another_shoreline` | DTH country | Set `death_focus_another_shoreline`; coastal cooldown helper should prefer `constant:death_focus_reward.coastal_cooldown_days` after this flag |
| `death_focus_apply_no_ferry_returns` | DTH country | Set `death_focus_no_ferry_returns`; coastal watch should reduce pressure/cooldown, not act as an absolute high-chaos/world-end block |
| `death_focus_apply_wasteland_roads` | DTH country | Set `death_focus_wasteland_roads`; wither pulse should read this flag for pressure/progress |
| `death_focus_apply_every_road_slows` | DTH country | Set `death_focus_every_road_slows`; refresh active Death wasteland modifiers and recaptured modifiers through existing modifier helpers |
| `death_focus_apply_mourning_host` | DTH country | Set `death_focus_mourning_host`; spawn passive hosts only if threshold and active wasteland exist |
| `death_focus_apply_orders_without_breath` | DTH country | Set `death_focus_orders_without_breath`; set local-counterattack AI strategy/flag, spawn stronger hosts only if threshold allows |

### New or revised triggers

Add or revise in `common/scripted_triggers/010_death_triggers.txt`:

| Trigger | Purpose |
| --- | --- |
| `death_focus_black_census_available` | True when Death has enough consumed population or has already been publicly revealed |
| `death_focus_ghost_muster_available` | True at 600 chaos threshold or world-end |
| `death_focus_orders_without_breath_available` | True at 800 chaos threshold or world-end |
| `death_focus_public_death_available` | True only after `death_publicly_revealed` |
| `death_focus_last_shores_available` | Wraps current `death_can_start_world_end` or `death_world_end_started` |
| `death_is_valid_island_spread_target_lowest_names` | Stricter Hunger target pool: island, no divisions, not capital, below `death_focus_reward.lowest_names_cap_k`, not consumed |
| `death_coastal_watch_blocks_current_jump` | Centralizes when `death_coastal_watch` blocks a jump versus reduces chance/pressure after `death_focus_no_ferry_returns` |

### Existing helpers that must read focus flags

- `death_try_island_spread`: if DTH has `death_focus_lowest_names_first`, try the stricter target helper before the current general island spread target.
- `death_try_mainland_pressure_spread`: if DTH has `death_focus_hunger_shore`, apply the Hunger pressure constant; do not reveal early without the existing mainland threshold.
- `death_try_wither`: if DTH has `death_focus_wasteland_roads` or `death_focus_every_road_slows`, add focus wither bonus through constants; still pause when non-Death divisions are present.
- `death_start_coastal_jump_cooldown`: if DTH has `death_focus_another_shoreline`, use focus cooldown for revealed-stage jumps; keep world-end cooldown stronger.
- `death_attempt_coastal_jump`: after `death_focus_no_ferry_returns`, coastal watch should reduce the attempt's pressure/cooldown effect rather than permanently blocking all high-chaos return logic.
- `death_spawn_ghost_hosts_for_current_tier`: after `death_focus_mourning_host` and `death_focus_orders_without_breath`, allow one extra bounded spawn per eligible pulse from constants; do not remove tier gates.
- `death_schedule_missing_island_reports` or the equivalent report-scheduling effect: after Shroud capstone, apply report-delay bonus only to future report scheduling. Do not try to rewrite already-fired reports.

## AI Behavior

The focus tree can use per-focus `ai_will_do` modifiers. If script constants are accepted in `ai_will_do`, use `base = constant:death_focus_ai.*`; otherwise mirror them as file-local `@death_ai_*` constants and keep the same names in the script constants for documentation.

Minimum AI weights:

| Focus id | Base | Important modifiers |
| --- | ---: | --- |
| `death_first_silence_focus` | 100 | none |
| `death_country_on_the_island` | 100 | none |
| `death_shroud_whispers` | 55 | `factor = 2` if no missing reports seen; `factor = 0.5` after public reveal |
| `death_no_mail_before_spring` | 55 | `factor = 2` if hidden; `factor = 0` after public reveal |
| `death_hunger_shore` | 50 | `factor = 2` if consumed states are below the mainland-pressure threshold; `factor = 0.5` if already revealed |
| `death_lowest_names_first` | 50 | `factor = 2` before reveal; `factor = 0.5` after reveal |
| `death_black_census_focus` | 35 | `factor = 3` if consumed population gate met; `factor = 0.25` if gate not met |
| `death_first_ghost_muster_focus` | 45 | `factor = 3` at 600 chaos; `factor = 0` below 600 |
| `death_public_death_focus` | 100 | `factor = 0` if not publicly revealed |
| `death_another_shoreline` | 50 | `factor = 2` if DTH controls fewer than `constant:death_spread.coastal_jump_contained_state_limit` states; `factor = 2` at world-end |
| `death_no_ferry_returns` | 50 | `factor = 2` if watch network is high or world-end started |
| `death_wasteland_roads` | 45 | `factor = 2` if any Death active wasteland borders a non-Death state |
| `death_every_road_slows` | 45 | `factor = 2` if Death has mainland active wastelands |
| `death_mourning_host` | 45 | `factor = 3` at 600 chaos; `factor = 0` below 600 |
| `death_orders_without_breath` | 45 | `factor = 3` at 800 chaos; `factor = 5` at world-end; `factor = 0` below 800 |
| `death_last_shores_focus` | 100 | `factor = 3` when `death_can_start_world_end = yes`; `factor = 0` otherwise unless `death_world_end_started` |
| `death_world_consumed_focus` | 200 | availability already gates it |

Do not add a broad new AI strategy file unless the parent decides focus weights cannot express this safely. A narrow `add_ai_strategy` from `death_focus_apply_orders_without_breath` is acceptable if it only affects DTH local aggression and is cleared by defeat cleanup.

## Localisation And Icon Needs

New focus localisation keys in `localisation/english/010_death_l_english.yml`:

- `death_first_silence_focus`
- `death_first_silence_focus_desc`
- `death_country_on_the_island`
- `death_country_on_the_island_desc`
- `death_no_mail_before_spring`
- `death_no_mail_before_spring_desc`
- `death_lowest_names_first`
- `death_lowest_names_first_desc`
- `death_first_ghost_muster_focus`
- `death_first_ghost_muster_focus_desc`
- `death_public_death_focus`
- `death_public_death_focus_desc`
- `death_another_shoreline`
- `death_another_shoreline_desc`
- `death_no_ferry_returns`
- `death_no_ferry_returns_desc`
- `death_every_road_slows`
- `death_every_road_slows_desc`
- `death_orders_without_breath`
- `death_orders_without_breath_desc`

Update existing descriptions for:

- `death_shroud_whispers_desc` so it promises report concealment, not generic spread.
- `death_hunger_shore_desc` so it promises low-pop island targeting and pressure.
- `death_black_census_focus_desc` so it matches adding the Black Census idea.
- `death_wasteland_roads_desc` so it matches wither/wasteland pressure.
- `death_mourning_host_desc` so it matches passive/stronger host tier behavior.

New focus sprites in `interface/010_death.gfx` with matching `_shine` entries:

| Sprite id | DDS path |
| --- | --- |
| `GFX_focus_death_first_silence` | `gfx/interface/goals/death/focus_death_first_silence.dds` |
| `GFX_focus_death_country_on_the_island` | `gfx/interface/goals/death/focus_death_country_on_the_island.dds` |
| `GFX_focus_death_no_mail_before_spring` | `gfx/interface/goals/death/focus_death_no_mail_before_spring.dds` |
| `GFX_focus_death_lowest_names_first` | `gfx/interface/goals/death/focus_death_lowest_names_first.dds` |
| `GFX_focus_death_first_ghost_muster` | `gfx/interface/goals/death/focus_death_first_ghost_muster.dds` |
| `GFX_focus_death_public_death` | `gfx/interface/goals/death/focus_death_public_death.dds` |
| `GFX_focus_death_another_shoreline` | `gfx/interface/goals/death/focus_death_another_shoreline.dds` |
| `GFX_focus_death_no_ferry_returns` | `gfx/interface/goals/death/focus_death_no_ferry_returns.dds` |
| `GFX_focus_death_every_road_slows` | `gfx/interface/goals/death/focus_death_every_road_slows.dds` |
| `GFX_focus_death_orders_without_breath` | `gfx/interface/goals/death/focus_death_orders_without_breath.dds` |

Placeholder rule for implementation: register stable sprite ids and copy a thematically close existing Death or vanilla focus DDS as a temporary placeholder only if the art package is not ready. Report placeholders explicitly. Do not rename sprite ids later.

## Dark Methods And Black Oath Boundary

This focus-only plan kept Dark Methods, Black Oath, Herald of Zol, and Black Apostolate out of the DTH focus tree. The later remaining-route addendum implemented them as living-country decisions, ideas, cosmetic identities, achievements, and Black Atlas state instead. They still do not belong in DTH focus ids or public focus descriptions.

## Acceptance Criteria

The focus depth finding can close when all of these are true:

- The tree contains the 17 focus ids listed above, or the parent explicitly supersedes this plan in writing.
- Current seven focus ids are retained or migrated with clear compatibility notes; no duplicate ids are introduced.
- `Public Death` is a real focus gated by the actual reveal flag.
- `death_last_shores_focus` requires the three post-reveal lane capstones, not just the current two short branches.
- Black Census adds or maintains `death_black_census` and has a visible lifecycle.
- Wasteland lane changes the existing wither/wasteland mechanics through helpers and constants.
- Coastal lane changes coastal-jump cooldown/target blocking through helpers and constants.
- Host lane changes ghost spawn or AI aggression through helpers and constants without removing 600/800/world-end gates.
- Each new focus has name/description localisation, base sprite, shine sprite, and appropriate search filters.
- AI weights are stage-aware and cannot select impossible stage content.
- Dark Methods and Black Oath are implemented as full living-country routes and remain outside the DTH focus tree.
- `docs/events/010_death.md` and the country/focus-tree source spec are updated or annotated after implementation so the plan is no longer a loose unresolved addendum.

## Promotion Guidance

This plan is implemented and retained as audit history. Current source-of-truth status lives in `docs/events/010_death.md` and the Event 010 specs.

The implemented design has been promoted into:

- `docs/specs/010_death_specs/specs/010_death_country_package_and_focus_tree.md`, as the accepted fixed-purpose Death focus architecture;
- `docs/events/010_death.md`, as the implemented focus route map;
- the final completion report route-coverage evidence.
