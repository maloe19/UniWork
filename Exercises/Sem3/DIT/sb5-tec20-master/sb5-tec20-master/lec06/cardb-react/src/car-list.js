import React from 'react';

class CarList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            carArray: [{ producer: "Renault", model: "Clio" }, { producer: "Renault", model: "Twingo" }, { producer: "Citroen", model: "C3" }],
        }
    }

    render() {
        const cararray = this.state.carArray.map((car) =>
            <li>{car.producer +" " + car.model}</li>);
        return (
            <ul>{cararray}</ul>
        );
    }

}

export default CarList;