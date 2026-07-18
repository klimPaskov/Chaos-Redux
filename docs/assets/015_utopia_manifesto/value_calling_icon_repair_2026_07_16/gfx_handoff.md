# Event 015 Ledger Value and Calling Icon GFX Handoff

## Parent-owned integration boundary

This package supplies final runtime textures and stable identifiers only. It does not edit `interface/015_utopia_manifesto.gfx`, `interface/015_utopia_manifesto_ledger.gui`, scripted GUI, gameplay, or localisation.

At handoff time, the shared working tree already contains matching sprite registrations and Ledger consumers for these identifiers. The parent should review those concurrent edits and retain the exact paths below.

## Sprite mapping

Suggested owning registry: `interface/015_utopia_manifesto.gfx`.

| Sprite | Runtime texture | Native texture size | Intended consumer |
| --- | --- | ---: | --- |
| `GFX_utopia_ledger_value_need` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_value_need.dds` | 32x32 | `utopia_ledger_value_need_icon` |
| `GFX_utopia_ledger_value_plenty` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_value_plenty.dds` | 32x32 | `utopia_ledger_value_plenty_icon` |
| `GFX_utopia_ledger_value_concord` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_value_concord.dds` | 32x32 | `utopia_ledger_value_concord_icon` |
| `GFX_utopia_ledger_value_balance` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_value_balance.dds` | 32x32 | `utopia_ledger_value_balance_icon` |
| `GFX_utopia_ledger_calling_provisioning` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_calling_provisioning.dds` | 48x48 | `utopia_ledger_calling_provisioning_icon` |
| `GFX_utopia_ledger_calling_workshops` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_calling_workshops.dds` | 48x48 | `utopia_ledger_calling_workshops_icon` |
| `GFX_utopia_ledger_calling_civic_works` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_calling_civic_works.dds` | 48x48 | `utopia_ledger_calling_civic_works_icon` |
| `GFX_utopia_ledger_calling_learning_and_care` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_calling_learning_and_care.dds` | 48x48 | `utopia_ledger_calling_learning_and_care_icon` |
| `GFX_utopia_ledger_calling_maritime_and_settlement` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_calling_maritime_and_settlement.dds` | 48x48 | `utopia_ledger_calling_maritime_and_settlement_icon` |
| `GFX_utopia_ledger_calling_defense_and_watches` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_calling_defense_and_watches.dds` | 48x48 | `utopia_ledger_calling_defense_and_watches_icon` |

## Registration pattern

Use ordinary one-frame `spriteType` registrations. No `noOfFrames`, animation block, or lazy-load override is required for these static textures.

```txt
spriteType = {
	name = "GFX_utopia_ledger_value_need"
	texturefile = "gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_value_need.dds"
}
```

Apply the same two-field pattern to the other nine rows. Keep the exact stable names in the table; in particular, the neutral Choice-versus-Assignment source is intentionally registered through the existing engine-facing `GFX_utopia_ledger_value_balance` identifier.

## Consumer notes

- The four Value files are native `32x32` textures from the current crosswalk and handoff authority.
- The six Calling files are native `48x48` textures. If the current GUI uses `scale = 0.75`, that is a parent-owned display decision; the runtime texture remains `48x48`.
- The Choice-versus-Assignment art is a neutral split emblem, not a pro-Choice or pro-Assignment state marker.
- These static icons do not replace the Need-warning animation or either balance-shift animation. Those are separate state-driven surfaces.
- Do not substitute Event 015 decision, focus, case-card, or district-card art for any row.

## Verification packet

- Human manifest: `manifest.md`.
- Machine source records: `source_records.json`.
- Machine validation: `validation.json`.
- Full checksums: `checksums.sha256`.
- Processed alpha review: `contact_sheets/processed_alpha_contact_sheet.png`.
- DDS decode review: `contact_sheets/dds_decoded_contact_sheet.png`.

All ten package DDS copies and runtime DDS files are byte-identical in their corresponding pairs. No asset is blocked or awaiting replacement art.
