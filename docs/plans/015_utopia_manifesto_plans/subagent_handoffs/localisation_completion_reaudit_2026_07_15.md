# Event 015 Localisation Completion Re-audit

Date: 2026-07-15  
Auditor: `chaosx_localisation_auditor`  
Baseline: current working source after `localisation_completion_handoff_2026_07_15.md` and the corrections made while this audit was active  
Scope: Event 015 English player-facing localisation and its live source wiring  
Mode: read-only, except for this report; no commit created

## Verdict

**PASS.** The current Event 015 English localisation surface is statically complete. No open P0-P2 localisation finding remains.

The core event/decision inventory contains 1,287 unique required keys and zero missing keys. The broader Event 015 audit also found zero missing keys across focuses, ideas, characters, advisor traits, dynamic state modifiers, opinion modifiers, achievements, cosmetic identities, the private wargoal, the Ledger, scripted localisation, event history/evolutions, Event Details, news events, and route-specific super-events.

This is a static source-to-localisation result. Runtime rendering and tooltip-scope evaluation were not performed; those limits are recorded below.

## Current-source inventory

| Surface | Current source inventory | Result |
| --- | ---: | --- |
| Decisions and missions | 164 IDs; name and description for each | 328/328 present |
| Decision categories | 9 IDs; name and description for each | 18/18 present |
| Custom costs | 92 bases; base, `_blocked`, and `_tooltip` for each | 276/276 present |
| Decision custom effect/trigger tooltips | 163 unique keys | 163/163 present |
| Event title, description, option, and event-tooltip references | 502 unique keys, including 36 event effect tooltips | 502/502 present |
| **Core required set** | **1,287 unique keys** | **0 missing** |
| National focuses | 125 IDs; name and description for each | 250/250 present |
| National ideas | 50 IDs; name and description for each | 100/100 present |
| Characters | 24 IDs; name and description for each | 48/48 present |
| Advisor traits | 16 IDs; name and description for each | 32/32 present |
| Dynamic state modifiers | 19 IDs; name and description for each | 38/38 present |
| Opinion modifiers | 5 IDs | 5/5 present |
| Achievements | 14 IDs; `_NAME`, `_DESC`, and bespoke condition tooltip for each | 42/42 present |
| Cosmetic identities | 5 tags; base/DEF/ADJ plus four ideology variants | 75/75 present |
| Necessary Ground wargoal | type name, description, and war-name format | 3/3 present |
| Event 015 scripted-localisation outputs | 200 unique output keys | 200/200 present |
| Ledger/direct scripted-GUI localisation | 25 direct localisation references | 25/25 present |

The nine `015_utopia_manifesto*_l_english.yml` files contain 2,224 unique keys. Exact case-sensitive duplicates within those files or against other English localisation files: zero. Uppercase cosmetic-tag keys and similarly named lowercase idea keys were compared ordinally and are intentional distinct keys, not duplicates.

## Accuracy and wiring evidence

### Costs, thresholds, durations, and outcomes

The 92 live custom-cost families were compared with their decision triggers and payment effects, including the separately displayed Political Power cost. Fixed equipment, manpower, stability, war-support, command-power, convoy, and reserve costs agree with the live constants and payment paths. Dynamic formation and institutional costs use the variables prepared by their corresponding source effects.

Equality-sensitive district and repeal wording now matches the live triggers. District survey, four district starts, penal works, district charter, and total repeal say `at least` where the source accepts exact equality. The district's continuing housing, transport, and role-plan obligations still say `more than` or `above` where the scripted triggers intentionally use strict `>` comparisons.

Explicit duration text agrees with the current source:

- published accounts last 90 days;
- Necessary Ground cases display the live expiry variable, while the draft tooltip identifies the Need-law alternatives as 120, 180, or 240 days;
- the pre-fire domestic shore repair is bounded at 90-210 days;
- foreign support gives a 30-day project-planning credit;
- island lease renewal and counteroffer text matches three-year and two-year extensions;
- Consent of Households adds 30 days to district charter review;
- emergency calling and levy text uses the prepared live duration variables.

Target and completion text was compared with the live effects for transfers, state control, settlement and stewardship status, member obligations, project cancellation, expiry, route locks, mission cleanup, and constitutional teardown. No current text promises an effect that is absent or omits a material route-specific consequence found in the audited paths.

### Prefire and aftermath

Events `chaosx.nr15.105` through `.109` and `.117`, their three deadline missions, and the domestic shore-repair decision are fully localised. The foreign-support text discloses the immediate Plenty and Assignment movement, the 30-day planning credit, Sponsored Law, and its route-resolved consequences. Perfect Island prefire text correctly describes a recorded choice for later compatible-route consumption.

Aftermath events `.120` through `.123` have bespoke titles, descriptions, options, and effect tooltips. Their text follows the implemented sequence: snapshot and viable successor selection, stewardship/assigned-colony release, controlled and owned state return, exactly one practical legacy, the book's public fate, identity teardown, and League/faction handoff where applicable.

The acceptance warning is consistent with the current identity package: the focus tree is replaced; existing forces, territory, technology, leaders, parties, and base flag initially remain; later route choices may establish institutions, leadership, and a cosmetic identity. Event 015 does not call `set_party_name`. Teardown retires Event 015 characters, restores the saved original ideology, exact surviving original leader, and original election permission, then drops the cosmetic tag.

### Country identity, leaders, and achievements

All five cosmetic identities have complete base and ideological name/DEF/ADJ coverage. Ten route-organisation short/long names exist; the Ledger's `GetUtopiaManifestoPoliticalOrganization` selector exposes the five long names plus a localised inherited-organisation state without overwriting native parties.

