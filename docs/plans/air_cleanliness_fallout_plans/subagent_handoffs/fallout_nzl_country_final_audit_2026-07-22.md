# Fallout NZL Lifeboat State country package audit

Date: 2026-07-22
Scope: dormant Fallout NZL Lifeboat State package
Owner: country package subagent
Status: audited with narrow setup patches and activation remains intentionally dormant

## Changed files

- `common\countries\fallout_nzl_lifeboat_cosmetics.txt`
  - Added the three cosmetic identities used by the runtime route effects.
  - Added `NZL_FALLOUT_LIFEBOAT_STATE`, `NZL_FALLOUT_PACIFIC_RELIEF_REPUBLIC`,
    and `NZL_FALLOUT_SOUTHERN_REFUGE` color and UI color blocks.
- `common\scripted_effects\fallout_nzl_lifeboat_effects.txt`
  - Added explicit province priorities to the three bounded starting
    formations: Wellington `1814`, Auckland `4543`, and Canterbury `2197`.
  - Added Auckland `4543` as the priority for the one-shot Southern Escort
    Volunteers formation.
- `common\scripted_effects\fallout_nzl_lifeboat_effects.md`
  - Documented the bounded formation placement contract.
- `docs\plans\air_cleanliness_fallout_plans\FALLOUT_NZL_LIFEBOAT_ENGINE_PROOF.md`
  - Reconciled the starting-force note with the explicit province priorities.
- This handoff.

No activation caller, fallback path, new country tag, new focus route, or new
asset was added.

## Country package coverage checklist

- Carrier tag: `NZL` remains the only gameplay tag. The package is additive and
  does not replace vanilla NZL history or OOB setup.
- Cosmetic identities: all three runtime `set_cosmetic_tag` identifiers now
  have definitions in `common\countries\fallout_nzl_lifeboat_cosmetics.txt`.
- Exact core states: `284` Wellington, `1079` Auckland, `723` Canterbury,
  `1080` Marlborough, and `1081` Otago are validated by the package trigger.
- Capital choices: `284` is the first choice and `1079` is the reviewed
  secondary choice after the assignment ledger commits it.
- Samoa state `726` is intentionally excluded from package ownership until the
  separate Samoa disposition is resolved.
- Leaders and advisors: six fictional characters are generated idempotently at
  activation. The parliament uses an institutional name. The other five use
  the regional names in localization and the generated role metadata.
- Parties and politics: activation promotes the generated parliament leader,
  applies the route politics, and writes all four route party names.
- Ideas: fourteen ideas are defined with `allowed = { always = no }`, runtime
  lifecycle removal, route identity spirits, and icon references.
- Localisation: `localisation\english\fallout_nzl_lifeboat_l_english.yml` is
  UTF-8 with BOM and covers country identities, parties, characters, traits,
  ideas, decisions, focuses, event text, achievement text, and tooltips.
- Focuses: 42 authored focus IDs are present. Every focus has an icon,
  localisation, package-current availability, cancellation guard, and AI block.
- AI: both route plans contain the 42 focus IDs in ordered lists, with current
  package and route gates. Advisor idea tokens match generated character IDs.
- Decisions: 18 category actions are present and the current focus-open flags
  have consumers in `common\decisions\fallout_nzl_lifeboat_decisions.txt`.
- On actions: war, capitulation, peace conference, annexation, and state
  control hooks use narrow exact-target checks. No recurring world iteration is
  used by the NZL package.
- Starting forces: three two-battalion `Lifeboat Home Guard` formations are
  bounded by states and now prioritize the exact requested provinces. The
  escort decision remains one-shot and prioritizes Auckland.

## File surface checklist

Inspected package surfaces:

- `common\national_focus\fallout_nzl_lifeboat_focus.txt`
- `common\ideas\fallout_nzl_lifeboat_ideas.txt`
- `common\characters\fallout_nzl_lifeboat_characters.txt`
- `common\country_leader\fallout_nzl_lifeboat_traits.txt`
- `common\ai_strategy_plans\fallout_nzl_lifeboat_ai.txt`
- `common\on_actions\fallout_nzl_lifeboat_on_actions.txt`
- `common\scripted_triggers\fallout_nzl_lifeboat_triggers.txt`
- `common\scripted_effects\fallout_nzl_lifeboat_effects.txt`
- `common\script_constants\fallout_nzl_lifeboat_constants.txt`
- `common\decisions\fallout_nzl_lifeboat_decisions.txt`
- `common\decisions\categories\fallout_nzl_lifeboat_categories.txt`
- `interface\fallout_world_end.gfx`
- `localisation\english\fallout_nzl_lifeboat_l_english.yml`

