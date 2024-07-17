import React from "react"
import Header from "./Header"
import { BrowserRouter as Router, Route, Routes } from "react-router-dom"

function App() {
    return (
        <div className="App">
            <Router>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/PV" element={<PV />} />
                </Routes>
            </Router>
        </div>
    )
}