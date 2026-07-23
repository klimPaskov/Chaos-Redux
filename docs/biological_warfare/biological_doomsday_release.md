# Biological Doomsday Release

## Purpose

The biological doomsday decision is the exceptional last-resort release allowed by Spec 06.

It is not an ordinary biological deployment route and does not replace strategic raids, battlefield land raids, intelligence operations, or historically specific exact-state campaign actions.

The route opens only for a country with an explicit unrestricted national route or the unrestricted use policy, at more than 80 percent surrender progress or during a verified world-end condition, with at least one real ordinary-agent payload and at least one exact eligible state.

## Exact target definition

The target collector starts with every eligible state controlled by the releasing country.

It then visits those controlled states and adds every unique eligible neighboring state whose controller is at war with the releasing country.

The neighboring states are deduplicated in one temporary state array before any payload is allocated.

The installed game exposes no exact current-version state trigger for an active land front or ongoing land combat.

“Nearby fronts” therefore means exact enemy-controlled wartime border adjacency, following the installed vanilla `any_neighbor_state` and `CONTROLLER = { has_war_with = ROOT }` precedent.

This definition is not an activity estimator and does not infer a front, launch state, air mission, or substitute target.

The decision separately builds a domestic-state array and prints every eligible controlled state in the warning tooltip before the release.

## Arsenal debit and allocation

The resolver snapshots the aggregate national stock of `anthrax_bomb_1`, `plague_bomb_1`, `tularemia_bomb_1`, and `smallpox_bomb_1`.

Negative stockpile effects omit a producer filter so captured and licensed payloads are consumed together with domestically produced payloads.

All four captured counts are removed before state dispatch begins.

Each agent stock is divided across the exact target array in engine-provided array order.

The allocation rounds the current remaining stock across the current remaining state count, enforces a minimum allocation of one while stock remains, and never exceeds the remaining stock.

If an agent stock is smaller than the target count, only that many states receive one unit of that agent.

No payload is duplicated, fabricated, refunded, reassigned to an alternate state, or retained after a failed dispatch.

## Shared biological lifecycle

Every successful state-agent allocation calls `bio_lifecycle_dispatch_seed` with the exact state, current controller, releasing country, agent, route, source, result, required payload, consumed payload, and proof fields.

The route is `bio_lifecycle_route.doomsday_release` and the source is `bio_lifecycle_source.doomsday`.

Overall weapon severity follows the canonical hierarchy `Tularemia < Anthrax < Plague < Smallpox`.

Tularemia is low severity, Anthrax is moderate, Plague is serious, and only Smallpox belongs to the severe weapon tier.

Tularemia, Anthrax, and Plague use the successful-release result and receive their canonical 0.85, 1.00, or 1.15 agent-strength multiplier inside the shared lifecycle.

Smallpox alone uses the severe result, whose 1.15 operational multiplier combines with Smallpox’s canonical 1.30 agent strength.

The result token records operational release quality while the agent profile records disease potency, so an effective delivery never changes the weapon-severity classification.

Every accepted episode receives the doomsday route’s intensity, exposed share, 0.85 friendly-spread risk, maximum evidence, incubation schedule, later detection and spread behavior, medical load, deaths, contamination, and attribution records.

The public order confirms responsibility immediately, while the individual agents still incubate and activate on their own schedules.

The validated doomsday record suppresses each state-agent episode’s ordinary probable and confirmed political release before forced detection can run.

This does not suppress evidence, detection, attribution, physical harm, or state history; it prevents an already-active episode from adding a second political consequence before the country resolver settles the one public batch.

Direct allied-state targeting is prohibited.

Connected spread can still reach allied territory and can return through the releasing country because the doomsday route retains the maximum friendly-spread risk defined by the matrix.

Weaponized zombies do not enter this resolver and retain their separate project, operation, effects, and history.

## Doctrine and consequence contract

Theater Contamination and Terminal Hazard doctrine may increase seed potency, outbreak growth, spread, death pressure, duration, medical saturation, and AI willingness through the shared lifecycle.

