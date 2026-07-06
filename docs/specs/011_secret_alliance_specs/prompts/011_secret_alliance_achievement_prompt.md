# Follow-Up Achievement Prompt: Event 011 Secret Alliance

Implement Event 011 achievements only after the core event, decisions, reveal, and war outcome tracking exist.

Source package:

- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_4_ai_balance_assets_acceptance.md`

Working hooks:

- `secret_alliance_all_lamps_lit`: reveal every current pact member before Evolution III public reveal
- `secret_alliance_clean_break`: split a founding member without entering war with any pact member first
- `secret_alliance_no_first_shot`: defeat the revealed pact war without escalating a border clash into formal war
- `secret_alliance_iron_curtain_raiser`: win the defensive pact war after reaching readiness and industrial security thresholds
- `secret_alliance_border_sentinel`: win multiple pact border clashes without losing one and without formal war during those clashes
- `secret_alliance_smoke_without_fire`: expose the pact through observers and proof while keeping public awareness below panic

Implementation requirements:

- hidden tracking flags for each hook
- disqualifier flags for first-shot, wrong-war, and reveal-order failures
- event log or details notes only where useful
- achievement icon manifest and final DDS icons
- final localisation in achievement style

Do not mention achievements in ordinary decision or event text.

