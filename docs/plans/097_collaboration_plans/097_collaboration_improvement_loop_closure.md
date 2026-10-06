# Event 097 Collaboration: Improvement Loop Closure

- Role: `chaosx_improvement_loop_planner`, plan-only, mandatory near-completion pass of the planning goal.
- Date: 2026-10-06.
- Evidence class: design and source review. There is no HOI4 MCP evidence, because the `hoi4_agent_tools` server failed to connect (`cmd.exe` is not available in this Linux container). No vanilla files or vanilla documentation were available. One web search supplied a historical anchor, cited from its search summary only.
- Disposition: unresolved, for parent review.
- Files written: this file only.
- Package state reviewed: the specification package at commit `07fe1e08`, and the working-tree revision of `docs/plans/097_collaboration_plans/097_collaboration_scripted_architecture_plan.md`, which was still being edited during this pass.

## Recommendation

Closure. Broad expansion is not recommended.

The design delivers the brief. Native collaboration is the only stored power, the layer is global and uniform, each evolution adds one new rule on top of the same networks, and both named connections have a contract. Every player-facing surface answers a moment in a war that the native mechanic creates: a capture, a slide toward defeat, a capitulation, or a government that follows it. The package sits at the upper edge of the brief's limit on event-specific management. Another mechanic, decision, value, rare variant, or asset family would push it past that limit and add maintenance without adding play.

The remaining gaps are contradictions between files, three moments the player never sees, two surfaces that exceed what the brief and the partner events ask for, and one missing Chaos rate guard. Existing events, options, images, and helpers cover all of them. None needs new design depth.

The loop can stop once the parent settles the finalization list below and records each item's disposition. This handoff does not claim that the package is complete. Completion still depends on the parent confirming that no accepted plan is unresolved and on carrying the blockers at the end of this file into the final report.

| Group | Items | Nature |
| --- | --- | --- |
| Required alignment | R1 to R10 | Contradictions, stale statements, or engine conflicts to settle before the package is finalized |
| Recommended cuts and merges | C1 to C3 | Remove or merge surfaces so the event stays inside the brief |
| Recommended small additions | S1 to S3 | Moments built only from existing events, options, images, and helpers |
| Optional | O1 | One effect change on an existing decision |
| Carried blockers | B1 to B4 | Engine, tooling, and user-decision facts the package already reports |

## Answers to the six questions

### 1. Do the four evolutions change play strongly enough?

| Evolution | What changes in play | What the player sees | Verdict |
| --- | --- | --- | --- |
| I Deep Networks | Larger layers, one deepening tranche, prepared cadres after capitulation | A tranche report, a pre-fire opening variant, a state modifier in occupied states, and a report to the exiled host | Mostly numbers. The occupier, who gains from the cadres, receives no report. S1 gives it one. |
| II Administrations in Waiting | Seats on capture, Open Ministries, Collaborators Unmasked | Seat report, Open Ministries report, and a Purge or Amnesty choice | Strong |
| III The Fifth Column | Fifth Column spirit, Open Gates, A3 and A4 | The spirit and its tooltip, and the Open Gates reports. The acquisition report exists only in the localisation direction and the asset prompt (R4). | Strong once R4 is settled |
| IV Collaboration Governments | Offer, B1 and B2, the Installed Administration lifecycle, Turned Regime, competing orders | Offer event, Turned Regime reports, super-event | Strong for the installer. The defeated country receives nothing when a government is installed over it (S2). |

### 2. Does the baseline firing give a meaningful choice and a visible consequence?

The choice is meaningful. Accept costs nothing, Cultivate gives offense at the price of defense, Screen gives defense at the price of stability and consumer goods, and the option tooltips state each consequence in plain terms.

The consequence is hard to see. After one firing every Accept country sits at the second band in both readings, and the engine converts collaboration into compliance at capitulation without any Event 097 surface. A player who chose Cultivate never sees the moment it paid off. S1 adds that moment.

At baseline the only wartime response is A1. Before Evolutions II and III its only effect is a compliance cut after our own capitulation (Part 4, A1 at capitulation), which a player cannot feel while fighting and which is weak for its price. O1 offers a direct counter to the engine's surrender-limit effect, if the parent wants one.

### 3. Does the design stay inside the brief's limit on management systems?

Yes, at the upper edge.

