# Event 016 native selection localisation review

Disposition: implemented owner wording fixes and getter field correction; rendered evidence remains unassessed.
Acceptance basis: the parent's follow-up explicitly reports applying the prose fixes and approves the new presentation getter and branch keys.
The bounded source review covers all current 24 localisation values, the getter, and their current source requirements.
Only this handoff was edited by the localisation worker.
No gameplay, localisation, spreadsheet, model, public GUI, or identifier changes were made by this worker.
No MCP calls, game launch, or commit were performed.
The parent owns source edits, final MCP evidence, spreadsheet reconciliation when applicable, and the commit.

## Applied prose fixes

Disposition: implemented.

- Vagueness: Cloning now names project availability or completed history.
Flying Bomb names the exact Experimental Rockets requirement.
Jet Engine uses the applicable DLC technology branch and preserves the completed-project alternative.
- Bloat and repetition: the Rocketry sentence "Its result will carry the programme forward" is removed.
All three selection descriptions state the programme, chosen source, free commitment, facility research, and adoption of a completed project in two sentences.
- Obvious explanation: the descriptions convey actual consequences instead of repeating the title and promising generic programme advancement.
- Overcomplication: the getter presents one applicable aircraft research branch rather than both DLC branches.
- Requirement and style repair: withdrawal says the project is not being researched, covering both never-started and stopped research, and includes the matching funded-stage restriction.
- Cross-action feedback: the existing blocked tooltip now describes an action instead of incorrectly describing withdrawal as confirmation of a commitment.

The six titles remain clear and unchanged.
All three withdrawal requirements match the current source.
The selected-result tooltip directs the player to begin or resume native facility research and does not claim the decision has begun research.
The adopted-result tooltip preserves existing research and rewards and does not promise replay.
The earlier optional adopted-result rewrite is superseded by acceptance of the retained accurate text.
The released-result tooltip retains progress and explicitly denies a research-cost refund.
There are no remaining prose decisions requiring a rewrite in these 24 values.
The neutral blocked feedback does not identify one exact failed predicate, but the requirement tooltip supplies the conditions.
No hidden-route spoilers, update-history wording, em dashes, sentence semicolons, unsupported icons, or resource-label cost fallback were found.

## Exact requirements and dynamic tokens

The Jet Engine tooltip calls [This.GetMengeleNativeJetRequirements].
Its getter tests By Blood Alone first and always = yes last.
The offline wiki specifies first matching text selection.
The predicate order therefore selects BBA when installed and the legacy branch otherwise.
The getter contains no flag, formatting character, temporary variable, research start, or payment effect.

With BBA, the intended display is "Complete Engines II and either Improved Small Airframe or Improved Medium Airframe."
That exactly describes engines_2 AND (improved_small_airframe OR improved_medium_airframe).

Without BBA, the intended display is "Complete Fighter II or Tactical Bomber II research."
That exactly describes fighter2 OR tactical_bomber2.
The equipment-name substitutions are generic labels for those technology unlocks, not changed research predicates.

The enclosing Jet Engine requirement retains Rocketry Theory, an empty paid Rocketry receipt, no Flying Bomb commitment, and the alternative of an already completed exact Jet Engine project.
The completed-history alternative bypasses the technology requirements as the core allows.
It does not require both researched prerequisites and completed native history.

Flying Bomb's $experimental_rockets$ resolves to Experimental Rockets and matches its non-completed technology predicate.
Cloning's availability-or-completion requirement matches the existing private availability flags or completed exact source.
Provider ownership remains hidden.

Directly verified installed source locations:

