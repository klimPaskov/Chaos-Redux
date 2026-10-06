# Event 097 Collaboration: Decision and Mission Design Audit

- Role: `chaosx_decision_mission_auditor`, audit-only design-review mode.
- Date: 2026-10-06.
- Evidence class: design review of a planning specification, source review of repository precedents, offline wiki snapshot under `paradox_wiki/`. No HOI4 MCP evidence, because `hoi4_agent_tools` failed to connect in this session. No vanilla game files or vanilla documentation, because the Windows Steam paths do not exist in this Linux container.
- Disposition: unresolved audit findings for parent review.
- Files written: this report only. No spec, prompt, gameplay, localisation, or asset file was edited.

## Spec version audited

Part 4 and the other spec parts were edited while this audit ran. Part 4 was last modified at 14:53 UTC on 2026-10-06. Parts 1, 2, 3, and 6 and the probability matrix also differ from the committed versions. This report reflects the working-tree text re-read after those edits.

These earlier findings are resolved by the current text:

- The A1 plus A3 band contradiction is fixed. Part 4 now says "A1 or A3 drops a Collapsing host to the Defecting band".
- A3 visibility now matches matrix P7. A3 is visible only at Defecting or Collapsing.
- The unreachable B1 example (a 20-point network needing 70) is gone. The text now gives a reachable range down to about 67 percent.
- Cleanup now says "Measures already running finish their duration". This closes the refund risk of penalties ending when the Fifth Column ends. The implementation must still avoid `cancel_if_not_visible` and any Fifth Column cancel on A3 and A4.
- The A2 AI rule now defines "can spare the manpower" (available manpower at least twice the cost) and a target order. B1 now has a target preference.
- A five-action case is handled by hiding A2 when all five actions qualify. See H1 for the remaining gap.

## Sources reviewed

