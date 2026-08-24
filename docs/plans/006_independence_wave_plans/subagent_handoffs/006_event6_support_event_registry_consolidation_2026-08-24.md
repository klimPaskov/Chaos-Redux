# Event 006 support-event registry consolidation

Date: 2026-08-24

## Scope

The three small same-namespace Event 006 event files were consolidated into `events/006_independence_wave_support_events.txt` to reduce file-count overhead without changing gameplay contracts.

The registry preserves the five evolution incidents (`chaosx.nr6.360` through `chaosx.nr6.364`), the FORM-05 events (`chaosx.nr6.28` through `chaosx.nr6.34`), and the FORM-16 human reply (`chaosx.nr006.6816`). The registry declares `chaosx.nr6` once; every moved event keeps its original fully qualified ID and source-local constants.

SCN-008 remains in `events/006_independence_wave_scenario.txt` because it owns the separate `chaosx.triggerable_scenarios` namespace and delayed launch-barrier contract. The Join report also remains separate as its own player-facing offer/retry surface.

## Changed files

- Added `events/006_independence_wave_support_events.txt`.
- Removed `events/006_independence_wave_evolution_incidents.txt`.
- Removed `events/006_independence_wave_form05.txt`.
- Removed `events/006_independence_wave_form16_events.txt`.
- Updated `docs/events/006_independence_wave/evolutions.md` and `docs/events/006_independence_wave/transcaucasus_packages_and_form16.md` to point at the registry.

## Evidence

- The merged registry contains the same 13 event IDs as the three source files and has balanced Clausewitz braces.
- The merged registry is 10,333 bytes versus 11,112 bytes for the three source files, saving 779 bytes while reducing three files to one.
- The static Event 006 allocator audit passes with 149 publishers, 126 automatic/high-chaos selectors, 32 attested packages, the 20-package standalone witness, and the 3/4/5/7/10 automatic count ladder.

## Boundary

This is a source-layout consolidation only. It does not promote packages, change allocator admission, alter event IDs, or claim live in-game execution evidence.
