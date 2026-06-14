# Achievement Prompt: Event 008 Tensions Rising

Implement and/or prepare achievement design for Event 008 `Tensions Rising`.

Read:

- Event 008 specs under `docs/specs/008_tensions_rising_specs/`
- `matrices/008_tensions_rising_cluster_and_achievements.md`
- existing Chaos Redux achievement implementation patterns
- `chaos-redux-event-assets` for achievement icon workflow

Do not make achievements unlock just because Event 8 fires once. These achievements must reward rare timing, restraint, deep-stage consequences, and hidden-system observation.

## Achievements

### `achievement_tensions_thin_wire`  -  The Thin Wire

- Visible.
- Any player country.
- Unlock after Event 8 reaches Stage III or IV, then the player remains at peace for 180 days while global world tension is 100%.
- Disqualify if the player enters a war during the window.
- Icon: taut telegraph wire over dark map.

### `achievement_tensions_only_headlines`  -  Only Headlines

- Hidden.
- Any player country.
- Unlock after three Stage II+ Event 8 firings occur while the world has no active wars.
- Disqualify if any active war begins before the third qualifying firing.
- Icon: stacked newspapers under silent clock, no readable text.

### `achievement_tensions_insurance_market`  -  The Insurance Market Knows

- Visible.
- Any country with convoy/trade relevance.
- Unlock when the `Insurance Rates Jump in Neutral Ports` follow-up fires while the player has a meaningful convoy pool and is not at war.
- Icon: marine insurance ledger and ship silhouette, no text.

### `achievement_tensions_one_denial`  -  One Denial Too Many

- Hidden.
- Any player country.
- Unlock when a recently affected Event 8 relation actor enters a war relation within 120 days after Event 8 applies relation damage. Use the existing war-relation on-action; Event 8 must not create the war.
- Avoid false positives from unrelated old history.
- Icon: denied stamp motif over sealed cable, no readable text.

### `achievement_tensions_blackout`  -  Diplomatic Blackout

- Visible.
- Any player country.
- Unlock when ten distinct Event 8 timed opinion modifiers are active globally at once.
- Icon: blacked-out embassy facade with ten lit windows.

## Tracking notes

- Add flags/variables for Stage III/IV reached, relation-damage window, no-war windows, and active opinion modifier count as needed.
- If the achievement framework requires player-owned flags, mirror relevant global state into eligible player scope safely.
- Asset work must produce 64x64 completed icons and any grey/not-eligible variants required by current patterns.
- Update localisation and docs in the same implementation pass.
