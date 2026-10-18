# Event 114 achievement-implementation prompt

Implement the five Event 114 achievements from docs/specs/114_demilitarization_specs/114_demilitarization_achievements.md. Read that entire file and its shared tracking section before touching the registry. Also read the core, evolutions, desertion, decisions and missions, world interactions, presentation, validation and handoff, and review dispositions. The specification owns the gameplay contract. This prompt routes its complete implementation and does not replace any eligibility or reset requirement.

Follow current AGENTS.md, the full relevant achievement and event guides, the asset guide, and the actual achievement specialist definition. Use the existing root registry at common/achievements/chaos_redux_achievements.txt after verifying its current effective owner. Check proposed IDs for collisions. A negative text search does not prove an identifier is available.

All challenge labels, title directions, and description directions are design instructions. Write final native localisation during implementation. Do not copy headings into final player text without the required writing and localisation review.

## Five required challenges

### A114-01, chaosx_114_sustained_service

Reward maintaining an established military institution under prolonged restriction. At attempt entry, require active Desertion Crisis, five mature eligible formations, at least 20,000 actual fielded soldiers, and at least one third of controlled states restricted by Event 114. Require 180 consecutive peacetime days, cohesion at least 70 at each review, both a service-conditions and cadre completion during the interval, the maintained army floors, and no spontaneous dissolution. Maintain at least 80% of the starting eligible manpower. Apply the geography grace and all reset conditions from the authoritative achievement file.

This is hard and visible. Its original icon subject is A114-A01, the intact regimental standard with a repaired fastening. The title and description should communicate institutional endurance and the actual sustained requirements.

### A114-02, chaosx_114_inland_withdrawal

Reward a real withdrawal with identifiable surviving forces. Require at least three physically new Deeper DMZ states, an eligible army of at least 20,000, and legal same-controller interior destinations. Observe at least three pre-existing formations actually leaving the added footprint, with at least 10,000 combined pre-relocation soldiers. Maintain their identities for 60 consecutive peacetime days and at least 85% of their combined starting manpower, with the shared maintained army requirements.

This is hard and visible. A114-A02 shows the boot, closed barrier, and intact field pack. Do not award movement credit for an overlapping DMZ claim, a generic relocation request, or fabricated destination success. GATE-02 and GATE-05 must establish actual preservation and identity.

### A114-03, chaosx_114_capital_cantonments

Reward service under an actual capital-only deployment condition. Total must leave exactly one legal controlled state, the controlled capital. Require at least six controlled states, 30,000 eligible fielded soldiers, and five mature formations. Maintain the real capital-only state, cohesion at least 50 at every review, at least 80% of starting manpower, and the shared minimum army floors for 120 consecutive peacetime days without a spontaneous dissolution.

This is very hard and visible. A114-A03 shows the barracks gate, folded standard, and small civic dome. A border capital remains restricted and is ineligible for this particular challenge. Do not add an exemption to make the achievement available. A capital move, war, additional legal state, or other stated reset ends the attempt.

### A114-04, chaosx_114_rebuilt_service

Reward rebuilding after a substantial verified spontaneous loss. The qualifying receipt must remove at least 5,000 actual soldiers, or at least 10% of a pre-loss eligible army of at least 20,000. Freeze a target equal to the post-incident eligible army plus the ceiling of 90% of the actual lost personnel. Reach that target through legitimate fielding, then maintain it and cohesion at least 70 across 90 consecutive peacetime days and each review, without another spontaneous dissolution.

A later loss cannot lower the old target. Preserve separate immutable obligations and use the highest outstanding target. War resets the streak while retaining the historic qualifying incident. Voluntary consolidation, combat loss, another event's removal, replacement-unit scripts, and duplicate returns cannot qualify.

This is very hard and hidden until a qualifying incident. A114-A04 shows the repaired sleeve insignia on closed service kit. The writing must distinguish real loss followed by sustained rebuilding from a planned administrative disband.

### A114-05, chaosx_114_independent_conditions

Reward service while Event 114 and Event 096 independently constrain the army. Require Desertion Crisis, a legitimate 096 template lock with more than 60 days of owner-proven remaining duration, an eligible army of at least 20,000, and five already mature formations. Maintain both systems and peace for 60 consecutive days, cohesion at least 60 at each review, the maintained minimum army and 80% manpower floors, and one cadre completion using an existing locked template.

Require actual Event 114 personnel departures of at least 0.25% of the attempt's starting eligible manpower, rounded down with a minimum of one soldier. The inspected 096 implementation uses a 90-day lock. Unknown historical unit age can make a simultaneous first opening ineligible. Do not fabricate maturity or extend that lock. A legitimate owner-driven release ends the attempt without implying an implementation fault.

This is hard and hidden until both systems overlap. A114-A05 shows a service ledger with two separate clasps. Event 114 must not clear templates, grant allowances, or treat war as satisfying 096's own conditions.

## Historical tracking and award transaction

Mature means 60 continuous calendar days of verified service identity under the legitimate owner. Trust native age only after verification. Otherwise first observation is the lower bound. A rename retains a genuine identity. Splits, mergers, transfers, and reconstructions cannot copy age or one achievement identity into several units.

Use one attempt owner, actual starting observations, immutable incident and movement receipts, and explicit reset reasons. Check applicable minimum eligible manpower, formation count, and starting or recovered proportions at scheduled reviews, verified army-change notifications, and the final check. Empty-army time cannot silently advance an endurance attempt while the review clock is frozen. War and identity transitions follow the challenge-specific rules. Award once through the shared system after physical results settle.

Do not implement these challenges as final-day snapshots. Missing historical identity or actual-loss proof blocks the dependent challenge. Do not reduce its requirement to a country flag or an easier trigger to claim completion.

## Artwork and presentation

Each achievement needs its own original 64x64 subject and the exact completed, grey, and not-eligible triplet. Follow 114_demilitarization_asset_prompt.md, the canonical references under assets/gfx_references/, the supplied achievement templates, unchanged red-cross overlay, and process_achievement_icons.py. Runtime triplets belong directly in gfx/achievements/ using the exact ID, ID_grey, and ID_not_eligible identities.

The actual icon specialist owns subject production. The main implementation owner registers final GFX and connects each state to the current registry consumer. Review native-size readability and the entire triplet together. An image file is not a complete achievement.

## Acceptance and handoff

For each challenge, document a positive case and a near-miss differing by one meaningful condition. Include premature war, one review below cohesion, temporary army-floor failure, repeated callbacks, save/load, target identity loss, controlled-state changes, incomplete actual recovery, and invalid 096 expiry assumptions where relevant.

Use current source validation, event inspection, and installed owner evidence through their actual available schemas. Keep live engine proof distinct from scripted trigger inspection. No HOI4 route was available during specification planning, so none of these future cases is pre-validated.

Return the exact registry and localisation changes, tracked fields and their mutation owners, all five final triplet mappings, verification evidence, and unresolved gates. Coordinate with the main implementer and near-completion improvement review. Do not mark any challenge complete while its required history, artwork, or owner integration remains missing.
