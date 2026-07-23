# MCP Installation and Security Plan

## Installation goal

Install and verify three managed components on the Windows workstation:

1. the official Meshy MCP server
2. the official Blender Lab MCP server for isolated development and operator-assisted work
3. the Paradox `io_pdx_mesh` Blender extension

A fourth component, the Chaos Redux Blender HOI4 adapter, is built in the repository and is the only Blender-facing interface permitted for unattended production jobs.

## Version policy

Every dependency is locked by exact version or commit and SHA256 before it is used in a production job.

| Component | Initial planning pin | Promotion rule |
| --- | --- | --- |
| Node.js | 20 LTS or a newer project-approved LTS | Must satisfy Meshy MCP Node 18+ requirement and pass smoke tests |
| Meshy MCP | `@meshy-ai/meshy-mcp-server@0.4.0` | Recheck the official release before implementation and relock after tests |
| Blender | One project-approved version per workstation profile | Must pass Blender MCP and `io_pdx_mesh` compatibility tests together |
| Blender Lab MCP | Exact official release or commit | Install from the official Blender Lab source and lock the archive or commit |
| Community Blender MCP | No default production pin | May be used only as an explicitly approved compatibility backend |
| `io_pdx_mesh` | `0.91` as the initial research baseline | Download the current approved release, hash it, and test mesh and animation export |
| Python/uv | Project-approved current versions | Used for the adapter and Blender MCP server, never inferred from a global install |

The planning pins are not permanent promises. `config/dependencies.lock.example.json` shows the fields that must be resolved on the target machine.

## Meshy MCP installation

### Prerequisites

- Node.js 18 or newer
- `npx` available on `PATH`
- a Meshy API key with API access
- sufficient API credit balance
- outbound HTTPS access to the Meshy API

### Secret handling

The API key must be stored in one of these locations:

1. a user-scoped secret manager used by the MCP host
2. a Windows user environment variable named `MESHY_API_KEY`
3. a local untracked `.env` file read only by the wrapper

The key must never appear in:

- committed MCP JSON
- job YAML
- logs
- screenshots
- task request archives
- issue reports
- handoff documents

The wrapper in `wrappers/run_meshy_mcp.cmd` checks that the variable exists without printing it.

### Windows MCP configuration

Use `cmd /c npx` on Windows. The repository config should point to the wrapper rather than embedding the key.

```json
{
  "mcpServers": {
    "meshy": {
      "command": "C:\\path\\to\\chaos_redux\\.tools\\3d_pipeline\\wrappers\\run_meshy_mcp.cmd",
      "args": [],
      "env": {}
    }
  }
}
```

The wrapper should launch the exact locked package version, not an unversioned latest package.

### Codex project configuration

For Codex, copy the selected tables from `config/codex_mcp.example.toml` into either the user configuration or a trusted project configuration. The template uses stdio `command` and `args`, forwards the Meshy secret by environment-variable name, sets explicit startup and tool timeouts, and restricts Meshy to the workflow's approved tool list.

The proposed `blender_hoi4` table is disabled in the template until the repository-owned server exists and passes its allowlist, path-confinement, dependency-lock, and clean-profile tests. The unrestricted Blender Lab development profile is also disabled by default and must never be substituted silently for the production adapter.

### Meshy smoke test

The installation is accepted only when all of these pass:

1. MCP initializes over stdio.
2. The tool inventory includes image-to-3D, task status, download, remesh, rigging, animation, and balance operations.
3. Balance can be read without exposing the API key.
4. A dry metadata request succeeds.
5. A deliberately invalid request returns a structured error and does not create a paid task.
6. Logs redact authorization headers and environment values.

A paid generation is not part of the installation smoke test. The first paid request belongs to the pilot tranche and requires an approved job record.

## Blender MCP installation

### Two-mode design

#### Development mode

The official Blender Lab MCP server can be enabled in a dedicated Blender profile for exploration, scene inspection, and development of deterministic scripts. It is treated as a privileged tool because it exposes Blender's Python capabilities.

#### Production mode

Unattended jobs call the Chaos Redux `blender_hoi4` adapter. The adapter accepts only structured commands listed in `mcp/blender_allowlist_contract.md` and runs version-controlled scripts. The general Blender MCP server is not exposed to the production orchestration agent.

### Isolated Blender profile

Create a separate profile directory for the workflow. Do not use the artist's normal Blender profile for automation.

Recommended environment isolation:

```text
.tools/3d_pipeline/blender_profile/
  config/
  scripts/
  extensions/
  cache/
```

