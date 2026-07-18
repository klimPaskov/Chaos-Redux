# Event 019 Final Claimant Identity Closure

> Superseded visual evidence: all human-portrait, face, sex-presentation, source-dimension, hash, and contact-sheet claims in the body describe rejected art. Current fixed portrait slots show twenty regional claimant armies/musters and six derivative massed hosts with no individual focal human/person; see `019_full_portrait_regeneration_handoff_2026_07_16.md` and the current 26-row crosswalk. Runtime claimant sex/name correction remains governed by `019_male_claimant_identity_correction_handoff_2026_07_16.md`; nonvisual regional/profile and lifecycle findings below remain historical audit evidence.

Date: 2026-07-16

Mode: fresh read-only specialist audit with one documentation handoff

Result: claimant identity closure is clean. The four historical remediation areas are closed. Exact open severity is **P0: 0, P1: 0, P2: 0**.

## Scope and ownership

This audit covers only Event 019 claimant identity, its four report events, its Muster Board presentation, the one-state claimant resolution, and the claimant portrait package. It does not approve or alter the separate exact-division transfer and same-battle achievement contracts.

The binding registry rule is satisfied. The only Event 019 registry code file is:

- `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`

No second Event 019 registry code file was created.

The persistent audit artifact from this pass is this handoff. No gameplay, localisation, GUI, GFX, asset-path, or registry-source edit was made by the audit.

Skills used:

- `chaos-redux-subagents` for the read-only audit boundary, severity handling, and handoff requirements
- `chaos-redux-events` for Event 019 integration and exact report-context criteria
- `chaos-redux-event-assets` for portrait provenance, source-to-runtime crosswalk, full portrait, and DDS validation criteria

## Required references consulted

The audit consulted the required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, interface modding, and scripted GUI modding.

It also consulted the official installed-game documentation for scripted GUIs, script concepts and constants, collections, effects, triggers, and dynamic variables. Relevant engine definitions included event targets, `meta_effect`, `create_corps_commander`, character roles, variable and array access, dynamic-country reservation, and controlled-state counts.

Direct vanilla precedents included:

- `common/decisions/HOL.txt:2081-2091` for a corps commander with a named portrait, id, traits, and stats
- `common/national_focus/spain.txt:7255-7275` for male and female corps commanders and `female = yes`
- `interface/_leader_portraits.gfx:5-17` for the neutral `GFX_portrait_unknown` sprite
- `interface/_random_portraits.gfx:134-135` and the canonical commander reference library for full `156x210` commander portraits

## Severity totals

| Severity | Open count | Finding |
| --- | ---: | --- |
| P0 | 0 | none |
| P1 | 0 | none |
| P2 | 0 | none |

## Historical remediation closure matrix

| Historical area | Status | Primary evidence |
| --- | --- | --- |
| Exact selected and created identity | Pass | `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:77-98`, `207-264`, `302-372`; `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt:10-91`, `95-201`, `205-286`; `localisation/english/019_infrantry_spawn_l_english.yml:1139-1307` |
| Neutral invalid context and hidden invalid portrait | Pass | `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt:116`, `141`, `166`, `191`; `interface/019_infantry_spawn_muster_board.gui:196`; `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:162-166`, `230-232` |
| Correct regional pools with no global fallback | Pass | `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:27-109`; `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:100-163`; `docs/specs/019_infantry_spawn_specs/matrices/019_possessed_general_matrix.md`; `docs/assets/019_infantry_spawn/notes/claimant_identity_metadata.md:7-30` |
| Exact asset crosswalk and lifecycle ownership | Pass | `docs/assets/019_infantry_spawn/notes/claimant_portrait_asset_crosswalk_2026_07_16.md:11-40`; `docs/assets/019_infantry_spawn/prompts/claimant_portrait_reproduction_specs_2026_07_16.md:19-44`; `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:49-75`; `common/script_constants/019_infantry_spawn_claimant_constants.txt:77-94` |

## 1. Exact selected and created claimant identity

The runtime identity is one aligned claimant row rather than a collection of independently selected presentation values.

- `infantry_spawn_load_claimant_localisation_context` clears the prior visible identity, requires aligned ledgers and a bounded exact row, then copies that row's profile, name variant, archetype, uid, and headquarters at `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:77-98`.
- The created commander receives the exact row candidate's name, full portrait sprite, stable character id, gender flag, archetype trait tokens, and stats through the two picture meta effects at `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:207-264`.
- The even profiles 02, 04, 06, 08, 10, 12, 14, 16, 18, and 20 are the ten female-presenting profiles and set `female = yes`. The remaining ten do not. The mapping is explicit at `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:29-46` and matches the twenty metadata rows.
- Creation appends the aligned row, freezes its index in `infantry_spawn_new_claimant_index`, and later loads that frozen row for report `.200` at `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:302-372`.
- `GetInfantrySpawnClaimantName` and `GetInfantrySpawnSelectedClaimantName` each provide all eighty profile and name-variant combinations. The localisation file has exactly four regional and gender-matched names for each of twenty profiles. All twenty primary names match the asset metadata.
- The selected title and description selectors cover profiles 01 through 20 at `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt:144-191`. All twenty authored titles and descriptions are consumed by `infantry_spawn_muster_gui_claimant_identity` at `localisation/english/019_infrantry_spawn_l_english.yml:1091`.
- The default trait token is `infantry_spawn_claimant_traits_none` at scripted-localisation line 201, and that key is an empty string at localisation line 1307. Invalid archetype context does not inherit Quartermaster traits.

