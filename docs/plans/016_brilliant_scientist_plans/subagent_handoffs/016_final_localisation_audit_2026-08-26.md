# Event 016 and DHR final localisation audit

Date: 2026-08-26

Baseline: commit `fbd5f6703a0484733cca205e092e148ae595acd9` (`fix: isolate alien landing registries by country`).

Mode: final read-only localisation audit. No gameplay, localisation, scripted-localisation, GFX, GUI, asset, model, sound, focus, decision, event, achievement, workbook, or shared-helper source was changed. This handoff is the only file created.

> Current Alien Infantry correction after commit `0e724fb8a` (`Wire Meshy alien infantry firearm runtime package`): the accepted V13 provider package and promoted static entity/GFX/animation/sound registrations now exist. The remaining model-runtime blockers are the unsupported muzzle locator, unbound particle/light effects, strict audio selection/acknowledgement/impact/special-role provenance, positional/runtime wiring, and user-owned live acceptance; this localisation audit does not certify those gates.

## Scope and evidence

The audit covered every file under `docs/specs/016_brilliant_scientist_specs/`, the Event 016 localisation prompt and acceptance criteria, current Event 016 and DHR event scripts, both Event 016 focus trees, decisions and missions, project and technology definitions, country and character surfaces, achievements, Event Log and Event Details selectors, Alien Infantry and Event 019 provider 508 presentation, Portal Warfare raid text, model-runtime names, linked GFX and sprite definitions, current asset/model handoffs, and prior Event 016 localisation handoffs.

The localisation rules were checked against the offline `Localisation - Hearts of Iron 4 Wiki.md` page, including its scripted-localisation and dynamic-token sections, the other core offline wiki pages required by `AGENTS.md`, and the installed vanilla `loc_formatter_documentation.md` and `loc_objects_documentation.md` files.

The source scan found 56,463 distinct case-sensitive English localisation keys. It checked 1,013 unique explicit or focus-derived Event 016 references. The 91 apparent misses were GFX return values or AI-plan labels rather than localisation consumers, leaving 922 localisation references resolved. All 346 unique explicit Event 016 event title, description, and option references resolve. Both focus trees are complete at 100 KRG focus nodes and 88 DHR focus nodes, with title and description pairs for every node. All 17 Event 016 achievements have name, description, and condition-tooltip localisation.

## Disposition by severity

### P1: no blocking localisation defect found

No missing key, exact duplicate, broken Event 016 scripted-localisation output, malformed dynamic token, wrong Event 016 namespace, or missing linked sprite texture was found.

The Alien Infantry runtime package remains incomplete for non-localisation reasons. The accepted V13 model, seven action exports, and promoted static `alien_infantry_entity`/GFX/animation/sound registrations now exist, but no supported muzzle locator is available, the particle/light definitions remain unbound, strict audio-role provenance is incomplete, and positional/runtime plus live acceptance remain unproved. This remains a model-runtime blocker and is not a missing-localisation finding.

### P2: DHR revolt tooltip does not describe the ownership branch exactly

Key: `chaosx.nr16.47.a.tt` in `localisation/english/016_dhrondan_contact_l_english.yml`.

Current text: `D’Rhonda takes every marked landing state we still own. Occupied enclaves become D’Rhondan claims.`

Current source in `dhrondan_release_and_transfer_landing_states` transfers a caller-registry state when the pact host still owns it. Every caller-registry state owned by neither the host nor DHR receives a DHR claim, whether it is occupied, annexed, or otherwise lost. `Occupied enclaves` is therefore narrower than the actual ownership test.

Recommended replacement: `D’Rhonda takes every recorded landing state we still own. Recorded landing states owned by another country become D’Rhondan claims.`

Disposition: patch recommended by the owning parent. It was not applied because this assignment is read-only.

### P2: six certain player-facing style defects remain

The following are direct violations of the Event 016 prose contract rather than subjective tone preferences.

