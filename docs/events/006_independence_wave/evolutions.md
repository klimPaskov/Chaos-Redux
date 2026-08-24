# Event 006 Independence Wave Evolutions

## Purpose

Event 006 has five visible evolution stages that change both future release plans and countries already created by the Independence Wave. The evolution state is global and canonical, while delivery is restricted to the aligned Event 006 active-country and generation arrays. The system does not scan the world and is not attached to a daily, weekly, or monthly on action.

Each stage has one shared incident family with two paid outcomes. These incident families are a country-facing resolution layer inside the five evolution stages, not additional evolution rows.

The five player-facing stages are:

1. **The Manuals Cross the Border**
2. **Old Nations Wake**
3. **Flags Rise Behind the Barracks**
4. **The Sovereigns Take Their Seats**
5. **No Border Is Final**

Their Event Log identity is Event `6`, evolution type `21`, stages `1` through `5`, and chaos tiers `1` through `5` respectively.

## Progression

Before an Event 006 allocator freezes its contribution, `independence_wave_prepare_evolution_for_incident` reconciles the active registry and evaluates progression.

- If there are no living Event 006 countries, every enabled evolution whose tier has been reached activates immediately. This gives the first wave a genuine pre-fire package rather than applying changes only after release.
- If Event 006 countries already exist, active stages are synchronized to the aligned registry. Missing stages advance through `independence_wave_evolution_interval`, sampled only on Event 006 invocations.
- A due active invocation can activate at most one stage. A disabled stage is skipped without blocking later enabled stages.
- Each transition stores its activation date and either records its Event Log row immediately with a living Event 006 actor or defers the row until the first frozen country is initialized.
- Country delivery uses one applied flag per stage, so repeated registry synchronization is idempotent.

Evolution settings are default-enabled through the standard Event Log settings system. The normal disabled-evolution flag contract remains authoritative for each exact Event 6/type 21/stage row.

## Frozen Planner Effects

`independence_wave_freeze_evolution_plan_state` copies canonical evolution state before package weighting. Each selected country then receives its own pending evolution flags, preventing later setting or tier changes from rewriting a locked plan.

| Stage | Frozen-plan effect |
| --- | --- |
| The Manuals Cross the Border | Softens the repeat penalty for regions already connected to a prior wave. |
| Old Nations Wake | Allows registered, absent, and unique-state candidates to appear one chaos band earlier and favors registered, regional, and signature packages. |
| Flags Rise Behind the Barracks | Favors industrial-security and mountain/frontier packages. |
| The Sovereigns Take Their Seats | Favors regional and signature packages suited to delegates and leadership. |
| No Border Is Final | Opens high-chaos pools, admits the nine route-only/formable packages into their regional automatic lists, and strongly favors high-chaos and formable dispositions. |

The baseline wave sizes remain unchanged. Evolutions change composition and opening conditions, not the Event 006 count ladder.

## Active and Opening Delivery

### The Manuals Cross the Border

Countries receive legitimacy, recognition, administrative capacity, network standing, and access to the foreign-service exchange. Countries entering a network that already had living members also receive prior-contact recognition and standing.

### Old Nations Wake

Countries receive legitimacy, recognition, capacity, reduced instability, the formable-discovery layer, and a strengthened identity lifecycle. Their focus layout is dirtied so the existing conditional formable branch can appear immediately.

### Flags Rise Behind the Barracks

Countries receive security and military influence, unlock the professional-army layer, and acquire an Armed Birth force authorization consumed by the force calculator. The same stage raises instability, bilateral hostility, and reconquest fear, and alerts a living former host.

The force calculator adds a centrally tuned budget bonus plus equipment and experience factors when the authorization is present. It does not itself invoke force creation. Package initialization must call the existing dynamic starting-force adapter only after package setup, command-roster, and reinforcement-pathway proof is complete.

### The Sovereigns Take Their Seats

Countries gain legitimacy, recognition, capacity, network standing, and access to the league-congress layer. Each active origin is classified as a delegate, observer, or rejected client from its route, package depth, and network standing. The stage seeds common cause, cohesion, reserve, confidence, and the shared strategic problem, then attempts to open the existing conference state machine through its canonical trigger.

### No Border Is Final

Countries reveal the high-chaos and radical-sovereignty route surfaces, gain formable discovery, and receive security alongside instability, bilateral hostility, reconquest fear, and sponsorship pressure. The league gains common cause, patron-capture pressure, and one revisionist-action step. Focus layout is dirtied so existing `allow_branch` logic reflects the canonical evolution immediately.

## State and Tuning

Canonical global flags:

- `independence_wave_evolution_replicable_independence_active`
- `independence_wave_evolution_dormant_nations_active`
- `independence_wave_evolution_armed_birth_active`
- `independence_wave_evolution_sovereign_congress_active`
- `independence_wave_evolution_open_sovereignty_active`

