# ARX Sardinia portrait GFX handoff

Date: 2026-07-22
Mode: documentation-only; no `.gfx`, runtime DDS, gameplay, localisation, or
binary edit is authorised by this package.

## Handoff status

No candidate in this retry is approved for runtime use. Consequently every
final DDS path, sprite name, target `.gfx` file, and copy-ready sprite snippet
remains deliberately deferred. This file exists so the parent can wire an
accepted result later without mistaking source research for approval.

| Intended role / consumer | Candidate | Asset status | Source master | Final DDS path | Sprite name | Target `.gfx` file | Runtime action |
|---|---|---|---|---|---|---|---|
| `ARX_sardinian_crown_consultative_council` | Prince Adalberto di Savoia-Genova | `needs_user_review` | `source_masters/sardinia/arx_adalberto_savoia_genova_1935_original.png` | `deferred` | `deferred` | `deferred` | Do not process or wire until the US-publication-evidence and independent visual-review gates pass and the parent accepts the Savoy-Genova dynastic interpretation. |
| `ARX_gavino_piras` | Prince Adalberto di Savoia-Genova | `needs_user_review` | same unchanged Adalberto master | `deferred` | `deferred` | `deferred` | Do not process or wire until the same rights/visual gates pass and the parent explicitly accepts a dual dynastic-and-command role or chooses this role instead of the council role. |
| `ARX_gavino_piras` naval/coastal alternative | Giovanni Sechi | `rejected_external_mod_owner` | retained provenance master only | `not_applicable` | `not_applicable` | `not_applicable` | Never wire from this package. Parent ownership evidence identifies active Kaiserreich Sardinia character `SRD_giovanni_sechi`. |
| `ARX_gavino_piras` army alternatives | Nino Salvatore Villa Santa / Gavino Pizzolato | `blocked` | none copied | `not_applicable` | `not_applicable` | `not_applicable` | Resume sourcing only if a rights-clear archival master is found. |

## Legacy slot context

Prior Event 006 audit material associates the unresolved fictional portrait
slots with the `Vittorio Pala` crown/council role and the `Gavino Piras`
commander role. This package does not instruct the parent to overwrite those
legacy files or retain their filenames. Whether an accepted real person replaces
an existing sprite in place or receives a newly named sprite must be decided
against the live Event 006 registry after approval.

## Deferred wiring contract

- Final leader/commander texture size, once approved: `156x210`.
- Final DDS path: deferred until a candidate passes all gates and a processed
  portrait is accepted.
- Proposed or stable sprite name: deferred; no name is reserved here.
- Suggested `.gfx` target: deferred; the main agent must use the live Event 006
  portrait registry and keep its naming contract coherent.
- Ready-to-copy sprite snippet: intentionally absent because there is no final
  DDS and no approved sprite name.
- Localisation, character, history, focus, decision, and GUI references:
  outside this source package and unchanged.

The parent should update this handoff only after approval with the exact final
DDS path, stable sprite name, target `.gfx` file, and live character consumer.

## Blockers

- Adalberto: ownership scan has no match, but Commons `PD-Italy` lacks the
  publication evidence needed to establish the US condition independently;
  visual approval is also outstanding.
- Giovanni Sechi: rejected by active external-mod ownership
  (`SRD_giovanni_sechi` in Kaiserreich Sardinia).
- Villa Santa and Pizzolato: no rights-clear source master.