- `brilliant_scientist_directorate_gui_sovereignty` in `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml` uses a sentence semicolon. Replace `Kruger's authority and laboratory control set the response; dangerous projects and state capacity determine what follows.` with `Kruger's authority and laboratory control set the response. Dangerous projects and state capacity determine what follows.` Preserve the existing manual GUI line breaks.
- `brilliant_scientist_establish_portal_calibration_network_effect_tt` in `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` uses a sentence semicolon. Split after `committed at once` and retain every cancellation condition and the no-refund consequence.
- `brilliant_scientist_prepare_high_speed_materials_trial_effect_tt` in `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` uses a sentence semicolon. Split after `committed at once` and retain every cancellation condition and the no-refund consequence.
- `brilliant_scientist_achievement_the_one_who_left_tooltip` in `localisation/english/chaosx_achievements_l_english.yml` says Kruger is `atomically` transferred. That is transaction implementation language. Use concrete player wording such as `bring him fully under our authority from another host` without changing the actual trigger.
- `brilliant_scientist_achievement_population_one_tooltip` in `localisation/english/chaosx_achievements_l_english.yml` calls the required clone cycles `bounded growth cycles`. `Bounded` describes the implementation guard rather than the in-world requirement. `controlled growth cycles` preserves the intended meaning more clearly.
- `brilliant_scientist_achievement_yesterday_sent_help_tooltip` in `localisation/english/chaosx_achievements_l_english.yml` calls the action a `bounded intervention`. `one-use intervention` already states the visible limit, so `bounded` should be removed.

No em dash was found in the scoped player-facing files. No additional sentence-semicolon instance was found in the direct Event 016, DHR, Alien Infantry, Portal, Event 019 provider, achievement, or shared GUI scope.

### P3: stale internal country-registry wording

`common/scripted_effects/chaosx_dynamic_effects.md:459` still says `alien_infantry_register_landing_state` owns a `sparse global state-scope registry`. The next output paragraph correctly says it writes the caller country’s registry and that no global cross-provider array exists. The first sentence should say `the caller country's sparse state-scope registry`.

Disposition: documentation correction recommended. It was not patched because `common/scripted_effects/chaosx_dynamic_effects.md` already contains substantial concurrent, unrelated humanitarian-system edits. The Event 016-specific API document and post-commit handoff already state the country-scoped rule correctly.

### P3: safe dynamic-text opportunities

The public landing keys `alien_infantry_landing_category_desc`, `alien_infantry_call_landing_desc`, `alien_infantry_landing_reserve_cost_text`, and `alien_infantry_call_landing_effect_tt` hardcode the accepted values 2,000, 7, 1, 5, 30, 24, 18, and 12. The same values already exist under `constant:alien_infantry_landing.*`, and DHR focus and Event 019 provider text already render those constants with `|0`. These strings are correct today, but using the existing constant tokens would remove a future drift point without changing gameplay.

This is an opportunity, not a current mismatch. The exact keys and values agree with the current constants.

## Required audit lists

### Missing keys

None in the assigned Event 016, DHR, Alien Infantry, Portal, project, technology, decision, mission, focus, Event Log, Event Details, achievement, or model-presentation scope.

### Duplicate keys

None exact and case-sensitive in the English localisation set. `KRG_XENOBIOLOGICAL_ASCENDANCY` and `KRG_xenobiological_ascendancy` are a deliberate country-identity/focus-name pair distinguished by case, not a duplicate. No duplicate Event 016 `defined_text` name was found.

### Scripted-localisation issues

None in the Event 016 definitions. All 157 exact `localization_key` outputs in the direct `016_*.txt` scripted-localisation files resolve to localisation or registered GFX sprites. All 180 `Get*` calls found in the scoped Event 016, DHR, Event 019 provider, Portal, achievement, and shared GUI localisation resolve to a `defined_text` definition.

`GetDhrondanEventDetailClause` still returns `dhrondan_event_detail_clause` only after DHR sovereignty forms and otherwise returns the intentional blank key. The localisation token `[dhrondan_diplomatic_actor.GetNameDef]` correctly omits the `event_target:` prefix.

### Dynamic text opportunities

The four Alien Infantry landing keys listed above can render the existing `alien_infantry_landing` constants. No new variable, helper, or gameplay source is required. Existing DHR focus cooldown values, landing equipment cost, achievement thresholds, Event 019 request and sustainment profiles, actor names, target names, state names, and Event Details clauses already use dynamic tokens appropriately.

### Cross-surface mismatch notes