The tuning sources are:

- `common/script_constants/006_independence_wave_constants_registry.txt`
- `common/mtth/006_independence_wave_evolution_mtth.txt`

The effects and triggers are:

- `common/scripted_effects/006_independence_wave_evolution_effects.txt`
- `common/scripted_effects/006_independence_wave_evolution_incident_effects.txt`
- `common/scripted_triggers/006_independence_wave_evolution_triggers.txt`
- `common/on_actions/006_independence_wave_evolution_on_actions.txt`
- `events/006_independence_wave_support_events.txt`

Replicable Independence also exposes `global.independence_wave_replicable_opening_confidence`, initialized at 50 and clamped to 0–100. Lifecycle failures are recorded once per origin generation from government collapse, recognition blockade, command or border failure, congress discredit, and open-sovereignty escalation. Annexation, puppetry, and capitulation are recorded at their transaction boundaries. The allocator applies the low-confidence penalty or high-confidence bonus before candidate weighting, so earlier survival directly changes later wave composition. The League Congress category displays the live value.

## Shared incident resolution

The shared incident-resolution core is source-wired by commit `9231c15f5` and recorded in `subagent_handoffs/006_evolution_incident_resolution_core_2026_08_01.md`. It does not promote a country package or change the whole-event **HOLD / PARTIAL** disposition.

Each active evolution exposes one paid, generation-scoped decision in
`independence_wave_evolution_incident_category`. The decision consumes an
existing administration, diplomatic, security, or strategic material package,
then opens a two-option country event. The options write the country ledger
and, where applicable, the former-host, Network, or League ledgers through the
shared transaction effects.

| Stage | Incident families | Runtime surface |
| --- | --- | --- |
| The Manuals Cross the Border | institution compact or recognition campaign | `chaosx.nr6.360`, administration cost, capacity or recognition/network trade-off, former-host obligations/property |
| Old Nations Wake | civic charter settlement or pluralist compact | `chaosx.nr6.361`, diplomatic cost, identity flags, legitimacy/recognition/capacity/instability |
| Flags Rise Behind the Barracks | civilian chain of command or frontier mobilization | `chaosx.nr6.362`, major security cost, security/instability and bilateral hostility/fear; frontier option can open a reclamation conflict |
| The Sovereigns Take Their Seats | equal-rights charter or concentrated secretariat | `chaosx.nr6.363`, strategic cost, country/Network and League cohesion/common-cause/patron/confidence changes |
| No Border Is Final | synchronized claims or containment diplomacy | `chaosx.nr6.364`, strategic cost, territorial pressure and revisionist action versus recognition/Network shelter |

Pending and resolution flags are cleared by both generation reset and origin
cleanup. This prevents reused `chaosx_country_*` API tags from inheriting a
previous government's incident decision while retaining the global opening-
confidence feedback memory.

## Event 005 Boundary

Event 006 uses evolution type `21`; Event 005 retains its existing secession and high-chaos evolution types, origin variables, history rows, and collision arbitration. Evolution delivery checks `is_independence_wave_active_country` and traverses only Event 006 aligned arrays, so Soviet Collapse countries cannot receive these stages through origin overlap.

## Visual Assets

No bespoke visual asset is required for this tranche. The stages use the existing Events Log evolution row, settings controls, tier presentation, and Event 006 event identity.

If bespoke stage icons are commissioned later, stable source names should be registered in `interface/006_independence_wave.gfx`, with final DDS files under `gfx/interface/goals/006_independence_wave/evolutions/`. Suggested sprite names are `GFX_independence_wave_evolution_1` through `GFX_independence_wave_evolution_5`. No current gameplay or localisation key references those optional sprites.

## Remaining Follow-through

- Keep the civilian-command outcome on the one-shot opening-force authorization path and keep the frontier-mobilization outcome tied to the paid DM-22 reserve decision. The frontier choice therefore materializes a bounded, understrength reserve from the audited force template without adding a free-unit loop or changing the synchronized release transaction.
- The transaction-boundary hooks for rapid annexation, puppetry, and capitulation now feed the Replicable Independence opening-confidence calculation. Collapse is represented by the existing lifecycle failure flags and is recorded once per generation through the central refresh hook.
- Revisit MTTH pacing after runtime observations across multiple Event 006 invocations at each chaos tier, especially when several stages are disabled in settings.

Dedicated evolution art is not currently referenced by the Events Log. If that UI gains per-evolution sprite support, register stable sprites in `interface/006_independence_wave.gfx` and place the final DDS files under `gfx/interface/goals/006_independence_wave/evolutions/`; do not introduce unused assets.