| Role | What the player handles |
| --- | --- |
| Any country | One stance choice per firing |
| Host at war after Evolutions II and III | Divided Loyalties with at most four rows, and at most one Collaborators Unmasked choice per enemy per war |
| Installer after Evolution IV | The offer event and Prepared Governments with at most six rows |
| Original country of an installed government | Nothing to manage, and one qualitative mood line once S2 exists |

There is no currency, no meter with a number, and no scripted GUI. The registry, public contract, restoration inputs, and depth ledgers are hidden infrastructure. A1 to A5, B1 and B2, Collaborators Unmasked, Open Gates, the lifecycle, and Turned Regime each answer a war moment the native mechanic creates, so none of them should be cut. Turned Regime needs the drop rule in R8.

Two parts of the infrastructure go beyond what the brief and the partner events ask for: the cluster depth write (C1) and the sphere registry (C2). One presentation surface uses two vocabularies for one value (C3). These are the cuts and merges this pass recommends.

### 4. Is the aftermath of an installed government complete?

- Event 095 restoration: the contract is complete for a rework that does not exist yet. Event 095 can read one band, target the government, and call Retire.
- Event 063 independence and the installer losing its war: the package states two incompatible rules (R2).
- The original country: it receives no report when a government is installed over it, and the restoration mood that Part 5 makes public has no surface (S2).
- Restoration itself: the original country regains its land with no reckoning, although Event 097 already owns the right choice in Collaborators Unmasked (S3).

### 5. Do the Chaos impact map, achievements, super-event, and assets cover every important moment without padding?

- Chaos: the rows are well chosen, but only one recurring row has a rate guard, and the lifetime estimate is several times lower than the rows allow (R5). One "never changes Chaos" reason is wrong outside Evolution III (R6).
- Achievements: the six cover offense, defense, empire breadth, the rare variant, exile return, and internal collapse without padding. Clean Ministries depends on the size of the event pool (R9), and Two Masters needs a rule for a blocked Turned Regime (R8).
- Super-event: Competing Orders marks a real change in how the world is governed and fires once. C2 removes its only ambiguity, which is whether sphere governments count while Evolution IV is disabled.
- Assets: coverage is complete for the mapped surfaces. The prepared cadres report has no image (R10), and S1 to S3 need reuse notes only.

### 6. Contradictions and stale statements

The parent already fixed these after the audits, so they are not re-reported: the matrix line about A2 hiding at five actions, the Part 6 installed-government row, the A5 transport rule, and the P26 expectations.

| Id | Files | Conflict |
| --- | --- | --- |
| R1 | Part 5 lines 79 to 84, Part 4 line 135, Part 2 line 210 | Sphere route opens from Evolution II while Evolution IV gates the category and the whole package |
| R2 | Part 1 line 245, Part 3 lines 267 and 302, Part 5 line 127, edge matrix lines 24 and 26 | Abandoned stage versus retirement as independent for the same engine outcome |
| R3 | Coding prompt line 66, goal prompt line 14, Part 5 line 59 | Public value list omits the public restoration band |
| R4 | Localisation direction line 57, asset prompt line 34 | A report and image for an event that no mechanic defines |
| R6 | Chaos impact map line 32 | Reason holds only with Evolution III active |
| R7 | Part 1 line 175 | A blocked option cannot stay visible in HOI4 |
| R10 | Part 1 lines 226 and 247, README line 63, Part 2 lines 153 and 222, Part 5 line 125, edge matrix line 28, acceptance criterion 7 | Inaccurate weight-hook reason, unconditional Fallout promise, naming, and wording |

## Finalization list

### Required alignment

**R1. Sphere route against Evolution IV gating.**

- Where: Part 5 lines 79 to 84, Part 4 line 135, Part 2 line 210, architecture plan sections 3.2 and 3.19.
- Conflict: Part 5 opens the offer and B1 inside a registered sphere from Administrations in Waiting onward. Part 4 shows Prepared Governments only while Collaboration Governments is active. Part 2 says a disabled Evolution IV means no offer, no decision, no installed-administration package, no Turned Regime, and no competing orders. The architecture plan follows Part 5, so the implementation would contradict Parts 2 and 4.
- Resolution: settle it through C2. If the parent keeps the sphere registry, Parts 2 and 4 must name the sphere exception, and Part 3 must say whether sphere governments count toward competing orders while Evolution IV is disabled. This pass recommends that they count only while Evolution IV is live.

