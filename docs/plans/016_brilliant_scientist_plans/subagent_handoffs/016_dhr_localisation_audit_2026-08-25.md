# Event 016 Alien Infantry and D’Rhonda Localisation Audit

> Historical localisation snapshot superseded for Alien Infantry runtime status by the accepted V13 provider package and static runtime promotion recorded in `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/v13_firearm_preset/final_manifest.md` and `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_infantry_meshy_runtime_promotion_2026-08-26.md`. Retain the localisation findings, but do not use its pre-promotion absent-entity statement as current status.

Date: 2026-08-25

## Scope and authority

Audited the current Event 016 Alien Infantry and Empire of D’Rhonda package against `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md` and `docs/plans/016_brilliant_scientist_plans/016_alien_dhrondan_acceptance_scenarios.md`.

The review covered the provider-neutral unit and equipment names, technology and tactic text, Events `chaosx.nr16.40` through `.51`, Event Details scripted localisation, DHR country and cosmetic identities, all 88 DHR focuses, DHR characters and portraits, contact and sovereignty decisions and missions, the envoy project, Event 019 provider-508 text, achievements, flags, sprites, and the current alien-infantry runtime asset surface.

## Files changed

- `localisation/english/016_alien_infantry_api_l_english.yml`
- `localisation/english/016_brilliant_scientist_country_l_english.yml`
- `localisation/english/016_dhrondan_contact_l_english.yml`
- `localisation/english/016_dhrondan_focus_l_english.yml`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhr_localisation_audit_2026-08-25.md`

## Changed keys

- `alien_infantry_desc`
- `alien_laser_weapon_equipment_desc`
- `brilliant_scientist_alien_predictive_warfare_tech_desc`
- `DHR_paid_landing_network_effect`
- `DHR_reopen_the_orbital_channel_desc`
- `alien_infantry_call_landing_effect_tt`
- `dhrondan_rebellion_pulse_mission_desc`

## Before and after

The shared Alien Infantry battalion, equipment, and predictive-warfare descriptions previously called the reusable family D’Rhondan. They now use provider-neutral extraterrestrial or alien wording, while the D’Rhondan cohort, contact, and country surfaces retain their route identity.

Two focus strings previously called the canonical `Alien Laser Weapons` “exotic laser weapons.” They now show the exact equipment name and preserve the live integer equipment-cost token.

The landing effect tooltip and rebellion mission description previously placed every condition and result in one dense paragraph. They now separate reservation, refund, success, cooldown, and probability tiers with localisation newlines. All costs, timers, probabilities, and dynamic tokens are unchanged.

## Audit lists

### Missing keys

None in the scoped source audit. All 88 DHR focus IDs have title and description keys. All 37 explicit title, description, name, and tooltip references in the two DHR event files resolve. All seven explicit custom decision tooltip references resolve.

### Duplicate keys

None among 412 scoped DHR, D’Rhondan, Alien Infantry, Alien Laser Weapon, alien-tactic, predictive-warfare, envoy-project, and Event 016 `.40` through `.52` keys.

### Scripted localisation issues

None found. `GetDhrondanEventDetailClause` still selects `dhrondan_event_detail_clause` after sovereignty forms and otherwise selects the intentional blank key. The caller remains in `chaosx.events_log.window.event_details.brilliant_scientist`.

The event-target token `[dhrondan_diplomatic_actor.GetNameDef]` remains correctly written without an `event_target:` prefix in localisation.

### Dynamic text opportunities

Existing integer formatters for Alien Presence, Pact Strain, landing equipment cost, landing cooldown tiers, Event 019 family costs, and achievement thresholds were preserved. No new scripted-localisation block was needed.

The fixed 2,000-weapon landing reserve remains explicit in the shared landing decision text because the binding public contract fixes that price. DHR focus text continues to use the live landing-cost variable.

### Cross-surface mismatch notes

Fixed the only current naming drift: shared unit, equipment, and tactic-technology prose no longer assigns the provider-neutral family exclusively to D’Rhonda, and DHR focus text now uses the canonical `Alien Laser Weapons` name.

Event 019 provider 508 still refers to the D’Rhondan landing network by design. Its player-facing text describes contact and paid arrivals rather than a Kruger-owned unit family.

No retired guard name, Kruger-specific Alien Infantry identifier, or D’Rhondan-specific unit identifier remains in the inspected gameplay, localisation, interface, sound, or maintained Event 016 and Event 019 documentation surfaces.

The exported Event 016 catalog detail repeats the current premise-only D’Rhondan Event Details clause. No catalog mismatch was found, so the workbook was not edited.

### File encoding concerns

None. The seven scoped localisation files checked after the patch retain UTF-8 BOM bytes. No audited key uses `:0`.

### Prose-quality repairs

- Vagueness: the shared family descriptions now state what the battalion, weapon, and technology are without implying a single route owner.
- Bloat: no broad prose reduction was necessary.
- Obvious explanation: no title-repeating or button-narrating line required removal.
- Repetition: the two densest mechanical passages were separated by outcome rather than repeating their subjects in one paragraph.
- Overcomplication: landing refund, success, cooldown, and rebellion probability tiers are now individually readable.
- Style-rule repair: no em dash, sentence semicolon, prompt fragment, implementation-history wording, or staged contrast remains in the patched values.

### Sourced quotation preservation

No sourced or attributed quotation appears on the audited Alien Infantry, DHR, contact, focus, decision, event, technology, tactic, project, Event Details, or Event 019 provider-508 surfaces. No quotation was changed.

## Asset and identifier audit

The four linked GFX definition files contain 237 texture references and every referenced texture exists. The current package has four DHR flag identities in all three required sizes, for 12 flag files total. All 12 DHR character portrait textures exist.

The event report/news art, DHR decision/category art, envoy project icon, 88 focus icons, DHR idea icons, Alien Infantry counters, Alien Laser Weapon icon, and both alien tactic icons are present under their registered sprite families.

The four alien-infantry sound files exist and `alien_infantry_laser_fire`, `alien_infantry_move`, `alien_infantry_idle`, and `alien_infantry_death` are registered in the shared sound category.

Current runtime blocker: there is still no `alien_infantry_entity` definition, no `gfx/entities/alien_infantry.asset` model binding, and no `gfx/models/units/alien_infantry/` mesh/action package in the repository snapshot inspected by this audit. Only the alien laser particle and light definitions are present under `gfx/entities/`. This is a model/runtime wiring blocker for the owning parent or 3D worker, not a localisation defect, and no fallback was added.

## MCP evidence

### Event chain

`hoi4.event_inspect` lint for `chaosx.nr16.40` completed with `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, and zero skipped sources.

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ddf06f502901b2defce3c171d2d1601a96d9daacfc88c14e212b6b44c8ed42ae/8a87acd5dfcd03f572c576fe177bd7a3a149972d35085d77c0a14bb0ca7fc49f/event-lint-7d541a2019d5.json`
- Revision: `7d541a2019d5a129c40fd9666b825bf87b88628b0a3ff4f2ba44df4ea382d8e1`

The event inspector is structural and does not measure popup text-box overflow. Popup overflow remains a user-owned live-consumer check.

### Focus tree

`hoi4.focus_inspect` resolved all 88 DHR focus titles and reported no DHR tree diagnostic. Its only localisation warning concerns the vanilla `continuous_restrict_freedom_desc` key, outside this scope.

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59f99990f9d8ead0b0f5b094574e2319135bb0fa341e385f59ea133fff9cd751/fca4e2f24b157e1b32d4972454654a72198f57ff006bb2268a5647f1ca2f0720/focus-inspect.5cf1d337bc3cac06.json`
- Revision: `5cf1d337bc3cac0648e622ecadc34c6a6d49973c355be996d199db4be1fe74d6`

