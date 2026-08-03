# Event 015 Focus Tree Layout Fix

## Scope

This pass supersedes the earlier coordinate-only repair and records the final structural cleanup in `common/national_focus/015_utopia_manifesto_focus_tree.txt`.

The pass preserves route gates and rewards while moving complex convergence requirements into explicit `available` blocks with custom tooltips where a visible prerequisite line created an unavoidable crossing or through-node overlap.

## Layout changes

The opening fan-out was reordered so the capital-store, social-city, household-consent, common-table, guardianship, founding-crisis, and external-policy families occupy stable horizontal lanes before their internal branches expand.

The regional commonwealth sequence was aligned with its league and reserve-council predecessors.

The guardianship children `utopia_manifesto_penal_works` and `utopia_manifesto_natural_right_of_need` were placed beneath their actual parents instead of crossing the two parent lanes.

The final pass removes layout-only visible lines for the Capital Store, homes, stores, leased island, Ground Held in Trust, military capstone, proof, and post-formation integration where the source already exposes the same gate through a country flag or reusable formation trigger. The route-correction focus keeps a visible founding-crisis anchor while its `allow_branch` and `available` checks still wait for any of the five correction outcomes. The tooltips now state those gates directly.

## Validation evidence

The HOI4 focus inspector resolves 124 focuses and 126 visible prerequisite connectors.

The final measured layout is clean: 0 connector crossings, 0 connector-through-node intersections, 0 long connectors, 0 duplicate coordinates, and 0 same-row spacing violations. Bounds are x=-3..56 and y=0..16.

The MCP compact reflow was not used because it rejected the authored route graph; the final repair keeps all route gates in source-level `available` conditions and does not weaken gameplay eligibility.

No gameplay fallback was used. The only visual simplification is replacing redundant connector lines with explicit, localizable availability requirements. `a_mixed_commonwealth` remains gated by its route flag rather than a literal Admit prerequisite because the natural island correction resolves the crisis without completing that focus; `a_settled_interim_charter` is anchored to the founding crisis and retains the constitutional-resolution gate for all five correction routes.