**R2. One lifecycle rule for a government that loses its installer.**

- Where: Part 1 line 245, Part 3 line 267 (Abandoned entry), Part 3 line 302 (registry cleanup), Part 5 line 127 (Event 063), edge matrix lines 24 and 26, architecture plan section 3.15 and question Q8.
- Conflict: Part 3 sends a government that loses its installer into Abandoned. Part 1, the Part 3 registry cleanup, Part 5, and the edge matrix retire it as independent and remove its spirit. The edge matrix treats installer annexation as Abandoned and Event 063 independence as retirement, although both leave the government without an overlord.
- Recommended rule, replacing all five statements:
  - Contested covers the losing installer. Its condition gains "the installer has capitulated and is still at war", so it holds even if surrender progress resets after capitulation, which the decision audit lists as unverified. Installer capitulation alone no longer starts Abandoned.
  - Abandoned starts when the government stops being a subject of its installer for any reason other than Turned Regime: the installer's annexation, Event 063, or release at a peace conference.
  - An Abandoned row stays in the registry with an abandoned status. It leaves the counts for competing orders, the installer-system Chaos row, Administrations Everywhere, and B2 targets. Its restoration pressure stays readable at the highest band. Competing orders is re-checked when a government enters Abandoned, as it already is when one turns or stops existing.
  - If the former installer makes the government its subject again, the row returns to Imposed with its original route. Event 063 lets the old overlord declare war for exactly that purpose (`events/063_subject_independence.txt`, option a).
  - The row retires when the original country is restored over its territory, when the government stops existing, or after two years in Abandoned. Expiry leaves the former-collaboration marker and the history row for Event 095 and achievements.
- Why: a regime that loses its protector is still a regime of collaborators. That is the Terijoki failure mode the research notes already use for the Abandoned stage, and it gives Event 095 its clearest target. Clean retirement on independence would let a collaboration government drop its whole problem whenever Event 063 happens to pick it.

**R3. The public value list in the prompts.**

- Where: coding prompt line 66, goal prompt line 14, Part 5 line 59, localisation direction line 67.
- Conflict: both prompts limit public values to the two readings and the Fifth Column band, while Part 5 makes the restoration band public "in its exile reports". No exile report exists anywhere else in the package.
- Resolution: the prompts name the restoration mood as a qualitative line shown only in the S2 reports to the original country, with no persistent display. The event then has three persistent public values and one report line, inside the budget. Part 5 names the S2 reports as the carrier.

**R4. The Fifth Column acquisition report has no mechanic.**

- Where: the localisation direction (line 57) and the asset prompt (line 34) define it. Part 3, Part 6, and the architecture event list in section 4.4 do not.
- Resolution: Part 3 sends one report to the host the first time it gains the spirit in a war, to human players, under the host guard rules. Part 6 lists it among the presentation surfaces. The architecture plan gives it an event id. It uses the existing fifth_column image.

**R5. Chaos lifetime estimate and an event-wide rate guard.**

- Where: the Chaos impact map rows for Collapsing, Open Gates, capitulation under the Fifth Column, installation, and Turned Regime, and the lifetime perspective at line 39.
- Problem: only the Collapsing row has a rolling cap.
- Planning arithmetic, not evidence: assume a world war at Chaos 600 or higher with all four evolutions active, five capitulations of participant hosts a year with one of them a major, one Open Gates incident per collapsing host, and the matrix target of one to four installations a year. Every capitulating host passes 60 percent surrender progress on its way to capitulation, so it reaches Collapsing. That gives about +5 from Collapsing after its cap, +10 from Open Gates, +16 from capitulation under the Fifth Column, and +4 to +10 from installations, so roughly 35 to 40 a year. Three such years give about 100 to 150 before the once-per-campaign milestones, against the map's lifetime estimate of 30 to 45.
- Recommendation:
  - Add one event-wide rolling cap on the recurring rows together (Collapsing, Open Gates, capitulation under the Fifth Column, installation, and Turned Regime). A starting anchor of +10 in any 365 days fits the planning skill's band for a national or systemic gain. Once-per-campaign milestones stay outside the cap, and reversals are never capped.
  - Award Open Gates Chaos only for the first incident per host per war, because the capitulation row already measures the collapse that the incidents feed.
  - Restate the lifetime perspective as an output of scenario P27 against a target band the parent chooses, and keep every row value as a tuning anchor.

