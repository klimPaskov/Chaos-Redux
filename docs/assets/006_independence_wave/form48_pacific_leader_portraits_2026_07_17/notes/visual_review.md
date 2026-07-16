# Independent visual approval record

- Date: 2026-07-17
- Producer: `/root/form48_leader_portraits`
- Independent reviewer and approving parent: `/root`
- Reference family: canonical skill-local eight-leader contact sheet
- Decision: both exact processed candidates approved for DDS conversion and runtime handoff

| Requirement | Subject | Approved processed PNG SHA-256 | Review-sheet SHA-256 |
|---|---|---|---|
| `IW-184` | Daniel Mercer | `40fc48f166fdccb3b2777ecbcf402ed487d043366d80e5ff55382f78cd0c0242` | `4dc693f5291b439510ab287d75628e248e356a382a7d72726d9d4c7583703f50` |
| `IW-179` | Elias Kihleng | `0ab2385c51562af1557bf3839dbe3fedcf9f5bc19a1a76564709fe997cc68310` | `d3f81fe9b994a78d25cfb9d79d417544dfab06e096864851b83ed13d611e5560` |

## Native-size verdict

Both candidates were reviewed at their actual `156x210` country-leader canvas.
The faces, shoulders, expressions, civilian clothing, and silhouettes remain
legible at native size. Daniel reads as a distinct graying California civic
lawyer; Elias reads as a distinct adult Micronesian civil chair. Neither reads
as a reused European identity or a generic stock face.

## Enlarged reference-comparison verdict

The processor review sheets and the package contact sheet compare the portraits
with the canonical vanilla large-leader family. The package contact sheet shows
the approved runtime image at `1.5x` nearest-neighbor enlargement so the actual
native pixels remain auditable. At that view, facial edges, controlled value
range, restrained painted finish, quiet period interiors, and sober 1930s
civilian clothing remain consistent with the vanilla family; no conversion-
blocking artifacts were found.

## Reviewer approval

Reviewer `/root` approved both exact candidates with this finding:

> APPROVE both exact processed candidates for conversion. Independent visual
> review against the skill-local eight-leader contact sheet: both are single
> adult men; head-and-shoulders scale, controlled value range, facial edge
> treatment, subdued 1930s civilian clothing, quiet painted interiors, and
> native-size face readability fit the vanilla large-leader family. Daniel
> Mercer is visually distinct (grey-streaked hair, narrow moustache, tired
> civic-lawyer expression); Elias Kihleng is visually distinct and reads as an
> adult Micronesian civil chair, not a generic European reuse. No women,
> group/council imagery, text, advisor framing, or modern props.

Approval applies only to the file hashes in the table. Any pixel change requires
a new independent review. The runtime DDS decode evidence in `validation.json`
is pixel-equal to these approved PNGs.
