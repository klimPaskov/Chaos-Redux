# Prempeh II rejected-conversion audit record

**Audit date:** 2026-07-18
**Rejected PNG:** `processed_png/portrait_DOX_prempeh_ii.png`
**Deleted DDS path:** `gfx/leaders/006_independence_wave/portrait_DOX_prempeh_ii.dds`
**Current runtime status:** absent; rejected; unwired.

Before the parent visual rejection, the repository converter produced one DDS
from the candidate. Mechanical validation found:

* PNG and DDS dimensions were `156x210`.
* PNG SHA-256: `f113cefba729b8a852252d48c81965cce9a89595d3c1487a085056edc2ea9941`.
* Deleted DDS SHA-256: `0e028b3ec9823fa356aa7c4618123215e06040d1092f37413dab5b2cc2b0ea0f`.
* Decoded PNG/DDS RGBA pixels were equal.
* The DDS had the expected one-level uncompressed BGRA header and exact length.

These facts prove only that the converter reproduced the rejected PNG. They do
not prove visual suitability. The parent rejected the underlying PNG as a
sharpened grayscale archival photograph rather than a painted/colour HOI4
leader portrait, so the DDS was deleted and must not be reconstructed or wired
without a new approved replacement.
