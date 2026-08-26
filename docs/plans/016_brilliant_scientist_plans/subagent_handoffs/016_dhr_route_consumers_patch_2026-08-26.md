# Event 016 D'Rhondan route-consumer patch

Date: 2026-08-26

## Scope

The parent implementation repaired the five focus-owned support markers that
the current acceptance audit identified as set-only. The patch keeps each
marker attached to the route promise that created it instead of adding a
duplicate decision or a generic spirit.

## Changes

- Added stable focus triggers for standardized components, the laboratory
  route, perfected predictive warfare, the reassembled orbital office, and
  access-map exchange.
- The landing decision AI now values standardized components and the orbital
  office when choosing paid alien landings.
- Reclamation requires perfected predictive warfare and advertises that
  requirement in its availability tooltip.
- Disconnected-enclave supply support requires the completed laboratory route
  and advertises that requirement in its availability tooltip.
- Covenant compact offers require the completed access-map exchange route.
- Shuttle-dock salvage is available only when a controlled coastal state has a
  free dockyard slot, preventing a landlocked DHR from silently setting a
  completion marker without the promised facility.
- Added the two route-requirement localisation keys used by the decision
  tooltips and centralized the two landing-AI factors in the shared constants.

## Files

- `common/scripted_triggers/016_dhrondan_focus_triggers.txt`
- `common/scripted_triggers/016_dhrondan_country_triggers.txt`
- `common/script_constants/016_alien_infantry_api_constants.txt`
- `common/decisions/016_alien_infantry_landing_decisions.txt`
- `common/decisions/016_dhrondan_country_decisions.txt`
- `common/national_focus/016_dhrondan_focus_tree.txt`
- `localisation/english/016_dhrondan_country_l_english.yml`

## Validation and remaining risk

The source checks confirm all five markers now have downstream consumers and
the focus remains in the existing orbital lane. Fresh focus/decision MCP
inspection was unavailable during the current transport window; previously
successful DHR focus evidence remains the structural baseline. Live game
acceptance is still owned by the user.
