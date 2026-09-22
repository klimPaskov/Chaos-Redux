# Event 073 achievement implementation and asset prompt

Read the current achievement patterns and registry, the owning event and asset skills, and `docs/specs/073_mongols_rise_specs/presentation/03_achievements.md`. That file is the complete sixteen-entry design registry. For every entry it supplies a planning ID, title and description direction, eligible country, unlock condition, disqualifiers, difficulty, visibility, reason it is nontrivial, icon direction and tracking requirements. These fields are mandatory and must not be dropped during implementation.

Implement A01 through A16: a sustained first mounted campaign, a stronger-opponent cavalry victory, the actual Karakorum capital project, prepared personal succession, administrative recovery, an honored council campaign, four functioning regional settlements, a connected imperial economy, Chinese production supporting a later campaign, a durable European campaign, universal recognition, a smaller recovered empire, opponent containment, independent khanate survival, feasible tribute through war, and regional influence in a genuine succession.

Allocate collision-free runtime IDs through the existing central registry. Planning labels are not final localisation and numeric registry IDs have not been allocated. Do not create a parallel event-local achievement engine.

Implement every required persistent condition and anti-farming guard. A one-day template change must not prove an entire cavalry campaign. A province visit must not count as a durable European settlement. A cosmetic rename must not count as an actual Karakorum capital move. A dummy subject, fictional payment, forced test entry, auto-completed focus, or deliberately farmed release and reconquest must not unlock the corresponding achievement.

The asset role creates separate readable icons using the exact immutable three-state templates. Complete all three state outputs for every achievement, register the correct consumer and central asset path, and review at native size. Do not infer completion from one color icon.

Write final concise player-facing titles and descriptions after the condition and source checks. Verify that descriptions reflect actual tracking and do not promise unsupported mechanics. Record all new flags, variables, source events and reset rules in the implementation documentation.

Test each achievement with a legitimate positive scenario and at least one relevant negative or adversarial scenario. Include save continuity, actor changes, successor identity, normal campaign eligibility, and custom-cavalry composition where required. Keep blocked achievements visibly blocked in development records until their underlying feature is truly implemented. Return registry proof, assets, localisation, tracking documentation, and actual test evidence for all sixteen entries.
