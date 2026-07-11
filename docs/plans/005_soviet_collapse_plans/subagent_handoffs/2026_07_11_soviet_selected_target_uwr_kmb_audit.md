# Event 005 Selected-Target and UWR/KMB AI Audit

Date: 2026-07-11

Role: `chaosx_decision_mission_auditor`

Mode: read-only gameplay audit

## Verdict

The selected Moscow and foreign-patron desks have static registration and scope support for the four pre-terminal target classes requested by the accepted improvement addendum: a normal base republic, TAJ, a dynamic non-base republic, and a high-chaos successor. They do not yet pass an end-to-end lifecycle audit.

The shared implementation has four material failures:

1. A human player can use every selected foreign-patron action without satisfying its action-specific eligibility trigger. This includes the client-cabinet puppet action.
2. Closing and reopening either desk can bypass each action's `days_re_enable` cooldown because the open helpers explicitly reactivate targeted decisions.
3. Annexation and other resolution paths do not consistently clear both the target's selection state and the owning country's desk state.
4. Both desks are unavailable after Union Unmade, even though the accepted July 11 addendum requires a usable post-terminal case. Terminal cleanup also does not close an already-open desk.

The requested implementation-count evidence is present: Event 005 has exactly 43 successor focus trees containing 1,728 focuses, plus 118 numbered mission definitions. UWR and KMB have no route-specific entries in `common/ai_strategy/005_soviet_collapse.txt`. They receive only the shared breakaway-survival strategy and their local focus or decision `ai_will_do` blocks.

## Sources consulted

