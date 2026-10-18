# Handoff 14: HOI4 Agent Tools renderer stalls on the Chaos Redux workspace

This handoff works in a DIFFERENT repo: `C:/Users/klimp/Documents/Projects/hoi4-agent-tools` (github.com/klimPaskov/hoi4-agent-tools). Read that repo's `AGENTS.md` first. Of `00_common_rules.md`, only these apply: work autonomously, no AI attribution, never force-push `main`. It can run at the same time as all the others.

## Why

Every Chaos Redux job that tried `hoi4_gui_render`, `hoi4_tech_render` or `hoi4_gui_inspect` on the full Chaos Redux workspace reported that it stalled or timed out, so no restored window or technology folder has been checked visually. Earlier the same tools crashed with `JOB_WORKER_EXIT` and leaked temporary folders; fixes for those were merged for 4.0.1 and later.

## Tasks

1. Reproduce against `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux` (read-only use of that repo): `hoi4_tech_render` of the chemical and biological folders, `hoi4_gui_render` of the event log, Chaos Meter, settings and camps windows, and one super event. Measure where the time goes (indexing, asset decoding, layout, worker start-up, memory).
2. Fix the cause so a single window or folder renders in well under a minute on this workspace: incremental or cached indexing, lazy asset decoding limited to what the requested view needs, bounded memory, a clear progress and timeout error instead of a silent stall.
3. Known renderer defects to fix while there: hidden sub-windows drawn, animated sprites shown as static first frames, 16-bit DDS portraits not decoded, raw localisation keys and `$TOKEN$` placeholders left unresolved, white super-event text, division designer running out of memory.
4. Tests for each fix; CI green on Windows and Ubuntu; release a patch version through the repo's normal release process, keeping exactly one clean release, and update the installed copy the Chaos Redux repo's MCP configuration points at.
5. Then render the windows and folders from task 1 and save the PNGs to `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.tmp/renders_2026-10-13/` for the owner.

## Deliverable

Short report: cause, fix, timings before and after, release URL, the render paths, what still fails.
