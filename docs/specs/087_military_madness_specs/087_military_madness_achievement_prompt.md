# Military Madness Achievement Implementation

Implement the three achievements defined in [Part 6](087_military_madness_spec_part_6_assets_and_achievements.md), which is the only copy of their objectives, frozen targets, interruptions and deadlines.
Read Parts 1, 4 and 6 and the acceptance cases U14–U20, then follow the repository rules and the `chaos-redux-events`, `chaos-redux-event-assets` and `chaos-redux-subagents` skills.

## Registry

- Use only `common/achievements/chaos_redux_achievements.txt` with its existing `unique_id = chaos_redux_achievements`, grouped in an Event 087 section.
- Proposed IDs: `087_military_madness_minor_major_offensive`, `087_military_madness_core_recovery`, `087_military_madness_hold_after_expiry`; confirm there is no collision first.
- Write final titles, descriptions, progress tooltips and blocked reasons that state the action, opening condition, deadline and control requirement, distinguishing direct from allied control, a frozen set from current ownership, and one package deadline from the whole active period.

## Tracking

- Use the installed game's war, control-change, capitulation and expiry hooks, verified against the documentation and current source; invent no exclusive battle-credit field.
- Keep sparse active-attempt records with frozen targets and deadlines; add no daily worldwide state or war scan.
- Delivery and observations are idempotent and survive save and load.
- Forced occurrences, console intervention, settings manipulation, invalid country lifetimes and AI-to-player switching cannot create progress, using the existing achievement integrity owner.
- Receiving a package, rare draws, duplicates or reaching Evolution III earn nothing.

## Art and review

Produce the three icon triplets through the [asset prompt](087_military_madness_asset_prompt.md); all nine DDS files sit directly in `gfx/achievements/`.
Use `chaosx_localisation_auditor` for the text.

## Handoff

Return the registry entries, tracking and cleanup owners, localisation keys, icon paths, acceptance-case results, unsupported hooks and remaining limits.
The parent owns final integration and the user performs live validation.
