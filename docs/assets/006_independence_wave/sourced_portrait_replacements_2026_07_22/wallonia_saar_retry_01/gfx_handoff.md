# Event 006 Wallonia/Saar source retry - GFX handoff

This is a documentation-only handoff. No `.gfx` file, runtime DDS, character,
or localisation file was edited in this source tranche.

## Source masters

| Candidate | Source master | Current disposition | Deferred processing/final path |
|---|---|---|---|
| Willy Schmelcher | `source_masters/AJX/AJX_willy_schmelcher_commander_1938.jpg` | `source_ready` primary AJX security/industrial commander | After parent approval and portrait processing: `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds` (existing role-key path; do not write it in this handoff) |
| Anton Dunckern | `source_masters/AJX/AJX_anton_dunckern_security_commander_c1937.jpg` | `needs_user_review` alternate; 315x405 low-resolution master | Do not process or wire until rights, historical-context, and target-resolution review are complete |

There is no source master for the AFX Wallonia roles or AJX civic role in this
package. Their fail-closed dispositions are recorded in [`manifest.md`](manifest.md)
and [`search_notes/ownership_and_candidate_log.md`](search_notes/ownership_and_candidate_log.md).

## Existing consumers to review before any wiring

The current interface file `interface/006_independence_wave_region_01_portraits.gfx`
already declares these role-key consumers:

```text
GFX_portrait_AFX_walloon_provisional_assembly
  -> gfx/leaders/006_independence_wave/portrait_AFX_walloon_provisional_assembly.dds
GFX_portrait_AFX_walloon_reserve_commander
  -> gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds
GFX_portrait_AJX_friedrich_hoffmann
  -> gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds
GFX_portrait_AJX_karl_becker
  -> gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds
```

The AFX civic key is currently occupied by Jules Destrée and must not be
silently cloned or retitled. The AJX commander role path is the likely runtime
consumer for a processed Schmelcher portrait, but the parent must decide
whether to preserve the existing generic key or perform a guarded identity
transfer.

## Suggested sprite shape after approval

Use the repository's normal leader portrait sprite convention and canonical
156x210 portrait texture target. A final sprite definition would be structurally
equivalent to:

```text
spriteType = {
	name = "GFX_portrait_AJX_karl_becker"
	texturefile = "gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds"
}
```

That block is a handoff example, not an instruction to edit the interface file;
the existing role-key name and path must be reconciled with the approved
character identity by the parent implementation agent. No `_small` texture was
created here. If the parent adds one, follow the current portrait adapter's
large/small consumer convention rather than inventing a second naming scheme.

## Source and review links

- [Willy Schmelcher Commons source](https://commons.wikimedia.org/wiki/File:Willy_Schmelcher.jpg)
- [Anton Dunckern Commons source](https://commons.wikimedia.org/wiki/File:Anton_Dunckern.jpg)
- [AJX commander comparison sheet](contact_sheets/ajx_commander_source_candidates.png)
- [Package manifest](manifest.md)
- [SHA-256 inventory](source_hashes.sha256)

No generated face, paid-rights proxy, thumbnail, or re-encoded source is
presented as a runtime asset.
