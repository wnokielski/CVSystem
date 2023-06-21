import {Component} from '@angular/core';
import {User} from "../../common/models/user";
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {API_URL} from "../../common/consts";
import {Router} from "@angular/router";

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {
  constructor(private http: HttpClient,
              private router: Router) {
  }

  firstName: string = "";
  lastName: string = "";
  email: string = "";
  password: string = "";
  accountType: string = "";
  birthDate: Date = new Date();

  registerUser() {
    const userData = new User(this.firstName, this.lastName, this.email, this.password, this.birthDate, this.accountType)

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    };

    this.http.post(`${API_URL}/users`, JSON.stringify(userData), httpOptions).subscribe(
      response => {
        console.log('Response:', response);
        this.router.navigate(['/login'])
      },
      error => {
        console.error('Error:', error);
        alert(error.error.detail)
      }
    );

  }
}
