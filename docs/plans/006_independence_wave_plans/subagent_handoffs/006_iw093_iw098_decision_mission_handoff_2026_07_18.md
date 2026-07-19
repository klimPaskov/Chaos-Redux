# Event 006 IW-093 / IW-098 decision and mission handoff

## Scope completed

Implemented the bounded Asante (IW-093) and Sokoto (IW-098) signature
decision categories from the accepted improvement addendum. This gameplay
tranche introduced stable sprite identifiers but no advisor, portrait, or
content-attestation surface. The matching static icon package was subsequently
produced and wired by the parent.

## Changed files

- `common/decisions/categories/006_independence_wave_iw093_iw098_categories.txt`
- `common/decisions/006_independence_wave_iw093_iw098_decisions.txt`
- `common/ideas/006_independence_wave_iw093_iw098_ideas.txt`
- `common/scripted_effects/006_independence_wave_iw093_iw098_decision_effects.txt`
- `common/scripted_effects/006_independence_wave_iw093_iw098_decision_effects.md`
- `localisation/english/006_independence_wave_iw093_iw098_categories_l_english.yml`
- `localisation/english/006_independence_wave_iw093_iw098_decisions_l_english.yml`
- `localisation/english/006_independence_wave_iw093_iw098_ideas_l_english.yml`

The package-effects owner also integrated the required initialization, final
idea validation, and cleanup helper calls in
`common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt`.

## Decision and mission identifiers

| Package | Category | Timed actions |
| --- | --- | --- |
| IW-093 | `independence_wave_iw093_asante_compact_category` | `train_forest_guard`; `royal_confederacy_conference`; `constitutional_cabinet_conference`; `veterans_emergency_conference`; `rebuild_cocoa_depots`; `relay_kumasi_railway`; `negotiate_host_settlement`; `prepare_form24_congress` |
| IW-098 | `independence_wave_iw098_sokoto_compact_category` | `reorganize_cavalry_screen`; `sultanic_federal_compact`; `northern_constitution_compact`; `frontier_command_compact`; `secure_caravan_wells`; `open_livestock_market`; `negotiate_native_administration`; `prepare_form25_congress` |

The staged ideas are `independence_wave_iw093_unsettled_restoration_idea`,
`independence_wave_iw093_cocoa_rail_compact_idea`,
`independence_wave_iw098_disputed_emirate_compact_idea`, and
`independence_wave_iw098_caravan_network_compact_idea`.

## Behaviour before and after

Before this tranche, IW-093 and IW-098 had package foundations and visible
values but no category, paid project lifecycle, force-upgrade receipt, route
choice, project construction, or host-settlement decision surface.

After it:

- Forest Guard and cavalry-screen actions pay concrete command and equipment
  bundles over 90 days, issue a one-time upgrade receipt, and never create a
  unit or award equipment.
- Each package has a 70-day, 100-political-power route conference. The Asante
  veterans and Sokoto frontier-command emergency choices require severe host
  threat and lock their founding-congress path. Royal/cabinet and
  sultanic/constitutional routes move the specified balance values.
- Asante cocoa depots then Kumasi rail are staged 120-day, 500-rifle,
  two-civilian-factory projects. Sokoto caravan wells then livestock market
  are staged 90/120-day, 500-rifle/350-support-equipment,
  two-civilian-factory projects. Map construction occurs only after the paid
  ledger has closed and the anchor remains owned and controlled.
- Host settlements spend command and trains, fail or cancel under severe host
  threat, and record a receipt. FORM-24/FORM-25 preparation then requires the
  relevant route-aware helper, the receipt, material cost, and 90-day mission;
  it prepares but does not execute a formable.
- Every paid mission has active, success, failure, cancellation, and package
  cleanup paths. A single package transaction flag prevents overlapping paid
  operations; cancellation and failure never refund a spent ledger.

## Audit notes

### Issues, sorted by severity

1. **P1 — focus unlock ownership remains outside this tranche.** These
   categories are package-active surfaces because no accepted IW-093/IW-098
   focus identifiers were supplied to this subagent. The focus owner should
   attach any intended focus-gated reveal or reward hooks without weakening
   the exact package and route checks.
