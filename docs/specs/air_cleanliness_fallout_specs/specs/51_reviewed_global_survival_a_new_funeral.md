# A New Funeral

## Acceptance role

A New Funeral is a dormant Fallout global-survival chain for the first winter and first recovery year. It is a country-level ritual governance crisis, not an Air Winter opening and not a super-event. It does not set either Fallout scheduler activation flag.

## Country admission and memory

The candidate producer initializes family trust, religious tension, public health, and cause-memory ledgers once for each current Fallout country row. The opening requires a current country identity and resource row, at least 25,000 recorded civilian deaths, Recognition below 65, winter disease pressure at or above 18 or Cohesion below 62, and one complete authored cost route. The candidate has no state, province, character, bilateral partner, or invented tag target. It stores candidate `541`, transaction `710051`, and route `7151` in the Fallout-owned candidate arrays.

## Four human choices and one AI lane

1. Build one civic rite spends Scrap and Power to give several communities one heated hall, a shared reading, and a public correction route.
2. Keep the rites separate spends less Scrap but more Power to preserve local grounds and require custodians to exchange verified names.
3. Let the state conduct the ceremony spends Food and Scrap to make the government responsible for the grounds and the public register.
4. Pass a rapid burial law spends Scrap and Recognition to move marked crews through frozen lanes while preserving a district witness for each grave.

The hidden AI lane uses the same four branches and deterministic delayed result path. Government form, Cohesion, available resources, and the absence of a current war influence the authored branch choice. No branch is a political-power purchase or a harmless failure.

## Deterministic delayed consequences

The result freezes Deaths, Recognition, Cohesion, Air Winter disease pressure, family trust, religious tension, and public health. Viability weights Deaths, Recognition, Cohesion, inverse disease pressure, family trust, and inverse religious tension. The result resolves after 21 days and the callback resolves after another 180 days. Each branch has success, partial, and failure text with distinct resource, Cohesion, Stability, War Support, exposure, family trust, religious tension, and disease changes. Failure routes population loss through `apply_exact_state_civilian_population_loss` and the Deaths system. Result and callback updates call `air_winter_apply_disease_modifier`, clamp the Air Winter disease ledger, refresh public health, set cause memory, and attach a branch-specific temporary dynamic modifier.

The callback closes the chain only after one hidden cleanup event releases the result and callback receipts. Every delayed trigger reauthenticates the current generation, country owner, candidate id, no-target registry value, country row, durable resources, and frozen ledgers. Cleanup clears only transaction state and frozen values while preserving funeral memory.

## Event Log and presentation

The chain owns event ids `chaosx.fallout.541` through `chaosx.fallout.553` and Event Log history `9156`. The shared Event Log maps the history to `fallout.event_log.new_funeral`, and dedicated scripted localisation maps twelve branch outcomes and three callback outcomes. All visible events use `GFX_report_event_fallout_new_funeral` and the dedicated DDS at `gfx/event_pictures/fallout_world_end/report_event_fallout_new_funeral.dds`.

## Engine-sensitive boundary

Static source review proves that the country candidate is built inside the current Fallout registry loop, that its ordinary opening receipt uses a no-target subject, that the delayed result and callback use one authenticated owner-bound registry, and that disease pressure is the existing Air Winter country ledger. Static review also proves the Deaths path supplies an explicit minimum remaining population for every held state. No HOI4 runtime was launched, so popup order, scheduler issuance, z-order, save recovery, multiplayer behavior, and live Event Log rendering remain unobserved.

## Review boundary

The chain is manually authored and dormant. It adds thirteen defined event blocks to the documented living-world total, but the countable Fallout total remains `0 of 660`. Scheduler activation, live human review, hidden-AI review, and the exact engine-native manual all-valid-province thermonuclear sweep remain open acceptance work.
