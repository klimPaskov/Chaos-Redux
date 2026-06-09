# Event005 Focus Tree Audit: Priority Republic Layout Patch

Subagent role: `chaosx_focus_tree_auditor`

Date: 2026-06-05

## Scope

Audited the current working-tree versions of:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

References consulted before focus edits:

- Offline Paradox wiki core pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding.
- Offline Paradox wiki National focus modding page.
- Vanilla documentation: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`.
- Vanilla focus precedent: `baltic_shared.txt`, `poland.txt`, `soviet.txt`.
- Repo skills: `hoi4-focus-trees`, `chaos-redux-events`.

No flag, sprite, image, or asset files were touched.

## Files Changed

- `common/national_focus/005_soviet_collapse_republics.txt`

Layout-only coordinate changes were made for exact focus-on-pathline defects in the three priority republic trees:

- `ukr_soviet_collapse_open_the_liaison_offices`: `y 5 -> 6`
- `ukr_soviet_collapse_officer_patronage_lists`: `y 7 -> 6`
- `ukr_soviet_collapse_dead_fields_living_columns`: `x 28 -> 29`
- `ukr_soviet_collapse_black_banner_takes_the_villages`: `x 31 y 17 -> x 30 y 18`
- `blr_soviet_collapse_railway_neutrality`: `y 11 -> 10`
- `blr_soviet_collapse_village_warning_bells`: `y 7 -> 8`
- `blr_soviet_collapse_minsk_does_not_own_every_tree`: `y 17 -> 16`
- `kaz_soviet_collapse_alash_memory_restored`: `x 25 -> 26`
- `kaz_soviet_collapse_aul_councils_and_red_teachers`: `x 29 -> 28`

No focus prerequisites, mutual exclusions, rewards, AI, localisation, icons, or mechanics were changed.

## Validation

Read-only parser checks after the patch:

- `soviet_collapse_ukraine_focus_tree`: 83 focuses, 0 duplicate coordinates, 0 exact focus-on-pathline candidates, approx prerequisite crossings reduced to 20.
- `soviet_collapse_belarus_focus_tree`: 53 focuses, 0 duplicate coordinates, 0 exact focus-on-pathline candidates, approx prerequisite crossings reduced to 39.
- `soviet_collapse_kazakhstan_focus_tree`: 92 focuses, 0 duplicate coordinates, 0 exact focus-on-pathline candidates, approx prerequisite crossings remains 82.
- `rg` check found no unsupported `<=` usage in the four audited focus files.

I did not run the game or a full HOI4 load validation.

## Audit Findings

The current files no longer show focus reward idea spam in the priority republic trees: direct `add_ideas` usage was 0 for Ukraine, Belarus, and Kazakhstan in the audited focus blocks. The remaining reward complaint is instead mostly repeated abstract helper rewards and repeated generic tooltip families, especially in the custom splinter file.

Ukraine, Belarus, and Kazakhstan have distinct political, industry/logistics, military/diplomacy, and expansion-like lanes on paper, but the layouts are still not compact-clean. Kazakhstan is the largest offender: 92 focuses and 82 approximate prerequisite-line crossings make it too tangled for the requested readable compact tree. Belarus still has 39 approximate crossings after the small patch. Ukraine is improved but still has 20 approximate crossings and a very wide spread.

The three priority republic trees still lack direct route-level AI strategy payoffs in focus rewards. Direct `add_ai_strategy` count was 0 for Ukraine, Belarus, and Kazakhstan. They rely on `ai_will_do` and shared crisis variables, but the skill standard expects route-specific AI behavior for major routes.

Direct claims/wargoals were also absent in the three priority republic trees during the parser pass. Some expansion behavior may be routed through helper effects or decisions, but direct focus rewards do not visibly show the requested aggressive expansion/settlement identity.

Factory and ancient-restoration successors are stronger than the generic splinter set. CFR/MFR/OGB and the ancient trees include more concrete construction, claims, decisions, wargoals, and route-specific effects. The generic 47-focus custom splinter templates still repeat generic reward tooltips such as `soviet_collapse_custom_splinter_political_route_reward_tt` across many route nodes, which supports the user complaint about repeated generic helper rewards.

No midpoint focus between mutually exclusive alternatives was detected in the priority republic trees by checking OR-prerequisite groups against mutually exclusive pairs. The issue there is pathline density and branch sprawl, not midpoint OR joins.

## Remaining Blockers

- A real compact-layout pass is still needed for Ukraine, Belarus, and especially Kazakhstan. The remaining crossing counts are too high for the user request.
- The custom splinter trees need more country-specific rewards, decisions, claims, wars, units, and AI instead of repeated generic route helper/tooltip packages.
- Major republic expansion branches need clearer direct focus-to-map consequences or documented decision handoffs: claims, cores, wars, settlement decisions, mandates, or postwar handling.
- Route-specific AI strategy remains underdeveloped for Ukraine, Belarus, Kazakhstan, and most generic custom splinters.
- This patch is intentionally bounded; it does not satisfy full focus-tree completion standards.
