import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { ListGroup } from 'react-bootstrap';

import ShopServicesIcon from './ShopServicesIcon';

function ShopInformationCard(props) {
  function displayShopInformation() {
    var shop = props.shop;
    var services = props.shop.services;
    return (
      <div className="shop-card-container d-flex align-items-center justify-content-between">
        <div className="shop-card-information">
          <h3 className="mb-0 text-weight-bold text-dark">{shop.name}</h3>
          <p className="mb-0 text-secondary">{shop.location}</p>
          <p className="mb-2 text-dark">{shop.distance} Away</p>
          <h5 className="mb-0 text-weight-bold text-dark">Occupancy: <span>{shop.occupancy}</span></h5>
          <h5 className="mb-0 text-weight-bold text-success mb-2">Open unit <span>{shop.timing}</span></h5>
          <ShopServicesIcon services={services}/>
        </div>
        <div className="shop-card-options d-flex">
          <div className="mr-3">
            <FontAwesomeIcon icon="shopping-cart" size="2x"/>
          </div>
        </div>
      </div> 
    );
  }
  return (
    <ListGroup.Item className="shop-card border-0 p-3 mb-3 bg-light rounded">
      {displayShopInformation()}
    </ListGroup.Item>
  );
}

export default ShopInformationCard;
