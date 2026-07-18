# Event 15 reachability correction handoff — 2026-07-15

## Scope and outcome

This patch restores bounded, actor-scoped producers for foreign reactions `chaosx.nr15.110`–`.115`, public milestones `.160`–`.162`, and the existing regime-collapse aftermath provenance consumed by `.120`. It does not add a recurring country scan. It does not modify localisation, focuses, assets, prefire events `.105`–`.109`, or prefire event `.117`.

Foreign interest is no longer treated as proof of a real league network. Event `.116` records a favorable response only in `utopia_manifesto_foreign_reaction_contacts`; it no longer writes `utopia_manifesto_recognized_external_partners` or calls `utopia_manifesto_refresh_league_state`.

## Files changed

- `common/scripted_triggers/015_utopia_manifesto_reachability_triggers.txt` — new recipient safety, evolution/route/context, regional-threshold, news, and constitutional-abandonment gates.
- `common/scripted_effects/015_utopia_manifesto_reachability_effects.txt` — new one-shot selection, reaction dispatch, and news milestone effects.
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
  - `utopia_manifesto_mark_enforcement_war_active`
  - `utopia_manifesto_trigger_stewardship_revolt`
  - `utopia_manifesto_refresh_league_state`
  - `utopia_manifesto_clear_external_network_runtime`
  - `utopia_manifesto_apply_necessary_shores_evolution`
  - `utopia_manifesto_apply_cities_of_one_measure_evolution`
  - `utopia_manifesto_apply_nowhere_made_law_evolution`
- `common/scripted_effects/015_utopia_manifesto_identity_effects.txt`
  - `utopia_manifesto_form_current_route_identity` calls reachability only after a real identity flag exists.
- `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt`
  - adds `utopia_manifesto_begin_regime_collapse_aftermath`.
- `common/on_actions/015_utopia_manifesto_on_actions.txt`
  - adds collapse entry from `on_capitulation` and constitutional abandonment from `on_government_change`.
- `events/015_utopia_manifesto.txt`
  - adds delivery triggers to `.110`–`.115`;
  - changes `.116` to non-network contact acknowledgement;
  - makes `.160`–`.162` major news events with producer-provenance triggers.
- This handoff.

## Exact reaction call graph

### Route reactions `.110`–`.112`

1. Either route identity formation or a later applicable evolution calls `utopia_manifesto_refresh_event_reachability`:
   - `utopia_manifesto_form_current_route_identity`
   - `utopia_manifesto_apply_necessary_shores_evolution`
   - `utopia_manifesto_apply_cities_of_one_measure_evolution`
   - `utopia_manifesto_apply_nowhere_made_law_evolution`
   - `utopia_manifesto_refresh_league_state`
2. `utopia_manifesto_refresh_event_reachability` calls `utopia_manifesto_try_dispatch_route_foreign_reaction`.
3. A reaction is eligible only when Necessary Shores is both recorded and still enabled at delivery time:
   - Voluntary Commonwealth / Consent of Households selects a safe nearby non-major democracy and fires `.110`.
   - Council Union / Common Table selects a safe nearby non-major communist country and fires `.111`.
   - Planned Utopia / Guardians of Measure selects a safe nearby non-major neutral or fascist country and fires `.112`.
4. Selection uses an effect-chain event target, then sets the actor's named `*_reaction_dispatched` flag before firing the event in the selected country. The selected country is event `ROOT`; the Event 15 actor is `FROM`, preserving a real human response.
5. A favorable option fires hidden actor event `.116`. In `.116`, `ROOT` is the Event 15 actor and `FROM` is the responding country. A first favorable response adds `FROM` to `utopia_manifesto_foreign_reaction_contacts` and applies the existing small Concord response. It grants no recognized-partner, league-member, network-count, formation, or proclamation credit.

### Context reaction `.113`

There are two genuine producers, both behind recorded-and-enabled Necessary Shores:

- `on_war_relation_added` verifies Event 15 actor `ROOT`, active case target `FROM`, and the enforced Necessary Ground case. It calls `utopia_manifesto_mark_enforcement_war_active`, which calls `utopia_manifesto_record_enforcement_war_milestone`, then `utopia_manifesto_try_dispatch_colonial_reaction`.
- `utopia_manifesto_trigger_stewardship_revolt` first captures the live revolt targets/states, then calls `utopia_manifesto_record_assigned_colony_revolt_milestone`, which calls `utopia_manifesto_try_dispatch_colonial_reaction` before stewardship state is cleared.

`utopia_manifesto_try_dispatch_colonial_reaction` requires either the verified enforcement-war context or active Assigned Colony stewardship represented by the failure-stage stewardship idea. It selects a safe real country that currently has at least one subject and fires `.113` once.

### Regional reactions `.114`–`.115`

