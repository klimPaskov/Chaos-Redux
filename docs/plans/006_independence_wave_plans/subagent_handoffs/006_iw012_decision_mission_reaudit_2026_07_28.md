# IW-012 decision and mission re-audit — 2026-07-28

## Scope and conclusion

Read-only post-IW-012 audit of the accepted Event 006 decision/mission matrix, shared founding decisions, the Iceland package decisions, mission cleanup, AI, localisation, and route guards.

No gameplay, localisation, GUI, or focus source was changed.

The prior local-package fixes remain sound, but one high-impact shared/local collision remains: `independence_wave_secure_provisional_capital` activates for IW-012 at the same time as `independence_wave_ice_hold_the_harbour` and imposes a four-division capital condition that a fragile IW-012 release cannot meet.

## Issues, sorted by severity

### High — DM-01 can auto-fail every fragile IW-012 release while a second founding crisis is active

`independence_wave_secure_provisional_capital` activates for every `is_independence_wave_active_country` without an IW-012 exclusion in [common\\decisions\\006_independence_wave_decisions.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\006_independence_wave_decisions.txt:20).

Its cancellation guard demands `size > constant:independence_wave_decision_gate.secure_capital_divisions` at [line 35](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\006_independence_wave_decisions.txt:35), and the constant is `3` in [common\\script_constants\\006_independence_wave_decision_constants.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\script_constants\006_independence_wave_decision_constants.txt:268).

Vanilla `divisions_in_state` documentation defines `size >` as a strict comparison, so this requires at least four divisions.

The Event 006 fragile force tier is capped at one to three divisions in [common\\script_constants\\006_independence_wave_force_constants.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\script_constants\006_independence_wave_force_constants.txt:74).

IW-012 receives the scenario force level unchanged at [common\\scripted_effects\\006_independence_wave_packages_region_01_effects.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_effects\006_independence_wave_packages_region_01_effects.txt:324), while the low-intensity scenario selects the fragile tier at [common\\scripted_effects\\006_independence_wave_scenario_effects.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_effects\006_independence_wave_scenario_effects.txt:98).

Therefore a fragile IW-012 start cannot satisfy DM-01, causing immediate cancellation, the `independence_wave_dm01_capital_failed` flag, and the documented legitimacy, capacity, security, and instability loss in [common\\decisions\\006_independence_wave_decisions.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\006_independence_wave_decisions.txt:42).

In parallel, the local harbour mission activates immediately after IW-012 setup at [common\\decisions\\006_independence_wave_ice_decisions.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\006_independence_wave_ice_decisions.txt:15) and has its own 1,440-day survival lifecycle.

The shared active-founding helper omits the local harbour mission entirely at [common\\scripted_triggers\\006_independence_wave_decision_triggers.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_triggers\006_independence_wave_decision_triggers.txt:36), so neither system knows it is competing for the founding-state capacity.

This is a bounded source-level gap, but it needs one design-owner choice before patching because the accepted matrix gives DM-01 to every released country while IW-012 adds a deliberately bespoke survival mission.

Recommended repair choice: declare the harbour crisis the IW-012 replacement for generic DM-01, then add an IW-012 exclusion to DM-01 activation and explicitly connect harbour resolution to the intended founding progression.

Alternative repair choice: preserve both missions, replace DM-01's static four-division test with a force-tier-aware garrison trigger, and include `independence_wave_ice_hold_the_harbour` in `has_independence_wave_active_founding_mission` so downstream generic founding missions cannot overlap the local crisis.

Do not apply only the helper addition, because it does not prevent DM-01 and the harbour mission from activating on the same daily tick.

### Medium — player-facing category text does not disclose the competing founding clocks

The generic founding category tells the player that the capital must be secured before the state survives its first season in [localisation\\english\\006_independence_wave_decisions_l_english.yml](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\localisation\english\006_independence_wave_decisions_l_english.yml:3), while the Iceland category presents the harbour crisis as the emergency-state deadline in [localisation\\english\\006_independence_wave_ice_l_english.yml](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\localisation\english\006_independence_wave_ice_l_english.yml:3).

No localisation is missing, but the overlap makes both descriptions simultaneously true without explaining their relationship.

Resolve this only after selecting the high-severity lifecycle ownership model.

## Decision category lifecycle notes

