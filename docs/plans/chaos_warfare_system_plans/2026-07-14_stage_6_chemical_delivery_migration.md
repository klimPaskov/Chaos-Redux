# Stage 6: Chemical Delivery, Payload Logistics, and Consequence Dispatch

Status: in progress; the overall Chaos Warfare goal remains incomplete

Current tranche: the equipment, payload-profile, exact-debit, shared-dispatch, defender-shock, targeted-recovery, sanctions-recognition, exact CAS/tactical chemical-module eligibility, class-specific native raid reservation, five-band raid outcome accounting, no-release attempt consequences, and matching asset foundation are implemented. No new ground or air release route is active yet, and the idempotent legacy stock migration has no caller while old consumers remain. Exact-state condition adapters, active route decisions/raids, remaining legacy retirement, AI, designers, and specialist audits remain open.

## Accepted sources and conflict resolution

This stage implements the chemical-delivery and payload-logistics requirements from the numbered specifications, then the delivery, equipment, decision, AI, and asset matrices, then the specialist prompts. Numbered specification 08 continues to control the occupation boundary: chemical doctrine and delivery do not unlock camps, extermination infrastructure, experiment sites, or a generic Concentration law.

The user explicitly confirmed that doctrine may reduce Condemnation impact. The shared action record therefore keeps the bounded doctrine multiplier for Condemnation only. Payload consumption, protection, disruption, military and civilian deaths, contamination, medical saturation, evidence, attribution, confirmed-use history, resistance trauma, domestic penalties, biological-use counters, and public-harm floors remain independent and may not be reduced by doctrine.

## Verified engine boundaries

- Selected-state raids expose `var:target_state`, `var:actor_country`, and `var:victim_country` in raid-instance effects. Chemical raids can therefore dispatch the shared pipeline against the exact selected state.
- Raid `essential_equipment` is collected when the raid is created. Outcome effects may return unused payload to the actor, producing explicit net-consumption bands without a second debit.
- No verified current-version hook proves that an ordinary continuous air mission with a chemical module is presently executing eligible activity. Continuous-air contamination remains disabled. No estimator, aircraft-presence proxy, front-heat proxy, or region-wide contamination fallback will be retained.
- Vanilla's current `divisions_in_state` trigger accepts a scoped state (`state = PREV`) or a state-valued variable and can filter a specific subunit. Ground operations can therefore prove that the required projector, ammunition-train, or armored-delivery formation is physically present in a friendly state adjacent to the selected target. Army Headquarters abilities still do not expose an exact command-assignment relationship, so the engine cannot prove that the particular prepared headquarters commands that particular border. The Headquarters remains the theater authorization layer and the adjacent formation remains the delivery layer; no stronger association may be claimed.
- Current selected-state decision and raid scopes expose no verified live target-weather or province-terrain trigger. `is_fighting_in_weather`, `is_fighting_in_terrain`, and `temperature` are documented for combatant scope, while state structure can prove only state category, buildings, supply nodes, ports, airfields, victory points, population, and control. No forecast estimator, structure-as-terrain substitution, or neutral condition fallback may be activated without explicit approval.
- Combat tactics expose no verified activation effect capable of consuming payload before dispatch. The legacy Chemical Barrage tactic remains weight zero and fail-closed.
- Strategic-bomber eligibility will not be added unless an exact local current-version module/mission precedent is verified. Chemical air modules remain limited to the verified CAS/tactical surface.

## Compatibility and migration policy

- Keep legacy cylinder, Livens projector, chemical tank, chemical bomb, and raid identifiers available where save compatibility requires them, but remove passive release and free broad combat buffs.
- Convert each legacy chlorine, phosgene, mustard, lewisite, tabun, sarin, and soman cylinder reserve into its exact strategic-agent lot. Convert legacy malodor and behavioral bombs into their exact strategic-agent lots. Use centralized conversion ratios without collapsing exact agent identity.
- Record migration with an idempotent country flag and never fabricate doctrine milestones, headquarters preparation, route formation presence, payload-use history, evidence, casualties, or contamination.
- Preserve legacy state contamination modifiers while the shared dispatcher owns all new consequence arithmetic, so Air Cleanliness and existing presentation surfaces continue to recognize contaminated states without duplicate deaths.

## Implementation order

### 1. Central payload and route model

