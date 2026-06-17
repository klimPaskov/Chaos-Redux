# Event 012 Africa Is One Route-Gate Handoff

Date: 2026-06-17

## Scope

Corrected the ordinary `Africa Is One` capstone gate so normal political/integration routes can reach continental unification without first completing the high-chaos World Root path.

## Changed Files

- `common/national_focus/012_africa_focus.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_africa_is_one_gate_handoff.md`

## Behavior Before

- `AFR_africa_is_one` required `AFR_continent_sponsor_office`, `AFR_world_root_mandate`, and either `AFR_forest_parliament` or `AFR_archive_bestiary_clause`.
- Its `available` block also required `africa_world_root_mandate_open`, `africa_continent_sponsor_ready`, and `africa_minimum_high_chaos_packages_ready`.
- The sponsor readiness mission required World Root and minimum Bestiary packages, so ordinary federal, sovereign-seat, liberation, military, crown, and integration routes could not reach the focus-tree `Africa Is One` endpoint without high-chaos progression.

## Behavior After

- `AFR_africa_is_one` requires the normal continental route spine: integrated or autonomous regions, the Continental Register, regional-authority threshold, living-core threshold, and six-line dossier coverage.
- Continent Sponsor Office remains a near-post-unification office, but sponsor readiness now starts after `Africa Is One` rather than after World Root.
- Evolution IV recording was removed from ordinary `AFR_africa_is_one` and added to `AFR_world_root_mandate`, so baseline unification no longer logs the high-chaos/world-root evolution. The existing high-chaos package-threshold helper can still record Evolution IV if the Bestiary threshold is reached before the World Root focus, which remains a broader evolution-design follow-up rather than part of this capstone-gate fix.
- World Root, minimum Bestiary packages, Bestiary containment success, and Bestiary actions remain required by `can_africa_certify_continent_unifiers_for_world_is_one` and `can_africa_prepare_world_is_one_gate`, preserving the terminal World Is One gate.

## Validation Notes

- The offline national focus wiki confirms separate `prerequisite = { ... }` blocks are ANDed, and multiple `focus = ...` entries inside one prerequisite block are ORed.
- The patch therefore changes the capstone from mandatory high-chaos AND-gating to the intended integration/register path while leaving high-chaos as a later terminal route requirement.
- Static inspection confirms `AFR_africa_is_one` no longer contains `AFR_world_root_mandate`, `AFR_forest_parliament`, `AFR_archive_bestiary_clause`, `africa_world_root_mandate_open`, `africa_continent_sponsor_ready`, `africa_minimum_high_chaos_packages_ready`, `allow_branch`, or `africa_record_evolution_iv_if_needed`.

## Remaining Risks

- The Continent Sponsor Office focus can still be taken before `Africa Is One`, although the sponsor readiness mission now waits for `Africa Is One`. A fuller layout pass could move the focus below the capstone and redraw the post-unification branch.
- The Second Scramble remains represented through the existing Scramble decision/focus systems rather than a clean post-`Africa Is One` focus fork.
