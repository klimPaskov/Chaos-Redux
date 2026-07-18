# IW-058 regional settlement-partner decision audit

Date: 2026-07-18

Scope: `IW-058` sovereign-autonomy partner transaction only. This audit covers
the named decision, package triggers/effects, `chaosx.nr006.5810`, and their
direct IW-058 localisation. It does not claim completion of Event 006.

## Result

The transaction has a former-host path and a bounded regional-guarantor path.
Both use the same five treaty chapters and preserve the `ASY` carrier's
sovereignty. One high-severity proof-order gap was corrected: a counterpart
could become invalid after the 180-day compact completed but before the final
ratification focus fired `chaosx.nr006.5810`. The proof gate now rechecks that
the locked former host remains at peace, or that the locked regional guarantor
still exists, remains sovereign, remains at peace with ASY, and still
guarantees ASY.

## Changed files

- `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt`
  - `can_write_independence_wave_iw058_mesopotamian_settlement_complete`
  - Former-host proof branch now also requires
    `iw058_former_host_security_settlement_complete` and a live non-war
    former-host relation.
  - Regional proof branch now calls
    `has_independence_wave_iw058_regional_settlement_partner` instead of
    trusting the persistent confirmation flag alone.
- `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.md`
  - Updated the regional-target lifecycle contract to state the final-proof
    revalidation.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw058_regional_settlement_partner_audit_2026_07_18.md`
  - This handoff.

No decision, event, effect implementation, localisation, GUI, GFX, asset,
portrait, advisor, or dossier file was changed.

## Issue list

1. High, fixed: final-proof target validity was weaker than mission-expiry
   validity. The sovereignty compact revalidated the counterpart at expiry,
   but the final proof condition retained only static former-host/regional
   flags. A later bilateral war, regional guarantor subjection, guarantor
   withdrawal, or target death could therefore leave the final focus able to
   write the settlement proof. The strengthened branch conditions fail closed
   on each of those cases.
2. No remaining critical or high issue found within this transaction scope.

## Decision-category lifecycle

`independence_wave_iw058_ratify_sovereign_autonomy_compact` is visible only
after the autonomy-charter focus and before its one-time receipt. Availability
requires the exact IW-058 carrier, ASY sovereignty, a constitutional route,
no Levies Guardianship, Mosul owned and controlled, all four guarantee flags,
the pre-existing church-civil jurisdiction record, a valid treaty partner, and
the paid-administration preflight.

At start, the decision commits command power and manpower once, marks the
transaction active, and deterministically prefers the saved former host when
both paths are available. Otherwise it locks the saved regional guarantor.
The pending counterpart flag prevents a mid-mission switch. At expiry it either
commits a single settlement mode or consumes the commitment and records the
applicable failure pressure. Cancel and package cleanup clear active and
pending transaction state; package cleanup also clears all records, modes,
receipts, and the package-owned global regional-partner target.

## Mission quality notes

| Mission | Owner/category | Region/partner | Requirement and duration | Success/failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `independence_wave_iw058_ratify_sovereign_autonomy_compact` | ASY, Council of Communities | Mosul 676 plus saved former host or named regional guarantor | Constitutional sovereign ASY, four guarantees, settled jurisdiction, valid partner, 180 days, paid administration commitment | Writes the mutually exclusive sovereign-autonomy mode only after all five records and live partner checks. Timeout or cancel consumes the commitment and applies treaty/host pressure. | Low. FORM-18 is a separately gated federal congress with a different consent ledger and mode. |

The action is a real treaty negotiation, not a passive inventory check. Its
counterpart is locked rather than reselected, and no unit is created,
refunded, or recycled by its success, timeout, or cancellation path.

## Requirement, AI, and route-lock notes

- The regional-partner trigger is bounded to same-region Event 006 actors or a
  reviewed explicit tag list. It requires existence, independent status, a
  bilateral peace relation, and an active guarantee of ASY. The former-host
  branch requires its established settlement receipt and the same bilateral
  peace condition.
- ASY must be sovereign at start and expiry. The shared proof gate also rejects
  subject status, patron-client state, historical client capture, lost Mosul,
  and protection breach.
- The compact's AI base is high and doubles only when the former-host route is
  unavailable and the current regional partner remains valid. Availability
  blocks impossible targets, so AI cannot choose an invalid counterpart.
- FORM-18 sets federation mode and clears autonomy mode. The compact sets
  autonomy mode and clears federation mode. The final proof trigger requires
  exactly one mode.

## Treaty record and proof notes

`has_independence_wave_iw058_autonomy_treaty_records` requires all five
two-flag chapters:

- boundary;
- return/protection;
- church-civil jurisdiction;
- transit/property;
- security.

`independence_wave_record_iw058_autonomy_external_treaty_terms` creates only
the four external chapters. It deliberately cannot manufacture jurisdiction,
which remains exclusively owned by the prior competence settlement. The final
focus is the only discovered caller of `chaosx.nr006.5810`, and it calls that
event only when the strengthened settlement-proof trigger already passes.

## Localisation and tooltip notes

The decision has title, description, start, success, timeout, and cancellation
text. The description identifies the former-host and regional-guarantor
alternatives, the five treaty chapters, sovereignty protection, and the
absence of a client relationship. The start tooltip names the 180-day
duration, paid commitment, and counterpart lock. The final event has complete
federal and autonomy option text. No raw scripted trigger is exposed.

## Cleanup and exploit-risk notes

The paid transaction helper records one matching transaction id, subtracts its
resources once, and clears the ledger on commit or rollback. Rollback does not
refund resources. The autonomy decision never creates formations or stockpile
rewards. The active/pending counterpart flags clear on success, timeout, and
cancellation; the persistent named-guarantor target is revalidated wherever it
gates play and is cleared by exact IW-058 package cleanup.

The audited decision, trigger, effect, and event files contain no daily,
weekly, monthly, or all-country pulse. The only `every_country_division` calls
in the package effect file are owner-country division cleanup, not a world
scan.

## Meaningful validation

- Traced both former-host and regional-guarantor paths from selection through
  180-day expiry, five-record completion, final-focus gate, and
  `chaosx.nr006.5810` writer call.
- Confirmed the sole normal caller of `chaosx.nr006.5810` is the final IW-058
  ratification focus effect, which first tests
  `can_write_independence_wave_iw058_mesopotamian_settlement_complete`.
- Confirmed mode writers clear the opposite mode, while the final proof trigger
  explicitly rejects coexistence.
- Confirmed the new proof conditions reuse existing, documented Clausewitz
  scopes and existing partner predicates. `git diff --check` reported no patch
  whitespace error.
- Used the offline Paradox wiki and vanilla documentation for targeted
  decisions, mission cancellation, country scopes, event targets, guarantees,
  subject checks, war checks, custom costs, and stockpile effects. Vanilla
  decision examples were checked for timed-decision and cancellation
  precedent. `hoi4.event_inspect` was not available in this session.

## Skipped meaningful validation

No live save scenario or engine parser invocation was available to this
subagent. Runtime confirmation of a guarantor losing its guarantee or entering
a bilateral war between compact expiry and final focus remains for the parent
scenario pass. The static proof gate now fails closed in each case.

## Remaining risks and recommended follow-up

- The regional target is a package-owned global target. Its lifecycle is exact
  at setup and package cleanup, while the transaction revalidates it at start,
  expiry, and final proof. A parent live scenario should exercise target death,
  guarantee withdrawal, subjection, and bilateral war during each interval.
- The final proof path depends on the final focus effect outside this audit's
  patch authority. It was read as evidence only and currently uses the
  strengthened proof trigger before firing `.5810`.
- No broader decision-system expansion is recommended. No asset work is
  requested or performed.
