# Event 006 decision surface audit and narrow patch handoff

Date: 2026-08-22

Scope: Event 006 decision categories, missions, admitted package decisions, costs, tooltips, AI route guards, cleanup, and lifecycle reachability after pre-event crisis retirement and compact cost fixes.

Disposition: PARTIAL with two narrow source-backed fixes applied. The surface remains HOLD for broad category redesign, cost-family reduction, dynamic mission commitment presentation, and package promotion.

## Changed files and identifiers

- `common/decisions/categories/006_independence_wave_categories.txt`: `independence_wave_founding_category` now has `visible_when_empty = yes`.
- `common/decisions/006_independence_wave_karelia_crimea_decisions.txt`: `independence_wave_kar_codify_durable_sovereignty` and `independence_wave_cri_codify_durable_sovereignty` now expose completion effect tooltips.
- `localisation/english/006_independence_wave_karelia_crimea_l_english.yml`: added `independence_wave_kar_durable_sovereignty_effect_tt` and `independence_wave_cri_durable_sovereignty_effect_tt`.
- `common/decisions/006_independence_wave_transcaucasus_decisions.txt`: seven admitted FORM-16 actions now expose completion effect tooltips: `independence_wave_form16_confirm_yerevan_capital`, `independence_wave_form16_confirm_tbilisi_capital`, `independence_wave_form16_confirm_baku_capital`, `independence_wave_form16_convene_language_commission`, `independence_wave_form16_unify_transcaucasian_rail_command`, `independence_wave_form16_settle_baku_oil_revenue`, and `independence_wave_form16_standardize_federal_army`.
- `localisation/english/006_independence_wave_transcaucasus_l_english.yml`: added the seven matching `_effect_tt` keys.

## Before and after behavior

Before the category patch, the active founding category could disappear while automatic mission `independence_wave_secure_provisional_capital` was still pending because its lifecycle uses `activation` and `available = { always = no }`, leaving no visible action in the category. After the patch, `independence_wave_founding_category` remains visible only when `is_independence_wave_active_country = yes`, including the empty pre-DM-01 interval. This makes the accepted Event 006 status scripted GUI reachable after release without exposing any pre-event category.

Before the tooltip patch, the nine admitted package actions above spent resources or changed state without a custom completion effect summary. After the patch, each action presents a concise outcome statement while preserving its existing payment, trigger, AI, one-shot, route, and cleanup behavior.

## Decision category lifecycle notes

The founding category is active-country gated and now visible while empty so Phase A status remains reachable. The automatic DM-01 starter remains intentionally non-selectable and starts through the existing helper. DM-02 and DM-03 retain their accepted activation and cancellation gates. Government, recognition, security, host, patron, network, league, border, high-chaos, and formable categories retain their existing phase and package gates.

The formables category was not given `visible_when_empty`. Its ordinary discovery decision is family-selected and unlock-gated, so exposing an empty formables surface would add a new scan target without improving reachability. No new category or GUI was created.

## Cognitive-load notes

The active status GUI presents the five Event 006 ledgers as a compact state surface. The founding header repeats those ledgers in localisation, and government text repeats some of them. This duplication is a future presentation cleanup item, but changing it would require a broader localisation and GUI contract.

The structural scan found 87 Event 006 categories and 782 action blocks. Fifty-six categories contain more than six action blocks and 37 contain more than ten, with a maximum of 23. This is a source-density signal only because no runtime scenario evidence proves simultaneous visibility of all those actions. Broad phasing or category consolidation remains out of scope.

DM-01 dynamically commits capital, garrison, equipment, supply, and transport inputs, but the exact material quantities are not disclosed before activation. A safe fix would require a dynamic status/localisation helper that stays synchronized with payment and cancellation logic, so it remains queued rather than patched here.

## Mission quality notes

`independence_wave_secure_provisional_capital` (DM-01) is owned by the active country and the founding category. It requires the capital, garrison, equipment, supply, and transport commitment and uses the accepted dynamic 30 to 75 day duration band. Timeout is success, while cancellation from inactivity, capital loss, or relocation is failure. Its one-shot and helper duplicate guards remain intact.

`independence_wave_establish_revenue_service` (DM-02) follows DM-01 and retains its capital and administration requirements, founding duration, salary-crisis timeout result, inactive cancellation, and one-shot guard.

`independence_wave_register_population` (DM-03) is intentionally automatic with `available = { always = no }`; it is not a missing reveal. It follows DM-02, checks light administration affordability, resolves on timeout according to affordability, cancels on inactivity, capital loss, or severe instability, and remains fire-once guarded.

FORM-16 actions are one-shot package decisions rather than missions. Their member-state, territory, formation, anchor, and congress gates remain unchanged. The new effect tooltips describe the state mutation without changing reachability.

## Cost and requirement clarity

The admitted custom cost crosswalk has matching base and blocked localisation keys after the patch. The only missing blocked keys found are for unadmitted IW-057 Far Eastern package costs, so they were intentionally left fail-closed and untouched. FORM-16 cost strings use the correct `£command_power` and `£pol_power` texticons.

Several shared and package cost families still exceed the four spendable-type limit. Strategic and strategic-major costs combine stability, war support, command power, transport, and civilian factories. Security standard-factory costs combine manpower, army experience, civilian factories, infantry equipment, and support equipment. Border ultimatum, integration, breakaway, reclamation, Pacific, and other package families also need coordinated payment, trigger, effect, AI, balance, and localisation changes. Localisation-only shortening would misrepresent the actual spend and was not applied.

