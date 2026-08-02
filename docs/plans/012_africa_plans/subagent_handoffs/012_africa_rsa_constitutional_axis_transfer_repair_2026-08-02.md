# Event 012 RSA constitutional-axis transfer repair

Date: 2026-08-02.

Status: Implemented source repair; live-save acceptance remains open.

## Scope

The RSA exile transfer copies the original host's constitutional payoff axes to the accepted exile patron.

The seventh axis was written under the nonexistent name `africa_constitutional_crisis_authority`, while Event 012 initializes, modifies, prices, gates, and displays the axis as `africa_constitutional_crisis_resilience`.

## Change

`common/scripted_effects/012_africa_rsa_effects.txt` now copies `FROM.africa_constitutional_crisis_resilience` into `africa_constitutional_crisis_resilience` during exile-host succession.

The other six axes and the existing `africa_constitutional_payoff_axes_active` guard are unchanged.

## Expected behavior

- A valid exile patron receives all seven constitutional payoff values from the suppressed host.
- Crisis-resilience continues to feed route gates, action-axis pricing, risk calculations, and Charter localisation after succession.
- The nonexistent `africa_constitutional_crisis_authority` identifier is no longer referenced by the Event 012 source.

## Validation boundary

Static source search found no remaining `africa_constitutional_crisis_authority` references and confirmed the corrected variable is the same name used by the focus-route effects, triggers, and Charter localisation.

The bounded `hoi4_event_inspect` lint for `chaosx.nr12.1` returned status `ok` with no blocking diagnostics, while its workspace-wide helper analysis remained deferred by the adapter.

No Hearts of Iron IV executable or live save was launched, so the seven-axis equality after an actual RSA exile transfer remains open acceptance work.
