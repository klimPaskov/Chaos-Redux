# Event 018 Foreign Interest Scoring Handoff

Date: 2026-07-12

Status: bounded patch complete. No files were staged or committed.

## Files changed

- `common/scripted_effects/018_resources_found_decision_effects.txt`
- `common/script_constants/018_resources_found_foreign_interest_constants.txt`
- `docs/events/018_resources_found.md`
- `docs/events/018_resources_found_helper_contracts.md`
- `docs/plans/018_resources_found_plans/subagent_handoffs/foreign_scoring_handoff.md`

## Identifiers and call site

- Added `resources_found_score_foreign_interest_candidate` in country scope.
- Replaced the body of `resources_found_select_foreign_interest_actor`.
- Kept its one existing call in the Invite Strategic Bids completion branch of `resources_found_complete_selected_field_project`.
- Added the `resources_found_foreign_interest_score` script-constant table.
- Added regular event target `resources_found_foreign_interest_best_candidate_target` for the current effect chain only.
- Retained regular targets `resources_found_foreign_interest_owner_target` and `resources_found_foreign_interest_field_target`.

## Behavior before and after

Before this patch, Invite Strategic Bids selected one country uniformly through `random_country` from the broad foreign-partner trigger. A neighboring importer and a distant resource-rich major had equal selection probability once both passed that trigger.

After this patch, completion of that project runs one `every_country` scan. The field-wide and owner-wide component is calculated once. Every valid country then receives a candidate score based on the live strategic-resource economy and current diplomatic context. The first country at the minimum qualifies, and only a strictly higher later score replaces it. The final regular event target therefore gives deterministic tie behavior without a periodic scan.

The scan does not run for a closing, cave-converted, or transaction-locked field. Candidate validity still uses `resources_found_decision_is_valid_foreign_partner`, which excludes the owner, DHO, special chaos countries, actual nonhuman countries, and countries at war with the owner. Capitulated countries are also excluded by the scan.

## Exact scoring factors

### Shared field and owner component

- Event 018 field total, capped at 600, adds 0.04 per unit.
- Each distinct Event 018 resource type adds 3.
- Each Developed Yield point adds 0.10.
- The globally significant field flag adds 10.
- Suspension subtracts 12.
- An active international commission subtracts 10.
- A non-major owner adds 5 to foreign opportunity.
- An owner below 15 factories adds 6.
- Owner stability below 0.40 adds 4.
- Owner surrender progress above 0.25 adds 8.

### Resource-specific country component

The following calculation runs separately for oil, aluminium, rubber, tungsten, steel, and chromium only when that resource is present in the field's Event 018 ledger.

- A negative live country balance is negated into a deficit, capped at 80, then adds 0.50 per missing unit.
- Live imports are capped at 80, then add 0.25 per imported unit.
- Live industrial consumption is capped at 120, then adds 0.10 per consumed unit.
- Live domestic production above 40 is treated as abundant extraction. The excess is capped at 120, then subtracts 0.10 per unit.

The calculation uses `resource@<type>`, `resource_imported@<type>`, `resource_consumed@<type>`, and `resource_produced@<type>`. The documented `has_resources_in_country` balance, imported, and extracted modes were used to verify the meaning of these current dynamic values.

### Route, relations, rivalry, and capacity

Only the strongest route applies.

- Land neighbor adds 18.
- Same faction adds 14.
- Military access in either direction adds 10.
- Same continent adds 7.
- A valid maritime route adds 6.
- No route subtracts 20.

The maritime route requires a candidate-owned and controlled coastal state. It also requires either a coastal field state or an inland field connected to its owner's home area while that owner controls a coastal state.

Additional candidate factors are:

- Candidate opinion of the owner, clamped from -100 to 100, adds 0.08 per opinion point. Negative opinion therefore subtracts interest.
- A core on the field adds 16. A claim adds 12 when no core exists.
- Being the existing concession or contract partner adds 10.
- Being at war with that existing partner adds 8 when the candidate is not the partner.
- Being at war adds 8 for wartime demand.
- Major status adds 10.
- Factory capacity, capped at 100, adds 0.08 per factory.
- Surrender progress above 0.50 subtracts 10 for wartime overextension.

The minimum qualifying score is 20. A country below that score does not receive the foreign actor flag or persistent owner and field pointers.

## Preserved downstream wiring

The winning country still receives:

- `resources_found_foreign_field_actor`
- `resources_found_foreign_interest_owner` pointing to the inviting owner
- `resources_found_foreign_interest_field` pointing to the selected field
- `resources_found_refresh_decision_cost_previews = yes`

No winning candidate means none of these writes occur. Existing actor lifecycle and cleanup outside this selection helper were not changed.

## Reference basis

The required offline wiki core pages were consulted, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and Resources modding. Targeted sections covered regular event targets, unscoped temporary variables, `every_country`, resource balance and imports, opinion, adjacency, access, continent checks, and scripted effects.

Vanilla documentation consulted:

- `documentation/effects_documentation.md`
- `documentation/triggers_documentation.md`
- `documentation/dynamic_variables_documentation.md`
- `documentation/script_concept_documentation.md`
- `common/script_constants/documentation.md`

Vanilla precedents included the imported-resource calculation in `common/scripted_effects/SWE_scripted_effects.txt`, live opinion weighting in `events/AAT_Iceland.txt`, and neighbor, major, factory, and continent factors in `common/scorers/country/generic_platonic_scorers.txt`.

## Focused validation

- Resource coverage found one field-ledger gate and one balance, import, consumption, and production read for each of all six standard resources.
- The selector contains zero `random_country` calls, one `every_country` call, one external selector call site, and one candidate-score helper call site.
- All 43 `resources_found_foreign_interest_score` references resolve to the dedicated constants table, with no unused table entry.
- The score, component, field score, and best score temporary variables have zero scoped references.
- The winning block contains exactly one actor-flag write, one owner-pointer write, one field-pointer write, and one preview refresh.
- Structural brace checks finished at depth zero for the effect file and the new constants file.
- A baseline field arithmetic fixture produced 70.1 for a neighboring wartime importer, 25.2 for a modest same-continent buyer, and 0 for a distant resource-abundant major. The same modest buyer fell to 3.2 when suspension and commission penalties applied, below the minimum of 20.

No live game session was run in this subagent task. Static validation used the current official game documentation and vanilla script precedents for every engine-facing construct added here.

## Simplifications, omissions, and risks

No requested scoring factor was omitted or replaced with a fallback. The score intentionally reads the instant resource economy when Invite Strategic Bids completes, so a country's rank can change between separate invitations as imports, production, wars, access, and relations change. Owner weakness and field significance are shared across all candidates, which means they affect whether a bid market forms while candidate-specific need and access decide the ranking.
