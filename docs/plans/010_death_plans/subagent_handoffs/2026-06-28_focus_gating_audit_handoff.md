# Event 010 Death Focus Gating Audit Handoff

## Scope

Audited `common/national_focus/010_death_focus_tree.txt` against the current Event 010 Death gating request after the parent rework.

## Files Changed

- `common/national_focus/010_death_focus_tree.txt`

## Changed Focus IDs

- `death_first_ghost_muster`
- `death_public_death_focus`

## Behavior Before

- `death_first_ghost_muster` could be taken before `death_evolution_weak_ghost_hosts_recorded`, which let the player or AI spend the focus before the 600-tier weak host stage could produce a meaningful host reward.
- `death_public_death_focus` required `death_island_pattern`, `death_mainland_smell`, and `death_first_ghost_muster` as AND prerequisites. This tied the post-reveal focus to the Shroud terminal and the 600-tier ghost branch even though the scripted reveal is driven by the Mainland Hunger mainland path.

## Behavior After

- `death_first_ghost_muster` requires `death_evolution_weak_ghost_hosts_recorded`, so it is a real 600-tier weak host focus unlock.
- `death_public_death_focus` now requires only `death_mainland_smell` plus `death_publicly_revealed`, so the Mainland Hunger mainland path can reach the public focus without waiting for the Shroud terminal or 600-tier ghosts.

## Localisation And Icons

- No localisation keys changed.
- No icon IDs changed.

## Validation

- Checked focus IDs against `localisation/english/010_death_l_english.yml`. No individual focus name keys were missing.
- Checked focus description keys against `localisation/english/010_death_l_english.yml`. No individual focus description keys were missing.
- Checked focus icon IDs against `interface/010_death.gfx`. No regular or shine sprite definitions were missing.
- Checked duplicate focus icon references in `010_death_focus_tree.txt`. No duplicates were found.
- Re-read the relevant reveal and host gates in `010_death_triggers.txt` and `010_death_effects.txt` to confirm `death_can_push_mainland_reveal`, `death_publicly_revealed`, `death_evolution_weak_ghost_hosts_recorded`, `death_evolution_hollow_ghost_hosts_recorded`, and `death_can_start_world_end` still line up with the focus gates.

## Remaining Risks

- The tree still relies on local `ai_will_do` weights rather than a strict AI strategy plan. The gates now prevent the main invalid route ordering found in this audit, but AI ordering remains weight driven.
- No broader route redesign was attempted.
