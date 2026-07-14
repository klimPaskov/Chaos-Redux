# Stage 5 Chaos Warfare balance and scenario audit

Status: complete for Stage 5; the overall Chaos Warfare goal remains in progress

## Scope

This audit covers the Stage 5 grand doctrine, four mastery tracks, institutional decisions, use policy, doctrine-only technology commissions, officer-corps spirits, generic high command, commander trait, exact-state decontamination assignment, and their shared-exposure integrations. It does not claim the later chemical-delivery, biological-agent, nerve-suppression, consequence, achievement, or full country-profile stages are complete.

All values below come from `common/script_constants/cbrn_doctrine_constants.txt`, the canonical legacy-compatible Condemnation ladder in `common/script_constants/chemical_warfare_constants.txt`, and the static doctrine parser mirrors in the five Chaos Warfare doctrine files. The shared pipeline and not-yet-migrated legacy adapters read the same 0.90/0.80/0.70 ladder, so tuning does not diverge during route migration.

## Permanent-modifier ceilings

The accepted design removes the old broad 20-percent chemical-support attack package. Maximum permanent stacks within this tranche are:

| Modifier | Maximum Stage 5 stack | Composition and constraint |
| --- | ---: | --- |
| Global army attack | +5% | Terminal Hazard Doctrine only; mutually exclusive with Controlled Retaliation and Theater Contamination |
| Designated hazard-unit attack/defence | +5% / +5% | Hazard Assault Cadres; Chaos Assault Battalion and Hazard Pioneer only |
| Artillery attack | +3% | Contaminant Fire Coordination; +8% total only when combined with Terminal Hazard's +5% global attack |
| Army organization | +5% | Integrated Command M5 +2%, Controlled Retaliation +1%, Mask Discipline +1%, Biological Security Director +1% |
| Coordination | +8% | Contaminant Fire M2 +1%, Toxic Armor M5 +1%, Integrated Command M4 +1% and M5 +2%, Terminal Hazard +3% |
| Planning speed | +13% | Grand doctrine +5%, Theater Contamination +5%, Operations Director +3% |
| Global attrition reduction | -8% | Theater Contamination -5% and Chemical Logistics Inspector -3% |
| Global supply consumption | net +7% at terminal posture | Terminal Hazard +10% and Chemical Logistics Inspector -3%; unit/HQ category reductions apply only to their mapped formations |
| Special-forces cap | +2% | Hazard Assault Cadres only |
| Army experience gain | +3% | Hazard Assault Cadres only |
| Maximum Command Power | +15 | Controlled Retaliation +10 and Operations Director +5 |

No doctrine node grants a generic casualty, contamination, evidence, attribution, or payload effect. Track unlock flags are eligibility inputs for later prepared operations.

## Protection and operational multipliers

- Military Filter Standardization (0.85), Controlled Retaliation (0.95), and Mask Discipline (0.90) combine multiplicatively to 0.72675 of baseline military mask/filter consumption: a maximum 27.325-percent reduction. Civilian loss is unaffected by the two spirits.
- Controlled Retaliation reduces prepared friendly exposure risk to 0.85 and raises victim evidence recovery to 1.15. It never lowers attacker evidence.
- Theater Contamination raises prepared dose to 1.05 and cleanup output to 1.25, but adds 5 percent supply consumption.
- Terminal Hazard raises operational effect to 1.10, deaths to 1.15, and Condemnation to 1.25, while adding 10 percent supply consumption.
- At Integrated Command mastery 5 plus Terminal Hazard, the pre-floor Condemnation factor is 0.70 x 1.25 = 0.875 of baseline. Public-harm floors still apply after multiplication. Evidence, attribution, deaths, contamination, medical saturation, use counters, and history are independent.

## Progression costs and pacing

| Gate | Cost/pacing | Balance purpose |
| --- | --- | --- |
| Grand doctrine | 100 Army XP | prevents casual universal adoption |
| Each mastery track | 100 Army XP | forces strategic track commitment |
| Establishment | 90 days plus 500 masks, 50 decon, 100 support, two fielded formation proofs | prevents paper institutions |
| Delayed remediation | 35 PP, 10 CP, 14 days, exact proof retained | failure has a recoverable but real cost |
| Hazard Assault Training | 100 masks, 10 Army XP; 0.25 mastery/day for 30 days; 90-day re-enable | 7.5 mastery per cycle, equipment-backed and bounded |
| Technology commission | 25 PP, 5 non-refundable CP, 7 days | prevents instant mastery-to-formation conversion |
| Policy reassessment | 15-100 PP, 0-40 CP, 90-day lock | makes escalation a strategic commitment |
| Exact-state cleanup | one assignment per nation per 28 days; 3-10 points before spirit | prevents free simultaneous theater cleansing |

