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

A1. **Q** (Welcome window text restored in `b9258e251e`; main-screen about text and help text still open.) Welcome text and main-screen "about" text: restore the pre-sweep wording; keep only new mechanic sections and dynamic values. Same for the Chaos Redux help text. Completed: 440fe01242ca41c7a65c30a29f1fc4540e44014b. Final text audit: `c65be58abe8323c8a06969a5f8c4a9bacdebafd1`.
A2. **Q** Audit the large localisation sweep of the past weeks. Find its commits, compare before and after per file, and where it made text vague or generic, revert it across all events and systems: event, evolution and world-end descriptions, report and news events and their options, decision and decision-category texts, tooltips on every interface surface, raids, super events. Keep only text for genuinely new content and dynamic values. Completed: `78e6554affd48ebcce7191ccded8c564353ac447`, `707df10ab81269eb1eaf9dfaf5e9cd7f804fe783`, `3a0a56a5c5ef9b8e66945cecdb0e7e828ccc384e`, `870440c437abb4eed00a6ecee00d6727bcfa967f`, `a1866880500dbbc83e39bb4194179eebb812ce48`, `9a9181c1f3c99a045e9b294bd762dda460b09b77`, `f3c31c8d1c7934eee66bca6eef5788807780678f`, `e25b11e0304e2ce96e09b7af9aa2d36bd30a9c02`, `9b59ef36afb7420c6ffed15eee6b7445f47a0e34`, `6eb33d883b2dc50b1604eaf474ad06f52f7e73a8`, `22ca369adc6208bc35efa3a21650f86eddb06bc1`, `ddfa77393b34a44736f9403a37080cd8d02875d4`, `256a17709aaf29cb00d641dd3de3cc04613c37ba`, `a6fcb2670e4ebee35ca4b9aed879b3a170131da0`, `be16542f341a16d4fe3739e595f016c9f3c41b45`, `b81f60173b974143ab7085bc15ca5b38ee899093`, `c02ffce521afc9484811e9b47cd87744fb0e7c19`, `1f40cb2e3294a502d3a138dc0dd383e55087309e`, `3975313519c0bc1a7259fa5335e5db5938166cea`, `8114f722529d6b71b309b1dbd66f8a59064ef03d`, `6e1e6080f3ba40d775c48925d5c6ea3724c7124e`, `5ae2808830d4bc29a3d725554373db265f5627dd`, `bc6a099d3f09fe1e9d9db24e7aba276d10567d16`, `3dd404db53add92293f09a37bb002e4003ec68bb`, `2572ac0a6337bae0ac27d3a4b1e3ae546707178c`, `d259cd9f626b4f9685379cc45625d00af83e15d4`, `fe70593119bf021c3a3501f2430756db107824af`, `82a578a32393c7779f0e85efbadc809a3c73288c`, `79328b209cc513972d574d1c376c1dba088d6b0f`, `a24fc5ca77ada3404062f99c1382fddc57aff21b`, `5cb387e323965bf3d4430fbf9ecba74fe73980b4`, `032e851a6086dc907cc1358c44ce35cb269d1813`, `5d61c5d413ac1b17c59a1ccc297833621552562d`, `682a925492663f9471c93d6a2a18de076081f78d`, `2a6223d4be29005d00ae8a189190ea408b89345d`, `e0b1a08946de1a69868fdbd073b8c9a7b6c852eb`, `a27afb609fd77de536c37397255b6482a5bf1b87`, `7cfdaec912d3dbabe4806d0b2eb683d5d4373710`, `7c9382190c8dedc3fc6c00352fd626e797f2398c`, `b3dfe57de5b9ba9df3a8a04f057cfd2dd0f7467a`, `a8903d7b8a15e70eccb1266d74b9bea0605ea5c0`, `3ae0eebc2fc6866cdf52e6b73ea2e02d040265d6`, `10b3e2638dd0b27870407902b295118169cf6a57`, `0d140d27fcf7cd35f5fade167815adc8efa3e83c`, `8904ea2f02e36b76b524adbead8ea9fa478d9c19`, `76156787c6764bd959d9ebb6156b695691c4acbc`, `440fe01242ca41c7a65c30a29f1fc4540e44014b`, `0331ae2fefbadf6eb4848be3e3eafb4af7d95d26`, `c0fd59ec9b41600bd05e7911800dfeaf0383d46d`, `5b93d3d47baafa2c8b1ecdb115820e8efade1147`, `442c8a9e1d09271dd0f5c8919010c502d1364911`, `8f676ea5258b0fff06b66f14288556db500235e6`, `c65be58abe8323c8a06969a5f8c4a9bacdebafd1`. Full key audit: `docs/plans/chaos_redux_text_restore_2026-10-12.md`.
A3. **Q** Super events: restore every text changed without request; keep only additions. Zombie outbreak super event still plays the wrong audio: restore the original audio routing for it and any other reroute. (Audio restored: 10292700c22304f1181b96733b797d2faf681a25.) Completed text scope: c0fd59ec9b41600bd05e7911800dfeaf0383d46d. Final text audit: `c65be58abe8323c8a06969a5f8c4a9bacdebafd1`.
A4. **Q** Chemical warfare cylinder tech icons: restore the originals (asked several times; verify against the pre-change commit, byte-exact). (Original DDS already restored in 75fcd313b1acf70a0f15903fa236197957c337dc; byte-exact originals and research sprite paths verified in 8933be0a8955b27cef6119cd4d1b4e4b7c878b9f; equipment aliases restored in 98e55344a43936fe5c503125b1cf18d536229492.)
A5. **Q** Icons changed in bulk: restore. Decisions must use decision icons, categories category icons, ideas idea-size icons. Keep only new icons that replaced vanilla placeholders. Wire the event ideas that are missing icons. (Partial: 935 original DDS restored and 171 idea bindings fixed in 539006cd86, c9ff9d16a5, 6344893ec7, 2aa9a2b531, 325bd35762, 2f100da79a, 25f0fbd38f, 99efdc907f, 6a07b3b661, 91073d05ed, f2a56c615d, 079a3a6c0b, fa54ab5c5b, 97666705a6, 163ad74e4c, f2be4e603d, d7dd251166, d27ab9d082, 7bdaf62ef8, 8d283d598a, 57759c7485, 7a9cfcbf79, 6ba18c584, f6012031f3, a3bf9361ae. Inhumane original restored in 8b8f213542 and verified in 8933be0a89. Incomplete: 36 idea assets without originals, 2 category-sized decision icons, 5 oversized seals, and 1 missing vanilla texture; see docs/plans/chaos_redux_restore_assets_audio_2026-10-12.md.) (A5-only resume: f501fbddf4d60efb96febacc99c49d926fc128e9 restores the 5 original animated Dhyana bindings from e5a528fc7^; provenance and blocker recheck: f57c5947243903cb014ffc16d6b51b9b6efaed25. The 36 missing idea sources, 2 category-sized selectors, five 96x96 frame size warnings, and missing Matignon DDS remain unresolved.)
A6. **Q** Portraits that were replaced: restore the previous ones. (Restored 165 portraits: 59267b7c8c, 85594b9971, dc9d31e380, 75bb1f633a, ebcc55bfd5, c888f80392, b456340082, 2eec6523f2, bfe0bf648f, a376c644a7, 12b431f69f.)
A7. **Q** Unit and decision text icons: some are flat green with no detail (for example the truck). Use the normal truck icon and restore the earlier detailed versions so the set is consistent. (Restored: b23e41257f78895546fcbb2843756610ba2875f2 and 753397bb5b9212931eed16b63a8236cc892174d3; truck verified as unchanged vanilla.)
A8. **Q** Chaos Meter history alignment: restore the earlier layout. — implemented in `1fca4df6a7`.
A9. **Q** Condemnation description: restore. Deaths entries spacing: restore. — implemented in `1fca4df6a7`.
A10. **Q** Cluster entries in the event log: restore the earlier entry layout and alignment; remove the available/unavailable text on the right. — implemented in `360245b7ff`. Alignment: `13aea99060`.
A11. Scientists: restore the balance that was changed (everyone became level 3 with no traits). Find the hidden biowarfare and chemical scientists and make them available again. Completed: `d2f7111d16e84b6b9a8fadf4b9967af12d165d15`.
A12. Biological warfare deployment and containment: restore the simpler year-old flow (deploy field hospitals and similar direct actions; easy and fast policy change; a raid must be doable without friction). The Disease Containment Board in its current form is rejected. Compare with the old implementation in git history before deciding what to keep. Completed: `3deac2d4da401de6e47c04f3170a409833ddffa4`.

