# Event 001 Release QA decisions, 2026-10-05

The parent task explicitly authorized weak-design changes for this release QA pass, named the Custerdome first choice as defective, required one report of each repeated type per country crisis, and accepted a bounded per-incident-type cap that preserves the first choice/outcome. Broad Event 001 specification acceptance remains unresolved.

## Applied decisions

- Guard forced root setup and fan-out by an eligible regular host. Provide a readable invalid-host response and keep the valid communist-government acknowledgement.
- Rewrite the unrelated or misleading root, incident, report, tooltip, and option prose; align result descriptions with the actual consequences.
- Cap repeated per-country reports for state spread/escalation, local-intervention results, sabotage/strike types, war warnings, emergency outcomes, and each rare incident variant. Candidate pools now contain only unseen report types. The first player choice for each type remains available. Clear all report receipt flags with the country crisis cleanup.
- Apply intervention success/failure costs on every outcome while showing each matching `.6`/`.7` report once. Reduce the duplicate failure support award from 3% to the single configured 1.5% per failure.
- Disallow a second rebel war for one host. Retain each dynamic rebel's parent country scope so third-party annexation can clear the correct host flag. Dispatch `.10` only if rebel creation succeeded; otherwise dispatch `.9` when a no-uprising outcome actually resolved.
- Cancel a local intervention timer when its selected state leaves the actor's control; cancel emergency resolution if a rebel war begins.
- Remove fixed AI PP hints from local and emergency decisions because their dynamic costs cannot be represented accurately. Keep the national hint at 65, its maximum under the ten-state cost cap. No AI resource-reserve scenario validated the remaining hint.
- Reduce emergency command-power cost from a 75 base plus 5 per state and 10 per Level 3 state to a 25 base plus 2 per state and 3 per Level 3 state, capped at 60. This brings the base within the decision's 60-point limit and the inclusive 4-resource payment set. Leave PP, manpower, and equipment scaling intact.
- Display PP, manpower, and equipment as the three inline payments, and show dynamic command power and the 8% stability, 6% war-support, and 150-day disruption consequences in the cost tooltip. Apply those three backlash consequences only when the operation resolves, so stale or canceled callbacks do not impose them.
- Centralize durations that duplicated existing or newly named tuning constants and expose the emergency gate explanation.

The repeated incident eligibility changes alter random candidate pools, and AI cost-hint corrections alter AI resource-reserve behavior. Probability tools and a saved scenario comparison were unavailable, so numeric behavior is unresolved. No weights, `ai_will_do`, `ai_chance`, or raw outcome chance constants were tuned.

## Unresolved specification items

The Event 001 spec describes 40/80/100% state-level conversion probabilities while source uses a capped priority budget; it describes uncapped per-state drift while source caps state contribution at 0.90. The supplied spec has no explicit parent/user acceptance evidence resolving either design conflict. The portrait's styled final, GUI visual evidence, weighted comparisons, achievement design coverage and Event091 runtime ordering remain outside completed proof.
The reconciliation below governs current installation status.
# Parent asset review

Acceptance basis: the user's release QA and G6 authority permits correcting inappropriate report art and recording the design reason.
`chaosx.nr1.34` uses the installed vanilla strike-meeting photograph instead of the Helsinki bombing scene.
The dedicated `GFX_report_event_communist_strike_wave` sprite resolves to `gfx/event_pictures/001_communism_spread/communist_strike_wave.dds`, copied without visual changes from vanilla `gfx/event_pictures/report_event_generic_strike.dds`.
The 210x176 RGBA DDS hash is `526aa7ad0da0a94fb6eb7b33ccdfe7e185aaf88e8f41c844a5941194c8f54191`.
Parent review confirmed the visible speaker and assembled workers suit a coordinated strike and show no bombing damage.
The immediate source is installed game art and no public-domain claim is made for that photograph.
That asset audit is historical; fifteen approved generated report scenes are installed as documented in subagent_handoffs/report_art_20261005.md.
The institutional portrait uses a separately reviewed source placeholder and remains pending the user's styled final.

## Current parent reconciliation, 2026-10-06

Acceptance basis is the user's 2026-10-05 release-QA/G6 direction and parent review.
Fifteen fictional report DDS files are approved and installed; the vanilla strike image is separately approved reuse.
The collective portrait is an approved grounded source_placeholder with provenance in subagent_handoffs/portrait_source_20261005.md; the user's styled final remains pending.
Source implements inclusive CP 10 affordability, initialized Revolution weight output, event-owned .35 invalid-host preflight, one-captured-seed REV bootstrap, existing-REV bypass, guarded REV actor and removal of the unrelated monthly Portugal-Galicia dispatch.
Capped-conversion and 0.90-drift spec acceptance conflicts remain unresolved.
See `release_qa_completion_20261006.md` for current dispositions, source evidence and review gates.


# Graphics decisions accepted on 2026-10-06

The user-authorized graphics review requires distinct, period-appropriate report photographs and removal of the legible slogan poster.
Parent review accepted generated anonymous documentary scenes for State Control and Insurgency Start because neither depicts a required historical person or photographed incident.
The municipal checkpoint and railway-bridge compositions communicate their report subjects and remain distinct from the existing militia assembly and barricade cards.
The older reviewed 15-scene package is reused after current DDS hashes and subjects were checked, rather than replacing valid artwork.
Runtime filenames and sprite identifiers remain stable; gameplay design is unchanged.
Evidence and the thirteen-row disposition table are in `docs/plans/gfx_fix_2026-10/001_report.md`.