## AI validity and route locks

No AI weights or probability-bearing logic were changed. The FORM-16 contract audit confirms admitted ARM, GEO, and AZR carriers with exact member states 230, 231, and 229, including consent, refusal, mutation, rollback, cleanup, and readiness. Existing Karelia and Crimea route guards remain unchanged. The custom `chaosx_ai_probability_auditor` route was unavailable in this run, so no probability compare is claimed. Existing structural probability artifacts are recorded below for parent review.

## Localisation and tooltip gaps

The nine admitted actions listed above were the remaining admitted decision blocks found without a custom completion effect or trigger tooltip. They now have matching keys in UTF-8 BOM localisation files. The new strings are outcome summaries and do not duplicate cost labels. Long category descriptions, raw ledger dumps, and some package-local cost prose remain unresolved because they require a wider player-facing presentation pass.

## Cleanup and exploit-risk notes

The patch adds only presentation metadata and completion descriptions. Existing one-shot flags, active-project locks, route flags, event targets, cancellation cleanup, and DM-01 duplicate guards remain unchanged. No payment, refund, war-goal, core, unit, equipment, target, cooldown, or AI exploit surface was introduced.

## MCP evidence and skipped validation

Existing read-only GUI artifacts used for the audit:

- Status inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6ff50e75abd1c602d184d5715f78167147c922e2d605a2f28a2558cdcc9a88b3/aafdeaf4bb1e7d4e40833d5f4a12e58841b7958d90bd45ed6770f3747bf056e7/gui-inspect.4810e6db3b628432.json`.
- Formable inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ceafdfe54ac57cf49c962864588a9be5d62be188d0f3d2d063791d49a9938a6/2f9080649970dab4b93f36cd4f3462ca13835d48fd625f6c223d8a44b265e112/gui-inspect.29dc700b4e152a05.json`.
- Status render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7d245b460614d138be4d724b8fbbe4c0c3ae510648ae12c90abf3733e231c13/d338d48ff29e92e22f3f8fa051291bb47280836c5a57b0656e32e5c8ba167b57/independence_wave_status_window-full.svg`.
- Formable render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0d6628e50f989b4c7b7264b970286e228543cf35b7af4a53813387d4ae62f51/abf65cf55a81b66e84031c62641df89489aedf0eca5985865128a2f8ce792e09/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

Fresh mandatory `hoi4.gui_inspect` and `hoi4.gui_render` calls for the status and formable windows each timed out at 180 seconds. No `hoi4.gui_rewrite` was used because no GUI layout patch was in scope and fresh engine evidence was unavailable. The earlier artifacts report validation false and global diagnostics, so they are evidence of existing structural issues rather than clean engine proof.

The custom probability-auditor route was unavailable, so no AI balance compare was run. The parent should treat the decision surface as partially validated until those routes are available.

Task-specific checks completed:

- `python .tools/audit_event6_form16.py` passed the admitted ARM, GEO, and AZR FORM-16 contract.
- `python .tools/audit_event6_allocator.py` passed the current admitted-package boundary, adapter inventory, witness set, ladder, and retired pre-event crisis checks.
- A static admitted-decision scan found no admitted decision block lacking a custom effect or trigger tooltip after the patch.
- Localisation references resolved and both changed localisation files retained UTF-8 BOM encoding.

## Remaining issues and recommended follow-up

1. Keep the active founding category `visible_when_empty` change and verify its post-release reachability in a live consumer save. It preserves the pre-event gate because the category remains active-country gated.
2. Route a dedicated cost-family pass through the decision owner and probability auditor. Reduce or restructure over-four-type costs only with synchronized payment, available, effect, AI, and localisation changes.
3. Route the DM-01 material commitment disclosure to the existing Event 006 status GUI owner. Do not duplicate or approximate the dynamic payment calculation in localisation.
4. Re-run GUI inspect/render once the MCP timeout is resolved and compare status/formable states. Do not treat the existing global diagnostics as resolved by this patch.
5. Keep unadmitted package IDs and missing FER blocked strings fail-closed. Do not promote or expose them from this decision-surface pass.

## Structural probability artifact references

- Shared decision inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6aa085cc53ef56d4be8f2bb3084ec9268f576c904b2b1d1c8be2108256bd099d/9466001b873678b3f052ea65934b854bf07c56f8b7eecae106dc3b099ee1e5de/probability-inspect-35b229abc47d.json`.
- Komi mission inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95dadfabd3ec21015b5a4716e0d965e2aa3bd5bb2a3bf8b62e9a46f83442eea7/b0436a19d9530441087195c38510ae78c4fd2211a602383c4ed80aacadb7251d/probability-inspect-e5f696ef78fd.json`.
- Pacific discovery inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/377003b4b52b91c205993740f302e64dc29c46d46cc0ebe1e83f560ba71acb57/c25b9911da431881170f282a02b817a7b329b6c7d77f7182317e7d4193d709cb/probability-inspect-53f86f4d0544.json`.

No unrelated fallout file was changed by this handoff or included in the intended patch. Parent review should separate the five files above from any other dirty worktree paths.
