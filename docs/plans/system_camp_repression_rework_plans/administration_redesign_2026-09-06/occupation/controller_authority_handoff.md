# Occupation controller authority handoff

Disposition: implemented within the assigned source boundary; awaiting parent integration and review.

Acceptance basis: latest Camps audit r3 items 1 and 3 and `accepted_implementation.md`. Scope was limited to authority triggers and consumers in the assigned occupation and administration trigger/effect modules, paired documentation, and this source suite. I did not edit shared decision or event definitions, the GUI, spreadsheet, campaign dates or agent decision log. No commit was created.

## Changes

- `common/scripted_triggers/camp_administration_occupation_triggers.txt` adds one COUNTRY-scope German authority predicate and STATE-scope German/Japanese authority predicates. The German rule accepts GER or its subjects except special Chaos countries and HUN, ROM, BUL, SLO, CRO, VIC, cosmetic FRA_VICHY, ITA and FIN. The Japanese rule accepts JAP or JAP subjects for eligible China-region states, with MAN and MEN cores excluded from that geography. Existing Pingfang eligibility is unchanged.
- `common/scripted_effects/camp_administration_occupation_effects.txt` enrolls German rows under GER and Japanese China rows under JAP; routes both responsible-country arrays into their existing eligible-state and monthly pulse registries; makes current-authority checks preserve open rows when the controller becomes an eligible subject; updates exact movement destination authority and removes the redundant direct-controller check from the Łódź source.
- `common/scripted_triggers/camp_administration_triggers.txt` accepts German-subject control for German custody sites.
- `common/scripted_triggers/camp_administration_country_triggers.txt` uses German authority for state 88 Kraków setup and the Mengele historical gate.
- The paired occupation trigger and effect documentation describes responsibility, Japanese core exclusions, syntax references and the remaining AI consumer dependency.
- `occupation/test_controller_authority.py` covers the German authority list, Vichy cosmetics versus ordinary FRA identity, special Chaos exclusion, state-88 GEN, RKO/POL subjects, post-registration handover, movement and Łódź gates, RNG/state-613 pattern, captured MAN-controlled Chinese state, MAN/MEN core exclusions, third-country subjects and unchanged Pingfang state 328 gates.

The vanilla `common/countries/cosmetic.txt` line 929 defines `ITA_rsi` as a cosmetic identity. No separate RSI country tag was found in vanilla country tags or country definitions, so the exact accepted ITA partner exclusion remains in force. The vanilla German Generalgouvernement decision is at `common/decisions/GER.txt` lines 6141 and 6218 and transfers states to GEN; this confirms the state-88 handover case.

## Evidence and checks

`python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/test_controller_authority.py` passes all five tests. These are production-source assertions plus small scenario models; they are not engine execution evidence.

Installed documentation: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`: `has_cosmetic_tag` lines 3605–3608, `is_controlled_by` lines 5381–5384, `is_subject_of` lines 6285–6289. The installed files identify HOI4 1.17.0 in `common/defines/00_defines.lua` line 7.

Offline wiki: `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`: `has_cosmetic_tag` line 645, `is_subject_of` line 964, `is_controlled_by` line 1842. The local wiki snapshot does not expose a source revision in the file; the repository was at HEAD `984798e530a268221aad388756906e9956dfb76b` when the change began.

The required HOI4 reference MCP tools were exposed. A bounded `hoi4.reference_context` call for the decision/controller surface did not return within roughly one minute and was terminated; no revision-bound MCP citations were produced. `hoi4_probability_compare` was not exposed in this session, so the comparison remains unperformed and must be recorded as a route failure by the parent if it remains unavailable.

## Parent integration

The parent was notified that source edits are ready and has begun its own integration. The parent updated the separate AI Kraków role condition in `common/scripted_effects/camp_administration_country_effects.txt` to accept German authority when GEN holds state 88. The parent also owns the partner route additions to occupation source/close gates, decision/event integration and the agent decision log. Review those shared files after parent integration; the source suite may need to extend its candidate/route assertions.

Remaining limits: no live-game run was performed. Consequently state-array dispatch, subject-controller relationship semantics at runtime, closure and population movement still need the user's game validation. No campaign dates were modified.
