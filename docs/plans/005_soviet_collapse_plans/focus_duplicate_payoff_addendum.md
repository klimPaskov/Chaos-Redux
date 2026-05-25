# Event 005 Focus Duplicate Payoff Addendum

## Current Depth Status

Event 005 focus trees are source-valid and much deeper than the first broad scaffold, but several high-volume reward clusters still read as helper payoffs rather than player-facing mechanics. The next pass should not add focus count. It should turn the most repeated focus payloads into visible decisions, missions, route states, and capstone payoffs.

The previous sidecar `event005_focus_duplicate_payoff_addendum.md` already targets Ukraine officer/democratic pairs, Baltic legal/defense pairs, Don Host mediation/oath boards, and the MFR steel/CFR rivalry pair. This addendum focuses on the next five priority clusters.

## Evidence

- Final clean merged Part 3 requires focuses and decisions to affect visible mechanics, especially sponsor influence, League cohesion, local support, patronage risk, and mission surfaces.
- Final clean merged Part 5 rejects focus trees dominated by flat PP, stability, equipment, factories, or generic modifier rewards, and requires focus-decision interaction.
- Final clean merged Part 6 requires every splinter and internal republic package to have distinct playable identity, decisions, AI, local league or influence interaction, and validation notes.
- Current source evidence: `common/national_focus/005_soviet_collapse_*.txt` still contains very high-use helper families: `soviet_collapse_apply_focus_legal_recognition` 294 uses, `military_consolidation` 266, `depot_and_supply_control` 261, `league_preparation` 211, and `foreign_channel` 171.
- Current decision evidence: Event 005 already has relevant decision categories for breakaways, foreign patrons, regional factions, Central Asia, CFR/MFR, and compact high-chaos actors. The payoff pass should wire focus progress into those surfaces before inventing more branches.

## Core Expansion Thesis

Repeated helper rewards should become route-facing unlocks. A focus can still call a shared helper, but the player should also see what changed: a new decision, a stronger existing decision, a timed objective, a named project, an influence stance, a local compact, or a capstone choice.

## Accepted Design Constraints

- Preserve existing focus IDs, tree layout, prerequisites, and country tags unless the main agent explicitly expands scope.
- Do not add whole-world on actions.
- Prefer existing Event 005 categories and helper patterns before adding new surfaces.
- Keep tooltip text concise; use one readable custom effect tooltip when a focus unlocks or upgrades a decision family.
- Any new visible decision/focus text must update localisation and icon/docs surfaces in the implementation pass.

## Top 5 Immediate Implementation Additions

### 1. Custom Splinter Diplomatic Plan Cluster

