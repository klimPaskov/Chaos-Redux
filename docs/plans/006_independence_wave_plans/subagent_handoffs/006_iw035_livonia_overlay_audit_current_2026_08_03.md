# Event 006 IW-035 — current Livonia overlay country-package audit

Date: 2026-08-03.

Scope: current-source audit of the IW-035 Livonia vanilla-route overlay adapter. Obsolete pasted flag-log claims were excluded.

Disposition: SOURCE PASS for the bounded living-LIT adapter, but NOT ADMITTED as a selectable Event 006 country package. No gameplay source patch was safe or necessary in this audit.

This handoff supersedes the current-status portions of `subagent_handoffs/006_iw035_livonia_overlay_adapter_2026_07_28.md`. The older handoff remains useful as implementation history, while this receipt is the current contract and blocker statement.

## Country package coverage checklist

| Surface | Current result | Evidence and identifiers |
| --- | --- | --- |
| Carrier identity | PASS | `is_independence_wave_iw035_livonia_route_active` requires `exists = yes`, `tag = LIT`, `has_cosmetic_tag = LIVONIA`, and rejects `independence_wave_iw035_livonia_permanent_identity_loss` in `common/scripted_triggers/006_independence_wave_iw035_livonia_triggers.txt`. |
| Vanilla route ownership | PASS | Vanilla `common/national_focus/lithuania.txt` focus `LIT_claim_livonia_monarchy` keeps the living `LIT` tag, applies cosmetic `LIVONIA`, and adds Baltic cores without creating a dynamic country. The adapter does not replace this tree or rewrite the route. |
| State and host preservation | PASS with a P3 policy note | `has_independence_wave_iw035_livonia_anchor_control` accepts owns-and-controls state `12` or `191`, and the watch objective additionally requires a division in one of those states. The installed map binding is primary `12` with compact `12|191`; vanilla state histories remain authoritative. Host-survival conditions are `EST=812` and `LAT=808`. Initialization records shared `independence_wave_anchor_state = 12`; the local adapter does not consume that variable when state `191` is the active alternate. A future shared consumer needs an explicit primary-versus-active-anchor policy, but changing it here would broaden the contract. |
| D01-D50 hooks | PASS | IW-035 intentionally has only `on_daily_LIT` in `common/on_actions/006_independence_wave_iw035_livonia_on_actions.txt`. Dynamic `on_daily_D01`–`on_daily_D50` hooks belong to dynamic-country-origin overlays such as IW-022/IW-025 and would be wrong for the living `LIT` carrier. No global `on_daily` iteration is used. |
| Paid decisions | PASS | `common/decisions/006_independence_wave_iw035_livonia_decisions.txt` contains five player actions: `independence_wave_iw035_compile_baltic_rail_ledgers`, `independence_wave_iw035_establish_baltic_coastal_watch`, `independence_wave_iw035_mobilize_livonian_watch`, `independence_wave_iw035_charter_baltic_municipalities`, and `independence_wave_iw035_establish_federal_coastal_compact`. Each has an availability cost trigger, `custom_cost_trigger`, dynamic `custom_cost_text`, an explicit payment effect, and an effect tooltip. |
| Timed mission | PASS | `independence_wave_iw035_hold_livonian_corridor_watch` is activated by the paid mobilisation effect, has a 45-day continuous hold requirement, a 135-day base timeout, explicit completion, cancellation, and timeout effects, and AI urgency. The objective is anchor ownership and control plus a garrison division. |
| Lifecycle ideas | PASS | `common/ideas/006_independence_wave_iw035_livonia_ideas.txt` defines the four route ideas `independence_wave_iw035_livonia_contested_baltic_administration`, `independence_wave_iw035_livonia_coordinated_rail_authority`, `independence_wave_iw035_livonia_municipal_baltic_charter`, and `independence_wave_iw035_livonia_federal_coastal_compact`. Their `allowed` gate is the exact route trigger, and the effect lifecycle removes and refreshes them on activation, settlement, suspension, and loss. |
| Route-loss cleanup | SOURCE PASS | `independence_wave_iw035_livonia_suspend_overlay`, `independence_wave_iw035_livonia_pause_watch_mission`, `independence_wave_iw035_livonia_resume_overlay`, and `independence_wave_iw035_livonia_cancel_watch_permanent_identity_loss` remove ideas, interrupt the watch, extend the mission by one day per suspended day, resume before the 30-day grace limit, and permanently remove the mission and route flags at the limit. The permanent-loss helper resets `independence_wave_iw035_livonia_watch_hold_days` and sets `independence_wave_iw035_livonia_permanent_identity_loss`. Exact engine ordering around mission timeout versus the daily hook remains a live-runtime boundary. |
| AI and playability | SOURCE PASS, runtime evidence open | All five actions and the mission have AI weights. Mobilisation is disabled without a garrison, preparatory actions are high priority, settlement weights change with war status, and the mission is urgent. No live weighted-selection or save/load scenario was run by this audit. |
| Localisation and UI | PASS | `localisation/english/006_independence_wave_iw035_livonia_l_english.yml` is UTF-8 with BOM and covers the decision category, five actions, mission, cost strings, blocked-cost strings, effect tooltips, and four idea keys. The dynamic cost strings read the IW-035 script constants and use canonical equipment/train icons. |
| Generic focus ownership | PRESERVED, admission remains closed | Lithuania retains vanilla `lithuania_tree`. IW-035 is absent from `can_attach_independence_wave_additive_focus_carrier` in `common/scripted_triggers/006_independence_wave_focus_triggers.txt`, whose current allowlist is limited to the reviewed Iceland and IW-023 carriers. No generic tree assignment or unconditional shared-focus insertion is performed. |
| Network, League, and formable participation | NOT ADMITTED | IW-035 source contains no `independence_wave_network_member`, `independence_wave_league_route_available`, `independence_wave_formable_family_registered`, or package attestation setup. The generic network, League, and formable triggers therefore remain fail-closed. Adding these flags would be a design expansion, not a narrow country fix. |
| Tag, country, leader, portrait, flag, and advisor surfaces | Intentional overlay omission | IW-035 has no country definition, country history, character, leader, advisor, portrait, or new flag files. This is correct for a living `LIT` cosmetic overlay, but it is a blocker if the route is ever promoted to a selectable package. Do not promote provisional registry tag `BIX` without a new identity and asset review. |
| Military, technology, industry, supply, and production | Vanilla carrier preserved | No IW-035 OOB, technology, country-history, factory, supply, railway, port, or production override exists. The overlay spends manpower, command power, trains, infantry equipment, support equipment, and army experience through its costed actions, but it does not grant free units or alter the vanilla LIT starting setup. This is expected for a non-selectable route and insufficient for standalone package admission. |

