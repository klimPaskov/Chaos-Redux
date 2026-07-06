# Follow-Up Asset Prompt: Event 011 Secret Alliance

Use `chaos-redux-event-assets` for Event 011 Secret Alliance visual assets. Use `chaos-redux-frame-animation` as well if any animated UI asset is requested.

Source package:

- `docs/specs/011_secret_alliance_specs/`

Asset list:

- opening report image: secret meetings and courier pattern
- Evolution I report image: widening minor-state network
- Evolution II report image: sabotage aftermath
- Evolution III report image: public compact
- reveal super-event image
- decision category icon
- decision icons for investigation, preparation, exposure, negotiation, counter-sabotage, propaganda, and border incidents
- idea icons for suspicion, preparation, sabotage damage, pact pressure, and war readiness
- faction emblem for the Anti-[player country] Pact
- achievement icons for the Event 011 hooks

Style direction:

- period-authentic documentary wartime mood
- fictional, campaign-dynamic pact
- no readable generated text
- no modern intelligence-wall aesthetic
- no generic atmospheric image when the player needs to understand the subject
- avoid real historical meeting photos unless the final implementation explicitly researches and names the source context

Required handoff:

- source files
- processed PNGs
- final DDS files where appropriate
- sprite names and target `.gfx` files
- manifest with sizes, source mode, prompts or source URLs, and remaining risks
- static fallback for every animated asset

Animated assets, if requested:

- sealed dossier pulse
- cipher-line warning
- red frontier warning frame
- broken reveal seal

Animation rules:

- final animation must be a frame sheet wired through HOI4 sprite definitions
- no transform-only final animation
- no GIF-only final asset

