# Event 005 Successor Relations resolution

Status: Implemented and source-complete before the terminal focus-layout rewrite.

The formerly unwired Black International, Free Soviet Congress, and Iron Production Bloc are now complete members of the Event 005 regional-faction system. This closes the separately queued Successor Relations label in the July 11 improvement addendum.

Implemented surfaces:

- three founding decisions with shared dynamic costs and route-sensitive AI
- three founder and member identity families
- identity-specific eligibility for Black Banner, socialist/council, and industrial/rail/mining successors
- common faction creation, member recruitment, registration, Moscow pressure, goals, mandates, units, wars, and withdrawal lifecycle
- charter events `chaosx.nr5.33`, `chaosx.nr5.34`, and `chaosx.nr5.37`
- missing-member mandate integration for all three blocs
- Black Banner endgame create-or-join behavior that prevents duplicate Black International factions
- UWR and KMB eligibility for the Iron Production Bloc
- final pre-existing decision and faction assets retained under their stable GFX identifiers
- dedicated system documentation at `docs/events/005_soviet_collapse/successor_relations.md`

The focused Event MCP refresh recognized three additional event definitions and nine additional options, increasing the parsed workspace counts from 9,491 events and 14,676 options to 9,494 events and 14,685 options. The trace artifact for `chaosx.nr5.33` is `event-trace-8c2577b32af5.json`. Focused seven-node option renders for all three charter events returned zero blocking diagnostics: `chaosx.nr5.33` produced JSON hash `fce3954c000e64d53c3fdf2554cab751eed130a6db529ce8c712cdf6ab6693e2`, `chaosx.nr5.34` produced `66217ae885fbd30883d90766e9379d811000a2b823a62a8aed53104c19908a4a`, and `chaosx.nr5.37` produced `e5c3274db6da5460fe330ced31db88318ee1bb444ab142bd6aa4459ed8453fcf`.

The charter options use unique event-owned identifiers and localisation keys: `chaosx.nr5.33.a/b/c`, `chaosx.nr5.34.a/b/c`, and `chaosx.nr5.37.a/b/c`. Their complete two-scenario probability analyses report zero unresolved inputs: `.33` is `probability-f0f4bc34292ccf15c5eefe77`, `.34` is `probability-9a73f57c2853aceedabf7c6b`, and `.37` is `probability-5e3e97eec6b1c11cbe72f27d`.

No simplification, fallback faction, placeholder event, placeholder localisation, copied country package, missing asset, or deferred accepted item remains in the Successor Relations scope.
