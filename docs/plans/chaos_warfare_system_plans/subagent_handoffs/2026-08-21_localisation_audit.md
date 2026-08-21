# Chaos Warfare localisation and scripted-localisation audit

Date: 2026-08-21

Mode: fresh read-only audit. No localisation, script, GUI, doctrine, event, raid, decision, technology, achievement, spreadsheet, or asset source was changed.

## Authority and scope

The audit used the current worktree as authoritative and applied the accepted package under `docs/specs/chaos_warfare_system_specs/`, including the README, source-of-truth map, numbered specs 01 through 12, all matrices and research files, staged implementation plan, implementation surface map, coding and specialist prompts, and completion checklist. Conflict order was numbered specs, matrices, then specialist prompts. The binding user corrections in the parent prompt were treated as higher authority.

The inspected player-facing surfaces were Chaos Warfare doctrine and subdoctrines, CBRN technologies and special projects, decision categories and decisions, raids, espionage operations, events, scripted localisation, achievements, characters, advisors and theorists, MIOs/designers, facilities, equipment, units, Army Headquarters support and abilities, protection and disease-response ideas, occupation/camp integration, and the Disease Containment and Repression Ledger GUIs. Current source confirms multiple delivery types: strategic and battlefield raids, supply-chain raids and direct decisions, espionage operations, Japan-China decisions, facility recovery raids, and a doomsday decision.

Required offline references consulted included the Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface Modding, Scripted GUI Modding, National focus modding, Technology modding, Doctrine modding, Equipment modding, Division modding, Achievement modding, Character modding, Building modding, and Intelligence agency modding. Installed vanilla documentation and live vanilla precedents were also consulted for doctrines, technologies, raids, decisions and costs, scripted GUIs, characters, equipment, achievements, and localisation formatting.

## Executive result

The English CBRN set is mechanically broad and mostly key-complete, but it is not ready for a completion claim. There are twelve missing scripted-localisation targets, two large stale route families, a direct contradiction of the accepted nerve-suppression design, several descriptions that expose implementation concepts, and widespread overlong requirement/effect text. The biological severity order is mostly stated correctly, but two Smallpox texts incorrectly call it the only severe ordinary agent and an older project description claims permanent contamination and nationwide epidemics. Doctrine text communicates potency, lethality, and Condemnation mitigation well, but it does not communicate increased aggression and wrongly advertises reduced forensic evidence for camp nerve mastery.

## Missing key list

### Confirmed missing scripted-localisation targets

`common/scripted_localisation/camp_repression_ledger_scripted_localisation.txt` references twelve keys that do not exist in the mod English localisation or vanilla English localisation:

- Lines 139, 145, 151, 157, 163, 169: `camp_gui_select_pool_state_1`, `camp_gui_select_pool_state_2`, `camp_gui_select_pool_state_3`, `camp_gui_select_pool_state_4`, `camp_gui_select_pool_state_5`, `camp_gui_select_pool_state_6`.
- Lines 211, 217, 223, 229, 235, 241: `camp_gui_select_site_1`, `camp_gui_select_site_2`, `camp_gui_select_site_3`, `camp_gui_select_site_4`, `camp_gui_select_site_5`, `camp_gui_select_site_6`.

Only the `_tt` variants exist in `localisation/english/camp_repression_rework_l_english.yml:159-164` and `:186-191`. The affected `defined_text` branches therefore have no valid display key when a pool row or active-site row exists.

### Other key coverage

- No missing explicit `title`, `desc`, option `name`, `custom_trigger_tooltip`, `custom_effect_tooltip`, raid target, or other directly assigned localisation key was found in the CBRN event, decision, raid, achievement, character, idea, building, ability, technology, or doctrine sources inspected.
- All 80 CBRN/chemical technology identifiers sampled from the current technology files have name and description keys.
- All 67 characters in `common/characters/cbrn_historical_scientists.txt` and `common/characters/cbrn_historical_specialists.txt` have name and description keys.
- The 11 active Chaos Warfare achievement identifiers all have `_NAME`, `_DESC`, and tooltip coverage. The four rejected achievement concepts named in the completion checklist are absent from both achievement source and this localisation file.

