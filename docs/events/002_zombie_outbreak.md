# chaosx.nr2.1 Zombie Outbreak System

## Scope

This is the full documentation file for the zombie outbreak chain rooted at `chaosx.nr2.1`.

This is the canonical zombie doc. Zombie event-specific mechanics should live in `docs/events/` and be folded into this file instead of being split into separate top-level zombie docs.

It covers:

- the initial outbreak event
- all `chaosx.nr2.*` zombie subevents
- dynamic rear-area outbreaks
- zombie evolution and target-tier syncing
- Anti-Zombie League integration that is driven by the outbreak system
- main-horde succession after `ZZZ` capitulates
- outbreak shutdown after repeated zombie collapses
- isolated zombie capital relocation
- convoy-limited island evacuation requests
- special-country exclusions for zombies, dynamic zombies, and `ZIN`

`chaosx.nr2.9` is included here even though it is the fallout world-end branch, because it shares the same numeric event chain and interacts with the same super-event namespace.

## Main Files

Primary script and data files:

- `events/chaosx_events.txt`
- `common/on_actions/chaosx_on_actions.txt`
- `common/scripted_effects/chaosx_effects.txt`
- `common/scripted_triggers/chaosx_scripted_triggers.txt`
- `common/script_constants/zombie_constants.txt`
- `common/decisions/chaosx_anti_zombie_league_decisions.txt`
- `common/decisions/categories/chaosx_decisions_categories.txt`
- `common/ai_strategy/ZZZ.txt`
- `common/ai_strategy/anti_zombie_league.txt`
- `common/ai_templates/templates_ZZZ.txt`
- `common/ideas/chaosx_ideas.txt`
- `common/technology_sharing/chaosx_tech_sharing.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `interface/chaosx_super_events.gfx`
- `localisation/english/chaosx_events_l_english.yml`

Related non-zombie UI documentation:

- `docs/events_log_evolutions_and_clusters.md`

## Events Log Integration

The events-log UI now has dedicated zombie-chain detail content.

### Event details for event `2`

In the `Events` tab, opening event `2` now shows a gameplay-facing summary instead of generic placeholder text.

The written summary intentionally focuses on useful player information:

- where the main horde starts
- how zombie expansion behaves
- why rear-area outbreaks matter
- what zombie evolutions change in practice
- which player systems counter the outbreak
- how repeated main-horde defeats eventually shut the system down

### Clickable zombie evolution drill-down

Related zombie evolutions are now clickable from:

- the history-details overlay for zombie outbreak entries
- the event-details window for event `2`
- the `Evolutions` tab

Opening one of those entries shows:

- the logged evolution date
- the chaos tier that triggered the logged step
- the actor country
- the evolved zombie portrait in a bordered frame
- the exact modifier package for the logged evolution stage

Each listed zombie evolution stage now also has an event-log checkbox. It behaves like the `Events` tab toggle: disabling a stage blocks that future zombie evolution from firing, but does not erase already logged entries.

The underlying implementation is generic: scripts set `events_log_evolution_event_id`, `events_log_evolution_type`, and `events_log_evolution_stage`, then check `is_current_evolution_enabled = yes`. The zombie chain now uses that shared hook instead of stage-specific hardcoding.

No new art was required for this integration. The popup reuses the existing zombie leader portraits and `GFX_tiled_window_2b_border`.

## Event Map

The outbreak namespace currently uses these IDs:

- `chaosx.nr2.1`: hidden initial zombie outbreak bootstrap
- `chaosx.nr2.2`: cure activated event
- `chaosx.nr2.3`: player-facing zombie super-event trigger
- `chaosx.nr2.4`: zombie evolution step
- `chaosx.nr2.5`: zombie target-tier sync after chaos-tier growth
- `chaosx.nr2.6`: dynamic rear-area zombie outbreak
- `chaosx.nr2.7`: Anti-Zombie League formation invitation
- `chaosx.nr2.8`: zombie apocalypse world-end branch
- `chaosx.nr2.9`: fallout world-end branch in the same namespace
- `chaosx.nr2.10`: emergency island refugee convoy request
- `chaosx.nr2.11`: Wendigo ascendancy world-end branch
- `chaosx.nr2.12`: postwar survivor compact announcement
- `chaosx.nr2.13`: annual Day of the Buried memorial
- `chaosx.news.3`: news follow-up for dynamic rear outbreaks

`chaosx.nr2.10` is a zombie subevent in the same chain.

The zombie super-event slots currently used by this chain are:

- slot `1`: initial outbreak
- slot `3`: zombie apocalypse world-end
- slot `6`: Wendigo ascendancy world-end
- slot `5`: final zombie defeat after the last active zombie-held territory is erased

## Runtime Flow

### 1. Initial outbreak bootstrap: `chaosx.nr2.1`

`chaosx.nr2.1` is hidden and triggered by the wider chaos event system.

What it does:

1. Checks that the outbreak is not already active and that the system is not disabled.
2. Picks a random non-island, high-population state that is not already controlled by `ZZZ`.
3. The dormant `ZZZ` tag already carries one fixed `Zombie Horde` character in country history, with all four political roles attached to that same token so the game does not generate extra zombie politicians at startup.
4. Transfers the chosen state to `ZZZ`, adds a core, refreshes the zombie leader portrait, loads the zombie OOB, and spawns 20 `Brainzz Horde` divisions.
5. Gives `ZZZ` starting infantry equipment, three economy-law upgrades, the permanent zombie setup ideas (`never_ending_hunger`, `tot_economic_mobilisation`, `extensive_conscription`), and the current evolution idea `zombies_idea_0`.
6. Sets `zombie_target_tier` from the current global chaos tier.
7. Sets `zombie_current_tier = 0`.
8. Applies mutual `zombie_hostile` opinion modifiers between `ZZZ` and every non-zombie country.
9. Sets `has_zombie_outbreak`.
10. Clears `zombie_system_disabled`.
11. Initializes `global.zombie_main_capitulation_count = 0`.
12. Recomputes outbreak risk and cure research values worldwide.

This event is the only true root outbreak event. Everything else in the chain either reacts to it or expands it.

### 2. Daily zombie behavior: `on_daily`

The active zombie system is driven every day from `common/on_actions/chaosx_on_actions.txt`.

When the scope country is `ZZZ` and the outbreak is active:

- neighboring non-zombie countries are attacked immediately
- neighboring non-weaponized dynamic zombie outbreak countries are annexed into `ZZZ`
- subjects next to `ZZZ` are annexed instead of war-decled
- every occupied state is cored
- `relocate_isolated_zombie_capital = yes` runs
- `USA` is forced into the war in the Monroe Doctrine edge case

This preserves the intended design that `ZZZ` is the main outbreak center even when normal dynamic outbreaks splinter nearby. Weaponized outbreaks are excluded from this daily annex rule.

### 3. Evolution and target sync: `chaosx.nr2.4` and `chaosx.nr2.5`

#### `chaosx.nr2.4`: evolution

This hidden event fires for `ZZZ` and dynamic zombie countries while the outbreak is active.

It advances zombies one tier at a time:

- tier 0 -> 1 swaps `zombies_idea_0` to `zombies_idea_1`
- tier 1 -> 2 swaps `zombies_idea_1` to `zombies_idea_2`
- tier 2 -> 3 swaps `zombies_idea_2` to `zombies_idea_3`

Each evolution step also:

- updates `zombie_current_tier`
- swaps the portrait of the single `Zombie Horde` leader to the next zombie GFX
- writes an events-log evolution entry for `ZZZ`
- respects the matching evolution checkbox from the events-log UI before advancing

Dynamic zombie countries inherit the same tier state, and their leader sync now keeps one fixed `ZZZ_leader` character while updating its portrait to the current evolution tier instead of swapping between different character tokens. The log is intentionally kept on `ZZZ`.

#### `chaosx.nr2.5`: target-tier synchronization

This hidden event reacts to rising global chaos tiers. It only raises `zombie_target_tier`; it never lowers it.

Rules:

- chaos tier 1 raises target to 1
- chaos tier 2 raises target to 2
- chaos tiers 3 to 5 raise target to 3

That separation allows the outbreak to have:

- a target tier driven by world chaos
- a current tier that still needs time to evolve into that target

### 4. Dynamic rear outbreaks: `chaosx.nr2.6`

`chaosx.nr2.6` is the dynamic splinter-outbreak event. It is hidden and repeats while the system is active.

Base eligibility:

- `has_zombie_outbreak`
- not `zombie_system_disabled`
- no active global dynamic-outbreak cooldown
- `uses_normal_civilian_systems = yes`
- more than one controlled state
- at least one rear outbreak state
- no recent outbreak in that same country
- no `extreme_martial_law_active`

All of those checks now use controlled territory, not merely owned territory. Lost occupied land does not count toward outbreak exposure or state selection.

#### Country-level risk and selection logic

The per-country MTTH now drives both the risk display and the actual weekly zombie-side roll. `ZZZ` refreshes every country once per week, stores the best eligible outbreak time, and then uses that live value for the one allowed weekly outbreak roll. That means the system can only create one dynamic outbreak at a time, and the 7 day global cooldown now actually blocks follow-up outbreaks instead of just slowing later rolls.

It now depends on:

- zombie evolution tier
- hygiene, migration, quarantine, and border-closure decisions
- outbreak-prevention tech chain
- total manpower population bands
- research-slot count
- total factory count
- presence of medium-risk, high-risk, or extreme-risk rear states
- exposure tier:
  - direct zombie border
  - neighboring a country that has a zombie border
  - sharing a continent with zombie-held territory
  - or only the distant global background risk
- island-capital safety
- major-power status
- low total state count
- number of times the main zombie horde has collapsed
- a one-year country cooldown after a country has already suffered one

Weekly selection flow:

1. `ZZZ` runs a single dynamic-outbreak selection pass in weekly zombie logic.
2. The system first checks the 7 day global cooldown and whether any country can roll at all.
3. The weekly outbreak roll is now dynamic rather than a fixed phase table. It uses the best eligible country MTTH and turns that into a weekly chance, so faster-risk countries really do make the world more dangerous while safer countries no longer get treated as if they had the same outbreak pressure.
4. If the outbreak system rolls successfully that week, it builds a weighted country pool from the live `zombie_outbreak_days` values and picks from that pool.
5. Countries with lower MTTH get more entries in the pool, but very-safe countries can still stay in it with only a tiny number of entries instead of being hard-cut out by a bucket threshold.
6. Population, research capacity, factory count, and rear-state quality now separate countries more aggressively. A populous, underdeveloped giant such as China should sit much higher on the danger ladder than an advanced country like Germany unless Germany is far more exposed locally.

Design direction:

- direct proximity still matters, but country population and development now pull much harder on the final MTTH
- developed countries no longer end up near China-like risk levels just because they have one large city
- populous and lower-capacity countries now separate more clearly from advanced industrial countries
- outbreaks still prefer rear areas rather than obvious frontline tiles
- medium-risk countries near the front can still roll outbreaks later, but the truly dangerous outcomes are concentrated in the higher-risk rear areas first

#### State-level selection

The event does not pick a random state uniformly. It calls `select_dynamic_zombie_outbreak_state` and builds a weighted pool of all rear states.

Selection behavior:

1. every rear state gets at least a tiny base weight
2. medium-risk, high-risk, and extreme-risk rear states get progressively more weight
3. additional weight comes from dense urban categories, very large population, weak infrastructure, and weak local industry
4. advanced rear states are still possible, but only with very low weight compared to crowded, underdeveloped rear states

Rear state definition:

- the controlled state itself must not neighbor a zombie-controlled state

Risk escalation is driven by:

- high `state_population_k`
- low infrastructure
- low local industry
- dense urban state categories such as `city`, `large_city`, `metropolis`, and `megalopolis`
- but the higher tiers now require combinations of urban density plus poor infrastructure and-or poor industry, instead of treating any advanced city as automatically high risk
- the minimum population and development thresholds are now slightly lower again, so smaller rear states can qualify for low-level danger instead of being hard-blocked out of the system

#### Dynamic zombie country creation

When a rear outbreak fires:

1. A dynamic country copied from `ZZZ` is created.
2. The new tag is marked with `zombie_outbreak_dynamic_country` immediately.
3. The selected state is transferred, cored, and made the new capital.
4. Only after the country flag and capital exist, the `ZZZ_1936` OOB is loaded and `Brainzz Horde` is explicitly unlocked for recruitment.
5. The dynamic country receives zombie politics, zombie ideas, copied tier flags, and hostility opinions.
6. Ordinary dynamic splinters also receive `Fragmented Zombie Horde`, a dedicated debuff idea that keeps them significantly weaker than the main outbreak until one of them is promoted into the new `ZZZ`.
7. Starting zombie divisions are created from the outbreak-state scope with `owner = var:dynamic_zombie_new_country`, using the current main-zombie tier to choose strength.
8. The dynamic country keeps using the single fixed zombie leader copied from `ZZZ`, and its portrait is synced to the current evolution tier without generating a fresh leader.
9. `ZZZ` now also has a one-entry fallback name pool in `common/names/ZZZ_names.txt`, so if the engine does try to auto-generate a temporary zombie character during setup, that name resolves cleanly as `Zombie Horde`.
10. The source country gets a timed local cooldown and the whole world gets a 7 day global cooldown before another dynamic outbreak can fire.
11. `chaosx.news.3` fires as public narrative fallout.

#### Dynamic zombie template recruitment

The zombie battalion itself is inactive for normal template design use, so the outbreak system has to explicitly keep `Brainzz Horde` recruitable.

Both the initial outbreak and each dynamic splinter:

- load the zombie OOB/template
- reapply the country-wide division-template lock so zombie countries do not drift into non-zombie templates
- keep `Brainzz Horde` recruitable with `force_allow_recruiting = yes`
- keep `Brainzz Horde` template-locked as the single forced zombie template
- mark `Brainzz Horde` as an explicit `infantry` AI role with high template priority
- push strong AI role/template pressure toward that zombie infantry template and away from ordinary human training queues

Dynamic outbreak units are also spawned from the selected outbreak state with an explicit owner, rather than from an ambiguous post-creation country scope.

### 5. Capital relocation for stranded zombie capitals

Zombie capitals can get trapped on isolated island states that have no land neighbors.

The daily effect `relocate_isolated_zombie_capital` fixes that.

Rules:

1. If the current capital is an isolated island and the zombie country owns a mainland connected state, move the capital there.
2. If no mainland connected state exists but some other owned state has land neighbors, move the capital there instead.

This runs for zombie countries in the existing daily outbreak loop, so it does not need a separate world scan.

### 6. Anti-Zombie League integration: `chaosx.nr2.7` and weekly emergency logic

The outbreak system has direct League integration. The league is not a loose side mechanic anymore; it is a synchronized emergency coalition tied into outbreak pressure, cure sharing, and weekly zombie escalation checks.

Core goals of the current implementation:

1. Keep league membership logic centralized so higher investment tiers still count as real members everywhere.
2. Let the league form reliably even when the founder or joiner is already inside another faction.
3. Force a democratic major to create the league automatically once the zombie threat reaches continent-scale proportions.
4. Keep all current members synchronized to the same global investment tier so late joiners and absorbed factions do not get stuck on outdated bonuses.
5. Use the vanilla faction framework so the League has a manifest, faction rules, and faction goals in the diplomacy UI instead of being a plain custom faction shell.

#### `chaosx.nr2.7`

This event is the global invitation event once the league has formed.

It:

- excludes `ZZZ` and dynamic zombie countries
- excludes existing members and the leader
- calculates current combined zombie strength
- marks overwhelming-force cases for AI decision pressure

AI acceptance weighs:

- active war with zombies
- government ideology
- prevention decisions
- cure-sharing participation
- proximity to zombie fronts
- chaos tier
- major status
- lack of preparation
- island geography
- overwhelming global zombie strength

#### Manual formation

The standard formation path still comes from `common/decisions/chaosx_anti_zombie_league_decisions.txt`.

Current behavior:

- only eligible major non-zombie countries can see the formation decision
- the founder no longer has to pre-seed hygiene, quarantine, and cure-sharing manually
- formation now applies the preparation package automatically through shared scripted effects
- if the founder is already in another faction, it leaves first and then creates the league
- the league is now created from `faction_template_anti_zombie_league`, not a raw `create_faction`
- that template gives the league a live survival manifest, visible faction rules, and a dedicated goal track

This makes the manual path consistent with the emergency path instead of producing two different membership states.

#### Weekly emergency formation

The outbreak system can force league formation without player costs when:

- chaos is at least `constant:anti_zombie_league.emergency_chaos`
- zombie divisions exceed `constant:anti_zombie_league.emergency_divisions`
- zombie control reaches continent-scale thresholds
- no league already exists
- the system is not disabled

The founder must be a democratic major and is chosen in this order:

1. democratic majors already fighting zombies
2. democratic majors on the zombie front
3. democratic majors already in cure sharing
4. any remaining democratic major candidate

#### Joining and absorption

Joining now runs through the same shared preparation and membership-grant logic as formation.

Important results:

- countries that join immediately from `chaosx.nr2.7` now actually join immediately instead of only getting an activated decision
- if a joining country is already in another faction, it leaves that faction first
- if the zombie threat is still confined to the mainland Americas and holds no mainland outside them, countries outside the Americas become much less willing to join
- once the league exists and the zombie threat reaches strong emergency pressure, the zombie system now registers itself as a mod-wide world threat source
- when the league forcibly absorbs smaller factions, those absorbed countries also receive the full league preparation package
- absorbed countries are moved to the correct current league tier instead of being left on a stale member idea
- vanilla faction joining rules now also prevent zombie outbreak countries from being valid league members in the faction UI layer

#### Membership tiers and investment

Membership is now evaluated through shared scripted membership logic instead of scattered level checks.

Practical rules:

- every real member level from `0` through `17` counts as league membership everywhere
- league research investment is restricted to actual league members
- global investment maps cleanly to member levels `0` through `17`
- the broken `level_18` overflow path is gone
- every time investment changes, all current members are reapplied to the current global tier
- league membership only counts while a country is actually inside the Anti-Zombie League faction
- joining some other faction strips league membership, cure-sharing participation, and league-only doctrine benefits
- the member-tier idea itself no longer carries negative economic or research penalties
- visible faction-rule bonuses now add extra positive-only coordinated command and shared-lab modifiers on top of the hidden membership package

That keeps late joiners, emergency founders, and absorbed countries synchronized with the same bonuses.

#### Leaving and disbanding

The league leader can no longer use the normal leave decision. The leader must use the dedicated disband path.

Threat checks now:

- look at all zombie countries, including dynamic outbreaks, not just the main `ZZZ` tag
- use the same shared zombie-strength logic for leave and disband pressure

Disbanding also clears:

- current league investment
- stored league tier level
- league formation announcement state
- the stored league leader event target

#### Weekly forced consolidation

If the league already exists and zombie strength is extremely high, the leader can forcibly absorb smaller non-hostile factions into the league.

This gives the system a hard emergency response once zombies become too large for fragmented resistance to make sense.

#### Shared league helpers

The system now relies on reusable scripted helpers so the same rules are shared by decisions, events, AI, and forced faction absorption.

#### Faction-system layer

The template-backed Anti-Zombie League now exposes a proper vanilla faction package:

- Manifest:
  `faction_manifest_anti_zombie_global_survival`
  This tracks the share of world states still outside zombie control.
- Rules:
  `azl_joining_rule_human_survivors_only`
  `azl_member_rule_joint_operations`
  `azl_member_rule_shared_labs`
- Goals:
  `faction_goal_azl_secure_cure_exchange`
  `faction_goal_azl_fund_joint_labs`
  `faction_goal_azl_field_the_cure`

This means the League now has visible faction-level direction in the diplomacy screen:

- coordinated military planning against zombie offensives
- faster shared special-project work
- stronger research-sharing output
- explicit cure-network and cure-deployment goals

Important helpers:

- `is_anti_zombie_league_member`
- `can_lead_anti_zombie_league`
- `can_join_anti_zombie_league`
- `is_at_war_with_any_zombie_country`
- `prepare_anti_zombie_league_member`
- `grant_anti_zombie_league_membership_benefits`
- `establish_anti_zombie_league`
- `join_anti_zombie_league_effect`
- `calculate_zombie_continent_presence`
- `force_emergency_anti_zombie_league_formation`

#### League tuning

Shared league tuning lives in `common/script_constants/zombie_constants.txt` under `anti_zombie_league`.

Exposed values include:

- manual formation thresholds
- low-threat join reluctance thresholds
- emergency chaos and division thresholds
- continent-scale control thresholds for Europe, Africa, and Asia
- leave and disband pressure limits
- investment contribution values for majors and minors
- maximum investment cap used for tier synchronization

Current formation and join behavior:

- the League can be formed a bit earlier than before
- only countries that pass `uses_normal_civilian_systems = yes` can lead or join it
- if total live zombie strength is still below `650` divisions, AI countries are much less willing to join
- the one-time `chaosx.nr2.7` formation invitation now only goes to countries that are actually pressured by the threat, not to every technically eligible country on the map
- the faction joining rule itself now uses that same pressure gate, so countries cannot bypass the tuned invitation logic by silently joining through the faction-rule layer
- major democracies no longer get an automatic far-away early-entry carve-out; they still come in early when the threat is regional, continental, or truly global
- countries now evaluate proximity much more aggressively, so wars with zombies, direct borders, nearby fronts, and same-continent outbreak presence matter far more than before
- countries on other continents are now blocked from joining unless the outbreak has become a true global emergency
- same-continent countries without an actual front threat are only weakly inclined to join, so expansion should remain gradual instead of becoming instantly global
- countries with no meaningful regional zombie threat are now strongly biased toward delaying or refusing unless the outbreak has become a true global emergency
- if there is no live main `ZZZ` outbreak on the map, countries stop joining or rejoining the League and the alliance begins to decay through member exits instead
- countries that leave during that no-main-outbreak decay are now marked separately and do not cycle back into the League while the alliance shell still exists
- continent-level emergency pressure only counts Europe, Africa, and Asia
- Arabia / `middle_east` no longer counts as its own AZL continent pressure bucket
- the League can also be dismantled earlier once zombies are reduced to either:
  - fewer than `10` divisions total in practice, or
  - a situation where no Anti-Zombie League member still has a land border with any zombie country

That means large overseas zombie realms do not automatically keep the League alive on their own.
If zombies are stranded on islands or overseas landmasses and no AZL member actually borders them by land, the alliance can wind down.
If even one AZL member still directly borders zombie territory, the League stays relevant and should not fully disband yet.

When that distant-front state happens, the League no longer relies only on the leader's manual disband decision.
Instead, a weekly AZL review now asks current members whether they want to stay in the alliance:

- most countries leave
- major democracies are biased toward staying
- the leader is not asked to leave through this flow
- countries that leave through this distant-front review do not use the normal join decision anymore
- countries that leave because there is no live main outbreak also stop using the rejoin path entirely for that league instance

Those former members can be pulled back only by a renewed crisis.
If the main outbreak opens a fresh continental front and actually borders an AZL member on a continent it had not previously reached, former members receive a separate rejoin event and may return to the League through that event.

#### League assets

No new league-specific sprites are required by the current implementation.

The system reuses existing decision icons such as:

- `GFX_decision_generic_operation`
- `GFX_decision_generic_prepare_civil_war`
- `GFX_decision_generic_research`
- `GFX_decision_generic_nationalism`

### 7. Main horde collapse, succession, and shutdown

The main continuity logic sits in `on_capitulation`.

#### What happens when `ZZZ` capitulates

1. `ZZZ` removes its cores.
2. If the outbreak is active and not disabled, `global.zombie_main_capitulation_count` increases by 1.
3. The outbreak checks how long the current main-horde life lasted since the last main restoration.
4. Collapse `1` is only treated as survivable if it happened within `180` days of the outbreak appearing.
5. Collapse `2` is only treated as survivable if it happened within `90` days of the restored outbreak appearing.
6. Collapse `3` always shuts the system down.

This means the main zombie country can collapse multiple times without ending the mechanic outright, but only if those first two collapses were rapid suppressions of a freshly restored main horde.

When a surviving normal dynamic outbreak is chosen as the successor, `ZZZ` now inherits it through annexation. That means the main outbreak keeps the `ZZZ` tag while taking over the successor's owned territory, divisions, and capital, instead of manually transferring states first and risking partial handoffs.

#### Dormant main-horde recovery

If `ZZZ` has been wiped out and no splinter zombie country currently holds territory, the next successful rear-outbreak roll does not create a splinter tag.

Instead, the selected outbreak state is transferred straight back to `ZZZ`, which:

- regains a capital
- reapplies the permanent zombie setup ideas if needed
- reloads the `Brainzz Horde` template if needed
- spawns its starter zombie divisions from the recovered state
- resumes acting as the main outbreak country

That fallback matters until the shutdown limit is reached. If the main horde is wiped out early, later rear-outbreak rolls can still restore `ZZZ` so the crisis continues.

#### Outbreak slowdown after each main collapse

Before shutdown, both the actual MTTH and the displayed outbreak-risk calculation can still react to `global.zombie_main_capitulation_count`.
The count now directly governs continuity:

- collapse `1`: system remains active only if it happened within `180` days
- collapse `2`: system remains active only if it happened within `90` days
- collapse `3`: `disable_zombie_outbreak_system` fires

### 7.1 Prevention-decision AI gating

The prevention-decision AI now uses the same displayed no-risk threshold as the outbreak-risk UI.

Practical rule:

- if a country shows `No Risk`, AI will not spend political power on the outbreak-prevention decisions
- AI also refuses those decisions for countries that cannot currently roll a dynamic outbreak at all

This keeps AI spending aligned with the actual rear-outbreak system instead of reacting to the mere global existence of zombies.

### 8. Global shutdown behavior

`disable_zombie_outbreak_system` is the hard stop for the outbreak mechanic.

It:

- clears `has_zombie_outbreak`
- sets `zombie_system_disabled`
- sets every country to `No Risk` through `set_zombie_outbreak_no_risk`

Practical results:

- spontaneous outbreak propagation stops
- outbreak-risk displays are forced to no-risk values
- zombie AI setup that checks `zombie_system_disabled` no longer behaves like an active outbreak system

The zombie countries themselves are not force-deleted here. The system is disabled; it is not retroactively rewritten into a different scenario.

Shutdown also clears the zombie world-threat source, which lets the shared `world_in_threat` framework fall back to any other active existential threats rather than leaving the zombie source stuck on.

While the outbreak system is active, zombie-controlled states now also decay over time:

- every `30` days they lose `0.5%` population for up to `36` monthly ticks per state
- every `180` days they attempt one structural degradation pass, removing one productive building and degrading the state category by one step only if the state is already `rural` or lower

Those losses are handled through the shared chaos-meter deaths pipeline rather than a separate zombie-only casualty tracker.

### 8.1 Final zombie defeat after shutdown

Shutdown is not the same thing as total victory.

After the system has already been shut down, the chain now watches zombie capitulations for a second endpoint:

- no zombie outbreak country may still control any state
- `zombie_threat_defeated` must not already be set

When that happens, `on_zombie_threat_defeated`:

- sets `zombie_threat_defeated`
- shows super-event slot `5`
- reduces the global chaos meter by `constant:zombie_threat.defeat_chaos_reduction`
- writes a chaos-history entry for the zombie threat being eradicated
- snapshots the campaign's peak zombie strength and recorded dead
- can activate a permanent postwar survivor order if the zombie war was large and costly enough

If `ZZZ` itself is the last zombie polity on the map when it capitulates, this final defeat condition is met immediately and the super event fires on that same collapse.

If the Anti-Zombie League still exists at that point, it is dismantled automatically through the same shared teardown used by the manual disband decision:

- the faction is broken up
- membership ideas and doctrine are removed
- `cure_sharing` is cleaned up
- the AZL leader/event-target bookkeeping is cleared
- the zombie world-threat source is refreshed back to its post-defeat state

### 8.2 Postwar survivor order: `chaosx.nr2.12` and `chaosx.nr2.13`

If the zombie campaign lasted long enough and cost enough lives, the defeat flow now creates a lasting postwar settlement rather than ending as a pure cleanup.

Current activation thresholds:

- peak zombie strength reached at least `200` divisions
- the campaign lasted at least `365` days
- recorded zombie-side war dead plus recorded civilian deaths under zombie occupation reached at least `250000`

When that happens:

- `zombie_postwar_order_active` is set
- all normal non-zombie countries gain `zombie_postwar_global_vigilance`
- those same countries join the `zombie_postwar_research_compact` tech-sharing group for engineering, construction, electronics, and biowarfare work
- every country marked with `was_ever_at_war_with_zombies` receives `chaosx.nr2.12`

`chaosx.nr2.12` announces the survivor compact and shows the recorded zombie-war dead.

`chaosx.nr2.13` is the annual remembrance event. It repeats every `365` days for countries that were ever at war with zombies and grants `10` political power each year.

### 9. World-end branches: `chaosx.nr2.8`, `chaosx.nr2.9`, and `chaosx.nr2.11`

#### `chaosx.nr2.8`: zombie apocalypse

This hidden fire-once event represents the outbreak winning the wider scenario.

Requirements:

- zombie outbreak active
- chaos tier 5
- no other `world_end`
- system not disabled
- `ZZZ` has more than 300 divisions

Effects:

- plays zombie music
- shows super-event slot `3`
- sets `world_end`
- sets `world_end_zombies`
- if `ZZZ` has no neighboring normal countries when the world-end branch fires, it immediately creates coastal breakout beachheads

Current coastal breakout tuning:

- only active for `world_end_zombies`
- only used when `ZZZ` has no neighboring country that uses normal civilian systems
- picks `3` random coastal states that are not one-state islands and are still held by normal countries
- transfers those states to `ZZZ`
- spawns `24` `Brainzz Horde` divisions in each breakout state

#### `chaosx.nr2.9`: fallout

This is the air-contamination collapse world-end event in the same namespace. It is not a zombie outbreak event, but it shares the same super-event numbering block and therefore belongs in this namespace-level documentation.

#### `chaosx.nr2.11`: Wendigo ascendancy

This hidden repeatable-check event handles the weaponized Wendigo end-state.

Requirements:

- chaos tier 5
- no `world_end`
- world-end system not disabled
- zombie system not disabled
- the scoped country is a weaponized Wendigo outbreak country

Runtime check:

- the event recalculates continent control on the outbreak country itself
- a continent qualifies when the Wendigo controls at least `85%` of its states and is missing no more than `3`
- the first qualifying continent marks the country as `wendigo_world_end_ready`

Effects when ready:

- sets `world_end`
- sets `world_end_wendigo`
- grants `weaponized_zombie_wendigo_world_end`
- shows super-event slot `6`

### 10. Refugee evacuation subevent: `chaosx.nr2.10`

This is the zombie-chain refugee request event. It is not a separate root event.

#### Weekly request generation

Every week, any country that meets `can_request_zombie_evacuation` will attempt the system.

Source-country requirements:

- uses normal civilian systems
- not capitulated
- not already pending evacuation
- not on evacuation cooldown
- at war with a zombie country
- surrender progress above `constant:zombie_evacuation.source_surrender_threshold`
- at least one controlled state
- at least one convoy
- at least one controlled state with population

#### Evacuation amount

`calculate_zombie_evacuation_request` computes:

- total population pool from all controlled states
- available convoys through `num_equipment@convoy`
- `zombie_evacuation_population_to_move = convoys * people_per_convoy`
- cap at the actual remaining controlled population

Current tuning is `10000` civilians per convoy.

#### Host-country selection

`select_zombie_evacuation_host_country` uses a strict scriptable priority, not exact geometric distance.

Selection order:

1. direct neighboring island host
2. same home-area island host
3. island faction partner
4. any valid island host

Host requirements:

- uses normal civilian systems
- exists
- not capitulated
- surrender progress below `constant:zombie_evacuation.host_surrender_threshold`
- capital state is an island and still controlled by that host

This is a deliberate heuristic. HOI4 script does not expose a reliable "nearest island country by real distance" sort for this mechanic.

#### Host event behavior

If a host is found, the source country gets `zombie_evacuation_request_pending` and the host receives `chaosx.nr2.10`.

The host can:

- refuse
- accept

Timeout behavior:

- the event times out after `constant:zombie_evacuation.event_timeout_days`
- refusal is the default timeout outcome

#### Population transfer

On acceptance, `apply_zombie_evacuation_transfer`:

1. recalculates the request size
2. removes population proportionally from every currently controlled source state
3. tracks the amount actually removed
4. adds that total to the host capital state
5. clears the pending flag
6. applies the retry cooldown
7. clears stored request variables

Implementation note:

- HOI4 has no direct civilian-population migration resource
- this mechanic uses state manpower as the population carrier

That is an abstraction, not a literal refugee-pop model.

## Special-Country Exclusions

The zombie system now explicitly distinguishes between normal countries and special/system countries.

Shared triggers:

- `is_zombie_outbreak_country`
- `is_special_chaos_country`
- `uses_normal_civilian_systems`

Special countries currently covered:

- `ZZZ`
- all dynamic zombie countries with `zombie_outbreak_dynamic_country`
- `ZIN`
- `THR` / countries using the Holy Realm cosmetic tag

Practical effect:

- outbreak risk display and dynamic outbreaks skip them
- mass panic is cleaned off them
- normal civilian and political logic is prevented from treating them like standard countries
- evacuation requests and refugee hosting also skip them

This keeps nonstandard scenario actors out of mechanics that only make sense for normal societies.

## Flags, Variables, and Event Targets

### Global flags

- `has_zombie_outbreak`
- `zombie_system_disabled`
- `world_end`
- `world_end_zombies`
- `anti_zombie_league_formed`
- `azl_formation_announced`
- `azl_dissolved`
- `super_event_visible`
- `zombie_threat_defeated`
- `zombie_postwar_order_active`

### Global variables

- `global.zombie_main_capitulation_count`
- `global.zombie_peak_divisions`
- `global.zombie_peak_controlled_states`
- `global.zombie_campaign_start_day`
- `global.zombie_campaign_duration_days`
- `global.zombie_campaign_zombie_dead`
- `global.zombie_campaign_civilian_dead`
- `global.zombie_campaign_total_dead`
- `global.chaos_meter_value`
- `global.azl_global_investment`
- `global.target_level`

### Zombie country flags

- `zombie_current_tier`
- `zombie_target_tier`
- `zombie_outbreak_dynamic_country`
- `was_ever_at_war_with_zombies`

### Evacuation flags and variables

- `zombie_evacuation_request_pending`
- `zombie_evacuation_cooldown`
- `zombie_evacuation_convoys`
- `zombie_evacuation_population_pool`
- `zombie_evacuation_population_to_move`

### Frequently used event targets

- `zombie_state`: initial outbreak state in `chaosx.nr2.1`
- `outbreak_state`: dynamic outbreak state in `chaosx.nr2.6`
- `refugee_host_country`: selected evacuation host
- `refugee_source_country`: requesting source country
- `events_log_evolution_actor`: canonical actor for zombie evolution logging

## Script Constants

Shared tuning lives in `common/script_constants/zombie_constants.txt`.

### `zombie_outbreak`

Controls:

- base outbreak MTTH
- prevention-decision multipliers
- population thresholds
- research-slot and factory thresholds
- rear-state risk thresholds
- frontline proximity weight
- island safety
- post-collapse slowdown
- no-risk sentinel values for display
- the shared displayed no-risk threshold used by both UI and AI prevention logic

### `zombie_threat`

Controls:

- very-high zombie division threshold
- very-high zombie controlled-state threshold
- main-collapse shutdown count
- final zombie-defeat chaos reduction

### `zombie_postwar`

Controls:

- postwar-order activation thresholds
- memorial timing and annual political-power reward
- the permanent outbreak-risk slowdown from the survivor-vigilance idea

### `anti_zombie_league`

Controls:

- formation thresholds
- emergency auto-formation thresholds
- continent-pressure thresholds
- leave and disband pressure limits
- investment scaling

### `zombie_evacuation`

Controls:

- source surrender threshold
- host surrender threshold
- people moved per convoy
- retry cooldown
- event timeout

## UI, Art, and Localisation

### Super-event image mapping

Mapped in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`:

