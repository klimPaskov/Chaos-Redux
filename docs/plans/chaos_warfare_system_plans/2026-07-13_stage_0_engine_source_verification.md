# Chaos Warfare rework: Stage 0 engine and source verification

Date: 2026-07-13

Status: accepted implementation preflight. This stage changes no gameplay, interface, localisation, or assets.

## Authority and reading record

Implementation authority is resolved in this order:

1. `docs/specs/chaos_warfare_system_specs/specs/01_...` through `12_...`, read in numerical order.
2. Every mapping file under `docs/specs/chaos_warfare_system_specs/matrices/`.
3. Specialist prompts under `docs/specs/chaos_warfare_system_specs/prompts/`.
4. Existing Chaos Redux behavior, retained only where it does not contradict the sources above or a later explicit user instruction.

The package entry points, source-of-truth map, staged plan, implementation surface map, completion checklist, all research notes, all handoffs, and the package manifest were also read. Current chemical-warfare and biological-warfare documentation and the current doctrine, technology, equipment, subunit, ability, raid, operation, decision, event, AI, startup-history, consequence, achievement, and UI integration surfaces were inspected before this note was written.

The required offline wiki snapshot was used, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, Scripted GUI modding, Equipment, Unit modding, Technology, State modding, Intelligence agency, Graphical assets, Military industrial organization, and the relevant country-history pages. No online Paradox wiki page was used.

## Installed engine baseline