## Duplicate key list

No duplicate English definitions were found for keys defined in the dedicated CBRN/biological files or for repository-wide English keys matching the audited CBRN agent, protection, doctrine, raid, and facility namespaces.

## Namespace and file-format findings

- All inspected English files use `l_english:`. No wrong-language namespace was found.
- All inspected CBRN-facing English localisation files are UTF-8 with BOM. No mojibake marker was found.
- Every key in `localisation/english/cbrn_battlefield_operations_l_english.yml:2-38` has a leading space. Many keys in `localisation/english/cbrn_achievements_l_english.yml:2-35` also have a leading space. The engine may tolerate this, but it violates the repository localisation contract and should be normalized when those files are next patched.
- No `:0` key suffix was found in the audited set.

## Scripted-localisation issue list

1. **Broken camp selector branches.** The twelve missing keys above are used as `localization_key` results, not merely unused placeholders. Add the base keys or point the branches to the existing `_tt` keys after confirming the intended row text.
2. **External strategic-region keys are valid dependencies.** `common/scripted_localisation/biowarfare_disease_containment_region_scripted_localisation.txt:17-259` intentionally references installed strategic-region name tokens. These are supplied by vanilla, including the nonnumeric `STRATEGICREGION_NAMIBIA` at line 172. They are not missing mod keys.
3. **Dynamic state name is source-valid but visually unverified.** `common/scripted_localisation/camp_repression_ledger_scripted_localisation.txt:733` returns `"[?camp_selected_state_id.GetName]"` as a dynamic localisation key. Source inspection found the expected state variable path, but the GUI render route timed out, so the resolved display and overflow remain unverified.
4. **No direct formatting codes in scripted-localisation source.** No direct `§` or `£` characters were found in the audited scripted-localisation files.

## Cross-surface mismatches and stale content

### Critical: accepted camp-only nerve mastery conflicts with an active occupation route

The accepted rule says nerve suppression is mastery of the gas-chambers subdoctrine and requires only that doctrine unlock plus its doctrine-unlocked researched nerve agent. Current camp text partly matches this:

- `localisation/english/chaosx_doctrines_l_english.yml:31-38`, especially `chemical_suppression_zyklon_b_saturation_drills_desc`, `chemical_suppression_nerve_operations_unlocked_tt`, and `chemical_suppression_camp_nerve_methods_unlocked_tt`.
- `localisation/english/camp_repression_rework_l_english.yml:321`, `camp_gui_chemical_method_tt`.

However, a parallel occupation battlefield mechanism remains fully active and fully localized:

- `localisation/english/cbrn_occupation_l_english.yml:2-26`: `cbrn_occupation_measures_category`, `cbrn_authorize_coercive_security*`, `cbrn_nerve_suppression_sarin*`, and `cbrn_nerve_suppression_soman*`.
- `common/decisions/cbrn_occupation_decisions.txt:20-305`: authorization plus separate state-targeted Sarin and Soman preparations.
- `localisation/english/chaosx_technologies_l_english.yml:80-81`: `nerve_agent_suppression_formation*`.
- `localisation/english/chaosx_units_l_english.yml:126-127`: `cbrn_nerve_suppression_detachment*`.
- `common/technologies/cbrn_regimental_support_technologies.txt:183-209` and `common/units/cbrn_regimental_support.txt:685`: separate technology and unit consumers.

This is not a wording-only discrepancy. The owner should retire or formally redesign the occupation route first, then remove or rewrite its localisation. Do not merely hide these strings while the script remains active.

### Critical: doctrine text reduces forensic evidence

The binding correction permits lower Condemnation and political consequences, not reduced evidence. Three doctrine texts promise reduced forensic exposure or evidence generation:

- `localisation/english/chaosx_doctrines_l_english.yml:25`, `SUBDOCTRINE_CHEMICAL_SUPPRESSION_DESC`.
- `localisation/english/chaosx_doctrines_l_english.yml:32`, `chemical_suppression_zyklon_b_saturation_drills_desc`.
- `localisation/english/chaosx_doctrines_l_english.yml:38`, `chemical_suppression_camp_nerve_methods_unlocked_tt`.

The last key dynamically advertises an evidence multiplier while also saying evidence remains recorded. “Recorded” does not cure the contradiction. Align the owning mechanic and text so mastery improves killing efficiency, camp lethality, deployment, and aggression while reducing Condemnation/political consequences only.

### High: doctrine aggression is absent from player-facing text

`GRAND_DOCTRINE_CHAOS_WARFARE_DESC`, the four subdoctrine descriptions, and the theater/terminal spirit tooltips describe potency, contamination, biological growth/spread/deaths, camp killing, preparation, and Condemnation mitigation. None explains the accepted substantial increase to aggression or how aggressive doctrine behavior appears to the player. Add this to the relevant doctrine, spirit, and advisor/theorist text only after the owning behavior is identified.

### High: biological severity wording is partly stale

Correct statements appear in `localisation/english/biological_battlefield_raids_l_english.yml:8-14` and `localisation/english/chaosx_raids_l_english.yml:32-44`: Tularemia is least potent, Anthrax moderate, Plague serious, Smallpox most potent. Shared success odds are correctly separated from post-release potency in `cbrn_designers_l_english.yml:80,87` and biological raid text.

Conflicting or misleading keys:

- `localisation/english/chaosx_decisions_l_english.yml:450`, `smallpox_vaccination_mass_program_desc`, calls Smallpox “the only severe ordinary biological weapon.”
- `localisation/english/chaosx_ideas_l_english.yml:210`, `smallpox_vaccination_program_idea_desc`, repeats the same claim.
- `localisation/english/chaosx_special_projects_l_english.yml:237`, `smallpox_bomb_desc`, calls it the “ultimate strategic bioweapon,” promises nationwide epidemics, and claims permanent contamination until complete vaccination. This does not match the shared lifecycle.
- `localisation/english/chaosx_special_projects_l_english.yml:232`, `tularemia_bomb_desc`, says Tularemia “spares civilian populations.” The lifecycle and delivery surfaces do not guarantee that outcome.

Recommended shared formulation: “Tularemia is least severe, followed by Anthrax, Plague, and Smallpox. Delivery success is resolved separately from agent severity.” Put the full comparison in one shared explanatory surface and keep individual descriptions concrete.

### High: supply-chain duplication creates category and state-card bloat

`common/decisions/biological_sabotage_decisions.txt` defines twelve state-targeted decision variants: four agents multiplied by base, theater, and terminal preparation profiles. One profile per agent is visible at a time, but every valid target state can still produce separate cards. The same delivery family also exists as `common/raids/biological_raids.txt` and `common/raids/biological_sabotage_raids.txt`, with localisation split between `biological_sabotage_l_english.yml` and `biological_sabotage_raids_l_english.yml`.

This conflicts with the “no one-decision-per-state spam” correction and makes two sets of very similar player-facing explanations. Choose the canonical consumer before editing text. Keep historically grounded Japan-China direct decisions, espionage operations, raids, and doomsday as distinct surfaces; consolidate generic supply-chain delivery instead of explaining duplicate routes more fully.

### Medium: HQ naming mismatch

- `localisation/english/cbrn_hq_l_english.yml:4`: `cbrn_hq_intelligence_weather_cell` is “Chemical Intelligence and Weather Cell.”
- `localisation/english/chaosx_doctrines_l_english.yml:70`: `integrated_chemical_operations_operational_recon_grids_tt` unlocks “Intelligence and Weather Cell.”

Use one name everywhere. “CBRN Intelligence and Weather Cell” is the clearest match for a headquarters that can support chemical and biological operations.

### Medium: facilities use generic and implementation-facing descriptions

- `localisation/english/chaosx_buildings_l_english.yml:4`, `biowarfare_facility_desc`.
- `localisation/english/chaosx_buildings_l_english.yml:8`, `cw_facility_desc`.

