# Utopia Balance to Assignment — Frame Provenance

Every accepted source frame is a separate built-in ImageGen output. Frames 001–007 reference the preceding accepted output; frame 000 corrects the rejected draft documented in `notes/rejected_drafts.md`. No processed frame was synthesized from transforms of another frame.

| Frame | State | Accepted ImageGen handle | Generation mode and image reference | Source dimensions | Source SHA-256 | Processed SHA-256 |
| --- | --- | --- | --- | --- | --- | --- |
| 000 | unsorted measure | `exec-1443141b-6258-4f7b-82dc-147e06fa1a42.png` | precise-object edit of rejected `exec-bc6f22dd-8477-4350-a992-d5ce9e2d41f9.png` | `1910x823` | `b70070df05f2069b7c9d10351a704330a4195e99e6a179019314fb92f8b3140d` | `f56ec61413d2839373a6f4e36b7c2227c30cfedde64388729285ed79d49c3f4b` |
| 001 | gauge engages | `exec-b306e1f7-8dfe-43c4-95ba-fc31693da9e4.png` | precise-object edit of frame 000 handle | `1910x823` | `99b1f7d763c59186b890af96e5e896acfabba259d9cfaf006488f5286d4dce7f` | `cc19524728d525f403f145b4d60f3fa4757be8d67b83895731ed7d3a6c17fa7a` |
| 002 | first alignment | `exec-96f71524-3a6a-4b4c-96cc-ed1b797ef07e.png` | precise-object edit of frame 001 handle | `1910x823` | `ca651df3336d77a5e2ba93334fef1d07a7712ad177b91aae45c6502fda57facd` | `491529f1971d602caf4955fba27761d834502d69a819d14df018f30315e521e6` |
| 003 | row forming | `exec-26e34345-7792-4167-9dd8-37659a4b4f5d.png` | precise-object edit of frame 002 handle | `1909x824` | `553a2d5101cebc55c4224dcd2d935f4e45f013b7db8f3e1fd5e693085bb22c1f` | `8da4c9be2b3e6e3991cddf7c0f0c342fa5dd3e29f3cc5a3777780c30592bd76d` |
| 004 | grid rising | `exec-36ce26a8-7b89-4f37-a889-79fed40aca95.png` | precise-object edit of frame 003 handle | `1909x824` | `0dfefc180711ed3afe6caebf94383e3dfb823f615919f5515518d94b1a005d25` | `a60b9d8cbea7760f61542e3fb1852dfc0da140719879f1aaa5f719c3412e59b6` |
| 005 | measured placement | `exec-32fea8be-e9d3-4a6d-82bf-67253ceda640.png` | precise-object edit of frame 004 handle | `1909x824` | `247b8b8f743e9e567d35a79f493875b8e266aceb8f883db8b526f1c83d0a3b34` | `9d351d6fe9428a04ef66bf8951e1483388ead56ccf18daf90346b4c72166a2d3` |
| 006 | assignment lock | `exec-11ecf0ab-3a20-421c-8bee-90ff143c73e9.png` | precise-object edit of frame 005 handle | `1909x824` | `f702b1b4b09784769f683ad067bf83914968eb8831554ca8638e3b7fcaedfbca` | `7387bf190a41495ed4afa740d3db148a18581801bfba1555670062eaae508468` |
| 007 | Assignment reached | `exec-1d4d7a14-e0d3-4027-855d-9a36f26ea9c1.png` | precise-object edit of frame 006 handle | `1908x824` | `07722ab8239d022638af58f35fbd0d475dc00ba44bd69be1f178224087834b66` | `e39f205f4a4c7fa1af2cf9179f4d68149bb9f774bb5d3f7e6248449640052fc9` |

Prompt construction is preserved in `prompts.md` and `frame_plan.md`; crop geometry and per-frame alpha measurements are preserved in `processing_report.json`.
