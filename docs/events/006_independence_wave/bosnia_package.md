# IW-029 Bosnia package

IW-029 is the Bosnia carrier overlay for the Independence Wave. It reuses the vanilla `BOS` country, vanilla state 104 as the Sarajevo anchor, optional state 804 as the Herzegovina expansion state, and the living `YUG` former-host relationship. It never writes a BOS history file and does not replace the meaningful vanilla tree.

## Runtime contract

- Exact package ID: `independence_wave_package_id.iw_029`.
- Region: Balkans/Danube; depth: regional; archetype: mountain/frontier.
- Reservation group: `rg_104`; anchor: state 104; optional territory: state 804.
- Candidate gate: `is_independence_wave_exact_package_iw_029_tag_available`.
- Setup adapter: `independence_wave_setup_iw_029_bosnia`.
- Final validation: `independence_wave_validate_iw_029_bosnia`.
- Cleanup adapter: `independence_wave_cleanup_iw_029_bosnia`.
- Event 006 uses the shared generic focus framework with all five government routes, four host routes, the Danube formable family, the ambition ledger, the internal power-struggle type, signature module, league route, and p29 mountain-frontier force mapping.

## Visible mechanics

`independence_wave_bos_drina_civic_mandate` measures Sarajevo/cantonal administration, while `independence_wave_bos_mountain_defence` measures the mixed officer board, depots, and defecting formations. The lifecycle ideas `bos_divided_drina_authority` and `bos_drina_compact` expose the state of both ledgers. Route ideas are mutually exclusive: `bos_sarajevo_charter`, `bos_drina_workers_council`, `bos_cantonal_compact`, `bos_mountain_command`, and `bos_corridor_accord`.

The package exposes a 420-day founding mission plus paid administration, security, diplomatic, and strategic projects. Projects cancel on loss of the Sarajevo anchor, a broken host relationship, invalid package origin, or a closed league phase. All failure paths lower the country ledgers and shared state values; no project creates a political-power store or free-unit loop.

## Forces and leadership

The force mapping is p29 (`mountain_frontier`, military tradition 66) with the documented pathways: integrate militias, secure depots, convert defecting host units, recruit terrain units, and create a professional officer corps. The synchronous `chaosx.nr6.350` roster checkpoint idempotently attaches `BOS_independence_wave_drina_council`, which is promoted through the five route ideologies and supplies the same sourced male Mehmed Spaho portrait to the civilian and army-large consumers. No advisor, dossier, commander-small, or alternate portrait art is defined.

## Files and asset wiring

- Gameplay: `common/scripted_triggers/006_independence_wave_bosnia_package_triggers.txt`, `common/scripted_effects/006_independence_wave_bosnia_package_effects.txt`, `common/decisions/006_independence_wave_bosnia_decisions.txt`, `common/ideas/006_independence_wave_bosnia_ideas.txt`, `common/script_constants/006_independence_wave_bosnia_constants.txt`, `common/characters/006_independence_wave_bosnia_characters.txt`, `common/ai_strategy/006_independence_wave_bosnia.txt`.
- Runtime portrait consumer: `interface/006_independence_wave_iw029_bosnia_portraits.gfx`, sprite `GFX_portrait_BOS_independence_wave_mehmed_spaho`, texture `gfx/leaders/006_independence_wave/portrait_BOS_independence_wave_mehmed_spaho.dds`.
- Source master, explicit crop, processed PNG, provenance, and visual review: `docs/assets/portraits/006_independence_wave/iw029_bosnia_mehmed_spaho_source_placeholder_2026_08_06/` and `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw029_bosnia_portrait_source_placeholder_2026_08_06.md`.
- Localisation: `localisation/english/006_independence_wave_bosnia_l_english.yml`.

## Future deepening

The shared generic tree can later add BOS-specific signature focuses that call the five `independence_wave_bos_focus_*` hooks. A later accepted package tranche may add researched historical flags or additional sourced male consumers, but this carrier remains fail-closed until those assets and the independent country, decision, localisation, AI, host-survival, and MCP checks are recorded.
