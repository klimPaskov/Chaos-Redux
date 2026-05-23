# Event 005 Custom Splinter Focus Reward Improvement Handoff

## Current Depth Status

The custom-splinter focus file is source-valid and already contains stronger bespoke late branches for several tags. The main 2026-05-23 implementation pass has addressed the worst `*_first_guard`, `*_special_arm`, `*_settlement`, `*_industry_plan`, and `*_propaganda` clusters, plus the adjacent `*_stores`, `*_legitimacy`, `*_rival`, `*_civil_rule`, `*_enemy_front`, `*_league`, and `*_foreign` clusters, with tag-family helper effects hidden behind one concise route-identity tooltip. `KRS_industry_plan` remains bespoke and carries the shared recovery-progress and consolidated-idea refresh tail directly.

This is not a request to rewrite the trees. The next implementation pass should focus on bespoke late-branch AI weighting, live tooltip readability, and any remaining tag-specific late-branch gaps rather than reworking the already-patched helper surface.

## Evidence From Current Source

Inspected file: `common/national_focus/005_soviet_collapse_custom_splinters.txt`.

Parser pass found 1,005 focus blocks across 25 uppercase custom-splinter tags, plus three lowercase `mrc_*` focus ids that should be reviewed during validation. The five target clusters repeat across the same 19 broad custom successor trees:

| Cluster | Count | Current common payoff pattern | Main issue |
| --- | ---: | --- | --- |
| `*_first_guard` | 19 | `militia_manpower` plus medium infantry equipment | Every first armed force feels like the same rifle levy. |
| `*_special_arm` | 19 | `front_manpower` plus large infantry equipment | Signature arms are not signature; cavalry, sailors, internal troops, pass guards, columns, and port guards all behave alike. |
| `*_settlement` | 19 | medium stability plus large recognition gain | Settlement choices do not show what the regime actually settles: ports, communes, passes, archives, grain routes, or councils. |
| `*_industry_plan` | 19 | one random arms factory, usually with one slot | Industry identity collapses into the same factory reward. |
| `*_propaganda` | 19 | small political power | Broadcasts, assemblies, oath rolls, court registers, and manifesto networks do not change pressure, recruitment, diplomacy, or decisions. |

Adjacent repeated clusters should be considered while the file is open:

| Cluster | Count | Current repeated payoff |
| --- | ---: | --- |
| `*_stores` | 19 | support equipment plus one infrastructure |
| `*_legitimacy` | 19 | small stability plus small recognition |
| `*_rival` | 19 | small war support plus small Soviet old-movement pressure |
| `*_civil_rule` | 19 | medium stability |
| `*_enemy_front` | 19 | medium war support plus army XP |
| `*_league` / `*_foreign` | 19 each | medium recognition or small foreign appetite pressure |

Existing helper surface already available:

- `soviet_collapse_apply_focus_legal_recognition`
- `soviet_collapse_apply_focus_military_consolidation`
- `soviet_collapse_apply_focus_depot_and_supply_control`
- `soviet_collapse_apply_focus_league_preparation`
- `soviet_collapse_apply_focus_foreign_channel`
- `soviet_collapse_apply_focus_high_chaos_identity`
- Endgame helpers for the major custom splinter identities
- Cost triggers for custom splinter decisions: `can_pay_soviet_collapse_custom_splinter_low_cost` and `can_pay_soviet_collapse_custom_splinter_medium_cost`

Existing docs already mark focus reward variety as partial: `docs/events/005_soviet_collapse_full_implementation_ledger.md` says broad `*_settlement`, `*_industry_plan`, and `*_propaganda` clusters remain the next focus-quality surface.

## Core Expansion Thesis

Keep the shared tree architecture, but make each repeated scaffold focus express one of five concrete gameplay roles:

