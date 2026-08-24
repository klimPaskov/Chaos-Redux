# Replacement-key v3 lineage rejection

Status: **rejected — repeated firearm-animation deformation**.

- Exact input: `refs/original/meshy_input.png`, SHA-256 `AB15C53A9BF317F5BD0BBD8E9A881F85E4F9EDFE4B5A38FFE4472BBDD33D604B`.
- Meshy 7 generation: `01a03428-78a3-7861-b4ac-7a0b050c937f`, 30 credits. Neutral seven-view geometry passed alien identity, full ray gun, two-hand contact, and vanilla-scale review.
- Remesh: `01a0342e-8baa-7a02-a555-cd79e8c88abc`, 5 credits. The 101,657-triangle provider model retained the weapon and hand contact.
- First rig: `01a03438-b0fd-7d37-940c-c212018c93bf`, 5 credits. Neutral rig passed after excluding only the disconnected provider `Icosphere` helper artifact.
- Shooting action 690: `01a0343b-fa22-7e42-b92a-153ba86b66ed`, 3 credits. Rejected at frames 0, 20, 40, 60, and 80 for catastrophic torso/arm stretching and gun collapse into the upper body.
- Independent shooting action 680: `01a0343e-d522-7f6a-894b-67d51b92dcdf`, 3 credits. Rejected at frames 0, 8, 16, 24, and 32 for the same deformation.
- Recovery re-rig: `01a03442-e622-7acf-9d53-f0167818bb74`, 5 credits. Neutral contact passed, but action 690 task `01a03444-ebc1-7b43-9b49-08602b02b19f`, 3 credits, reproduced the failure at frames 0, 40, and 80.

No Blender weapon attachment, weight repair, replacement action, transform-only motion, or semantic reuse was attempted. Heavy v3 provider and Blender artifacts were deleted after this record; retained rejection evidence is limited to the task receipts, adapter reports, and three representative frame previews.
