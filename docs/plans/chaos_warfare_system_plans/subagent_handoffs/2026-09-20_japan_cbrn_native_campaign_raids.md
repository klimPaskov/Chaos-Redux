# Japan-China CBRN native campaign raid handoff

Status: source migration under final integration review. The country-root bridge is installed; the Black Friday achievement bridge remains blocked as described below. The parent authorized static normal, sale, and evolution raid variants and removal of the old biological Political Power charge as part of the simplified native raid economy. No game was launched and no commit was made.

## Behavior and ownership

The chemical campaign uses `chemical_raids` and the biological campaign uses `biological_raids`, the two shared CBRN raid categories maintained by the native raid owner. Every Japan variant is one native land raid in `common/raids/japan_cbrn_campaign_raids.txt`: the player and AI choose the same ID, select one enemy state, originate at a supply node, assign a qualifying division, wait for the native preparation timer, and reserve exact equipment through `essential_equipment`. Each of four engine outcomes calls its Japan callback once. Neither callback removes equipment, pays Command Power, refunds a failed attack, or dispatches the same release twice.

Chemical raids cover chlorine, phosgene, mustard, and lewisite. The selected agent is fixed in the raid ID, and each reserves the matching `<agent>_agent_payload` archetype. An immediate hidden country event reconstructs the fixed agent, price, payload, and outcome from regular event-target markers, then `japan_resolve_chemical_campaign_raid_outcome` calls the shared `cbrn_resolve_chemical_land_raid_country_outcome` once and records Japan campaign history only after `cbrn_raid_release_accepted`. The shared adapter performs the chemical action, contamination, evidence, and Condemnation dispatch.

Biological raids cover anthrax and plague. `japan_bio_campaign_resolve_native_raid_outcome` uses the exact actor, victim, and state supplied by the raid instance, resolves failure evidence or one ordinary lifecycle seed with `bio_lifecycle_route.japan_china_campaign`, and records the existing Japan actor/state history. It does not use the generic food, water, and medical supply-chain sabotage route.

The Japan biological callback brackets its one seed dispatch with the short-lived actor flag `bio_native_raid_dispatch_in_progress`. The shared lifecycle guard on `bio_lifecycle_grant_integrated_operations_release_command_recovery` checks that flag, so the ordinary seed does not return Command Power on top of the native allocation.

The campaign decisions and their now-empty categories were removed. The chemical agent-cycle selector, selected-agent stockpile and Command Power helpers, Black Friday decision payment/refund helpers, and obsolete cost/selection localisation were removed after a zero-reference check. The shared Black Friday lifecycle, achievement, and other owner adapters remain.

## Exact raid IDs

```text
japan_china_chemical_chlorine_normal_raid
japan_china_chemical_chlorine_normal_optimized_raid
japan_china_chemical_chlorine_sale_raid
japan_china_chemical_chlorine_sale_optimized_raid
japan_china_chemical_chlorine_evolution_raid
japan_china_chemical_chlorine_evolution_optimized_raid
japan_china_chemical_phosgene_normal_raid
japan_china_chemical_phosgene_normal_optimized_raid
japan_china_chemical_phosgene_sale_raid
japan_china_chemical_phosgene_sale_optimized_raid
japan_china_chemical_phosgene_evolution_raid
japan_china_chemical_phosgene_evolution_optimized_raid
japan_china_chemical_mustard_normal_raid
japan_china_chemical_mustard_normal_optimized_raid
japan_china_chemical_mustard_sale_raid
japan_china_chemical_mustard_sale_optimized_raid
japan_china_chemical_mustard_evolution_raid
japan_china_chemical_mustard_evolution_optimized_raid
japan_china_chemical_lewisite_normal_raid
japan_china_chemical_lewisite_normal_optimized_raid
japan_china_chemical_lewisite_sale_raid
japan_china_chemical_lewisite_sale_optimized_raid
japan_china_chemical_lewisite_evolution_raid
japan_china_chemical_lewisite_evolution_optimized_raid
japan_china_biological_anthrax_normal_raid
japan_china_biological_anthrax_sale_raid
japan_china_biological_anthrax_evolution_raid
japan_china_biological_plague_normal_raid
japan_china_biological_plague_sale_raid
japan_china_biological_plague_evolution_raid
```

## Cost and preparation review

