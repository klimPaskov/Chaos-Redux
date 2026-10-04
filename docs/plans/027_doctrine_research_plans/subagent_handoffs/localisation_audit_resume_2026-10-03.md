# Event 027 localisation audit resume, 2026-10-03

Disposition: implemented bounded localisation fixes, with consumer presentation and native execution unresolved.
Acceptance basis: the parent explicitly authorized an active audit and small localisation/helper-state fixes in the two owned files, plus this handoff.
This report does not approve or complete Event 027.

## Ownership and shared-workspace preservation

Repository: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.
Edited gameplay-facing files: `localisation\english\027_doctrine_research_l_english.yml` and `common\scripted_localisation\027_doctrine_research_scripted_localisation.txt`.
Both already contained substantial uncommitted changes when the audit began.
The audit applied individual hunks and preserved those changes.
The parent concurrently changed `027_doctrine_research_achievement_eligible_tooltip` to "Complete this country's own curriculum in a campaign without manual or forced doctrine setup."
That change belongs to the parent and is excluded from this auditor's changed-key list.
No achievement string, shared scripted localisation, Event Details text, workbook, gameplay, asset, or GUI was edited by this auditor.
No game was launched.
No commit was created because mandatory consumer proof remains unresolved and the owned files include other agents' changes.

Skills used: `.agents\skills\chaos-redux-events\SKILL.md` and `.agents\skills\chaos-redux-subagents\SKILL.md`.
There is no separately named localisation skill in the repository skill catalog or the bounded skill-path search.
The localisation rules in AGENTS.md, the events skill, and the offline localisation reference were applied.

## Changed keys and helper

There are 27 auditor-owned changed or added localisation keys.

- `chaosx.nr27.5.army_infantry`
- `chaosx.nr27.5.army_combat_support`
- `chaosx.nr27.5.army_armor`
- `chaosx.nr27.5.army_operations`
- `chaosx.nr27.5.navy_submarines`
- `chaosx.nr27.5.navy_screens`
- `chaosx.nr27.5.navy_carriers`
- `chaosx.nr27.5.navy_capital_ships`
- `chaosx.nr27.5.air_fighter_aircraft`
- `chaosx.nr27.5.air_strike_aircraft`
- `chaosx.nr27.5.air_medium_aircraft`
- `chaosx.nr27.5.air_heavy_aircraft`
- `chaosx.nr27.5.special_forces_first`
- `chaosx.nr27.5.special_forces_second`
- `chaosx.nr27.5.chaos_warfare_infantry`
- `chaosx.nr27.5.chaos_warfare_combat_support`
- `chaosx.nr27.5.chaos_warfare_armor`
- `chaosx.nr27.5.chaos_warfare_operations`
- `doctrine_research.result.detail.mastery`
- `chaosx.nr27.2.a.tt`
- `chaosx.nr27.7.a.tt`
- `chaosx.nr27.11.d`
- `chaosx.nr27.11.a.tt`
- `chaosx.nr27.12.d`
- `chaosx.nr27.12.a`
- `chaosx.nr27.12.a.tt`
- `doctrine_research.option.state.complete_at_maximum`

Changed helper: `GetDoctrineResearchOptionStatus60PeoplesWar`.
Its consumer is `chaosx.nr27.60.peoples_war`.
Added display temporary variable: `doctrine_research_option_maximum`, assigned from `constant:doctrine_research_event.peoples_war_max_mastery_level` in the selected text trigger.
The formatted number lives in a real localisation value, not an inline dynamic key.

## Behavior before and after

The 18 track labels previously combined the track name, branch name, current/maximum/next levels, completion state, and Milestone status in one button label.
They now show the track name and the existing dynamic current/maximum-to-next preview.
Every corresponding `.tt` retains the branch, maximum, next level, completion, native Milestone context, and successful-choice cost.
This is a concise visible-label change authorized by the parent, rather than a removal of required information from the choice surface.
Actual fit and overflow have not been proved.

The People's War level-four fallback previously used `doctrine_research.option.state.level_4`, which says "Mastery 4 -> 5."
It now reads "Complete at Mastery 4" using the owning maximum constant.
The higher-priority historical-completion branch still says "Complete."
The native source contains four rewards, and the event's maximum constant is four.
Normal eligibility should already omit a completed branch, so this repairs defensive/stale display state rather than enabling a new action.

The suspended-review description previously asserted that the branch did not advance and offered another review of the same curriculum.
An ambiguous native result does not prove that no effect occurred.
All inspected ambiguous-result paths call the quarantine/close helper, which clears the active curriculum.
The description now acknowledges that progress could not be confirmed, states that no choice was spent and the curriculum has closed, and offers continuation to the next curriculum.
The option label is "Continue."