- `AGENTS.md`.
- Decision skill. The uploaded copy at the session scratchpad was treated as the newer authority. Compared with the repo copy at `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, it adds:
  - the six-primary-action note
  - the `<base>`, `<base>_blocked`, and `<base>_tooltip` custom-cost key rule
  - inclusive affordability checks
  - the rule that `ai_hint_pp_cost` must never be assumed dynamic
  - the trigger evaluation cost section
  - the `days_remove` rule for decision-level modifiers
- `chaos-redux-scripted-gui` "Content and interaction budget", and the `chaos-redux-events` sections on spec fidelity, writing, evolutions, and scripted GUI presentation.
- Spec Parts 1, 2, 3, 4, 5 (Fallout and restoration sections), and 6, the decision prompt, the AI probability matrix, the edge case matrix, the research notes, and `docs/plans/097_collaboration_plans/subagent_handoffs/097_repo_explorer_handoff.md`.
- Precedents:
  - Categories: `common/decisions/categories/033_acid_rain_categories.txt`, `039_murder_mystery_categories.txt`, `famine_decision_category.txt`, `migration_decision_category.txt`, `condemnation_sanctions_categories.txt`, and `fallout_consolidated_categories.txt`.
  - Custom costs: `common/decisions/migration_decisions.txt` (custom costs with `£GFX_train_texticon`) and `common/decisions/016_brilliant_scientist_containment_decisions.txt` (a timed consumer goods modifier counted as a cost and shown inline).
  - `core_compliance`: `common/decisions/formable_nation_decisions.txt` lines 1198 to 1210.
  - Texticons: `interface/chaosx_texticons.gfx` and the `£` tokens used across `localisation/english/`.
- Wiki: Decision modding (costs lines 305 to 335, timers lines 337 to 355, targeted decisions lines 514 to 560), Effects (`add_collaboration` line 1246, `instantiate_collaboration_government` line 4723), Triggers (`has_collaboration` line 642, `core_compliance` line 1158, exile triggers lines 976 to 979), and Data structures game variables (`core_compliance`, `has_collaboration` near line 1512).

## How the skill classifies timed-modifier costs

The skill's hard cost budget counts anything an action "consumes, removes, reduces, or commits as payment". Its cost list names stability, civilian factory burden, and military factory output loss as cost types. A timed stability penalty or a timed factory output penalty that the player accepts as the price of an action is therefore a spendable cost type. It counts toward the four-type limit and is not a non-consumed requirement.

The repository precedent agrees. `016_brilliant_scientist_containment_decisions.txt` counts a decision-level consumer goods `modifier` with `days_remove` among its four cost types and shows it inline with `£consumer_goods_texticon`.

Any such cost shown in the cost row needs a correct texticon. Stability and consumer goods have texticons in use. Factory output has none in the mod. It must either receive a new texticon or appear as the action's timed modifier in the effect tooltip, and it still counts toward the budget.

Counting the modifiers this way does not push any Part 4 action past four cost types. It does affect the inline display and texticon rules for A3. See the cost-count table.

## Findings, sorted by severity

### High

**H1. The four-action ceiling still fails with several seating enemies, and "running actions are not shown" is undefined in engine terms.**

- Where: Part 4 "Divided Loyalties decisions" (the paragraph that sets the ceiling and the A2 hide rule) and prompt requirement 1.
- Problem 1, several seating enemies: A2 is per enemy (120-day cooldown per enemy, AI target order across enemies), so it is a targeted decision with one row per seating enemy. The new rule hides A2 only while all five actions qualify.
  - Once any measure is running, A2 returns.
  - At Defecting with A3 running and two seating enemies, the visible rows are A1, A4, A5, and two A2 rows, which is five.
  - With three seating enemies it is six, the hard maximum of the content and interaction budget.
- Problem 2, "qualifies" is undefined: The spec does not say whether an action qualifies on visibility alone or also on affordability. If affordability counts, A2 will appear and disappear as stockpiles change.
- Problem 3, running rows: The wiki (Decision modding line 341) says a decision with `days_remove` keeps its timer in the list until it is removed. The newer skill requires `days_remove` on every decision-level `modifier`. If A3's factory output penalty or A4's stability penalty is a decision-level modifier, the running decision stays listed, which conflicts with "not shown as a button". The spec does not say whether a running timer row counts toward the ceiling.
- Fix:
  - Count A2 as at most one visible row. Either aim one untargeted row at the seating enemy the AI rule already prefers (highest band, then most seated states) and name it in the tooltip, or show the targeted row only for that enemy.
  - Define "qualifies" as "visibility conditions met and not running or cooling down", excluding affordability.
  - Either implement A1, A3, and A4 effects and penalties as timed ideas or dynamic modifiers with timed flags, so the decision itself disappears after the click, or state that a running timer row is allowed and does not count toward the ceiling.

**H2. "One band lower than Wavering" is undefined, and A1 is the top action at Wavering.**

- Where: Part 4 A1 row ("the Fifth Column counts one band lower"). Matrix S5 P7 ("A1 ranks first" at Wavering).
- Problem: The matrix expects A1 first at Wavering, but the spec never says what lowering Wavering by one band does. It could suspend every Fifth Column effect for the run, or it could do nothing. The answer decides whether A1 is worth taking in P7.
- Fix: Add one sentence: "Below Wavering, the spirit stays for records, its modifier values are zero, and Open Gates cannot start." Alternatively, say that A1 has no band effect at Wavering, and rebalance P7.

**H3. The spec never says whether each consumer reads the raw band or the effective band.**

- Where: Part 4 A1 to A4 rows, the A3 and A4 hide rule ("falls below Defecting"), the dynamic cost table (A1 stability surcharge at Collapsing, A3 political power discount at Collapsing), the header, and the AI orderings. Part 3 "Cleanup" (highest band recorded per war) and "Qualification threshold" (Collapsing lowers the threshold to 30). Part 6 achievements that read the band.
- Problem: A1 and A3 make the Fifth Column count one band lower. The spec does not say whether the following read the raw band (from surrender progress) or the lowered band:
  - A4 visibility and the A3 and A4 hide rule.
  - The A1 stability surcharge.
  - The A3 discount.
  - Open Gates eligibility.
  - The header.
  - The recorded highest band.
  - The Evolution IV threshold.
  - Achievements.
- Each choice changes play.
  - If the hide rule reads the effective band, taking A3 at Defecting lowers the host to Wavering and immediately hides A4. That breaks the stated rule that A3 and A4 stack.
  - If the recorded band is the effective band, A1 at Collapsing denies the occupier the lower installation threshold.
- Fix: Add a short rule table to Part 4.
  - The raw band drives visibility and hiding, dynamic costs, the recorded highest band, the Evolution IV threshold, and achievements.
  - The effective band drives the spirit's modifier values, Open Gates eligibility and timing, and the seat bonus.
  - The header shows the effective band and says that the measures are holding it down when they do.
  - The design owner may choose another split, but one must be written down.

**H4. The B1 reduced compliance threshold is still not implementable as written.**

- Where: Part 4 "Reduced compliance threshold" and the B1 row. Part 3 "Qualification threshold". Part 6 "Decision texts".
- Problems:
  - (a) The units are mixed. The wiki gives `add_collaboration` and `has_collaboration` a 0 to 1 scale, while the formula uses points. The snapshot does not document the scale of the `has_collaboration` game variable.
  - (b) The read path is not named. The wiki ties `has_collaboration` and `core_compliance` to target cores occupied by the scope. B1 satisfies this, but the spec should say so and name the reader.
  - (c) Rounding and inclusivity are missing. The text says "about 67 percent". `core_compliance` requires `<` or `>`, and the wiki lists its value as an integer, so "at least 67.5" has no defined form.
  - (d) A trigger cannot compute "80 minus half of a value". The only repo precedent (`formable_nation_decisions.txt` lines 1198 to 1210) uses a literal. Whether `value` accepts a variable is unverified.
  - (e) Every requirement sits in "Visible when". The decision appears without warning, and the player cannot plan toward the compliance target. Showing that target would currently break Part 6, which says decision text must not reveal hidden thresholds.
  - (f) Part 3 clears the Collapsing reduction and the A5 surcharge "when the war ends", but B1 can be used after a war against a target in exile. The spec does not say which threshold applies then.
- Fix:
  - Replace the formula with one of two implementable forms.
    - A band ladder of script constants that a pure trigger can check, for example: a network of at least 60 needs compliance above 50, at least 50 needs 55, at least 40 needs 60, and at least 25 needs 67. Write each pair as `has_collaboration` and `core_compliance` comparisons.
    - Or a cached threshold variable that only the existing capture and capitulation hooks refresh, injected through `meta_trigger`.
  - State the units: collaboration on a 0 to 1 scale and compliance on a 0 to 100 scale.
  - Split B1 into two blocks.
    - Visible: the target has capitulated or is in exile, we control at least one of its cores, no living government exists for its original tag, and the installer is eligible.
    - Available: the network and compliance conditions, with a custom tooltip that names the current average compliance and the required value.
  - Amend Part 6 so that requirement values the player acts on are shown while formulas stay hidden.
  - Say whether a post-war B1 uses the ordinary threshold of 40.

**H5. Part 4 still has no Fallout rule.**

- Where: Part 4 "Decision cleanup" and the category table. Part 1 "Cleanup and persistence" and Part 5 "Fallout" require every Event 097 write to check the Fallout gate, and require evolution behaviors to stop creating consequences once the transition begins. Matrix P26 names a Fallout scenario but states no decision expectations.
- Problem: Several Part 4 surfaces ignore the Fallout gate.
  - A2 and Purge write to native collaboration.
  - B1 creates a new consequence.
  - Divided Loyalties visibility reads the incoming depth record, which Fallout does not reset. After the Fallout reset the category would stay open, with actions about networks the engine no longer holds.
  - P26 therefore has no rule to test against.
- Precedent: `air_cleanliness_treaty_category` in `fallout_consolidated_categories.txt` hides on `fallout_transition_active` and `fallout_active`.
- Fix: Add these rules to Part 4 and give P26 matching expectations.
  - Both categories hide while `fallout_transition_active` or `fallout_active` is set.
  - A2 and Purge check the Fallout gate before any write.
  - Collaborators Unmasked does not fire during or after the transition.
  - B1 and B2 hide.
  - State whether running spirits and modifiers expire on their own timers or are removed.

**H6. Auxiliary costs are not tied to the divisions they create, so the "transferred, not created" guard is unproven.**

- Where: Part 4 B1 and B2 cost tables, the exploit row "Using B2 as a free unit loop", and Part 3 "Local auxiliaries".
- Problem: Part 3 does not fix the size of the auxiliary template. B1 charges 500 infantry equipment and 2,000 manpower per division, and B2 charges 1,000 and 4,000 for two divisions. If the template holds several ordinary infantry battalions, each division needs more than it pays for. Battalion values could not be checked against vanilla here.
- Whether `create_unit` spawns divisions fully equipped is unverified. If it does, B2 creates equipment and manpower, and annexing the subject hands those divisions to the installer. The exploit table asserts the opposite without evidence.
- Fix:
  - Fix the battalion count of the auxiliary template in Part 3.
  - Derive the per-division cost from that template's needs through script constants, so payment covers what the divisions hold. Alternatively, spawn the divisions understrength and transfer exactly the paid stock to the government.
  - Add an implementation check of how `create_unit` equips divisions.
  - If annexation is allowed while B2 uses remain, count B2 uses against the installer as well as the government.

### Medium

**M1. A1 has little effect early in a campaign, yet it opens in every war.**

- Where: Part 4 category table and A1 row. Part 6 actor groups. Matrix P22 and P25.
- Problem: Divided Loyalties opens for every participant at war with another participant once any layer exists.
  - Without Administrations in Waiting or The Fifth Column, A1 only cuts compliance at our capitulation by a quarter of each occupier's collaboration.
  - That is about 4 points after one firing. It reaches 25 points only near the native cap, which Part 1 now expects in long campaigns with a small event pool.
  - In early wars A1 costs political power plus 10 percent stability and 10 percent consumer goods for 180 days, for a small effect. That is weak under the skill's effect-strength rule.
  - The AI ordering also allows A1 every 270 days through a long war, which drains stability across many AI countries.
- Fix:
  - Show A1 only when incoming networks are at least Deep (matching P22), when Administrations in Waiting or The Fifth Column is active and enabled, or when a participant enemy controls one of our cores.
  - Allow AI one A1 per war unless the Fifth Column is active.

**M2. A1's capitulation effect has no defined hook, order, or reader.**

- Where: Part 4 A1 row.
- Problem: "Every occupier's capitulation compliance is reduced by a quarter of its collaboration inside us" leaves four things undefined:
  - the hook (`on_capitulation` or `on_capitulation_immediate`)
  - the order relative to the engine's collaboration-to-compliance conversion
  - how the reduction is applied (`add_compliance` in each host core state that the occupier controls)
  - how each occupier's collaboration is read
- The order is unverified. A reduction that runs before the engine conversion could be overwritten.
- Fix: Write the rule as: "In the capitulation hook, after the engine conversion, for each participant enemy that controls host cores, subtract a quarter of its collaboration in compliance points from each of those states, never below zero." Require the implementation to verify the hook order. If the order is wrong, the parent decides whether a one-day delayed event is an accepted alternative. It must not be used silently.

**M3. The A2 and Purge reductions are not precise enough to implement.**

- Where: Part 4 A2 row and the paragraph below the table, Collaborators Unmasked, and prompt requirement 6.
- Problems:
  - The call shape is not stated. Per the wiki it is `add_collaboration` in the enemy's scope with `target` set to the host and a value of minus 0.15 for A2 or minus 0.10 for Purge.
  - "Relative" can be misread as a proportional cut.
  - Clamping at zero is unverified.
  - Purge fires after the owner retakes a seated state. If that was the enemy's last occupied core, the occupation-tied read has nothing to read, so a read-and-clamp guard cannot work there.
  - The spec forbids an absolute set. A `set_collaboration` computed from the current native value minus the delta keeps other sources and gives the same result, but it is not mentioned.
  - The spec does not say whether the incoming depth record or the header reading falls after A2 or Purge.
  - Part 1 says collaboration from other sources "stays untouched", but A2 lowers the native total, which includes collaboration from vanilla operations.
- Fix:
  - Write the call shape and the units.
  - Replace "relative reduction" with "subtract a fixed number of points from the current value".
  - Allow a computed `set_collaboration` only where the current value can be read in an occupation context, and only with parent acceptance.
  - For Purge, read the value before control changes, or rely on engine clamping once that is verified.
  - State what happens to the header reading after A2 or Purge.
  - Narrow the Part 1 sentence to "never overwritten", and say that A2 and Purge lower the native value whatever its source.

**M4. `ai_hint_pp_cost` cannot follow the dynamic political power quotes.**

- Where: Part 4 dynamic cost tables and prompt requirement 4.
- Problem: Wiki Decision modding line 335 says the hint must be a constant. Political power varies by minor or major status, by the Collapsing discount (A3), and by held governments (B1, 25 more for each). The newer skill forbids assuming that the hint can be dynamic.
- Fix: In the prompt, have each decision use a static file-scoped hint mirrored from its script constant at the highest quote that action can reach, as `016_brilliant_scientist_containment_decisions.txt` does. Where a lower quote must stay reachable for AI, omit the hint instead. Record the choice per action.

**M5. The targeting mechanism and its evaluation cost are unspecified.**

- Where: Part 4 A2, B1, B2, and the Prepared Governments category visibility.
- Problem: A2, B1, and B2 are targeted decisions, but the spec does not say how targets are chosen.
  - Without `target_array` or `targets`, `target_trigger` runs daily against every country, for every participant that sees the decision. That comes close to a daily world scan.
  - Category `visible` blocks run every frame, and "when it has a valid target" would need `any_country`. The `condemnation_participant_action_category` precedent shows that pattern, and it should not be copied.
  - The 180-day B1 cooldown applies per installer, but native `days_re_enable` applies per target.
- Fix: Specify arrays that the event maintains.
  - For each host: the enemies holding seated states, written by the seat and recapture hooks.
  - Globally: capitulated or exiled B1 targets, written by the capitulation and exile hooks and the Evolution IV entry pass.
  - For each installer: its live registry rows, for B2.
  - Use `target_root_trigger` for installer prechecks.
  - Gate Prepared Governments on a country flag set by those hooks.
  - Implement the per-installer B1 cooldown as a timed country flag whose duration comes from a variable.

**M6. A3's payment rule and display break the inline cost rules.**

- Where: Part 4 A3 row and cost table.
- Problem: "Trains or trucks" does not say which one is debited when both are available, how the player chooses, or what AI does. Showing both inline needs a filler word and a fourth inline value, which breaks the three-value rule. The mod has no factory output texticon, and `£civ_factory` and `£mil_factory` mean factory counts, so they would be wrong.
- Fix:
  - State the rule, for example: "Pay trains when the country holds enough, otherwise trucks, and show only the resource that will be debited."
  - Show the factory output penalty in the effect tooltip as a timed modifier lasting 120 days. Following H1, it should be a timed idea or dynamic modifier rather than a decision-level `modifier`. It still counts as a cost type. The alternative is to create and wire a correct texticon.

**M7. Stability penalties stack, and A4 has no stability floor.**

- Where: Part 4 A1, A4, and Purge. Part 1 now sets a 30 percent stability floor for the Screen stance.
- Problem: At Collapsing a host can carry all of these at once:
  - the Fifth Column's 15 percent stability loss
  - A1 at 15 percent
  - A4 at 10 percent
  - one or more Purge penalties of 10 percent each
- Only A1 has a stability requirement, and its threshold is still "civil-war risk" with no number. The spec does not say whether the A1 floor binds human players. It also does not say whether repeated Purge penalties from different enemies stack or refresh.
- Fix: Give A1 and A4 a named stability floor constant in `available` for every country, with a custom tooltip that names it, and say whether it reuses the 30 percent Screen anchor from Part 1. State whether repeated Purge penalties refresh one timed idea or stack. Matrix P15 then follows from that floor.

**M8. A5 has gaps in eligibility and lifecycle.**

- Where: Part 4 A5 row, cleanup, and the AI section.
- Problems:
  - The phase is labelled "Exile", although A5 must come before capitulation (Part 3 says "before capitulating"). A5 is not hidden after capitulation.
  - "Once per war" and "for this war" have no defined war identity.
  - "An enemy with a Strong network" should read "at least Strong".
  - Countries with no convoys cannot pay, including most landlocked states.
  - In the AI rule, "the enemy most likely to install a government" is undefined. If Part 3's democratic or non-aligned installation is refused by the engine, A5 against such an enemy does nothing.
  - Installed governments and other subjects can see A5.
  - A5 is not covered when Collaboration Governments is disabled.
- Fix:
  - Add `has_capitulated = no` and rename the phase "Before capitulation".
  - Define war identity as in M14.
  - For countries without convoys, a political-power-only quote or another payment needs explicit acceptance. It must not be added as a silent fallback.
  - Define the likely installer as the participant enemy that controls our cores, has the highest band, and can install under the resolved Part 3 route. This matches the Part 3 selector.
  - Hide A5 for subjects and for countries carrying the Event 097 installed-government marker. Also hide it when Collaboration Governments is disabled.

**M9. B1 has eligibility gaps.**

- Where: Part 4 B1 row and the AI section.
- Problems:
  - There is no `is_subject = no` check on the installer, so an installed government, which is itself a participant, could install governments of its own.
  - There is no installer ideology or engine-route check, although Part 3 expects that democratic and non-aligned installation may be refused. The democratic AI line assumes the route works.
  - There is no war requirement, so the post-peace case where the installer owns the cores is undefined.
  - The one-government rule reads only this route's registry, so a vanilla collaboration government for the same original tag does not block a second one.
  - It is unverified whether the vanilla `instantiate_collaboration_government` effect applies its own compliance or ideology conditions, which would override the reduced threshold.
- Fix:
  - Add `is_subject = no` and exclude countries with the installed-government marker.
  - Add a visibility clause that the installer can use the resolved Part 3 route, so B1 is hidden rather than weighted down when the route is refused.
  - Require war with the target, or define the post-peace case.
  - Extend the one-government rule to any living collaboration government with the same original tag, or say why vanilla ones are allowed alongside.
  - Add an implementation check of the vanilla effect's conditions.

**M10. B2's effect and counters are under-specified.**

- Where: Part 4 B2 row and cost table. Part 3 "Installed Administration lifecycle".
- Problem: "Moves 90 days closer to the Entrenched stage" only makes sense in the Imposed stage. Part 3 resets or pauses the Imposed timer when Contested begins, yet the AI prefers B2 for Contested governments. The spec does not say what B2's timer effect does in the Entrenched or Contested stage. B2's cost does not scale. Its three-use counter, if stored on a dynamic tag, may survive tag reuse.
- Fix: State that the timer effect applies only in Imposed, and say what B2 does in Contested (shorten the Contested period, or only raise units). Scale B2's cost with the auxiliary template (H6). Clear the counter when the registry row retires.

**M11. An install, annex, and reinstall loop is open.**

- Where: Part 4 B1 scaling, the exploit table, and Part 3 "Registry cleanup".
- Problem: The B1 price rise counts only living governments. An installer can install a government, annex it, and install again for the same original tag at the base price after 180 days. Each cycle can repeat the installation Chaos row, feed achievements that read the registry, and count toward the Part 6 target of one to four installations per year.
- Fix: Count this installer's installations within a rolling window (a script constant) toward the price, add a reinstallation cooldown per original tag, and limit the installation Chaos row to once per original tag per war.

**M12. Screen during Loyalty Commissions costs almost nothing.**

- Where: Part 4 "Vetting spirit lifecycle". Edge case matrix row "A country chooses Screen while already under Loyalty Commissions".
- Problem: Screen's only price is the vetting spirit. If Loyalty Commissions has a few days left, choosing Screen halves the incoming layer and charges almost nothing. The exploit table does not list this.
- Fix: When Screen is chosen during Loyalty Commissions, extend the spirit so that at least the Screen campaign duration remains, and let it fall back to the Vetting Campaign form when the commissions end.

**M13. The header can exceed the value budget.**

- Where: Part 4 "Presentation choice", the ceiling paragraph ("the header names the running measure instead"), and prompt requirement 9.
- Problem: The header shows the networks band, the Fifth Column band, the strongest network country, and "the active protective measure and its remaining days". A1, A3, and A4 can run together, so the singular "measure" may cover three items. Three measures with timers exceed four simultaneous values.
- Fix: List running measures by name on one short line and show remaining days only in each measure's tooltip. Keep the "compact status block" as category description text rather than an attached scripted GUI, so the category still passes the picture gate.

**M14. "Per war" guards have no war identity.**

- Where: Part 4 A5, Collaborators Unmasked, and the exploit table. Part 3 Open ministries and Open Gates caps.
- Problem: Script has no war id, and overlapping wars make "this war" ambiguous.
- Fix: Clear guards tied to a pair of countries when that pair stops being at war (the peace hook for that pair). Clear guards tied to one host when that host is at peace with every participant enemy. Note that a host who stays at war with one enemy keeps its host guards.

**M15. Disabling an evolution after activation is covered only for Evolution IV.**

- Where: Part 4 cleanup. Edge case matrix row "One evolution disabled after activation". Matrix P26.
- Problem: Part 4 only says that Prepared Governments hides when Collaboration Governments is disabled.
- Fix: Add one row per evolution.
  - Administrations in Waiting disabled: A2 hides, existing seats end at the next evaluation, and Collaborators Unmasked stops.
  - The Fifth Column disabled: the spirit is removed at the next evaluation, A3 and A4 hide, A1's band and Open Gates effects go inert, and the header line hides.
  - Collaboration Governments disabled: A5 and Prepared Governments hide, and B2 counters freeze.
  - In each case, state whether running timed spirits and modifiers expire on their own timers.

### Low

**L1. Part 4 mixes two band vocabularies.** Part 1 uses an aggregate scale (Scattered, Established, Deep, Pervasive at 20, 40, and 70). Part 3 uses a per-enemy scale (Thin, Ordinary, Strong, Total at 15, 40, and 70). Part 4 uses both: the A1 AI rule uses Deep or Pervasive, while A2 and A5 use Strong or Total. The player sees the first in the header and the second only in the Fifth Column tooltip. Fix: Show the enemy's band in the A2 and A5 tooltips, which are valid reads because that enemy occupies our cores. State which scale each condition uses.

**L2. Amnesty has no upside.** It loses to Purge whenever stability can absorb the penalty. Fix: Give Amnesty a visible, bounded benefit tied to the retaken state, such as faster recovery of that state's output for the purge duration. Otherwise, record it as a deliberate do-nothing option.

**L3. The Part 4 AI section has remaining gaps.**

- Collaborators Unmasked is covered only in matrix S4.
- There is no AI rule for the A3 transport choice.
- Installed governments' use of A2, A4, and A5 is not covered. Part 6 mentions only A1 and A3.
- "Large garrisons" (B1) has no constant.

Fix: Reference S4 and add the missing rules.

**L4. Prepared Governments has no total row limit.** "At most two visible decisions per target" does not cap the total, and an installer with many governments and targets can pass six rows. Fix: Show B2 only where it can be taken now (Imposed or Contested stage, uses left, cooldown over). Use the selected-target pattern if the total can still pass six.

**L5. Minor and major anchors give only a two-step scale.** Fix: Scale with core states, factories, or manpower within clamps, as the skill's dynamic-values section prefers.

**L6. The picture reference path has drifted.** The asset prompt and the newer skill name `assets/gfx_references/icons/decision_categories/pictures/`. The repository currently has `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures/` with `contact_sheet.png`. Fix: Point the asset prompt at whichever folder exists when the picture is produced.

**L7. The prompt omits the newer custom-cost rules.** It should name the `<base>`, `<base>_blocked`, and `<base>_tooltip` keys and require inclusive affordability checks just below, at, and just above each quote. The migration precedents use strict `>` comparisons, which the newer skill says not to copy.

**L8. A1's cooldown timing is unverified.** "180 days, then a 90-day cooldown" assumes `days_re_enable` counts from removal, which the wiki does not state. Fix: State the intended uptime and let the implementation verify it.

**L9. The order of the seat bonus and its cap is unstated.** A1 halves seat compliance. The Fifth Column raises it by half and lifts the cap to 50. Fix: State the order of multipliers and caps.

## Clarity of player-facing values (question 3)

The two qualitative readings and the Fifth Column band are enough for choosing between A1, A3, and A4 once H3 says which band the header shows. The player is missing these values:

- Each seating enemy's band, which decides whether A2 is worth it and is needed to read A5.
- Whether measures are currently holding the band down.
- B1's current and required average compliance, and whether our network is deep enough.
- A5's effect in plain words ("a foreign power will need a deeper network here to install a government over us"), because the threshold itself is hidden.
- The stability floor for A1 and A4.

The header reading also never falls after A2 or Purge unless M3 defines that, so the player sees no feedback from those actions.

## Cost-count table per action

Inline values assume the cost row shows each value the skill would count, and that factory output has no texticon.

| Action | Spendable cost types | Of which timed-modifier costs | Inline values | Texticons | Verdict |
| --- | --- | --- | --- | --- | --- |
| A1 Loyalty Commissions | 3: political power, stability (spirit), consumer goods (spirit) | 2 | 3 | `£pol_power`, `£stability_texticon`, `£consumer_goods_texticon` | Within limits. Put the 180-day duration in the `_tooltip` key. |
| A2 Arrest the Prepared Officials | 3: manpower, infantry equipment, political power | 0 | 3 | `£manpower_texticon`, `£infantry_equipment_text_icon`, `£pol_power` | Within limits. |
| A3 Evacuate the Ministries | 3: trains or trucks, factory output (timed), political power. Four if both transports are offered as separate payments | 1 | 3 with one transport and factory output inline. 4 if both transports are shown | `£GFX_train_texticon` or `£GFX_motorized_equipment_text_icon`, no factory output texticon, `£pol_power` | Fails the display rules as written (M6). |
| A4 Commissars in the Ministries | 3: command power, army experience, stability (timed) | 1 | 3 | `£command_power`, `£army_experience`, `£stability_texticon` | Within limits. Command power of 25 or 40 is under the cap of 60. Needs a stability floor (M7). |
| A5 Charter a Government in Exile | 2: political power, convoys | 0 | 2 | `£pol_power`, `£convoy_texticon` | Within limits. Countries without convoys cannot pay (M8). |
| B1 Seat the Prepared Government | 3: political power, infantry equipment, manpower | 0 | 3 | `£pol_power`, `£infantry_equipment_text_icon`, `£manpower_texticon` | Within limits. Static hint issue (M4) and quotes vary per target. |
| B2 Arm the Installed Administration | 3: infantry equipment, manpower, political power | 0 | 3 | as B1 | Within limits. Cost does not scale (M10). |
| Purge (event option) | 1: stability (timed) | 1 | No cost row. Shown in the option tooltip | `£stability_texticon` | Within limits. |
| Amnesty (event option) | 0 | 0 | none | none | No cost. |

The mod itself defines only `GFX_motorized_equipment_text_icon` and `GFX_support_equipment_text_icon` among these (`interface/chaosx_texticons.gfx`). The other tokens are used widely in mod localisation but defined outside the mod, presumably in vanilla. No action mixes a non-consumed requirement into the cost string as written. The A1 stability floor and the B1 compliance and network conditions are requirements and must stay out of the cost row.

## Visible-action density under the current text

Running and cooling-down actions are hidden by the current rule. E is the number of seating enemies, and A2 is counted as one row per seating enemy because it is targeted.

| Situation | Rows in Divided Loyalties |
| --- | --- |
| At war, neither Administrations in Waiting nor The Fifth Column active | A1, so 1 |
| Administrations in Waiting active, E enemies hold seated states, no Fifth Column | A1 and E A2 rows, so 1 + E |
| Fifth Column at Wavering, Administrations in Waiting and Collaboration Governments active, an occupier with at least a Strong network | A1, E A2 rows, A5, so 2 + E |
| Defecting or Collapsing, all evolutions active, nothing running | A1, A3, A4, A5. A2 is hidden by the five-action rule, so 4 |
| Defecting or Collapsing, all evolutions active, A3 running | A1, A4, A5, E A2 rows, so 3 + E. Five with two seating enemies, six with three |

## What could not be verified

- Everything that needs installed vanilla files or vanilla documentation, including `common/decisions/_documentation.md`, the dynamic variable documentation, the vanilla collaboration-government decision, and vanilla `interface` texticon definitions.
- Whether `add_collaboration` accepts negative values and clamps at zero.
- The exact name and scale of the `has_collaboration` and `core_compliance` game variables, and whether the read returns anything after the last occupied core is lost.
- Whether `core_compliance` accepts a variable in `value`.
- The order of scripted capitulation hooks relative to the engine's collaboration-to-compliance conversion.
- Whether `instantiate_collaboration_government` enforces ideology or compliance rules itself, which tag pool it uses, and whether the government's `original_tag` equals the host's.
- Whether `create_unit` spawns fully equipped divisions, and the manpower and equipment of an ordinary infantry battalion.
- Whether `days_re_enable` counts from completion or from removal. Whether a running `days_remove` row counts visually as an action in the category list.
- Whether a vanilla factory output texticon exists.
- Whether scripted localisation in `custom_cost_text` can show per-target dynamic quotes for targeted decisions (FROM scope).
- Whether surrender progress resets after capitulation, which affects A5 visibility.
- All AI willingness and probability conclusions. No `hoi4.probability_*` route was available, so the AI ordering review above is source reading only and stays unresolved under the matrix's evidence rules.
- Header layout and picture rendering. No `hoi4.gui_inspect` or `hoi4.gui_render` was available.
