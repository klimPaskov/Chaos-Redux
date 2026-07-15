# Event 006: Rhineland and Bavaria Gameplay Packages

## Overview

This document describes the package-owned gameplay implemented for Event 006 package `IW-008` (Rhineland, `RHI`) and package `IW-009` (Bavaria, `BAY`). Both packages use the shared full Independence Wave focus framework and add their own rosters, portraits, founding crises, political settlements, host negotiations, ambitions, network projects, high-chaos actions, AI profiles, and lifecycle ideas.

The implementation does not create tag history files, duplicate vanilla characters, override global portrait sprites, or spawn bespoke units. Existing dormant vanilla tags are configured only after the Event 006 transaction has prepared their origin. The shared dynamic force layer remains authoritative for starting formations and reinforcement packages.

## Runtime setup

The bounded dispatcher adapters are:

- `independence_wave_dispatch_rhineland_bavaria_package_setup`
- `independence_wave_dispatch_rhineland_bavaria_package_final_validation`
- `independence_wave_dispatch_rhineland_bavaria_package_cleanup`

The parent Event 006 transaction calls these adapters from its setup, final-validation, and cleanup dispatchers, and its immutable adapter registry recognizes the exact ID/tag pairs for package IDs 8 and 9. Readiness is not stored in dormant vanilla history. Both rows remain absent from the static content-attestation registry until their independent package audits are complete. Rhineland additionally depends on the shared `FORM-04` identity transaction and flag package. Bavaria has a South German restoration ambition and no shared formable dependency.

Each prepared proof checks the exact tag, package ID, region, depth, archetype, anchor, former-host pointer, capital, laws, command roster, full focus assignment, allowed routes, power struggle, ambition policy, force mapping, applied starting force, lifecycle, and AI profile. Both proofs require `independence_wave_radical_sovereignty_route_excluded`, which keeps their accepted route matrices authoritative when Evolution 5 applies Open Sovereignty; other countries retain the shared evolution behavior. Rhineland also proves that `IW-010` Ajax is not active, preserving the shared `RG-RHINE-SAAR` exclusion.

## Characters and portraits

The package creates stable institutional characters with guarded `generate_character` calls and reapplies their exact portraits on every setup:

- `RHI_independence_wave_provisional_directorate`
- `RHI_independence_wave_river_commandant`
- `BAY_independence_wave_state_council`
- `BAY_independence_wave_mountain_commandant`

The two commandants have distinct corps-commander roles and do not reuse vanilla political figures as generic military officers. Institutional leaders and commanders use independently generated HOI4-painted masters, with separate `156x210` large DDS files and `50x67` army thumbnails for the commandants.

`RHI_josef_friedrich_matthes` is used only when he remains recruited by Rhineland. Package setup applies `GFX_portrait_RHI_josef_friedrich_matthes` with `set_portraits`, while the provisional directorate remains the opening government. Matthes becomes leader only for the labor settlement; when he is unavailable, the established directorate retains office as the designed institutional outcome.

`BAY_rupprecht_of_bavaria` is used only when Bavaria still has the character and Germany does not. Package setup applies `GFX_portrait_independence_wave_BAY_rupprecht_of_bavaria` with `set_portraits`, while the State Council remains the opening government. Rupprecht becomes leader only for the traditional restoration settlement; the State Council acts as the institutional regency if he is unavailable.

Cleanup restores both vanilla character portraits. No `.gfx` character sprite is globally replaced.

### Advisor offices

Each package recruits three fictional specialists with independently composed `65x67` advisor dossier cards:

- Rhineland: Municipal Customs Administrator, Rail and Public Works Liaison, and River Defense Planner.
- Bavaria: District Finance Administrator, Estates' Constitutional Liaison, and Alpine Supply Inspector.

Their substantial traits affect customs and consumer burdens, rail and infrastructure construction, river defense and planning, district finance, constitutional stability, or alpine logistics. Hiring costs and route-aware AI weights are centralized in `common/script_constants/006_independence_wave_nwe_advisor_constants.txt`. The advisors are visible only for their exact active Event 006 package and never overwrite either tag's vanilla advisor content.

Hidden setup event `chaosx.nr6.10` recruits these static records within the frozen release chain. The package adapter will not publish success unless the exact three-advisor roster is present, and no scripted effect or on action contains `recruit_character`.

## Starting forces

Both packages call `independence_wave_load_force_package_mapping` and `independence_wave_apply_dynamic_starting_force` after their command rosters prove ready.

### Rhineland (`IW-008`)

