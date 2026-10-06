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
