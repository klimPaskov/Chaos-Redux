# Protective Aid startup dispatch repair

Disposition: implemented source repair, with the next live startup result pending.
Acceptance basis: the user supplied the live startup error for `common/scripted_effects/026_black_friday_effects.txt:4136` and instructed that it be fixed first.

`black_friday_quote_cbrn_external_aid_pp_fee` is a scripted trigger in `common/scripted_triggers/026_black_friday_triggers.txt`.
Its direct invocation from an effect block produced the reported unknown-effect error.
`black_friday_pay_cbrn_external_aid_pp_fee` invokes `black_friday_can_pay_cbrn_external_aid_pp_fee` inside its payment `limit` instead.
That predicate calls the quotation trigger, refreshes the fee and validity scratch values, and checks affordability before the existing target, escrow, debit, and receipt code runs.
No duplicate effect definition or separate quotation formula was introduced.

The current source audit cross-referenced all scripted trigger/effect definitions and checked Event 26 calls outside condition blocks.
It found no remaining trigger-only calls in effect positions in this file.
The fixed fee of 25 quotes to 13 at ratio 5000 and 7 at ratio 2500, with affordability boundaries 12/13/14 and 6/7/8 respectively.
Those arithmetic and source checks do not establish engine payment or startup acceptance.
The normal fee, mask escrow, native factory commitment, delayed settlement, refunds, and achievement ownership retain their existing source contracts.

The relevant custom-cost reference is the offline Decision modding cost section, lines 284–336, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`.
The installed decision scope and refresh reference is `common/decisions/_documentation.md`, lines 1–46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.
The coding agent did not launch HOI4, and the orchestrating live session owns the next startup result.
Event 26 remains default-disabled while its full cost registry and acceptance gates are incomplete.
