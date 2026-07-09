# Event 018 Public Repo Exploration Handoff

Working label only, not final localisation.

This handoff replaces the earlier unverified repo handoff with a public GitHub source pass. It is not a substitute for local implementation exploration. The local Windows repository, offline Paradox wiki snapshot, vanilla HOI4 documentation, and custom Codex subagent runner were not mounted in this sandbox. The implementation agent must still repeat the local `AGENTS.md`, offline wiki, vanilla documentation, and vanilla pattern pass before editing.

## Confirmation level

| Item | Confirmation |
| --- | --- |
| Public repository | Confirmed through the public `klimPaskov/Chaos-Redux` GitHub repository on 2026-07-07. |
| Local working tree | Not mounted here. Local branch state may differ from public GitHub. |
| Offline Paradox wiki | Not mounted here. Required before implementation. |
| Vanilla HOI4 docs and files | Not mounted here. Required before implementation. |
| Custom Codex subagents | No runner exposed here. Their TOML instructions were read and carried into prompts. |
| Event catalog workbook | Not mounted here. CSV catalog extracts were read. Workbook update remains blocked until final in-game localisation exists. |

## Current public repo facts

- The current event file is `events/018_random_resource.txt` and uses namespace `chaosx.nr18`.
- The current player-facing event is `chaosx.nr18.2`, with picture `GFX_report_event_random_resource`.
- The current old implementation chooses a random owned controlled state and uses an equal random list of oil, steel, tungsten, chromium, aluminium, and rubber.
- The current old implementation adds `amount = 200` for the selected resource. The canonical rework must not copy that value as the baseline. The user baseline remains around 100 of one random resource. Higher values belong to exploitation, repeated discoveries, or evolved openings.
- The current localisation file is tiny and includes an empty description for `chaosx.nr18.2.d`.
- The random event system still registers Event 18 as a repeatable event.
- Public repo folder listings show existing event-specific decisions and decision categories for other events, but no public `018_resources_found_decisions.txt` or matching category file was visible in the GitHub folder listing during this pass.
- Event 29 is `029_riches_found.txt`. Do not merge Event 18 into Event 29 or reuse that identity without explicit user approval.

## Source URLs inspected

| Source | Use |
| --- | --- |
| `https://github.com/klimPaskov/Chaos-Redux/tree/master/events` | Confirmed `018_random_resource.txt` and separate `029_riches_found.txt`. |
| `https://github.com/klimPaskov/Chaos-Redux/blob/master/events/018_random_resource.txt` | Confirmed current namespace, popup, resource random list, old amount, and news follow-up. |
| `https://github.com/klimPaskov/Chaos-Redux/blob/master/localisation/english/018_random_resource_l_english.yml` | Confirmed minimal existing localisation and empty event description. |
| `https://github.com/klimPaskov/Chaos-Redux/blob/master/common/scripted_effects/chaosx_logic_effects.txt` | Confirmed Event 18 is still in `global.repeatable_events`. |
| `https://github.com/klimPaskov/Chaos-Redux/tree/master/common` | Confirmed broad file surface folders. |
| `https://github.com/klimPaskov/Chaos-Redux/tree/master/common/decisions` | Confirmed current event decision-file pattern and lack of visible Event 18 decision file in the folder listing. |
| `https://github.com/klimPaskov/Chaos-Redux/tree/master/common/decisions/categories` | Confirmed current event category-file pattern and lack of visible Event 18 category file in the folder listing. |
| `https://github.com/klimPaskov/Chaos-Redux/blob/master/common/scripted_triggers/chaosx_dynamic_triggers.txt` | Confirmed shared special and nonhuman country classification trigger surface. |
| `https://github.com/klimPaskov/Chaos-Redux/blob/master/common/scripted_effects/chaosx_dynamic_effects.txt` | Confirmed shared world-threat refresh surface and population modification helper. |

## Likely edit surfaces for the implementation agent