| Route | Old decision cost | Native normal | Native sale | Native evolution | Preparation |
| --- | --- | --- | --- | --- | --- |
| Chemical cylinder, each agent | 120 selected legacy cylinders; 20 CP, or 16 CP with reagent optimization | 40 exact agent payload; 20 or 16 CP | 20 payload; 10 or 8 CP | 10 payload; 5 or 4 CP | 5 days |
| Anthrax | 35 PP, 8 anthrax bombs, 35 support, 10 CP; doctrine could refund 2 or 4 CP | 8 bombs, 35 support, 10 CP | 4 bombs, 18 support, 5 CP | 2 bombs, 9 support, 3 CP | 30 days |
| Plague | 40 PP, 10 plague bombs, 45 support, 14 CP; doctrine could refund 2 or 4 CP | 10 bombs, 45 support, 14 CP | 5 bombs, 23 support, 7 CP | 3 bombs, 12 support, 4 CP | 45 days |

The chemical normal amount follows the shared cylinder route's 40 exact-agent lot instead of converting legacy cylinders into new archetypes. The old biological Political Power charge and post-payment Command Power doctrine refund are absent by parent-approved economy simplification. The 50% and 75% Black Friday variants use static integer reservations with upward rounding for odd quantities. Static native costs do not include other composed Black Friday owner modifiers that the old universal quote could apply.

Only the matching price tier is available when a raid is created. The price and exact equipment are reserved before preparation, so a sale raid may launch after the one-day sale ends without repricing or a second debit. War, actor readiness, target control, victim-specific CBRN authority, project, and cooldown gates are checked at launch. Outcome callbacks fail closed if the state, victim, route, or project becomes invalid during preparation. Native cancellation and target-loss equipment handling remain engine owned; there is no script refund path.

The final cross-audit changed the sale and evolution price predicates to explicit equality. The earlier shorthand `check_variable` threshold would also admit the 75% evolution price when the 50% sale ratio was active. The biological outcome effect now prepares the exact victim id before evaluating its victim-specific policy trigger, so that input does not depend on nested trigger evaluation order.

The later receipt audit changed both Japan outcome wrappers from `price_tier > normal` to exact tier branches. The baseline 50% tier alone sets `japan_chemical_campaign_black_friday_purchase_history` or `japan_bio_campaign_black_friday_purchase_history`; the 75% evolution tier sets its separate `*_black_friday_evolution_purchase_history` flag. Both branches retain `*_last_price_tier`, while normal-price outcomes set neither sale-history flag. Source evidence is `japan_cbrn_raid_price.normal/sale/evolution` in `common/script_constants/japan_cbrn_campaign_raid_constants.txt` and the branches in `common/scripted_effects/JAP_chemical_campaign_effects.txt` and `common/scripted_effects/japan_biological_campaign_effects.txt`.

The shared native outcome tooltips now describe an attempted release and conditional consequences, because target control, war, policy, readiness, and project conditions can change after preparation and the country-root resolver can reject the final discharge. The 24 chemical and six biological IDs all use those shared actor/target tooltip keys. The Black Friday raid titles identify the reservation tier; neither their names nor descriptions claim an achievement transaction on completion.

## Changed source

- Added `common/raids/japan_cbrn_campaign_raids.txt`, `events/japan_cbrn_campaign_raid_bridge.txt`, `common/script_constants/japan_cbrn_campaign_raid_constants.txt`, and `localisation/english/japan_cbrn_campaign_raids_l_english.yml`.
- Reworked `common/scripted_effects/JAP_chemical_campaign_effects.txt`, `common/scripted_effects/japan_biological_campaign_effects.txt`, `common/scripted_triggers/japan_biological_campaign_triggers.txt`, `common/script_constants/japan_biological_campaign_constants.txt`, and Japan campaign entries in `common/script_constants/chemical_warfare_constants.txt`.
- Deleted `common/decisions/japan_chemical_campaign_decisions.txt`, `common/decisions/japan_biological_campaign_decisions.txt`, `common/decisions/categories/japan_chemical_campaign_categories.txt`, `common/decisions/categories/japan_biological_campaign_categories.txt`, `common/scripted_localisation/japan_chemical_campaign_scripted_localisation.txt`, and `localisation/english/japan_biological_campaign_l_english.yml`.
- Removed retired Japan decision strings from `localisation/english/chaosx_decisions_l_english.yml` and old selected-stockpile/Command Power helpers from `common/scripted_triggers/cbw_triggers.txt`; its Japan-China war and exact target triggers remain.
- Removed only orphaned Japan campaign owner adapters from `common/scripted_effects/026_black_friday_effects.txt`, affordability triggers from `common/scripted_triggers/026_black_friday_triggers.txt`, and decision-cost scripted text from `common/scripted_localisation/026_black_friday_scripted_localisation.txt`.