## File surface checklist

The live IW-035 adapter files are:

- `common/script_constants/006_independence_wave_iw035_livonia_constants.txt`
- `common/scripted_triggers/006_independence_wave_iw035_livonia_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw035_livonia_effects.txt`
- `common/decisions/categories/006_independence_wave_iw035_livonia_categories.txt`
- `common/decisions/006_independence_wave_iw035_livonia_decisions.txt`
- `common/ideas/006_independence_wave_iw035_livonia_ideas.txt`
- `common/on_actions/006_independence_wave_iw035_livonia_on_actions.txt`
- `localisation/english/006_independence_wave_iw035_livonia_l_english.yml`

The contract and admission surfaces checked were:

- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` row `IW-035`.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` row `IW-035`.
- `common/scripted_triggers/006_independence_wave_packages_region_04_triggers.txt`, where `can_plan_independence_wave_package_iw_035 = { always = no }`.
- `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt`, where the dormant `iw_035` loader, weight, and reservation stubs remain unreachable under that fail-closed trigger.
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt` and the generic focus source for ownership and admission checks.
- Vanilla `common/national_focus/lithuania.txt`, `history/states/12-Latvia.txt`, and `history/states/191-Tartu.txt` for route and map precedent.

No IW-035 country, state-history, focus-tree, character, portrait, flag, advisor, technology, OOB, production, or map-write file was added or changed by this audit.

## Missing or stale country-package surfaces

The route remains intentionally `vanilla_route_overlay_only` and `overlay_nonselectable` in the installed binding. Its registry row has provisional tag `BIX` but an empty `resolved_tag`; the provisional token is not a runtime carrier and must not be promoted.

The planner remains fail-closed because `can_plan_independence_wave_package_iw_035` is `always = no`. The dormant region loader in `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt` describes IW-035 with archetype `port_or_island`, while the live adapter records `independence_wave_package_archetype = river_or_corridor` and `independence_wave_force_profile = coastal_maritime`. This metadata mismatch is unreachable while admission is disabled, but it is a stale contract surface that should be reconciled only in a separately authorized registry/package pass.

The exact route adapter is not registered for the shared generic focus, Network, League, or formable systems. That omission preserves the meaningful vanilla Lithuania tree and prevents a half-wired package from becoming selectable, but it leaves promotion blocked.

## Map and state setup

Vanilla state `12` is Latvia/Vidzeme with owner `LAT` in 1936; vanilla state `191` is Tartu with owner `EST`. The mod has no IW-035 state-history override. The accepted compact binding is `12|191`, and host survival requires `EST` to retain state `812` and `LAT` to retain state `808` after any future compact operation. The local adapter only checks current owns-and-controls status, so runtime ownership remains authoritative.

The initializer writes shared anchor variable `independence_wave_anchor_state = 12` as the contract primary. Because the local watch trigger accepts `12` or `191`, future shared systems must not assume that variable always equals the currently occupied alternate without an explicit policy decision.

No map write was made. Read-only map inspection reported the selected state/network definitions as structurally valid, while unrelated global building and floating-harbor diagnostics were outside IW-035 scope.

## Politics, leader, portrait, flag, advisor, and party issues

The overlay keeps Lithuania's existing tag, parties, leader, portrait, flag, advisors, laws, diplomacy, and focus owner. It adds no fictional leader or portrait and therefore has no gender-pool or provider-pipeline issue. A future selectable Livonia package would require a new identity, party, leader, symbol, and asset-source review; that work is outside this bounded audit.

## Focus, decision, idea, and asset issues

The five decisions and one mission are wired through the living LIT route and carry dynamic costs from `common/script_constants/006_independence_wave_iw035_livonia_constants.txt`. Settlement thresholds are closed by the existing value math: the route starts at rail `28`, legitimacy `30`, and security `24`; the depot, coastal-watch, and successful corridor-watch gains bring the required rail/legitimacy or rail/security pairs to the settlement threshold before either municipal or federal settlement.

The four ideas are route-gated and have complete localisation. The working tree contains a concurrent, unclaimed edit to the idea file that mirrors static modifier values into file-scoped constants; this audit did not touch or claim that edit.

No new art asset is required for the overlay decision icons because it reuses registered shared decision sprites. No flag, portrait, focus icon, idea icon, or advisor art was added.

## Starting military, technology, industry, supply, and production issues

The living LIT carrier keeps vanilla starting forces, technologies, industry, supply, rail, port, and production. IW-035 has no independent setup to audit and no free-unit effect. Its only military/economic surface is the paid corridor-watch sequence and the four visible lifecycle modifiers. This is coherent for a route overlay and remains insufficient for standalone admission.

## AI and playability issues

Source-level AI weights are present for every action and the mission. The mobilisation action refuses AI selection without a division in state `12` or `191`; peace/war modifiers steer preparation and settlement choices. The audit did not claim live AI survival, save/load persistence, mission-timeout ordering, or runtime weighted-selection evidence. Those checks belong to a live consumer validation pass and cannot be replaced by source inspection.

## Validation performed

- Read the required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, national focuses, and country creation.
- Read the relevant vanilla documentation for effects, triggers, modifiers, and script concepts, including mission activation, timeout extension, cancellation, and variable usage.
- Ran a bounded static check over the IW-035 trigger, effect, decision, on-action, idea, and localisation files. It passed the exact `LIT`/`LIVONIA` identity gate, state `12`/`191` anchor checks, `on_daily_LIT`-only hook, five paid decisions, timed mission, permanent-loss cleanup, four idea IDs, BOM, and 24 decision localisation keys.
- Inspected vanilla `lithuania_tree` and `LIT_claim_livonia_monarchy` with the read-only focus viewer. The viewer's unrelated vanilla diagnostics were not treated as IW-035 failures.
- Inspected map state/network data read-only for states `12` and `191`; no map rewrite was attempted.

No Hearts of Iron IV process was launched, and no live/save/load or in-game AI claim is made.

## Changed files and patch disposition

Changed by this audit: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw035_livonia_overlay_audit_current_2026-08-03.md` only.

No gameplay source, tag, state, leader, party, focus, decision, mission, idea, localisation, asset, map, or registry admission patch was made. The current source already contains the permanent-loss hold reset and mission removal needed by the latest lifecycle contract, so a duplicate patch would have been unsafe.

## Remaining blockers and next actions

- Keep IW-035 non-selectable and keep `can_plan_independence_wave_package_iw_035 = always = no` until a reviewed identity, generic-focus ownership, Network/League/formable contract, and asset package exists.
- Do not promote registry provisional tag `BIX` or create a new country from this overlay receipt.
- Reconcile the dormant loader's `port_or_island` metadata with the live adapter's `river_or_corridor` archetype only in a separately authorized package-registry pass.
- Define whether shared consumers should read primary anchor `12` or a runtime-selected active anchor `12|191` before exposing `independence_wave_anchor_state` to generic systems.
- Perform live mission timeout, temporary route-loss, permanent route-loss, save/load, and AI validation when the parent authorizes a runtime evidence pass.

No fallback, placeholder country, new tag, or identity redesign was used.