A13. Chemical release abilities: re-add the army-leader chemical release abilities (chlorine, phosgene and the others in `common/abilities/chemical_abilities.txt`) as working abilities, restored from the last version in git history where they were active, with their traits, icons, localisation and AI. They are currently disabled with `allowed = { always = no }`. Raids stay as a second delivery route. Completed: `d640c653cb864864df84a8432acf8ab8d9f092fa`. Localisation follow-up: `0e2814d61b981479c82a9a2348534e717ddd4cb9`.

## B. UI fixes

B1. **Q** Super-event volume multiplier arrows: tooltip saying which volume they change (Luna). (commit: f5b8f4a61a5dc09e88692fd623b83d87e8314dae)
B2. **Q** Event log clusters view: remove the "show" control and the cluster, status and auto subheaders. In cluster details every member gets an enable/disable checkbox. Fix the "fires automatically" text overlapping the checkbox. (commit: 13ac669bcb60176ed8458bcb3b5a449bdcf78e45)
B3. **Q** World-end scenario details view: fix the positioning. — implemented in `7ea7d51f5b`.
B4. **Q** Event history flag hover shows "Japanese Empire" instead of the country the click pans to: fix. (commit: 13ac669bcb60176ed8458bcb3b5a449bdcf78e45)
B5. **Q** Move the auto event logs setting to the Miscellaneous view. (commit: f5b8f4a61a5dc09e88692fd623b83d87e8314dae)
B6. **Q** Event history logging: entries show only the event name, never the full description. Completed: 78e6554affd48ebcce7191ccded8c564353ac447. Parent-exact selector verified in `442c8a9e1d09271dd0f5c8919010c502d1364911`. Audit: `c65be58abe8323c8a06969a5f8c4a9bacdebafd1`.
B7. **Q** Air contamination idea "no longer fulfilled" message spam: hide it. (commit: 48255b6781aef430ac7e1fd332ba180fa2b0c491)
B8. **Q** Trait description shows broken scripted localisation: fix. (commit: 567ff94cd6ec1069fdfc391732af469d5a99f311)
B9. Camps UI: buttons do not work and throw errors (latest lines of error.log): fix (Sol). Source repair and independent button audit: `4b0967bd7ad2d8386a2ec137146af8b0cd225ad5`; state scopes retained; layout and art preserved; rendering timed out and no game was launched. Evidence: `docs/plans/chaos_redux_load_camps_repair_2026-10-13.md`.
B10. Migration UI: empty area on the left; the image goes inside the box. — implemented in `76c7815224`.
B11. Decisions for outbreak responses appear on the map only, not listed in the decision category. Completed: `3deac2d4da401de6e47c04f3170a409833ddffa4`.
B12. Technology folders: fix overlaps, disconnected techs and bloat. Bring back the consolidation that removed the excess techs, but leave the upper part of the chemical warfare tree exactly as it is. — implemented in `30ac00fb03`.

