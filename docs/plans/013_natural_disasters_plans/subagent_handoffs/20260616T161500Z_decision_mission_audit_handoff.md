# Event 013 Decision/Mission Audit Handoff

Audit surface:
- `common/decisions/013_natural_disasters_decisions.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/scripted_triggers/013_natural_disasters_triggers.txt`
- `localisation/english/013_natural_disasters_l_english.yml`

Result:
- The decision and mission audit found that timed recovery missions could read as satisfied by passive expiry rather than deliberate recovery work.
- The main implementation changed recovery missions to use active mission flags plus matching objective-complete flags set by recovery helpers.
- The audit also identified missing cross-border pressure coverage for the border-camp branch. The main implementation added `natural_disaster_seal_border_camps_against_FROM`, concrete rifle/manpower/stability/war-support cost checks, payment helpers, target pressure effects, AI weights, and localisation.

Follow-up status:
- Recovery missions now complete through explicit recovery objectives.
- Cross-border aid now includes both relief intake and hardened border-camp pressure.
- A final decision/mission audit should re-check the added border-camp decision before completion.
