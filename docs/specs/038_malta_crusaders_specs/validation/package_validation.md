# Package validation

## Validation result

The Event 38 specification package passed the structural checks available in this planning environment.

## Coverage

- Numbered specification files: `31`
- Expected numbered specification range: `00` through `30`
- Missing numbered specifications: `none`
- Prompt files: `22`
- Expected prompt range: `00` through `21`
- Missing prompts: `none`
- Template files: `7`
- Source manifest rows: `43`
- Total package files before ZIP creation: `67`
- Markdown files: `64`
- Markdown word count: `73471`
- Markdown line count: `10851`

## Encoding and content integrity

- Empty files: `none`
- UTF-8 decoding errors: `none`
- Unicode em dash occurrences: `0`
- Semicolon occurrences: `0`
- Unicode replacement-character occurrences: `0`
- Broken relative Markdown links: `none`
- Goal prompt character count: `3996`
- Required goal prompt range: `3500` to `4000`

## Intentional substitution fields

`prompts/15_3d_model_pipeline_prompt.md` is a reusable per-model dispatch template. Its bracketed fields are hard-gate inputs that the parent must replace before dispatch. They are not gameplay placeholders or approved asset fallbacks.

Detected fields: `[ACTION_ROLES], [ASSET_ID], [ASSET_SLUG], [CONSUMER], [COUNTER_BRIEF], [FIRES_IN_COMBAT_OR_NON_FIRING], [FORBIDDEN], [GEOMETRY], [LOCK], [MODE_AND_REASON], [PAID_PLAN], [PATH_AND_CHECKSUM], [PERIOD_RULES], [PROFILE], [SOUND_BRIEF], [SOURCE_MODE_AND_PROVENANCE], [VANILLA_CROSSWALK]`

## Scope validation

The package contains specifications, research notes, implementation prompts, templates, and validation contracts. It contains no claimed gameplay implementation, generated asset, portrait, audio cue, 3D model, workbook edit, CSV export edit, or MCP result.

No named project subagent was executed in this runtime. The package records that limitation and supplies context-complete prompts for later use in the configured repository environment.

## Direct extraction contract

The distributable ZIP is built from the package root so extraction places files directly under:

```text
docs/specs/038_malta_crusaders_specs/
```

The ZIP must not add another wrapper folder above `docs/`.

## Remaining evidence gates

Implementation blockers and required live evidence are listed in `unresolved_implementation_gates.md`. They are not treated as planning omissions.
