# Event 014 Cannibalism Achievements

Event 014 defines 18 custom achievements. Each achievement uses the same stable identifier across `common/achievements/chaos_redux_achievements.txt`, `common/scripted_triggers/014_cannibalism_achievement_triggers.txt`, Event 014 evidence effects, English localisation, and `interface/014_cannibalism_achievements.gfx`. Manual `SCN-010` launches permanently disqualify the campaign achievement set, but they do not disable the underlying gameplay systems.

## 1. Rations, Records, No Graves

Identifier: `014_cannibalism_clean_first_country`.

As the first Event 014 host, achieve local and worldwide victory through humane containment before any second country is infected and before any commune or warlord forms. Terror exploitation, a corrupted clean route, or foreign spread disqualifies the run.

## 2. Only One Table

Identifier: `014_cannibalism_no_second_table`.

Control the first host or earn decisive joint-suppression credit, then reach worldwide victory without a second infected country ever being recorded.

## 3. Three Fronts Closed

Identifier: `014_cannibalism_three_front_containment`.

Receive unique suppression credit in three countries, complete a joint suppression operation, prevent every warlord country from forming, and finish worldwide containment.

## 4. Signal Lamps Relit

Identifier: `014_cannibalism_silent_islands_reclaimed`.

Liberate and fully stabilize three island or isolated coastal nodes. The recovery effects award credit only after the convoy, train, support-equipment, and local-supply requirements survive the full recovery sequence.

## 5. The Line Held Twice

Identifier: `014_cannibalism_cured_then_returned`.

Win local containment, later face a ledgered external reinfection or Host invasion, and win again without reopening terror exploitation.

## 6. The Weapon Confessed

Identifier: `014_cannibalism_repentant_weapon`.

Authorize terror exploitation, renounce it through the public court-martial route, never authorize it again, prevent a domestic commune, and complete local victory.

## 7. Breakwater

Identifier: `014_cannibalism_break_the_island_host`.

Maintain a blockade against an Island Host, fund the landing, defeat the Host, rescue the surviving population, prevent an Island Host from remaining active, and finish worldwide containment.

## 8. No Master at My Table

Identifier: `014_cannibalism_warlord_without_master`.

As a player-controlled Event 014 warlord, resist the public convergence, remain independent and uncapitulated, and complete the recorded 365-day defiant-survival period without becoming CBL.

## 9. The Chosen Seat

Identifier: `014_cannibalism_host_of_unification`.

Become the player-selected unification host, retain at least three named warlords as commanders, and complete at least one major unified command, Larder, air, cell, or counterwar capstone.

## 10. All Mouths, One Command

Identifier: `014_cannibalism_all_mouths_one_command`.

After the public reveal, absorb every surviving warlord, remove every resistant warlord, control every surviving commune, retain at least 400 Global Larder, and maintain at least three connected routes.

## 11. Three Continents for Supper

Identifier: `014_cannibalism_continental_larder`.

As the unified Host, maintain feeding states on three continents and record at least ten million consumed people before either terminal world-end flag is set.

## 12. Break the Empty Frame

Identifier: `014_cannibalism_stop_the_reveal`.

Win the convergence mission, destroy the recorded likely host, break convergence, reduce Network Reach to 50 or less, and reach worldwide victory before the reveal flag exists. The icon and achievement visibility must remain spoiler-safe while the portrait frame is still empty.

## 13. The Command Mantle Falls

Identifier: `014_cannibalism_defeat_hannibal`.

Contribute materially to defeating the publicly revealed unified Host, clear every remaining cell, commune, and warlord, finish worldwide victory and cleanup, and prevent any world-end flag.

## 14. Torch Against the Winter

Identifier: `014_cannibalism_break_the_winter_hunger`.

After the Wendigo merger, earn counterwar contribution, destroy every transformation anchor before lock, defeat the transformation route, and finish worldwide victory without the Wendigo world end.

## 15. The World Is the Larder

Identifier: `014_cannibalism_ordinary_world_end`.

As the unified Host, satisfy the complete ordinary terminal contract and finish the ordinary world end while Chaos is strictly greater than 1000.

## 16. No Thaw Will Come

Identifier: `014_cannibalism_wendigo_world_end`.

As the transformed Wendigo command, preserve the anchor chain, complete the countdown, enter the locked form, and finish the Wendigo world end while Chaos is strictly greater than 1000.

## 17. The Burial Detail

Identifier: `014_cannibalism_global_burial_detail`.

Contribute to an eligible global defeat, finish reconstruction in every former feeding state, contribute to the reconstruction ledger, and maintain the international inspection compact for 365 days.

## 18. No Empty State

Identifier: `014_cannibalism_no_empty_state`.

Contribute to worldwide victory after at least one warlord country has formed while preventing every state from ever reaching Silent Larder status.

## Evidence and transfer rules

Achievement checks read recorded Event 014 history rather than button presses. Evidence includes first-host status, unique suppressed countries, recovered isolated nodes, reinfection history, exploitation and renunciation, Island Host operations, defiant survival, unification-host selection, named-command integration, capstones, route and Larder ledgers, convergence targeting, global-defeat contribution, anchor destruction, terminal flags, reconstruction, and Silent Larder history.

Before a player tag changes into a warlord, CBL, or the existing Wendigo country, Event 014 captures the player's achievement evidence and reapplies it to the destination. This prevents a legitimate route from losing its history during the required country transfer. AI countries cannot complete player achievements, capitulated players are excluded, and a manual Event 014 scenario launch disables the campaign set.

## Icon package and wiring

Every identifier requires three independent runtime states under `gfx/achievements/`: the completed icon, a true monochrome `_grey` icon, and a `_not_eligible` icon with the project ineligibility treatment. The 54 textures are registered in `interface/014_cannibalism_achievements.gfx`. The source package must preserve one purpose-built generated master composition per achievement, processed variants, exact 64 by 64 DDS files, hashes, contact sheets, and a GFX handoff. No focus, decision, idea, or report composition may be reused as an achievement icon.

Reveal-dependent achievements remain hidden or use spoiler-safe locked art until their public gates. `Break the Empty Frame` must not depict Hannibal Lecter's face. The transformed route icon must not borrow living Indigenous or sacred motifs.

## Principal implementation surfaces

- definitions: `common/achievements/chaos_redux_achievements.txt`;
- completion predicates: `common/scripted_triggers/014_cannibalism_achievement_triggers.txt`;
- evidence writes and player-transfer helpers: `common/scripted_effects/014_cannibalism_achievement_effects.txt` plus Event 014 core, spread, country, unification, Wendigo, decision, focus, and aftermath effects;
- international response and reconstruction actions: `common/decisions/014_cannibalism_achievement_decisions.txt`;
- localisation: `localisation/english/chaosx_achievements_l_english.yml`;
- sprite registration: `interface/014_cannibalism_achievements.gfx`.

## Future plans

Future achievements should bind to persistent Event 014 evidence: a specific route, country transfer, population ledger, suppression target, anchor, reconstruction obligation, or terminal contract. Event receipt, an unverified decision click, generic conquest, or an untracked casualty total is not sufficient.

