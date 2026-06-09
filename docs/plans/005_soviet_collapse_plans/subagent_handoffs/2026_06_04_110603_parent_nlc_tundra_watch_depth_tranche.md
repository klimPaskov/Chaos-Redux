# Parent Tranche Handoff: NLC Tundra Watch Depth

## Scope

Event005 Soviet Collapse focus-depth cleanup for the Northern Lights Commune only.

Flags and flag sprites were explicitly out of scope and were not touched.

## Files Changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Identifiers Changed

- Focus: `NLC_tundra_watch_posts`
- Decision: `nlc_consolidate_claim`
- Scripted effects:
  - `nlc_soviet_collapse_apply_tundra_watch_posts`
  - `nlc_soviet_collapse_apply_tundra_watch_consolidation`
  - `soviet_collapse_update_pra_authority_idea`
- Localisation:
  - `NLC_tundra_watch_posts_tt`
  - `nlc_tundra_watch_claim_bonus_tt`

## Before

`NLC_tundra_watch_posts` gave army XP, one land fort, and one radar station. It did not unlock or alter a decision, did not pressure the Soviet collapse system, and did not help the Northern Lights Commune become more aggressive at high chaos.

## After

`NLC_tundra_watch_posts` now:

- unlocks/surfaces `nlc_consolidate_claim`
- calls a named NLC-specific helper instead of listing flat reward clutter
- improves depot control, independence resilience, liaison reach, command power, XP, radar, forts, infrastructure, airbase coverage, and decryption against SOV
- pressures the Soviet crisis source values when the Soviet collapse system is active
- prepares high-chaos neighbor expansion behavior without adding national spirits

`nlc_consolidate_claim` now gains a one-time extra tundra-watch payoff after the focus is complete, adding recognition, resilience, radar coverage, and high-chaos expansion escalation.

The Pale Railway Authority authority-spirit updater now only clears and adds a railway authority spirit when the target tier changes. Repeated focus/helper refreshes no longer remove and re-add the same tier.

## Validation

- `git diff --check` passed on touched gameplay/localisation files.
- Brace balance passed on touched script files.
- No unsupported `<=` or `>=` operators found in touched files.
- Helper/key grep confirmed focus, decision, scripted-effect, and localisation wiring.
- The PRA authority helper was inspected after patching and now gates each `add_ideas` call behind `NOT = { has_idea = ... }`.
- `git status --short -- gfx/flags interface/flags` returned no scoped flag changes.

## Remaining Gaps

This is one bounded focus-depth tranche, not the full Soviet Collapse focus-tree rework. The active goal still needs broad audit follow-up across all Soviet Collapse trees, especially repeated idea rewards, Ukraine/Belarus layout, chaos-country power identity, release/evolution linkage, and expansion branch depth.
