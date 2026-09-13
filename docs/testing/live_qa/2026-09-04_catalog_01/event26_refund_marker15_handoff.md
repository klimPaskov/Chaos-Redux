# Event 26 refundable marker parser repair

Status: implemented source repair; native parser and gameplay acceptance pending parent launch 15.
Acceptance basis: parent assigned this exact unsupported effect under the user's autonomous QA and safe parser repair authorization, with no redesign and no other source writes.

## Changed surface

Only common/scripted_effects/026_black_friday_effects.txt:2764 changed:
```txt
set_temp_variable = { black_friday_purchase_is_refundable = constant:universal_cost_framework.zero }
```
This replaces the unsupported clear_temp_variable operation in black_friday_begin_alien_infantry_landing_reservation.
No new helper, call site, constant, event target, asset, localisation, probability, price, or timing change was introduced.
The existing universal_cost_framework.zero is declared as zero in common/script_constants/chaosx_universal_cost_constants.txt:16.

## Exact consumer contract and lifecycle proof

The marker is a temporary input to black_friday_record_achievement_transaction in country scope.
Its existing source contract at lines 235–238 expressly identifies an optional positive marker.
The only executable reads are the conjunction has_variable = black_friday_purchase_is_refundable and check_variable = { black_friday_purchase_is_refundable > 0 } at lines 268–269.
A positive marker records a pending achievement transaction.
An absent marker and a present zero marker both take the committed branch, which records the committed state and calls black_friday_add_achievement_family.
Zero is not claimed equivalent to absence generally: has_variable distinguishes them, but its only observation here is conjoined with the strictly positive check.

The sole producer sets the marker to constant:universal_cost_framework.one at line 2762, immediately calls the recorder at 2763, and resets it at 2764.
The successful reservation remains pending because recording occurs before reset.
The record helper neither mutates the marker nor calls a helper that reads it.
Failure and inactive-sale branches do not set it and do not reach this reset.
The sole caller of the reservation helper is common/decisions/016_alien_infantry_landing_decisions.txt:38 in alien_infantry_call_landing.complete_effect.hidden_effect; both effect blocks end immediately after the call.
A subsequent same-chain ordinary recorder invocation sees a nonpositive marker and therefore commits; another successful reservation overwrites with one before recording.
The existing confirm and retract helpers consume stored transaction states and transaction ids, not this marker.

All 13 recorder call sites were inventoried: seven in 026_black_friday_effects.txt (742, 1386, 1528, 1704, 2228, 2387, 2763); two in 017_random_faction_effects.txt (1625, 2285); and one each in 012_africa_elephant_operations_decisions.txt:98, JAP_chemical_campaign_effects.txt:166, japan_biological_campaign_effects.txt:228, and germany_mengele_effects.txt:654.
Only the landing reservation supplies the refundable marker.
Repository-wide hidden-file exact-token search, excluding Git internals and archival live-QA copies, found no other source observations.
Additional active-source searches for purchase_is_, is_refundable, and purchase_[ found no dynamic reference construction of this identifier.
There is no absence-sensitive downstream branch, localisation display, alias output, array storage, or scoped copy of this marker in current source.

## Evidence and preservation

The supplied launch_14 error.log reports this exact invalid effect at source line 2764 eight times (log lines 649, 1501, 2299, 3096, 3904, 4701, 5419, 6216).
A full-byte backup was captured before source inspection or mutation in pre_patch_event26_refund_marker15/026_black_friday_effects.txt.
SHA256 before: 0907FEBF5FC43646A290585144E18A02C06537D0AE1EE1E544CE8EF93670E3F5.
SHA256 after: 182DA423CABA285634D143287AAFBE2BEB06774F6C5C5A13EE91065E7A93030D.
The source hash was checked against the backup immediately before replacement.
Post-write comparison confirmed the current file equals the captured baseline with exactly this one replacement, preserving every other byte through UTF-8 round-trip.
Do not restore the entire backup over later collaborators' edits; reverse only the exact replacement after checking current contents if recovery is required.

## References and required inspection

Read AGENTS.md and the events, debug-playtest, subagents, and decisions-missions skills.
Consulted all eleven required core offline wiki pages, especially Data structures variable lifetime, clear_variable restriction to regular variables, has_variable existence semantics, and strict check_variable examples.
Installed vanilla effects_documentation.md set_temp_variable and clear_variable, triggers_documentation.md has_variable and check_variable, script_concept_documentation.md Script Constants, and common/script_constants/documentation.md were consulted.
Vanilla common/scripted_effects/GER_scripted_effects.txt:1273 provides a temporary zero initialization precedent.
Existing chaosx_dynamic_effects.txt and its matching documentation were checked; no new abstraction is needed.
Event 26 registry BF-ALIEN-001 and current owner-adapter inventory describe the delayed landing reservation and preserve its owner-controlled resolution.

Initial MCP schema attempts using selector.path and a string stateSubject were rejected without source mutation.
The accepted file state_flow request returned full-workspace data rather than an exact helper proof: revision f75c229d49083bc73ef83735837605c26839d8e8dc7f5401da729fdda08191e1, 3915 blocking event-chain diagnostics.
Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d924fa716012d23c1941618e86c37103e3e2a27924a0fedebebd74670de3c334/33262f735d4cd25042ee19f8d1ddaa24bb1911d4c75b84678cd299b9d75689e3/event-state_flow-f75c229d4908.json
The file render likewise selected 12 nodes while omitting 102704, and is not semantic validation.

Following the parent's bounded-selector instruction, event_inspect trace used event chaosx.nr26.1, maxDepth 1, maxNodes 5, maxEdges 10, expandHelpers false.
Revision: 86077b1d5f2fc155ad9a17fff30027ac88a6ac544a8a3c242b19b79f1d6b0260.
Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6afa0c49f8c9a78e020d3e2241f279605d162dea5e189f09423e3fb5c4394128/0a4c2d10df36fa4f134e5d66873680a0de857367ee1626e3cf523ed2a5a26c32/event-trace-86077b1d5f2f.json
The matching bounded state render returned selectedNodes 0 and validation passed false with the message: Large workspace analysis deferred workspace-wide helper projections and lifecycle passes; direct evidence is linked.
Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d8dc76d312614f09a97305104d6ecaa273aa412da7d64957b971658ce1e2754/05f6ced460348fc960700886fa2c4624b1843d029349b5b6f6f62374706c8b96/event-state-86077b1d5f2f-manifest.json
Native helper projections are deferred in this workspace; no exact helper projection route was identified.
These partial projections are explicitly not a proof of reset semantics or installed-engine acceptance.
The source proof above supports the narrow repair independently; required MCP evidence remains limited.

## Remaining work and limitations

No gameplay simplification or fallback was used.
No source work remains for this exact marker repair.
Native launch acceptance and pending-reservation/ordinary-transaction gameplay behavior have not been observed by this subagent.
The parent owns launch 15, final native verification, broader QA, and commit.
No game launch, process control, commit, other source edit, or skill update was performed.
Read-only MCP event_compare was attempted between the recorded file-inspection and bounded-entry revisions, with render false and maxRenderNodes 5.
It returned status error, code EVENT_REVISION_NOT_CACHED, validation passed false, and no artifacts.
The failed comparison provides no semantic evidence; no source-only substitute is represented as an engine comparison.
Earlier comparison schema attempts using kind fields or an empty after selector were rejected before execution.
