# Stage 5: Chaos Warfare Doctrine, Officer Corps, and Balance

Status: complete for Stage 5; the overall Chaos Warfare goal remains in progress

## Accepted sources and conflict resolution

This stage implements numbered specification 02, the doctrine and technology matrix, the staged implementation plan, and the mapped doctrine/officer-corps surfaces. Numbered specification 08 controls the occupation boundary: Chaos Warfare may unlock nerve-agent suppression capability, but it must not unlock camps, extermination infrastructure, experiment sites, or a generic Concentration occupation law.

The user confirmed that doctrine may reduce Condemnation impact, directly resolving the contrary wording in the Operations Mastery 4 paragraph of numbered specification 02. This applies only to the Condemnation result. It must not reduce or erase payload consumption, deaths, contamination, medical saturation, evidence, attribution, confirmed-use history, resistance trauma, or shared-pipeline public-harm floors.

## Verified engine boundaries

- Grand-doctrine milestone blocks are ordered one-for-one with doctrine tracks and fire when that track is completed. They cannot express the specification's cross-track institutional requirements.
- Country decisions can evaluate the exact institutional requirements without a periodic on-action. The four native milestone blocks will record their corresponding track completion and remain part of the doctrine; four zero-cost claim decisions will enforce the accepted cross-track requirements and grant readiness caps/unlocks.
- `activate_mission` can start a country mission directly. A mission `cancel_trigger` can detect exact establishment success and run `cancel_effect`; `timeout_effect` handles the ninety-day failure state.
- Script has exact cumulative equipment-production dynamic variables, including the generic `total_equipment_produced_<type>` family, but no documented trigger for a currently assigned production line. Protective Foundation will therefore require both a post-adoption increase in gas-mask production and a live gas-mask reserve. This proves real production during the doctrine program and does not estimate factory activity.
- Combat tactics have no verified activation effect that can debit payload and dispatch the shared exposure pipeline. Chemical Barrage remains fail-closed until a prepared-operation adapter consumes payload before making it eligible.

## Compatibility policy

Stable internal IDs remain available for save and script compatibility while their player-facing names and effects are replaced:

| Internal ID | Player-facing doctrine |
| --- | --- |
| `chaos_warfare` | Chaos Warfare |
| `extermination_columns` | Hazard Assault Formations |
| `chemical_suppression` | Toxic Armored Warfare |
| `contaminant_firebases` | Contaminant Fire Support |
| `integrated_chemical_operations` | Integrated CBRN Command |

Legacy reward IDs may remain as compatibility identifiers, but localisation, tooltips, unlocks, and effects must follow the accepted design. The legacy `concentration_occupation_law_unlocked` link will be removed and no replacement genocide unlock will be added.

## Implementation order

### 1. Central doctrine model

- Add `common/script_constants/cbrn_doctrine_constants.txt` for adoption, establishment, milestone thresholds, policy costs, readiness changes, mastery bonuses, AI weights, and balance bands. Keep the 0.90/0.80/0.70 Condemnation ladder in the existing `chem_integrated_operations.condemnation_mult` table so shared chemical records and legacy chemical/biological adapters have one tuning source during migration.
- Add `common/scripted_triggers/cbrn_doctrine_triggers.txt` for capability adoption, establishment proof, all four institutional milestones, policy gates, track/mastery counting, exact reserve checks, and route-aware AI eligibility.
- Add `common/scripted_effects/cbrn_doctrine_effects.txt` for adoption, mission success/failure/remediation, milestone claims, doctrine-only technology grants, policy changes, native track completion records, and migration cleanup.
- Document every new reusable helper in the dynamic trigger/effect references.

### 2. Adoption and institutional progression

- Make Chaos Warfare visible to all countries and available only through one accepted capability gate: masks plus an agent, a completed chemical special project, CBRN command flag, mapped historical program profile, or manual scenario override.
- Keep the 100 Army XP adoption cost.
- On adoption, initialize the CBRN model, set the initial readiness cap to 39, expose program decisions, unlock the Operations HQ Section and Gas Mask/Decontamination support, expose doctrine-only technology progression, enable Defensive Preparation and Retaliation Authority, record the protective-production baseline, and activate the ninety-day establishment mission.
- Establishment success requires the minimum protective reserve, one fielded Operations HQ Section, and one fielded Gas Mask/Decontamination protected formation. Timeout leaves the doctrine active at low readiness with offensive gates closed. A delayed-establishment decision permits exact remediation using the same requirements.
- Implement four explicit claim decisions:
  1. Protective Foundation: post-adoption mask production, live protective reserve, and one fielded CBRN HQ company; cap 59.
  2. Delivery Integration: one delivery track at mastery 2, a payload reserve above the centralized operational minimum, and a historically recorded protected Army HQ order; cap 74.
  3. Theater Exploitation: any two tracks at mastery 3, decontamination capacity at least 40, and a fielded Intelligence/Weather Cell; cap 89.
  4. Terminal CBRN Command: all four tracks active, any track at mastery 5, policy at Limited Battlefield Authority or higher, and advanced gas-mask technology or an explicit equivalent-project flag; cap 100.

