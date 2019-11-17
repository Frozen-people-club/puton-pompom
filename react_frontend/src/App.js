import React, { Component, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import CurrentWeather from './component/CurrentWeather';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      city: "Yaroslavl",
      currentWeather: [],
      forecast: [],
      error: ""
    };

}
  setCity(city) {
    this.setState({
      city: city
    });

  }

  componentDidMount() {
    this.setState({ error: "" });
    this.getWeather(this.state.city);
  }

  componentDidUpdate(prevProps, prevState) {
    if (this.state.city !== prevState.city) {
      this.setState({ error: "" });
      this.getWeather(this.state.city);
    }
  }


  getWeather(city) {
    const mappedData = this.mapDataToWeatherInterface(window.current);
    this.setState({currentWeather: mappedData});
    this.getForecast(this.state.city, mappedData);
    }



  getForecast(city, mappedData) {
    let result = window.forecast;
    const forecast = [];
    for (let i = 0; i < result.list.length; i += 8) {
        forecast.push(this.mapDataToWeatherInterface(result.list[i + 4]));
    }
    this.setState({
            forecast: forecast
          });
   }

  mapDataToWeatherInterface = data => {
    const mapped = {
      city: data.name,
      country: data.sys.country,
      date: data.dt * 1000,
      humidity: data.main.humidity,
      icon_id: data.weather[0].id,
      temperature: data.main.temp - 273.15,
      description: data.weather[0].description,
      wind_speed: Math.round(data.wind.speed * 3.6), // convert from m/s to km/h
      condition: data.cod

    };


    if (data.dt_txt) {
      mapped.dt_txt = data.dt_txt;
    }

    if (data.weather[0].icon) {
      mapped.icon = data.weather[0].icon;
    }

    if (data.main.temp_min && data.main.temp_max) {
      mapped.max = data.main.temp_max;
      mapped.min = data.main.temp_min;
    }

    return mapped;
  };




  render() {
    const { city, currentWeather, forecast, error } = this.state;
    let current_weather = <CurrentWeather city={this.state.currentWeather.city} temp={this.state.currentWeather.temp} />
    return (
      <div className="App">
           city={city}
            {current_weather}
            {this.state.currentWeather.temp}
      </div>
    );
}
}

export default App;
