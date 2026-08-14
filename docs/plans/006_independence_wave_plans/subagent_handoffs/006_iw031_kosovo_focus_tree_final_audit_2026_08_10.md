# IW-031 Kosovo shared-focus integration final audit — 2026-08-10

## Scope and verdict

This is the final active focus-tree audit for Event 006 IW-031 Kosovo (`KOS`). The audit covers the shared `independence_wave_focus_tree`, the five Kosovo package hooks, full-framework assignment and carrier protection, route reachability, reward and AI alignment, focus icons and localisation, and idempotence with the Kosovo decisions.

The current source satisfies the requested integration contract. IW-031 uses the full shared framework exactly once, exposes one reachable Kosovo package hook in each requested lane, has no Kosovo-specific or additive focus tree, and preserves the meaningful-vanilla-tree boundary through the central generic-focus contract. No bounded gameplay patch was necessary, so the existing concurrent source edits were left untouched. This handoff is the only file changed by this audit; no gameplay file was committed or staged.

## Route coverage

| Requested lane | Shared focus id and source | Kosovo hook | Reachability and reward evidence | Result |
| --- | --- | --- | --- | --- |
| Administration | `independence_wave_prepare_capital_administration` (`common/national_focus/006_independence_wave_focus.txt:99-118`) | `independence_wave_kos_focus_convene_assembly` at line 114 | The focus is available under `can_use_independence_wave_full_focus_framework`; it calls the assembly hook once. The hook raises Civic Concord and Municipal Reach, then applies the shared administration reward and sets `independence_wave_kos_assembly_convened` (`common/scripted_effects/006_independence_wave_kosovo_package_effects.txt:206-215`). | Covered, reachable, and idempotent. |
| Community | `independence_wave_inventory_the_state` (`common/national_focus/006_independence_wave_focus.txt:139-159`) | `independence_wave_kos_focus_guarantee_communities` at line 155 | The focus has the capital-administration prerequisite and full-framework availability. The hook raises both public ledgers, applies `independence_wave_focus_reward_public_settlement`, and sets `independence_wave_kos_communities_guaranteed` (`common/scripted_effects/006_independence_wave_kosovo_package_effects.txt:217-226`). | Covered, reachable, and idempotent. |
| Military | `independence_wave_bind_the_first_oath` (`common/national_focus/006_independence_wave_focus.txt:161-181`) | `independence_wave_kos_focus_integrate_territorial_guards` at line 177 | The focus has the capital-administration prerequisite and full-framework availability. The hook raises Municipal Reach and Civic Concord, applies `independence_wave_focus_reward_security_reform`, and sets `independence_wave_kos_guards_integrated` (`common/scripted_effects/006_independence_wave_kosovo_package_effects.txt:228-237`). | Covered, reachable, and idempotent. |
| Former host | `independence_wave_define_former_host_policy` (`common/national_focus/006_independence_wave_focus.txt:1399-1415`) | `independence_wave_kos_focus_settle_yugoslav_ledgers` at line 1407 | The focus requires `independence_wave_complete_founding_settlement`, full-framework use, and an unsettled host relation. The hook raises both public ledgers, applies the bilateral host settlement only when the former host is usable, progresses the shared host ledger in that branch, and sets `independence_wave_kos_host_ledgers_settled` (`common/scripted_effects/006_independence_wave_kosovo_package_effects.txt:239-252`). | Covered, reachable, and idempotent. |
| Network | `independence_wave_recognize_fellow_new_states` (`common/national_focus/006_independence_wave_focus.txt:1669-1685`) | `independence_wave_kos_focus_open_balkan_corridor` at line 1677 | The focus requires founding settlement completion and `can_participate_in_independence_wave_network_focuses`, which requires an active network member and no client lock (`common/scripted_triggers/006_independence_wave_focus_triggers.txt:340-344`). The shared focus grants network cooperation and the Kosovo hook opens the corridor once and adds the package ambition reward (`common/scripted_effects/006_independence_wave_kosovo_package_effects.txt:254-261`). | Covered, reachable, and idempotent. |

