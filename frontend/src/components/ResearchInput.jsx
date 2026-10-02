import { useState } from "react";


function ResearchInput({
    onResearch,
    loading
}) {

    const [question, setQuestion] =
        useState("");


    const [sourceMode, setSourceMode] =
        useState("web_and_documents");


    const handleSubmit = (event) => {

        event.preventDefault();


        if (loading) {
            return;
        }


        if (!question.trim()) {
            return;
        }


        onResearch(
            question.trim(),
            sourceMode
        );
    };


    const handleKeyDown = (event) => {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            handleSubmit(event);
        }
    };


    return (
        <section className="research-section">

            <div className="hero-text">

                <span className="eyebrow">
                    AI RESEARCH WORKSPACE
                </span>


                <h2>
                    Research complex questions
                    <span> with evidence.</span>
                </h2>


                <p>
                    RAGOps breaks your question into
                    research tasks, gathers relevant
                    information, verifies evidence,
                    and creates a structured report.
                </p>

            </div>


            <form
                className="research-box"
                onSubmit={handleSubmit}
            >

                <label htmlFor="research-question">
                    Research question
                </label>


                <textarea
                    id="research-question"

                    placeholder="Example: What are the main concepts discussed in my document?"

                    value={question}

                    onChange={(event) =>
                        setQuestion(
                            event.target.value
                        )
                    }

                    onKeyDown={handleKeyDown}

                    rows="5"

                    disabled={loading}
                />


                <div className="source-mode">

                    <span className="source-mode-label">
                        Research sources
                    </span>


                    <label className="source-option">

                        <input
                            type="radio"

                            name="sourceMode"

                            value="web_and_documents"

                            checked={
                                sourceMode ===
                                "web_and_documents"
                            }

                            onChange={(event) =>
                                setSourceMode(
                                    event.target.value
                                )
                            }

                            disabled={loading}
                        />

                        <span>
                            Web + Documents
                        </span>

                    </label>


                    <label className="source-option">

                        <input
                            type="radio"

                            name="sourceMode"

                            value="documents_only"

                            checked={
                                sourceMode ===
                                "documents_only"
                            }

                            onChange={(event) =>
                                setSourceMode(
                                    event.target.value
                                )
                            }

                            disabled={loading}
                        />

                        <span>
                            Documents only
                        </span>

                    </label>

                </div>


                <div className="research-box-footer">

                    <span>
                        Enter to research ·
                        Shift + Enter for new line
                    </span>


                    <button
                        type="submit"
                        disabled={
                            loading ||
                            !question.trim()
                        }
                    >

                        {loading
                            ? "Researching..."
                            : "Start Research"
                        }

                    </button>

                </div>

            </form>

        </section>
    );
}


export default ResearchInput;