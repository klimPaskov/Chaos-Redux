# Event 006 decision and mission surface re-audit

Date: 2026-09-02

Scope: Decision categories, player-facing decisions/missions, custom-cost localisation, lifecycle gates, and the two Event 006 scripted GUI surfaces relevant to the reported pre-event leakage and bloated decision-cost surface.

Disposition: PATCHED (one-line gate); no mechanic or localisation redesign was applied.

## Executive conclusion

The source-level Event 006 audit finds no player-facing Independence Wave category, pressure value, mission, queue, cost, or pre-event crisis indication before `chaosx.nr6.1` commits the event. The root event is hidden and trigger-only, the retired `.3` callback only cleans stale crisis state, and the 88 registered categories are now closed either by `is_independence_wave_active_country` directly or by the shared player-surface helper.

The narrow source gap was in `is_independence_wave_event6_player_surface_allowed`: it excluded Event 021 adapter receipts but did not itself require the canonical active-origin flag. I added that predicate in the working tree, so all 33 helper-gated categories now transitively require the active Event 006 origin as well as the 55 categories that gate directly.

This is source-level proof, not an absolute engine proof. The Event MCP inspection/render completed only as a partial large-workspace projection, and the valid GUI inspect calls hung until terminated; the exact blockers are recorded below. No direct decision or mission inspection route is exposed by the installed HOI4 MCP tool set.

## Severity-sorted issues

### P1 — shared player-surface helper needed the canonical active-origin gate — fixed locally

File: `common/scripted_triggers/006_independence_wave_triggers.txt`.

Identifier: `is_independence_wave_event6_player_surface_allowed`.

Before this audit, the helper rejected `random_civil_war_event6_adapter_preparing`, `random_civil_war_event6_adapter_complete`, `random_civil_war_origin_adapter_complete`, and `independence_wave_event021_adapter_setup_proven`, but it did not require `is_independence_wave_active_country = yes` itself.

After this audit, the helper begins with `is_independence_wave_active_country = yes` and retains all four adapter exclusions.

This is a one-line gate-only repair and does not change Event 006 effects, costs, timers, AI, or adapter mechanics.

Integration hazard: the current staged index contains concurrent broad edits that remove strict active-origin/helper gates from category wrappers and the trigger registry, while the working tree retains the strict gates plus this audit line. Do not replace the current working-tree gate behavior with that staged version during parent integration.

### P1 — selected formable commit cost is mechanically over-budget and incomplete — not locally safe to patch

Decision: `independence_wave_proclaim_military_union` (DM-55) in `common/decisions/006_independence_wave_decisions.txt`.

Effect: `independence_wave_formable_pay_selected_commit_cost` in `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` first calls `independence_wave_decision_pay_strategic`, then calls administration-standard for civic/negotiated methods, security-standard for revolutionary methods, or security-major for military and hidden high-chaos methods.

Trigger: `can_pay_independence_wave_strategic_cost` reserves civilian factories, stability, and the diplomatic standard palette, while the security predicates add manpower, army experience, infantry equipment, and support equipment.

Localisation: `localisation/english/006_independence_wave_formable_registry_l_english.yml`, keys `independence_wave_formable_commit_cost_civic`, `independence_wave_formable_commit_cost_revolutionary`, and `independence_wave_formable_commit_cost_military`.

The revolutionary and military rows expose seven spendable families when transport is counted as one alternative family, while the effect also requires the strategic civilian-factory reservation that those rows do not show. Adding the factory icon alone would make the already over-budget surface worse, and hiding an existing value would make the cost text inaccurate. This requires an owner-level decision about the canonical payment palette, followed by coordinated changes to the trigger, payment effect, base/blocked/tooltip localisation, and likely the dynamic cost helper.

### P2 — category density remains high in route-gated phases

Source counts are founding 5, government 6, recognition 6, security 7, host relations 7, patron 8, network 7, league 6, borders 5, formables 4, high chaos 3, and scenario ledger 3 visible primary actions before route-specific gating.

The categories above six are not pre-event leakage by source proof, but they need scenario fixtures and a full GUI state matrix before a visual-density claim can be closed. League and formable surfaces also expose several dynamic values that need a clearer significance audit.

### P2 — direct decision/mission engine inspection is unavailable

The installed MCP exposes event, focus, GUI, map, technology, and probability routes, but no `hoi4_decision_inspect` or `hoi4_mission_inspect` route. Event 006 was therefore checked through source inventories and the available event graph projection, with the limitation retained rather than treated as equivalent engine evidence.

### P3 — stale specialised cost localisation may be dead

`independence_wave_cost_security_standard_factory` and its blocked/tooltip rows remain in `localisation/english/006_independence_wave_decisions_l_english.yml`, but the focused active decision scan found no current `custom_cost_text` caller for that specialised key. Remove it only after an indirect scripted-localisation/reference proof confirms it is unused; it was not changed here.

## Decision category lifecycle notes

There are 88 Event 006 first-level category blocks in `common/decisions/categories/006_independence_wave_categories.txt`, and all 88 category identifiers referenced by decision files resolve in the registry.

