import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals }) => {
	// redirect user if not logged in
	if (!locals.user) {
		throw redirect(302, '/');
	}

	const response = await fetch('http://back:8080/mock/receipts/list');
	const list = await response.json();

	return {
		list: list
	};
};
