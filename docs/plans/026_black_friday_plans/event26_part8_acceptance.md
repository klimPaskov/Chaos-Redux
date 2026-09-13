# Event 26 Part 8 acceptance record

## Evidence boundary

This record is reconciled against the current implementation worktree on 2026-09-02 and is not a claim of completion. `Source` means the relevant script, localisation, registry, or asset path was inspected. `MCP-partial` means the installed HOI4 MCP returned a workspace-wide partial result without a selector-specific blocker. `Live-blocked` means the scenario requires the user-owned live game or multiplayer session. `Calendar-calibration-blocked` means the absolute `global.num_days % 7 == 2` source anchor resolves known Fridays on 3 January 1936, 17 June 1938 (project day 898), and 1 September 1939, but installed Vanilla exposes no weekday trigger or Friday-index precedent and the running engine has not supplied live date progression evidence. `Adapter-blocked` means the final cost registry has no complete owner callsite or engine-accessible route for the scenario; the bounded Communist-spread, Fury, Japan chemical, biological medical-capacity, CBRN shelter, Japan biological, Germany Mengele, and D'Rhondan alien-reserve source tranches have separate bounded adapter status.

Event 26 remains disabled in the default event allowlist until every completion blocker below is resolved.

## Reservation and timing

| ID | Source status | Evidence or blocker |
| --- | --- | --- |
| `BF-T01` | Source; Live-blocked | Event-list status returns `N/A` below 200 Chaos and the reservation trigger requires the threshold; live picker evidence is unavailable. |
| `BF-T02` | Source; Live-blocked | Automatic selection sets the global reservation, rejects the reserved event from later candidate evaluation without mutating its stored weight, and resolves the timer without history or pacing; live timer evidence is unavailable. |
| `BF-T03` | Source; Calendar-calibration-blocked; Live-blocked | The bounded daily pulse activates a reservation when the shared absolute-date helper reports Friday. Known-date arithmetic supports remainder 2, but no installed Vanilla weekday precedent or live date progression closes the acceptance row. |
| `BF-T04` | Source; Calendar-calibration-blocked; Live-blocked | A helper-qualified Friday selection calls the canonical entry and activates in the same transaction; the absolute-date anchor is source-checked, while the Vanilla precedent and live same-day behavior remain unproven. |
| `BF-T05` | Source; Calendar-calibration-blocked; Live-blocked | Natural activation requires current Chaos at or above 200, so a helper-qualified low-chaos Friday is skipped while reservation state remains; the Vanilla weekday precedent and live behavior remain unproven. |
| `BF-T06` | Source; Calendar-calibration-blocked; Live-blocked | The Chaos-change hook rechecks an existing reservation and permits activation on a helper-qualified Friday; the source anchor is checked, while the Vanilla precedent and live behavior remain unproven. |
| `BF-T07` | Source; Live-blocked | Activation defaults to the 50-percent snapshot below the Evolution I threshold; live evidence is unavailable. |
| `BF-T08` | Source; Live-blocked | Activation selects the 75-percent snapshot only when the threshold and Evolution I gate both pass; live evidence is unavailable. |
| `BF-T09` | Source; Live-blocked | The global snapshot is not recomputed by later Chaos changes; live evidence is unavailable. |
| `BF-T10` | Source; Live-blocked | The evolved snapshot is not recomputed by later Chaos changes; live evidence is unavailable. |
| `BF-T11` | Source; Live-blocked | Disable cancellation clears the pending reservation without history; live toggle evidence is unavailable. |
| `BF-T12` | Source; Live-blocked | Re-enable uses the current enabled-country gate and does not restore the canceled reservation; live toggle evidence is unavailable. |
| `BF-T13` | Source; Live-blocked | Disabling an active sale does not clear the snapshot or create a duplicate; live toggle evidence is unavailable. |
| `BF-T14` | Source; Live-blocked | Terminal cleanup clears a reservation; live terminal-state evidence is unavailable. |
| `BF-T15` | Source; Live-blocked | Terminal cleanup expires or removes the active sale on the documented terminal path; live evidence is unavailable. |
| `BF-T16` | Source; Calendar-calibration-blocked; Live-blocked | The central Chaos-change hook can activate later on a helper-qualified Friday after the daily pulse saw low Chaos; the Vanilla weekday precedent and live behavior remain unproven. |
| `BF-T17` | Source; Calendar-calibration-blocked; Live-blocked | Resume invokes the same-Friday activation hook without rebuilding reservation state; the absolute-date anchor is source-checked, while the Vanilla precedent and live pause/resume behavior remain unproven. |
| `BF-T18` | Source; Live-blocked | Reservation and activation are actorless global state and do not depend on the former country tag; live tag-change evidence is unavailable. |
| `BF-T19` | Source; Live-blocked | Evolution toggles do not rewrite the saved ratio or activation log; live evidence is unavailable. |

