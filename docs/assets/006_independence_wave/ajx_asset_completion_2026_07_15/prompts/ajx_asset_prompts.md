# Event 006 AJX advisor and neutral-commission focus prompts

Generation date: `2026-07-15`

Generation mode: official built-in ImageGen (`$imagegen`), one independent
generation per source master. All depicted people are fictional.

## Advisor reference inputs

The three canonical vanilla leader portraits below were style and framing
references only. Their identities, clothing, facial features, and backgrounds
were not copied.

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/ire_eamon_de_valera.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png`

## Shared advisor prompt contract

```text
Use case: stylized-concept
Asset type: fictional Hearts of Iron IV advisor portrait master for a later independent 65x67 dossier-card crop
Input images: Images 1-3 are canonical vanilla HOI4 style and framing references only. Do not copy their identities, clothing, facial features, props, or backgrounds.
Style/medium: restrained 1936-1945 grand-strategy painted portrait; realistic anatomy; muted oil-and-gouache finish; fine economical brushwork; lightly aged print texture; subdued saturation and controlled contrast; natural facial asymmetry; period-authentic civilian clothing.
Composition/framing: one person only; vertical head-and-shoulders portrait with upper chest and both shoulders fully visible; face centered and fully visible; restrained near-front or three-quarter gaze; generous margin around head and shoulders. This is the portrait master only, not the advisor dossier card.
Lighting/mood: soft diffused period office or industrial-window light; sober, capable, understated institutional mood.
Constraints: disclosed fictional original person; readable eyes and silhouette at very small size; no real-person likeness; no text; no typography; no signature; no watermark; no UI frame; no dossier paper; no border; no flag; no medals; no uniform insignia; no propaganda pose; no weapon; no cinematic color grade; no glossy concept-art finish; no photographic finish; no caricature.
```

## Independent advisor briefs

### `advisor_AJX_independence_wave_mine_rail_dispatch_superintendent`

- ImageGen handle: `exec-1f9d8f33-1677-45f2-864b-073da1149acc`.
- Apparent gender presentation: female-presenting.
- Primary request: one original fictional female Saar mine-and-rail dispatch
  superintendent from the late 1930s.
- Character brief: early 40s; long narrow face with a strong chin and slightly
  asymmetrical brows; ash-blond hair in short practical finger waves tucked
  behind the ears; pale weathered complexion; no spectacles; slate-grey 1930s
  dispatch-office jacket over a muted rust blouse; alert, precise, unsentimental
  expression. She is a civilian rail-and-colliery logistics specialist.
- Backdrop cue: quiet Saar dispatch office with indistinct switchboard and
  rail-window geometry, without readable writing, signs, maps, flags, or logos.

### `advisor_AJX_independence_wave_cross_border_accounts_comptroller`

- ImageGen handle: `exec-e372cf51-25fd-4947-ac88-b85bc7426952`.
- Apparent gender presentation: male-presenting.
- Primary request: one original fictional male Saar cross-border accounts
  comptroller from the late 1930s.
- Character brief: late 50s; tall gaunt face, prominent slightly crooked nose,
  deep-set dark eyes, receding iron-grey hair combed back, narrow
  salt-and-pepper moustache, thin half-rim spectacles; dark charcoal
  double-breasted civilian suit, cream shirt, muted blue-grey tie; cautious,
  exacting, quietly skeptical expression.
- Backdrop cue: dim ledger office with indistinct shelves and a frosted window,
  without readable writing, numbers, stamps, maps, flags, or logos.

### `advisor_AJX_independence_wave_factory_security_inspector`

- ImageGen handle: `exec-7faebefc-e93b-4332-8c98-54e0f23d77cc`.
- Apparent gender presentation: female-presenting.
- Primary request: one original fictional female Saar factory-security
  inspector from the late 1930s.
- Character brief: mid-40s; broad square face, high cheekbones, olive-fair Saar
  complexion, dark brown hair parted sharply and gathered in a low practical
  bun, one faint healed line through the left eyebrow, no spectacles; sturdy
  brown herringbone civilian inspector's coat over a high-collared cream
  blouse; calm, unflinching, observant expression. She is a civilian auditor
  who subordinates private factory guards to municipal authority.
- Backdrop cue: subdued factory inspection office with indistinct steel window
  frames and shadowed filing cabinets, without writing, signs, flags, weapons,
  or logos.

## Neutral-commission focus icon

Reference inputs:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/focus_generic_nuclear_development.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/focus_aus_reestablish_austrian_navy.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/focus_eth_expand_the_levy.png`

ImageGen handle: `exec-a5622973-69a8-4cbc-9670-fa81a62e80f2`.

```text
Use case: stylized-concept
Asset type: original Hearts of Iron IV national-focus icon master for Event 006 Saar Municipal Neutral Commission
Primary request: Design one distinct civilian municipal-neutrality focus icon for the Saar, suitable for the stable sprite GFX_goal_independence_wave_ajx_neutral_commission.
Input images: Images 1-3 are canonical vanilla HOI4 national-focus style, rendering, silhouette, and scale references only. Do not copy their symbols or arrangements.
Subject: a strong central aged-silver balance scale set in front of a compact dark-stone civic hall pediment; the two scale pans level and linked by one brass crossbar; behind them a restrained half-wreath combining dark laurel leaves with small black coal facets and a thin steel rail arc; one small enamel shield beneath the scales divided into muted Saar blue, white, and red fields with no emblem and no text. The composition must read as civilian municipal commission, negotiated neutrality, coal-and-rail administration, and balanced authority, not monarchy or military command.
Style/medium: authentic vanilla Hearts of Iron IV focus-tree icon; painterly aged metal and enamel, crisp dark outline, subtle depth, compact heraldic composition, period 1930s visual language, strong value separation, restrained weathering, no modern flat-vector or glossy mobile-game finish.
Composition/framing: one centered emblem on a transparent-ready canvas; broad readable silhouette; all important details clear at 94x86; generous empty padding; no element touches the canvas edge.
Background-removal contract: place the entire emblem on a perfectly flat solid #00ff00 chroma-key background. The background must be uniform with no shadows, gradients, texture, reflections, floor plane, vignette, or lighting variation. Do not use #00ff00 in the emblem. No cast shadow or reflection on the green field.
Constraints: no words, letters, numbers, generated writing, signature, watermark, map, flag fabric, person, face, weapon, eagle, crown, swastika, military insignia, propaganda poster, circular medallion fill, opaque square panel, fake checkerboard, white sticker border, white halo, glow, excessive tiny detail, or modern UI.
```

The raw master was alpha-processed with the official ImageGen chroma-removal
helper before the visible-alpha bounds were mechanically cropped, resized to
`88x82`, and centered at `(3, 2)` on the existing Event 006 `94x86` focus
canvas. No visible symbol or frame was drawn locally.