The mastery result now leads with the actual branch and reached level instead of "Subdoctrine advanced."
The opening and confirmation tooltips explain whether a choice is spent without repeating their button title.
The no-option report now states that unused choices expire instead of discussing a substitute reward.

## Final wording for review

```text
doctrine_research.result.detail.mastery: "[GetDoctrineResearchSubdoctrineName] reached mastery level [?doctrine_research_last_transaction_post_level|0] in the [GetDoctrineResearchTrackName] track."
chaosx.nr27.2.a.tt: "Choose a doctrine domain without spending a curriculum choice."
chaosx.nr27.7.a.tt: "Spend one curriculum choice only if the selected doctrine action succeeds."
chaosx.nr27.11.d: "[ROOT.GetName] has no eligible doctrine action at present. [GetDoctrineResearchRemainingChoiceStatus] Review the available doctrines once more. If none can advance, the curriculum closes and unused choices expire."
chaosx.nr27.11.a.tt: "Check for an eligible doctrine action. If none remains, the curriculum closes and unused choices expire."
chaosx.nr27.12.d: "The staff could not confirm the selected doctrine's progress, so no choice was spent and this curriculum has closed. [GetDoctrineResearchRemainingChoiceStatus] Continue to the next curriculum awaiting review."
chaosx.nr27.12.a: "Continue"
chaosx.nr27.12.a.tt: "Begin the next curriculum awaiting review."
doctrine_research.option.state.complete_at_maximum: "Complete at Mastery [?doctrine_research_option_maximum|0]"
```

Track labels follow this exact pattern, with each existing icon and track-specific variable preserved:

```text
chaosx.nr27.5.army_infantry: "£GFX_doctrine_milestone_infantry_land Study Infantry: [?doctrine_research_track_menu_army_infantry_current|0]/[?doctrine_research_track_menu_army_infantry_maximum|0] -> [?doctrine_research_track_menu_army_infantry_next|0]"
chaosx.nr27.5.army_combat_support: "£GFX_doctrine_milestone_artillery_land Study Combat Support: [?doctrine_research_track_menu_army_combat_support_current|0]/[?doctrine_research_track_menu_army_combat_support_maximum|0] -> [?doctrine_research_track_menu_army_combat_support_next|0]"
chaosx.nr27.5.army_armor: "£GFX_doctrine_milestone_armored_land Study Armor: [?doctrine_research_track_menu_army_armor_current|0]/[?doctrine_research_track_menu_army_armor_maximum|0] -> [?doctrine_research_track_menu_army_armor_next|0]"
chaosx.nr27.5.army_operations: "£GFX_doctrine_milestone_operations_land Study Operations: [?doctrine_research_track_menu_army_operations_current|0]/[?doctrine_research_track_menu_army_operations_maximum|0] -> [?doctrine_research_track_menu_army_operations_next|0]"
chaosx.nr27.5.navy_submarines: "£GFX_doctrine_milestone_submarine_naval Study Submarines: [?doctrine_research_track_menu_navy_submarines_current|0]/[?doctrine_research_track_menu_navy_submarines_maximum|0] -> [?doctrine_research_track_menu_navy_submarines_next|0]"
chaosx.nr27.5.navy_screens: "£GFX_doctrine_milestone_screens_naval Study Screens: [?doctrine_research_track_menu_navy_screens_current|0]/[?doctrine_research_track_menu_navy_screens_maximum|0] -> [?doctrine_research_track_menu_navy_screens_next|0]"
chaosx.nr27.5.navy_carriers: "£GFX_doctrine_milestone_carriers_naval Study Carriers: [?doctrine_research_track_menu_navy_carriers_current|0]/[?doctrine_research_track_menu_navy_carriers_maximum|0] -> [?doctrine_research_track_menu_navy_carriers_next|0]"
chaosx.nr27.5.navy_capital_ships: "£GFX_doctrine_milestone_ships_naval Study Capital Ships: [?doctrine_research_track_menu_navy_capital_ships_current|0]/[?doctrine_research_track_menu_navy_capital_ships_maximum|0] -> [?doctrine_research_track_menu_navy_capital_ships_next|0]"
chaosx.nr27.5.air_fighter_aircraft: "£GFX_doctrine_milestone_fighter_air Study Fighter Aircraft: [?doctrine_research_track_menu_air_fighter_aircraft_current|0]/[?doctrine_research_track_menu_air_fighter_aircraft_maximum|0] -> [?doctrine_research_track_menu_air_fighter_aircraft_next|0]"
chaosx.nr27.5.air_strike_aircraft: "£GFX_doctrine_milestone_striker_air Study Strike Aircraft: [?doctrine_research_track_menu_air_strike_aircraft_current|0]/[?doctrine_research_track_menu_air_strike_aircraft_maximum|0] -> [?doctrine_research_track_menu_air_strike_aircraft_next|0]"
chaosx.nr27.5.air_medium_aircraft: "£GFX_doctrine_milestone_medium_air Study Medium Aircraft: [?doctrine_research_track_menu_air_medium_aircraft_current|0]/[?doctrine_research_track_menu_air_medium_aircraft_maximum|0] -> [?doctrine_research_track_menu_air_medium_aircraft_next|0]"
chaosx.nr27.5.air_heavy_aircraft: "£GFX_doctrine_milestone_heavy_air Study Heavy Aircraft: [?doctrine_research_track_menu_air_heavy_aircraft_current|0]/[?doctrine_research_track_menu_air_heavy_aircraft_maximum|0] -> [?doctrine_research_track_menu_air_heavy_aircraft_next|0]"
chaosx.nr27.5.special_forces_first: "£GFX_doctrine_milestone_special_forces Study First Special Forces: [?doctrine_research_track_menu_special_forces_first_current|0]/[?doctrine_research_track_menu_special_forces_first_maximum|0] -> [?doctrine_research_track_menu_special_forces_first_next|0]"
chaosx.nr27.5.special_forces_second: "£GFX_doctrine_milestone_special_forces Study Second Special Forces: [?doctrine_research_track_menu_special_forces_second_current|0]/[?doctrine_research_track_menu_special_forces_second_maximum|0] -> [?doctrine_research_track_menu_special_forces_second_next|0]"
chaosx.nr27.5.chaos_warfare_infantry: "£GFX_doctrine_milestone_infantry_land Study Chaos Infantry: [?doctrine_research_track_menu_chaos_warfare_infantry_current|0]/[?doctrine_research_track_menu_chaos_warfare_infantry_maximum|0] -> [?doctrine_research_track_menu_chaos_warfare_infantry_next|0]"
chaosx.nr27.5.chaos_warfare_combat_support: "£GFX_doctrine_milestone_artillery_land Study Chaos Combat Support: [?doctrine_research_track_menu_chaos_warfare_combat_support_current|0]/[?doctrine_research_track_menu_chaos_warfare_combat_support_maximum|0] -> [?doctrine_research_track_menu_chaos_warfare_combat_support_next|0]"
chaosx.nr27.5.chaos_warfare_armor: "£GFX_doctrine_milestone_armored_land Study Chaos Armor: [?doctrine_research_track_menu_chaos_warfare_armor_current|0]/[?doctrine_research_track_menu_chaos_warfare_armor_maximum|0] -> [?doctrine_research_track_menu_chaos_warfare_armor_next|0]"
chaosx.nr27.5.chaos_warfare_operations: "£GFX_doctrine_milestone_operations_land Study Chaos Operations: [?doctrine_research_track_menu_chaos_warfare_operations_current|0]/[?doctrine_research_track_menu_chaos_warfare_operations_maximum|0] -> [?doctrine_research_track_menu_chaos_warfare_operations_next|0]"
```