**R6. Chaos map reason for prepared cadres.**

- Where: Chaos impact map line 32.
- Problem: "the capitulation row already covers the outcome" is true only while The Fifth Column is active. With Deep Networks alone, no Event 097 row covers that capitulation.
- Resolution: state that generic capitulation Chaos covers the capitulation and that prepared cadres only change how the territory is held afterward.

**R7. Screen when its requirement fails.**

- Where: Part 1 line 175, the Screen option in the localisation direction, architecture row V23 and question Q11.
- Problem: the offline wiki (`Event modding`, line 157) says an option whose trigger is false does not appear. Part 1 says Screen stays visible with a blocked tooltip. HOI4 cannot show that natively.
- Resolution: Screen is hidden when its requirement fails, and the Accept option's tooltip names the missing requirement, which is stability below the Screen minimum or an open civil war. Matrix scenarios P4 and P17 keep their expectations.

**R8. Dependent surfaces of a blocked variant.**

- Where: Part 3 Turned Regime and Open Gates engine checks, the Part 6 achievements, the asset prompt, the Chaos impact map, and matrix surfaces S8, S9, S12, and S13.
- Problem: the spec tells the implementation to leave Turned Regime or Open Gates unimplemented if its engine route fails, but it does not say what happens to the surfaces that depend on it. Two Masters would remain as an achievement that can never unlock.
- Resolution: add one sentence per variant to Part 3. If Turned Regime is blocked, Two Masters, the turned_regime image and reports, its Chaos row, the world spacing, and S9 and S13 are removed together and reported as one blocker. If Open Gates is blocked, its reports and image, its Chaos row, and S8 and S12 are removed together, and A3 and A4 drop their Open Gates clause and tooltip line.

**R9. Clean Ministries depends on the size of the event pool.**

- Where: Part 6 line 190 and the achievement prompt.
- Problem: "Screen in at least three firings" is out of reach in most campaigns with every event enabled, where the probability review estimates one to three natural firings in ten years.
- Resolution: "Screen in every Event 097 firing of the campaign, with at least two firings", with the rest of the requirement unchanged. The defender identity stays, and the achievement works for every pool size.

**R10. Smaller text, engine, and naming fixes.**

- Part 1 line 226 and README line 63 say no event-owned weight hook exists. `get_event_weight` in `common/scripted_effects/chaosx_logic_effects.txt` (from line 516) already has a branch for the White Peace event, so the reason is inaccurate. Keeping the ordinary weight remains the recommended choice, as architecture question Q3 also says.
- Part 1 line 247, edge matrix line 28, and acceptance criterion 7 promise that no Event 097 collaboration survives the Fallout reset. That holds only if Fallout's reset sees pairs between countries that do not occupy each other (architecture rows V6 and V9). Add that condition and route the cross-system question to the Fallout owner, as the architecture plan proposes. If V6 shows those pairs read as zero, the parent chooses between asking the Fallout owner for an unconditional reset and a one-time Event 097 stand-down pass that sets the pairs it wrote to zero, which matches what Fallout itself does.
- Part 5 line 125 calls Event 063 "Subjects Break Free". Its in-game name is "Subject Independence" (`localisation/english/chaosx_event_names_l_english.yml` line 65), and the catalog calls it "End Subject Status".
- Part 2 line 222 says Open Gates needs "an enemy with a strong network", while Part 3 uses the enemy with the strongest network, which can be at the Ordinary band. Part 2 line 153 calls Open Gates "the evolution's rare incident", while at Collapsing it can happen three times in one war. "Uncommon", the word Part 2 already uses below its variant table, fits better.
- Part 3 line 45 sends the prepared cadres report to the exiled host, and the asset prompt names no image for it. S2 proposes a reuse.
- Architecture plan, which was still being edited: row V4 says Part 4 accepts the computed set for A2, which the second-pass commit turned into a user decision (README, Unresolved). Question Q13 asks whether to build a CXT package, which the coding prompt and acceptance criterion 36 already require. R2 answers question Q8. The sphere helpers follow whichever answer C2 receives.

### Recommended cuts and merges

**C1. Cut Add network depth and both cluster combinations.**

