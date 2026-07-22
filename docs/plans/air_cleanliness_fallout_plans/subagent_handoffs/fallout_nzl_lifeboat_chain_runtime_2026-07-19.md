# Fallout NZL lifeboat chain runtime handoff - 2026-07-19

## Scope and evidence

This handoff covers the bounded runtime repairs requested for the dormant New
Zealand lifeboat package. I read `AGENTS.md`, the required Chaos Redux event,
focus-tree, and subagent skills, the offline Paradox wiki pages for data
structures, triggers, effects, scopes, on actions, events, decisions, ideas,
AI, modifiers, and localisation, plus the vanilla script-constant,
effects, and triggers documentation. The implementation proof and pilot spec
were reviewed in:

- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_NZL_LIFEBOAT_ENGINE_PROOF.md`
- `docs/specs/air_cleanliness_fallout_specs/fallout_nzl_lifeboat_state_pilot_spec.md`
- `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/fallout_nzl_lifeboat_focus_audit_2026-07-19.md`

The package remains dormant: no activation caller was added and no focus file
was edited.

## Files changed

- `common/scripted_effects/fallout_nzl_lifeboat_effects.txt`
  - Added `fallout_nzl_add_chain_context_score` call support and
    `fallout_nzl_clear_partner_response_receipt`.
  - Made no-partner external startup dispatch the authored `.139`/`.140`
    choice event after recording the current generation.
  - Replaced six fixed `recruit_character` calls with guarded
    `generate_character` definitions carrying stable token bases, portraits,
    country-leader roles, and advisor roles.
  - Clears partner response flags through the stored partner target during
    package reset, new transaction selection, and external-chain cleanup.
  - Central reset also clears the home-guard mobilization and quiet-seas
    access-in-progress flags and tears down the generation-bound relief
    guarantee relation/receipt without touching persistent mobilization or
    postwar partner history.
- `common/scripted_effects/fallout_nzl_lifeboat_effects.md`
  - Documents helper scopes, inputs, outputs, side effects, call sites, and
    the character migration.
- `common/scripted_triggers/fallout_nzl_lifeboat_triggers.txt`
  - Uses inclusive `check_variable` for the pirate forced-settlement boundary.
  - Adds `fallout_nzl_year_ten_values_are_ready`, requiring current package and
    all four values at or above the central stable threshold.
- `common/on_actions/fallout_nzl_lifeboat_on_actions.txt`
  - Settles the receipt from NZL scope for capitulation, peace-conference, and
    annexation while matching the exact stored aggressor. This catches
    capitulation/annexation by actors other than NZL without settling an
    unrelated country.
- `common/script_constants/fallout_nzl_lifeboat_constants.txt`
  - Added `fallout_nzl_score` fixed-point tuning category for state control,
    choices, routes, war pressure, and prior-result quality.
- `common/characters/fallout_nzl_lifeboat_characters.txt`
  - Removed duplicate static definitions. Runtime generation now owns the six
    tokens and roles.
- `events/fallout_world_end_events.txt`
  - Removed tag-only admission from delayed resolvers `.130`, `.136`, `.144`,
    and `.150` (`always = yes`). Immediate blocks retain current package and
    chain guards.
  - Generation-binds partner response flags in `.141` and `.142`.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `fallout_nzl_add_chain_context_score` | NZL country | temp `fallout_nzl_chain_score`, temp `fallout_nzl_prior_result`, current state/route/war/choice context | adjusted temp score | clears helper temps and makes no persistent writes | opening, domestic, external partner, late calculators |
| `fallout_nzl_clear_partner_response_receipt` | partner country | none | none | clears three response flags and generation variable | package reset, transaction start, external cleanup |
| `fallout_nzl_year_ten_values_are_ready` | NZL country trigger | current package values | boolean | none | ready for parent focus/decision call site |

The context score is deliberately deterministic. State control uses the five
spec states (284, 1079, 723, 1080, 1081) and a central divisor. Choice, route,
war pressure, and prior quality are all named constants rather than literals.
No fallback result path was added.

## Event target and cleanup plan

- `fallout_nzl_external_partner_target` remains the global pointer for the
  current short-lived bilateral transaction. Before replacing or clearing it,
  the new helper clears response flags and the partner generation receipt.
- `fallout_nzl_external_owner_target` remains the owner pointer used by partner
  response events and existing chain cleanup.
- No new global target was introduced for pirate settlement. On-action scopes
  enter static `NZL`, then compare the stored aggressor variable with the
  documented `ROOT`/`FROM` terminal country before calling the existing
  settlement effect.
- No recurring world-iteration on action was added.

## Migration and validation

The character migration preserves all six token names used by promotions and
advisor references. The inline role definitions copy the former static
portraits, ideologies, traits, advisor slots, visibility, availability, costs,
and AI weights. Each generation is guarded by `NOT = { has_character = ... }`,
so repeated package calls do not duplicate characters.

Meaningful static checks run:

- `rg` confirms no `recruit_character` remains in the NZL lifeboat effect or
  on-action files, and all six `generate_character` blocks are present.
- `rg` confirms exactly four delayed resolver events use `trigger = { always =
  yes }`, while `.132`, `.138`, `.146`, and `.152` cleanup callbacks retain
  their existing package-tag guard.
- `rg` confirms all six partner response branches set
  `fallout_nzl_partner_response_generation` and the cleanup helper clears it.
- `rg` confirms all four score calculators call the shared context helper and
  the constants file contains `fallout_nzl_score`.
- Offline wiki and vanilla documentation checks cover `generate_character`,
  `save/clear_event_target`, `check_variable`, `surrender_progress`, and
  `on_annex`/`on_capitulation`/`on_peaceconference_ended` scope semantics.

The four delayed resolvers now enter even after a temporary tag/package
transition. Their immediate success branch still requires the current package
and current chain receipts. If either guard fails, the existing `else` branch
closes the chain through a cleanup helper that does not itself require the
package gate. This preserves fail-closed result application while preventing a
stale hidden event from blocking cleanup.

Skipped meaningful validation: no live HOI4 load, console scenario, or
`hoi4-agent-tools` runtime was available/required in this bounded handoff.
The remaining risk is engine acceptance of this dormant package's runtime
generation and static-tag on-action scope, which follows the repository's
existing `generate_character` and direct country-scope precedents but still
needs the parent agent's final integration review.

## Parent integration notes

- The focus caller should dispatch `.139`/`.140` only for a current partner
  transaction. No-partner startup now dispatches those events itself after the
  generation receipt is recorded.
- The parent may wire `fallout_nzl_year_ten_values_are_ready` from the focus or
  decision surface without editing this handoff's runtime files.
- The decision agent should use the clear helper if it ever retains a partner
  response beyond the external chain. Raw response flags are no longer
  unscoped persistent state.

## Simplifications, omissions, and blockers

No requested runtime branch was replaced with a fallback or placeholder. No
focus, decision, asset, GUI, localisation, spreadsheet, or activation caller
was changed. Live engine validation remains a follow-up owned by the parent.