## Audit findings

Missing key list: none found among owned scripted-localisation output keys, nested dollar-key references, and 289 distinct Event027 event title/description/option/tooltip references.
Duplicate key list: none inside the owned English file, and no other English file redeclares its Event027 key namespaces in the scoped search.
Scripted localisation issue list: repaired the People's War 4-to-5 fallback.
No duplicate owned helper names or missing called Event027 helpers were found.
All 139 distinct Event027 constant references in the owned helper file resolve to declared keys.
No other scripted-localisation file redeclares `GetDoctrineResearch*` helpers in the scoped search.

Result-state review: `GetDoctrineResearchResultDetail` already dispatches on `doctrine_research_last_transaction_action`, rather than `doctrine_research_selected_action`.
`doctrine_research_record_last_transaction` captures receipt action, domain, Grand Doctrine, track, branch, and post-level before successful finalization clears only the selected action.
The result page is gated on a successful last transaction.
Its domain/Grand Doctrine/track/branch name getters still read retained selection variables, which the current successful path preserves until continuation.
No demonstrated result-state defect was patched.
Captured-name-only getters would be a resilience opportunity if the parent later changes selection cleanup timing.

Dynamic text opportunities: plural-aware choice/domain/track counts remain optional polish.
Empty-track menu projections currently default to a five-level maximum before a branch is chosen, including a track that may offer People's War.
This is a generic preview, not proof of a specific branch's maximum.
The parent should consider an explicit "Choose a branch" preview for empty tracks, preserving exact branch-specific levels and Milestone context in the chosen-branch confirmation.
No gameplay or additional preview subsystem was invented here.