Both say they are “needed for special ... projects (Chaos Redux).” Remove the mod-name aside and describe their concrete laboratory, containment, filling, testing, and safety functions.

### Confirmed alignments

- Chemical delivery text consistently says idle units and ordinary air missions do not release agents and that accepted releases use one shared consequence/exposure path. The phrases are mechanically correct even where the word “pipeline” should be rewritten.
- Biological delivery is not described as all raids or all decisions. The current set includes raids, Japan-China direct decisions, espionage operations, generic direct sabotage decisions, facility recovery, and doomsday. The problem is duplication and card volume, not lack of delivery variety.
- `common/scripted_triggers/camp_repression_rework_triggers.txt:14-16` excludes special Chaos countries, and both Repression Ledger scripted GUI visibility blocks call that eligibility trigger. No localisation claims that special Chaos countries participate.
- Decision category source uses relevance gates and `visible_when_empty = no` for the inspected CBRN categories. No category-localisation key explicitly promises game-start visibility.

## Dynamic text opportunities

1. **HQ abilities:** `localisation/english/cbrn_hq_l_english.yml:16-48`, keys `CBRN_PREPARE_CHEMICAL_OFFENSIVE_*`, `CBRN_THEATER_PROTECTIVE_POSTURE_*`, `CBRN_DECONTAMINATION_CORRIDOR_*`, `CBRN_SEAL_OPERATIONAL_AREA_*`, `CBRN_MASS_ANTIDOTE_RESPONSE_*`, `CBRN_SEAL_INFECTION_CORRIDOR_*`, and `CBRN_COMBINED_OVERMATCH_*`, hardcode command costs, durations, manpower, medical capacity, modifiers, and cooldowns. Replace these values with the existing constants or scripted values so localisation cannot drift from the force-band dispatcher.
2. **Japan biological campaign:** `localisation/english/japan_biological_campaign_l_english.yml:13-24`, all `japan_bio_campaign_anthrax_*` and `japan_bio_campaign_plague_*` requirement, cost, and effect keys hardcode every cost and refund. Use constants and icon-first cost strings.
3. **Generic biological sabotage:** `localisation/english/biological_sabotage_l_english.yml:13-24`, all four agent requirement and begin keys hardcode payload, support-equipment, and command costs. The source already uses constants.
4. **Facility recovery:** `localisation/english/biological_facility_recovery_raids_l_english.yml:14-17` hardcodes five-equipment reserve packages. Use the facility-capture constants.
5. **Achievement thresholds:** `localisation/english/cbrn_achievements_l_english.yml` spells out counts, percentages, and ninety days. Where the achievement UI supports scripted values, use the achievement constants; otherwise record these strings in the same tuning checklist as the achievement triggers.
6. **Current selected actor/agent:** preserve existing `[FROM.GetName]`, state, agent, reserve, timer, and constant tokens. The audit found no reason to replace them with static names.

## Prose-quality issue list

### Vagueness and implementation vocabulary

- `localisation/english/cbrn_doctrine_l_english.yml:6-7`, `cbrn_convene_institutional_review_desc` and `_effect_tt`: “reconcile ... records,” “verified native doctrine,” “bounded establishment review,” and “exact proof” describe implementation state rather than an in-world staff review.
- `localisation/english/cbrn_battlefield_operations_l_english.yml:3,17,37-38`: “exact-state battlefield operation,” “shared exposure pipeline,” “recorded operation,” and “condition receipt” should become concrete target, weather, payload, and consequence language. This whole file is attached to the currently stale ground-operation route and should not be polished until route ownership is resolved.
- `localisation/english/cbrn_diplomacy_l_english.yml:22,24`: `cbrn_share_forensic_evidence_requirements_tt` and `_complete_tt` expose successor/proxy inheritance rules and exact record mechanics. Lead with the publishable evidence and political consequence.
- `localisation/english/biological_facility_recovery_raids_l_english.yml:13,34-44,50,56`: “exact facility ledger,” “hazard schedule,” “ordinary biological lifecycle/response,” “safety monitor,” and “sole active arsenal” read as save-state documentation.
- `localisation/english/biological_sabotage_raids_l_english.yml:3,52`: “same native delivery odds” should be “the same chance of successful delivery.”
- `localisation/english/biological_battlefield_raids_l_english.yml:18`: “one-day final release assembly” exposes a tuning stage. State the preparation time only if the raid UI does not already show it.
- `localisation/english/cbrn_protection_l_english.yml:23,50,89,94,108`: repeated “ledger,” “eligible states,” and processing-order explanations obscure what stock will be issued and who receives it.
- `localisation/english/cbrn_chemical_delivery_l_english.yml:31,35,39,43`: “exact raid-reservation archetype” is database language. Describe the prepared payload and eligible agents.
- `localisation/english/chaosx_ideas_l_english.yml:191,197,203`: “exact-state treatment courses” should identify distribution to an affected state.