The five Kosovo helper call sites occur exactly once each in the shared focus source. There are no additional Kosovo hooks, KOS-specific focus IDs, or duplicate route branches in `common/national_focus/006_independence_wave_focus.txt`.

## Full-framework assignment and vanilla-tree protection

`independence_wave_setup_iw_031_kosovo` sets the temporary assignment input to `independence_wave_focus_assignment.full_framework` and calls `independence_wave_assign_focus_framework` (`common/scripted_effects/006_independence_wave_kosovo_package_effects.txt:263-304`). The assignment effect sets `independence_wave_full_focus_framework` and `independence_wave_generic_focus_tree_assigned`, loads `independence_wave_focus_tree` with `keep_completed = no`, and marks the layout dirty (`common/scripted_effects/006_independence_wave_focus_effects.txt:33-84`).

The additive branch never calls `load_focus_tree` and fails closed without a reviewed carrier (`common/scripted_effects/006_independence_wave_focus_effects.txt:63-82`). The only registered additive carriers are ICE, IW-023, and BOS with an Austro-Hungarian owning tree (`common/scripted_triggers/006_independence_wave_focus_triggers.txt:70-87`); KOS is not an additive carrier. The central finalization barrier requires `has_independence_wave_generic_focus_contract` and `independence_wave_generic_ai_profile` before accepting any package (`common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:41-80`). The generic contract itself requires the full-tree flags and `has_focus_tree = independence_wave_focus_tree` (`common/scripted_triggers/006_independence_wave_focus_triggers.txt:55-68`).

The IW-031 static admission proof is dormant `original_tag = KOS` with capital state 802, a distinct living owner, and the anchor-availability predicate (`common/scripted_triggers/006_independence_wave_package_triggers.txt:150-164`). No KOS `focus_tree`, country-specific tree, or KOS `shared_focus` import exists in `common/national_focus/`. Vanilla supplies KOS through the default `generic_focus` tree (`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/generic.txt:18-29`), so replacing it during the explicitly admitted IW-031 release does not discard a meaningful KOS-specific vanilla tree.

## Icon coverage

| Focus id(s) | Icon id | Shine sprite | Evidence | Result |
| --- | --- | --- | --- | --- |
| `independence_wave_prepare_capital_administration`, `independence_wave_name_provisional_authority`, `independence_wave_establish_permanent_ministries` and related administration nodes | `GFX_goal_independence_wave_founding_administration` | `GFX_goal_independence_wave_founding_administration_shine` | `interface/006_independence_wave.gfx:3-4` | Present and valid. |
| `independence_wave_inventory_the_state`, `independence_wave_restore_regional_communications` and related infrastructure nodes | `GFX_goal_independence_wave_infrastructure_authority` | `GFX_goal_independence_wave_infrastructure_authority_shine` | `interface/006_independence_wave.gfx:19-20` | Present and valid. |
| `independence_wave_bind_the_first_oath` and related security nodes | `GFX_goal_independence_wave_army_integration` | `GFX_goal_independence_wave_army_integration_shine` | `interface/006_independence_wave.gfx:17-18` | Present and valid. |
| `independence_wave_define_former_host_policy` and its settlement family | `GFX_goal_independence_wave_former_host_settlement` | `GFX_goal_independence_wave_former_host_settlement_shine` | `interface/006_independence_wave.gfx:21-22` | Present and valid. |
| `independence_wave_recognize_fellow_new_states` and its league family | `GFX_goal_independence_wave_league_congress` | `GFX_goal_independence_wave_league_congress_shine` | `interface/006_independence_wave.gfx:23-24` | Present and valid. |

Shared lane icons intentionally repeat within their lane; no KOS-specific focus icon is required because IW-031 has no bespoke focus nodes. The MCP focus diagnostics did not report any icon error in `mod:common/national_focus/006_independence_wave_focus.txt`.

