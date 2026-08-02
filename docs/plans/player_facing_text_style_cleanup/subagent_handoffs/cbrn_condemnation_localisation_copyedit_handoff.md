# CBRN and Condemnation Localisation Copyedit Handoff

## Scope

This pass was limited to existing English localisation files whose names begin with `cbrn`, `cbw`, `chemical`, or `condemnation`.

The copyedit removed em dashes, sentence semicolons, rhetorical tradeoff framing, staged public-versus-concealed contrast, and fragmented list prose without changing gameplay meaning.

No mechanics, identifiers, localisation keys, dynamic tokens, formatting codes, numeric values, facts, or operational content were added, removed, or changed.

## Files changed

- `localisation/english/cbrn_chemical_delivery_l_english.yml`
- `localisation/english/cbrn_designers_l_english.yml`
- `localisation/english/cbrn_diplomacy_l_english.yml`
- `localisation/english/cbrn_doctrine_l_english.yml`
- `localisation/english/cbrn_hq_l_english.yml`
- `localisation/english/cbrn_occupation_l_english.yml`
- `localisation/english/cbrn_protection_l_english.yml`
- `localisation/english/condemnation_sanctions_l_english.yml`

## Reviewed without changes

- `localisation/english/cbrn_achievements_l_english.yml`
- `localisation/english/cbrn_battlefield_operations_l_english.yml`

No matching `cbw*` or `chemical*` English localisation filename was present in the assigned directory.

## Reference and validation evidence

The required offline Paradox wiki pages and the vanilla Hearts of Iron IV documentation set were consulted before the localisation files were opened.

Vanilla `localisation/english/decisions_l_english.yml` was consulted as the localisation precedent.

All matching files retain their UTF-8 BOM.

Every localisation key, dynamic bracket token, dollar-delimited substitution, formatting code, icon token, and numeric value matches the pre-edit `HEAD` version.

The assigned file set contains no remaining em dash or semicolon character and no remaining identified rhetorical `but`, `rather than`, official-versus-unofficial staging, or similar thesis-antithesis construction.

Temporal uses of `while` and the fixed modifier label `Organisation Loss While Moving` were retained where they state timing or an engine-facing label rather than rhetorical contrast.

## Simplifications, omissions, and blockers

No simplifications, omissions, fallbacks, or blockers remain within the assigned copyedit scope.

No commit was created because this subagent worked inside a shared dirty worktree and left final integration to the parent agent.
