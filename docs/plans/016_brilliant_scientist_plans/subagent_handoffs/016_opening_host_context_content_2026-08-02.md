# Event 016 opening host-context content handoff

Date: 2026-08-02

## Scope

This presentation tranche adds the accepted country-specific opening variation without creating a new mechanic or changing the minor fire-once transaction. The evolved opening descriptions remain higher priority and continue to win whenever a prefire evolution is active.

## Changed files

- `events/016_brilliant_scientist.txt`
  - Added six ordinary `.2` descriptions and six ordinary `.3` recipient descriptions.
  - Each branch is gated to prefire stage zero and uses the existing host-fact thresholds from `brilliant_scientist_host_flavor_gate`.
- `localisation/english/016_brilliant_scientist_l_english.yml`
  - Added BOM-preserving English localisation for refugee, colonial, university, industrial, militarized, and threatened openings for both host and recipient events.
- `docs/events/016_brilliant_scientist/overview.md`
  - Records the new context-sensitive opening presentation and its precedence relative to evolved openings.

## Behavior

The ordinary opening now reflects the selected country's institutional situation. Exile hosts use the refugee text first, then colonial, university, industrial, militarized, threatened, and generic facts follow the same priority used by the existing host-archetype classifier. A recipient receives the same contextual treatment based on its own country facts. The branches only change prose and do not alter eligibility, AI weights, actor identity, research speed, Directorate meters, referral limits, project history, or event-log state.

## Validation

- Confirmed all twelve new localisation keys have exact event references.
- Confirmed the localisation file retains UTF-8 BOM encoding.
- Confirmed evolved `.2` and `.3` descriptions remain above the ordinary branches, so active prefire evolution context is preserved.
- Ran focused Event 016 event inspection after the preceding runtime patch. It returned `EVENT_INSPECTED_PARTIAL`, no blocking diagnostics, and the documented large-workspace validation limitation.

## Remaining risks

The ordinary fallback opening remains generic when no context gate matches. No new report art, model, entity, unit, or project reward was created or wired.