- armed identity: what kind of force the tag can field
- production identity: what map assets, routes, or resource networks the tag depends on
- political settlement: what social bargain keeps the regime from collapsing
- propaganda channel: who the tag speaks to and what pressure it creates
- decision unlock: what repeatable action becomes available after the focus

Flat manpower, factories, political power, stability, and recognition can remain as supporting rewards, but no cluster should end with only those flat rewards.

## Accepted Design Constraints

- Do not edit focus files, scripted effects, localisation, interface, assets, or existing docs in this subagent pass.
- Do not touch `common/scripted_effects`; the main agent is concurrently patching military reward helpers.
- Avoid new whole-world on actions. All proposed logic should live in focus rewards, existing decisions, existing helper effects, or narrow targeted decisions.
- Use script constants for shared tuning if the implementation adds repeated new values.
- Preserve current focus ids, route shape, and prerequisites unless the main agent explicitly expands scope.
- Prefer existing helpers first; add new helpers only where repeated tag-family logic would otherwise create large copy-paste blocks.

## Top Duplicated Clusters And Replacement Direction

### 1. `*_first_guard`

Current reward gives the same militia manpower and infantry equipment to 19 different regimes. Replace with first-force packages:

| Tag family | Tags | Replacement package |
| --- | --- | --- |
| Steppe, oasis, and Central Asian insurgent states | `BSC`, `TNC`, `ALA` | Smaller infantry grant, cavalry or motorized equipment where available, command power, and `soviet_collapse_apply_focus_military_consolidation`. Add a pass/caravan state improvement: infrastructure or land fort in owned mountain/desert/pass states where possible. |
| Black-banner and commune mobile states | `FTH`, `BBH` | Manpower plus motorized equipment or command power, not only rifles. Add a hidden flag such as `<tag>_column_force_ready` for later column/sabotage decisions. Increase old-movement pressure slightly for radical identities. |
| Port, naval, and arctic corridor states | `KRS`, `ARD`, `NLC` | Port guard package: infantry/support equipment, coastal fort or anti-air in a coastal owned state where valid, small navy/air XP if thematically appropriate, and depot/supply helper. |
| Command, archive, and security directorates | `UDC`, `SDZ` | Lower manpower, higher command power or army XP, support equipment, and a temporary/hidden readiness flag for command-network decisions. Avoid presenting them as mass militias. |
| Agrarian, Cossack, mountain, and rural defense states | `GAC`, `DHC`, `KHC`, `MRC` | Militia manpower plus terrain defense: land fort/infrastructure in rural, mountain, or river-adjacent owned state, and local authority pressure or league support depending on settlement tone. |
| Siberian, Far Eastern, Ural, Idel-Ural, Birobidzhan | `FEV`, `SZA`, `UWD`, `IUL`, `BAC` | Rail/worker guard package: smaller manpower, trains or support equipment, one rail/infrastructure improvement, and depot-control helper. |

### 2. `*_special_arm`

Current reward is `front_manpower` plus large infantry equipment. Replace with signature arms:

| Tags | Specific replacement |
| --- | --- |
| `BSC`, `TNC`, `ALA` | Pass and cavalry columns: add command power, motorized equipment or cavalry-themed equipment support, one land fort/infrastructure in border/pass state, plus military consolidation. |
| `FTH`, `BBH` | Mobile columns: motorized equipment, army XP, command power, and a decision unlock for raids or prisoner/registry actions. Avoid only adding larger infantry stockpiles. |
| `KRS` | Naval infantry and fortress signal rooms: support equipment, coastal bunker/anti-air, army/navy XP, and depot/supply helper. |
| `ARD`, `NLC` | Arctic watch or ice-road forces: support equipment, trains, winter logistics flavor through infrastructure/air base/anti-air in northern/coastal states. |
| `UDC`, `SDZ` | Signal/internal troop branch: command power, support equipment, maybe armoured-car/motorized equipment, and a command-network flag consumed by later decisions. |
| `GAC`, `DHC`, `KHC`, `MRC` | Rural guard, stanitsa hosts, mountain pass troops: manpower plus state fortification and local-authority/league variable movement. |
| `FEV`, `SZA`, `UWD`, `IUL`, `BAC` | Rail, factory, federal, or archive guards: trains/support equipment, factory/supply helper, and tag-specific resource or route flags. |

