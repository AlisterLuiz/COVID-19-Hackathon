import React from 'react';
import { ListGroup } from 'react-bootstrap';

// Components
import ShopInformationCard from './ShopInformationCard';

function GroceryList() {
  function displayGroceries() {
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
    return data.map(grocery => {
      return (
        <ShopInformationCard key={grocery.id} shop={grocery}/>
      )
    })
  }
  return (
    <div className="grocery-list-section container">
      <div className="section-header mb-3">
        <h3 className="text-dark mb-0">Grocery Near You</h3>
        <p className="text-secondary mb-3">Find groceries near you</p>
      </div>
      <ListGroup variant="flush" id="grocery-list">
          {displayGroceries()}
      </ListGroup>
    </div>
  );
}

export default GroceryList;
