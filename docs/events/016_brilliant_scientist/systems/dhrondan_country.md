# Empire of D’Rhonda country runtime

## Purpose

The Empire of D’Rhonda is a fixed dormant country tag that can emerge from the D’Rhondan pact rebellion owned by Events `chaosx.nr16.40` through `.47`.

The country package owns tag setup, route identities, state transfer, force conservation, country initialization, political leaders, advisors, commanders, reclamation and integration decisions, diplomatic compact events, country AI, Event 016 detail text, and the alternative completion path for the existing `Not From Here` achievement.

The national focus tree, reusable alien-infantry API, contact-event definitions, Event 019 migration, binary art, flags, icons, portraits, model, audio, and event catalog are separate ownership surfaces.

## Revolt transaction

Event `.47` calls `dhrondan_start_revolt = yes` in the pact-host country scope through the contact package’s one-shot bridge.

The runtime proceeds as one guarded transaction:

1. It requires at least one host-owned, passable state carrying `dhrondan_landing_state`.
2. It records the pact host, the first host-controlled and passable marked capital when one exists, then falls back to the first host-owned and passable marked state even if a third party controls it.
3. It counts every state carrying `dhrondan_landing_state`, including markers no longer owned by the pact host, then calculates the ordinary opening force as `max(5, min(15, marked_states + floor(arrivals / 2)))` with a subtract-by-two loop, so no rounding mode can change the result.
4. It adds a DHR core to the selected capital and releases DHR if the fixed tag is not active.
5. Because the engine’s `release` effect removes a releasing-country core from transferred release states, it immediately restores the origin host core on the released capital.
6. It adds a DHR core to every other marked state still owned by the host and restores the origin host core after transfer.
7. A host-controlled marked state uses `transfer_state_to = DHR`, changing owner and controller together.
8. A marked state controlled by a third party uses `set_state_owner_to = DHR`, changing ownership while preserving the existing occupier.
9. Every marked state not owned by DHR after the transfer pass receives a DHR claim.
10. A newly released or re-released DHR receives the selected viable marked capital.
11. Only after DHR exists and owns the selected state does the runtime set the contact bridge’s success receipt.
12. Every surviving host division using the locked `D’Rhondan Landing Cohort` template is deleted with `disband = no`, so no equipment returns to the host.
13. Every `alien_laser_weapon_equipment_1` unit remaining in the host stockpile is sent to DHR.
14. DHR reloads `dhrondan_focus_tree` while preserving completed DHR focuses, restores its regime and leader, restores the sovereignty contact receipt, and reconciles the shared alien-infantry API.
15. The first successful formation receives one-time expedition stores equal to 2,000 laser weapons per ordinary calculated cohort and consumes those stores through the shared locked-cohort API.
16. The runtime uses `is_in_home_area = no` plus repeated DHR `every_owned_state` passes whose frontier test is `any_neighbor_state` to group passable DHR-owned and DHR-controlled states into unique components in the engine’s state-neighbor graph. Each component containing a marked landing state receives one cohort before the remaining cohorts are placed in the capital.
17. If the ordinary capped reserve is exhausted while an uncovered component remains, the one-time formation path grants exactly one supplemental 2,000-weapon reserve for that component, records it in `dhrondan_initial_enclave_floor_extensions`, and consumes it through the same API. Supplemental reserves are created only inside the component-first pass, so they cannot increase the later capital concentration.
18. The formation news event fires once, and the Event 016 details text gains a sovereignty aftermath paragraph.

The fixed tag, startup character registry, global opening-grant receipts, and global initial-force receipt make later uprisings and release after annexation idempotent.

Later host rebellions transfer their marked states and laser stockpile into the active DHR tag, add claims for lost marked states, and do not repeat the opening political-power grant, stability reset, war-support reset, news event, expedition stores, or initial cohort package.

Because each controlled disconnected component contains at least one marked state, the ordinary formula supplies enough cohorts to cover every such component whenever there are at most fifteen components.

The user-approved enclave precedence rule resolves the former extreme-case conflict: fifteen remains the ordinary force cap, but a revolt with more than fifteen viable disconnected components receives only the additional costed cohorts required to seed those components. The persistent extension counter proves exactly how far the opening force exceeded its normal cap.

