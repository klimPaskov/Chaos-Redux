# Dated partner deportation orders

The occupation administration directs finite handovers from Slovakia, Croatia, Bulgarian-held Macedonia and Thrace, and Vichy France.
Germany remains responsible for each origin row, movement and subsequent death.
Hungary retains its separate 1944 route and existing numbers.

## Entry and lifecycle

`camp_occ_try_extended_partner_orders` runs in Germany from the existing month-guarded occupation pass.
It visits five explicit country scopes, with FRA eligible only under its Vichy cosmetic identity.
`camp_occ_extended_partner_process` runs in a partner country with temporary `camp_occ_extended_authority` identifying GER and `camp_occ_extended_destination` identifying state 92.
It admits only the selected living share of eligible origins, through `camp_occ_register_cohort`, without changing population on enrollment.
It first reconciles an eligible destination's physical baseline, including a previously unused reception host, while preserving any provenance warning.
Each partner receives `camp_occ_partner.3` once, covering every province and both Croatian waves.
No transport leaves until the government answers.
Comply and delay dispatch the current month's transport immediately through `camp_occ_extended_partner_dispatch_answer`, so a March-only Bulgarian window remains playable.
A successful movement stores `camp_occ_extended_last_transport_month`, and repeating the processor in that month cannot send another wave.
An invalid or captured destination permits no enrollment or debit.

`camp_occ_extended_partner_move_source` runs in a partner-controlled source state.
It bounds whole-person requests by the living source row, the country transport allowance and physical population outside custody.
It stages state 92 and invokes `camp_occ_transfer_survivors_exact` with the explicit partner route proof.
The shared helper requires equal measured source debit and destination credit before appending origin metadata.
Only a successfully appended arrival row can request arrival violence, through `camp_occ_record_deaths` at the receiving host.
The arrival fraction remains `camp_occ_arrival.violence_request_fraction`, followed by the existing campaign rate on surviving eligible arrivals.
Movement does not itself count as a death and awards no research, equipment or productive workforce.

Delay halves each source's offered transport and the country's monthly transport allowance.
The first Croatian operation offers 70 percent of its enrolled living remainder once per source, retaining the rest for May 1943.
That split is a scheduling abstraction because the source establishes two operations and their combined total without supplying a reliable split.
Between Croatian waves the partner host retains its living remainder without campaign deaths, another enrollment or another report.

Halt is permanent and idempotent.
It costs stability, war support and German goodwill, and a German subject also loses autonomy.
The paid halt decision additionally spends the same sale-aware political power quote as Hungary's halt decision.
The next monthly pass releases the remaining people at home without adding population or deaths.
Germany receives one notification and one Records entry, located at the partner capital.
The decision disappears when no living people remain to deport, and a rejected stale completion refunds political power without sale credit.

## Table and historical sources

`common/script_constants/camp_occ_partner_constants.txt` owns windows, enrollment shares, Croatian wave timing and transport capacity.
Dates are numeric components inserted into one documented `meta_trigger` date comparison, never date arithmetic on `global.date`.
The start is inclusive and the end is exclusive.

| Partner | Window | Enrollment share and basis |
| --- | --- | --- |
| Hungary | 15 May to 9 July 1944 | Existing 0.53 living enrollment share and Auschwitz capacity remain unchanged. |
| Slovakia | 25 March to 20 October 1942 | 0.64 of living assigned origins, approximating 57,000 deported from 88,951 residents. |
| Croatia | First transport month from 13 August 1942, then May 1943 | 0.1795, approximating 7,000 handed over from 39,000 residents. |
| Bulgarian occupation | March 1943 | 0.8725, approximating 11,343 handovers from the approximately 13,000 people targeted in occupied territories. |
| Vichy | 11 August to 10 November 1942 | 0.042, approximating 10,500 handovers relative to the unchanged 250,000-person French source ceiling, restricted to Vichy-held mainland origins. |