### Technology

`hoi4.tech_inspect` traced `brilliant_scientist_alien_predictive_warfare_tech` and returned `TECH_INSPECTED_PARTIAL` without a selected-technology blocker.

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/17a184bf5d347578aa494d48efd59a525015117dc6053426179e8c3367cfc321/bb718b7ffa24e86e50d5263a378fbd0e425741707bbffab6e8aa13dca3a2583e/technology-trace-b2b1e58d15b2.json`
- Revision: `b2b1e58d15b202cb0a2dd7bcfc38f88072c0384c80adefbf4fefc1a30c19bed0`

The result is partial because the workspace-wide analysis reports four unresolved technology references outside the narrow inline result. It is not complete runtime proof.

### Decisions and overflow

The installed HOI4 MCP exposes no standard decision or decision-category inspection/render route. The audited decisions do not own a scripted GUI, so the GUI inspector is not an applicable substitute. Standard decision/category overflow therefore remains unresolved and source review is not treated as rendered evidence.

## Meaningful validation

- Re-ran scoped key coverage and duplicate checks after the patch: 88 focus IDs, 412 scoped keys, zero missing focus pairs, and zero scoped duplicates.
- Checked explicit event and decision tooltip consumers: 37 event references and seven custom decision tooltip references resolve.
- Checked 237 DHR/Alien Infantry sprite texture references across the linked GFX files: zero missing texture paths.
- Confirmed 12 flag files and 12 character portrait textures.
- Confirmed the scoped localisation files retain UTF-8 BOM encoding and the patched values preserve all dynamic tokens and formatting codes.
- Confirmed the maintained source tree contains none of the retired guard names or Kruger-specific Alien Infantry identifiers listed above.

## Skipped meaningful validation

- No in-game or live-consumer validation was run because it belongs to the user.
- Event popup, hover tooltip, and standard decision/category text overflow could not be measured by an applicable installed MCP route.
- No technology compare was run because technology source did not change. The technology inspection is structural evidence only.
- No model reimport or entity render was possible because the runtime entity, mesh, and action package is absent from the inspected tree.

## Unresolved wording decisions

None.

## Parent follow-up

The owning parent or 3D worker must add and validate the accepted `alien_infantry_entity`, packed model, and seven genuine action files before asset/runtime acceptance. The localisation and sprite-key work must not be presented as whole-package completion while that blocker remains.

## Simplifications and omissions

No localisation fallback, asset alias, hidden route, or gameplay simplification was introduced. The missing runtime model/entity package and unrenderable standard decision/popup overflow are reported explicitly.
