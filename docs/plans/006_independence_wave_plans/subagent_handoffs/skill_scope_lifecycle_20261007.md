# Scope and lifecycle skill maintenance

Disposition: implemented within the bounded skill/documentation scope, pending parent review and commit.

Repository root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Owned changes: three additive skill hunks and this new handoff only.
No gameplay source, configuration, workbook, generated mirror, Git index, commit, game session, or log was changed or used.
The parent owns review and selective staging, preserving all other agents' changes.

## Coverage checked and duplicates avoided

- Updated `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-events\SKILL.md`: proposal popup lifecycle at final lines 213-220 and the ROOT contract extension at final lines 574-576.
- Existing Event anatomy lines 207-212 already cover the safe first option, timeout selection, fire-time option visibility, click-time guards, duplicate requests, and authority loss. Retained that guidance and added only snapshot survival through withdrawal, replacement serialization through after, exact reply identity, stale-close wording, and the absence of a special timeout branch.
- Existing Country activation and ROOT lines 541-565 already cover ROOT invariance, callback scope tracing, participant pointers, nested input freezing, and recipient-rooted setup events. Added only debug/iterator coverage, explicit actor contracts, generation-bound recipient relays, and separate entry-path checks.
- Updated `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-decisions-missions\SKILL.md`: Paid timed-decision entry and expiry at final lines 249-259.
- Existing custom-cost lines 237-245 cover shared inclusive affordability, display/payment alignment, and coherent quotes. Existing refund, receipt, and cleanup sections retain their ownership. Production action contract tests at pre-edit lines 997-1004 already distinguish source tests from native execution.
- Added only the exact native-reserved entry exception, active receipt before debit, exact paid expiry proof without quote/slot-open retesting, success-before-active-clear ordering, and corresponding source cases.
- Created no new skill. Left all other skills and generated Claude/Qoder/Cursor mirrors unchanged. No AGENTS.md or subagent-routing update is required.
- Used skill-creator, chaos-redux-events, chaos-redux-decisions-missions, and AGENTS.md section 9 maintenance guidance.

## Reviewed handoff evidence

These are citations to already-reviewed source handoffs, not a fresh gameplay or native audit.
Earlier findings are historical where a later follow-up in the same handoff records a correction.

- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\006_independence_wave_plans\subagent_handoffs\signature_decision_review_20261007.md`, lines 26-40, 137-138, 149-179, and 181-193. Read snapshot SHA-256: `83F129E56E440AC18172BF0C471D88BCFBBD64454E499863642738985A32E472`.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\006_independence_wave_plans\subagent_handoffs\ready_formable_dependency_review_20261007.md`, lines 60-69, 110-142, 249-255, and 296-303. Read snapshot SHA-256: `26AB3A20840BE48BCF7EA71882717A44EBE45E52061C475EA69469ADC4CD1FFF`.

The signature follow-ups record serialized project slots and finish gates, receipt-before-payment ordering, current receipt checks at expiry, immutable popup snapshots retained on withdrawal, current-inviter replacement relays, guarded stale replies, and the native-reservation entry exception.
The later correction at signature line 164 disclaims dynamic disappearance of an acceptance option that was visible when fired, so every reply retains its effect guard.
The dependency review identifies foreign-root cleanup/debug hazards and the earlier unresolved popup replacement case, while explicitly limiting its ordered-source models to declared primitives.
Underlying gameplay paths and line spans remain recorded in signature lines 143, 176 and 191, and dependency lines 60-69 and 110-142.

## Direct reference evidence

Connected reference_context, reference_search and reference_read routes returned successful results for workspace `mod_chaos_redux_ea3b2d67c2c0`.
Source lookup exposure was verified. No engine-facing source inspection was required for these documentation-only insertions.
Both context bundles had omittedSources at limit 4. Targeted searches/reads covered the cited rules below, without claiming comprehensive surface coverage.
No web wiki access was used.

| Directly read reference | Lines | Revision | Rule or limit |
| --- | --- | --- | --- |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 260 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` | ROOT within an event is its recipient. |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md` | 180-191, especially 184-186 | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` | after follows the chosen option and timeout_days selects the first option. |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 2943-2967 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | country_event is a COUNTRY-scope effect with optional delivery delay. |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` | 337-356 | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` | complete_effect at selection, remove_effect at expiry, modifiers during the timer, separate cancellation. |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md` | 1-46 | `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019` | Native selection/target scope and evaluation contracts. |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\modifiers_documentation.md` | 2202-2206 | `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e` | civilian_factory_use schema, without callback-ordering proof. |

## Owned preimages and exact patch

Capture basis: the current shared file bytes immediately before this worker's additions, rather than Git HEAD.
Before-text blocks preserve the text lines around each insertion. Hashes identify complete byte preimages.
The unified diff below includes only this worker's additions. This handoff is wholly owned as a new file.
If hashes no longer match, reconcile the three anchor-local insertions rather than restoring whole files or staging full shared diffs.

- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-events\SKILL.md`: before SHA-256 `AE6DA830EA31B9D1B7499D22240ED31F95E116220DD18518F7759D4E7482407E`, after SHA-256 `88037fc7f66e0d02c766ece6f381f12fc82cbdb4314caa4ce0bf909952c78f4a`.

