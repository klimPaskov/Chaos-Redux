# Event 006 AJX grounded portrait source handoff

This is a documentation-only source handoff. No `.gfx` file, runtime texture,
character definition, localisation key, history file, or interface file was
edited in this tranche.

## Package outputs

| Candidate | Source master | Processed PNG | Package DDS | Status | Review gate |
|---|---|---|---|---|---|
| Johannes Hoffmann | `source_masters/AJX/AJX_johannes_hoffmann_nationaal_archief_1955.jpg` | `processed_png/AJX/AJX_johannes_hoffmann_head_shoulders.png` | `final_dds/AJX/AJX_johannes_hoffmann.dds` | `needs_user_review` | Exact Saar civic identity and CC0 source; image is 7 Sep 1955, after the 1936 scenario. Parent must approve the era/age gap before wiring. |
| Willy Schmelcher | `source_masters/AJX/AJX_willy_schmelcher_polizeipraesident_1938.jpg` | `processed_png/AJX/AJX_willy_schmelcher_head_shoulders.png` | `final_dds/AJX/AJX_willy_schmelcher.dds` | `source_ready` | Exact Saarbruecken police/security role and 1938 archival portrait. Parent should retain the SS/police historical context and complete the final rights/context review. |

## Deferred runtime paths

The parent may choose either stable role-key transfer or new identity-key
sprites. These are suggestions only; they do not authorise a `.gfx` edit.

### Preserve the current Event 006 role keys

If the parent keeps the existing fictional character tokens while transferring
their historical identities, the likely runtime consumers are:

```text
GFX_portrait_AJX_friedrich_hoffmann
    texturefile = "gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds"

GFX_portrait_AJX_karl_becker
    texturefile = "gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds"
```

Copy the approved package DDS to those runtime paths only after the parent has
resolved the character IDs and leader/commander role semantics. The Hoffmann
path must remain review-gated until the post-1936 image is accepted.

### Rename sprites to the grounded identities

If the parent performs a guarded identity transfer and renames the consumers,
the corresponding sprite structure would be:

```text
spriteType = {
    name = "GFX_portrait_AJX_johannes_hoffmann"
    texturefile = "gfx/leaders/006_independence_wave/portrait_AJX_johannes_hoffmann.dds"
}

spriteType = {
    name = "GFX_portrait_AJX_willy_schmelcher"
    texturefile = "gfx/leaders/006_independence_wave/portrait_AJX_willy_schmelcher.dds"
}
```

These blocks are handoff examples, not edits made here. Use the repository's
normal leader/commander sprite convention and keep the canonical 156x210
large portrait shape. No `_small` or advisor/dossier texture was made.

## Source and review links

- [Johannes Hoffmann Commons source](https://commons.wikimedia.org/wiki/File:Stemming_Saarstatuut_Minister_President_Hoffmann,_Bestanddeelnr_907-3171.jpg)
- [Johannes Hoffmann Nationaal Archief record](http://proxy.handle.net/10648/a93ab252-d0b4-102d-bcf8-003048976d84)
- [Willy Schmelcher Commons source](https://commons.wikimedia.org/wiki/File:Willy_Schmelcher.jpg)
- [Original/crop comparison sheet](contact_sheets/ajx_grounded_sources_and_crops.png)
- [Source manifest](manifest.md)
- [SHA-256 inventory](source_hashes.sha256)

## Review decisions still owned by parent

1. Decide whether the post-1936 Hoffmann photograph is acceptable for the
   1936 grounded leader or leave the leader surface `needs_user_review`.
2. Decide whether to preserve the existing fictional role-key sprites or use
   the identity-key examples above; no transfer is implicit in this package.
3. Review Schmelcher's SS/police context and the Commons public-domain basis
   before releasing the DDS into the runtime `gfx/` tree.
