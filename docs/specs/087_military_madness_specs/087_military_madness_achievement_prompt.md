# Military Madness Achievement Implementation

Implement the three Military Madness achievements defined in `docs/specs/087_military_madness_specs/087_military_madness_spec_part_6_assets_and_achievements.md`.

Read the entire Part 6, the core and lifecycle parts, the acceptance scenarios, `AGENTS.md`, the events, event-assets, and subagents skills, and the current achievement registry and integrity helpers. The objectives below are a task map. The full specification remains authoritative for frozen actors, provenance, interruptions, and deadlines.

## Registry and identifiers

Use only `common/achievements/chaos_redux_achievements.txt`. Preserve its existing `unique_id = chaos_redux_achievements`. Group these entries in the Event 087 section.

Proposed IDs:

`087_military_madness_minor_major_offensive`

`087_military_madness_core_recovery`

`087_military_madness_hold_after_expiry`

Confirm there are no conflicting registrations before using them. Final player-facing titles and descriptions are written during this task, following the localisation directions. Do not expose working objective labels, debugging fields, or this prompt in player text.

## Objective A1

At a natural package's opening, the recipient is independent, is not a major, and is already at war with a qualifying major that owns and controls its recorded capital state.

Within that same 365-day package, the recipient directly seizes the frozen capital state through hostilities, directly holds it for 30 consecutive days, and the frozen enemy capitulates. Complete all conditions before the original deadline.

An ally's seizure alone does not qualify. Capital relocation, later major status, newer packages, peaceful gifts, and changing target identity do not shorten or renew the objective.

## Objective A2

At a natural package's opening, the recipient is already at war, has at least 50% surrender progress, and has at least five owned core states under enemy control.

Freeze its complete set of owned core states. It must directly recover all those states and hold the complete frozen set for 30 consecutive days before that package expires.

Cession, release, de-coring, or changing borders cannot shrink the frozen requirement. Recheck hostile recovery provenance for originally occupied states. Reset the hold on loss, without extending the package.

## Objective A3

Bind to a continuous natural active period starting when a package arrives with no earlier package active and ending when the last overlapping package expires. The country must already be at war when that period begins.

During that period, directly seize at least five opening enemy-owned states not initially under direct control, with at least 50 combined victory points frozen from the opening. Diplomatic transfers do not count.

At the final expiry, freeze the complete qualifying gain set still directly controlled. It must meet both thresholds. Hold all of it for 90 days while continuously at war and without another Military Madness package.

A new package interrupts this unassisted hold and is still granted normally. Do not let the player refuse or remove a reward for the achievement. Settings or debug actions used to manipulate the attempt invalidate it under the shared integrity rules.

## Tracking and proof

Use actual supported country, war, control-change, capitulation, expiry, and identity hooks. Verify their exact context from installed documentation and current source. Do not invent a contributor field that claims exclusive battle credit.

Use sparse active-attempt records with frozen targets and deadlines. Do not add a daily worldwide state-and-war sweep. Delivery and achievement observations must be idempotent and survive save/load without replaying rewards.

Country lifecycle, tag reuse, civil-war copying, forced events, console intervention, settings changes, and AI-to-player switching need the specified integrity treatment. Keep common integrity logic with its existing owner.

Do not reward mere receipt, duplicates, a rare random combination, or reaching Evolution III.

## Art and text

Route the three original transparent subjects and exact three-state processing to `chaosx_icon_artist` through the separate asset prompt. Keep all nine achievement DDS files directly under `gfx/achievements/`, matching exact IDs and suffixes.

Write direct, precise titles, descriptions, progress tooltips, and blocked reasons. Distinguish direct control from allied control, a frozen objective set from current ownership, and one package deadline from the entire active period.

Use the localisation auditor for key coverage, dynamic units, clarity, and rendered fit. Any relevant weighted surface requires the read-only probability auditor. Do not create probability assertions for deterministic predicates.

## Handoff

Return the exact registry entries, tracking and cleanup owners, final localisation keys, icon lookup paths, source and MCP evidence, applicable acceptance-case results, remaining unsupported hooks, and live-validation limits.

The parent owns final integration. The user performs live-game validation. Do not claim the achievements are complete merely because the registry entries and icon filenames exist.
