# Utopia Balance to Choice — Frame Provenance

Every accepted source frame is a separate built-in ImageGen output. Frames 001–007 reference the preceding accepted output; frame 000 corrects the rejected draft documented in `notes/rejected_drafts.md`. No processed frame was synthesized from transforms of another frame.

| Frame | State | Accepted ImageGen handle | Generation mode and image reference | Source dimensions | Source SHA-256 | Processed SHA-256 |
| --- | --- | --- | --- | --- | --- | --- |
| 000 | neutral measure | `exec-9c321acd-bf97-4e61-b52b-97c96feedcac.png` | precise-object edit of rejected `exec-159881cb-6d2d-4086-8950-4290ebc90a80.png` | `1774x887` | `38cfacd7af997525e516d899179ede7e3483f3adde3930364511285a19c4e0a6` | `8aeea0d817f345bf22911355f4c33316014a0188975fbd1f179af7728b1d053d` |
| 001 | first release | `exec-4684edb7-abd3-4c32-917d-464d3adc237f.png` | precise-object edit of frame 000 handle | `1774x887` | `0d73fdc1444f5805a3a7e359088d3b378805648fc4fb9d056e9edd02bc081702` | `9fe056d957f5b75492471a46332fe89e1e188512231eddbe4d59fb2dbe3cd6bd` |
| 002 | fork emerging | `exec-0af4a5a1-b54d-40d6-beb8-bc372ed64259.png` | precise-object edit of frame 001 handle | `1774x887` | `7fffc55730a150047aa463e22ffda0f427211889855e11224ef20140889f4803` | `f5c525e5209af6ea6a710a3698e4a090926395cf1b5a08312d4733f08476c4f0` |
| 003 | paths separating | `exec-baf805c3-15be-421d-9c0a-85c8a9fb369f.png` | precise-object edit of frame 002 handle | `1774x887` | `0097dc5ad2a66e673257b006077d0aa51199ae3b2d75397cef53b07ad7a528bb` | `5e0c5c89fb87077a1538d368ef16b8c2f864ef3a36c28fe682daf229d3d980d3` |
| 004 | free distribution | `exec-cb1fec19-14cb-468e-bdc6-026a0b893448.png` | precise-object edit of frame 003 handle | `1774x887` | `dc8d2fd8633981355d114ca5b2d406dfaa46d054b98c89dc4871d8a36cb760ec` | `4a2924e52ad044e95e271c9a67bf7549256c0bd7eedd06d765782ebe0d5cd534` |
| 005 | routes fully open | `exec-e7d604ed-1784-4244-9fdf-2e11947a10ad.png` | precise-object edit of frame 004 handle | `1774x887` | `7832cf10e8c8cee190d9826c623b0eee71ebf55cf75f385764c787432e083f40` | `23167aedf955137e167fd5d1bc891d34a6529397ad34c12dfc5149a4c4e1b83f` |
| 006 | voluntary settlement | `exec-f6b5c87c-1a4a-4ee4-ad25-6b6bb6602143.png` | precise-object edit of frame 005 handle | `1774x887` | `1325a1ee4c7eb0274bbdc29f557c29aa0260f91e1a707752cb6993d36f0cdfc0` | `f5a367569069828a392d99bb41be42e7076a091189366967168b16e312e5b386` |
| 007 | Choice reached | `exec-c0adc5a7-0c33-4b1f-98f0-a3222dbe9f00.png` | precise-object edit of frame 006 handle | `1774x887` | `30c45ca5d11e219d9905aac8ff9b5e817d4c7490b6add056b63321253dfd4fff` | `40b0bc5d9bf48f026dacd08a1fd617a1d93a506bbaf5319b5b36ee205fde832e` |

Prompt construction is preserved in `prompts.md` and `frame_plan.md`; crop geometry and per-frame alpha measurements are preserved in `processing_report.json`.
