# Event 016 retired advisor workflow skill cleanup handoff

Date: 2026-07-29

Scope: skill-local cleanup only, plus this handoff. No gameplay, runtime asset, `.tools`, or other documentation file was edited.

## Completed changes

- Removed `the retired portrait-processing utility`.
- Removed `.agents/skills/chaos-redux-event-assets/tools/tests/test_the retired portrait-processing utility`.
- Removed the entire the retired advisor dossier asset kit kit, including manifests, generated frame/paper sources, overlays, prompts, and test variants.
- Removed the advisor processor bytecode cache entry; the unrelated `extract_portrait_source_crop` cache entry remains untouched.
- Updated `.agents/skills/chaos-redux-event-assets/SKILL.md` to remove the retired full-size and dossier processor commands, frozen processor/render hashes, schema and manifest contracts, reusable overlay requirements, and style-band gates.
- Updated `.agents/skills/chaos-redux-event-assets/tools/README.md` to document deterministic/manual full-size portrait processing and native advisor/high-command handling without naming a replacement processor.
- Updated `.agents/skills/chaos-redux-event-assets/assets/README.md` to retain the separate authorized native `65x67` advisor/high-command family, vanilla-reference inspection, manual visual review, provenance, DDS conversion, and stable sprite wiring requirements without the retired kit.

## Preserved guidance

The skill still treats explicitly authorized advisor, theorist, military-high-command, officer-corps, and army-small portraits as a separate native `65x67` asset family. It retains grounded-identity source rules, vanilla precedent inspection, independent visual review at native and enlarged scale, provenance records, repository DDS conversion, stable `.gfx` sprite wiring, and the rule that `army.small` is `65x67` while `army.large` remains the full `156x210` commander portrait. No replacement advisor workflow was created or registered.

## Historical-only references outside scope

Older Event 014, Event 015, Event 006, and other plan/audit handoffs still mention the deleted processor, overlay kit, or frozen hashes as historical production evidence. Examples include `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/`, `docs/plans/014_cannibalism_plans/subagent_handoffs/`, and `docs/plans/006_independence_wave_plans/subagent_handoffs/`. Those files were intentionally not edited because this task owns only `.agents/skills/chaos-redux-event-assets/**` and this handoff; their references should be treated as historical records, not active workflow instructions.

## Validation

- `python -B C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-event-assets` returned `Skill is valid!`.
- Exact-path existence checks confirm the retired processor, its test, its advisor bytecode cache, and the overlay-kit directory are absent.
- `rg --files .agents/skills/chaos-redux-event-assets` finds no retired processor, advisor overlay-kit, or retired test path.
- Vanilla precedent review confirmed native `65x67` small advisor/high-command sprites in `interface/ideas.gfx` and `common/characters/TUR.txt`, plus separate full `army.large` and small portrait consumers in `common/characters/AFG.txt`.

No gameplay or runtime validation was attempted, and no fallback advisor tool was introduced.