### 3. `*_settlement`

Current reward is medium stability plus large recognition. Replace with settlement consequences:

| Tags | Settlement should do |
| --- | --- |
| `BSC`, `TNC`, `ALA` | Create an oasis/steppe compact: stability, league support, recognition, and reduced foreign dependency risk if no dominant patron exists. Unlock or improve regional-league decisions for Central Asian cooperation. |
| `FTH`, `BBH` | Create anti-domination pacts: stability should be paired with old-movement pressure or no-protector flags. Settlement is not normal recognition; it should reject permanent protectorates and improve local authority. |
| `KRS`, `ARD`, `NLC` | Create port/free-corridor statutes: recognition, foreign-channel access, coastal/port defenses or dockyard/convoy support, and better League logistics eligibility. |
| `UDC`, `SDZ` | Create command/chain-of-custody statutes: stability, command power, legal recognition helper, and an internal purge/inspection decision unlock. |
| `GAC`, `DHC`, `KHC`, `MRC` | Create village, stanitsa, grain, or mountain-pass settlements: stability, local authority, reduced local resistance pressure, and state infrastructure or supply-node work. |
| `FEV`, `SZA`, `UWD`, `IUL`, `BAC` | Create city-federation/worker/council settlements: recognition, factory/supply helper, and decision access for city congresses, rail corridors, or workshop compacts. |

Implementation rule: the settlement focus must set a visible route flag that at least one later decision, AI weight, or follow-up focus can check. Otherwise it remains a flat payoff.

### 4. `*_industry_plan`

Current reward is nearly always one random arms factory. Replace with geography and production identity:

| Tags | Industry identity |
| --- | --- |
| `BSC`, `TNC`, `ALA` | Caravan roads, irrigation, and pass workshops: infrastructure, supply node or rail where possible, support equipment, and depot-control helper. |
| `FTH`, `BBH` | Portable arsenals and hidden workshops: smaller arms reward, motorized/support equipment, and a raid/workshop decision unlock rather than fixed factory spam. |
| `KRS`, `ARD`, `NLC` | Ports, dockyards, airstrips, ice roads: dockyard/coastal state branch where valid, anti-air/air base, trains/convoys, and foreign-channel/depot helper. |
| `UDC`, `SDZ` | Staff cars, signal vans, archive depots: support equipment, motorized equipment, infrastructure or supply node, and command-network variables. |
| `GAC`, `DHC`, `KHC`, `MRC` | Grain depots, river ports, mountain workshops: industrial complex only when tied to agricultural/river/mountain state improvements; otherwise use infrastructure/supply/forts. |
| `FEV`, `SZA`, `UWD`, `IUL`, `BAC` | Far Eastern ports, Siberian rail towns, Ural steel, Kazan-Ufa workshops, Birobidzhan archives: rail/infrastructure, industrial complex or arms factory where tag-specific, and a route variable/flag. |

### 5. `*_propaganda`

Current reward is small political power. Replace with audience-specific pressure:

| Tags | Propaganda effect |
| --- | --- |
| `BSC`, `TNC`, `ALA` | Steppe/oasis legitimacy: recognition, local authority, and Central Asian league support. Add a small Soviet old-movement pressure only for explicitly insurgent or anti-Moscow lines. |
| `FTH`, `BBH` | Anti-capital manifesto network: old-movement pressure, local authority, and possible volunteer/raid decision availability; political power is secondary. |
| `KRS` | Sailor-worker broadcasts: recognition plus league support, and maybe foreign-channel access if coastal observers exist. |
| `ARD`, `NLC` | Weather/port survival bulletins: recognition, foreign-channel access, and logistics/relief decision modifier. |
| `UDC`, `SDZ` | Order, archives, witness protection: stability/command power and legal recognition; do not use generic mass-propaganda PP. |
| `GAC`, `DHC`, `KHC`, `MRC` | Village, grain, stanitsa, or mountain oath networks: local authority, manpower if appropriate, and lower dependency on foreign aid. |
| `FEV`, `SZA`, `UWD`, `IUL`, `BAC` | City congress, worker ledger, minority council, or federal broadcast: recognition, league preparation, and tag-family congress/relief decisions. |

