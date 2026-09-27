# Richard Kuhn availability correction

**Disposition: implemented.** The user-approved calibration of all 67 CBRN scientists authorizes source-supported individual availability corrections. This correction changes only `GER_richard_kuhn` recruitment timing and retains the character in the 67-person roster.

## Source and decision

The [ETH-Bibliothek profile of Richard Kuhn](https://library.ethz.ch/sammlungen-und-archive/kurzportraets/richard-kuhn-1900-1967.html) says that after the war began he sought protective agents against chemical warfare. Its 1940 wording is: “Ab 1940 erforschte er im Auftrag der Wehrmacht umgekehrt Hemmstoffe von Vitaminen hinsichtlich ihrer Brauchbarkeit als Chemiewaffen.” From late 1942, he also pursued poison-gas research, first seeking protection against nerve agents before developing soman.

The earliest source-explicit year for Kuhn's Wehrmacht study of chemical-weapon use is 1940. The same profile says he sought protective agents after the war began, but it gives no month for that work. Under the approved 1940-or-later scientist-access boundary, 1 January 1940 is the year-level floor. This does not assert that protection-related competence began only then. His prewar chemistry and 1938 Chemistry Nobel remain represented by the approved CW skill 4 and `scientist_trait_genius`. His approved portrait is unchanged.

Scientific competence and offensive authorization remain separate. Recruitment only makes the existing scientist character available. The independent CBRN use-policy decisions and triggers continue to govern authorization; this correction does not grant policy, an advisor card, doctrine, or an offensive action.

## Implementation and source cases

The static `recruit_character = GER_richard_kuhn` entry was removed from `history/general/chaosx_startup_character_recruitment.txt`. The existing `chaosx_startup_recruit_dated_ger_cbrn_characters` helper in `common/scripted_effects/chaosx_startup_history_effects.txt` now recruits him when `date > 1939.12.31` and `NOT = { has_character = GER_richard_kuhn }`.

The helper is called during startup through `common/on_actions/chaosx_on_actions.txt` and from the bounded `on_daily_GER` callback in `common/on_actions/cbrn_historical_startup_on_actions.txt`. The character is absent at the 1 January 1936 start and the installed 1939 bookmark, 14 August 1939, because both dates fail the gate. At a 1 January 1940 start the startup helper satisfies the gate. A continuing earlier campaign becomes eligible on the first Germany callback whose current date is 1 January 1940 or later. `has_character` prevents repeat recruitment.

This changes one entry from static to dated recruitment. The 67-person roster count, Kuhn's identity, skill, trait, and portrait remain unchanged. The prior distribution of 39 direct and 28 dated recruitments becomes 38 direct and 29 dated recruitments.

## Engine-reference evidence

The offline wiki's `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md:91-126`, revision `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a`, describes `on_daily_TAG` as a daily action for the specified country that only runs while that country exists. Its `on_startup` entry says it runs on the first day of a new game after country selection. The offline wiki's `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:445-469`, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64f4c0c0ce06`, defines `date` as a comparison against the current date and requires `>` or `<`.

The installed `documentation/effects_documentation.md:5696-5708`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, documents `recruit_character` as a country-scope effect. Installed `documentation/triggers_documentation.md:2490-2498` and `:3410-3421`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, document the current-date `date` trigger and country-scoped `has_character` guard. Installed vanilla `common/on_actions/00_on_actions.txt:5762-5772` contains a Germany-specific daily callback precedent, and `common/bookmarks/blitzkrieg.txt:5` sets the 1939 bookmark to `1939.8.14.12`. No dedicated installed on-actions manual appeared in the documentation search. The exposed `hoi4.source_lookup` route returned zero definitions and references for `recruit_character` at revision `5d23ea5c64a751980e6516ea67e756a98f72ba156398839244a06d7a55db9162`, so the installed effect documentation, vanilla source, and existing Chaos Redux dated-recruitment helper were read directly.

The [Nobel Prize facts page](https://www.nobelprize.org/prizes/chemistry/1938/kuhn/facts/) records Kuhn's 1938 Chemistry Nobel for work on carotenoids and vitamins. This supports his broad chemistry expertise; retaining `scientist_trait_genius` remains the accepted gameplay mapping rather than a literal archival trait.

## Validation limits

The 1936, 1939, and 1940 results above were checked from the date gate and startup/daily call paths. No live HOI4 session was launched. The source evidence does not establish engine execution timing or appointment at an exact day. No CBRN policy, character skill, trait, portrait, or gameplay authorization behavior was changed.