Historical P2-01 is closed.

## 2. Invalid context is neutral and cannot impersonate claimant 01

Invalid or cleared context does not substitute a valid claimant.

- Both portrait selectors default to `GFX_portrait_unknown` at `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt:116` and `141`.
- The GUI declaration also starts from `GFX_portrait_unknown` at `interface/019_infantry_spawn_muster_board.gui:196`.
- The scripted GUI shows the portrait only when the selected row is valid and its profile is within 1 through 20 at `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:162-166`.
- Its dynamic image is the selected-profile sprite at scripted-GUI line 231.
- The exact-row loader clears every presentation variable before validation at `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:80-97`.
- The title, description, and name selectors use the explicit non-claimant diagnostics `No Claimant File`, `No verified private command identity is selected.`, and `Unnamed Muster Claimant` for invalid context at localisation lines 1299-1301.

No runtime selector, GUI base sprite, or source-of-truth document authorizes claimant 01 as an invalid-context or region fallback.

Historical P2-02 is closed.

## 3. Regional pools and fail-closed selection

The runtime region trigger maps every profile explicitly at `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:27-109`.

The corrected cross-region rows are exact:

- Profile 04 supports Asia and Australia at trigger lines 41-44.
- Profile 12 supports Asia and Australia at trigger lines 73-76.
- Profile 09 supports Europe and North America at trigger lines 61-64.
- Profile 13 supports Europe and South America at trigger lines 77-80.
- Profile 19 supports North America and South America at trigger lines 101-104.
- Profile 20 supports Australia only at trigger lines 105-108.

Compatible-profile capacity before any live-profile reservation is:

| Runtime region | Compatible profiles | Count |
| --- | --- | ---: |
| Europe | 01, 02, 05, 09, 10, 13, 14, 18 | 8 |
| Asia | 04, 05, 06, 07, 11, 12, 17 | 7 |
| Australia | 04, 12, 20 | 3 |
| North America | 08, 09, 19 | 3 |
| South America | 08, 13, 19 | 3 |
| Middle East | 03, 11, 16 | 3 |
| Africa | 03, 15, 16 | 3 |

Every supported region therefore has at least three compatible identities, matching the three-active-claimant ceiling.

The random selector requires both availability and regional compatibility at `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:118-125`. Its deterministic exhaustion scan repeats both requirements at lines 128-151. If no compatible unused row exists, `infantry_spawn_claimant_profile_selected` remains false and creation stops. There is no global, catch-all, or regionally mismatched recovery branch.

The matrix, identity metadata, prompt record, crosswalk, and exposed descriptions agree on the two Australasian diaspora profiles and the Australia-only profile.

Historical P2-04 is closed.

## 4. Exact 20-row asset and provenance crosswalk

The claimant asset package is exact and complete.

- The crosswalk contains twenty numbered rows. Each row names the working identity, required regional pool, built-in ImageGen provenance record, source PNG, processed PNG, runtime DDS, sprite, dimensions, and SHA-256 values.
- The prompt record contains twenty rows and twenty unique built-in ImageGen output ids. Each source hash agrees with the crosswalk.
- All twenty source paths, twenty processed paths, and twenty DDS paths exist. All sixty current SHA-256 values match the crosswalk. Each stage has twenty unique hashes.
- Every processed PNG and DDS is `156x210`.
- Every DDS has the complete legacy one-level uncompressed BGRA layout, including the 128-byte header, 32-bit pixel format, BGRA masks, texture capability, exact `131168` byte length, and no unexpected mipmaps.
- Every processed PNG is decoded-pixel equal to its paired DDS.
- `interface/019_infantry_spawn.gfx:50-129` registers exactly one sprite and one numbered texture path for each profile 01 through 20.
- Original-detail inspection of the source and processed contact sheets confirms twenty distinct, readable one-person portraits with the required ten-male and ten-female split. The presentation agrees with the recorded regional and gender metadata.
- The full portrait sprite is used both in the commander picture meta effect and the Muster Board. No 50x67 substitute is used.

Historical P2-03 is closed.

### Retained processor audit note

The retained processor `docs/assets/019_infantry_spawn/_tooling/process_event_019_generated_art.py` has no help-only argument path. Querying it with `--help` executed its deterministic main function under the shell's Python 3.9/Pillow 11.1 environment.

Within the bounded claimant crosswalk, that first pass temporarily changed only the encoded PNG bytes for processed profile 19 from the documented SHA-256 `316190c21adba57393d9de7aa517b7b8e0b702ae5ebee2c0dbf6fb9b7271d208` to `a8f2b52a120b2cccfaa68947a772fd7fe7edd213f0ee5bd044a6ef06dea9d6e9`. The decoded pixels remained exactly equal to the unchanged DDS.

