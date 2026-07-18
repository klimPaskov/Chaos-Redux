# Event 12 Scramble Response and World Order

## Purpose

This subsystem begins after `africa_is_one` and preserves the original Event 12 host. It resolves the foreign Scramble response through recognition, conditional recognition, sanctions, ultimatums, an optional expedition war, and an aftermath congress. It then exposes six continent-package candidates and the later world-order routes.

No response grants African membership, integration, annexation, or cores. The foreign response is a diplomatic and military settlement around the already negotiated Charter League.

## State flow

1. `chaosx.nr12.309` calls `africa_initialize_scramble_and_world_packages` once.
2. One explicit post-unification census registers foreign majors, faction leaders, and governments with African holdings. No recurring daily, weekly, or monthly world scan exists.
3. Each participant explicitly chooses recognition, conditional recognition, sanctions, or an ultimatum in `africa_world_order.1`.
4. Four timed phases track diplomatic shock, coalition formation, intervention or settlement, and aftermath.
5. Intervention can produce a real war. Pairwise on-actions record war, capitulation, and peace without periodic country iteration.
6. During the aftermath, Action 85 installs one documented actor for each of the six external continent packages. Sponsorship creates a separate 180-day material obligation.
7. The aftermath cannot close until all six dedicated packages are installed and the Scramble requirements are resolved.
8. Settled packages can consent to union, remain sovereign, become rivals, fight a prepared continental war, or accept a postwar submission settlement.
9. The terminal World identity remains unavailable until all continent packages are resolved, chaos is above the terminal threshold, no ordinary settlement remains pending, and the researched final super-event package sets `africa_the_world_super_event_package_ready`.

## Tuning and shared logic

- `common/script_constants/012_africa_world_order_constants.txt` contains phase identifiers, continent identifiers, package statuses, shared costs, durations, thresholds, and reward values.
- `common/scripted_triggers/012_africa_world_order_triggers.txt` contains candidate, phase, sponsorship, union, war, and terminal checks.
- `common/scripted_effects/012_africa_world_order_effects.txt` contains the one-time census, response choices, package installation, obligations, package ledgers, and terminal cleanup.
- Actions 77 through 92 continue to use the shared Action 1 through 102 selector and outcome kernel. The world-order file supplies their exact full, partial, and failure semantics.
- Candidate countries qualify only if they still use the generic focus tree or carry the explicit `africa_world_package_focus_replacement_approved` audit flag. Meaningful existing country trees are not replaced.
- A candidate also needs `africa_world_package_implementation_ready` before Action 85 can install it. This is an implementation gate, not a gameplay fallback.

## Continent packages

The six package mechanics are distinct and use separate public values:

- Middle East: Crossroads Balance, including Arab, Persian, Anatolian, minority, holy-site, water, and oil values.
- Europe: Continental Settlement, including industry, sovereignty, war memory, ideology, colonial debt, and borders.
- Asia: Centers of Asia, including eastern, southern, inland, archipelago, food and river, and corridor values.
- North America: Continental Bargain, including industry, federal representation, sovereignty, Caribbean inclusion, indigenous settlement, migration, and command.
- South America: Andes, Amazon, and Plata Balance, including three regional voices, indigenous representation, resources, and foreign debt.
- Oceania: Ocean Network, including convoy reach, island representation, naval protection, indigenous settlement, air routes, and dispersed industry.

The Middle East, Europe, and Asia packages currently have their full dedicated focus architectures in their respective `common/national_focus/012_africa_world_<region>_focus.txt` files. Other candidates are not marked implementation-ready until their complete package files exist. This keeps unfinished packages unreachable and prevents a generic or copied focus-tree substitute.

## Middle East implementation

The Crossroads Balance begins by ending foreign mandates and establishing water, food, pipeline, and holy-city settlements. It has five mutually exclusive constitutional routes:

- Arab Federal Pact
- Plural Crossroads Federation
- Royal Concert
- Union of Socialist Republics
- Desert Covenant

The Desert Covenant is additionally locked by `africa_middle_east_high_chaos_package_reviewed`. That flag must remain unset until the dedicated source and sensitivity review confirms its text, nonhuman actors, symbols, and asset treatment. It never turns a human Middle Eastern identity into a supernatural species.

Every route must complete representation, command, Africa diplomacy, withdrawal law, and a final settlement congress before receiving a public cosmetic identity and replacing the founding-problem spirit.

## Europe implementation

The Continental Settlement begins with border guarantees, industrial and rail reconstruction, and a colonial reckoning. It has six mutually exclusive routes: democratic federation, socialist union, royal concert, continental command, neutral confederation, and a reviewed mythic compact. Each route receives its own representative institution before converging on common defence, withdrawal and crisis law, a post-colonial treaty with Africa, and final ratification. The mythic compact remains locked until `africa_europe_high_chaos_package_reviewed` confirms its separate source and sensitivity review.

## Asia implementation

Centers of Asia uses four founding regional institutions and five mutually exclusive settlements: plural federation, revolutionary union, imperial congress, anti-colonial common front, and a reviewed celestial covenant. Each route has its own congress before converging on food, river, and monsoon management, rail and maritime corridors, common defence, autonomy and withdrawal law, an Indian Ocean partnership with Africa, and final ratification. The celestial covenant remains locked until `africa_asia_high_chaos_package_reviewed` confirms its separate source and sensitivity review.

## Asset contracts

The accepted matrix entries are registered in `interface/012_africa_world_order.gfx`. No generic texture redirection is used.

- Scramble news: `GFX_news_event_012_africa_scramble_response` at `gfx/event_pictures/012_africa/news_event_012_africa_scramble_response.dds`
- Continental war news: `GFX_news_event_012_africa_continental_war` at `gfx/event_pictures/012_africa/news_event_012_africa_continental_war.dds`
- Middle East focus icons: `gfx/interface/goals/012_africa/world_order/goal_012_middle_east_<focus_slug>.dds`
- Package ideas: `gfx/interface/ideas/012_africa/world_order/idea_012_<continent>_<identity>.dds`
- Route flags: the seven `continent_package_*` identity packages in `docs/specs/012_africa_specs/matrices/012_africa_asset_animation_matrix.csv`
- Scramble super-event: `GFX_super_event_012_africa_scramble_response`
- Continental-wars super-event: `GFX_super_event_012_africa_continental_wars`
- Terminal World package: `GFX_012_the_world_<asset>` plus its separate researched final image and audio record

The registered news, focus, idea, and flag binaries are still asset work until their source files, processed files, final DDS files, provenance, manifest rows, and review artifacts exist. Missing binaries remain blockers rather than being replaced by fallback art.

## Cleanup

Scramble phase flags and intervention-war flags are cleared at settlement or defeat. Sponsorship missions remove their target from the bounded sponsorship array on fulfilment or default. Continental-war target flags are cleared when war launches or resolves. The final World effect closes incompatible world-order and Scramble flags only after its complete presentation readiness gate passes.

## Future implementation work

- Finish and audit the Europe, Asia, North America, South America, and Oceania focus trees and their political, military, AI, decision, identity, and asset packages.
- Add route-specific post-settlement decisions and breakup rules for every two-continent union.
- Bind all 64 Event 12 AI profiles to the Scramble and world-order action choices.
- Complete the accepted news, focus, idea, flag, super-event, animation, and audio assets with no substitutions.
- Research and approve the high-chaos continent routes before enabling their review flags.
- Research and wire the four super-event roles only after final text, images, licensed music, slots, and unique audio IDs are complete.
