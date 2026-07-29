# Event 006 rival bloc contract handoff

## Scope completed

Implemented the accepted post-expulsion rival-bloc boundary as a separate, generation-safe registry contract. The existing Event 006 league remains registry-driven; no vanilla faction was introduced.

## Files changed by this subagent

- `common/script_constants/006_independence_wave_rival_bloc_constants.txt`
- `common/scripted_triggers/006_independence_wave_rival_bloc_triggers.txt`
- `common/scripted_effects/006_independence_wave_rival_bloc_effects.txt`
- `common/scripted_effects/006_independence_wave_effects.txt` (narrow call-site guards, expulsion opening, crisis/split pending transition, reunification call, and origin/network cleanup hook)
- `common/decisions/categories/006_independence_wave_rival_bloc_categories.txt`
- `common/decisions/006_independence_wave_rival_bloc_decisions.txt`
- `common/scripted_localisation/006_independence_wave_rival_bloc_scripted_localisation.txt`
- `localisation/english/006_independence_wave_rival_bloc_l_english.yml` (UTF-8 BOM)
- `common/ai_strategy/006_independence_wave_rival_bloc.txt`
- `docs/events/006_independence_wave/systems/rival_bloc.md`

## Identifiers and behavior

- Contract globals: `global.independence_wave_rival_bloc_contract_generation`, route, five values, host pressure, member/region counts, leader pointer, active/rivalry/invitation flags, and pending invitation target.
- Aligned member arrays: country, origin generation, contract generation, region, contribution, confidence.
- Triggers: `is_independence_wave_rival_bloc_active`, `is_independence_wave_rival_bloc_member`, `is_independence_wave_rival_bloc_leader`, `is_valid_independence_wave_rival_bloc_invitation_target`, pending invitation, host/patron pressure, leadership candidate, and all seven cost gates.
- Actions: invite, accept, decline, reserve commitment/failure, host-front coordination, patron balancing, leadership challenge, and leave.
- Lifecycle: expelled member opens generation and becomes leader; stale/dead rows are pruned; leader replacement chooses highest-confidence survivor; empty contracts clear arrays, flags, variables, and event targets; formal-league reunification copies rows before mutating them.
- Main league call sites reject rival members in founder/member reconcile/register paths so a country cannot occupy both ledgers accidentally.

## Meaningful validation performed

- Balanced-brace source audit for all new script files.
- Repository-wide helper-definition/reference audit for new rival helper names.
- Constant-reference audit against the new shared constants file and existing Event 006 constants.
- Checked that the new files contain no `on_daily`, `on_weekly`, `on_monthly`, or other world-iterating action.
- Verified localisation begins with the UTF-8 BOM bytes `239,187,191`.
- Read the required offline Paradox wiki pages and vanilla documentation for arrays, event targets, effects/triggers, decisions, missions, scripted localisation, and cost syntax before editing.

## Known limitations / follow-up

- The existing Event Details UI does not yet render the rival arrays; the new global names are documented for a later narrow UI surface.
- Invitation acceptance is a country decision rather than a response event, which keeps the lifecycle deterministic and generation-checked without adding an event asset.
- Patron balancing lowers the rival contract's capture value and refreshes the member's existing patron ledger; it does not invent a second patron ledger.
- The parent agent should update the stale Event 006 event documentation sentence that still describes rival-bloc creation as unresolved, and should review any concurrent edits in `common/scripted_effects/006_independence_wave_effects.md` before final commit.
