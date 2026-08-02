# Event 020 Rat King route depth

The separate `RTX` Rat King now has a 70-focus tree in `common/national_focus/020_black_plague_rat_king_focus_tree.txt`. The tree stays inside the two-tag boundary: `RTA` remains the base Rat Nation and `RTX` remains the separate sentient King.

The opening establishes the Royal Basin, crown, registers, refuge nodes, and capital seals. The player then chooses one mutually exclusive government route: Absolute Crown, Brood Council, or Black-Breath Hierophancy. Each route has its original four-focus core and an additional six-focus lane that explores a distinct royal cost profile.

The Crown lane builds road tithes, wardens, brood ledgers, sanctioned migration corridors, royal auditors, and a final edict. It favors dominion, reserve mass, sentience, cohesion, and advanced royal formations.

The Council lane builds a burrow census, common stores, mobile hospices, shared signal, veteran recall, and a charter of nests. It favors cohesion, hunger relief, sentience, and a resilient division cap without granting human manpower or ordinary equipment.

The Hierophancy lane builds flea liturgy, sea breath, burial rations, ash strongholds, echoes of Doctor Wu, and a terminal omen. It trades hunger risk for dominion, overseas-capable reach, advanced formations, and sentience.

Two shared late lanes sit beside the crisis and terminal branches. Royal Node Watch improves register cohesion and sentience after the first crisis. Crown Strike Preparations improves dominion, the non-human division cap, and terminal preparation while preserving the Evolution V route gate. The court's state-targeted Royal Strike uses the dedicated Royal Node sprite and the canonical exposure route, keeping the rat-side operation legible beside the shared human counterstrike.

Every added reward writes to an existing Rat King register or existing terminal-preparation variable. No focus creates a country tag, a human division, normal equipment, or a political-power store. The existing Evolution V gate now requires the route flag, sentience/cohesion thresholds, terminal preparation, a paid and permanent target-continent selection, target-scoped control, designated capitals, and refuge nodes before the world-end lane can open. Selection is fail-closed to continents with at least 20 eligible states, two capital targets, and two refuge targets, so neither a human choice nor the AI can commit the sovereign to an impossible geography. After Evolution V and the earned route, `black_plague_rat_king_close_the_harbors` and `black_plague_rat_king_silence_the_capitals` provide timed state-targeted operations with Dominion, Brood Mass, military-allocation, factory, and time costs before the 180-day `black_plague_rat_king_crown_the_continent` mission. The operation cancels when the selected geography falls below its gate and reports either `chaosx.nr20.81` or `chaosx.nr20.82`.

The `black_plague_rat_king_court_category` also exposes one route operation per government: Crown Tithe spends Dominion for Brood Mass, Council Audit spends Cohesion for Sentience and renewed Cohesion, and Hierophant Broadcast spends Sentience for Terminal Preparation. Each operation has a visible meter cost and a timed, idempotent country flag so a route choice changes the living court rather than remaining focus-only text. The terminal branch adds a paid target-continent selection with six named choices for human RTX and ratio-based AI selection, followed by harbor interdiction and capital-silencing operations in the same category and a separate Crown-the-Continent mission. Successful harbor and capital actions fire `chaosx.nr20.83` and `.84`; invalidated reserves or targets fire `.85` and `.86` without bypassing the shared disease lifecycle. The three government root focuses also fire the guarded `chaosx.nr20.77` route report once per RTX lifecycle, applying a distinct first-decree effect to Dominion, Cohesion, or Sentience and recording the route's Hunger tradeoff where appropriate.

The three continuing court operations now fire `chaosx.nr20.79` with route-specific descriptions. The report records the Crown tithe, Council ledger, or Hierophant broadcast at completion while the timed operation flag and meter cost remain authoritative for repeat safety.

All added focus names and descriptions are in `localisation/english/020_black_plague_rat_focus_l_english.yml`. The tree uses the existing Event 020 custom focus sprites; no new models are required for this route pass.

## Future depth

Further depth can add route-specific crisis art without changing the three-route or two-tag contract. No bespoke 3D models are required or planned for this route. Live in-game focus timing, AI completion order, and visual spacing remain user-side validation surfaces because the repository workflow does not launch Hearts of Iron IV.
