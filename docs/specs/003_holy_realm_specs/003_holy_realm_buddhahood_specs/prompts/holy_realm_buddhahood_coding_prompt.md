# Coding Prompt: Holy Realm Buddhahood

Implement `holy_realm_buddhahood` from the spec package under `docs/specs/003_holy_realm_buddhahood_specs/`.

Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-super-events`, `hoi4-decisions-missions`, `hoi4-focus-trees`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, and related Chaos Redux skills.

Implement all mapped surfaces:

- Event chain, target selection, event registration, debug names, event log, event details, evolutions, and world-end branch.
- Holy Realm country transformation or event-created package, including origin flags, names, cosmetic tags, leader stages, portraits, flags, starting ideas, starting forces, and AI.
- Bodhi Progress, Dhyana Depth, Compassion, Detachment, Defilements, Meditation Charge, World Suffering, and Sangha Cohesion.
- Teaching missions, sanctuary decisions, Sangha Compact decisions, meditation ritual or accepted fallback, Buddha powers, Final Silence decisions, cleanup, and AI equivalents.
- Scripted GUI mandala panel with animated sprites where supported and static fallbacks everywhere.
- Focus tree or overlay branch preserving the route design, with non-linear structure, route locks, branch payoffs, varied rewards, focus filters, AI weights, localisation, icons, and route coverage reporting.
- Super-events for The Awakened One, Powers of the Awakened, and The Final Silence with researched quote, image, audio, slot, settings-aware playback, docs, and spreadsheet alignment.
- Assets through the asset workflow, including DDS conversion, manifests, and GFX handoffs.
- Achievements from the achievement spec.
- Event docs and event catalog spreadsheet alignment.

Do not simplify the three core rules:

1. Final Silence can only start after Buddhahood.
2. Buddha powers require meditation and are strongest against valid chaos countries.
3. The portrait, mandala, country identity, and super-event presentation must change when the Bodhisattva becomes the Buddha.

If literal mouse holding for three real minutes is unsupported by HOI4 GUI, implement the accepted concentration sequence fallback and document the engine limitation. Do not replace it with a plain instant button.

Do not claim completion until the implementation satisfies the route coverage matrix and reports every simplification, fallback, blocker, validation, and asset status.