- Where: Part 5 write table line 30, the second Event 052 hook at line 92, the Event 039 section at line 98, the README accepted-design list, and the architecture public API in section 3.20 with its request arrays and caller ids.
- Why:
  - It is the only write that makes one host deeper than every other host, which works against the global and symmetrical identity that the brief fixes.
  - Event 039's specification has no Event 097 hook, so the 039 combination reaches into a package whose owner never agreed to it.
  - Event 052's interaction matrix asks for "one network risk or disclosure result" from Event 097. Burn networks and the read surface already provide that.
  - The Intelligence cluster has no runtime id yet, so both combinations would ship dormant.
  - The cut removes a write that has to queue behind a running application pass, two caller ids, and a custom cluster runtime branch.
- Keep: Event 097 as a plain Medium member of the Intelligence cluster, and Event 052's Burn networks hook.

**C2. One entry point for the Tordesillas event.**

- Where: Part 5 lines 31 and 79 to 84, the "Install through Event 097" write, and architecture sections 3.2, 3.13, and 3.19.
- Recommendation: drop "Register an external sphere" and the Evolution II exception. The Tordesillas owner calls "Install through Event 097" with the External sphere route, and that call applies the sphere threshold reduction within the Part 3 limits. B1 and the capitulation offer stay Evolution IV content everywhere. An external-sphere install needs Event 097 networks inside the host, the reduced threshold, and every ordinary limit. It does not need Evolution IV, because the calling event owns its own timing and its own enable setting. Sphere governments receive the full Installed Administration package, and Turned Regime and competing orders consider them only while Evolution IV is live. Part 2's disabled row then applies to Event 097's own routes.
- Why: Event 097 then holds no sphere concept and never names a partner in its own decisions, which Part 5 already promises. R1 disappears, and the Tordesillas owner keeps control of when its spheres consolidate.
- Note for the future Tordesillas owner: the reduced threshold of 30 points still needs at least two Accept firings of Event 097 inside the host. Tordesillas content that must install earlier needs its own route.

**C3. One band ladder for networks.**

- Where: the Part 1 public presentation table (Scattered, Established, Deep, Pervasive at 20, 40, and 70), the Part 3 network bands (Thin, Ordinary, Strong, Total at 15, 40, and 70), the Part 4 A1 AI rule, matrix scenario P22, the localisation direction, and the architecture constant groups `collaboration_depth_band` and `collaboration_depth_band_id`.
- Recommendation: use the Part 3 edges and one set of four player-facing words for both readings and for the per-enemy band words in the A2 and B1 tooltips. One Accept firing then reads as the second band on every surface, which matches Part 3's "one baseline layer or more is in place".
- Why: the player otherwise meets eight band words with nearly the same edges for one native value, and the decision audit already had to ask which scale each condition used. The two readings stay, because together they show the event's central idea that every foreign government holds as much inside this country as this country holds inside them.

### Recommended small additions

These reuse existing events, options, images, and helpers. None adds a value, decision, rare variant, Chaos row, or asset.

**S1. Capitulation report for the occupier.**

- Moment: a participant host with Event 097 networks capitulates.
- Delivery: the one-day capitulation follow-up that A1 already needs (architecture event `chaosx.nr97.24`) runs for every such capitulation and sends one report to each human participant enemy that controls host cores with at least the second band.
- Content direction: the occupier's viewpoint. The provinces came over with their staff, and the administration was ready to work for the new controller. The report names the occupier's band word inside the host and the starting compliance in the host cores it controls, read after the engine conversion and after any A1 reduction, in plain text on parchment. A Deep Networks line appears when prepared cadres were applied.
- Limits: once per capitulation for each human occupier. AI countries receive nothing, and no Chaos changes.
- Image: reuse `report_event_097_collaboration_seat`.
- Why: it answers questions 1 and 2 together. The Cultivate choice and Evolution I both get a moment where the player sees what they bought.

**S2. Report to the original country at installation and abandonment.**

- Moment: the shared installation helper succeeds, and later the row enters Abandoned.
- Delivery: one report to the original country while it still exists, to human players.
- Content direction: the defeated government's viewpoint. Its own former officials now run the homeland under the installer, and the report names the installer and the installed government. It closes with the restoration mood line, using the selector word for the current band. The Abandoned variant says the regime has lost its protector.
- Image: reuse `report_event_097_collaboration_open_ministries`. The same image covers the prepared cadres report in Part 3 line 45.
- Why: the most important moment for the defeated country has no surface, and the restoration mood from R3 needs one. Contested changes send nothing, because Contested can switch back and forth during a war.

