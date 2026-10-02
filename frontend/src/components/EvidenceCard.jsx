function EvidenceCard({ evidence }) {

    const confidence =
        Math.round(
            evidence.confidence * 100
        );

    const sourceUrl =
        evidence.source?.url || "";

    const isWebUrl =
        sourceUrl.startsWith("http://") ||
        sourceUrl.startsWith("https://");


    return (
        <article className="evidence-card">

            <div className="evidence-header">

                <span className="evidence-label">
                    {evidence.verification}
                </span>

                <span className="confidence">
                    {confidence}% confidence
                </span>

            </div>


            <h4>
                {evidence.claim}
            </h4>


            <p className="evidence-text">
                {evidence.evidence}
            </p>


            <div className="source">

                <span>
                    Source
                </span>

                {isWebUrl ? (

                    <a
                        href={sourceUrl}
                        target="_blank"
                        rel="noreferrer"
                    >
                        {evidence.source.title}
                    </a>

                ) : (

                    <p>
                        {evidence.source?.title ||
                            sourceUrl ||
                            "Document source"}
                    </p>

                )}

            </div>

        </article>
    );
}

export default EvidenceCard;