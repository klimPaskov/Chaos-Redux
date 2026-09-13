# Launch04 native crash evidence

## Capture

- Source: `.tools/qa/dumps/launch_04/hoi4.exe_260905_092433.dmp`.
- ProcDump completed at 2026-09-05 09:28:04 with 4,395 MB written, then logged `Dump count reached` at 09:28:07.
- Analysis was read-only and used a memory mapped dump with bounded reads; no HOI4 process was launched, queried, stopped, or controlled.

## Recovered exception

- Exception thread: `0x6104` (decimal 24836).
- Exception code: `C0000005`.
- Exception RIP: `0x7FF6C2C7868A`, which is `hoi4.exe` image RVA `0xA9868A` for module base `0x7FF6C21E0000`.
- x64 context was present at dump RVA `0xCD22` with size `0x4D0`.
- Registers at the exception include `R14=0`, `R12=0`, `RSP=0x573BFFC700`, and `RBP=0x573BFFC800`.
- Bytes at the fault are `45 38 66 20`, decoded as `cmp byte ptr [r14+20h],r12b`; the attempted address is therefore null plus `0x20`.

## Call-state evidence

- The crashing function at RVA `0xA98600` computes `r14 = [r9] + (fifth_argument * 40)` before the fault.
- The saved original `r9` points to `0x573BFFC8B0`, whose value is null in the captured stack.
- The saved original `RCX` points to heap object `0x23693134510`.
- That object contains the inline key `carrier_support_equipment_availability_threshold`.
- Repository search maps this key uniquely to `common/script_constants/006_independence_wave_constants_registry.txt:3470` under `independence_wave_form48_cost`.
- The two source consumers are `common/scripted_triggers/006_independence_wave_form48_triggers.txt:382` and `:388`.
- The captured heap contains neighboring constant keys and source-path data, and the executable contains `script_constant.cpp` schema-diagnostic strings, supporting a script-constant/schema processing path.

## Phase classification

The evidence does not conclusively distinguish constant-database/schema ingestion from a later lookup or consumer validation call. It favors engine processing of the loaded constants/schema object because the live original `RCX` is the parsed key object and the call builds a 40-byte indexed table entry, but this is not proof that the key definition alone caused the null table.

## Narrow next diagnostic

Use a reversible source-level A/B test owned by the parent that isolates the Form48 constant path while preserving the rest of the registry, then compare whether the crash remains at the same RVA. A disappearing crash would identify the Form48 constant/consumer path as the trigger; persistence would shift attention back to another loaded constant or engine table initialization. Do not treat this dump as proof of a sole causal line.

## Reusable command

```text
dumpbin.exe /disasm /range:0x140A98600,0x140A98800 "C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\hoi4.exe"
```

No gameplay files, GUI files, documentation, or concurrent event files were edited, and no commit was created.
