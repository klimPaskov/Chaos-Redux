# BRI/AJX portrait retry — search and ownership notes

Date: 2026-07-22

## Bounded ownership scan

The scan was restricted to the current Chaos Redux `common`, `history`,
`interface`, `gfx/leaders`, and `localisation` roots and the corresponding
vanilla roots. It checked exact and spelling variants for the retained and
rejected candidates (including accented/unaccented forms, underscore forms, and
country-tag variants).

Results:

- `Marcel Cachin`, `Marcel_Cachin`, and `Cachin`: no current-project or vanilla
  character/portrait owner.
- `Henri-Léon Devin`, `Léon-Henri Devin`, `Leon Henri Devin`,
  `Leon_Henri_Devin`, `FRA_devin`: no exact current-project or vanilla identity
  owner. Broad `Devin` hits were unrelated French localisation words.
- `Johannes Hoffmann`, `Johannes_Hoffmann`, `Friedrich Hoffmann`, and the
  relevant `Hoffmann` variants: no active current-project or vanilla
  character/portrait owner. Current docs references are retry documentation,
  not runtime ownership.
- `Raoul Castex`/`Castex`: no active character or portrait owner. A vanilla
  historical naval-unit comment uses “Castex” as a command note; this is not an
  active leader identity or portrait definition.
- `Jean-Marie Charles Abrial`/`Jean_Marie_Abrial`: vanilla owns
  `FRA_jean_marie_abrial` and `FRA_jeanmarie_charles_abrial`, their FRA
  portrait, and related localisation/idea references. Rejected as
  `rejected_active_vanilla`.
- `Charles Huntziger`/`FRA_charles_huntziger`: vanilla owns the FRA character,
  portrait, and localisation. Rejected as `rejected_active_vanilla`.

## Role and rights leads that did not survive the gates

- **Raoul Castex:** role/date fit is excellent (Brest maritime prefect from
  1935-10-22 until September 1936), but the retained 1935 CC0 source is a bust
  photograph rather than a period headshot. A colorized blog photograph was
  found, but the blog's redistribution rights are not clear; no binary is
  retained.
- **Henri-Léon Devin:** source-ready. His command of the École navale at Brest
  from September 1930 satisfies the accepted Joint Coastal Command role on
  1936-01-01. The later maritime-prefect appointment must not be projected
  backward into player-facing text.
- **Josef Bürckel:** available period source but antagonistic Nazi occupation/
  annexation official, incompatible with AJX's civic-neutral role.
- **Anton Dunckern:** exact Saarbrücken Gestapo chief lead, but unknown-author
  circa-1937 image has no defensible US redistribution basis.
- **Willy Schmelcher:** Saar police-president role lead, but foreign 1938
  publication leaves US/URAA status unresolved.
- **Theodor Berkelmann:** role/date and US rights both unresolved.
- **Kurt Daluege:** rights are usable (Bundesarchiv CC BY-SA 3.0 Germany), but
  the 1936 Berlin police role is not Saar-specific; only a 1940 Saar inspection
  is evidenced.
- **Max Braun:** prior retry lead; civilian role and rights did not satisfy the
  AJX industrial-security command brief.

## Processing boundary

This folder intentionally has source masters only. No source was cropped,
resized, recoloured, generated, or converted to PNG/DDS. The parent owns the
native portrait processor and independent review. The exact AJX commander and
strict-start-date BRI commander therefore remain blocked rather than receiving
a generic fallback.
