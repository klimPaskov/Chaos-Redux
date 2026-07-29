# Event 020 two-tag country audit handoff

## Acceptance result

The current package contains exactly two country tags: reusable Rat Nation carrier `RTA` and separate Rat King `RTX`.

## Patches

- `common/script_constants/020_black_plague_rat_constants.txt:49` sets `minimum_rat_nations_for_king = 1`. Obsolete multi-slot spawn constants were removed.
- `common/scripted_effects/020_black_plague_scenario_effects.txt:253` fixes the Evolution III actor target to `event_target:black_plague_rat_selected_country`.
- `common/scripted_effects/020_black_plague_rat_effects.txt:817-824` retires the selected RTA source during King transfer and removes the incorrect slot-release flag assignment from RTX.
- `common/scripted_effects/020_black_plague_evolution_effects.txt:47-64` prefers the rat actor target for Evolution III and IV logging.
- Older multi-carrier handoffs were marked superseded, and the prior alias handoff now describes the two-tag package.

## Audit coverage

- `common/country_tags/020_black_plague_rat_countries.txt` contains only RTA and RTX.
- Only `history/countries/RTA - Rat Nation.txt` and `history/countries/RTX - Rat King.txt` remain, both using `020_black_plague_rat_1936`.
- Both tags have normal, medium, and small flags; country localisation, parties, leaders, AI allow-lists, focus loaders, and custom units resolve.
- Runtime slot selection allocates only RTA; King and scenario paths target only RTX.
- Shared special-country and non-human classifiers include both current package flags.
- SCN-012 remains one-shot through its launch guard and clears the scoped bootstrap flag.

## Remaining risks

- Dormant country history uses runtime-owned state transfer with `capital = 1` and no static owner.
- Research, conventional production, and normal recruitment remain intentionally disabled.
- RTA cleanup after King transfer depends on valid adjacency and subsequent pulses.
- Timed-flag duration variables in parent-owned runtime still need separate review.
- No Technology Tree Viewer is exposed by the installed MCP package.

No new country identity, focus route, unit family, or asset family was added in this correction.