The retained package's original environment was then identified as Python 3.13/Pillow 12.2. Re-running the retained processor in that environment reproduced the documented profile-19 hash exactly and returned the bounded claimant package to its recorded state. The final independent crosswalk check is sixty of sixty hashes matching. No claimant source, processed PNG, or runtime DDS hash delta remains from the audit.

## 5. Reports `.200` through `.203` and Muster Board exact-row binding

All four claimant reports load the exact intended row before firing:

- Appearance `.200` freezes the newly appended row before later selection refresh and loads `infantry_spawn_new_claimant_index` at `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:364-372`.
- Demand `.201` loads the exact selected demanding row at `common/scripted_effects/019_infantry_spawn_claimant_demand_effects.txt:147-155`.
- Revolt warning `.202` loads the exact warning row at `common/scripted_effects/019_infantry_spawn_claimant_effects.txt:259-273`.
- Takeover `.203` loads the winning row after its status becomes terminal at `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt:201-229`. The localisation loader deliberately validates array bounds rather than ordinary active status, so the takeover row remains available to this report.

The events are registered as triggered-only country events at `events/019_infantry_spawn.txt:125-194`. Each uses the claimant evolution report picture, and each description consumes `GetInfantrySpawnSelectedClaimantName` at localisation lines 27, 31, 36, and 40.

The Muster Board loads its exact selected row at `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:483-485`. Cycling chooses a valid active row and then invokes the same loader at lines 488-514. The command panel consumes the selected name, title, description, archetype, status, demand, and portrait from that single loaded context.

## 6. One-state takeover and failed-coup handling

One-state countries do not attempt a territorial civil war.

- `infantry_spawn_country_is_microstate` is controlled-state count below the centralized minimum of two at `common/scripted_triggers/019_infantry_spawn_triggers.txt:698-700` and `common/script_constants/019_infantry_spawn_constants.txt:1094`.
- A due claimant crisis routes a microstate to takeover or failed coup at `common/scripted_effects/019_infantry_spawn_claimant_effects.txt:289-307`.
- Takeover requires the exact selected claimant and the configured influence threshold. It is allowed only when muster control is below the configured failed-coup control threshold.
- A different living Event 067 Generalissimo forces the natural microstate result to failed coup at `common/scripted_effects/019_infantry_spawn_claimant_effects.txt:278-286`.
- Successful takeover resolves the exact character id, promotes that existing character to country leader, preserves the portrait and name through character-role promotion, records status `takeover`, closes ordinary claimant creation, and retires other claimant commanders at `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt:126-237`.
- Failed coup removes the exact claimant character by id, restores its controlled rows, records status `arrested`, decrements active claimant count, and clears crisis state at `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt:239-262`.

This is the required one-state government replacement or failed-coup result. It does not manufacture a zero-state claimant derivative.

## 7. Identity reservation and release lifecycle

Profile ownership is based on live identity, not permanent historical row presence.

The stable status enum is:

- active ordinary statuses `emerging`, `recognized`, `demanding`, and `countermanded`
- terminal or special statuses `retired`, `arrested`, `takeover`, `revolt_staged`, `revolted`, and `defeated`

`infantry_spawn_evaluate_current_claimant_profile_availability` reserves a profile when an ordinary active row has it, when the victorious claimant remains ruler under `takeover`, or when a derivative handoff remains in `revolt_staged`. It releases the profile for `retired`, `arrested`, `revolted`, and `defeated` history rows at `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:49-75`.

Takeover also sets `infantry_spawn_claimant_takeover_complete`, and claimant creation rejects that country at `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:160-170`. The ruling identity remains reserved without consuming regional capacity in an active country that can still create claimants. Failed coup and retired rivals release their profiles after their exact characters are removed.

The lifecycle contract therefore prevents simultaneous live duplicate identities without exhausting a region through terminal history.

## Separate approval-gated global blockers

The following remain global Event 019 blockers. They are not claimant identity findings and are not included in the 0/0/0 claimant severity totals:

- `B-019-001`: exact live recorded-formation subset ownership transfer. The approved native capability remains unavailable. Recreate, prove, and delete would lose live division state, so that fallback remains unapproved.
- `B-019-002`: exact same-battle proof for the four division-specific achievements. The current engine-facing callbacks cannot atomically prove the exact recorded division and battle predicates, so weaker proxy awards remain unapproved.

Their current disposition is documented at `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_decision_mission_final_closure_2026_07_16.md:273-286`. Neither blocker reopens claimant identity closure.

## Simplifications, omissions, and blockers

No claimant identity simplification, fallback, placeholder, missing profile, missing name pool, missing portrait, missing sprite, stale crosswalk row, unwired title or description, or lifecycle omission was found.

The two approval-gated global blockers above remain outside this claimant audit. No additional claimant blocker remains.

Final exact open count: **P0: 0, P1: 0, P2: 0**.
