import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
    const response = await fetch('http://localhost:8080/mock/basic');
    const text = await response.text()

    return {
        test: text
    };
}