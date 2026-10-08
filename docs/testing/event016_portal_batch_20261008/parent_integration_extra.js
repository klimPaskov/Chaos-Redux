// Append before the retained core driver's final result serialization.
// This is a source test using its actual parsed helpers and native input VM.
for (const count of [3, 4, 5]) {
	test('parent-native-factory-admission-boundary-' + count, () => {
		const v = fresh();
		v.factories = ticks(count);
		assert.equal(v.call(prefix + 'portal_batch_can_start'), count >= 4);
		assert(v.call(prefix + 'portal_batch_can_pay_direct'));
	});
}
