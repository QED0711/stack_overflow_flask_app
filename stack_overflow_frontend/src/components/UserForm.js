import React from 'react'

import request from '../js/request'

const UserForm = ({ setPrediction }) => {

    const handleSubmit = (e) => {
        e.preventDefault()
        const text = document.getElementById("user-form-text").value
        setPrediction("")
        request(text, setPrediction)
    }

    return (
        <form id="user-form" onSubmit={handleSubmit}>
            <textarea id="user-form-text" placeholder="paste or write your text here..."></textarea>
            <br/>
            <input type="submit" value="Predict Tag"/>
        </form>
    )

}

export default UserForm