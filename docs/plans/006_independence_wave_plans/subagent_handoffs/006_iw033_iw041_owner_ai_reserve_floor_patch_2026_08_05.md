# Event 006 IW-033 / IW-041 owner AI reserve-floor patch

Date: 2026-08-05

Owner: `/root`

## Scope

This bounded owner tranche closes the executable AI gap identified by the probability and completion audits for the Karelia and Crimean Tatar State package adapters. It does not change player-facing costs, package identity, allocation, or the shared focus tree.

## Changes

- Added the centralized `independence_wave_karelia_crimea_ai_floor` table for command power, manpower, infantry equipment, support equipment, trains, convoys, fuel, and separate major-security reserve thresholds.
- Added package-scoped scripted predicates for foundation readiness, lower-ledger preference, land and maritime reserve floors, diplomatic reserve selection, and major-security floors.
- Added `ai_will_do` modifiers to all regular IW-033/IW-041/combined host and network decisions. The AI now waits for foundation settlement, doubles weight for the lower regional ledger, and receives a zero-weight safety gate when the action would consume the package's protected reserve. Founding missions remain passive and are not made selectable.
- Documented the trigger contract in `common/scripted_effects/chaosx_dynamic_effects.md` and the package behavior in `docs/events/006_independence_wave/karelia_crimea_packages.md`.

## Source review

- Offline wiki: `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` (strict comparison, resource, manpower, command-power, and `check_variable` forms) and `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` (MTTH/`ai_will_do` modifier structure).
- Vanilla documentation: `documentation/triggers_documentation.md` and the decision documentation section of the offline snapshot.
- Existing Chaos Redux precedents: Event 006 custom-cost triggers and `check_variable` comparisons between scoped variables.

## Static validation

- Touched Clausewitz files have balanced braces.
- No unsupported `<=` or `>=` operators were introduced.
- All decision-referenced helper names are defined in the package trigger file.

## Remaining evidence and risks

- The next `chaosx_ai_probability_auditor` pass must run `hoi4.probability_compare` against the same IW-033/IW-041 decision scenarios used in the baseline handoff. The current MCP evidence is source/typed-state partial, so this patch does not claim a normalized probability result.
- No live game was launched; runtime consumer validation remains user-owned under the repository rules.
