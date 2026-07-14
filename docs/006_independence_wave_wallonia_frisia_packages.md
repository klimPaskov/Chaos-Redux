# Event 006 Wallonia and Frisia Packages

## Scope

This package layer implements the playable country content for two accepted Event 006 packages:

| Package | Tag | Anchor | Depth | Economy | Opening force |
| --- | --- | ---: | --- | --- | --- |
| IW-006 Wallonia | AFX | State 34 | Regional | Industrial breakaway | Industrial security, score 61 |
| IW-007 Frisia | AGX | State 36 | Standard | Port or island | Coastal maritime, score 44 |

The implementation is isolated from the shared allocator and executor. Regional setup, final-validation, and cleanup adapters are registered through the parent-owned generic dispatchers. The combined gameplay, transaction, localisation, and asset audit passed, so the dormant AFX and AGX histories carry `independence_wave_package_content_ready` and the pre-release registry may select these two exact adapters.

## Runtime setup sequence

Each exact package setup follows the same fail-closed order:

1. Verify the persistent package ID, the temporary executor package ID, the original tag, the former-host event target, and the exact anchor state.
2. Install the provisional political authority and party landscape.
3. Prove that the custom-tag history supplied the baseline civilian-economy, export-focus, and volunteer-only laws together with the civic authority and named commander.
4. Set `independence_wave_command_roster_ready` only after the commander is confirmed as a corps commander.
5. Initialize the package crisis value or values and install the appropriate starting national spirit.
6. Assign `independence_wave_focus_assignment.full_framework` and load the shared Event 006 focus tree.
7. Publish only the routes accepted for that package, then register former-host routes, the internal power struggle, regional ambition, network and league access, and the Low Countries formable family.
8. Load the researched package force mapping and call the dynamic starting-force transaction.
9. Enable the package AI profile.
10. Run the prepared package proof. Only a passing proof sets the package setup-complete flags and returns a successful setup-dispatcher result.

The prepared proof includes baseline laws, roster, focus mode, accepted and rejected routes, power struggle, formable family, force-mapping generation lock, force application, package AI flag, crisis idea, persistent anchor and former-host pointers, and the exact capital. After the shared activation pass publishes reversible registries, a separate live proof requires activation readiness, aligned active-country and network-member arrays, and exact membership in both registries before the shared transaction may commit durable history.

## Wallonia, IW-006

### Political authority and command

The Walloon Provisional Assembly is a fictional collective institution representing mineworkers, steel engineers, municipal magistrates, and reserve security officials. It can lead the constitutional, labor, or patron settlement. Marcel Delcourt is a fictional former industrial engineer and reserve commander. He is recruited as a real corps commander before any opening formations are created and leads the emergency-military settlement.

Accepted political routes:

- Constitutional Compact, led by the Walloon Provisional Assembly under centrism.
- Workers' Industrial Charter, led by the Assembly under socialism.
- Emergency Works Command, led by Marcel Delcourt under despotism.
- Patron Industrial Mandate, led by the Assembly under oligarchism.

Traditional-restoration and radical-sovereignty routes remain unavailable. The internal power struggle is civilians against the army.

Accepted former-host routes are negotiation, guarded frontier, association, and reclamation. The former host is dynamic and normally resolves to Belgium through the executor's saved event target.

### Industrial-continuity mechanic

`independence_wave_afx_industrial_continuity` measures whether the Sambre-Meuse mines, steelworks, rail junctions, and factory guards still function as a common system. Wallonia begins with `afx_disrupted_industrial_belt`. Securing the threshold swaps it for `afx_sambre_meuse_industrial_covenant`. The lifecycle can regress if a failed project pushes continuity below the threshold.

The timed `Prevent an Industrial Stoppage` crisis gives the country 360 days to stabilize the system. The player can commit shared Event 006 material packages to:

