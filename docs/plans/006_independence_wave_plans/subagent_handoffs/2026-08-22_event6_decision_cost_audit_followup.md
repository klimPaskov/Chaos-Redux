# Event 006 decision-cost audit follow-up

Date: 2026-08-22.

Mode: read-only source audit; no gameplay file was edited or reverted.

Scope: the seven requested decision, scripted-trigger, scripted-effect, and localisation files, plus the dependent Pacific, Transcaucasus, FORM-03, IW-058, FORM-05, FORM-39, Montenegro, and formable-registry files needed for the named callsites.

This handoff covers current source only and does not claim whole Event 006 completion.

## Verdict

Verdict: CONDITIONAL; follow-up fixes remain.

DM-51, DM-52, DM-56, DM-57, DM-58, the Pacific island palette, IW-058 fortification, FORM-05’s three named strategic actions, and FORM-39 plebiscites are within the four-group ceiling and have matching payment paths in current source.

The remaining findings are a shared-strategic factory reservation gap, a FORM-39 shipping palette decision, a missing MNT strategic factory reservation, stale Transcaucasus cost prose, a FORM-03 major-factory trigger mismatch, a strategic-major trigger mismatch, and stale FORM-05 reopening wording.

## Severity-sorted findings

### High: six shared strategic decisions display and gate a factory without reserving one

The shared trigger at common/scripted_triggers/006_independence_wave_decision_triggers.txt:386-390 requires stability, command power, transport, and available civilian factories.

The shared payment at common/scripted_effects/006_independence_wave_decision_effects.txt:331-334 pays stability, command power, and transport; the factory must be reserved by the decision modifier.

These six decisions use the shared strategic trigger, payment, and four-group strategic text but have no civilian_factory_use modifier: independence_wave_demand_recognition_by_force at common/decisions/006_independence_wave_decisions.txt:1439-1499, independence_wave_offer_association_or_reunion at 1502-1551, independence_wave_grant_base_or_transit_rights at 1790-1848, independence_wave_choose_client_future at 2006-2045, independence_wave_challenge_league_leadership at 2706-2767, and independence_wave_transform_league_charter at 3687-3759.

Recommended fix: add the standard factory modifier to these six blocks, or intentionally replace their trigger and localisation with a three-group palette if factories are not meant to be committed.

### High: Transcaucasus IW-070, IW-071, and IW-072 text overstates command power and descriptions still mention Army XP

The new triggers at common/scripted_triggers/006_independence_wave_transcaucasus_package_triggers.txt:319-325, 339-345, and 353-359 use material security plus package command and equipment thresholds.

The matching payments at common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt:221-227, 265-271, and 291-297 consume manpower, infantry equipment, support equipment, and only the package-specific command amount.

The base cost strings at localisation/english/006_independence_wave_transcaucasus_l_english.yml:59, 61, and 62 still add command_power_standard to the package-specific command value, displaying 20 more command power than the effects consume.

Recommended fix: remove command_power_standard from those three base strings, or add the same standard command payment to all three effects if the larger total is intended.

The descriptions at the same localisation file lines 12, 23, and 32 still mention experience even though the current trigger and payment paths no longer use Army XP.

Recommended fix: remove the Army XP wording from all three descriptions.

### Medium: FORM-39 shipping has four paid groups but an unreserved factory gate

FORM-39 shipping at common/decisions/006_independence_wave_form39_decisions.txt:90-119 calls the shipping trigger, payment, and cost triad.

The current payment at common/scripted_effects/006_independence_wave_form39_effects.txt:160-163 consumes stability, two standard command spends, standard convoy or trains, and standard manpower.

The current base cost at localisation/english/006_independence_wave_formable_registry_l_english.yml:160 shows four groups: stability, command power, transport, and manpower.

The trigger at common/scripted_triggers/006_independence_wave_form39_triggers.txt:194-202 still delegates to strategic and standard-administration helpers, which require available factories, while the decision has no factory modifier.

The tooltip and blocked text at localisation lines 161-162 still mention spare factories.

Preferred palette: retain stability, command power 40 total, convoy or train, and manpower because those are the four resources actually paid.

Recommended fix: make the shipping trigger directly check those four paid groups plus family, member, and active-project gates, then remove the unreserved factory clause from tooltip and blocked text.

If a factory commitment is intended, add a factory modifier and drop manpower so the action remains at four groups.

### Pass with current edits: FORM-39 plebiscites

FORM-39 plebiscites at common/decisions/006_independence_wave_form39_decisions.txt:152-181 use a trigger at common/scripted_triggers/006_independence_wave_form39_triggers.txt:221-228 and payment at common/scripted_effects/006_independence_wave_form39_effects.txt:170-173.

Those paths and localisation/english/006_independence_wave_formable_registry_l_english.yml:166-168 agree on command power, manpower, infantry, and support equipment, with no stability, war support, transport, factory, or Army XP.

