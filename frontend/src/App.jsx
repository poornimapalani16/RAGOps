import { useEffect, useState } from "react";

import Header from "./components/Header";
import ResearchInput from "./components/ResearchInput";
import DocumentUpload from "./components/DocumentUpload";
import ResearchProgress from "./components/ResearchProgress";
import ResearchReport from "./components/ResearchReport";
import ResearchHistory from "./components/ResearchHistory";

import {
    startResearch,
    getResearchStatus
} from "./services/api";


function App() {

    const [loading, setLoading] =
        useState(false);

    const [progress, setProgress] =
        useState(null);

    const [result, setResult] =
        useState(null);

    const [error, setError] =
        useState("");

    const [history, setHistory] =
        useState([]);


    // =========================================
    // Load saved research history
    // =========================================

    useEffect(() => {

        const savedHistory =
            localStorage.getItem(
                "ragops_history"
            );


        if (!savedHistory) {
            return;
        }


        try {

            const parsedHistory =
                JSON.parse(
                    savedHistory
                );


            if (Array.isArray(parsedHistory)) {

                setHistory(
                    parsedHistory
                );

            }

        } catch (error) {

            console.error(
                "Could not load research history:",
                error
            );

            setHistory([]);

        }

    }, []);


    // =========================================
    // Save research to local history
    // =========================================

    const saveHistory = (item) => {

        const updatedHistory = [

            item,

            ...history.filter(
                existing =>
                    existing.id !== item.id
            )

        ].slice(0, 10);


        setHistory(
            updatedHistory
        );


        localStorage.setItem(
            "ragops_history",
            JSON.stringify(
                updatedHistory
            )
        );
    };


    // =========================================
    // Polling delay
    // =========================================

    const wait = (
        milliseconds
    ) => {

        return new Promise(
            resolve =>
                setTimeout(
                    resolve,
                    milliseconds
                )
        );

    };


    // =========================================
    // Start Research
    // =========================================

    const handleResearch = async (
        question,
        sourceMode
    ) => {

        try {

            setLoading(true);

            setError("");

            setResult(null);

            setProgress(null);


            // ---------------------------------
            // Create research job
            // ---------------------------------

            const job =
                await startResearch(
                    question,
                    sourceMode
                );


            let finished = false;


            // ---------------------------------
            // Poll until completed
            // ---------------------------------

            while (!finished) {

                await wait(1500);


                const status =
                    await getResearchStatus(
                        job.job_id
                    );


                setProgress(
                    status
                );


                // ---------------------------------
                // Completed
                // ---------------------------------

                if (
                    status.status ===
                    "completed"
                ) {

                    const completedResult = {

                        question,

                        sourceMode,

                        report:
                            status.report ||
                            "",

                        evidence:
                            status.evidence ||
                            []

                    };


                    setResult(
                        completedResult
                    );


                    // Save to history

                    saveHistory({

                        id:
                            job.job_id,

                        question,

                        sourceMode,

                        date:
                            new Date()
                                .toLocaleString(),

                        report:
                            status.report ||
                            "",

                        evidence:
                            status.evidence ||
                            []

                    });


                    finished = true;
                }


                // ---------------------------------
                // Failed
                // ---------------------------------

                if (
                    status.status ===
                    "failed"
                ) {

                    throw new Error(
                        status.error ||
                        "Research failed."
                    );
                }

            }


        } catch (error) {

            console.error(
                "Research error:",
                error
            );


            setError(
                error.message ||
                "Something went wrong while researching."
            );


        } finally {

            setLoading(false);
        }
    };


    // =========================================
    // Select history item
    // =========================================

    const handleHistorySelect = (
        item
    ) => {

        setResult({

            question:
                item.question,

            sourceMode:
                item.sourceMode ||
                "web_and_documents",

            report:
                item.report ||
                "",

            evidence:
                item.evidence ||
                []

        });


        setProgress(null);

        setError("");

    };


    // =========================================
    // Main UI
    // =========================================

    return (
        <div className="app">

            <Header />


            <main>

                {/* =================================
                    Research Input
                ================================= */}

                <ResearchInput
                    onResearch={
                        handleResearch
                    }
                    loading={
                        loading
                    }
                />


                {/* =================================
                    Document Upload
                ================================= */}

                <DocumentUpload />


                {/* =================================
                    Research History
                ================================= */}

                {!loading && (

                    <ResearchHistory
                        history={
                            history
                        }

                        onSelect={
                            handleHistorySelect
                        }
                    />

                )}


                {/* =================================
                    Research Progress
                ================================= */}

                {loading && (

                    <ResearchProgress
                        progress={
                            progress
                        }
                    />

                )}


                {/* =================================
                    Error Message
                ================================= */}

                {error && (

                    <div
                        className="error-message"
                    >
                        {error}
                    </div>

                )}


                {/* =================================
                    Research Result
                ================================= */}

                {result && (

                    <ResearchReport
                        question={
                            result.question
                        }

                        report={
                            result.report
                        }

                        evidence={
                            result.evidence
                        }
                    />

                )}

            </main>


            {/* =================================
                Footer
            ================================= */}

            <footer>

                <p>
                    RAGOps · Evidence-driven AI research
                </p>

            </footer>

        </div>
    );
}


export default App;