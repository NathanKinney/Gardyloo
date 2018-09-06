// const yargs = require('yargs');
//
// const geocode = require('./geocode/geocode');
//
// const argv = yargs
//   .options({
//     a: {
//       demand: true,
//       alias: 'address',
//       describe: 'Address to fetch weather for',
//       string: true
//     }
//   })
//   .help()
//   .alias('help', 'h')
//   .argv;
//
// geocode.geocodeAddress(argv.address, (errorMessage, results) => {
//   if (errorMessage) {
//     console.log(errorMessage);
//   } else {
//     console.log(JSON.stringify(results, undefined, 2));
//   }
// });

// api.darksky.net/forecast/a569e0881d0a65b38de1794028db85f5/45.5461375,-122.6766628

const request = require('request');

request({
  url: 'https://api.darksky.net/forecast/a569e0881d0a65b38de1794028db85f5/45.5461375,-122.6766628',
  json: true
}, (error, response, body) => {
  if (!error && response.statusCode == 200) {
      console.log(body.currently.temperature)
  }else {
      console.log('unable to fetch weather.')
  }
});
