# Asset LFS Hydration Skill Update

Status: complete.

Scope: Updated `.agents/skills/chaos-redux-event-assets/SKILL.md` with a reusable preflight for mixed `.gfx` text registries and binary artwork or audio.

## Captured workflow

- Detect LFS pointer stubs by the exact pointer signature, never a byte-size threshold; legitimate tiny images remain valid candidates.
- Run scoped `git lfs checkout <paths>` first when objects are already present locally, preserve modified files, and use fetch or pull only for missing objects with explicit authorization.
- Compare every expected hydrated file's SHA-256 with the index OID from `git lfs ls-files -l`, confirm zero remaining pointer stubs, and record any index-refresh warning without discarding successful content/OID evidence.
- Validate image and audio containers with format-aware decoders or parsers after hydration.

Files changed: `.agents/skills/chaos-redux-event-assets/SKILL.md` and this handoff.

No gameplay, assets, `.gfx`, AGENTS, Qoder, or tools were changed, and no blocker remains for this bounded documentation update. The parent agent owns the commit.
