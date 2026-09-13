# Asset reference skill check

Date: 2026-09-05.
Disposition: implemented and parent-reviewed.
Acceptance basis: the parent explicitly assigned one conditional reusable paragraph for inherited asset reference validation and this handoff.

Full reads completed before editing: `AGENTS.md`, `C:\Users\klimp\.codex\skills\.system\skill-creator\SKILL.md`, and the entire `.agents/skills/chaos-redux-event-assets/SKILL.md` in four contiguous character chunks.
The owning skill matched the supplied 128543-byte baseline with SHA-256 `8289c79cdaf2358ddcbde92dc05156b4375b741d0ed2b51672ec4729989fec5d`.
The required eleven offline core wiki pages were opened, along with Interface modding, Scripted GUI modding, and the relevant Graphical asset modding declarations.
Installed vanilla documentation was searched for the applicable asset terms, and the matching texture, shader, and interface documentation entries were consulted.
No general effect-file extension mapping was documented by that search.

Existing coverage in section 4 required following cataloged vanilla source paths to owning definitions, but the complete skill contained no explicit `effectFile`, `.lua`, or `.shader` lookup rule.
Added one paragraph at section 4's end, starting at line 382, requiring mod and vanilla path checks, matching vanilla GFX and shader inspection before a missing-source finding, exact lookup evidence, and separation of source linkage from rendered or live proof.
The paragraph explicitly rejects assuming a generic `.lua` to `.shader` mapping.
No other skill was created or edited.

Verified source evidence under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`:

- `interface\alerts.gfx` lines 12 and 24 declare `gfx/FX/buttonstate_blendframes.lua` for `GFX_green_alert_glow` and `GFX_yellow_alert_glow`.
- `interface\core.gfx` lines 303 and 637 use the same effect declaration.
- The literal `gfx\FX\buttonstate_blendframes.lua` path is absent.
- `gfx\FX\buttonstate_blendframes.shader` exists and was read in full, including its frame blending and Up, Down, Disable, and Over effects.
- `interface\alerts.gfx` line 5 references `gfx/interface/green_alert_glow.dds`, which exists under vanilla and is absent under the mod root.
- The offline Graphical asset modding page describes relative texture paths and literal Lua effect paths, so installed source evidence is necessary to avoid an unsupported missing-file conclusion.

Validation: the official `quick_validate.py` returned `Skill is valid!`.
Byte comparison against the supplied baseline proved that removing only the inserted paragraph restores the exact baseline bytes.
Final skill SHA-256: `77c4b80516665551a4f36a54e11a4b61bbd590965b6fec5adcb9e64c616bfe34`.
All existing policy, provenance, approval rules, commands, and numbers were preserved.

No simplifications, omissions, or blockers in this bounded change.
Evidence establishes source declarations and resource presence only, with no rendered or live-game correctness claim.
No MCP guidance, routes, viewer capabilities, configuration, runtime files, gameplay, or agent routing changed.
No commit was made under the parent-owned integration boundary.

Parent review confirmed the exact vanilla-reference evidence and the bounded paragraph.
An independent linear byte comparison proved that the 563-byte insertion is the only change from the supplied skill baseline.
The parent owns the selective commit and records it in the central cleanup state.

The reviewed changes are preserved on `codex/documentation-cleanup-review-20260906`.
Integration into the shared working branch remains pending because its Git index lock is owned outside this task.
See the central cleanup record for the selective manifests and integration boundary.

A post-commit comparison on 2026-09-06 found concurrent working-tree changes to the asset skill's animated-unit and armed-unit motion-source paragraphs and completion item 31.
Those protected production-policy changes are outside this cleanup and are not part of review commit `4d069dfb3db3e54f5f9b749f694e564e85e25da5`.
The shared working copy is preserved.
Integration must carry only this task's inherited-reference paragraph and reconcile the independent policy edits through their owner, rather than replacing the whole skill from the review branch.