Native Milestone wording: mastery steps and Grand Doctrine Milestones remain distinct.
The menu and confirmation projections use dynamic completion/Milestone state.
The final summary's `doctrine_research_summary_milestone_reached` is currently inferred in `doctrine_research_finalize_receipt` from the post-level reaching the branch maximum.
That does not independently prove that the engine activated a native Milestone.
Parent follow-up: verify native Milestone readback before acceptance, or change the owning summary-state calculation.
The auditor did not relabel this as proven native activation or change gameplay meaning through a wording workaround.

Navigation: the source contains 14 next-page and 14 previous-page option occurrences using shared navigation wording.
All 22 distinct back-option keys resolve.
The pages use explicit doctrine-page navigation, and the shared navigation tooltip states that it spends no choice.
The successful result continues either to another choice or to the final summary.
The no-option report checks again and closes when no action remains.
The native-bank completion page describes existing mastery, preserves the no-choice-spent distinction, and returns to tracks or the no-option route.
These are source findings, not executed flow proof.

Icon references: all 127 distinct text-icon references resolve to sprite declarations in recursive mod and installed-game interface scans.
The initial root-only scan missed `interface\doctrines\doctrines.gfx` and was corrected before reporting.
No missing icon is claimed from that discarded partial scan.
Key locations include installed `interface\doctrines\doctrines.gfx` at lines 141-142 for the infantry Milestone sprite and line 326 for People's War.
Sprite declaration coverage does not prove rendered texture visibility or native text-icon sizing.

Domain/track/branch coverage: owned getters cover Army, Navy, Air, Special Forces, and Chaos Warfare.
All 18 track-label tooltip pairs retain required context.
The source correspondence scan examined 144 branch-option occurrences, including repeated paginated/track consumers, and found no mismatch between the selected branch token and its option-status helper.
This occurrence count is not a count of distinct native filter targets.
The parent's f9978e9 native-filter repair and 107 unique startup targets were retained as the supplied baseline, not reimplemented by this auditor.

## Prose quality review

Vagueness: the mastery result now names who/what advanced, and the suspended review no longer turns an unconfirmed outcome into a definite failure.
Bloat: the 18 button labels remove duplicated branch/completion/Milestone text that remains in their tooltips.
Obvious explanation: opening/confirmation tooltips lead with choice consumption instead of repeating the button action.
Repetition: the result drops its introductory label, and track details are presented in the tooltip instead of duplicated in the button.
Overcomplication: the suspended/no-option pages state the player's next action and the consequence for unused choices directly.
Style-rule repair: no em dash or sentence semicolon was found in the owned localisation passages.
No staged contrast, attributed quotation, or hidden route reveal was introduced.

The repeated empty-track descriptions `chaosx.nr27.60.d` through `chaosx.nr27.77.d` are data-heavy and can show "No Subdoctrine" beside a generic level preview before selection.
They were examined, not accepted as proof of a good rendered page.
A branch-aware display treatment is recommended alongside the empty-track preview issue above.
The five domain labels and all populated branch labels also need actual consumer fit review.
Their source validity does not settle overflow.

Sourced-quotation preservation: no actual sourced or attributed quotation appears on the inspected Event027 surfaces.
Established doctrine and branch proper names and nested vanilla localisation references were preserved.
Dynamic tokens and icons were preserved, except that duplicated branch/completion/Milestone tokens were removed from the 18 labels with their unchanged counterparts retained in the same options' tooltips.
No cost, requirement, or consequence was removed from the choice surface.
The suspended-page wording changes the explanation to match existing source behavior, without changing that behavior.

## Cross-surface and spreadsheet handoff

Choice-flow and presentation specs require concise result pages, explicit choice consumption, branch/level context, native Milestone terminology, and navigation that spends no choice.
The patch follows those requirements.
The package's self-described "accepted" status does not itself establish user acceptance.
The active parent instruction establishes acceptance for this bounded patch only, and full feature acceptance remains open.

The catalog workbook was not read or edited in this bounded pass.
The earlier `spreadsheet_worker_current_2026-09-01.md` records "one mastery level" in Event Details and "Established domains can divide those choices" in Evolution III.
The current owned localisation instead uses "one mastery step" and the following Evolution III wording.
Those are historical-handoff mismatches requiring a current workbook check, not a claim that the workbook is presently stale.
None of this auditor's changed keys are catalog detail fields.

Give `chaosx_spreadsheet_doc_worker` these authoritative current key/value pairs if those fields differ:

```text
chaosx.events_log.window.event_details.doctrine_research: "Military academies across the world periodically receive a shared curriculum. Each curriculum grants one choice at first and as many as five in later stages. A choice can establish a Grand Doctrine or advance one eligible subdoctrine by one mastery step."
chaosx.events_log.window.evolution_details.doctrine_research.body.stage_3: "Each participating country receives four doctrine choices. Countries with established Grand Doctrines can divide those choices among several eligible tracks."
```

