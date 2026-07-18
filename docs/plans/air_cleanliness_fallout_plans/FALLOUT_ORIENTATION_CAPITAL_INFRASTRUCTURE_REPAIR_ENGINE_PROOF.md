# Fallout Orientation Capital Infrastructure Repair Engine Proof

Date: 2026-07-18

Status: exact one-damaged-level repair remains blocked

## Required result

The accepted capital-condition contract requires a successful civic-core branch to repair exactly one damaged infrastructure level in the authenticated assigned capital. This is operational repair. It must not create a permanent level, raise the state's infrastructure cap, erase more than one damaged level, or silently succeed when no damaged level exists.

## Authoritative engine surfaces

The offline Building Modding reference and the installed official documentation expose these relevant surfaces:

- `damaged_building_level@infrastructure` reads damaged infrastructure levels in state scope.
- `non_damaged_building_level@infrastructure` reads operational infrastructure levels in state scope.
- `damage_building` adds building damage. Its optional `repair_speed_modifier` changes later repair speed until full repair. It does not repair damage.
- `remove_building` permanently removes total building levels.
- `add_building_construction` starts or instantly completes new building construction. The documentation does not state that it consumes existing damage.
- `set_building_level` sets the total building level. The documentation does not state that setting the current total repairs one damaged level or preserves the other damaged levels.

The official trigger documentation provides `non_damaged_building_level`, while `has_damaged_buildings` is country-scoped and does not identify an exact state, building type, or repaired amount.

## Precedent review

Vanilla uses `damage_building` for infrastructure damage and uses repair-speed modifiers to change ordinary engine repair. Vanilla also reads `damaged_building_level@infrastructure` in occupation logic. No reviewed vanilla event, effect, decision, or focus combines those reads with a documented exact one-level repair effect.

Kaiserreich and the other approved reference mods use new infrastructure construction, absolute level setters, or repair-speed modifiers. No reviewed precedent proves that any of those operations removes exactly one damaged infrastructure level while preserving total level and remaining damage.

## Rejected substitutes

The following routes are not accepted implementation:

- `add_building_construction` with `instant_build = yes`, because the documented effect creates construction and does not promise damage consumption
- `set_building_level` at the current total, because the documented effect does not promise one-level damage repair
- remove then rebuild, because removal is permanent and the engine does not document whether it removes damaged or operational capacity first
- a timed repair-speed modifier, because it cannot guarantee exactly one repaired level or an exact delivery time
- a variable-only receipt, because it would not change the engine building state

## Required proof before implementation

An authorized runtime pass must freeze total, damaged, and operational infrastructure for a controlled state, issue one candidate native mutation, then observe all three values after the mutation and after a save recovery boundary. Acceptance requires:

1. total infrastructure is unchanged
2. damaged infrastructure decreases by exactly one
3. operational infrastructure increases by exactly one
4. all other building families are unchanged
5. a second issue cannot occur from the same transaction
6. the result is identical for a human and AI country

Hearts of Iron IV was not run. The capital-condition repair branch therefore remains blocked. No gameplay helper, approval setter, receipt, or fallback repair was added.