### Bloat and overcomplication

- `localisation/english/cbrn_hq_l_english.yml:16-48`: each ability repeats costs in the description, requirements in a trigger tooltip, then duration, modifiers, cooldown, and caveats in an effect tooltip. Keep the description to purpose, the trigger tooltip to the first blocking requirement plus the cost display, and the effect tooltip to duration and material consequence.
- `localisation/english/cbrn_occupation_l_english.yml:22-26`: Sarin and Soman requirements are long noun-stack inventories and effect tooltips mix forecasts, mechanics, doctrine, evidence, and aftermath. This route is stale under the accepted design.
- `localisation/english/biological_battlefield_raids_l_english.yml:4-5,17-30` and `biological_facility_recovery_raids_l_english.yml:4-17,34-41`: category, availability, launch, actor-result, and target-result keys repeatedly explain the same prerequisites and lifecycle.
- `localisation/english/cbrn_doctrine_l_english.yml:102,105` and `chaosx_doctrines_l_english.yml:71-73`: the multiline doctrine and spirit tooltips are accurate tables but too long for ordinary hover reading. Group chemical harm, biological harm, command recovery, preparation, and Condemnation into short labelled lines, with one consequence-preservation sentence.
- `localisation/english/cbrn_achievements_l_english.yml:25-26`, `chaos_warfare_terminal_contagion_DESC` and tooltip, are overloaded condition lists. The description should state the fantasy; the tooltip should use short requirement lines.

### Obvious explanation and repetition

- `localisation/english/biological_facility_recovery_raids_l_english.yml:45,48,51,54,57`: all five options begin “Acknowledge the ...”. Use short reactions that add tone or consequence, such as securing the perimeter, warning medical commands, or preserving records.
- `localisation/english/biowarfare_disease_containment_l_english.yml:77-88`, GUI open/refresh/close labels and tooltips, repeatedly narrate the visible button action. Keep only non-obvious persistence or refresh consequences.
- `localisation/english/camp_repression_rework_l_english.yml:23,28,116,119`: open, close, and refresh tooltips narrate obvious UI behavior and repeatedly mention returning to the decisions overview.
- `localisation/english/cbrn_achievements_l_english.yml`: every achievement has both a sentence description and a near-duplicate prose tooltip. Convert tooltips to concise criteria rather than restating the description.

### Style-rule repairs

