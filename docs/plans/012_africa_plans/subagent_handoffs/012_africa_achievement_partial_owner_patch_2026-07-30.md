# Event 012 Africa achievement partial-owner patch

## Scope and ownership

This handoff records the bounded owner-callsite patch for the reachable or partial achievement rows assigned from `012_africa_achievement_callsite_audit_2026-07-29.md`.

The patch wires only exact Event 012 final-result witnesses for annexation, external puppeting, constitutional route history, formation ordering, and final regional proof counts.

The nine `ACTIVE/BLOCKED` rows, four model-gated rows, and four world-gated rows were not opened; the annexation callback is a shared exact owner that also supplies already-declared restoration disqualifiers for active rows.

No fallback, proxy flag, inferred victory, new country, recurring all-country on_action, model/world package, acceptance-ledger edit, or commit was added.

## Helper and owner map

| Helper or owner | Scope and inputs | Outputs and side effects | Exact callsite |
|---|---|---|---|
| `africa_achievement_record_coercive_annexation` | Annexed-country `FROM` scope during the engine `on_annex` transaction; reads the victim's current-generation member variable or immutable counted/restoration flags. | Sets the existing coercive, direct-member, and untracked-member lifetime DQs, maps counted protected/guaranteed/archive/restoration victims to their row-specific DQs, and now maps the last-convoy candidate to `africa_achievement_last_convoy_partner_annexed` plus its country cleanup flag. | `on_annex` in `common/on_actions/012_africa_world_order_on_actions.txt`; helper body in `common/scripted_effects/012_africa_achievement_effects.txt`. |
| `africa_achievement_record_external_puppet_status` | Event 012 puppet `ROOT` scope; called only when the puppet has an African core, is the current host or a current-generation member, and `FROM` has a capital outside Africa. | Sets `africa_achievement_external_puppet_in_africa`, the existing no-foreign-boot lifetime DQ. | `on_puppet` in `common/on_actions/012_africa_world_order_on_actions.txt`. |
| Formation regional proof barriers | Host scope at the single atomic `africa_complete_continental_milestone` commit; reads the existing food, represented-region, and overlap-settled arrays before setting `africa_is_one`. | Sets `africa_achievement_formed_before_food_security` when the pre-unification food snapshot did not pass, and sets the two existing region DQs when either nine-region final proof array is incomplete. | `africa_complete_continental_milestone` in `common/scripted_effects/012_africa_focus_route_effects.txt`. |
| Covenant-route history writer | Host scope at the exact `africa_commit_covenant_route` constitutional result; no dynamic input. | Sets `africa_achievement_covenant_route_used`, satisfying the existing lifetime route DQ for consent federalism. | `africa_commit_covenant_route` in `common/scripted_effects/012_africa_focus_route_effects.txt`. |

## Constants and tuning table plan

No constants or tuning values were added or changed.

The formation barriers reuse `constant:africa_achievement_count.continental_regions` and the existing global proof arrays, so no duplicate threshold can drift from the achievement trigger.

## Event targets, variables, flags, and cleanup

The patch uses the engine-provided `ROOT`/`FROM` scopes for `on_annex` and `on_puppet` and the existing `africa_host` and `africa_member_host_generation` ownership witnesses.

No new event target, global event target, variable, array, or cleanup path was introduced.

All new writes are lifetime global disqualifier flags or an existing country cleanup flag, so they intentionally do not clear on later retries or relationship transitions.

## Row dispositions