- slot `1`: zombie outbreak
- slot `3`: zombie apocalypse world-end
- slot `5`: final zombie defeat

Sprite definitions live in `interface/chaosx_super_events.gfx`.

### Required and reused assets

Required zombie final-defeat asset:

- file: `gfx/super_events/super_event_zombie_defeat.dds`
- sprite: `GFX_super_event_zombie_defeat`
- wired in: `interface/chaosx_super_events.gfx`

Existing outbreak-related assets already used by the system:

- `gfx/super_events/super_event_zombies.dds`
- `gfx/super_events/super_event_zombie_apocalypse.dds`
- `GFX_news_zombie_outbreak`
- `GFX_report_event_generic_research_lab`
- `GFX_report_event_generic_sign_treaty2`
- `GFX_report_event_merchant_ship_01`

`chaosx.nr2.10` reuses `GFX_report_event_merchant_ship_01`; it does not require new event art.
`chaosx.nr2.12` and `chaosx.nr2.13` reuse `GFX_report_event_generic_research_lab`; the postwar compact and memorial flow does not require new art or icons.

## Design Constraints and Known Heuristics

These are intentional implementation choices, not oversights:

- "Nearest island host" is a priority heuristic, not a true distance sort.
- Population migration uses state manpower because HOI4 does not provide a separate dynamic civilian-population transfer resource.
- Rear-area outbreak selection now uses a weighted rear-state pool instead of a strict risk-tier fallback, so unusual but plausible outbreaks can still happen without letting advanced states dominate the system.
- The system still uses `ZZZ` as the canonical main outbreak tag. Successors are folded back into `ZZZ` instead of replacing the root tag globally.

