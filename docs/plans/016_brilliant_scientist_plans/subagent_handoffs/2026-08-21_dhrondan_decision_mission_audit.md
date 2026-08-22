# Event 016 D’Rhondan decision and mission audit — 2026-08-21

## Scope and result

This audit covers the current shared-state versions of `common/decisions/016_dhrondan_contact_decisions.txt`, `common/decisions/categories/016_dhrondan_contact_category.txt`, `common/scripted_triggers/016_dhrondan_contact_triggers.txt`, `common/scripted_effects/016_dhrondan_contact_effects.txt`, `common/script_constants/016_dhrondan_contact_constants.txt`, and `localisation/english/016_dhrondan_contact_l_english.yml` against the binding Event 016 addendum and acceptance scenarios.

No gameplay or localisation files were patched by this audit.

The current source has no confirmed P0/P1 gameplay defect in the owned tranche, and the latest shared corrections are present: pact success does not reset arrival, presence, or strain; the rebellion pulse is refreshed after the contact API call; the future-craft route flag is distinct from the future-contact API; and the rebellion caller does not pre-set the bridge receipt while a failed DHR transaction clears the unresolved trigger and refreshes the country pulse.

## Severity-sorted findings

### MEDIUM — required MCP evidence is blocked

The installed `hoi4-agent-tools` probability route was attempted with the decision source path and timed out with `tool call failed for hoi4_agent_tools/hoi4.probability_inspect: timed out awaiting tools/call after 180s`.

The mandatory decision-category `hoi4.gui_inspect` route was attempted with pre-pact, expedition, pact, and pulse scenarios and timed out with `tool call failed for hoi4_agent_tools/hoi4.gui_inspect: timed out awaiting tools/call after 180s`.

The mandatory `hoi4.gui_render` route was attempted for normal, active, warning, disabled, long-text, and missing-localisation states at 1280x720 and 1920x1080 and timed out with `tool call failed for hoi4_agent_tools/hoi4.gui_render: timed out awaiting tools/call after 180s`.

No dedicated callable `hoi4.decision_inspect` route was exposed in the installed tool surface.

These are evidence blockers, not source-equivalent validation; the parent must retain them as unresolved MCP acceptance blockers.

### LOW — secondary prose repeats spendable costs as literal resource names

The automatic decision `cost` fields are icon-backed, and `dhrondan_expedition_fuel_cost_tt` uses `£fuel_texticon`, but the player-facing descriptions at lines 12, 14, and 25 of `localisation/english/016_dhrondan_contact_l_english.yml` spell out `Political Power` and `fuel` as prose, and `chaosx.nr16.40.a.tt` repeats the same literal cost in its event tooltip.

If the repository icon-first rule applies to descriptive cost prose as well as dedicated cost keys, replace those repeated cost phrases with `£pol_power` and `£fuel_texticon` values or point them at a shared icon-first localisation key.

This was not patched because the event tooltip is outside the owned decision files and the regular decision cost renderer already supplies the PP icon.

### INFO — out-of-scope API localisation remains an external follow-up

The shared landing API still has a reserve-cost string that spells out `Alien Laser Weapons` without its equipment texticon, but it is API-owned and explicitly out of scope for this audit.

## Contract audit

The Kruger and Mengele decisions each use exactly 50 political power through their `cost` field, gate and consume exactly 500 fuel, and assign the shared 180-day mission variable before activation.

Kruger suspension uses the canonical `dhrondan_kruger_expedition_obligation`, transaction lock, and `brilliant_scientist_remove_kruger_roles` helper, while restoration clears only that obligation and re-adds roles through the canonical helper when the character is still the active, uninjured, unconfined host token.

Kruger cancellation and invalid-transfer paths route through `dhrondan_fail_expedition` and `dhrondan_clear_expedition_state`, with no contact receipt, pact, or return Directorate delta on failure.

The Mengele route sets only its own expedition flags and does not call Kruger Directorate mutation helpers.

The pact success path applies the route-specific receipt and Directorate return where applicable, calls `alien_infantry_grant_contact`, refreshes the rebellion pulse, and then clears expedition state without resetting arrival count, Alien Presence, or Pact Strain.

Honor the D’Rhondan Accord costs exactly 75 political power, subtracts exactly 10 Pact Strain with a zero clamp, and applies a 180-day country cooldown.

The compact status header exposes Alien Presence and Pact Strain in one decision row with a concise explanatory description, and the category has no scripted GUI or global scan.

The rebellion pulse requires the pact, at least six arrivals, Pact Strain at least 30, shared chaos at least 600, and no world-end state, then activates one country-scoped 90-day mission.

The random-list weights total 100 and resolve to 10, 20, or 40 percent revolt probability: the high tier is at least ten arrivals with chaos at least 800; the medium tier is exactly eight or nine arrivals, or strain at least 50, or chaos at least 800, with the high tier checked first; all remaining eligible cases are 10 percent.

