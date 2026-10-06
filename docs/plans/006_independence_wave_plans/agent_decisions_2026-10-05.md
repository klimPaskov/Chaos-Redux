# Event 006 finishing decisions

These decisions implement the user's 2026-10-06 instruction to finish the interrupted Event 006 takeover under the quality rules issued on 5 October.
Earlier decisions and their acceptance evidence remain in `agent_decisions_2026-10-04.md`.

## D35. Transfer history-recruited characters at runtime

Disposition: `implemented` at source, with native release and clean-load confirmation pending the orchestrator.
Basis: priority-one inbox finding L1 and the user's requirement to preserve the characters while removing runtime recruitment warnings.

The executor's 31 missing-roster repairs and NAV's Aguirre repair use character-scope `set_nationality = PREV` instead of runtime `recruit_character`.
Each of the 32 referenced tokens has an existing history recruitment, and the missing-character guards remain intact.
Inside each character scope, PREV is the receiving carrier rather than the wave executor's ROOT.
No character, role, portrait, startup recruitment, or package identity was deleted.
The installed effects documentation supports COUNTRY and CHARACTER scopes for `set_nationality`, and the offline character documentation says recruitment must occur in history and explains restoring retired characters with `set_nationality`.
Vanilla `events/AAT_Sweden.txt:7899-7914` transfers history-recruited Finnish and Danish officers through their character scopes.

The runtime transfer also replaces the invalid recovery branch added by D11, while retaining D11's decision to keep Aguirre during package cleanup and restore his corps command when necessary.
The exact history crosswalk and reference citations are in `subagent_handoffs/runtime_roster_transfer_20261006.md`.

## D36. Explain rejected manual Independence Wave requests

Disposition: `implemented` at source, with Settings delivery confirmation pending the orchestrator.
Basis: G7 in the finishing task requires an event-owned explanation when a forced launch cannot apply, and G2 requires one report per request.

The canonical entry keeps its existing pending-response barrier inside `immediate`, so a manual request can receive an explanation instead of being silently rejected by the event's top-level trigger.
A failed standalone attempt calls the same event-owned feedback helper.
The helper uses the requesting player's existing Settings request target and per-request failure flag, sets that flag before dispatch, and sends `chaosx.nr6.73` only once.
It snapshots whether talks are still pending or a release failed after mutation without a completed rollback.
The three descriptions distinguish waiting for replies, unfinished changes, and a launch that established no wave.
Automatic requests without a manual requester remain silent, and the helper changes no allocator, release, history, or retry state.
The shared Settings framework files remain untouched.

The new report uses the registered wave-summary image and the existing 13-day report timeout.
All its title and description strings are plain text.
The popup count for one failed Settings request is one, including repeated failure calls in that request's dispatch chain.

## Inherited uncommitted checklist hunk

Disposition: `unresolved` as working-tree formatting, with no design change.
The only pre-existing uncommitted Event 006 path at the start of this pass was `docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md`.
Its 129 removed and 129 added lines compare identically with whitespace at line endings ignored.
The physical working copy is preserved, and no acceptance claim is inferred from that formatting hunk.
The CHU/ASY source hunks and the TAT specification paragraph mentioned by the takeover history have already been adopted by its committed D13 and D14 work.

## D37. Reserve the factory capacity advertised by regional projects

Disposition: `implemented` at source, with native reservation and release confirmation pending.
Basis: G4 requires a visible cause and cost for every benefit, and the parent accepted the decision auditor's confirmed missing reservation.

The nine D25-D33 regional decision files contain 48 administration-standard and 38 strategic-standard projects that advertised two civilian factories and tested for free capacity without holding it.
Each has a timed native `civilian_factory_use` modifier of two for its existing 120- or 180-day duration.
Upfront command power, manpower, stability and the train-or-convoy choice remain unchanged, as do rewards and AI coefficients.
The transport payer selects exactly one alternative.
The [decision handoff](subagent_handoffs/decision_regional_audit_20261006.md) lists every affected id and the vanilla timed-decision precedent.
An army security project spends four resource types, and the compact blocked-price selector puts manpower first when manpower is missing while the full hover tooltip retains all four charges.

## D38. Resolve live dynamic formable countries and their display values

Disposition: `implemented` for the reviewed non-weighted source, with the weighted dependency comparison tracked separately.
Basis: D34 queued these static-template lookups, and the parent reviewed the bounded country audit.

FORM-02/03/04/05/48 requirements, consent accounting, member callbacks and status selectors find the actual country through the bounded active-country registry and `original_tag`.
Effect lookups are deterministic and preserve PREV, with zero or one qualifying family carrier under the existing identity locks.
The FORM-04 adjacency and peace proof addresses the dynamic Saar country rather than its absent AJX template.
The [country handoff](subagent_handoffs/country_dynamic_carriers_20261006.md) records the exact files, ids, references and limits.

