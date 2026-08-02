# Names for the Missing event addendum

## Scope

Names for the Missing is the next reviewed global survival candidate in the Fallout scheduler. It is a country-level social memory chain for the first winter year. It is not a super-event and it does not create a state target. The candidate is dormant until the activation audit opens the ordinary human and hidden AI lanes.

## Eligibility and ownership

The candidate producer admits one row when the country registry and survival rows are current, the Deaths system has recorded at least 25,000 civilian deaths, Recognition is below 65, and at least one branch can pay its resource cost. A durable memory flag prevents a second opening after cleanup. The scheduler owns transaction key 710013, route 7113, and event ids 269 through 281. The opening, result, callback, and cleanup all authenticate the current country row.

The candidate severity is `clamp(recorded civilian deaths * 0.001, 0, 100)`. Names uses a survival-resource pressure source with mechanic pressure fixed at zero. The human opening reserves three visible budget units for its opening, result, and callback envelope. Human delayed rows cost one unit each. Hidden AI delayed rows cost zero while the AI opening retains the same envelope reservation.

## Narrative contract

The opening presents a cold census room where family papers, shelter rolls, and a military archive disagree. The player chooses among publishing the names, maintaining military secrecy, permitting community memorials, and delegating to local clerks. Each branch has concrete costs and distinct effects on Food, Scrap, Power, Recognition, Cohesion, Stability, War Support, and a Fallout-owned intelligence-exposure ledger.

The result is delayed 21 days. Deterministic grading freezes deaths, Recognition, Cohesion, and exposure before scheduling. Viability combines recognition, cohesion, and a death-pressure component. Branch-specific thresholds produce success, partial, or failure. Failure routes a small casualty request through the Deaths API for every owned state. It never writes population directly.

The callback is delayed 180 days. It applies a second ledger pass, records a durable memory flag, adds a maintenance or backlog modifier, and sends any further losses through the same Deaths API. The idempotent cleanup releases both delayed receipts, clears temporary registry values, retains durable memory and exposure, and prevents duplicate resolution.

## Event Log and assets

History id 9118 uses payloads 11 through 53. The detail text is selected by `GetFalloutEvent269EventLogDetail`, with central Event Log mappings for the name and detail window. The dedicated report art is `GFX_report_event_fallout_names_missing` and lives at `gfx/event_pictures/fallout/report_event_fallout_names_missing.dds`. Source art, processing evidence, hashes, and the handoff are under `docs/assets/air_cleanliness_fallout/fallout_names_missing/`.

## AI and runtime boundary

The hidden AI lane chooses deterministically. High Cohesion prefers a public register, authoritarian governments with archive resources prefer secrecy, and stable countries with memorial resources prefer community rooms. The fallback order is clerks, public register, secrecy, then memorial rooms. Human and AI lanes call the same scheduler effects and result effects.

The chain remains dormant in this tranche. No scheduler activation flag, scenario dispatch, blackout authority, or live campaign result is claimed. A live review must still prove ordinary receipt production, delayed queue delivery, host authority, cleanup after save recovery, and multiplayer input handling before the row becomes countable.

## Source-spec disposition

The implementation contract is promoted to `docs/specs/air_cleanliness_fallout_specs/specs/13_reviewed_global_survival_pilots.md`. This addendum remains the detailed plan and evidence companion. It is not a second gameplay authority. Memorial, archive, and family-reunion consumers named in the global matrix are queued for later reviewed tranches and are not represented as completed by candidate 269.
