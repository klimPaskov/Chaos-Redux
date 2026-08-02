# Event 012 weather commitment visibility and launch-gate audit

Date: 2026-08-02.

Status: implemented narrow decision and localisation correction.

## Scope

Audited the Event 012 shared Charter action launch surface, the four shared missions, target validation, action cleanup, AI parity, and the hostile natural-disaster bridge.

The patch is limited to the host's two shared launcher decisions and their existing quote data.

No tags, models, GUI source, Event 013 source, focus source, category structure, or new decision system were added.

## Patched issue

`africa_execute_selected_country_action` and `africa_execute_selected_host_action` previously tested only `africa_can_pay_action_quote`.

For `petition_the_rain` and `defy_the_drought`, the Event 013 caller reserve is charged separately by `africa_reserve_natural_disaster_weapon_cost`.

The final action validator correctly rejected an unaffordable reserve, but the launcher remained enabled and the quoted-cost line omitted the caller reserve.

`africa_can_pay_selected_action_commitment` now combines the normal dynamic quote affordability test with `africa_natural_disaster_weapon_cost_is_available` only for those two weather actions.

Both shared launchers use it for `available` and `custom_cost_trigger`.

The quote now copies the configured `africa_natural_disaster.caller_pp_cost` and `caller_cp_cost` into dedicated display variables only for weather actions, resets them when the quote is cleared, and renders them as an additional normal or blocked cost line.

## Changed files and identifiers

- `common/decisions/012_africa_decisions.txt`
  - `africa_execute_selected_country_action`
  - `africa_execute_selected_host_action`
- `common/scripted_triggers/012_africa_triggers.txt`
  - `africa_can_pay_selected_action_commitment`
- `common/scripted_effects/012_africa_action_effects.txt`
  - `africa_clear_action_quote`
  - `africa_refresh_selected_action_quote`
  - variables `africa_quote_natural_disaster_caller_pp` and `africa_quote_natural_disaster_caller_cp`
- `common/scripted_localisation/012_africa_scripted_localisation.txt`
  - `GetAfricaSelectedActionAdditionalCost`
  - `GetAfricaSelectedActionAdditionalCostBlocked`
- `localisation/english/012_african_union_l_english.yml`
  - `africa_selected_action_dynamic_cost`
  - `africa_selected_action_dynamic_cost_blocked`
  - `africa_selected_action_dynamic_cost_tooltip`
  - `africa_selected_action_weather_reserve_cost`
  - `africa_selected_action_weather_reserve_cost_blocked`
  - `africa_selected_action_no_additional_cost`

## Before and after

Before, a host that could pay the quoted Charter commitment but lacked the additional weather reserve could click the weather launcher and receive the existing final-preflight rejection.

The cost display also made the visible quote appear complete even though the launch required an additional caller payment.

After, that launcher is blocked until both the dynamic Charter commitment and the  Event 013 caller reserve are affordable.

Weather actions show the added reserve in normal text when affordable and red text when unavailable.

Non-weather matrix actions keep their former availability and cost display.

## Decision category lifecycle notes

The host-only Charter Council owns the selected action, selected target, quote, capacity reservation, active action record, and four duration-band missions.

The weather selectors only choose action IDs 69 and 70.

The shared launcher requotes against the exact target, reserves the caller cost, pays the host quote, creates one target action record, and activates the matching duration band.

`africa_cleanup_action` removes the active mission, target arrays, state markers, capacity reservations, weather reservation flags, member active state, and global Event 013 actor and target pointers.

## Mission and natural-disaster quality notes

The four shared missions are generation-gated, have separate cancellation handling, and resolve through the common idempotent cleanup path.

Rain and drought use an exact hostile target, require an active war, revalidate caller reserve and target validity at launch, apply a 180-day caller cooldown after the Event 013 bridge, and preserve the existing acceptance, rejection, and backfire outcomes.

Priority-member AI uses the same explicit enemy roster and shared action ledger as the player path.

No new free-unit, equipment-farming, target-substitution, cooldown-bypass, or stale-global-target path was introduced.

## Remaining issues and design gaps

- Medium, pre-existing: the shared matrix still uses four duration-band missions rather than a per-action objective system. The existing handoff documents the engine constraint around scoped targeted-mission duration values.
- Major, pre-existing and out of scope: `weaponise_fictional_pathogen` and the three strange-formation actions remain hidden behind missing authorisation or model-package gates. Enabling them requires an accepted design tranche, not a decision-audit patch.
- No decision-owned GUI source was changed. No GUI inspection or render artifact was required for this bounded non-GUI patch.

## Meaningful validation

Static assertions confirmed:

- both launchers invoke the full-commitment helper for availability and custom cost state;
- the weather reserve variables reset with the quote and load from the existing script constants only for Rain and Drought;
- only those two action IDs route through the Event 013 reserve gate;
- normal and blocked localisation both resolve dedicated dynamic reserve strings; and
- the modified English localisation retains UTF-8 BOM.

`git diff --check` found no patch-specific formatting error.

## Skipped validation

No Hearts of Iron IV launch or live-session test was run because in-game validation belongs to the user.

The relevant live cases are a host one unit below the Event 013 reserve, exact-reserve affordability, and a non-weather action with the same quoted resources.

No commit was created because the shared worktree contains concurrent Event 012 and unrelated edits; the parent should review and commit this bounded change with its own tranche.