- keep mine pumps running,
- secure Sambre-Meuse rail junctions,
- settle industrial ledgers with the dynamic former host,
- unify factory guards under civilian warrants and professional officers.

Actions take 75 to 180 days. The emergency pump and rail projects sequentially commit the one spare civilian factory that a one-state opening can realistically provide, then pay the shared light-administration command-power and manpower package. The rail project still contributes security progress, but it does not compete with automatic division reinforcement for the opening equipment stockpile. The stronger factory-guard project consumes manpower, Army Experience, infantry equipment, and support equipment. The former-host settlement consumes command power plus trains or convoys. Capital loss, war during negotiations, or origin termination cancels the relevant work. Failed work reduces industrial continuity and statehood values while increasing founding instability. Completing the pumps and rail junctions supplies the baseline 150-day stabilization path; the guard and former-host projects provide stronger but more demanding alternatives.

After recognition and stabilization, the Meuse Industrial Conference raises network standing and opens the package's Meuse and Low Countries political identity. It uses the shared strategic cost and takes 300 days.

## Frisia, IW-007

### Political authority and command

The Friesland Coastal Council is a fictional collective institution representing municipalities, harbor administration, dike engineering, and the coastal constabulary. It can lead every accepted political settlement. Sjoerd Hoekstra is a fictional coastal constabulary commander recruited as a real corps commander before the coastal-maritime force package is applied.

Accepted political routes:

- Constitutional Water Board, led by the Council under centrism.
- Coastal Labor Councils, led by the Council under socialism.
- Patron Harbor Mandate, led by the Council under oligarchism.

Traditional-restoration, emergency-military, and radical-sovereignty routes remain unavailable. The internal power struggle is labor councils against permanent ministries.

Accepted former-host routes are negotiation, guarded frontier, and association. Reclamation is not published. The former host is dynamic and normally resolves to the Netherlands through the executor's saved event target.

### Waterline mechanic

Frisia tracks two independent values:

- `independence_wave_agx_waterline_integrity` for dikes, pumps, sluices, and evacuation roads.
- `independence_wave_agx_coastal_security` for ports, harbor stores, maritime approaches, and guard readiness.

Both values must reach their thresholds to replace `agx_exposed_waterline` with `agx_dike_and_coast_authority`. Losing either threshold restores the exposed-waterline spirit.

The timed `Hold the Waterline` crisis gives the country 540 days to secure both systems. The player can commit shared Event 006 material packages to:

- inspect pump stations,
- organize a harbor watch,
- secure the inland rail link,
- train dike guards,
- reconcile water-board records with the dynamic former host.

Actions take 75 to 180 days and divide their gains between waterline integrity and coastal security. The pump survey uses the same one-factory emergency-administration predicate as Wallonia, while the harbor watch and inland rail link make two sequential light commitments from the opening coastal logistics reserve. Interrupted work reduces one or both values and worsens the shared founding settlement. Pump inspection, harbor watch, and inland rail security together reach both thresholds in 270 days. The design therefore prevents the country from solving coastal defense merely by buying equipment or solving flooding merely by raising troops, while avoiding dependence on Army Experience or a living former host.

After recognition and stabilization, the North Sea Coastal Conference raises network standing and connects the North Sea coastal hook to the negotiated Low Countries formable family. It uses the shared strategic cost and takes 300 days.

## Shared framework interactions

Both packages receive the full shared Event 006 focus framework. They register:

- a package-specific internal power struggle,
- the appropriate government-route subset,
- package-appropriate former-host route subsets,
- the regional ambition family,
- an Event 006 network membership and league route,
- `independence_wave_formable_family.low_countries_federation`,
- package hooks for the Meuse industrial corridor or North Sea coast.

The Low Countries family is negotiated rather than imposed. Constitutional and popular-council governments receive the strongest package AI preference for the regional conferences. Patron governments remain valid package routes but cannot use an independent conference while the shared client-route lock is active.

