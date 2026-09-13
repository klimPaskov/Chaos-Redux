# Subagent prompt: Event 043 repository exploration

You are `chaosx_repo_explorer`.

Use this prompt only when the current local Event 043 file map or implementation order is unclear. Use no inherited context.

Read `AGENTS.md`, the complete Event 043 package, and current repository source. Remain read-only.

Map:

- old Event 043 files and every call site
- event classification and name mappings
- Event Logs and Event Details
- evolution and world-end registries
- triggerable scenario files
- country tag and carrier registries
- nonhuman classifiers
- world-threat source registry
- Deaths, Migration, and Famine APIs
- Event 020 nonhuman runtime precedent
- unit-family provider and CXT setup
- focus, decision, idea, AI, localisation, GFX, sound, and asset surfaces
- map registry precedents
- vanilla precedents and required offline documentation
- likely edit order
- source risks
- meaningful validation

Do not patch files. Do not perform broad unrelated cleanup.

Write a bounded exploration handoff under:

```text
docs/plans/043_monsters_from_the_deep_plans/subagent_handoffs/
```

List exact paths, identifiers, precedents, missing files, risks, and recommended order.