| Path | Role in Event 018 rework | Implementation note |
| --- | --- | --- |
| `events/018_random_resource.txt` | Existing event entry point and current popup. | Prefer reworking this file to preserve stable event ids unless the local repo already renamed it. Keep `chaosx.nr18` unless a repo-wide migration is explicitly done. |
| `common/script_constants/018_resources_found_constants.txt` | Tuning for deposits, extraction, sickness, monster pressure, Cave Host spawn math, AI weights, cooldowns, and thresholds. | Use constants for shared tuning. Mirror file-scoped `@` constants only where engine fields reject script constants. |
| `common/scripted_effects/018_resources_found_effects.txt` | Target selection, deposit application, exploitation state, depletion closure, Cave Host spawning, resource counting, world-end spread, cleanup. | Avoid copy-paste across events, decisions, focuses, and GUI. Escalate reusable helpers into shared dynamic effects only when they are not event-specific. |
| `common/scripted_triggers/018_resources_found_triggers.txt` | Valid host, valid state, field phase, closure eligibility, Cave Host deployment eligibility, non-origin cap checks. | Keep player-visible requirements behind clear tooltips and scripted localisation. |
| `common/decisions/018_resources_found_decisions.txt` | Field exploitation, extraction, safety, closure, evacuation, hunting, diplomacy, concessions, smuggling, border crisis actions. | Must not become a political power store. Costs must use equipment, manpower, XP, supply, trains, convoys, stability, war support, local support, construction capacity, or field pressure where appropriate. |
| `common/decisions/categories/018_resources_found_categories.txt` | Owner decision category or scripted GUI entry point. | Category must stage visibility by field phase and hide obsolete actions. |
| `common/on_actions/018_resources_found_on_actions.txt` | Event-owned pulses if local repo supports event-owned hooks. | Do not add whole-world daily or monthly iteration without explicit permission. Prefer scoped actors, target arrays, and event-owned periodic chains. |
| `common/ideas/018_resources_found_ideas.txt` | Field-boom modifiers, concession burdens, sickness, panic, Cave Host states, emergency mobilization, aftermath. | Ideas need lifecycles and should not become permanent dead stacks. |
| `common/dynamic_modifiers/018_resources_found_dynamic_modifiers.txt` | State-level extraction boom, sickened field, evacuation pressure, monster infestation, occupied-resource draw. | Use where state modifiers need living intensity. |
| `common/country_tags/*.txt`, `common/countries/*`, `history/countries/*`, `history/units/*` | Cave Host country package. | Public country name should stay short. `Cave Host` is acceptable as a working map name, not final localisation. The leader is a fictional nonhuman cave monster. |
| `common/national_focus/*cave*host*.txt` | Cave Host focus tree. | The focus blueprint already exists. Final implementation must create the exact layout and route locks locally. |
| `common/ai_strategy/018_resources_found_ai_strategy.txt` | AI handling for exploitation, closure, crisis response, Cave Host war behavior, foreign trade interest, and containment. | AI must avoid suicidal closure or exploitation choices unless chaos, desperation, or ideology supports it. Cave Host AI is aggressive by design. |
| `common/scripted_triggers/chaosx_dynamic_triggers.txt` | Shared classification. | Add Cave Host to `is_special_chaos_country` and `is_actual_nonhuman_country`. This also keeps normal civilian systems from targeting the nonhuman country through `uses_normal_civilian_systems`. |
| `common/scripted_effects/chaosx_dynamic_effects.txt` | Shared world-threat state. | Add a Cave Host source flag to `refresh_world_threat_state` if the Host becomes a shared world threat. |
| `localisation/english/018_random_resource_l_english.yml` or `localisation/english/018_resources_found_l_english.yml` | Final implementation text. | The planning package stays direction-only. The implementation agent writes final in-game text. |
| `docs/events/018_resources_found.md` | Canonical gameplay documentation after implementation. | Must align with real implemented mechanics, event log, evolutions, super-events, assets, and spreadsheet wording. |
| `docs/assets/018_resources_found/` | Asset manifests, source art, processed previews, DDS handoffs, contact sheets. | Required after actual asset production. |
| `music/018_resources_found/` and `sound/018_resources_found/` | Final super-event audio if used. | No audio was downloaded here. Verified candidates are documented separately. |

