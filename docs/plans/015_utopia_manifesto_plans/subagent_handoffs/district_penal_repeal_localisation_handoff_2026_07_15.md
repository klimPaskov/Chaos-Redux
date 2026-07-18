# Event 015 district, Penal Works, and repeal localisation handoff

Handoff date: `2026-07-15`  
Role: bounded localisation implementation worker  
Scope: Garden Settlement district lifecycle, Penal Works, total repeal, and Events `chaosx.nr15.45` through `.47` plus `.120` through `.123`

## Outcome

The assigned player-facing English localisation is implemented and aligned to the current decision, trigger, scripted-effect, event, and dynamic-modifier source.

The Commonwealth Ledger Stores panel now shows the recorded district state and public project details whenever a state exists. The display reports the live phase, the intersection of surveyed and currently suitable roles, live housing and transport obligations, the live role-plan obligation or Penal Works substitute, expected calling relief, and the first applicable invalidation or retry reason. It no longer uses the right-hand Stores panel for internal batch reporting.

The district decisions and missions describe exact state suitability, start holdings, consumed costs, live completion obligations, four role outputs, incomplete-state consequences, route-charter effects, and permanent calling relief. Penal Works describes its exact cost, initial and revised state modifiers, role-plan substitution, immediate and completion civilian deaths through the shared Deaths system, and the historical conduct that survives a halt.

Total repeal is localized as a terminal constitutional course with exact cost and cancellation conditions. Its aftermath wording distinguishes ordinary dissolution, succession by a viable external League member, abandonment without a practical domestic legacy, the three available practical legacies, return of administered ownership or control, equal reconstruction, refusal of restitution, and the three possible public statuses of the Manifesto.

## Files changed

- `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt`
  - Added the seven required district helpers.
  - Added one district project-summary helper and three obligation-requirement helpers used by the status text.
  - Surveyed-role output now requires both the recorded survey flag and the corresponding live suitability trigger.
- `localisation/english/015_utopia_manifesto_l_english.yml`
  - Replaced the right-hand Stores panel with bounded-center and district project state.
  - Added all district scripted-localisation strings.
  - Added district and Penal Works decisions, missions, costs, and tooltips.
  - Added total-repeal decision, mission, cost, terminal warning, outcome, and cancellation localisation.
- `localisation/english/015_utopia_manifesto_events_l_english.yml`
  - Added Events `.45`, `.46`, and `.47` with exact Ledger, state-modifier, relation, and Deaths consequences.
  - Reworked Events `.120` through `.123` against the final aftermath chain.
  - Added all twelve aftermath effect tooltips referenced by those events.
