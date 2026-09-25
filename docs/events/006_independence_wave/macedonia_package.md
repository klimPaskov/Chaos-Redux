# Event 006 IW-026 — Macedonia package

IW-026 uses the registered vanilla `MAC` carrier and the installed-map Macedonia anchor at state `106`. State `970` (Western Macedonia) is an optional extended objective. The package belongs to the Balkans and Danube region, uses the `mountain_or_frontier` archetype, and loads force mapping profile `p26` / `mountain_frontier` with military tradition `65`.

The package preserves the vanilla MAC country definition, history, capital, cores, and base flag family. It does not create a duplicate country, copy a vanilla history file, replace a living country, add advisor icons, or rely on a political-power store. The former Yugoslav host is retained through the allocator's protected-remnant event target and the MAC host-ledger project.

## Runtime surfaces

| Surface | Source |
| --- | --- |
| Package effects and setup/cleanup | `common/scripted_effects/006_independence_wave_balkan_package_effects.txt` (Macedonia source block) |
| Package triggers and exact state/host proof | `common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt` (Macedonia source block) |
| Visible tuning | `common/script_constants/006_independence_wave_constants_registry.txt` |
| Ideas and lifecycle | `common/ideas/006_independence_wave_ideas_registry.txt` |
| Costed decisions and founding mission | `common/decisions/006_independence_wave_balkan_decisions.txt` (Macedonia source block) |
| AI strategy | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` |
| Sourced leader/commander consumer | `common/characters/006_independence_wave_characters_registry.txt` |
| Portrait sprite wiring | `interface/006_independence_wave_portraits_registry.gfx` |
| Localisation | `localisation/english/006_independence_wave_balkan_l_english.yml` (Macedonia section) |

The shared `independence_wave_focus_tree` is assigned as a full framework. Survival, government, economy, military, host, regional, league, and formable lanes therefore update MAC's shared country, host, network, league, and ambition values. Five route governments are available: Municipal Charter, Mountain Workers' Council, Village Autonomy Compact, Mountain Defence Commission, and Patron Rail Compact.

The five-focus REG-03 Vardar group is imported into the full framework only. It opens municipal offices, surveys rail and grain movement, chooses village appeals or mountain-veteran screening, and publishes an arbitration docket. A four-focus route costs 24 focus units, or 168 days at normal speed, and requires state 106 to remain the controlled capital. The root raises civic mandate by 5, the survey raises mountain defence by 5, and the selected branch trades +10 on one ledger for −5 on the other. The docket adds 5 to both ledgers and requires the successful paid community-council or veteran-screening project.

The matching paid project adds a further 5 points to the selected branch ledger whether it succeeds before the focus or afterward. Cancellation grants no companion reward. Its durable awarded marker follows completed focus history and a full-framework reload clears both together. The group uses the five existing Event 006 focus icons in `interface/006_independence_wave.gfx`: `GFX_goal_independence_wave_founding_administration`, `GFX_goal_independence_wave_infrastructure_authority`, `GFX_goal_independence_wave_popular_councils`, `GFX_goal_independence_wave_army_integration`, and `GFX_goal_independence_wave_former_host_settlement`. Their textures live under `gfx/interface/goals/006_independence_wave/`; the focus names, descriptions, ledger tooltips, paid companion tooltips, and docket requirement tooltip are in `localisation/english/006_independence_wave_focus_l_english.yml`.

The complete focus IDs, reward ordering, source wiring, and validation limits are documented in [REG-03 Danube Package Focus Groups](reg03_danube_focus_groups.md).

The group has no custom `ai_will_do` weights. The current probability adapter omits imported shared focuses and the recorded baseline lacks typed campaign inputs, so route-aware AI selection remains unresolved.

The package-specific ledgers are `independence_wave_mac_civic_mandate` and `independence_wave_mac_mountain_defence`, each clamped to the shared 0–100 range and refreshed into `mac_divided_vardar_authority` or `mac_vardar_compact`. The project map pays concrete administration, security, diplomatic, and strategic costs for depots, veteran screening, community representation, host settlement, route selection, durable sovereignty, and Danube network access. The founding crisis is a passive 420-day mission resolved through those costed projects and the shared checkpoint, and fails with a ledger/stability consequence when the compact loses control.

The package-local project lock serializes MAC's own timed projects. It intentionally does not join the shared Event 006 diplomatic/security operation locks, so a MAC founding crisis or host settlement can progress alongside a shared operation. The Danube action is gated to live league phases where the shared league-value writer consumes its deltas, and it cancels if that phase or the league route is withdrawn.

MAC registers the researched `danubian_confederation` formable family for discovery and regional ambition, but FORM-08's three-member identity, anchor, consent, and integration proof remains a separate fail-closed gate. The package is now included in the central content-attestation set; exact host, anchor, reservation, collision, force, and synchronized-transaction preflight still decide every live release.

## Leader and asset gate

The package uses the sourced, male, period-compatible Metodija Andonov-Cento consumer (`MAC_independence_wave_vardar_presidium`) with an unchanged-source head-and-shoulders placeholder and a deterministic 156x210 DDS. No female portrait, generated substitute, generic face, or advisor icon is permitted. The portrait identity, source, crop, role corroboration, rights basis, and runtime wiring are recorded in `006_iw026_macedonia_portrait_source_placeholder_2026_08_06.md`; central attestation still waits for the independent country-package, decision, localisation, AI, flag, and runtime contract audits.

## Admission status

IW-026 is **SOURCE-ATTESTED / CONDITIONAL**. The registry, state binding, package gameplay surfaces, sourced leader/commander consumer, shared-tree assignment, force mapping, AI, localisation, cleanup adapters, and central content attestation are present. The installed MCP probability adapter cannot expose the MAC `ai_strategy_factor` surface, so no quantitative AI-balance claim is made; the package remains subject to the normal exact runtime preflight and its Danubian formable remains separately fail-closed. MAC may therefore enter the active automatic `3 / 4 / 5 / 7 / 10` ladder only when the frozen world-state plan satisfies every shared host, anchor, reservation, collision, force, and synchronized transaction predicate. World Collapse also targets 10 while changing intensity and package pressure.