### 3. Doctrine track rewrite

- Remove the grand doctrine's broad 20 percent chemical-support attack package.
- Replace broad permanent stacks with modest unit-specific retention/reliability effects and explicit unlock flags consumed by prepared operations.
- Hazard Assault Formations: mask discipline, Hazard Pioneer technology, Chaos Assault Battalion, shock exploitation, and a fail-closed terminal-operation unlock.
- Toxic Armored Warfare: sealed crews, armored delivery, nerve-suppression formation, protected breakthrough logistics, and a costed synchronized-operation unlock. Remove every genocide/camp link.
- Contaminant Fire Support: ammunition train, projector fire control, counterbattery fire, shell logistics, persistent distribution, and deep-contamination operation unlocks.
- Integrated CBRN Command: Operations HQ, intelligence/weather, protective logistics, mobile decontamination, air/biological coordination, and Theater CBRN Headquarters.
- Keep all delivery effects behind the shared exposure pipeline. Doctrine flags may enable adapters; they may not create free contamination or casualties.

### 4. HQ ability and tactic gates

- Protective Posture requires Protective Foundation.
- Prepare Chemical Offensive requires Delivery Integration.
- Decontamination Corridor and combined-delivery preparation require Theater Exploitation.
- Combined Overmatch requires Terminal CBRN Command.
- Successful completion of Protective Posture preparation records the exact historical protected-order fact used by Delivery Integration. Starting an order that later fails preparation does not qualify.
- Chemical Barrage remains weight zero and ineligible unless a later prepared-order adapter provides an exact payload-consumed proof.

### 5. Use policy ladder

- Add player-facing policy decisions with political power, command power, readiness, institution, and stockpile gates.
- Adoption exposes Defensive Preparation and Retaliation Authority.
- Delivery Integration exposes Limited Battlefield Authority.
- Theater Exploitation exposes Strategic Release Authority.
- Terminal CBRN Command exposes Unrestricted Chaos Warfare with explicit consequence warnings.
- Ordinary democratic and defensive AI remains at defensive/retaliation policy unless an accepted route/profile condition authorizes escalation.

### 6. Officer corps and leader traits

- Replace the legacy stackable CBRN spirits with mutually exclusive Army Command families: Controlled Retaliation Doctrine, Theater Contamination Doctrine, and Terminal Hazard Doctrine.
- Add mutually exclusive Division Command families: Mask Discipline, Hazard Assault Cadres, and Contaminant Fire Coordination.
- Implement generic high-command role traits without inventing historical people: CBRN Operations Director, Civil Defence Coordinator, Chemical Logistics Inspector, and Biological Security Director.
- Replace the old cylinder-ability commander trait with command roles tied to the prepared HQ system; preserve obsolete status IDs only where live cleanup needs them.
- Keep bonuses modest and route-specific. Strong effects must be operational, supplied, and cooldown-bound.

### 7. Doctrine-only technology and unlock audit

- Wire exact mastery/institution grants for Hazard Pioneer Formation, Chemical Artillery Shells, Persistent Agent Shell Filling, Armored Agent Delivery, Sealed Tank Crews, Nerve Agent Suppression Formation, Chaos Assault Battalion, Chemical Air Interdiction if a mapped current technology exists, Theater CBRN Headquarters, and Biological Security Assault Formation.
- Keep doctrine-only technologies non-researchable and grant them through doctrine effects only.
- Do not invent a continuous-air contamination hook.

### 8. Assets and localisation

- Register stable sprite IDs before asset production.
- Produce unique final doctrine, spirit, and trait icons through the Chaos Redux asset workflow. No placeholder, cross-type resize, or single-icon reuse is acceptable.
- Replace all player-facing legacy atrocity terminology and write final English localisation from the package direction.
- Keep localisation UTF-8 with BOM and synchronize requirements, costs, readiness caps, unlocks, and consequence warnings.

### 9. Validation and audits

- Run doctrine balance analysis against all permanent modifiers, support-company stats, technologies, spirits, and active abilities.
- Audit adoption gates, establishment success/failure/remediation, every milestone permutation, policy ladder, AI refusal/escalation profiles, doctrine-only tech grants, HQ ability gates, legacy migration, and Condemnation floor preservation.
- Run the doctrine-relevant specialist audits, localisation audit, asset audit, improvement-loop pass, and Stage 5 completion checklist.
- Commit only the complete Stage 5 surface. Carry any unsupported behavior or unresolved finding forward explicitly; do not mark the overall goal complete.