1. `utopia_manifesto_refresh_league_state` rebuilds `utopia_manifesto_external_network_members` exclusively from genuine league members and recognized external partners.
2. Only after the real regional network threshold is currently met does `utopia_manifesto_refresh_event_reachability` call `utopia_manifesto_try_dispatch_regional_foreign_reactions`.
3. With Nowhere Made Law recorded and enabled, a safe real major is selected for `.114`.
4. With Cities of One Measure recorded and enabled, a safe nearby non-major democratic or communist state is selected for `.115`.
5. Each has its own actor dispatch flag and therefore fires at most once. If no safe recipient exists, no flag is set and no unsafe substitute is chosen.

## Exact news call graph

- `.160` — `utopia_manifesto_refresh_league_state` -> `utopia_manifesto_refresh_event_reachability` -> `utopia_manifesto_try_emit_league_news`. The actor must have initialized the league, currently satisfy the actual regional-proclamation network threshold, and retain at least one live, non-capitulated scope in the rebuilt external network array. `utopia_manifesto_league_news_emitted` makes it one-shot.
- `.161` — `on_war_relation_added` -> `utopia_manifesto_mark_enforcement_war_active` -> `utopia_manifesto_record_enforcement_war_milestone`. The active enforced case and actual active-case defender are rechecked. `utopia_manifesto_necessary_ground_war_news_emitted` makes the first real coercive Necessary Ground war one-shot.
- `.162` — the actual stewardship-failure path -> `utopia_manifesto_trigger_stewardship_revolt` -> `utopia_manifesto_capture_stewardship_revolt_scopes` -> `utopia_manifesto_record_assigned_colony_revolt_milestone`. It requires Closed Island, active stewardship, the Assigned Colony conduct flag, and the Assigned Colony failure-stage idea. `utopia_manifesto_assigned_colony_revolt_news_emitted` makes it one-shot.

All three definitions use `major = yes` and require their matching producer-provenance flags.

## Exact regime-collapse call graph

- Non-annexed capitulation: `on_capitulation` uses documented scopes (`ROOT` capitulated country, `FROM` winner), requires an existing accepted Event 15 actor with a formed identity, then calls `utopia_manifesto_begin_regime_collapse_aftermath`.
- Constitutional abandonment: `on_government_change` checks `utopia_manifesto_current_identity_has_been_constitutionally_abandoned`, then calls the same helper. The trigger compares each formed identity with its required ruling ideology and election constitution. Practical Commonwealth has no forced ideology, so its deterministic abandonment edge is elections being disabled.
- `utopia_manifesto_begin_regime_collapse_aftermath` rejects total repeal, an existing aftermath schedule/chain, prior resolution, kernel disable, and duplicate collapse provenance. It then sets `utopia_manifesto_aftermath_event_scheduled`, sets `utopia_manifesto_aftermath_from_regime_collapse`, calls `utopia_manifesto_record_achievement_regime_collapse`, and fires `.120`.
- Ordinary `on_war` remains ledger-only. It has no aftermath call.
- Existing `on_annex` still calls `utopia_manifesto_enter_annexation_safe_state`, which clears both aftermath provenance flags and wins if annexation follows capitulation. Total-repeal entry and finalization were not changed.

## Validation performed

- Producer search confirms one natural dispatch site for each of `.110`–`.115`, `.160`–`.162`, plus both total-repeal and regime-collapse producers for `.120`.
- Definition search confirms every new scripted effect and trigger has exactly one definition.
- The `.116` acknowledgement block contains no `utopia_manifesto_recognized_external_partners` write and no league refresh; `utopia_manifesto_foreign_reaction_contacts` is excluded from the network rebuild and cleared by `utopia_manifesto_clear_external_network_runtime`.
- The collapse audit confirms `utopia_manifesto_begin_regime_collapse_aftermath` is called only by `on_capitulation` and gated `on_government_change`; it is absent from `on_war`.
- The reaction/news surface contains no daily, weekly, or monthly on-action, and the new files contain no references to reserved prefire IDs `.105`–`.109` or `.117`.
- Brace-depth and unique-definition checks passed across all touched script files. The edited tracked files pass `git diff --check`.

## Risks, omissions, and ownership notes

- No fallback recipient was added. If the world contains no country satisfying an event's safety and context gates, that reaction remains undispatched instead of selecting a fake or unsafe actor. The dispatch flag remains clear so a later actor-scoped reachability refresh can retry.
- Country selection is a one-shot `random_country` search invoked only from the Event 15 actor's real formation, evolution, league, enforcement-war, or revolt edge. It is not attached to a recurring world on-action.
- The new regular event targets intentionally last only for their originating effect chain. No persistent global target or cleanup obligation was introduced.
- Localisation, focus trees, assets, spreadsheets, prefire implementation files, and event IDs `.105`–`.109` / `.117` were not edited.
- No commit was created.
