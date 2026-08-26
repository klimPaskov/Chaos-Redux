# Event 016 final localisation audit

Date: 2026-08-26

Baseline: committed Event 016 state through `18f7c7d67` (`docs: attest directorate gui and localize dhrondan outcomes`). The later repository HEAD commits inspected after that point do not change Event 016 localisation.

Mode: read-only final localisation audit. No gameplay, localisation, scripted-localisation, GUI, GFX, asset, focus, decision, event, workbook, or shared-helper source was changed. This evidence handoff is the only file written. It does not claim Event 016 completion.

## Authority and scope

The audit used `AGENTS.md`, the offline Paradox wiki localisation and scripted-localisation guidance, the other core wiki pages required by `AGENTS.md`, the installed vanilla `loc_formatter_documentation.md` and `loc_objects_documentation.md`, and the event, event-asset, decision/GUI, focus-tree, and subagent skills.

The source comparison covered the accepted Event 016 specification package, the D’Rhondan addendum, current Event 016 and DHR localisation, direct scripted localisation, Event Log and Event Details selectors, the Kruger and DHR focus trees, Directorate GUI bindings and controls, Event 016 and DHR decisions and events, the Alien Infantry landing API, Event 019 alien-family presentation, the DHR survival clause, linked asset and GFX paths, the catalog-alignment handoff, and prior localisation handoffs.

## Disposition

No blocking localisation-key defect was found. The current direct `016*_l_english.yml` set contains 20 UTF-8-BOM files, 3,204 exact case-sensitive keys, and zero exact duplicate keys. No direct Event 016 file uses a `:0` key suffix. The prior full consumer scan at the immediately preceding Event 016 baseline resolved 922 applicable explicit references, including all 346 visible event references, all 100 KRG and 88 DHR focus title/description pairs, all 17 achievement pairs and tooltips, 157 direct scripted-localisation outputs, and 180 scoped `Get*` calls. Commit `18f7c7d67` changes only two already-resolved localisation values and introduces no key or token rename.

Four KRG focus-effect tooltips remain mechanically vague or expose implementation language. They should be rewritten by the focus/localisation owner before a final player-facing acceptance claim.

## Required audit lists

### Missing keys

None found in the current direct Event 016, DHR, Alien Infantry, Event Log, Event Details, focus, event, decision, mission, achievement, or Directorate GUI localisation surface.

### Duplicate keys

None exact and case-sensitive among the 3,204 direct Event 016 keys. `KRG_XENOBIOLOGICAL_ASCENDANCY` in `localisation/english/016_brilliant_scientist_country_l_english.yml:68` and `KRG_xenobiological_ascendancy` in `localisation/english/016_brilliant_scientist_focus_l_english.yml:87` differ by case and serve country-identity and focus-name consumers respectively. They are not an exact duplicate, although case-insensitive audit scripts will report them as a collision.

### Scripted-localisation issues

None found in the inspected Event 016 selectors.

