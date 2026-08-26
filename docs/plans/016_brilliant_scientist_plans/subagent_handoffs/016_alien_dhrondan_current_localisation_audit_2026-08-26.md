# Event 016 Alien Infantry and D’Rhonda current localisation audit

Date: 2026-08-26

Mode: bounded localisation audit and patch. No gameplay source, interface source, spreadsheet, or asset was changed. No commit was created.

> Later shared MCP receipt correction: `016_current_mcp_audit_2026-08-26.md` supersedes the timeout-only characterization of the DHR focus and Alien Infantry technology routes in this handoff by recording successful focus inspect/render and partial technology inspect/render. The localisation overflow and live typography limits below remain unresolved because the shared receipt does not provide a complete typography or per-state consumer certification.

## Scope and authority

The audit used `AGENTS.md`, the `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, and `chaos-redux-subagents` skills, the binding `016_alien_infantry_and_dhronda_addendum.md`, and the current acceptance scenarios.

The source review covered the provider-neutral Alien Infantry unit, equipment, tactics, hidden technologies, D’Rhondan envoy project, landing and accord decisions, expedition and rebellion missions, Events `chaosx.nr16.40` through `.52`, DHR country identities and decisions, all 88 DHR focuses, the conditional Event Details clause, Event 019 provider-508 presentation, and the linked Alien Infantry text icon.

The localisation rules were checked against the required offline Paradox Wiki pages, including Localisation, Events, Decisions, Focuses, scopes, effects, triggers, modifiers, ideas, on actions, and AI. Vanilla `loc_formatter_documentation.md` and `loc_objects_documentation.md` were also consulted.

## Audit results

### Missing keys

None in the assigned surface.

All 16 in-scope decision and category ids have name and description keys. All 88 DHR focus ids have title and description keys. All 38 explicit title, description, option, and conditional text references in the D’Rhondan event files resolve. The public unit, equipment, technology, tactic, project, and landing keys resolve.

`GetDhrondanEventDetailClause` is a scripted-localisation call rather than a localisation key. Its `defined_text` exists and both outputs, `dhrondan_event_detail_clause` and `dhrondan_event_detail_clause_blank`, resolve.

### Duplicate keys

None exact and case-sensitive in the English localisation set.

The apparent `KRG_XENOBIOLOGICAL_ASCENDANCY`/`KRG_xenobiological_ascendancy` and `ZIN`/`zin` pairs differ by case and are not exact duplicates.

### Scripted-localisation issues

None found in `common/scripted_localisation/016_dhrondan_country_scripted_localisation.txt`.

The conditional Event Details clause appears only after DHR sovereignty forms and otherwise returns the deliberate blank key. The event-target token `[dhrondan_diplomatic_actor.GetNameDef]` correctly omits the `event_target:` prefix.

### Retired and stale names

No maintained source contains a retired guard name, a Kruger-specific Alien Infantry identifier, or a D’Rhondan-specific unit identifier as a current identifier or player-facing name.

The public names remain provider-neutral: `Alien Infantry`, `Alien Laser Weapon`, `Predictive Vector Assault`, and `Probability Screen`. Event 019 provider 508 describes D’Rhondan contact without restoring Kruger ownership.

Two Alien Arms project descriptions still referred to a `capped guard doctrine`. That wording implied the retired guard concept and exposed an implementation cap despite the current gameplay granting general strategic field-projector and army doctrine effects. Both descriptions now refer to defensive doctrine built around authenticated alien artifacts.

### Dynamic text opportunities

Implemented for the landing and rebellion surfaces.

The landing category, decision description, cost line, and effect tooltip now render the existing `alien_infantry_landing.*` constants for equipment cost, reservation time, gains, and all four recovery tiers.

The rebellion mission now renders the existing `dhrondan_contact.*` constants for mission duration, eligibility thresholds, tier boundaries, and probabilities. No new helper or gameplay value was introduced.

Remaining hardcoded expedition and accord values currently match source. They were left unchanged because the assignment was bounded and no current mismatch was found.

### Cross-surface mismatch notes

No unresolved mismatch was found after the patch.

- `chaosx.nr16.47.a.tt` correctly says every marked landing state still owned by the host transfers and every marked state held by another power becomes a claim.
- DHR remains an Event Details conditional clause, not a fifth Event 016 evolution. Events `.40` through `.52` are follow-ups and country responses rather than logged evolutions.
- The DHR package has no dedicated scripted GUI. Its linked presentation surfaces are ordinary decision categories, focuses, event popups, Event Details, country identities, and sprites.
- `GFX_alien_laser_weapon_equipment_medium` resolves in `interface/alien_infantry_system.gfx`, and the referenced Event 019 text-icon alias remains present.

### File encoding concerns

None. The eight directly checked English files begin with the UTF-8 BOM: the six principal Alien Infantry, D’Rhondan, country, focus, and project files, the Event Details/evolutions file, and the Event 019 provider file. No scoped key uses `:0`.

ASCII apostrophes in double-quoted English strings are valid and require no escape. D’Rhonda and the direct D’Rhondan package consistently use the typographic apostrophe. No malformed quote delimiter was found.

### Prose-quality issues

- Vagueness: `capped guard doctrine` did not state what force or practice the project created. It now names strategic field projectors, defensive doctrine, and the authenticated artifacts that constrain the work.
- Bloat: the rebellion mission previously repeated full eligibility clauses inside every percentage tier. It now states the common entry gate once and lists only each tier’s additional condition.
- Obvious explanation: the landing effect repeated the full 2,000-weapon value in its refund line. It now says the full reserve is refunded after the value has already been shown.
- Repetition: landing costs, timers, gains, and recovery tiers no longer repeat independently hardcoded numbers across four keys.
- Overcomplication: the rebellion text replaces nested `unless the higher tier applies` clauses with a common eligibility line and ordered tier lines.
- Style-rule repair: the Alien Arms project text no longer uses the implementation term `capped` or the stale guard implication. No em dash or sentence semicolon remains in the direct patched surface.

### Sourced-quotation preservation

No quote-bearing surface was in the assigned Alien Infantry or D’Rhondan chain. No sourced quotation, attribution, punctuation, or super-event text was changed.

## Patch details

### Changed files

- `localisation/english/016_alien_infantry_api_l_english.yml`
- `localisation/english/016_dhrondan_contact_l_english.yml`
- `localisation/english/016_brilliant_scientist_projects_l_english.yml`

### Changed keys

- `alien_infantry_landing_category_desc`
- `alien_infantry_call_landing_desc`
- `alien_infantry_landing_reserve_cost_text`
- `alien_infantry_call_landing_effect_tt`
- `dhrondan_rebellion_pulse_mission_desc`
- `brilliant_scientist_alien_arms_weaponization_desc`
- `brilliant_scientist_advance_alien_arms_weaponization_desc`

### Behavior and display before and after

Gameplay behavior is unchanged.

Before, the landing strings copied fixed values from script constants, the rebellion mission repeated threshold logic in long tier clauses, and the Alien Arms weaponization text referred vaguely to capped guard doctrine.

After, existing values render dynamically, the rebellion gate and its three probabilities are readable in order, and the project description matches the current general field-projector and defensive-doctrine effect without suggesting a retired unit family.

All existing dynamic tokens, icons, state names, actor names, country names, colors, and line breaks were preserved unless the key was deliberately converted from a fixed value to its existing constant token.

## MCP evidence and limitations

Fresh current calls were attempted for every supported linked surface.

- `hoi4.event_inspect` for `{ kind: event, eventId: chaosx.nr16.40 }` did not return after repeated bounded waits and was terminated. `hoi4.event_render` for the same event options view also did not return and was terminated.
- `hoi4.focus_inspect` and `hoi4.focus_render` for `dhrondan_focus_tree` did not return after repeated bounded waits and were terminated. An initial inspection with the incorrect id `DHR_focus_tree` returned the exact blocker `FOCUS_TREE_NOT_FOUND`; the source id is `dhrondan_focus_tree`.
- `hoi4.tech_inspect` and `hoi4.tech_render` for `brilliant_scientist_alien_predictive_warfare_tech` did not return after repeated bounded waits and were terminated.
- The installed package exposes no ordinary decision-category, event-popup typography, achievement, or native tooltip renderer. The Technology Tree Viewer is absent.

The latest successful historical artifacts remain useful context but are not represented as fresh proof:

- Event `.47` state flow: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc3cd6c47c9f9412410975e6cc452487783d158c2f8098de9474377c3c042d99/7e0ecd2f9a291a10ff69e056a0a9259b89ef049b1156bf6e60d740a1b8236bdf/event-state_flow-f588a2607444.json`
- DHR focus inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59f99990f9d8ead0b0f5b094574e2319135bb0fa341e385f59ea133fff9cd751/fca4e2f24b157e1b32d4972454654a72198f57ff006bb2268a5647f1ca2f0720/focus-inspect.5cf1d337bc3cac06.json`
- Alien Predictive Warfare trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/17a184bf5d347578aa494d48efd59a525015117dc6053426179e8c3367cfc321/bb718b7ffa24e86e50d5263a378fbd0e425741707bbffab6e8aa13dca3a2583e/technology-trace-b2b1e58d15b2.json`

