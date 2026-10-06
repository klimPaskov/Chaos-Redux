# Event 097 Collaboration: Decision and Mission Design Audit

- Role: `chaosx_decision_mission_auditor`, audit-only design-review mode.
- Date: 2026-10-06.
- Evidence class: design review of a planning specification, source review of repository precedents, offline wiki snapshot under `paradox_wiki/`. No HOI4 MCP evidence, because `hoi4_agent_tools` failed to connect in this session. No vanilla game files or vanilla documentation, because the Windows Steam paths do not exist in this Linux container.
- Disposition: unresolved audit findings for parent review.
- Files written: this report only. No spec, prompt, gameplay, localisation, or asset file was edited by this auditor.

## Spec version audited

The spec was revised three times while this audit ran. Earlier drafts of this report were read and applied during the run, and the decision prompt now cites this report for its reasoning.

This version reviews the working-tree text with these modification times (UTC, 2026-10-06):

| File | Modified |
| --- | --- |
| Part 4 | 14:56:07 |
| Parts 1, 3, and 6, the probability matrix, the edge case matrix, and the Chaos impact map | 14:56:35 |
| Decision prompt | 14:57:04 |

Findings are numbered in two series.

- First-pass findings use H, M, and L numbers. Each keeps its reasoning in one or two sentences and states where the current text resolves it.
- New or residual findings on the revised text use N numbers.

## Sources reviewed

- `AGENTS.md`.
- The uploaded decision skill, treated as the newer authority over `.agents/skills/chaos-redux-decisions-missions/SKILL.md`. It adds:
  - the six-primary-action note
  - the `<base>`, `<base>_blocked`, and `<base>_tooltip` custom-cost keys
  - inclusive affordability checks
  - static `ai_hint_pp_cost`
  - the trigger evaluation cost section
  - `days_remove` on decision-level modifiers
- `chaos-redux-scripted-gui` "Content and interaction budget", and the relevant `chaos-redux-events` sections.
- Spec Parts 1 to 6, the decision and asset prompts, the probability matrix, the edge case matrix, the research notes, and `097_repo_explorer_handoff.md`.
- Precedents:
  - Category files for Events 033 and 039, plus `famine_decision_category.txt`, `migration_decision_category.txt`, `condemnation_sanctions_categories.txt`, and `fallout_consolidated_categories.txt`.
  - Custom costs in `migration_decisions.txt` and `016_brilliant_scientist_containment_decisions.txt`.
  - `core_compliance` in `formable_nation_decisions.txt` lines 1198 to 1210.
  - `any_country_with_original_tag` in `024_video_game_in_sweden_triggers.txt` line 40.
  - `has_autonomy_state = autonomy_collaboration_government` in `012_africa_rsa_triggers.txt`.
  - `interface/chaosx_texticons.gfx`, and the `£` tokens across `localisation/english/`.
- Wiki:
  - Decision modding: costs at lines 305 to 335, timers at lines 337 to 355, targeted decisions at lines 514 to 560.
  - Effects: lines 1246 and 4723.
  - Triggers: lines 107, 642, 1158, and 976 to 979.
  - On actions: line 450.
  - Data structures: game variables near line 1512.

## How the skill classifies timed-modifier costs

The skill's hard cost budget counts anything an action "consumes, removes, reduces, or commits as payment". Its cost list names stability, civilian factory burden, and military factory output loss.

A timed stability or factory output penalty taken as the price of an action is therefore a spendable cost type. It counts toward the four-type limit and is not a requirement.

The repository precedent agrees. `016_brilliant_scientist_containment_decisions.txt` counts a decision-level consumer goods `modifier` with `days_remove` among its four cost types and shows it inline with `£consumer_goods_texticon`.

A displayed cost needs a correct texticon. Factory output has none in the mod, so it belongs in the effect tooltip and still counts. The revised Part 4 now says exactly this for A3.

## Status of first-pass findings

