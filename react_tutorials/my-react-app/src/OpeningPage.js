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
  
    handleClick = () => {
      console.log("Heading clicked");
      // Add your desired functionality here
    };
  
    render() {
      return (
        <div className="opening-page" onClick={this.handleClick}>
          <h1>Olivia Berry</h1>
          <h2>
            12 PPG | 12 RPG | 12 FPG
            <span className="cursor">|</span>
          </h2>
          <img src={myImage} alt="Olivia" className="slide-in" />
          <video className="video-bg" src={myVideo} autoPlay muted loop />
        </div>
      );
    }
  }
  



export default OpeningPage;