- Add nine distinct producible strategic-agent models under one formation-compatible archetype, one filled-shell model, and four class-specific prepared-air-payload archetypes/models, with stable categories, script-enum registration, production costs, reliability, storage risk, and model progression where mapped. Exact operations must continue to select and debit one exact strategic agent even though formation reinforcement uses the common archetype.
- Centralize strategic-payload-to-shell and strategic-payload-to-air conversion losses, route payload costs, raid reserve quantities, outcome salvage bands, cooldowns, profile-change delay/wastage, AI weights, and consequence limits in Stage 6 script constants.
- Add country-selected shell-filling and air-payload profiles. A profile selects one agent/class at a time; changing it incurs a real delay and wastage before new operations may use the profile.
- Update Projector Battery, Chemical Ammunition Train, and Armored Delivery Detachment equipment requirements where the accepted matrix requires essential delivery hardware. Operational payload remains a national debit/reservation so a battalion cannot create free exposure.

### 2. One shared consequence dispatcher

- Extend the shared exposure system with one dispatch helper that accepts only a prepared action record with positive payload-consumption proof and an exact target state.
- Calculate protection, conditions, route, agent/class, and dose before dispatch. Then, exactly once, record disruption, military casualties, civilian deaths, contamination, medical saturation, evidence, attribution, friendly risk, confirmed use, treaty consequences, Condemnation, and sanctions integration.
- Apply civilian deaths through the shared state-death ledger and population-loss helper. Apply military damage only to eligible hostile units in the selected state; the existing casualty tracker records resulting military deaths.
- Apply the legacy contamination dynamic modifier under a shared-dispatch guard so presentation and Air Cleanliness compatibility remain intact without a second death calculation.
- Keep doctrine mitigation solely inside the Condemnation branch. Strategic and mass-casualty floors apply after the doctrine multiplier.

### 3. Defender first-use shock and adaptation

- Replace the legacy attacker-wide First Use buff with a defender-side First Chemical Shock modifier that increases vulnerability only for the first unadapted exposure.
- Record chemical awareness and adaptation on the victim after the first exposure. Subsequent use receives no first-use shock and raises defensive protection, decontamination, detection, and research priorities instead.
- Never remove evidence, attribution, deaths, contamination, medical load, or confirmed-use history during adaptation.

### 4. Exact-state ground operations

- Add an exact-state CBRN Operations decision category and timed preparation missions for cylinder release, projector barrage, artillery fire plan, and armored local delivery.
- Require an active prepared Chemical Offensive Army Headquarters, policy, readiness, agent/profile selection, payload reserve, route-specific equipment/formation proof, war, and an eligible adjacent enemy-controlled target state.
- Recheck every gate on completion. Abort or cancel cleanly if the target, headquarters preparation, formation, equipment, policy, readiness, or payload condition is lost.
- Debit payload before the shared exposure helper is called. A failed debit makes the operation inert and records no exposure.
- Preserve route identity: cylinder weather sensitivity and blowback, projector range/terrain limits, artillery persistence and shell logistics, and armored protected local delivery.

### 5. Exact-state chemical air raids

- Implement Chemical Air Interdiction and mapped strategic chemical raid types only on verified aircraft/module surfaces.
- Reserve Chemical Air Payload Lots as essential raid equipment at creation. Resolve aborted, failed, partial, success, and catastrophic outcomes with centralized payload salvage and dose bands:
  - aborted: 10–25 percent net payload use, no target exposure, at most trace friendly risk;
  - failed: 40–80 percent net payload use, no target exposure, possible crash evidence;
  - partial: 70–100 percent net payload use and 35–65 percent target dose;
  - success: 100 percent net payload use and full dose;
  - catastrophic/critical: 100 percent payload use, 110–140 percent dose, extreme evidence and consequences.
- Every exposing result dispatches against `var:target_state`. No result may contaminate an arbitrary state or whole air region.
- Idle chemical-capable aircraft and ordinary continuous missions never call the exposure system.

Reservation/outcome foundation completed before activation: native `essential_equipment` now has one exact archetype per agent class; the shared helper maps four engine outcomes to five accepted results, refunds unused stock, records net consumption, and separates consumed payload from delivered-dose efficiency. Active raid IDs remain unwired until the approved weather/terrain condition policy is available.

Unsupported continuous-air estimator retired: army combat no longer creates `chem_air_ground_ops_heat`; the deployed-aircraft/region estimator and its tuning tables are removed. The stable `chemical_air_bomb.1` event is retained only as a one-shot cleanup endpoint for a previously queued tick and cannot calculate exposure or reschedule itself.

Aircraft eligibility foundation completed before activation: all seven standard agents have exact CAS/tactical payload-rack modules, including the previously unreachable Tabun rack. The Malodor and experimental Behavioral-Agent projects unlock their own exact modules. Ordinary mission attack is capped at a modest value and never substitutes for raid execution; strategic bombers remain unsupported.