| Surface | Owner and category | Region and requirement | Duration | Success and failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `independence_wave_secure_provisional_capital` | Shared DM-01, `independence_wave_founding_category` | Every Event 006 active country; capital controlled and at least four divisions in the capital | 75 days | Succeeds on timeout while guarded; cancels with lasting DM-01 failure and ledger losses on capital loss or under-garrisoning | High for IW-012, because its local harbour mission runs concurrently |
| `independence_wave_ice_hold_the_harbour` | IW-012, `independence_wave_ice_north_atlantic_category` | Iceland package, setup complete, capital controlled, former host living | 1,440 days | Resolves when the five local ledgers are stable; fails on timeout, capital loss, former-host loss, or package loss | High only against shared DM-01 |
| Six IW-012 projects | IW-012, North Atlantic category | Material cost, capital control, package validity, and route-specific gates | 120 / 180 / 180 / 300 / 270 / 180 days | One-time flags and ledger progress on completion; project failure on capital/package/host route loss | No intra-package duplicate risk because `has_independence_wave_ice_active_package_project` serializes all six |

The six local projects total 1,230 days, leaving the accepted 210-day margin below the harbour deadline.

## Cost and requirement clarity

The IW-012 projects are not passive political-power exchanges.

Shipping and municipal projects use administration costs and civilian-factory burdens, coastwatch and armed neutrality use security costs, and compact and former-host settlement use diplomatic costs in [common\\decisions\\006_independence_wave_ice_decisions.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\006_independence_wave_ice_decisions.txt:56).

Each cost has a matching `custom_cost_trigger`, `custom_cost_text`, and `complete_effect` payment call.

The compact requires compact support and observed network standing, the charter requires a living non-hostile former host, and armed neutrality requires coastwatch readiness plus an unlocked government route.

The only clarity defect is the unresolved coexistence of the generic four-division capital condition and the package's normal fragile force allocation.

## AI validity and route-lock notes

All six projects have explicit `ai_will_do` priorities in [common\\decisions\\006_independence_wave_ice_decisions.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\006_independence_wave_ice_decisions.txt:81).

The former-host charter checks both former-host existence and no current war, and cancels when either changes.

Armed neutrality checks and cancels on `independence_wave_government_route_locked`, preventing a late route overwrite.

No invalid target, dead target, route-lock, or AI-cost bypass was found in the local project set.

## Localisation, tooltip, cleanup, and exploit-risk notes

All audited decision and category keys resolve in the shared and IW-012 English localisation files.

Each completed local project has a custom effect tooltip, and each cost is represented by custom cost text.

`independence_wave_ice_cleanup_package` removes the harbour mission and all six project decisions at [common\\scripted_effects\\006_independence_wave_ice_package_effects.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_effects\006_independence_wave_ice_package_effects.txt:350), then clears lifecycle flags and local ledgers.

Completion flags and `fire_only_once` on armed neutrality prevent project replay, while project serialization prevents concurrent cost and reward loops.

No local equipment, unit, core, war-goal, or cooldown exploit was found.

## Recommended next change

Owner: Event 006 decision/founding-system maintainer.

Decision required: choose whether IW-012's harbour crisis replaces DM-01 or coexists with it.

If it replaces DM-01, patch [common\\decisions\\006_independence_wave_decisions.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\006_independence_wave_decisions.txt:20) with a package-specific activation exclusion and wire the harbour-success path to the intended generic founding/phase receipt.

If it coexists, add a force-tier-aware capital-garrison scripted trigger, use it at [common\\decisions\\006_independence_wave_decisions.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\006_independence_wave_decisions.txt:30), and register the harbour mission in [common\\scripted_triggers\\006_independence_wave_decision_triggers.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_triggers\006_independence_wave_decision_triggers.txt:36).

## Evidence and validation

Reviewed the accepted decision/mission matrix, IW-012 package implementation and prior IW-012 audit handoff, offline Paradox wiki decision-mission semantics, vanilla decision documentation, vanilla `divisions_in_state` trigger documentation, force-tier constants, scenario force-tier dispatch, and all local decision lifecycle call sites.

Read-only Event MCP artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6205c2fba5d5ddd81646a1c0da8fc251818ab9bd700fbd380bcf3e3518f9024e/5a2f823f803086088b6c9703d181f0b0306b3c6c39e102321fbf2b214c2ebef6/event-impact-dbe4d677c869.json`.

The MCP artifact is partial because its focused impact pass deferred workspace-wide helper projections, so the conclusion above relies on direct source traces for the shared mission, helper, and force-tier paths.

No GUI inspection was performed because this audit found no IW-012 decision-owned GUI defect and made no GUI patch.

Meaningful runtime validation was intentionally not run because this was a read-only audit and repository policy assigns live game validation to the user.

## Remaining issues

The high-severity DM-01/IW-012 ownership conflict remains unpatched pending a design-owner choice.

No simplifications were made in this audit.