- The post-commit country-scoped landing registry is mechanically reflected by the possessive `we` in `chaosx.nr16.47.a.tt`, but the tooltip's `Occupied enclaves` clause does not cover every foreign-owner branch. The exact replacement is listed above.
- `common/scripted_effects/chaosx_dynamic_effects.md:459` contradicts the current country-scoped implementation and its own output paragraph.
- The Event Details key remains premise-only and appends the DHR sovereignty clause without exposing counters, probabilities, provider receipts, or registry implementation.
- The catalog alignment handoff dated 2026-08-26 matches the current base Event Details text, conditional DHR clause, four evolutions, and two world-end branches. No workbook change is required by this audit.
- Portal Warfare localisation matches the current two native raids, seven-day preparation, 60 Teleportation Equipment reservation, 10 Command Power cost, six-battalion requirement, formation reconstruction, beachhead result, and one-or-two-installation extraction wording. Its unresolved state-marker lifecycle is a gameplay ownership gap, not a localisation mismatch because no accepted expiry or containment rule exists to describe.
- Event 019 provider 508 names Alien Infantry and the D’Rhondan landing network without restoring Kruger ownership. Provider 509 names Portal Raiders. Their request and sustainment profiles resolve through the current owner-side registry tokens.
- No maintained gameplay, localisation, interface, history, event documentation, achievement documentation, or Event 016 source specification contains a retired guard name, a Kruger-specific Alien Infantry identifier, or a D’Rhondan-specific unit identifier.

### File encoding concerns

None. All 25 scoped English YAML files, including the direct `016_*` files and the shared raid, Event 019, achievement, GUI, and event-name files, begin with the UTF-8 BOM. No scoped key uses `:0`.

### Prose-quality issues

- Vagueness: `Occupied enclaves` is too vague and too narrow for the actual foreign-owner claim branch.
- Bloat: no broad bloat problem was found that justifies a final-audit rewrite.
- Obvious explanation: no title-repeating or button-narrating defect requires a patch in the post-commit DHR registry text.
- Repetition: no new repetition defect was introduced by `fbd5f6703`.
- Overcomplication: `atomically transfers`, `bounded growth cycles`, and `bounded intervention` expose implementation language instead of player-visible actions.
- Style-rule repair: three sentence semicolons remain in scoped Event 016 localisation. No em dash remains.

### Sourced-quotation preservation

All six super-event quotations remain verbatim against `docs/super_events/016_brilliant_scientist/text_research.md`: Vannevar Bush, Niccolò Machiavelli in the recorded Marriott translation, Frederick Douglass, Francis Bacon, Mary Shelley, and Harry S. Truman. This audit made no quotation, attribution, title, punctuation, or button change. The research notes explicitly document excerpt boundaries and normalized terminal punctuation where applicable.

## Asset, sprite, and model-runtime presentation

Fifteen linked Event 016, DHR, Alien Infantry, and Portal GFX files contain 808 texture references. Every referenced texture path exists. Alien Infantry has the three counter sprites and the equipment sprite in `interface/alien_infantry_system.gfx`. Portal Raider has the three counter sprites in `interface/portal_raider_system.gfx`. The linked DHR report/news art, portraits, focus icons, decision/category icons, flags, project icon, technology icons, and tactic icons retain registered source locations.

No localisation alias or fallback was added for the incomplete Alien Infantry runtime. Its promoted static entity and seven action registrations do not close the missing muzzle locator, effect binding, strict audio-role, positional/runtime, or live-acceptance gates. Portal Raider's counter presentation is wired, while its rejected or unwired 3D runtime package remains outside any localisation completion claim.

## MCP evidence and limitations

The post-commit country-registry handoff records a fresh Event `chaosx.nr16.47` state-flow artifact at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc3cd6c47c9f9412410975e6cc452487783d158c2f8098de9474377c3c042d99/7e0ecd2f9a291a10ff69e056a0a9259b89ef049b1156bf6e60d740a1b8236bdf/event-state_flow-f588a2607444.json` and lint artifact at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9963b02624e1fdfb0f9bd4a10ec3db72b1b8db028c641f51e6fa8d6324948e6/5b6f397a1f7a568336c50e3e8c55fcfed407986978ce04e175a1dcd3cd9b1ba9/event-lint-f588a2607444.json`. Both report zero blocking diagnostics at revision `f588a2607444400ec9fa9d102943fc0e10dc4482ebca9935232a4df2966f59d5`.

The latest DHR focus inspection resolved all 88 focus titles and reported no DHR diagnostic: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59f99990f9d8ead0b0f5b094574e2319135bb0fa341e385f59ea133fff9cd751/fca4e2f24b157e1b32d4972454654a72198f57ff006bb2268a5647f1ca2f0720/focus-inspect.5cf1d337bc3cac06.json`.

The latest Alien Predictive Warfare technology trace is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/17a184bf5d347578aa494d48efd59a525015117dc6053426179e8c3367cfc321/bb718b7ffa24e86e50d5263a378fbd0e425741707bbffab6e8aa13dca3a2583e/technology-trace-b2b1e58d15b2.json`. It is partial structural evidence and not a Technology Tree Viewer overflow render. The installed package has no Technology Tree Viewer.

