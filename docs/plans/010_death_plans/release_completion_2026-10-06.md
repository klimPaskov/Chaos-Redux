# Event 010 release repairs, 6 October 2026

Disposition: implemented source repairs; release qualification remains incomplete.
The parent accepted the October changes within the user's G6 and G7 authority.
The implementation decision table is `agent_decisions_2026-10-05.md`; catalog edits are queued in `catalog_changes_pending.md`.
The parent completed the final wiring after the Event 010 owner repeatedly encountered a model-capacity error.

## What was repaired

A valid quiet origin remains silent.
Each country receives at most one missing-island report pair (`.2` and `.3`) during the campaign, and the identical mainland news `.4` emits once with `major = yes` and aggregate totals.
The report says Death reached a coastal state rather than claiming the whole mainland fell.
Failed manual quiet or Instant Outbreak launches use one pending `.5` acknowledgement per country, preserving its first reason until acknowledgement.
Automatic failed quiet launches do not add a player report.
Successful Instant Outbreak launches acknowledge all four intensities through `.6`; only a successful maximum launch records maximum use.
A failed launch cannot set the successful Instant Outbreak flag, and that flag enables the scenario's later ordinary island-spread route without forging natural evolution completion.

Public Death converges on the Shroud, Hunger and Census preparations and retains the successful Instant Outbreak bypass.
No Graves Needed adds the current weak-host cost to the existing fungible soul-power pool; it does not promise an earmarked host.
Wasteland Roads contributes to the real state-consuming wither progress, subject to the existing target restrictions.
Interrogate reports the current available route, including both coastal readiness and an eligible spatial target.

Survey and Outpost require a division owned by the acting country in the selected living-controlled recaptured state, together with their real equipment and transport payments.
The unverified supplied-division and native supply-connection requirements were superseded by this explicit guarded field-work design.
Neither action claims to test actual unit supply status.
Outpost does not restore population, factories or resources.

Seal Names is state-targeted and reachable on recaptured land despite its persistent consumed-state marker.
Living recaptured wasteland adjacent to active Death land now receives the existing border hazard; a paid seal removes that hazard and daily division damage for 120 days.
The next existing DTH-neighbor pulse can restore the hazard after expiry.
A separate 180-day state cooldown remains, and normal DTH recapture before expiry applies +2 spread pressure before clearing protection.
Landing and combat remain possible.
State-control callbacks intentionally suppressed during a Fallout world rewrite have no demonstrated backlash replay; this integration limit is not presented as tested.

The four-type limit includes custodial capacity.
Patrol retains Command Power, Fuel, Convoys and Support; Last Shores Response retains Command Power, Army XP, Fuel and Trucks.
Transit setup retains capacity, Support, Trucks and Fuel; upkeep retains the last three.
All 34 custom-cost families show at most three total inline values, with complete payment and timing on hover.
Final parity review restored the displayed truck gate/debit in both Transit helpers and added the six omitted quoted Stability affordability checks; numerical prices and AI scores are unchanged.
Capacity prices use constant-derived display variables, and capacity and Soul power have dedicated native-alpha texticons.

Six Continents counts distinct reached continents instead of foothold states.
Defeat saves its world-end super-event qualification before teardown clears the world-end flags.
The shared Event Log actor-output initialization repair is separately committed as `c265f3db6eae4e15252a3da96593b14655da1062`.

## Asset review and evidence

Six news/super-event DDS files and two Zol world-end portrait DDS files retain their runtime paths, dimensions, pixels and effective alpha while using uncompressed BGRA32 containers.
The six news/super registrations were rechecked in `interface/chaosx_pictures.gfx` and `interface/chaosx_super_events.gfx`; the portrait manifest records the existing character sprites and eight-frame strip.
Original DDS bytes, source/output hashes, PNG previews and exact decoded equality are retained in the owned asset archives.
The parent viewed the six-art 938x1100 contact sheet and the 468x702 static/eight-frame portrait sheet separately.
These are format repairs, not new art or proof of the missing original masters or original animation-frame production.
The two new 18-pixel currency glyphs have their own generated source, prompt, alpha, native-size and DDS evidence.
No character art or inherited animation was regenerated.

The supplied live QA sheet contains no Death popup; the other popups are unrelated vanilla events.
Its downscaled review supports the quiet-start finding but cannot validate the revised Death reports or interfaces.

## MCP and release limits

Focused report lint returned partial prior-source evidence, including the legitimate effect-free mainland acknowledgement.
Later `.1` inspect/render attempts remained unobserved at their 60-second client bounds, with no current graph or artifact.
The 26-focus inspection found no tree-blocking diagnostics; its render reported no connector crossings and layout hash `afe9a7ce44ea42428115815cd2c328dfd8135f711991db9c26c1bc7b9464adf1`.
The four-scenario focus evaluation and sweep were partial (53 unresolved items and four unresolved candidates), with differing source revisions; they do not prove current selection ranks or campaign balance.
The three-decision, five-synthetic-scenario before/after comparison was submitted but produced no observed result before the 60-second client bound.
Its synthetic map IDs were not real-map fixtures, and its restricted pool does not cover every containment action.
The existing Atlas summary is split into four native tabs with no lost fields, at most four visible values and five navigation controls including Close.
The free opener hides while open and can reopen immediately after closing, resetting to Seas.
Twenty-nine flag requirement texts prevent implementation names from reaching native tooltips.
Current event lifecycle, full weighted logic, cost boundaries, GUI scale/layout and inherited source-master provenance remain unverified.
The earlier Atlas inspection reported seven overlaps and an unresolved animated-header static fallback; its provenance artifact could not be recovered.
The redesigned Atlas has the required named-worker handoff, source snapshots, native-derived references, and matching post-change inspect/render attempts; both final calls returned `Transport closed` without artifacts.
Its new source bounds and controls are reviewed, but the inherited diagnostics and current glyph/layout appearance remain open production-render gates.
No game or desktop window was launched.