Required offline references were consulted before the audit:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`

Vanilla documentation and precedents consulted:

- `common/decisions/_documentation.md`
- `common/ai_strategy/_documentation.md`
- `common/on_actions/_documentation.md`
- `documentation/effects_documentation.md`, including targeted-decision activation and removal, event-target, and array effects
- `documentation/triggers_documentation.md`, including decision, mission, event-target, array, original-tag, existence, and strength-ratio triggers
- A vanilla AST targeted-decision activation precedent

Project guidance consulted:

- `chaos-redux-events`
- `chaos-redux-subagents`
- `hoi4-decisions-missions`
- The accepted July 11 improvement-loop addendum
- The Event 005 source-of-truth map and documentation-state map
- The Event 005 event overview and all nine source specifications
- Existing Event 005 handoffs covering foreign-patron selection, focus release visibility, and playability

### Primary implementation anchors

| Evidence | Location |
|---|---|
| Accepted five-case requirement | `docs/plans/005_soviet_collapse_plans/2026_07_11_soviet_collapse_improvement_loop_addendum.md:98` and `:157` |
| Source-map verification boundary | `docs/plans/005_soviet_collapse_plans/source_of_truth_map.md:14` |
| Moscow selector and selected actions | `common/decisions/005_soviet_collapse_decisions.txt:4818` through the Moscow action block |
| Foreign selector and 17 selected actions | `common/decisions/005_soviet_collapse_decisions.txt:6111` through `:7264` |
| Foreign actions use `available = { always = yes }` | `common/decisions/005_soviet_collapse_decisions.txt:6162` through `:7207` |
| Moscow selection, activation, and removal | `common/scripted_effects/005_soviet_collapse_effects.txt:3900`, `:3979`, and `:4018` |
| Foreign selection, activation, and removal | `common/scripted_effects/005_soviet_collapse_effects.txt:4057`, `:4168`, and `:4260` |
| Shared resolved-target cleanup | `common/scripted_effects/005_soviet_collapse_effects.txt:4334` |
| Breakaway setup and array insertion | `common/scripted_effects/005_soviet_collapse_effects.txt:4600` and `:4632` |
| Annexation defeat handler | `common/on_actions/005_soviet_collapse_on_actions.txt:9` and `common/scripted_effects/005_soviet_collapse_effects.txt:4985` |
| Terminal effect and terminal cleanup | `common/scripted_effects/005_soviet_collapse_effects.txt:3687` and `:25249` |
| Base-tag, breakaway, patron, and Moscow eligibility triggers | `common/scripted_triggers/005_soviet_collapse_triggers.txt:2638`, `:3135`, `:3302`, `:3367`, and `:3499` |
| UWR and KMB setup | `common/scripted_effects/005_soviet_collapse_effects.txt:20438` and `:20489` |
| UWR and KMB focus flags | `common/national_focus/005_soviet_collapse_custom_splinters.txt:1390` through `:1750` |
| KMB decisions and concession AI | `common/decisions/005_soviet_collapse_decisions.txt:13064` through `:13291` |

## Count verification

The focus counts below were independently derived from the Event 005 focus files, rather than copied from a report.

| File | Trees | Focuses |
|---|---:|---:|
| `common/national_focus/005_soviet_collapse_republics.txt` | 9 | 515 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 27 | 1,021 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 3 | 128 |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | 4 | 64 |
| **Total** | **43** | **1,728** |

The Soviet mission file contains 118 numbered mission definitions. Their numeric suffixes span 001 through 128. The absent suffixes are 090, 109, 110, 112, 113, 114, 115, 116, 117, and 118. No duplicate numeric suffix was found.

## Shared selected-target contract

### Persistent and transient state

The breakaway target registry is:

- `global.soviet_collapse_breakaway_countries`

The Moscow desk stores:

- Owner flag: `soviet_collapse_moscow_republic_menu_open`
- Owner variable: `soviet_collapse_moscow_selected_republic_country`
- Target flag: `soviet_collapse_moscow_republic_selected_target`

The foreign-patron desk stores:

- Sponsor flag: `soviet_collapse_foreign_patron_menu_open`
- Sponsor variables: `soviet_collapse_menu_selected_target_country` and `soviet_collapse_menu_selected_target_influence`
- Target flag: `soviet_collapse_foreign_patron_selected_target`
- Target variables: `soviet_collapse_selected_foreign_patron_country` and `soviet_collapse_selected_foreign_patron_influence`

The open and close chains also use regular event targets:

- `soviet_collapse_moscow_republic_menu_target`
- `soviet_collapse_foreign_patron_menu_target`

These are correctly regular rather than global event targets. They only need to survive the current effect chain, and the lasting selection is stored in flags and country variables. No missing global-event-target cleanup was found.

### Scope proof

For both targeted-decision families, `ROOT` is the desk owner and `FROM` is the chosen republic. The selection helpers preserve that relationship through all three activation paths:

- Direct `target = FROM`
- `target = event_target:<selected_target>`
- Array iteration followed by `ROOT = { ... target = PREV }`

In the array form, `PREV` correctly resolves to the iterated target while `ROOT` restores the desk owner. Representative completion helpers also charge and modify the owner in `ROOT`, then apply the republic-side result in `FROM`. No ROOT/FROM inversion was found in the inspected Moscow or foreign action completions.

The six Moscow action identifiers are:

- `soviet_collapse_offer_new_union_treaty`
- `soviet_collapse_open_republic_negotiation_table`
- `soviet_collapse_embed_loyal_republic_administrators`
- `soviet_collapse_offer_federal_reintegration_compact`
- `soviet_collapse_issue_republic_military_ultimatum`
- `soviet_collapse_authorize_republic_punitive_operation`

The 17 foreign-patron action identifiers are:

- `soviet_collapse_recognize_breakaway_government`
- `soviet_collapse_fund_ideological_liaison_offices`
- `soviet_collapse_ship_border_armaments`
- `soviet_collapse_dispatch_military_advisers`
- `soviet_collapse_open_republican_intelligence_channel`
- `soviet_collapse_sponsor_volunteer_corps`
- `soviet_collapse_negotiate_republican_trade_mission`
- `soviet_collapse_fund_civilian_construction_mission`
- `soviet_collapse_fund_military_construction_mission`
- `soviet_collapse_sponsor_press_and_radio_network`
- `soviet_collapse_secure_republican_aid_corridor`
- `soviet_collapse_build_republics_league_conference`
- `soviet_collapse_route_aid_through_league_logistics`
- `soviet_collapse_demand_anti_puppet_clause`
- `soviet_collapse_offer_protection_treaty`
- `soviet_collapse_demand_adviser_privileges`
- `soviet_collapse_install_client_cabinet`

All six Moscow actions and all 17 foreign actions are present in both their activation and removal helpers. There is no static list mismatch.

## Five-case audit matrix

| Case | Registration and activation | Visibility and availability | Completion scope | Cleanup and reopen | Result |
|---|---|---|---|---|---|
| Base republic, using UKR as the exemplar | Release setup gives the target the breakaway flag and inserts it into `global.soviet_collapse_breakaway_countries`. The target passes the shared breakaway trigger. | A qualifying human SOV or foreign patron can select it before terminal collapse. The shared foreign availability bypass and cooldown issue apply. | ROOT/FROM handling is structurally correct. Owner costs and target results resolve to the intended scopes. | Close state is cleared on the ordinary close helper, but reopen can reset cooldown. Annexation cleanup is incomplete. | **Fails end-to-end** despite valid registration. |
| TAJ | `is_soviet_collapse_base_republic_without_kazakhstan_tag` explicitly includes TAJ. Standard release setup gives it the same breakaway flag and array membership as the other base republics. | No TAJ-specific visibility gap was found. It reaches the same pre-terminal desk surfaces and inherits the same shared failures. | No TAJ-specific ROOT/FROM exception was found. | Same cooldown-reset and stale-selection risks as the base case. | **Fails end-to-end** for shared lifecycle reasons, not a TAJ registration defect. |
| Dynamic non-base republic | Progressive and first-wave release setup mark dynamically created targets with `soviet_collapse_event_created_republic`, then call the shared breakaway setup that adds the breakaway flag and array entry. | The dynamic flag and array membership satisfy the shared target path before terminal collapse. The foreign selected-target branch still bypasses action eligibility. | The generic helper scopes correctly because it operates on the selected country scope, not a hardcoded tag. | Dynamic re-release is particularly exposed to inherited stale target flags when annexation did not call full cleanup. | **Fails end-to-end** despite generic-tag support. |
| High-chaos successor, including UWR or KMB | Each setup marks the country with its high-chaos or successor identity before calling the shared breakaway setup. The high-chaos flag is accepted by `is_soviet_collapse_breakaway_country`, and the target enters the global array. | It can reach the same pre-terminal selected surfaces. No UWR/KMB-specific selected-target exclusion was found. | Generic completion helpers preserve scope. | Same cooldown and cleanup failures apply. | **Fails end-to-end** despite valid high-chaos registration. |
| Post-Union-Unmade | Terminal collapse clears `soviet_collapse_active` and sets the terminal state. Both desk surfaces explicitly depend on pre-terminal activity or reject the terminal state. | Moscow selection additionally rejects targets at war with SOV, while terminal breakaways are placed at war with SOV. Foreign candidate and decision-surface triggers explicitly reject Union Unmade. | No post-terminal completion path can be reached. | Terminal cleanup does not remove selected action rows or reset the already-open Moscow or foreign desk state. | **Static failure. The accepted post-terminal case is not implemented.** |

## Detailed findings

### 1. Selected foreign targets bypass every action-specific eligibility trigger

Severity: critical gameplay exploit

All 17 foreign action definitions use:

```hoi4
available = {
	always = yes
}
```

Their target triggers accept a selected-target branch independently of the normal action trigger. In practical terms, selection proves only that the row belongs to the chosen target. It also accidentally acts as permission to execute the row. The custom cost blocks check resources, but they do not restore the missing diplomatic, ideological, dependency, dominance, or weakness conditions.

This permits a human patron to pay for and execute any selected action whose cost is affordable. The bypass reaches the strongest dependency outcomes:

- `soviet_collapse_offer_protection_treaty`
- `soviet_collapse_demand_adviser_privileges`
- `soviet_collapse_install_client_cabinet`

The last action applies its autonomy result to `FROM`, so the scope is correct but the permission gate is not. AI evaluation is less exposed because unselected target evaluation reaches the action-specific `can_target_*` branch.

Minimal repair requirement:

- Keep the selected-target condition in `target_trigger` so only the chosen republic is displayed to a human player.
- Put the matching `can_target_*` trigger in each action's `available` block.
- Preserve hard prerequisite gates for dependent action tiers.
- Prefer a visible but disabled row when the target is selected and the action is not yet valid.

This repair must cover all 17 actions as one shared audit surface. Fixing only the three puppet-chain decisions would leave the same structural exploit in the other fourteen.

### 2. Desk close and reopen can reset targeted-decision cooldowns

Severity: high, repeatable reward farming

The official vanilla decision documentation states that `activate_targeted_decision` ignores normal trigger conditions, cooldown, and `fire_only_once`. Both open helpers explicitly activate all action rows. Both close helpers remove them. Reopening therefore creates a new explicit activation path that can bypass the intended `days_re_enable` timing.

Affected cooldowns include:

- Moscow actions: 28, 35, or 70 days
- Foreign actions: 45 days

Minimal repair requirement:

- Do not remove and explicitly reactivate cooldown-bearing action decisions whenever the player closes and opens a desk.
- Let broad target eligibility keep the target instance alive.
- Use selected-target visibility to expose only the chosen target.
- Keep action validity in `available`.

If daily target refresh is required by the engine after selection, the expected one-day refresh is safer than manually overriding cooldown state. An activation helper must not be the mechanism that reconstructs the action rows.

### 3. Defeat and resolution cleanup do not clear the complete two-country state

Severity: high, stale selection and tag-reuse risk

The annexation on-action reaches `soviet_collapse_handle_breakaway_defeat` in the defeated country's scope. That effect removes the target from the global array and clears `soviet_collapse_breakaway`, but it does not call the full resolved-target cleanup helper. It does not remove the targeted decisions, clear the target's selected flags, or reset the owner-side Moscow or sponsor menu variables.

The existing `soviet_collapse_cleanup_resolved_breakaway_target` is also asymmetric. It clears Moscow owner state, and it clears the foreign target's stored patron variables and flag. It does not first scope through `var:soviet_collapse_selected_foreign_patron_country` to reset the foreign sponsor's open-menu flag, selected target variables, or active decision rows.

Minimal repair requirement:

- Create or consolidate one idempotent resolved-target cleanup helper.
- Call it from annex defeat, federal reintegration, reconquest, terminal conversion, and every other path that removes a breakaway from the registry.
- Before clearing the target's stored sponsor identifier, scope into `var:soviet_collapse_selected_foreign_patron_country` and clear the sponsor-side desk state and targeted decisions.
- Clear the corresponding SOV selection state when the resolved target matches the Moscow selected-target variable.
- Protect global array removal and any associated counters from double application.

### 4. Post-Union-Unmade desk use is statically unreachable

Severity: high, accepted case missing

`soviet_collapse_apply_terminal_collapse` invokes terminal mission cleanup, which clears the global active state, and then establishes Union Unmade. The shared active trigger rejects terminal collapse. Moscow's category, selector, and actions depend on the active state, and its selector rejects a target at war with SOV. The terminal effect places breakaways at war with SOV.

The foreign-patron candidate and decision-surface triggers explicitly reject `soviet_collapse_super_event_union_unmade_fired` and the terminal state. Terminal cleanup does not close an already-open selected-target desk.

The older Part 4 specification says obsolete categories should be canceled or converted at terminal collapse. The accepted July 11 addendum and the current source-of-truth map require a usable post-Union-Unmade target case. These can be reconciled only through an explicit aftermath conversion, not by relaxing one category flag.

Required design decision before implementation:

- Define which Moscow actor, if any, owns an aftermath desk once the Union is unmade.
- Define whether wartime targets receive military, diplomatic, or reconstruction actions.
- Define which pre-terminal actions are obsolete and must be removed.
- Define the foreign-patron aftermath candidate rules and whether hostile patrons are intentional participants.

No fallback is recommended. Treating the existing prewar reintegration actions as valid during the terminal war would conflict with their current conditions and narrative purpose.

### 5. Foreign-patron root eligibility excludes several intended patron situations

Severity: medium, route-scope mismatch

The foreign-patron candidate requires `is_major = yes` and rejects a country at war with SOV. This can exclude named regional patrons from the core specification depending on their current major status. It also makes the scripted hostile-patron double-game branches unreachable through the normal desk because a hostile patron cannot qualify to open it.

This is a sponsor-side scope issue rather than a target-class issue. The intended list of regional and hostile patrons should be translated into a reusable candidate trigger instead of relying only on current major status.

## Runtime verification facts

This audit is static. The following facts are the minimum runtime evidence needed after the repair. They are deliberately expressed as observable game state rather than generic load checks.

### Repeat for base, TAJ, dynamic non-base, and high-chaos targets

1. The target exists, has `soviet_collapse_breakaway`, and is a member of `global.soviet_collapse_breakaway_countries`.
2. A dynamic non-base target also has `soviet_collapse_event_created_republic`. A high-chaos target has its high-chaos successor marker.
3. The selector is visible to a qualifying human owner.
4. Opening the Moscow desk produces exactly six Moscow action rows for the selected target and no rows for another target.
5. Opening the patron desk produces exactly 17 foreign action rows for the selected target and no rows for another target.
6. The owner selected-target variable equals the selected country's ID.
7. The selected target flag is set on the target, not the owner.
8. For the foreign desk, the target's stored patron variable equals the patron country's ID.
9. A representative action subtracts its cost from `ROOT` and applies its reward, flag, idea, autonomy, or other result to `FROM`.
10. An action whose dependency or strength condition is false remains visible for the selected target but is disabled. The current implementation is expected to fail this fact for human foreign actions.
11. After executing an action, closing and reopening before its 28, 35, 45, or 70 day cooldown expires does not restore it. The current implementation is expected to fail this fact.
12. Closing the desk clears the owner's menu-open flag and variables, clears the target selected flag, removes the selected rows, and restores the selector.
13. Annexation or federal reintegration clears the target registry entry, both sides' selection state, and every selected row.
14. Releasing the same tag again does not inherit any previous selected-target or sponsor state.

### Post-Union-Unmade case

The accepted target state requires a separately defined aftermath surface. Once designed, runtime proof must show:

1. No obsolete pre-terminal selected rows remain after terminal conversion.
2. The intended aftermath owner can select an eligible surviving republic.
3. The terminal war state does not accidentally invalidate every aftermath target.
4. Converted actions use their new wartime or reconstruction conditions and do not reuse invalid prewar permission gates.

Without implementation changes, the static expectation is that both selected-target categories are absent after Union Unmade.

## UWR and KMB AI audit

### Current shared coverage

`common/ai_strategy/005_soviet_collapse.txt` contains no UWR or KMB tag, successor flag, focus flag, or route entry. Both countries inherit `soviet_collapse_breakaway_survival`, which provides only the shared military posture:

- `build_army = 80`
- Infantry equipment allocation factor `35`
- Support equipment allocation factor `35`

This does not express either country's route identity.

### UWR current behavior

UWR has seven focuses:

- `UWR_open_the_special_pathogen_republic`
- `UWR_tver_pathogen_directorate`
- `UWR_cw_facility_section`
- `UWR_experiment_camp_registry`
- `UWR_zombie_weapon_section`
- `UWR_field_release_doctrine`
- `UWR_chaos_warfare_path`

Its setup effect is `soviet_collapse_setup_uwr_successor`, and its identity flag is `soviet_collapse_unconventional_warfare_successor`. The setup already adds permanent conquest and antagonism strategies against SOV. Neighbor helper effects add dynamic conquest, antagonism, and war goals. The focus nodes have local `ai_will_do` weights.

What is missing is a strategic posture for building and protecting the blacksite route, then escalating force concentration after field-release doctrine. There is no dedicated UWR decision category. The current contamination application is a scripted focus result, not an AI choice. A route strategy can improve military behavior, but it cannot honestly satisfy a future requirement for AI to choose between controlled contamination and escalation until the queued UWR decision work exists.

### KMB current behavior

KMB has nine focuses:

- `KMB_open_the_subsoil_ledger`
- `KMB_guard_the_pitheads`
- `KMB_coal_for_every_front`
- `KMB_export_treaty_board`
- `KMB_iron_and_chromium_quotas`
- `KMB_raise_furnace_columns`
- `KMB_oil_shale_emergency`
- `KMB_concession_treaties`
- `KMB_the_earth_is_the_treaty`

Its setup effect is `soviet_collapse_setup_kmb_successor`, its identity flag is `soviet_collapse_kuznetsk_mining_successor`, and its home state is 569.

Its six decisions are:

- `kmb_deepen_subsoil_extraction`
- `kmb_sell_coal_for_machines`
- `kmb_open_export_auction`
- `kmb_sign_resource_treaty`
- `kmb_trade_oil_for_trucks`
- `kmb_force_mining_concession`

Each decision has local `ai_will_do`, and the concession effect adds dynamic conquest and antagonism toward a neighbor. There is no shared strategic overlay for basin defense, rail and train supply, coal-golem production, treaty restraint while isolated, or concession escalation when KMB is stronger. The `coal_golem_equipment` archetype exists, and vanilla AI strategy documentation supports `equipment_production_min_factories_archetype` for this purpose.

## Minimal AI blueprint

This is a bounded implementation blueprint for `common/ai_strategy/005_soviet_collapse.txt` and the matching reusable triggers. It adds no focuses and does not redesign either route.

### Tuning constants

Keep weights centralized. File-scoped constants are sufficient for values used only in the AI strategy file:

```hoi4
@SOV_COLLAPSE_AI_UWR_BLACKSITE_ARMY = 100
@SOV_COLLAPSE_AI_UWR_BLACKSITE_INFANTRY = 40
@SOV_COLLAPSE_AI_UWR_BLACKSITE_SUPPORT = 30
@SOV_COLLAPSE_AI_UWR_FIELD_RELEASE_ARMY = 120
@SOV_COLLAPSE_AI_UWR_FIELD_RELEASE_CONCENTRATION = 25