Route formalization is deliberately payable from each package's proven opening economy. Wallonia's four settlements and Frisia's constitutional and popular settlements use the one-factory light-administration commitment; the political outcomes still apply route-specific administrative, security, or diplomatic progress. Frisia's patron settlement uses one remaining light coastal-logistics commitment after its 270-day crisis baseline. Formalization shares the serialized package-project lane, requires control of the capital, and can be attempted again after an occupation cancels the timer. No route government depends on an unproven second spare civilian factory, starting Army Experience, or a landlocked opening train reserve.

All package missions, projects, formalizations, and conferences use generation-local state instead of engine-persistent `fire_only_once`. Package predicates, active-decision checks, and completion or failure flags prevent repetition during one live origin. Regional cleanup explicitly removes every active package mission and decision without applying its result, then clears those flags. An accepted Annexation and Return recreation can therefore receive fresh timers and costs and complete the full package decision layer in a later Event 006 generation, including when reset and preparation share one effect chain.

The force layer remains authoritative. IW-006 loads the researched industrial-security mapping. IW-007 loads the researched coastal-maritime mapping. The package code does not duplicate templates, unit counts, stockpiles, or inheritance rules.

## AI behavior and balance intent

Wallonia prioritizes infantry, support equipment, artillery, trains, arms factories, and infrastructure. Frisia prioritizes infantry, support equipment, trains, convoys, infrastructure, and coastal defenses. Both avoid initiating wars while they remain founding states and the dynamic former-host ledger shows no severe threat. A severe former-host threat activates a defensive buildup. Wallonia's emergency route adds a stronger army and artillery overlay. Frisia's AI defers the optional standard-convoy former-host settlement until both waterline thresholds are secure, preserving the two light logistics payments required by its baseline crisis path.

Important balance scenarios:

1. A fragile one-state Wallonia can stabilize through the complementary pump and rail projects in 150 days, but it must commit its spare factory, manpower, and command attention twice; automatic reinforcement cannot consume either project's decision reserve. Alternate projects remain valuable for statehood progress.
2. A hostile former host cannot be ignored. The dynamic threat ledger shifts AI behavior even when the former host is not the historical Belgian or Dutch tag.
3. Frisia must improve both dike administration and coastal security. Its 270-day baseline path combines pump, harbor, and rail work; completing only civil work or only guard work cannot end the crisis.
4. Capital loss during a package project produces a real setback instead of a free cancellation.
5. The regional conferences require recognition, a stable package mechanic, network membership, an unlocked independent diplomatic posture, and the strategic cost.
6. Opening formations cannot appear without a recruited commander, a valid researched mapping, the exact anchor event target, and the current-generation lock.
7. Every accepted government route can install its package leader and national spirit from the guaranteed post-crisis opening reserve: six settlements use one spare factory, and Frisia's patron route uses the sixth convoy remaining after its two baseline logistics commitments.
8. Route formalization cannot overlap recovery work or complete while the capital is occupied; a canceled timer remains available after the capital is recovered.

## Cleanup and lifecycle ownership

`independence_wave_dispatch_wallonia_frisia_package_cleanup` removes package ideas, crisis variables, route-government flags, decision outcome flags, AI profile flags, and regional hooks. It is registered in the generic cleanup dispatcher, which both the shared reset and successful origin-end path call before clearing the package identity needed by the regional adapter.

Character recruitment remains in the dormant custom-tag history files, following the character-system contract. Leaders and commanders are not recruited from on actions or scripted effects. They are not retired during origin cleanup because the tag continues to exist and may retain its post-origin government.

## Visual inventory and wiring

### Required package portraits