Readiness caps rise 39 -> 59 -> 74 -> 89 -> 100 only through exact institutions. Readiness minima rise 10 -> 30 -> 45 -> 65 -> 85; establishment success first raises readiness to 20, while timeout caps it at 9.

## Scenario audit

| Scenario | Expected result | Implementation evidence |
| --- | --- | --- |
| Incapable minor with no masks/agent/project/command/profile | Chaos Warfare visible but unavailable | `cbrn_chaos_warfare_adoption_capable` accepts only five explicit routes |
| Prepared power adopts but fields no Operations HQ | 90-day establishment fails and offense remains closed | mission cancellation requires exact fielded HQ and protected formation |
| Failed institution later acquires all requirements | 14-day paid remediation can succeed | same establishment trigger is reused; no waiver path |
| Country stockpiles masks but produces none after adoption | Protective Foundation remains unavailable | cumulative `total_equipment_produced_gas_mask_equipment` must exceed the stored baseline |
| Delivery track reaches mastery 2 without a protected HQ order | Delivery Integration remains unavailable | success history is written only after Protective Posture preparation completes |
| Country has high doctrine mastery but no payload | offensive policy and prepared attack gates fail | live reserve thresholds remain independent of mastery |
| Ordinary democratic defensive AI | prefers defensive/retaliation policy and receives no base first-use weight | limited/strategic/unrestricted bases are zero; route trigger is required for positive escalation weight |
| Explicit aggressive-route AI | may consider first use but still pays all player-equivalent gates | route flags add weight only; they grant no stock, readiness, institution, or operation proof |
| Nonhuman AI evaluates Stage 5 policy, commission, spirit, or high-command surfaces | receives zero selection weight | each mapped AI block has an explicit `is_actual_nonhuman_country` zero-factor path |
| Chemical Barrage without an exact payload-consumed proof | tactic remains ineligible | trigger requires proof variable and current base route has no adapter that can set it |
| Active Decontamination Corridor, two contaminated states | player may select one exact state; national lock prevents a second assignment for 28 days | state target plus country and state locks; no random-state loop |
| Catastrophic contamination | cleanup is 3 points, or 3.75 with Theater Contamination | inverse output table prevents rapid capstone cleanup |
| Integrated Command M5 chemical use | Condemnation base receives 0.70 before floors; all other outputs unchanged | doctrine multiplier is assigned inside `cbrn_prepare_chemical_action_record` after validation |
| Integrated Command M5 biological use | only biological Condemnation base receives 0.70 | legacy use-count and war-support multipliers removed; potency/duration neutral and CP refunds zero |
| Country adopts Limited, Strategic, or Unrestricted use policy without the occupation-policy gate | nerve-suppression commission remains unavailable | Chaos Warfare policy changes never set `cbrn_nerve_suppression_policy_authorized`; the later CBRN Coercive Security occupation policy owns it |
| Idle chemical-capable aircraft | no contamination or exposure record | no ordinary-air hook or estimator exists; Chemical Air Interdiction is an eligibility marker only |
| Doctrine migration with legacy Concentration unlock | unlock is cleared; native mastery flags are reconstructed | `cbrn_migrate_legacy_chaos_warfare` is idempotent and grants no institution proof |
| Existing save loads with Chaos Warfare but no institutional adoption flag | a one-time zero-cost review decision appears and AI takes it at high priority | no periodic pulse is added; the review calls the same idempotent migration and disappears after adoption is recorded |

Condition-band coverage:

- Weak-program conditions: incapable minor adoption refusal; adoption without an Operations HQ; masks stockpiled without post-adoption production; high mastery without payload; idle chemical-capable aircraft; and suppression commission without the occupation-policy authorization.
- Normal-program conditions: failed establishment followed by exact remediation; Delivery Integration without protected-order history; defensive-profile and explicit aggressive-route AI; nonhuman refusal; fail-closed Chemical Barrage; selected-state decontamination with two eligible states; and legacy/new-save migration.
- High-chaos/capstone conditions: catastrophic contamination cleanup; Integrated Command mastery 5 chemical use; Integrated Command mastery 5 biological use; Terminal Hazard consequence multiplication; and unrestricted-policy consideration under an explicit unrestricted route.

