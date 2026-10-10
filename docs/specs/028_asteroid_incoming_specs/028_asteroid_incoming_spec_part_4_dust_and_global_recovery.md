# Asteroid Incoming, Part 4: Dust and Global Recovery

Status: implemented, except the global-mitigation revision marked as proposed.
Values are in `asteroid_incoming_dust` and `asteroid_incoming_dust_protection`; the [tuning matrix](028_asteroid_incoming_tuning_matrix.md) lists them.

## Purpose

Dust gives every strike a world-scale consequence even when the footprint is regional.
It weighs on production, supply, air operations, weather and Air Cleanliness for a meaningful period, then fades through visible stages.
It is a global environmental state, not radiation, chemical or biological contamination, and not a world-end route.

## What the player sees

The player-facing dust surface is deliberately small:

- one global **dust stage** (Residual Haze, Global Dust Veil, Impact Winter, Severe Impact Winter), shown as a national idea and in the Asteroid Recovery header;
- one national **protection tier** (unprepared, basic, organized, hardened), shown as an idea and in the header;
- the asteroid row in the Air Cleanliness source history.

The numeric Dust Load (0 to 100) is a record value: Event Details shows it beside the stage, but no decision reads it from the player.
Raw contributors, mitigation points and compensation variables stay internal.

## Dust Load

The opening load is computed once, after all fragments resolve, from the impact that actually happened.

| Contributor | Basis |
| --- | --- |
| Main crater base | Fixed; even a sparse continental strike creates real dust |
| Civilian deaths | Measured impact deaths, banded and capped |
| Industry levels destroyed | Factories and dockyards actually removed, banded and capped |
| Logistics and strategic levels destroyed | Infrastructure, railway, supply, port, air base, radar and similar levels actually removed, banded and capped |
| Footprint size | Processed states weighted by profile, capped |
| Fragments | A fixed amount per applied fragment centre plus their measured destruction, capped |
| Event 013 secondaries | A small fixed amount per accepted secondary disaster, capped |

Each contributor has its own cap so one industrial state cannot break the world economy, and no death or building is counted under two contributors.
The result is clamped to 1 through 100 for a strike; a near miss stays at zero.

## Stages

| Load | Stage | Campaign meaning |
| --- | --- | --- |
| 1 to 24 | Residual Haze | Noticeable air and transport disruption, limited economic pressure |
| 25 to 49 | Global Dust Veil | Broad production and supply problems, poor flying weather |
| 50 to 74 | Impact Winter | Strong worldwide output, logistics and Air Cleanliness pressure |
| 75 to 100 | Severe Impact Winter | The strongest non-terminal aftermath, with long recovery |

Every country receives the current stage idea.
Its effects stay within production (factory output, construction speed, production-efficiency growth), supply, air missions and weather; there is no bundle of unrelated army, navy, political or research penalties.
Weather quality uses supported modifiers only; the event claims no meteorological simulation.

The load never rises from its own reservoir.
After the strike, it changes only by decay and mitigation.

## Air Cleanliness

Dust writes the shared ledger's asteroid source slot.

- The opening injection scales with the opening stage and is applied once, guarded by a persistent receipt; fragments add to the same transaction, never a separate popup.
- While dust lasts, the current stage adds a small monthly reservoir, reduced by global mitigation and applied at most once per date.
- Falling stages and zero dust remove current pressure without refunding the historical injection.
- Removing contamination stays the shared recovery system's job, and Fallout eligibility stays under the shared contamination rules; Event 028 never requests Fallout.

## Decay

The opening stage holds for 30 days.
After that the load falls monthly by a stage-based amount (faster in raw points at higher stages) plus global mitigation.
Severe Impact Winter normally lasts well over a year; Residual Haze clears within a few months.
Fragmentation lengthens recovery only because it starts from a higher load.

## National protection

The global stage is shared; protection reduces part of a country's own penalty.
Each protection tier offsets a fixed share of the current stage's penalties through a hidden country dynamic modifier beneath the visible protection idea, so protection can never turn fading dust into a bonus.

| Source | Effect |
| --- | --- |
| Distribute Emergency Filters (emergency action, damaged countries) | Basic tier (15 percent) if the country has no higher tier |
| Protect Transport Reserves | Organized tier (30 percent) if the country has no higher tier |
| Harden Factories Against Dust | Hardened tier (45 percent) |
| Join the Observation Network | Adds 15 percent to the air-mission and weather offset, with or without a tier |

A higher tier replaces a lower one; ideas never stack.
Protection ends at zero dust, and a project that finishes after the sky has cleared lapses, as its tooltip says.

## Global mitigation

Global mitigation adds extra monthly decay, capped at `maximum_mitigation_decay`.

The implemented source adds one mitigation point for every completed protection or observation action anywhere in the world, clamped at the cap.
In practice the first three completed actions saturate it, so most countries' contributions change nothing globally, and national protection is conflated with global help.

**Proposed revision (2026-10-10 audit, not implemented):** only the Observation Network contributes to global decay.
Each member adds a fixed half point, capped at the existing maximum, so six members saturate it and the action keeps a real global meaning for later joiners.
Filters, transport and factory hardening stay national protection only.
This needs parent acceptance; it changes no visible value and no AI weight.

## Event 013 secondary disasters

Inside the impact transaction, catastrophic-ring states and fragment centres in disaster-prone zones may request one supported Event 013 family each, up to four per impact, in state-id order.
Event 013 validates geography and family, skips unsupported families without substitution, and owns the secondary disaster's effects, deaths, food consequences and reports, with Event 028 recorded as the caller.
Only accepted requests add their small dust amount; rejected ones add nothing.
No secondary disaster is requested after the transaction, so dust never rises later.

## Coexistence with other atmospheric sources

Dust can coexist with smoke, volcanic ash, nuclear winter, chemical contamination and outbreaks.
The Air Cleanliness ledger combines sources normally, Event 028 never replaces another source's modifier, and overlapping production penalties from several systems should be reviewed for runaway stacking.

## Milestone bulletins

The world receives the opening stage inside the impact bulletin, then at most one bulletin when the stage falls below Impact Winter (`chaosx.news.92`), one when only Residual Haze remains (`chaosx.news.93`) and one when the dust clears (`chaosx.news.94`).
Rapid stage changes are coalesced so a single sharp fall does not stack near-identical bulletins.
Bulletins describe conditions and recovery, never the formula.

## Near miss

The near miss creates no Dust Load, Air Cleanliness change, protection decisions, secondary disasters or bulletins beyond the close-passage news.

## Performance

Dust changes only at the impact, at the existing monthly global-host pulse and at bounded decision completions.
There is no daily scan of every country.