## Implementation and audit evidence

- The decision/mission audit tightened Theater CBRN Headquarters to Terminal CBRN Command, restored Defensive Preparation after adoption/establishment failure, and kept nonhuman AI at zero weight for offensive policy and nerve-suppression commission decisions.
- The migration-decision re-audit passed after moving each offensive-policy and nerve-commission nonhuman zero factor after every additive route modifier, replacing parser-sensitive temporary-variable timed flags with exact file-local 28/90-day mirrors, and making the non-refundable remediation commitment explicit to the player.
- A proposed shortcut that treated Limited Battlefield Authority as nerve-suppression authorization was rejected. Numbered specification 08 makes the later CBRN Coercive Security occupation policy the sole owner of `cbrn_nerve_suppression_policy_authorized`; Stage 5 therefore leaves the commission fail-closed until that surface exists.
- Installed `add_daily_mastery` documentation demonstrates literal amount and duration fields only. Hazard Assault Training injects its centralized values through `meta_effect` rather than relying on undocumented direct variable parsing.
- Event-chain lint reports no blocker. Its sole relevant warning is the expected static-unreachable notice for `cbrn_hq.1`, whose actual delayed scripted-helper callers are outside the selector's static reachability model.
- The localisation audit covered 190 Stage 5 identifiers/tooltips with no missing keys, removed one duplicate, converted 34 tuning-sensitive strings to dynamic constants, and verified UTF-8 BOM and key-format compliance across all four Stage 5 localisation files.
- Parent integration consolidated the doctrine's 0.90/0.80/0.70 Condemnation ladder into the existing `chem_integrated_operations.condemnation_mult` table used by shared and legacy chemical/biological callers, added explicit nonhuman-AI refusal to all remaining Stage 5 selection surfaces, and replaced residual derived tooltip literals with direct constant-backed displays.
- Offline on-action documentation proves that `on_startup` does not execute on save loading. A one-time zero-cost institutional review decision now exposes the idempotent migration to any existing doctrine holder missing the adoption flag, without a broad periodic pulse or fabricated institution proof.
- The institutional review uses an independent final 32x32 ledger/dossier icon with source, alpha master, processed PNG, DDS, contact-sheet, manifest, and GFX handoff coverage. Parent inspection accepted the decision-scale concept and registered its exact runtime sprite.
- Asset integration found and corrected a shifted custom DDS pixel-format header in the Stage 5 processor. All 45 Stage 5 DDS files were regenerated with the standard 128-byte uncompressed BGRA header, `DDSCAPS_TEXTURE`, real alpha, exact declared dimensions, and no mipmaps.
- The required read-only Stage 5 completion-auditor invocation was attempted after the decision/mission and localisation audits. The service safety filter stopped that auditor before it produced findings. The blocked invocation is not treated as a passed specialist verdict and was not retried; the parent completed the closure comparison locally against the numbered specifications, matrices, specialist prompts, balance scenarios, asset manifest, localisation coverage, helper ownership, and disclosed engine limits.
- The final local refresh covered 30 Stage 5 script/GFX files, all five doctrine parser files, 530 localisation keys and 88 dynamic constant references, 50 doctrine effects, 48 doctrine triggers, all 45 DDS/GFX registrations, the canonical 0.90/0.80/0.70 Condemnation ladder, AI modifier ordering, parser-sensitive 28/90-day mirrors, and suppression-policy ownership. It found no unresolved Stage 5 defect.

## Stage acceptance criteria

- No universal 20 percent doctrine attack package remains.
- The 90-day mission has exact success, failure, and remediation outcomes.
- All four institutional milestones enforce their accepted requirements and set caps 59/74/89/100.
- Every strong doctrine unlock is equipment-, readiness-, policy-, and/or operation-gated.
- Doctrine Condemnation mitigation is bounded to the shared 0.70 minimum and public-harm floors.
- Evidence, attribution, deaths, contamination, medical saturation, and historical-use records are unaffected by doctrine mitigation.
- Chemical tactics cannot create free exposure.
- No doctrine or reward unlocks genocide infrastructure or the legacy Concentration law.
- Officer-corps families are mutually exclusive, localized, AI-gated, and represented by final assets.
- All compatibility IDs and migration cleanup are documented.

Stage 5 closes on these criteria. Chemical delivery-route migration, the complete biological and nerve-suppression systems, full consequences and sanctions, achievements, scripted GUI, country profiles, and package-wide scenarios remain mandatory later-stage work and prevent an overall completion claim.
