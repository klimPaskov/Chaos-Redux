# Event 006 Economy Capstone Decision Repair

## Scope and outcome

This bounded repair gives `independence_wave_create_independent_treasury` an active, material-cost consumer without changing the focus tree, category registry, or wider Event 006 economy system.

The focus still sets `independence_wave_economy_capstone_complete` and applies the `independence_wave_independent_treasury` idea.

The new `independence_wave_treasury_backed_public_works` decision in `independence_wave_government_category` is visible only to an active Event 006 origin with that capstone flag.

## Changed files and identifiers

- `common/decisions/006_independence_wave_decisions.txt`: added `independence_wave_treasury_backed_public_works`.
- `common/scripted_effects/006_independence_wave_decision_effects.txt`: added its removal to `independence_wave_cleanup_decision_layer`.
- `localisation/english/006_independence_wave_decisions_l_english.yml`: added the four `independence_wave_treasury_backed_public_works*` localisation keys.

The decision reuses `can_pay_independence_wave_strategic_cost`, `independence_wave_decision_pay_strategic`, and existing Event 006 decision constants.

## Before and after behaviour

Before this repair, the treasury focus supplied only a passive idea and its completion flag had no decision consumer.

After completion, the owner may start a 240-day capital public-works programme if it controls the capital, has no severe instability, and still has either unused government capacity or recoverable instability.

Starting the programme immediately uses the established strategic commitment: 10% stability, 5% war support, 20 command power, and either 10 convoys or 10 trains, while reserving two civilian factories.

On completion, it adds one capital infrastructure level where the network can still expand, grants 15 government capacity and 5 security, and reduces instability by 5.

The decision has a 365-day re-enable period and becomes unavailable once capacity and instability are both fully resolved.

It cancels if the origin becomes inactive, the capstone flag is removed, or the owner loses its capital.

The existing origin reset cleanup explicitly removes both the active decision and any cooldown, so a later origin cannot inherit an in-flight programme or cooldown.

## Audit findings

### Severity-sorted issues

1. High, resolved: `independence_wave_economy_capstone_complete` was set by the focus but had no continuing decision or mission consumer.
2. Medium, resolved: no lifecycle cleanup prevented a possible retained active or cooling capstone decision during an origin reset because no such decision existed.
3. Low, remaining: capital infrastructure follows the engine building cap, so the infrastructure portion can naturally stop adding a level while the ledger improvements still remain valid.

### Decision category lifecycle

`independence_wave_government_category` already owns state-building actions, so it is the appropriate existing category for the treasury programme.

The lifecycle is focus completion, flag-gated reveal, cost-gated start, 240-day execution, reward, 365-day cooldown, then optional repeat only while its capacity or instability requirement remains unmet.

### Mission quality notes

No mission was created because the requested continuing consumer is a repeatable decision and the existing category already follows that action model.

Owner: the active Event 006 origin.

Region: the owner capital.

Requirement: capstone completion, capital control, no severe instability, remaining capacity or instability work, and the strategic material cost.

Duration: 240 days.

Success: infrastructure plus ledger gains.

Failure or cancellation: losing the origin, capstone status, or capital stops the programme without granting its reward.

Duplicate risk: prevented by the decision engine while it runs, then by the 365-day cooldown and origin-reset removal.

### Cost and requirement clarity

The decision uses the existing `independence_wave_cost_strategic` custom cost text and actual spending helper, so its displayed transport, command, stability, war-support, and civilian-capacity costs match its effect.

The custom requirement tooltip explains the capital-control, instability, and capacity conditions rather than exposing the raw trigger block.

### AI validity and route-lock notes

The AI weight is 25 in peace and halves during war.

It has no country target and all origin, capital, and resource checks are in `visible` or `available`, so the AI cannot validly select it after the route is closed or the capital is lost.

### Localisation, cleanup, and exploit-risk notes

All player-facing name, description, requirement, and effect strings were added in the Event 006 English decision file.

The cancellation and cleanup paths clear the active decision; the origin reset also removes any cooldown without firing completion effects.

The material cost, civilian-factory reservation, major cooldown, and saturation requirement prevent a free unit, equipment, factory, core, or unlimited capacity loop.

## Validation evidence

The decision syntax and lifecycle were checked against the offline Decision Modding reference, the vanilla custom-equipment-cost precedent in `common/decisions/AUS.txt`, and the vanilla trigger, effect, and script-constant documentation.

A scoped static check confirmed one decision definition, one origin-reset cleanup hook, one localisation definition for each new key, a UTF-8 BOM in the localisation file, and no unsupported comparison operator in the added decision block.

`git diff --check` passed for the three gameplay and localisation files.

The focus consumer relationship was inspected with `hoi4.focus_inspect`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/559269657d3d55c3d275f4fbd121b577150c6645a840a365d381fad17ce6b74c/9fddd40648c2b2dd8d5c6ab65f3515c0bea06db97f087508b05aca82524089d0/focus-inspect.e7ad516d30b8871b.json`.

That inspection reported pre-existing focus-layout diagnostics elsewhere in the tree, including crossings and unrelated long connectors; this bounded task neither changes nor resolves those focus-layout findings.

No live-game test was run because repository policy assigns that validation to the user.

No decision probability sweep was run because this AI block is a direct static weight with one wartime factor rather than a weighted selection pool.

## Remaining issues and simplifications

No unapproved simplification or fallback was introduced.

The existing wider focus-tree layout diagnostics remain outside this decision-only scope.

The decision intentionally preserves the normal building-cap behaviour for capital infrastructure; the resource and ledger gains still have explicit, bounded outcomes.