Focus IDs/tags:
`FTH_diplomatic_plan`, `BSC_diplomatic_plan`, `TNC_diplomatic_plan`, `ALA_diplomatic_plan`, `BBH_diplomatic_plan`, `KRS_diplomatic_plan`, plus the matching `*_diplomatic_plan` focuses for `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `UWD`, and other broad custom splinter trees.

Current shallow pattern:
Most of these focuses combine `custom_splinter_league_identity`, `legal_recognition`, `foreign_channel`, and `league_preparation`. That proves the branch is valid, but the player still mostly receives abstract recognition/League progress.

Intended route identity:
Each splinter should decide how it speaks to outsiders: anti-puppet commune diplomacy, caravan/oasis mediation, sailor-worker port recognition, command continuity, archive custody, village congress legitimacy, host passage bargains, or arsenal labor representation.

Player-visible payoff:
Unlock or upgrade one route-specific diplomatic action in the existing breakaway, foreign-patron, or regional-faction decision surface. Examples: anti-puppet clause, balanced sponsor desk, League observer corridor, non-domination pact, neutral port/corridor statute, archive inspection guarantee, or caravan mediation board.

Minimal affected surface:
Focus rewards in `005_soviet_collapse_custom_splinters.txt`; existing decision categories in `005_soviet_collapse_decisions.txt`; localisation/tooltips; decision icons only if an existing icon is not appropriate.

### 2. Custom Splinter War Plan / Enemy Front Cluster

Focus IDs/tags:
`FTH_war_plan`, `BSC_war_plan`, `TNC_war_plan`, `ALA_war_plan`, `BBH_war_plan`, `KRS_war_plan`, `UDC_war_plan`, `SDZ_war_plan`, `GAC_war_plan`, `DHC_war_plan`, `KHC_war_plan`, `FEV_war_plan`, `SZA_war_plan`, `UWD_war_plan`, and equivalent `*_enemy_front` follow-ups.

Current shallow pattern:
The route typically resolves through `custom_splinter_enemy_front_identity` plus `military_consolidation` and/or `depot_and_supply_control`. That makes different regimes fight similarly.

Intended route identity:
War plans should define the kind of front the tag fights: commune columns, caravan pass defense, naval port denial, command-district counteroffensive, security cordon, village ambush belts, host river crossings, Far Eastern harbor defense, Siberian rail depth, or Ural arsenal front.

Player-visible payoff:
Unlock one active war-preparation objective or decision keyed to route terrain. The action should ask for a real commitment: hold a named port/pass/rail hub, spend equipment and command power, garrison a depot belt, open a supply route, or prepare an offensive staging area.

Minimal affected surface:
Focus rewards and existing decision/mission categories. Avoid adding a new mission pool unless the existing breakaway/regional category cannot carry the objective cleanly.

### 3. Central Asian League And Steppe Compact Cluster

Focus IDs/tags:
`central_asia_soviet_collapse_southern_republics_coordinate`, `central_asia_soviet_collapse_loose_southern_pact`, `central_asia_soviet_collapse_the_south_survives_together`, `BSC_central_asian_defense_council`, `TNC_central_asian_defense_council`, `ALA_central_asian_league_draft`, and related `BSC`/`TNC`/`ALA` caravan, pass, cotton, water, and mediation focuses.

Current shallow pattern:
The focuses set useful flags and call League/preparation helpers, while `005_soviet_collapse_central_asia_league_decisions.txt` already has water council, cotton rail, caravan board, member vote, mediation, and settlement decisions. The connection can be more deliberate.

Intended route identity:
Central Asia should play as a water, cotton, caravan, pass, and mediation compact, not only as a generic regional League.

Player-visible payoff:
Focuses should graduate the existing Central Asian decisions. Early focuses unlock the surface; route focuses improve specific actions; capstones add a settlement vote or chairmanship effect. The player should see different costs/benefits for local council, military border authority, foreign patronage, and Turkestan federation routes.

Minimal affected surface:
`005_soviet_collapse_republics.txt`, `005_soviet_collapse_custom_splinters.txt`, `005_soviet_collapse_central_asia_league_decisions.txt`, localisation for decision availability/effect text.

### 4. Internal Republic Compact Payoff Cluster

Focus IDs/tags:
`internal_soviet_collapse_northern_republic_accord`, `internal_soviet_collapse_volga_ural_compact`, `internal_soviet_collapse_black_sea_compact_observers`, `internal_soviet_collapse_yakut_arctic_resource_compacts`, `internal_soviet_collapse_tuvan_steppe_compact`, `internal_soviet_collapse_trade_oaths_with_neighbors`, `internal_soviet_collapse_free_republics_wire`, and `internal_soviet_collapse_many_republics_common_front`.

Current shallow pattern:
The internal tree is compact and tag-aware, but several compact/accord/common-front focuses still mostly look like legal, League, depot, or military helper endpoints.

Intended route identity:
Internal republics should become small but real compact states: northern rail/timber accord, Volga-Ural oil/workshop compact, Black Sea peninsula settlement, Yakut Arctic resource board, Tuvan steppe compact, and mutual-defense common front.

Player-visible payoff:
Unlock tag-family compact decisions: rail/timber contracts, oilfield security, Black Sea observer vote, Arctic convoy/resource board, steppe border-road pact, or common-front volunteer standards. These should also affect AI route choice and Moscow reintegration/federal-compact reactions.

Minimal affected surface:
Internal republic focus rewards, existing breakaway/regional decision categories, AI weights where the compact matters, localisation. No new country packages.

### 5. Factory And Special-Actor Project Board Cluster

Focus IDs/tags:
For `CFR`: `CFR_cities_first`, `CFR_rails_first`, `CFR_factories_first`, `CFR_contracts_first`, `CFR_apartment_blocks_for_loyalty`, `CFR_buy_peace_with_concrete`, `CFR_pour_the_final_foundation`.

For `MFR`: `MFR_orders_outlive_ministries`, `MFR_arsenal_ration_law`, `MFR_who_owns_the_rifle`, `MFR_factory_war_cabinet`, `MFR_the_arsenal_state`, `MFR_eternal_arsenal_marches`.

For compact special actors: `PRA_rails_over_capitals` / `PRA_the_pale_line_endures`, `TSC_starfall_mandate` / `TSC_the_quiet_sky_settlement`, `RMC_resurrection_without_state` / `RMC_republic_of_witnesses`, `DSC_congress_of_the_dead_army` / `DSC_republic_of_roll_calls`, `NRF_northern_revenant_fleet` / `NRF_port_republic_of_the_living`, `ICD_commissariat_without_end` / `ICD_citizens_after_death`.

Current shallow pattern:
CFR/MFR already have categories, but many focus rewards still feel like construction/arsenal helper increments. Compact special actors often complete endgame identity directly while their decision categories repeat the same low/medium action pattern.

Intended route identity:
CFR should run project boards; MFR should run arsenal orders and client contracts; compact special actors should make the player choose whether their strange identity becomes a governed settlement or an extreme mandate.

Player-visible payoff:
CFR focuses should add or upgrade project slots in `soviet_collapse_reconstruction_state`. MFR focuses should add quota tiers or client-order variants in `soviet_collapse_arsenal_state`. Special-actor capstone focuses should unlock the decisive category action or make it cheaper/stronger, not silently replace the decision.

Minimal affected surface:
`005_soviet_collapse_factory_successors.txt`, compact actor focus blocks in `005_soviet_collapse_custom_splinters.txt`, existing CFR/MFR and special-actor decision categories, localisation/tooltips.

## Deeper Branch Additions

After the immediate pass, the main agent can add route-specific aftermath events only where the decision loop proves useful in play: Central Asian chairmanship dispute, internal republic compact vote, factory-state merger/rivalry escalation, or special-actor settlement versus mandate report event. These are optional follow-ups, not required for the first implementation pass.

## Duplicate Content To Merge Or Remove

- Do not remove the named focus IDs.
- Merge repeated flat helper-only payoffs into visible unlock tooltips.
- Remove any focus payload where the only new player-facing result is PP, stability, war support, one factory, one equipment batch, or another hidden flag.
- Avoid duplicating new decisions per tag when a tag-family decision with route flags can carry the distinction cleanly.

## Visual Progression Plan

Use existing focus icons unless a new decision action needs a distinct decision icon. If new icons are required, route them through `chaos-redux-event-assets` / `chaosx_icon_artist`. Priority visuals: diplomatic desk, war-plan board, Central Asian compact board, internal compact seal, CFR project ledger, MFR quota ledger, and special-actor mandate/settlement choice icons.

## Lore And Readability Plan

Tooltips should name the institution the focus creates, not the helper it calls. Use terms like "League observer corridor", "water-sharing council", "Volga-Ural compact", "reconstruction project board", "arsenal quota order", or "starfall mandate". Avoid update-history wording and avoid exposing long mechanical lists in focus hover text.

## AI And Balance Notes

AI should prefer the new decisions when the matching route pressure exists: war state for war plans, foreign appetite or sponsor risk for diplomacy, League cohesion for compact choices, low stability/local authority for settlement boards, and chaos tier for extreme mandates. Costs should use existing low/medium custom splinter costs or existing category costs first; only add new tuning constants if the same value is reused across several categories.

## Validation And Audit Follow-Up

After implementation:

- Re-run focus audit for the five clusters above and verify the named focuses no longer end as helper-only payoffs.
- Re-run decision/mission audit if any new objectives or category actions are added.
- Verify no category clutter spike: decision unlocks should be route-gated and cooldown-gated.
- Check localisation for concise unlock/effect text and no raw trigger clutter.
- Check AI blocks for route-aware use, not base-only weights.

## Queued Future Ideas

- Add short report events for Central Asian compact chairmanship, internal republic compact votes, and special-actor settlement/mandate choices.
- Add achievements only after the mechanics survive a focus and decision audit.
- Consider one shared in-event detail section that lists which compact/project boards have formed, but only if the current event-detail UI can present it cleanly.
