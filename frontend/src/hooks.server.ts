import type { Handle } from '@sveltejs/kit'

export const handle: Handle = async ({ event, resolve }) => {
    // get cookies from browser
    console.log('Hook works!')
    const session = event.cookies.get('session')

    if (!session) {
        // if there is no session load page as normal
        return await resolve(event)
    }

    const authenticationRequest = await fetch('http://auth:8090/authenticate', {
        method: 'POST',
        headers: {
            'Accept': 'text/plain',
            'Content-Type': 'text/plain'
        },
        body: session
    })

    let authResult = await authenticationRequest.json()

    // if `user` exists set `events.local`
    if (authResult.username != 'error'  ) {
        event.locals.user = {
            name: authResult.username
        }
    }

    // load page as normal
    return await resolve(event)
}