- Sentence semicolons occur in `localisation/english/biowarfare_disease_containment_l_english.yml:110`, key `disease_containment.gui.selected.black_plague_crisis_seal.tt`, and were found in the audited CBRN-facing set in `cbrn_designers_l_english.yml:60` and several CBRN protection completion tooltips. Replace with full stops or conjunctions.
- `localisation/english/cbrn_chemical_delivery_l_english.yml:52`, `cbrn_first_chemical_shock_idea_desc`, ends with “This short national penalty represents the first adaptation cycle.” That is visible mechanic commentary. Delete it after the concrete reports, drills, and warning changes.
- `localisation/english/cbrn_doctrine_l_english.yml:120,122,124,126`, the four generic advisor descriptions, end with “No historical individual is implied.” This is authorial/legal commentary. Describe the office only.
- `localisation/english/cbrn_doctrine_l_english.yml:126` adds “It remains distinct from weaponized-zombie command,” an implementation boundary unrelated to the advisor’s role. Remove it unless a visible selection conflict genuinely requires clarification.
- `localisation/english/biowarfare_disease_containment_l_english.yml:74`, `disease_containment.gui.header.summary.tt`, explains that the board avoids a separate category. This is UI architecture history, not player guidance.
- `localisation/english/chaosx_special_projects_l_english.yml:308,311` uses a spaced hyphen and inflated phrases such as “most dangerous ... ever conceived” and “most stringent ... ever used.” Replace with concrete Smallpox containment risk and the actual research/safety tradeoff.

## Decision visibility and concise-tooltip findings

- The category sources themselves are relevance-gated: `cbrn_operations_category`, `cbrn_program_management_category`, `cbrn_civil_defence_category`, `cbrn_occupation_measures_category`, `cbrn_international_response_category`, `chaosx_disease_containment_category`, and the Japan campaign categories all use scripted relevance or war/route conditions plus `visible_when_empty = no` where appropriate.
- The CBRN text nevertheless spends too many words proving that categories, ordinary air activity, or state records are bounded. Rewrite these as player consequences, not architecture guarantees.
- Cost strings in `japan_biological_campaign_l_english.yml:16-21` and `cbrn_doctrine_l_english.yml:31` are not consistently icon-first and duplicate the same numbers in adjacent tooltips. Use icons and values in the cost line, then reserve the tooltip for timing, refund, loss-on-failure, or target consequences.
- The stale occupation nerve decisions and generic biological sabotage decisions are the main one-card-per-state risk. Localisation cannot solve that structural bloat.

## Advisors and theorists

- Historical scientist and specialist name/description coverage is complete for the two CBRN character files.
- `localisation/english/chaosx_characters_l_english.yml:220-250` gives chemical, biological, weaponization, program-director, toxicological, and resistance-sabotage traits concrete dynamic bonuses. The potency/death and Condemnation language follows the accepted asymmetry, and evidence/attribution are explicitly unchanged.
- These keys still omit the accepted doctrine-driven increase in aggression. If aggression is an AI behavior rather than a direct character modifier, explain it in doctrine text rather than falsely assigning it to every advisor.
- The four generic high-command advisors in `cbrn_doctrine_l_english.yml:119-126` are mechanically clear but contain visible authorial disclaimers, as noted above.

## Facilities, units, HQ, and support

- Facility names exist, but the two facility descriptions are generic and contain the mod name.
- CBRN support unit and HQ descriptions generally identify equipment, purpose, and release boundaries clearly.
- `localisation/english/chaosx_units_l_english.yml:32-85` repeats “increases international condemnation when used” for every Livens and chemical-tank agent variant. Put this once in the parent category or shared delivery tooltip.
- `localisation/english/chaosx_units_l_english.yml:126-127` and `chaosx_technologies_l_english.yml:80-81` are stale because the separate nerve-suppression formation conflicts with camp-only mastery.
- `localisation/english/cbrn_hq_l_english.yml:15-50` is complete but numerically duplicated and too long, as detailed above.

## Raids, espionage, direct decisions, and doomsday

- Strategic biological raids, battlefield raids, facility recovery raids, supply-chain raids, espionage operations, Japan-China direct decisions, and doomsday all have distinct localisation families.
- `localisation/english/biological_sabotage_raids_l_english.yml:3` correctly separates delivery success from severity but uses technical wording.
- `localisation/english/chaosx_operations_l_english.yml` gives each espionage operation a concrete target and consequence. No missing operation key was found.
- `localisation/english/japan_biological_campaign_l_english.yml` is historically situated and state-specific, but its requirements and effects are static, repetitive, and cost-heavy.
- Doomsday remains a decision and its localisation is present. No text claims that all biological delivery occurs through decisions or raids.

## Achievements