Removed Black Friday effect IDs: `black_friday_credit_japan_chemical_cylinder`, `black_friday_record_japan_chemical_component`, `black_friday_prepare_japan_chemical_campaign_payment`, `black_friday_refund_japan_chemical_campaign`, `black_friday_record_japan_bio_component`, `black_friday_pay_japan_bio_native_component`, `black_friday_credit_japan_bio_payload`, `black_friday_prepare_japan_bio_campaign_payment`, and `black_friday_refund_japan_bio_campaign`.

Removed Black Friday trigger IDs: `black_friday_japan_chemical_campaign_stockpile_is_affordable`, `black_friday_can_pay_japan_chemical_campaign_attack`, `black_friday_japan_bio_campaign_payload_is_affordable`, `black_friday_can_pay_japan_bio_campaign_anthrax`, `black_friday_can_pay_japan_bio_campaign_plague`, and `black_friday_japan_bio_campaign_selected_agent_cost_is_available`.

Removed Japan selected-stockpile trigger IDs: `has_japan_chemical_campaign_selected_stockpile_attack`, `has_japan_chemical_campaign_attack_command_power`, and `has_japan_chemical_campaign_any_stockpile_attack`. Removed scripted localisation IDs: `GetBlackFridayJapanChemicalCampaignAttackCost`, `GetBlackFridayJapanChemicalCampaignAttackCostBlocked`, `GetBlackFridayJapanChemicalCampaignCylinderRequirement`, `GetBlackFridayJapanBioAnthraxCost`, `GetBlackFridayJapanBioAnthraxCostBlocked`, `GetBlackFridayJapanBioPlagueCost`, and `GetBlackFridayJapanBioPlagueCostBlocked`.

## Validation and unresolved coverage

An invariant check reviewed all 30 IDs against the full variant matrix, two shared categories, supply-node origin, three qualifying division options, exact essential equipment and CP aliases, mutually exclusive price gates, victim-specific policy gates, four outcome callbacks and raid-history entries, and all 60 name/description localisation keys. Source searches found no remaining references to the removed selector, decision-payment helpers, or deleted scripted localisation.

`hoi4.probability_inspect` captured the old chemical and biological decision `ai_will_do` baselines. Post-edit inspection found no supported weighted adapter in the raid file; `hoi4.probability_compare` returned `PROBABILITY_SURFACE_EMPTY` for both old-decision/new-raid comparisons. Event 026 `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL`; `hoi4.event_render` timed out. No native raid MCP inspector is exposed, so source validation does not prove the prepared raid's engine behavior.

- Old chemical weighted source revision: `895aff8ad85fdbff6d875714070d18424f5f27d36ec8e279304d4b61a2c56f52`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88de0d836ccdac3dc6f47c8c0bf7d13f58f07ae9a267a5d7146c46b5e53e716e/10e5a3a515ecd3304f07615c8401a12670e2fd675e237cec2ab79caedcfae7a0/probability-inspect-20af6f4486d7.json`.
- Old biological weighted source revision: `16c0d2d94772430261c5b690818cacce38b07d284e926abfb79b6bbd5ab97d7d`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7bdb2167b7afda8e12f8bad4501b73d84e985b258a90d6bebd16dc4f11ad65b3/b2e8475853c776bfeb1c1090c59ea7460300990a8f6545a117ad941a86f70cb8/probability-inspect-30eb72f6e042.json`.
- Native raid weighted discovery source revision: `bdbc643e4047c8e059ae033c3293e2139f679988ad456dd46e1f703941fca5a4`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5239bf6a457675cd74df8af537fc4961aa35f80491c7a5aedc739ecb532aea81/414f83a2fc77ea3e7a8a88e687f055be6135cbabf914d974d6486e8dfaa38679/probability-inspect-f269237f84df.json`.
- Event 026 partial trace source revision: `6628682c3ab8ea938f359dd6217f915377950ff27b4b786a813733d97f94146c`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fae84ace8257f30e0c16ff1451b477a7d4d22e80f5389e1b117a0b6bb6dad074/241f3ffb0280bad438096b9748a24a6bbadc83f7ac67be75fab45aef1f3481ed/event-trace-6628682c3ab8.json`.