## Localisation and reward alignment

All five shared focus titles and custom tooltips are present in `localisation/english/006_independence_wave_focus_l_english.yml`: `independence_wave_prepare_capital_administration` and `_tt` at lines 63-65, `independence_wave_inventory_the_state` and `_tt` at lines 69-71, `independence_wave_bind_the_first_oath` and `_tt` at lines 72-74, `independence_wave_define_former_host_policy` and `_tt` at lines 273-275, and `independence_wave_recognize_fellow_new_states` and `_tt` at lines 329-331.

The Kosovo helper effects are hidden package adapters rather than player-facing focus IDs. Their player-facing decision and mission tooltips are localised in `localisation/english/006_independence_wave_kosovo_l_english.yml`; the existing localisation audit reports complete package-key coverage and no duplicate English keys (`docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw031_kosovo_localisation_audit_2026_08_09.md`).

No reward/name mismatch was found. Administration, community, military, former-host, and network focus descriptions describe the shared lane, while the package adapters add the Kosovo civic-concord, municipal-reach, territorial-guard, host-ledger, and Balkan-corridor outcomes documented by the package spec. The network focus's second network cooperation call is the established package-hook pattern used by the Montenegro and Bosnia adapters and is protected by the Kosovo corridor flag, so it is not an accidental repeat.

## AI behavior

Each shared hook focus has an `ai_will_do` block: administration is urgent with a severe-instability boost, community is urgent, military is urgent with a wartime preference, and former-host/network are high with a founding-settlement prerequisite boost (`common/national_focus/006_independence_wave_focus.txt:117-118`, `158-159`, `180-181`, `1408-1414`, `1678-1684`). The KOS setup publishes all four government-route availability flags and the league route before completing setup (`common/scripted_effects/006_independence_wave_kosovo_package_effects.txt:281-295`), so the route-aware shared AI branches remain available to the KOS package.

The package adds four source-declared AI strategy blocks for municipal survival, host restraint, settled compact, and emergency guard (`common/ai_strategy/006_independence_wave_kosovo.txt:15-63`). No AI weight was changed by this audit, so no new probability comparison was required. The existing probability handoff records an MCP transport blocker for the focus and strategy adapters; exact scenario ranking and timing remain unresolved rather than being inferred from source scores (`docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw031_kosovo_probability_audit_2026_08_09.md`).

## Idempotence with decisions

Every package hook has a one-shot country flag guard in `common/scripted_effects/006_independence_wave_kosovo_package_effects.txt:206-261`. The administration, community, and military hooks are each called by one shared focus and one matching Kosovo project decision (`common/decisions/006_independence_wave_kosovo_decisions.txt:43-90`). The former-host helper is called by the normal ledger project and the host-loss cancellation branch (`common/decisions/006_independence_wave_kosovo_decisions.txt:93-109`); its `independence_wave_kos_host_ledgers_settled` guard prevents duplicate ledger changes. The network helper is called by the shared focus and by the corridor project before the separate project settlement reward (`common/decisions/006_independence_wave_kosovo_decisions.txt:188-201`), and its corridor flag makes the hook idempotent while preserving the paid-project reward.

## MCP focus evidence