## Country identity and politics

The dormant history file uses state `1` only as the engine bootstrap capital.

The first committed revolt replaces it before DHR is presented as an active country.

`western_european_gfx` and `western_european_2d` are deliberate engine-base graphical cultures because the package’s country UI still consumes the standard terrestrial equipment, diplomacy, construction, and interface families.

The alien unit entity, counters, portraits, flags, equipment icons, event art, decisions, and focus icons are separately bespoke, so this engine-base inheritance is not a substitute for missing D’Rhondan art.

The three exclusive political outcomes are:

- `DHR_IMPERIAL`: Emperor Vael IX, non-aligned Imperial Continuity.
- `DHR_SYNOD`: First Calculant Sera Qel, neutrality-mapped Predictive Synod with a distinct cosmetic identity.
- `DHR_COVENANT`: Speaker Ilyr Ren, democratic Two-World Covenant.

No fascist or communist D’Rhondan regime is installed by the runtime or focus package.

The fixed roster contains the three regime leaders, five civilian advisors, one high-command advisor, and three corps commanders.

All twelve characters are recruited once by the dormant DHR country-history file and are never recruited from a general-history block or the revolt effect.

## Decisions and diplomatic events

The `dhrondan_sovereignty_category` contains four targeted surfaces:

- `dhrondan_reclaim_landing_site` prepares a take-state war goal for a marked DHR claim held by another country and keeps that state unavailable for a duplicate demand until the war-goal authorization expires.
- `dhrondan_establish_enclave_supply_bridge` supports a controlled landing enclave outside the capital’s home area and resolves the crisis once every such enclave is bridged.
- `dhrondan_integrate_reclaimed_landing_site` adds a DHR core to a recovered marked state and records postwar integration.
- `dhrondan_offer_two_world_compact` sends a formal recognition and non-aggression proposal to a valid partner after the Covenant integration route begins; a government that has already ratified a compact cannot be targeted again.

Country event `.49` owns the compact recipient’s accept and refuse options, marks the DHR offer as delivered before the recipient responds, `.50` reports ratification to DHR, `.51` reports refusal, and hidden `.52` clears an offer receipt only when delivery becomes invalid.

The active receipt remains set while a delivered player popup is awaiting an answer, so a delayed multiplayer response cannot reopen a duplicate compact offer.

These events are country follow-ups, not Event 016 evolutions.

The package does not change Event 016’s exactly four logged evolutions or its no-cluster status.

The shared event log continues to treat the root Event 016 history row as Doctor Kruger’s arrival and therefore keeps the accepted Kruger host as its actor.

DHR formation does not rewrite that historical actor to the later-created alien country.

Instead, the existing Event 016 Event Details entry appends the sovereignty aftermath after `dhrondan_sovereignty_formed`; events `.48` through `.52` remain consequence popups under the same root event rather than new random-event catalog rows.

The existing `Not From Here` achievement accepts either its original Kruger provenance proof or a completed DHR sovereign route with postwar integration and a concluded Two-World Compact.

No achievement entry was added, so Event 016 retains exactly 17 achievements.

## AI behavior

The focus-owned `016_dhrondan_focus_ai.txt` is the sole national-focus plan surface: its opening plan hands off to three mutually exclusive route plans that prioritize each regime’s political settlement, support lanes, matching world-order branch, postwar integration, enclave resolution, and final sovereign capstone.

Three route strategy surfaces give Imperial Continuity an infantry-heavy force preference, the Synod a more armor-weighted predictive army, and the Covenant a broader infantry, mountain, and marine composition.

Decision weights favor urgent enclave support, systematic integration, Imperial reclamation, and Covenant diplomacy.

Compact acceptance and refusal use distinct opinion and government modifiers rather than a fixed outcome.

## Assets and stable wiring

The country package consumes these sprites and runtime paths:

