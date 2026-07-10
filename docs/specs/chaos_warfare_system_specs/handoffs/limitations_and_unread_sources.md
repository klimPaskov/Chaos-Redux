# Limitations and Unread Sources

## Fully read

All files supplied directly with the task were read in full. This includes every provided skill, every provided subagent definition, the mechanics guide, AGENTS.md, all catalog CSV files, and every markdown file inside the biological-warfare archive.

## Not fully readable in this environment

The following source sets were not available as complete mounted directories:

- the full live Chaos Redux repository
- the user's offline `paradox_wiki/` snapshot
- the user's local Hearts of Iron IV installation and its `documentation/` folder
- approved comparison mods in the user's Steam Workshop installation

Targeted live repository files were inspected through GitHub. Current vanilla behavior was researched through official announcements and patch notes. These steps are enough for a detailed design package, but not enough to guarantee engine-facing syntax or the final installed 1.19 balance values.

## Subagent limitation

The supplied custom subagent definitions were fully read. No tool was available to spawn those custom subagents. The package applies their standards manually and includes a manual improvement-loop review and completion audit. It does not claim that the named agents executed.

## Simplification statement

The design itself was not intentionally truncated to produce a quick answer. It is a full system specification with matrices and prompts. A few engine-specific choices remain conditional because only the implementation environment can verify them. Those conditions are marked as validation gates rather than replaced with fallbacks.

## Required closure before implementation completion

The implementation agent must read the relevant offline wiki pages and vanilla documentation, inspect the installed 1.19 files, identify exact Army HQ and regimental-support schema, verify chemical-air mission hooks, and record any unsupported design surface. Unsupported mechanics must be discussed rather than silently approximated.
