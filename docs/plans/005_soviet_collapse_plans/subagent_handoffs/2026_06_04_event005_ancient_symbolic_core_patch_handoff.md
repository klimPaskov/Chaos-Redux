# Event005 Focus Tree Auditor Handoff: Ancient Symbolic Core Patch

Date: 2026-06-04

## Scope and no-touch confirmation

- Audited Event005 focus script files: `common/national_focus/005_soviet_collapse_factory_successors.txt`, `common/national_focus/005_soviet_collapse_custom_splinters.txt`, `common/national_focus/005_soviet_collapse_ancient_restorations.txt`, and `common/national_focus/005_soviet_collapse_republics.txt`.
- Patched only `common/national_focus/005_soviet_collapse_ancient_restorations.txt`.
- Did not edit `common/national_focus/005_soviet_collapse_custom_splinters.txt` or `common/national_focus/005_soviet_collapse_republics.txt`.
- Did not inspect or edit `gfx/flags`, `interface/flags`, flag sprites, flag DDS files, or other flag/gfx asset files.
- Did not inspect or edit interface/gfx asset definitions.

## Route coverage table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Political branch | All four ancient restorations have council, law debate, charter, and symbolic-vs-expansion route choice branches. | Implemented but compact | Political identity is present, but route-specific leader/advisor/law changes remain limited. |
| Industry branch | Ancient restorations have market/workshop/road/water/pass branches plus state construction rewards. | Implemented but still reward-heavy | Industry is geographically flavored but mostly one-time buildings and helper rewards. |
| Expansion branch | Ancient restorations have old-border files, expansionist route focuses, returned-names endgames, and high-chaos late endpoints. | Implemented | Existing parent work already added war goals, assault columns, neighbor expansion helpers, and claim/core behavior on expansion paths. |
| Symbolic survival route | `KZR_restoration_survives_modern_war`, `SOG_restoration_survives_modern_war`, `KHW_restoration_survives_modern_war`, `ALN_restoration_survives_modern_war`. | Patched | These now core controlled claimed territory and add rail/mobile guard power instead of staying mostly authority/building payoffs. |
| AI route behavior | Every focus in the four files has `ai_will_do`. | Partial | Most AI remains base-weighted; ancient route forks have some war/no-war modifiers, but broader route-aware plans are still shallow. |

## Remaining shallow or generic content

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`: 1005 focuses, but the scan still found 404 `custom_effect_tooltip` calls, 396 construction reward calls, 130 equipment stockpile calls, and only 6 direct `create_wargoal` / 6 direct `declare_war_on` calls. This suggests many custom splinter branches still lean on helper-visible reward packages rather than direct route mechanics.
- `common/national_focus/005_soviet_collapse_republics.txt`: 501 focuses with 170 construction rewards, 91 stability rewards, and only 7 state claims. Several republic branches likely remain state-building heavy and expansion-light compared with the spec.
- `common/national_focus/005_soviet_collapse_factory_successors.txt`: 128 focuses with stronger route mechanics than republics, but repeated icon assignments and construction-heavy rewards remain visible.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`: 64 focuses are compact and distinct, but still share several icon families and helper reward motifs by design.

## Icon coverage table

| File | Focuses | Icon assignments | Unique assigned icons | Repeated icon risk |
| --- | ---: | ---: | ---: | --- |
| `005_soviet_collapse_factory_successors.txt` | 128 | 128 | 113 | Several CFR/MFR icon ids repeat across branch variants. |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 1005 | 885 | Repeated generic branch icon ids remain across multiple compact trees. |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 64 | 42 | Reused family icons include `ancient_guard_old_routes`, `ancient_league_bargain`, `ancient_old_border_files`, `ancient_restoration_survives`, `ancient_returned_names_endgame`, `ancient_symbolic_state`, and `ancient_workshop_compact`. |
| `005_soviet_collapse_republics.txt` | 501 | 501 | 458 | Repeated regional/republic icons remain, but no asset definitions were inspected due no-touch constraints. |

