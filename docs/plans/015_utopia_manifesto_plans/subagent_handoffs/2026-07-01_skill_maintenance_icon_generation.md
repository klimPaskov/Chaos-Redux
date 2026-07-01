# Skill Maintenance Handoff: Generated Icon QA

## Scope

Updated generic Chaos Redux skill guidance for generated focus, decision, idea, achievement, and other gameplay icon workflows. No gameplay, localisation, asset, spreadsheet, or Event 015 source docs were edited.

## Skills changed

- `.agents/skills/chaos-redux-event-assets/SKILL.md`
  - Added a generated icon package rule requiring visible `$imagegen` source evidence through saved source atlas or source PNGs.
  - Added manifest requirements for prompt and source mode.
  - Added contact-sheet QA requirements for final alignment, dimensions, transparency, and absence of white matte or opaque square backgrounds.
  - Added a completion guard against primitive local drawings, resized unrelated icons, or locally assembled shape substitutes being treated as generated final icons.
- `.agents/skills/chaos-redux-subagents/SKILL.md`
  - Added a `chaosx_icon_artist` parent-prompt rule requiring source atlas/source PNG evidence, prompt and source-mode notes, transparent-background processing, contact sheets, dimension and alignment QA, no white matte or opaque square backgrounds, and confirmation that generated icons are not primitive local drawings or resized unrelated icons.

## Skills left unchanged

- `.agents/skills/chaos-redux-frame-animation/SKILL.md`
  - Already requires real per-frame source artwork, contact sheets, frame QA, and rejects primitive or transform-only final animation. No static generated-icon gap was found there.

## Validation

- Inspected the relevant existing skills for current coverage before editing.
- Confirmed the new rules are generic and do not mention Event 015-specific assets or implementation history.
- Confirmed changes are limited to skill documentation plus this requested handoff.

## Remaining issues

No blocked work. If parent routing prompts for `chaosx_icon_artist` are stored outside the skill files, they may need the same generic evidence requirement added separately.
