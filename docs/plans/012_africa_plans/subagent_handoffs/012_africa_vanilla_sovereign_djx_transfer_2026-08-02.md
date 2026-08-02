# Event 012 vanilla sovereign reserved-carrier transfer handoff

Date: 2026-08-02

Status: bounded source repair complete. Live package registration and leader-surface validation remain open.

## Scope

The Event 012 vanilla-carrier handoff owns nine sovereign characters held by the existing Event 006 `DJX` reservation country.

The repair changes only the hidden `africa_priority_member.1240` ownership handoff. It does not add a country tag, a cosmetic tag, a state, a portrait, or a second character definition.

## Change

`events/012_africa_priority_member_events.txt` now transfers each reserved sovereign from `DJX` with the documented `set_nationality = { target_country = ROOT character = ... }` form.

The existing package, vanilla-carrier, country-flag, and per-character guards remain unchanged.

The completion branch still requires the matching character to be present before writing `africa_priority_member_vanilla_sovereign_recruitment_complete`.

The seven Event 006 niche shells remain on their own country-history ownership path and are not routed through this event.

## Evidence

`history/countries/DJX - Unresearched Reservation.txt` recruits the nine Event 012 vanilla sovereigns as roleless reserved characters.

Vanilla effects documentation defines the two-country `set_nationality` form used here.

`common/scripted_effects/016_brilliant_scientist_effects.txt` provides the repository precedent for transferring a reserved `DJX` character to the selected host.

## Validation

Static source review confirms all nine character IDs are defined and all nine are recruited by the reserved `DJX` history.

The hidden event retains one package guard, one carrier guard, one completion flag guard, and idempotent per-character checks.

The edited event has balanced Clausewitz braces and no whitespace errors.

No Hearts of Iron IV process or live save was launched.

## Remaining risk

Live package registration should confirm that each vanilla carrier receives exactly one sovereign, that the `DJX` roster is emptied for that character, and that repeated package recovery calls do not duplicate or orphan the leader.