| Audit row | Exact owner now connected | Remaining gap |
|---:|---|---|
| 1 `africa_guardians_without_borders` | Counted protected-partner annexation now runs from the real annex transaction. | Permanent archive destruction and other non-annex partner loss owners remain absent. |
| 2 `africa_last_convoy_home` | Last-convoy candidate annexation now sets its existing partner-annexed DQ. | Exit/abandonment and capitulation owners remain separate existing paths. |
| 3 `africa_no_empty_promises` | Counted guarantee partner annexation now runs from the real annex transaction. | No additional owner gap was invented. |
| 4 `africa_the_interveners_left` | No partition or Scramble-settlement proxy was added. | `africa_achievement_partition_accepted` has no exact owner. |
| 5 `africa_archive_of_the_living_state` | Evacuated archive partner annexation now runs from the real annex transaction. | Permanent destruction and sale/suppression owners remain absent. |
| 6 `africa_twelve_empty_chairs_filled` | No new owner was inferred; existing congress reset helpers remain the source of truth. | A full agenda final-result owner still needs to replace the accepted simplification. |
| 7 `africa_the_clause_is_the_country` | Untracked member annexation now runs from the real annex transaction. | Protected-clause cancellation has no exact final writer. |
| 8 `africa_exit_without_war` | No exit-war, coup, or coerced-return proxy was added. | Those exact final-result owners remain absent. |
| 9 `africa_no_second_capital` | No rival-crisis annexation or terminal-coercion proxy was added. | Those exact final-result owners remain absent. |
| 10 `africa_every_region_speaks` | The final Africa-is-One barrier records incomplete representation or overlap proof arrays before formation. | There is still no state-control cleanup owner for a region that loses proof after it was recorded but before formation. |
| 11 `africa_confidence_is_contagious` | Direct annexation of a current-generation member now sets the existing shared DQ. | A separate relationship-loss clock refresh remains future work. |
| 12 `africa_federation_by_consent` | Covenant route commitment is recorded, and direct annexation uses the shared exact owner. | Military-takeover and other coercive final dispositions remain unowned. |
| 13 `africa_republic_of_many_capitals` | No republic-suspension, centralisation, or military-transition proxy was added. | Constitutional DQ writers remain absent. |
| 14 `africa_crowns_at_one_table` | Direct annexation of a recorded court now uses the shared exact owner. | Court deposition and monarchy-abolition owners remain absent. |
| 15 `africa_union_of_work_and_land` | No takeover, concession, or famine proxy was added. | Those exact constitutional/economic/famine owners remain absent. |
| 16 `africa_order_without_partition` | No partition, emergency, or genocide proxy was added. | Those final-result owners remain absent. |
| 17 `africa_confederation_that_endured` | Direct annexation uses the shared exact owner where a member is absorbed. | Federal annexation and final confederal cleanup remain incomplete. |
| 25 `africa_return_without_compulsion` | No forced-relocation or disaster-negligence proxy was added. | Exact diaspora failure owners remain absent. |
| 26 `africa_tools_books_and_ballots` | No military-only-labour or representation-denial proxy was added. | Those exact programme/constitutional failure owners remain absent. |
| 27 `africa_four_oceans_homeward` | No catastrophic-return-loss or forced-relocation proxy was added. | Exact return-wave failure owners remain absent. |
| 28 `africa_capital_without_capture` | External-puppet creation now has an exact engine callback for an African-core Event 012 host/member. | Government capture, diaspora-government capture, and corruption owners remain absent. |
| 29 `africa_rails_rivers_roads_and_ports` | No connected-region-loss proxy was added. | State/network loss cleanup remains absent. |
| 30 `africa_ore_leaves_as_machines` | No raw-export or forced-resource-seizure proxy was added. | Live concession-share and exact resource failure owners remain absent. |
| 31 `africa_bread_before_banners` | Formation now records the exact formed-before-food ordering failure. | Preventable famine and maximum ecological-wrath civilian owners remain absent. |
| 34 `africa_no_foreign_boot_remains` | External puppeting of a current Event 012 host/member with an African core now records the existing DQ. | African-core cession and unreversed capitulation owners remain absent. |
| 37 `africa_the_forest_kept_its_word` | An accepted Event 012 hostile-actor natural-disaster call now records the exact disaster-weaponisation DQ. | Forest-rampage remains absent because no exact final actor-rampage disposition is exposed. |
| 39 `africa_disease_made_and_unmade` | No uncontrolled-release, irreversible-outcome, or terminal-disease proxy was added. | Those exact disease-system final dispositions remain absent. |

The shared annexation callback also supplies already-declared restoration identity DQs for rows 19-24 and 38 when their recorded victim is actually annexed; no new readiness gate was changed.

## Migration plan

Annexation callers should continue to use the single achievement helper rather than duplicating row-specific global flags in action, event, or peace-conference code.

Future external-subject paths should call the same external-puppet helper only from exact subject-creation or autonomy-result callbacks after confirming the African-core and Event 012 ownership predicates.

Future region-loss work should add a real state-control or final-disposition owner and either clear the affected proof array entry or set the existing sticky DQ; this patch deliberately does not infer loss from current-control counts.

## Validation

The touched-script diff was inspected for block structure and limited to the two Event 012 scripted-effect files, the Event 012 on-action file, and this handoff.

`rg` confirmed the new helper definition, both exact on-action callers, the covenant writer, the formation barrier flags, and the last-convoy annexation branch.

The vanilla `on_actions` documentation comments and examples were checked to confirm `ROOT`/`FROM` orientation for annexation and puppeting, and the offline trigger/effect references were consulted for `any_core_state`, `capital_scope`, global flags, and array-size comparisons.