- Installed game: Hearts of Iron IV 1.19.2.0/develop (Operation Postern generation).
- Revision evidence: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/hoi4_branch.txt`, `clausewitz_branch.txt`, and `clausewitz_rev.txt` (`a729d47bd1c55457e6886b6eeb2fcdef4ac05057`).
- Official documentation inspected: script concepts and Script Constants, effects, triggers, modifiers, decisions, on actions, scripted GUIs, units, equipment, equipment groups, doctrines, raids, operations, operation phases and tokens, AI templates/equipment/strategy, military industrial organizations, and special projects.
- Vanilla is the syntax and structure precedent. Existing Chaos Redux conventions take precedence where they are compatible with the accepted design.

## Verified current-version surfaces

### Army Headquarters

Supported. Current vanilla HQ companies use `allow_in_army_hq = yes`, `allow_in_non_army_hq = no`, deployed-leader modifiers, explicit `essential` equipment, `need`, and HQ abilities. Current vanilla HQ abilities support `requires_deployed_hq = yes`, command-power cost, duration, cooldown, unit modifiers, and AI evaluation. These are sufficient for the six mapped CBRN headquarters companies and their theater abilities.

The Army Headquarters is therefore the theater layer. No division-level substitute will be used for theater command.

### Regimental support

Supported. Current vanilla subunits support `regimental = yes`, regimental-support categories, essential-equipment shortage scaling, and the current division-designer regimental row. The mapped regimental CBRN units will occupy that row and will not be implemented as ordinary support companies.

The Hazard Pioneer mapping follows the numbered specs: it is a regimental division-layer unit. Theater decontamination remains an HQ company/ability responsibility.

### Equipment and shortage behavior

Supported. Producible archetypes and dated models can represent four gas-mask generations, decontamination equipment, CBRN instruments, and offensive payload lots. `essential` plus `need` provides engine-native shortage scaling for HQ and division subunits. Every new archetype/type will be added to `script_enum_equipment_bonus_type` in the same implementation tranche.

Gas-mask stockpiles will be additive startup grants in `common/scripted_effects/chaosx_startup_history_effects.txt`, backed by script constants and the accepted starting-stockpile matrix. A crate is the package abstraction (approximately 1,000 civilian sets or 100 military sets); the values are gameplay tuning, not precise historical inventories. Britain receives the largest prepared reserve.

### Medical response

Supported through scripted medical capacity backed by existing equipment. Vanilla field hospitals use support equipment and motorized equipment as essential needs, and the current mod has no clean separate medical-equipment archetype. The first implementation will therefore use:

- a centralized medical-capacity variable/ledger;
- support equipment and trucks for deployment and replenishment;
- field-hospital technology and CBRN treatment technologies as efficiency gates;
- explicit costs in decisions, HQ companies, regimental medical units, and response abilities.

No hidden local substitute and no new `cbrn_medical_equipment` archetype will be introduced unless later evidence demonstrates a clean engine/repository pattern.

### Raids and exact target state

Supported. Current raid instances preserve the selected target state through `var:target_state`, and outcome effects can execute in that exact state. Chemical air raids and biological raids can therefore consume real payload and apply their consequences to the selected state without selecting a random state.

All chemical delivery routes will call one shared exposure pipeline. Route-specific code may prepare inputs, but it may not independently calculate payload consumption, protection, disruption, deaths, contamination, medical saturation, evidence, attribution, or Condemnation.

### Continuous ordinary air missions

Unsupported for contamination in the installed version. The current official trigger/effect/on-action documentation and vanilla scripts expose plane counts, stationed regions, air-region ledgers, module/mission eligibility, and carrier-specific mission checks, but no verified hook that proves an ordinary chemical-capable air wing is currently flying an eligible mission over a target region.

Consequences:

- selected-state chemical raids are supported and will contaminate their selected state;
- the legacy ground-operations-heat/stationed-aircraft estimator will be removed;
- idle chemical-capable aircraft will never contaminate a region;
- no replacement estimator or approximation is retained;
- continuous-air contamination remains disabled unless a later current-version hook is demonstrated.

This is an engine limit, not a scope reduction for the supported raid route.

### Operations

Supported. Intelligence operations preserve actor, target country, and selected state/region scopes and support staged outcomes. Biological planting and covert chemical actions can therefore use the same agent lifecycle, evidence, attribution, and consequence helpers as raids.

### Military industrial organizations and designers

Supported with one exact-filter limit. Current MIO documentation and vanilla templates support allowed equipment types/categories, trait trees, production bonuses, research bonuses, AI selection, and completed-trait queries. Custom CBRN payload archetypes can therefore receive exact designer bonuses. Current MIO equipment filters and equipment groups cannot require that an aircraft variant carry one named module, so a native airframe weight, agility, or range bonus would also benefit conventional variants assigned to that MIO. Module-specific airframe-stat directions remain unsupported; no broad conventional-aircraft substitute is permitted. No current Chaos Redux CBRN MIO exists, so the mapped country program/designers will be implemented as new, differentiated definitions rather than aliases to generic organizations.

### AI

Supported through AI strategies, technology AI, decision `ai_will_do`, raid/operation AI, ability AI, and country-profile scripted gates. The existing AI is fragmented around individual cylinder, Livens, and tank-shell variants and has no readiness, reserve, protection, route, outbreak-safety, or consequence policy. It will be migrated to route-aware profiles and shared reserve/usage gates.

No broad all-country daily, weekly, or monthly pulse is authorized. Outbreaks, response missions, contamination cleanup, and other continuing jobs must use targeted self-scheduling or already-authorized narrow hooks.

### Scripted GUI

Supported. Current official documentation and the repository's existing scripted-GUI windows demonstrate custom windows, clickable effects, visible/enabled triggers, dynamic lists, variable-backed text, and controlled refresh. A dedicated CBRN overview can therefore expose readiness, policy, reserves, coverage, active contamination/outbreaks, evidence/attribution, medical saturation, and Condemnation links.

Persistent gameplay scope will remain in variables/arrays or explicitly managed targets; short-lived scripted-GUI interaction scope will not be treated as a durable event-target store.

## Locked implementation decisions

1. Continuous chemical-air contamination is raid-only because no eligible-activity hook is verified. The estimator is removed.
2. Army Headquarters is the theater layer; mapped regimental support is the division layer. Hazard Pioneers remain regimental.
3. Medical response uses scripted capacity plus support equipment/trucks and vanilla medical technology, not a new equipment archetype.
4. Tabun is a complete payload-capable agent where the numbered specs and delivery matrix map it. The legacy precursor-only description and missing delivery support will be migrated.
5. The dedicated CBRN scripted GUI is implementable and remains in scope.
6. Current-version MIO schemas support the six designer families and exact custom payload archetypes. They do not support a module-presence filter for aircraft-stat bonuses; that narrow designer direction remains an explicit engine limit rather than a broad-airframe fallback.
7. Doctrine may reduce Condemnation impact. This is an explicit user instruction dated 2026-07-13. Evidence generation, attribution state, and confirmed-use records remain intact; doctrine mitigation does not erase the underlying use.

## Reconciliation and conflict ledger

### Genocide infrastructure

The compact goal says doctrine must unlock genocide infrastructure, while numbered spec 08 states that chemical doctrine must not unlock camps or genocide infrastructure and keeps targeted nerve-agent suppression separate from genocide. Under the package authority order, numbered spec 08 governs. Existing doctrine-gated `concentration_occupation_law_unlocked` behavior is a legacy conflict and will be removed or migrated without deleting the independent genocide/camp systems.

### Condemnation mitigation

Numbered-spec language was initially read as disallowing doctrine-based reductions to confirmed-use consequences. The user explicitly corrected this on 2026-07-13: doctrine should reduce Condemnation impact. That instruction governs implementation. It does not authorize evidence removal, false non-use records, or consequence immunity.

### Legacy delivery fragmentation

Current abilities, Livens companies, chemical tank companies, chemical raids, and biological paths calculate overlapping consequences independently. Several paths infer rather than consume payload, use strongest-researched-agent fallbacks, or register deaths at contamination application. These conflict with the shared pipeline and distinct-agent lifecycle and will be migrated.

### Biological lifecycle

Current biological raids and events often apply contamination immediately, spread directly to neighboring states, and register deaths at application time. The accepted design requires agent-specific incubation, detection, spread, containment, countermeasures, treatment, stockpile safety, accidents, evidence, and attribution. Weaponized zombies remain separate except for explicitly shared helpers.

### Assets and player text

Current files contain placeholder special-project pictures, under-development player text, and reused/cross-type substitutes. These are not acceptable final assets. Required visual identifiers will be registered before production, then delivered through the event-asset workflow with source, processed output, final DDS, manifest, and wiring evidence.

## Worktree boundary

The repository was already dirty when this work began. In particular, unrelated Air Cleanliness/Fallout, chaos-meter, map-mode, package-document, interface, localisation, and asset changes are user-owned. They will not be reverted, overwritten, staged, or included in Chaos Warfare commits. Later integration with shared Air Cleanliness or Condemnation files will be done as narrow patches after re-reading their then-current state.

## Stage 0 exit result

The required gameplay surfaces are supported except continuous ordinary-air mission contamination. The supported exact-state raid route covers chemical air delivery without approximation. No estimator is retained, no broad world pulse is added, no gameplay fallback is introduced, and no gameplay file is changed in Stage 0.