Shared Event Details wording still lists choice counts and mechanical advancement.
AGENTS.md's prose-only Event Details rule conflicts with the event presentation spec's explicit mechanics direction.
This remains a parent-owned scope/acceptance decision.
The auditor did not edit those keys.

Achievement eligibility and wording remain parent-owned.
No achievement acceptance is claimed from the concurrent tooltip change.

## Meaningful validation and limitations

Source checks found 370 owned localisation keys, 183 owned scripted-localisation helpers, zero missing referenced localisation keys, zero missing called helpers, zero branch/helper mismatches, and zero unresolved text-icon declarations.
The 18 required track tooltip contexts were checked after shortening the labels.
The People's War fallback uses the existing four-level constant and cannot select the five-level transition key.
The result dispatcher was checked with selected action cleared and last action retained.
All 27 auditor-owned key edits remained applied after detecting the parent's concurrent achievement edit.
The localisation BOM was preserved, with no encoding concern found.

Full native mastery, bank settlement, save/reload recovery, text wrapping, button fit, texture visibility, and rendered Milestone state were not validated.
The user/orchestrator owns game execution and live evidence.
No gameplay balance or achievement audit was performed.

## MCP evidence and package gap

The connected tool list exposes the HOI4 reference, event, and technology routes, contrary to the initial parent-side expectation.
Exposure does not establish complete service health.
`hoi4.reference_context(surface=localisation, limit=4)` returned successfully for workspace `mod_chaos_redux_ea3b2d67c2c0`.
It reported no missing or omitted sources.
`hoi4.reference_search(query="Scripted localisation")` also returned successfully and identified the exact offline sections.
These successful reference responses do not establish event or doctrine consumer coverage.

Corrected narrow event request: `hoi4.event_inspect(mode=trace, selector={kind:event,eventId:chaosx.nr27.1}, maxDepth=2, maxNodes=25, maxEdges=50, expandHelpers=false)`.
It failed with `timed out awaiting tools/call after 600s`.
No inspection artifact, revision-bound graph, or native verdict was returned.
Earlier malformed selector attempts were rejected and corrected, not used as evidence.

The narrow `hoi4.event_render(view=options, eventId=chaosx.nr27.5)`, wiki `reference_read`, and land-doctrine `tech_inspect/tech_render` requests did not return before this bounded audit ended.
Their local orchestration cells were terminated to honor the parent's instruction not to wait for whole-workspace MCP.
There was no job identity or server cancellation receipt.
No event/technology render URI or consumer verdict is claimed.
The other four domain renders and post-change compare remain unrun because consumer evidence was not obtainable within the bounded pass.
Source review is explicitly limited and does not replace mandatory inspect/render/compare evidence.

Standalone Technology Tree Viewer was checked separately from the exposed `hoi4.tech_*` routes.
No standalone viewer tool or identifiable viewer plugin surfaced in the connected tool catalog or bounded plugin-path search.
Record this as a viewer package/capability gap in this session, without claiming that no viewer exists elsewhere on the machine.
No viewer was opened or modified.
Server version/health and native task negotiation were not available as confirmed evidence, so no helper-expansion or job route was used.

Useful artifact URIs: none returned for this audit.
The source paths and hashes below are the usable evidence.

## Reference sections read locally

