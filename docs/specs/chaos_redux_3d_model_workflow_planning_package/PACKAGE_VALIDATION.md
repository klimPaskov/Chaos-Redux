# Package Validation

Validation date: 22 July 2026.

## Result

The planning package passed its available structural, schema, helper, safety, and archive checks. No live Meshy task, Blender session, PDX export, or HOI4 runtime test was possible in this hosted environment. Those remain mandatory pilot gates before repository promotion.

## Checks completed

### Source and package structure

- Confirmed that the source reading record covers all 31 supplied files.
- Confirmed that the skill folder copy and flat package copy are byte-identical.
- Confirmed that the compact goal prompt is 2,585 characters, below the 4,000-character target.
- Confirmed that all local Markdown links resolve.
- Confirmed that no Python bytecode or cache directory remains in the final package.

### Python and data files

- Compiled all three Python scripts with `py_compile`.
- Parsed all JSON files.
- Parsed all TOML files.
- Parsed the YAML job example.
- Validated `config/job.example.yaml` against `schemas/model_job.schema.json`.
- Validated `templates/model_manifest.example.json` against `schemas/model_manifest.schema.json`.

### Blender add-on installer helpers

The pure helper layer of `scripts/install_blender_addons.py` passed synthetic tests outside Blender:

- detected `io_pdx_mesh` from a valid `blender_manifest.toml`
- found a flat archive module root correctly
- rejected a ZIP path traversal entry using `../escape.py`

The Blender operators, preference persistence, extension repository, and add-on enablement paths still require a real Blender 4.2 or later pilot.

### Model package validator

`scripts/validate_model_package.py` passed three synthetic test classes:

- an empty package failed as expected with blocking findings
- a complete package with one mesh, one DDS texture, idle, move, and attack animation exports passed with zero blockers and zero review findings
- a manifest path that escaped the package root failed as expected with `path_escapes_package`

The positive fixture also proved that complete manifests require explicit animation action labels and at least one runtime consumer.

### PowerShell bootstrap

- Confirmed balanced parentheses, braces, and brackets by static inspection.
- Confirmed that the script is dry-run first and gates configuration writes, downloads, and Blender invocation behind `-Apply`.
- Confirmed that the Codex configuration forwards `MESHY_API_KEY` by variable name through `env_vars` and does not write its value.
- Confirmed that the Paradox release resolver refuses ambiguous archive selection.

PowerShell was not installed in this environment, so the script was not parsed or executed by a PowerShell runtime. A Windows pilot must run the dry mode first, then the apply mode in a disposable setup.

### Content hygiene

- No em dash or semicolon was found in package Markdown.
- No real API key was found. Secret-looking values are explicit replacement placeholders only.
- No third-party binary, add-on archive, model, texture, or font is included.

## Runtime validation still required

The package must not be promoted as a proven production workflow until a local pilot supplies all of the following evidence:

1. Meshy MCP connects in a new Codex session and the balance-only smoke test succeeds.
2. Blender MCP connects only to localhost and persists after Blender restart.
3. Blender MCP optional external asset providers remain disabled and telemetry remains disabled.
4. The Paradox extension persists after restart.
5. A named vanilla `.mesh` imports successfully.
6. A disposable static model exports and reimports successfully.
7. A disposable animated model exports and reimports successfully.
8. One static prop pilot and one animated humanoid pilot pass the full manifest and QA gates.
9. HOI4 displays correct scale, direction, materials, shadow behavior, and action mapping.
10. Exact local versions, hashes, exporter settings, executed Blender scripts, and evidence paths are recorded.

## Validation boundary

These checks prove package consistency and defensive behavior. They do not prove visual fidelity, rig deformation, loop quality, exporter compatibility, entity wiring, or in-game rendering. The package deliberately keeps those as blocking runtime evidence rather than treating structural validation as completion.
