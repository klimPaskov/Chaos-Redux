# Lootboxes decision implementation prompt

Read `README.md` for the accepted design scope, open AI tuning values, and confirmed Event 107 identity. Follow the current event and decision owner skills when implementing this handoff.

Read current `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, the six Lootboxes design parts, and the exact existing cost, country, and event-owner helper contracts before editing. Use `docs/specs/shared_identifier_registry.md` for event IDs; the parent owns workbook and status changes.

## Owned actions

The permanent Lootboxes category offers one next gameplay action. With access and no unresolved box, the country may purchase one box for exactly 50 PP. With an unresolved paid box, it may resume that same opening for free. The initial report acknowledgement establishes access once and is not a repeat purchase or a free demonstration box.

Keep the single purchase row through Premium Boxes, Bonus Drops, and Chaos Loot. Premium is an automatic random form selected after the shared evolution owner unlocks it. It is not a second priced product. Ordinary remains possible. The shared thresholds are 200+, 400+, and 600+, while actual enablement, unlock and pacing remain with the evolution owner.

Use the correct PP texticon and one authoritative inclusive price check. Exactly 50 PP passes. A fractional amount below 50 fails. Display, enabled state, custom-cost trigger where used, payment, and actual-paid receipt must all agree. Opening, resumption, result viewing, and closing have zero cost.

The fixed price explicitly overrides discountable or dynamically scaled purchase guidance. Establish the exact Event 107 exception under Black Friday and other active cost sources without modifying discounts for other owners. Do not assume a zero eligibility mask means exempt. Inspect the current framework contract and verify actual native debit.

## Transaction and UI boundary

Pure preflight checks country identity, access, absence of an unresolved or in-flight purchase, exact affordability, and certified useful reward coverage in every rarity. Hover and visibility evaluation do not sample, debit, grant, or change history.

A successful purchase creates one country-owned paid receipt and seals form, rarity, contents, quantities, reward evolution snapshot, provider version, and deterministic delivery policy. It opens the dedicated local chest window. The UI owns five accepted physical stages, while the core resolver owns the one complete reward and one influence increase at completion.

Close and Escape preserve the paid box and accepted stage. The category must resume it with 0 PP if necessary. A second purchase is blocked while one is unresolved. Reopening a completed result reads its receipt only. A rejected input, stale country, duplicate callback, or already-consumed record cannot authorize another reward or refund.

Validate fresh record identity, exact actor, lifecycle phase, actual paid fields, and current consumption proof. Preinitialize every consumed temporary output at each caller boundary. Preserve immutable pending context through nested helpers. A permanent tombstone is not a fresh success receipt.

Normal closing is not cancellation and does not refund payment. A technical invalid-record repair follows Part 1's mutually exclusive completion or compensation contract and cannot refund an already delivered reward.

## AI and scheduling

Give AI the same paid purchase and sealed resolver without a human window. Apply the strategic reserve, ordinary priorities, and bounded opportunity policy from Part 5. Keep price and reward odds identical to a human in the same outcome context. Do not read hidden burden, omen weights, relief timers, or the next reward in purchase willingness.

Use the verified native decision AI route or an existing bounded country-owned callback. Maintain one opportunity and a success cooldown, preserve original due dates through reload, and avoid catch-up bursts. Do not introduce a daily, weekly, or monthly all-country scan. Willingness scores are not exact probabilities.

## Public presentation

Use the separate accepted 32x32 purchase and resumption icon compositions. Keep the category restrained, with no custom influence value, rarity-assistance meter, omen timer, hidden recovery counter, or additional cleansing action. Disabled reasons explain public affordability, an existing paid box, an in-flight transaction, or a stale country context.

Write final localisation from the spec direction. The category's paid-resumption meaning must be clear, but the exact concealed influence and opening-to-omen link remain absent. The initial report and evolution reports follow their own accepted report art and public premise directions.

## Evidence and handoff

Use Part 6 cases LB-T01 through LB-T08, LB-O01 through LB-O12, and LB-A01 through LB-A05, plus the exact fixed-price discount cases. Inspect the actual production helper chain through payment, receipt, sealing, resolution, compensation, AI, cleanup, and load recovery. Do not replace it with a toy gate that mirrors only the implementation expression.

Route read-only numeric checks and weighted AI scenarios to `chaosx_ai_probability_auditor`; do not independently redo the numeric audit or alter weights without parent coordination. Preserve immutable pre-edit source and fixtures only when an accepted weighted change is being compared. Coordinate available GUI evidence with the event UI worker, without taking ownership of layout or shared UI systems. For each newly accepted paid purchase, evaluate the reward-selection path once with fresh randomness before sealing; resumption, reload, opening, retry, and replay never resample. If the sampler runs in the repeatable native purchase decision, use verified `fixed_random_seed = no` in that decision body, as documented by offline Decision modding lines 383–386 and vanilla `common/decisions/FRA.txt`, line 56; the [auditor handoff](../../plans/108_wrestling_tournament_plans/subagent_handoffs/107_108_probability_review_2026-10-10.md) carries the source revision. If the chosen path differs, verify its native RNG behavior before choosing syntax. Include the matched immediate-AI versus delayed-human fixture from Part 6 without adding a timeout or balance rule.

Use MCP only when a live schema is available and the result answers a concrete question. Make one initial read-only call and at most one useful corrected retry; then use local source and installed documentation. Missing optional tools do not block source completion, and source review cannot prove native runtime behavior. Agents do not launch HOI4, request a user-run session, or wait for live evidence.

Return exact changed files and identifiers, before/after behavior, the full action coverage table, quote/gate/debit and persistence evidence, source and scenario identities, skipped checks with reasons, and remaining risks. Keep iterating until every mapped action and boundary is satisfied. Do not call the category complete while a valid paid box can be lost, rerolled, charged again, or resolved twice.