B13. Biowarfare folder: fix disconnected techs (started 12 Oct, Sol job `sol_bio_folder_links`).
B14. **Q** Rule for all UI text: large numbers are never shown plainly; shorten with k (48.2k). (commit: f41b58e6c34ae9f47598033d03d0e0aa459b6a2d)

## C. Systems (Sol unless noted)

C1. All load errors in error.log. Partial source fixes: `3c098421e86f16eece355d268c2ea75c19d765db`, `f64ef507a2717e7c15239243ce41c373f71d7ce1`, `e0f807c1d492165a29b252bc55929f94ec2bba54`, `6cf5d0120866354fbc023bcb2c119bc4f2357e1e`; zero current localisation collisions. Incomplete: five never-tracked flag ladders and unlocated font diagnostics; no Linux launch loop under the explicit no-launch instruction. Evidence: `docs/plans/chaos_redux_load_camps_repair_2026-10-13.md`.
C2. Crisis pressure setting: worded as applying to any event, made dynamic so other events use it, a slight effect only, disabled by default.
C3. UI fractures: remove the fracture cascade events, keep the setting. Cracks follow the Chaos Meter tier: none at calm, very slight at the next tier, larger, more visible and redder with each tier. Never over main buttons, only in free space. At world end more cracks, without the dim purple glow.
C4. Performance: the game becomes very slow after some events fire. Profile and fix.
C5. Random terror event is broken one year in: fix.
C6. Non-human countries must never be affected by systems meant for humans.
C7. A super event's audio stops as soon as the next super event fires; only one plays at a time.
C8. Report events: audit for more than 4 options and fix. (commit: 212a23bca2e1fcac6668e0a69bc80aba4532e824)
C9. Events must not hand out strong bonuses casually (for example Orders from Unknown Hands). Audit every event for this, for tooltips showing internal details, and for duplicate ideas being granted.
C10. Orders from Unknown Hands: rewrite plainly and concretely. Confirm Event 11's first incident varies.
C11. Migration: decisions must not appear on arbitrary owned islands. They appear only under real pressure: famine, blockade, states next to outbreaks, special chaos countries at war, states near the front. Remove political power costs; use fuel, and convoys for islands not connected to the mainland. Check whether the migration and famine systems were simplified and restore depth from history if so.
C12. Outbreak response: many distinct actions, not one generic decision, but not bloated.

