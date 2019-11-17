import React, { Component, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import CurrentWeather from './component/CurrentWeather';

class App extends Component {

  constructor(props) {
    super(props);
    this.getWeather = this.getWeather.bind(this);
    this.getForecast = this.getForecast.bind(this);
    this.state = {
      weatherData: null,
      forecast: [],
    };

  }

componentWillMount() {
    let current = this.getWeather(window.current);
    let fore = this.getForecast(window.forecast);
    this.setState({
    weatherData: current,
    forecast: fore
    });
 }

  componentDidMount() {
    let current = this.getWeather(window.current);
    let fore = this.getForecast(window.forecast);
    this.setState({
    weatherData: current,
    forecast: fore
    });
   }

  /*componentDidUpdate(prevProps, prevState) {
    if (this.state.city !== prevState.city) {
      this.setState({
    currentWeather: this.getWeather(this.state.city)
    });
    this.setState({
    forecast: this.getForecast(this.state.city)})
    }
  }
*/


  getWeather(current) {
    const mappedData = this.mapDataToWeatherInterface(current);
    return mappedData;
    }



  getForecast(fore) {
    let result = fore;
    const forecast = [];
    for (let i = 0; i < result.list.length; i += 8) {
        forecast.push(this.mapDataToWeatherInterface(result.list[i + 4]));
    }
    return forecast;
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
    let currentWeather = this.state.weatherData;
    let forecast = this.state.forecast;
    let current_weather = <CurrentWeather city={this.state.weatherData.city} temp={this.state.weatherData.temperature} />
    return (
      <div className="App">
            {current_weather}
      </div>
    );
}
}

export default App;
