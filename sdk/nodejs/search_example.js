var StockX = require('stock_x_api');

var exampleConstants = new ExampleConstants();

var defaultClient = StockX.ApiClient.instance;
	defaultClient.basePath = 'https://gateway.stockx.com/stage';

var apiKey = defaultClient.authentications['api_key'];
	apiKey.apiKey = exampleConstants.AWS_API_KEY;

var stockx = new StockX.StockXApi();

var login = new StockX.LoginRequest();
	login.email = exampleConstants.STOCKX_USERNAME;
	login.password = exampleConstants.STOCKX_PASSWORD;

stockx.loginWithHttpInfo(login)
	.then(res => {
		defaultClient.defaultHeaders['jwt-authorization'] = res.response.headers['jwt-authorization'];
		return res.data.Customer;
	}).then(customer => {
		return stockx.search('yeezy');
	}).then(result => {
		console.log('Search successful: ' + JSON.stringify(result));
	}).catch(err => {
		console.log('Error performing search: ' + err);
	});