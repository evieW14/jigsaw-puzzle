const API_URL = "http://localhost:8000";

export async function api<T>(
    url: string,
    options: RequestInit = {}
): Promise<T> {
    const response = await fetch(`${API_URL}${url}`, {
        ...options,
        headers: {
            "Content-Type": "application/json",
            ...(options.headers || {}),
        },
    });

    if (!response.ok) {
        const body = await response.text();
        throw new Error(`API error ${response.status}: ${body}`);
    }

    if (response.status === 204) {
        return undefined as T;
    }

    return response.json();
}