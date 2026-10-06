# Camp achievement repair handoff

Disposition: implemented in the assigned source scope. Acceptance basis: the accepted implementation contract and the parent task routing the latest camps audit round 3 item 2. Source edits are evidence of implementation, not a new design decision.

## Changes

- `common/scripted_effects/camp_administration_civil_effects.txt`: `camp_administration_civil_finish_review` now sets `camp_rework_uk_raj_review_complete` for ENG. Its USA branch sets `camp_rework_achievement_usa_redress_before_victory` only when `has_war = yes`, while retaining the normal court-review completion flag for peace reviews. The claims programme eligibility still starts after `1948.7.1` in the existing trigger and monthly payment path.
- `common/achievements/chaos_redux_achievements.txt`: achievement 68 now requires `camp_admin_civil_review_complete` and `camp_rework_italy_desert_camps_closed` in place of the retired conventional road and garrison flags. Its no-active-sites, controlled Libyan core state infrastructure threshold, and stationed division requirements remain intact.
- `localisation/english/chaosx_achievements_l_english.yml`: descriptions and tooltips for 65, 66, and 68 now state the reachable civil review paths. Achievement 66 names ending relocation authority, finishing the court review during the war, and then settling property claims. Achievement 68 retains the developed Libyan state and stationed Italian division requirements in its wording.
- `common/scripted_effects/camp_administration_civil_effects.md`: the helper map now records ENG and wartime USA achievement tracking.
- `camp_achievement_source_tests.py`: added an executable source-contract suite under this plan folder.

## Source suite and verification

Ran `python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/camp_achievement_source_tests.py` successfully. It executes the parsed finish-review effect for ENG, USA at war, USA at peace, and ITA, verifies the finish readiness and paid-month gate, checks that Italy's achievement still requires its developed Libyan state and stationed division, confirms the two retired flags are absent from achievement 68, and asserts the 1 July 1948 claims date remains.

No other camp achievement blocks were changed. Localisation remained UTF-8 with BOM. HOI4 was not launched; runtime achievement evaluation remains for the user's live game.

## Setter trace for achievements 60 to 69

- 60, `Inherit the Ledger, Close the Ledger`: `camp_rework_achievement_inherited_dormant_legacy` and `camp_rework_achievement_large_inherited_network` are set by `common/scripted_effects/genocide_crisis_effects.txt:220,231`; `camp_rework_achievement_inherited_network_dismantled` and `_during_war` are set in `common/scripted_effects/camp_repression_rework_effects.txt:4425-4428` and `4488-4491`. `camp_rework_reformed_legacy` is set by review completion in `camp_administration_civil_effects.txt:188` and multiple cleanup routes. Severe-discovery and tribunal disqualifiers are set in `genocide_crisis_effects.txt:912`, `camp_repression_rework_effects.txt:1111`, and `genocide_crisis_effects.txt:743` for `camp_rework_achievement_severe_discovery_reached`, `camp_rework_achievement_severe_tribunal_reached`, and `genocide_condemnation_tribunal_threshold` respectively.
- 61, `Papers for the Liberated`: `camp_rework_achievement_severe_sites_documented` is set in `genocide_crisis_effects.txt:1321`; `camp_rework_achievement_operated_radicalized_site` is set by responsible-country scope in `camp_repression_rework_effects.txt:771`.
- 62, `The Doctor Loses His War`: the four checked flags are set in `germany_mengele_effects.txt:1676,1969,2060` (`germany_mengele_program_authorized`, coup fired, and defeat) and `camp_repression_major_country_effects.txt:1212` (`germany_auschwitz_complex_dismantled`).
- 63, `No Pingfang Shadow`: `camp_rework_achievement_japan_internal_exposure` and `camp_rework_achievement_ishii_removed` are set in `camp_repression_major_country_effects.txt:1747,1780`; `japan_prisoner_experiments_shutdown` is set in `camp_administration_country_effects.txt:598` or `camp_repression_major_country_effects.txt:1839`; `camp_rework_achievement_major_outbreak_occurred` is set in `camp_repression_major_country_effects.txt:1404` as the disqualifier.
- 64, `Grain Before Fear`: `soviet_collapse_crisis_desk_disbanded` is set in `common/decisions/005_soviet_collapse_decisions.txt:4909`; `sov_famine_critical_fired` is set in `camp_repression_major_country_effects.txt:2098` as the disqualifier.
- 65, `Dominion Without Chains`: the civil review now sets `camp_rework_uk_raj_review_complete` in `camp_administration_civil_effects.txt:189`; the shared review path sets `camp_rework_reformed_legacy` at line 188. The colonial revolt disqualifier `camp_rework_achievement_uk_colonial_revolt_occurred` is set in `camp_repression_colonial_country_effects.txt:323`.
- 66, `Redress Before Victory`: the civil review now sets `camp_rework_achievement_usa_redress_before_victory` inside its wartime branch at `camp_administration_civil_effects.txt:199`. Authority termination remains set in civil effects at lines 174 and 223, and in legacy country effects at `camp_repression_colonial_country_effects.txt:2438`; redress completion remains set by the civil claims path at line 289 and legacy route at line 2467.
- 67, `Congo Reformed`: civil review sets `camp_rework_belgium_concessions_reformed` at `camp_administration_civil_effects.txt:206`; `camp_rework_reformed_legacy` is set at line 188. The `camp_rework_crisis_exposed` disqualifier has several setters in `camp_repression_colonial_country_effects.txt`, including lines 320, 342, 372, 389, 424, 1842, 1879, 1883, 1906, 1910, 2405, and 2446.
- 68, `Roads Without Camps`: civil review completion and Italian camp closure are set in `camp_administration_civil_effects.txt:187,205`; the achievement retains state development, control, no-active-site, and stationed-division checks in `common/achievements/chaos_redux_achievements.txt`.
- 69, `Gurs Closed`: the civil review sets `camp_rework_france_legacy_closed` in `camp_administration_civil_effects.txt:204` and the shared `camp_rework_reformed_legacy` at line 188. `camp_rework_achievement_severe_tribunal_reached` is set in `camp_repression_rework_effects.txt:1111` as the disqualifier.

