// The file contents for the current environment will overwrite these during build.
// The build system defaults to the dev environment which uses `environment.ts`, but if you do
// `ng build --env=prod` then `environment.prod.ts` will be used instead.
// The list of which env maps to which file can be found in `.angular-cli.json`.

export const environment = {
  production: false,
  firebaseConfig: {
    apiKey: 'AIzaSyB5Bl41J02gvS5CD3LqMZ0cFkSmhHpdvMk',
    authDomain: 'dont-waste-food.firebaseapp.com',
    databaseURL: 'https://dont-waste-food.firebaseio.com',
    projectId: 'dont-waste-food',
    storageBucket: 'dont-waste-food.appspot.com',
    messagingSenderId: '1092162180235'
  }
};
