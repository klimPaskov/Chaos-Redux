# Warfare, Condemnation and dynamic-weight planning review

Disposition: unresolved candidate improvements awaiting explicit parent review within the 8 October planning request.
All three packages were reviewed; five passage-level candidates are supplied.
Broad expansion is not recommended, and this review makes no implementation or closure claim.

## Candidates and rationale

| Package | Candidate passages | Design problem and proposed improvement |
| --- | --- | --- |
| Chaos Warfare | `specs/01_core_system_and_gameplay_loop.md`, opening policy choice and delivery/HQ preparation | The core loop still promises six policy postures and a paid offensive headquarters stage. Reconcile it with the accepted three policies, native raid delivery, three HQ sections and five protective orders; distinguish protective investment from offensive permission. |
| Chaos Warfare | `specs/09_condemnation_deaths_air_cleanliness_and_diplomacy.md`, Protective Aid, humanitarian carve-out and Sponsor Decontamination | Make allocation of scarce protection and cleanup the player choice. Sanction permission, physical dispatch, evidence publication and disease response retain distinct owners; no second payment, reward, death process or Chaos contribution is created. |
| Chaos Warfare | `specs/11_balance_tuning_and_consistency_rework.md`, doctrine consequence passage | The older fix says doctrine affects evidence and collateral damage, contradicting the accepted boundary. Restore bounded Condemnation mitigation while preserving physical and forensic consequences; keep any separately authorized camp exception with its owner. |
| Condemnation | `specs/condemnation_impact_system_spec.md`, chemical/biological source, participant carve-out, integrations and validation cases | Outbreak severity establishes relief need, not guilt. Blame follows the stored responsible actor and public evidence; later discovery charges the unpaid portion once. Humanitarian relief does not grant cure/progression or erase responsibility. Broader sanctions routes remain unresolved beyond recorded tuning acceptance. |
| Dynamic major weights | `specs/dynamic_major_event_weights_spec.md`, counting, accounting time, clusters and validation | Define a source entry separately from helper/report multiplicity and consume the pool owner's membership. Clarify one accounting-time calculation and Black Friday's reserved-versus-activated lifecycle without changing formula, tuning, clamp or unresolved rounding choice. |

## Connected owners

[CBRN accepted amendment](../../../../specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md) and [current requirement ledger](../../../chaos_warfare_system_plans/2026-09-20_cbrn_overhaul_requirement_ledger.md) control accepted policy, raid, HQ, protection, cost, and doctrine boundaries.
The [consequence spec](../../../../specs/chaos_warfare_system_specs/specs/09_condemnation_deaths_air_cleanliness_and_diplomacy.md) owns the action record and unpaid attribution increments; Condemnation consumes it rather than reapplying harm.
The [Sponsor Decontamination correction](../../../../specs/chaos_warfare_system_specs/corrections/2026-09-25_international_decontamination_cost.md) preserves exact target/access, the 45-day mission, ordinary/sale material bills, factory commitments, and cancellation settlement.
The [civilian field-kit correction](../../../../specs/chaos_warfare_system_specs/corrections/2026-09-26_civilian_decontamination_field_kit_pool.md) and [Medical Capacity sale boundary](../../../../specs/chaos_warfare_system_specs/corrections/2026-09-26_black_friday_medical_capacity_sale_boundary.md) preserve equipment ownership, military priority and discounted affordability; no alternative cost or allocation formula is proposed.
[Event 020 Part 3](../../../../specs/020_black_plague_specs/specs/020_black_plague_spec_part_3_cure_spread_and_biowarfare.md) owns distinct Black Plague identity and countermeasures, including its explicitly authorized pre-event provider exception.
[Event 026 Part 2](../../../../specs/026_black_friday_specs/026_black_friday_spec_part_2_friday_reservation_and_lifecycle.md) owns reservation, eligibility, activation, cancellation and timer handling: reservation gives no pacing; eligible Friday activation gives one receipt.
These connections work only through an already eligible owning action or existing episode; they neither fire another event nor grant its progression.
Existing AI must obey the same actor, target, access and affordability boundaries; no willingness coefficient or selection probability is changed or claimed validated.