## Event-system pacing

| ID | Source status | Evidence or blocker |
| --- | --- | --- |
| `BF-P01` | Source; Live-blocked | Reservation writes selection state only and does not call the fire-once pacing/history path. |
| `BF-P02` | Source; Live-blocked | Activation calls the minor pacing path once, including dynamic major gain and one history row. |
| `BF-P03` | Source; Live-blocked | Activation deliberately does not recalculate the timer selected before reservation. |
| `BF-P04` | Source; Live-blocked | Global reservation and fired guards reject a second same-date selection. |
| `BF-P05` | Source; Calendar-calibration-blocked; Live-blocked | Same-day helper-qualified Friday activation records one fire through the activation path, but the missing Vanilla weekday precedent and live behavior keep the row open. |
| `BF-P06` | Source; Live-blocked | Global flags and variables are initialized only when absent and therefore survive save/reload. |

## Discount arithmetic and composition

A source-level harness mirroring the implemented Euclidean-remainder formula passed all BF-R01 through BF-R13 values, BF-C01, BF-C02, and both source orders for a two-source BF-C03 case (17 of 17). This proves the checked arithmetic against the source formula, not engine execution or owner display/payment agreement.

A source mirror verified the thirty-bit family eligibility matcher separately. The trigger-readable ratio cache now contains twelve canonical families—political power, command power, manpower, equipment, trains, convoy, fuel, army experience, navy experience, air experience, stability, and war support. The previously recorded 1,080-case cache mirror covered the then-supported eight-family cache and is not promoted as a twelve-family result; the added cache paths require a refreshed mirror. The remaining family bits are matchable by the source mask but have no trigger-cache slot and therefore remain explicitly registry- and adapter-blocked. The current registry records 104 logical component rows across ten bounded owner tranches, including ten Random Faction actions and the Africa Elephant logistics contract. The bounded sale strings no longer contain fixed numeric 50/75-percent variants where their owner adapters are active; their active and blocked forms read quote-backed values. This remains source evidence rather than engine or live UI evidence.

| ID | Source status | Evidence or blocker |
| --- | --- | --- |
| `BF-R01` | Source | Zero bypasses source composition and remains zero. |
| `BF-R02` | Source | Positive one-unit values quantize upward to one registered quantum. |
| `BF-R03` | Source | Positive one-unit values remain one at the Evolution I 25-percent payment ratio (75 percent off). |
| `BF-R04` | Source | The exact-ratio ceiling helper returns one for two units at 50 percent. |
| `BF-R05` | Source | The exact-ratio ceiling helper returns two for three units at 50 percent. |
| `BF-R06` | Source | The exact-ratio ceiling helper returns one for three units at 75 percent. |
| `BF-R07` | Source | The exact-ratio ceiling helper returns three for five units at 50 percent. |
| `BF-R08` | Source | The exact-ratio ceiling helper returns two for five units at 75 percent. |
| `BF-R09` | Source | The exact-ratio ceiling helper returns 51 for 101 units at 50 percent. |
| `BF-R10` | Source | The exact-ratio ceiling helper returns 26 for 101 units at 75 percent. |
| `BF-R11` | Source; Adapter-blocked | The arithmetic harness keeps one factory commitment at one; the native payment framework has no factory-commitment component adapter. |
| `BF-R12` | Source; Adapter-blocked | The arithmetic harness returns three for five commitments at the baseline ratio; an owner or engine adapter is still absent. |
| `BF-R13` | Source; Adapter-blocked | The arithmetic harness returns two for five commitments at the Evolution I ratio; an owner or engine adapter is still absent. |

