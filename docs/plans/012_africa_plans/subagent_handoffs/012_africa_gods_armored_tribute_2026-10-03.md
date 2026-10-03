# Event 012 armoured tribute

Disposition: implemented and reviewed in source; live transaction acceptance remains pending.
Acceptance basis: the user's active complete Gods goal and accepted full specification `012_gods_of_africa_full_spec.md:442-446` require actual tanks, an Evolution II or proven-need entry, and quotes based on actual stock and production.
The reserve and quote fractions are parent implementation choices within that authorized scope, centralized in `gods_of_africa_armor`.
No design simplification or motorized substitute is accepted for this family.

## Implementation

The host's `gods_of_africa_armor_needed` flag is recomputed from aggregate chassis stock and actual army shortfall.
Evolution II adds a 100-unit reserve target; before Evolution II, only a proven unfilled army requirement opens the lane.
Automatic selection follows emergency/fuel needs and precedes manpower, industry, and later material lanes, while the existing meaningful host priority remains first.
A participant must have at least five spare tanks before this family can be selected.

For each light, medium, heavy, modern, super-heavy, or amphibious chassis, the operating reserve is the larger of 25 and the army reinforcement shortfall plus 10% of the army target.
Negative surplus is zero, and fractional surplus is rounded down with documented modulo arithmetic.
The base quote is 10% of total spare tanks plus 1% of actual cumulative armoured production.
Its ceiling is 25% of spare stock, bounded to five through 300 tanks when five tanks are transferable.
The five-unit minimum may consume a larger share of very small spare stocks, while preserving every chassis's operating reserve.
Existing demand multipliers apply before the quote is bounded to that ceiling and rounded down.
The production input is historical actual output, not a forecast or a claim about active production lines.

The payment dispatcher uses native `send_equipment` in up to six slices, remeasuring each chassis before delivery.
It does not convert a tank payment into trucks or manufacture recipient variants.
Each slice sends only the smaller of the remaining payment and that chassis's spare amount.
Full, partial, and substitute affordability use the same live capacity helper.
A five-tank contract's partial shipment is two tanks, leaving three due.
Temporary outputs needed after nested helper calls are initialized by their caller.
Normal quote fields are cleared after demand preparation and again by demand cleanup; the host need flag is cleared on unifier loss.

## Changed surfaces

- `common/scripted_effects/012_africa_gods_equipment_effects.txt` and its adjacent contract Markdown: quote, whole-unit arithmetic, and native shipment slices.
- `common/scripted_triggers/012_africa_gods_equipment_triggers.txt`: per-chassis reserve and live inclusive capacity.
- `common/scripted_effects/012_africa_gods_effects.txt`: host need, automatic selection, scaled quote, integer partial amount, payment dispatch, and cleanup.
- `common/scripted_triggers/012_africa_gods_triggers.txt`: full, substitute, and partial armour affordability, removing the truck alias and duplicate branch.
- `common/script_constants/012_africa_gods_constants.txt`: all armour tuning.
- `common/scripted_localisation/012_africa_gods_scripted_localisation.txt` and English localisation: tank cost icons, capacity requirement, and accurate partial-payment wording.
- Canonical Gods guide and this handoff: implementation and evidence limits.
- `common/scripted_effects/chaosx_dynamic_effects.md`: a bounded link to the owner helper contract, preserving concurrent documentation edits.

No equipment definition, enum type, independent event, additional player value, country iteration, clock, or paid decision was added.
The existing Event 012 CXT extension remains the subsystem registration; this tranche uses installed vanilla equipment.
The medium-tank text icon is reused from vanilla `interface/texticons.gfx:2167-2172`; no new art is required.
Catalog public Event Details and evolution fields were not changed, so no workbook edit or export is required for this tranche.

## Source scenarios

| Case | Result implied by the source contract |
| --- | --- |
| No tanks, even with a large production history | Spare stock is zero, so armour cannot be selected or paid. |
| Host before Evolution II, no army shortfall | No reserve-only tank demand. |
| Host before Evolution II, 100 missing tanks and no stock | Proven need opens the lane. |
| Host after Evolution II, 99 stock and no shortfall | The 100-unit reserve need opens the lane; at 100 it closes. |
| Sender has 200 light tanks, target 1,000 and fielded 900 | Reserve is 200; light chassis contributes no spare tanks. |
| Sender also has 300 medium tanks, target/fielded 500, and has produced 2,000 armour | Medium reserve is 50, spare total 250, base quote 45, and ceiling 62 whole tanks. |
| The 45-unit quote is partially paid | 22 tanks transfer, 23 remain due, and the running timer is preserved. |
| Sender's army need grows before a click | Every payment rechecks the larger reserve and blocks before a debit if spare capacity has disappeared. |
| Several chassis have spare stock | All slices count toward one fixed amount and each retains its own reserve. |
| Quote generation fails or demand is cleared | Both hidden quote fields are cleared; no stale quote becomes a later demand. |

These are source scenario reviews, not observed native execution.
No AI weight or probability multiplier was changed.
Current decision AI continues to use the shared affordability predicates; full weighted scenario acceptance remains open.

## References and route evidence

Exact references and the vanilla/native field discrepancy are recorded in `common/scripted_effects/012_africa_gods_equipment_effects.md`.
Installed documentation is read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`; offline wiki is read from the repository's `paradox_wiki/`.
`reference_context` with a bounded event question timed out after 600 seconds.
The initial `num_equipment` reference search timed out, and the narrower retry used the exact example `num_equipment@infantry_equipment`, `sources = [game_doc]`, and limit one; it also timed out after 600 seconds.
The revision-bound dynamic-variable read timed out after 600 seconds, so the pertinent local sections were read directly.
No online Paradox wiki or live game was opened.
The `.603` narrow trace from the timer tranche is direct source evidence only and does not expand these new helpers.
The parent requested a matching four-node `.603` options render and a four-node selected-chain comparison from revision `e9e470262f1ea057b06851d06c768e7e69517688395c2427a2d534af5005edff`; both results are pending at commit preparation, and neither is counted as armour lifecycle validation.
The Systems Architect's dedicated audit at `012_africa_gods_armor_architecture_audit_2026-10-03.md` re-read the integer-operation and partial-payment corrections and found no outstanding source-level must-fix in its reviewed snapshot.
The parent additionally reviewed the later selector guard that requires a real candidate before fallback, preventing an armour-only need from manufacturing a financial relief quote for a country with no transferable tanks.
The specialist records moving-source hashes and does not claim that the entire later main-effects revision received an independent second audit.
The installed tool list exposes no `script_validate`, health/version endpoint, or confirmed task negotiation, so no helper-expansion task or undocumented validation route was invoked.

The supplied cycle-one menu-load error log predates these armour changes and does not establish their runtime behavior or a clean full build.
The full goal remains incomplete, including mobile/artillery coverage, raw visible flag requirements, detailed outcome reports, weighted scenarios, owner lifecycle, and live native transfer evidence.
Skills used: events, decisions/missions, subagents, and shared Git commit.