| Id | Finding and reason | Status in the current text |
| --- | --- | --- |
| H1 | The four-action ceiling failed with several seating enemies, because A2 was per enemy. "Qualifies" and the handling of running rows were undefined. | Resolved. A2 is one row aimed at the strongest seating enemy, A1 hides at Defecting and Collapsing, and the "Rows by situation" table caps the category at four. Running actions are not buttons, and their timers show in the spirit or decision row. |
| H2 | Lowering Wavering by one band was undefined, although A1 ranks first at Wavering (P7). | Resolved in Part 4 "Strength". The spirit stays for records with no modifier values, and Open Gates cannot start. See N14. |
| H3 | Raw versus effective band was undefined for visibility, costs, records, the Evolution IV threshold, Open Gates, and achievements. Reading the effective band would hide A4 right after A3. | Resolved by the Part 4 "Raw and effective band" table. |
| H4 | The B1 threshold formula mixed units, could not be computed in a trigger, and hid every requirement in visibility. | Resolved. The compliance ladder, units, visible and available split, tooltip values, and post-war rule are in place, and Part 6 now allows requirement values in tooltips. See N8. |
| H5 | Part 4 had no Fallout rule, although A2 and Purge write collaboration and the depth record survives the reset. | Resolved in Part 4 lines 16 and 124 and the cleanup list. See N18 for the matrix. |
| H6 | Auxiliary prices did not match the divisions created, so B2 could create units. | Resolved. Part 3 fixes a six-battalion template, and Part 4 prices each division from it. See N15. |
| M1 | A1 was weak in baseline wars and could be retaken all war by AI. | Resolved by the A1 visibility rule and the AI zero-weight and once-per-war rules. |
| M2 | A1's capitulation effect had no hook, order, or reader. | Resolved by the one-day follow-up in "A1 at capitulation". See N13. |
| M3 | The A2 and Purge call shape, clamp, and read path were undefined, and Part 1 claimed other sources stayed untouched. | Resolved in "How reductions work". See N2 and N3. |
| M4 | `ai_hint_pp_cost` must be static while quotes vary. | Resolved in prompt requirement 5. |
| M5 | Targeting and category visibility could scan every country. | Resolved in Part 4 line 14 and prompt requirement 8. See N1. |
| M6 | A3's transport choice and the factory output display broke the inline rules. | Resolved in the cost paragraph and prompt requirement 3. |
| M7 | Stability penalties stacked, and A4 had no floor. | Resolved by the shared floor and one refreshed Purge spirit. See N7 and N8. |
| M8 | A5 was mislabelled, stayed visible after capitulation, could not be paid without convoys, and appeared for subjects. | Resolved in the A5 row and the AI rule. See N6. |
| M9 | B1 allowed subjects as installers, ignored the Part 3 route outcome and vanilla governments, and had no war rule. | Resolved in B1 visibility. See N1. |
| M10 | B2's stage effect, scaling, and counters were undefined. | Resolved in the B2 row and Limits. |
| M11 | An install, annex, and reinstall loop reset the price and could farm Chaos. | Resolved by the three-year count, the 365-day reinstallation cooldown, and the Chaos row limit. |
| M12 | Screen during Loyalty Commissions was nearly free. | Resolved in the vetting lifecycle and the edge case matrix. |
| M13 | The header could exceed four values. | Resolved. Measure names only, with no remaining days. |
| M14 | "Per war" had no war identity. | Resolved by Part 3 "War-scoped guards". |
| M15 | Only the Evolution IV disable case was covered. | Resolved by the Part 4 disable table. See N10. |
| L1 | Two band vocabularies were mixed. | Resolved. The A2 tooltip names the enemy band, and the A5 tooltip uses plain words. |
| L2 | Amnesty had no upside. | Resolved by the 90-day state modifier. See N12. |
| L3 | The AI section had gaps. | Resolved. S4 is referenced, installed governments are covered, and the B1 core count is set. See N5, N16, and N17. |
| L4 | Prepared Governments had no total row cap. | Resolved by the six-row cap. See N9. |
| L5 | Minor and major anchors were a two-step scale. | Resolved by linear scaling between two core-state counts. |
| L6 | The picture reference path had drifted. | Resolved. The asset prompt names both paths. |
| L7 | The prompt omitted the newer custom-cost rules. | Resolved in prompt requirement 2. |
| L8 | Whether `days_re_enable` counts from completion or removal was unverified. | Moved to the prompt's engine checks. |
| L9 | The order of seat multipliers and caps was unstated. | Resolved in Part 3 line 71. |

## Residual and new findings on the revised text

No High findings remain.

### Medium

**N1. The vanilla collaboration-government check in B1 needs a narrow route.**

- Where: Part 4 B1 "Visible when" ("No living collaboration government exists for its original tag, whether installed through Event 097 or through vanilla"). Part 4 line 14 and prompt requirement 8 ("Nothing searches every country").
- Problem: Event 097's hooks never see a vanilla collaboration government being created, so its registry cannot answer this check. A plain `any_country` check would break the promise in line 14.
- The wiki documents `any_country_with_original_tag` with `original_tag_to_check` (Triggers line 107). Combined with `has_autonomy_state = autonomy_collaboration_government`, it gives a narrow check.
- The only repo use passes a literal tag (`024_video_game_in_sweden_triggers.txt` line 40). It is unverified whether `original_tag_to_check` accepts a scope such as FROM.
- Fix:
  - Name this route in Part 4.
  - Run the check in `target_trigger` (daily), not in `visible`.
  - Add a prompt engine check for whether a scope is accepted, with `meta_trigger` injecting the target's original tag as the planned form if it is not.

**N2. Purge cannot read the value before control changes.**

