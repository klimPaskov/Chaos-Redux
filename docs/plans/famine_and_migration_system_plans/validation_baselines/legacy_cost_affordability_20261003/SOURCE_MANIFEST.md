# Legacy Custom-Cost Affordability Before-Source Manifest

Date: 2026-10-03.

This exact before archive was copied from the shared pre-patch worktree at Git HEAD `b4131e5d6dc008188054ad67eac66eb03a978917`. It is a fresh legacy-cost baseline, not a source reuse of `validation_baselines/prospective_reception_20261003/` and not the prospective after-source identifier `runtime59ee4eb62`.

Copies were made with `Copy-Item -LiteralPath` and their SHA-256 values were immediately checked against their original source paths. Every listed source/copy pair matched byte-for-byte at capture. The folder-local `.gitattributes` disables text normalization and filters for the archived `.txt` sources and `.csv` scenario fixture.

| Frozen copy | Original source | SHA-256 |
| --- | --- | --- |
| famine_decisions.txt | common/decisions/famine_decisions.txt | 52E84B51B6C9FAF5827F3152613870E4EBBD65215EDD35D70E913D18BA01DFAA |
| migration_decisions.txt | common/decisions/migration_decisions.txt | 66D5DACCB52B11787A53A899B748B2E8F5427E0A8B46A4B303E8BB6A37A01D2F |
| humanitarian_cost_scripted_localisation.txt | common/scripted_localisation/humanitarian_cost_scripted_localisation.txt | 73022A01B7FC1521DE409B97395C628A3373A86B8F687D7AF6C489EC730551D1 |
| famine_relief_triggers.txt | common/scripted_triggers/famine_relief_triggers.txt | A90EF53B81102D7E3BBCA5D0A6856EA4054428E46DEE2B4AC14DC596B2347B4F |
| famine_relief_effects.txt | common/scripted_effects/famine_relief_effects.txt | 571C9A3BCC299CF67A0A32F1844859D226137C4E434026A7E9AB899E733B2959 |
| humanitarian_corridor_triggers.txt | common/scripted_triggers/humanitarian_corridor_triggers.txt | A580C3D9852927B3FB0BB2195A8BB894D4533ADD5750F4B5834022DB8DE8BE50 |
| humanitarian_corridor_effects.txt | common/scripted_effects/humanitarian_corridor_effects.txt | 2FB40A4A239374B40A05D935419B1A744C6DDD6A41B977011493BE0B2A02211B |
| famine_relief_constants.txt | common/script_constants/famine_relief_constants.txt | CAAA63C52EA7765D65392A2F3D96AE98A5DAEB4981D469822200C0E64883CA41 |
| famine_decision_constants.txt | common/script_constants/famine_decision_constants.txt | 32E53D81DEDAE55852B3FD2EC4F81889E41E1EEC471D04255F9877B45B20CB4C |
| migration_decision_constants.txt | common/script_constants/migration_decision_constants.txt | 48C0CBC35AD6E98E2FAC0A4CB5A499DFA71CB06F5B7ADB484A1D05B47E33F9CE |
| humanitarian_corridor_constants.txt | common/script_constants/humanitarian_corridor_constants.txt | 12B774D71734564E8D423BFE68B401E37ADFD73C801B1B3FA9EFAAE0E25C0AAB |
| famine_and_migration_system_probability_scenarios.csv | docs/specs/famine_and_migration_system_specs/famine_and_migration_system_probability_scenarios.csv | 0CA5707ADE8C5565623F1F965B54411523C1EFE25E1AA3909311ECF9B1A4279D |

The source family covers both decision files, their resource-cost selectors, the Famine relief helper that supplies conditional candidate-stock checks and contract setup/delivery, the deferred corridor offer helper path, and the corresponding fee/candidate/AI constants. `migration_open_reception` is not in the 25-decision tranche and is excluded. No absent before source was fabricated.

The exact official scenario CSV is copied unchanged. Existing named cases relevant to the cost tranche include `prob_famine_relief_dense`, `prob_famine_relief_blocked_island`, `prob_humanitarian_border`, `prob_capacity_exhausted_border`, and `prob_corridor_acceptance`; other relevant named scenarios remain available in the CSV. Parent-declared cost cases `cost_stock_exact`, `cost_stock_one_short`, and `cost_stock_late_deficit` are recorded as case labels only; no unsupported scenario objects, countries, scopes, or stock bindings were invented. The proposal/evidence name `fm09_service_affordability` is not treated as accepted design or as an approved fixture.

The Airlift fee remains 10 air experience. The separate 50-XP constant is an existing AI factor threshold, not a player-training minimum or fee. No cost, duration, or AI tuning change is authorized by this baseline audit.
