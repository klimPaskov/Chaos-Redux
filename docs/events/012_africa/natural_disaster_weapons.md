# Event 012 hostile nature calls

Event 012 reuses the existing high-chaos actions `petition_the_rain` (69) and `defy_the_drought` (70) as bounded hostile nature weapons when a full action resolves against the exact selected enemy country.

The current host keeps the canonical Rain/Drought selectors. A completed priority member can also open the explicit `africa_natural_disaster_enemy_targets` roster, choose one enemy, and route the same action IDs through the current host. No new country tag, cosmetic tag, or duplicate action store is created.

Both surfaces use the shared timed-country/country target contract so human and AI selection pass the same selected enemy into the action record and Event 013 call.

## Package-specific invocation names

The two decisions keep one shared mechanic and one shared target store, but their descriptions identify the promoted package's bounded nature tradition. The labels are presentation only: authority, route, ecological pressure, target size, costs, severity, cleanup, and Event 013 dispatch remain governed by the shared scripted effects.

| Package | Visible invocation |
| --- | --- |
| Asante | Golden Stool Rain Rite |
| Oyo | Alaafin's Thunder Road |
| Sokoto | Harmattan Break |
| Kanem-Bornu | Lake Chad Tempest |
| Manden | Niger River's Wrath |
| Kongo | Forest-Basin Tempest |
| Buganda | Lake Victoria Stormcall |
| Aksum | Highland and Red Sea Thunder |
| Harar | Harar Rain Covenant |
| Kilwa | Kilwa Monsoon Spear |
| Nubia | Nile Flood Oath |
| Luba | Copperbelt Earthshock |
| Lunda | Ancestral Rainfront |
| Great Zimbabwe | Stone Country Storm |
| Merina | Highland Cyclone Crown |
| Zulu | Thunder of the Royal Shield |

## Runtime contract

`africa_natural_disaster_weapon_actor_is_eligible` remains the host-side bridge in `common/scripted_triggers/012_africa_triggers.txt`.

It requires Evolution III, a completed host ecology/covenant route, or a saved `africa_natural_disaster_action_actor` whose priority package has its host-generation receipt, political settlement, distinct mechanic, and nonzero nature authority complete.

`africa_natural_disaster_member_actor_is_eligible` is the member-side gate. It requires the existing Event 006 carrier package, current host generation, Evolution III, settled politics, the distinct package mechanic, a live war, no cooldown or reservation, and a non-host country scope.

`africa_natural_disaster_weapon_target_is_valid` is evaluated on the existing `event_target:africa_action_target` and requires a distinct country that is at war with the Event 012 host.

For a member-directed call, the selected target is at war with the priority member and carries the explicit roster validation flag. The target is never widened to a different country merely because the host is not a belligerent.

`africa_natural_disaster_weapon_cost_is_available` checks the additional political-power and command-power reserve and rejects a host-side cooldown or in-flight reservation. The member path uses `africa_natural_disaster_member_cost_is_available` so the caller reserve is paid by the member, while the host still pays the quoted Charter commitment.

`africa_reserve_natural_disaster_weapon_cost` runs before the shared action quote is paid and stores the reservation in `africa_active_action_natural_disaster_cost_reserved` on the existing action record.

`africa_begin_priority_member_natural_disaster_action` saves the member as `africa_natural_disaster_action_actor`, saves the selected enemy as `africa_action_target`, and invokes `africa_begin_quoted_action_against_target` on the current host. The host therefore owns one generation-safe action record and one mission, while the member owns its reservation, cooldown, and result receipt.

`africa_call_hostile_natural_disaster_from_action` runs only on a full result for action 69 or 70.

The helper saves the selected action target as `natural_disaster_call_target_country`, then calls the public Event 013 `call_natural_disaster = yes` wrapper in the exact selected-country scope.

The caller sets `natural_disaster_call_caller_type = hostile_actor`, Event ID 12, a random Event 013 family, random family group, selected-country mode, target-supplied proof, a single sequence, meaningful news, affected-country reporting, normal aftermath, family chaining, and Event 013 history logging.

Event 013 may reject the random family when the selected enemy has no eligible controlled state, so the selected-country target remains exact without silently widening to another country.

Severity is severe for `petition_the_rain`, regional for `defy_the_drought`, a fully promoted priority sovereign package, the documented warfare-doctrine path, or a package with more than low nature authority, and catastrophic for the covenant route capstone or a high/ancestral member package. The package ladder also adds bounded strength points, so stronger packages produce stronger Event 013 scales even when the host route is unchanged.

`africa_prepare_hostile_natural_disaster_strength` converts the live host route floor, reserved nature-call payment, drought action, member nature authority when present, ecological wrath bands, and continental war-readiness bands into actor strength, then adds a bounded selected-target factory/state adjustment so a major enemy is not normalised to the same impact envelope as a minor enemy.

The helper writes the Event 013 public scales before `call_natural_disaster = yes`: deaths increase by 0.20 per strength point above the base, building damage by 0.18, warning chance by 0.05, recovery burden by 0.15, and supply disruption by 0.20.

The warning increment is deliberate signal visibility rather than damage; higher-impact calls give the affected country a larger warning multiplier while deaths, damage, recovery burden, and supply disruption still rise with strength.

All five scales are clamped to Event 013's shared 0.25 to 4.00 range, so a stronger Africa actor produces a quantitatively stronger random disaster without changing Event 013's family pool, exact target, sequence policy, or rejection behavior.