## Specific Replacement Mechanics By Tag Family

### Central Asian / Steppe Set: `BSC`, `TNC`, `ALA`

Immediate replacements:

- `first_guard`: cavalry/pass guard package with small manpower, infantry equipment, command power, and infrastructure/land fort in mountain/desert/pass state if valid.
- `special_arm`: unlock a targeted raid/escort decision family or set a flag consumed by existing custom-splinter decisions.
- `industry_plan`: caravan/irrigation logistics, not arms factory by default.
- `settlement`: oasis/steppe compact with league support and recognition.
- `propaganda`: language, madrasah, aksakal, or kurultai messaging that moves local authority and recognition.

Suggested helper:

- `soviet_collapse_apply_focus_steppe_pass_network = yes`
  - Inputs: ROOT only.
  - Effects: infrastructure or fort in valid owned mountain/desert/pass states, small command power, depot-control helper.
  - Use in `BSC`, `TNC`, `ALA`, and potentially `MRC`.

### Commune / Black Banner Set: `FTH`, `BBH`

Immediate replacements:

- `first_guard` and `special_arm`: mobile column package with motorized equipment, command power, and old-movement pressure. Keep manpower lower than the generic front package to avoid free-army inflation.
- `propaganda`: old-movement pressure plus local authority, not PP.
- `settlement`: anti-protectorate or no-masters clause; recognition should be conditional or paired with refusal of permanent patrons.
- `industry_plan`: portable arsenals/hidden workshops with support equipment and raid decision unlocks.

Suggested decision unlocks:

- `soviet_collapse_raid_state_depots`
- `soviet_collapse_break_prison_or_registry_network`
- `soviet_collapse_sign_non_domination_pact`

These can reuse custom-splinter low/medium cost triggers and should be hidden unless the matching focus flag is set.

### Port / Naval / Arctic Corridor Set: `KRS`, `ARD`, `NLC`

Immediate replacements:

- `first_guard`: port guard, coastal fort, anti-air, support equipment.
- `special_arm`: naval infantry or ice-watch forces: army/navy/air XP depending on tag, plus local coastal or airbase defense.
- `industry_plan`: dockyard or port logistics where coastal state exists; for `NLC`, use airbase, anti-air, infrastructure, or supply instead of dockyard if geography is not coastal.
- `settlement`: free-port, convoy, or polar neutrality statute with foreign-channel/league logistics support.
- `propaganda`: observer bulletins and survival reports that improve recognition and foreign-channel access.

Suggested helper:

- `soviet_collapse_apply_focus_port_or_ice_corridor = yes`
  - Select coastal owned controlled state for dockyard/coastal defense when valid.
  - Else select northern/owned controlled state for airbase, anti-air, infrastructure.
  - Apply depot/supply or foreign-channel helper depending on focus.

### Command / Archive / Security Set: `UDC`, `SDZ`

Immediate replacements:

- `first_guard`: command staff and internal guard readiness: support equipment, command power, army XP.
- `special_arm`: signal trucks/vans, witness protection, custody convoy flags; use motorized/support equipment rather than manpower.
- `propaganda`: authority broadcast or chain-of-custody proof: legal recognition, command power, small stability.
- `settlement`: statute/inspection settlement that unlocks cleanup or internal inspection decisions.
- `industry_plan`: signal depots and document transport workshops, with infrastructure/supply and small motorized equipment.

