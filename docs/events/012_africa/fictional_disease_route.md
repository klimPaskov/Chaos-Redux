# Event 012 fictional disease route

Event 012's disease branch is a fictional high-chaos interface over the repository's native ordinary-pathogen lifecycle. It is available only after Evolution III and an explicit host decision establishes an isolated research station.

The authorisation decision records a research site, selects one native agent slot, creates a two-unit payload reserve, and starts a progress ledger. It does not create an outbreak. Two full research action results are required before weaponisation can be selected.

The weaponisation action targets a country at war with the host and selects one eligible controlled state. The state dispatch proves the host as actor, its controller as victim, the deliberate battlefield route, the payload debit, and the native ordinary-pathogen state eligibility before calling `bio_lifecycle_dispatch_seed`. A full result seeds a success episode, a partial result seeds the native partial band, and a rejected or lost target records a failed release and attempts the native laboratory-accident route only when that dispatch is accepted. The host payload is debited only after the native dispatch receipt is supplied; an accepted backfire consumes one payload and increments the release history. Every attempt starts a 45-day host cooldown, while successful dispatches increment separate host and target histories.

Containment actions target a country with a native episode. Full, partial, and failed responses call the native countermeasure adjustment effects across the affected country's controlled states and preserve the native scheduler and state modifiers; stale receipt flags alone cannot open containment. A failed research action selects one eligible host state and enters the native laboratory-accident route only after the native lifecycle accepts the accident. Crisis and release receipts are written only after accepted native dispatches, release counts initialise before their first increment, and shared action cleanup clears temporary receipts without deleting native outbreak history.

The shared action ledger remains the only action store. Outcome hooks live in `common/scripted_effects/012_africa_action_effects.txt`; reusable disease effects and triggers live in `common/scripted_effects/012_africa_disease_effects.txt` and `common/scripted_triggers/012_africa_disease_triggers.txt`; tuning lives in `common/script_constants/012_africa_disease_constants.txt`.

## UI and asset contract

The review decision and the three disease actions use the existing Event 012 Charter Ledger icon registered by `interface/012_africa_charter.gfx`. No disease-specific image or portrait is required. Player-facing text is in `localisation/english/012_african_union_l_english.yml`.

## AI and probability evidence

The authorisation decision has a base willingness score of 5 and a wartime factor of 2 after every visibility, affordability, host, and Evolution III gate succeeds. The latest mandatory HOI4 probability baseline inspected the high-chaos random picker at source hash `75618d14c2b102798f21dee2e428682dde79bf7182016a52f31f0b9e26f6f091`; the full workspace pool remained incomplete (118 candidates, 28 required inputs, one unresolved). After the picker gate, the random-list census recognised four branch pools (10, 7, 7, and 4 entries), source hash `dce9b2319a247b720dd61c949e60cfcc8a3dbca9b2b76fff0961c1417419d2c5`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07d5b8e50ffaad3e301f3e5d113f9c42db4536af1588a7d47f248d9074f22f0c/ffc0b3894dd66bc45ee9c62e4eb4592c8e26fd4c6689e837fa3d4242984d306b/probability-inspect-dce9b2319a24.json`. The same A-D six-scenario compare (`probability-246ef5b92db382ab585cf757`) returned zero comparison changes; the adapter cannot interpret arbitrary cap, target-loss, cooldown, or spawned-state scenario keys, so this is parser evidence rather than live eligibility proof. Family selection, three-draw scoring, and target dispatch remain unresolved, and no numeric action weight was changed.

## Future extension

If a later design adds a new fictional agent family, it must extend the native lifecycle constants, agent profile, state triggers, scheduler, countermeasure profile, event detail text, and audit evidence together. It must not add a second periodic world scan or a parallel action ledger.
