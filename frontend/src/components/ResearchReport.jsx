import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

import EvidenceCard from "./EvidenceCard";
import SourceList from "./SourceList";


function ResearchReport({ question, report, evidence }) {

    if (!report && (!evidence || evidence.length === 0)) {
        return null;
    }


    const downloadReport = () => {

        let markdown = "";


        // -------------------------
        // Title
        // -------------------------

        markdown += "# RAGOps Research Report\n\n";


        // -------------------------
        // Research Question
        // -------------------------

        if (question) {

            markdown += "## Research Question\n\n";

            markdown += `${question}\n\n`;
        }


        // -------------------------
        // Generated Report
        // -------------------------

        if (report) {

            markdown += report.trim();

            markdown += "\n\n";
        }


        // -------------------------
        // Verified Evidence
        // -------------------------

        if (
            evidence &&
            evidence.length > 0
        ) {

            markdown +=
                "## Verified Evidence\n\n";


            evidence.forEach(
                (item, index) => {

                    markdown +=
                        `### ${index + 1}. ${item.claim}\n\n`;

                    markdown +=
                        `**Verification:** ${item.verification}\n\n`;

                    markdown +=
                        `**Confidence:** ${Math.round(
                            item.confidence * 100
                        )}%\n\n`;

                    markdown +=
                        `**Evidence:** ${item.evidence}\n\n`;

                    if (item.source) {

                        markdown +=
                            `**Source:** ${item.source.title || "Unknown source"}\n\n`;

                        if (item.source.url) {

                            markdown +=
                                `**URL:** ${item.source.url}\n\n`;
                        }
                    }

                    markdown += "---\n\n";
                }
            );
        }


        // -------------------------
        // Download file
        // -------------------------

        const blob = new Blob(
            [markdown],
            {
                type: "text/markdown;charset=utf-8"
            }
        );


        const url =
            URL.createObjectURL(blob);


        const link =
            document.createElement("a");


        link.href = url;


        const safeQuestion =
            (question || "research-report")
                .replace(
                    /[^a-z0-9]+/gi,
                    "-"
                )
                .replace(
                    /^-+|-+$/g,
                    ""
                )
                .toLowerCase();


        link.download =
            `${safeQuestion || "research-report"}.md`;


        document.body.appendChild(link);

        link.click();

        document.body.removeChild(link);

        URL.revokeObjectURL(url);
    };


    return (
        <section className="report-section">

            <div className="section-heading report-heading">

                <div>

                    <span className="eyebrow">
                        RESEARCH OUTPUT
                    </span>

                    <h2>
                        Research Report
                    </h2>

                    <p>
                        Structured findings generated from the
                        research workflow and verified evidence.
                    </p>

                </div>


                <button
                    className="download-button"
                    type="button"
                    onClick={downloadReport}
                >
                    ↓ Download Report
                </button>

            </div>


            {report && (

                <article className="report-card">

                    <div className="markdown-report">

                        <ReactMarkdown
                            remarkPlugins={[remarkGfm]}
                        >
                            {report}
                        </ReactMarkdown>

                    </div>

                </article>
            )}


            {evidence?.length > 0 && (

                <div className="evidence-section">

                    <div className="section-heading small">

                        <span className="eyebrow">
                            EVIDENCE
                        </span>

                        <h3>
                            Verified Evidence
                        </h3>

                        <p>
                            Claims collected and evaluated
                            during the research process.
                        </p>

                    </div>


                    <div className="evidence-list">

                        {evidence.map(
                            (item, index) => (

                                <EvidenceCard
                                    key={index}
                                    evidence={item}
                                />

                            )
                        )}

                    </div>

                </div>
            )}


            <SourceList
                evidence={evidence}
            />

        </section>
    );
}

export default ResearchReport;