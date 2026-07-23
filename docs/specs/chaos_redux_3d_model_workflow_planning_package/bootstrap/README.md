# Windows Bootstrap Assets

These scripts are guarded setup assets. They do not claim the workstation is already configured.

## Safety model

- Discovery and validation run by default.
- Changes require `-Apply`.
- External archives must already exist locally and match approved SHA256 values.
- No API key is written to disk.
- Existing MCP configuration is backed up before a project configuration is copied.
- Blender extensions are installed into the selected Blender profile only.

## Expected sequence

```powershell
# 1. Fill and approve the dependency lock.
Copy-Item ..\config\dependencies.lock.example.json ..\config\dependencies.lock.json
# Edit versions, commits, archives, hashes, and approved states.

# 2. Discovery only.
.\setup_windows.ps1 `
  -RepoRoot "C:\path\to\chaos_redux" `
  -BlenderExe "C:\Program Files\Blender Foundation\Blender 5.1\blender.exe"

# 3. Install checksum-locked extensions after reviewing the dry run.
.\install_blender_extensions.ps1 `
  -BlenderExe "C:\Program Files\Blender Foundation\Blender 5.1\blender.exe" `
  -PdxZip "C:\approved_downloads\io_pdx_mesh.zip" `
  -PdxSha256 "REPLACE" `
  -BlenderMcpZip "C:\approved_downloads\blender_lab_mcp.zip" `
  -BlenderMcpSha256 "REPLACE"

# 4. Repeat with -Apply.

# 5. Verify and write a JSON report.
.\verify_environment.ps1 `
  -RepoRoot "C:\path\to\chaos_redux" `
  -BlenderExe "C:\Program Files\Blender Foundation\Blender 5.1\blender.exe" `
  -OutputPath "C:\path\to\chaos_redux\.tools\3d_pipeline\reports\environment.json"
```

## API key

Set the user environment variable outside the repository:

```powershell
[Environment]::SetEnvironmentVariable("MESHY_API_KEY", "msy_REDACTED", "User")
```

Open a new terminal after changing it. Verification reports only whether it exists.

## Required review before `-Apply`

- dependency lock has no placeholder hashes
- Blender version is the approved version
- extension archives come from the recorded sources
- MCP config destination is correct for the selected host
- the Blender profile is isolated from the normal artist profile

## MCP configuration templates

`setup_windows.ps1` defaults to the Codex TOML template. Pass `-ProjectMcpTemplate` explicitly to use the generic JSON host template instead. Both files contain placeholders and no secrets. The production Blender entry stays disabled until the adapter is implemented and verified.