Suggested helper:

- `soviet_collapse_apply_focus_command_network = yes`
  - Adds command power and support/motorized equipment.
  - Adds institution strength and legal recognition.
  - Sets a tag-local flag for command-network decisions.

### Agrarian / Cossack / Mountain Set: `GAC`, `DHC`, `KHC`, `MRC`

Immediate replacements:

- `first_guard`: village/stanitsa/mountain guard package with state fortification, manpower, and local authority.
- `special_arm`: river, steppe, or mountain force: fort/infrastructure, army XP, smaller equipment.
- `industry_plan`: grain stores, river-port tolls, blacksmith carts, pass workshops; avoid arms-factory-only rewards.
- `settlement`: autonomy, village mediation, grain passage, or pass league compact with local authority and League support.
- `propaganda`: oath boards and village congresses that alter local authority and manpower instead of PP only.

Suggested helper:

- `soviet_collapse_apply_focus_local_settlement_compact = yes`
  - Adds local authority, stability, and either league support or recognition.
  - For Cossack tags, can add small war support; for `MRC`, can add mountain-pass defense.

### Siberian / Far Eastern / Ural / Idel-Ural / Birobidzhan Set: `FEV`, `SZA`, `UWD`, `IUL`, `BAC`

Immediate replacements:

- `first_guard`: rail/worker/federal guard with trains/support equipment and infrastructure, not generic militia only.
- `special_arm`: factory guards, city militias, signal lines, or archive security with command power and supply.
- `industry_plan`: state-specific production identity: `UWD` steel/workshops, `IUL` Kazan-Ufa workshops, `FEV` port/ferry routes, `SZA` Siberian rails, `BAC` archive workshops.
- `settlement`: federal congress, city duma, worker council, or Birobidzhan council records with recognition and legal helper.
- `propaganda`: congress missions, relief conference, worker records, minority council messaging; add recognition/league support or foreign-channel access.

Suggested decision unlocks:

- `soviet_collapse_run_far_eastern_ferry_protocol`
- `soviet_collapse_secure_siberian_city_rail_ledger`
- `soviet_collapse_expand_ural_workshop_quota`
- `soviet_collapse_convene_idel_ural_corridor_congress`
- `soviet_collapse_route_birobidzhan_relief`

These can be queued if the first pass only changes focus rewards.

## Suggested Constants, Helpers, And Decision Unlocks

Use a new script-constant category only if the implementation adds more than a few repeated values. Suggested category:

```txt
soviet_collapse_custom_splinter_focus = {
    schema = {
        any_key = yes
        data = fixed_point
    }

    mobile_column_motorized = 120
    port_guard_support_equipment = 80
    signal_network_support_equipment = 90
    local_settlement_authority = 3
    propaganda_local_authority = 2
    steppe_pass_command_power = 15
    settlement_dependency_relief = -2
}
```

If the main agent adds helpers, keep them narrow and documented in the existing dynamic/helper docs as required by `AGENTS.md`. Recommended helper order:

1. `soviet_collapse_apply_focus_signature_military_package`
2. `soviet_collapse_apply_focus_custom_settlement_package`
3. `soviet_collapse_apply_focus_custom_industry_package`
4. `soviet_collapse_apply_focus_custom_propaganda_package`

However, the current concurrent military-helper patch may already cover item 1. If so, the main agent should reuse that helper and only add non-military helpers after the focus reward patch is stable.

Decision unlocks should be implemented only where a focus creates a real repeatable action. Avoid adding decisions just to remove duplicate rewards. Best first unlocks:

