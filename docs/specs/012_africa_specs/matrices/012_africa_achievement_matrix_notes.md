# Event 12 Africa achievement matrix notes

## Purpose

`012_africa_achievement_matrix.csv` defines 44 difficult achievement concepts across protection, League government, constitutional routes, restoration settlements, diaspora return, development, warfare, high-chaos systems, and world order.

Keys and title directions are working material. Final titles and descriptions belong to implementation localisation. The matrix gives exact campaign-state requirements, disqualifiers, visibility, difficulty, tracking needs, icon direction, and the reason each achievement deserves to exist.

## Coverage

| Family | Count | Campaign skill tested |
| --- | ---: | --- |
| Protection | 5 | credible guarantees, rescue, aid, and intervention |
| League | 6 | voluntary membership, congresses, clauses, confidence, and peaceful crisis handling |
| Constitutional | 7 | all seven main political end states |
| Restoration | 6 | difficult polity combinations, overlap settlements, and member resistance |
| Diaspora | 4 | consent, safety, citizenship, skills, and non-capture investment |
| Economy | 4 | corridors, processing, food security, and controlled development |
| Military | 4 | reserve response, great-power war, strange units, and ethical high-chaos force use |
| High chaos | 4 | ecological restraint, weather, disease containment, and nonhuman constitutional inclusion |
| World order | 4 | sponsorship, two-continent union, continental war, and The World |

## Tracking standard

Use permanent tracking only when the final state cannot prove the achievement. Important lifetime facts include:

- whether a guarantee was broken
- whether a counted partner was annexed coercively
- whether a member left peacefully or under force
- whether an accession clause was breached
- whether diaspora relocation was voluntary
- whether transport losses were preventable
- whether a high-chaos action targeted civilians or neutral African states
- whether a restored polity was erased before settlement
- whether another continent unifier was sponsored, puppeted, betrayed, or preserved
- whether a union was negotiated or produced only through conquest

Tracking should use event-owned flags, counters, arrays, or achievement helper effects. It should not depend on reading obsolete missions after cleanup.

## Eligibility and origin

Achievements that begin with any Event 12 host should preserve the original selected host as a persistent origin. Achievements for restored members must verify that the player began as, released into, or validly switched to the named Event 12 package. Ordinary tag switching should not allow a player to collect incompatible route achievements.

Normal-play achievements should reject forced triggerable-scenario launches. Scenario-specific challenge achievements can be added later, but none are assumed in this source spec.

## Difficulty bands

- **Hard** requires focused play inside one system.
- **Very hard** requires several linked systems and a sustained result.
- **Extreme** requires continent-scale management, route discipline, or long survival windows.
- **Mythic** requires a rare restoration, high-chaos, Scramble, or world-order campaign.
- **Terminal** requires the final The World identity and campaign-ending state.

## Asset handoff

Every achievement requires:

- one completed 64x64 source concept designed for the exact condition
- a processed completed DDS
- a grey variant
- a not-eligible variant using the project overlay workflow
- one manifest entry with the exact achievement key
- root placement under `gfx/achievements/`
- registry, localisation, interface, docs, and package alignment

Historical motifs must be sourced or derived from documented symbols. Fictional high-chaos and world-order motifs may be generated. A restoration achievement icon should not use a generic continent silhouette when a specific researched court, city, trade, river, or architecture motif can identify the challenge.

## Anti-triviality check

No achievement in the matrix unlocks merely because Event 12 fires, a country joins the League, a first focus completes, or Africa is formed by the easiest available method. Every entry requires multiple conditions, a difficult timing or survival condition, an explicit restriction, or a rare route.

## Audit handoff

The completion auditor should receive a disposition for every row: implemented, merged into a named achievement, queued with reason, rejected with reason, or superseded. The final implementation report should include tracking hooks, registry identifiers, icons, disqualifier checks, and at least one validation scenario for every achievement family.