- `GetDhrondanEventDetailClause` in `common/scripted_localisation/016_dhrondan_country_scripted_localisation.txt:9` returns `dhrondan_event_detail_clause` only after `dhrondan_sovereignty_formed` and otherwise returns the intentional blank key at line 14.
- `chaosx.events_log.window.event_details.brilliant_scientist` in `localisation/english/016_brilliant_scientist_evolutions_l_english.yml:12` appends `[GetDhrondanEventDetailClause]` without exposing state-transfer mechanics.
- The Event Log evolution selector in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:752-753` maps Event 016 to `brilliant_scientist.evolution.type`. The localisation surface defines exactly Evolutions I through IV at `016_brilliant_scientist_evolutions_l_english.yml:4-11`. No Evolution V text was found.
- Country and state tokens retain valid localisation namespaces, including `[dhrondan_diplomatic_actor.GetNameDef]` and `[brilliant_scientist_primary_facility.GetName]` without an invalid `event_target:` prefix.

### Dynamic text opportunities

No current correctness gap was found. The four Alien Infantry landing strings that previously hardcoded reservation, timer, Presence, Strain, and cooldown values now render `constant:alien_infantry_landing.*` tokens with integer formatting in `localisation/english/016_alien_infantry_api_l_english.yml:3-10`.

The Event Details DHR clause, landing costs, rebellion gates and percentages, focus cooldown reductions, actor names, recipient names, facility state names, project names, and visible Directorate values already use existing dynamic tokens. No new variable or scripted-localisation helper is recommended by this pass.

### Cross-surface mismatch notes

- The DHR transfer tooltip changed in `18f7c7d67`. `chaosx.nr16.47.a.tt` at `localisation/english/016_dhrondan_contact_l_english.yml:75` now says that D’Rhonda takes marked states still owned by the pact host, while states held by another power remain with that power and receive D’Rhondan claims. This matches the ownership branch described by the current handoffs and removes the earlier ambiguous `we still own` wording.
- The Directorate authority summary changed in `18f7c7d67`. `brilliant_scientist_directorate_gui_sovereignty` at `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml:61` preserves the manual line breaks and now uses `establish the response`, avoiding the repeated `set` wording without changing the GUI binding.
- The Event Details key remains premise-only. The workbook alignment handoff records the same base wording, the conditional DHR clause, exactly four evolutions, a blank Evolution V cell, two Event 016 world-end branches, and blank cluster fields. No Event 016 cluster membership or cluster localisation was found.
- The Event 019 alien-family presentation continues to identify Alien Infantry and the D’Rhondan landing network without restoring Kruger ownership of the unit family.
- The Alien Infantry API uses the exact current landing constants rather than stale fixed numbers.

### File encoding concerns

None. All 20 direct `016*_l_english.yml` files begin with UTF-8 BOM bytes `EF BB BF`. No direct file contains a versioned `:0` key.

### Prose-quality issues

#### Vagueness and implementation-facing language

1. `KRG_recall_the_defector_officers_effect_tt` in `localisation/english/016_brilliant_scientist_focus_l_english.yml:128` says `Adds bounded army experience and mandates an origin-sensitive officer amnesty or purge proceeding.` The source effect grants `constant:brilliant_scientist_focus.defector_officer_army_experience` and sets an unlock flag at `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1098-1101`. `bounded army experience`, `mandates`, and `proceeding` do not state the visible amount or concrete outcome. Recommended direction: render the existing experience constant and say that an origin-specific officer amnesty or purge becomes available.
2. `KRG_link_the_depot_network_effect_tt` at `016_brilliant_scientist_focus_l_english.yml:248` says `Mandates bounded terminal transit and supply links between at least two verified terminals.` The focus sets the terminal-transit and supply-link unlock flags at `016_brilliant_scientist_kruger_state_focus.txt:1898-1901`. Recommended direction: state that controlled terminals can exchange units or supplies through the unlocked network, using the exact implemented consumer behavior. `mandates bounded` is an implementation label, not a player consequence.
3. `KRG_arm_the_alien_cohorts_effect_tt` at `016_brilliant_scientist_focus_l_english.yml:284` says `Reconciles the alien-infantry project record and authorizes bounded Alien Laser Weapon production for D’Rhondan landings.` The focus rebuilds the project-force runtime package and sets the production unlock at `016_brilliant_scientist_kruger_state_focus.txt:2212-2215`. `Reconciles the ... record` exposes bookkeeping, and `bounded production` does not state the limit. Recommended direction: say which Alien Laser Weapon production or landing action becomes available and surface any existing cap dynamically.
4. `KRG_found_the_foreign_intelligence_bureau_effect_tt` at `016_brilliant_scientist_focus_l_english.yml:296` says `Creates an agency when the relevant expansion is active and none exists, then adds Diplomatic Training when available. Mandates bounded foreign operations.` The focus calls `brilliant_scientist_focus_found_foreign_intelligence_agency` and unlocks foreign intelligence operations at `016_brilliant_scientist_kruger_state_focus.txt:2310-2313`. `relevant expansion`, `when available`, and `bounded operations` expose compatibility gating. Recommended direction: describe the agency, Diplomatic Training, and the newly available foreign operations in ordinary player terms while leaving unavailable engine/DLC branches silent.

#### Bloat and overflow risk

No broad prose rewrite is justified, but three source strings remain high-risk for consumer overflow and need live or supported render confirmation rather than source acceptance alone:

- `alien_infantry_call_landing_effect_tt` at `localisation/english/016_alien_infantry_api_l_english.yml:10` is 795 source characters. Its line breaks and dynamic constants are useful, but the standard decision tooltip has no installed MCP renderer.
- `dhrondan_rebellion_pulse_mission_desc` at `localisation/english/016_dhrondan_contact_l_english.yml:32` is 1,040 source characters and carries four probability tiers. It is mechanically clear but cannot be certified for mission-description fit from source alone.
- `brilliant_scientist_origin_investigation_category_desc` at `localisation/english/016_brilliant_scientist_achievements_l_english.yml:3` is 537 source characters. It includes two live counters and a premise paragraph, but no achievement/category overflow renderer is installed.

Long physical YAML lines are required by HOI4 localisation syntax and are not themselves a defect. The concern is painted consumer fit.

#### Obvious explanation, repetition, and overcomplication

No remaining title-repeating or option-narrating defect was found in the two values changed by `18f7c7d67`. The four KRG focus tooltips above are the remaining concrete overcomplication findings. No em dash or sentence semicolon was found in the 20 direct Event 016 files or the shared Event 016 achievement localisation.

### Sourced-quotation preservation

All six Event 016 super-event quotations remain unchanged in `localisation/english/016_brilliant_scientist_super_events_l_english.yml:3-24`: Vannevar Bush, Niccolò Machiavelli in the recorded translation, Frederick Douglass, Francis Bacon, Mary Shelley, and Harry S. Truman. No quotation, attribution, punctuation, excerpt boundary, title, or button text was edited. No sourced quotation appears on the inspected DHR landing or Directorate GUI surface.

## GUI controls and display evidence

The active event-owned scripted GUI remains `brilliant_scientist_directorate_scripted_gui`, attached to `brilliant_scientist_directorate_category`, with root window `kruger_directorate_container`. Source inspection confirms one presentation-only open control, one presentation-only close control, Kruger profile presentation, and exactly four visible values: Mandate, Dependence, Exposure, and Project Capacity. Independent Capacity and Grievance remain hidden. The dormant tab/project/facility/foreign/sovereignty localisation keys are not bound to active elements in the compact GUI and therefore do not create live controls.

A fresh `hoi4.gui_inspect` call for `kruger_directorate_container` succeeded with `GUI_INSPECTED` and retained this artifact:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6cac330b25a225514680b84a755e1f335798457f9c0fabf00b6deb5d9924248/95cce70629c29af0d729e69691a7634bd495b94da3a38d83561f63839ba58e52/gui-inspect.017d249c791c0735.json`