Doctrine does not reduce payload debit, evidence, attribution, deaths, contamination, medical load, confirmed-use history, domestic war-support loss, biological-use counters, public-harm floors, or route history.

Only the base Condemnation value reads the doctrine Condemnation multiplier.

The public batch starts from 300 Condemnation and is clamped to the matrix-required 200–500 range after that multiplier.

The resolver registers one public biological-doomsday Condemnation source, one treaty-breach callback, one confirmed-use callback, one route-use record, one national deliberate-use record, and one five-percent domestic war-support loss for the complete multi-state release.

Per-agent payload and use totals remain separate, and each successful state records its exact agent payload and responsible actor.

The batch deliberately does not fabricate a single victim country for a multi-country release.

## Failure semantics

The public decision is gated by the same route, crisis, arsenal, and target contract that the resolver rechecks.

Once the resolver accepts the operation, the complete arsenal is consumed before the first lifecycle dispatch.

If every state dispatch fails its exact lifecycle validation, the country records a dispatch-failure history flag, receives no fabricated release history, and does not publish the release news event.

If at least one allocation dispatches, the public batch consequence and news event occur once.

If fewer payload units dispatch than were consumed, the country records partial-resolution history and the unmatched material remains lost.

Only exact equality between seeded payload and consumed arsenal records full-resolution history.

These branches provide no alternate state, delayed retry, proxy actor, payload refund, or inferred release.

## AI behavior

AI willingness is multiplied by zero unless `cbrn_ai_route_allows_unrestricted_use` is true, even when a player-facing extreme policy makes the decision visible.

Theater Contamination and Terminal Hazard doctrine, a large arsenal, and minimum containment preparation increase willingness.

Unsafe handling, an active domestic outbreak, high Condemnation combined with high import vulnerability, and treaty membership suppress willingness.

The decision’s availability still requires the same last-resort, arsenal, and exact-target gates used by the player.

The installed decision analyzer confirms a raw willingness score of 0 without the unrestricted AI route, 0.35 for an unrestricted unsafe baseline, 1.05 for an unrestricted Terminal Hazard country with a large arsenal, and 0.021 for that country when an active domestic outbreak and treaty membership apply.

The analyzer cannot currently resolve script-constant operands inside the two `check_variable` clauses of the sanctions-vulnerability helper.

Source arithmetic applies the additional 0.10 factor only when both accepted thresholds are met, reducing the last scenario to 0.0021.

Decision willingness is a score rather than a click probability, and no categorical probability is claimed.

## Assets and wiring

The decision reuses `GFX_decision_bio_unleash_stockpiled_pathogens` from `interface/chaosx_gfx_cleanup.gfx`.

The sprite points to `gfx/interface/decisions/biowarfare/decision_bio_unleash_stockpiled_pathogens.dds`.

The existing DDS is 4,224 bytes with SHA-256 `4F711064D2A7E0E70631C79538387E9C78A8DF8731D524FCC0AB90D64A1BC1FF`.

No new doomsday asset, placeholder, resized cross-type substitute, or duplicate sprite was introduced.

The existing strategic biological raid sprites and files under `gfx/interface/military_raids/` remain untouched and continue to serve native biological raids.

## Engine limits

The engine does not expose an exact current-version active-front state predicate, so the target contract stops at verified enemy-controlled wartime border adjacency.

The engine provides no transactional rollback across several state lifecycle dispatches, so an accepted release debits the arsenal first and records exact partial resolution if a later state rejects the seed.

The decision does not use continuous air missions, aircraft presence, air-region estimates, daily country scans, weekly country scans, monthly country scans, or any broad all-country pulse.

## Future plans and suggestions

No additional behavior is required for this doomsday tranche.

If a future installed version exposes a documented exact active-front state predicate, the wartime-border target helper can be narrowed after a new source review.

It must not be replaced by combat estimates, aircraft-activity estimates, or an inferred-state fallback.
