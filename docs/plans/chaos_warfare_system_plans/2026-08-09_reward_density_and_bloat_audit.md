# Chaos Warfare and CBRN reward-density and bloat audit

Date: 2026-08-09

Status: supported playable core is source-ready. No additional gameplay subsystem is required. Remaining omissions are exact-engine surfaces or user-owned live consumer validation and are listed explicitly below.

## Audit conclusion

The implemented package covers the accepted national program, protection, command, division-support, chemical-delivery, biological-lifecycle, camp, consequence, diplomacy, AI, technology, equipment, designer, advisor, achievement, asset, and documentation loops. The final pass found no orphan top-level CBRN helper, no second active consequence ledger, no unsupported periodic world pulse, and no active route bypassing the shared chemical action record.

The principal player-reward weakness was not missing content. Several active rewards had been tuned strongly in script while their localisation or older audit text still advertised obsolete weak values. Those mismatches are reconciled. The package now communicates the same high-impact progression that the mechanics apply.

Adding another agent family, support-company family, headquarters company, general CBRN meter, all-purpose scripted GUI, delivery estimator, or ordinary-use event chain would duplicate existing decisions without adding meaningful player choice. Those additions are rejected as bloat.

The later 2026-08-21 closure pass removes two further card-volume risks. The twelve generic biological supply-chain state-target decisions can no longer list new targets because their shared actor gate is migration-only, while the four native espionage operations remain the covert route. External occupation aid now requires an exact chemical alert, contamination, outbreak, or trauma record, so it cannot create cards for every ordinary occupied state.

## Reward-density result

### Doctrine and mastery

- Chaos Warfare adoption gives a visible conventional payoff: 15 percent planning speed and 35 percent soft attack, breakthrough, and defense for mapped chemical support companies.
- Contaminant Fire Support reaches 1.65 chemical operational effect and 1.80 contamination output while adding 20–40 percent artillery and chemical-formation bonuses across its progression.
- Integrated CBRN Command reaches 1.70 chemical operational effect, 1.60 chemical-air dose, 1.50 chemical-air duration, strong army-level reconnaissance, planning, coordination, reinforcement, organization, supply, and attrition rewards, and a 0.35 Condemnation multiplier. Evidence, attribution, deaths, contamination, medical saturation, responsibility, and history remain unchanged.
- Toxic Armored Warfare provides large suppression, organization, supply, reliability, planning, coordination, attack, defense, and breakthrough rewards. Gas-Chamber Saturation Drills multiply nerve-agent camp killing efficiency to 225 percent of the selected agent's baseline, reduce payload consumption to 45 percent of standard, reduce generated evidence to 55 percent of standard, and add agent-scaled resistance suppression.
- Terminal Hazard further multiplies an independently active camp network's resolved death rate by 1.75 under Unrestricted Chaos Warfare. It reduces Condemnation impact only and does not create or conceal infrastructure.
- Chemical Operations Commanders reduce paid CBRN Headquarters preparation to 70 percent of baseline. The doctrine-independent Chemical Operations Academy gives eligible new and newly promoted army leaders a 50 percent chance to gain the trait.

### Headquarters, units, equipment, and technology

- Headquarters companies now provide substantial standing value: Operations Sections add 30 percent planning speed, Intelligence and Weather Cells add 50 percent reconnaissance, Medical Countermeasure Directorates reduce wounds and sickness by 40 percent, and Biological Security Sections add 35 percent reconnaissance and reduce sickness by 40 percent.
- Paid headquarters postures use large, readable effects with real supply and equipment burdens. Prepared Chemical Fire Plans add 20 percent planning speed and maximum planning; Mass Antidote Response reduces wounds and sickness by 40 percent; Sealed Infection Corridors reduce sickness by 50 percent; Combined CBRN Overmatch adds 30 percent planning speed and 20 percent maximum planning while reducing wounds and sickness by 30 percent.
- Regimental support is materially combat-relevant instead of cosmetic. The role family supplies organization in the 18–26 range, reconnaissance up to 4 before technology, suppression up to 12, medical trickleback of 25 percent, experience-loss reduction of 30 percent, strong terrain modifiers, and substantial defense, breakthrough, and attack according to role.
- The Chaos Assault Battalion has 15 soft attack, 18 breakthrough, 12 defense, 6 suppression, and strong terrain bonuses before later technology and doctrine rewards. Its improved package adds 10 breakthrough and 15 organization.
- Each improved or advanced projector technology adds 5 soft attack, hard attack, defense, and breakthrough to Chemical Projector Batteries. Portable Anemometers, Meteorological Stations, and Upper-Air Soundings add 2, 3, and 5 reconnaissance to Chemical Reconnaissance Detachments instead of exposing a fake release-weather estimator.
- Chemical projector, tank-shell, and aircraft-module ladders have large agent-scaled combat values. Producible masks, decontamination equipment, instruments, strategic agent lots, shell lots, air payload lots, and biological payloads retain real cost, reliability, resource, and stockpile tradeoffs.

