# Event 014 Final Localisation Audit

## Scope and result

This pass audited Event 014 player-facing text and scripted-localisation consumers across events, decisions and missions, focus trees, the Event 014 GUI, countries and leaders, ideas, irregular units, achievements, scenarios, the Events Log and Event Details, evolutions, super-events, and super-event audio metadata.

The audit found one release-blocking hidden-identity leak: fourteen always-loaded tips named Hannibal Lecter, Bedelia Du Maurier, or their actors before `cannibalism_reveal_complete` could exist. Those attributed quotations were removed from the live loading-tip pool and replaced with original spoiler-free gameplay guidance. No ancient-general disclaimer was added. The revealed identity remains Hannibal Lecter.

Three in-scope prose repairs split overloaded contrast or semicolon constructions without changing mechanics or dynamic tokens. No missing key, duplicate key, encoding, or broken scripted-localisation defect remains in the audited Event 014 surfaces.

## Changed files

- `localisation/english/014_cannibalism_l_english.yml`
- `localisation/english/loading_tips_l_english.yml`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_localisation_final_audit.md`

The Event 014 localisation file already contained concurrent irregular-unit and paid-guard text changes when this pass began. This pass preserved them. The only keys changed here in that file are listed below.

## Changed keys

- `cannibalism_raise_bone_guard_effect_tt`: replaced the sentence semicolon with two direct sentences.
- `chaosx.nr14.60.d`: separated the guarded-reception and military-seal consequences so each option is immediately legible.
- `cannibalism_warlord_raise_the_bone_guard_tt`: replaced the sentence semicolon with two direct sentences.
- `LOADING_TIP_0`, `LOADING_TIP_1`, `LOADING_TIP_2`, `LOADING_TIP_4`, `LOADING_TIP_5`, `LOADING_TIP_6`, `LOADING_TIP_7`, `LOADING_TIP_8`, `LOADING_TIP_9`, `LOADING_TIP_10`, `LOADING_TIP_11`, `LOADING_TIP_13`, `LOADING_TIP_14`, and `LOADING_TIP_15`: replaced ungated character quotations and actor attributions with original spoiler-free gameplay guidance.

## Before and after

Before this pass, global loading tips could identify Hannibal Lecter and Bedelia Du Maurier from the loading screen before Event 014 fired. Several tips also exposed actor names, which contradicted the package's in-world presentation. After this pass, the loading-tip file contains no match for `Hannibal`, `Bedelia`, `Mads Mikkelsen`, or `Gillian Anderson`.

Before this pass, two guard tooltips joined separate consequences with sentence semicolons, and event `chaosx.nr14.60.d` buried two distinct policy outcomes in one staged comparison. After this pass, the consequences are separate direct sentences. All existing state, source-name, route-label, cost, and formation tokens were preserved.

## Missing key list

None.

The explicit key-consumer pass covered 379 `title`, `desc`, `name`, `custom_effect_tooltip`, `custom_trigger_tooltip`, `localization_key`, and GUI `text` references. The only initially unmatched tokens were `defined_text` selector names or GUI element identifiers rather than localisation keys. All 204 actual Event 014 focuses have title and description keys. All 127 Event 014 decisions and missions, 13 decision categories, 37 ideas, and 9 custom irregular sub-units have their required names and descriptions.

## Duplicate key list

None. The final cross-file English localisation scan found zero duplicate Event 014, CBL, CWG, WGO, or Event 014 super-event keys.

## Scripted-localisation issue list

No broken public scripted-localisation branch was found.

- The pre-reveal Event Details body uses `chaosx.events_log.window.event_details.cannibalism.pre_reveal`.
- Revealed Event Details content is selected only after `cannibalism_reveal_complete`.
- Every inspected evolution-stage-three title and body selector requires both the Event 014 evolution type/stage and `cannibalism_reveal_complete`.
- The spread-source and spread-route selectors have no generic fallback, but every public consumer is gated by the active inbound-spread state and the durable source/route values saved by the Event 014 effect path. No unsafe public lookup was found.
- Target and status selectors used by decisions and the GUI retain their existing neutral fallbacks.

## Hidden-identity audit

The final source audit found no pre-reveal player-facing Hannibal exposure in Event 014 events, decisions, focuses, GUI headers, countries or leaders, ideas, units, achievements, scenarios, Events Log entries, Event Details, or evolutions.

- Event Details has an explicit pre-reveal branch and a revealed fallback guarded by `cannibalism_reveal_complete`.
- Evolution stage III title/body selectors are guarded by `cannibalism_reveal_complete` in current, historical-detail, event-detail, and selected-evolution getters.
- Hannibal-bearing decisions and relevant event continuations are reveal-gated.
- Super-event 49, 50, 52, and 53 text is post-reveal or post-outcome content.
- Scenario type labels remain neutral: Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, and Convergence.
- Hidden achievement names that reveal Hannibal or route outcomes remain staged behind reveal or route flags.
- The global loading-tip bypass was removed in this patch.

No Carthaginian, ancient-general, Hannibal Barca, or similar disclaimer was added. After the reveal, text continues to identify the character as Hannibal Lecter.

## Dynamic text opportunities

No new dynamic localisation was needed. Existing current-value, state, country, route, cost, and timer tokens were preserved.

Six cost displays remain an owner-level presentation issue because they expose five simultaneous spendable resource types. The decisions-and-missions skill sets a hard display budget of four spendable types. Localisation cannot remove one without concealing a real scripted cost, so no misleading text-only change was made:

- `cannibalism_logistics_cost_land`
- `cannibalism_logistics_cost_island`
- `cannibalism_joint_suppression_cost_text`
- `cannibalism_convergence_interdiction_cost_text`
- `cannibalism_island_landing_cost_text`
- `cannibalism_aftermath_institution_cost_text`

Recommended owner fix: reduce or consolidate each underlying cost contract to four spendable resource types, then keep these icon-first dynamic strings aligned with the script.

## Cross-surface mismatch notes

- Fixed: global loading tips contradicted the reveal boundary and used actor-likeness attribution while the event, GUI, achievements, and Event Details correctly concealed the identity.
- Unresolved: the six five-resource decision cost displays exceed the established decision UI budget. They accurately mirror current costs, so this is a gameplay/presentation contract issue rather than a missing-localisation issue.
- No contradiction was found between Event 014 scenario labels, Events Log/evolution wording, Event Details wording, achievement staging, super-event outcome text, or audio-slot metadata.
- Super-event audio IDs 49, 50, 52, and 53 are assigned by Event 014 effects, registered in `sound/chaosx_sound.asset`, and listed with matching runtime WAV paths in `music/chaosx_music_track_list.html` and `docs/super_events/014_cannibalism/audio_research.md`.

## File encoding concerns

None after patch. Every English localisation file containing an audited Event 014 key has a UTF-8 BOM. The two changed localisation files retain their BOM. No leading-space key or `:0` form was found in the consolidated Event 014 localisation file.

## Prose-quality findings and repairs

### Vagueness

No unresolved vague player-facing passage was found in the bounded final pass. Event and decision text states concrete actors, targets, costs, or consequences.

### Bloat

`chaosx.nr14.60.d` previously packed two distinct response outcomes into one compound sentence. The revised text gives each outcome one sentence while retaining the necessary source, route, and state context.

### Obvious explanation

No tooltip was changed solely to restate its title or button action. The replacement loading tips provide system guidance rather than narrating obvious controls.

### Repetition

The loading-tip pool contained a duplicated Hannibal quotation. All ungated Event 014 character quotations were removed from that surface, eliminating the duplication and the spoiler together.

### Overcomplication

The two guard tooltips used sentence semicolons to join contract sequencing clauses. They now state the initial contracts and later Bone Guard return in separate sentences.

### Style-rule repair

The changed Event 014 prose contains no sentence em dash, sentence semicolon, implementation-history language, actor attribution, or staged ancient-general disclaimer. Existing dynamic tokens and formatting codes remain intact.

## Sourced-quotation preservation notes

The four Event 014 super-event quotations remain unchanged and attributed:

- `chaosx_super_event.49.q`: Thomas Hobbes, *Leviathan*.
- `chaosx_super_event.50.q`: William Shakespeare, *King Lear*.
- `chaosx_super_event.52.q`: Walt Whitman, *Specimen Days*.
- `chaosx_super_event.53.q`: Lord Byron, *Darkness*.

Retained non-Event-014 loading-tip quotations at `LOADING_TIP_3`, `LOADING_TIP_12`, and `LOADING_TIP_17` were not edited. The semicolon in the Henry Adams quotation at `LOADING_TIP_17` remains because attributed quotations must not be normalized.

Exception: fourteen Hannibal/Bedelia loading-tip quotations were removed from the live loading-tip surface rather than rewritten. Their wording was not altered or reused. Removal was necessary because the engine presents loading tips globally and offers no Event 014 reveal gate at that surface.

## MCP evidence

Fresh focus inspection resolved every title in all three Event 014 trees:

- Unified tree, 108 focuses: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0680eff17d2a008bbc4fe8efc1f3513666e282f3399d4b526a300c81b3c6f7b6/62a0eb58f777895b7eef4e28c80fd8df09eaf9d9e032cd59d69e1543ebb13ae6/focus-inspect.1b9d867a468a8e6e.json`
- Warlord tree, 68 focuses: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b85e004dfd5dc7e3dc006b464eb116b1a69fecd5b6d4a860ffd75e0919b3756/938a2eb66c45d10f6f52c548069cd1ec9d0d3d5c02a931d61c5ffa9d271711b5/focus-inspect.1b9d867a468a8e6e.json`
- Wendigo tree, 28 focuses: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/071ca5933d350071bb145c07ca80a7046efdfd6ff251407b8f1ae281e205a1cb/f747d49d5e494ca15643d894482e1a771dd8c56b0c08540024394739f9b29fe4/focus-inspect.1b9d867a468a8e6e.json`

