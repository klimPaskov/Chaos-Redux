# Event 015 Current Full Localisation Re-audit

Date: 2026-07-15
Auditor: `chaosx_localisation_auditor`
Scope: current Event 015 English localisation, all live player-facing references, shared event-log/catalog mappings, and source-fidelity checks
Mode: bounded localisation corrections plus this report; no gameplay, asset, workbook, or audio edit; no commit created

## Verdict

**PASS.** The frozen current Event 015 English localisation surface is complete at the static source level. No open P0-P2 localisation finding, missing key, duplicate Event 015 key, stale Event 15 identity, placeholder, fallback copy, or catalog mismatch remains.

The nine Event 015 English files contain **2,448 actual quoted definitions**. This count excludes each file's `l_english:` namespace header. All 2,448 keys are unique, and none has another exact definition anywhere else under `localisation/english`.

One bounded vocabulary defect was closed during this re-audit: four live strings still exposed the retired `Surplus` wording. The current values use `Commonwealth in Plenty`, `material-aid offer`, and `exportable stores`. The final visible-value scan has zero uses of the retired term.

This verdict is tied to the frozen current source hashes recorded below, including `events/015_utopia_manifesto.txt` at `a7d27155c463424f19fb1d661356a42ccb90cc4b29f8e42a03ea78ba86b9b164` and `common/decisions/015_utopia_manifesto_decisions.txt` at `5dcd41ef8669a4384fedb2efa9761e657fe8a5ff8ea686e45046005fd23d17fd`.

## Complete source-to-localisation inventory

| Surface | Current source inventory | Localisation result |
| --- | ---: | --- |
| Event definitions | 99 total: 96 country events and 3 news events | 507/507 direct popup references present |
| Event direct references | 91 titles, 90 direct descriptions, 2 conditional description texts, 288 option names, 36 effect tooltips | 507 unique keys; 0 missing; 0 duplicates |
| Decisions and missions | 121 decisions and 43 missions | 328/328 name/description keys present |
| Decision categories | 9 | 18/18 name/description keys present |
| Decision requirement/target wrappers | 125 unique keys: 124 `_requirements_tt` plus the case-target survival wrapper | 125/125 present |
| Decision and mission effect tooltips | 163 unique keys | 163/163 present |
| Custom costs | 92 live bases | 276/276 base, `_blocked`, and `_tooltip` keys present |
| Core event/decision union | 1,417 unique keys | 0 missing; 0 duplicate definitions |
| National focuses | 124 focus IDs | 248/248 name/description keys present |
| Focus availability/bypass wrappers | 94 availability and 5 bypass keys | 99/99 present |
| Focus tree label | tree name and description | 2/2 present |
| National ideas | 50 | 100/100 name/description keys present |
| Institutional characters and advisors | 24 | 48/48 name/description keys present |
| Advisor traits | 16 | 32/32 name/description keys present |
| Dynamic state modifiers | 19 | 38/38 name/description keys present |
| Opinion modifiers | 5 | 5/5 names present |
| Achievements | 14 | 42/42 `_NAME`, `_DESC`, and bespoke condition-tooltip keys present |
| Cosmetic identities | 5 tags | 75/75 base/DEF/ADJ plus four ideology-variant triplets present |
| Necessary Ground wargoal | type, description, and war-name format | 3/3 present |
| Event 015 scripted localisation | 34 `defined_text` functions; 235 output occurrences | 200/200 unique output keys present |
| Ledger GUI | 25 direct text/button/tooltip references | 25/25 present; no literal player prose embedded in the GUI file |
| Event name, Event Details, and evolution catalog | 20 shared parity keys | 20/20 present and referenced; 47 shared reference occurrences |
| Route super-events | slots 96-100, each with title, quote, response, and description | 20/20 present |
| Music display strings | six volume variants for audio ID 57 | 6/6 present and identical in title |

The 507 event count includes the three single-line news-event option names. An anchored line-only parser would report 504 and is therefore incomplete for the current file.

Eight hidden bridge/cleanup events intentionally have no popup text. Every non-hidden event has a complete title and description path; event `.45` uses its two conditional `text =` descriptions, and the three news-event option names are included in the count above.

## Raw-trigger and public-wrapper audit

All 99 focus condition blocks are wrapped:

- 94 `available` blocks expose one localised availability key each;
- 5 `bypass` blocks expose one localised bypass key each;
- no focus availability or bypass condition is shown as an unwrapped raw trigger.

