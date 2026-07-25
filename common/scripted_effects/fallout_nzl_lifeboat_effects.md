# Fallout NZL lifeboat scripted effects

This reference documents the runtime helpers owned by
`common/scripted_effects/fallout_nzl_lifeboat_effects.txt`. The package remains
dormant until its allocator receipts are current. These helpers do not add an
activation caller.

## `fallout_nzl_add_chain_context_score`

Scope: country (the NZL package owner).

Inputs:

- `fallout_nzl_chain_score` is the caller's current value average in a
  temporary variable.
- `fallout_nzl_prior_result` is a temporary result token supplied by the
  caller. Callers use `fallout_nzl_chain_result.none` when no earlier chain is
  available.
- `fallout_nzl_chain_choice`, route flags, `has_war`, and the five package
  states provide current context.

Outputs and side effects:

- Adds deterministic state-control, choice, route, war-pressure, and prior-result adjustments to `fallout_nzl_chain_score`.
- Uses only temporary variables and clears both helper temporaries before it
  returns.
- Reads all tuning values from the `fallout_nzl_score` script-constant
  category. No score magic numbers are embedded in the effect.

Call sites:

- `fallout_nzl_calculate_opening_result`
- `fallout_nzl_calculate_domestic_result`
- `fallout_nzl_calculate_external_result` (partner branch)
- `fallout_nzl_calculate_late_result`

## `fallout_nzl_clear_partner_response_receipt`

Scope: partner country. Clears the three response flags and the generation
receipt written by events `chaosx.fallout.141` and `chaosx.fallout.142`.

It is called through the stored partner event target before a new external
transaction, package reset, or external-chain cleanup. This prevents a stale
partner response from surviving a generation change while retaining the
response flags for any current-generation diagnostics.

## Numbered sea-road helpers

`fallout_nzl_activate_sea_road_licensing` records the current Fallout transition generation and opens the existing Fishery Quota Compact. The focus caller retains the immediate Sea-Lane Security gain and does not remove convoys.

`fallout_nzl_issue_sea_road_patrol_window` fails closed unless the licence receipt is current. It writes one 90-day timed flag through a temporary duration variable, stamps the current generation, increments the licence serial, and adds the visible `fallout_nzl_quiet_seas_patrol_window` dynamic modifier. Reissuing the window refreshes the same timed flag and does not create a second countdown.

`fallout_nzl_close_quiet_seas_patrol_window` clears the timed flag, generation receipt, and visible modifier during package cleanup. Natural expiry satisfies the modifier's `remove_trigger`, so no recurring on action is required.

The reusable Fishery Quota Compact pays five convoys under current licensing, raises Food Security and Sea-Lane Security, and renews the window. The one-shot Quiet-Seas Patrol pays ten convoys under current licensing, retains its navy-experience and factory commitments, raises Sea-Lane Security by twelve, and renews the same window. Their non-licensed branches retain the earlier costs and results.

## `fallout_nzl_add_sea_road_score`

Scope: country (the NZL package owner).

Input: temporary `fallout_nzl_chain_score` after the shared context score.

For a current isolation-route licence, the helper adds four points when the patrol window is current and subtracts four points when it has lapsed. Only the external and Year 10 result calculators call it. Opening, domestic, and humanitarian scoring remain unchanged. Both values come from `fallout_nzl_sea_road` script constants.

## `fallout_nzl_start_external_transaction`

Scope: NZL country. Chooses the deterministic lowest-id valid partner. When a
partner exists, it records the current generation and target. When no partner
exists, it records a generation-bound no-partner receipt and dispatches the
authored human (`.139`) or AI (`.140`) external choice event. The choice event
continues to own payment, delayed result resolution (`.144`), visible result,
and cleanup.

## Runtime character roster

`fallout_nzl_recruit_package_characters` is idempotent on each token and uses
`generate_character` with stable `token_base`, inline portraits, and the full
country-leader/advisor role definition. The former static definitions in
`common/characters/fallout_nzl_lifeboat_characters.txt` are intentionally empty
apart from this ownership note, so the engine cannot load duplicate token
definitions.

## Dormant activation and Year 10 clock

`fallout_nzl_activate_lifeboat_package` remains dormant outside the B7 vertical slice. The B7 caller reaches it only after the guarded existing-tag assignment commits its current-generation receipts. After the receipt gate passes, it resets NZL-owned package state and writes a timed `fallout_nzl_before_year_ten` country flag for 3,650 days. The duration field uses the file-scoped literal `@FALLOUT_NZL_YEAR_TEN_DAYS`, mirrored by `constant:fallout_nzl_duration.year_ten` for shared tuning and documentation surfaces. `fallout_nzl_year_ten_values_are_ready` requires the timed flag to have expired. Reset clears the old flag before any later valid activation writes a fresh one.

## Bounded formation placement

`fallout_nzl_create_starting_force_family` remains guarded by the exact NZL
state package and one generation receipt. Its three two-battalion formations
use explicit province priorities for Wellington (`1814`), Auckland (`4543`),
and Canterbury (`2197`) while retaining the state scope and enemy-province
spawn restriction. `fallout_nzl_create_extra_escort_formation` places its
one-shot Southern Escort Volunteers at Auckland province `4543`.

## Pirate terminal outcomes

`common/on_actions/fallout_nzl_lifeboat_on_actions.txt` enters NZL scope for
capitulation, peace-conference completion, and annexation. Each path matches
the exact stored aggressor before calling `fallout_nzl_record_pirate_settlement`.
Annexation therefore closes when any actor annexes the recorded aggressor and
does not settle an unrelated country.

`fallout_nzl_record_pirate_defeat` is the paired losing terminal helper.

Scope: NZL country.

Inputs:

- the current Lifeboat package
- a generation-bound exact pirate-war receipt
- no current settlement or defeat receipt

Outputs and side effects:

- writes `fallout_nzl_pirate_defeat_recorded`
- writes `fallout_nzl_pirate_defeat_generation`
- closes the force-settlement decision

The capitulation and peace-conference hooks call it only when New Zealand is
the defeated side. This unlocks the late isolation focus with a reduced
security reward and a trust loss. It does not counterfeit a settlement and it
does not satisfy the Closed Seas achievement settlement condition.

The four hidden delayed resolver events admit the scheduled scope without a
tag-only trigger. Their immediate result branch remains package- and
generation-guarded. When that branch is stale, the existing close helper runs
without the package gate so stale callbacks still clean their runtime state.

## Tuning and validation notes

The `fallout_nzl_score` constants are shared by all four result families and
keep state weights, choice adjustments, route pressure, war pressure, and
prior-result quality in one tuning table. Settlement surrender uses an
inclusive `check_variable` comparison so the forced-settlement boundary is
reachable. Delayed resolver events `.130`, `.136`, `.144`, and `.150` no longer
have a tag-only admission trigger. Their immediate blocks still require the
current package and current chain receipts before applying any result.