Before `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-events\SKILL.md`, lines 209-215:

```markdown
Keep the option-availability guard separate from a click-time effect guard that rechecks permission, the current request and context against the immutable pending receipt before applying consequences.
Duplicate requests must not overwrite that receipt.
Treat controller changes or loss of authority as no consent.
Existing affirmative-first event patterns are not general precedents for safe confirmations.

## Chaos source handling

```

Before `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-events\SKILL.md`, lines 562-568:

```markdown
Partition recorded-owner and physical-holder accounting by the state disposition so each amount is debited and credited once even when both pointers identify the same country.
Review matching and stale nonces, distinct and identical owner/holder identities, repeated closure, and dead-actor cleanup along the exact source call chains.

When setup helpers require the recipient country as ROOT, invoke them from a hidden triggered-only country event received by that country; regular event targets carry through events fired by the originating effect chain.
Give a dormant tag owned land and a valid capital before entering capital-based setup or spawning units; use runtime meta construction when its TAG scope must be deferred until activation.
For a player-transfer bootstrap, queue the delayed recipient event before `change_tag_from` and make player transfer the final effect in that country block, so receiver scheduling does not reuse an invalidated country scope.
Inject file-scoped duration constants as meta arguments when generating a new script buffer, rather than leaving an unresolved `@` token inside generated text.
```
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-decisions-missions\SKILL.md`: before SHA-256 `60FE85F29AD547B84153F0D7288D8FBEF9CE9CA2241A5FC80E0FA0BED3F04EF9`, after SHA-256 `ec159cc0f9e76a2f7948d18b22f8ce9776b0b8c7d84eb34fe1b8d94e931bdbfe`.

Before `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-decisions-missions\SKILL.md`, lines 246-252:

```markdown

When accepted design requires emergency resolution to remain available while every other recovery is unaffordable, do not gate it on full nominal reserves. Bound each actual fee by its nominal fee and the nonnegative current reserve, show the actual quote with matching texticons, and recompute all fees together before any debit, then charge that coherent quote once. Avoid hidden partial payments and threshold fee-waiver cliffs. For variable-fee emergency actions, use an `ai_hint_pp_cost` matching the actual quote only if that input form is verified as supported, otherwise omit the fixed nominal hint so a zero quote remains available to AI at zero political power. Never assume `ai_hint_pp_cost` accepts dynamic values. Verify exact numeric reader tokens in installed dynamic-variable documentation rather than assuming a display or stat name: `has_political_power`, `has_stability`, and `has_war_support` are documented readers, while raw `war_support` is not a documented built-in reader. This does not forbid a custom normal variable named `war_support`. Make final resolution and cleanup idempotent with a closed-state guard, and require queued work and late timed callbacks to match the active context before invoking cleanup. Preserve earned finite aftermath until its intended expiry and retain achievement receipts when removing active-crisis state.

### Refundable native political-power credit receipts