**S3. The reckoning at restoration.**

- Moment: a registry row retires because the original country is restored, either through Event 095 and the Retire write or when the original tag annexes the government.
- Delivery: the original country receives Collaborators Unmasked in a national variant, once per retired row.
- Options: Purge subtracts the existing Purge points from the former installer's collaboration inside the restored country, never below zero, and applies the existing refreshed Purge spirit. Amnesty applies the existing Amnesty state modifier once to every owned core state of the restored country. The variant sets the pair guard for the owner and the former installer, so a district-level Unmasked does not follow in the same war.
- AI: matrix surface S4, with the same inputs as P14 and P15.
- Engine dependency: Purge here has no occupation context, so it relies on the native clamp at zero (architecture row V4), as Burn networks does. If V4 fails, this Purge joins the existing Purge blocker.
- Image: reuse `report_event_097_collaboration_unmasked`.
- Chaos: none beyond the restoration row, which already applies at retirement.
- Research basis: after the liberation of France, summary reprisals were followed by legal trials and administrative sanctions that reached the civil administration, and the most common sentence, national degradation, barred people from the civil service ([Épuration légale, Wikipedia](https://en.wikipedia.org/wiki/%C3%89puration_l%C3%A9gale), read from a search summary only, page not opened). A choice between punishing the officials who served and keeping the state running with them therefore has a firm historical basis. The sensitivity boundary in the research notes applies unchanged: no real names, and neither option may make light of reprisals.

### Optional

**O1. A baseline counter for Loyalty Commissions.**

- Problem: before Evolutions II and III, A1 only cuts compliance after we capitulate, which a player cannot feel while fighting.
- Change: while Loyalty Commissions runs, the spirit adds a positive surrender-limit modifier sized by the band of Foreign networks among us, offsetting part of the collaboration loss. A1 also becomes visible when the host is at war with a participant enemy and that reading is at the third band or higher, so a deeply penetrated country can act before a core falls. The baseline category then shows one row.
- Dependency: the size can be set only after the behavior of the surrender-limit define is verified (research notes, uncertainty 3).
- Matrix effect: P22 becomes reachable at baseline. Balance scenario 3 must include the offset, because a host could combine it with A1's band reduction under the Fifth Column.
- The event stays coherent without O1, so the parent may skip it.

## What must not be added

- No new value, meter, currency, or numeric display. Restoration pressure stays a hidden composite shown as one word.
- No scripted GUI and no attached category display.
- No new decision in either category, and no new response event beyond the S3 variant of an existing one.
- No new rare variant, cluster combination, or partner hook. Future partners use the read surface, Burn networks, Retire, and Install.
- No news events, new achievements, or new asset families. S1 to S3 reuse existing images.
- No Chaos for stances, decisions, Unmasked choices, or the S1 to S3 reports.
- No war-weighted selection factor.
- No Event 097 AI strategy files.

## Carried blockers

These are already reported by the package. This pass adds none.

- B1. The HOI4 MCP server failed to connect. Every probability conclusion in the matrix stays unresolved, and no `hoi4.event_inspect` evidence exists for the event chain.
- B2. Vanilla files and documentation are absent. Architecture rows V2, V4, V6, V9, V10, V12, V13, V14, and V32 decide whether mapped features can be built. V2, whether pair values written without occupation still drive surrender limits and compliance, can block the whole event.
- B3. User decisions: the installer route for democratic and non-aligned governments, and the A2 computed-set route if V4 fails.
- B4. The Intelligence cluster id and its runtime build.

## Parent handoff

### Design problems found

- R1: the sphere route opens Evolution IV content from Evolution II while Parts 2 and 4 gate it on Evolution IV.
- R2: the package retires a freed government in four places and abandons it in one.
- R3: the prompts' public value list omits the restoration band, and the band has no report to live in.
- R4: the Fifth Column acquisition report has localisation and art but no mechanic or event id.
- R5: the Chaos map has no event-wide rate guard, and its lifetime estimate is several times lower than its rows allow.
- R6: one "never changes Chaos" reason is wrong without Evolution III.
- R7: Screen cannot stay visible when blocked.
- R8: a blocked Turned Regime or Open Gates leaves dependent achievements, art, Chaos rows, and surfaces behind.
- R9: Clean Ministries is out of reach in large event pools.
- R10: an inaccurate weight-hook reason, an unconditional Fallout promise, naming drift for Event 063, Open Gates wording, a missing image reuse, and stale lines in the architecture plan.
- C1 to C3: an asymmetric depth write and cluster combinations nobody asked for, a sphere registry where one install call would do, and two vocabularies for one value.
- S1 to S3: no moment for the occupier at capitulation, nothing for the defeated country at installation, and no reckoning at restoration.

### Recommendation

Closure. Settle R1 to R10 before finalizing the package. Accept or reject C1 to C3, S1 to S3, and O1 with a recorded reason. Record each disposition in `docs/plans/097_collaboration_plans/097_collaboration_plan_dispositions.md`. The design loop can then stop. Another improvement-loop pass for this planning goal is not needed unless a later audit finds a gap these items do not cover.

### Research basis

- The whole specification package, the plan dispositions, the repo explorer handoff, the decision and AI probability audits, and the architecture plan.
- Repository source: `events/063_subject_independence.txt` (Event 063 frees a random subject and lets the old overlord fight to re-subject it), `events/095_occupation_revolt.txt`, `events/097_collaboration.txt`, `get_event_weight` in `common/scripted_effects/chaosx_logic_effects.txt`, and the Event 063 name in `localisation/english/chaosx_event_names_l_english.yml`.
- Event 039's specification folder, which has no Event 097 hook, and Event 052's interaction matrix line 11.
- Offline wiki: `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`, line 157, on option triggers.
- Web: one search on the French post-liberation purge, used for S3 and cited from its summary.

### Implementation surfaces affected

| Item | Spec parts and README | Prompts, matrices, and handoffs | Architecture plan |
| --- | --- | --- | --- |
| R1 and C2 | Parts 2, 4, and 5, README | Coding and decision prompts, edge matrix | Sections 3.2, 3.13, 3.19, 3.20 |
| R2 | Parts 1, 3, and 5 | Edge matrix, achievement prompt, acceptance criterion 15 | Sections 3.14 and 3.15, Q8 |
| R3 | Part 5 | Coding and goal prompts, localisation direction | none |
| R4 | Parts 3 and 6 | none | Section 4.4 |
| R5 and R6 | none | Chaos impact map, probability matrix P27 | Sections 3.18 and 6.1 (`collaboration_chaos`) |
| R7 | Part 1 | Localisation direction | Row V23, Q11 |
| R8 | Parts 3 and 6 | Achievement and asset prompts, Chaos impact map, probability matrix | Sections 3.10 and 3.16 |
| R9 | Part 6 | Achievement prompt | none |
| R10 | Parts 1, 2, 3, and 5, README | Edge matrix, acceptance criterion 7, asset prompt | Row V4, Q13 |
| C1 | Part 5, README | none | Sections 2.1, 3.20, 6.1 |
| C3 | Parts 1, 3, and 4 | Probability matrix P22, localisation direction | Section 6.1 band groups |
| S1 | Part 3 baseline section, Part 6 presentation | Localisation direction, asset prompt reuse note | Section 4.4, event 24 |
| S2 | Part 3 installation section, Part 5 restoration | Localisation direction, asset prompt reuse note | Sections 3.13 and 3.15 |
| S3 | Part 4 Collaborators Unmasked, Part 5 Event 095 | Probability matrix S4 | Section 3.14 |
| O1 | Part 4 A1 | Probability matrix P22, Part 6 balance scenario 3 | Section 3.19 |

### Open questions

1. C2: accept the single install entry point, or keep the sphere registry and write the exceptions into Parts 2 and 4?
2. R5: which annual cap, and which lifetime band should P27 test against?
3. O1: include or skip?
4. R2: confirm that a government re-subjected by its former installer returns to Imposed with its original route and counts again toward competing orders.
5. R10: if V6 shows that pairs between countries that do not occupy each other read as zero, should the Fallout owner make its reset unconditional, or should Event 097 run its own stand-down pass?
6. S1 and S2: confirm human-only delivery, with nothing sent to AI countries.

### Promotion into the specification

Fold each item the parent accepts into the named spec parts and prompts, and record its acceptance basis in the README "Accepted design" section and in the dispositions file. This closure file stays in the plans folder with its final disposition. Nothing here is accepted design until the parent records it.