| ID | Source status | Evidence or blocker |
| --- | --- | --- |
| `BF-C01` | Source; Live-blocked | Fixed-point composition supports an ordinary 20-percent discount followed by Black Friday; live owner display/payment proof is unavailable. |
| `BF-C02` | Source; Live-blocked | The arithmetic harness returns 63 for an ordinary payable cost of 125 at the baseline ratio; live owner display/payment proof is unavailable. |
| `BF-C03` | Source; MCP-blocked; Live-blocked | Effect-side registered sources compose by priority and quantize once, and the source-family modulo-span matcher agrees with ordinary bitwise intersection for all 4,096 source/quote mask pairs from 0 through 63. Successful source mutations rebuild the twelve-family trigger-readable composed-ratio cache through the effect-side quote; the remaining 18 family bits have no trigger-cache slot and stay explicitly blocked. The earlier 1,080-case source mirror covered eight cached families before the additional cache paths were added, so a refreshed twelve-family mirror is still required. The current source registry records 104 bounded logical component rows across ten owner tranches. Focused MCP/runtime proof for both source orders, visible price, and confirmation debit is still absent. |
| `BF-C04` | Source; Live-blocked | Source matching removes expired sources without restoring stale values; live evidence is unavailable. |
| `BF-C05` | Source; Live-blocked | Black Friday cleanup removes only its own source registration; live evidence is unavailable. |
| `BF-C06` | Registry-blocked | Exclusion families are recorded in the registry, but no complete owner-level family audit is closed. |

## Transaction integrity

| ID | Source status | Evidence or blocker |
| --- | --- | --- |
| `BF-X01` | Source; Live-blocked; Adapter-blocked | The bounded owner tranches route their registered components through the shared quote and payment contract, but the remaining owner surfaces have no complete adapter and no live click evidence exists. |
| `BF-X02` | Adapter-blocked | Post-expiry owner quote recalculation cannot be proven without an owner adapter. |
| `BF-X03` | Adapter-blocked | No generic confirmation hook is exposed for all owner panels. |
| `BF-X04` | Adapter-blocked | Delayed project upfront payment requires a project owner adapter. |
| `BF-X05` | Adapter-blocked | Delayed installments require an owner-defined transaction contract. |
| `BF-X06` | Source; Adapter-blocked | Bounded owners record successful receipts and custom-resource adapters acknowledge external refunds, but the remaining owners have no receipts and no complete live cancellation proof exists. |
| `BF-X07` | Source; Live-blocked; Adapter-blocked | The bounded owners settle receipts and the shared refund state is idempotent, with explicit external refunds for owner-controlled payloads; the remaining owner cancellation paths and live second-refund proof do not exist. |
| `BF-X08` | Source | Negative values and rewards bypass discount composition. |
| `BF-X09` | Adapter-blocked | No static normal/50/75 variant set is installed for owner-defined actions. |
| `BF-X10` | Source; Adapter-blocked | Framework receipts persist as regular payer-country arrays, and bounded owner actions register refundable transactions; most owner actions remain unregistered. |
| `BF-X11` | Source; Live-blocked; Adapter-blocked | Bounded owners supply multi-component transactions for supported native and documented external resources, but the full registry still has no universal owner coverage and no live proof. |
| `BF-X12` | Adapter-blocked | Remaining multi-component refunds need owner transaction receipts and completion/failure callbacks; the bounded adapters have source-level refund paths but no live proof. |
| `BF-X13` | Source; Live-blocked; Adapter-blocked | The bounded owners commit one registry-defined primary family per logical transaction, while all other owners remain unconnected and no live achievement proof exists. |
| `BF-X14` | Source; Live-blocked | Payer-scoped receipts prevent quote overwrite in the framework; simultaneous country proof requires live multiplayer. |