@SOV_COLLAPSE_AI_KMB_BASIN_ARMY = 100
@SOV_COLLAPSE_AI_KMB_BASIN_INFANTRY = 45
@SOV_COLLAPSE_AI_KMB_BASIN_TRAINS = 50
@SOV_COLLAPSE_AI_KMB_COAL_GOLEM_FACTORIES_EARLY = 1
@SOV_COLLAPSE_AI_KMB_COAL_GOLEM_FACTORIES_MASS = 2
@SOV_COLLAPSE_AI_KMB_TREATY_RESTRAINT = 80
@SOV_COLLAPSE_AI_KMB_CONCESSION_ARMY = 120
@SOV_COLLAPSE_AI_KMB_CONCESSION_CONCENTRATION = 25
```

The concession strength threshold is shared between decision AI and strategy AI, so it belongs in the existing `soviet_collapse_kmb_balance` script-constant category:

```hoi4
ai_concession_strength_ratio = 1.25
```

### UWR entries

#### `soviet_collapse_uwr_blacksite_posture`

`allowed`:

- `original_tag = UWR`

`enable`:

- Has `soviet_collapse_unconventional_warfare_successor`
- `has_soviet_collapse_successor_decision_surface = yes`
- Has `uwr_focus_tver_pathogen_directorate`, `uwr_focus_cw_facility_section`, or `uwr_focus_experiment_camp_registry`

`abort`:

- Negation of the enabling successor and surface conditions

Strategies:

- `type = build_army`, `value = @SOV_COLLAPSE_AI_UWR_BLACKSITE_ARMY`
- `type = equipment_production_factor`, `id = infantry`, `value = @SOV_COLLAPSE_AI_UWR_BLACKSITE_INFANTRY`
- `type = equipment_production_factor`, `id = support`, `value = @SOV_COLLAPSE_AI_UWR_BLACKSITE_SUPPORT`

#### `soviet_collapse_uwr_field_release_posture`

`allowed`:

- `original_tag = UWR`

`enable`:

- Has the UWR successor flag and successor decision surface
- Has `uwr_focus_field_release_doctrine` or `uwr_focus_chaos_warfare_path`

`abort`:

- Negation of the enabling conditions

Strategies:

- `type = build_army`, `value = @SOV_COLLAPSE_AI_UWR_FIELD_RELEASE_ARMY`
- `type = force_concentration_factor`, `value = @SOV_COLLAPSE_AI_UWR_FIELD_RELEASE_CONCENTRATION`

Do not duplicate conquest targets in these entries. Existing UWR neighbor helpers already own target selection, antagonism, and war-goal setup.

### KMB entries

#### `soviet_collapse_kmb_basin_posture`

`allowed`:

- `original_tag = KMB`

`enable`:

- Has `soviet_collapse_kuznetsk_mining_successor`
- `has_soviet_collapse_successor_decision_surface = yes`
- Controls state 569

`abort`:

- Negation of the enabling successor, surface, or home-state conditions

Strategies:

- `type = build_army`, `value = @SOV_COLLAPSE_AI_KMB_BASIN_ARMY`
- `type = equipment_production_factor`, `id = infantry`, `value = @SOV_COLLAPSE_AI_KMB_BASIN_INFANTRY`
- `type = equipment_production_factor`, `id = train`, `value = @SOV_COLLAPSE_AI_KMB_BASIN_TRAINS`

#### `soviet_collapse_kmb_coal_golem_early_production`

`enable`:

- KMB successor and surface conditions are true
- Has `kmb_focus_guard_the_pitheads`
- Does not have `kmb_focus_raise_furnace_columns`

Strategy:

- `type = equipment_production_min_factories_archetype`, `id = coal_golem_equipment`, `value = @SOV_COLLAPSE_AI_KMB_COAL_GOLEM_FACTORIES_EARLY`

#### `soviet_collapse_kmb_coal_golem_mass_production`

`enable`:

- KMB successor and surface conditions are true
- Has `kmb_focus_raise_furnace_columns`

Strategy:

- `type = equipment_production_min_factories_archetype`, `id = coal_golem_equipment`, `value = @SOV_COLLAPSE_AI_KMB_COAL_GOLEM_FACTORIES_MASS`

The early gate must explicitly exclude the mass flag so the minimum-factory strategies do not stack ambiguously.

#### KMB concession target triggers

Add a reusable `has_soviet_collapse_kmb_valid_concession_target` trigger that proves at least one neighboring country:

- Exists
- Is not KMB
- Is not in KMB's faction
- Is not already at war with KMB
- Can be legally selected by the existing concession effect

Add `has_soviet_collapse_kmb_superior_concession_target` as the same target set plus a `strength_ratio` comparison against `constant:soviet_collapse_kmb_balance.ai_concession_strength_ratio`.

#### `soviet_collapse_kmb_treaty_posture`

`enable`:

- KMB successor and surface conditions are true
- Has `kmb_focus_export_treaty_board`
- Is at peace
- Is not in a faction
- Does not have a superior valid concession target

Strategy:

- `type = avoid_starting_wars`, `value = @SOV_COLLAPSE_AI_KMB_TREATY_RESTRAINT`

#### `soviet_collapse_kmb_concession_posture`

`enable`:

- KMB successor and surface conditions are true
- Has `kmb_focus_concession_treaties`
- Has a superior valid concession target

Strategies:

- `type = build_army`, `value = @SOV_COLLAPSE_AI_KMB_CONCESSION_ARMY`
- `type = force_concentration_factor`, `value = @SOV_COLLAPSE_AI_KMB_CONCESSION_CONCENTRATION`

All route entries should abort when their enable conditions cease to hold. Use `has_soviet_collapse_successor_decision_surface`, not `is_soviet_collapse_active`, so UWR and KMB do not lose route behavior merely because the Soviet-wide event reached its terminal aftermath.

### KMB decision-AI correction

`kmb_force_mining_concession` should require `has_soviet_collapse_kmb_valid_concession_target` in `available`. Its `ai_will_do` should start at zero and receive its existing positive route weight only when `has_soviet_collapse_kmb_superior_concession_target` is true, followed by the existing chaos and threat modifiers.

This prevents the AI from paying for an empty concession or selecting coercion while strategically weaker. The existing treaty decisions already favor isolation, so they can remain the restrained alternative after the shared treaty strategy is added.

## Files changed

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_07_11_soviet_selected_target_uwr_kmb_audit.md`

No gameplay, localisation, interface, asset, spreadsheet, or source-specification file was edited.

## Simplifications, omissions, and blockers

- No fallback, tag-specific exception, or focus addition is proposed.
- Runtime execution was outside this read-only audit. The exact runtime facts required after repair are listed above.
- Post-Union-Unmade desk behavior is blocked on explicit aftermath semantics. The current implementation cannot meet that accepted case by merely removing a terminal-state trigger.
- The UWR AI blueprint improves route posture with existing content. It cannot choose a controlled contamination decision until the queued UWR decision mechanic exists.
- The AI weights are a minimal first implementation and require scenario balance review against neighboring armies, equipment throughput, and decision costs before completion can be claimed.