## Testing Notes

Important live behaviors to verify in-game after changes to this system:

1. `chaosx.nr2.1` still seeds `ZZZ` correctly.
2. `chaosx.nr2.6` still prefers dense rear states and does not spawn directly on the zombie frontline.
3. Dynamic zombie countries can keep using the zombie AI division template path after the first outbreak wave.
4. Manual and emergency Anti-Zombie League formation produce the same membership state and synchronized tier bonuses.
5. Immediate joiners from `chaosx.nr2.7` actually enter the league and do not remain half-prepared.
6. `ZZZ` succession after capitulation transfers troops and states cleanly.
7. After three main-horde collapses, outbreak risk becomes zero everywhere and no new outbreak propagation occurs.
8. Once the last active zombie-held territory is removed after shutdown, super-event slot `5` fires exactly once and chaos drops.
9. `chaosx.nr2.10` times out to refusal and only fires for valid island hosts.
10. Special countries never receive mass-panic or normal-civilian zombie-risk handling.

## Future Work

- Replace the current rear-state priority ladder with a more expressive scoring system if the script architecture later supports it cleanly.
- Add player-facing reporting for forced Anti-Zombie League faction absorption if that mechanic needs more visibility.
- Add a dedicated league reorganization event if emergency auto-formation needs more narrative visibility than the current decision-event flow.
- Consider a proper replacement-leader path for the league if the founder collapses without formally disbanding it.
- Replace the continent-state thresholds with a weighted territorial-pressure score if the zombie front needs finer regional behavior.
- Expand evacuation destinations beyond capital-only concentration if a better state-targeting model is later introduced.
- Consider a true persistent "current main zombie controller" scope if the system ever needs to stop hard-centering on `ZZZ`.
