import React from 'react'

const Predictions = ({ prediction }) => {

    return (
        <div>
            <h2 className="section-header">Predictions:</h2>
            <hr/>
            <div>
                <div className={`tag prediction-${prediction === 'c#'}`}><h1>C#</h1></div>
                <div className={`tag prediction-${prediction === 'c++'}`}><h1>C++</h1></div>
                <div className={`tag prediction-${prediction === 'java'}`}><h1>Java</h1></div>
                <div className={`tag prediction-${prediction === 'python'}`}><h1>Python</h1></div>
                <div className={`tag prediction-${prediction === 'javascript'}`}><h1>Javascript</h1></div>
            </div>
        </div>
        )

}

export default Predictions