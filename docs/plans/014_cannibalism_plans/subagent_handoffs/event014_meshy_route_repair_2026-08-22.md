# Event 014 Meshy MCP route repair handoff

## Scope and result

The bounded repository-owned Meshy MCP compatibility route is healthy. No Event 014 gameplay or asset file was edited, no model was generated, and no paid Meshy operation was called.

The initial failure came from the compatibility runtime resolving `@modelcontextprotocol/sdk` through the Meshy package's broad `^1.6.1` range to `1.30.0`. That installed package advertised `dist/esm/server/index.js` but did not contain it, and the wrapper's manifest-only test incorrectly reused the broken runtime.

The repaired route locks the last SDK release available when `@meshy-ai/meshy-mcp-server@0.4.0` was published: `@modelcontextprotocol/sdk@1.29.0`. The runtime root is versioned by both package versions at `.tmp/meshy_mcp_compat_v4_0_4_0_sdk_1_29_0`, verifies the required SDK entry point, and reconstructs exact dependencies through npm when the version or entry point is absent.

## Files changed

- `.tools/3d_pipeline/config/dependencies.lock.json` — records Meshy package integrity and the exact SDK package, version, git head, integrity, and required entry point. SHA-256 `4B8B569DD1032F2D75D216660ECF6F54B8C229804F3D067ED3673851E8216439`.
- `.tools/3d_pipeline/config/meshy_tool_schema.lock.json` — records compatibility SDK `1.29.0`. SHA-256 `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`.
- `.tools/3d_pipeline/wrappers/run_meshy_mcp.ps1` — reads the SDK version from the dependency lock, uses a package-and-SDK-versioned compatibility runtime, checks actual package versions and `dist/esm/server/index.js`, and installs both exact packages when repair is needed. SHA-256 `D77B0A4CD995E93C2FCE3F91688B4D03F21D7C9380901B7A1B386982A4D17852`.
- `.tools/3d_pipeline/lib/mcp_stdio.py` — adds a strict `tools/list` request mode using the same one-shot stdio lifecycle and descendant cleanup. SHA-256 `97BE3ABE33903C9B64B93783F3F3A454CC4392C5C7375E6C9D80320A3286B503`.
- `.tools/3d_pipeline/verify_environment.py` — verifies the exact Meshy and SDK versions, required SDK entry point, all locked tool identifiers, explicit `meshy-7` schema exposure, and the read-only balance probe. SHA-256 `A62B5AA452266FC4C05BBBE112D7545CE995093B946B72A416DEB409A5738C7C`.
- `.tools/3d_pipeline/reports/environment_report.json` — refreshed successful dependency and route evidence. SHA-256 `67BCD49313C4EEEB27AD700A19F7285A86A5D6B6DADAECEF8BBDAB4172294AB6`.

## Locked dependency evidence

- Node: `v24.15.0`.
- Meshy MCP: `@meshy-ai/meshy-mcp-server@0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, npm integrity `sha512-py2xFIrrBcU4SW7ked90/qjRqa6bheVn0fNLEW8Lnki3BCJTFaVvWN0W6a9mJYr26+M9y0WezGsTCKalzWrGtg==`, installed manifest SHA-256 `969EACB956C2F2EE89735A2B1BE772C41E1BDBA263596659BD272ADBCAEA104C`.
- MCP SDK: `@modelcontextprotocol/sdk@1.29.0`, git head `e12cbd7078db388152f6e839abdbe09ba01f3f32`, npm integrity `sha512-zo37mZA9hJWpULgkRpowewez1y6ML5GsXJPY8FI0tBBCd77HEvza4jDqRKOXgHNn867PVGCyTdzqpz0izu5ZjQ==`, installed manifest SHA-256 `7AB20EBA8FEE70F316516B5B3FC45837294CAEE7E4DD36F2A1593210B0F003AC`.
- Blender: lock-selected `5.1.2`; full verifier check passed.
- Blender HOI4 adapter: lock-selected `1.5.0`; version, operation list, and source checksum checks passed.
- `io_pdx_mesh`: `0.91.0`; archive, checksum, installed manifest, export, animation, and reimport checks passed.

## Commands and meaningful output

Hard key gate, performed before repository or job discovery:

```powershell
if ([string]::IsNullOrWhiteSpace($env:MESHY_API_KEY)) { Write-Output 'MISSING' } else { Write-Output ("PRESENT length=" + $env:MESHY_API_KEY.Length) }
```

Output: `PRESENT length=40`. The key value was never printed or stored.

Two consecutive schema probes used the repository wrapper through `lib.mcp_stdio.call_stdio(..., list_tools=True)`. Each returned 24 tools, all eight locked tools were present, and the `meshy_image_to_3d` input schema contained the exact `meshy-7` identifier:

- `meshy_check_balance`
- `meshy_image_to_3d`
- `meshy_get_task_status`
- `meshy_download_model`
- `meshy_remesh`
- `meshy_rig`
- `meshy_convert`
- `meshy_animate`

The patched/runtime files were identical after both probes:

- `dist/constants.js`: 9,615 bytes, SHA-256 `76A5D40B149B781CC53C8D94E12BFC9B5612C1B359C9E3AB6FE4AC67807AD8A6`.
- `dist/tools/generation.js`: 22,754 bytes, SHA-256 `5380E2E89E739A95BF67BFA3361D43D2A85E539F2DE263F79762B7E9C6B57496`.
- `dist/schemas/generation.js`: 12,551 bytes, SHA-256 `F2796DAC0B8F9CAED1D32092E5DD4197F460EB0ED85A083AEA99CDDDF00DB724`.
- SDK `dist/esm/server/index.js`: 21,161 bytes, SHA-256 `8DBEE2AC3001C9685AD49A2D6B2C59973CA0B223579EC353F9C2E199484591B0`.
- SDK `dist/esm/server/streamableHttp.js`: 6,534 bytes, SHA-256 `E811D93AF3F5E62497CF208CE162761C64CFD1C79FC4A0D8C77BE59E0A77360B`.

Full verification was run repeatedly with:

```powershell
python .tools/3d_pipeline/verify_environment.py --probe-meshy
```

Final output:

```json
{
  "report": "C:\\Users\\klimp\\OneDrive\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\chaos_redux\\.tools\\3d_pipeline\\reports\\environment_report.json",
  "findings": []
}
```

The live read-only balance result was `626` credits. Balance checks consume no credits. Estimated and consumed credits for this repair are both `0`.

## Status and parent follow-up

- Meshy MCP route: `complete` for this repair scope.
- Meshy 7 schema gate: `complete`.
- Balance gate: `complete`.
- Paid/model work: deliberately not started.
- Remaining blocker: none in the repaired route.
- Parent may proceed with Event 014 job/reference preflight and ordinary production gates. Final runtime wiring and in-game validation remain parent-owned.

No fallback or simplification was used. The earlier failed `1.6.1` diagnostic runtime and original broken `1.30.0` runtime remain under `.tmp` as non-runtime evidence; the wrapper deterministically selects only the locked `1.29.0` runtime.
