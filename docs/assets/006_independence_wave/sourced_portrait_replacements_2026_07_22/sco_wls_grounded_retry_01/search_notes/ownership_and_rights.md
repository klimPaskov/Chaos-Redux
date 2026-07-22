# Bounded Scotland/Wales source retry notes

Date: 2026-07-22

## Search and source decisions

The earlier Event 6 ledgers had Cunninghame Graham and Saunders Lewis as
source-ready but lacked a clean crop package, had David Lloyd George rejected as
a civilian for the Welsh commander role, and had William Edmund Ironside rejected
for ownership conflict. This retry sought one stronger civic source for Scotland,
one reproducible Welsh civic source, and one rights-defensible Welsh formation
commander. It did not broaden to unrelated countries or invented portraits.

### Robert Bontine Cunninghame Graham

The Commons file `Photo of R. B. Cunninghame Graham.jpg` is a face-visible
813x1101 scan sourced to HathiTrust's *An artist's reminiscences* page, no later
than 1907. Commons metadata records the image as public domain under its
pre-1931/PD-US-expired basis and names the subject. This is a cleaner, centered
portrait than the earlier Rijksmuseum page scan and was downloaded directly from
the Commons original URL.

### Saunders Lewis

The unchanged `Y Drych` newspaper page is the direct file used in the previous
retry. Its National Library of Wales record identifies the 3 February 1916 issue;
Commons records a Public Domain Mark / pre-1931 publication basis. Wikimedia
returned HTTP 429 when the original was requested again, so this package copies
the verified local master byte-for-byte. The source hash is identical to the
previous package (`d1552ea79f34d162e972ebe0528c219755e52f851226d6e07ef560e8c29b80e3`).

### Robert Knox Ross

Erfgoed 's-Hertogenbosch identifies Robert Knox Ross as the leader of the 53rd
Welsh Division from D-Day through 1945 and publishes a face-visible uniform
portrait. The Brabant/Erfgoed collection search record reports `CC BY-SA 3.0 NL`.
The direct image response was archived unchanged at 423x598. The biography page
was available and confirms role/date; the collection-detail page itself returned
a cache miss during this run, so a parent reviewer must confirm the licence and
credit line before runtime conversion. This is why the manifest uses
`needs_user_review`, not an unconditional rights claim.

### Gerard Corfield Bucknall (alternate)

The IWM B 5468 image is a 1944 No. 5 Army Film & Photographic Unit photograph,
authored by Sgt Laing and marked public domain under the UK Government/Crown
copyright expiry rationale on Commons. Bucknall commanded the 53rd (Welsh)
Division from 1941 to 1942. The original is a two-person walking photograph;
isolating his profile is mechanically possible but visually weaker than Ross's
single portrait, so it remains an alternate only.

### Andrew Jameson McCulloch (blocked Scottish commander lead)

McCulloch is the strongest role-fit lead found: born Edinburgh and GOC 52nd
(Lowland) Division in 1934-35 and 1936-38. The Western Front Association and
British Military History sources establish the identity and command dates. The
National Portrait Gallery lists three face-visible portraits, but its image use
route requires a paid/licensed permission; no free original was acquired. The
role is therefore blocked rather than replaced with Ironside, Dowding, a generic
officer, or a generated face.

## Ownership scan evidence

The scan covered installed vanilla and the current project under:

- `common/characters/`
- `history/countries/`
- `gfx/leaders/`
- `interface/`
- `localisation/`

Search terms included exact and variant forms of Cunninghame Graham, Saunders
Lewis, Robert Knox Ross, Gerard Bucknall, Andrew Jameson McCulloch, Edmund
Ironside, and Hugh Dowding. No character/portrait consumer was found for the
three selected subjects or the Bucknall alternate. The project localisation file
contains intentional Event 6 strings for Cunninghame Graham and Saunders Lewis;
that is not a vanilla/project character definition. Vanilla ownership was
confirmed for `ENG_hugh_dowding` and `ENG_edmund_ironside` in `common/characters/ENG.txt`,
the England country history recruitment block, and the relevant interface/idea
portrait definitions. Those two people are not reusable Scotland substitutes.

## Review outcome

- Complete source-and-crop rows: SCO civic, WLS civic.
- Complete source with rights confirmation gate: WLS commander (Ross).
- Rights-clear alternate retained for comparison: WLS commander (Bucknall).
- Fail-closed blocker: SCO territorial commander (McCulloch source gap).
- No generated real-person likeness, modern reenactment, film still, or weak
  rights substitute was used.

