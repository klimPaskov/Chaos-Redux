# Event 006 round-number balance preflight

Date: 2026-07-15

Scope: shared Event 006 country values, lifecycle ideas, focus rewards, force
profiles, scenario/evolution tuning, formable risk, the NWE regional packages,
and the six currently wired package force rows.

Status: implementation preflight, not an independent package attestation and
not an Event 006 completion claim.

## Outcome

The current Event 006 working tree no longer uses the earlier reward-dust
ladders built around `3`, `7`, `8`, `12`, or `18`, nor authored idea modifiers
such as `3%`, `7%`, or `8%`. Player-facing progression uses round increments
and thresholds that can be read and planned around: predominantly 5, 10, 15,
20, 25, 30, 40, 45, 50, 55, 60, 65, 70, 75, and 100.

The pass also corrected an AI-sign defect in the Wallonia/Frisia package.
Targetless `avoid_starting_wars` additive values restrain war through negative
weights; the founding and settled values are therefore `-140` and `-45`, not
positive `140` and `45`.

All automatic and scenario readiness gates remain fail-closed. These tuning
changes do not certify a package by themselves.

## Surfaces normalized

- `common/script_constants/006_independence_wave_constants.txt`
  - shared opening legitimacy, recognition, capacity, security, and
    instability values.
- `common/script_constants/006_independence_wave_mechanics_constants.txt`
  - common country-value bands and host, patron, network, territory, and
    archetype deltas.
- `common/ideas/006_independence_wave_ideas.txt`
  - lifecycle, recognition, command, border, patron, instability, league, and
    regional-identity modifiers.
- `common/script_constants/006_independence_wave_focus_constants.txt`
  - AI weights, equipment, experience, and country-value focus rewards.
- `common/script_constants/006_independence_wave_force_constants.txt`
  - force-component ceilings, equipment factors, experience, stockpiles,
    naval/air ratios, and military-influence bands.
- `common/script_constants/006_independence_wave_formable_constants.txt`
  - formable risk and consent/settlement adjustments.
- `common/script_constants/006_independence_wave_evolution_constants.txt`
  - package weights, force bonuses, country deltas, and league changes across
    the five evolutions.
- `common/script_constants/006_independence_wave_scenario_constants.txt`
  - all four intensity ladders and type-specific country, network, and patron
    changes. Candidate count remains invariant across intensity.
- `common/script_constants/006_independence_wave_nwe_advisor_constants.txt`
  - the twelve advisor dossier modifiers.
- `common/script_constants/006_independence_wave_scotland_wales_constants.txt`
  and `common/ideas/006_independence_wave_scotland_wales_ideas.txt`
  - route popularities and all package idea modifiers.
- `common/script_constants/006_independence_wave_wallonia_frisia_constants.txt`
  and `common/ideas/006_independence_wave_wallonia_frisia_ideas.txt`
  - route popularities, force-AI weights, idea modifiers, and the corrected
    negative war-restraint weights.
- `common/script_constants/006_independence_wave_rhineland_bavaria_constants.txt`
  and `common/ideas/006_independence_wave_rhineland_bavaria_ideas.txt`
  - package pressure ladders, route popularities, AI weights, and idea
    modifiers.
- `common/script_constants/006_independence_wave_force_package_constants.txt`
  - only the six currently wired package rows were normalized: IW-001 70,
    IW-002 60, IW-006 60, IW-007 45, IW-008 70, and IW-009 75 military
    tradition.
- the three NWE package documents and RHI/BAY localisation were aligned with
  the exact revised values.

## Focused checks

- Every authored decimal modifier in the touched Event 006 idea and advisor
  families is a multiple of `0.05`.
- Every touched route-popularity group sums to exactly 100.
- A scan of Event 006 `common/` and `events/` decimal values found no remaining
  hundredths outside five-point increments.
- The approved BAY and RHI historical portraits remain byte-identical to their
  accepted hashes; this balance pass did not touch visual assets.

## Required follow-up

1. Re-run the independent country-package audit after the complete current
   package/formable tranche is present. Round tuning is evidence, not static
   content attestation.
2. Review and normalize each remaining force-registry military-tradition row
   when that package becomes release-ready. The dormant 206-row table still
   contains older irregular entries; changing all of them without package
   review would be unverified bulk balancing.
3. Validate costs and AI behavior in the package, decision/mission, scenario,
   and completion audits. This preflight checks authored tuning shape and the
   identified AI-sign defect; it does not claim live-game combat balance.

## Simplifications, omissions, and blockers

No cost was removed, no reward was replaced with political-power dust, and no
free-unit loop was introduced. The unready registry rows were deliberately not
bulk-normalized. Their tuning remains a documented follow-up tied to package
readiness rather than a hidden completion claim.