- Key coverage matches all 11 active achievement definitions.
- `chaos_warfare_achievement_eligible_tooltip` uses vague phrases “ordinary Chaos Warfare campaign” and “real CBRN decisions.” Replace with the actual eligibility rule or omit it if the engine already communicates eligibility.
- `chaos_warfare_evidence_survives_tooltip` uses “exact biological facility capture,” which should become “captured biological facility.”
- `chaos_warfare_terminal_contagion_DESC` is a tooltip-sized checklist rather than an achievement description.
- Leading spaces before many keys should be removed in the eventual patch.

## Sourced-quotation preservation notes

No attributed or sourced quotation was found in the inspected CBRN-facing localisation. Historical character descriptions and research-backed event prose are paraphrases, not quoted passages. Therefore no quotation punctuation or wording is authorized for preservation as verbatim text. Historical factual claims were not rewritten in this audit.

## MCP inspection and rendering evidence

The installed HOI4 MCP routes were invoked as required, but the server did not return inspect or render artifacts:

- `hoi4.tech_inspect`, folder discovery: accepted and ran for roughly two minutes, then returned no structured result.
- `hoi4.tech_inspect`, trace for `anthrax_bomb_delivery_systems`: timed out after 180 seconds.
- `hoi4.gui_inspect`, `disease_containment_window` with scenario `{ id = "default" }`: timed out after 180 seconds.
- `hoi4.event_inspect`, trace for `cbrn_bio_facility.2`: timed out after 180 seconds.

Because inspect did not complete, dependent `hoi4.tech_render`, `hoi4.gui_render`, and `hoi4.event_render` calls could not be used responsibly. There are no useful artifact URIs. Overflow, resolved dynamic text, event presentation, and doctrine/technology render coverage remain unverified. The Technology Tree Viewer named in the subagent instructions is absent from the installed package, so it supplied no independent visual evidence. No CBRN national-focus or map-definition surface was identified in the accepted package, so focus and map routes were not applicable. Source-only findings above are not presented as engine-render evidence.

## Recommended correction order

1. Resolve the design conflict in `common/decisions/cbrn_occupation_decisions.txt`, `common/technologies/cbrn_regimental_support_technologies.txt`, and `common/units/cbrn_regimental_support.txt`. Then remove or rewrite the stale `cbrn_occupation_*`, `nerve_agent_suppression_formation*`, and `cbrn_nerve_suppression_detachment*` keys.
2. Align camp nerve mastery mechanics and `chaosx_doctrines_l_english.yml:25,32,38` with the rule that doctrine reduces Condemnation/political consequences only, not evidence.
3. Choose one generic supply-chain consumer and retire the duplicate state-card family. Keep the distinct historical decisions, espionage operations, raids, and doomsday surface.
4. Add the twelve missing camp selector keys or redirect the scripted-localisation branches to intentional existing keys.
5. Repair biological severity text in `chaosx_decisions_l_english.yml:450`, `chaosx_ideas_l_english.yml:210`, and `chaosx_special_projects_l_english.yml:232,237`.
6. Convert hardcoded HQ, Japan campaign, sabotage, facility recovery, and achievement values to existing dynamic constants where supported.
7. Perform a bounded prose pass over the exact keys listed in this report, prioritizing implementation vocabulary, repeated requirements, obvious button narration, and the stale authorial disclaimers.
8. Re-run MCP technology, GUI, and event inspect/render after the server route is available, specifically checking long doctrine tooltips, Disease Containment filters and state rows, Repression Ledger pool/site rows, and event option overflow.

## Uncertainty and blocked validation

- Visual overflow and missing-localisation rendering are blocked by the MCP timeouts above.
- The current worktree changed substantially during this read-only audit due to concurrent agents. Findings cite the source state read during this audit and no unrelated change was reverted or incorporated deliberately.
- No gameplay source was changed, so no behavior claim in this report should be interpreted as a patch result.
- No plan addendum was written because design-gap ownership already exists in the accepted Chaos Warfare package; this audit report is the requested handoff.