## Localisation and reward mismatch list

- Ancient focus ids changed by this patch already have localisation in `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`; no new player-facing keys were added.
- The patched symbolic endpoint descriptions still match the new rewards because they describe guarded roads, city survival, water/road control, and pass control. The new controlled-claim coring fits those descriptions.
- No full localisation encoding or missing-key audit was run. This handoff only confirms existing ancient focus keys were found during targeted search.
- Remaining mismatch risk: some custom/republic focus titles likely still promise distinctive politics while rewards are generic construction, stability, equipment, or helper packages. This was audited at pattern level only because the requested patch scope was ancient restorations.

## AI behavior gaps

- All four Event005 focus files have `ai_will_do` blocks for every focus in the mechanical scan.
- Ancient symbolic-vs-expansion choices have some context weighting (`has_war = no` or `has_war = yes`), but endpoint AI still uses mostly base weights.
- Custom splinter and republic trees need deeper route-aware AI behavior around expansion validity, league membership, high-chaos escalation, and invalid target avoidance.

## High-priority fixes made

Changed focus ids:

- `KZR_restoration_survives_modern_war`
- `SOG_restoration_survives_modern_war`
- `KHW_restoration_survives_modern_war`
- `ALN_restoration_survives_modern_war`

Before:

- These symbolic survival endpoints mostly granted authority variables, recognition/stability, and one-time buildings.
- They did not convert controlled old claims into cores and had weak unit/map payoff compared with the expansionist endpoints.

After:

- `KZR_restoration_survives_modern_war` adds `soviet_collapse_apply_focus_rail_authority_reward = yes` and cores controlled claimed states.
- `SOG_restoration_survives_modern_war` adds `soviet_collapse_apply_focus_mobile_columns_reward = yes` and cores controlled claimed states.
- `KHW_restoration_survives_modern_war` adds mobile columns, cores controlled claimed states, and improves infrastructure in those integrated controlled claims.
- `ALN_restoration_survives_modern_war` adds mobile columns, cores controlled claimed states, and fortifies those integrated controlled claims.

## Safety notes

- The patch uses existing scripted effects and existing localisation.
- The new core logic uses existing state-scope patterns already present in `soviet_collapse_apply_high_chaos_neighbor_expansion_plan`: `every_controlled_state`, `is_claimed_by = ROOT`, `is_core_of = ROOT`, and `add_core_of = ROOT`.
- No new ideas, flags, icons, decisions, formables, asset references, or localisation keys were added.
- No broad route redesign or new route family was created.

## Validation run

- `git diff --check -- common/national_focus/005_soviet_collapse_ancient_restorations.txt` passed.
- Unsupported comparison operator scan on `common/national_focus/005_soviet_collapse_ancient_restorations.txt` returned no matches.
- Brace balance check with `awk` returned `0`.
- Mechanical audit counts were generated for focus count, AI count, search filter count, icon assignment count, and common reward/effect patterns across the four Event005 focus files.

## Skipped validation and why

- No in-game focus-tree layout validation or screenshot pass was run from this subagent context.
- No full HOI4 parser run was available in this turn.
- No asset validation was run because the task explicitly forbids inspecting or editing flag/gfx asset files and interface/flag assets.
- No localisation file was edited, so localisation encoding conversion was not needed.

## Remaining route risks

- The ancient trees are still compact 16-focus trees per tag; they are stronger after this patch, but they are not full major-country trees.
- Reused ancient icon families remain a visible identity weakness unless the parent later routes icon work through the asset pipeline.
- The symbolic route now has real core/unit/map payoff, but it still lacks a separate decision or mission family for postwar integration.
- Custom splinter and republic trees still need a deeper audit pass for repeated helper rewards, generic construction/stability rewards, and route-aware AI.
- No plan addendum was written because this task requested one bounded patch, not a broad ancient-restoration redesign.
