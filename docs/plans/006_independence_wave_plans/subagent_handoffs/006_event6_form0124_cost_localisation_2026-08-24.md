# Event 006 FORM-01/02/04 combined cost localisation handoff

Date: 2026-08-24

The shared `independence_wave_form0124_administrative_diplomatic_cost` family in `localisation/english/006_independence_wave_form01_02_04_l_english.yml` now uses the compact icon-first presentation used by the other Event 006 decision surfaces.

The displayed bundle matches the source decision contract in `common/decisions/006_independence_wave_form01_02_04_decisions.txt`: standard Command Power and manpower, a convoy-or-train transport alternative, and the one civilian-factory project reservation.

The available text is the compact base key, the tooltip aliases that base key, and the blocked variant prefixes the same four groups with `Unavailable:` and red formatting.

No gameplay triggers, effects, constants, decision identifiers, or payment semantics changed.

Focused evidence:

- `independence_wave_form01_rotate_congress_session` gates on both `can_pay_independence_wave_administration_standard_cost` and `can_pay_independence_wave_diplomatic_standard_cost`, pays both standard effects, and reserves the light factory commitment.
- The shared constants resolve to 20 Command Power, 5,000 manpower, 10 convoys or 10 trains, and 1 civilian factory for this family.
- The localisation file retains UTF-8 BOM, has no NUL bytes, and the targeted family has no padded literal cost prose.

This is source/static evidence only and does not claim live tooltip observation or in-game execution.
