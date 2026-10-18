# Handoff 4: missing art and mass asset production

Read `00_common_rules.md` in this folder first. This handoff suits several parallel workers; split by the numbered tasks or by event ranges and claim work in `docs/assets/_claims_2026-10-13.md` before starting it (re-read the file first so two workers never take the same item).

## Rules specific to art

- Read `.claude/skills/chaos-redux-event-assets/SKILL.md` first, and `chaos-redux-frame-animation` for animated pieces.
- Image generation: the `gptimage` MCP server (`generate_image` with an ABSOLUTE `out` path inside the repo). If it is not available, native image generation is allowed provided the file is moved into the repo immediately and the outside copy deleted. Every file you create stays inside the repo.
- Never replace or repoint existing art. New art gets a new name. Wire it only where the consumer has no art or a vanilla placeholder; otherwise leave it unwired and list it.
- Real people's portraits need an attributed source; do not generate faces of real people.
- Transparent families (icons, counters, emblems) need a real alpha channel; verify it in the saved PNG.
- Review a sample of each batch rather than every image. Commit about every 15 minutes.
- Pause generation only if C: has less than 6 GB free.

## Tasks

1. **Art the restore jobs could not recover** (`docs/plans/icons_needing_new_art_2026-10-13.md` and `chaos_redux_restore_assets_audio_2026-10-12.md`): 36 idea icons with no historical original, two category-sized decision icons, five oversized seals, five missing flags, the Matignon texture, and one missing vanilla texture. First search harder for originals (all branches, `git log --all`, dangling commits, `docs/assets/`, `.tmp/`, the Workshop copy of the mod). Only create new art for what truly has none, matching the neighbouring icons of the same family and size.
2. **Blocked families from the earlier shards.** Their progress files are `C:/Users/klimp/Videos/chaos_redux_trailer/records/cx/assets_shard_1.md` to `assets_shard_7.md` (read-only for you). Resolve the blockers instead of skipping them where a decision is all that is missing:
   - Event 072: the approved state-geometry projection and producer;
   - Event 090: flag identities and consumers;
   - Event 108: portrait sources and the animation canvas and binding;
   - Event 114: the category picture consumer size;
   - Event 111: fictional portraits and the 32-frame overlay; four institutional slots without sources;
   - Event 091: real-person portraits and the Lenin super event need sourced placeholders;
   - Events 073 and 095: records out of step with the art that exists.
   Decide from the event spec and the consuming `.gfx`/`.gui` definitions, record the decision in the event's asset handoff, and produce the art.
3. **Mass production.** For every event spec under `docs/specs/` whose asset inventory still lists missing report images, news images, decision, idea, focus, category and achievement icons, flags or super-event scenes: produce the whole family. Events 040 and later first, then unreworked events 001 to 040 that still lack art, then the system packages (chemical, biological, Chaos Warfare doctrine, camps, migration, famine, Chaos Meter, UI fracture variants).
4. **Ten misaligned animated sprite sheets** found earlier: rebuild them from real per-frame art on a fixed canvas so they do not jitter, under new names, and list them for the owner to approve before any rewiring.

## Deliverable

Per worker, a progress section appended to `docs/assets/_progress_2026-10-13.md`: families produced, counts, what was wired, what is unwired and why, commits.
