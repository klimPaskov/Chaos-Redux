# Validation Report

**Generated:** 2026-07-22T11:28:07.125915+00:00

**Status:** `passed_with_environment_limitations`

**Pre-manifest package files inspected:** 50

## Results

| Check | Status | Detail |
| --- | --- | --- |
| `source_file_count` | PASS | 50 pre-manifest package files inspected |
| `no_empty_files` | PASS | none |
| `utf8_text_package` | PASS | all package files are UTF-8 text |
| `json_parse` | PASS | 7 files parsed |
| `json_schema_meta_validation` | PASS | 2 schemas valid |
| `model_job_example_validation` | PASS | schema-valid |
| `evidence_example_validation` | PASS | schema-valid |
| `toml_parse` | PASS | 2 files parsed |
| `codex_mcp_safety_defaults` | PASS | Meshy enabled, proposed Blender servers disabled, secret forwarded by name, tool allowlists present |
| `python_compile` | PASS | 2 files compiled |
| `credit_estimator_known_case` | PASS | subtotal=29, total=29 |
| `unknown_uv_unwrap_price_not_invented` | PASS | exit=2, unknown price rejected |
| `artifact_hash_tool` | PASS | files=7 |
| `asset_profile_coverage` | PASS | static_prop, building, humanoid_unit, nonhumanoid_creature, vehicle_land, aircraft, naval, articulated_attachment |
| `source_register_complete` | PASS | 31 supplied sources named |
| `supplied_source_files_present` | PASS | 31 supplied sources present in /mnt/data |
| `required_package_paths` | PASS | 33 required paths present |
| `no_embedded_secrets` | PASS | no likely literal credentials found |
| `meshy_wrapper_version_and_secret_policy` | PASS | exact default version and no key echo |
| `blender_production_forbidden_capabilities` | PASS | arbitrary code, shell, URL, and unrestricted filesystem are explicitly forbidden |
| `no_em_dash_in_project_prose` | PASS | none |
| `no_semicolon_in_project_prose` | PASS | none |
| `bootstrap_static_contracts` | PASS | dry-run support, checksum gate, extension command, Codex template, and readiness report present |

## Environment limitations

- PowerShell and Windows CMD scripts were statically reviewed but not executed because this Linux environment does not provide PowerShell, Windows CMD, or the target Blender installation.
- Meshy MCP was not started and no paid Meshy API call was made because the target API key, entitlement, and credit approval are not available in this environment.
- Blender Lab MCP, the proposed Blender HOI4 adapter, io_pdx_mesh, vanilla HOI4 model files, and the live Chaos Redux repository were not available for runtime compatibility tests.
- No in-game HOI4 validation was possible. The package correctly leaves runtime completion blocked until target-machine pilots and in-game evidence exist.

## Interpretation

The planning package and its machine-readable examples passed structural validation. This does not prove that the target Windows workstation, current Blender release, Blender MCP server, Paradox exporter, Meshy account, vanilla model precedents, or HOI4 runtime are compatible. Those are explicit promotion blockers in `14_open_decisions_and_blockers.md`.

No fallback, installation, export, or in-game completion claim is made by this report.
