import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

function ShopServicesIcon(props) {
    function displayShopServices() {
        var services = props.services;
        if(services){
        return (
            <div className="shop-services-section w-100">
            <h5 className="mb-0">Services</h5> 
            <div className="shop-services d-flex align-items-center justify-content-between">
            {services.pickup ?
            <div className="shop-service d-flex align-items-center">
                <div className="service-icon bg-primary mr-2">
                <FontAwesomeIcon icon="store" color="white" size="lg"/>
                </div> 
                <p className="mb-0 mr-3 text-secondary">Pick Up</p>
            </div>
            : ""}
            {services.delivery ?
            <div className="shop-service d-flex align-items-center">
                <div className="service-icon bg-warning mr-2">
                <FontAwesomeIcon icon="home" color="white" size="lg" />
                </div> 
                <p className="mb-0 mr-3 text-secondary">Home Delivery</p>
            </div>
            : ""}
            </div>
            </div>
        );
        }
    }
    return (
        <div>
            {displayShopServices()}
        </div>
    );
}

export default ShopServicesIcon;