# Event005 Soviet Collapse Focus Tree Current Audit Handoff

Date/time: 2026-06-04 06:37:38 UTC

Subagent role: `chaosx_focus_tree_auditor`

## Scope

Audited the current state of these Event005 focus files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Related scripted effects, triggers, ideas, and localisation were inspected only where needed to understand focus rewards, especially the generic republic reward helpers and high-chaos composite payloads.

Required references consulted before patching:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- Required core offline wiki pages listed in `AGENTS.md`
- Vanilla docs under `~/projects/Hearts of Iron IV/documentation`, including `effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md`
- Vanilla focus precedent from `~/projects/Hearts of Iron IV/common/national_focus/uruguay.txt`

## Files Changed

- `common/national_focus/005_soviet_collapse_republics.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_063738_event005_focus_tree_current_audit_layout_patch.md`

## Focus IDs Changed

Coordinate-only layout patches:

- `ukr_soviet_collapse_army_of_the_republic`
  - Moved from `x = 25, y = 4` to `x = 26, y = 4`.
  - Reason: it overlapped `ukr_soviet_collapse_war_without_a_declaration`.
- `ukr_soviet_collapse_black_sea_port_ledgers`
  - Moved from `x = 25, y = 5` to `x = 26, y = 5`.
  - Reason: it overlapped `ukr_soviet_collapse_open_the_liaison_offices`.
- `baltic_soviet_collapse_singing_barricades_early`
  - Moved from `x = 20, y = 3` to `x = 22, y = 4`.
  - Reason: it overlapped `baltic_soviet_collapse_baltic_league_first`.

No reward, prerequisite, mutual exclusion, AI weight, localisation, icon, sprite, or flag edits were made.

## Audit Findings

Current audit scale:

- Parsed 1,698 focuses across 41 focus trees in the four audited files.
- File split: 501 focuses in republics, 1,005 in custom splinters, 128 in factory successors, 64 in ancient restorations.

Duplicate/repeated payload checks:

- No exact duplicate helper calls were found inside a single focus completion reward.
- No duplicate `unlock_decision_tooltip` calls were found inside a single focus.
- No duplicate one-line `add_ideas = ...` calls were found inside a single focus.
- No unknown prerequisite or mutual-exclusion focus references were found in the four audited focus files.
- No asymmetric mutual-exclusion pairs were found after parsing all `mutually_exclusive` blocks.

Layout/pathline findings:

- Three same-tree duplicate coordinate collisions were found and patched.
- A post-patch duplicate-coordinate scan reports zero duplicate coordinate groups across the four audited files.
- Several dense branches still have long crosslinks, especially in Ukraine, Baltic, Kazakhstan, custom splinter late-game routes, and factory successor capstones. These need visual review in-game or with a focus-layout renderer before larger coordinate work; they were not redesigned in this bounded patch.

Reward-depth findings:

- Many republic and custom-splinter focuses still rely on repeated generic helpers such as:
  - `soviet_collapse_apply_focus_legal_recognition`
  - `soviet_collapse_apply_focus_military_consolidation`
  - `soviet_collapse_apply_focus_depot_and_supply_control`
  - `soviet_collapse_apply_focus_foreign_channel`
  - `soviet_collapse_apply_focus_republican_compact_plan`
- These helpers are not literal duplicate calls within the same focus, and they now carry deeper scripted effects, recovery progress, route payloads, and high-chaos escalation guards. The remaining issue is design variety: many mid-branch focuses still feel like the same helper family under different names unless they also have a local decision unlock, route-specific flag, map change, special unit, or capstone effect.
- The high-chaos composite path is safer than earlier reward-spam patterns because `soviet_collapse_apply_high_chaos_focus_payload` gates its one-time escalation behind `soviet_collapse_high_chaos_focus_payload_granted` and its assault columns behind `soviet_collapse_high_chaos_focus_assault_columns_granted`. Manual assault-column calls in late capstones remain intentional-looking endgame spikes, not duplicate same-focus calls.

Route/branch findings:

- Republic trees generally have political, industry, military, diplomacy, and special-route content, but most lack explicit `FOCUS_FILTER_ANNEXATION` tagging even where high-chaos, border, federation, or direct-claim gameplay exists. This makes expansion routes harder to search and visually under-signaled.
- Kazakhstan and Ukraine are deep but still heavy on repeated generic helper families. Their distinct identity is strongest where focuses add concrete mechanics: League councils, claim/endgame routes, foreign missions, high-chaos branches, railway/depot map changes, and route flags.
- Baltic, Moldova, Caucasus, Belarus, and internal republic trees have real political/diplomatic/military depth, but several expansion-adjacent payoffs are represented through diplomacy or high-chaos helpers rather than explicit expansion branch labels.
- Custom splinter trees mostly have broad 47-focus structures with political, industrial, military, diplomacy, and special branches, but many do not expose expansion through `FOCUS_FILTER_ANNEXATION`; expansion usually arrives through hidden-doctrine, extreme, or endgame helpers. This is a route-visibility gap, not a syntax blocker.
- Factory successors are more distinctive than generic splinters:
  - `CFR` has construction mandate, housing, contract, and builder-state identity.
  - `MFR` has arsenal/client/unsafe-output identity but only a shallow explicit expansion signal.
  - `OGB` is shorter but has a clear old-name restoration path and endgame.
- Ancient restorations are playable and thematic but short at 16 focuses each. They have clear symbolic-vs-expansion choices and old-name mechanics, but their industry and diplomacy branches are thin compared with the focus-tree skill’s large-country depth standard. This should be treated as a future expansion plan, not a small patch.

## Remaining Gaps

- Add a dedicated follow-up plan for expansion route visibility:
  - audit focuses that create claims, cores, war goals, high-chaos neighbor pressure, federation plans, or endgame expansion;
  - add `FOCUS_FILTER_ANNEXATION` where appropriate;
  - avoid broad route redesign in a subagent patch.
- Continue reducing generic-helper repetition by swapping select mid-branch focuses to existing specific helpers where a specific helper already matches the local country identity.
- Ancient restoration trees need deeper industry/military/diplomacy payoffs if they are intended to be long-lived playable countries rather than compact special trees.
- Custom splinter trees should receive targeted route-specific decision unlocks or visible map/unit/advisor consequences in branches that currently only apply one generic helper.
- Dense pathline crossings should be reviewed with a focus tree visual pass before broad coordinate changes.

## Validation

Validation was run after the focus-coordinate patch and after this handoff was created.

- Brace balance across the four audited focus files:
  - `005_soviet_collapse_republics.txt`: balanced, 4,248 open braces and 4,248 close braces.
  - `005_soviet_collapse_custom_splinters.txt`: balanced, 10,876 open braces and 10,876 close braces.
  - `005_soviet_collapse_factory_successors.txt`: balanced, 1,381 open braces and 1,381 close braces.
  - `005_soviet_collapse_ancient_restorations.txt`: balanced, 638 open braces and 638 close braces.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt`: passed with no output.
- `git diff --check --no-index /dev/null docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_063738_event005_focus_tree_current_audit_layout_patch.md`: produced no whitespace diagnostics for the new untracked handoff.
- Unsupported comparison operator scan on the changed focus file and this handoff: clean after removing the literal command text from this handoff.
- `git diff --name-only` flag-file scan limited to this patch's changed files: no matches.

## No-Flag-Touch Proof

Hard constraint observed: no `gfx/flags`, `.tga`, flag sprite, flag `.gfx`, or visual flag asset files were edited. This patch only changes focus coordinates and adds this markdown handoff.