- Shared force profile: `regular_defectors`
- Military tradition: package constant `p8` = 70
- Reinforcement mask: `p8` = 1612
- Package features: secure depots, converted defectors, factory and rail guards, professional officers, capital defense, border defense, and inherited air support where the shared ledger permits it

### Bavaria (`IW-009`)

- Shared force profile: `regular_defectors`
- Military tradition: package constant `p9` = 75
- Reinforcement mask: `p9` = 1676
- Package features: secure depots, converted defectors, terrain units, professional officers, capital defense, border defense, and inherited air support where the shared ledger permits it

No package-owned OOB or direct unit spawning is present.

## Rhineland gameplay

### Founding crisis

`independence_wave_rhi_corridor_authority` begins at 25. The mission **Keep the Rhine Arteries Open** gives the country 420 days to reach 65. Bridge dispatch, factory and rail guard integration, host customs ledgers, and river crossing security supply distinct administrative, military, and diplomatic ways to reach the threshold. Cancellation after loss of the capital or timeout applies a concrete authority loss and shared legitimacy, recognition, capacity, security, and instability penalties.

The lifecycle swaps from `rhi_divided_river_authority` to `rhi_rhine_civic_industrial_compact` once the threshold is reached.

### Government routes

The package publishes constitutional, labor, emergency military, and patron client routes. It deliberately does not publish traditional or radical-sovereignty routes.

- Constitutional: elected river assembly and civil administration
- Labor: industrial councils, with Matthes when available and the established directorate retaining office otherwise
- Emergency: the river commandant controls crossings and depots
- Patron: foreign credit and transit protection in exchange for political freedom

Each route installs one mutually exclusive route spirit. **Codify Durable Rhenish Independence** is a later capstone that requires a completed founding settlement and stable Corridor Authority.

### Ambition, formable, league, and high chaos

Rhineland selects the shared `rhine_federation` family (`FORM04`), surveys the federation corridor, and can convene the Rhine Congress. The congress sets the shared formation-congress proof and submits a commit request to the selected-family registry. The final family-specific formation transaction remains owned by that shared registry.

The Event 006 package closes the vanilla German reunification decision only after its prepared proof succeeds, preventing the Rhenish FORM04 identity from competing with a second German path. Cleanup reactivates the vanilla decision as part of rollback.

The network project **Charter Network Transit** raises Independence Wave network standing. The regional high-chaos action **Seize the Corridor Authorities** requires regional-power status, the shared high-chaos action unlock, and Open Sovereignty. It does not replace the accepted government settlement and trades legitimacy, recognition, and stability for decisive security and Corridor Authority.

## Bavaria gameplay

### Founding crisis

`independence_wave_bay_civic_settlement` begins at 25 and `independence_wave_bay_mountain_security` begins at 30. The mission **Hold the Bavarian State Together** gives the country 480 days to raise both values to 60. District treasury reconciliation advances civic authority; pass organization advances security; the host ledger advances civic legitimacy; integrating mountain companies advances both.

The lifecycle swaps from `bay_disputed_state_inheritance` to `bay_estates_and_districts_settlement` only when both thresholds are satisfied.

### Government routes

The package publishes constitutional, labor, traditional, and emergency military routes. It deliberately does not publish patron-client or radical-sovereignty routes.

- Constitutional: a restored Landtag and district liberties
- Labor: strong civic mobilization at a cost to mountain security
- Traditional: restoration court led by Rupprecht when available, with the State Council retaining the institutional regency otherwise
- Emergency: mountain guardians gain security while weakening civic consent

The paired visible values make the court-versus-guardians power struggle mechanically relevant. Each government installs one mutually exclusive route spirit. **Codify Durable Bavarian Independence** is the later independence capstone.

### South German ambition and Germany coexistence

Bavaria does not register a new Germany formable and does not select a shared formable family at setup. After opening the regional ambition lane it must choose one of two mutually exclusive policies:

- **Choose a South German Restoration** closes the vanilla German reunification decision and keeps the ambition as a package identity rather than a duplicate Germany tag. It opens **Convene the South German Estates**, a timed diplomatic settlement that strengthens both Bavarian ledgers and network standing without creating a second German formable.
- **Keep the German Reunification Claim** deliberately preserves the vanilla `declare_germany_reunified_decision` and applies recognition and stability tradeoffs appropriate to the broader claim.

The network project **Negotiate an Alpine Supply Accord** raises network standing. The regional high-chaos action **Seize South German Protectorates** requires regional-power status, the shared high-chaos action unlock, and Open Sovereignty. It leaves the accepted government settlement in force while sharply increasing mountain security and damaging civic settlement, legitimacy, recognition, and stability.