- `BBH`/`FTH`: raid depots, free prisoners/registers, non-domination pact.
- `KRS`/`ARD`/`NLC`: convoy corridor, port observer, ice-road relief.
- `UDC`/`SDZ`: command inspection, custody ledger, officer amnesty.
- `BSC`/`TNC`/`ALA`: caravan escort, pass guard, oasis mediation.
- `GAC`/`DHC`/`KHC`/`MRC`: grain convoy, stanitsa mediation, mountain pass watch.
- `FEV`/`SZA`/`UWD`/`IUL`/`BAC`: rail ledger, workshop quota, federal congress, relief routing.

## Implementation Priority

1. Patch `*_propaganda` and `*_settlement` first.
   - They are currently the least mechanically expressive and easiest to make distinct with existing variables/helpers.
   - They should set route flags consumed by later AI/decision checks.

2. Patch `*_first_guard` and `*_special_arm` after the concurrent military-helper work lands.
   - Reuse the main agent's military reward helper if it exists.
   - Keep manpower/equipment grants under current balance caps; move identity into equipment type, XP, command power, state defenses, and flags.

3. Patch `*_industry_plan`.
   - Replace random arms factory spam with tag-family infrastructure, dockyard, rail, supply, airbase, or workshop packages.
   - Keep a factory only when the tag's identity supports it.

4. Sweep adjacent scaffold duplicates while the file is open.
   - `*_stores`, `*_legitimacy`, `*_rival`, `*_civil_rule`, `*_enemy_front`, `*_league`, and `*_foreign` should not all remain identical after the target five clusters are fixed.

5. Run focus reward audit and localisation audit after implementation.
   - The focus text already distinguishes many identities; effects should catch up to that text rather than requiring broad rewrites.

## Duplicate Content To Merge Or Remove

- Merge repeated direct manpower/equipment packages into a helper only after the concurrent military-helper patch is reviewed.
- Remove redundant direct `add_political_power = constant:soviet_collapse_republic_focus.political_power_small` from `*_propaganda` unless paired with a tag-specific pressure or unlock.
- Remove arms-factory-only `*_industry_plan` rewards from non-industrial tags.
- Avoid adding new focuses with new names to hide duplicate payoffs; update the existing repeated nodes.
- Review lowercase `mrc_close_the_passes`, `mrc_reject_moscow_border_troops`, `mrc_summon_mountain_elders`, `mrc_raid_lowland_depots`, `mrc_negotiate_with_georgia_or_azerbaijan`, and `mrc_protect_village_autonomy`. If these ids are intentional, document why; otherwise normalize to `MRC_*` and update refs/localisation in a separate implementation pass.

## Visual Progression Plan

No asset edits in this handoff. The reward patch should still leave clear sprite guidance:

- If a focus changes from generic manpower to a signature force, verify the icon matches that force type.
- Prioritize unique icon follow-up for any cluster whose effect identity changes: mobile columns, pass guards, naval infantry, command networks, grain convoys, port statutes, and rail ledgers.
- The existing final report still has a focus-icon uniqueness blocker. Reward differentiation should feed the icon cleanup list instead of creating a second unrelated visual pass.

## Lore And Readability Plan

The localisation often already contains better identity than the effects. Implementation should align effects to existing wording:

- If text says "tachanka", "mobile columns", or "portable arsenals", rewards should include mobility, raids, or command power.
- If text says "port", "convoy", "dockyard", "ice road", or "weather station", rewards should touch coastal/air/logistics assets.
- If text says "archives", "custody", "records", or "command seal", rewards should support legality, command power, support equipment, and inspection decisions.
- If text says "oasis", "pass", "caravan", or "aksakal", rewards should support local authority, pass infrastructure, and regional cooperation.
- If text says "grain", "stanitsa", "village", or "mountain elders", rewards should support local settlement, supply, and terrain defense.

Do not rewrite player-facing text to mention implementation changes. Write as if the content has always behaved this way.

## AI And Balance Notes