The 34 paid-growth focuses—26 institutional and 8 military—retain their own localised availability wrappers. All 34 cancel if the live payment gate becomes invalid, and all 34 fail closed before applying downstream rewards if payment cannot be completed. The atomicity repair did not add or change a localisation key.

All 164 decision/mission entries have an `available` block:

- all 121 player-started decisions use a localised wrapper;
- 3 foreign-response missions use localised response wrappers;
- the remaining 40 mission gates are non-clickable mission sentinels contained entirely in `hidden_trigger` blocks;
- no player-started decision exposes raw internal flags, variables, or helper triggers.

The achievement conditions use bespoke `custom_override_tooltip` keys for all 14 Event 015 achievements. The visible condition copy describes player proofs rather than internal flag names.

## Dynamic text, integer formatting, costs, and consequences

The Event 015 files contain 113 variable-style localisation references:

- 108 numeric values, all explicitly formatted with `|0` or `|+=0` as appropriate;
- 5 state-name lookups through recorded state variables;
- 78 dynamic country-name occurrences, consisting only of `[FROM.GetName]` and `[FROM.GetNameDef]` in target-aware event or decision text.

No numeric reference is left with engine-default decimal formatting. Timers, dynamic military costs, dynamic institutional costs, Ledger totals, Ledger deltas, calling components, reserve values, case values, stewardship counts, and League counts all use integer display formats.

For all 92 custom-cost families:

- base and blocked strings normalize to the same icon/amount sequence after colour codes are removed;
- every number shown in a base cost also appears in its explanatory tooltip;
- all three required keys exist exactly once;
- fixed Political Power, equipment, manpower, stability, war-support, command-power, convoy, train, and reserve wording agrees with the current decision source;
- dynamic formation and institutional tooltips display the prepared live variables rather than a hardcoded substitute.

The final auxiliary-contract family was checked against the atomic combined-cost gate. Its requirement wrapper requires the full contract-and-formation stockpile; its cost triplet lists 50 Support Equipment, 50 Motorized Equipment, 20 Convoys, and the displayed 60 Political Power; its effect text separately discloses the live formation manpower, infantry equipment, support equipment, and army-experience cost. Both Support Equipment obligations are explicitly described as jointly affordable before signing.

Equality-sensitive district, repeal, and foundation wording remains aligned with the current triggers: equality-safe gates say `at least`, while genuinely strict continuing obligations say `more than` or `above`. Player-visible mission durations and expiry text use the live variables where the duration branches dynamically.

## Tree-replacement warning and country identity

`utopia_manifesto_accept_tree_warning_tt` accurately states that acceptance replaces the national focus tree while existing forces, territory, technology, leaders, parties, and the base flag initially remain. It also states that later choices may establish institutions, leadership, and a cosmetic identity.

This agrees with the current source:

- acceptance loads `utopia_manifesto_tree`;
- Event 015 does not call `set_party_name`;
- route formation may change politics, promote institutional leadership, and apply one of five cosmetic identities;
- teardown restores the recorded political/leader state and removes the Event 015 cosmetic identity.

The five cosmetic-country families and the five long-form public-organisation names are complete and route-distinct: Voluntary Commonwealth, Union of Common Tables, Commonwealth of Measure, Closed Island, and Practical Commonwealth each retain their own institutional tone.

## Ledger vocabulary and visible-state audit

The current visible Ledger uses only **Need**, **Plenty**, **Concord**, and **Choice versus Assignment** as central values. It includes complete public breakdown text for base, policy/public record, live material/institutional contributions, war, occupation, territorial loss, capital, subject status, and pressure where implemented.

Final value-only scan:

- `Surplus`: 0;
- `Overreach`: 0;
- `Vocation Balance`: 0;
- `Foreign Suspicion`: 0;
- `League Confidence`: 0;
- `contradiction meter`: 0;
- `World Tension`, `World Tension Subsides`, `Event 15`, and `ID15`: 0.

Engine-facing identifiers such as `_surplus_` remain stable identifiers but do not display that retired wording. `Consent` remains only as the Consent of Households route, focus/achievement/constitutional proper names, or ordinary household assent; it is never presented as a Ledger scalar. Three uses of `excess` refer to physical stores or goods, not a renamed meter.

The two high-Plenty focus gates now name the displayed **Commonwealth in Plenty** band rather than the retired band label.