HOI4 was not launched, and no in-game save or live consumer validation was performed because runtime validation belongs to the parent/user workflow.

## Limitations and follow-up

No fallback or simplification was introduced by this patch.

The remaining absent owners listed above are intentional blockers and must not be replaced with opinion, current-control-only proxies, generic action failures, recurring scans, or inferred victories.

The parent should review the annexation and external-puppet callbacks against the final Event 012 actor-registration lifecycle before integrating the tranche.

## Second-tranche exact owner audit (2026-07-30) — superseded on 2026-08-01

This historical audit is retained for provenance, but its hostile-disaster classification for the civilian-weaponisation disqualifier is no longer an accepted Event 012 owner.
The current Event 013 result exposes an accepted selected-country call, not a civilian-casualty witness.
The authoritative disposition is recorded in `012_africa_b3_achievement_owner_closure_2026-08-01.md` and `012_africa_final_completion_audit_2026-08-01.md`: the civilian-disaster helper remains dormant until an exact civilian-damage API or terminal owner is approved.

This tranche re-audited the remaining non-model, non-world rows against the current action, focus, event, natural-disaster, annexation, capitulation, peace-conference, and state-control surfaces.

### Helper map

| Helper or owner | Scope and inputs | Outputs and side effects | Exact callsite |
|---|---|---|---|
| `africa_achievement_record_disaster_weaponised_against_civilians` | Reserved Event 012 host helper retained for a future exact civilian-damage or terminal owner. The current selected-country hostile wrapper does not provide that witness. | Would set the existing sticky `africa_achievement_disaster_weaponised_against_civilians` DQ and reset the ecological-stability retention clock once an approved owner supplies the civilian-damage proof. | No current callsite. The dormant helper body remains in `common/scripted_effects/012_africa_achievement_effects.txt`; the accepted hostile wrapper in `common/scripted_effects/012_africa_action_effects.txt` deliberately does not call it. |

The original proposal treated an accepted hostile selected-country call as the narrowest witness for Row 37's disaster-weaponisation clause.
That proposal is superseded: accepted calls, impact scales, generic ecological wrath, Event 013 aftermath flags, and random backfire are not treated as civilian-damage proof.

### Constants and tuning table plan

No constants or tuning values were added or changed.

The new helper reuses the existing `africa_achievement_days.unset_deadline` retention sentinel and adds no thresholds, duration bands, or AI weights.

### Event targets, variables, flags, and cleanup

No new event target, global event target, variable, array, or recurring on-action was introduced.

The helper writes one lifetime global DQ and invalidates the existing ecological-stability clock, matching the surrounding sticky achievement-owner helpers.

### Migration plan

Existing hostile disaster callers should continue to route through `africa_call_hostile_natural_disaster_from_action`.
Its accepted-result branch owns target classification, weather campaign receipts, and backfire handling; it must not call the civilian-disaster helper until Event 013 exposes an exact civilian-damage witness or another approved terminal owner is wired.

No migration was possible for the other audited rows because their exact terminal owners are not exposed by the current action, focus, event, state-control, capitulation, or peace-conference callbacks.

### Remaining exact-owner dispositions

Rows 4–17, 25–31, 34, and 39 remain unchanged; Row 37 has no accepted hostile-disaster owner: no exact writers were found for partition acceptance, archive destruction or suppression, protected-clause cancellation, exit war or coup, coerced return, rival terminal coercion, post-proof region loss, military takeover, republic suspension or centralisation, court deposition, monarchy abolition, takeover, concession cap, famine, permanent emergency rule, genocide, federal annexation, diaspora negligence, returnee discrimination, military-labor-only programming, representation denial, catastrophic return loss, government capture, corruption, connected-region loss, raw-export dependency, forced resource seizure, preventable famine, maximum ecological wrath against civilians, African-core cession, unreversed capitulation, forest rampage, or disease severity outcomes.

The existing congress-agenda completion simplification remains documented and was not broadened in this tranche.

### Risks, unsupported fields, and validation

The accepted Event 013 result does not expose a separate civilian-casualty field to Event 012, so the helper remains dormant rather than being inferred from Event 013 aftermath, impact scales, or wrath values.

The state-control callback still lacks a safe region-to-state proof mapping for Row 10 or Row 29 cleanup, and the capitulation callback lacks a later exact reversal witness for Row 34; neither was approximated.

Validation was limited to the touched callsite/helper diff, `rg` confirmation of the new helper and existing DQ trigger, and a re-read of the surrounding action contract and handoff row matrix.

HOI4 was not launched, and no in-game save or live consumer validation was performed because runtime validation belongs to the parent/user workflow.