- Update `ai_will_do` modifiers where a reward becomes route-specific.
- AI should prefer settlement packages when stable, not at war, or seeking recognition.
- AI should prefer special-arm and first-guard packages during war, low equipment, weak command, or nearby Soviet pressure.
- AI should prefer industry plans when it has few factories, low depot control, or needs a route-specific logistics base.
- Avoid stacking all helper effects into the same focus. Existing threat and monthly pressure caps should remain meaningful.
- Keep new decision unlocks gated by focus flags and existing low/medium custom-splinter costs to prevent free repeated rewards.
- If a reward adds state buildings, prefer one or two grounded improvements over broad random factory grants.

## Likely Touched Files And Systems

Implementation likely touches:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/script_constants/005_soviet_collapse_constants.txt` if new tuning constants are added
- `common/scripted_effects/005_soviet_collapse_effects.txt` if new helpers are added after the concurrent helper patch
- `common/scripted_triggers/005_soviet_collapse_triggers.txt` if new decision costs or availability gates are added
- `common/decisions/005_soviet_collapse_decisions.txt` and `common/decisions/categories/005_soviet_collapse_categories.txt` if focus rewards unlock new actions
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml` only if new visible decision names/tooltips/flags are surfaced
- `interface/005_soviet_collapse_custom_icons.gfx` and asset docs only if new decision or focus icons are required
- `docs/events/005_soviet_collapse_focus_tree_audit.md`, validation report, and completion ledger after implementation facts exist

## Validation Checklist

Source checks:

- Count target clusters after patch and confirm no `*_first_guard`, `*_special_arm`, `*_settlement`, `*_industry_plan`, or `*_propaganda` cluster still has the same normalized reward across all 19 tags.
- Confirm every changed focus still has `completion_reward`, `ai_will_do`, search filters, prerequisites, and no invalid `<=` or `>=`.
- Confirm no new whole-world daily/weekly/monthly on-action logic was added.
- Confirm any new constants live in `common/script_constants/` and are referenced with `constant:category.key` where supported.
- Confirm any new helper is documented if it belongs in a dynamic/shared helper file.
- Confirm any decision unlock has visible/available gates, cost text, AI, cooldown or one-use guard, localisation, and cleanup if needed.
- Confirm all new visible localisation uses UTF-8 BOM and no `:0` key style.
- Confirm route flags set by settlement/propaganda focuses are consumed by later decisions, AI, or follow-up focuses.
- Confirm lowercase `mrc_*` ids are either intentionally preserved with references/localisation or queued for a safe rename pass.

Gameplay/balance checks:

- For each family, compare total manpower/equipment against pre-patch totals so identity changes do not create large accidental buffs.
- Check at least one tag per family through the focus path: `BSC`, `BBH`, `KRS`, `UDC`, `DHC`, `FEV`, `ARD`.
- Verify Soviet threat variables still move through intended channels: old-movement pressure, foreign pressure, depot vulnerability, military obedience, league cohesion, and republic confidence.
- Verify settlement routes are meaningfully different from radical routes.
- Verify AI weighting prefers the new family-specific payoffs in plausible states.

Audit follow-up:

- Spawn/use `chaosx_focus_tree_auditor` after implementation.
- Use `chaosx_decision_mission_auditor` if new decision unlocks are added.
- Use `chaosx_localisation_auditor` if visible decision/focus/localisation text changes.
- Use `chaosx_scripted_system_architect` if helper proliferation begins to repeat across more than one family.

## Queued Future Ideas

- Add one unique decision family per tag family after the reward patch proves stable.
- Add late-branch follow-up events for settlement choices that create diplomatic or local backlash.
- Tie icon cleanup to the new reward identities: one icon request packet per family rather than one huge all-tag pass.
- Add achievement hooks for rare custom-splinter settlements, such as anti-protectorate commune settlement, free-port survival, mountain-pass league, or Ural workshop federation.
- Re-audit compact special actors (`PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`) after the 19 large custom trees are fixed; they have fewer target-cluster ids but still contain repeated foreign-letter and compact-settlement payoffs.
