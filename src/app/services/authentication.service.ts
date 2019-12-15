import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { map } from 'rxjs/operators';
import { Router } from '@angular/router';

export interface UserDetails {
  _id:string;
  FirstName: string;
  LastName: string;
  Username:string;
  Password:string;  
  source:number;
}

interface TokenResponse {
  token: string;
} 

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  private token: string
  private user: Object
  uri = 'http://localhost:5000';
  constructor(private http: HttpClient, private router: Router) { 
    this.token='';
  }

  private saveToken(token: string): void {
    localStorage.setItem('usertoken', token);
    this.token = token;
  }

  private getToken(): string {
    if (!this.token) {
      this.token = localStorage.getItem('usertoken');
    }
    return this.token;
  }

  //public getUserDetails(): UserDetails {
    // const token = this.getToken();
    // let payload;
    // if (token) {
    //   payload = token.split('.')[1];
    //   payload = window.atob(payload);
    //   return JSON.parse(payload);
    // } else {
    //   return null;
    // }
    //return JSON.parse(this.user);
  //}

  public isLoggedIn(): boolean {
    //const user = this.getUserDetails();
    if (this.token != '') {
      return true;
    } else {
      return false;
    }
  }
  public register(FirstName,LastName) {
    const obj = {
      FirstName,
      LastName
    };
    return this.http.post(`${this.uri}/register`, obj);    
  }
  public saveAcc(FirstName,LastName,Username,Password,source){
    const obj={
      FirstName,LastName,Username,Password,source
    }
    return this.http.post(`${this.uri}/saveAcc`,obj);
  }

  public login(Username,Password){

    const obj={
          Username,Password
      };
    const base = this.http.post(`${this.uri}/login`,obj);

    const request = base.pipe(
      map((data: TokenResponse) => {
        if (data.token) {
          this.saveToken(data.token[0]['Username']);
          this.user=data.token[0];
        }
        return data;
      })
    )

    return request;
  }
  public getPubs(){
    const obj={
      source:this.user['source'],
      FirstName:this.user['FirstName'],
      LastName:this.user['LastName']
    }
    return this.http.post(`${this.uri}/getPubs`,obj);
  }
  public logout(): void {
    this.token = '';
    this.user={};
    window.localStorage.removeItem('usertoken');
    this.router.navigate(['login']);
  }
}