- Where: Part 4 "How reductions work" ("Purge reads the value in the same hook, before the retaken state's control changes, if the hook order allows that read"). Also the promise that the Collaborators Unmasked text shows the enemy's band before and after.
- Problem: The wiki (On actions line 450) gives `on_state_control_changed` ROOT as the new controller, so the hook runs after the change. If the retaken state was the enemy's last occupied core of the owner, the occupation-tied read has nothing to read.
  - In that case only a native negative change that stops at zero can work, and the "before and after" band text cannot be computed.
- Fix:
  - State that in the last-core case Purge depends only on native clamping, and is a reported blocker without it.
  - For text only, read the band from a value cached on the seat marker when the seat was created. Never use that cache for a write.

**N3. The new "accepted" alternatives lack a recorded acceptance basis.**

- Where: Part 4 "How reductions work" ("is an accepted equivalent for A2"), A3 trucks, and A5 trucks for landlocked countries.
- Problem: `AGENTS.md` "Specs and Plans" requires each accepted claim to record its basis, either an explicit user decision or parent acceptance within the user's scope. Rule 17 forbids unapproved fallbacks. This audit recommended these routes only with acceptance. A spec label or this report does not supply that basis.
- Fix: Record the acceptance basis beside each item, or mark it `unresolved` until the parent or user accepts it.

**N4. The probability matrix still tests a removed rule.**

- Where: Matrix S5, line 105 ("P23 checks both conditions together and that A2 hides when all five actions qualify").
- Problem: The five-action A2 rule no longer exists. A1 now hides at Defecting and Collapsing, so P23 should see A2, A3, A4, and A5.
- Fix: Replace the clause with "and that only A2, A3, A4, and A5 are visible".

### Low

**N5.** Part 6's "Installed government" row says installed governments use A1 and A3. Part 4 says they use A1 to A4. Align Part 6.

**N6.** The A5 transport rule is stated two ways.

- The A5 row says convoys for a coastal country and trucks for a landlocked one.
- The cost paragraph and prompt requirement 3 say A5 shows its transport "the same way" as A3, which means by availability.
- Choose one. Under the coastline rule, a coastal country with no convoys still cannot pay.

**N7.** Part 1 sets the Screen floor at 30 percent stability, while A1 and A4 use 20 percent. A1 applies the same spirit penalties as Screen. Align the floors, or add one sentence saying why wartime commissions accept a lower floor.

**N8.** Boundary conventions are open.

- The A1 AI rule says "past 10 percent" surrender progress, while matrix P22 tests exactly 10 percent.
- The ladder row "60 points or more" needs a small offset because `has_collaboration` only accepts `<` or `>`.
- The "20 percent" stability floor does not say whether it is inclusive.
- Fix: State one inclusive convention in the constant group and apply it to all three, consistent with prompt requirement 2.

**N9.** The six-row cap in Prepared Governments hides rows through visibility, which also hides them from AI. The skill's selected-target pattern keeps every target visible to AI. Ranking by "fewest controlled cores" also needs an order kept by the hook that maintains the target list. Fix: Apply the cap only to human players, and compute the rank in that hook.

**N10.** When Administrations in Waiting is disabled, "existing seats end at their next evaluation", but seats are event-driven and have no scheduled evaluation. Fix: State when they end, either at that state's next control change or through a bounded one-time pass when the evolution is disabled.

**N11.** A2 targets "the seating enemy with the strongest network". The AI rule no longer gives a tie-break. Fix: State whether the comparison uses the numeric value or the band, then break ties by most seated states and then randomly.

**N12.** The Amnesty modifier names (local factory output and recruitable population in one state) must be verified against the installed modifier documentation, as Part 3 requires for the Fifth Column.

**N13.** The A1 capitulation follow-up should skip states whose controller changed during the one-day delay. Examples are states handed to a government installed by the capitulation offer, and retaken states.

**N14.** Part 3 line 69 grows seat compliance "while the Fifth Column is active". Part 4 makes the seat bonus read the effective band. Fix: Say that the bonus does not apply when the effective band is below Wavering.

**N15.** If spawned divisions arrive without equipment, Part 4 sends the paid equipment to the government but says nothing about the paid manpower.

- The six-battalion template also makes B1 far more expensive than the earlier anchors, with up to six divisions per installation.
- Fix: State the manpower handling, and add B1 affordability to Part 6 balance scenario 5, so the target of one to four installations per year is checked against real stockpiles.

**N16.** At Defecting and Collapsing, the AI ordering ranks A3, A4, and A2 but does not place A5. Fix: Add its rank.

**N17.** The B1 AI rule requires at least three controlled cores, so AI never uses B1 on one- or two-state targets. Fix: Confirm that this is intended. The capitulation offer still covers those targets.

