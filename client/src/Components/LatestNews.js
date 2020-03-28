import React from 'react';
import "react-responsive-carousel/lib/styles/carousel.min.css";
import { Carousel } from 'react-responsive-carousel';

function LatestNews() {
  return (
    <Carousel showArrows={false} showThumbs={false} infiniteLoop={true} autoPlay={true} showStatus={false} showIndicators={false} className="">
      <div>
          <img src="/placeholder-slider.png" />
          <p className="legend">Legend 1</p>
      </div>
      <div>
          <img src="/placeholder-slider.png" />
          <p className="legend">Legend 2</p>
      </div>
      <div>
          <img src="/placeholder-slider.png" />
          <p className="legend">Legend 3</p>
      </div>
    </Carousel>
  );
}

export default LatestNews;
