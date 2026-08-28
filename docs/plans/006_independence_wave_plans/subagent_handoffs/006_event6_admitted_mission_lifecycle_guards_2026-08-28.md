# Event 006 admitted mission lifecycle guards handoff

Date: 2026-08-28.

Owner: parent Event 006 implementation agent.

Scope: admitted Event 006 package categories and founding missions whose setup receipts and capital-control conditions were not consistently enforced at the lifecycle boundary.

The package decision categories for IW-001, IW-002, IW-004, IW-006, IW-007, IW-012, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-033, IW-041, IW-070, IW-071, IW-072, IW-173, and IW-184 now require their matching setup receipt before becoming visible. Karelia/Crimea and Transcaucasus retain package-specific OR branches so one package receipt cannot expose the other package's category.

The founding-mission success branches for those packages now require the matching setup receipt and controlled capital in addition to their existing package, stability, route, ledger, and force conditions. The seven missions whose cancellation triggers lacked receipt loss guards now cancel when the setup receipt disappears. IW-045, IW-040, IW-044, and IW-038 success branches also require their existing setup receipts.

The Pacific founding-mission descriptions state the player-facing capital-control requirement without exposing implementation receipt names.

Changed files:

- `common/decisions/categories/006_independence_wave_categories.txt`
- `common/decisions/006_independence_wave_western_decisions.txt`
- `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt`
- `common/decisions/006_independence_wave_mediterranean_decisions.txt`
- `common/decisions/006_independence_wave_balkan_decisions.txt`
- `common/decisions/006_independence_wave_karelia_crimea_decisions.txt`
- `common/decisions/006_independence_wave_pacific_decisions.txt`
- `common/decisions/006_independence_wave_transcaucasus_decisions.txt`
- `common/decisions/006_independence_wave_bashkiria_mari_decisions.txt`
- `common/decisions/006_independence_wave_frontier_decisions.txt`
- `common/decisions/006_independence_wave_siberian_decisions.txt`
- `localisation/english/006_independence_wave_pacific_l_english.yml`

Focused source assertions cover all 27 targeted founding missions, receipt-gated category visibility, receipt-loss cancellation for the seven previously incomplete missions, setup-and-capital success guards, and the UTF-8 BOM on the touched localization file.

The allocator, country API, strict flag-family, FORM-16, and SCN-008 audits pass with the unchanged 32 content-attested packages, 29 compatible reservation groups, 40 runtime adapters, 161 unattested selectable rows, and 3/4/5/7/10 automatic ladder.

The required Event 006 inspect and render retries remain blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with zero artifacts, so this tranche makes no engine, GUI, probability, balance, or live-runtime claim.

No admission, reservation, package identity, portrait, flag, asset, cost mechanic, timer, AI weight, ledger value, route, or pre-event surface was widened. No fallback or simplification was promoted.