Black Friday's sale achievement requires `black_friday_is_active` when `black_friday_record_achievement_transaction` runs, but these raids prepare for 5, 30, or 45 days and the sale lasts one day. The installed native raid documentation exposes no creation or cancellation callback that can record a paid reservation and unwind it after cancellation. Sale variants retain the discounted native reservation and set Japan campaign purchase history on outcome; they do not produce a Black Friday achievement transaction. The visibility of a prepared sale-tier raid after the sale ends, cancellation/target-loss stock handling, and live AI selection require engine verification. An eventual achievement bridge should rely on a proven native reservation/cancellation receipt rather than award on mere preparation.

Specifically, `common/raids/_documentation.md` says `essential_equipment` is collected after raid creation but documents only the four `success_levels` outcome hooks, not a creation or cancellation effect. `black_friday_achievement_is_valid_sale` in `common/scripted_triggers/026_black_friday_triggers.txt` requires an active natural sale, and `black_friday_record_achievement_transaction` in `common/scripted_effects/026_black_friday_effects.txt` requires a unique transaction id, cost family, ordinary cost, and paid cost after a proven debit. A static sale-tier marker in the later outcome proves which raid variant was chosen; it does not prove the original transaction id, cancellation status, or the paid receipt under that helper's contract. Recording on outcome would usually be after the one-day sale and could misattribute a delayed launch to a later sale. The history flags are therefore not treated as achievement receipts.

No new icons were needed. The chemical raid reuses `GFX_decision_japan_chemical_campaign_attack` in `interface/chaosx_gfx_cleanup.gfx`; biological raids reuse `GFX_raid_type_icon_anthrax_strike` and their agent equipment icons. Future work is limited to the achievement bridge and engine validation above.

## Country-root bridge and remaining limits

Native `actor_effects` start with raid-instance `ROOT`. All 120 Japan outcome callbacks now save chain-local regular targets for the exact actor, victim, selected state, agent, price tier, and outcome, then fire `chaosx_japan_cbrn_raid.1` or `.2` immediately under the actor country. The hidden event checks exact-one markers per family and selected-state control, reconstructs temporary inputs, and runs the whole chemical or biological transaction with country `ROOT`. No country-global pending scalar or delayed callback is used, so simultaneously prepared raids cannot overwrite one another's receipt. A source audit found all 30 IDs and 120 callbacks mapped correctly and no global event-target writer for the Japan marker prefix. These source and offline-documentation checks are not live engine proof of regular target propagation.

Fresh `hoi4.probability_inspect` on `common/raids/japan_cbrn_campaign_raids.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, even though raid `ai_will_do` and success factors exist. Source revision `0bf8c42a7a5830348e0832444fed4c04195458b5fcb9a9b088efa3bff8587d12`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1d6b1b5876b3fea4d503beb226532cfa224ee58e146cb69184dec268dd91e14c/2dbc31d3929b9d5732aefa2ed0de314c035f9857625e791d8d8e07b8ac0a2c6f/probability-inspect-fee3ae116752.json`. Narrow Event 026 trace again returned `EVENT_INSPECTED_PARTIAL` because workspace-wide helper and lifecycle passes were deferred. Its source revision was `316825c8445e7868f05adbf83dd97f211030552e30b1ca364eb0c1b0084471fd`; no blocking diagnostic was reported, and the partial trace is not engine proof.

Fresh `hoi4.event_inspect` traces for bridge events `.1` and `.2` also returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics and a 64-path inline inventory limit; the linked reports are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7acf6526b82e9bae9c11ad3e2fea1f58c361bb5ca38e28c01b7d85ed316f3244/a182c2c261f3b42ebab851795e3fe24c9022ef2ea15c69480784f1ee413a4306/event-trace-f4c3e836d079.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e2461d88ea25265b85805593a09ac1fe44b63e3c40e599322ef3876cf87056b/c82ab1239a98f32176066b1b3ed579b868685d77c2a33b2a94d0d697276bed3d/event-trace-70f0dc4645cc.json`. The installed MCP has no native raid adapter for preparation, targeting, or equipment reservation.

The `.1` bridge scope render returned `EVENT_RENDERED_PARTIAL` at source revision `53cfc668c05d032d7d279e9e9b3ddd7bfd6852cc288bbd5c857f7600bc679964`, with the same deferred helper/lifecycle coverage and no blocking diagnostic; manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f46d43962502e9854823d30d9230f6330efcf0bd84e3ada9da0f82e0dd861df/20a2fb95250261c391ea7e69970d2c58bb7bfc35e66ce218ae44bcc1c450c9cd/event-scope-53cfc668c05d-manifest.json`.