Fifty-five category blocks contain `is_independence_wave_active_country = yes` directly.

Thirty-three category blocks use `is_independence_wave_event6_player_surface_allowed = yes`; the repaired helper now requires the active origin and excludes all known Event 021 adapter receipts.

No category lacks both a direct active-origin gate and the shared runtime helper in the current working tree.

`events/006_independence_wave.txt` keeps `chaosx.nr6.1` hidden and `is_triggered_only = yes`. Its global `independence_wave_event6_runtime_unlocked` overlay flag is set only after the joint or standalone root commits, so it is not a pre-event publisher.

The retired `chaosx.nr6.3` callback clears stale crisis flags and variables and does not launch the wave, apply pressure, create a queue, or expose a category.

The bounded Event 021 adapter may still use package-content helpers for internal setup, leaders, forces, and auto missions. Those adapter-internal activations are not player-facing because the category/helper gate and overlay runtime gate remain closed without the active Event 006 origin.

A focused source scan found zero legacy pre-event, pre-wave, crisis-category, crisis-pressure, or crisis-mission hits in Event 006 decision, category, and localisation files.

## Cognitive-load notes

The category counts above include state/phase and route gating, so they are a source inventory rather than a claim that every action is simultaneously visible in one live fixture.

The status scripted GUI presents legitimacy, recognition, capacity, security, and instability through labelled state frames rather than a raw pre-event pressure row. Its render still reports non-blocking overlap/clipping and static-animation fallback diagnostics, which are existing GUI-quality follow-ups rather than leakage fixes.

The formable commit surface is the clearest cost-cognitive-load defect because its revolutionary and military rows combine stability, command power, dynamic transport, manpower, army experience, infantry equipment, and support equipment, while the payment effect also reserves civilian factories. The player cannot reliably infer the true spend from the visible row.

The generic blocked formable cost string `independence_wave_cost_selected_formable_commit_blocked` says the method, carrier, member consent, and material requirements must be valid, but does not identify which requirement is missing. This is a follow-up localisation improvement after the owner resolves the canonical cost palette.

No visible Event 006 value was found whose source meaning is an unlabelled pre-event pressure counter. Remaining significance gaps are route-specific formable and league value density, not pre-event publication.

## Mission quality notes

The source inventory found 88 decision blocks with `activation` and 86 timed-mission timeout rows/effects.

All 88 activation blocks have a cancellation trigger and a success/completion/removal/timeout contract in the current source inventory.

Two entries, `independence_wave_rival_bloc_coordinate_host_front` and `independence_wave_rival_bloc_balance_patron` in `common/decisions/006_independence_wave_shared_decisions.txt`, are repeatable decisions with `days_remove` and `days_re_enable` rather than timed missions; they are not missing-timeout defects.

Representative mission owners and requirements are the central founding/phase owner in `006_independence_wave_decisions.txt`, package owners such as the Balkan package in `006_independence_wave_balkan_decisions.txt`, FORM03 regional decisions in `006_independence_wave_form03_decisions.txt`, and minor-overlay registries in `006_independence_wave_minor_overlay_decisions_registry.txt` and related files.

Those missions carry owner/category and route or region predicates, package/anchor requirements, constant-backed durations, success or completion effects, failure/timeout effects, cancellation cleanup, and cooldown or one-shot protection where appropriate.

Duplicate risk is primarily hidden adapter-internal auto activation during Event 021 setup, not a player-visible duplicate queue; the helper/category gates prevent that internal path from publishing the Event 006 surface before the root commit.

## Cost and requirement clarity

The focused inventory covers 24 Event 006 decision files, 699 custom-cost call sites, 191 unique custom-cost keys, and 37 English Event 006 localisation files.

All 191 custom-cost keys have base, `_blocked`, and `_tooltip` triplets.

Expansion of the custom-cost aliases and dynamic transport helper found no spendable row lacking a texticon or the approved dynamic transport representation.

The nine native cost rows are three zero-cost scenario-ledger navigation controls and six native political-power conference rows; they are not part of the custom-cost text problem.

The formable DM-55 rows remain the exception at the design level because the rendered palette exceeds the four-distinct-spendable-type limit and omits a required factory reservation in two method branches. Do not paper over this with a localisation-only edit.

## AI validity and route-lock notes

The focused source pass found AI blocks, package predicates, anchor/region checks, and route-lock checks in the Event 006 decision families reviewed.

No invalid or dead country target was found in this narrow pass, and the allocator audit passed its package, anchor, adapter, former-host, and order checks.

No AI weight or probability-bearing code was changed, so no probability compare was required for this patch. The dedicated `chaosx_ai_probability_auditor` route is not callable in this runtime; no quantitative AI/balance claim is made here.

## Localisation and tooltip gaps

Triplet completeness and texticon coverage are clean for the 191 custom-cost keys, and no literal resource names were found in active Event 006 cost rows.

The selected formable blocked text is generic and should become a concise dynamic blocked-reason list after the payment palette is redesigned.

