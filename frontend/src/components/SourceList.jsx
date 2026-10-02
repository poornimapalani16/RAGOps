function SourceList({ evidence }) {

    if (!evidence || evidence.length === 0) {
        return null;
    }

    const sources = [];

    for (const item of evidence) {

        const source = item.source;

        if (!source) {
            continue;
        }

        const key =
            `${source.title || ""}|${source.url || ""}`;

        const alreadyExists =
            sources.some(existing => existing.key === key);

        if (!alreadyExists) {
            sources.push({
                key,
                title: source.title || "Untitled source",
                url: source.url || "",
                snippet: source.snippet || "",
            });
        }
    }


    return (
        <div className="sources-section">

            <div className="section-heading small">

                <span className="eyebrow">
                    SOURCES
                </span>

                <h3>
                    Research Sources
                </h3>

                <p>
                    Sources referenced by the evidence collected
                    during this research.
                </p>

            </div>


            <div className="sources-list">

                {sources.map(source => {

                    const isWebUrl =
                        source.url.startsWith("http://") ||
                        source.url.startsWith("https://");

                    return (
                        <article
                            className="source-card"
                            key={source.key}
                        >

                            <div className="source-card-icon">
                                ↗
                            </div>

                            <div className="source-card-content">

                                <h4>
                                    {source.title}
                                </h4>

                                {source.snippet && (
                                    <p>
                                        {source.snippet}
                                    </p>
                                )}

                                {isWebUrl ? (

                                    <a
                                        href={source.url}
                                        target="_blank"
                                        rel="noreferrer"
                                    >
                                        Open source
                                    </a>

                                ) : (

                                    <span className="document-source">
                                        Document source
                                    </span>

                                )}

                            </div>

                        </article>
                    );
                })}

            </div>

        </div>
    );
}

export default SourceList;