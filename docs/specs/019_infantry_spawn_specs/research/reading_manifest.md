# Reading manifest and source processing notes

All uploaded source files in `/mnt/data` listed below were read from the local filesystem before the package was written. The package uses the uploaded catalogs, Markdown skill and source files, and TOML subagent instruction files as the available project context.

| File | Bytes | Lines | SHA256 |
| --- | ---: | ---: | --- |
| `AGENTS.md` | 31714 | 372 | `3a1d0e3ec31907507ef403f80245186613c739108fe638f57376430f46556886` |
| `CHAOS_REDUX_MECHANICS.md` | 44359 | 973 | `fb4ed4ab5894c5c93c319c4a144f2f6f95c7593f22286de449681e94675d4715` |
| `chaos-redux-event-assets.md` | 56437 | 1046 | `d145f4300dcba259c8a7a1e28fda36210287942544f41a0e25911bf0a6032f62` |
| `chaos-redux-event-planning.md` | 136300 | 1799 | `8b9091691a0fec22ce912a4fda1634d58918b5bd8ad0dcf3393d52a8f212238a` |
| `chaos-redux-events.md` | 52452 | 692 | `3a16c0fa87a0a9cfe3a48c9d59ce0df746411d91710cd017b2fec47db6703db3` |
| `chaos-redux-frame-animation.md` | 23669 | 483 | `6a4e68dc4e5a89f0b7b8fc8984c0b9cb64665046eaefd728bd41056375cb0d98` |
| `chaos-redux-improvement-loop.md` | 24080 | 275 | `7e137b6135c335e4e92c61768b8231ab433028e8a17d264531d94c3d7c17d4bd` |
| `chaos-redux-subagents.md` | 19124 | 288 | `1d155c650f16f6c4bd0934f8b9e93a063ce79a65b895f45c0aaa860cc713c50e` |
| `chaos-redux-super-events.md` | 30648 | 791 | `8836762ea72460e5686724d090a70f90a30eb588bfb5d4322e5bff99feae1fba` |
| `chaos_redux_clusters_catalog.csv` | 1721 | 15 | `6d21ad63a942c17e0a2a5fa0f836ffa2045b91596c8f6afa8b103bb8bd9fc60e` |
| `chaos_redux_events_catalog.csv` | 56282 | 1035 | `8c669b51f762ec299555bcb79da022221861dea12d80c46fc1770475144a6cfd` |
| `chaos_redux_scenarios_catalog.csv` | 3660 | 20 | `e972443ca43849b3a877ceb2bc4f7171a309c03eaa79cb0df0c630732f496a6a` |
| `chaosx_asset_source_researcher.toml` | 3768 | 55 | `7f313190c45020e62e09a3f66cc3e8ad2015be608e6a0872c2a4c476bc6d7ba3` |
| `chaosx_country_package_auditor.toml` | 6658 | 82 | `77bd4a05c781b059d496b6a4841ea57bdfc5fb905bb97f92bc42c4b1fbea5ea6` |
| `chaosx_decision_mission_auditor.toml` | 4614 | 79 | `eee82ade38e0cf1486b9bfe488369892d6e427d4e5ad364d958e9cd95fdf7455` |
| `chaosx_documentation_curator.toml` | 8360 | 120 | `2f38c7c877c8cc73b6e561ed4d399ae57aa40dcbec5e27f732cd6b532afb9211` |
| `chaosx_event_completion_auditor.toml` | 2947 | 51 | `d37412648d179dc7dadc8913dba8bff3925fb5786b4c2e0f71d3b72678f71ac1` |
| `chaosx_focus_tree_auditor.toml` | 3590 | 76 | `f860bd94466723ef9cac2507b535df1a1e654c8be0bf5e934672df7ea30bd3f6` |
| `chaosx_generated_event_art.toml` | 5843 | 65 | `d11a171e599f51b934961126c788f841b5b60eaa4bd76d87f2d198541b2cc812` |
| `chaosx_icon_artist.toml` | 7178 | 87 | `1efdf3ab7d87531f9ee58c5afc2f89f347eb0a049ee7073d0a933230ceca6759` |
| `chaosx_improvement_loop_planner.toml` | 6261 | 58 | `de14dc22bde794d375a764493d0e4421478a2b31059c78a27c115ab09f8360ba` |
| `chaosx_localisation_auditor.toml` | 4152 | 74 | `51bdc60e44a525ff85d566c7ee87b9ab2958edd7995a53d832f8cbf4376be235` |
| `chaosx_repo_explorer.toml` | 11827 | 231 | `a6aa621bcd37a6fe532881b5cffe148de19561098285bb828fb971d6ed1cc7ca` |
| `chaosx_scripted_system_architect.toml` | 4589 | 71 | `0da8650fcbea795aedc2d225f0dd2ee07f8b853268b7b4cfb423914d2a2c3e89` |
| `chaosx_skill_maintainer.toml` | 3191 | 44 | `56c8c3d4175e5a964bde58beffbd78affb6d02f6953c7ab2cd8b27b6c60d6491` |
| `chaosx_spreadsheet_doc_worker.toml` | 3943 | 54 | `107d79714af672f951c140b64baeaf40bfabb0ff5b9d3c007be1bb81ed1403cf` |
| `chaosx_super_event_audio_researcher.toml` | 3248 | 64 | `ccabb1c32d425c3bbfdc528894b28e62698d16324810001db01f332732247d6f` |
| `chaosx_super_event_text_researcher.toml` | 3839 | 61 | `e434e849ac72ce188e8638541682a4862385c3e4fbbbd170b2655fac5d1125ba` |
| `hoi4-decisions-missions.md` | 43564 | 890 | `04e8fa35106f0557b5e1e313036662747eb180b090a533d59af8830ead801ffa` |
| `hoi4-focus-trees.md` | 45298 | 898 | `bebb8e91fbc5f3c013f99a3237458b50ba9278de44f659337100976372f1d824` |


## Catalog row used

Event 019 in `chaos_redux_events_catalog.csv` is Infantry Spawn, Minor Repeatable, status To Be Reworked. Its stale catalog detail says every country spawns one infantry division on every owned state, with no evolution details filled.

## Sources not available in this chat

The actual Chaos Redux repository tree, offline Paradox wiki snapshot, vanilla Hearts of Iron IV documentation, and the event catalog workbook were not mounted in this chat. The planning package therefore does not claim repository implementation inspection, wiki inspection, vanilla precedent inspection, or workbook editing. The implementation prompt requires those checks before code work.

## Subagent execution note

The project subagent TOML files were read. This chat did not expose a custom Codex subagent execution tool, so subagents were not actually spawned. Their responsibilities were converted into the work orders under `handoff/infantry_spawn_subagent_work_orders.md`.
