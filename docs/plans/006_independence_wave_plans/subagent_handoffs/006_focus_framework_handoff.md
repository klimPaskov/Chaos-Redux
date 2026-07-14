# Event 006 Focus Framework Handoff

## Scope and result

This tranche implements the shared Independence Wave focus framework without editing the dirty Event 6 foundation, execution, decision, registry, achievement, or global integration files.

The full tree contains 107 focuses and the additive contract contains 8 shared focuses, for 115 manually authored focus blocks in total. The implementation covers:

- survival and state construction
- an opt-in package-registered internal power struggle
- six mutually exclusive government settlements
- package-archetype economy and regional transport programs
- force-profile military programs plus five military policy choices
- diplomacy, recognition, neutrality, patron balancing, and patron-client development
- five former-host outcomes written through the shared bilateral ledger
- regional ambition, package signature, league, formable, and high-chaos hooks
- World Collapse ambition and high-chaos differentiation
- a durable-sovereignty capstone
- a non-destructive additive overlay for reused registered tags

This is a framework tranche. It does not mark any country package content-ready and does not create copied per-country trees.

## Files created

- `common/national_focus/006_independence_wave_focus.txt`
- `common/script_constants/006_independence_wave_focus_constants.txt`
- `common/scripted_effects/006_independence_wave_focus_effects.txt`
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt`
- `common/scripted_localisation/006_independence_wave_focus_scripted_localisation.txt`
- `localisation/english/006_independence_wave_focus_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_focus_framework_handoff.md`

No `.gfx` file was edited. No commit was created.

## Assignment contract

`independence_wave_assign_focus_framework` accepts temporary `independence_wave_focus_assignment_input`:

- `constant:independence_wave_focus_assignment.full_framework`
- `constant:independence_wave_focus_assignment.additive_overlay`
- `constant:independence_wave_focus_assignment.post_formation_overlay`

Only `full_framework` calls `load_focus_tree`. It is reserved for Event 6-created tags and an explicitly reviewed registered-tag exception whose existing tree is known to be minimal. Both overlay modes only set flags and never replace the owning tree.

`independence_wave_clear_focus_runtime` removes the assignment, package adapter flags, focus milestones, internal-power values, military choices, charter proposals, ambition factor, and focus-owned unlocks for the outgoing generation. It deliberately does not clear DM success or failure flags.

## Required root wiring

The main integration owner has applied generation cleanup. Assignment and package-specific wiring remain below.

### Generation cleanup — resolved by the parent

`common/scripted_effects/006_independence_wave_effects.txt` calls the focus cleanup from both generation reset and active-origin termination while the released country is still scoped:

```txt
	independence_wave_clear_focus_runtime = yes
