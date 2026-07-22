# Event 006 AJX grounded portrait source handoff

This is a documentation-only source handoff. No `.gfx` file, runtime texture,
character definition, localisation key, history file, or interface file was
edited in this tranche.

## Package outputs and approval boundary

| Candidate | Source master | Processed PNG | Package DDS | Status | Review gate |
|---|---|---|---|---|---|
| Johannes Hoffmann | `source_masters/AJX/AJX_johannes_hoffmann_nationaal_archief_1955.jpg` | `processed_png/AJX/AJX_johannes_hoffmann_head_shoulders.png` | `final_dds/AJX/AJX_johannes_hoffmann.dds` | `needs_user_review` | Exact Saar civic identity and CC0 source; image is 7 Sep 1955, after the 1936 scenario. Parent must approve the era/age gap before wiring. |
| Willy Schmelcher | `source_masters/AJX/AJX_willy_schmelcher_polizeipraesident_1938.jpg` | `processed_png/AJX/AJX_willy_schmelcher_head_shoulders.png` | `final_dds/AJX/AJX_willy_schmelcher.dds` | `role_mismatch_research_only` | Rights-documented 1938 Saarbruecken police/SS portrait retained for provenance. It is not an army corps commander and must not be wired to `AJX_karl_becker`. |
| Karl Becker | - | - | - | `rejected_vanilla_owner` | Exact historical identity is owned by vanilla as `GER_karl_heinrich_emil_becker`; technical/administrative artillery role is also weak for the live corps commander. No local output. |
| Wilhelm Fahrmbacher | - | - | - | `blocked` | Strong Zweibruecken/Palatinate and later corps-command fit, but no rights-clear face-visible pre-war source. No local output. |

There is currently **no role-correct, source-ready commander DDS** in this
package. The Schmelcher file paths above are research-only and are not a
suggested runtime handoff.

## Deferred runtime path: civic leader only

If the parent keeps the existing fictional leader token while accepting the
1955 era review, the likely runtime consumer remains:

```text
GFX_portrait_AJX_friedrich_hoffmann
    texturefile = "gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds"
```

Copy the approved Hoffmann package DDS to a runtime path only after the parent
has resolved the age/era review and character identity transfer. No `_small`
or advisor/dossier texture was made.

## Commander wiring gate

Do not define a grounded commander sprite from this package. Do not copy the
Schmelcher DDS into the existing
`gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds`
path: that would present a Saar police/SS chief as the live army corps
commander and would bypass the role gate. Karl Becker cannot be cloned from
vanilla, and Fahrmbacher remains blocked pending a defensible face source.

## Source and review links

- [Johannes Hoffmann Commons source](https://commons.wikimedia.org/wiki/File:Stemming_Saarstatuut_Minister_President_Hoffmann,_Bestanddeelnr_907-3171.jpg)
- [Johannes Hoffmann Nationaal Archief record](http://proxy.handle.net/10648/a93ab252-d0b4-102d-bcf8-003048976d84)
- [Johannes Hoffmann pre-1940 lead](https://www.saar-nostalgie.de/Joho1.htm)
- [Willy Schmelcher Commons source](https://commons.wikimedia.org/wiki/File:Willy_Schmelcher.jpg)
- [Karl Becker Bundesarchiv source](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-H27401,_Karl_Becker.jpg)
- [Karl Becker Deutsche Biographie](https://www.deutsche-biographie.de/sfz2563.html?language=en)
- [Wilhelm Fahrmbacher career lead](https://www.generals.dk/general/Fahrmbacher/Wilhelm_Karl/Germany.html)
- [Original/crop comparison sheet](contact_sheets/ajx_grounded_sources_and_crops.png)
- [Source manifest](manifest.md)
- [SHA-256 inventory](source_hashes.sha256)

## Review decisions still owned by parent

1. Decide whether the post-1936 Hoffmann photograph is acceptable for the
   grounded 1936 leader; otherwise leave that surface `needs_user_review`.
2. Do not transfer Schmelcher to the corps role. Select a role-correct source
   only after a new rights-clear, face-visible commander candidate passes the
   ownership and era gates.
3. Do not clone Karl Becker from vanilla or crop a Fahrmbacher group image.
4. No ImageGen identity-preserving edit is authorised until both selected
   identities are role-correct and source-ready; this retry did not invoke it.