### Designers, advisors, protection, and medicine

- The six CBRN MIO families provide 15–60 percent production, reliability, handling, detection, cleanup, treatment, containment, or operational changes rather than token bonuses. Offensive capstones deliberately trade higher potency for greater evidence, Condemnation, or accident risk.
- Historical theorists and advisors provide 15 percent research, 20–25 percent army experience, 25–35 percent special-project speed, 10 percent stability, 15 percent production-efficiency cap, or large CBRN operational multipliers according to role. Offensive specialists increase chemical or biological potency by 20–40 percent while medical specialists reduce harm by 30–35 percent.
- Dimercaprol reduces every accepted chemical exposure's deaths by 15 percent and medical saturation by 35 percent, then halves the remaining deaths from blister-agent exposure.
- Gas-mask investment remains consequential because actual models, issued stock, civilian distribution, fit, filter condition, training, shelter, warning, medicine, and decontamination feed protection. It lowers casualties without erasing persistent contamination or attacker consequences.

## Gap and nonduplication audit

### Supported active routes

- Chemical air raids, rockets, the Japan-China chemical campaign, chemical doomsday release, and the exact camp chemical method all prepare and dispatch through `cbrn_prepare_chemical_action_record` and `cbrn_dispatch_chemical_action_record` after exact target and payload proof.
- The shared dispatcher owns disruption, deaths, canonical contamination, medical saturation, evidence, attribution, confirmed-use history, treaty response, Condemnation, and victim memory.
- Chemical state changes use the canonical contamination mutator. Cleanup and diplomacy call that same mutator rather than writing a second state ledger.
- Failed or aborted chemical air raids use a no-release record and cannot contaminate the selected state. Idle chemical-capable aircraft cannot enter the exposure pipeline.
- Ordinary biological warfare preserves Tularemia < Anthrax < Plague < Smallpox potency, with only Smallpox using the severe tier. Native raid success is agent-neutral. Delivery remains split between raids, operative or espionage actions, bounded historical decisions, and doomsday release where each route has an exact consumer.
- Weaponized zombies retain a separate lifecycle.

### Starting position and progression access

- The one-time startup transaction remains wired from `common/on_actions/chaosx_on_actions.txt` and grants country-specific technologies, reserves, seven Chemical Warfare facilities, and eight Biological Warfare facilities through exact province helpers.
- Gas-mask starting reserves remain differentiated by the accepted matrix, including Britain's strongest prepared reserve.
- Chemical Operations trait acquisition depends on the officer-corps academy and commander creation or level-up, not Chaos Warfare doctrine.
- Route-aware AI retains differentiated country profiles for research, production, headquarters, regimental roles, protection, containment, sanctions, and supported operations.

### Bloat removed or rejected

- Stockpile-risk and other state-marker national ideas are absent. Functional program and response ideas remain because they carry actual costs or effects.
- Four obsolete direct chemical helper bodies and their scripted-localisation surface were removed. Stable legacy ability identifiers remain permanently unavailable compatibility entries because that engine surface cannot prove an exact target or release.
- CBRN-specific helpers are absent from the general `chaosx_dynamic_effects.txt` and `chaosx_dynamic_triggers.txt` registries. Reusable subsystem helpers remain in CBRN-specific files.
- The old attacker first-use buff is absent. First use produces defender-side command shock and later adaptation only.
- No additional all-country daily, weekly, or monthly CBRN pulse was added.
- The native decision-category presentation remains the accepted command surface. No duplicate all-purpose CBRN scripted GUI or unsupported window-only animation layer was added.
- Existing `gfx/interface/military_raids` assets remain untouched; separate new raid assets do not overwrite them.

