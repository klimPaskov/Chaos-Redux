# Event 006 missing flag package, chunk 3

This package supplies the flat flag source masters, processed PNG ladders, and runtime TGA triplets for eight registered Event 006 tags.

The selected source masters are ImageGen outputs made from the documented identity references below; they are clean orthographic flag designs and are not photographs, fabric renders, or scene art.

| Tag | Identity | Status | Source/provenance | Era fit and uncertainty |
| --- | --- | --- | --- | --- |
| GMX | East Turkestan | needs_user_review | ImageGen synthesis guided by the 1933-1934 Kokbayraq reference at the linked Wikipedia page; no external image is shipped as runtime art. | The blue crescent-and-star identity is historically grounded, but Event 006's East Turkestan scope is an alternate-history 1936 route and should receive community review. |
| GTX | Tonga | handed_off | ImageGen redraw guided by Tonga's attested 1875 flag design. | The red field, white canton, and red Greek cross are period-compatible; the source is a generated clean redraw rather than a copied file. |
| GYX | Acadia | handed_off | ImageGen redraw guided by the Acadian flag adopted in 1884. | French tricolour and gold star are historically attested and fit the registry identity; generated rendering is intentionally flat. |
| GZX | Newfoundland | needs_user_review | ImageGen redraw guided by the 1904-1949 Dominion of Newfoundland red ensign and its seal roundel. | The period ensign structure is grounded, but the tiny seal is a simplified generated emblem and should be reviewed at 10x7. |
| HAX | Cascadia | needs_user_review | ImageGen fictional civic synthesis using Pacific Northwest forest, fir, river, and water motifs. | This is a route/formable identity rather than an asserted 1936 historical flag; no modern movement flag was copied. |
| HCX | Texas | handed_off | ImageGen redraw guided by the attested Texas Lone Star flag. | Blue hoist, white upper fly, red lower fly, and one white star are period-safe and identity-specific. |
| HDX | Cherokee Nation | needs_user_review | ImageGen civic synthesis using the exact Cherokee seven-point star cue and seven-oak-leaf institutional motif, with the modern official flag used only as a context reference. | The compact emblem is not an asserted historical Cherokee flag and needs Cherokee community/institutional review. |
| HEX | Haudenosaunee Confederacy | needs_user_review | ImageGen negotiated-confederacy synthesis using the Eastern white pine and wampum-belt design language from the Iroquois Confederacy reference. | This is not a claim that one universal historical flag existed; exact confederacy/community approval remains required. |

All selected masters are retained under `source_png/` with SHA-256 hashes in `metadata/flag_validation.json` and `metadata/hashes.sha256`.

Each tag has processed PNGs at 82x52, 41x26, and 10x7 and uncompressed 32-bit BGRA bottom-left-origin TGAs at the same dimensions.

No ideology variants are supplied because the registry does not provide evidence for distinct historical variants.

The small 10x7 previews are mechanically downsampled and are intentionally flagged for review where a seal, crescent, tree, or other emblem becomes a compact pixel cluster.