The parent-locked boundary is therefore preserved: ten or more arrivals with chaos 600–799 and strain 30–49 remain at 10 percent, while chaos at least 800 promotes the result to the 40-percent high tier.

There is no `on_daily`, `on_weekly`, or `on_monthly` world iteration in the owned contact files.

## Lifecycle, cognitive load, and mission quality

Before the pact, the category exposes at most two route actions, and after the pact it exposes the status row and one Honor action; route missions are mutually exclusive and the rebellion pulse is the only additional country mission.

Every owned visible value has a stated meaning and consequence in the status description or mission/event text, although the header has no graphical meter or explicit threshold marker because the current design intentionally uses a compact ordinary decision row.

The route missions have a named owner (Kruger or the Mengele Directorate), a single country category, no map region target, a 180-day requirement window, explicit success through the audience/pact event, and explicit failure through cancellation or timeout invalidation.

The pulse mission is country-owned, has no region target, runs for 90 days, resolves through the bounded random list, and renews only while its eligibility trigger remains true.

The mutually exclusive expedition flags, pact guard, one-time Directorate delta flags, contact receipts, rebellion trigger, bridge-called guard, and cooldown flag prevent duplicate route grants, repeated return deltas, repeated bridge transactions, and Honor spam.

## AI, route validity, and localisation notes

The two visible authorization decisions use the effectively dominant `dhrondan_contact_ai.dominant` value of 10000 and repeat the same route and fuel checks used by their completion effects.

The Event .40 AI path checks political power, fuel, and at least one valid route, debits the exact political-power cost once, prefers a valid Kruger route, and otherwise takes the valid Mengele route.

Honor uses the low baseline and a fourfold strained modifier, reaching an effective 100 weight at high strain while remaining a support action rather than an authorization route.

The dedicated expedition tooltip uses the fuel texticon, and the regular `cost` fields supply the PP icon through the decision engine; the low-severity prose duplication finding above is the remaining icon-first gap.

## Recommended follow-up

Retain the three MCP timeout records above in the parent completion packet and rerun probability inspection/evaluation and GUI inspect/render when the server transport is available.

Optionally normalize the secondary cost prose to icon-first localisation, keeping the exact 50 PP, 500 fuel, 75 PP, 180-day, and 10-strain values unchanged.

No plan handoff was created because the owned decision and mission contract is implemented and the only actionable source-level item is a narrow localisation cleanup.

## Changed files

None.

## Remaining uncertainty

No live gameplay or engine-backed MCP evidence was available in this audit because the required routes timed out, so mission visual lifecycle, rendered density, and probability adapter fidelity remain unverified rather than passed by source inspection.

## Cross-host lifecycle recheck

The current `dhrondan_apply_kruger_authorization_directorate_changes` effect treats `KRG_warren_kruger` character flag `dhrondan_kruger_authorization_reward_received` as authoritative, writes the country mirror `dhrondan_kruger_authorization_changes_applied`, and applies the Directorate deltas only when the character flag is absent.

The current `dhrondan_apply_kruger_return_directorate_changes` effect follows the same pattern for character flag `dhrondan_kruger_return_reward_received` and country mirror `dhrondan_kruger_return_changes_applied`, so a retry on a later host cannot repeat either reward.

The Kruger availability trigger now gates on character flag `dhrondan_kruger_pact_completed` in addition to the route and host checks, so a successful pact blocks later-host expedition replay even if a country-scoped mirror is not present on that later host.

The successful Kruger authorizer sets `dhrondan_kruger_pact_completed` on the canonical character and writes the country-scoped contact receipt before clearing expedition state; this is the correct persistent-character versus host-mirror split.

A failed pre-pact transfer does not clear the three character reward flags, and the authorization/return helpers re-establish the destination country mirrors without reapplying prior deltas, so the intended retry is idempotent.

### Conditional medium-risk defect

`dhrondan_authorize_pact_and_return` currently validates only the expedition and audience flags in its outer limit and does not re-check `dhrondan_kruger_expedition_remains_valid` or `has_character = KRG_warren_kruger` immediately before the Kruger return reward and pact marker are written.

The normal mission timeout path has already checked route validity, and the broader transfer cleanup is expected to invalidate and clear stale expedition state, so this is not proven to be exploitable from the owned files alone.

However, if an audience event survives a cross-host transfer or canonical-character loss without that external cleanup, the return reward helper can skip its delta while the subsequent character-scoped pact assignment may not write, leaving a country pact without the persistent character pact marker and allowing a later-host replay.

Recommended narrow hardening is to make the authorizer’s route selection require `dhrondan_kruger_expedition_remains_valid = yes` for the Kruger branch and `dhrondan_mengele_expedition_remains_valid = yes` for the Mengele branch before any pact flag, receipt, or API grant is applied; no patch was made in this recheck.

No other cross-host reward duplication or replay defect was found in the current contact effects/triggers.
