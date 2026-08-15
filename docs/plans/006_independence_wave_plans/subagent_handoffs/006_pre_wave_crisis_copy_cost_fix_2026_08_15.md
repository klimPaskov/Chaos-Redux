# Event 006 pre-wave crisis copy and cost fix

Date: 2026-08-15

## Disposition

Implemented a player-facing localisation correction for the pre-wave pressure mission without changing its trigger, payment, timeout, cancellation, or release logic.

The category is intentionally available before a wave begins when pressure conditions are met, so the old crisis wording was misleading rather than a missing event gate.

## Changed files

- `localisation/english/006_independence_wave_decisions_l_english.yml`

## Player-facing changes

- Renamed the category to `Pre-Wave Pressure`.
- Replaced the crisis-opening decision title with `Prepare a Synchronized Liberation Request`.
- Explicitly states that no wave has begun and that no territorial change occurs during preparation.
- Replaced the prose-heavy custom cost line and blocked-cost line with compact icon-first values for manpower, Army Experience, Command Power, infantry equipment, and support equipment.
- Kept the detailed cost and stability consequence in the hover tooltip.

## Preserved mechanics

The existing pressure trigger remains pre-wave by design, including low stability, severe resistance, cooldown, active-crisis, queued-release, and release-barrier checks.

The existing five-resource payment remains unchanged at the standard manpower, Army Experience, infantry equipment, and support equipment values plus the standard Command Power requirement.

## Evidence

`hoi4.event_inspect` scanned `events/006_independence_wave.txt` with `EVENT_INSPECTED_PARTIAL` and zero blocking diagnostics; the linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ff2926b334f9b16e1b4c170fd466d82145a06a1248a62de82fdcd982903d36e9/44a6ed93085c1cc2988e4f7611fb1f391ad766531f2570f70c4c03cbf921e9ad/event-scan-79be311981e5.json`.

`hoi4.event_render` produced `EVENT_RENDERED_PARTIAL` overview artifacts with zero blocking diagnostics; the overview manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d5c5b47de5b9753fdb3b5cfd26f69190b1c43cc730bba9705e45a87344e85daa/067ed7add984567a66ea133e2599db44a37a1f6fac95d5f13c65d826d850905e/event-overview-79be311981e5-manifest.json`.

The installed MCP surface has no dedicated decision-category renderer, so the exact in-game decision panel wrap remains a user-side visual check.
