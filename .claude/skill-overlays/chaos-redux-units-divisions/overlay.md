---
description: Use when creating, changing, or auditing Chaos Redux sub-units, support companies, division templates, package formations, orders of battle, division names, unit-spawning or unit-removal effects, manpower handling, unit counters and texticons, or sub-unit stats and modifiers. Covers the definition files, the loading rules, the runtime effects and triggers, the Event 19 and test-country obligations, and the silent failures.
---

### In Contents

- Chaos Redux specifics

### In Chaos Redux specifics

The `CLAUDE.md` coding, constants, dynamic-effect, and localisation rules apply and are not repeated here. Loops over divisions use `every_country_division` inside a bounded country scope; world-wide hooks need permission. (Chaos Redux wording differs from the kit)

**Where Chaos Redux units live**

- `common/units/` has one file per family or owning event: CBRN support (`cbrn_hq_support.txt`, `cbrn_regimental_support.txt`, `livens_projector_support.txt`), `chaos_battalion.txt`, `zombies.txt`, `clone_infantry.txt`, `coal_golems.txt`, and numbered event files (`010_*`, `012_*`, `014_*`, `016_*`, `018_*`, `020_*`, `039_*`). `common/units/unit_modifiers/chaosx_unit_modifiers.txt` holds shared stat modifiers and `common/units/names_divisions/` the division name groups.
- Division templates for AI use are in `common/ai_templates/` per family (`cbrn_hq_support.txt`, `cbrn_regimental_support.txt`, event files); see `chaos-redux-ai-strategies`.
- Counters and texticons: event counter sprites in `interface/*_counters.gfx`, texticons in `interface/*texticons*.gfx` with art in `gfx/texticons/`. A CBRN texticon is a native-alpha `60x12` strip of two `30x12` frames (`noOfFrames = 2`), copied from the vanilla support texticon family (`docs/systems/cbrn_warfare/cbrn_unit_texticon_assets.md`). Entities are `gfx/entities/<owner>.asset` plus `.gfx`; the runtime contract is `docs/systems/3d_model_pipeline/chaosx_3d_runtime_contract.md`.

**Rules that recur**

1. A new Chaos Redux land sub-unit carries three obligations in the same change. (a) Test-country registration through the dynamic extension contract and family roster rules below; `docs/testing/chaosx_test_country.md` owns the current helper API. (b) An Event 19 disposition: a combat unit extends an existing unit-family provider or gets a full provider registration; a support unit is documented as an inseparable provider attachment, a parent-owned support consumer, or a rejected standalone lot with the engine reason. Update `docs/events/019_infantry_spawn/systems/unit_family_coverage.md` and `docs/systems/cbrn_warfare/chaos_unit_family_registry.md`. (c) Counter, texticon, and entity wiring.
2. CBRN formations use `chaos_battalion` as the combat anchor; armored delivery formations use `autonomous_robot` as the armor-group anchor. The shared `same_support_type` exclusion `cbrn_offensive_delivery` stops the armored delivery roles and the Livens variants sharing one roster, so each needs its own formation.
3. A custom 3D model, animation, sound, or counter follows `chaos-redux-3d-model-pipeline`. The worker hands off the bespoke vanilla-green counter requirement; final counter art is `chaosx_icon_artist` under `chaos-redux-event-assets`; the parent wires the runtime. Never ship a unit with a stand-in counter or a static pose passed off as an animation. (Chaos Redux wording differs from the kit)
4. A unit family is not available merely because its definition exists: package readiness flags (for example the Africa strange-force manifest) gate runtime use until every family model, entity, counter, and audio item is promoted together.
5. Read manpower through `manpower_k`. Population loss that must not create recruitable manpower uses the exact state-loss helpers in `common/scripted_effects/chaosx_dynamic_effects.md` (`chaos-redux-map-states`).
6. Equipment the unit consumes follows `chaos-redux-equipment`, including the `script_enum_equipment_bonus_type` entry. (Chaos Redux wording differs from the kit)

**CXT family roster contract**

Read [the test-country dynamic extension contract](../../../docs/testing/chaosx_test_country.md#dynamic-extension-contract) before adding a family; use its current metadata fields and helper signatures rather than copying an older call pattern.

- Every custom combat type needs an individually fielded showcase whose dominant battalion exposes that type's model and counter. A mixed family formation may also be useful, but its dominant type hides the other models and counters and does not prove individual showcase coverage.
- Support showcases need an explicit compatible, registered combat anchor. Place divisional support in `support`, regimental support in `regimental_support` against an allowed battalion-group column, and HQ-only support in an `is_army_hq` template with a valid HQ anchor. Check `regimental`, `divisional`, `allowed_battalion_groups`, HQ permissions, slot bounds, and `same_support_type`; never create a support-only division or force every support token into the ordinary support grid.
- Future unit packages self-register through one package-owned idempotent `_apply` effect and its modifier-free hidden-idea carrier. Publish stable family metadata for combat and support tokens, explicit compatible anchors, and any owner-authored formations through the current API. Startup registration uses one bounded existing-country scope; an additive CXT-only daily fallback may register and mark pending work, but may not grant or deploy content.
- Custom scripted helpers take caller-owned variable or token inputs and are invoked with `= yes`; named argument blocks and `$PARAMETER$` expansion are not a HOI4 custom-helper API. Native effects retain their documented argument blocks. For literal string fields, use matching replacements declared on a `meta_effect` text block, supplied by native variable or scripted-localisation getters. Family selectors need real tokenizable database definitions, such as modifier-free idea markers; dynamic unit or formation names resolve published payload variables through `GetTokenKey`, not unbound `[UNIT]` localisation placeholders. Follow the current test-country API and [shared helper guidance](../chaos-redux-events/references/scripted-systems-and-country-integration.md#duration-fields-and-constants) for the exact input and replacement contract.
- Template existence and successful initial deployment are separate receipts. An existing template must not suppress a missing initial spawn, and a processed token or attempted creation must not masquerade as a successful spawn receipt. Record deployment success only after the documented deployment contract confirms it; keep a failed or unavailable placement eligible for bounded retry.
- Select and retain one owned, controlled province per family, then reuse it for all that family's individual showcases, support consumers, and package-owned formations. Revalidate the mapping before deployment and replace it only when invalid; per-division random state selection cannot enforce family co-location.
- Initial setup and pending-package application are idempotent for templates and successful initial deployments. Repeating the console entry or registration must not add another army. The player-triggered deployment decision intentionally reinforces the roster using existing templates and the same family province mapping; periodic hooks never replenish divisions.