[USHMM, Slovakia](https://encyclopedia.ushmm.org/content/en/article/the-holocaust-in-slovakia) supports the March to October operation, its population and its handover into German custody.
[USHMM, Jasenovac](https://encyclopedia.ushmm.org/content/en/article/jasenovac) supports Croatia's two operations and their combined handover total.
[The US State Department's Croatia restitution report](https://2017-2021.state.gov/reports/just-act-report-to-congress/croatia/) supplies the 39,000 population denominator.
[USHMM, Bulgaria](https://encyclopedia.ushmm.org/content/en/article/bulgaria) supports the March handovers and exclusion of Bulgaria's home provinces.
[USHMM, France](https://encyclopedia.ushmm.org/content/en/article/france) supports summer 1942 cooperation, roughly 10,000 foreign residents handed over from the unoccupied zone, and its occupation in November.
The 10,500 Vichy anchor is the takeover audit's rounded planning estimate, not a claim of a precise count in that USHMM article.
The 11 August movement anchor follows the first convoy from Les Milles in the [USHMM France chronology](https://encyclopedia.ushmm.org/content/en/article/france).
The existing monthly cadence can place the first order after the first partial month, as in the Hungarian window, rather than moving people before the dated anchor.

## Geography and abstraction

Slovak and Croatian orders use their core regions.
The Bulgarian source filter names vanilla states 106, 184, 731 and 803, approximating Macedonia, Thrace and the Pirot area without touching Bulgaria's prewar provinces.
State 803 includes territory beyond Pirot, so its source apportionment is an explicit geographic approximation.
State 731 includes Salonika, which historically remained under German administration.
Its inclusion applies only if Bulgaria actually controls that whole vanilla state, an altered-control scenario that can expose more people than the historical Bulgarian handover total.
All amounts remain shares of the existing apportioned and still-living origins, and do not guarantee historical transport or casualty totals.
Outside population losses and territorial changes can reduce them.
The Croatian first operation is represented by a one-month movement window rather than a single transport date.

State 92 is a German or German-administration-controlled occupation reception district, as authorized by the takeover's proposed generic-movement caller.
It represents the district-level handover and wider killing campaign, including transports beyond the individual place represented on the map.
It does not claim that Croatia's or Bulgaria's historical destinations were Lublin, and it does not create an Auschwitz custody institution before its separate date gate.
This is a parent-selected aggregate destination abstraction under the user's G6 design authority, rather than an exact killing-center geography model.
The source tests and completion report retain that limitation.

## Presentation and integration

Events `.3` and `.4` reuse the installed 210-by-176 vanilla report sprite `GFX_report_event_generic_train`, whose DDS was visually inspected.
The Hungarian reports keep their existing national pictures.
Both halt decisions use `GFX_decision_generic_protection` in vanilla `political_actions`.
No new sprite or texture is needed.
Report titles and descriptions are plain text, including the German notification's country-name substitution.
Halt saves the partner as the regular `camp_occ_halted_partner` event target before sending the notification, so the report carries an explicit sender rather than relying on nested `FROM` inheritance.
Records use `camp_admin_history_kind.extended_partner_halt` and `camp_admin_history_extended_partner_halt` through the existing Records row.
The existing camps package and its CXT setup token continue to own the occupation administration, with no added recurring grant or world iterator.

## Usage and checks

In a dated, valid German campaign, `eval_effect GER = { camp_occ_monthly_country = yes }` reaches the route through its normal month guard.
For an isolated QA replay of the same month, clear only `camp_occ_last_month` in a QA copy before invoking that command.
Never clear a successful partner transport month marker to test idempotence.
The government answers the real report, or a QA caller can invoke the corresponding comply, delay or halt effect in that partner's country scope.
These effects still require the live order's eligibility.

Future work could split reception across individually modeled historical destinations and replace coarse origin geography with independently sourced local allocations.
Those extensions require separate accepted design and accounting tests rather than another casualty multiplier.
