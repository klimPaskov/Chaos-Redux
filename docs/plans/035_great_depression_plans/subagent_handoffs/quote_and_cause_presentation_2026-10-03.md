# Event 35 quote and cause presentation

## Disposition and scope

Implemented presentation tranche under the user's requirement for dynamic quoted costs and the current Severity causes.
This tranche contains the two Event 35 scripted-localisation files, English localisation, and the cause-display handoff.
The separate payment, commitment-cleanup, and transaction repairs remain outside this commit until their own integration is finished.

## Presentation contract

All seventeen cost families show one to three compact resource amounts in the decision row, with their complete one to four amounts in the hover tooltip.
Nine resource selectors independently mark an affordable quote yellow and an unavailable quote red.
Both normal and blocked rows use the same selectors, so a shortage of one resource does not imply a shortage of every resource.
Stability and War Support retain two decimal places in percentage quotes.
War Support uses the installed `GFX_war_support_icon` sprite.

The first cause remains compulsory, and the second and third are optional comma-prefixed suffixes.
The opening shock occupies the third slot only when two higher-priority causes are active.
The six report descriptions and the national category description compose these selectors without unconditional commas.

## Evidence and limits

The actual cause selectors were evaluated against all 32 combinations of their five input flags, with no repeated cause or fallback.
The nine resource fragments, eighteen output keys, and all 51 cost-family strings resolve in source.
Every fourth resource remains in its cost tooltip, and every mapped resource texticon resolves to a real sprite.
Reference paths, sections, and hashes are in `cost_contract_repair_2026-10-03.md` and `cause_display_repair_2026-10-03.md`.
The supplied cycle-one live log predates this tranche, so it does not prove its visual rendering.
HOI4 domain requests, including the narrowed source-lookup retry, timed out after 600 seconds.
No native render, executed payment, normalized probability, or full Event 35 completion is claimed.
