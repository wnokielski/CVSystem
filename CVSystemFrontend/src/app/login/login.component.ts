import {Component} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Router} from "@angular/router";
import {API_URL} from "../../common/consts";
import {JwtPayload} from "../../common/models/jwtPayload";
import {StateService} from "../state.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  constructor(private http: HttpClient,
              private router: Router,
              private stateService: StateService) {
  }

  token: string = "";
  email: string = "";
  password: string = "";

  login() {
    let encodedString = 'Basic ' + btoa(this.email + ':' + this.password)

    const httpOptions = {
      headers: new HttpHeaders({
        'Authorization': encodedString
      })
    };

    this.http.get(`${API_URL}/auth/token`, httpOptions).subscribe(
      response => {
        console.log('Response:', response)
        this.token = (response as JwtPayload).token;
        this.stateService.userID = (response as JwtPayload).user_id
        this.stateService.isUserLoggedIn = true
        this.router.navigate(['/offers'])
      },
      error => {
        console.error('Error:', error);
        alert(error.error.detail)
      }
    );
  }
}