### Medium: MNT strategic sovereignty displays a factory without reserving one

MNT durable sovereignty at common/decisions/006_independence_wave_montenegro_decisions.txt:233-244 uses the MNT strategic trigger and shared strategic payment.

The trigger at common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt:49-53 checks one available project factory, stability, command power, and transport.

The current localisation at localisation/english/006_independence_wave_montenegro_l_english.yml:78-80 displays those four groups and has already removed war support, but the decision has no civilian_factory_use modifier.

Recommended fix: add the one-factory light modifier used by the MNT constants and neighboring projects, or remove the factory gate and display if the factory is eligibility-only.

### Medium: strategic-major actions use a standard factory custom trigger

The strategic-major text at localisation/english/006_independence_wave_decisions_l_english.yml:40 displays major factories.

Buy-out concession, sponsor plebiscite, and negotiate transfer at common/decisions/006_independence_wave_decisions.txt:1912-1930, 3070-3079, and 3147-3160 use the standard strategic helper in both available and custom_cost_trigger, but use a major factory modifier and text.

Recommended fix: add a major factory gate to those checks or add a reusable strategic-major helper.

### Medium: FORM-03 reopening custom-cost trigger omits its major factory gate

FORM-03 reopening at common/decisions/006_independence_wave_form03_decisions.txt:640-665 has a major factory available check, modifier, and four-group text at localisation/english/006_independence_wave_form03_l_english.yml:214-216.

Its custom_cost_trigger still calls only the standard strategic helper.

Recommended fix: add the major factory gate to custom_cost_trigger or route both checks through a major helper.

### Low: FORM-05 reopening description retains removed war-support wording

FORM-05 proclamation, reopening, and first-board reconvening cost triads at localisation/english/006_independence_wave_form05_l_english.yml:81-87, 100-103, and 112-113 now show stability, command power, convoy or train, and one light factory.

The proclamation payment no longer adds the former administration-light charge, and the FORM-05 strategic trigger no longer checks war support.

The reopening description at localisation line 60 still says it commits war support.

Recommended fix: remove war support from that description.

## Four-group decision matrix

| Surface | Trigger/payment | Text and group count | Verdict |
| --- | --- | --- | --- |
| DM-51 border ultimatum | Border helper and matching payment | Main localisation lines 45, 57, 58; stability, command, infantry, support | Pass |
| DM-52 and DM-56 integration | Integration helper and matching payment | Main lines 46, 71, 72; command, manpower, infantry, support | Pass |
| DM-57 breakaway sponsorship | Coordinated-operation helper and payment | Main lines 47, 59, 60; command, convoy or train, infantry, support | Pass |
| DM-58 reclamation front | Coordinated-operation helper and payment after the witness | Main lines 48, 75, 76; command, convoy or train, infantry, support | Pass |
| Pacific island strategic | Pacific trigger lines 186-191 and effect lines 195-203 | Pacific localisation lines 117-119; stability, command, manpower, convoy | Pass |
| IW-070, IW-071, IW-072 | Material helper plus package command/equipment thresholds and payments | Transcaucasus lines 59, 61, 62; command, manpower, infantry, support | Text mismatch |
| IW-058 fortification | Direct infantry/support/train transaction, zero command and manpower, factory modifier | IW-058 lines 147-149; infantry, support, train, factory | Pass |
| FORM-05 three named actions | Shared strategic payment plus light factory modifier | FORM-05 triads; stability, command, transport, factory | Pass with stale reopening prose |
| FORM-39 shipping | Strategic plus administration payment | Registry lines 160-162; four paid groups plus unreserved factory gate | Follow-up |
| FORM-39 plebiscites | Command plus material-security payment | Registry lines 166-168; command, manpower, infantry, support | Pass |
| MNT strategic | Shared strategic payment plus factory availability gate | Montenegro lines 78-80; stability, command, transport, factory | Missing modifier |

Convoy or train is one spendable group because the payment selects one alternative.

## Lifecycle and mission quality

DM-51, DM-52, DM-56, and DM-57 use target validity, active-operation guards, completion effects, cancellation conditions, one-shot or cooldown controls, and route-specific AI checks.

DM-58 is a selectable mission with a three-compliant-member and three-external-owner witness, timeout, success payment after validation, invalid-witness rollback, crisis escalation, and cleanup flags.

Pacific projects are package- and capital-locked, timed, cancellable, and failure-cleaned.

IW-070, IW-071, and IW-072 are package-bound timed projects with capital cancellation and in-progress flags cleared by completion or cleanup.

FORM-03 reopening is a timed post-charter repair project with route-loss cancellation.

IW-058 binds one force package, begins one paid transaction, stores a receipt, and commits or rolls back on success, invalid binding, timeout, or cancellation.

