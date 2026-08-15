# IW-053 ALT localisation implementation handoff — 2026-08-15

## Disposition

Completed the bounded ALT package-local English localisation after `common/decisions/006_independence_wave_altai_decisions.txt` became available. All source-defined category, mission, project, tooltip, idea, and party consumers in scope now have English keys. No ALT route cosmetic tag is source-defined, so no cosmetic localisation was invented.

## Changed files

- `localisation/english/006_independence_wave_altai_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw053_altai_localisation_2026_08_15.md`

No gameplay, central lists, assets, focuses, cosmetic definitions, or workbook files were changed.

## Changed keys

### Party names

- `ALT_independence_wave_constitutional_party`
- `ALT_independence_wave_constitutional_party_long`
- `ALT_independence_wave_socialist_party`
- `ALT_independence_wave_socialist_party_long`
- `ALT_independence_wave_traditional_party`
- `ALT_independence_wave_traditional_party_long`
- `ALT_independence_wave_emergency_party`
- `ALT_independence_wave_emergency_party_long`

### Ideas

Titles and `_desc` keys were added for:

- `alt_fragmented_mountain_mandate`
- `alt_altai_frontier_compact`
- `alt_oyrot_council`
- `alt_mountain_council_charter`
- `alt_land_rights_compact`
- `alt_mountain_workers_council`
- `alt_mountain_emergency_command`

### Decision category and founding mission

- `independence_wave_altai_mountain_compact_category`
- `independence_wave_altai_mountain_compact_category_desc`
- `independence_wave_altai_hold_mountain_council`
- `independence_wave_altai_hold_mountain_council_desc`

### Ten project decisions

Titles and `_desc` keys were added for:

- `independence_wave_altai_secure_oyrot_depots`
- `independence_wave_altai_integrate_mountain_guards`
- `independence_wave_altai_register_communities`
- `independence_wave_altai_settle_former_host_ledgers`
- `independence_wave_altai_ratify_constitutional_autonomy`
- `independence_wave_altai_adopt_traditional_compact`
- `independence_wave_altai_convene_socialist_councils`
- `independence_wave_altai_establish_emergency_command`
- `independence_wave_altai_codify_durable_sovereignty`
- `independence_wave_altai_open_frontier_network`

### Effect and failure tooltips

- `independence_wave_altai_depots_effect_tt`
- `independence_wave_altai_guards_effect_tt`
- `independence_wave_altai_communities_effect_tt`
- `independence_wave_altai_host_ledgers_effect_tt`
- `independence_wave_altai_host_loss_effect_tt`
- `independence_wave_altai_constitutional_route_effect_tt`
- `independence_wave_altai_traditional_route_effect_tt`
- `independence_wave_altai_socialist_route_effect_tt`
- `independence_wave_altai_emergency_route_effect_tt`
- `independence_wave_altai_sovereignty_effect_tt`
- `independence_wave_altai_network_effect_tt`
- `independence_wave_altai_project_failure_effect_tt`

## Dynamic localisation added

- The category displays current Council Cohesion and Mountain Guard Readiness against `constant:independence_wave_altai_pressure.maximum`, then prints the stability threshold from `constant:independence_wave_altai_pressure.stable`.
- The founding mission prints `constant:independence_wave_altai_duration.founding_crisis` and the same stability threshold.
- The failure tooltip prints `constant:independence_wave_altai_pressure.standard_loss` and names every shared value affected by the helper.

## Before and after

Before this patch, the ALT category, founding mission, ten projects, seven ideas, and four party families had no package-local English localisation, exposing raw identifiers if the package became visible. After the patch, every source-defined player-facing consumer in the bounded decision, idea, and party surfaces has concise English text. The category and mission show their live values and tuning constants instead of copied numbers.

## Prose-quality repairs

### Vagueness

The text names the Oyrot depots, mountain guards, community registers, land rights, former-host ledgers, and frontier network instead of relying on generic institutional language.

### Bloat

Descriptions state one concrete action and its purpose. Tooltips lead with the affected compact or shared system value and omit implementation detail.

### Obvious explanation

Tooltips do not repeat their titles or narrate that clicking a decision starts it. They explain the consequence that is not already visible in the label.

### Repetition

The four government routes use distinct institutions and consequences. Common compact vocabulary remains consistent without copying the same description across routes.

### Overcomplication

Requirements are summarized through the category and mission values instead of reproducing raw trigger blocks.

### Style-rule repair

Player-facing prose contains no em dashes, semicolon-linked sentences, implementation history, tuning notes, staged contrast formulas, or hidden future outcomes.

## Audit results

- Missing keys: none among the source-defined ALT category, founding mission, ten decisions, twelve effect/failure tooltips, seven ideas, and four short/long party pairs.
- Duplicate keys: none inside the target file and none matching these ALT package keys elsewhere in English localisation.
- Scripted localisation issues: no ALT-specific scripted-localisation consumer exists, and no broken reference was found.
- Dynamic text opportunities remaining: none required by the current source. Existing shared cost keys are deliberately reused by the decision file.
- Cross-surface mismatches: no mismatch found between the final decision `name`, `desc`, and `custom_effect_tooltip` consumers and the added keys. No route cosmetic tag is defined or set by the ALT package.
- File encoding concerns: the target file is UTF-8 with BOM.
- Dynamic tokens and formatting: all source-backed variable and constant tokens were preserved. No exception or uncertainty remains.
- Sourced quotations: no sourced or attributed quotation appears on the inspected ALT surfaces. No quotation was added or altered.

## MCP evidence and exact limitation

The installed HOI4 MCP exposes event, focus, GUI, technology, probability, and map routes, but no read-only decision/localisation inspection or decision-category rendering route. `hoi4.probability_inspect` is not a localisation coverage or overflow tool and was not substituted for one. Source-linked key coverage was validated statically, while visual decision-text overflow remains unverified because the required MCP route is unavailable.

## Meaningful validation

- Compared the final ALT decision source's `name`, `desc`, and `custom_effect_tooltip` values with the target localisation keys.
- Compared the seven idea IDs and the eight `set_party_name` consumers with the target localisation keys.
- Checked the complete English localisation tree for duplicate definitions of the added ALT keys.
- Verified the target file begins with the UTF-8 BOM and the `l_english:` header.

## Skipped meaningful validation

- Decision-category rendering and overflow review were blocked because the installed MCP has no decision/localisation inspection or rendering route.
- Live game validation is parent/user-owned and was not attempted.

## Unresolved wording decisions

None. The wording follows the concrete institutions, actions, routes, and effects present in the package-local source. No simplification, fallback, cosmetic identity, or unsourced quotation was introduced.
