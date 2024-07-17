import "./header.css";
import { Link } from "react-router-dom"
import React from 'react'

function Header() {
    <div className='header'>
        <div className="header_title">
            <h1>Finance Calculator</h1>
        </div>
        <div className="nav_bar">
            <Link to = "/PV">
                <span className="nav_PV">Present Value</span>
            </Link>
            <Link to = "/FV">
                <span className="nav_FV">Future Value</span>
            </Link>
            <Link to = "/Annuity">
                <span className="nav_Annuity">Annuity</span>
            </Link>
            <Link to = "/Interest">
                <span className="nav_Interest">Interest</span>
            </Link>
            <Link to = "/Periods">
                <span className="nav_Periods">Periods</span>
            </Link>
            <Link to ="/Payment">
                <span className="nav_Payment">Payment</span>
            </Link>
        </div>
    </div>
}