# Event 006 northern/western Europe advisor dossier prompts

Generation mode: official built-in ImageGen (`imagegen` skill), one independent generation per fictional advisor master.

Reference inputs for every generation:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/ire_eamon_de_valera.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png`

The reference portraits are style and framing references only. Every depicted specialist is fictional and must be visually distinct. ImageGen produces a full portrait master without an advisor frame. A separate explicit head-and-shoulders crop is later passed through `.tools/process_hoi4_portrait.py advisor`, which composes the final `65x67` dossier card.

## Shared prompt contract

```text
Use case: stylized-concept
Asset type: fictional Hearts of Iron IV advisor portrait master for a later independent 65x67 dossier-card crop
Input images: Images 1-3 are style and framing references only for a subdued vanilla HOI4 painted portrait finish; do not copy their identities, clothing, or facial features.
Style/medium: restrained 1936-1945 grand-strategy painted portrait; realistic anatomy; muted oil-and-gouache finish; fine but economical brushwork; lightly aged print texture; subdued saturation and contrast; natural facial asymmetry; period-authentic civilian clothing.
Composition/framing: one fictional person only; vertical head-and-shoulders portrait with upper chest and both shoulders visible; face fully visible and centered; restrained three-quarter or near-front gaze; generous margin around the head; quiet painted institutional interior with no readable detail. This is the portrait master only, not the finished advisor card.
Lighting/mood: soft diffused window light; sober, competent, understated institutional mood.
Constraints: disclosed fictional character; original face; clear silhouette and readable eyes at very small size; no real-person likeness; no text or typography; no labels; no signatures; no watermark; no logo; no dossier paper; no bevelled card; no border or UI frame; no flag; no medals; no propaganda pose; no modern object; no cinematic color grade; no glossy concept-art finish; no photographic finish; no exaggerated caricature.
```

## Independent advisor briefs

### `advisor_RHI_independence_wave_municipal_customs_administrator`

- Apparent gender presentation: male-presenting.
- Character brief: late-50s Rhineland municipal and customs administrator; narrow face, receding dark-grey hair, tidy moustache, round wire spectacles, charcoal three-piece civil-service suit, muted burgundy tie, reserved and exacting expression.
- Backdrop cue: softly suggested customs ledger office, without visible writing.

### `advisor_RHI_independence_wave_rail_works_liaison`

- Apparent gender presentation: female-presenting.
- Character brief: early-40s Rhineland rail-and-public-works liaison; broad cheekbones, dark auburn hair pinned in a practical low roll, no spectacles, dark bottle-green service jacket over a cream blouse, alert and pragmatic expression.
- Backdrop cue: subdued rail works office with only indistinct structural shapes.

### `advisor_RHI_independence_wave_river_defense_planner`

- Apparent gender presentation: male-presenting.
- Character brief: late-40s Rhineland river-defense planner and civil engineer; square jaw, cropped sandy-grey hair, clean-shaven, weathered face, dark brown technical coat over shirt and tie, calm calculating gaze.
- Backdrop cue: muted river engineering office, without maps, labels, or legible plans.

### `advisor_BAY_independence_wave_district_finance_administrator`

- Apparent gender presentation: female-presenting.
- Character brief: early-50s Bavarian district finance administrator; oval face, silver-streaked brown hair in a neat side-parted bun, small rectangular spectacles, deep navy tailored jacket, composed and fiscally severe expression.
- Backdrop cue: dim district treasury office with indistinct shelves.

### `advisor_BAY_independence_wave_estates_constitutional_liaison`

- Apparent gender presentation: male-presenting.
- Character brief: early-60s Bavarian estates and constitutional liaison; high forehead, swept-back silver hair, clean-shaven, pince-nez spectacles, conservative black frock-style civilian coat and muted tie, courteous jurist's expression.
- Backdrop cue: quiet parliamentary antechamber with no emblems or writing.

### `advisor_BAY_independence_wave_alpine_supply_inspector`

- Apparent gender presentation: female-presenting.
- Character brief: mid-40s Bavarian alpine supply inspector; sturdy face, sun-reddened cheeks, short wavy chestnut hair tucked behind the ears, no spectacles, practical grey-brown wool field coat with no insignia, direct and unsentimental gaze.
- Backdrop cue: shadowed mountain depot interior, no labels or signs.

### `advisor_SCO_independence_wave_shipping_authority_commissioner`

- Apparent gender presentation: male-presenting.
- Character brief: mid-50s Scottish shipping authority commissioner; long weathered face, salt-and-pepper hair, close-trimmed moustache, heavy charcoal tweed suit and dark tie, steady maritime administrator's gaze.
- Backdrop cue: subdued port authority office with indistinct window light, no ships' names or signage.

### `advisor_SCO_independence_wave_industrial_reconstruction_secretary`

- Apparent gender presentation: female-presenting.
- Character brief: late-30s Scottish industrial reconstruction secretary; pale freckled complexion, strong jaw, dark copper hair in a compact waved bob, no spectacles, sober brown wool jacket and pale blouse, focused and quietly forceful expression.
- Backdrop cue: muted reconstruction office with vague factory-window geometry only.

### `advisor_SCO_independence_wave_territorial_defense_planner`

- Apparent gender presentation: male-presenting.
- Character brief: early-40s Scottish territorial defense planner; lean angular face, black hair with an early grey streak, clean-shaven, restrained olive-grey civilian field jacket over shirt and tie with no insignia, watchful analytical expression.
- Backdrop cue: dark planning room without maps, markings, or weapons.

### `advisor_WLS_independence_wave_bilingual_civil_service_commissioner`

- Apparent gender presentation: female-presenting.
- Character brief: early-50s Welsh bilingual civil-service commissioner; warm medium complexion, softly lined face, black hair braided into a low crown, oval spectacles, dark maroon tailored jacket and cream blouse, patient but authoritative expression.
- Backdrop cue: restrained civic office with blank paper shapes only and no visible writing.

### `advisor_WLS_independence_wave_coal_rail_organizer`

- Apparent gender presentation: male-presenting.
- Character brief: mid-40s Welsh coal-and-rail organizer; broad working face, coal-dark wavy hair, clean-shaven, faint grime and weathering without caricature, worn dark blue workman's jacket over collared shirt, determined practical expression.
- Backdrop cue: subdued railway workshop interior with no signage.

### `advisor_WLS_independence_wave_mountain_defense_planner`

- Apparent gender presentation: female-presenting.
- Character brief: late-30s Welsh mountain-defense planner; narrow alert face, short dark curly hair, no spectacles, robust charcoal wool service coat with no insignia over a high-collared blouse, calm field-planner's gaze.
- Backdrop cue: quiet upland operations office, no maps, labels, or weapons.
