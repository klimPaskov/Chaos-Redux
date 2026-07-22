# Portrait identity-ownership gate skill update — 2026-07-22

## Scope

Updated only `.agents/skills/chaos-redux-event-assets/SKILL.md` and this dated
handoff. No gameplay, character, portrait, GFX, interface, localisation, asset,
specification, spreadsheet, or agent-prompt files were edited. No commit was
created.

## Reusable rule added

The portrait workflow now fails closed before sourcing or wiring a real-person
leader, commander, operative, or named officeholder token unless an exact/variant
identity search covers installed vanilla and the current project: character
definitions, country histories and recruitment, portrait files, `.gfx`/interface
consumers, leader/commander/operative/officeholder consumers, and relevant
localisation. A person already defined, recruited, or meaningfully portrait-owned
by a live roster cannot be cloned into another country.

Reuse is permitted only through an explicit guarded existing-character
transfer/availability contract that removes origin ownership before target
ownership and prevents simultaneous ownership. Ship names, production-line names,
streets, equipment, and incidental prose do not establish ownership without an
actual character or portrait/leader/commander/operative/officeholder consumer.
Manifests and handoffs must retain search terms, checked roots/files and ids,
match/no-match evidence, disposition, and any transfer guard. The existing
grounded-source-only (`grounded_source_only`) versus `fictional_high_chaos` gate is
unchanged; this update does not authorize generated grounded people or advisor/high-
command dossier icons.

## Evidence that motivated the gate

- `docs/assets/006_independence_wave/sourced_portrait_treatments_2026_07_22/manifest.md:13-24`
  records no Event 006 advisor/dossier requirement and three visually valid
  treatments rejected as active vanilla characters: Konrad Adenauer, Franz Ritter
  von Epp, and Edmund Ironside.
- The same ledger's rows at `:36`, `:39`, and `:53` tie each rejected subject to
  an installed vanilla character definition and game-start recruitment, proving
  that a good source portrait still cannot be cloned into another live roster.
- `docs/assets/006_independence_wave/sourced_portrait_treatments_2026_07_22/visual_review.md:77-86`
  records the exact vanilla-character rejection and confirms that Luigi Rizzo's
  name appears only in two Italy ship-production lines, with no character,
  portrait, or leader consumer; incidental prose is therefore not ownership.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_sco_agx_postportrait_admission_audit_2026_07_22.md:90,134,150`
  records the required cross-surface search: Edmund Ironside resolves to an active
  ENG character/history/localisation consumer, while Cunninghame Graham, Douwe
  Kalma, and Pieter Reenalda have no exact vanilla character/history/localisation
  hit; localisation-only renaming or portrait reuse is explicitly rejected.

## Validation and handoff

- Reviewed the offline Paradox Wiki core pages and the installed vanilla
  documentation required by `AGENTS.md`; no Clausewitz syntax was changed.
- Reviewed the surrounding source-mode, real-person, advisor, manifest, and final
  checklist sections to avoid duplicating or weakening existing gates.
- Parent agent should review the skill diff and carry this ownership evidence into
  future portrait manifests/handoffs. No unresolved implementation blocker remains
  for this skill-only change.