- `localisation/english/015_utopia_manifesto_ideas_l_english.yml`
  - Added the incomplete district modifier, five route-charter state modifiers, and active Penal Works modifier.
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/district_penal_repeal_localisation_handoff_2026_07_15.md`
  - Records the bounded implementation and parent integration evidence.

These files already contained concurrent Event 015 work in the shared worktree. This handoff covers only the surfaces listed above and does not claim unrelated changes in the same files.

## Scripted localisation contract

Required helpers implemented exactly once:

- `GetUtopiaManifestoDistrictRole`
- `GetUtopiaManifestoDistrictPhase`
- `GetUtopiaManifestoDistrictHousingStatus`
- `GetUtopiaManifestoDistrictTransportStatus`
- `GetUtopiaManifestoDistrictRolePlanStatus`
- `GetUtopiaManifestoDistrictCallingRelief`
- `GetUtopiaManifestoDistrictInvalidationReason`

Supporting helpers:

- `GetUtopiaManifestoDistrictProjectSummary`
- `GetUtopiaManifestoDistrictHousingRequirement`
- `GetUtopiaManifestoDistrictTransportRequirement`
- `GetUtopiaManifestoDistrictRolePlanRequirement`

The role helper covers all fifteen non-empty combinations of the four surveyed roles. A combination is displayed only when each listed role still passes its live suitability trigger, so a stale survey does not advertise an option that its decision target trigger currently rejects.

## Mechanical alignment evidence

District and Penal Works wording reflects the implemented source values:

- Survey cost: `25` Political Power, `5` Trains, and `25` Motorized Equipment.
- Market-Garden start and consumption: more than `500` Manpower, `70` Support Equipment, and `15` Trains held, then `500`, `50`, and `10` consumed with `40` Political Power.
- Industrial Housing start and consumption: more than `1,500` Manpower, `120` Support Equipment, and `75` Motorized Equipment held, then `1,500`, `100`, and `50` consumed with `40` Political Power.
- Rail Junction start and consumption: more than `1,500` Manpower, `25` Trains, and `70` Support Equipment held, then `1,500`, `20`, and `50` consumed with `40` Political Power.
- Refugee Municipality start and consumption: more than `3,000` Manpower, `120` Support Equipment, `15` Trains, and `75` Motorized Equipment held with Common Reserve above `30`, then `3,000`, `100`, `10`, `50`, and `5` Common Reserve consumed with `60` Political Power.
- District charter cost: `40` Political Power and `20` Support Equipment. Household Consent adds `30` days.
- Penal Works cost: `15` Political Power, `3,000` Manpower, `500` Infantry Equipment, `100` Support Equipment, and `10` Common Reserve.
- Penal Works state values: `+25%` Building Construction Speed, `-10%` Local Supplies, `+25%` Required Garrisons, and initial `+12%` Resistance Target. Supervision or inspection sets resistance to `+8%`, while the hardened timetable sets it to `+18%`.
- Penal Works deaths: `500` civilians at activation and `1,000` on successful district completion while active, both recorded through the shared Deaths system.

Total-repeal wording reflects `90` Political Power, `5%` Stability, `100` Support Equipment, and `10` Trains. The mission cancellation text reports the implemented Ledger change of Need `+3`, Plenty `-3`, Concord `-5`, and Assignment `+3`, with no refund of the paid cost.

The League-survival tooltip states the actual formal-defense behavior. If the founder leads the faction and the selected viable successor belongs to it, leadership transfers to the successor and the founder leaves. Non-faction compact continuity is described as durable post-founder member records.

The colonial aftermath tooltips distinguish ownership return for purchased or enforced states from controller return for leased, jointly administered, or Assigned Colony states. Every route returns the recorded ground. Only the compact route records reconstruction partnerships, and only the refusal route records refusal of restitution and the Stale Claim disqualifier.

## Validation evidence

- All `194` unique scripted-localisation key references in the Event 015 scripted-localisation file resolve in the three owned localisation files. Missing references: `0`.
- The district helpers introduce `78` unique `utopia_manifesto.district.*` localisation keys. Missing definitions: `0`.
- All seven required helper names occur exactly once.
- Required district, Penal Works, total-repeal, event, modifier, and twelve aftermath-tooltip keys are present. Missing required keys: `0`.
- Duplicate keys across the three owned localisation files: `0`.
- The scripted-localisation brace delta is `0`, and it contains no direct localisation formatting tokens.
- The three English localisation files retain UTF-8 BOM encoding.
- The newly written player-facing ranges contain no em dash, semicolon, or `:0` localisation version suffix.

## Parent integration

The parent should retain these edits when reconciling the final Event 015 commit. No gameplay or interface file was edited by this worker. No commit was created because the parent owns the integrated Event 015 commit and the shared worktree contains concurrent changes.

The district-aftermath availability check was reviewed during this work. It now reads the same `utopia_manifesto_completed_district_projects` variable that district completion increments.

## Skills and references used

- `chaos-redux-events` for Event 015 localisation voice, event-chain alignment, and completion handoff requirements.
- `hoi4-decisions-missions` for targeted decision, mission, dynamic cost, cancellation, and timeout localisation alignment.
- `chaos-redux-subagents` for bounded ownership and evidence-rich parent handoff.

The required offline Paradox wiki core pages and the relevant vanilla localisation, trigger, effect, scope, event, decision, idea, AI, and script-concept documentation were consulted. Vanilla scripted-localisation precedents were inspected. No skill was created or updated because the existing skills already covered this reusable workflow.

## Simplifications, omissions, blockers, and residual risks

- Simplifications: none.
- Fallbacks: none.
- Missing assigned localisation: none.
- Blockers: none.
- Residual risks: none identified in the bounded localisation surface after source comparison and key-coverage checks.
