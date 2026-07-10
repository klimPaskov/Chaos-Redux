# Event 014 Cannibalism Achievement Implementation Prompt

Read Part 11, the achievement section of the planning skill, the event asset skill, and existing Chaos Redux achievement files.

Implement all 18 planned achievements. Treat the IDs in Part 11 as working keys that can be adjusted only to match repository naming rules. Preserve their conditions, disqualifiers, visibility, difficulty, and route coverage.

Requirements:

- no achievement unlocks merely because Event 14 fires
- no early achievement title or description reveals Hannibal or the Wendigo branch
- hidden achievements become visible only after the matching public reveal
- exploitation disqualifiers are permanent where specified
- population, state, country, and network conditions use real tracked values
- tag transfer during Hannibal or Wendigo unification preserves eligible player history
- global victory requires all cells, communes, islands, warlords, and unified actors to be gone
- terminal achievements require chaos above 1000 and the correct world-end flag
- manual scenario eligibility follows project-wide achievement policy

Implement:

1. Clean containment in the first host without spread or exploitation.
2. Worldwide containment before a second country develops a cell.
3. Containment in three countries with joint suppression and no warlord state.
4. Recovery of three silent islands or isolated coastal nodes.
5. A locally cured country defeating later external return.
6. Dismantling a terror-exploitation program before commune formation.
7. Defeating an Island Host through blockade, landing, and rescue.
8. A defiant warlord surviving Hannibal's reveal and remaining independent.
9. A player warlord becoming unification host while retaining three named warlords.
10. Unified Hannibal absorbing every surviving cult actor.
11. Unified Hannibal maintaining feeding states on three continents before terminal world-end.
12. Breaking convergence and preventing the reveal.
13. Defeating revealed Hannibal before terminal lock and completing global stabilization.
14. Breaking every Wendigo transformation anchor before lock.
15. Completing ordinary Hannibal world-end.
16. Completing Wendigo Hannibal world-end.
17. Completing global recovery and the memory system after a costly defeat.
18. Defeating the evolved crisis without any state reaching Silent Larder.

For each achievement implement:

- tracking flags and variables
- unlock trigger
- disqualifiers
- localisation written from the spec direction
- completed, grey, and not-eligible 64 by 64 icons
- `.gfx` registration
- documentation and manifest entry
- event, focus, decision, evolution, country, or super-event hooks

Run a spoiler audit on the achievement list and a route coverage review. Report any merged, simplified, omitted, or blocked achievement. No fallback icons or automatic unlocks are allowed.
