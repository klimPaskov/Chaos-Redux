# Event 012 Africa — Current Source of Truth Map

Updated: 2026-06-18

## Current accepted design

The accepted source package is the full Event 012 Africa spec folder under `docs/specs/012_africa_specs/`. The implementation should treat the main design files as one package rather than elevating any small correction above the continental-unifier system.

Primary design surfaces:

- `specs/012_africa_spec_part_1_core.md`
- `specs/012_africa_focus_tree_plan.md`
- `specs/012_africa_decisions_missions_ui.md`
- `specs/012_africa_country_packages_and_subjects.md`
- `specs/012_africa_evolutions_world_end_and_scenarios.md`
- `specs/012_africa_niche_country_expansion.md`
- `specs/012_africa_niche_polity_expansion.md`
- `specs/012_africa_niche_polities_and_absurd_paths.md`
- `specs/012_africa_niche_authorities_high_chaos_expansion.md`
- `specs/012_africa_high_chaos_absurd_paths.md`

Supporting surfaces:

- `research/` for historical and ecological inspiration notes.
- `matrices/` for AI, asset, decision, country-package, achievement, and acceptance maps.
- `focus_graphs/` for architecture sketches.
- `prompts/` for implementation, asset, achievement, super-event, decision/mission, and `/goal` handoff prompts.

## Country naming style

Country and cosmetic names use direct polity names. Avoid generic political attachments in country names: no `Compact`, `Office`, `Bureau`, `Board`, `Commission`, `Registry`, `Mission`, `College`, `Guard`, or `Authority` as the public country name unless it is a real intended state form. `Kingdom`, `Sultanate`, `Republic`, `Federation`, `Confederation`, `Union`, `Empire`, and similar direct state forms are fine when they fit the route. Ideology-specific names are encouraged where they make the tag feel alive.

Mechanic names can still use administrative language. A country can be `Kongo` while its focus branch contains a reconstruction office, or `Oyo` while its army route has a cavalry bureau.

## Leader display-name flavour

The Event 012 leader/court display-name pool includes:

- `qaama saalaa koo xuuxaa`
- `haadha kee waliin wal qunnamtii saalaa raawwadhe`

Keep those strings untranslated in player-facing English and keep raw strings out of internal ids, file paths, tags, variables, sprite names, and asset text. The joke belongs to event-created or event-recast public ruler/court/council display names; serious country, office, historical polity, institution, symbol, and source notes remain researched.

## Current design emphasis

- A valid African-capital country becomes the unifier and receives the Africa package.
- Paper cores and staged integration satisfy the catalogue fantasy without creating an instant snowball.
- The Charter League lets African countries cooperate against colonisers before integration pressure begins.
- RSA in the Allies uses the civil-war branch and Allied peace-out rule.
- The Archive of Old Seats and Authority Atlas add niche historical authorities, restoration offices, specialist schools, and high-chaos absurd actors without turning human polities into caricatures.
- Nonhuman/supernatural routes are explicit fictional/high-chaos actors and use shared nonhuman classification when implemented.
- Final super-event titles, quotes, button remarks, cultural references, and audio stay research-gated.

## June 18 implementation disposition

Parent commit `9858db02` closes the previously queued high-chaos actor package gap for:

- `BON` Bonobo Kinship Congress
- `HYR` Hyena Radio Dominion
- `BIR` Bird of the Walls
- `SAO` Sao Terracotta Host

The current documentation evidence for that closure is:

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_missing_high_chaos_actor_parent_handoff.md`
- `docs/assets/012_africa/missing_high_chaos_actor_assets/manifest.md`
- `docs/assets/012_africa/implementation_asset_manifest.md`
- `docs/events/012_africa_foundation.md`

This closes the actor-package, portrait/flag, achievement-icon, and prompt-named achievement queue for those four tags. It does not close the broader Event 012 completion blockers around accepted foundation-addendum depth, Continental Congress presentation depth, country-package depth, UI/animation proof, balance proof, or targeted scenario validation.

The root-terminal World Is One super-event disposition is an intentional hybrid. The World Root terminal branch shares base slot `72` text and image presentation (`The World Is One`) and uses distinct root-terminal audio id `80`. Archive remains the distinct terminal presentation variant where implemented through slot `79`.

Later June 18 parent tranches close additional bounded gaps:

- `c37da58d` regenerates the Event 012 Africa goal and idea icons without white backgrounds. Goal icons remain goal-sized DDS files, while idea icons are distinct 64x64 designs rather than downscaled goal art. The live DDS files are under `gfx/interface/goals/012_africa/` and `gfx/interface/ideas/012_africa/`, with source packages and manifests under `docs/assets/012_africa/`.
- `c13fe459` makes the high-chaos Bestiary focus branch hidden until `AFR_high_chaos_door` reveals it through `africa_high_chaos_branch_revealed` and `mark_focus_tree_layout_dirty`.
- `94857ce3` gives the Continental Congress Seats and Bestiary Terms GUI actions the same concrete support-equipment, manpower, and command-power requirements as their decision equivalents, using shared helpers so the GUI and normal decision paths cannot diverge.
- The current dossier-AI tranche adds Authority Atlas lifecycle and eight-profile historical dossier AI to `common/ai_strategy/012_africa.txt`, and weights the Authority Atlas dossier decisions by route/profile in `common/decisions/012_africa_decisions.txt`.
- The current dossier-settlement tranche adds once-only value-only settlement outcomes for every historical dossier ID through `africa_apply_selected_dossier_specific_settlement_effects`, visible through `GetAfricaSelectedDossierSettlementSummary` in the Authority Atlas header.
- The current dossier-resistance tranche turns post-settlement resistance watches into active gameplay: observer settlements can commit timed Congress mediation, direct Archive settlements can commit timed enforcement, both pay concrete non-PP resources plus dossier-profile logistics, both use the stored resistance dossier/seat context after the selected dossier advances, both block further settlements while the one active watch is unresolved, and both produce profile-specific value movement plus visible local reports that name the intervention method.

These tranches reduce the active blocker list, but they do not close Event 012. Remaining known blockers still include deeper package-specific historical dossier missions beyond settlement and resistance value movement, richer settlement forks beyond the observer/direct plus intervention split, fuller Continental Congress presentation families, targeted scenario validation, and final super-event sourcing/audio blockers where the research handoffs still require it.

## Cleanup note

Earlier correction-only name-protocol files and matrices have been removed from the current handoff. Their useful content is folded into the normal country-package, prompt, and acceptance surfaces above.

## V7 prompt note

The implementation goal prompt is intentionally longer than the V6 compact version and still points to the spec pack instead of repeating the whole design.

## V8 naming note

The latest cleanup keeps the longer V7 goal prompt but adds the direct country-name rule. Country and cosmetic names should be simple polity/place names with ideology variants where useful, while generic administrative words stay in mechanics, decisions, focus groups, or subject-status notes.

## V9 structure cleanup note

Short addenda and duplicate manifests are no longer separate source files. Their content is folded into the main spec, matrix, prompt, graph, and subagent-handoff files. Use the primary design surfaces listed above instead of chasing small revision fragments.