The only focus localisation warning was vanilla `continuous_restrict_freedom_desc`, outside Event 014.

Fresh Event 014 namespace inspection returned partial graph evidence with no blocking diagnostic. Workspace helper and lifecycle passes were deferred because the graph exceeded the bounded inspection size: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f3269efa0cf1b5cf5ce62f7910ec78c35c3454b984a55c8374c3f93d3e249862/0fa3a37c9ff11408ba382cdf54bd9ccc814c82d7e97d0be87aca082fcb3a192f/event-lint-2be037dcc948.json`.

Fresh early-header GUI inspection completed: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8864a6442e120f611785c630ba23f890fbeda70d0e54796e514872e644f8c11/d99a1a7befdaddff58b074ae075bd060b4ebadf65cc3ca02b4171db9aa7763a4/gui-inspect.e87d866fe71bc127.json`. Its global validation failure comes from unrelated Event 003/005 repository collisions and truncation, not the selected Event 014 window.

Existing post-change Event 014 visual evidence remains useful for the five staged windows:

- Early render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9eb6bc5791159e6125ba7a184e10f9021687d72827ca32cece5d2744a56c95ec/afa6c9317c3c6b3bfd3d7c8393bdf0e9e6529f573ca0b0ec73e8c077988ca3c6/cannibalism_early_header_window-full.svg`
- Network render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1400f648d294b965b9c40181909726c5a642a648fe3dcb1764cdca5664a28ffe/43fd118011a3c1b6fc4bda7d8e1a908abee45a8dd96b74c21d7318bce8b3a79a/cannibalism_network_window-full.svg`
- Warlord render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/581c72f83874a3c384e29c3617e893b5231674452fc03e64420bfb8b69810806/8012f62f9f517151eef2abf4ce0d01cee91072e02978d6ef23c105550b1d9b29/cannibalism_warlord_command_window-full.svg`
- Revealed render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bbf0fb6a06f20032a4a7648c16c82af4f4b9f50ac4b7d310978151bc2e329bed/c694367243f895825c984b446149d07229957c46324ee053024473748ece5079/cannibalism_revealed_command_window-full.svg`
- Wendigo render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d8017f0e3782340b2d90c1153bf9fc22f8c903e6d92b49c8b240263299157800/9b42fdc0220aa1595b46d17586aceb71e2dbfc79fa6c9a457b2f27f537927897/cannibalism_wendigo_command_window-full.svg`

## Meaningful validation

- Final duplicate scan: zero Event 014-related duplicate English keys.
- Final encoding scan: zero Event 014-related English files without a UTF-8 BOM.
- Final loading-tip spoiler scan: zero matches for Hannibal, Bedelia, Mads Mikkelsen, or Gillian Anderson.
- Coverage audit: 204 focus title/description pairs, 127 decision/mission pairs, 13 category pairs, 37 idea pairs, and 9 irregular-unit pairs are present.
- Focus MCP inspection resolved 108 unified, 68 warlord, and 28 Wendigo focus titles.
- Audio metadata inspection matched super-event slots 49, 50, 52, and 53 across effect assignment, sound registration, track-list metadata, and audio research.
- Diff review confirmed that the four Event 014 super-event quote keys and retained non-Event-014 loading-tip quotations were untouched.

## Skipped or blocked meaningful validation

- Fresh Event 014 event rendering timed out after 180 seconds. The namespace inspect artifact is partial and source review is not claimed as equivalent to a complete render.
- Fresh five-state GUI rendering at 1920x1080 across normal, long-text, and missing-localisation states did not finish and was terminated after several minutes. Existing post-change staged-window artifacts are recorded above, but they do not replace a fresh post-patch render. The patch did not change GUI-bound layout strings.
- The installed package has no Technology Tree Viewer. Event 014 defines no dedicated technology or doctrine localisation surface in this pass, so no technology render could be produced.
- HOI4 was not launched. Live consumer validation belongs to the user.

## Unresolved wording or owner decisions

- Decide whether to simplify the six five-resource decision costs to the four-type presentation budget. Localisation currently reports the real costs accurately.
- No unresolved Event 014 identity wording remains. The revealed name is Hannibal Lecter.

## Recommended fixes

- Decision owner: simplify or consolidate the underlying costs behind the six keys listed under Dynamic text opportunities, then update those same keys to match.
- GUI owner: rerun the five staged Event 014 renders when the renderer can complete, using normal, long-text, and missing-localisation states.

## Simplifications, omissions, and blockers

No localisation fallback or wording simplification was used. The two MCP timeouts and unavailable Technology Tree Viewer are the only validation blockers. The five-resource cost contract remains unresolved and is reported explicitly rather than concealed.