## Idea lifecycle and limits

Each package can hold at most two package spirits at once:

1. one founding or mature lifecycle spirit; and
2. one mutually exclusive government-route spirit.

The implementation therefore remains below the requested maximum of three tree-created spirits. No decision creates a third persistent package idea.

## AI behavior

Decision AI prioritizes the founding crisis, reacts to low values, and changes route or ambition preferences according to historical-character availability, former-host threat, regional-power status, and high-chaos access.

Macro AI strategies:

- prioritize infantry, support equipment, artillery, trains, infrastructure, and defensive construction;
- avoid early offensive wars until the country is settled or has become a regional power;
- increase army and fortification priority under severe former-host threat;
- favor civil industry under constitutional, labor, or Rhineland patron settlements;
- increase army production under emergency governments and completed high-chaos actions; and
- remove founding restraint from the decision layer only through the existing regional-power and threat conditions.

The AI uses the same costs, gates, route exclusions, and mission consequences as the player.

## Visual assets and icon wiring

No new decision icon files are required. The package reuses registered Event 006 sprites:

- `GFX_decision_independence_wave_government_actions` -> `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds`
- `GFX_decision_independence_wave_former_host_negotiations` -> `gfx/interface/decisions/006_independence_wave/decision_independence_wave_former_host_negotiations.dds`
- `GFX_decision_independence_wave_depot_border_actions` -> `gfx/interface/decisions/006_independence_wave/decision_independence_wave_depot_border_actions.dds`
- `GFX_decision_independence_wave_army_integration_actions` -> `gfx/interface/decisions/006_independence_wave/decision_independence_wave_army_integration_actions.dds`
- `GFX_decision_independence_wave_integration_missions` -> `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds`
- `GFX_decision_independence_wave_formable_proclamation` -> `gfx/interface/decisions/006_independence_wave/decision_independence_wave_formable_proclamation.dds`
- `GFX_decision_independence_wave_league_votes` -> `gfx/interface/decisions/006_independence_wave/decision_independence_wave_league_votes.dds`

The historical-character portraits are registered in `interface/006_independence_wave.gfx`:

- `GFX_portrait_RHI_josef_friedrich_matthes` -> `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds`
- `GFX_portrait_independence_wave_BAY_rupprecht_of_bavaria` -> `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds`

The package effects reference those stable sprite names directly through `set_portraits`.

The fictional package roster is registered in `interface/006_independence_wave_region_01_portraits.gfx`:

- `GFX_portrait_RHI_independence_wave_provisional_directorate`
- `GFX_portrait_RHI_independence_wave_river_commandant` and its `_small` army sprite
- `GFX_portrait_BAY_independence_wave_state_council`
- `GFX_portrait_BAY_independence_wave_mountain_commandant` and its `_small` army sprite

The six package advisor cards are registered in `interface/006_independence_wave_nwe_advisors.gfx` and live under `gfx/interface/ideas/006_independence_wave/advisors/`. Their full ImageGen masters, explicit crops, processed PNGs, DDS decodes, review sheets, hashes, and manifests live under `docs/assets/006_independence_wave/nwe_advisor_dossiers_2026_07_15/`. The authoritative user-directed HOI4 leader production and review package lives under `docs/assets/006_independence_wave/portrait_regeneration_2026_07_15/`.

## Readiness boundary

Gameplay, AI, localisation, large and small leader portraits, and advisor dossiers are wired. `IW-008` remains fail-closed in automatic and SCN-008 allocation because `FORM-04` still lacks a certified X-ending identity adapter and complete flag triplet. `IW-009` remains fail-closed until an independent package attestation is granted. Its South German ambition is package-owned and does not inherit a `FORM-01`, `FORM-02`, or `FORM-04` dependency. Neither package gains a readiness flag through vanilla history.

## Future plans and suggestions

- Certify the shared `FORM-04` identity adapter, X-ending tag, historical-design research, ImageGen flag triplet, member consent, territory policy, and integration transaction before granting `IW-008` content attestation.
- Give the South German restoration ambition a dedicated regional diplomacy module if a future accepted specification defines its member states and treaty outcomes.
- Add route-specific event writing for the Rhine Congress, the Bavarian restoration court, and the court-versus-guardians settlement after their event IDs and presentation requirements are accepted.
- Consider dedicated decision art only if a later Event 006 asset pass replaces the current shared icon language across all regional packages.
