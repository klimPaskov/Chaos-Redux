# Event 028 named-save observations, 2026-10-07

Disposition: implemented read-only runtime evidence and an owner source correction, with full Event 028 and current graphics acceptance incomplete.
Acceptance basis: the existing named QA saves and the user's exact-impact, once-only receipts, nonnuclear presentation and full acceptance requirements.
The save is not copied, changed or committed, and no game was launched.

## Save and exact command scope

File: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/save games/qa_evt028.hoi4`.
It is a 107.1 MiB `HOI4txt` save for USA, democratic, normal difficulty, dated `1936.3.7.4`, Operation Postern `v1.19.2.0.a729 (2bce)`, save version 33.
The bundled read-only `chaos-redux-save-inspection` inspector was used for `info`, top-level `keys`, `find asteroid_incoming --in variables`, `find asteroid_incoming --in countries/USA` and `find asteroid_incoming --in states/506`.
Additional key discovery covered `entity` and `states`, and the first `saved_event_target` block was inspected, not assumed to enumerate all eighteen repeated blocks.
The initial `states/506/manpower` lookup returned no field; no population conclusion is based on that absent guessed path.

## Observed values

| Exact saved field | Value | Evidence scope |
| --- | --- | --- |
| `variables/asteroid_incoming_target_1_state_id` and `variables/asteroid_incoming_target_state_id` | `-10737.41318` | Encoded reference corresponding to the registered main-crater state 506, not a plain numeric state ID. |
| `variables/asteroid_incoming_target_country_id` | `10787.41059` | Stored country reference, not assumed to be a plain country enumeration. |
| `variables/asteroid_incoming_opening_day` / impact day | `706640` / `706642` | Difference two game days in this saved episode; does not prove every dual-callback/watchdog case. |
| `variables/asteroid_incoming_affected_country_count` / state count | `6` / `29` | Retained incident totals in this one ordinary-impact save. |
| `variables/asteroid_incoming_total_deaths` | `5301708` | Recorded total, not yet independently reconciled against every state's receipt and shared Deaths reasons. |
| `variables/asteroid_incoming_fragment_site_count` | `0` | No fragmentation in this episode. |
| Dust raw / score / stage | `62` / `57` / `3` | Saved impact-winter state, not a complete decay/mitigation/reload trace. |
| Secondary-disaster count | `4` | Saved bounded count, not yet independently checked against all actual Event 013 outcomes. |
| `states/506/variables/asteroid_incoming_state_population_before_people` | `424135` | Pre-impact receipt. |
| State 506 after / lost people / actual deaths | `0` / `424135` / `424135` | The state's observed receipt accounts for all 424,135 people, and its permanent main-crater and transaction-applied flags are present. |
| State 506 profile / ring / transaction | `70` / `0` / `1` | Main-centre profile and original receipt, flags dated `1936.1.3.12`. |
| State 506 removed building receipt / industry / logistics / strategic | `7` / `3` / `3` / `1` | Observed receipt values only, without asserting complete exceptional-network/queue removal or provincial getter semantics. |
| USA controlled fragments / fragment armour bonus / two hold counters | `0` / `0` / `0` | USA is not a mineral holder in this snapshot. Its ideas include the impact-winter spirit. |

The affected-state registry has 28 entries while the total processed-state count is 29.
An independent narrow `flatten --in states` reconciliation found 29 complete population receipts, with one main centre, five Ring 1, nine Ring 2 and fourteen Ring 3 profiles.
Every before-minus-after value equals its recorded actual deaths, every profile matches positive half-up rounding of its required population share, and their sum is exactly 5,301,708, matching the saved global total.
States 963 and 964 retain planned profiles without population receipts and are not counted as additional deaths.
The 28-entry registry difference is retained rather than called a duplicate, since the permanent main crater and recoverable-state registry have different consumers.
The state-506 `buildings` subtree stores infrastructure, industrial complex, dockyard and air-base level, partial health and healthy levels all as zero, and its category is `wasteland`.
That is actual saved state-level clearance, not a complete provincial building, railway, supply-node or project-queue inventory.
ARG, BOL, BRA, CHL, PRU and PAR each carry `asteroid_incoming_report_seen = 1`, dated `1936.1.4.11` or `.12`, consistent with the six saved recipient total.
Those receipts do not alone establish visible popup multiplicity or ordering.
CHL also stores `condemnation_nuclear = 38.15625`, while its nuclear-strike Deaths cause is zero.
No causal attribution to a particular earlier event or visual is inferred from that one value, and it is not zero-nuclear proof for the new graphics-only path.

An independent read-only bitmap audit compared the saved ring assignments to shortest four-connected land adjacency from the installed `map/provinces.bmp`, `definition.csv` and all state province memberships, including x-wrap and excluding sea/strait links.
The radius-three graph contains exactly the 31 saved planned states, with no missing bitmap member and no distance mismatch: main 506, five Ring 1 states, nine Ring 2 and sixteen Ring 3 graph carriers.
The two empty Deep Amazonas carriers 963 and 964 account for the difference between 31 graph members and 29 population receipts.
This is an installed-map/source comparison against saved assignments for one episode, not a guarantee for every target or special adjacency configuration.
The mandatory MCP lookup independently returned `MAP_LOOKUP_COMPLETED` for 506, 302, 508, 951, 952, 959, 963 and 964 at revision `dc6c8af6725cfdba304569ba5b55555df936e9abdf40e4b3d59d52bf03fd6050`, with lookup-only coverage.
Its linked bulk report is not enumerated by the exposed resource inventory, so no unread full-map validation is claimed.
The snapshot contains no evidence of the graphics-only patch, its reserved entity IDs or retirement, and cannot validate those newer source changes.

## Corrected source assumption

The first graphics-only source and host model treated `THIS.id` as plain numeric state 506 or 64 when computing a reserved graphical ID.
The saved values show that scope references use an encoded representation, so that assumption is unproved and unsafe.
The owner replaced the addition with the existing shared cache's numeric anchor-province literal and made the host model reject numeric `THIS.id`.
All 1,081 real source anchors are unique, and their derived IDs are unique with zero overlap against the audited Air Winter/proof allocations.
This is a source/model correction, not a claim that a failed graphics dispatch was observed in the save or that undocumented native arithmetic conversion is universally impossible.

## Remaining acceptance

This one saved low-fragment episode supplies observed fields for a main-centre receipt, two-day date difference and persistent ordinary aftermath.
It does not establish all sixteen Part 10 scenarios, actual building/network demolition, generic frozen names/flags, supplied divisions, original-target annex/reload behavior, complete Deaths reconciliation, current nonnuclear graphics, mineral transfers, continuous achievement holds or native UI/audio.
No acceptance gate is closed from save metadata alone, and no clean live error log is claimed.
Guidance used: events, state-ledger evidence boundaries and save-inspection.
