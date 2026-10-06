# Occupation authority triggers

These triggers define which state controllers can act under an existing national occupation campaign. They preserve the responsible country recorded on each occupation cohort.

`camp_occ_country_counts_as_german_authority` is COUNTRY scope. It accepts Germany and its subjects except special Chaos countries and the sovereign partner list: Hungary, Romania, Bulgaria, Slovakia, Croatia, Vichy France (identified by original tag VIC or active cosmetic tag FRA_VICHY), Italy and Finland. `camp_occ_state_has_german_authority` applies that rule to a state's current controller. German-puppet administrations therefore remain within Germany's occupation authority without becoming responsible countries themselves.

The installed vanilla `common/countries/cosmetic.txt` identifies `ITA_rsi` as a cosmetic identity, not a separate country tag; the authority predicate therefore keeps it within the explicitly excluded ITA partner identity when subject control is checked.

`camp_occ_state_has_japanese_client_authority` accepts Japan and its subjects as controller. China-region campaign eligibility independently excludes Manchukuo and Mengjiang core states, so those pre-war home territories do not enter Japan's China campaign. Pingfang's state-328 institution remains governed by its separate existing setup and role gates.

`camp_occ_state_has_current_authority` uses the recorded responsible country to choose the direct-control, German administration, or Japanese China-client path. The monthly pass and control-change closure call this trigger, so a registered row remains active only while an eligible controller and the original national campaign remain. Registration and exact movement use the same state authority predicates. Germany remains responsible for German rows, deaths and history; Japan remains responsible for Japanese rows.

The item-1 audit requires authority consumers for registration, monthly processing and closure, custody, Kraków setup, Mengele eligibility, the Łódź source and destination, the Hungary destination, Danish rescue and the manual German transfer. The shared checks live in `camp_administration_occupation_triggers.txt`; the national-site consumers live in the paired national trigger modules. The parent integrated the AI Kraków role selection check in `camp_administration_country_effects.txt` with the same state-88 German authority predicate.

Syntax references: installed `documentation/triggers_documentation.md`, `has_cosmetic_tag` lines 3605–3608, `is_controlled_by` lines 5381–5384 and `is_subject_of` lines 6285–6289; offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, `has_cosmetic_tag` line 645, `is_subject_of` line 964 and `is_controlled_by` line 1842. The HOI4 MCP `hoi4.reference_context` request for the decision surface did not return during the bounded request window; direct local sources were used and the MCP route gap is recorded in the task handoff.