## Exact orchestrator checks

1. Load `qa_001_fresh_head` as USA on 1 January 1936 and force Event 010 from Settings.
Expected: a valid quiet origin changes the selected island without an opening popup; the Event Log records the successful chain.
Run at speed 5 until the USA becomes a relevant report recipient and count `.2`, `.3` and `.4`: at most one of each, ignoring vanilla popups.
Inspect Event Details before and after reveal for the proper actor and short premise.

2. On separate fresh setups, launch Instant Outbreak at Low, Medium, High and Maximum.
Expected: territory changes hands only on a valid start; one `.6` success acknowledgement follows, one mainland world news emits, and only Maximum sets its maximum-use receipt.
Force a blocked launch twice before the next day, wait for `.5`, then acknowledge it.
Expected: one unchanged reason, no duplicate generic refusal, and no `.6` success message or maximum-use flag from failure.
After a successful launch, allow an ordinary spread pulse and verify the island route is not locked behind unearned Hunger/Shroud completion.

3. Switch to DTH after public reveal, inspect the 26-focus route, complete No Graves Needed and Wasteland Roads, and observe one revealed spread pulse.
Expected: the shared soul pool rises by the live weak-host cost; the gain can be spent by another soul purchase, and roads affect only a valid adjacent wither target.
Check focus title fit and shortcuts at 1920x1080 and 1366x768, scale 1.

4. As a living country, recapture a wasteland bordering active DTH land.
Move one of your own divisions into it; an allied-only division must not qualify Survey or Outpost.
Test each quoted fee at one below, exactly equal and one above, both outside and during Black Friday.
Survey and then build Outpost: exactly one payment, no population/industry restoration, and each state's capacity grant occurs once.
Hover every price, including Soul and capacity; check the new glyphs and no more than three inline values.
For Transit setup and upkeep, verify the displayed trucks are both required and debited; repeat each of the six Black Book/Herald Stability fees below and at its live quote.
Open Black Atlas with the Black Book both closed and open, at low and high counters; visit Seas, Fronts, Compact and Book at both declared resolutions.
Expected: each pane shows at most four values, the selected tab is clear, Book hides when it cannot matter, all eleven existing fields remain accessible, and Close/immediate reopening returns to Seas.
Clear the forbidden context while Book is selected: the Seas view must appear without a blank pane.
Check the population label/value gutter, long status values, footer and click regions.

5. With the Black Book exposed, buy Seal Names on that state.
Expected: the border hazard/daily unit damage stops immediately; after 120 days it returns on the existing pulse, and repeat purchase stays blocked by the 180-day state cooldown.
On a separate setup, let DTH retake the sealed state before expiry: pressure rises by exactly two once, protection clears, and the cooldown remains.
Run Interrogate with no valid coastal target, with a ready target, and during Last Shores: its band must describe the actual current route.

6. Reach six distinct continents through Last Shores and compare a second foothold on the same continent.
Expected: only the new continent advances Six Continents; a second foothold still counts for ordinary foothold costs but not the unique-continent achievement.
Reclaim every DTH state after Last Shores begins: the appropriate defeat super-event and eight-frame portrait render correctly, and the cleared world-end flag does not suppress the already-earned aftermath.
Inspect all affected news/super/portrait art for blank, wrong-format, crop or animation defects.

## Deviations and outstanding gates

The guarded field-work replacement for unverifiable supply status, state-local border-hazard Seal design, cost consolidation and fungible No Graves reward are explicit accepted design changes.
The Fallout callback replay limit, current GUI/MCP/runtime verification and inherited master/animation lineage remain open.
Catalog workbook/export updates are accepted and queued by the user's no-edit instruction.
Skills used: events, decisions/missions, focus trees, scripted GUI, event assets, super-events, MTTH, subagents and shared Git commit.
No skill was created or changed; the existing events skill already records caller-owned helper results.

## Final parent source identities

- `events/010_death.txt`: `268a6a37d9532e253208f79b132f728d49580104d6f712f93944a919db68587a`.
- `common/scripted_effects/010_death_effects.txt`: `7bbcc7dcde966c73ede0886193cf9965387520f96689c02da2577e29fcead790`.
- `common/scripted_triggers/010_death_triggers.txt`: `457e7c74383b12e3b5c16637799bebf66c484d80cc719f50db3a723892a57bf2`.
- `common/decisions/010_death_decisions.txt`: `d734796e6aca2ad158ddfcd3c560ed52ba123b3de62e28d0f60cce1fef97800e`.
- `common/national_focus/010_death_focus_tree.txt`: `99a40741abbb2422654eb1f13eb874511130128d3b2cdd704a0e675a0d878763`.
- `localisation/english/010_death_l_english.yml`: `6bcdd877df8006b7a5068280ae272767e0d450bb309333d12415a0a0b35aae38`.

Earlier MCP artifacts and the initial bounded three-decision comparison predate the final currency and cost-parity changes.
The final cost-eligibility handoff `final_cost_eligibility_audit_2026-10-06.md` records the later restricted scenario attempt separately: its comparison returned `Transport closed`, without an artifact or analysis.
It confirms current gate/debit quote parity and explains that the baseline decision body resolves both sets of helpers from the current workspace; it cannot prove old helper eligibility.

The final Atlas state-reset and free opener changes followed the cost audit; the cost helper bodies and prices are unchanged by those UI-only hunks.
The former two-column summary is superseded by the four-tab source; the prior overlap report remains unreviewable without its missing provenance artifact.