For refundable native political-power decisions using the sale price table, read the [receipt API contract](../../../common/scripted_effects/026_black_friday_simple_cost_api.md#refundable-native-political-power-decisions) and its [production helpers](../../../common/scripted_effects/026_black_friday_effects.txt).
Keep the exact paid quote in an owner normal variable for currency refunds; achievement credit is a separate receipt and must never be inferred from the price or sale activity.
```

Exact owned skill patch:

```diff
--- a/.agents/skills/chaos-redux-events/SKILL.md
+++ b/.agents/skills/chaos-redux-events/SKILL.md
@@ -209,7 +209,15 @@
 Keep the option-availability guard separate from a click-time effect guard that rechecks permission, the current request and context against the immutable pending receipt before applying consequences.
 Duplicate requests must not overwrite that receipt.
 Treat controller changes or loss of authority as no consent.
 Existing affirmative-first event patterns are not general precedents for safe confirmations.
+
+### Proposal popup lifecycle
+
+Keep a visible human popup's carrier pointer, family, proposal sequence, and carrier/recipient generation snapshots immutable through proposal withdrawal.
+Invalidate the live proposal separately, retain the shown-popup lock, and serialize replacement delivery until the old event's `after` has closed its snapshot.
+Every reply effect must revalidate the snapshot against the current proposal before mutation, even if its option was visible when the event fired.
+A stale close option must remain usable and describe closing the old prompt without promising to accept, refuse, or change another proposal.
+Treat `timeout_days` as execution of the guarded first option, followed by normal `after` closure, rather than a special timeout branch (offline Event modding, lines 184-186).
 
 ## Chaos source handling
 
@@ -562,7 +570,10 @@
 Partition recorded-owner and physical-holder accounting by the state disposition so each amount is debited and credited once even when both pointers identify the same country.
 Review matching and stale nonces, distinct and identical owner/holder identities, repeated closure, and dead-actor cleanup along the exact source call chains.
 
 When setup helpers require the recipient country as ROOT, invoke them from a hidden triggered-only country event received by that country; regular event targets carry through events fired by the originating effect chain.
+Apply this ROOT contract to country scopes entered by `for_each_scope_loop` or debug dispatch as well.
+Country-owned helpers need an explicit actor input contract or a generation-bound `country_event` relay rooted in the actual recipient.
+Revalidate the saved recipient and generation before dispatching the helper, and cover direct actor entry and foreign-root debug/iterator entry separately.
 Give a dormant tag owned land and a valid capital before entering capital-based setup or spawning units; use runtime meta construction when its TAG scope must be deferred until activation.
 For a player-transfer bootstrap, queue the delayed recipient event before `change_tag_from` and make player transfer the final effect in that country block, so receiver scheduling does not reuse an invalidated country scope.
 Inject file-scoped duration constants as meta arguments when generating a new script buffer, rather than leaving an unresolved `@` token inside generated text.

--- a/.agents/skills/chaos-redux-decisions-missions/SKILL.md
+++ b/.agents/skills/chaos-redux-decisions-missions/SKILL.md
@@ -246,7 +246,18 @@
 
 When accepted design requires emergency resolution to remain available while every other recovery is unaffordable, do not gate it on full nominal reserves. Bound each actual fee by its nominal fee and the nonnegative current reserve, show the actual quote with matching texticons, and recompute all fees together before any debit, then charge that coherent quote once. Avoid hidden partial payments and threshold fee-waiver cliffs. For variable-fee emergency actions, use an `ai_hint_pp_cost` matching the actual quote only if that input form is verified as supported, otherwise omit the fixed nominal hint so a zero quote remains available to AI at zero political power. Never assume `ai_hint_pp_cost` accepts dynamic values. Verify exact numeric reader tokens in installed dynamic-variable documentation rather than assuming a display or stat name: `has_political_power`, `has_stability`, and `has_war_support` are documented readers, while raw `war_support` is not a documented built-in reader. This does not forbid a custom normal variable named `war_support`. Make final resolution and cleanup idempotent with a closed-state guard, and require queued work and late timed callbacks to match the active context before invoking cleanup. Preserve earned finite aftermath until its intended expiry and retain achievement receipts when removing active-crisis state.
 
+### Paid timed-decision entry and expiry
+
+For a `days_remove` decision, selection must pass the full quote, including free factories committed by its native `civilian_factory_use` modifier.
+At `complete_effect` entry, recheck live requirements and spendable reserves without counting that project's own native factory reservation twice.
+Limit that factory exception to the exact native-reserved path, retaining full affordability checks elsewhere.
+Reject duplicate starts and publish the actor/family/generation-bound active receipt before the custom debit, then charge once.
+At `remove_effect` expiry, require exact current paid-project proof and continuing finish requirements without rerunning the purchase quote or slot-open start gate.
+Publish the success receipt before clearing active proof so cancellation cannot mistake successful closure for receipt loss.
+Cover exact-quote selection, reservation-before-entry, duplicate start, depleted reserves after payment, stale generation, and successful expiry in source cases.
+Source ordering models do not prove native reservation or callback ordering.
+
 ### Refundable native political-power credit receipts
 
 For refundable native political-power decisions using the sale price table, read the [receipt API contract](../../../common/scripted_effects/026_black_friday_simple_cost_api.md#refundable-native-political-power-decisions) and its [production helpers](../../../common/scripted_effects/026_black_friday_effects.txt).
 Keep the exact paid quote in an owner normal variable for currency refunds; achievement credit is a separate receipt and must never be inferred from the price or sale activity.
```

## Validation, uncertainty and parent handoff

Both skills passed the skill-creator validator. The decisions validator was run with Python UTF-8 mode after the default Windows text decoder could not read its existing Unicode prose.
Removing only the added lines reproduced both pre-edit SHA-256 hashes exactly, proving that existing shared bytes were preserved.
Reviewed all additions against existing coverage and the cited follow-ups, including fire-time visibility versus reply-time guards.
All three insertions are generic and contain no event IDs, country names, event-specific history, routing changes, or new assets.
Source-case guidance covers exact factory capacity, reservation-before-entry, duplicate debit protection, depleted post-payment reserves, stale generation, and expiry after a project owns its slot.
Native factory reservation/callback ordering and popup coexistence are not established by this maintenance pass. The skill retains those evidence limits.
No implementation simplification or fallback was introduced. No requested skill work is blocked.
Parent review and commit remain outstanding by instruction. Stage only the three owned additions and this handoff.
