import { Component, OnInit } from '@angular/core';
import { FormGroup,  FormBuilder,  Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

import {AuthenticationService} from '../services/authentication.service';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  angForm: FormGroup;
  angForm2:FormGroup;
  found:boolean;
  err:boolean;
  structure:any=[];
 
  constructor(private fb: FormBuilder,private auth: AuthenticationService,private route: ActivatedRoute, private router: Router) { 
    this.createForm();
    this.createForm2();
    this.err=false;
    this.found=false;
  }
  createForm(){
    this.angForm = this.fb.group({
      FirstName: ['', Validators.required ],
      LastName: ['', Validators.required ]
      
    });
  }
  onSubmit(){
    
    var FirstName=this.angForm.get('FirstName').value;
    var LastName=this.angForm.get('LastName').value;
   
    this.auth.register(FirstName,LastName).subscribe(
      res => {
        if(res['result']=="not found")
        {
            this.err=true;
            this.found=false;
        }
        else{
          this.found=true;
          this.err=false;
          this.structure=res['result'];  
          this.createForm2(); 
        }
        
      }
      
    );
  }
  createForm2(){
    this.angForm2 = this.fb.group({
      source:['',Validators.required],
      Username: ['', Validators.required ],
      Password: ['', Validators.required ]
      
    });
  }
  onSubmit2(){
    var source=this.angForm2.get('source').value;
    var Username=this.angForm2.get('Username').value;
    var Password=this.angForm2.get('Password').value;
    var FirstName=this.angForm.get('FirstName').value;
    var LastName=this.angForm.get('LastName').value;

    this.auth.saveAcc(FirstName,LastName,Username,Password,source).subscribe(
      res => {
        if(res['result']=='OK')
          this.router.navigate(['login']);
      }
      
    );
  }

  ngOnInit() {
  }

}
