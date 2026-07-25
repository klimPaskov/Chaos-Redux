# B7 USA focus effect correction handoff

Date: 2026-07-26

## Scope

The B7 USA focus layer was checked with the offline focus inspector and the installed official effects documentation. The two military rewards used `add_army_experience`, which is not the documented effect key in this repository or the installed build.

## Changed files

- `common/national_focus/fallout_successor_b7_usa_focus.txt`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_SUCCESSOR_PLAYER_CONTINUATION_B7_PROOF.md`

The guard compact and continental radio rewards now use `army_experience` with their existing values of 10 and 5. No focus ids, prerequisites, costs, AI weights, or package gates changed.

## Validation

- Official `effects_documentation.md` lists `army_experience` and not `add_army_experience`.
- Repository-wide precedents use `army_experience` for this reward.
- The offline focus inspector parsed all seven B7 focuses and found no layout crossings, node intersections, or long connectors.
- The inspector still reports missing generic icon sprites because its source scan does not load the installed vanilla interface definitions. Dedicated B7 icon assets remain a separate blocker.

## Remaining risks

The USA package remains dormant. It still lacks final dedicated focus and idea DDS assets, GFX registration, runtime focus-tree loading proof, and the general successor materializer and player-continuation path.