## Hidden-route spoiler audit

The Event Details text and workbook row contain zero exact occurrences of:

- `Joke Understood`;
- `Commonwealth of Revision`;
- `Humanist Reform`;
- `hidden route`.

The shared Event Details copy may allude to public revision, but it does not disclose the hidden route's name or unlock condition. Exact hidden-route names occur only on hidden achievements, branch-gated focuses, route-specific Ledger outputs, or constitutional-correction actions whose live visibility requires the route or its reveal condition. The hidden focus branch is protected by `allow_branch` before its route-specific availability text can appear.

## Event Details, history, evolutions, and catalog

The 20 shared event-name/details/evolution keys have exactly one English definition and are all referenced by the shared scripted-localisation surfaces. The current mapping resolves Event ID 15 symbolically to `chaosx.event_name.15: "Utopia Manifesto"` and the bespoke Event Details body.

All five evolution stages are complete in current detail, selected detail, locked title, public title, body, summary, and history paths:

1. Glosses in the Margin
2. Necessary Shores
3. Cities of One Measure
4. Nowhere Made Law
5. The Perfect Island

Workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx` contains Event ID 15 exactly once at `Events!A16:M16`.

| Cell/surface | Current result |
| --- | --- |
| A16 | numeric `15` |
| B16 | exact `chaosx.event_name.15` value |
| C16 | exact Event Details value |
| D16:H16 | exact title, two newlines, and body for evolutions I-V |
| I16 | blank world-end scenario |
| J16 | `Minor Fire-Once` |
| K16:L16 | blank cluster ID and member severity |
| M16 | `Fully Functional` |

No Event 015 cluster membership exists. The runtime and workbook both contain zero uses of `World Tension Subsides`, `world_tension_subsides`, `Event 015 Placeholder`, `015_placeholder`, `015_world_tension_falls`, or visible `ID15`. Shared runtime registries contain zero literal Event ID 15 assignment and 17 symbolic `constant:utopia_manifesto_event.id` references.

## Super-event text and audio-source fidelity

Slots 96-100 exactly reproduce the approved research package:

- shared title: `UTOPIA HAS NEIGHBORS`;
- shared Thomas More quotation and `Thomas More, Utopia, trans. Gilbert Burnet` attribution;
- shared response: `Nowhere has a timetable.`;
- five distinct route descriptions, each byte-for-byte present in the text research note.

The voluntary description emphasizes sovereign exit and kept promises; the council description emphasizes recallable mandates and coordination; the planned description balances visible infrastructure with assignment; the closed description exposes compulsory labour, hierarchy, and checkpoints; the practical description emphasizes revision, criticism, and amendable agreements. No description reveals counters, focus names, trigger thresholds, or hidden-route logic.

The six audio-ID-57 music display keys all read `Symphony No. 3 in F major: III. Poco allegretto`, agreeing with the frozen Brahms/Musopen CC0 research and the music catalog. No placeholder title or historical Event 15 audio identity survives in the current localisation path.

## Encoding and language hygiene

- 9/9 Event 015 English files have a UTF-8 BOM and the exact `l_english:` header.
- Versioned `:0` keys: 0.
- Leading whitespace before keys: 0.
- Malformed active localisation lines: 0.
- Empty values: 0.
- Bracket or colour-format imbalance: 0.
- Placeholder values (`TODO`, `TBD`, `FIXME`, `PLACEHOLDER`): 0.
- Mojibake/replacement characters: 0.
- Player-facing update-history language (`reworked`, `newly added`, `hardcoded`, `capped`, or update-request wording): 0.
- Em dashes and semicolons in Event 015 player-facing values: 0.
- Exact Event 015 key duplicates inside the nine files: 0.
- Exact Event 015 key duplicates against all other English localisation files, including legacy `:0` syntax: 0.

Eight English division/template names remain direct engine strings inside `create_unit`: Citizen Watch, Workers' Defense Column, Commonwealth Engineer Corps, Household Service Formation, Small Professional Guard, League Defense Group, Auxiliary Service Column, and Commonwealth Field Guard. Official effect syntax and vanilla precedents use direct strings for these fields. They are valid and complete for this English audit, but remain a translation-portability limit outside English.

## Bounded corrections made by this audit

Only four existing English values were changed:

- `decision_utopia_initialize_league_requirements_tt`: `first surplus offer` to `first material-aid offer`;
- `decision_utopia_send_surplus_abroad_requirements_tt`: `exportable surplus` to `exportable stores`;
- `utopia_manifesto_surplus_beyond_the_shore_available_tt`: retired Plenty band name to `the Commonwealth in Plenty band`;
- `utopia_manifesto_offer_the_first_surplus_available_tt`: retired Plenty band name to `the Commonwealth in Plenty band`.

Files changed by this auditor:

- `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml`;
- `localisation/english/015_utopia_manifesto_focus_l_english.yml`;
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/localisation_completion_current_full_reaudit_2026_07_15.md`.