Paths under the game directory are relative to `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.

| Source | Lines | SHA-256 / revision | Purpose |
| --- | --- | --- | --- |
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 184-216, 656-760 | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` | Integer formatting, first matching scripted text, current scope, temporary display values. |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 481-528 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` | Temporary-variable trigger use and localisation scope. |
| Installed `documentation\script_concept_documentation.md` | 1-64 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` | Localisation key/binding structure. |
| Installed `documentation\triggers_documentation.md` | 3526-3538 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` verified locally | Historical meaning of completed subdoctrine. |
| Installed `common\doctrines\tracks\_documentation.md` | 1-44 | `7b34cc7f2ac59fd7cdb2dd6c9fa87d6d683db2d2b71eea176b690bdb6d6b2ec8` | Distinguish track mastery rewards from Grand Doctrine Milestone. |
| Installed `common\doctrines\subdoctrines\_documentation.md` | 1-70 | `81dcc8e9565e16050c269220c7a706ec894bb5b22712ecabfcb598e1fb671df0` | Native branch names/icons and reward structure. |
| Installed `common\doctrines\subdoctrines\land\infantry_subdoctrines.txt` | 716-823 | `8bcd67f6f7d108325c78a14daa39f2807d4bdc59ea27b726520cd6751caebc5f` | People's War name, icon, and four-level shape. |
| Installed `common\scripted_localisation\WUW_GER_scripted_loc.txt` | 1-40 | `82233d7bb8362d933182c7da345606089a67b92adedb764c37a942e1e2f67683` | Vanilla conditional numeric-state scripted-text precedent. |

The reference-search section ID for scripted localisation was `8466af7164ce523520ef7e725d7711b333cc284bf7a70f0eeb7834993db17bb8`.
The relevant section was read directly from the local wiki after the MCP read route stalled.
No successful MCP section read is claimed.

## Source identities and resume instructions

Observed repository HEAD: `3bfe73111f848886b7cbe0dacf8f98beef25e672`.
The repository is shared and these are observation-time identities, not a frozen whole-workspace snapshot.

| File | SHA-256 |
| --- | --- |
| Owned English localisation, audit-entry state | `8e6a8fd54de78cdc92da712dd84a5d2ea729cb1ef4b1523efa4621addb9455c4` |
| Owned scripted localisation, audit-entry state | `662a475bd579339bfae7ed5428823adf340daeb810def8fc184c569c05a3cc8e` |
| Owned English localisation, final observed state including parent tooltip edit | `0dfb4b32c313f23fb629e87828a7d028681a8f737b7ae45e6ccc6e21653ff5cf` |
| Owned scripted localisation, final observed state | `7bbd4ebf37eb14b634aa1f781aa7945d1c019601f01a5a0bb21ad683b925321a` |
| `events\027_doctrine_research.txt` | `d61145d94a54d6ef542999ea120973d2bba4a1db877dd10e47dadeaf3a2ab2d1` |
| `common\scripted_effects\027_doctrine_research_effects.txt`, latest observed | `4a6ad8aec0733be61251735ab94e941e11cf9a7f5ad3941168957a95a752826a` |
| `common\scripted_triggers\027_doctrine_research_triggers.txt`, latest observed | `3e4e3c6f46e9c8b457cf0a97b1d96196454a56d6e08dc84e9ac155ca2e599b86` |
| `common\scripted_effects\chaosx_startup_history_effects.txt` | `42a878dec327ec2a58764bfa9b25c2620f4b9cfeca12355d6a2fea90808d4f4a` |
| `common\script_constants\027_doctrine_research_constants.txt` | `d24ba6d1c77f76880be4297f01cd848859466ac806643b29b41561376861d87a` |

Effects/triggers changed concurrently during the audit.
The result capture, action clearing, ambiguous closure, maximum display, and summary Milestone logic were reread in their latest observed state.
Recheck these hashes before relying on line positions or expanding the patch.

Unresolved wording decisions: empty-track generic preview, proof of native summary Milestone activation, shared Event Details rule conflict, and current workbook wording alignment.
Achievement eligibility/handoff remains with the parent.
No feature simplification or gameplay substitute was introduced.
Evidence omissions are the unreturned mandatory consumer inspections/renders/comparisons, the absent standalone viewer capability, and the intentionally uninspected current workbook.
The parent should review the bounded patch and carry those limitations into final acceptance.

## Read-only appendix: parent integration verification, 2026-10-03

Disposition: source-verified parent corrections, with payload production and consumer execution still unresolved.
This appendix updates the observation-time findings above without changing the historical audit record.
Only this handoff was edited during this follow-up.
The owned localisation/helper files and all shared source files were read-only.

### Native Milestone summary correction

The earlier maximum-level inference has been removed from `doctrine_research_finalize_receipt`.
For a mastery action, finalization now calls `doctrine_research_prepare_display_levels` and sets `doctrine_research_summary_milestone_reached` only when `doctrine_research_display_milestone_reached = 1`.
The display helper resets that value before checking the selected domain/track through native `has_completed_track` branches.
Adoption cannot set the summary through this branch.
The correction runs before selected action is cleared, while the domain/track identity remains available.
This resolves the earlier source-level concern that reaching a branch maximum alone was treated as a native Milestone.
Actual engine track/Milestone behavior remains unexecuted.

Installed `documentation\triggers_documentation.md`, lines 3541-3554, defines `has_completed_track` as checking completion of the given subdoctrine track.
The locally read revision remains `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.

### Eligibility tooltip verification and wording caveat

The owned key is present exactly once:

```text
027_doctrine_research_achievement_eligible_tooltip: "Complete this country's own curriculum in a campaign without manual or forced doctrine setup."
```

The campaign limitation matches the current guard against `doctrine_research_achievement_forced_setup_used` and `doctrine_research_achievement_debug_setup_used`.
The campaign-valid trigger also requires a living human country, excludes initialized CXT and corrupt state, and requires aligned country state.
Those internal integrity checks do not need to be narrated in the player-facing tooltip.
The root achievement registry uses this key for all three achievements and allows an already-earned achievement flag to preserve its eligibility display.
Receipt checks use the country's own batch arrays and require human-started batches.

