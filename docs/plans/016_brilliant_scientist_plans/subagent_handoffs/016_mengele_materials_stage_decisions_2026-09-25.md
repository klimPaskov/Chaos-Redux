# Event 016 Mengele Materials stage decision handoff

Disposition: implemented as a bounded source tranche after parent reconciliation; AI probability and native decision acceptance remain unresolved.

## Accepted scope and source ownership

The user-authorized Event 016 portfolio closure plan and final completion contract require four ordered Materials stages in both DLC states, with the native `sp_brilliant_scientist_advanced_materials` Prototype authoritative under Götterdämmerung and one paid fallback Prototype without it.
Theory, Deployment, and Weaponization already existed in `common/decisions/016_mengele_conventional_stage_decisions.txt`, with gates in `common/scripted_triggers/016_mengele_conventional_stage_decision_triggers.txt` and text in `localisation/english/016_mengele_conventional_stage_decisions_l_english.yml`.
The worker's initial four-row draft duplicated these three IDs and their trigger/localisation keys, which the independent completion audit caught before integration.
The parent retained only the missing no-DLC Prototype in `common/decisions/016_mengele_materials_stage_decisions.txt`, `common/scripted_triggers/016_mengele_materials_stage_decision_triggers.txt`, and `localisation/english/016_mengele_materials_stage_l_english.yml`; each Materials decision ID and private gate now has one definition.

## Prototype transaction

The Prototype decision uses private family ID 3 and aligned receipt index 2, the shared fallback quote, an existing Advanced Materials Prototype icon, a native two-civilian-factory reservation, and a 240-day timer.
It consumes 68 Political Power, 200 Support Equipment, and 200 Fuel through `brilliant_scientist_mengele_begin_project_stage`, not a Kruger board effect.
Its exact family/stage cancel and removal callbacks call the private cancel/finish effects; the no-DLC Prototype finish records the authorized private Prototype flag and modifier, while the existing Deployment decision later grants the conventional package.
The existing Götterdämmerung native project remains the Prototype path and retains its own clock and payment.
The new Prototype AI uses the existing Kruger fallback base `ai_high`, wartime preferred factor, and a provider-specific low-factory-margin cautious factor.

The existing three paid stage wrappers retain their more detailed technology, military-factory, and strategic-resource requirements; the duplicate draft's simpler conditions were discarded.
The full four-stage lifecycle is documented in `docs/events/016_brilliant_scientist/systems/mengele_materials_stages.md`.

## Review and limits

The worker consulted the eleven required offline wiki core pages, relevant Decision and Idea Modding sections, installed vanilla docs, the Event 016 source contract, and the decisions, events, and subagents skills.
The parent confirmed one definition each for the four decision IDs and no duplicate Materials-specific trigger or localisation key, the Prototype icon and DDS, family index, callback selectors, price/duration constants, and localisation BOM.
No HOI4 process was launched.
The mandatory probability baseline/comparison, native factory reservation and callback order, same-family timer restart, current decision-list presentation, and live Materials consumer remain acceptance work.