No gameplay, scripted localisation, interface, asset, audio, source-research, or workbook file was changed by this auditor.

## Frozen Event 015 localisation hashes

| File | Definitions | Lines | SHA-256 |
| --- | ---: | ---: | --- |
| `015_utopia_manifesto_country_package_l_english.yml` | 210 | 223 | `42bbc60ef46e9f3c8233c9842a0646b02a72560cd77649195b739fb57416ae92` |
| `015_utopia_manifesto_decision_completion_l_english.yml` | 671 | 699 | `01452765d2413b06844a46aaba1c5e0a552fbd2a7ea319b70d59262dbd83c445` |
| `015_utopia_manifesto_events_l_english.yml` | 486 | 576 | `5d5e0aa9caaa1d39e5065ff7e43bb1c43c812f313e2eb22cb3954adb6d70215b` |
| `015_utopia_manifesto_evolution_consumption_l_english.yml` | 84 | 101 | `fc4b71c1190ab45a3d6723a30b7256cee228871a513476345658982b20e534b1` |
| `015_utopia_manifesto_evolutions_l_english.yml` | 18 | 19 | `bbf1d8af6246fbf892f4a9d7b4b41e9fc94e8ff5a810588d74180d00cde85cf7` |
| `015_utopia_manifesto_focus_l_english.yml` | 349 | 353 | `c8d34f7e48facc7eac266d64383af3fa66e93c7a9a48d4d46ba2e96a8e570828` |
| `015_utopia_manifesto_ideas_l_english.yml` | 136 | 137 | `0591a362d9ed653e132915c4d4a83e019048e5cc8fde2aa0505eca7d53be702a` |
| `015_utopia_manifesto_l_english.yml` | 474 | 485 | `a80a6dbaf7e2591a46e836fcbd419d3c7dfac324ccc1f7ba118266678e3fdaa5` |
| `015_utopia_manifesto_super_event_l_english.yml` | 20 | 21 | `8f14e4fb22578e942ba5019e1022032b12a794c464e61fcef8d7d01bb5527e32` |
| **Total** | **2,448** | **2,614** | all nine BOM |

## Frozen authority hashes

