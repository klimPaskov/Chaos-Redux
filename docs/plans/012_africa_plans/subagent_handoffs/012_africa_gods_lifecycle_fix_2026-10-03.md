# Event 012 participant lifecycle repair — 2026-10-03

Disposition: implemented source repair of F1–F3 from `012_africa_gods_lifecycle_audit_2026-10-03.md`.
The acceptance basis is the active user goal: retain hidden conduct until settlement, preserve permanent defiance until accepted restoration, and cancel live authority when the host is lost.
This is a bounded repair, with no new world iteration, timer, route, cost, or simplification.

## Changed behavior

`common/scripted_effects/012_africa_gods_lifecycle_effects.txt` separates first-enrollment history initialization, durable opt-out, and live reconciliation cleanup.
An existing history-count variable, including zero, proves an existing ledger; counters and aligned kind/day arrays are initialized only when that proof and the initialization flag are both absent.
Wrath and its band are initialized only when absent.
Returning enrollment preserves conduct and restores live defiance from permanent opt-out.
Archival, participant cleanup, and unifier-loss cancellation remember permanent opt-out before removing live authority and clear interrupted reconciliation permissions and dates.
Accepted paid reconciliation is the sole clear of permanent opt-out.

The real ten-political-power transfer remains unchanged.
Its completed offer records history kind `reconciliation_offer = 12` before any interruption can clear payment permission.
Cleanup neither refunds a completed transfer nor grants unpaid acceptance.
Reconciliation requires an existing future deadline, paid reparations, and the pending offer before the host acceptance helper can resolve it.

The participant territory Wrath floor uses `gods_of_africa_participant_holds_host_core_state`, which checks the participant's controlled African states against the explicit host.
It no longer depends on the initiating event's ROOT or on the participant's own cores.

Changed source: core Gods effects, core Gods triggers, Gods constants, and the new lifecycle helper file.
`docs/events/012_africa/gods_of_africa.md` describes retained history and review interruption consistently.
No assets or player-facing costs changed; hidden initialization and opt-out flags have no exposed requirement blocks.

## Meaningful review scenarios

`L1_same_host_revival`: a participant with nonzero conduct is archived or cleaned, then registered again; initialization preserves every counter and aligned history array, and live review state is rebuilt independently.
`L2_successor_authority`: a defiant participant loses live authority with the host; cancellation first records durable opt-out, and later enrollment restores live defiance and its Wrath floor.
`L3_pending_review_revival`: a paid review is interrupted; live pending/payment/offer permissions and dates are cleared, the completed transfer and offer history remain, and the existing owner tick can open a fresh review.
These are source-path reviews, not observed native execution.
The independent follow-up review belongs in `012_africa_gods_lifecycle_fix_review_2026-10-03.md`.

## References and validation limits

Installed `documentation/effects_documentation.md:661–670` defines explicit mission activation; `6083–6091` states that removal runs neither completion nor timeout effects.
Revision SHA-256: `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Vanilla `common/scripted_effects/SWI_scripted_effects.txt:1886–1901` removes the former president's mission separately from clearing his flags, confirming that callers own permission cleanup.
Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:465–478` covers explicit activation and mission lifecycle, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`.
Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:1147–1156,1210–1256` covers membership and scope-array iteration, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.

The connected inventory exposes event inspect/render/compare and reference context/search/read; fresh narrow requests were made for `.606` and mission removal.
Results and any narrower retries must be recorded before claiming MCP acceptance.
The prior audit's U1 membership reachability, U2 archived surviving participants at settlement, and U3 victor/restoration milestone remain unresolved separately.
No native clean-log, save, inherited-country-state, or full Event 012 completion claim is made.