No-release consequence foundation completed before activation: Aborted and Failed outcomes keep zero release proof, retain exact native payload loss, and call a one-shot path that can add exact-state evidence, cumulative attribution, separate attempt history, and doctrine-mitigated Condemnation. The path cannot call exposure or write casualties, contamination, medical saturation, mask loss, treaty use, confirmed-use history, or a chemical-use achievement. A separate Condemnation proof prevents no-release attempts from masquerading as actual unconventional-weapon use.

### 6. Legacy route retirement

- Remove passive daily cylinder dispersal, Livens/projector contamination, chemical-tank contamination, attacker First Use effects, and ground-operations heat registration from on-actions.
- Make legacy cylinder commander abilities inert compatibility wrappers or redirect them only into the prepared headquarters path. They may not grant free general-wide attack buffs or emit exposure directly.
- Make the old chemical-air estimator event and helper cleanup-only compatibility surfaces with no self-scheduling, region scan, aircraft-presence inference, or contamination effect.
- Keep the automatic Chemical Barrage tactic at zero weight until an exact activation/debit adapter exists.

### 7. Route-aware AI and differentiated profiles

- Score target states using route legality, hostile troop density, victory points, supply significance, weather, terrain, civilian exposure, protection estimates, expected evidence, current Condemnation, sanctions risk, retaliation posture, and country profile.
- Defensive/democratic profiles refuse first use unless an explicit retaliation or existential route authorizes it. Aggressive, ideological, desperate, and historically prepared profiles receive differentiated thresholds without bypassing player-equivalent gates.
- AI must reserve payload, select profiles, prepare headquarters, field route equipment, respect cooldowns, and abort unsafe or invalid operations. It may not receive hidden stock, preparation, or exposure.

### 8. Designers, assets, localisation, and documentation

- Implement mapped chemical payload and delivery designers with route-specific, bounded modifiers; do not create generic global attack packages.
- Register all stable equipment, decision, mission, raid, route, designer, idea, and notification sprite IDs before art production.
- Produce independent final equipment models, route icons, decision/category icons, raid assets, designer icons, and first-use/adaptation icons through the Chaos Redux asset workflow. No placeholders, resized cross-type substitutes, or reused visible concepts are accepted.
- Write final English localisation for equipment, profiles, decisions, missions, raids, outcomes, consequence warnings, tooltips, AI-facing requirements, and migration. Keep all tuning-sensitive values synchronized with constants.
- Update the chemical-warfare system documentation, dynamic-helper references, asset manifests, migration ledger, and implementation surface map.

### 9. Validation and audits

- Exercise every delivery route under low/normal/high protection; dry/wet/cold/hot/windy conditions; weak/normal/strong decontamination; first and repeat use; low and high Condemnation; payload shortage; lost headquarters preparation; route-formation loss; target ownership change; and abort/cancel paths.
- Verify exact selected-state contamination for every exposing air-raid outcome and zero target exposure for aborted/failed outcomes.
- Verify net raid payload use stays inside the accepted bands after salvage, with no double debit.
- Verify no idle aircraft, passive support unit, legacy commander ability, combat on-action, or compatibility event can create contamination.
- Run the decision/mission audit, localisation audit, asset audit, route-balance scenarios, improvement-loop pass, and Stage 6 completion audit. Resolve every finding before committing the tranche.
- Commit only Stage 6-owned files. Preserve unrelated Air Cleanliness, map-mode, package-spec, temporary-asset, and legacy dirty-file work.

## Stage acceptance criteria

- Every active chemical delivery route debits or reserves real payload before one shared exposure calculation and one shared consequence dispatch.
- Chemical air raids contaminate only the exact selected state on exposing outcomes.
- Continuous ordinary-air contamination and all activity estimators remain absent.
- Cylinder, projector, artillery, armored, and air routes preserve distinct equipment, condition, protection, payload, and consequence behavior.
- First use harms the unadapted defender; it is not an attacker-wide permanent buff.
- Doctrine can reduce only Condemnation and cannot suppress any other consequence field.
- Legacy passive/free delivery paths cannot emit exposure.
- AI follows the same route, stock, headquarters, policy, readiness, target, cooldown, and consequence gates as the player.
- All visible content has final localisation and independent final assets, with migration and engine limits documented.

Stage 6 cannot close until every criterion and specialist finding above is resolved. Biological warfare, nerve-agent suppression, full package achievements/scripted GUI, and package-wide completion remain mandatory later work even after this chemical-delivery tranche passes.
