# DM-01 — Secure the Provisional Capital

DM-01 is the automatic founding mission every admitted Independence Wave country uses to establish a functioning administrative seat.

## Lifecycle

The mission opens only after the country is active, its package setup is complete, its capital is controlled, and the required force-tier garrison is assigned to that capital.

At activation the country pays infantry and support equipment scaled to the published force level. A capital with no supply node also pays either trains or trucks, using whichever transport reserve is available. The commitment is marked with `independence_wave_dm01_costs_reserved` and is not refunded if the mission fails.

The mission uses a 75-day ceiling. Fragile force levels shorten that ceiling by 45 days and viable force levels shorten it by 30 days, producing the accepted 30-to-75-day founding window; armed and high-chaos levels retain the full 75 days.

The mission cancels if the country ceases to be an active Event 006 origin, loses capital control, or removes the required garrison. Failure applies the country ledger penalties, marks government and command pressure, refreshes the collapsed-cabinet and warlord-command ideas, and opens the country-scoped emergency relocation event `chaosx.nr6.311`.

The relocation event either moves the capital to another owned, controlled state or records dispersed emergency offices. The relocation choice clears the pending failure handoff without manufacturing a state or a free unit.

On timeout, the mission records the capital as secured, marks the capital administration as ready, improves capacity and security through the shared Event 006 ledgers, and refreshes the functioning-administration idea lifecycle.

## Runtime surfaces

- Decision and mission definition: `common/decisions/006_independence_wave_decisions.txt`.
- Cost and garrison triggers: `common/scripted_triggers/006_independence_wave_decision_triggers.txt`.
- Payment, activation, and cleanup effects: `common/scripted_effects/006_independence_wave_decision_effects.txt`.
- Country-scoped retry hook: `common/scripted_effects/006_independence_wave_effects.txt` through `independence_wave_refresh_country_state`.
- Relocation event: `events/006_independence_wave.txt`, `chaosx.nr6.311`.
- Player-facing text: `localisation/english/006_independence_wave_decisions_l_english.yml` and `localisation/english/006_independence_wave_l_english.yml`.

No periodic world scan is used. The refresh hook retries only in the current country scope when a previously unavailable material gate becomes valid.

## Assets and future work

DM-01 reuses `GFX_decision_independence_wave_government_actions` and the existing wave-summary report image, so no new icon or event art is required. A future pass may add a dedicated capital-crisis illustration after the shared Event 006 asset manifest and MCP event render are available again.
