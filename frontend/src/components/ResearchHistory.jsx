function ResearchHistory({ history, onSelect }) {

    if (!history || history.length === 0) {
        return null;
    }


    return (
        <section className="history-section">

            <div className="section-heading small">

                <span className="eyebrow">
                    HISTORY
                </span>

                <h3>
                    Recent Research
                </h3>

            </div>


            <div className="history-list">

                {history.map(item => (

                    <button
                        className="history-item"
                        key={item.id}
                        onClick={() => onSelect(item)}
                    >

                        <span className="history-question">
                            {item.question}
                        </span>

                        <span className="history-date">
                            {item.date}
                        </span>

                    </button>

                ))}

            </div>

        </section>
    );
}

export default ResearchHistory;