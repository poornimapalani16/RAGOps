const API_BASE_URL =
    import.meta.env.VITE_API_URL ||
    "http://127.0.0.1:8000";


// =========================================
// Upload Document
// =========================================

export async function uploadDocument(file) {

    const formData = new FormData();

    formData.append(
        "file",
        file
    );


    const response = await fetch(
        `${API_BASE_URL}/documents/upload`,
        {
            method: "POST",
            body: formData
        }
    );


    if (!response.ok) {

        let errorMessage =
            "Document upload failed.";

        try {

            const error =
                await response.json();

            errorMessage =
                error.detail ||
                errorMessage;

        } catch {
            // Keep default message
        }


        throw new Error(
            errorMessage
        );
    }


    return response.json();
}


// =========================================
// Start Research
// =========================================

export async function startResearch(
    question,
    sourceMode
) {

    const response = await fetch(
        `${API_BASE_URL}/research`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                question,

                source_mode:
                    sourceMode ||
                    "web_and_documents"

            })
        }
    );


    if (!response.ok) {

        let errorMessage =
            "Research request failed.";

        try {

            const error =
                await response.json();

            errorMessage =
                error.detail ||
                errorMessage;

        } catch {
            // Keep default message
        }


        throw new Error(
            errorMessage
        );
    }


    return response.json();
}


// =========================================
// Get Research Status
// =========================================

export async function getResearchStatus(
    jobId
) {

    const response = await fetch(
        `${API_BASE_URL}/research/${jobId}`
    );


    if (!response.ok) {

        let errorMessage =
            "Could not get research status.";

        try {

            const error =
                await response.json();

            errorMessage =
                error.detail ||
                errorMessage;

        } catch {
            // Keep default message
        }


        throw new Error(
            errorMessage
        );
    }


    return response.json();
}


// =========================================
// Health Check
// =========================================

export async function checkHealth() {

    const response = await fetch(
        `${API_BASE_URL}/health`
    );


    if (!response.ok) {

        throw new Error(
            "Backend health check failed."
        );
    }


    return response.json();
}