- localisation\english\plane_designer_l_english.yml:458: engines_2 = Engines II.
Lines 390 and 408 alias improved_small_airframe and improved_medium_airframe to small_plane_airframe_2 and medium_plane_airframe_2.
Lines 230 and 310 resolve those aliases to Improved Small Airframe and Improved Medium Airframe.
- localisation\english\equip_air_l_english.yml:46,81: fighter_equipment_2 = Fighter II and tac_bomber_equipment_2 = Tactical Bomber II.
- common\technologies\air_techs.txt:296-306,1572-1586: fighter2 enables fighter_equipment_2 and tactical_bomber2 enables tac_bomber_equipment_2.
The blocks also contain Jet Engine project unlock tooltips.
SHA-256: b9cbd21b2dbfa819b07d435f3557b037420f8885a7d0ec8c221c1a78015b941d.
- localisation\english\research_l_english.yml:466: experimental_rockets = Experimental Rockets.

Installed paths above are relative to C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV.

## Scripted localisation finding

Disposition: implemented.
Acceptance basis: the parent reports correcting both getter fields and requests verification.
The final source read confirms localization_key in both text blocks at lines 9 and 13.
The output keys, getter name, branch order, predicates, and localisation tokens remain unchanged.
The spelling matches the offline wiki and the actual defined_text fields in the installed vanilla source cited below.
The earlier field-spelling finding is resolved.
This is source validation and does not certify runtime output or rendered fit.

Field and branch-order evidence:

- paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md:656-689, particularly 681 and 683, specifies localization_key and first matching branch selection.
SHA-256: 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064.
- Installed common\scripted_localisation\00_scripted_localisation_SPR_loc.txt:1-27, particularly lines 8, 18,25, documents and uses localization_key.
SHA-256: 0997ce02f60303f6d23278da44aa3c6f52e420458a11b3f6fa566099a2f742f9.

## Final gameplay-source alignment

The current core selection predicates allow an already selected exact source when that exact project is completed.
They preserve Theory, empty paid family receipt, unsettled Prototype, and opposite Rocketry commitment restrictions.
The presentation wrappers mirror selected-or-completed behavior.

The core release predicates require matching selection, an empty matching paid receipt, and the exact project not being researched.
The release effect checks that gate immediately before retirement and matching selection removal.

Cloning's source is fixed to sp_brilliant_scientist_cloning.
Rocketry commitments are mutually exclusive alternatives sp_rockets_flying_bomb and sp_air_jet_engine.
All six decision costs reference zero and contain no research timer.
Selection authorizes a source and does not prove native research start or payment.

Completed exact-source selection enters adoption rather than the fresh native output wrapper.
The core does not restart native research or replay native completion rewards.
The adapter separately invokes the existing Cloning operational-package grant on successful adoption, so adoption must not be described as having no Directorate effects.

Withdrawal clears matching commitment, retains native progress, and invokes no native cancellation or refund.
Result codes remain selected 1, fresh settlement 2, adopted settlement 3, released 4, blocked 5, and none 0.
The adapter presents selection, adoption, withdrawal, and blocked results.
Fresh settlement belongs to native output callbacks and does not need a decision feedback branch.

All visible and available decision helper calls remain under hidden_trigger.
Availability has custom requirement text.
No owner flags need new localisation on this surface.

## Required localisation audit results

- Missing key list: none among the six titles, six descriptions, six requirement references, four result references, two getter output keys, and six installed text substitutions.
- Duplicate key list: none in the assigned 24-value file.
The original 22 keys were searched for duplicates during the first pass.
The new getter name and two output-key definitions were searched in their owning folders during this follow-up.
- Namespace issue list: none found in the assigned set.
- Scripted localisation issue list: none remaining on the assigned surface; both getter fields are corrected.
- Dynamic localisation added by owner: [This.GetMengeleNativeJetRequirements], $experimental_rockets$, $engines_2$, $improved_small_airframe$, $improved_medium_airframe$, $fighter_equipment_2$, $tac_bomber_equipment_2$.
Airframe nested alias targets resolve to installed values.
- Dynamic text opportunities: the previously requested technology names and DLC branch selection are implemented at the presentation level; the getter field finding is resolved.
No additional timer, cost quote, actor, or state display is required.
- Cross-surface mismatch notes: the earlier blocked-selection\withdrawal wording mismatch is resolved.
Displayed technology branches match the core.
Workbook alignment is unassessed because no catalog source or export was read or edited.
- Encoding concerns: no assigned-localisation concern.
The previous handoff had damaged smart-quote and line-span punctuation from shell transport, which this rewrite repairs with plain ASCII punctuation.
- Sourced quotation preservation: no sourced or attributed quotation occurs on this surface.
- Dynamic token preservation: the worker changed no source token and records final source values verbatim below.
- Recommended fixes: none remaining from the bounded source audit.
No additional prose rewrite is required.

