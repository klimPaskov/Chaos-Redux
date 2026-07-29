# Event 015 Focus Tree Layout Fix

## Scope

This pass changes authored focus coordinates only in `common/national_focus/015_utopia_manifesto_focus_tree.txt`.

Focus identifiers, prerequisites, mutual exclusions, availability, bypasses, rewards, AI weights, icons, costs, and localisation references remain unchanged.

## Layout changes

The opening fan-out was reordered so the capital-store, social-city, household-consent, common-table, guardianship, founding-crisis, and external-policy families occupy stable horizontal lanes before their internal branches expand.

The regional commonwealth sequence was aligned with its league and reserve-council predecessors.

The guardianship children `utopia_manifesto_penal_works` and `utopia_manifesto_natural_right_of_need` were placed beneath their actual parents instead of crossing the two parent lanes.

## Validation evidence

The HOI4 focus inspector resolves 124 focuses and 174 prerequisite connectors, matching the pre-change tree.

The measured layout improved from 47 connector crossings, 20 connector-through-node intersections, and 20 long connectors to 35 crossings, 19 connector-through-node intersections, and 16 long connectors.

Same-row spacing remains valid with no duplicate authored coordinates.

A semantic comparison with all authored `x` and `y` lines removed matches the pre-change source exactly.

## Remaining layout constraints

The remaining warnings are concentrated in intentional multi-parent convergence structures, especially the interpretive congress and interim charter pair, the commune governance pair, the measurement governance pair, and the long optional formation-proof link from the social-city route.

Automatic compact reflow and several bounded manual alternatives were rejected because they increased crossings, long connectors, or connector-through-node intersections.

No gameplay simplification or fallback was used.