Wording caveat: "Complete" can imply that every choice in the curriculum must be spent before any achievement can qualify.
First Lesson can qualify after the adoption and later matching mastery receipt, and Joint Curriculum can qualify after the fourth distinct track receipt in a five-choice batch.
Their inspected checks do not require the entire curriculum to close.
Single School has its own completion/remaining-choice requirement.
For precise common eligibility wording, the parent could replace only "Complete" with "Use":

```text
027_doctrine_research_achievement_eligible_tooltip: "Use this country's own curriculum in a campaign without manual or forced doctrine setup."
```

This is a recommendation, not an applied change or a broad achievement audit.
The exact supplied tooltip remains preserved.
The producer coverage of every manual/forced origin was not audited.

### All nine shared selectors

The source correspondence scan found these nine selectors, each defined once, with 15 distinct Event027 output keys.
Every output key resolves exactly once in English localisation.
No duplicate Event027 arm within a selector was found.
Repeated use of the same key by different selectors is expected reuse.

| Selector | Event027 output coverage |
| --- | --- |
| `GetEventsLogEvolutionTypeView` | Evolution type name. |
| `GetEventsLogEvolutionNameView` | Four stage titles. |
| `GetEventsLogSelectedHistoryEvolutionTypeView` | Evolution type name. |
| `GetEventsLogSelectedHistoryEvolutionNameView` | Four stage titles. |
| `GetEventsLogEventDetailEvolutionTypeView` | Evolution type name. |
| `GetEventsLogEventDetailDescription` | Five recorded-history descriptions plus generic premise. |
| `GetEventsLogEventDetailEvolutionTitle` | Four stage titles. |
| `GetEventsLogSelectedEvolutionTitle` | Four stage titles. |
| `GetEventsLogSelectedEvolutionBody` | Four stage bodies. |

The 15 keys are `chaosx.events_log.evolution.type.doctrine_research`, `chaosx.events_log.window.event_details.doctrine_research`, its five `.history.1` through `.history.5` keys, and the four `chaosx.events_log.window.evolution_details.doctrine_research.title.stage_*` and four corresponding `.body.stage_*` keys.
The selector definition/arm scan and relevant English-file duplicate scan returned no missing or duplicate key.
The common eligibility key also has one English definition.

### Recorded history and honest zero-payload fallback

In `common\scripted_localisation\chaosx_scripted_localisation_events_log.txt`, lines 5729-5778, all five history descriptions precede the generic Event027 premise.
Each requires all of these conditions: current `event_id = 27`, `events_log_detail_use_history_context`, selected history event 27, selected sequence greater than zero, and an exact payload matching its batch-size constant.
The constants are 1, 2, 3, 4, and 5 in order.
No branch maps payload zero to the Foundational curriculum.

These are source-derived outcomes, not an executed engine scenario matrix:

| Relevant source state | Event027 description selected |
| --- | --- |
| History context, selected event 27, positive sequence, payload 1 through 5 | Matching `.history.1` through `.history.5`. |
| Same valid history context, payload 0 | Generic Event027 premise. |
| Same valid history context, unsupported payload such as 6 | Generic Event027 premise. |
| History-context flag absent | Generic Event027 premise. |
| Sequence zero | Generic Event027 premise. |
| Selected history event differs from 27 | Generic Event027 premise. |
| Current event differs from 27 | No Event027 description arm matches. |

The generic premise explains the recurring curriculum and its possible choice range.
It does not assert that the selected zero-payload row granted a particular number of choices.
This is an honest fallback for unresolved or legacy payload data.
An unset-payload runtime scenario was not executed, and no assumption about engine default reads is needed to establish that an explicit zero does not match 1 through 5.
The producer/profile work remains open, so correct selectors do not prove that new history entries contain the intended payload.

### Four catalog preview rows

The Event027 block at `common\scripted_effects\chaosx_events_log_effects.txt`, lines 2822-2836, invokes `events_log_add_event_detail_evolution_preview` four times under event 27.
It uses evolution type 27 and the paired tier/stage constants for I, II, III, and IV in order.
The shared add helper, lines 2930-2958, appends type, tier, stage, and enabled state to the catalog preview arrays.
It does not create a history sequence or a firing date.
These are four catalog rows, not evidence that any evolution or curriculum fired.
Selector title/body keys exist for every corresponding stage.

### Preserved patch, identities, and remaining limits

The owned English and scripted-localisation hashes remain identical to the end of the original audit.
This confirms preservation of the earlier 27-key patch and People's War helper repair, including the parent's existing eligibility tooltip.
No source or achievement wording was edited in this follow-up.
No sourced quotation is present on the inspected passages, and no dynamic token or attributed text was changed.