2. **Resolved after handoff — stable sprite ids.** The category, decision, and
   idea ids retain their final names. The reviewed
   `docs/assets/006_independence_wave/iw093_iw098_icons_2026_07_18/` package and
   four matching interface files now register every referenced icon.
3. **P2 — no force binding helper was supplied.** The 90-day guard/cavalry
   actions issue durable upgrade receipts and do not manufacture replacement
   units. A future existing-force package may consume those receipts; this
   tranche does not introduce a force system merely to do so.

### Category lifecycle

Categories appear only for exact active IW-093/IW-098 scopes. Their opening
ideas are installed safely during prepared setup, validated after activation,
swap only when both reconstruction stages complete, and are removed with every
decision receipt, flag, ledger, and active mission on package cleanup.

### Mission quality

| Owner | Category | Region | Requirement | Duration | Success / failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| IW-093 | Asante Compact | Kumasi, state 274 | exact package; anchor control; paid bundle; route/settlement where relevant | 70/90/120 days | map and package-value receipts on success; state/threat/route failures reduce values and retain costs | one transaction flag plus permanent receipts/failure flags |
| IW-098 | Sokoto Compact | Sokoto, state 902 | exact package; anchor control; paid bundle; route/settlement where relevant | 70/90/120 days | map and package-value receipts on success; state/threat/route failures reduce values and retain costs | one transaction flag plus permanent receipts/failure flags |

### Costs and requirements

Costs are not political-power stores. They are concrete political-power,
command-power, infantry/support equipment, trains, convoys, civilian-factory
occupancy, and elapsed-time commitments. Custom cost text states the resource
bundles, while custom trigger blocks keep raw checks out of player-facing
requirements. FORM preparation calls the centralized route/threshold helpers
and independently requires its completed host/administration receipt.

### AI, route locks, cleanup, and exploit risk

AI favors the appropriate court/cabinet or sultanic/civic route from balance
values, uses emergency options only under severe host threat, and prioritizes
network/throughput/settlement work below form thresholds. Emergency routes set
the terminal lock; FORM decisions use the centralized route-aware helpers.
All stale active flags, ledger variables, completion/failure/cancellation
records, ideas, and live decision instances are removed by package cleanup.
No country-target scan, free-unit loop, equipment grant, war-goal spam, core
grant, or repeatable material-reward loop was added.

### Localisation and tooltip gaps

All category, decision, idea, custom-cost, and custom-effect-tooltip keys used
by this tranche are present in UTF-8-with-BOM English localisation. No scripted
GUI surface exists, so no GUI inspect/render artifact is applicable.

## Meaningful validation

- Cross-checked every `custom_cost_text` and `custom_effect_tooltip` reference
  against the new decision localisation: no missing keys.
- Cross-checked every decision, category, and idea id against its name and
  description keys: no missing localisation.
- Verified brace parity in each new Clausewitz file, no unsupported `<=` or
  `>=` operator, and `git diff --check` for all owned files.
- Verified all three localisation files begin with UTF-8 BOM bytes `EF BB BF`.
- Counted six IW-093 and five IW-098 paid-ledger starts; reviewed the matching
  success, timeout, cancellation, and cleanup closures. Emergency conferences
  are the only non-ledger timed decisions because their 100 political-power
  cost is native decision cost; the Asante veterans route also uses the paid
  command ledger.
- Searched the owned gameplay files: no unit creation, positive stockpile
  grant, advisor/portrait/interface reference, or runtime-attestation setter.
  The sole stockpile effects use a temporary variable multiplied by `-1` to
  spend the stated equipment.

## Skipped meaningful validation

No live game load or GUI render was run. This package has no authored scripted
GUI, and a live test would require the parent-owned runtime attestation and
release path to be satisfied. Those are valid parent integration tests, not a
reason to add an unsafe fallback.

## Remaining integration work

- The focus owner should wire intended focus unlocks and confirm the category
  reveal order alongside its branch work.
- The reviewed icon package and parent interface wiring now own the stable
  sprite identifiers; this decision tranche remains free of advisor assets.
- The parent should exercise release, forced anchor-loss, severe-host-threat,
  and cleanup scenarios after all package foundations are assembled.