## Reference evidence and route gap

The offline wiki snapshot describes achievement `possible` and `happened` behavior and trigger evaluation in `paradox_wiki/Achievement modding - Hearts of Iron 4 Wiki.md:34-42`; country-flag trigger use is documented at `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:643-669`; conditional `if`/`else_if` effect behavior is described at `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:4456-4492`; and boolean flag-setting syntax is at `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:897-921`.

The installed documentation confirms the `has_country_flag` country-scope trigger at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:3624-3636` and the country-scope `set_country_flag` effect at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:6730-6737`.

The MCP service exposed `hoi4.reference_context` and `hoi4.reference_search`, but bounded reference-context calls did not return within roughly 90 seconds and were terminated. I used the exact offline wiki and installed-game documentation files directly as the repository fallback; no MCP revision metadata was available.

## Exact owned patches for shared files

`common/achievements/chaos_redux_achievements.txt` changes only the camp 68 condition hunk:

```diff
-            has_country_flag = camp_rework_italy_desert_camps_closed
-            has_country_flag = camp_rework_achievement_italy_conventional_infrastructure_complete
-            has_country_flag = camp_rework_achievement_italy_conventional_garrison_used
+            has_country_flag = camp_admin_civil_review_complete
+            has_country_flag = camp_rework_italy_desert_camps_closed
```

`localisation/english/chaosx_achievements_l_english.yml` changes only these six lines:

```diff
-000_chaos_redux_65_dominion_without_chains_DESC: "As the United Kingdom, avoid a Raj revolt while completing the postwar review and dismantling the detention network."
+000_chaos_redux_65_dominion_without_chains_DESC: "As the United Kingdom, complete the civil review, close every active site, and keep the Raj loyal without a colonial revolt."
-camp_repression_achievement_dominion_without_chains_tooltip: "As the §YUnited Kingdom§!, keep the Raj loyal without a colonial revolt, complete the Raj review, and close every active site."
+camp_repression_achievement_dominion_without_chains_tooltip: "As the §YUnited Kingdom§!, complete the civil review, close every active site, and keep the Raj loyal without a colonial revolt."
-000_chaos_redux_66_redress_before_victory_DESC: "As the United States, terminate relocation authority and complete redress while the war is still being fought."
+000_chaos_redux_66_redress_before_victory_DESC: "As the United States, end relocation authority and finish the court review while the war is still being fought, then settle the property claims."
-camp_repression_achievement_redress_before_victory_tooltip: "As the §YUnited States§!, terminate relocation authority and complete the redress commission before the war ends."
+camp_repression_achievement_redress_before_victory_tooltip: "As the §YUnited States§!, end relocation authority and finish the court review while the war is still being fought, then settle the property claims."
-000_chaos_redux_68_roads_without_camps_DESC: "As Italy, retain Libya after replacing desert camps with conventional infrastructure and garrison security."
+000_chaos_redux_68_roads_without_camps_DESC: "As Italy, complete the civil review, close every desert camp, and retain a developed Libyan state with an Italian division stationed there."
-camp_repression_achievement_roads_without_camps_tooltip: "As §YItaly§!, complete the desert road works and establish the transport guard, close every camp, then retain a developed Libyan state with an Italian division stationed there."
+camp_repression_achievement_roads_without_camps_tooltip: "As §YItaly§!, complete the civil review, close every desert camp, and retain a developed Libyan state with an Italian division stationed there."
```

Both shared files contain other agents' worktree hunks, so the parent should stage only these owned ranges together with the camp effect, its paired documentation, this source suite, and this handoff.
## Remaining scope

The parent owns the decision log update, final shared-tree review, and isolated commit. No unresolved implementation gaps remain in this delegated repair. The user owns live-game validation.
