# Occupation transaction proof and dated calibration boundaries

Disposition: implemented sequential disjoint-receipt reconciliation; historical total acceptance remains unresolved.
Acceptance basis: parent follow-up explicitly authorized replacing blanket occupation-law suppression if outside debit retirement, current custody exclusion and measured receipts establish finite disjoint accounting.

## Sequential transaction proof

Let `E` be remaining exposed civilians, `P` current actual state population, `C` current custody, `F` the protected civilian floor, and `L` the shared territorial civilian-death ledger, all converted to thousands.
Observation baselines `P0` and `L0` are taken at enrollment and after every reconciliation/own receipt.
Let `H = max(0, P - C - F)`.
The module retires `R = min(E, max(0, P0-P, L-L0, E-H))` as exposure removed, without changing `P` or adding any authority death.
`P0-P` detects outside net population decline, `L-L0` detects recorded deaths even if growth or arrival hides that decline, and `E-H` prevents a stale exposure reservation from exceeding current noncustody membership.
Taking the maximum rather than summing avoids counting the same physical loss twice.
The resulting exposure `E1 = E-R` is nonnegative and does not exceed current noncustody headroom.

The next request is a fraction of `E1`, bounded by `E1`, current physical headroom and the per-receipt safety limit.
It is rounded down to whole people before calling the public physical-loss API once with logging disabled.
The actual own receipt is `D = P_before-P_after` measured after that synchronous call.
Only `D` is added to state/original-authority monthly, cumulative and campaign-cause records.
One public Deaths projection uses `apply_state_pop = 0` and `record_state_ledger = 1`, publishing `D` without another physical debit.
The module then snapshots the territorial ledger after that projection, so its own receipt is absent from the next outside-delta measurement.
The row invariant is `initial = remaining + own measured deaths + exposure removed + released survivors`.
Capture or reform closes the row, records remaining survivors in place, and preserves the original country pointer and past receipts.

The shared generic occupation pathway in `chaos_meter_effects.txt` physically debits through `chaos_meter_apply_state_civilian_pop_loss_from_deaths_change` and synchronously records its territorial ledger.
It therefore supplies the gross-death observation needed here even when population growth is positive.
That read is solely a conservative membership reduction; generic occupation, famine, combat or unknown deaths are never relabeled as the campaign authority's deaths.
Foundation custody projection also sets the existing public `chaos_deaths_record_state_ledger = 1` flag.
No shared source was changed by this module.

The country owner confirmed processing order: historical census admission, foundation, occupation, then country institutions.
Admission excludes occupation remainder, existing detainees and civilian replacements, and increments only accepted census receipts.
Institutional receipts later in the chain become visible to the next occupation reconciliation; if a core receipt occurs after the occupation tick, it is likewise retired at the next campaign transaction.
Physical population is already smaller in the meantime, so it cannot be debited as a previously living person again.

The public snapshots cannot identify an unlogged outward transfer exactly offset by an inward transfer between observations.
Such a flow needs its own explicit receipt callback for individual-origin identity proof.
This is a precise limitation of aggregate flow observation, not a reason to suppress the documented core occupation pathway, which does publish its synchronous ledger.

## Dated scenarios and sources

The tests use the runtime source constants without increasing rates or making a residual-to-six-million adjustment.
The [USHMM national population source](https://encyclopedia.ushmm.org/content/fr/article/jewish-population-of-europe-in-1933-population-data-by-country) supplies the fixed circa-1933 national ceilings.
They are geographically apportioned before control changes, so a partially controlled origin remains a partial source.

The Hungarian scenario begins German-controlled exposure in March 1944, supported by [USHMM's Hungary account](https://encyclopedia.ushmm.org/content/en/article/the-holocaust-in-hungary?parent=en%2F11710), and closes the model row after April 1945.
The 1933-border ceiling is 445,000; it must not be confused with wartime Hungary after territorial annexations.
With full control of that fixed source, the model records 132,801 campaign deaths; quarter control records 33,195; reform at January 1945 records 99,530.
These are finite dated model outcomes, not a claim to reproduce the historical deportation or murder total.
USHMM records roughly 440,000 [deportations from Hungary during May–July 1944](https://encyclopedia.ushmm.org/content/en/timeline-event/holocaust/1942-1945/deportation-of-hungarian-jews); deportation is a movement and cannot be imported as an additional death receipt.
Without a cross-state origin-preserving transfer module and the changing territorial population coverage, that historical sequence cannot be certified by this occupation-only ledger.

The China stress scenario uses July 1937 through August 1945, consistent with [Cambridge's war chronology](https://www.cambridge.org/highereducation/books/world-war-ii/F81FB18F5B948CFFB25C5B6939AF6497/japan-and-china-19371940/119B63CA09ADAF2F123D57CA4C2A7F81) and [Richard B. Frank's National WWII Museum interview](https://www.nationalww2museum.org/war/articles/asia-pacific-war-richard-b-frank).
It observes records through 1949 and verifies that closure does not restore deaths or resume exposure.
The 100-million affected-region population and 1,000-person-per-row monthly external debit are explicit stress inputs, not sourced historical cause frequencies or a reconstructed occupation map.
Across ten finite regional rows, the scenario records 8,358,200 campaign deaths and 980,000 outside deaths, giving 9,338,200 distinct physical losses.
Only the campaign receipts belong to the campaign authority; the outside total is a test sum for conservation and receives no inferred blame.
Half the territory produces 4,155,370 campaign deaths; peace at the end of 1940 produces 3,694,450.
The Museum's broad estimate of roughly 11.7 million Chinese noncombatant deaths is a comparison for combined war and occupation consequences, not a target to fill with additional campaign debits.

## Remaining historical acceptance constraint

Six million Jewish victims cannot be certified from a scenario that activates every supplied national source for the same 48 months.
The resulting 6.376-million capacity bound includes sources that were never occupied on that schedule and omits changing custody, forced movement, emigration and collaborator control.
The precise missing evidence is a dated, origin-preserving combined custody/occupation scenario across the implemented geographical source rows with actual controlled shares and accepted transfer/attrition receipts.
This module has no accepted cross-state transfer receipts, and its authority gate supports direct German/Japanese control only.
Those omissions cannot be corrected by raising the monthly fraction or consuming a national residual as deaths.
The blanket generic-occupation suppression gap is resolved; the separate historical total acceptance remains honestly open pending that combined scenario evidence.

`accounting_results.json` records 16 passing source-linked model scenarios.
No MCP calls were made during this follow-up, per the parent's coordination instruction.
