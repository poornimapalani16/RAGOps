const stages = [
    {
        key: "planning",
        title: "Planning research tasks",
        description: "Breaking your question into focused tasks."
    },
    {
        key: "researching",
        title: "Gathering information",
        description: "Searching the web and your documents."
    },
    {
        key: "verifying",
        title: "Verifying evidence",
        description: "Checking claims against the collected evidence."
    },
    {
        key: "synthesizing",
        title: "Creating final report",
        description: "Combining verified evidence into a report."
    }
];


function ResearchProgress({ progress }) {

    const completedSteps =
        progress?.completed_steps || 0;


    return (
        <section className="progress-section">

            <div className="progress-header">

                <div>

                    <span className="eyebrow">
                        RESEARCH IN PROGRESS
                    </span>

                    <h2>
                        Building your report
                    </h2>

                </div>

                <span className="progress-count">
                    {completedSteps}/4
                </span>

            </div>


            <div className="progress-list">

                {stages.map((stage, index) => {

                    const completed =
                        index < completedSteps;

                    const active =
                        progress?.current_stage === stage.key;

                    return (
                        <div
                            className={`progress-item ${
                                completed
                                    ? "completed"
                                    : active
                                        ? "active"
                                        : ""
                            }`}
                            key={stage.key}
                        >

                            <div className="progress-icon">

                                {completed
                                    ? "✓"
                                    : active
                                        ? "•"
                                        : ""
                                }

                            </div>

                            <div>

                                <h3>
                                    {stage.title}
                                </h3>

                                <p>
                                    {stage.description}
                                </p>

                            </div>

                        </div>
                    );

                })}

            </div>

        </section>
    );
}

export default ResearchProgress;