## Cost-family coverage

| ID | Source status | Evidence or blocker |
| --- | --- | --- |
| `BF-F01` | Engine-inaccessible; Adapter-blocked | The installed native schema exposes political-power cost as an absolute/ongoing field rather than a relative one-time purchase factor; the Event 26 ideas therefore do not install a false native discount, and one-time native decision costs remain unadapted. |
| `BF-F02` | Source; Live-blocked | Native law factor fields are installed; live law-change evidence is unavailable. |
| `BF-F03` | Source; Live-blocked | Native advisor and character factor fields are installed; live hiring evidence is unavailable. |
| `BF-F04` | Source; Live-blocked | Native command-ability factor is installed; live ability/cooldown evidence is unavailable. |
| `BF-F05` | Source; Engine-inaccessible; Live-blocked | Land-doctrine factor fields are installed; land-equipment XP upgrade fields are flat/native-owner costs and remain engine-inaccessible, so live doctrine evidence cannot promote the unadapted XP row. |
| `BF-F06` | Source; Engine-inaccessible; Live-blocked | Naval-doctrine factor fields are installed; naval-equipment XP upgrade fields are flat/native-owner costs and remain engine-inaccessible, so live doctrine evidence cannot promote the unadapted XP row. |
| `BF-F07` | Source; Engine-inaccessible; Live-blocked | Air-doctrine factor fields are installed; air-equipment XP upgrade fields are flat/native-owner costs and remain engine-inaccessible, so live doctrine evidence cannot promote the unadapted XP row. |
| `BF-F08` | Source; Live-blocked; Adapter-blocked | Design and licensed-equipment factor fields are source-present, but equipment-upgrade XP and flat license-purchase fields remain engine-inaccessible or owner-bound; live designer/license display and payment evidence is unavailable. Technology-category, factory-conversion, and refit-IC fields are explicitly excluded because they alter research, construction, or production time. |
| `BF-F09` | Adapter-blocked | Random Faction observer and corridor convoy components are source-adapted with dedicated owner component IDs; other convoy owners remain incomplete, and no live payment proof exists. |
| `BF-F10` | Source; Live-blocked; Adapter-blocked | CBRN shelter movement registers exact train-equipment payment through the shared adapter; other train owners remain unadapted and live proof is unavailable. |
| `BF-F11` | Source; Adapter-blocked | Fuel payment exists in the native helper, but no owner callsite supplies a registered transaction. |
| `BF-F12` | Source; Live-blocked; Adapter-blocked | Communist local/emergency and Fury adapters quote, pay, and receipt manpower, but the remaining manpower owners have no adapter and live proof is unavailable. |
| `BF-F13` | Source; Adapter-blocked; Live-blocked | The native helper supports fixed-point stability and war-support payment, and the Fury march-core stability component is registered through it with its reserve-floor gate; no war-support owner transaction or complete owner-wide stability adapter is registered, and live proof is unavailable. |
| `BF-F14` | Adapter-blocked | Civilian-factory commitments are not represented by the native resource payment helper. |
| `BF-F15` | Adapter-blocked | Military-factory and dockyard commitments are not represented by the native resource payment helper. |
| `BF-F16` | Engine-inaccessible | Intelligence-operation cost fields are flat absolute values and are intentionally absent from the Event 26 dynamic modifier source; no generic operation confirmation adapter exists, so live network/target/duration evidence cannot promote this row. |
| `BF-F17` | Adapter-blocked | The four documented MIO assignment, design-team, manufacturer, and policy cost fields are flat absolute modifiers rather than relative factors; Event 26 does not install them in its sale modifiers and no generic MIO confirmation adapter is exposed. The MIO rows remain engine-inaccessible in the registry, and live MIO-panel evidence is unavailable. |
| `BF-F18` | Engine-inaccessible | Special-project costs have no generic confirmation adapter in the installed surface. |
| `BF-F19` | Adapter-blocked | Custom currencies require owner-defined quantum, receipt, and refund adapters. |
| `BF-F20` | Adapter-blocked | No dedicated owner GUI action is wired to the shared quote/payment contract. |