Current overflow, font wrapping, and rendered source-location evidence therefore remain unresolved. Source review is not treated as equivalent MCP render evidence.

## Meaningful validation

- Rebuilt the case-sensitive English key index and found no exact duplicate.
- Resolved all in-scope decision/category pairs, all 88 DHR focus title/description pairs, all 38 explicit D’Rhondan event text references, the public unit/equipment/tactic/technology/project keys, and both DHR Event Details outputs.
- Compared the displayed rebellion tiers directly with `dhrondan_rebellion_pulse_is_eligible`, `dhrondan_rebellion_medium_tier_is_active`, `dhrondan_rebellion_high_tier_is_active`, and the current script constants.
- Compared every dynamic landing token with `016_alien_infantry_api_constants.txt` and the current reservation, refund, success, and cooldown call sites.
- Confirmed the patched files retain UTF-8 BOM and the linked Alien Laser Weapon icon resolves.

## Skipped meaningful validation and why

- Current MCP inspection and render evidence is incomplete because the supported calls did not return within bounded waits.
- Decision, event-popup, ordinary tooltip, and technology-tree overflow cannot be rendered through an available applicable route.
- Live in-game typography and display acceptance belongs to the user.

## Unresolved wording decisions

None inside the patched keys.

The broad Event 016 project file contains older generic project-board prose outside this bounded Alien Infantry and D’Rhondan audit. It was not turned into a repository-wide tone rewrite.

## Simplifications, omissions, and blockers

No localisation fallback, alias, hidden-route reveal, quote normalization, gameplay simplification, or broad unrelated rewrite was introduced.

The localisation patch is complete within its bounded source scope. Fresh MCP overflow/render evidence remains blocked as described above, so this handoff does not certify whole-event visual acceptance.
