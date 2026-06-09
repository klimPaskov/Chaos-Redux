# Event 006 Patron Ledger Cost Patch Audit Handoff

Date/time: 2026-05-30T08:47:12Z

Scope: bounded audit of the Event 006 Patron Ledger cost patch. I did not edit flags, flag assets, country flag files, or any visual assets.

## Changed Files

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`

## Audited Parent Files

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`

## Findings By Severity

- Medium, fixed: several new Patron Ledger resource checks used strict `>` gates against the exact spend amount. This could block a country with exactly the advertised resource amount, most visibly the `15` command power reward from local defense brigades against the `15` command power broker exposure spend.
- Low, not patched: the six cost tooltips are present and player-facing, but they describe the resource type rather than showing icon-first numeric values. This is readable enough for the current patch, but a later dynamic cost localisation pass would make the ledger clearer.
- No high-severity issues found in the bounded Patron Ledger cost pass.

## Patched IDs

Constants added:

- `independence_wave_decision.patron_advisers_army_xp_gate`
- `independence_wave_decision.patron_expose_broker_command_power_gate`
- `independence_wave_decision.patron_arms_corridor_infantry_equipment_gate`
- `independence_wave_decision.patron_arms_corridor_support_equipment_gate`

Triggers adjusted:

- `can_independence_wave_accept_patron_advisers`
- `can_independence_wave_balance_rival_patrons`
- `can_independence_wave_expose_foreign_broker`
- `can_independence_wave_reject_dependency_clauses`
- `can_independence_wave_request_arms_corridor`
- `can_independence_wave_convert_loans_to_treaty_debt`

## Before And After Behavior

Before:

- Army XP, command power, equipment, coalition cohesion, and legitimacy checks could require strictly more than the amount spent.
- Variable checks for cohesion and legitimacy used `compare = greater_than`.
- Army XP, command power, and equipment checks used strict `>` against the spend constants.

After:

- Variable checks for cohesion and legitimacy use `compare = greater_than_or_equals`, matching the spend amount.
- Army XP, command power, infantry equipment, and support equipment checks use dedicated gate constants just below the spend amount, because those trigger forms do not use `greater_than_or_equals`.
- The actual resource spends and rewards are unchanged.

## Decision Category Lifecycle Notes

- `independence_wave_patron_ledger_category` remains visible only when `can_independence_wave_open_patron_ledger` is true.
- The ledger opens from patron cabinet route, port ledger, balanced sponsors, anti-puppet proof, or patron leverage pressure.
- Each of the six Patron Ledger actions keeps a one-use country flag and the shared `independence_wave_patron_ledger_cooldown`.
- No hidden decision without reveal logic was found in this bounded surface.

## Mission Quality Notes

No Patron Ledger timed missions are part of this patch. The audited surface contains clickable decisions only.

## Cost And Requirement Clarity Notes

- All six Patron Ledger decisions retain PP decision costs plus the new varied resource/institutional requirements.
- All six decisions have custom requirement tooltip keys in localisation.
- All six decisions have custom effect tooltip cost keys in localisation.
- The current cost keys are player-facing prose. They do not yet show numeric icon-first costs.

## AI Validity And Route-Lock Notes

- AI weights remain route-aware for patron cabinet, balanced sponsors, war state, anti-puppet proof, civic, revolutionary, and national routes.
- No invalid country target or dead target issue was found in the six Patron Ledger decisions because they are non-targeted country decisions.
- Route gates appear reachable from existing Event 006 startup and focus paths:
  - `independence_wave_barracks_count` gives enough army XP for advisers.
  - startup equipment and depot/military support rewards cover the arms corridor costs.
  - congress/permanent delegation/cohesion rewards can fund cohesion spends.
  - local defense brigades and normal command power accumulation can fund broker exposure; the exact-15 command power edge is fixed.

## Localisation And Tooltip Gaps

- `localisation/english/006_independence_wave_l_english.yml` is UTF-8 with BOM.
- No `:0` key style was found in the audited Event 006 localisation file.
- The six Patron Ledger requirement and cost tooltip keys are present.

## Cleanup And Exploit-Risk Notes

- The ledger still uses one-use flags and the shared cooldown, so no obvious repeated free-unit/equipment farming loop was introduced by the cost patch.
- `independence_wave_request_arms_corridor_effect` spends corridor guard equipment before adding patron stockpiles; the decision is one-use and cooldown-gated.
- No stale-target cleanup issue was found in the bounded Patron Ledger cost changes.

## Validation Commands And Results

- `rg -n "<=|>=" common/script_constants/006_independence_wave_constants.txt common/scripted_triggers/006_independence_wave_triggers.txt common/scripted_effects/006_independence_wave_effects.txt common/decisions/006_independence_wave_decisions.txt localisation/english/006_independence_wave_l_english.yml docs/events/006_independence_wave.md || true`
  - Result: no unsupported `<=` or `>=` operators found.
- `for f in common/script_constants/006_independence_wave_constants.txt common/scripted_triggers/006_independence_wave_triggers.txt common/scripted_effects/006_independence_wave_effects.txt common/decisions/006_independence_wave_decisions.txt; do printf '%s ' "$f"; awk 'BEGIN{b=0} {for(i=1;i<=length($0);i++){c=substr($0,i,1); if(c=="{") b++; else if(c=="}") b--}} END{print b}' "$f"; done`
  - Result: all four script files reported brace balance `0`.
- `file localisation/english/006_independence_wave_l_english.yml && xxd -l 8 localisation/english/006_independence_wave_l_english.yml`
  - Result: file reports UTF-8 with BOM; first bytes are `ef bb bf`.
- `rg -n "^[^#\\s][^:]*:0\\s|^\\s+[^#\\s].*:" localisation/english/006_independence_wave_l_english.yml | head -40`
  - Result: no bad `:0` keys or leading-space keys found.
- `rg -n "independence_wave_(accept_patron_advisers|balance_rival_patrons|expose_foreign_broker|reject_dependency_clauses|request_arms_corridor|convert_loans_to_treaty_debt)_(requirements|cost)_tt" localisation/english/006_independence_wave_l_english.yml`
  - Result: all twelve requirement/cost tooltip keys found.

## Skipped Validation

- No in-game load was run from this subagent session.
- No full repository parser exists in the repo for Clausewitz syntax; validation was limited to targeted static checks and vanilla documentation/precedent review.

## Remaining Risks

- Exact resource matching is now fixed for this cost pass, but the cost text still omits numeric icon-first values.
- Because the Event 006 files are currently untracked/dirty in the parent worktree, Git cannot show a normal tracked-file diff for all audited parent files.
