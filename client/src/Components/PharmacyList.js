import React from 'react';
import { ListGroup } from 'react-bootstrap';

// Components
import ShopInformationCard from './ShopInformationCard';

function PharmacyList() {
  function displayPharmacies() {
    var data = [{
      id: 1,
      name: "Lorem Ipsum 1",
      location: "Lorem ipsum dolar sit amet",
      distance: "2.5km",
      occupancy: 10,
      timing: "12 am",
      services: {
        pickup: true,
        delivery: true
      }
    },
    {
      id: 2,
      name: "Lorem Ipsum 2",
      location: "Lorem ipsum dolar sit amet",
      distance: "2.5km",
      occupancy: 10,
      timing: "12 am",
      services: {
        pickup: true,
        delivery: false
      }
    },
    {
      id: 3,
      name: "Lorem Ipsum 3",
      location: "Lorem ipsum dolar sit amet",
      distance: "2.5km",
      occupancy: 10,
      timing: "12 am",
      services: {
        pickup: false,
        delivery: true
      }
    }];
    return data.map(pharmacy => {
      return (
        <ShopInformationCard key={pharmacy.id} shop={pharmacy}/>
      )
    })
  }
  return (
    <div className="pharmacy-list-section container">
      <div className="section-header mb-3">
        <h3 className="text-dark mb-0">Pharmacy Near You</h3>
        <p className="text-secondary mb-3">Find pharmacies near you</p>
      </div>
      <ListGroup variant="flush" id="pharmacy-list">
          {displayPharmacies()}
      </ListGroup>
    </div>
  );
}

export default PharmacyList;
