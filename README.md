# puton-pompom

1. \api\v1.0\current?(q={city} || lan={lan}&&lon={lon})<br>
      get json for current weather<br>
      Respone example:<br>
        `{`<br>
          `"_id":"Yaroslavl"`<br>
          `"base":"stations",`<br>
          `"clouds":{"all":90},`<br>
          `"cod":200,`<br>
          `"coord":{"lat":57.63,"lon":39.89},`<br>
          `"dt":1573237899,`<br>
          `"id":468902,`<br>
          `"main":{"humidity":92,"pressure":1026,"temp":270.15,"temp_max":270.15,"temp_min":270.15},`<br>
          `"name":"Yaroslavl",`<br>
          `"sys":{"country":"RU","id":9023,"sunrise":1573188479,"sunset":1573219221,"type":1},`<br>
          `"timezone":10800,`<br>
          `"visibility":10000,`<br>
          `"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],`<br>
          `"wind":{"deg":150,"speed":2},`<br>
          `"clothes":{"icon_id": "set5"}`<br>
        `}`<br>
			
  
2. \api\v1.0\forecast?(q={city} || lan={lan}, lon={lon})<br>
      get json for forecast weather for 5 days by 3 hours<br>
      Response example:<br>
        `{`<br>
          `"city":{`<br>
            `"coord":{"lat":57.6264,"lon":39.8934},`<br>
            `"country":"RU",`<br>
            `"id":Yaroslavl,`<br>
            `"name":"Yaroslavl",`<br>
            `"population":606730,`<br>
            `"sunrise":1573188477,`<br>
            `"sunset":1573219222,`<br>
            `"timezone":10800`<br>
          `},`<br>
          `"cnt":40,`<br>
          `"cod":"200",`<br>
          `"list":[`<br>
            `{`<br>
              `"clouds":{"all":32},`<br>
              `"dt":1573246800,`<br>
              `"dt_txt":"2019-11-08 21:00:00",`<br>
              `"main":{`<br>
                `"grnd_level":1012,`<br>
                `"humidity":88,`<br>
                `"pressure":1027,`<br>
                `"sea_level":1027,`<br>
                `"temp":270.5,`<br>
                `"temp_kf":-1.1,`<br>
                `"temp_max":271.6,`<br>
                `"temp_min":270.5`<br>
              `},`<br>
              `"sys":{"pod":"n"},`<br>
              `"weather":[{"description":"scattered clouds","icon":"03n","id":802,"main":"Clouds"}],`<br>
              `"wind":{"deg":163,"speed":2.07}`<br>
            `},`<br>
            `{`<br>
              `"clouds":{"all":26},`<br>
              `"dt":1573257600,`<br>
              `"dt_txt":"2019-11-09 00:00:00",`<br>
              `"clothes":{"icon_id": "set5"},`<br>
              `"main":{`<br>
                `"grnd_level":1014,`<br>
                `"humidity":94,`<br>
                `"pressure":1029,`<br>
                `"sea_level":1029,`<br>
                `"temp":270.76,`<br>
                `"temp_kf":-0.83,`<br>
                `"temp_max":271.58,`<br>
                `"temp_min":270.76`<br>
              `},`<br>
               `"sys":{"pod":"n"},`<br>
               `"weather":[{"description":"scattered clouds","icon":"03n","id":802,"main":"Clouds"}],"wind":{"deg":194,"speed":2}`<br>
             `}, `<br>
          `...] etc`<br>

3. /loadfile/<filename><br>
	load file from resources
