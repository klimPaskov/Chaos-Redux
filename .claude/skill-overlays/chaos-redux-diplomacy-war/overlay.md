---
description: Use when scripting or auditing Chaos Redux diplomacy, factions, subjects and autonomy, wargoals, declarations of war, white peace or peace conferences, embargoes, opinion modifiers, condemnation and sanctions, Chaos Meter war hooks, annexation, release, or state transfer between countries.
---

### In Contents

- Chaos Redux specifics

### In Source map

Chaos Redux wording differs from the kit:

| Topic | Authoritative text | Vanilla precedent |
| --- | --- | --- |
| Rules, game-rule options | `WIKI/Autonomy state modding` rule table; `set_rule` / `has_rule` in the effects and triggers docs | |

### In Chaos Redux specifics

The `CLAUDE.md` coding, constants, and localisation rules apply and are not repeated here. Never add a world-iterating `on_daily`, `on_weekly`, or `on_monthly` diplomacy hook without permission; use the event-style on actions above or `on_daily_TAG`. (Chaos Redux wording differs from the kit)

**Shared systems that own diplomacy outcomes**

- **Condemnation and sanctions** (`docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md` is the source-of-truth map). Publicly known unconventional warfare and exposed atrocities register a condemnation source through the adapters named in that map, never through a new opinion or embargo script. The system converts the total into seven tiers, scores participants, creates native embargo relations, applies scalable penalties, and offers response decisions. Tuning is in `common/script_constants/condemnation_sanctions_constants.txt`, effects in `common/scripted_effects/condemnation_*.txt`, hooks in `common/on_actions/condemnation_sanctions_on_actions.txt`, and the targeted monthly pulse in `events/condemnation_sanctions_events.txt`. `common/scripted_triggers/zz_condemnation_diplomacy_overrides.txt` overrides vanilla lend-lease gates by load order; a new gate on lend-lease or similar diplomacy actions must respect it.
- **Chaos Meter war hook.** New war relations are counted from `on_war_relation_added` (`ROOT` attacker, `FROM` defender) by `chaos_meter_on_war_relation_added`, wired in `common/on_actions/chaosx_on_actions_chaos_meter.txt`. Faction follow-up relations against a defender an ally already fights are ignored, and minor declarations are capped per attacker per day by constants. Do not count wars in a second hook; change the shared handler (`docs/systems/chaos_meter/chaos_meter_war_declaration_counting.md`).
- **Liberation release coordinator.** Any release that creates or frees several countries at once (Events 5 and 6) plans, validates, and commits through `chaosx_liberation_release_*` (`docs/systems/liberation_release_coordinator.md`): reserve a protected state per host, freeze the allocation, revalidate it against the live map, and change ownership only after the whole plan passes. Ownership changes for those events go through it.
- Opinion modifiers are defined per owner in `common/opinion_modifiers/<owner>_opinion_modifiers.txt` (CBRN diplomacy, protection, biowarfare, air contamination, condemnation, camp partners). Wargoals, autonomy states, and peace conference modifiers exist only for the events that need them (`common/wargoals/`, `common/autonomous_states/`, `common/peace_conference/`).

**Rules that recur**

1. Validate every country you act on with an existence check; scope existence alone does not prove a dormant or annexed country is a legal actor, owner, or destination (`common/scripted_triggers/humanitarian_validation_triggers.md`).
2. Special Chaos countries are excluded from the humanitarian systems (`humanitarian_country_is_valid`); test that exclusion before treating one as a refugee host, aid donor, or sanction participant.
3. A diplomatic outcome that moves population or states fixes the physical transfer first; see `chaos-redux-map-states` for the transfer contract.
4. AI behaviour around these systems follows `chaos-redux-ai-strategies`. (Chaos Redux wording differs from the kit)