## Parser and asset boundaries

- Installed doctrine documentation does not explicitly support global script constants in static doctrine fields. The five doctrine files therefore use file-local `@` parser values that mirror the centralized tables. Scoped effects, triggers, decisions, ideas, and variables continue to use script constants.
- Installed `add_daily_mastery` documentation and vanilla examples demonstrate literal `amount` and `days` fields only. Hazard Assault Training therefore uses `meta_effect` to inject its centralized variable values as numeric text instead of assuming direct variable-token support.
- All 45 registered Stage 5 runtime asset paths exist. Declared dimensions are seven 64x64 doctrine/technology icons, four 1000x88 ten-frame reward strips, four 212x83 two-frame milestone sheets, six 45x45 spirits, four 60x68 high-command emblems, one 23x33 trait, eighteen 32x32 decisions/missions, and one 52x40 category.
- Every Stage 5 DDS uses the standard 128-byte uncompressed BGRA header, texture caps, real alpha, exact declared dimensions, and no mipmaps. The processor and all 45 runtime files were corrected and regenerated after parent review detected a shifted pixel-format header in the initial custom export.
- Native mastery has no exact per-formation equipment-fill trigger. Hazard Assault Training is the explicit equipment-backed mastery source; ordinary combat mastery remains the current engine's fielded-unit model.

## Specialist findings and closure state

- The decision/mission audit corrected the Theater CBRN Headquarters grant to require Terminal CBRN Command, made adoption and establishment failure restore Defensive Preparation, and assigned zero weight to the three offensive policy decisions and the nerve commission for nonhuman AI. Its proposed use-policy-to-suppression authorization shortcut was rejected because numbered specification 08 assigns that authority to CBRN Coercive Security occupation policy.
- The focused migration-decision re-audit found and fixed two parser/AI ordering risks: nonhuman zero factors now follow all additive route modifiers, and 28/90-day timed flags use exact file-local literals mirroring centralized tuning rather than temporary variables in parser-sensitive `days` fields. Remediation text now discloses that committed PP/CP is not refunded if proof lapses. The auditor returned a commit-safe verdict with no open decision/mission defect.
- Event-chain lint found no blocking issue. Its only relevant warning is static `EVENT_UNREACHABLE_IN_SELECTION` for `cbrn_hq.1`; the event is intentionally dispatched by delayed scripted-helper callers that the static selector does not discover.
- The localisation audit covered 190 Stage 5 identifiers and explicit tooltip keys. It found no missing keys, removed the sole duplicate, converted 34 tuning-sensitive strings to existing dynamic constants, corrected both missing BOMs, and confirmed all four Stage 5 files use valid headers, key format, and resolved nested references.
- Parent integration removed the remaining parallel 0.90/0.80/0.70 tables: shared chemical records and legacy chemical/biological adapters now read `chem_integrated_operations.condemnation_mult` as one migration-safe source. All nonhuman AI policy, commission, spirit, high-command, and commander-trait paths have explicit zero factors. Remaining Stage 5 derived tooltip percentages were replaced with direct constant-backed multiplier or baseline displays; all 88 constant-reference occurrences resolve.
- Offline on-action documentation confirms `on_startup` does not run on save loading. The parent pass added a one-time exact migration decision for doctrine holders missing the new adoption flag, with a distinct final asset and high AI priority, instead of adding a periodic country pulse.

Closure:

- The required read-only completion-auditor invocation was stopped by the service safety filter before it returned findings. This is recorded as an audit limitation, not as a passed specialist verdict. The parent completion audit then rechecked every Stage 5 requirement, scenario band, asset registration, localisation surface, helper, parser mirror, AI refusal path, migration path, and documented engine boundary.
- The final refresh found no Stage 5 balance or scenario defect: all 30 scoped script/GFX files remained structurally coherent; all five doctrine parser files retained defined and used local mirrors; all 50 effects and 48 triggers retained callers and documentation; all 45 runtime DDS files retained valid registered BGRA surfaces; and the Condemnation-only ladder remained exactly 0.90/0.80/0.70.

No balance simplification is accepted by this audit. Unsupported continuous-air activity, combat-tactic payload debit, and direct commander selected-state targeting remain fail-closed engine boundaries rather than estimated substitutes.
