export const environment = {
    production: false,
    apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
    auth0: {
      url: 'fsnd-ms', // the auth0 domain prefix
      audience: 'cast', // the audience set for the auth0 app
      clientId: '2Z5nsMhKBp9uc7WJW78WXlZFz3OsJmCF', // the client id generated for the auth0 app
      callbackURL: 'http://localhost:8100', // the base url of the running ionic application. 
    }
  };