| Read-only file | Follow-up SHA-256 |
| --- | --- |
| `localisation\english\027_doctrine_research_l_english.yml` | `0dfb4b32c313f23fb629e87828a7d028681a8f737b7ae45e6ccc6e21653ff5cf` |
| `common\scripted_localisation\027_doctrine_research_scripted_localisation.txt` | `7bbd4ebf37eb14b634aa1f781aa7945d1c019601f01a5a0bb21ad683b925321a` |
| `common\scripted_localisation\chaosx_scripted_localisation_events_log.txt` | `641a78580e2291c97c0f45ff8efc0397e26812cad39a25c9a6b759bf34dcdb8a` |
| `common\scripted_effects\chaosx_events_log_effects.txt` | `5f9f99be4aa88dfddb17eb1f7a171dfbf6d49283ca51a2ee54b60940d2a770ce` |
| `common\scripted_effects\027_doctrine_research_effects.txt` | `b1c32460a261b06712b2fc3c39a5b7a37759251f70641c1f757a0b4f4baf8663` |
| `common\scripted_triggers\027_doctrine_research_triggers.txt` | `3e4e3c6f46e9c8b457cf0a97b1d96196454a56d6e08dc84e9ac155ca2e599b86` |
| `common\scripted_effects\027_doctrine_research_achievement_effects.txt` | `809edbf5df1bc4cbeb7e0af8b908baca994678dab72a503149acdc4c1d0ba2fe` |

Meaningful checks: nine unique selector definitions, 15 uniquely defined output keys, five exact guarded history arms, four explicit catalog-preview additions, actual native track readback in the mastery summary, and unchanged owned-file hashes.
The earlier MCP timeout/render limitations remain in force.
No new MCP artifact or executed consumer proof was obtained in this bounded read-only follow-up, and no game was launched.
Profile/payload producer behavior, live text fit, actual native reward activation, and full acceptance remain unresolved.
The earlier maximum-level inference concern is superseded by the verified parent source correction.
The eligibility "Complete" wording caveat remains actionable for the parent.

## Current wording and profile-build note, 2026-10-03

This is a read-only source observation following the parent's profile/history build.
Only this handoff was appended.
The previous eligibility wording caveat is resolved by the parent's one-key change:

```text
027_doctrine_research_achievement_eligible_tooltip: "Use this country's own curriculum in a campaign without manual or forced doctrine setup."
```

The wording no longer implies that First Lesson or Joint Curriculum must wait for every curriculum choice to be spent.
This key change belongs to the parent and is additional to the auditor's preserved 27-key patch.
The owned scripted-localisation hash is unchanged.

`chaosx.nr27.14` is a hidden, triggered-only receiver whose immediate effect calls `doctrine_research_wake_country_batches`.
Its omitted title, description, and screen-option keys are intentional.
It is not a missing player-facing localisation surface.

The history binder is now inside the exact `record_events_log_history_entry` definition, guarded by event 27, at current lines 817-820.
The recorder copies the payload override before adding its history payload row.
The Event027 producer prepares the firing profile, captures recipient scopes, publishes their batch rows, and supplies the captured firing size as the history payload override.
The binder records the actual history sequence and releases hidden receiver 14 only after batch publication.
This verifies the intended source ordering, not native execution, reentrancy, or payload persistence.

The bounded National Breakthroughs selector search found four event-log name references, one event-log description reference, and the Settings `GetSettingsClusterName` name reference.
They resolve to the existing `chaosx.event_cluster.national_breakthroughs.name` and `chaosx.events_log.window.cluster_details.description.national_breakthroughs` keys in `localisation\english\chaosx_gui_l_english.yml`, current lines 901 and 428.
No shared source was changed by this auditor.

| Current observed source | SHA-256 |
| --- | --- |
| Owned English localisation | `aab9117be89de76206de3691200d9d01d7397678b41663c00d473f7c4dacc1b4` |
| Owned scripted localisation | `7bbd4ebf37eb14b634aa1f781aa7945d1c019601f01a5a0bb21ad683b925321a` |
| `events\027_doctrine_research.txt` | `777149623bf633fc07c04cf4f7f747a208024d2afee00d6e7120ae4bf9e01751` |
| `common\scripted_effects\027_doctrine_research_effects.txt` | `794ce5ae417b98807a3c8b7c35aac578c6c6e98b42398aeb341783807f7898d4` |
| `common\scripted_effects\chaosx_events_log_effects.txt` | `7fde6b681e3bd62a38eb2c01a22ffab8fc262ad2b0e37e7d0fede43c028d9b81` |

Text fit remains open for the shorter track labels, five domain labels, populated branch labels, long empty-track descriptions, tooltips, and shared detail views.
No actual overflow or wrapping clearance is claimed after this profile build.
The earlier source-verified zero-payload fallback remains the appropriate honest display when a row does not contain a recognized payload.
Profile/payload runtime proof and full feature acceptance remain with the parent and user/orchestrator.
No game was launched, and no 600-second MCP attempt was repeated.
