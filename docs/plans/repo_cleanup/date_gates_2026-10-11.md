# Calendar date gates audit, 2026-10-11

Rule from user brief 3.3: dates influence, gameplay conditions decide.
Total 145 checks. Scope: every `date >`, `date <` and `date =` check in Chaos Redux owned `common/` and `events/` script, plus the year and month readers.
Classes: (a) structural or technical, kept; (b) AI timing or weight, kept as influence only; (c) rigid gameplay gate, replaced by the gameplay condition it stood for; (v) byte-identical vanilla override, kept.
Line numbers are those of the file before this change.
Not counted: `global.date` timestamps stored in variables (elapsed-time bookkeeping), `global.year` readers, `is_historical_focus_on` (the game rule, not a date) and equipment or technology `year =` attributes.

Already handled before this pass: camps and genocide paths (1d123f711), Events 002, 003 and 016.

## Counts

| Class | Gates | Result |
| --- | --- | --- |
| (c) replaced | 48 | 4 systems edited (advisor cards, Showa Denko concern and MIO, PUSA decision, famine profiles) plus one easter egg trigger |
| (a) structural, kept | 68 | commented where the file lacked a comment |
| (b) AI timing, kept | 5 | camp AI entries only, none block a player |
| (v) vanilla override, kept | 24 | Iceland focus, radar project, electronic and mechanical engineering technologies |

## Replaced (class c)

| File:line | Old gate | New condition |
| --- | --- | --- |
| common/characters/cbrn_historical_specialists.txt:71 (Heatley) | `date > 1939.12.31` | removed; the Field Antibiotics project requirement already beside it decides |
| :131 (Bayne-Jones) | `date > 1941.12.31` | removed; the Mass Vaccine Production project requirement decides |
| :168 (Fildes), :453 (Olson), :486 (Baldwin), :357 (Witaszek) | `date > 1939.12.31`, `1942.12.31`, `1942.12.20`, `1940.06.30` | `cbrn_convention_has_biological_capability` (Pathogen Handling Protocols or a completed biological bomb project), tooltip `cbrn_advisor_biological_programme_required_tt` |
| :263 (Blome), :324 (Kitano) | `date > 1943.06.30`, `1942.01.01` | `bio_battlefield_country_has_any_agent_project` (a completed biological bomb project), tooltip `cbrn_advisor_biological_weaponization_required_tt` |
| :230 (Schrader), :390 (Mairanovsky) | `date > 1936.12.31`, `1937.12.31` | `cbrn_chaos_warfare_has_agent_technology` (a researched chemical agent), tooltip `cbrn_advisor_chemical_agent_required_tt` |
| common/ideas/cbrn_industrial_concerns.txt:60-61 | `date > 1939.5.31` on visible and available | `has_war = yes` (native tooltip) |
| common/military_industrial_organization/organizations/cbrn_national_organizations.txt:105-106 | `date > 1939.5.31` on visible and available | `has_war = yes` on the same country |
| common/scripted_triggers/006_independence_wave_signature_modules_triggers.txt:129 | `date > 1939.5.4` (PUSA decision) | `has_independence_wave_atj_signature_settlement_complete = yes`; the decision description names the settlement and school network instead of 5 May 1939 |
| common/scripted_effects/famine_core_effects.txt:275-343 and :1508-1587 (selector and resolver, seven profiles each) | `date > A date < B` windows for Henan 1942, Bengal 1943, Vietnam 1944, Java 1944, Greece 1941, Leningrad, Dutch Hunger Winter | new state trigger `famine_state_holders_at_war` (owner or controller at war); the existing owner, war-evidence or food-pressure proofs stay |
| famine_core_effects.txt:376-377 and :1620-1621 | Spain `date > 1939.01.01 date < 1943.01.01` | removed; the SPR owner and the existing war-evidence or food-pressure proof decide, since the Spanish famine followed autarky rather than a war on its soil |
| events/_chaosx_easter_eggs.txt:23 | `date > 1942.9.11` (Chamberlain) | removed; `war_length_with GER months > 36` and the strength, casualty and war-support conditions already stand for it |

## Kept structural (class a)

| File:line | Gate | Why it stays |
| --- | --- | --- |
| common/achievements/chaos_redux_achievements.txt:26, :1037, :1214 | `date > 1939.12.31`, `date < 1940.01.01`, `date > 1944.12.31` | the achievement is defined by the calendar ("before 1940", "survive to 1945"); the file carries another agent's uncommitted hunks and is untouched |
| common/scripted_effects/chaos_meter_effects.txt:4404, :4476 and chaosx_settings_effects.txt:3314, :3357 | `date < 1945.01.01`, `date < 1940.01.01` | the achievement flags that feed the entries above |
| common/scripted_effects/chaosx_startup_history_effects.txt (46 checks) | `date >` and `date <` at startup | one-time bookmark detection (1936 or 1939 start) and documented career dates of real scientists; header now says so |
| common/scripted_effects/camp_administration_effects.txt:524-534 | `date < "[YEAR].N.1"` | month number from the calendar, already commented |
| common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:445, :449 | `date < 1938.06.17` | which historical Sultan holds an office; no player action is gated and the existing comment states the reason |
| common/scripted_effects/famine_core_effects.txt:284, :1518 | `date > 1936.01.01` | not on the start day, a live food shock is needed; comment added |

## Kept AI timing (class b)

| File:line | Gate | Note |
| --- | --- | --- |
| common/decisions/camp_administration_civil_decisions.txt:31-33 | ENG, USA, RAJ `date >` inside an `ai_will_do` modifier | weight only |
| common/scripted_effects/camp_administration_country_effects.txt:43, :693 | `date >` as an alternative to a war with SOV, inside `is_ai = yes` | AI-only effect, the human path uses the decision |

## Kept vanilla overrides (class v)

| File | Gates |
| --- | --- |
| common/national_focus/iceland.txt:1536, :1540 | vanilla `ICE_american_protection` AI weight |
| common/special_projects/projects/radar_projects.txt:39 | vanilla radar project AI weight |
| common/technologies/electronic_mechanical_engineering.txt (21) | vanilla technology availability and AI hints |

## Follow-up candidates

The 29 dated scientist arrivals (`chaosx_startup_recruit_dated_*`) place real people by their documented careers.
They gate no player action, but a later pass could let a country at war or with the matching program receive its scientist earlier.
