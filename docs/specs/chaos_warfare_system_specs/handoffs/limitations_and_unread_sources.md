# Limitations and Unread Sources

## Fully read

All files supplied directly with the task were read in full. This includes every provided skill, every provided subagent definition, the mechanics guide, AGENTS.md, all catalog CSV files, and every markdown file inside the biological-warfare archive.

## Package-time limitations

The package handoff was written before the implementation workspace was mounted and recorded these limitations:

- the full live Chaos Redux repository
- the user's offline `paradox_wiki/` snapshot
- the user's local Hearts of Iron IV installation and its `documentation/` folder
- approved comparison mods in the user's Steam Workshop installation

Those statements describe the design-package authoring environment, not the current implementation workspace. During implementation, `AGENTS.md`, the mounted offline wiki pages, installed vanilla documentation, relevant vanilla examples, current Chaos Redux surfaces, and the required repository skills were consulted before edits.

## Subagent limitation

The supplied custom subagent definitions were fully read. No tool was available to spawn those custom subagents. The package applies their standards manually and includes a manual improvement-loop review and completion audit. It does not claim that the named agents executed.

## Simplification statement

The design itself was not intentionally truncated to produce a quick answer. It is a full system specification with matrices and prompts. A few engine-specific choices remain conditional because only the implementation environment can verify them. Those conditions are marked as validation gates rather than replaced with fallbacks.

## Required closure before implementation completion

The implementation agent must identify exact Army HQ and regimental-support schema, verify chemical-air mission hooks, and record any unsupported design surface. The current audit found no verified selected-state weather/terrain hook for the timed Army-HQ battlefield family and no verified continuous-air mission-activity hook. Those surfaces remain explicitly fail-closed; unsupported mechanics are not silently approximated.
