# Event 020 Rat King route depth

The separate `RTX` Rat King now has a 70-focus tree in `common/national_focus/020_black_plague_rat_king_focus_tree.txt`. The tree stays inside the two-tag boundary: `RTA` remains the base Rat Nation and `RTX` remains the separate sentient King.

The opening establishes the Royal Basin, crown, registers, refuge nodes, and capital seals. The player then chooses one mutually exclusive government route: Absolute Crown, Brood Council, or Black-Breath Hierophancy. Each route has its original four-focus core and an additional six-focus lane that explores a distinct royal cost profile.

The Crown lane builds road tithes, wardens, brood ledgers, sanctioned migration corridors, royal auditors, and a final edict. It favors dominion, reserve mass, sentience, cohesion, and advanced royal formations.

The Council lane builds a burrow census, common stores, mobile hospices, shared signal, veteran recall, and a charter of nests. It favors cohesion, hunger relief, sentience, and a resilient division cap without granting human manpower or ordinary equipment.

The Hierophancy lane builds flea liturgy, sea breath, burial rations, ash strongholds, echoes of Doctor Wu, and a terminal omen. It trades hunger risk for dominion, overseas-capable reach, advanced formations, and sentience.

Two shared late lanes sit beside the crisis and terminal branches. Royal Node Watch improves register cohesion and sentience after the first crisis. Crown Strike Preparations improves dominion, the non-human division cap, and terminal preparation while preserving the Evolution V route gate. The court's state-targeted Royal Strike uses the dedicated Royal Node sprite and the canonical exposure route, keeping the rat-side operation legible beside the shared human counterstrike.

Every added reward writes to an existing Rat King register or existing terminal-preparation variable. No focus creates a country tag, a human division, normal equipment, or a political-power store. The existing Evolution V gate still requires the route flag, sentience/cohesion thresholds, terminal preparation, continental control, designated capitals, and refuge nodes before the world-end effect can fire.

The `black_plague_rat_king_court_category` also exposes one route operation per government: Crown Tithe spends Dominion for Brood Mass, Council Audit spends Cohesion for Sentience and renewed Cohesion, and Hierophant Broadcast spends Sentience for Terminal Preparation. Each operation has a visible meter cost and a timed, idempotent country flag so a route choice changes the living court rather than remaining focus-only text.

All added focus names and descriptions are in `localisation/english/020_black_plague_rat_focus_l_english.yml`. The tree uses the existing Event 020 custom focus sprites; no new models are required for this route pass.

## Future depth

Further depth can add route-specific report text and crisis art without changing the three-route or two-tag contract. Live in-game focus timing, AI completion order, and visual spacing remain user-side validation surfaces because the repository workflow does not launch Hearts of Iron IV.