## Meaningful validation and remaining limits

Final reads checked all 24 values, the getter, its output keys, nested aliases, both DLC branches against the core, and legacy technology-to-equipment mappings.
Documented field-name comparison identified the getter finding rather than treating the existence of output keys as proof of a functional getter.
Selected-completed adoption and empty-receipt inactive-exact-project withdrawal remain present in the core.

This is source-only evidence.
Rendered wrapping, overflow, clipping, native tooltip fit, runtime getter output, native clicks, MCP service health, and standalone Technology Tree Viewer availability remain unassessed.
MCP calls and game launch are explicitly forbidden for this worker.
The parent owns final MCP\render evidence and must retain those limits in the final review.
No source-only review is presented as equivalent to rendering or engine execution.
No gameplay simplification was made by this worker.
No model or public GUI was added.
The owner's new getter and two output keys have explicit approval in the follow-up task.

## Final wording for spreadsheet alignment

Disposition: current source wording.
The spreadsheet owner should mirror these exact keys and values only where catalog fields actually reflect these controls, after the parent resolves any getter defect.
No catalog mismatch was established because workbook contents were outside scope.
The list below supersedes the earlier proposals and contains no unresolved technology-name placeholder.

```yaml
mengele_event016_native_select_cloning: "Choose the Cloning Prototype"
mengele_event016_native_select_cloning_desc: "Commit the Directorate's Cloning programme to the Cloning special project at no cost. Research proceeds at its facility, or a completed project supplies the Prototype."
mengele_event016_native_select_flying_bomb: "Choose the Flying Bomb Prototype"
mengele_event016_native_select_flying_bomb_desc: "Commit the Directorate's Rocketry programme to the Flying Bomb special project at no cost. Research proceeds at its facility, or a completed project supplies the Prototype."
mengele_event016_native_select_jet_engine: "Choose the Jet Engine Prototype"
mengele_event016_native_select_jet_engine_desc: "Commit the Directorate's Rocketry programme to the Jet Engine special project at no cost. Research proceeds at its facility, or a completed project supplies the Prototype."
mengele_event016_native_release_cloning: "Withdraw the Cloning Commitment"
mengele_event016_native_release_cloning_desc: "Withdraw the Cloning commitment while its project is not being researched and no Cloning stage is being funded. Project progress is retained and research costs are not refunded."
mengele_event016_native_release_flying_bomb: "Withdraw the Flying Bomb Commitment"
mengele_event016_native_release_flying_bomb_desc: "Withdraw the Flying Bomb commitment while its project is not being researched and no Rocketry stage is being funded. Project progress is retained and research costs are not refunded."
mengele_event016_native_release_jet_engine: "Withdraw the Jet Engine Commitment"
mengele_event016_native_release_jet_engine_desc: "Withdraw the Jet Engine commitment while its project is not being researched and no Rocketry stage is being funded. Project progress is retained and research costs are not refunded."
mengele_event016_native_select_cloning_requirements_tt: "Cloning Theory is complete and no Cloning stage is being funded. The Cloning special project is available or has already been completed."
mengele_event016_native_select_flying_bomb_requirements_tt: "Rocketry Theory is complete, no Rocketry stage is being funded, and no Jet Engine commitment is active. $experimental_rockets$ research is complete or the Flying Bomb project has already been completed."
mengele_event016_native_select_jet_engine_requirements_tt: "Rocketry Theory is complete, no Rocketry stage is being funded, and no Flying Bomb commitment is active. [This.GetMengeleNativeJetRequirements] Alternatively, the Jet Engine project has already been completed."
mengele_event016_native_release_cloning_requirements_tt: "The Cloning project is selected and is not being researched. No Cloning stage is being funded."
mengele_event016_native_release_flying_bomb_requirements_tt: "The Flying Bomb project is selected and is not being researched. No Rocketry stage is being funded."
mengele_event016_native_release_jet_engine_requirements_tt: "The Jet Engine project is selected and is not being researched. No Rocketry stage is being funded."
mengele_event016_native_selection_committed_tt: "This project is the Directorate's selected Prototype route. Begin or resume research at the appropriate special-project facility."
mengele_event016_native_selection_adopted_tt: "The completed project is recorded as the Directorate's Prototype. Existing research and project rewards are retained."
mengele_event016_native_selection_released_tt: "The Directorate withdraws its commitment to this Prototype route. Progress remains with the project and no research costs are returned."
mengele_event016_native_selection_blocked_tt: "The project's current status prevents this action. Check its selection requirements or, for withdrawal, stop its research and finish any funded stage in the programme."
mengele_event016_native_jet_requirements_bba: "Complete $engines_2$ and either $improved_small_airframe$ or $improved_medium_airframe$."
mengele_event016_native_jet_requirements_legacy: "Complete $fighter_equipment_2$ or $tac_bomber_equipment_2$ research."
```