## Documentation reconciliation performed

- Corrected Gas-Chamber Saturation Drills documentation to 225 percent killing efficiency, 45 percent payload use, and 55 percent evidence generation.
- Corrected all seven CBRN Headquarters ability tooltips to the active strong status-trait values.
- Corrected Theater Contamination cleanup documentation from the obsolete 1.25 multiplier to the active 1.75 multiplier.
- Reconciled the Stage 14 nerve-suppression scenario to the supported camp route and retained the separate legacy occupation operation as the fail-closed compatibility surface.
- Added supersession notes to staged ledgers and handoffs whose historical statuses predate the supported camp integration and final supported-core checklist.

## Meaningful validation evidence

- HOI4 technology comparison between revisions `e7171c37` and `d9a6815d` reports zero added, removed, renamed, moved, or regressed technologies after the reward and layout changes. Evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1cfced7ac9db3ec7e5bff3fe1467b476973e27937eaaf4510d3395bc0153e729/91c03d326fc2ea08b81463494e57eda13984af95525afeeee5407068921b284b/technology-compare-e7171c37-d9a6815d.json`.
- The Japan chemical campaign decision passed a bounded `hoi4.probability_inspect` with no diagnostics. Evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4143f5f30a663588c6969610ec4a8be9ca496877e07f067ce972ebbbbc205d38/a3f30b6fa44536345537ba34b0bd208f6f28c5a88ff52b2c7e2d2c286801ce36/probability-inspect-6c230ab4e129.json`.
- A manifest-to-GFX filesystem audit checked 397 registered textures across the CBRN doctrine, protection, chemical delivery, battlefield, occupation, diplomacy, designer, advisor, biological, special-project, and subunit registries and found no missing texture path.
- Source call-site review found no active supported chemical route with an independent consequence writer, no remaining reference to the four deleted direct helper files, and no CBRN helper entry in the general dynamic registries.
- The technology category used by the strengthened wind-observation branch is defined in `common/unit_tags/chaosx_categories.txt` and consumed by the Chemical Reconnaissance Detachment.

Fresh multi-family probability inspection could not be completed after the HOI4 MCP transport closed. Repeated specialist audit workers were rejected by the platform before producing reports. These tool failures are recorded as audit-evidence limitations and are not represented as passed checks.

## Simplifications, omissions, and genuine blockers

- Continuous ordinary-air contamination remains unsupported because no current-version eligible-activity callback proves an actual release. No estimator is retained.
- Four ground Chemical operation families remain fail-closed because the current Army Headquarters and operation surfaces do not expose the required exact selected-state target, weather, terrain, and release-condition receipt.
- The separate legacy selected-state occupation suppression operation remains fail-closed because exact condition and target-loss receipts are unavailable. This does not block the supported Gas-Chamber Saturation Drills camp route.
- Hardened Mobile Plant remains omitted because no exact bombing or facility-capture transaction exposes the decontamination-equipment model and amount lost. No substitute reliability bonus is used.
- Four receipt-dependent achievement proposals remain absent from active runtime: Air Is Still Breathable, No Wind Is Friendly, The Antidote Arrived, and Unbroken Supply Corridor.
- Exact live production shares, long-duration AI campaign pacing, native random outcomes, UI readability in the running game, and other live consumer behavior remain user-owned validation. Source-relative AI weights are not represented as exact runtime percentages.
- Historically unique national MIO company identities remain skipped as non-core. The active generic MIO families are mechanically distinct and country AI remains differentiated.
- Window-only readiness-seal, contamination-border, and preparation animations remain omitted because the accepted native decision-category presentation has no consumer for them.

No approximation, estimator, proxy target, neutral condition receipt, random-state fallback, cross-type asset substitute, or broad periodic pulse was introduced for any omitted surface.