```

### Release assignment

In `common/scripted_effects/006_independence_wave_execution_effects.txt`, `independence_wave_initialize_frozen_countries` must read the matching entry from `global.independence_wave_plan_selected_registered_tag_statuses` before entering the released-country scope.

After `independence_wave_initialize_country_origin = yes` succeeds, and after that package's exact focus adapter contract has been published, assign:

```txt
# Event 6-created tag
set_temp_variable = {
	independence_wave_focus_assignment_input = constant:independence_wave_focus_assignment.full_framework
}
independence_wave_assign_focus_framework = yes
```

For a reused registered tag with a meaningful tree, assign:

```txt
set_temp_variable = {
	independence_wave_focus_assignment_input = constant:independence_wave_focus_assignment.additive_overlay
}
independence_wave_assign_focus_framework = yes
```

Do not infer the full tree from tag registration. The planner's registered-tag status must select additive mode unless a separate reviewed minimal-tree exception explicitly says otherwise.

### Existing-tree opt-in

Every reused registered tag assigned additive mode needs this one line inside its owning focus tree:

```txt
shared_focus = independence_wave_overlay_take_stock_of_independence
```

The other seven shared focuses descend from that root. Do not add them separately and do not load `independence_wave_focus_tree` for a meaningful existing tree.

Audit result at handoff: no owning national focus tree currently contains that `shared_focus =` line. Setting `independence_wave_additive_focus_overlay` alone does not inject any focus. The additive path therefore remains an explicit integration blocker until each reviewed meaningful tree opts in through a real shared-focus inclusion or another equally concrete additive mechanism.

### Package contract order

Before focus assignment, the package initializer must publish its researched contract. No default route pool is provided.

Government route entry points:

- `independence_wave_focus_allow_constitutional_route`
- `independence_wave_focus_allow_popular_council_route`
- `independence_wave_focus_allow_traditional_route`
- `independence_wave_focus_allow_emergency_military_route`
- `independence_wave_focus_allow_patron_client_route`
- `independence_wave_focus_allow_radical_sovereignty_route`

Former-host entry points:

- `independence_wave_focus_allow_host_negotiation_route`
- `independence_wave_focus_allow_host_guarded_frontier_route`
- `independence_wave_focus_allow_host_association_route`
- `independence_wave_focus_allow_host_reclamation_route`

Module entry points:

- `independence_wave_focus_register_ambition_family`
- `independence_wave_focus_register_signature_module`
- `independence_wave_focus_register_formable_family`
- `independence_wave_focus_allow_league_route`

For a package with two credible internal power centers, set temporary `independence_wave_power_struggle_input` to exactly one of the seven `constant:independence_wave_power_struggle.*` values, then call:

```txt
independence_wave_focus_register_power_struggle = yes
```

Packages without two researched power centers must not call it. The optional branch then remains absent.

## Decision contract

The framework sets exactly the agreed ten focus-facing unlock flags:

- `independence_wave_unlock_first_assembly`
- `independence_wave_unlock_traditional_authority`
- `independence_wave_unlock_foreign_service`
- `independence_wave_unlock_professional_army`
- `independence_wave_unlock_forced_host_recognition`
- `independence_wave_unlock_patron_client_route`
- `independence_wave_unlock_league_congress`
- `independence_wave_unlock_border_ambitions`
- `independence_wave_unlock_formable_discovery`
- `independence_wave_unlock_high_chaos_actions`

Government route ownership is split deliberately:

- DM04 opens the constitutional ratification focus.
- DM05 opens the traditional restoration focus.
- DM38 commits the patron-client route through the shared government-route effect. The focus tree follows that commitment and does not lock it a second time.
- The constitutional, popular council, traditional, emergency military, and radical focus commitments call `independence_wave_select_government_route` through focus-owned lock effects.

The five mutually exclusive league proposal flags are:

- `independence_wave_charter_proposal_defensive_congress`
- `independence_wave_charter_proposal_development_compact`
- `independence_wave_charter_proposal_sovereign_equality`
- `independence_wave_charter_proposal_armed_liberation`
- `independence_wave_charter_proposal_radical_revisionist`

DM46 consumes these exact identifiers. On the fifth pillar it maps the surviving proposal to its matching `independence_wave_league_route.*`, proclaims the formal league, and clears all five. The decision cleanup also clears them if the origin ends first. There is no default proposal or fallback route.

## World Collapse evidence

World Collapse does not change the fixed release count. It materially changes post-release access and pressure through these exact contracts:

1. `has_independence_wave_world_collapse_mandate` checks `independence_wave_origin_chaos_band` against `constant:independence_wave_chaos_band.world_collapse`.
2. `can_open_independence_wave_regional_ambition` accepts World Collapse without the ordinary recognized-phase gate. Full-tree countries still need the founding-settlement prerequisite and overlay countries still need their overlay prerequisites.
3. `independence_wave_focus_open_regional_ambition` sets `independence_wave_post_release_ambition_factor` to `constant:independence_wave_allocation_factor.world_collapse_ambition`, currently `1.35`, and opens high-chaos actions immediately.
4. `can_open_independence_wave_high_chaos_lane` lets a World Collapse country enter after the registered ambition opens without requiring the Radical Sovereignty government settlement. Lower chaos bands require Radical Sovereignty or the explicit evolution flag.
5. `independence_wave_focus_add_revisionist_pressure` multiplies every high-chaos focus's league-danger pressure by the same `1.35` World Collapse factor.
6. AI weights strongly prefer the regional ambition, high-chaos sovereignty, and revisionist-charter focuses when the World Collapse trigger is true.

## Regional and package adaptation

The scripted localisation selectors use the validated package metadata rather than a generic country label:

- 14 region-specific transport focus titles
- 14 region-specific ambition focus titles
- 7 package-archetype economy focus titles
- 9 force-profile military focus titles
- 7 internal-power first-center titles
- 7 internal-power second-center titles

These resolvers live in the new focus-owned scripted-localisation file. The existing `common/scripted_localisation/006_independence_wave_scripted_localisation.txt` force-template and presentation resolvers were not edited or replaced.

The effect layer likewise writes one exact region, archetype, force-profile, ambition-family, and internal-power flag. The signature focus only publishes `independence_wave_signature_extension_anchor_reached`; it does not pretend the bespoke country module exists.

## Icon dependencies

The framework references only these stable sprites from the main-agent-owned `interface/006_independence_wave.gfx`:

- `GFX_goal_independence_wave_founding_administration`
- `GFX_goal_independence_wave_constitutional_state`
- `GFX_goal_independence_wave_popular_councils`
- `GFX_goal_independence_wave_traditional_restoration`
- `GFX_goal_independence_wave_military_emergency`
- `GFX_goal_independence_wave_patron_client`
- `GFX_goal_independence_wave_recognition_diplomacy`
- `GFX_goal_independence_wave_army_integration`
- `GFX_goal_independence_wave_infrastructure_authority`
- `GFX_goal_independence_wave_former_host_settlement`
- `GFX_goal_independence_wave_league_congress`
- `GFX_goal_independence_wave_regional_formable`
- `GFX_goal_independence_wave_high_chaos_sovereignty`

All thirteen sprite identifiers and their shine variants are present in the unified Event 6 GFX file. No new icon filename is required by this tranche.

## Audit evidence

- Parsed all 115 focus and shared-focus blocks and confirmed each has a unique ID, icon, coordinates, cost, availability, completion reward, custom tooltip, and AI weight.
- Checked every prerequisite and mutual-exclusion reference against the focus ID set. No missing focus reference remains.
- Checked all 106 script-constant references against loaded `common/script_constants` definitions. No undefined constant remains.
- Checked every Event 6 scripted trigger and effect call in the owned files against loaded trigger and effect definitions. No undefined call remains.
- Checked all focus names, descriptions, and 115 custom tooltips against the localisation file. No localisation key remains missing.
- Confirmed the localisation file is UTF-8 with BOM and uses keys without `:0` or leading whitespace.
- Confirmed all thirteen referenced icon sprites exist in `interface/006_independence_wave.gfx`.
- Reviewed route commitments, patron ownership, former-host outcomes, league proposals, World Collapse access, additive-tree safety, and generation cleanup as separate scenarios.

The main agent still needs to run the project `chaosx_focus_tree_auditor` after applying root and package wiring, because that audit must inspect the integrated package contracts rather than this isolated framework alone.

## Balance notes

- Focus durations are centralized at 5, 7, and 10 weeks.
- Major focuses change Event 6 values, buildings, equipment, doctrine, network or league values, bilateral ledgers, route state, or decision access. Flat stability and war support are supporting rewards rather than the primary result.
- No focus stores political power, spawns free divisions, loops free units, or relies on passive checklist rewards.
- Government route caps provide stronger statehood gains, but the patron route pays a legitimacy cost and radical rewards increase instability and reduce recognition.
- Military policy choices are five real pairs: civilian control versus autonomy, mass reserve versus professional core, domestic versus foreign arms, border defense versus reclamation, and league standardization versus independent command.
- The World Collapse 1.35 pressure multiplier increases danger progression but leaves the accepted country count unchanged.

## Future extension points

- Package-owned signature modules should attach several focuses, decisions, events, and a real end state to `independence_wave_signature_extension_anchor_reached`.
- Internal-power decisions can move `independence_wave_internal_power_balance` further and read the three settlement flags.
- Formable packages can consume `independence_wave_formable_integration_ready` after their exact territorial and consent checks pass.
- Regional ambition decisions can consume `independence_wave_post_release_ambition_factor` when calculating package-specific escalation or integration pressure.
- Formed countries should use `post_formation_overlay` and a reviewed owning-tree insertion rather than inheriting the full release tree automatically.

## Simplifications, omissions, and blockers

No fallback, generic per-country copy, placeholder route, or unapproved simplification was used inside the framework.

The generation cleanup call is integrated. The framework is not fully integrated until the main owner applies each release assignment mode, existing-tree shared-focus insertion, and exact package adapter call described above. Because those package files were outside this subagent's ownership, this tranche must not be used as evidence that any of the 206 packages is content-ready. The integrated focus-tree auditor remains required before the overall Event 6 completion claim.
