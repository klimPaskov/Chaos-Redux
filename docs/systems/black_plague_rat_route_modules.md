# Black Plague Rat Route Modules

Event 20 keeps one reusable Rat Nation carrier, `RTA`, while the Rat King remains the separate `RTX` country. The RTA focus tree first chooses one of three hierarchy routes, then gives the four origin archetypes a persistent logistics identity. Neither choice creates an additional tag.

## Hierarchy routes

- `Four Mouths` followed by `Many Nests, One Signal` selects Distributed Instinct. It trades raw Brood Mass for a wider cap, faster marker consolidation, and a lower Rat King candidacy score.
- `Choose a Voice` followed by `Fang Above the Warren` selects Dominant Beast. It produces larger pulses, a persistent cap bonus, extra inherited brood units, and a longer consolidation lock.
- `Read the Marks` followed by `Stolen Route Memory` selects Emergent Cunning. It trades force ceiling and raw growth for transport and occupation-route pressure and the strongest Rat King candidacy.

The hierarchy focus roots are mutually exclusive. `Capped Pulses` requires one hierarchy follow-up and one of the four fixed origin terminals, so every route remains reachable without changing the two-tag country package.

Each hierarchy route also has a continuing action in the existing `black_plague_rat_brood_category`. Distributed Instinct can distribute nest signals after the carrier controls more than one state, restoring Coherence and increasing the persistent cap. Dominant Beast can seat an alpha command pattern when Coherence is stable, increasing Sentience and cap while raising Hunger. Emergent Cunning can decode a selected human enemy capital, coastal, rail, or supply target beside rat-held ground; it spends Brood Mass and applies a bounded internal-transport exposure through the canonical disease ledger with a state cooldown.

## Runtime behavior

- Urban `Citadel Warrens` and `Citadel Relays` add a continuing Brood Mass pulse contribution, a capped division-cap bonus, and a physical exposure bonus from rat-controlled sources.
- Field `Grain Tunnels` and `Migration Burrows` add rural Brood Mass, a capped division-cap bonus, and a movement-route exposure bonus.
- Dock `Tide Court` and `Cross-Sea Cargo` add dock Brood Mass and a capped division-cap bonus. The route does not bypass Evolution II; its overseas exposure bonus applies only while the shared `black_plague_overseas_spread_enabled` flag is active.
- War `Frontline Command` and `Rail Breach` add frontline Brood Mass, a capped division-cap bonus, and an internal transport or troop-movement exposure bonus.

The persistent division-cap bonus is stored in `black_plague_rat_division_cap_bonus`. The refresh effect rebuilds the base cap from controlled states, then reapplies the stored bonus and route-module contribution, so focus rewards survive later pulse refreshes. Rat armies still grow only through the capped pulse effect and remain locked against manual recruiting.

## Rat King policy consumers

The separate `RTX` tree stores one of three policy routes: Absolute Crown, Council of Burrows, or Black-Breath Hierophancy. The runtime consumes those route values during every royal pulse and during Crown Strike resolution. Crown increases Dominion growth, Council increases Cohesion growth, and Hierophancy exposes overseas pressure; a successful Crown Strike applies route-specific losses or a temporary exposure suspension. When royal Hunger reaches crisis, the route fires its own country event: the Crown can replace a brittle warden, the Council can charter or empower an emergency speaker, and the Hierophancy can consume contaminated mass or seal the route.

After the Rat King loses every controlled state, the idempotent defeat resolver retires `RTX` and opens `black_plague_shared_seal_royal_burrows` in the shared disease category for a human responder. Each selected former Royal Node or Royal Basin state is sealed with equipment, manpower, fuel, command power, factories, Response Capacity, and a 180-day operation. Success lowers infestation, raises containment, and adds countermeasure progress; timeout raises infestation and exposure without changing the disease phase.

## Script surfaces

- `common/script_constants/020_black_plague_rat_constants.txt` owns the route tuning table.
- `common/national_focus/020_black_plague_rat_focus_tree.txt` owns route focus flags and one-time rewards.
- `common/scripted_effects/020_black_plague_rat_effects.txt` owns persistent cap bonuses and pulse mass.
- `common/scripted_effects/020_black_plague_spread_effects.txt` owns route-proven exposure modifiers.
- `common/scripted_triggers/020_black_plague_rat_triggers.txt` owns hierarchy predicates, merger-cooldown readiness, and continuing-action target gates.
- `common/decisions/020_black_plague_rat_decisions.txt` owns the three route-locked continuing actions inside the shared category.
- `common/ai_strategy/020_black_plague_rat_ai_strategy.txt` biases existing rat templates toward cities, rural corridors, coasts, or army fronts after a route is completed.

## UI and asset contract

The route modules reuse the existing RTA focus icons and shared disease mapmode overlays. No new category, mapmode colour, 3D model, unit entity, or decision icon is required for this runtime tranche. If route-specific icons are added later, place final DDS files under `gfx/interface/goals/020_black_plague/`, register them in the existing Event 20 GFX file, and keep each icon tied to the route's actual mechanic.

## Future extension

A later content pass can add further route-specific scripted decisions (city undermining, granary migration, cargo stowaway, or depot collapse) using the same shared disease category. Such decisions must select a real state, pay material and time costs, and remain gated by the corresponding route flag and live Evolution state. The three hierarchy actions above are already the minimum continuing route layer; further actions should not duplicate their cooldowns or bypass the canonical spread ledger.