The static characters file is intentionally empty. Runtime generation owns the
six character tokens and prevents duplicate definitions.

## Map and state setup

Vanilla references confirm the requested state and province mapping:

- state `284` contains victory point province `1814` Wellington and naval base
  history.
- state `1079` contains victory point province `4543` Auckland and the
  principal naval base.
- state `723` contains victory point province `2197` Christchurch and a naval
  base.
- states `1080` and `1081` are the reviewed supporting South Island states.
- state `726` is Samoa, has an `SAM` core, and remains outside the package
  until the conflict ledger resolves its disposition.

The starting force effect now uses `prioritize_location` for the three exact
requested provinces while retaining the exact state scopes and
`allow_spawning_on_enemy_provs = no`. This is safer than choosing an arbitrary
province from a state.

## Politics, leaders, portraits, flags, advisors, and parties

The generated leader roster and party names are present and localized. The
three leader DDS files are present. Dairy Relief Commissioner and Storm Port
Engineer advisor DDS files are present and registered in
`interface\fallout_world_end.gfx`.

Radio Service Coordinator remains blocked. The effect references
`GFX_portrait_NZL_fallout_radio_service_coordinator_small`, but there is no
matching sprite declaration in `interface\fallout_world_end.gfx` and no runtime
DDS under `gfx\`. The asset manifest and blocker review both record that the
processor rejected all candidates. No fallback portrait was introduced.

All three route flag ladders are present under `gfx\flags\` and are paired with
the cosmetic identity definitions added in this audit.

## Focus, decision, idea, and asset findings

Focus and decision wiring is complete for the authored package surfaces. A
previous focus audit reported missing search filters and orphan decision-open
flags. The current focus file has search filters on all 42 focuses, and the
current decision file consumes the previously reported flags. Those older
findings are stale and are not repeated here as active defects.

The focus `fallout_nzl_license_every_sea_road` currently opens the last-berth
decision and changes sea-lane security and harbor capacity. Its specification
also describes numbered permits, patrol windows, piracy reduction, and a
convoy operating tradeoff. Implementing those extra mechanics would require a
broader focus and decision design pass, so this audit leaves the mismatch
queued in the existing focus handoff rather than inventing a partial mechanic.

The idea lifecycle converges to the specified maximum of three persistent
focus-created spirits. No idea rewrite was necessary.

## Starting military, technology, industry, supply, and production

The package preserves vanilla NZL history and starting technology. Activation
removes obsolete NZL ideas and decisions, restores the package starting ideas,
and creates the bounded home-guard family after the exact package gate. The
escort decision has a one-shot receipt and cannot create repeated formations.

No broad industry, technology, equipment, naval, or supply rebalance was
attempted. Such changes are outside a narrow country package audit.

## AI and playability

The humanitarian and isolation plans are current-package and route gated. Their
focus lists cover all 42 focus IDs and their advisor idea tokens match the
generated advisor IDs. The package itself remains safe while dormant because
the activation effect has no caller.

The vanilla NZL alternate AI plans still contain empty abort blocks. They cannot
be safely repaired with a fallback plan inside this scope. The allocator caller
and transition scheduler also remain outside this package audit.

## Remaining blockers and uncertainty

1. The Fallout allocator must provide the generation, assignment, Samoa, and
   overlap receipts before activation can run.
2. No activation caller exists by design. Do not add one in this package.
3. The Samoa `726` disposition is unresolved.
4. Aotearoa and GRX overlap receipts for states `284` and `723` are unresolved.
5. Vanilla NZL alternate-plan empty abort blocks remain a shared scheduler
   compatibility blocker.
6. Radio Service Coordinator portrait production and `.gfx` registration are
   blocked by asset review. A real approved DDS and sprite declaration are
   required before the advisor can be safely surfaced.
7. The sea-road license focus has the broader specification mismatch documented
   above. It needs a design-supported implementation pass.

## Validation performed

- Counted 42 authored focus IDs and matched them against the two route AI focus
  lists.
- Compared focus, idea, decision, character, and route identity identifiers to
  the NZL localization file. No missing package keys were found.
- Confirmed localization begins with a UTF-8 BOM.
- Confirmed the three requested starting provinces exist in the vanilla state
  histories and the province priorities match the spec.
- Confirmed all three leader portraits and both approved advisor portraits
  exist. Confirmed the radio advisor DDS and sprite are absent, matching the
  asset blocker documents.
- Consulted the offline focus, country creation, effects, triggers, scopes,
  ideas, decisions, AI, and localisation references plus vanilla effects and
  NZL history documentation.

Skipped full game launch, map rewrite, and technology-tree viewer validation.
The installed package exposes no Technology Tree Viewer, activation is blocked
upstream, and this audit made no map rewrite.