The fresh render request covered 1280x720 and 1920x1080 at UI scale 1 with `normal`, `long-text`, and `missing-localisation` states. It failed with exact code `ARTIFACT_STORAGE_LIMIT` and produced zero artifacts. Therefore this audit does not claim fresh GUI overflow proof. The prior unchanged-source attestation artifact remains useful but retains its documented font-substitution, primary-frame-only button, and packaged-artifact limitations.

## Focus, event, technology, decision, and live-render limitations

- A fresh DHR focus inspection succeeded with `FOCUS_INSPECTED` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02cb30551c8621d534715459d1e239ca314d99a49f17068f9b57749951f60dd2/053aadb7a1f77e55422f85e883b1f652c05b497260bd92e531d9f1efd4d5df3d/focus-inspect.d56fa9e29324e4ac.json`.
- The first KRG focus call used the wrong tree id and returned `FOCUS_TREE_NOT_FOUND`. A corrected call for `brilliant_scientist_kruger_state_focus_tree` was terminated at the parent’s request rather than waiting on another long MCP operation. The prior KRG focus evidence remains the only rendered tree evidence for this final pass.
- The installed event renderer does not measure popup text-box overflow. Prior Event 016 event artifacts remain structural, partial evidence only.
- The installed package exposes no ordinary decision/category, mission-description, achievement, native-raid, Event Log, or Event Details text-box renderer. Source review is not treated as equivalent overflow evidence.
- A Technology Tree Viewer is absent. Existing technology traces are partial structural evidence and do not certify localisation overflow.
- No HOI4 session or live consumer was run. User-owned live display validation remains outside this audit.

## Asset and GFX path evidence

A fresh source-path scan covered the direct `016_*.gfx` files plus the linked Alien Infantry, Portal Raider, achievement, decision-category, and text-icon registries. It found 1,533 texture references across 18 inspected registries. The only three missing files were the shared vanilla Norway preparation icons referenced by `interface/chaosx_texticons.gfx:4`, `:9`, and `:14`; they are unrelated to Event 016 and are not Event 016 asset-path defects. No Event 016, DHR, Alien Infantry, Portal Raider, Kruger focus, Directorate GUI, achievement, portrait, flag, report/news, or super-event texture path was missing in the inspected set.

This path check proves source resolution only. It does not certify model/entity runtime, button animation frames, final font fit, or in-game asset presentation.

## Recommended fixes

1. Rewrite the four KRG focus-effect tooltips listed above in `localisation/english/016_brilliant_scientist_focus_l_english.yml` without changing the focus effects. Use existing constants and concrete unlock names where the current source exposes them.
2. Do not remove or shorten the DHR probability tiers merely to reduce source length. First inspect the actual mission consumer when an applicable renderer or user screenshot is available, then restructure with concise line breaks or a secondary tooltip only if overflow is observed.
3. Retain the current dynamic Alien Infantry constant tokens and the premise-only DHR Event Details clause.
4. Treat the GUI render storage limit, unsupported standard decision/mission/achievement render surfaces, absent Technology Tree Viewer, and interrupted KRG focus inspection as explicit evidence limitations rather than localisation passes.

## Changed files and keys

Changed by this audit: none. The only written file is this handoff.

Commit `18f7c7d67` changed the values of `brilliant_scientist_directorate_gui_sovereignty` and `chaosx.nr16.47.a.tt`; both current values are mechanically and stylistically clearer than their immediate predecessors and preserve all dynamic tokens.

## Unresolved wording decisions

The exact player wording for the four KRG focus-effect tooltips depends on the owning focus/system agent confirming the public names and visible limits of the unlocked officer proceeding, terminal network, Alien Laser Weapon production, and foreign operations. The current source proves the unlock flags and helper calls but does not by itself establish every downstream consumer sentence.

## Simplifications, omissions, and blockers

No localisation fallback, key alias, hidden fifth evolution, cluster entry, broad tone rewrite, quote normalization, gameplay change, or asset substitution was introduced.

This audit does not claim whole-event completion. Fresh GUI rendering is blocked by `ARTIFACT_STORAGE_LIMIT`; standard decision, mission, achievement, Event Log, and Event Details overflow routes are unavailable; the Technology Tree Viewer is absent; the corrected KRG focus inspection was terminated to avoid delaying the parent; and user-owned live display acceptance remains open.