The mandatory `hoi4.focus_inspect` call succeeded for `independence_wave_focus_tree` at `common/national_focus/006_independence_wave_focus.txt` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5a20f0ef65abfb495902c2b4f47297b95411042046fbff95606090f7e2455de6/27fc4c772620b89e9e9442a64ac2a28847c37666ab6ca321ec7de34b90831af0/focus-inspect.8f5919065cc7e0ff.json`.
- The tree resolved 184 focuses and 193 connectors with zero connector crossings and zero node intersections. The stable layout has one 13-column connector, from `independence_wave_adopt_military_archetype_program` to `independence_wave_preserve_independent_command`, outside the five IW-031 hook nodes.
- The normal inspect emitted five source-tree layout warnings for unrelated generic-tree detours and one long connector. The 14 blocking icon diagnostics refer to the installed vanilla `generic_focus` continuous palette, not Event 006 focus nodes; no KOS hook was named by a blocking diagnostic.

The mandatory `hoi4.focus_render` call also succeeded for the same tree.

- HTML artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb40f2bfb9a1333fa26ada4991a5b0b787d21d4fe3ea999e62e0b7cdbd3c5ec6/a737dab4c79db76a3760c1ff74df53f2e3deefb4814c52dd5487055cc55ddd2e/independence_wave_focus_tree.focus.html`.
- SVG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99315e3b89510ee95475cdcaa004b6120834db4ffe96f9ca9e101b1bae25ff3e/26db3df90e1c4901e2911e7bd2a08d303d38be6322f5adf1b66c62453b741db9/independence_wave_focus_tree.focus.svg`.
- JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d23283cd907667a7eac25c1c7fcc2871c7b0e29c5055563acee751a168929faf/5cb67130c18084bde142bd85d2500cd9866434770c5840ada2a2d0d7958c0d9/independence_wave_focus_tree.focus.json`.
- Render output preserved the same layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a` and the same five unrelated layout warnings plus the external vanilla continuous-focus icon diagnostics.

## Missing, simplified, or blocked content

- No requested administration, community, military, former-host, or network hook is missing or simplified in the shared tree.
- No KOS-specific focus tree or additive carrier was introduced or found.
- No KOS-specific focus icon is missing; the five shared icons and their shine sprites are registered.
- Exact focus and strategy AI rankings remain unresolved because the existing probability adapter transport receipt is blocked; no balance claim is made from source scores alone.
- The 14 MCP blocking icon diagnostics belong to vanilla `common/continuous_focus/generic.txt` and are outside the Event 006 focus ownership. They should not be repaired in this IW-031 handoff.
- Central Event 006 attestation remains outside this bounded focus audit and should stay closed until the parent reconciles the existing country, portrait, decision, AI, and completion handoffs.

## High-priority follow-up

1. Restore the probability adapter transport and rerun the named IW-031 focus and strategy scenarios through `chaosx_ai_probability_auditor`; preserve a baseline and comparison if any AI weight is later changed.
2. Keep the central generic-focus finalization barrier in place and do not convert KOS to an additive carrier without a reviewed owning tree.
3. Leave the unrelated vanilla continuous-focus icon diagnostics to their own owner; changing them here would expand the task beyond IW-031.

## Changed files, identifiers, and validation

Changed files: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw031_kosovo_focus_tree_final_audit_2026_08_10.md` only.

Changed focus ids: none. Audited ids: `independence_wave_prepare_capital_administration`, `independence_wave_inventory_the_state`, `independence_wave_bind_the_first_oath`, `independence_wave_define_former_host_policy`, and `independence_wave_recognize_fellow_new_states`.

Changed localisation keys: none. Changed icon ids: none.

Meaningful validation run: mandatory `hoi4.focus_inspect` and `hoi4.focus_render` both succeeded against the current worktree; source scans counted exactly one call site for each of the five KOS hook helpers, confirmed zero KOS-specific focus-tree definitions, matched all five focus title/tooltip keys, matched every icon with a shine sprite, and matched every focus hook with its idempotent decision consumer.

Skipped validation: no `hoi4.focus_rewrite` was used because no gameplay patch was required; no new probability inspection or compare was run because no AI weight changed and the existing IW-031 probability handoff documents the adapter transport blocker; no live HOI4 launch was performed because consumer validation belongs to the user.

Plan handoff path: none. This audit did not identify a broader route-depth or design gap requiring `docs/plans/<event>_<slug>_plans/` expansion beyond this handoff.

Remaining route risks are limited to unresolved typed AI ranking evidence, the external vanilla continuous-focus diagnostics, and the parent-owned central attestation gate; none is a missing or unreachable IW-031 shared-focus hook.