## Required shared integration decisions

### Baseline deposit amount

The canonical baseline remains around 100 of one random resource in one valid state. The public repo's old `amount = 200` should be treated as old implementation state, not as the rework target. If the implementation agent chooses a value far from 100, it must record that as a deliberate tuning deviation and explain why.

### Cave Host country classification

The Cave Host must be treated as an actual nonhuman country. It should be excluded from normal civilian systems through the shared nonhuman trigger surface instead of using event-local duplicate triggers. The implementation should add a clear host flag or tag check to both special-chaos and actual-nonhuman shared triggers.

### World threat state

When the Cave Host becomes public and aggressive, the implementation should use the existing world-threat aggregate rather than inventing a parallel global crisis flag. A likely source flag is `world_threat_source_cave_host`, but final naming must follow local helper conventions.

### Population loss

The public repo exposes a population-change helper in `chaosx_dynamic_effects.txt`. It is a likely candidate for worker sickness, city deaths, cave monster attacks, and evacuation losses, but the implementation agent must inspect and validate current local semantics before relying on it.

### Event 18 enablement

The catalog still marks Event 18 as `To Be Reworked` in the provided CSV. Implementation must verify the default reworked-event enable allowlist before claiming normal event-log selection is complete.

## Validation commands for the implementation agent

These are local commands for the future coding pass. They were not run here against a local repo.

```bash
rg "chaosx\.nr18|018_random_resource|018_resources_found|resources_found" events common localisation docs interface gfx music sound
rg "global\.repeatable_events = 18|get_event_type|event_log_event_is_reworked_default_enabled" common/scripted_effects common/scripted_triggers common/scripted_localisation
rg "cave_host|CAVE|world_threat_source_cave|is_actual_nonhuman_country|is_special_chaos_country" common docs localisation
rg "amount = 200" events/018_random_resource.txt common events
rg "GFX_report_event_random_resource|resources_found|cave_host" interface gfx localisation docs
```

## Required local manual validation scenarios

- Baseline discovery fires for a valid owned controlled state and adds around 100 of exactly one random resource.
- The owner receives a popup and a usable field-management category.
- Every resource type can be selected in repeated debug trials.
- Trade and diplomacy reactions appear only after a discovery exists.
- Border crisis logic cannot target invalid neighbors, dead countries, enclaves without borders, or disabled routes.
- Closure before Evolution IV removes the field resources and blocks the Cave Host branch.
- Evolution II sickness and cave incidents reduce real state population through the approved population helper or a locally validated equivalent.
- Evolution III public monster attacks can be hunted or evacuated at meaningful cost.
- Cave Host origin army is capped around 30 and scales with prior exploitation.
- Cave Host non-origin deployment uses captured non-origin resources only, one division per 10 total resources, capped at 10 per state.
- Cave Host divisions require no manpower and no equipment.
- Cave Host war declarations target neighboring countries immediately after emergence.
- Cave Host occupied resource counting updates after conquest, loss, state transfer, capitulation, and closure.
- World-end branch requires world-end conditions and the relevant continental control threshold.
- Event log, evolution log, event detail, assets, docs, achievements, and spreadsheet entries match final implementation.

## Blockers carried forward

- Local repo exploration was not possible in this sandbox.
- Offline Paradox wiki and vanilla HOI4 documentation were not mounted.
- No custom subagent runner was exposed.
- No final super-event localisation or audio file was produced.
- No event catalog workbook was edited because final in-game wording does not exist yet.
