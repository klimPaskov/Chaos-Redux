# Event 005 Soviet Collapse Mission Audit

Audit date: 2026-05-20

## Mission Catalogue

The active Soviet crisis board contains 118 manually activated missions. The full 118-row mission table is maintained in `docs/events/005_soviet_union_collapse_mission_audit.md` with the serious-audit columns for owner, category, region, target surface, duration, success condition, failure condition, effects, and duplicate check.

Verifier evidence:

- `mission_wiring_counts`: 118 mission blocks, 118 activation refs, and 118 terminal cleanup removals.
- `mission_objective_shape`: every mission is a non-selectable, good, timed objective with `days_mission_timeout`, `custom_trigger_tooltip`, a named requirement tooltip, a hidden scripted trigger, a completion effect, and a timeout effect; no success and failure bodies are identical.
- `mission_localisation_surface`: every mission has title, description, requirement tooltip, success tooltip, and failure tooltip localisation; requirement text contains no placeholder wording, unnamed state sets, or unknown targets.
- `mission_audit_table_surface`: the full mission audit table has the required serious-audit columns and one row per active Soviet crisis mission.
- `terminal_mission_cleanup`: the terminal cleanup pass removes all 118 active mission IDs.

## Family Coverage

| Category | Mission count |
| --- | ---: |
| Authority | 9 |
| Cleanup | 7 |
| Command | 21 |
| Depot | 10 |
| Foreign | 22 |
| League | 8 |
| Legal | 3 |
| Old Movement | 17 |
| Rail | 11 |
| Settlement | 10 |

## Clarity Requirements

Mission localisation uses named mission requirement keys such as `<mission_id>_req_tt`, with actual scripted triggers hidden behind `custom_trigger_tooltip`/`hidden_trigger`. Division-state missions name concrete state groups in localisation, for example:

- Moscow, Arkhangelsk, Leningrad, and Pskov for the Northern Signal Offices.
- Moscow and Arkhangelsk for the Capital Ministry Belt.
- Moscow, Smolensk, and Minsk for the Western Courier Belt.
- Moscow, Smolensk, Minsk, Baku, Tashkent, and Sverdlovsk for radio/admin hub missions.
- Moscow, Smolensk, Minsk, and Azerbaijan for loyal military districts.
- Smolensk, Minsk, Baku, Tashkent, Novosibirsk, Omsk, Chelyabinsk, Ashkhabad, Alma-Ata, Sverdlovsk, and Stalinabad for depot hub missions.
- Kyiv, Minsk, Alma-Ata, Vilnius, Riga, Tallinn, Tbilisi, Yerevan, Baku, Chisinau, Tashkent, Bishkek, Dushanbe, and Ashgabat for active or recovered breakaway-capital missions.
- Kyiv, Minsk, Tashkent, and Sverdlovsk for west/south League route-splitting.
- Kyiv, Minsk, Baku, Tashkent, and Sverdlovsk for League defensive calendar disruption.
- Ukrainian-Belarusian, Baltic, Caucasus, and southern disputes for League border-dispute missions.
- Žemaitija, Vidzeme, and Pärnu for Baltic legal counterclaim offices.
- Civilian Factory of Russia, Military Factory of Russia, and the Volga-Ural industrial/depot belt for factory-state containment.
- Moscow plus recovered Kyiv, Minsk, Alma-Ata, Vilnius, Riga, Tallinn, Tbilisi, Yerevan, Baku, Chisinau, Tashkent, Bishkek, Dushanbe, and Ashgabat for restored-budget and school reopening missions.
- Moscow treaty offices, district war rooms, barracks, recognition corridors, and the Moscow Crisis Desk for late settlement and cleanup missions.
- Overall Union Crisis Threat, Moscow Authority, Republic Confidence, Depot Vulnerability, and Foreign Penetration for final crisis-desk cleanup.

The audit rejects generic state placeholders as proof of completion unless a named region or state list is present in the mission tooltip.

## Duplicate Cleanup Result

Passive stockpile, stability-only, war-support-only, manpower-only, and generic waiting missions are absent from the active mission surface after recursive scripted-trigger expansion. Stockpiles and meters can still appear as costs, scaling values, or supporting conditions, but no mission completes from those alone.

## Non-Python Verification Commands

```text
rg -n "required[ ]states|border[ ]states|dynamic[ ]number|dynamic[ ]set|dynamic[ ]threshold|relevant[ ]border[ ]posts|equivalent[ ]Pacific[ ]port|distant[ ]military[ ]and[ ]rail[ ]districts|storehouse[ ]and[ ]rail[ ]states|one[ ]or[ ]more[ ]depot[ ]states|that[ ]region|vulnerable[ ]depots|secure[ ]Soviet-controlled[ ]hubs|recovered[ ]depots|Belarusian[ ]rail[ ]hubs|a[ ]depot[ ]that[ ]the[ ]League[ ]publicly[ ]promised|ammunition[ ]depots[ ]controlled|hold[ ]the[ ]capital[ ]area|disputed[ ]regions|loyal[ ]party[ ]offices[ ]in[ ]the[ ]region|core[ ]rail[ ]lines|wavering[ ]republics|selected[ ]republic[ ]capital|disputed[ ]state|regional[ ]clusters|one[ ]League[ ]member|key[ ]hub|controlled[ ]states|normal[ ]state[ ]labor[ ]law|restored[ ]region|remaining[ ]republics[ ]or[ ]regions|local[ ]support[ ]and[ ]legislative[ ]credibility|normal[ ]state[ ]structures|final[ ]cleanup[ ]conditions" localisation/english/005_soviet_collapse_l_english.yml docs/events/005_soviet_union_collapse_mission_audit.md | rg "soviet_collapse_soviet_mission_|docs/events/005_soviet_union_collapse_mission_audit.md"
rg -n '<''=|>''=' localisation/english/005_soviet_collapse_l_english.yml docs/events/005_soviet_union_collapse_mission_audit.md docs/events/005_soviet_collapse_mission_audit.md
xxd -p -l 3 localisation/english/005_soviet_collapse_l_english.yml
```

Expected result: the text searches return no vague mission-objective matches or unsupported operators, and the encoding check returns `efbbbf`.