The parent found an additional display defect after the selector repair.
Forty FORM-03 numeric return strings and two FORM-05 summaries still read AFX, AGX, ARX or ASX as static localisation namespaces.
Their `text.trigger` branches initialize caller-owned temporary outputs, capture the selected live country's numbers, and return those outputs through literal localisation keys.
FORM-05 also captures the live government pointer for its name.
No persistent variable or flag is created by this display repair, and the plain report variants retain their lack of colour codes.

## D39. Consume incident delivery before showing the report

Disposition: `implemented` at source, with re-release and duplicate-delivery scenarios pending native confirmation.
Basis: G2 and the parent review of D15's generation-safety claim.

The country-level incident-generation variable is overwritten when the same country starts another origin, so it cannot alone identify a delayed event instance.
The first and second package incidents store separate due dates using the shared days-to-date helper.
All 130 public incidents require their current appointment to be due and undelivered, and consume a delivery flag in `immediate` before either answer is chosen.
All 260 options validate that the current government still awaits that phase's reply and has not resolved it, before applying the original payment and outcome.
Generation cleanup clears both dates and delivery flags.
Early calls from a prior release are ignored, while a duplicate mature call cannot open or settle the same question twice.
The 45-day first and 150-day second intervals, option identities, payments, outcomes and normalized AI blocks remain unchanged.
This is a bounded delivery repair rather than an assertion that a delayed event carries an immutable generation payload.

## D40. Keep true status visible beneath decorative motion

Disposition: `implemented` for the reviewed art and source wiring, with final matching GUI evidence tracked in the UI handoff.
Basis: G5 and G6 authorize correcting visible defects and weak presentation.

The four optional status animations used the same strips as the static recognition, dependency, League and formable readouts.
Their loops cycled through semantic statuses regardless of the country's values.
The static symbols retain their live frame properties and remain visible with animation on or off.
Eight separately authored native-alpha frames animate a small flourish on a shared bronze ring with a transparent centre, leaving the inner status symbol legible.
The existing animated aliases and static fallbacks use that decorative ring instead of the semantic strips.
The recognition strip's idle cell receives the reviewed bronze treatment, with its other four cells unchanged.
This preserves animation and current-state information without a static substitute.
The parent reviewed every ring frame and native/4x composites, and accepted its deliberately translucent ornamental edge because the actual state symbols remain clear.

## D41. Aggregate member replies and consume opening reports

Disposition: `implemented` at source; duplicate native delivery remains a live check.
Basis: G2 requires a low report count per chain.

The founding report consumes a delivered flag in its immediate block while retaining its separate unanswered-choice flag until the player replies.
The former host's ordinary and two special response reports share one delivered flag, cleared only when the bounded host response is queued.
FORM-03 collects member outcomes into one report per origin, delayed thirteen days to include the ordinary reply window, instead of reporting each member separately.
Its text describes the current constitutional settlement and service agreements rather than whichever member last overwrote a reporting target.
The summary marker survives FORM-03 cleanup and is cleared by the next origin reset.
Package founding incidents remain at most one first report and one second report per package and origin.
World declaration news retains its existing one-dispatch guard, and foreign reaction routing retains its existing country reply guard.

## D42. Preserve threat coefficients while addressing the actual country

Disposition: `implemented` source correction; the probability handoff records unresolved scenario evaluation and comparison limits.
Basis: G4 and the read-only baseline audit found literal-template and nested-scope defects.

The Pacific HAW/FSM collapse modifiers resolve the current HBX country through the bounded active registry.
The FORM-05 threat helper resolves current ARX/ASX countries by the same contract.
The former-host war test addresses PREV, the government whose threat is being checked, rather than ROOT, which can be a different autonomous member or calling country.
All authored probability coefficients and normalized incident option weights remain unchanged.
An excluded or unresolved MCP scenario is not evidence that the score stayed equal.

## D43. Capture existing dynamic carriers for the Event 021 adapter

Disposition: `implemented` for actor capture; Event 021 release and origin ownership are preserved.
Basis: D34 queued this exact Event 006-owned mapping and the completion audit confirmed its literal-template gap.

The adapter first retains its existing static carrier lookup.
Only when no actor was captured, it searches the bounded aligned Event 006 active-country array for the requested package and its exact original tag among AFX, AGX, AJX, ARX, ASX and HBX.
The selection-owner target receives the validity flag with the captured country, and prevents a later row replacing it.
No country is released, initialized, enrolled or granted a different origin by this fallback.
Event 021's preflight, static release contract and consumer ownership checks remain authoritative.

## D44. State report choices in plain terms

Disposition: `implemented` at source.
Basis: G3 and a dependency walk over 752 report/news title, description and scripted-localisation return keys.

Thirteen title/description strings and eight public option labels used the prohibited words records, receipts, ledgers or pilots, including several literal financial nouns.
The revised text names wages, taxes, property claims, frontier disputes, agreement terms and aircrews directly.
The Clyde report title is "The Clyde Shipyard Accounts".
The shortened Asante and Sokoto reports retain their actual counterpart names and recognition, association, embargo and reconquest choices.
The Council of Communities report retains consent, community guarantees and autonomy conditions.
No event id, option, cost, effect, scope pointer or report dispatch changes with this wording.
The full report/news dependency colour audit returns zero findings.