| Character | Sprite | Final DDS | Registration |
| --- | --- | --- | --- |
| Walloon Provisional Assembly | `GFX_portrait_AFX_walloon_provisional_assembly` | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_provisional_assembly.dds` | `interface/006_independence_wave_region_01_portraits.gfx` |
| Marcel Delcourt | `GFX_portrait_AFX_walloon_reserve_commander` and `GFX_portrait_AFX_walloon_reserve_commander_small` | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` and `portrait_AFX_walloon_reserve_commander_small.dds` | `interface/006_independence_wave_region_01_portraits.gfx` |
| Friesland Coastal Council | `GFX_portrait_AGX_friesland_coastal_council` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` | `interface/006_independence_wave_region_01_portraits.gfx` |
| Sjoerd Hoekstra | `GFX_portrait_AGX_friesland_coastal_commander` and `GFX_portrait_AGX_friesland_coastal_commander_small` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` and `portrait_AGX_friesland_coastal_commander_small.dds` | `interface/006_independence_wave_region_01_portraits.gfx` |

### Required flags

The package uses only the authorized unsuffixed tag flags:

- `gfx/flags/AFX.tga`, `gfx/flags/medium/AFX.tga`, and `gfx/flags/small/AFX.tga`.
- `gfx/flags/AGX.tga`, `gfx/flags/medium/AGX.tga`, and `gfx/flags/small/AGX.tga`.

No ideology or cosmetic flag variants are referenced.

### Reused Event 006 icons

No additional focus, idea, or decision icon files are required by this package layer. It reuses sprites registered in `interface/006_independence_wave.gfx`:

- Ideas: `GFX_idea_independence_wave_founding_identity`, `GFX_idea_independence_wave_improvised_government`, `GFX_idea_independence_wave_fragmented_command`, and `GFX_idea_independence_wave_patron_pressure`.
- Decisions: `GFX_decision_independence_wave_government_actions`, `GFX_decision_independence_wave_army_integration_actions`, `GFX_decision_independence_wave_depot_border_actions`, `GFX_decision_independence_wave_former_host_negotiations`, `GFX_decision_independence_wave_patron_aid`, `GFX_decision_independence_wave_league_votes`, and `GFX_decision_independence_wave_formable_proclamation`.

Reusing the established Event 006 visual language is the intended framework design, not a fallback or placeholder.

## Source references consulted

The implementation was checked against the offline Paradox wiki snapshot for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, Character modding, National focus modding, Division modding, and Portrait modding.

Vanilla documentation consulted includes `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/modifiers_documentation.md`, `documentation/on_actions_documentation.md`, `documentation/script_concept_documentation.md`, `common/ai_strategy/_documentation.md`, `common/script_constants/documentation.md`, `common/characters/_documentation.md`, and the decision and country history documentation. Vanilla precedents included Belgian defense decisions, Dutch inundation and waterline content, institutional leaders, character promotion, and self-removing AI strategies.

## Future plans and extension ideas

- Add later package events that react to a failed industrial-stoppage or waterline mission without bypassing the shared Event 006 evolution system.
- Let a durable Low Countries league coordinate Meuse rail standards and North Sea flood-response stores through member-scoped decisions.
- Add package-specific focus modules only if the accepted Event 006 specification promotes either package to signature depth.
- Add additional commanders or advisors only after a researched roster and portrait plan replaces the current deliberate two-character package scope.

## Integration status and blockers

The isolated gameplay package files are implemented. The shared generic dispatchers register the setup, final-validation, and cleanup adapters; the four-pass transaction owns reversible preparation, activation, exact live validation, durable commit, rollback, and successful origin-end cleanup. The parallel art tranche's validated portrait and flag files are present, and all six AFX and AGX portrait sprites are registered in `interface/006_independence_wave_region_01_portraits.gfx`. The unsuffixed flag triplets require no `.gfx` registration.

The independent country-package audit and parent integration review granted `independence_wave_package_content_ready` to the dormant AFX and AGX histories after confirming exact setup/live proofs, generation-safe cleanup, complete localisation, six registered portraits, and both flag triplets. No gameplay fallback, placeholder leader, generic commander, generic route, or substitute flag was used.
