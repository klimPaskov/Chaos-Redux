# Event 006 Mediterranean and FORM-05 Decision/Mission Audit

**Date:** 2026-07-16
**Verdict:** **READY** for parent integration review after the two bounded mission fixes recorded below.
**Scope:** IW-017 Corsica (`COR`), IW-018 Sardinia (`ARX`), IW-019 Sicily (`ASX`), and FORM-05 Mediterranean Island League decision/mission surfaces.

This verdict does **not** admit IW-017, IW-018, or IW-019 into the allocator. Candidate-registry and allocator status were inspected only for context and were not edited.

## Files changed

- `common/decisions/006_independence_wave_form05_decisions.txt`
  - `independence_wave_form05_charter_deadline`
  - `independence_wave_form05_complete_first_maritime_board`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_mediterranean_form05_decision_mission_audit_2026_07_16.md`

No portrait, advisor-art, candidate-registry, allocator, spreadsheet, or gameplay file outside the bounded FORM-05 decision file was edited. No commit was created.

## Confirmed defect and correction

Both FORM-05 deadline missions were manually started with `activate_mission`, but their non-selectable `available` condition was absent. For a mission, the default available condition is true; that makes the mission satisfy its completion condition immediately instead of remaining active until its deadline or an explicit removal. Both missions also used `is_good = yes` even though timer expiry invokes a failure effect.

Each mission now has a fail-closed completion condition:

```txt
available = {
	hidden_trigger = { always = no }
}
```

Both now use `is_good = no`. They therefore remain active after manual activation, retain their 540-day and 720-day timers, and reach their failure effect if uninterrupted. Existing explicit `remove_mission` calls remain the successful completion path and, per the official effect documentation, remove the mission without running completion or timeout effects.

## Audit findings

### COR, ARX, and ASX packages

- The three founding missions are active deadline mechanics, not passive checklist missions. Their completion condition is explicitly false; progress comes from costed projects and incident choices, while capital loss or the 240-day timeout applies the founding failure.
- Package starting/stable values are COR 30/65, ARX 28/65, and ASX 22/70. Projects use visible gains of 5, 10, and 15 and visible failure pressure rather than hidden reward dust.
- Timed projects use concrete 75-, 120-, 180-, and 300-day durations and serialize through package-specific active-project gates.
- Shared cost classes debit actual resources: administration light/standard use 10/20 command power plus 2,500/5,000 manpower; diplomatic standard uses 20 command power plus 10 convoys or trains; security light uses 10 command power, 250 infantry equipment, and 50 support equipment; security standard uses 5,000 manpower, 20 army experience, 500 infantry equipment, and 100 support equipment; strategic projects also debit stability and war support. Factory assignments are visible through the decision modifiers and cost text.
- Cancellation and timeout conditions are tied to exact package eligibility, anchor control, route state, and project state. The decisions do not create divisions, equipment, manpower, or factories, so no repeatable free-unit/resource loop was found.
- AI weights are present on all selectable projects and incidents. Security, patron, congress, and route choices react to host threat or route state; the country AI strategy profiles are origin/package gated and do not start wars or bypass charter consent.

### FORM-05 readiness, consent, and sovereignty

- Carrier eligibility is exact: Event 006 origin, exact COR/ARX/ASX package identity, the correct anchor state and naval base, independent status, FORM-05 selection/readiness attestation, route mandate, regional-power status, and a connected partner.
- Sicily's FORM-05 mandate requires the Mediterranean-republic choice and excludes its Two Sicilies dossier route.
- Readiness requires FORM-05 family registration/selection, family value 5, adapter/audit flags, readiness attestation, identity availability, and either a valid preformation carrier or valid postformation carrier/member state.
- The charter needs two sovereign consents, including an actual connected second COR/ARX/ASX government. Connection is re-evaluated and candidate/member triggers require `is_subject = no`.
- Proclamation requires all three charter articles at 70, a settled congress seat after the 50-value compromise gate, and minimum live consent. Only the carrier receives the `MIX` cosmetic identity. Members retain their tags, states, cores, capitals, armed forces, and institutions; no annexation, state transfer, core grant, or subject creation occurs.
- The first maritime board requires all three institutional projects, all three public values at 95, and a live autonomous member. Its 720-day failure applies visible losses and a breakdown/recovery path; reconvening remains costed.

### Localisation and assets

- 189 direct name, description, title, custom-cost, and effect-tooltip consumers were checked. All resolve: 183 are in the two tranche localisation files and the six shared cost keys resolve in `006_independence_wave_decisions_l_english.yml`.
- Both tranche localisation files retain UTF-8 BOM encoding.
- 15 decision icon consumers resolve to registered sprites. All 45 textures referenced by the two Mediterranean/FORM-05 sprite files exist.
- Mission descriptions expose the 540-day charter deadline, 720-day first-board deadline, consent count, article thresholds, and sovereign-member behavior.

### Isolation and exploit checks

- No `SOV`, Event-5 namespace, Soviet event target, or Soviet helper reference occurs in the bounded decisions, triggers, effects, or events.
- No `create_unit`, `add_unit`, division-template load, equipment stockpile grant, OOB load, or manpower grant occurs in the bounded gameplay path.
- IW-017 through IW-019 allocator admission was not changed.

## References used

- Offline Paradox wiki core pages, including Decision Modding mission semantics, Triggers, Effects, Data Structures, Scopes, Localisation, Event Modding, On Actions, Modifiers, Ideas, and AI Modding.
- Vanilla `common/decisions/_documentation.md` and official effects/triggers documentation.
- Vanilla Philippine intervention mission as the manual-activation/fail-closed mission precedent.
- Vanilla Nordic League formable decision as the independent-member/formable structural precedent.
- Repository skills `chaos-redux-decisions-missions` and `chaos-redux-subagents`.

## Remaining risks and scope boundaries

- This was a static source audit of the bounded decision/mission package in a heavily concurrent worktree; it is not an allocator-admission approval.
- No fallback, placeholder, or simplification was introduced.
- No remaining blocker was found inside the audited surface.