## Guidance and additional local evidence

Applied AGENTS.md and the events, decisions-missions, and subagents repo skills.
No skill was modified.
Reference routes were not called because the task forbids MCP calls.

- paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md:61-91: key syntax, omitted version number, encoding, values.
SHA-256: 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064.
- paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:83-109,268-302: visibility, availability, immediate effects, costs.
SHA-256: 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162.
- Installed documentation\triggers_documentation.md:2431-2458,2482-2488,5103-5144: custom tooltip override, compatibility alias, hidden triggers.
SHA-256: 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29.
- Installed documentation\effects_documentation.md:3320-3340: custom effect tooltips.
SHA-256: 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af.
- Installed common\decisions\HUN.txt:2251-2270: custom requirement tooltip wrapping native decision conditions.

## Final source snapshot

Read at UTC 2026-10-03T11:52:08.222000+00:00.

- localisation\english\016_mengele_native_prototype_selection_l_english.yml: SHA-256 c484d8f30ac17aff2d358ee17943a00edc886a3ea46a0441fe6fea1a0641d906.
- common\scripted_localisation\016_mengele_native_selection_text.txt: SHA-256 a9f15c83584de930e14961fa6ec84c105d3f3cce447aacb95a1ebf36de94772d.
- common\decisions\016_mengele_native_prototype_selection_decisions.txt: SHA-256 9c49ffea996dfe5faa06e03e34b2676bf1bd314ad2eb5510a498936498384669.
- common\scripted_effects\016_mengele_native_selection_decision_effects.txt: SHA-256 ac950026a27264a2617d84eedd6e65f9956da4d1d6b66347cc274ee78aff1fa4.
- common\scripted_triggers\016_mengele_native_selection_decision_triggers.txt: SHA-256 f3aa2d778f847166e36f39a245a04799fe1e31c7818ceab91825f0d9932989d1.
- common\scripted_triggers\016_mengele_native_prototype_triggers.txt: SHA-256 6316a57859bdbf65914d8d11ec935d908d5a3e7b43b7c7a7a350a66441c19982.
- common\script_constants\016_mengele_native_prototype_constants.txt: SHA-256 175e6281d9c6c4fb86f5e0ef5d8a677965c11e28bfa4a3ad10ceb7b3238116c4.
- common\scripted_effects\016_mengele_native_prototype_effects.txt: SHA-256 f3ebe41d73c86160313119d5fef8a135c670a34569da715d718194c4bacc13d9.

Getter correction verified at UTC 2026-10-03T11:54:22.388614+00:00.
