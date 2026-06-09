# Event005 Parent Tranche - Release, Scenario, and Mission Notification Pass

## Scope

Parent-side patch while the focus-tree auditor remained active. This tranche avoided `gfx/flags` entirely and did not edit focus tree files to avoid overlapping the active focus audit.

## Changed Files

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `events/005_soviet_collapse.txt`

## Behavior Changes

- Opening-wave follow-on releases now use the Gathering Storm release table while `soviet_collapse_opening_wave_active` is set. This makes niche republic releases possible during the first release wave instead of waiting for the first-wave evolution flag to be recorded later.
- Terminal collapse now treats chaos tier 4 and 5 as forced high-chaos successor tiers, then runs a second forced high-chaos successor pass after ordinary/all-possible releases. This reduces cases where ordinary release ordering prevents special successors from appearing.
- Triggerable Soviet Collapse chaos scenarios now run a second forced high-chaos successor pass after ordinary/all-possible releases, followed by another all-possible and subject-freeing pass.
- Soviet mission outcome notices `chaosx.nr5.71` through `chaosx.nr5.94` are now `news_event` blocks with `major = no` and `minor_flavor = yes`.
- Active mission outcome calls for `chaosx.nr5.71` through `chaosx.nr5.74` now use `news_event` instead of `country_event`.
- `chaosx.nr5.95` was marked `major = no` as a minor Soviet crisis notice.

## Validation

- Brace balance:
  - `common/scripted_effects/005_soviet_collapse_effects.txt`: `balance=0 min=0`
  - `events/005_soviet_collapse.txt`: `balance=0 min=0`
  - `common/decisions/005_soviet_collapse_decisions.txt`: `balance=0 min=0`
- Unsupported comparison scan on touched files: no `<=` or `>=`.
- `git diff --check` on touched files: clean.
- `git diff --name-only -- gfx/flags`: no output.
- Targeted event scan confirmed `chaosx.nr5.71` through `chaosx.nr5.94` are `news_event` blocks with `major = no`.

## Remaining Risks

- Focus-tree depth, reward spam, and pathline cleanup remain with the active focus auditor and still need parent review.
- This pass strengthens release ordering but does not prove runtime map results; in-game validation is still required by the user.
- The terminal/all-possible helper is generic through `every_possible_country`; named niche tags are present in progressive release candidate tables, but country tag/core data should still be audited if a specific releasable remains absent in live testing.