- Formation news event: `GFX_news_event_016_dhrondan_sovereignty`.
- Diplomatic report event: `GFX_report_event_016_dhrondan_diplomatic_compact`.
- Sovereignty decision category: `GFX_decision_category_dhrondan_sovereignty`.
- Reclamation decision: `GFX_decision_dhrondan_reclamation`.
- Enclave supply decision: `GFX_decision_dhrondan_enclave_supply`.
- State integration decision: `GFX_decision_dhrondan_state_integration`.
- Two-World Compact decision: `GFX_decision_dhrondan_two_world_compact`.
- Portrait sprites: `interface/016_dhrondan_portraits.gfx`.
- Full portraits: `gfx/leaders/DHR/`.
- Advisor, high-command, and commander cards: `gfx/interface/ideas/016_dhrondan/`.
- Base and cosmetic flags: `gfx/flags/DHR*`, `gfx/flags/medium/DHR*`, and `gfx/flags/small/DHR*`.

The portrait asset handoff records which fictional ImageGen portraits are parent-approved and which nonleader cards still need final user visual review.

## Inspection evidence and current blockers

The installed HOI4 MCP exposed callable `hoi4.event_inspect`, `hoi4.event_compare`, and `hoi4.map_inspect` routes during final review.

A focused `.49` trace later returned `EVENT_INSPECTED_PARTIAL` at revision `641888481c1a01768798a266ac9e444348a73e8b0b9e1cbe5b49f9e413cd06f6`, graph hash `0116289c85b9d780e6cfc0bf50a7a9d678190ebc8c668e1e1a53fdd1e5634ad1`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1aec799e1f17c63d02911a6fffa3c04d68e4dda0fa68cef7272b57a7e6583ce4/ad77d3b9bc1cd1722e8f0e26f77ca1e2e7a74e4c427071bec178612fd0903f30/event-trace-641888481c1a.json`.

The file-scoped event scan and render overview each timed out after 180 seconds, and the partial trace deferred workspace-wide helper and lifecycle projections.

The map inspector also timed out after 180 seconds when limited to the dormant bootstrap state `1`.

Event comparison requires a meaningful before/baseline revision pair, which this new file never had, so no valid event comparison could be produced.

No separate runtime state-transfer inspect or compare route was exposed, and no declarative map source was changed for a `map_rewrite` operation.

The offline Paradox wiki’s `release` effect reference explicitly states that owned-but-not-controlled states transfer to the released country without becoming controlled by it, and its state-effect reference states that `set_state_owner_to` changes owner but not controller.

Those documented engine semantics close the occupied-capital controller question: both initial release and later ownership-only transfers preserve a third-party occupier.

The same `release` reference states that the releasing country loses its core on a transferred release state; the runtime compensates by restoring the origin host core on the released capital and after every explicit marked-state transfer.

MCP state-transfer comparison evidence remains unavailable because the map route timed out and the server exposed no separate runtime state-transfer inspect/compare route, but this is now an evidence-route limitation rather than an unresolved controller semantic.

The shared alien-infantry API honors `alien_infantry_initial_force_mode = 1` only when `alien_infantry_landing_batch_mode = 1` and the calling country holds a positive D’Rhondan sovereignty receipt.

The country runtime sets both temporary inputs only inside `dhrondan_deploy_initial_cohorts`, checks `alien_infantry_landing_spawn_succeeded` after each call, persists the remaining cohort count, and clears both inputs before returning.

The narrow API branch retains target validation, exact 2,000-weapon debit, unit creation, materialization proof, failure refund, and success output.

It skips only `dhrondan_arrival_count`, `dhrondan_alien_presence`, `dhrondan_pact_strain`, `dhrondan_landing_history_count`, and `dhrondan_record_successful_landing`, so the sovereignty allocation does not masquerade as new pact-host arrivals or re-enter rebellion presentation.

## Future extensions

Future D’Rhondan content can add negotiated enclave access, recognition blocs, homeworld communications, and integration outcomes that distinguish occupied, reclaimed, and voluntarily associated landing states.

Any extension should preserve fixed-tag idempotence, the shared alien-infantry API, the exact equipment debit, host-core preservation, third-party occupation preservation, the three political mappings, and the existing Event 016 achievement and evolution counts.