Set Blender user configuration variables or launch arguments so this profile owns its preferences, installed extensions, recent files, and automation settings.

### Network and listener rules

- Bind Blender MCP to loopback only.
- Do not expose its port through a firewall rule, VPN tunnel, reverse proxy, or LAN listener.
- Do not run it while untrusted `.blend` files are open.
- Disable optional external asset-provider integrations in the production profile.
- Disable telemetry in any compatibility backend that supports a telemetry control.
- Run the adapter against a job copy, never directly against the repository's only source `.blend`.

### Official Blender Lab MCP installation sequence

1. Resolve the current official Blender Lab MCP extension and server versions.
2. Save the source URL, version or commit, license, archive hash, and retrieval date in the dependency lock.
3. Install the extension into the isolated profile.
4. Install the MCP server into a dedicated `uv` or Python environment.
5. Start Blender with an empty scene in the isolated profile.
6. Start the MCP listener on loopback.
7. Start the MCP server and connect from the host.
8. Confirm that the server can inspect the empty scene.
9. Run a disposable cube test in a temporary directory.
10. Shut down and verify that no listener remains active.

### Community compatibility backend

A community Blender MCP backend is not a silent fallback. It may be approved when the official server cannot support the selected Blender version or required host. Approval must record:

- why the official backend cannot be used
- exact repository, release, commit, and checksum
- telemetry state
- listener address and port
- exposed tools
- arbitrary-code risks
- removal plan after official compatibility is restored

The production adapter remains mandatory even when a community backend is used underneath it.

## Paradox `io_pdx_mesh` extension installation

### Dependency lock

The lock entry must include:

- project: `ross-g/io_pdx_mesh`
- approved release or commit
- archive filename
- archive SHA256
- source URL
- GPL license note
- Blender version used for the compatibility test
- tested games and export types
- installation date

### Install sequence

For Blender 4.2 or newer, the extension can be installed from disk. The reproducible command-line route is preferred after its syntax is confirmed against the installed Blender version.

Conceptual command:

```powershell
& $BlenderExe --command extension install-file -r user_default -e $PdxExtensionZip
```

If the installed release is packaged as a legacy add-on rather than a Blender extension, use a version-controlled Blender bootstrap script and record the alternate path. Do not guess between the two packaging modes.

### Verification

The extension is accepted when:

- the expected module is importable
- the PDX Blender Tools registration is present
- a known vanilla `.mesh` can be imported when the extension supports that operation
- a disposable mesh exports without an uncaught exception
- a disposable skeleton action exports when animation export is supported
- the output files are created in the requested folder
- the log records the extension version or commit

A UI panel appearing is not sufficient verification.

## Chaos Redux Blender HOI4 adapter installation

The adapter is a repository-owned MCP server or command service with these properties:

- local-only transport
- structured JSON input
- allowlisted operation names
- path confinement to one job directory plus approved read-only reference roots
- no arbitrary source code argument
- no shell command argument
- no URL fetch from Blender
- deterministic script checksums
- append-only operation log
- explicit save points and rollback copies

The adapter may invoke Blender in foreground or headless mode depending on the operation. Human review operations may use foreground Blender. Audits, exports, and preview renders should support headless execution where the extension permits it.

## Bootstrap phases

`bootstrap/setup_windows.ps1` implements guarded preparation, not blind installation.

### Phase A: discovery

- locate Blender installations
- report Blender version
- report Node, npm, npx, Python, and uv versions
- locate an existing `io_pdx_mesh` installation
- detect Meshy and Blender MCP config entries
- confirm secret presence without displaying it

### Phase B: lock validation

- verify every archive checksum
- reject missing or placeholder checksums
- reject unapproved versions
- verify source archive filenames

### Phase C: installation

- create isolated directories
- install or update approved components
- write project-scoped MCP configuration from a template
- preserve any existing config before changing it

### Phase D: verification

- run `bootstrap/verify_environment.ps1`
- write a machine-readable environment report
- do not mark setup complete while a required check is unresolved

## Security acceptance checklist

- [ ] Meshy key exists but is absent from configuration and logs.
- [ ] Meshy MCP uses an exact package version.
- [ ] Blender MCP binds only to loopback.
- [ ] Production orchestration cannot call arbitrary Python.
- [ ] Blender uses an isolated automation profile.
- [ ] `io_pdx_mesh` archive checksum matches the dependency lock.
- [ ] Job paths are confined to approved roots.
- [ ] External model files are imported into a disposable scene copy.
- [ ] All paid Meshy calls require a job ID and budget gate.
- [ ] Every setup change has a backup or removal procedure.
