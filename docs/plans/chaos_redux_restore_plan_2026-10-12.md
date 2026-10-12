# Chaos Redux restore and fix plan (12 Oct 2026)

Source: the user's review of 12 Oct 2026.
Status of every item: `unresolved` until its commit is listed here.

## Gate

- Nothing here starts until the videos are rendered and the public repos (setup app, agentic package, Agent Tools, Live Tools) are merged, released and clean.
- Chaos Redux is NOT pushed in its current state under any circumstances. The push gate is: this plan's restores done, load errors fixed, LFS managed, main menu fixed, `e chaosx_test` fixed.
- First execution pass is selective: only the quick UI, localisation and restore items (marked **Q**). Report to the user afterwards and propose the next batch.
- Every job starts with its working directory inside the Chaos Redux repo.
- "Restore" means the exact earlier content, taken from git history, never a rewrite. Keep only genuinely new mechanic sections and values that were made dynamic.
- Options in report events: never more than 4.
- No world-wide periodic on_actions without permission. No AI attribution in commits.

## Routing

- Mass restores (text, icons, portraits, UI layouts, audio routing): Sonnet 5.5.
- Engine and system fixes: Codex `gpt-6.1-sol`.
- Small specific jobs and image generation: Codex `gpt-6-luna` at max.

## A. Mass restores (Sonnet 5.5)

A1. **Q** (Welcome window text restored in `b9258e251e`; main-screen about text and help text still open.) Welcome text and main-screen "about" text: restore the pre-sweep wording; keep only new mechanic sections and dynamic values. Same for the Chaos Redux help text.
A2. **Q** Audit the large localisation sweep of the past weeks. Find its commits, compare before and after per file, and where it made text vague or generic, revert it across all events and systems: event, evolution and world-end descriptions, report and news events and their options, decision and decision-category texts, tooltips on every interface surface, raids, super events. Keep only text for genuinely new content and dynamic values.
A3. **Q** Super events: restore every text changed without request; keep only additions. Zombie outbreak super event still plays the wrong audio: restore the original audio routing for it and any other reroute.
A4. **Q** Chemical warfare cylinder tech icons: restore the originals (asked several times; verify against the pre-change commit, byte-exact).
A5. **Q** Icons changed in bulk: restore. Decisions must use decision icons, categories category icons, ideas idea-size icons. Keep only new icons that replaced vanilla placeholders. Wire the event ideas that are missing icons.
A6. **Q** Portraits that were replaced: restore the previous ones.
A7. **Q** Unit and decision text icons: some are flat green with no detail (for example the truck). Use the normal truck icon and restore the earlier detailed versions so the set is consistent.
A8. **Q** Chaos Meter history alignment: restore the earlier layout.
A9. **Q** Condemnation description: restore. Deaths entries spacing: restore.
A10. **Q** Cluster entries in the event log: restore the earlier entry layout and alignment; remove the available/unavailable text on the right.
A11. Scientists: restore the balance that was changed (everyone became level 3 with no traits). Find the hidden biowarfare and chemical scientists and make them available again. Completed: `d2f7111d16e84b6b9a8fadf4b9967af12d165d15`.
A12. Biological warfare deployment and containment: restore the simpler year-old flow (deploy field hospitals and similar direct actions; easy and fast policy change; a raid must be doable without friction). The Disease Containment Board in its current form is rejected. Compare with the old implementation in git history before deciding what to keep.

A13. Chemical release abilities: re-add the army-leader chemical release abilities (chlorine, phosgene and the others in `common/abilities/chemical_abilities.txt`) as working abilities, restored from the last version in git history where they were active, with their traits, icons, localisation and AI. They are currently disabled with `allowed = { always = no }`. Raids stay as a second delivery route.

## B. UI fixes