All institutional leaders, successors, advisors, and advisor traits have bespoke names and descriptions. The 14 achievements have complete name, description, and condition-tooltip triplets. In particular, `The Perfect Measure` now matches its proof effect: four actual district roles plus the Provision Ring, not five ordinary district roles.

### Wargoal, event history, evolutions, news, and super-events

The private `utopia_manifesto_necessary_ground_take_state` wargoal has its own display name, description, and `UTOPIA_MANIFESTO_NECESSARY_GROUND_WAR_NAME`. Its text identifies the marked Necessary Ground state and target rather than implying a general conquest claim.

Event history resolves constant Event ID 15 to `chaosx.event_name.15: "Utopia Manifesto"`. The latest selected actor is saved as `utopia_manifesto_latest_actor` and is used by the default actor mapping. Event Details resolves Event 015 to its bespoke manifesto description, not a generic placeholder.

All five evolution stages are mapped in history, current-detail, selected-detail, locked-title, title, and body selectors: `Glosses in the Margin`, `Necessary Shores`, `Cities of One Measure`, `Nowhere Made Law`, and `The Perfect Island`. The evolution localisation file supplies the type, five title/locked-title/body triplets, locked body, and summary: 18/18 present.

News events `.160` through `.162` each have a title, description, and option. Super-event display slots 96-100 map to the five current route images and all 20 required `.t`, `.q`, `.a`, and `.d` keys. The effect uses the route-resolved slot, the documented 14-day visibility flag, and audio ID 57.

## Ledger vocabulary audit

The visible Ledger surface uses only **Need**, **Plenty**, **Concord**, and **Choice versus Assignment** as scalar concepts. The direct GUI keys and all 200 Event 015 scripted-localisation outputs resolve without missing text.

Visible-value scan results:

- `Surplus`, `Overreach`, `Vocation Balance`, `Foreign Suspicion`, `League Confidence`, `contradiction meter`, `World Tension`, `World Tension Subsides`, `Event 15`, and `ID15`: zero occurrences.
- `Consent`: 13 intentional occurrences. Every occurrence is a route, focus, achievement, or constitutional proper name/comparison; none is a Ledger scalar reading.
- `excess`: 3 intentional material-prose occurrences referring to excess stores or goods; none is a renamed Ledger scalar.
- Hidden identifiers such as `plenty_band.surplus` remain engine-facing key names whose displayed English values use Plenty vocabulary.

No stale `World Tension Subsides` or numeric-ID placeholder reaches Event 015's event name, history, evolution, or Event Details paths.

## Encoding and localisation hygiene

- All nine Event 015 English files have a UTF-8 BOM.
- Versioned `:0` keys: zero.
- Leading whitespace before localisation keys: zero.
- Malformed one-line entries: zero.
- Exact case-sensitive duplicate keys: zero.
- Placeholder values (`TODO`, `TBD`, `FIXME`, or `PLACEHOLDER`): zero. Ordinary narrative uses of the word `missing` describe in-world shortages or records and are not placeholders.
- No visible literal prose is embedded in `interface/015_utopia_manifesto_ledger.gui`.

Eight English division/template names are necessarily passed as direct strings to `division_template` and `create_unit`: `Citizen Watch`, `Workers' Defense Column`, `Commonwealth Engineer Corps`, `Household Service Formation`, `Small Professional Guard`, `League Defense Group`, `Auxiliary Service Column`, and `Commonwealth Field Guard`. Offline wiki, official effect documentation, and vanilla precedents use direct strings for these engine fields. They are valid English player-facing names and are not missing YAML keys, but they are a translation-portability limitation outside this English-only audit.

## Findings closed during re-audit

The following live defects were identified during this re-audit, corrected by the parent while the audit remained read-only, and rechecked in the current source:

1. Twelve dynamic state modifiers lacked display-name and description pairs; all 19 current state modifiers now have both.
2. The Necessary Ground wargoal lacked its type and war-name localisation; all three required keys now exist.
3. The acceptance warning implied a later party replacement that the current identity package does not perform; it now describes institutions, leadership, and cosmetic identity accurately.
4. Eight custom-cost/start strings and the refugee-municipality start description used strict `above` wording after their triggers became equality-safe; they now say `at least`, while genuinely strict district suitability/obligation language remains unchanged.
5. `The Perfect Measure` described five ordinary district kinds; it now states four district roles plus the Provision Ring in both achievement description and tooltip.
6. Necessary Ground expiry text hardcoded 180 days despite the 120/180/240-day Need-law branches; the mission now displays the live expiry variable and the draft tooltip states all three legal limits.

No open finding remains after the final rebaseline.

## Meaningful validation not performed

- No live HOI4 session was launched, so conditional tooltip branches, event-target scope substitution, and scripted-localisation variable formatting were not observed at runtime.
- No rendered Ledger/Event Details/super-event screenshot pass was performed, so clipping, line wrapping, and font/icon layout were not visually measured.
- Only English was in scope; the eight engine-direct division/template names were not internationalised.
- No optional Event Chain Viewer or Scripted GUI Studio artifact was needed for this source-level localisation audit.

These are validation limits, not known localisation failures.

## Simplifications, omissions, and blockers

No requested English source surface was omitted, no fallback or placeholder was accepted, and no blocker remains. The audit is complete at the static source/localisation level subject to the runtime/render limits above.

## Skills and references used

- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-subagents`
- Repository `AGENTS.md`
- Required offline Paradox wiki core pages, plus Interface Modding, Scripted GUI Modding, National Focus, Country Creation, Achievement Modding, and Division Modding
- Vanilla official localisation formatter/object, script-concept, effects, and triggers documentation, plus vanilla custom-cost, wargoal, dynamic-modifier, division-template, and `create_unit` precedents

The offline wiki snapshot was used as required; no Paradox wiki web access was used.