**N18.** Matrix P26 (Fallout, Event 097 disabled, one evolution disabled) appears only in the scenario table, with no expected results. Fix: Add expectations under S4, S5, and S6: categories hidden, zero willingness, no Purge write, and running modifiers expiring on their own timers.

## Clarity of player-facing values (question 3)

The revised text covers what the player needs.

- The effective band is shown, with a held-down note.
- The A2 tooltip names the target enemy and its band.
- The A5 tooltip states its effect in plain words.
- B1 shows current and required compliance and network depth.
- The A1 and A4 stability floor is named.

The networks reading deliberately does not fall after A2 or Purge, and the A2 tooltip and the Unmasked text carry the per-enemy change instead. In the last-core Purge case, that text depends on N2.

## Cost-count table per action (current text)

| Action | Spendable cost types | Of which timed-modifier costs | Inline values | Texticons | Verdict |
| --- | --- | --- | --- | --- | --- |
| A1 Loyalty Commissions | 3: political power, stability (spirit), consumer goods (spirit) | 2 | 3 | `£pol_power`, `£stability_texticon`, `£consumer_goods_texticon` | Within limits |
| A2 Arrest the Prepared Officials | 3: manpower, infantry equipment, political power | 0 | 3 | `£manpower_texticon`, `£infantry_equipment_text_icon`, `£pol_power` | Within limits. The quote follows the current target's band. |
| A3 Evacuate the Ministries | 3: trains or trucks (one charged), factory output (timed), political power | 1 | 2. Factory output is in the effect tooltip | `£GFX_train_texticon` or `£GFX_motorized_equipment_text_icon`, `£pol_power` | Within limits |
| A4 Commissars in the Ministries | 3: command power, army experience, stability (timed) | 1 | 3 | `£command_power`, `£army_experience`, `£stability_texticon` | Within limits. Command power of 25 or 40 is under the cap of 60. |
| A5 Charter a Government in Exile | 2: political power, convoys or trucks (one charged) | 0 | 2 | `£pol_power`, `£convoy_texticon` or `£GFX_motorized_equipment_text_icon` | Within limits. See N6. |
| B1 Seat the Prepared Government | 3: political power, infantry equipment, manpower | 0 | 3 | `£pol_power`, `£infantry_equipment_text_icon`, `£manpower_texticon` | Within limits. Per-target quotes depend on an engine check in the prompt. |
| B2 Arm the Installed Administration | 3: infantry equipment, manpower, political power | 0 | 3 | as B1 | Within limits |
| Purge (event option) | 1: stability (timed) | 1 | No cost row. Shown in the option tooltip | `£stability_texticon` | Within limits |
| Amnesty (event option) | 0 | 0 | none | none | No cost |

Among these, the mod itself defines only `GFX_motorized_equipment_text_icon` and `GFX_support_equipment_text_icon` (`interface/chaosx_texticons.gfx`). The others are used widely in mod localisation but are defined outside the mod, presumably in vanilla. No factory output texticon exists in the mod. No action mixes a requirement into its cost string.

## Visible-action density check (current text)

The "Rows by situation" table in Part 4 is consistent with the visibility rules.

| Situation | Rows |
| --- | --- |
| No Fifth Column | A1, A2, A5 at most |
| Wavering | A1, A2, A5 at most |
| Defecting and Collapsing | A2, A3, A4, A5 at most |

Each action contributes one entry, either a button or a running timer row. Divided Loyalties therefore stays at four or fewer, and Prepared Governments at six or fewer, subject to N9.

## What could not be verified

- Everything that needs installed vanilla files or vanilla documentation, including `common/decisions/_documentation.md`, the dynamic variable documentation, the vanilla collaboration-government decision and scripted effect, and the vanilla texticon definitions.
- Whether `add_collaboration` accepts negative values and stops at zero.
- The scale of the `has_collaboration` and `core_compliance` game variables, and what the read returns after the last occupied core is lost.
- Whether `core_compliance` accepts a variable, and whether `original_tag_to_check` accepts a scope.
- The order of scripted capitulation hooks relative to the engine's collaboration-to-compliance conversion. The one-day delay avoids depending on it.
- Whether `instantiate_collaboration_government` applies its own ideology or compliance conditions, and whether the government's `original_tag` equals the host's.
- How `create_unit` equips divisions, and the manpower and equipment of an ordinary infantry battalion.
- Whether `days_re_enable` counts from completion or removal, and how running decision rows render.
- Whether scripted localisation in `custom_cost_text` can show per-target quotes for targeted decisions.
- Whether surrender progress resets after capitulation.
- All AI willingness and probability conclusions. No `hoi4.probability_*` route was available, so the AI review is source reading only and stays unresolved under the matrix's evidence rules.
- Header layout and picture rendering. No `hoi4.gui_inspect` or `hoi4.gui_render` was available.
