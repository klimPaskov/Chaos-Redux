# Event 012 RSA prefire patron-pool repair

Date: 2026-08-02.

Status: Implemented source repair; live-save acceptance remains open.

## Scope

The one-shot weighted host selector built a temporary contact pool before freezing it, but original SAF could still enter the weighted host pool without a valid patron in that pool.

The later frozen-roster RSA gate could then reject the selected SAF, leaving the fire-once pass without a replacement candidate.

## Change

`common/scripted_triggers/012_africa_rsa_triggers.txt` now defines `africa_rsa_prefire_contact_pool_has_patron`, which checks the temporary contact pool for a valid African patron.

`common/scripted_effects/012_africa_effects.txt` only adds a SAF candidate to the weighted host pool when that patron trigger passes and the existing minimum-contact threshold is met.

Generic African hosts retain the existing contact-pool and weight path unchanged.

## Expected behavior

- Original SAF with a valid bounded patron is eligible for weighted selection, subject to the existing random three-to-five-contact freeze and final RSA gate.
- Original SAF without a valid patron is excluded before weighted selection, so another eligible generic host may be selected instead.
- If the random freeze omits the possible patron, the final gate rejects SAF and the new cleanup branch clears the frozen roster so a later explicit attempt is not poisoned by stale state.
- If no eligible host remains, the fire-once event stays closed rather than creating an invalid host or inventing a fallback tag.
- The existing frozen-roster and post-dispatch RSA gates remain authoritative.

## Validation boundary

The offline Paradox data-structure and trigger references confirm that `any_of_scopes` may inspect a temporary array and changes scope into each country element.

Static source checks confirmed one new trigger definition, one candidate-pool callsite, the existing minimum-contact guard, and no new country tag or periodic scan.

The bounded `hoi4_event_inspect` lint for `chaosx.nr12.1` returned status `ok` with no blocking diagnostics, while its workspace-wide helper analysis remained deferred by the adapter.

No Hearts of Iron IV executable or live save was launched, so patron selection, fallback selection, and no-host outcomes remain open acceptance work.