## D. Balance and content

D1. Japan, the United Kingdom, the United States and the Soviet Union start with the level 1 biowarfare breakthrough. Germany, the United Kingdom and France start with the chemical warfare breakthrough. Completed: `aa75244feb4062279c64e4d89f725481f414011b`.
D2. Starting technologies and stockpiles: audit for accuracy. Germany should start with tabun (GA) researched.
D3. Japan uses CBRN unrestricted from the start. Completed: `aa75244feb4062279c64e4d89f725481f414011b`.
D4. Traits: bonuses are generic and weak. Make them chaos-warfare focused; CBRN Operations Specialist gets strong, specialised CBRN bonuses.
D5. Remove the "Last Fury Standing" focus and merge its purpose into another focus. (commit: b5caeb8fb82351164a0849378c2791d3f998c4b6)

## E. Outside the mod

E1. Setup app: live-testing MCP choice step (Clausewitz MCP default with acknowledgement, HOI4 Live Tools experimental) and a Linux setup guide. In progress with the v0.4.0 release job.
E2. Chaos Redux playtest skill: use the Clausewitz MCP on the Linux game. In progress with the Clausewitz 1.19.3 port job.
E3. HOI4 Live Tools: rebuild on the Clausewitz MCP approach (live game data, no screenshots or saves, universal, faster). Not now.

## Answered

- Chemical release abilities (to be re-added, see A13): the old army-leader release abilities (chlorine, phosgene and the others in `common/abilities/chemical_abilities.txt`) are switched off with `allowed = { always = no }`. Release goes through the CBRN raid and operation system. The five remaining abilities in `cbrn_hq_abilities.txt` are protective and need a deployed army HQ with the CBRN company, not a trait.