## AI scenarios

| ID | Status | Evidence or blocker |
| --- | --- | --- |
| `bf_ai_01_low_reserve_advisor` | Partial; compare-blocked | Current MCP evaluation is exact only for the one informational acknowledgement option (`chaosx.nr26.2.a` at 100 percent); no advisor candidate pool or owner affordability adapter is registered. |
| `bf_ai_02_valid_law_change` | Partial; compare-blocked | Native law factors are present, but the required scenario-specific candidate and affordability comparison is unavailable. |
| `bf_ai_03_wartime_command` | Partial; compare-blocked | Native command factor is present, but the required command-ability candidate comparison is unavailable. |
| `bf_ai_04_invalid_target` | Partial; compare-blocked | Native target validity remains owner/engine-controlled, but no universal candidate pool was exposed. |
| `bf_ai_05_static_variant_pool` | Adapter-blocked | No static variants are installed, so the single-candidate proof cannot be run. |
| `bf_ai_06_overlapping_discount` | Source; compare-blocked | Framework source priority is deterministic, but no owner AI candidate uses the composed quote. |
| `bf_ai_07_sale_expiry` | Adapter-blocked | No owner AI action is wired to quote again after expiry. |
| `bf_ai_08_75_percent_high_chaos` | Source; compare-blocked | Evolution snapshot logic is source-implemented, but no owner candidate pool exposes the expected affordability shift. |

The current probability rerun records `probability-57a188d252255716ad0b76b9`, based on source revision `a477c32d9183b75725e09db4c376b6207faf6cfb97047b2b577b89c455cf75d5` and scenario hash `50c2954c8c1cfc5bf8e47c7c7e8a9c5eb8a0f36f460baee63cb4d5d3b0e691fd5`. It resolves only the one-option acknowledgement event at 100 percent across the eight named empty fixtures. The refreshed custom weighted-pool inspection returned an incomplete zero-candidate pool, and its evaluation returned `PROBABILITY_SURFACE_EMPTY`; no same-scenario before/after comparison exists for the sale-affected purchase owners. The bounded source adapters preserve their owner AI entry gates, but they do not provide a verified universal candidate pool. These results are evidence of the adapter boundary, not proof of universal AI coverage.

## Multiplayer and presentation

