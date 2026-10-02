import { useState } from "react";
import { uploadDocument } from "../services/api";


function DocumentUpload({ onUpload }) {

    const [uploading, setUploading] = useState(false);
    const [message, setMessage] = useState("");


    const handleFileChange = async (event) => {

        const file = event.target.files[0];

        if (!file) {
            return;
        }

        try {

            setUploading(true);
            setMessage("");

            const result = await uploadDocument(file);

            setMessage(
                `${result.details.file} indexed successfully`
            );

            onUpload?.(result);

        } catch (error) {

            setMessage(error.message);

        } finally {

            setUploading(false);
        }
    };


    return (
        <section className="upload-section">

            <div className="upload-icon">
                +
            </div>

            <div className="upload-content">

                <h3>
                    Add your research documents
                </h3>

                <p>
                    Upload PDF, DOCX, TXT or CSV files
                    to include them in your research.
                </p>

                <label className="upload-button">

                    {uploading
                        ? "Uploading..."
                        : "Choose document"
                    }

                    <input
                        type="file"
                        accept=".pdf,.docx,.txt,.csv"
                        onChange={handleFileChange}
                        hidden
                    />

                </label>

                {message && (
                    <p className="upload-message">
                        {message}
                    </p>
                )}

            </div>

        </section>
    );
}

export default DocumentUpload;