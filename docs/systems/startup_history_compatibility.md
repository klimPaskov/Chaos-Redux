# Startup History Compatibility Grants

Chaos Redux should avoid copying vanilla `history/` files when the goal is only to grant additive setup to existing countries or states. Copied vanilla country, state, and OOB files override other mods and can also freeze older vanilla data.

## Runtime flow

`common/on_actions/chaosx_on_actions.txt` calls `chaosx_apply_startup_history_grants` from `on_startup`.

The implementation lives in `common/scripted_effects/chaosx_startup_history_effects.txt`.

The tuning values live in `common/script_constants/startup_history_constants.txt`.

The master effect sets `chaosx_startup_history_grants_applied` so startup setup cannot apply twice.

## What belongs here

Use startup grants for additive existing-country setup:

- starting Chaos Redux technologies
- technology-linked tactic unlocks or startup sync effects required by those technologies
- starting equipment stockpiles
- starting chemical or biowarfare facilities
- generated Chaos Redux scientists, using `generate_character` or `generate_scientist_character`
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

Current intentional vanilla-history exceptions:

- `history/countries/GER - Germany.txt` remains because it changes vanilla equipment variant icon fields inside `create_equipment_variant` blocks.
- `history/units/CHL_1936.txt` remains because it guards a vanilla Chile OOB MIO assignment behind the required DLC check rather than granting Chaos Redux startup content.

## Migrated startup surfaces

The startup effect currently replaces copied vanilla overrides for:

- existing-country Chaos Redux technology, stockpile, generated scientist, trait, breakthrough, special-project, and delayed-event grants
- chemical warfare facility placement in states 16, 59, 122, 158, 239, 361, and 530
- biowarfare facility placement in states 247, 282, 328, 338, 440, 609, 816, and 823
- the Australia citizen-army tuning variables
- the British Raj famine state pointer

When adding a new startup grant, create or extend an individual `chaosx_startup_grant_<tag>` effect and call it from `chaosx_apply_startup_history_grants`.
