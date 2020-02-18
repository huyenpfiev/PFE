# PFE

This application allows to show your articles and co-authors once successful login. 

The backend is developed with [Python](http://python.org/) version 2.7.12, the frontend with [Angular CLI](https://github.com/angular/angular-cli) version 8.3.19.

### Prerequisites

Both the CLI and generated project have dependencies that require Node 8.9 or higher, together with NPM 5.5.1 or higher.

- [nodeJS](http://nodejs.org/) 13.1.0
- [MongoDB](https://www.mongodb.com/) 2.6

### Installing

Install Angular-CLI:

```shell
npm install -g @angular/cli
```

To build this project, simply clone this repository:

```shell
git clone https://github.com/huyenpfiev/PFE
```
Install Driver:

Extract and copy `geckodriver` file to /usr/local/bin folder in your PC.

### Running

You can run the servers independently, but you need them all to use the app completely:

Run a frontend dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.
```shell
cd PFE-master
```
```shell
ng serve -o
```

Run a backend server:
```shell
cd PFE-master/API
```
```shell
python server.py
```
Do not forget to launch the MongoDB server :
```shell
mongod
```

## Author

- **Thi Thanh Huyen DINH** 
- **Soukaina El Majdoubi** 