A fresh GUI inspection attempt for the Directorate window and an unfiltered GUI discovery attempt each produced no result before the tool call was terminated after repeated 30-second waits. No new GUI artifact or overflow evidence was available. The installed server also exposes no ordinary decision, decision-category, native raid, achievement, event-popup text-box, or model-entity localisation renderer. Those overflow and live-font-wrap checks remain unresolved and source review is not treated as rendered evidence.

## Meaningful validation

- Re-scanned exact case-sensitive localisation keys and explicit source consumers after `fbd5f6703`: 922 applicable references resolve, with zero missing keys and zero exact duplicate English keys.
- Rechecked 100 KRG and 88 DHR focus title/description pairs, 346 explicit Event 016 event references, 17 achievement name/description pairs and tooltips, 157 direct scripted-localisation outputs, and 180 scoped scripted-localisation calls.
- Compared the country-scoped registry implementation, DHR transfer and claim branches, Event `.47` tooltip, API documentation, and post-commit handoffs. This exposed the one tooltip ownership-wording defect and one stale API-documentation sentence.
- Checked 808 linked texture references across 15 GFX files with zero missing texture paths.
- Checked the maintained source for retired guard names and Kruger-specific Alien Infantry identifiers with zero matches.
- Compared all six super-event quotes with their recorded source-research selections and preserved them unchanged.

## Skipped meaningful validation and why

- No live HOI4 session, in-game popup inspection, or model consumer test was run. Live acceptance belongs to the user.
- Standard decision/category, native raid, achievement, event-popup, and ordinary tooltip overflow cannot be rendered by an applicable installed MCP route.
- Fresh GUI inspection did not return an artifact before termination, so no current Directorate long-text or missing-localisation render is claimed.
- No fresh technology compare was required because `fbd5f6703` changed no technology source. The available technology evidence remains partial.
- No new entity reimport or animation-role validation was attempted because this is a localisation audit; the V13 manifest and promotion handoff provide provider/export evidence, while runtime locator/effect/audio and live acceptance remain outside this audit.

## Changed files and keys

The parent applied the seven certain repairs identified above in a follow-up localisation tranche. The changed player-facing keys are `chaosx.nr16.47.a.tt`, `brilliant_scientist_directorate_gui_sovereignty`, `brilliant_scientist_establish_portal_calibration_network_effect_tt`, `brilliant_scientist_prepare_high_speed_materials_trial_effect_tt`, `brilliant_scientist_achievement_the_one_who_left_tooltip`, `brilliant_scientist_achievement_population_one_tooltip`, and `brilliant_scientist_achievement_yesterday_sent_help_tooltip`.

The D’Rhondan tooltip now covers marked states held by any other power rather than only occupied enclaves. The three sentence-semicolon repairs preserve every cost, cancellation, and no-refund condition. The three achievement repairs remove implementation terms while retaining the exact gameplay requirements.

The dynamic registry wording correction is intentionally kept separate because `common/scripted_effects/chaosx_dynamic_effects.md` has substantial concurrent edits; its current working-tree line is corrected, but it must be committed with the owning documentation tranche rather than sweeping unrelated changes into this localisation commit.

Dynamic localisation added or fixed: none.

Behavior is unchanged; only player-facing wording is clearer and mechanically broader where the DHR claim branch already covered foreign owners.

Dynamic tokens and sourced quotations were preserved without exception. No uncertainty remains about quote wording inside the inspected source. The unresolved uncertainty is visual overflow on consumers not supported by an available renderer.

## Unresolved wording decisions

The four public landing strings can still be converted to existing constant tokens in a future documentation/localisation pass; their current fixed values match the accepted constants and are not a correctness gap.

## Simplifications, omissions, and blockers

No localisation fallback, key alias, broad tone rewrite, quote normalization, hidden-route reveal, or gameplay simplification was introduced.

The audit is actionable but does not certify whole-event completion. Alien Infantry entity/action acceptance, Portal beachhead lifecycle ownership, unsupported overflow rendering, and user-owned live acceptance remain explicit blockers or limitations.