## Authority and previous dispositions

The warfare README, source-of-truth map, accepted amendment and current ledger distinguish accepted design from source and consumer evidence.
The July Stage 5 improvement addendum is closed, Stage 6 escalation addendum is marked implemented, and the July near-completion closure records no unresolved earlier addendum.
Those historical closure receipts do not close the September overhaul: the current ledger and October takeover still carry accepted source/engine/AI/GUI/achievement evidence backlog.
This pass does not supersede it or create another competing expansion layer.
Condemnation's 0-1000 range, `1 + C/500` equipment multiplier, whole-equipment rounding and 5-15% inspection burden for 180 days retain their explicit acceptance.
Its broader sanction, compliance and evasion designs remain unresolved where acceptance is absent.
Dynamic weights retain the README's unresolved acceptance and evidence disposition; finding existing source helpers is implementation-navigation evidence only.
No separate Condemnation/dynamic-weights plans folder appeared in the repository path search; their package acceptance boundaries remain controlling.

## Delivery and checks

External review directory: `C:\Users\klimp\AppData\Local\Temp\chaos-redux-specs-audit-20261008-qgzbgbrz\proposals\warfare_condemnation_weights`.
`manifest.json` lists all five intended repository paths, exact saved bases/candidates, SHA-256 hashes, reasons, package dispositions and concrete owner connections.
`review.patch` is an LF unified patch for only those candidate passages.
The five canonical files still match their saved base hashes; eight introduced owner links and heading fragments resolve.
The dynamic formula, examples, safety rules and constant sections are byte-equivalent after newline normalization, and Condemnation's accepted tuning and tier table are unchanged.
The patch passes read-only application checking; it has not been applied or staged.
Only this assigned handoff is written in the repository.
No gameplay, asset, workbook, CSV, skill, shared registry, original archive/brief/receipt, or Event 091 file is edited.

## Evidence limits and next review

The corrected live probability request is `probability_inspect(adapter = custom_weighted_pool, source.path = common/scripted_effects/chaosx_logic_effects.txt)`.
Reference context for AI and a focused Event 026 entry trace were also requested using the exposed tool metadata; no result arrived during bounded observation.
The initial probability probe used a wrong nonexistent source path and was abandoned without a response; it is not inspection evidence.
No MCP source revision, scenario hash, graph, numeric comparison or rendering artifact was obtained, so service health and current engine/weighted behavior remain unresolved.
The caller observations were then terminated locally without tool results; this does not establish a remote-task failure or cancellation.
The Event 026 render depends on a successful inspection and is unproved.
The assignment forbids nested delegation, so no probability auditor ran; the parent must route actual weighted-source evaluation/comparison through that owner before an implementation change.
The proposed `dmg_*` cases and added Condemnation relief/attribution cases are future checks, not completed audits.
No focus, map, GUI layout or technology change is proposed, and no standalone Technology Tree Viewer availability claim is made.
Historical stock, country programs, scientific identities and prior bibliography/source caveats are preserved; no new historical or scientific assertion was introduced.

Parent review should resolve whether the pool's temporary owner-controlled exclusions and delayed activation accounting are described at the right existing call point; source navigation shows those helpers exist but does not accept their behavior.
Review relief and attribution cases against owner acceptance, keep physical and diplomatic consequences separate, then promote only accepted passages into the existing canonical specs.
Keep this handoff in `docs/plans`; preserve broader unresolved alternatives, queued accepted implementation and all evidence limits.
Skills applied: improvement-loop, event-planning, events, decisions-missions and subagents.
No skill was changed.

## Parent disposition, 8 October 2026

Parent accepted reconciliation with the recorded CBRN policy, protective HQ and doctrine amendments, precise relief and biological responsibility ownership, and once-per-source/cluster Black Friday pacing. Formula and numerical tuning retained; future weighted validation explicitly remains required.
The reviewed edits have been promoted into the listed specifications for this planning task.
Explicit unresolved alternatives and implementation proof gates above remain unresolved; this accepts neither an unchosen design branch nor completed gameplay.