No pre-event crisis category, pressure, mission, queue, or cost localisation remains in the focused Event 006 files.

## Cleanup and exploit-risk notes

The retired `.3` callback only clears stale crisis markers and variables.

The allocator audit found no free-unit/equipment, war-goal, core-spam, or cooldown-loop exploit in this narrow surface pass.

Interrupted Event 021 adapter receipts remain a live-runtime cleanup risk if their proven receipts outlive the intended transaction, but the repaired player-surface helper fails closed for those receipts and does not expose Event 006 categories.

## Concrete recommendations

- Preserve `is_independence_wave_active_country = yes` in `is_independence_wave_event6_player_surface_allowed` and preserve the 55 direct gates and 33 helper-gated category wrappers in the working tree.
- Do not merge the staged index version that removes those strict player-surface predicates without an explicit parent-level lifecycle decision and replacement engine evidence.
- Redesign DM-55 `independence_wave_proclaim_military_union` payment as one canonical four-or-fewer spendable palette per method family, then update `can_pay_independence_wave_strategic_cost`, `independence_wave_formable_pay_selected_commit_cost`, and the three base/blocked/tooltip localisation paths together.
- After the cost redesign, replace the generic `independence_wave_cost_selected_formable_commit_blocked` text with a concise dynamic blocked reason that distinguishes requirements from consumed costs.
- Prove whether `independence_wave_cost_security_standard_factory` is indirectly referenced before removing its stale rows.
- Re-run `hoi4.gui_inspect` and `hoi4.gui_render` with full state coverage for `independence_wave_status_window` and `chaosx_independence_wave_formable_state_puzzle_window` after any GUI or cost-text change.

## Changed files and identifiers

Changed by this audit: `common/scripted_triggers/006_independence_wave_triggers.txt`.

Changed identifier: `is_independence_wave_event6_player_surface_allowed` gained the active-origin predicate.

Before: adapter exclusions only.

After: `is_independence_wave_active_country = yes` followed by the same adapter exclusions.

No decision, mission, scripted GUI, effect, trigger payment, or localisation identifier was otherwise changed by this audit.

The DM-03 anchor-gate and IW-095 cost-text changes visible in the working tree belong to concurrent edits and were preserved without attribution or modification here.

## Evidence and validation

`python -B .tools/audit_event6_allocator.py` passed, reporting the Event 006 allocator/package/adapter/anchor/order audit as clean.

The focused source checks reported 88 category blocks, 55 direct active gates, 33 shared-helper gates, zero ungated category blocks, and zero legacy pre-event source hits.

The cost checks reported 191 custom keys with complete base/blocked/tooltip triplets and zero expanded rows lacking texticons or dynamic transport.

The mission checks reported 88 activation blocks, 86 timeout rows/effects, zero missing cancellation triggers, and zero missing success/completion fields; the two no-timeout entries are repeatable decisions with removal/cooldown fields.

`hoi4.event_inspect` on `chaosx.nr6.1` completed with `EVENT_INSPECTED_PARTIAL`, no blocking diagnostics, and deferred large-workspace helper/lifecycle projections.

`hoi4.event_render` on `chaosx.nr6.1` completed with `EVENT_RENDERED_PARTIAL`, no blockers, and the source-linked overview artifact at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c100e0f3f8d9f49108a3fa57094297982bdb68c98d1cee89419207ec55c8baba/53bbd5b0065476103f4c168f77cbda66355ab9206d50dbcab8b8750415d9c358/event-overview-18bf807c8be3-manifest.json`.

The status GUI render for `independence_wave_status_window` passed validation and produced `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f39bc05763df4fcdef15eca4c0787d3c94531b151c72245e8dbc54cabd8e39bf/6019b81128f01f6d91f13bffaa30cf691284307ae76c86a023803839faecb8aeb/independence_wave_status_window-full.svg`; it reported incomplete state coverage plus non-blocking static-animation, overlap, and clipping diagnostics.

The formable GUI render for `chaosx_independence_wave_formable_state_puzzle_window` passed validation for normal, selected, locked, disabled, completed, and long-text states at 1280x720 and produced `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d202974f6702e6d78f473c71dc4a53874a21ba0aa6996197805f8fa63c769756/d856a88dc7b90ec47600eb16fe2bce48c805bfd3bf22a352dc5fb53c5399cc6e/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

Valid `hoi4.gui_inspect` calls for both known windows and their scenarios hung for roughly 270 seconds and were terminated, so no inspect artifact exists. This is the exact GUI inspection blocker and is not treated as equivalent to source review.

## Remaining issues and simplifications

The DM-55 cost palette remains unresolved and requires owner-level mechanic/localisation coordination.

Category-density follow-up and full GUI inspect/state coverage remain open.

Engine-level proof of every direct decision/mission visibility branch is blocked by the missing decision/mission MCP routes and the terminated GUI inspect calls.

No fallback, invented mechanic, broad category rewrite, or localisation-only concealment was used.

No staging or commit was performed, and all unrelated and concurrent agent edits were preserved.
