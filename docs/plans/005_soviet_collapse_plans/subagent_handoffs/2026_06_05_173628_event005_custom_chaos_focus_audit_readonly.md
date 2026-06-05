# Event005 Custom And Chaos Focus Tree Audit Handoff

Subagent role: `chaosx_focus_tree_auditor`

Scope: read-only audit of the current Event005 custom, chaos, factory, and ancient focus trees, with priority on `common/national_focus/005_soviet_collapse_custom_splinters.txt`.

This is not an Event005 completion claim.

## Required References Consulted

- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- Core offline wiki pages required by `AGENTS.md`: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding
- Vanilla focus precedent under `~/projects/Hearts of Iron IV/common/national_focus/`, especially China focus mutual-exclusion, path, AI, and war-goal structures
- Vanilla documentation under `~/projects/Hearts of Iron IV/documentation/`, especially effects, triggers, modifiers, and script concept documentation
- `hoi4-focus-trees` skill guidance
- Current Event005 source docs: `docs/events/005_soviet_collapse.md`, `docs/plans/005_soviet_collapse_plans/source_of_truth_map.md`, and spec parts 5 and 6

## Files Audited

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt` was read only to interpret shared payoff helpers. It was not edited.

## Files Changed

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_173628_event005_custom_chaos_focus_audit_readonly.md`

No focus, flag, sprite, image, asset, localisation, scripted effect, decision, event, or history file was edited.

## Mechanical Audit Results

Parsed current filesystem state, not clean `HEAD`.

- Total audited focus trees: 32
- Total audited focus blocks: 1,197
- `005_soviet_collapse_custom_splinters.txt`: 25 trees, 1,005 focuses
- `005_soviet_collapse_factory_successors.txt`: 3 trees, 128 focuses
- `005_soviet_collapse_ancient_restorations.txt`: 4 trees, 64 focuses
- Duplicate focus IDs in the three audited files: 0
- Duplicate coordinates within a tree: 0
- Parent focus at same row or below child focus: 0
- AND prerequisites requiring mutually exclusive branches: 0
- Vertical prerequisite line-through-focus heuristic hits: 0
- Missing `ai_will_do` blocks: 0
- Direct focus reward idea churn (`add_ideas`, `remove_ideas`, `swap_ideas`, `add_timed_idea`): 0
- Unsupported `<=` or `>=` operators in the three audited focus files: 0
- `git diff --check --` on the three audited focus files: no output

I did not make a coordinate or prerequisite patch because there was no narrow, unambiguous layout fault in the requested three files.

## Current Quality Findings

The custom/chaos trees are mechanically stronger than a pure reward-spam scaffold because shared helpers now do real work. The audited helper definitions include dynamic assault templates and units, manpower and stockpiles, controlled-state cores, Soviet and neighboring breakaway war goals, high-chaos direct wars, and AI conquer/antagonize strategies.

The remaining problem is presentation and route identity: many focus rewards still read as repeated `soviet_collapse_* = yes` helper calls rather than distinct country-specific payoffs.

Three-file aggregate:

- Custom splinters: 910 of 1,005 focuses call `soviet_collapse_*` helpers; broad helper-heavy heuristic flagged 898.
- Factory/OGB/MFR/CFR file: 119 of 128 focuses call helpers; broad helper-heavy heuristic flagged 104.
- Ancient restorations: 49 of 64 focuses call helpers; broad helper-heavy heuristic flagged 40.

Direct expansion visibility is uneven:

- Custom splinters contain 7 direct war effects and 22 direct AI strategy effects, but no direct claim/core effects in the focus file. Many trees rely on helper names for claims, cores, and neighbor expansion.
- Factory successors contain 3 direct war effects and 17 direct AI strategy effects, but no direct claim/core effects in the focus file.
- Ancient restorations contain 4 direct war effects, 8 direct AI strategy effects, and 35 direct claim/core effects. Their symbolic versus expansionist mutual exclusions are clearer than most custom splinter mutexes.

## Branch And Mutex Assessment

Current branch lines do not appear to run through mutually exclusive branches or through other focuses in the requested files.

Mutual exclusions are mechanically valid, but they vary in strength:

- Stronger examples: ancient symbolic versus expansionist choices, `PRA_the_pale_line_endures` versus `PRA_rails_over_capitals`, `DSC_republic_of_roll_calls` versus `DSC_congress_of_the_dead_army`, and MFR's route quadrants.
- Weaker repeated pattern: many 47-focus custom splinters use a settlement versus radical fork where one side mostly calls `soviet_collapse_apply_custom_splinter_settlement_identity` and the other applies pressure or chaos assault helpers. These are not broken, but they still feel scaffold-like because the lore and mechanics are too similar from tree to tree.

## Top Unresolved Blockers

1. `005_soviet_collapse_custom_splinters.txt` remains the main blocker for the user's complaint. Most 47-focus custom trees still rely on repeated helper identities instead of bespoke country mechanics, visible unlocks, direct claims/cores, or named local expansion programs.
2. Chaos countries are dangerous through shared helper effects, but that danger is often indirect. If the standard is direct focus-file expansion paths with visible claims, cores, wars, wargoals, units, and AI aggression per chaos tree, many custom splinters still fail it.
3. Several compact chaos trees are functionally aggressive but still shallow as focus trees: `TSC`, `RMC`, `NRF`, `ICD`, `PRA`, and `OGB` have fewer route nodes than the user-facing premise implies.
4. Ancient restorations now have clearer expansionist mechanics, but each is still a 16-focus skeleton. They satisfy compact symbolic/expansionist routing better than before, but not a deep ancient-restoration package.
5. Factory successors are mixed: CFR has recent depth work, MFR has direct war/AI strategy payoffs but remains helper-heavy, and OGB's Volga rival branch is meaningful but still too compact for its spec.

## Recommended Parent Work

Do not start with a global coordinate pass for these three files; the current blocker is depth and visible route payoff.

Recommended order:

1. Pick 3-5 high-chaos custom splinters with the weakest direct expansion visibility, then add explicit focus-file or tooltip-visible route payoffs using the existing shared helpers rather than inventing broad new mechanics.
2. Convert repeated settlement/radical mutexes into country-specific route locks with at least one bespoke visible unlock, claim/core package, unit template/formation, target family, or decision family per side.
3. Give compact chaos trees one additional direct route payoff each before broad polish: direct local war/claims/AI for aggressive endings, direct defensive/league/recognition mechanics for settlement endings.
4. Leave assets and flags untouched until the parent explicitly reopens that scope.