The caller supplies all three hostile-actor proof inputs at one: `natural_disaster_call_caller_cost_checked`, `natural_disaster_call_caller_cooldown_checked`, and `natural_disaster_call_target_legitimacy_checked`.

## Outputs and cleanup

The host stores Event 013 result, reject reason, sequence ID, resolved family, primary job count, and skipped-primary count in `africa_last_natural_disaster_call_*` variables. A member-directed call copies those receipts and the final strength to the caller's existing package scope for its own dossier and AI readback.

The host also stores the attempted call's calculated strength in `africa_last_natural_disaster_call_strength`, including when Event 013 rejects the exact target because no eligible controlled state exists.

Accepted calls set `africa_natural_disaster_call_accepted`, mark the numeric resolved-primary-country target with `africa_natural_disaster_targeted`, and copy the current `africa_host_generation` onto that target. The same accepted result records the member-disaster disqualifier when the target is already a current-generation Charter member or cooperative partner, and records the neutral-African disqualifier when the target is an African sovereign with an outside relationship.

When the marked target later capitulates directly to the same Event 012 host generation, the `on_capitulation` owner calls `africa_achievement_record_weather_army_defeated` on that distinct target and opens the weather-war milestone through `africa_achievement_record_weather_war_won`. A host transfer, peace conference, or third-party victory cannot satisfy this owner.

The target receipt flags used by scripted localisation are cleared when a new Rain or Drought action record starts, so a later result cannot inherit an earlier call's wording.

Rejected calls set `africa_natural_disaster_call_rejected` and record a bounded wrath increase as a backfire.

Accepted calls have a 20 percent bounded backfire chance that records `africa_natural_disaster_backfire_recorded` and increases ecological wrath. After the host meter is clamped, reaching `africa_achievement_ratio.ecological_rampage_threshold` records `africa_achievement_ecological_wrath_collapse`, which is a lifetime disqualifier for the weather achievement.

Every attempted call starts the 180-day `africa_natural_disaster_weapon_cooldown` flag on the controller and, for a member-directed action, on the member caller as well.

The normal `africa_cleanup_action` path clears `africa_natural_disaster_weapon_reserved` on the controller and caller, clears `africa_natural_disaster_member_nature_action_active`, clears the two member global pointers, and retains the action ledger's existing target cooldown, arrays, state flags, generation checks, and capacity restoration.

No global Event 013 target or recurring world loop is introduced.

## Tuning and player-facing surfaces

`common/script_constants/012_africa_action_constants.txt` contains the `africa_natural_disaster` integer caller ledger and the `africa_natural_disaster_strength` fixed-point ladder for route floors, pressure/war bands, target-size thresholds, and the five Event 013 scale increments.

`localisation/english/012_african_union_l_english.yml` documents the hostile-war gate, extra ritual payment, cooldown, and backfire in the existing action descriptions and adds accepted/rejected call strings.

`common/scripted_localisation/012_africa_scripted_localisation.txt` selects those accepted/rejected strings from the target receipt flags while retaining the normal action result text when no hostile call was made.

The shared Event 012 action ledger icon and existing action decision surfaces remain the only UI assets; no new icon, sprite, GFX definition, tag, model, or entity is required.

The two host selector decisions are visible only for an eligible nature host that is at war. `africa_priority_member_refresh_natural_disaster_targets` and the two targeted priority-member decisions are visible only for an eligible completed package; the roster is refreshed explicitly and is not rebuilt by a recurring on_action. Resource, exact-target, and cooldown checks remain authoritative when the action starts.

## AI parity

`africa_ai_selected_target_is_candidate_for_action` has a dedicated branch for actions 69 and 70 that uses the same host eligibility, war, cost, cooldown, and exact enemy-target gate as human execution. Priority members use `africa_priority_member_natural_disaster_ai_cycle`, which refreshes the same bounded roster, selects a random target and one of the two actions, and calls the shared member wrapper.

The member AI cycle uses the same recorded authority ladder as the player tooltip and Event 013 strength bridge. Trace authority suppresses opportunistic use, low authority remains conservative, medium authority is neutral, high authority is more willing to spend the caller reserve, and ancestral authority is the strongest AI preference. This changes willingness only after the package, politics, mechanic, war, target, cost, cooldown, and host-generation gates already pass.

The decision page exposes that recorded ladder as a visible Trace, Low, Medium, High, or Ancestral label. The label is presentation-only and reads the package value written during registration. It does not create a second store, a new carrier tag, or an alternate severity calculation.

The generic bounded-roster fallback excludes both actions, so the AI cannot select a peaceful or non-nature target and rely on a weaker downstream failure.

## Limitations and follow-up

The implementation deliberately reuses actions 69 and 70 and does not reinterpret `weaponise_fictional_pathogen` (73) as a weather family because Event 013 has no pathogen family.

Partial and failed Event 012 action outcomes do not call Event 013; only a full action result consumes the reserved hostile nature payment.

The Event 013 wrapper and contract files are unchanged and remain the source of truth for family availability, target-state eligibility, scale bounds, sequence planning, result semantics, and report/news presentation.

The Event 012 `strange-force` actions remain outside this integration and retain their existing documented formation-consumer gap.

## Strength boundary

Disaster severity is earned through the existing promotion, constitutional, ecological, war-readiness, payment, and target-size receipts. It is never derived from ethnicity, a tribal label, or an unreviewed cultural stereotype. A promoted sovereign or covenant route can therefore deliver a stronger call because its documented political and ecological authority is higher, while every call still targets one selected enemy and remains bounded by the Event 013 contract.
