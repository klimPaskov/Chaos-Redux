# Event 006 starting-force package mapping handoff

## Status

The starting-force implementation matrix and its readiness-gated runtime
dispatcher are complete for all accepted Event 006 package IDs from `IW-001`
through `IW-206`. The bounded dynamic starting-force calculator and
materializer are also implemented, but release wiring remains deliberately
blocked until each country has an accepted command roster and the synchronized
executor can provide its frozen host and anchor targets.

This handoff covers the matrix, runtime mapping, and reusable force framework.
It does not claim that any country package is playable or that opening forces
are currently materialized during a wave.

## Scope and ownership

Files created by this tranche:

- `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_force_package_mapping_handoff.md`
- `common/script_constants/006_independence_wave_force_constants.txt`
- `common/script_constants/006_independence_wave_force_package_constants.txt`
- `common/scripted_effects/006_independence_wave_force_effects.txt`
- `common/scripted_effects/006_independence_wave_force_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_force_triggers.txt`
- `common/scripted_triggers/006_independence_wave_force_package_mapping_triggers.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- nine force-template names in
  `localisation/english/006_independence_wave_l_english.yml`

No event, decision, idea, character, AI strategy, interface, asset,
spreadsheet, or accepted specification file was edited.

## Matrix contract

The CSV contains one row for every accepted candidate package and exposes these implementation inputs:

- `package_id`
- `working_name`
- `resolved_tag`
- `source_starting_force_archetype`
- `force_profile`
- `military_tradition_score`
- `support_access_direction`
- `navy_inheritance`
- `air_inheritance`
- `reinforcement_pathways`
- `officer_commander_direction`
- `force_specific_risk_tradeoff`
- `research_sensitive_leader_or_symbol_flag`
- `research_sensitive_direction`
- `evidence`

`force_profile` uses exactly one of the nine accepted implementation enums:

- `territorial_defense`
- `industrial_security`
- `regular_defectors`
- `mountain_frontier`
- `coastal_maritime`
- `mounted_mobile`
- `desert_nomadic`
- `river_jungle`
- `foreign_volunteers`

Every `reinforcement_pathways` value is drawn only from the accepted list in specification part 5. Each row receives five distinct paths, exceeding the requested minimum of three without inventing another pathway enum.

## Interpretation and implementation boundaries

The dominant force profile is an implementation classifier, not a claim that the country's whole force must use one division template. The source archetype remains in its own column so mixed coastal, air, river, mounted, industrial, and defecting-unit elements are not erased by the classifier.

The military-tradition score is a comparative planning input grounded in the accepted force archetype, regional military identity, and package research. It is not a historical worth ranking and must not become a generic combat bonus by itself. The implementation should use it as one input to bounded command readiness, officer access, training, or initial cohesion alongside package conditions.

Support access describes the order in which the package can plausibly open support companies and institutional capabilities. It does not authorize unconditional technology grants. Parent implementation should translate the direction into starting access, mission-gated access, or reinforcement rewards appropriate to the accepted package disposition and balance model.

`navy_inheritance = yes` and `air_inheritance = yes` mean the package is eligible for a bounded, relevant share of host assets when those assets exist and the release plan can transfer them without breaking host survival or another reserved package. They do not authorize transfer of an entire navy or air force. A `no` value does not forbid later construction, purchase, volunteers, or mission rewards.

The leader-or-symbol sensitivity flag gates unsafe personal leader and emblem assignment only. It does not disable the package's starting-force identity. A flagged package keeps its full mapped force profile, reinforcement routes, officer direction, and risk tradeoff while the accepted institutional, community-specific, dynastic, or dossier-backed identity direction controls final character and symbol wiring. These institutional directions are accepted identity designs, not fallback content.

Packages whose accepted disposition is scenario-only, formable-only, high-chaos-only, mutually exclusive, or specific-community-only still have a complete force row because all 206 accepted packages require a force identity. Their accepted disposition, anchor, reservation, and exclusivity rules remain authoritative and were not relaxed by this matrix.

## Coverage summary

| Measure | Result |
| --- | ---: |
| Package rows | 206 |
| Unique package IDs | 206 |
| Resolved tags matched to the accepted registry | 206 |
| Source force archetypes matched to the accepted registry | 206 |
| Rows with five distinct accepted reinforcement paths | 206 |
| Research-sensitive leader or symbol rows | 81 |
| Navy-inheritance eligible rows | 39 |
| Air-inheritance eligible rows | 26 |
| Military-tradition score range | 35-82 |

Force-profile distribution:

| Force profile | Packages |
| --- | ---: |
| `coastal_maritime` | 40 |
| `desert_nomadic` | 14 |
| `foreign_volunteers` | 7 |
| `industrial_security` | 8 |
| `mountain_frontier` | 53 |
| `mounted_mobile` | 27 |
| `regular_defectors` | 15 |
| `river_jungle` | 23 |
| `territorial_defense` | 19 |

## Sensitive identity resolution

The 81 flagged rows exactly match the accepted research categories that cannot safely receive an unverified personal leader or generic symbol:

- 46 rows whose research requires an institutional council or a sourced leader from the exact named community because one fictional person cannot represent the broad real identity;
- 25 rows whose research requires a sourced period incumbent or claimant, with an institutional regency or royal council where the accepted research does not establish a safe claimant;
- 10 signature-dossier rows: `IW-043`, `IW-058`, `IW-059`, `IW-093`, `IW-096`, `IW-097`, `IW-098`, `IW-150`, `IW-161`, and `IW-197`.

All 48 rows listed in `006_sensitive_package_resolution.md` are contained in that flagged set. Every flagged row has a package-specific `research_sensitive_direction`; no flagged row uses the normal provenance-only text. Conversely, all 125 unflagged rows use the normal accepted provenance direction.

## Evidence basis

Each row cites all three necessary evidence layers in its `evidence` field:

- the package row in `006_candidate_country_registry.csv`, including the accepted starting-force archetype and resolved tag;
- the matching regional military identity from `006_regional_overlay_matrix.csv` through its `REG-01` to `REG-14` identifier;
- the applicable package research dossier, sensitive-resolution row, or signature-country dossier.

The mapping also followed the accepted reinforcement model in `006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`, the accepted sensitive identity rules, the package research-resolution matrix, and the signature-country dossiers. No accepted source-of-truth text was modified.

Required reference reading completed before the mapping work:

- repository skills `chaos-redux-event-planning`, `chaos-redux-events`, and `chaos-redux-subagents`;
- offline wiki core pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding;
- additional offline wiki pages for Country creation, Division modding, Equipment modding, and Technology modding;
- installed vanilla documentation for AI templates, AI equipment, AI navy, characters, decisions, on actions, equipment units, script constants, script concepts, effects, and triggers;
- vanilla precedents for `create_unit`, `load_oob`, `transfer_units_fraction`, `transfer_navy`, `transfer_ship`, technology setup, and commander creation.

## Validation evidence

Cross-source validation against the final CSV found:

- the exact contiguous ID set `IW-001` through `IW-206`, with no duplicate or missing package ID;
- all 206 resolved tags equal the accepted candidate-registry tags and match the three-character tag format;
- all 206 source force archetypes equal the accepted candidate-registry values;
- all profile values belong to the nine-value force-profile enum;
- all military-tradition scores are integer values in the requested 0-100 range;
- all navy, air, and sensitivity fields use only `yes` or `no`;
- every row contains five distinct reinforcement paths and every path belongs to the eleven-value accepted reinforcement list;
- no blank cell in any of the 15 columns;
- no duplicate support-access direction, officer/commander direction, force-specific risk/tradeoff, or evidence entry;
- exact equality between the 81-row research-defined sensitive set and the 81 flagged rows in the mapping.

Final CSV SHA-256:

- `28AC99832A419FB5E8EA1521AB1B25A57DC41FCF481AC10E4B74419E1F77FBF8` - `006_force_package_mapping.csv`

## Runtime implementation

`independence_wave_probe_force_package_mapping` is the non-mutating public
probe. It accepts temporary `independence_wave_setup_package_id`, dispatches the
matching `p1` through `p206` constants through a meta effect, decodes the five
reinforcement paths and bounded inheritance bits, and exposes
`has_ready_independence_wave_force_package_mapping_probe` for pre-transfer
validation.

`independence_wave_load_force_package_mapping` persists the validated profile,
tradition, five pathway flags, inheritance eligibility, sensitivity flag, and
mapping revision on an initialized Event 006 country. It never grants
`independence_wave_command_roster_ready` and never materializes forces.

`independence_wave_apply_dynamic_starting_force` calculates one generation-
locked opening force from territory, population, industry, transport, host
condition, chaos, legitimacy, tradition, patron, network, and accepted force
profile. It is bounded to 1-3, 3-5, 4-7, or 6-10 divisions by the accepted
force tier, creates the profile template at the frozen anchor, adds concrete
equipment and logistics, inherits host technology, and transfers only an
approved 4-8 percent naval or air fraction. Land units, general stockpiles,
and host unit leaders are never transferred.

The balance bounds were exercised at all four force tiers. Representative
inputs produced 3 divisions for both a 59.2-point minimal fragile package and a
140-point developed fragile package, 5 for a 144.88-point viable package, 7 for
a 215-point armed package, and 10 for a 287.5-point high-chaos package. These
cases prove that richer inputs strengthen stockpiles and recorded force budget
without escaping the accepted 3, 5, 7, and 10 tier ceilings.

## Visual and localisation wiring

The runtime force framework does not require a dedicated sprite: it creates
normal division templates and exposes recorded values to the shared Event 6
mechanics and Event Details surfaces. The nine final template names are wired
through `GetIndependenceWaveForceTemplateName`. Any visible force-profile
indicator must reuse the registered Event 6 military focus or idea icon family
and be declared in `interface/006_independence_wave.gfx`; no unregistered icon
name is introduced by this tranche.

## Parent integration work

The parent implementation should treat this CSV as a package-content input beneath the accepted candidate registry and dispositions. The remaining work includes:

- call the non-mutating mapping probe during package readiness validation;
- load the validated mapping after country initialization and before force
  materialization;
- wire reinforcement decisions or missions to the exact accepted pathway names and package-specific access directions;
- implement commander and officer creation using the row direction plus the accepted research leader resolution;
- ensure sensitive rows never receive a generic leader or symbol while retaining their force package;
- set `independence_wave_command_roster_ready` only after that roster passes its
  package audit, then call the generation-locked force materializer;
- add AI choices, effect descriptions, trigger tooltips, localisation, documentation, and any required unit or character definitions;
- validate interaction with protected-host survival, reservation groups, mutually exclusive packages, and active Event 005 origins.

Final gameplay wiring remains the parent agent's responsibility. The CSV does not override the accepted automatic-pool disposition, state-anchor, host-protection, tag-collision, or identity-resolution rules.

## Simplifications, omissions, and blockers

No package, force field, accepted reinforcement path requirement, sensitive identity distinction, or evidence layer was omitted from the assigned mapping. No placeholder, fallback, or weaker substitute was used.

Country-specific command rosters, package AI, reinforcement decision outcomes,
and synchronized release calls remain unwired. The framework refuses to
materialize without the command-roster gate, so this is an explicit remaining
integration boundary rather than a fallback.

There is no mapping blocker.

## Skills used

- `chaos-redux-event-planning`
- `chaos-redux-events`
- `chaos-redux-subagents`

No skill was created or updated.
