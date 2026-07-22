# Portrait source-mode skill update — 2026-07-22

## Scope

Updated the reusable portrait workflow so source mode is decided from polity identity
before any portrait worker is routed. No gameplay, localisation, asset, GFX, spec, or
event files were edited. No commit was created.

## Exact edits

- `.agents/skills/chaos-redux-event-assets/SKILL.md`
  - Added a fail-closed portrait source-mode gate for grounded identities (real,
    historical, restored, separatist, regional, indigenous, dynastic, or otherwise
    plausibly historical countries, polities, and communities) versus
    `fictional_high_chaos`/impossible-supernatural identities.
  - Grounded identities now require a sourced real male leader or another defensible
    sourced real-person candidate appropriate to time and place; no invented
    officeholder or generated-face substitute is allowed. Missing candidates block the
    leader portrait.
  - Restricted generated one-person leaders to truly fictional high-chaos or
    impossible/supernatural entities and required memorable invented regalia, dress,
    adornment, ritual objects, altered uniforms, or coherent high-chaos motifs while
    banning modern props, generic faces, meme aesthetics, gore, mockery, stereotypes,
    and caricatures of real cultures.
  - Added manifest, handoff, workflow, and final-checklist requirements for explicit
    identity classification, source mode, evidence, and blocked outcomes.
- `.codex/agents/chaosx_asset_source_researcher.toml`
  - Requires the parent classification, routes grounded identities to sourced real
    candidates, and fails closed with `blocked` when no defensible source exists.
  - Preserved the concurrent repository-path correction for the report-image processor.
- `.codex/agents/chaosx_generated_event_art.toml`
  - Requires an explicit allowed classification for one-person leader/officeholder
    portraits, refuses grounded identities, and directs unresolved cases to the source
    researcher or `blocked` status.
  - Added the memorable high-chaos portrait direction and anti-stereotype/anti-meme
    constraints.

## Validation and remaining conflicts

- Reviewed the offline wiki core pages and relevant vanilla documentation as required
  by `AGENTS.md`; this change is instruction-only and does not alter Clausewitz syntax.
- Inspected the diff for accidental scope expansion and checked the edited TOML blocks
  remain inside their existing triple-quoted instruction strings.
- The broader sentence in `.agents/skills/chaos-redux-subagents/SKILL.md` that says
  fictional one-person portraits require ImageGen is still generic and was not edited:
  the new event-assets gate and both asset-agent prompts qualify that routing. Parent
  review may harmonize that sentence if the subagents skill is later in scope.
- Existing concurrent edits in the event-assets advisor paragraph and source-researcher
  processor path were preserved.
