# Event 006 Independence Wave Evolutions

## Purpose

Event 006 has five visible evolution stages that change both future release plans and countries already created by the Independence Wave. The evolution state is global and canonical, while delivery is restricted to the aligned Event 006 active-country and generation arrays. The system does not scan the world and is not attached to a daily, weekly, or monthly on action.

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

- `common/script_constants/006_independence_wave_evolution_constants.txt`
- `common/mtth/006_independence_wave_evolution_mtth.txt`

The effects and triggers are:

- `common/scripted_effects/006_independence_wave_evolution_effects.txt`
- `common/scripted_triggers/006_independence_wave_evolution_triggers.txt`

## Event 005 Boundary

Event 006 uses evolution type `21`; Event 005 retains its existing secession and high-chaos evolution types, origin variables, history rows, and collision arbitration. Evolution delivery checks `is_independence_wave_active_country` and traverses only Event 006 aligned arrays, so Soviet Collapse countries cannot receive these stages through origin overlap.

## Visual Assets

No bespoke visual asset is required for this tranche. The stages use the existing Events Log evolution row, settings controls, tier presentation, and Event 006 event identity.

If bespoke stage icons are commissioned later, stable source names should be registered in `interface/006_independence_wave.gfx`, with final DDS files under `gfx/interface/goals/006_independence_wave/evolutions/`. Suggested sprite names are `GFX_independence_wave_evolution_1` through `GFX_independence_wave_evolution_5`. No current gameplay or localisation key references those optional sprites.

## Required Follow-through

- Complete the package-initialization adapter hook after the command roster and reinforcement-pathway contracts are proven, so Armed Birth force modifiers are consumed before starting-force materialization.
- Implement and wire the accepted incident families for copied institutions, dormant identities, armed border crises, congress disputes, and open-sovereignty escalation and containment.
- Feed rapid annexation, puppetry, and collapse among earlier Event 6 countries into the Replicable Independence opening-confidence calculation.
- Revisit MTTH pacing after runtime observations across multiple Event 006 invocations at each chaos tier, especially when several stages are disabled in settings.

Dedicated evolution art is not currently referenced by the Events Log. If that UI gains per-evolution sprite support, register stable sprites in `interface/006_independence_wave.gfx` and place the final DDS files under `gfx/interface/goals/006_independence_wave/evolutions/`; do not introduce unused assets.