| Authority | SHA-256 |
| --- | --- |
| `events/015_utopia_manifesto.txt` | `a7d27155c463424f19fb1d661356a42ccb90cc4b29f8e42a03ea78ba86b9b164` |
| `common/national_focus/015_utopia_manifesto_focus_tree.txt` | `8a905d4b1922ab88bfab97716ba79721fc5b42679863c9543fb04d2cd489fc05` |
| `common/on_actions/015_utopia_manifesto_on_actions.txt` | `c2b26e499078d0c7782e46db587d377d8d64cee02e372f2ae8e087c7cea7ea81` |
| `common/decisions/015_utopia_manifesto_decisions.txt` | `5dcd41ef8669a4384fedb2efa9761e657fe8a5ff8ea686e45046005fd23d17fd` |
| `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt` | `aa8c813015cacbf2b5d588b82c39d3b440ed9e83f0009a6a048f83e5d0f82ed4` |
| `common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt` | `04c46f18ad0c23f70303d75d0d00bb45afcaaf9ab5d877ba01bfe1e9754e3347` |
| `common/decisions/categories/015_utopia_manifesto_categories.txt` | `feb02d3e2af05804a30d2c6ef4a1ebb647b3ced2dfe96cb6c8afed2e035a91e8` |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | `ed44d3a9892061bb77ebe6e6039be8d7a6a1bcc5f292091c4e5ede32b39d2b8d` |
| `common/scripted_effects/015_utopia_manifesto_prefire_evolution_effects.txt` | `1d757540eab0082a09df425578e4208e09cb364832d7b170591ea763d50c60c4` |
| `common/scripted_triggers/015_utopia_manifesto_triggers.txt` | `d0c304d2b4cd5dccd72b40cff8e9ab4caa3beab58838ce68057eacf31bcfe9af` |
| `common/scripted_triggers/015_utopia_manifesto_prefire_evolution_triggers.txt` | `ba4ac12603651718c633a0b3c90b530097ceadcf16969fadcec69c77508a1c5e` |
| `common/ideas/015_utopia_manifesto_ideas.txt` | `84f1e322ef827edd4eedff68ba99e67ae61e6c4ed1172193cf77eb3f4d05326a` |
| `common/characters/015_utopia_manifesto_characters.txt` | `5cdf2ea793216351b5a250bbb1bb0eea84103e7668791b30867216af436749cb` |
| `common/country_leader/015_utopia_manifesto_traits.txt` | `6cd9a84026b739030115c2a81d2303c5a94bd4a3b4b5178b10947897603230a2` |
| `common/dynamic_modifiers/015_utopia_manifesto_state_modifiers.txt` | `de99f8f7cf191da4eea3580a84e37a19409b1e53d821bb557b8a89f5bfc22387` |
| `common/opinion_modifiers/015_utopia_manifesto_opinion_modifiers.txt` | `5a7f8f83fd9d55f12a0b5549ad71695c51b095db5a4ade0167730cb719af9bb1` |
| `common/achievements/chaos_redux_achievements.txt` | `c1c729f4717129e8abb60303a79e6fe4318598e6ac0221c79c65faa1ffe4391c` |
| `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt` | `6e44014672139189c53bedb4dd441b9d27900d934a42b6f1fb2166287b6701ed` |
| `interface/015_utopia_manifesto_ledger.gui` | `e38e23553de6986525169a58359f29d620f733f747eb4abe7bfb31958efd01b8` |
| `common/wargoals/015_utopia_manifesto_wargoals.txt` | `d81e435349f9bcc1386b98e492d67eaa87f2d029886cb07b91588401a3314543` |
| `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` | `da2b2c86a47979dde9b7cae022e4f1798bac6029955858ca90fddd8a9167fa75` |
| `localisation/english/chaosx_event_names_l_english.yml` | `2e1c78a86e307b8cc19ebc735d02b52fb82d470eecea20133d2874c0c6a2796e` |
| `localisation/english/chaosx_gui_l_english.yml` | `451862430b424bf603626fac24aa66dad17120c3517c0447b41edb435e83ac1b` |
| `localisation/english/chaosx_music_l_english.yml` | `e6516afd808b30f7c825f2f9d8398d09c773406c93ee35249debc2779cbc4c19` |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | `6aa758d699d814599a1011d5f9acc1089bbf42baf053be7a4dbabadd525091a2` |
| `docs/super_events/015_utopia_manifesto/text_research.md` | `4eb5209323e8746ebdfc1c949298e45482db313f03f8565c5f35517967eb93af` |
| `docs/super_events/015_utopia_manifesto/audio_research.md` | `2c87617e505064368af282bf885664e47e78494efca80f137d9a76ec6d54d655` |
| `music/chaosx_music_track_list.html` | `7480d2595f9df579b8459b57547a6a53d25911644887a863a3cc248d29e775c2` |

## Meaningful validation limits

- No HOI4 session was launched, so conditional tooltip substitution, scope resolution, and scripted-localisation evaluation were not observed at runtime.
- No rendered Ledger, Event Details, focus tree, decision panel, achievement panel, or super-event screenshot pass was performed; clipping and wrapping remain outside this source audit.
- English only was in scope. The eight engine-direct unit/template names are the only known translation-portability limitation.

These are validation limits, not known failures in the audited English surface.

## Simplifications, omissions, fallbacks, and blockers

None. No requested English source surface was omitted; no placeholder or weaker fallback was accepted; no blocker remains. The four detected vocabulary defects were corrected and re-audited against the frozen current source.

## Skills and references used

- `chaos-redux-events`
- `xlsx` for read-only workbook parity
- repository `AGENTS.md`
- required offline Paradox wiki core pages, plus Interface Modding, Scripted GUI Modding, National Focus, Country Creation, Achievement Modding, and Music Modding
- vanilla official localisation formatter/object, script-concept, effects, triggers, and script-constant documentation
- vanilla focus, decision/mission, scripted-localisation, character/advisor, and achievement precedents

The required offline wiki snapshot was used. No Paradox wiki web access was used.
