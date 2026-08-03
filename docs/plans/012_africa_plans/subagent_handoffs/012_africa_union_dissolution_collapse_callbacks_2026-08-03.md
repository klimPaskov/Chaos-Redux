# Event 012 W4 dissolution and collapse callbacks

Date: 2026-08-03

Owner: Main Event 012 implementation agent

Status: Implemented source tranche; live-save acceptance remains open.

## Scope

This tranche closes two existing W4 callback gaps without adding a country tag, cosmetic carrier, model, or new persistent store.

## Dissolution callback

`africa_world_union_protocol_dissolve_by_treaty` already wrote `africa_world_dissolution_recorded` and `africa_world_union_protocol_dissolved` for both sovereign actors, but no caller opened the corresponding record events.

`events/012_africa_world_package_union_war.txt` now uses the canonical `africa_world_dissolution_recorded` receipt for event `.713`.

The treaty effect opens events `.713` and `.717` for both actors before pair cleanup, so the consented dissolution is visible to each government while the existing historical flags remain queryable.

## Collapsed-war callback

The pairwise `on_actions` peace hook previously cleaned a continental-war pair when neither actor had a settlement receipt, leaving the documented `collapsed` status and event `.733` unreachable.

The no-settlement branch now records `africa_world_war_protocol.status.collapsed` on both actors, sets `africa_world_continental_war_protocol_collapsed` on the registered attacker, opens event `.733`, and then runs the existing protocol cleanup.

The branch deliberately does not manufacture a sovereign, submission, constituent-release, breakup, or terminal-resolution receipt; a failed settlement remains distinct from an accepted disposition.

## Validation evidence

- Repository census shows the `.713` reader matches the existing dissolution writer and no protocol-prefixed dissolution receipt remains as an orphaned reader.
- The `.733` event now has a source writer and callback in the no-settlement peace branch.
- The collapse branch uses the existing `africa_world_war_protocol.status.collapsed` constant and existing cleanup helper.
- Edited Clausewitz blocks were checked for balanced braces and quoted event IDs.
- No live Hearts of Iron IV launch or save validation was performed.

## Remaining boundary

The broader event catalog still contains historical acknowledgement events whose callers are intentionally gated by later package and terminal proofs; this tranche does not promote those unrelated dormant surfaces.
