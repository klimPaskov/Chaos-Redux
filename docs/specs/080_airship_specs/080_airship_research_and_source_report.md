# Event 080: Research, sources, and release gates

## Authority

The user's Airship brief is authoritative for identity, route length, timing, controller-based hosting, Condition, real deaths, direct foreign-controller war, the named evolutions, and presentation. It overrides conflicting old catalog and runtime behaviour. Balance figures and expanded content in the numbered parts are authored design accepted within the planning briefs recorded in the [README](README.md).

The original legacy inspection was pinned to repository commit `879b3007d3b6bf75c726c11635473fccda45c569`. Re-read the current files before implementation; that commit is evidence of what the old event did, not of the current checkout.

## Legacy evidence

| Reference | Path | What it established |
|---|---|---|
| R01 | `events/080_airship.txt` | Legacy opening and ending rewards, host messages, delayed crash report, and war inside a later US event option |
| R02 | `common/decisions/080_airship_decisions.txt` | One-day mission, completion at 120, broad flag refresh, paid crash controls, nuclear shortcut, and fixed manpower loss |
| R03 | `common/scripted_guis/080_airship_scripted_guis.txt` | Decision-category GUI, window name, and dynamic trail sprite selection |
| R04 | `common/scripted_triggers/080_airship_triggers.txt` | Numeric route branches 0 through 121 and final region 117, without exact state bindings |
| R05 | `common/on_actions/080_airship_on_actions.txt` | Additive per-country risk and daily progression; read in substantial ranges |
| R06 | `common/scripted_effects/080_airship_effects.txt` | Broad owner-based host selection and the index-1 region-array discrepancy; lines 1 to 130 read |
| R07 to R10 | `interface/chaosx_decisions.gfx`, `interface/chaosx_decisions.gui`, `common/decisions/categories/080_airship_categories.txt`, `localisation/english/080_airship_l_english.yml` | Search excerpts identifying `GFX_airship_trail_120`, the Airship container, the category, and legacy wording |
| R11 | `docs/events/013_natural_disasters/overview.md` | Public disaster gateway, future-date jobs, wildfire family, existing-card merging, and Deaths ownership |

## Traceability of the main corrections

| Finding | Evidence | Design response |
|---|---|---|
| Stale Major and war-goal catalog description | Catalog row 80 against the brief | Minor Fire-Once and immediate declaration are authoritative |
| Daily route timing and early completion | R02 against R04 | 121 transitions at two days each, including the final return |
| Broad owner-based host flags | R05, R06 | Exact actual position and live state controller |
| Existing dynamic map | R03, R07, R08 | Preserve event-owned map and route art, validate rather than replace it |
| Popup-dependent retaliation | R01 | Immediate crash-resolution declaration, reports afterwards |
| Nuclear and manpower shortcuts | R02, R05 | Actual crash damage and exact state population deaths |
| Per-country and additive risk inflation | R05 | One bounded ship exposure per flight window |
| Wildfire ownership and delayed jobs | R11 | Immediate impact separated from owner-managed fire |
| Missing original stop and state map | R04 gives only region predicates | Preserve the crosswalk and keep exact binding as a release gate |

## Historical and asset research leads

The event is fictional. Passenger counts, refits, the Flying City, rewards, and unconditional American retaliation are design inventions, not claims about a real airship. No historical round-the-world route replaces the project's route. These sources are leads for the asset and super-event researchers; no redistribution permission is implied.

| Source | URL | Status |
|---|---|---|
| US Naval History and Heritage Command, USS Akron photography | `https://www.history.navy.mil/content/history/museums/nmusn/explore/photography/aircraft-us/aircraft-usn-a/uss-akron-zrs-4.html` | Located; full page not reviewed |
| US Naval History and Heritage Command, Akron ship history | `https://www.history.navy.mil/research/histories/ship-histories/danfs/a/akron.html` | Located; full page not reviewed |
| Zeppelin Museum, American rigid airship USS Akron | `https://www.zeppelin-museum.de/en/digital-offers/the-american-rigid-airship-uss-akron` | Headings and image references reviewed |
| Airships.net, Graf Zeppelin | `https://www.airships.net/lz127-graf-zeppelin/` | Specialist lead, including a manifest reference |
| Airships.net, Hindenburg disaster | `https://www.airships.net/hindenburg/disaster/` | Passenger and rescue context only |
| British Pathe, archival Hindenburg footage | `https://www.youtube.com/watch?v=CgWHbpMVQ1U` | Archive lead; rights not reviewed |

## Release gates

| Gate | What must be established | Owner |
|---|---|---|
| G01 | Exact state, water, stop, coordinate, and final-frame binding for all 122 route records | Repository explorer and event UI owner |
| G02 | Boarding-group death debits through the exact state population loss helper with correct Deaths attribution | Main implementation agent |
| G03 | Urban and industrial fire coverage where wildfire eligibility does not apply | Disaster owner |
| G04 | Immediate war against exact allied or subject controllers under native restrictions | Main implementation agent |
| G05 | Nearby-unit damage and casualty reconciliation | Main implementation agent |
| G06 | Technology targets and modifier support for rewards and trials | Technology review |
| G07 | Canonical asset references, original map files, and finished processed art | Asset specialists and UI owner |
| G08 | MTTH evolution pacing and AI and probability sequence evidence | Probability auditor |
| G09 | Researched super-event text and licensed audio | Super-event researchers |
| G10 | Workbook update and independent completion review | Workbook owner and completion auditor |

These gates identify implementation work; none of them justifies reducing the design.