FORM-05 reopening and first-board reconvening reserve and cancel the charter opening; proclamation and stage actions are gated by stage flags and project guards.

FORM-39 shipping and plebiscites set active-project flags at payment time and clear them on completion or cancellation, with bound-member checks limiting duplicate risk.

MNT sovereignty is fire-once and route-gated, but its advertised factory is not reserved.

## Cognitive-load and localisation notes

Named cost strings are at or below four displayed spendable groups after current edits.

DM-58’s reserve threshold is a non-spend witness requirement and is explained in its preflight and description.

FORM-05, FORM-39 plebiscites, Pacific, and IW-058 use compact icon-first triads.

FORM-39 shipping appends a prose spare-factory requirement outside its four displayed groups; this must be made an intentional requirement or removed.

Transcaucasus descriptions and command text are currently inaccurate.

The duplicate-key parser found no in-file or cross-file duplicate keys across the nine relevant localisation files: main decision, Pacific, Transcaucasus, Transcaucasus cost wrappers, FORM-03, IW-058, FORM-05, formable registry, and Montenegro.

Every named cost surface has a base, tooltip, and blocked key.

The adjacent FORM-39 civil-service key remains outside the six named remaining keys and still has separate strategic/transport prose.

The unrelated DM-22 emergency-formation action still has its own war-support behavior and is not part of the narrowed DM-51/52/56/57/58 palette.

## AI and MCP evidence

FORM-05 probability inspection used mission_ai_will_do and found all three requested candidates.

FORM-05 inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/10129f205803b2d6b49b6cad7e21f306c44ae1acf773c4b0ba6ed0774c6424b1/9ab6dfdb1b318460edafa80b98ce61ed96f1fc2865e5aa5324d8658dd26ff1b2/probability-inspect-bd0fc361f53a.json.

FORM-05 single-candidate evaluation probability-fb4115118bedeca6f6301ac0 was partial and reported the empty fixture as never eligible; no ranking claim is made.

The FORM-05 three-candidate evaluation returned the exact blocker INTERNAL_ERROR: Unexpected internal error.

FORM-39 inspection used mission_ai_will_do after decision-adapter discovery and found both requested candidates.

FORM-39 inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b130f1e9a05ae2855dc19a81c26b683ee5d3314bb7fa947fb9534fbd15fbfe9f/67c10eebe5937e0fb6ee83a8507b847c9b6f4f66e8e1dfc260398e8f9541330e/probability-inspect-2ab6709d573a.json.

FORM-39 evaluation probability-5cac68f15a5e4c20f7a083c6 was partial with 71 unresolved items and warned that both candidates were never eligible in the supplied empty/AI fixtures.

MNT inspection used decision_ai_will_do after adapter discovery and found the sovereignty candidate.

MNT inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dd25d6c6f95b9fc9108726ff872f3fdcdb40c0df06c3e422c31409a753b2c986/6546d75d04a1c92ffb0288c6fddbde821e4d348347020bf4847ca52807b70a49/probability-inspect-1fafda40d260.json.

MNT evaluation probability-d17016532061d053acc1bcf1 was partial with 16 unresolved items and warned that sovereignty was never eligible in the empty fixture.

The original DM pool was inspected through mission_ai_will_do because the decision adapter matched no candidates.

Original DM inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f697b040649a2f40c9281628bd29cc085879b9732aed23c44c93256b7594cc00/4b7e7d73115a0a1974ebc046e9ac10cf9ddce53a7698712c70cb6381654057a0/probability-inspect-ca15c59248ac4.json.

The original DM evaluation and numeric security sweep were partial with unresolved inputs; no exact rank or selection conclusion is claimed.

No probability compare was run because this auditor made no gameplay patch.

No scripted_gui, interface, or dedicated GUI identifier was found in the scoped decision surfaces or dependencies, so GUI inspect/render was not applicable.

The installed MCP inventory has no hoi4.decision_inspect route; source review and probability artifacts are not equivalent decision-engine evidence.

No live Hearts of Iron IV session was launched.

## Recommended fix order

1. Add factory modifiers to the six shared strategic actions, or remove their factory gates and text.
2. Choose the FORM-39 shipping four-group palette and synchronize trigger, payment, and text.
3. Add the MNT strategic light-factory modifier or remove the factory gate and text.
4. Correct Transcaucasus command text and Army XP prose.
5. Add major-factory custom triggers to FORM-03 reopening and the three strategic-major actions.
6. Remove war support from the FORM-05 reopening description.
7. Re-run probability inspection/evaluation against settled source and scenario fixtures, then compare only after an owner-applied patch.

Task-specific validation consisted of targeted source scans, the nine-file duplicate-key parser, cost-triad presence checks, and the MCP probability workflow.

Gameplay loading and live consumer validation were skipped because this was a read-only audit and live validation belongs to the user.

No gameplay file was changed; this handoff is the only artifact created by the auditor.
