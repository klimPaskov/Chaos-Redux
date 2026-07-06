# Event 011 Implementation Handoff

This handoff converts the source spec into an implementation order. It does not edit gameplay files.

## Required First Step In Implementation

Before coding, reopen the required offline wiki pages and vanilla docs listed in `research/011_secret_alliance_source_review_manifest.md`. Keep the faction, decision, on-action, event-target, and script-constant references open while editing.

## Implementation Order

1. Replace the Event 011 unavailable placeholder with the real event name mapping.
2. Add script constants and MTTH entries for setup, membership, pressure, timing, costs, AI, and border wars.
3. Add scripted triggers for target, founder, recruit, member, selected target, reveal, border, and cleanup validity.
4. Add scripted effects for context initialization, founder selection, member refresh, recruitment, hidden pulses, sabotage, counter-decision unlock, reveal, faction creation, war join, and cleanup.
5. Add event file `events/011_secret_alliance.txt` with `chaosx.nr11.1`, hidden pulse events, evolution events, report events, decision result events, and reveal wrapper.
6. Add faction template and icon registration placeholder.
7. Add narrow on-action hook for `on_war_relation_added`.
8. Add decision category, decisions, missions, target selector, and AI equivalents.
9. Add ideas and timed modifiers only where they carry real state.
10. Add super-event wiring, research docs, image/audio handoff, and event log integration.
11. Add localisation in UTF-8 with BOM and scripted localisation for dynamic values.
12. Add Event Details, Event Logs, actor mapping, evolution details, and spreadsheet/catalog alignment.
13. Run decision, localisation, event completion, and asset wiring audits before completion claims.

## Technical Gates

Dynamic faction name:

- verify that the faction template name can resolve the target player's country name
- if not, stop and request design approval

War join:

- verify exact `on_war_relation_added` ROOT/FROM behavior in the current game version
- verify the correct vanilla pattern for joining all members to the same war against the player

Constants:

- use script constants by default
- if a field rejects constants or variable tokens, use a variable assignment, file-scoped constant, or documented meta-effect

Candidate selection:

- do not allow invalid substitute founders
- no factioned true members in first implementation unless associate-state support is added and approved

On-actions:

- no recurring daily, weekly, or monthly world iteration
- setup scans and event-owned delayed pulses are acceptable

## Documentation To Keep Aligned

When implementation begins, keep these surfaces aligned:

- source specs in `docs/specs/011_secret_alliance_specs/`
- working plans in `docs/plans/011_secret_alliance_plans/`
- gameplay docs under `docs/events/` if the repo pattern uses one
- event catalog spreadsheet
- asset manifests
- super-event research notes
- Event Logs and Event Details text

## Completion Blockers

Do not claim implementation complete if any of these are true:

- only the opening event exists
- hidden roster lacks cleanup
- evolutions are not wired
- decisions exist without AI, costs, or cleanup
- reveal does not form a faction and join valid members to war
- dynamic faction name is replaced with an unapproved static fallback
- super-event is missing or unwired
- assets are missing, unwired, or undocumented
- localisation or event details are missing
- broad world iteration was added without approval

