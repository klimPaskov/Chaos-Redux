# Event 012 Africa Super-Event Missing Roles Text Handoff

Updated: 2026-06-16

Scope:

- Research-only handoff for two still-missing Event 012 Africa super-event roles.
- No gameplay or localisation edits made.
- Existing final-wired slots `68` through `73` in `localisation/english/012_african_union_l_english.yml` were treated as occupied and not reused.

Method:

- Read the bounded Africa super-event prompt, evolutions/world-end spec, existing super-event research note, and current Africa localisation file.
- Verified direct references against traceable sources, preferring Project Gutenberg, Marxists Internet Archive scans/transcripts, and other stable primary or near-primary archives.
- Avoided unsourced quote-site wording.

## 1. `africa_rsa_allies_peace`

Role fit:

- This is not a continental-apotheosis slot. It is a civil-war aftermath slot where the continental side wins inside South Africa and forces an Allied peace.
- The strongest package should sound exhausted, administrative, and irreversible rather than jubilant.

### Recommended package

- Candidate title: `The Continental Settlement`
- Main quote: `Peace hath her victories / No less renowned than War.`
- Quote source: John Milton, `To the Lord General Cromwell`
- Year: 1652
- Source link: https://www.gutenberg.org/files/31706/31706-h/31706-h.htm
- Button / cultural-political remark: `Yet much remains.`
- Button source: same Milton sonnet; the line immediately precedes the selected quote as `And Worcester's laureate wreath: yet much remains / To conquer still`
- Button source link: https://www.gutenberg.org/files/31706/31706-h/31706-h.htm
- Description direction: Pretoria, Johannesburg, the mine-port belt, exhausted congress cadres, defecting units, and Allied envoys accepting a peace they can no longer refuse. The text should stress that the old alliance assumption has broken inside South Africa and that the peace stops the foreign war without pretending the civil rupture was clean.
- Fit explanation: Milton gives a compact peace-after-war line that reads as settlement rather than triumph. It matches the branch structure better than purely tragic civil-war quotations because this slot fires after victory and negotiated external peace, not during the worst bloodletting.
- Attribution confidence: high
- Copyright note: public domain
- Ready for parent localisation wiring: yes

### Backup candidates considered

1. `The Peace of Pretoria`
   - Quote: `From ancient grudge break to new mutiny, / Where civil blood makes civil hands unclean.`
   - Source: William Shakespeare, *Romeo and Juliet*, Prologue
   - Source link: https://www.gutenberg.org/files/1513/1513-h/1513-h.htm
   - Suggested button: `Civil hands unclean.`
   - Why not selected: excellent civil-war wording, but it leans harder into the rupture than the settlement. Better if the parent wants urban devastation foregrounded over treaty aftermath.

2. `The Congress in Pretoria`
   - Quote: `Nevertheless, through the whole of South Africa there runs a certain unity.`
   - Source: Olive Schreiner, *Thoughts on South Africa*
   - Year: 1923 publication of late essays
   - Source link: https://www.gutenberg.org/cache/epub/64520/pg64520-images.html
   - Suggested button: `There runs a certain unity.`
   - Why not selected: regionally specific and thematically strong, but weaker as a super-event quote because it describes South Africa as a landscape and social whole more than a forced postwar peace.

3. Blocked variant
   - Idea: a Smuts or South African parliamentary line about settlement, union, or peace
   - Status: blocked
   - Reason: I did not find a sufficiently strong, short, and cleanly sourced primary-text line within the bounded pass that beat the Milton package.

## 2. `africa_dynamic_cross_continent_union`

Role fit:

- This slot marks Africa entering a cross-continental union before the terminal `World Is One` end-state.
- It must feel immense and politically impossible, but it should still read as a federative or congress-scale consolidation rather than the final abolition of all world plurality.

### Recommended package

- Candidate title direction: use the actual formed union name as the title rather than a static generic label
- Title examples from the spec:
  - `African-Middle Eastern Union`
  - `Afro-Asian Union`
  - `Afro-Eurasian Union`
- Main quote: `In the Parliament of man, the Federation of the world.`
- Quote source: Alfred, Lord Tennyson, `Locksley Hall`
- Year: 1842
- Source link: https://www.gutenberg.org/files/8601/8601-h/8601-h.htm
- Button / cultural-political remark: `Standards of the peoples.`
- Button source: short fragment from the immediately preceding line in `Locksley Hall`: `With the standards of the peoples plunging thro' the thunderstorm`
- Button source link: https://www.gutenberg.org/files/8601/8601-h/8601-h.htm
- Description direction: merged congresses, envoys, seals, ports, convoy routes, and treaty chambers binding two or more continental projects into one legal body. Emphasize that separate unifier logics are no longer merely allied; they are being folded into a shared form, charter, command, covenant, or federation. Keep it clearly below the terminal world-union register.
- Fit explanation: Tennyson is the cleanest public-domain line for transcontinental federation. It is grand enough for a super-event, but still recognizably about a large political union rather than the absolute terminality already occupied by `The World Is One`.
- Attribution confidence: high
- Copyright note: public domain
- Ready for parent localisation wiring: conditionally yes
- Condition: the parent should use the actual dynamic union name as `.t`. Do not force one static title across all continent combinations.

### Backup candidates considered

1. Dynamic title with Africa-led political frame
   - Quote: `The forces that unite us are intrinsic and greater than the superimposed influences that keep us apart.`
   - Source: Kwame Nkrumah, *Africa Must Unite*
   - Year: 1963
   - Source link: https://www.marxists.org/subject/africa/nkrumah/1963/africa-must-unite.pdf
   - Suggested button: `The union widens.`
   - Why not selected: strong for an explicitly Africa-led federation, but weaker for the full range of possible cross-continental combinations because it remains more narrowly Pan-African than transcontinental.

2. Dynamic title with more explicit federal language
   - Quote: `The federation of the world`
   - Source: Alfred, Lord Tennyson, `Locksley Hall`
   - Source link: https://www.gutenberg.org/files/8601/8601-h/8601-h.htm
   - Suggested button: `The federation widens.`
   - Why not selected: usable, but weaker than the full `Parliament of man` line for signalling the merged-congress character of the route.

3. Blocked variant
   - Idea: use a Bandung, OAU, or Afro-Asian Conference line as the main quote
   - Status: blocked
   - Reason: the bounded pass did not surface a short, exact, and suitably grand line from a traceable primary text that outperformed Tennyson for a generic dynamic cross-continent union role.

## Parent implementation recommendation

- `africa_rsa_allies_peace` is ready to wire as a distinct super-event text package if the parent wants the RSA branch to receive a dedicated slot beyond the current `68` to `73` package.
- `africa_dynamic_cross_continent_union` is also ready, but only if the parent keeps the title dynamic by actual formed union name.
- Do not reuse `The World Is One` text logic for the cross-continent union role. The recommended Tennyson package is intentionally one step short of terminal world-union finality.
- If the parent later wants route-specific variants for crown, command, covenant, or federation subforms, the safest split is to keep the Tennyson quote for federation/congress outcomes and revisit the quote only for overtly imperial or supernatural variants.
