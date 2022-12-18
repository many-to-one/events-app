import { useEffect, useState } from "react"
import React from 'react'
import ListItem from "../ListItem"
import AddButton from "../AddButton"
import { RiDeleteBack2Fill } from 'react-icons/ri'



function EventList() {

    const [events, setEvents] = useState([])

    useEffect(() => {
        getEvents()
    }, [])

    // ################### GET ALL EVENTS ###################
    const getEvents = async () => {
        const response = await fetch("/api/events/")
        const data = await response.json()
        setEvents(data)
    };

    // ################### DELETE ALL EVENTS ###################

    const deleteAll = async () => {

        fetch("/api/event/delete-all/", {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        window.location.reload(false);
      };

    return (

      <div className="event-list">

        <div className="event-list-cont">

            <div className="y">
                {events.map((ev, index) => (
                    <ListItem key={index} ev={ev} />
                ))}
            </div>

            <div className="btn-container">

            <button className="event-btn" onClick={deleteAll} type="submit">
                <RiDeleteBack2Fill
                    style={{
                        width: "50px",
                        height: "50px",
                        color: "#F0007F",
                    }}
                />
            </button>

            <AddButton />

        </div>

        </div>
        
      </div>  

      
    )
}

export default EventList
