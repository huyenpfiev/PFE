import { Component, OnInit } from '@angular/core';
import {AuthenticationService} from '../services/authentication.service'
import { Router } from '@angular/router'
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  articles:any=[];
  coauteurs:any=[];
  nom:string;
  info:any=[];
  constructor(private auth: AuthenticationService,private router: Router) { }

  ngOnInit() {
    this.auth.getPubs().subscribe(
      res=>{
        this.info=res['infos'][0].split(/\r\n|\r|\n/);
        this.nom=this.info[0];
        this.articles=res['infos'][1];
        this.coauteurs=res['infos'][2];
      }
    )
  }

}
