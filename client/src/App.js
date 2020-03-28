import React from 'react';
import { Tab, Nav } from 'react-bootstrap';

// Components
import PharmacyList from './Components/PharmacyList';
import GroceryList from './Components/GroceryList';

// Fontawesome 
import { library } from '@fortawesome/fontawesome-svg-core'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { faStore, faHome, faInfoCircle, faShoppingCart } from '@fortawesome/free-solid-svg-icons'
library.add(fab, faStore, faHome, faInfoCircle, faShoppingCart)


function App() {
  return (
    <div className="App">
      <div className="nearby-stores-section">
      <Tab.Container defaultActiveKey="pharmacy">
            <Nav fill variant="pills" className="mb-3">
              <Nav.Item>
                <Nav.Link eventKey="pharmacy" className="py-3">
                  <h5 className="mb-0 text-uppercase">Pharmacy</h5>
                </Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link eventKey="grocery" className="py-3">
                  <h5 className="mb-0 text-uppercase">Grocery</h5>
                </Nav.Link>
              </Nav.Item>
            </Nav>
            <Tab.Content>
              <Tab.Pane eventKey="pharmacy">
                <PharmacyList />
              </Tab.Pane>
              <Tab.Pane eventKey="grocery">
                <GroceryList />
              </Tab.Pane>
            </Tab.Content>
      </Tab.Container>
      </div>
    </div>
  );
}

export default App;
