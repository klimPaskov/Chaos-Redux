# Achievement implementation and asset prompt: Event 071 Persia

Read part 17 in full, the index, relevant route and system parts, and the project's actual achievement patterns. Implement all eight achievements. Their working labels are not final localisation. Final wording must state the real conditions clearly and must not promise an easier or different objective.

| Exact planned ID | Working label | Core requirement | Visibility |
|---|---|---|---|
| `071_persia_chartered_empire` | Chartered Empire | Achaemenid conclusion, five distinct regional satrapies, connected network, homeland and legitimacy for 180 days | Visible |
| `071_persia_two_frontiers` | Two Frontiers | Sasanian conclusion, western plus northern and eastern programs, supply, settled campaign, 180 days | Visible |
| `071_persia_industrial_order` | Industrial Order | Modern conclusion, three completed partner investments, transport, outlet, replacement program, 180 days | Visible |
| `071_persia_persepolis_restored` | Persepolis Restored | All site stages, institution, homeland, legitimacy, 180 days | Visible |
| `071_persia_guard_of_the_empire` | Guard of the Empire | Evolution II, advanced institution, 35,000 authorized guard manpower, actual readiness and campaign, 180 days | Visible |
| `071_persia_gulf_power` | Gulf Power | Political settlement, coastal and fleet programs, real outlet and access, operational force, 180 days | Visible |
| `071_persia_imperial_guarantor` | Imperial Guarantor | Evolution III, a guarantee honored in a real qualifying war, five protected or subordinate states, legitimacy, 180 days | Visible |
| `071_persia_restore_after_ruin` | Restore After Ruin | Genuine fragmentation followed by homeland and institutional recovery, no second opening grant, 180 days | Hidden until crisis entry |

Part 17 is authoritative for each achievement's country eligibility, exact gates, disqualifiers, difficulty, icon direction, nontriviality, and tracking notes. Do not implement from this summary table alone.

Use the existing achievement system. Inspect registered IDs for collisions before allocating these planned IDs. Any necessary naming adaptation must be documented and propagated to every icon and consumer. Do not silently drop an achievement because its readiness or naval query needs verification.

Track distinct regions, real charters, actual ownership and control, valid access, trained and deployed guard manpower, project completion, qualifying campaigns, guarantee timing, and continuous durations. Guard manpower in a training queue is not deployed. A treaty partner is not a satrapy. A guarantee issued after the attack does not qualify.

Preserve tracking through save and reload. Recheck all current conditions at the unlock boundary. Test a positive case, a near miss, an invalidation, and a reload for each achievement. Follow existing debug and forced-event disqualification rules without adding an unrelated anti-cheat framework.

Coordinate the icon artist through the asset prompt. Generate one original transparent subject per achievement, then derive the grey and not-eligible sources deterministically. Preserve the supplied template and red-cross overlay files exactly. Use the required complete-triplet processor and strict final DDS checks.

Put final `<id>.dds`, `<id>_grey.dds`, and `<id>_not_eligible.dds` directly under `gfx/achievements/`. Retain source triplets, reviewed native-size contact sheets, decoded pixel equality evidence, final localisation, tracking documentation, and tests. Do not mark an achievement complete with one icon state missing or a placeholder trigger.
