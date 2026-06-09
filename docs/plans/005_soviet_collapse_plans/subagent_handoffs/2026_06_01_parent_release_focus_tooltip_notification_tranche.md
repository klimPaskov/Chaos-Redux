# Event005 Parent Tranche: Focus Tooltip, Opening Releases, and Minor Notifications

## Scope

This tranche addresses three current-state issues without touching flag sprite files:

- focus rewards still exposing low-level helper payloads as long reward spam
- opening-wave internal republic releases not being eligible during the first cascade
- Soviet Collapse report and mission events behaving like normal popups instead of minor notifications

## Changed files

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `events/005_soviet_collapse.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

## Gameplay changes

- Wrapped these low-level chaos/DSC focus helpers behind concise `custom_effect_tooltip` text and moved their payloads into hidden `_payload` helpers:
  - `soviet_collapse_spawn_custom_splinter_assault_columns`
  - `soviet_collapse_apply_custom_splinter_expansion_claims`
  - `soviet_collapse_dsc_claim_front_road_states`
  - `soviet_collapse_dsc_core_controlled_front_road_states`
  - `soviet_collapse_dsc_launch_dead_army_neighbor_wars`
- Added matching localisation tooltip keys so focuses show a readable summary instead of repeated equipment, claim, core, and war-plan lines.
- Allowed `soviet_collapse_opening_wave_active` to satisfy the internal/dynamic progressive release candidate gates. This lets niche internal republics enter the opening cascade instead of waiting for a later evolution flag.
- Added `major = no` to every Event005 `minor_flavor = yes` event that lacked it, so Soviet Collapse mission/report events use minor notification behavior consistently.

## Validation

- Brace balance was clean for:
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `common/scripted_triggers/005_soviet_collapse_triggers.txt`
  - `events/005_soviet_collapse.txt`
- `git diff --check` passed on touched files.
- Unsupported comparison-operator scan returned no matches on touched gameplay and localisation files.
- A focus reward scan found no duplicate direct idea rewards and no focus with eight or more helper calls.
- `minor_flavor = yes` scan found zero Event005 minor-flavor events missing `major = no`.
- No `gfx/flags` or `interface/flags` files were edited.

## Remaining work

- Full focus-tree route redesign is still incomplete. The remaining work is broad route content, not this tooltip tranche.
- Pathline cleanup still needs a dedicated rendered/layout pass.
- Scenario and terminal release behavior needs live verification after the broader release and chaos-successor work settles.
