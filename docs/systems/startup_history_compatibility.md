# Startup History Compatibility Grants

Chaos Redux should avoid copying vanilla `history/` files when the goal is only to grant additive setup to existing countries or states. Copied vanilla country, state, and OOB files override other mods and can also freeze older vanilla data.

## Runtime flow

`common/on_actions/chaosx_on_actions.txt` calls `chaosx_apply_startup_history_grants` from `on_startup` through one existing-country scope. The effect keeps one global idempotence guard, dispatches all tag-specific facilities, starting technologies, stockpiles, projects, and other history grants by explicit country scope, then runs the per-country initialization helpers across existing countries. Mapped countries therefore do not depend on which country the engine selected as the startup caller.

The implementation lives in `common/scripted_effects/chaosx_startup_history_effects.txt`.

The tuning values live in `common/script_constants/startup_history_constants.txt`.

The master effect sets `chaosx_startup_history_grants_applied` so startup setup cannot apply twice.

The historical 1936 mask reconciliation runs after the common profile snapshot. It applies 75% active military issue to ENG, FRA, GER, SOV, and USA, 100% to ITA, 50% to JAP, and 25% to every other starting-mask profile tag, with a separate 25% replacement reserve and no fixed civilian issue. The 1939 British civilian receipt is separate: startup passes the sourced 40,000-crate target to the ENG-root `cbrn_protection.3` event, which debits real warehouse stock once. Core-owned Civil Defence visibility must consume the one-time historical receipt after that event so routine issue returns to threat-driven conditions.

## What belongs here

Use startup grants for additive existing-country setup:

- starting Chaos Redux technologies
- technology-linked tactic unlocks or startup sync effects required by those technologies
- starting equipment stockpiles
- starting chemical or biowarfare facilities
- static Chaos Redux scientists. The 67 approved historical identities are recruited by `history/general/chaosx_startup_character_recruitment.txt`; country grants only apply the persistent identity receipts and dated country setup.
- additive character traits
- startup-only variables and event targets
- delayed country events that previously lived in country history
- special-project or breakthrough progress setup

Do not use copied vanilla history files just to add one of these.

## What still belongs in history

History files remain valid for:

- custom Chaos Redux tags that need to exist before startup
- custom starting OOBs for custom countries
- `recruit_character` setup for custom tags or unavoidable history-only setup
- country setup that must happen before any startup effect can safely run
- unavoidable direct edits inside vanilla history definitions that cannot be recreated additively

Do not use `history/general` for country-specific Chaos Redux scientists. That folder is for generic character pools, not specific named characters assigned to specific countries.

Current intentional vanilla-history exceptions:

- `history/countries/GER - Germany.txt` remains because it changes vanilla equipment variant icon fields inside `create_equipment_variant` blocks.
- `history/units/CHL_1936.txt` remains because it guards a vanilla Chile OOB MIO assignment behind the required DLC check rather than granting Chaos Redux startup content.

## Script helper ownership

The complete startup API lives in `common/scripted_effects/chaosx_startup_history_effects.txt` rather than the cross-system dynamic-effect registry.

The dated CBRN personnel repair lives in `common/on_actions/cbrn_historical_startup_on_actions.txt` and uses only tag-specific daily callbacks. It does not add a world-wide periodic scan.

- `chaosx_apply_startup_history_grants` is the idempotent startup entry point and dispatches the country-specific additive grants.
- The historical scientist helper flags are no longer generated-character selectors; prewar identities retain their stable ids and portraits from history initialization, while dated wartime identities are recruited by `chaosx_startup_recruit_dated_*_cbrn_characters` and their bounded country callbacks.

The scientist helpers are internal to startup generation. Event chains should use their own event-owned character transactions instead of calling these helpers.

## Migrated startup surfaces

The startup effect currently replaces copied vanilla overrides for:

- existing-country Chaos Redux technology, stockpile, static scientist identity, trait, breakthrough, special-project, and delayed-event grants
- prepared-country starting chemistry/biology setup is preserved, while Britain's anthrax special project and British/US early biological breakthrough are deferred to later routes; Germany's `tabun` technology opens only after the late-1936 discovery and no startup tabun stockpile is granted
- chemical warfare facility placement in states 16, 59, 122, 158, 239, 361, and 530
- biowarfare facility placement in states 247, 282, 328, 338, 440, 609, 816, and 823, with the British 338 site gated after 31 December 1939 and the American 816 site gated after 1 January 1943
- the Australia citizen-army tuning variables
- the British Raj famine state pointer
- Liberia's vanilla support-equipment technology required by its startup AI production strategy

When adding a new startup grant, create or extend an individual `chaosx_startup_grant_<tag>` effect and call it from `chaosx_apply_startup_history_grants`.
