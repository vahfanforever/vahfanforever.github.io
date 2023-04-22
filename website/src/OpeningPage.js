import React from 'react';
import './OpeningPage.css';
import myVideo from './opening-vid.mp4';
import myImage from './goldfield-giants.png'

class OpeningPage extends React.Component {
  componentDidMount() {
      setTimeout(() => {
          const image = document.querySelector(".slide-in");
          image.classList.add("active");
      }, 500);
  }

  handleImageClick = () => {
      window.open("https://goldfieldsgiants.nbl1.com.au/player/11d51644-70a7-11ed-82bd-31f2e03f0ad7/e6a474cb-cc5a-11ed-afd1-614a18a0f55b/olivia-berry", "_blank");
  }

  handleClick = () => {
      console.log("Heading clicked");
      // Add your desired functionality here
  }

  render() {
      return (
          <div className="opening-page" onClick={this.handleClick}>
              <h1>Olivia Berry</h1>
              <h2>18 PPG | 3 APG | 41.94 FG%
              <span className="cursor">|</span>
              </h2>
              <img src={myImage} alt="Olivia" className="slide-in" onClick={this.handleImageClick}  style={{ cursor: 'pointer' }}/>
              <video className="video-bg" src={myVideo} autoPlay muted loop />
          </div>
      );
  }
}

export default OpeningPage;