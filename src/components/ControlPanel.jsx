import { useState } from "react";

function ControlPanel({ nextDay, irrigate, fertilize }) {

    const [litres, setLitres] = useState(20);

    const [fertilizerType, setFertilizerType] = useState("NPK");
    const [fertilizerAmount, setFertilizerAmount] = useState(10);

    return (
        <div className="card">

            <h2> Farm Controls</h2>

            <div className="control-group">
                <input
                    type="number"
                    value={litres}
                    onChange={(e) => setLitres(e.target.value)}
                    placeholder="Litres"
                />

                <button onClick={() => irrigate(litres)}>
                    Irrigate
                </button>
            </div>

            <div className="control-group">

                <input
                    type="text"
                    value={fertilizerType}
                    onChange={(e) => setFertilizerType(e.target.value)}
                    placeholder="Fertilizer"
                />

                <input
                    type="number"
                    value={fertilizerAmount}
                    onChange={(e) => setFertilizerAmount(e.target.value)}
                    placeholder="Amount"
                />

               <button
                onClick={() => {
                console.log("Button clicked");
                console.log(fertilize);
                fertilize(fertilizerType, fertilizerAmount);
    }}
>
    Fertilize
</button>

            </div>

            <button onClick={nextDay}>
                Next Day
            </button>

        </div>
    );
}

export default ControlPanel;