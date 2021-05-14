// Need to add d3 JSON to collect data
    // Feel free to change or delete any of the code you see in this editor!
    var svg = d3.select("body").append("svg")
      .attr("width", 960)
      .attr("height", 500)

    d3.json('https://jsonplaceholder.typicode.com/posts', {
      method:"POST",
      body: JSON.stringify({
        //   Below would the "names" (use d3 query to grab them)
        // title: 'Hello',
        // body: '_d3-fetch_ is it',
        // userId: 1,
        // friends: [2,3,4]
        positions['cf'] = d3.select(".cf").text()
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
    .then(json => {
     svg.append("text")
      .text(JSON.stringify(json))
      .attr("y", 200)
      .attr("x", 120)
      .attr("font-size", 16)
      .attr("font-family", "monospace")
    });