B1. **Q** Super-event volume multiplier arrows: tooltip saying which volume they change (Luna).
B2. **Q** Event log clusters view: remove the "show" control and the cluster, status and auto subheaders. In cluster details every member gets an enable/disable checkbox. Fix the "fires automatically" text overlapping the checkbox.
B3. **Q** World-end scenario details view: fix the positioning.
B4. **Q** Event history flag hover shows "Japanese Empire" instead of the country the click pans to: fix.
B5. **Q** Move the auto event logs setting to the Miscellaneous view.
B6. **Q** Event history logging: entries show only the event name, never the full description.
B7. **Q** Air contamination idea "no longer fulfilled" message spam: hide it.
B8. **Q** Trait description shows broken scripted localisation: fix.
B9. Camps UI: buttons do not work and throw errors (latest lines of error.log): fix (Sol).
B10. Migration UI: empty area on the left; the image goes inside the box.
B11. Decisions for outbreak responses appear on the map only, not listed in the decision category.
B12. Technology folders: fix overlaps, disconnected techs and bloat. Bring back the consolidation that removed the excess techs, but leave the upper part of the chemical warfare tree exactly as it is.

B13. Biowarfare folder: fix disconnected techs (started 12 Oct, Sol job `sol_bio_folder_links`).
B14. **Q** Rule for all UI text: large numbers are never shown plainly; shorten with k (48.2k).

## C. Systems (Sol unless noted)

C1. All load errors in error.log.
C2. Crisis pressure setting: worded as applying to any event, made dynamic so other events use it, a slight effect only, disabled by default.
C3. UI fractures: remove the fracture cascade events, keep the setting. Cracks follow the Chaos Meter tier: none at calm, very slight at the next tier, larger, more visible and redder with each tier. Never over main buttons, only in free space. At world end more cracks, without the dim purple glow.
C4. Performance: the game becomes very slow after some events fire. Profile and fix.
C5. Random terror event is broken one year in: fix.
C6. Non-human countries must never be affected by systems meant for humans.
C7. A super event's audio stops as soon as the next super event fires; only one plays at a time.
C8. Report events: audit for more than 4 options and fix.
C9. Events must not hand out strong bonuses casually (for example Orders from Unknown Hands). Audit every event for this, for tooltips showing internal details, and for duplicate ideas being granted.
C10. Orders from Unknown Hands: rewrite plainly and concretely. Confirm Event 11's first incident varies.
C11. Migration: decisions must not appear on arbitrary owned islands. They appear only under real pressure: famine, blockade, states next to outbreaks, special chaos countries at war, states near the front. Remove political power costs; use fuel, and convoys for islands not connected to the mainland. Check whether the migration and famine systems were simplified and restore depth from history if so.
C12. Outbreak response: many distinct actions, not one generic decision, but not bloated.

## D. Balance and content

D1. Japan, the United Kingdom, the United States and the Soviet Union start with the level 1 biowarfare breakthrough. Germany, the United Kingdom and France start with the chemical warfare breakthrough.
D2. Starting technologies and stockpiles: audit for accuracy. Germany should start with tabun (GA) researched.
D3. Japan uses CBRN unrestricted from the start.
D4. Traits: bonuses are generic and weak. Make them chaos-warfare focused; CBRN Operations Specialist gets strong, specialised CBRN bonuses.
D5. Remove the "Last Fury Standing" focus and merge its purpose into another focus.

## E. Outside the mod

E1. Setup app: live-testing MCP choice step (Clausewitz MCP default with acknowledgement, HOI4 Live Tools experimental) and a Linux setup guide. In progress with the v0.4.0 release job.
E2. Chaos Redux playtest skill: use the Clausewitz MCP on the Linux game. In progress with the Clausewitz 1.19.3 port job.
E3. HOI4 Live Tools: rebuild on the Clausewitz MCP approach (live game data, no screenshots or saves, universal, faster). Not now.

## Answered

- Chemical release abilities (to be re-added, see A13): the old army-leader release abilities (chlorine, phosgene and the others in `common/abilities/chemical_abilities.txt`) are switched off with `allowed = { always = no }`. Release goes through the CBRN raid and operation system. The five remaining abilities in `cbrn_hq_abilities.txt` are protective and need a deployed army HQ with the CBRN company, not a trait.