| ID | Source status | Evidence or blocker |
| --- | --- | --- |
| `BF-M01` | Source; Live-blocked | One global snapshot and one human-country report path are implemented; live multiplayer popup proof is unavailable. |
| `BF-M02` | Source; Live-blocked | Global reservation/fired guards prevent duplicate history; live dual-timer proof is unavailable. |
| `BF-M03` | Source; Live-blocked | Existing country refresh hook applies active status after tag changes; live proof is unavailable. |
| `BF-M04` | Source; Live-blocked | Existing country refresh hook applies active status to joining players; live proof is unavailable. |
| `BF-M05` | Source; Live-blocked | Payer-scoped receipt arrays isolate payments; simultaneous click proof is unavailable. |
| `BF-M06` | Source; Live-blocked | Global snapshot, reservation, and expiry state are persisted; live multiplayer reload proof is unavailable. |
| `BF-U01` | Source; MCP-partial | Localisation and list status return `N/A` below threshold; MCP workspace-wide validation is partial. |
| `BF-U02` | Source; MCP-partial | Reserved status mapping exists; Event Details/list selector evidence is partial. |
| `BF-U03` | Source; MCP-partial | Actorless Event 26 history mapping and the Event 26-specific global-scope visibility predicate exist; refreshed MCP evidence remains workspace-partial without end-to-end render proof. |
| `BF-U04` | Source; MCP-partial | Evolution I log mapping exists; selector-specific render evidence is unavailable. |
| `BF-U05` | Source; MCP-partial | Evolution-disabled baseline branch exists; selector-specific render evidence is unavailable. |
| `BF-U06` | Source; MCP-partial | Event Details uses the saved percentage and next-tick expiry; selector-specific render evidence is unavailable. |
| `BF-U07` | Source; Live-blocked; Adapter-blocked | Bounded owner cost tooltips consume their shared quote paths, while most custom owners still have no owner tooltip adapter and no live display/payment proof exists. |
| `BF-U08` | Source; Live-blocked | Source cleanup removes the sale idea and dynamic modifier on expiry; live tooltip evidence is unavailable. |
| `BF-U09` | Source; Live-blocked | Report, idea, and achievement assets are wired and round-trip checked; in-game texture evidence is unavailable. |
| `BF-U10` | Source; MCP-partial | Final localisation audit found no active Event 26 stale desert strings or unresolved scoped keys; the asset audit records the repaired report safe margins, deterministic achievement triplet, native-size DDS decode review, and exact in-game texture presentation remains unavailable. |

## Save/reload checkpoints

| Checkpoint | Status | Evidence or blocker |
| --- | --- | --- |
| Eligible and unfired | Source; Live-blocked | State is initialized/preserved, but no live save was created. |
| Reserved before Friday | Source; Live-blocked | Reservation variables/flags persist, but no live save was created. |
| Reserved after skipped low-chaos Friday | Source; Live-blocked | Reservation is not cleared by low Chaos, but no live save was created. |
| Active baseline sale | Source; Live-blocked | Ratio, sequence, expiry, and source registration are persisted, but no live save was created. |
| Active Evolution I sale | Source; Live-blocked | Evolution snapshot fields are persisted, but no live save was created. |
| Refundable transaction paid during sale | Source; Adapter-blocked | Bounded owners persist receipts and provide source-level native or external refund paths, but remaining owners lack adapters and no live refund acceptance exists. |
| Achievement progress before fifth family | Source; Live-blocked; Adapter-blocked | The bounded owners commit primary families to the ledger, but the full registry cannot yet supply the five-family path and live progress is unavailable. |
| Expired sale | Source; Live-blocked | Expiry clears active state/source and keeps receipt history, but no live save was created. |

## Catalog and documentation

The authoritative workbook row for ID 26 is Black Friday, the duplicate no-ID row is removed, and the three CSV snapshots were regenerated through the repository exporter. The row remains `Needs Testing`. Event documentation, cost registries, asset manifests, and specialist handoffs are present, but the cost registry is not frozen to an implementation commit because the completion gate is open.

## Blocking conclusion

The lifecycle, event-log, presentation, arithmetic, asset, and catalog source paths are implemented. Bounded quote/payment/receipt/settlement and achievement-primary-family callsites now cover the five Communist-spread actions, seventeen reachable Fury decisions, the Japan chemical campaign attack, biological medical-capacity expansion, CBRN civilian-shelter movement, two Japan biological campaign agents, four Germany Mengele command-power actions, and the D'Rhondan alien-infantry landing reservation. The CBRN diplomacy, CBRN doctrine, CBRN occupation, and genocide-crisis audits explicitly rejected unsafe partial adapters and recorded their exact component, commitment, delayed-payment, cross-owner, and refund blockers. The goal is incomplete because most of the 2,224 Chaos Redux custom-cost occurrences still lack complete owner quote/payment/receipt/refund integration, several engine-owned surfaces lack a generic confirmation route, probability comparisons cannot yet be run over all required owner candidate pools, the Friday index is not engine-calibrated, and live Part 8 evidence is unavailable. Event 26 must remain disabled.
